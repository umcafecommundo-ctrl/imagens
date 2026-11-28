"""Kit do formato FÁBULA (Curiosidades da IA, desde 27/11/2026, decisão do Luis em 26/11/2026).
Fábulas emocionantes em desenho 2D, traço grosso e cores chapadas e vivas. Use no historia.py:
    from kit import *; import kit; from sombrio import *; from fabula import *
    instala_legenda_fab(CHAVES)

PALCO QUADRADO 2208x2208 (chão dos interiores em y=1560): a MESMA cena serve para o vídeo vertical (vista 1242x2208 no zoom 1)
e para o horizontal (MOTOR_H=1: vista 2208x1242 no zoom 1). Cada cena devolve `cam(cx, cy, zv, zh, roll)`: zv = zoom no
vertical, zh = zoom no horizontal (no horizontal, zh=1 mostra o palco inteiro de largura e um adulto de 1000 px de corpo inteiro).

Personagem fixo LIPE (menino de 8-9 anos): pele clara-pêssego, cabelo castanho curto, camiseta AMARELA, calça AZUL, íris azul.
De pijama: pijama azul-claro (mesmo rosto e cabelo). Pai: barba castanho-escura, camisa azul, calça cinza. Mãe: cabelo comprido
ruivo-escuro, blusa coral. Alturas: Lipe h=700, adultos h=1000.
"""
import math, random, sys
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import kit
from kit import OW, OH, back, ramp, clamp, lerp, smooth, easeOut, blinkAt, kick, paste_c
from art import Pen, hexc, mul, ell_pts, INK
import sombrio
from sombrio import font, F_STAMP, F_CAP, F_B, F_R, F_MAO, put_menino

HOR = kit.OW > kit.OH
SW = SH = 2208          # palco quadrado
FY = 1560               # chão dos interiores

# ------------------------------------------------------------------ personagens fixos
LIPE = dict(pele='#f3c9a2', cabelo='#5b3a1e', penteado='curto', roupa='#f4b63f', calca='#3e6fb8')
LIPE_PIJAMA = dict(LIPE, roupa='#8ec3e8', calca='#6fa8d6')
PAI = dict(pele='#d9a47a', cabelo='#2e2420', penteado='curto', roupa='#4d79b3', calca='#5a5f6b', barba=True)
MAE = dict(pele='#e8bd96', cabelo='#7a3a1f', penteado='longo', roupa='#e06a55', calca='#4a4560')
VO = dict(pele='#e9c3a0', cabelo='#e8e6e0', penteado='coque', roupa='#9b6bb5', calca='#5a4a6a', velho=True, oculos=True)
GENTE = [dict(pele='#c98d62', cabelo='#1e1a18', penteado='coque', roupa='#5aa36f', calca='#3a3a48'),
         dict(pele='#f0d0b0', cabelo='#c8902e', penteado='longo', roupa='#d65a8a', calca='#3b4f7a'),
         dict(pele='#8a5a3c', cabelo='#141010', penteado='careca', roupa='#e08a3a', calca='#2f3540', barba=True),
         dict(pele='#e4b48c', cabelo='#3a2a20', penteado='curto', roupa='#7a5ab0', calca='#4a4036'),
         dict(pele='#b57a52', cabelo='#241a14', penteado='longo', roupa='#3aa0b0', calca='#5a3a30')]
KID, ADU = 700, 1000

# ------------------------------------------------------------------ luzes (cores chapadas e vivas)
kit.GRADES['noite_fab'] = dict(gain=(.8, .84, 1.02), lift=(8, 10, 22), sat=.88, vig=.42)   # noite azulada, ainda colorida
kit._VIG['noite_fab'] = (1 - kit.GRADES['noite_fab']['vig'] * kit._Q * 2.2)[..., None].astype(np.float32)


def cam(cx, cy, zv, zh=None, roll=0.0):
    """câmera para as 2 versões: zv no vertical, zh no horizontal (padrão: zh = max(1, zv*.85))."""
    if HOR: return (cx, cy, zh if zh is not None else max(1.0, zv * .85), roll)
    return (cx, cy, zv, roll)


def V(v, h):
    """valor do vertical ou do horizontal."""
    return h if HOR else v


def zf(z, f, k=.0008):
    return z * (1 + k * f)


@lru_cache(maxsize=32)
def _sombra_img(w):
    """sombra macia no chão (elipse borrada) com largura w."""
    hh = max(6, w // 6); im = Image.new('RGBA', (w + 40, hh + 40), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse((20, 20, w + 20, hh + 20), fill=(30, 20, 30, 85))
    return im.filter(ImageFilter.GaussianBlur(8))


# 28/11/2026 (pedido do Luis: "animação meio estranha", deixar mais viva): gestos, boca que fala, sombra no chão e balanço leve.
GESTOS = {
    'acena': lambda f: (None, 2.5 + .35 * math.sin(f * .5)),          # acenando com a mão direita
    'aponta': lambda f: (None, 1.55 + .04 * math.sin(f * .2)),         # apontando para a direita da imagem
    'abraco': lambda f: (1.15, -1.15),                                 # braços para a frente (abraçar/receber)
    'segura': lambda f: (.55, -.55),                                   # segurando algo na frente do corpo
    'comemora': lambda f: (-2.3 - .15 * math.sin(f * .4), 2.3 + .15 * math.sin(f * .4)),
    'maos_peito': lambda f: (.95, -.95),
    'ombros': lambda f: (-.6, .6),                                     # braços meio abertos (explicando / sem jeito)
}


def boca_fala(si, f, de=None, ate=None):
    """abertura da boca (0..1) de quem está FALANDO na cena si, pelo tempo das palavras da voz.
    de/ate = 1ª e última palavra da fala do personagem (se a frase mistura narrador e personagem)."""
    try: ws = kit.T.falas[si]['words']
    except Exception: return 0.0
    i0 = 0; i1 = len(ws) - 1
    if de: i0 = next((i for i, w in enumerate(ws) if kit._norm(w['w']) == kit._norm(de)), 0)
    if ate: i1 = next((i for i in range(len(ws) - 1, -1, -1) if kit._norm(ws[i]['w']) == kit._norm(ate)), i1)
    t = f / kit.FPS - kit.T.LEAD
    for w in ws[i0:i1 + 1]:
        if w['t'] - .03 <= t <= w['t'] + w['d']:
            return round((.35 + .65 * abs(math.sin(t * 13))) * 4) / 4
    return 0.0


def pessoa(c, x, feet, h, f, cores, gesto=None, boca=0.0, sombra=True, vivo=True, **kw):
    """personagem do formato FÁBULA. gesto = nome em GESTOS; boca = 0..1 (use boca_fala); sombra no chão; vivo = balanço leve."""
    if sombra and h > 60:
        sh = _sombra_img(int(h * .46 // 8 * 8)); c.alpha_composite(sh, (int(x - sh.width / 2), int(feet - sh.height / 2 + h * .01)))
    if gesto:
        ae, ad = GESTOS[gesto](f)
        if ae is not None: kw['braco_e'] = round(ae * 10) / 10
        if ad is not None: kw['braco_d'] = round(ad * 10) / 10
    if boca: kw['boca'] = round(boca * 4) / 4
    if vivo and not kw.get('walk') and 'tilt' not in kw:
        kw['tilt'] = round(1.2 * math.sin(f * .045 + kw.get('seed', 2)) * 2) / 2
    put_menino(c, x, feet, h, f, **dict(cores, **kw))


def cintura(x, feet, h, lado=1):
    """onde fica o pote preso na cintura (ao lado do quadril)."""
    return x + lado * .21 * h, feet - .27 * h


# ------------------------------------------------------------------ céu
CEU = {'dia': ('#6fbdf0', '#d6f0fb'), 'tarde': ('#f2875a', '#ffd89a'), 'noite': ('#1d2758', '#4b5c95')}


@lru_cache(maxsize=4)
def ceu_fab(luz='dia'):
    t, b = CEU[luz]
    y = np.linspace(0, 1, SH)[:, None, None]
    a = np.array(hexc(t)) * (1 - y) + np.array(hexc(b)) * y
    im = Image.fromarray(np.broadcast_to(a, (SH, SW, 3)).astype(np.uint8)).convert('RGBA')
    d = ImageDraw.Draw(im)
    if luz == 'noite':
        rnd = random.Random(4)
        for _ in range(120):
            x, yy = rnd.randint(0, SW), rnd.randint(0, 1200); r = rnd.choice((2, 3, 4))
            d.ellipse((x - r, yy - r, x + r, yy + r), fill=(255, 250, 220, 255))
    return im


def _nuvem(p, cx, cy, s=1.0, col=(255, 255, 255)):
    for dx, dy, r in ((-90, 12, 70), (0, -22, 95), (95, 10, 70), (0, 30, 76)):
        p.dot(cx + dx * s, cy + dy * s, r * s + 6, INK)
    for dx, dy, r in ((-90, 12, 70), (0, -22, 95), (95, 10, 70), (0, 30, 76)):
        p.dot(cx + dx * s, cy + dy * s, r * s, col)


def _astro(p, luz, x, y):
    if luz == 'noite':
        p.dot(x, y, 92, INK); p.dot(x, y, 86, hexc('#fff3c4')); p.dot(x + 34, y - 20, 70, hexc(CEU['noite'][0]))
    else:
        cor = hexc('#ffe27a') if luz == 'dia' else hexc('#ffb347')
        for i in range(12):
            a = i * math.pi / 6
            p.line([(x + 120 * math.cos(a), y + 120 * math.sin(a)), (x + 170 * math.cos(a), y + 170 * math.sin(a))], cor, 14, 4)
        p.shape(ell_pts(x, y, 100, 100, 48), cor, mul(cor, .85), 6, 14)


def _janela(c, x0, y0, x1, y1, luz, cortina='#e06a55'):
    """janela com o céu da luz (cola o céu e desenha a moldura)."""
    sky = ceu_fab(luz).crop((x0, 200, x1, 200 + (y1 - y0)))
    c.alpha_composite(sky, (x0, y0))
    p = Pen(SW, SH)
    if luz != 'noite': _nuvem(p, x0 + (x1 - x0) * .35, y0 + (y1 - y0) * .35, .55)
    else: p.dot(x0 + (x1 - x0) * .7, y0 + (y1 - y0) * .3, 40, hexc('#fff3c4'), 5)
    return p


# ------------------------------------------------------------------ cenários (palco 2208x2208)
def _base(parede, listra=None):
    p = Pen(SW, SH)
    p.poly([(0, 0), (SW, 0), (SW, FY), (0, FY)], hexc(parede))
    if listra:
        for x in range(0, SW, 110): p.stroke([(x, 0), (x, FY)], 8, hexc(listra))
    p.shape([(0, FY - 60), (SW, FY - 60), (SW, FY), (0, FY)], mul(hexc(parede), .82), None, 5, 0)   # rodapé
    return p


def _piso(p, col='#c99a62'):
    p.poly([(0, FY), (SW, FY), (SW, SH), (0, SH)], hexc(col))
    for y in range(FY + 90, SH, 120): p.stroke([(0, y), (SW, y)], 5, mul(hexc(col), .82))
    rnd = random.Random(3)
    for y in range(FY, SH, 120):
        for _ in range(4):
            x = rnd.randint(0, SW); p.stroke([(x, y), (x, y + 120)], 4, mul(hexc(col), .82))
    p.stroke([(0, FY), (SW, FY)], 9)


def _moldura(p, x0, y0, x1, y1, luz):
    p.shape([(x0 - 26, y0 - 26), (x1 + 26, y0 - 26), (x1 + 26, y1 + 26), (x0 - 26, y1 + 26)], hexc('#fbf7ee'), hexc('#ddd6c6'), 7, 8)


def _vidro(c, x0, y0, x1, y1, luz):
    sky = ceu_fab(luz).crop((x0, 150, x1, 150 + (y1 - y0)))
    c.alpha_composite(sky, (x0, y0))


def _cruz(p, x0, y0, x1, y1):
    p.stroke([((x0 + x1) / 2, y0), ((x0 + x1) / 2, y1)], 16, hexc('#fbf7ee'))
    p.stroke([(x0, (y0 + y1) / 2), (x1, (y0 + y1) / 2)], 16, hexc('#fbf7ee'))
    p.stroke([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], 7)


def _quadro(p, x, y, w, h, cor):
    p.shape([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], hexc('#8a5a32'), None, 6, 0)
    p.poly([(x + 18, y + 18), (x + w - 18, y + 18), (x + w - 18, y + h - 18), (x + 18, y + h - 18)], hexc(cor))
    p.poly([(x + 18, y + h - 18), (x + w * .4, y + h * .45), (x + w * .6, y + h * .65), (x + w * .75, y + h * .5), (x + w - 18, y + h - 18)], mul(hexc(cor), .7))


def _escuro(c, luz):
    if luz == 'noite':
        c.alpha_composite(Image.new('RGBA', c.size, (20, 30, 80, 40)))
    elif luz == 'tarde':
        c.alpha_composite(Image.new('RGBA', c.size, (255, 140, 60, 26)))
    return c


@lru_cache(maxsize=4)
def sala_fab(luz='dia'):
    """sala: janelão à esquerda (x 260..820, y 420..1060), quadros, sofá encosto ao fundo (x 760..1460, assento y≈1330)."""
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = _base('#f6e1b8', '#efd3a0')
    _moldura(p, 260, 420, 820, 1060, luz)
    _piso(p, '#c99a62')
    p.shape(ell_pts(1104, 1900, 820, 190, 60), hexc('#5aa3a0'), hexc('#3f8380'), 7, 14)   # tapete
    _quadro(p, 1000, 520, 300, 230, '#8fd6a0'); _quadro(p, 1380, 600, 220, 170, '#f2a65a')
    # luminária de pé à direita
    p.stroke([(1880, FY), (1880, 820)], 14); p.shape([(1760, 820), (2000, 820), (1950, 640), (1810, 640)], hexc('#ffd56a'), hexc('#e8b84a'), 7, 10)
    # encosto do sofá
    p.shape([(740, 1060), (1470, 1060), (1490, 1340), (720, 1340)], hexc('#e0583a'), hexc('#b8432a'), 8, 18)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    _vidro(c, 260, 420, 820, 1060, luz)
    q = Pen(SW, SH); _cruz(q, 260, 420, 820, 1060)
    if luz != 'noite': _nuvem(q, 420, 560, .5)
    c.alpha_composite(q.img.resize((SW, SH), Image.LANCZOS))
    return _escuro(c, luz)


@lru_cache(maxsize=4)
def sofa_frente():
    """frente do sofá (assento + braços) para cobrir as pernas de quem senta (assento em y≈1330)."""
    p = Pen(SW, SH)
    p.shape([(700, 1320), (1510, 1320), (1510, 1560), (700, 1560)], hexc('#ec6b48'), hexc('#c44f30'), 8, 18)
    p.stroke([(1104, 1335), (1104, 1500)], 6, hexc('#c44f30'))
    for x0 in (620, 1450):
        p.shape([(x0, 1180), (x0 + 140, 1180), (x0 + 140, 1560), (x0, 1560)], hexc('#d9563a'), hexc('#b0432a'), 8, 14)
    for x in (740, 1470): p.shape([(x - 20, 1560), (x + 20, 1560), (x + 14, 1610), (x - 14, 1610)], hexc('#6a4428'), None, 5, 0)
    return p.img.resize((SW, SH), Image.LANCZOS)


@lru_cache(maxsize=4)
def jantar_fab(luz='noite'):
    """sala de jantar: janela à direita, lustre, armário; encostos das cadeiras atrás de quem senta."""
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = _base('#dcebc8', '#cfe0b8')
    _moldura(p, 1480, 420, 1980, 980, luz)
    _piso(p, '#b98a58')
    p.shape([(140, 700), (560, 700), (560, 1560), (140, 1560)], hexc('#8a5a32'), hexc('#6a4428'), 8, 14)   # armário
    for y in (820, 1060): p.shape([(180, y), (520, y), (520, y + 180), (180, y + 180)], hexc('#cfe8ef'), None, 6, 0)
    p.stroke([(1104, 0), (1104, 360)], 8)
    p.shape([(960, 360), (1248, 360), (1180, 460), (1028, 460)], hexc('#ffd56a'), hexc('#e8b84a'), 7, 10)   # lustre
    for x in (760, 1104, 1450):   # encostos
        p.shape([(x - 120, 900), (x + 120, 900), (x + 120, 1300), (x - 120, 1300)], hexc('#9a6a40'), hexc('#7a5230'), 7, 10)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    _vidro(c, 1480, 420, 1980, 980, luz)
    q = Pen(SW, SH); _cruz(q, 1480, 420, 1980, 980)
    c.alpha_composite(q.img.resize((SW, SH), Image.LANCZOS))
    if luz == 'noite':
        g = Image.new('RGBA', (SW, SH), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((500, 300, 1700, 1400), fill=(255, 220, 140, 60))
        c.alpha_composite(g.filter(ImageFilter.GaussianBlur(90)))
    return _escuro(c, luz)


@lru_cache(maxsize=2)
def mesa_frente():
    """tampo + toalha da mesa de jantar (tampo em y≈1250, x 420..1790)."""
    p = Pen(SW, SH)
    p.shape([(420, 1240), (1790, 1240), (1790, 1290), (420, 1290)], hexc('#8a5a32'), None, 7, 0)
    p.shape([(440, 1280), (1770, 1280), (1730, 1500), (480, 1500)], hexc('#f4f1ea'), hexc('#d8d2c4'), 7, 12)
    for x in range(520, 1720, 120): p.stroke([(x, 1300), (x + 10, 1480)], 5, hexc('#e06a55'))
    for x in (520, 1690): p.shape([(x - 22, 1490), (x + 22, 1490), (x + 18, FY + 40), (x - 18, FY + 40)], hexc('#6a4428'), None, 5, 0)
    return p.img.resize((SW, SH), Image.LANCZOS)


@lru_cache(maxsize=4)
def quarto_fab(luz='noite'):
    """quarto do Lipe: parede azul com estrelas, janela à esquerda (x 240..760, y 380..900), prateleira (y=980, x 1000..1700),
    cama à direita (x 1650..2150, colchão y≈1300)."""
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = _base('#bcd6f2')
    rnd = random.Random(8)
    for _ in range(18):   # estrelinhas pintadas na parede
        x, y = rnd.randint(900, 2150), rnd.randint(120, 820)
        pts = [(x + (34 if k % 2 == 0 else 14) * math.cos(k * math.pi / 5 - math.pi / 2), y + (34 if k % 2 == 0 else 14) * math.sin(k * math.pi / 5 - math.pi / 2)) for k in range(10)]
        p.poly(pts, hexc('#fff0a8'))
    _moldura(p, 240, 380, 760, 900, luz)
    _piso(p, '#c99a62')
    p.shape(ell_pts(900, 1880, 520, 150, 60), hexc('#f2a65a'), hexc('#d98a3a'), 7, 12)   # tapete
    p.shape([(980, 980), (1720, 980), (1720, 1020), (980, 1020)], hexc('#9a6a40'), hexc('#7a5230'), 6, 6)   # prateleira
    for x in (1020, 1680): p.shape([(x - 12, 1020), (x + 12, 1020), (x + 12, 1080), (x - 12, 1080)], hexc('#7a5230'), None, 5, 0)
    # cama
    p.shape([(2080, 900), (2170, 900), (2170, 1600), (2080, 1600)], hexc('#8a5a32'), None, 7, 0)
    p.shape([(1620, 1290), (2100, 1290), (2100, 1560), (1620, 1560)], hexc('#5aa36f'), hexc('#3f8a52'), 8, 16)
    p.shape([(1880, 1200), (2060, 1200), (2060, 1300), (1880, 1300)], hexc('#fbf7ee'), None, 6, 0)
    # abajur
    p.shape([(1460, 1300), (1600, 1300), (1600, 1560), (1460, 1560)], hexc('#9a6a40'), None, 6, 0)
    p.stroke([(1530, 1300), (1530, 1180)], 10); p.shape([(1450, 1180), (1610, 1180), (1570, 1070), (1490, 1070)], hexc('#ffd56a'), None, 6, 0)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    _vidro(c, 240, 380, 760, 900, luz)
    q = Pen(SW, SH); _cruz(q, 240, 380, 760, 900)
    if luz == 'noite': q.dot(620, 500, 50, hexc('#fff3c4'), 6)
    c.alpha_composite(q.img.resize((SW, SH), Image.LANCZOS))
    if luz == 'noite':
        g = Image.new('RGBA', (SW, SH), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((1100, 800, 1960, 1600), fill=(255, 220, 140, 80))
        c.alpha_composite(g.filter(ImageFilter.GaussianBlur(90)))
    return _escuro(c, luz)


@lru_cache(maxsize=4)
def escritorio_fab(luz='noite'):
    """escritório do pai: estante à esquerda, janela no meio (x 760..1260, y 380..860), relógio de parede (1560, 520).
    A mesa é `mesa_trab()` (tampo em y≈1250, x 900..1800)."""
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = _base('#efe3cc', '#e6d6b8')
    _moldura(p, 760, 380, 1260, 860, luz)
    _piso(p, '#a8835c')
    p.shape([(80, 420), (620, 420), (620, FY), (80, FY)], hexc('#8a5a32'), hexc('#6a4428'), 8, 14)   # estante
    rnd = random.Random(12)
    cores = ['#e06a55', '#4d79b3', '#f4b63f', '#5aa36f', '#9b6bb5']
    for k in range(4):
        y = 500 + k * 250; x = 110
        while x < 580:
            bw = rnd.randint(34, 56); bh = rnd.randint(140, 190)
            p.poly([(x, y + 200 - bh), (x + bw, y + 200 - bh), (x + bw, y + 200), (x, y + 200)], hexc(rnd.choice(cores)), 3); x += bw + 4
        p.shape([(96, y + 200), (604, y + 200), (604, y + 222), (96, y + 222)], hexc('#6a4428'), None, 4, 0)
    p.shape([(1900, 1100), (2060, 1100), (2030, FY), (1930, FY)], hexc('#e06a55'), hexc('#b8432a'), 6, 8)   # vaso
    for a in (-1.0, -.4, .2, .8):
        p.shape(ell_pts(1980 + 110 * math.sin(a), 1000 - 80 * math.cos(a), 40, 100, 24, a), hexc('#5cae5e'), hexc('#3e8a42'), 5, 6)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    _vidro(c, 760, 380, 1260, 860, luz)
    q = Pen(SW, SH); _cruz(q, 760, 380, 1260, 860)
    if luz == 'noite': q.dot(1150, 470, 44, hexc('#fff3c4'), 6)
    c.alpha_composite(q.img.resize((SW, SH), Image.LANCZOS))
    if luz == 'noite':
        g = Image.new('RGBA', (SW, SH), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((900, 700, 1900, 1500), fill=(255, 225, 150, 85))
        c.alpha_composite(g.filter(ImageFilter.GaussianBlur(90)))
    return _escuro(c, luz)


def relogio(c, hora, minuto, x=1560, y=540, r=110):
    sombrio.mostrador(c, x, y, r, hora, minuto, aro=(244, 182, 63))


@lru_cache(maxsize=2)
def mesa_trab():
    p = Pen(SW, SH)
    p.shape([(880, 1240), (1980, 1240), (1980, 1295), (880, 1295)], hexc('#9a6a40'), None, 7, 0)
    p.shape([(900, 1290), (1960, 1290), (1960, FY + 30), (900, FY + 30)], hexc('#b07a48'), hexc('#8a5a32'), 7, 16)
    p.shape([(1600, 1340), (1910, 1340), (1910, 1440), (1600, 1440)], hexc('#9a6a40'), None, 5, 0)
    p.dot(1755, 1390, 12, hexc('#f4d48a'), 4)
    return p.img.resize((SW, SH), Image.LANCZOS)


def notebook(c, x, y, aberto=1.0, tela=True):
    """notebook em cima da mesa (base em y); aberto 0..1 (fecha a tela)."""
    d = ImageDraw.Draw(c)
    d.polygon([(x - 230, y), (x + 230, y), (x + 260, y + 26), (x - 260, y + 26)], fill=(120, 128, 140, 255), outline=INK + (255,))
    d.line([(x - 230, y), (x + 230, y), (x + 260, y + 26), (x - 260, y + 26), (x - 230, y)], fill=INK + (255,), width=7)
    hh = 300 * aberto
    if hh > 6:
        d.rectangle((x - 220, y - hh, x + 220, y), fill=(70, 76, 90, 255), outline=INK + (255,), width=7)
        if tela and aberto > .5:
            d.rectangle((x - 196, y - hh + 22, x + 196, y - 18), fill=(150, 205, 255, 255))
            for k in range(4): d.line((x - 170, y - hh + 60 + k * 50, x + 120 - 40 * (k % 2), y - hh + 60 + k * 50), fill=(90, 140, 210, 255), width=10)
    else:
        d.rectangle((x - 230, y - 14, x + 230, y + 4), fill=(70, 76, 90, 255), outline=INK + (255,), width=6)


@lru_cache(maxsize=4)
def quintal_fab(luz='tarde'):
    """quintal: céu, sol baixo, cerca de madeira (y 1000..1400), árvore à direita, gramado do y 1400 pra baixo, casa à esquerda."""
    c = ceu_fab(luz).copy()
    p = Pen(SW, SH)
    _astro(p, luz, 1500, 640 if luz == 'tarde' else 360)
    if luz == 'dia':
        _nuvem(p, 500, 380, .9); _nuvem(p, 1700, 260, .7)
    # casa à esquerda
    p.shape([(-40, 640), (520, 640), (520, 1420), (-40, 1420)], hexc('#f2c6a0'), hexc('#d9a882'), 8, 16)
    p.shape([(-80, 660), (240, 380), (580, 660)], hexc('#c0453a'), hexc('#9a3328'), 8, 12)
    p.shape([(160, 900), (380, 900), (380, 1420), (160, 1420)], hexc('#8a5a32'), None, 7, 0)
    p.dot(340, 1170, 14, hexc('#f4d48a'), 4)
    # cerca
    for x in range(560, SW + 60, 120):
        p.shape([(x, 1060), (x + 40, 1020), (x + 80, 1060), (x + 80, 1420), (x, 1420)], hexc('#f0d9a8'), hexc('#d6bb84'), 6, 6)
    p.shape([(540, 1130), (SW + 40, 1130), (SW + 40, 1170), (540, 1170)], hexc('#e6c890'), None, 5, 0)
    p.shape([(540, 1300), (SW + 40, 1300), (SW + 40, 1340), (540, 1340)], hexc('#e6c890'), None, 5, 0)
    # árvore
    p.shape([(1900, 1460), (1900, 880), (1980, 880), (1990, 1460)], hexc('#8a5a32'), hexc('#6a4428'), 8, 10)
    for dx, dy, r in ((-140, -60, 200), (120, -90, 210), (0, -260, 230), (-40, 60, 170), (200, 60, 150)):
        p.dot(1945 + dx, 860 + dy, r + 8, INK)
    for dx, dy, r in ((-140, -60, 200), (120, -90, 210), (0, -260, 230), (-40, 60, 170), (200, 60, 150)):
        p.dot(1945 + dx, 860 + dy, r, hexc('#5aa36f'))
    # gramado
    g = hexc('#7cc46a') if luz == 'dia' else hexc('#8bbf5a')
    p.shape([(-20, 1400)] + [(x, 1400 + 14 * math.sin(x / 140)) for x in range(0, SW + 1, 60)] + [(SW + 20, 1400), (SW + 20, SH), (-20, SH)], g, mul(g, .85), 7, 16)
    rnd = random.Random(6)
    for _ in range(26):
        x, y = rnd.randint(40, SW - 40), rnd.randint(1750, 2150)
        col = hexc(rnd.choice(['#ffe27a', '#f2a6c8', '#ffffff']))
        for k in range(5): p.dot(x + 14 * math.cos(k * 1.256), y + 14 * math.sin(k * 1.256), 10, col, 3)
        p.dot(x, y, 7, hexc('#f4b63f'))
    for _ in range(40):
        x, y = rnd.randint(0, SW), rnd.randint(1450, 2200)
        p.stroke([(x, y), (x - 8, y - 30)], 5, mul(g, .75)); p.stroke([(x + 12, y), (x + 16, y - 26)], 5, mul(g, .75))
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    return _escuro(c, luz)


# ------------------------------------------------------------------ rua colorida com rolagem
CASAS_COR = ['#f2c6a0', '#a8d0e6', '#f4e1a1', '#c9e2b3', '#e8b4b8', '#d7c4f0']
TETO_COR = ['#c0453a', '#4d79b3', '#e08a3a', '#5aa36f', '#9b6bb5']


@lru_cache(maxsize=4)
def casas_fab(luz='dia'):
    """faixa de casas 4416x760 (repete sem emenda); base das casas em y=760 da faixa."""
    Wt = 4416; p = Pen(Wt, 760); rnd = random.Random(5)
    n = 12; step = Wt / n
    for i in range(n):
        x = i * step + 20; w = step - 40 - rnd.randint(0, 40); hh = rnd.randint(300, 420)
        col = hexc(CASAS_COR[i % len(CASAS_COR)]); teto = hexc(TETO_COR[(i * 3) % len(TETO_COR)])
        p.shape([(x, 760), (x, 760 - hh), (x + w, 760 - hh), (x + w, 760)], col, mul(col, .86), 7, 14)
        p.shape([(x - 26, 760 - hh + 10), (x + w / 2, 760 - hh - 150), (x + w + 26, 760 - hh + 10)], teto, mul(teto, .8), 7, 10)
        lit = luz == 'noite'
        for k in range(2):
            wx = x + 40 + k * (w - 150)
            p.shape([(wx, 760 - hh + 70), (wx + 90, 760 - hh + 70), (wx + 90, 760 - hh + 170), (wx, 760 - hh + 170)],
                    hexc('#ffe9a0') if lit else hexc('#bfe3f5'), None, 5, 0)
        p.shape([(x + w / 2 - 50, 760 - 180), (x + w / 2 + 50, 760 - 180), (x + w / 2 + 50, 760), (x + w / 2 - 50, 760)], hexc('#8a5a32'), None, 6, 0)
        # arvorezinha entre as casas
        tx = (i + 1) * step - 10
        p.stroke([(tx, 760), (tx, 560)], 16, hexc('#6a4428'))
        p.dot(tx, 520, 78, INK); p.dot(tx, 520, 72, hexc('#5aa36f'))
    return p.img.resize((Wt, 760), Image.LANCZOS)


@lru_cache(maxsize=4)
def rua_base(luz='dia'):
    c = ceu_fab(luz).copy()
    p = Pen(SW, SH)
    _astro(p, luz, 1750, 380)
    if luz == 'dia': _nuvem(p, 420, 330, .9); _nuvem(p, 1150, 220, .7)
    p.poly([(0, 1460), (SW, 1460), (SW, 1820), (0, 1820)], hexc('#e8e2d4'))     # calçada
    for x in range(0, SW, 200): p.stroke([(x, 1460), (x - 60, 1820)], 5, hexc('#cfc7b4'))
    p.poly([(0, 1820), (SW, 1820), (SW, 1860), (0, 1860)], hexc('#b8b0a0'))
    p.poly([(0, 1860), (SW, 1860), (SW, SH), (0, SH)], hexc('#6f7680'))       # rua
    p.stroke([(0, 1460), (SW, 1460)], 7); p.stroke([(0, 1820), (SW, 1820)], 7)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    return c


def rua_fab(f, scroll=0.0, luz='dia'):
    c = rua_base(luz).copy()
    cs = casas_fab(luz); off = int(scroll * .5) % cs.width
    a = cs.crop((off, 0, min(cs.width, off + SW), 760)); c.alpha_composite(a, (0, 700))
    if a.width < SW: c.alpha_composite(cs.crop((0, 0, SW - a.width, 760)), (a.width, 700))
    d = ImageDraw.Draw(c); o = int(scroll) % 400
    for x in range(-o, SW + 400, 400): d.rectangle((x, 2010, x + 200, 2034), fill=(240, 240, 230, 255))
    if luz == 'tarde': c.alpha_composite(Image.new('RGBA', c.size, (255, 140, 60, 26)))
    return c


# ------------------------------------------------------------------ o POTE de tempo
AREIA, AREIA_D = (244, 192, 70), (214, 150, 40)


@lru_cache(maxsize=512)
def pote_img(nivel, nome='', rachado=0.0, brilho=False, w=260):
    """pote de vidro com areia dourada (nivel 0..1), etiqueta com o nome, rachaduras (0..1)."""
    S = 2; W0, H0 = 600, 880
    im = Image.new('RGBA', (W0 * S, H0 * S), (0, 0, 0, 0))
    def P(pts): return [(x * S, y * S) for x, y in pts]
    if brilho:
        g = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse(P([(110, 170), (490, 800)]), fill=(255, 220, 110, 150))
        im.alpha_composite(g.filter(ImageFilter.GaussianBlur(26 * S)))
    d = ImageDraw.Draw(im)
    body = (100, 190, 500, 850)
    # vidro (traseira)
    d.rounded_rectangle(P([body[:2], body[2:]]), 120 * S, fill=(214, 238, 248, 150))
    # areia (recortada no formato do corpo)
    if nivel > .005:
        m = Image.new('L', im.size, 0); md = ImageDraw.Draw(m)
        md.rounded_rectangle(P([(112, 202), (488, 838)]), 110 * S, fill=255)
        top = 838 - nivel * (838 - 230)
        sand = Image.new('RGBA', im.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sand)
        sd.rectangle(P([(100, top), (500, 850)]), fill=AREIA + (255,))
        sd.ellipse(P([(112, top - 22), (488, top + 22)]), fill=(255, 214, 110, 255))
        rnd = random.Random(int(nivel * 100))
        for _ in range(int(60 * nivel) + 4):
            x, y = rnd.randint(130, 470), rnd.randint(min(int(top) + 20, 826), 830)
            sd.ellipse(P([(x - 5, y - 5), (x + 5, y + 5)]), fill=AREIA_D + (255,))
        from PIL import ImageChops
        sand.putalpha(ImageChops.multiply(sand.split()[3], m)); im.alpha_composite(sand)
    # gargalo e boca
    d.rectangle(P([(190, 90), (410, 200)]), fill=(214, 238, 248, 170))
    d.rounded_rectangle(P([(160, 60), (440, 110)]), 20 * S, fill=(236, 248, 252, 210), outline=INK + (255,), width=10 * S)
    d.line(P([(190, 110), (190, 200)]), fill=INK + (255,), width=10 * S); d.line(P([(410, 110), (410, 200)]), fill=INK + (255,), width=10 * S)
    d.rounded_rectangle(P([body[:2], body[2:]]), 120 * S, outline=INK + (255,), width=12 * S)
    d.rectangle(P([(196, 186), (404, 206)]), fill=(214, 238, 248, 255))
    # brilho do vidro
    d.line(P([(150, 300), (150, 700)]), fill=(255, 255, 255, 190), width=22 * S)
    d.line(P([(185, 260), (210, 250)]), fill=(255, 255, 255, 190), width=14 * S)
    # etiqueta
    if nome:
        d.rounded_rectangle(P([(150, 430), (450, 560)]), 18 * S, fill=(252, 246, 228, 255), outline=INK + (255,), width=8 * S)
        fs = 76
        while fs > 30 and d.textlength(nome, font=font(F_CAP, fs * S)) > 270 * S: fs -= 2
        fnt = font(F_CAP, fs * S); tw = d.textlength(nome, font=fnt)
        d.text((300 * S - tw / 2, 495 * S - fs * S * .62), nome, font=fnt, fill=(70, 50, 40, 255))
    if rachado > 0:
        pts = [(380, 220), (350, 300), (395, 360), (330, 450), (370, 520), (310, 640), (340, 720)]
        n = max(2, int(len(pts) * clamp(rachado)))
        seg = pts[:n]
        d.line(P(seg), fill=INK + (255,), width=9 * S, joint='curve')
        d.line(P([(x + 6, y) for x, y in seg]), fill=(255, 255, 255, 220), width=4 * S)
        if rachado > .6:
            d.line(P([(395, 360), (450, 400), (470, 470)]), fill=INK + (255,), width=7 * S)
            d.line(P([(330, 450), (250, 480), (220, 560)]), fill=INK + (255,), width=7 * S)
    hh = int(w * H0 / W0)
    return im.resize((w, hh), Image.LANCZOS)


def put_pote(c, x, base, w, nivel, nome='', rachado=0.0, brilho=False, rot=0.0):
    """cola o pote com o fundo em y=base (centro x)."""
    if w < 12: return
    im = pote_img(round(clamp(nivel) * 50) / 50, nome, round(clamp(rachado) * 10) / 10, brilho, int(w // 4 * 4))
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height * .97)))


def boca_pote(x, base, w):
    """posição (x, y) da boca do pote desenhado com put_pote."""
    return x, base - w * (880 / 600) * .97 + w * 85 / 600


def graos(c, x, y, f, w=260, forca=1.0, seed=0):
    """areia dourada mágica caindo na boca do pote (x, y = boca); forca 0..1."""
    if forca <= .02: return
    d = ImageDraw.Draw(c); rnd = random.Random(seed)
    n = int(18 * forca) + 2
    for k in range(n):
        ph = (f * .045 + k / n + rnd.random() * .3) % 1
        gx = x + (rnd.random() - .5) * w * .5 * (1 - ph) + 6 * math.sin(f * .2 + k)
        gy = y - w * 1.1 * (1 - ph)
        r = w * .02 * (1.2 - .5 * ph)
        d.ellipse((gx - r - 2, gy - r - 2, gx + r + 2, gy + r + 2), fill=(150, 100, 20, int(200 * forca)))
        d.ellipse((gx - r, gy - r, gx + r, gy + r), fill=(255, 214, 110, int(255 * forca)))
    for k in range(3):   # brilhinhos
        ph = (f * .03 + k / 3) % 1
        sx = x + (k - 1) * w * .35; sy = y - w * .9 + w * .3 * math.sin(k * 2.1 + f * .05)
        brilho(c, sx, sy, w * .07 * math.sin(ph * math.pi) * forca)


def brilho(c, x, y, r, cor=(255, 246, 190)):
    if r < 2: return
    d = ImageDraw.Draw(c)
    pts = [(x + (r if k % 2 == 0 else r * .28) * math.cos(k * math.pi / 4), y + (r if k % 2 == 0 else r * .28) * math.sin(k * math.pi / 4)) for k in range(8)]
    d.polygon(pts, fill=cor + (255,))


def pote_cintura(c, x, feet, h, f, nivel, nome='', lado=1, cai=0.0, brilho_=False, rachado=0.0, seed=0):
    """pote preso na cintura de quem está em (x, feet, h); cai 0..1 = areia caindo."""
    px, py = cintura(x, feet, h, lado)
    w = h * .2
    d = ImageDraw.Draw(c)
    d.line((x + lado * .12 * h, py - h * .14, px, py - h * .1), fill=(120, 80, 50, 255), width=max(4, int(h * .012)))   # cordinha
    put_pote(c, px, py + w * .8, w, nivel, nome, rachado, brilho_)
    if cai > 0: graos(c, *boca_pote(px, py + w * .8, w), f, w, cai, seed)


# ------------------------------------------------------------------ cachorro, bola, celular
@lru_cache(maxsize=16)
def cachorro_img(fase=0, abana=0):
    p = Pen(700, 560)
    COR, CD = hexc('#d9a05b'), hexc('#b98040')
    lg = [(-1, 0), (1, 0)]
    for i, (x0) in enumerate((220, 300, 440, 520)):
        a = .35 * math.sin(fase * math.pi / 2 + i * math.pi) if fase >= 0 else 0
        p.line([(x0, 360), (x0 + 60 * math.sin(a), 520)], CD if i % 2 else COR, 42, 6)
    tail = .5 * math.sin(abana * math.pi / 2)
    p.line([(170, 300), (90, 220 - 60 * tail), (70, 150 - 80 * tail)], COR, 30, 6)
    p.shape(ell_pts(370, 320, 220, 110, 40), COR, CD, 7, 18)
    p.shape(ell_pts(560, 220, 110, 100, 36), COR, CD, 7, 14)
    p.shape(ell_pts(650, 255, 55, 42, 24), hexc('#f0c890'), None, 6, 0)
    p.dot(690, 240, 18, INK)
    p.shape([(500, 140), (470, 290), (540, 250)], hexc('#8a5a32'), None, 6, 0)   # orelha
    p.dot(590, 200, 24, hexc('#fbfbf7'), 5); p.dot(598, 202, 13, INK); p.dot(602, 196, 4, hexc('#ffffff'))
    p.arc(640, 290, 30, 14, 20, 150, 6)
    p.shape([(470, 300), (520, 330), (500, 350), (460, 320)], hexc('#e06a55'), None, 4, 0)   # coleira
    return p.img.resize((700, 560), Image.LANCZOS)


def put_cachorro(c, x, feet, h, f, andando=False, flip=False):
    im = cachorro_img(int(f / 4) % 4 if andando else 0, int(f / 3) % 4)
    im = im.resize((int(h * 1.25), int(h)), Image.LANCZOS)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - im.height)))


def bola(c, x, y, r, giro=0.0):
    d = ImageDraw.Draw(c)
    d.ellipse((x - r - 7, y - r - 7, x + r + 7, y + r + 7), fill=INK + (255,))
    d.ellipse((x - r, y - r, x + r, y + r), fill=(250, 250, 246, 255))
    for k in range(5):
        a = giro + k * 2 * math.pi / 5
        px, py = x + r * .55 * math.cos(a), y + r * .55 * math.sin(a)
        d.ellipse((px - r * .2, py - r * .2, px + r * .2, py + r * .2), fill=(40, 40, 46, 255))
    d.ellipse((x - r * .22, y - r * .22, x + r * .22, y + r * .22), fill=(40, 40, 46, 255))


def celular(c, x, y, h=120, mao='#e8bd96'):
    """celular aceso na mão (x, y = centro do aparelho)."""
    d = ImageDraw.Draw(c); w = h * .55
    g = Image.new('RGBA', (int(w * 3), int(h * 3)), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((0, 0, w * 3, h * 3), fill=(150, 210, 255, 90))
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(20)), (int(x - w * 1.5), int(y - h * 1.5)))
    d.rounded_rectangle((x - w / 2, y - h / 2, x + w / 2, y + h / 2), 12, fill=(40, 40, 50, 255), outline=INK + (255,), width=6)
    d.rectangle((x - w / 2 + 8, y - h / 2 + 12, x + w / 2 - 8, y + h / 2 - 12), fill=(150, 210, 255, 255))
    for dx in (-w * .55, w * .55):
        d.ellipse((x + dx - 24, y - 4, x + dx + 24, y + 44), fill=hexc(mao) + (255,), outline=INK + (255,), width=5)


# ------------------------------------------------------------------ CLOSE no rosto (serve nas 2 versões)
def close_fab(c, f, cx, cy, expr='neutro', look=0.0, s=1.0, escurece=0.0, shake=0.0, lagrima=0.0, dx=0, seed=2, boca=0.0, **kw):
    if boca: kw['boca'] = boca
    """recorta a vista em volta de (cx, cy), borra e põe o rosto grande. Devolve um palco BWxBH: use cam(BW/2, BH/2, 1.0x, 1.0x)."""
    BW, BH = kit.BW, kit.BH
    x0 = int(clamp(cx - BW / 2, 0, c.width - BW)); y0 = int(clamp(cy - BH / 2, 0, c.height - BH))
    bg = c.crop((x0, y0, x0 + BW, y0 + BH))
    bg = bg.resize((BW // 4, BH // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(3)).resize((BW, BH), Image.BILINEAR)
    if escurece > 0: bg.alpha_composite(Image.new('RGBA', bg.size, (20, 16, 30, int(150 * escurece))))
    kw['blink'] = 1 if blinkAt(f, seed) > .6 and expr not in ('choque', 'medo') else 0
    q = dict(kw); q['look'] = round(look * 4) / 4
    q['tremor'] = round(f / 3) if shake > 0 else 0
    if kw.get('boca'): q['boca'] = round(kw['boca'] * 4) / 4
    hh = int((1300 if HOR else 1700) * s)
    im = kit.sprite('rosto', tuple(sorted(dict(q, expr=expr).items())), hh, 1000 / 1700, False)
    bob = 6 * math.sin(f * .11); sx = shake * 8 * math.sin(f * 2.3)
    px, py = int(BW / 2 + dx - im.width / 2 + sx), int(BH - hh * .95 + bob)
    bg.alpha_composite(im, (px, py))
    if lagrima > 0:
        k = hh / 1700; d = ImageDraw.Draw(bg)
        for i, ex in enumerate((339, 661)):
            t = (lagrima + i * .37) % 1
            tx = px + (ex + (40 if i == 0 else -40)) * k; ty = py + (607 + 150 + 260 * t) * k
            r = 26 * k * 1.6
            d.polygon([(tx, ty - r * 1.8), (tx + r, ty), (tx, ty + r), (tx - r, ty)], fill=(160, 215, 250, 255), outline=INK + (255,))
            d.ellipse((tx - r, ty - r * .9, tx + r, ty + r * 1.1), fill=(160, 215, 250, 255), outline=INK + (255,), width=max(3, int(5 * k * 2)))
            d.ellipse((tx - r * .4, ty - r * .4, tx - r * .05, ty - r * .05), fill=(255, 255, 255, 255))
    return bg


def cam_close(f, z0=1.15, z1=1.0, f0=0, dur=10):
    """câmera do palco devolvido por close_fab (entra com zoom rápido e segue respirando)."""
    BW, BH = kit.BW, kit.BH
    z = lerp(z0, z1, easeOut(ramp(f, f0, f0 + dur))) * (1 + .0012 * max(0, f - f0))
    return (BW / 2, BH / 2, z, 0)


# ------------------------------------------------------------------ textos na tela (coordenadas da saída)
AMARELO = (255, 214, 64)


def _linhas_txt(im, linhas, x, y, size, cor=(255, 255, 255), alinha='c', s=1.0, fonte=None, maxw=None):
    """linhas de texto grande; palavras com * em volta ficam amarelas. alinha 'c' centraliza em x, 'e' começa em x.
    maxw = largura máxima (a fonte diminui até caber)."""
    if s <= .02: return
    fonte = fonte or F_CAP
    d = ImageDraw.Draw(im)
    if maxw:
        while size > 30 and max(d.textlength(l.replace('*', ''), font=font(fonte, size)) for l in linhas) > maxw: size -= 2
    size = int(size * (back(s) if s < 1 else 1))
    if size < 6: return
    fnt = font(fonte, size)
    for i, l in enumerate(linhas):
        ws = l.split(); total = d.textlength(l.replace('*', ''), font=fnt)
        xx = x - total / 2 if alinha == 'c' else x
        yy = y + i * size * 1.18
        for w in ws:
            amarela = w.startswith('*'); w2 = w.replace('*', '')
            d.text((xx + 6, yy + 8), w2, font=fnt, fill=(30, 20, 30), stroke_width=max(4, size // 9), stroke_fill=(30, 20, 30))
            d.text((xx, yy), w2, font=fnt, fill=AMARELO if amarela else cor, stroke_width=max(4, size // 9), stroke_fill=(36, 24, 34))
            xx += d.textlength(w2 + ' ', font=fnt)


def capa_txt(im, linhas, s=1.0, size=None, y=None, x=None, alinha='c'):
    """texto da CAPA (quadro 0): 2-3 linhas grandes."""
    if HOR:
        _linhas_txt(im, linhas, x if x is not None else 80, y if y is not None else 150, size or 112, alinha='e' if alinha == 'c' and x is None else alinha, s=s, maxw=1050)
    else:
        _linhas_txt(im, linhas, x if x is not None else OW / 2, y if y is not None else 150, size or 92, s=s, maxw=OW - 80)


def moral_txt(im, linhas, s=1.0):
    """MORAL no fim: faixa escura translúcida e texto grande no meio da tela."""
    if s <= .02: return
    a = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(a)
    size = 96 if not HOR else 92
    hh = len(linhas) * size * 1.18 + 120
    yc = OH * (.36 if not HOR else .42)
    d.rounded_rectangle((40 if not HOR else 260, yc - hh / 2, OW - (40 if not HOR else 260), yc + hh / 2), 40, fill=(30, 20, 34, int(190 * clamp(s))))
    im.alpha_composite(a)
    _linhas_txt(im, linhas, OW / 2, yc - hh / 2 + 60, size, s=s, maxw=OW - (140 if not HOR else 600))


def selo_txt(im, t, x, y, s=1.0, size=64, cor=(224, 88, 58), rot=-4):
    """etiqueta (no máximo 1 por frase): fundo creme, texto colorido."""
    if s <= .02: return
    fnt = font(F_STAMP, size); tw = ImageDraw.Draw(Image.new('L', (1, 1))).textlength(t, font=fnt)
    b = Image.new('RGBA', (int(tw + 80), int(size * 1.6)), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.rounded_rectangle((6, 6, b.width - 6, b.height - 6), 24, fill=(255, 246, 226, 255), outline=(36, 24, 34, 255), width=8)
    d.text((40, b.height / 2 - size * .62), t, font=fnt, fill=cor)
    paste_c(im, b.rotate(rot, Image.BICUBIC, expand=True), x, y, back(s) if s < 1 else 1)


# ------------------------------------------------------------------ legenda: 1 palavra grande, palavras-chave em amarelo
CHAVES_ATIVAS = set()


def cap_fab(im, ws, lf, y0=None):
    if y0 is None: y0 = 1490 if OH > OW else 915
    if not ws or lf < ws[0][1] - 2: return im
    cur = [w for w, t in ws if lf >= t - 1]
    if not cur: return im
    w = cur[-1].strip('.,:;!?…"\'')
    if not w: return im
    w = w.upper()
    age = lf - [t for ww, t in ws if lf >= t - 1][-1]
    d = ImageDraw.Draw(im); size = (84 if OH > OW else 70)
    size = int(size * (1 + .12 * (1 - clamp(age / 4))))
    f = font(F_CAP, size); tw = d.textlength(w, font=f)
    x = OW / 2 - tw / 2
    amarela = kit._norm(w) in CHAVES_ATIVAS
    d.text((x + 5, y0 + 7), w, font=f, fill=(30, 20, 30), stroke_width=9, stroke_fill=(30, 20, 30))
    d.text((x, y0), w, font=f, fill=AMARELO if amarela else (255, 255, 255), stroke_width=8, stroke_fill=(36, 24, 34))
    return im


def instala_legenda_fab(chaves=()):
    CHAVES_ATIVAS.update(kit._norm(c) for c in chaves)
    for nm in ('__main__', '__mp_main__', 'motor'):
        m = sys.modules.get(nm)
        if m is not None and hasattr(m, 'draw_caption'): m.draw_caption = cap_fab


def cta_card(im, cl, h):
    """cartão final (compartilhar), estilo fábula: creme com coração. Use CTA_CARD = cta_card."""
    im = im.convert('RGBA')
    s_ = back(ramp(cl, 0, 8))
    if s_ > .02:
        t = getattr(h, 'CTA_TEXTO', 'MANDA PRA QUEM VOCÊ AMA')
        f1 = font(F_STAMP, 104)
        tw = ImageDraw.Draw(Image.new('L', (1, 1))).textlength(t, font=f1)
        w = int(max(700, tw + 120)); w = min(w, OW - 40)
        while ImageDraw.Draw(Image.new('L', (1, 1))).textlength(t, font=f1) > w - 80: f1 = font(F_STAMP, f1.size - 4)
        c = Image.new('RGBA', (w, 360), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
        d.rounded_rectangle((6, 6, w - 6, 354), 40, fill=(255, 246, 226, 245), outline=(36, 24, 34, 255), width=9)
        tw = d.textlength(t, font=f1); d.text((w / 2 - tw / 2, 40), t, font=f1, fill=(224, 70, 58))
        hx, hy, r = w / 2, 258, 46   # coração
        d.ellipse((hx - r * 1.05, hy - r * .9, hx + r * .05, hy + r * .2), fill=(224, 70, 58))
        d.ellipse((hx - r * .05, hy - r * .9, hx + r * 1.05, hy + r * .2), fill=(224, 70, 58))
        d.polygon([(hx - r * 1.0, hy - r * .2), (hx + r * 1.0, hy - r * .2), (hx, hy + r * 1.0)], fill=(224, 70, 58))
        kit.paste_c(im, c, OW / 2, OH * (.3 if OH > OW else .38), s_)
    return im.convert('RGB')


# ------------------------------------------------------------------ trilha gerada (sem música de terceiros)
N_ = dict(C=261.63, Cs=277.18, D=293.66, Eb=311.13, E=329.63, F=349.23, Fs=369.99, G=392.0, Ab=415.3, A=440.0, Bb=466.16, B=493.88)


def _acorde(nomes, oit=-1):
    return [N_[n] * 2 ** oit for n in nomes]


HUMORES = {   # bpm, acordes (notas), brilho do arpejo, arpejo por compasso
    'misteriosa': (70, [['A', 'C', 'E', 'B'], ['F', 'A', 'C', 'E'], ['D', 'F', 'A', 'C'], ['E', 'A', 'B', 'E']], .9, 6),
    'triste': (62, [['D', 'F', 'A'], ['Bb', 'D', 'F'], ['F', 'A', 'C'], ['C', 'E', 'G']], .6, 4),
    'inspiradora': (82, [['C', 'E', 'G', 'C'], ['G', 'B', 'D', 'G'], ['A', 'C', 'E', 'A'], ['F', 'A', 'C', 'F']], 1.2, 8),
}


def _faixa(humor, N, SR):
    bpm, prog, bri, narp = HUMORES[humor]
    bar = 4 * 60 / bpm; nb = int(N / SR / bar) + 2
    out = np.zeros(int((nb + 3) * bar * SR))
    for i in range(nb):
        ch = prog[i % len(prog)]; st = int(i * bar * SR); n = int(bar * SR * 1.25)
        t = np.arange(n) / SR
        env = np.minimum(1, t / .5) * np.clip((bar * 1.25 - t) / .6, 0, 1)
        pad = sum(np.sin(2 * np.pi * f * .5 * t) * .5 + np.sin(2 * np.pi * f * .5 * 1.003 * t) * .5 + .25 * np.sin(2 * np.pi * f * t) for f in _acorde(ch, 0))
        out[st:st + n] += pad * env * .16
        bass = np.sin(2 * np.pi * _acorde(ch, -2)[0] * t) * env * .35
        out[st:st + n] += bass
        notas = (_acorde(ch, 1) + _acorde(ch, 2))[:narp]
        for k in range(narp):
            f0 = notas[k % len(notas)] if humor != 'triste' else notas[[0, 2, 1, 2][k % 4] % len(notas)]
            s0 = st + int(k * bar / narp * SR); m = int(1.4 * SR); tt = np.arange(m) / SR
            bell = (np.sin(2 * np.pi * f0 * tt) + .3 * np.sin(2 * np.pi * f0 * 2 * tt) * bri) * np.minimum(1, tt / .004) * np.exp(-tt / (.45 * bri + .2))
            out[s0:s0 + m] += bell * .22
    return out[:N]


def trilha(SC, N, SR, partes, fps=30):
    """partes = [(cena, 'misteriosa'|'triste'|'inspiradora'), ...]: troca de humor no começo da cena (crossfade de 2,5 s)."""
    fx = {}
    for _, hm in partes:
        if hm not in fx: fx[hm] = _faixa(hm, N, SR)
    mix = np.zeros(N); fade = int(2.5 * SR)
    starts = [int(SC[si][0] / fps * SR) for si, _ in partes] + [N]
    for k, (si, hm) in enumerate(partes):
        a, b = starts[k], starts[k + 1]
        w = np.zeros(N)
        w[a:b] = 1
        if k > 0: w[max(0, a - fade // 2):a + fade // 2] = np.linspace(0, 1, len(w[max(0, a - fade // 2):a + fade // 2]))
        if k + 1 < len(partes): w[max(0, b - fade // 2):b + fade // 2] = np.linspace(1, 0, len(w[max(0, b - fade // 2):b + fade // 2]))
        mix += fx[hm] * w
    e = min(N, int(1.5 * SR)); mix[:e] *= np.linspace(0, 1, e)
    e2 = int(2.0 * SR); mix[-e2:] *= np.linspace(1, 0, e2)
    return mix
