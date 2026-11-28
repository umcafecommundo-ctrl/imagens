"""Formato FÁBULA: "A loja dos esquecidos" (29/11/2026, 11h). Roteiro do doc nº 2 ("5 Fábulas Emocionantes — Roteiros", do Luis).
Tema: avós e as pessoas que a gente deixa de visitar. Moral: "Ninguém esquece de quem ama de uma vez. Esquece aos pouquinhos. Visite enquanto dá."
CTA: "Manda pra sua vó." LIPE e família com o visual fixo de fabula.py. A vó = VO (cabelo branco de coque, óculos, lilás).
Cenas/cores: s0 CAPA close Lipe + rua com a loja (vivo) | s1 ursinho/bicicleta/caderno esquecidos (vivo) | s2 ursinho some do quarto e aparece
na vitrine da loja (vivo) | s3 carrinho sumiu da prateleira -> Lipe vai atrás (vivo) | s4 prateleira empoeirada (vivo) | s5 CLOSE Lipe com o carrinho |
s6 vendedor no balcão (vivo) | s7 porta do fundo com luz amarela (vivo) | s8 Lipe empurra a porta e entra (vivo) | s9 sala das poltronas (tarde,
música triste) | s10 avós esperando (tarde) | s11 a vó tricota o cachecol azul (tarde) | s12 CLOSE vó com o cachecol | s13 lembrança: domingo,
bolo de fubá, história antes de dormir (tarde / noite_fab) | s14 Lipe diante da vó (tarde) | s15 CLOSE Lipe com lágrima | s16 CLOSE vó (virada) |
s17 os dois saem de mãos dadas, cachecol no pescoço (vivo, música inspiradora) | s18 a placa vira LEMBRADOS + CLOSE final (vivo) | s19 MORAL (tarde)."""
from kit import *
import kit
from sombrio import *
from fabula import *
from fabula import _piso, _escuro, _base

CHAVES = ['loja', 'amar', 'esquecidos', 'ursinho', 'bicicleta', 'caderno', 'carrinho', 'sumiu', 'poeira', 'esqueci', 'brincar',
          'devagarinho', 'porta', 'amarela', 'poltronas', 'avos', 'esperando', 'cachecol', 'azul', 'tres', 'aniversarios', 'domingos',
          'bolo', 'historias', 'tempo', 'vo', 'vir', 'mao', 'lembrados', 'pouquinhos', 'visite']
instala_legenda_fab(CHAVES)
MUSICA = True
MUSICA_NIVEL = .14
STING = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+2%'; PITCH = '-2Hz'

LINES = [
    "Nesta cidade, tudo o que você para de amar vai parar numa loja.",
    "O ursinho largado no canto. A bicicleta que ficou pequena. O caderno de desenhos que ninguém mais abriu.",
    "Quando ninguém lembra de uma coisa, ela some de casa... e aparece lá, na Loja dos Esquecidos.",
    "Um dia, o carrinho vermelho do Lipe sumiu do quarto. E ele foi atrás.",
    "Achou o carrinho numa prateleira cheia de poeira. Do lado, o ursinho dele. E a camisa do time que ele jurava que era a favorita.",
    "Eu não esqueci de vocês... só parei de brincar.",
    "O vendedor, um velhinho de óculos, sorriu: é assim que todo mundo esquece, menino. Devagarinho.",
    "No fundo da loja, tinha uma porta entreaberta, com uma luz amarela. O vendedor disse que ali ficava o que as pessoas mais esqueciam.",
    "O Lipe empurrou a porta, bem devagar... e entrou.",
    "Era uma sala cheia de poltronas. Em cada uma, tinha alguém sentado, olhando pra porta.",
    "Não eram objetos. Eram avós e avôs. Todos esperando alguém.",
    "Perto da janela, uma senhora tricotava um cachecol azul. Ela levantou os olhos.",
    "Lipe? Eu fiz esse cachecol pro seu aniversário. Faz três aniversários.",
    "O Lipe lembrou dos domingos na casa da vó. Do bolo de fubá. Das histórias antes de dormir.",
    "E percebeu que fazia muito tempo que ele não ia lá.",
    "Vó... eu não esqueci de você.",
    "Eu sei, meu amor. Você só parou de vir.",
    "O Lipe segurou a mão da vó, e os dois saíram juntos pela porta da loja. Com o cachecol azul no pescoço dele.",
    "Quando eles atravessaram a porta, a placa da loja mudou. Agora estava escrito: Lembrados.",
    "Ninguém esquece de quem ama de uma vez. Esquece aos pouquinhos. Visite enquanto dá.",
]
FALA_TIKTOK = "Manda pra sua vó."
CTA_TEXTO = "MANDA PRA SUA VÓ"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 16
FLASH = [9]
CAPA = 36
CHECK = [(0, 'loja', 8), (1, 'ursinho', 6), (1, 'bicicleta', 6), (1, 'caderno', 6), (2, 'some', 12), (2, 'aparece', 8), (2, 'esquecidos', 6),
         (3, 'sumiu', 6), (3, 'foi', 6), (4, 'carrinho', 6), (4, 'ursinho', 6), (4, 'camisa', 6), (5, 'brincar', 2), (6, 'sorriu', 4),
         (6, 'devagarinho', 4), (7, 'luz', 4), (7, 'vendedor', 6), (8, 'entrou', 4), (9, 'poltronas', 6), (9, 'porta', 4), (10, 'avos', 4),
         (11, 'cachecol', 4), (11, 'levantou', 6), (12, 'tres', 6), (13, 'bolo', 6), (13, 'historias', 6), (14, 'tempo', 4), (16, 'vir', 2),
         (17, 'mao', 4), (17, 'cachecol', 6), (18, 'placa', 4), (18, 'mudou', 8), (18, 'lembrados', 14), (19, 'pouquinhos', 6), (19, 'visite', 8)]
VOC = dict(VO)
VEND = dict(pele='#e4b48c', cabelo='#e0ddd6', penteado='curto', roupa='#3f7a5a', calca='#4a4036', velho=True, oculos=True)
VELHOS = [dict(pele='#c98d62', cabelo='#dcdad4', penteado='careca', roupa='#5aa36f', calca='#3a3a48', velho=True),
          dict(pele='#f0d0b0', cabelo='#e6e3dc', penteado='coque', roupa='#d65a8a', calca='#3b4f7a', velho=True, oculos=True),
          dict(pele='#8a5a3c', cabelo='#d0ccc4', penteado='curto', roupa='#e08a3a', calca='#2f3540', velho=True, barba=True)]


def TRILHA(SC, N, SR):
    return trilha(SC, N, SR, [(0, 'misteriosa'), (9, 'triste'), (17, 'inspiradora')])


def SFX(s):
    s.ting(s.W(0, 'loja'), .2)
    for w in ('ursinho', 'bicicleta', 'caderno'): s.thunk(s.W(1, w) - 2, 220, .3)
    s.trill(s.W(2, 'some'), .5, .06); s.ting(s.W(2, 'aparece'), .25)
    s.thunk(s.W(3, 'sumiu') - 2, 120, .5); s.patter(s.W(3, 'foi'), s.W(3, 'atras') + 30, 7, .08)
    s.ting(s.W(4, 'achou'), .2); s.ting(s.W(4, 'ursinho'), .12); s.ting(s.W(4, 'camisa'), .12)
    s.ting(s.W(7, 'luz'), .2)
    s.thunk(s.W(8, 'empurrou'), 80, .4); s.whoosh(s.W(8, 'entrou'), .7, .35)
    s.patter(s.cut(9) + 10, s.cut(10) - 10, 1.2, .05)
    s.ting(s.W(11, 'levantou'), .18)
    s.thunk(s.W(12, 'tres') - 2, 160, .35)
    s.ting(s.W(13, 'bolo'), .18)
    s.ting(s.W(16, 'vir'), .15)
    s.patter(s.W(17, 'sairam'), s.W(17, 'cachecol'), 5, .06)
    s.whoosh(s.W(18, 'mudou') - 4, .5, .4); s.ting(s.W(18, 'lembrados'), .3)
    s.ting(s.W(19, 'visite'), .22)


# ---------------------------------------------------------------- objetos esquecidos
def _poeira(im, n=60, seed=1):
    d = ImageDraw.Draw(im); rnd = random.Random(seed); a = im.split()[3]
    for _ in range(n):
        x, y = rnd.randint(0, im.width - 1), rnd.randint(0, im.height - 1)
        if a.getpixel((x, y)) > 200:
            r = rnd.randint(3, 7); d.ellipse((x - r, y - r, x + r, y + r), fill=(205, 200, 190, 170))
    return im


@lru_cache(maxsize=8)
def ursinho_img(w=300, po=True):
    p = Pen(600, 680)
    M, MD, C = hexc('#b07a48'), hexc('#8a5a32'), hexc('#e8c79a')
    for x in (190, 410): p.shape(ell_pts(x, 600, 95, 70, 30), M, MD, 7, 8)
    for x in (190, 410): p.dot(x, 612, 40, C)
    p.shape(ell_pts(300, 470, 170, 170, 40), M, MD, 7, 16)
    p.shape(ell_pts(300, 500, 95, 100, 30), C, None, 5, 0)
    for x in (135, 465): p.shape(ell_pts(x, 450, 60, 95, 24), M, MD, 6, 8)
    for x in (165, 435): p.dot(x, 110, 62, M, 7)
    for x in (165, 435): p.dot(x, 110, 32, C)
    p.shape(ell_pts(300, 220, 165, 150, 40), M, MD, 7, 14)
    p.shape(ell_pts(300, 275, 72, 55, 24), C, None, 5, 0)
    p.dot(300, 252, 22, INK); p.arc(300, 292, 26, 14, 20, 160, 6)
    for x in (235, 365): p.dot(x, 195, 20, INK)
    for x in (241, 371): p.dot(x, 188, 6, (255, 255, 255))
    p.shape([(380, 410), (445, 410), (445, 475), (380, 475)], hexc('#5aa3a0'), None, 5, 0)
    im = p.img.resize((600, 680), Image.LANCZOS)
    if po: im = _poeira(im, 70, 3)
    return im.resize((w, int(w * 680 / 600)), Image.LANCZOS)


@lru_cache(maxsize=8)
def carrinho_img(w=300, po=False):
    p = Pen(700, 400)
    R, RD = hexc('#e0473a'), hexc('#b8302a')
    p.shape([(40, 300), (55, 205), (190, 190), (255, 95), (470, 95), (545, 190), (655, 210), (668, 300)], R, RD, 8, 14)
    p.shape([(280, 120), (360, 120), (360, 190), (225, 190)], hexc('#bfe3f5'), None, 6, 0)
    p.shape([(385, 120), (455, 120), (515, 190), (385, 190)], hexc('#bfe3f5'), None, 6, 0)
    p.dot(640, 245, 18, hexc('#ffe27a'), 5)
    for x in (180, 520):
        p.dot(x, 305, 72, hexc('#2e2a30'), 7); p.dot(x, 305, 30, hexc('#c8c8cc'), 5)
    p.shape([(300, 230), (420, 230), (420, 270), (300, 270)], hexc('#fbf7ee'), None, 4, 0)
    im = p.img.resize((700, 400), Image.LANCZOS)
    if po: im = _poeira(im, 50, 5)
    return im.resize((w, int(w * 400 / 700)), Image.LANCZOS)


@lru_cache(maxsize=4)
def bicicleta_img(w=420):
    p = Pen(800, 540)
    T, TD = hexc('#3aa0b0'), hexc('#2a7a88')
    for cx in (170, 630):
        p.arc(cx, 390, 130, 130, 0, 360, 24, hexc('#2e2a30'))
        for k in range(6):
            a = k * math.pi / 3
            p.stroke([(cx, 390), (cx + 118 * math.cos(a), 390 + 118 * math.sin(a))], 4, hexc('#a0a0a8'))
        p.dot(cx, 390, 16, hexc('#c8c8cc'), 5)
    for pts in ([(170, 390), (370, 400), (320, 210)], [(320, 210), (560, 205), (370, 400)], [(560, 205), (630, 390)], [(170, 390), (320, 210)]):
        p.line(pts, T, 22, 6)
    p.shape(ell_pts(300, 190, 70, 24, 20), hexc('#2e2a30'), None, 5, 0)
    p.line([(560, 205), (545, 130), (620, 120)], hexc('#5a5a62'), 16, 5)
    p.dot(370, 400, 30, hexc('#5a5a62'), 5)
    im = p.img.resize((800, 540), Image.LANCZOS)
    return im.resize((w, int(w * 540 / 800)), Image.LANCZOS)


@lru_cache(maxsize=4)
def caderno_img(w=240):
    p = Pen(420, 520)
    p.shape([(60, 30), (390, 30), (390, 490), (60, 490)], hexc('#f2a65a'), hexc('#d98a3a'), 8, 12)
    for y in range(60, 480, 46): p.arc(60, y, 26, 14, 90, 270, 7)
    p.shape(ell_pts(225, 200, 70, 70, 30), hexc('#ffe27a'), None, 6, 0)
    for k in range(8):
        a = k * math.pi / 4
        p.stroke([(225 + 90 * math.cos(a), 200 + 90 * math.sin(a)), (225 + 120 * math.cos(a), 200 + 120 * math.sin(a))], 8, hexc('#ffe27a'))
    p.shape([(130, 430), (180, 340), (230, 430)], hexc('#5aa36f'), None, 5, 0)
    p.shape([(220, 430), (290, 320), (350, 430)], hexc('#4d79b3'), None, 5, 0)
    im = _poeira(p.img.resize((420, 520), Image.LANCZOS), 50, 7)
    return im.resize((w, int(w * 520 / 420)), Image.LANCZOS)


@lru_cache(maxsize=4)
def camisa_img(w=300):
    p = Pen(500, 470)
    G, GD = hexc('#2f9a5a'), hexc('#237a46')
    body = [(105, 60), (195, 22), (250, 52), (305, 22), (395, 60), (485, 170), (405, 215), (395, 445), (105, 445), (95, 215), (15, 170)]
    p.shape(body, G, GD, 8, 14)
    for x in (165, 335): p.poly([(x - 18, 70), (x + 18, 70), (x + 18, 440), (x - 18, 440)], hexc('#f4f1ea'))
    p.stroke(body + [body[0]], 8)
    p.shape([(205, 30), (295, 30), (250, 80)], hexc('#f4f1ea'), None, 5, 0)
    im = p.img.resize((500, 470), Image.LANCZOS)
    d = ImageDraw.Draw(im); fnt = font(F_CAP, 150); tw = d.textlength('10', font=fnt)
    d.text((250 - tw / 2, 170), '10', font=fnt, fill=(255, 246, 226), stroke_width=8, stroke_fill=(36, 24, 34))
    im = _poeira(im, 60, 9)
    return im.resize((w, int(w * 470 / 500)), Image.LANCZOS)


@lru_cache(maxsize=4)
def pipa_img(w=240):
    p = Pen(420, 620)
    p.shape([(210, 20), (400, 230), (210, 440), (20, 230)], hexc('#e0473a'), hexc('#b8302a'), 8, 10)
    p.poly([(210, 20), (400, 230), (210, 230)], hexc('#ffe27a'), 6); p.poly([(20, 230), (210, 440), (210, 230)], hexc('#ffe27a'), 6)
    p.stroke([(210, 20), (210, 440)], 6); p.stroke([(20, 230), (400, 230)], 6)
    p.stroke([(210, 440), (180, 500), (230, 550), (200, 610)], 5)
    for y, x in ((500, 180), (555, 230)): p.shape([(x - 20, y - 14), (x + 20, y + 14), (x + 20, y - 14), (x - 20, y + 14)], hexc('#4d79b3'), None, 4, 0)
    im = p.img.resize((420, 620), Image.LANCZOS)
    return im.resize((w, int(w * 620 / 420)), Image.LANCZOS)


AZUL_C, AZUL_CL = '#3e6fb8', '#7fa8e0'


@lru_cache(maxsize=4)
def cachecol_img(w=520):
    p = Pen(800, 260)
    pts = [(40, 80)] + [(x, 70 + 18 * math.sin(x / 90)) for x in range(80, 761, 40)] + [(760, 190)] + \
          [(x, 190 + 18 * math.sin(x / 90)) for x in range(720, 40, -40)]
    p.shape(pts, hexc(AZUL_C), mul(hexc(AZUL_C), .82), 8, 10)
    for x in range(120, 720, 120): p.poly([(x, 78 + 18 * math.sin(x / 90)), (x + 50, 78 + 18 * math.sin((x + 50) / 90)), (x + 50, 182 + 18 * math.sin((x + 50) / 90)), (x, 182 + 18 * math.sin(x / 90))], hexc(AZUL_CL))
    for k in range(5):
        p.stroke([(40, 90 + k * 22), (10, 92 + k * 22)], 7, hexc(AZUL_C)); p.stroke([(760, 100 + k * 20), (792, 102 + k * 20)], 7, hexc(AZUL_C))
    im = p.img.resize((800, 260), Image.LANCZOS)
    return im.resize((w, int(w * 260 / 800)), Image.LANCZOS)


def put_img(c, im, x, base, s=1.0, alpha=1.0, rot=0):
    """cola a imagem com o fundo em y=base, centro x; s = escala (pula com back), alpha 0..1."""
    if s <= .02 or alpha <= .02: return
    if s != 1: im = im.resize((max(2, int(im.width * s)), max(2, int(im.height * s))), Image.BILINEAR)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    if alpha < 1:
        a = im.split()[3].point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height)))


def faiscas(c, x, y, f, r=120, n=5, s=1.0):
    for k in range(n):
        a = k * 2 * math.pi / n + f * .05
        ph = (f * .06 + k / n) % 1
        brilho(c, x + r * math.cos(a) * (.6 + .4 * ph), y + r * math.sin(a) * (.6 + .4 * ph), 30 * s * math.sin(ph * math.pi))


def particulas(c, f, x0, y0, x1, y1, n=26, cor=(255, 240, 200), seed=4):
    """poeira flutuando no ar (na luz)."""
    d = ImageDraw.Draw(c); rnd = random.Random(seed)
    for k in range(n):
        bx, by = rnd.uniform(x0, x1), rnd.uniform(y0, y1); sp = rnd.uniform(.4, 1.2)
        x = bx + 30 * math.sin(f * .03 * sp + k); y = y0 + (by - y0 - f * sp * 1.5) % (y1 - y0)
        r = rnd.choice((4, 5, 7)); d.ellipse((x - r, y - r, x + r, y + r), fill=cor + (150,))


# ---------------------------------------------------------------- a loja (fachada)
@lru_cache(maxsize=2)
def fachada_img():
    W, H = 1100, 1000
    p = Pen(W, H)
    p.shape([(40, 150), (1060, 150), (1060, 1000), (40, 1000)], hexc('#9a86b8'), hexc('#7c689e'), 8, 18)
    for y in range(230, 1000, 90): p.stroke([(48, y), (1052, y)], 4, hexc('#86729f'))
    p.shape([(10, 140), (1090, 140), (1090, 180), (10, 180)], hexc('#6a4428'), None, 7, 0)
    for k in range(9):   # toldo listrado
        x0 = 30 + k * 116
        col = hexc('#e06a55') if k % 2 == 0 else hexc('#fbf7ee')
        p.shape([(x0, 340), (x0 + 116, 340), (x0 + 116, 410), (x0 + 58, 450), (x0, 410)], col, None, 6, 0)
    p.shape([(90, 470), (580, 470), (580, 880), (90, 880)], hexc('#6a4428'), None, 8, 0)    # vitrine (moldura)
    p.poly([(110, 490), (560, 490), (560, 860), (110, 860)], hexc('#f6e6b8'))
    p.shape([(80, 880), (590, 880), (590, 920), (80, 920)], hexc('#8a5a32'), None, 6, 0)
    p.shape([(690, 520), (960, 520), (960, 1000), (690, 1000)], hexc('#6a4428'), hexc('#553420'), 8, 0)   # porta
    p.shape([(730, 560), (920, 560), (920, 760), (730, 760)], hexc('#f6e6b8'), None, 6, 0)
    p.dot(910, 820, 14, hexc('#f4d48a'), 4)
    p.shape([(620, 980), (1030, 980), (1030, 1000), (620, 1000)], hexc('#8a8378'), None, 5, 0)
    im = p.img.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)   # teia de aranha num canto da vitrine
    for k in range(4): d.line((110, 490, 110 + 120 * math.cos(k * .45), 490 + 120 * math.sin(k * .45)), fill=(250, 250, 250, 200), width=3)
    for r in (40, 80, 115): d.arc((110 - r, 490 - r, 110 + r, 490 + r), 0, 90, fill=(250, 250, 250, 200), width=3)
    return im


@lru_cache(maxsize=4)
def placa_img(texto):
    novo = texto == 'LEMBRADOS'
    W, H = 900, 200
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    fundo = (255, 214, 64) if novo else (214, 196, 160)
    d.rounded_rectangle((8, 8, W - 8, H - 8), 26, fill=fundo + (255,), outline=(36, 24, 34, 255), width=10)
    f1 = font(F_STAMP, 52); t1 = 'LOJA DOS'
    d.text((W / 2 - d.textlength(t1, font=f1) / 2, 16), t1, font=f1, fill=(90, 60, 50) if not novo else (190, 60, 40))
    fs = 104
    while d.textlength(texto, font=font(F_STAMP, fs)) > W - 80: fs -= 4
    f2 = font(F_STAMP, fs)
    d.text((W / 2 - d.textlength(texto, font=f2) / 2, 66), texto, font=f2, fill=(110, 80, 70) if not novo else (200, 50, 40))
    if not novo:
        for x in (120, 520, 760): d.line((x, 30, x + 30, 170), fill=(170, 150, 120, 255), width=4)   # rachado/desbotado
    return im


def put_loja(c, x, base, f, placa='ESQUECIDOS', urso=1.0, vira=1.0, luz='dia'):
    """loja com a base (calçada) em y=base, centro x. urso 0..1 = ursinho aparecendo na vitrine; vira = escala vertical da placa (0..1)."""
    im = fachada_img(); x0, y0 = int(x - 550), int(base - 1000)
    c.alpha_composite(im, (x0, y0))
    put_img(c, bicicleta_img(300), x0 + 230, y0 + 860)
    put_img(c, pipa_img(130), x0 + 470, y0 + 700, rot=10)
    if urso > .02:
        put_img(c, ursinho_img(170), x0 + 470, y0 + 860, back(urso) if urso < 1 else 1)
        if urso < 1: faiscas(c, x0 + 470, y0 + 780, f, 110, 6, 1.3)
    d = ImageDraw.Draw(c)   # reflexo no vidro
    d.line((x0 + 140, y0 + 840, x0 + 260, y0 + 520), fill=(255, 255, 255, 150), width=14)
    d.line((x0 + 190, y0 + 840, x0 + 300, y0 + 540), fill=(255, 255, 255, 110), width=8)
    pl = placa_img(placa)
    if vira < .999: pl = pl.resize((pl.width, max(2, int(pl.height * max(.02, vira)))), Image.BILINEAR)
    pl = pl.rotate(-3 if placa == 'ESQUECIDOS' else 0, Image.BICUBIC, expand=True)
    c.alpha_composite(pl, (int(x - pl.width / 2), int(y0 + 140 - pl.height / 2 + 30)))
    if placa == 'LEMBRADOS':
        for k in range(5): brilho(c, x - 460 + k * 230, y0 + 60 + 30 * math.sin(f * .1 + k), 22 + 10 * math.sin(f * .2 + k))


PORTA_X = 1104 - 550 + 825   # centro da porta da loja na rua (x)


def rua_loja(f, luz='dia', scroll=0, placa='ESQUECIDOS', urso=1.0, vira=1.0):
    c = rua_fab(f, scroll=scroll, luz=luz)
    put_loja(c, 1104, 1460, f, placa, urso, vira, luz)
    return c


# ---------------------------------------------------------------- a loja (dentro)
@lru_cache(maxsize=2)
def loja_bg(carrinho=True):
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = Pen(SW, SH)
    p.poly([(0, 0), (SW, 0), (SW, FY), (0, FY)], hexc('#6f9c8f'))
    for x in range(0, SW, 130): p.stroke([(x, 0), (x, FY)], 6, hexc('#62897d'))
    p.shape([(0, FY - 60), (SW, FY - 60), (SW, FY), (0, FY)], hexc('#55786e'), None, 5, 0)
    _piso(p, '#9a7450')
    p.shape([(60, 360), (1010, 360), (1010, FY), (60, FY)], hexc('#7a5230'), hexc('#5e3e22'), 8, 14)   # estante
    p.poly([(100, 400), (970, 400), (970, FY - 10), (100, FY - 10)], hexc('#4e3420'))
    for y in (640, 980, 1320): p.shape([(80, y), (990, y), (990, y + 34), (80, y + 34)], hexc('#9a6a40'), hexc('#7a5230'), 6, 6)
    p.shape([(1110, 800), (1490, 800), (1490, FY), (1110, FY)], hexc('#6a4428'), None, 8, 0)   # batente da porta do fundo
    p.poly([(1140, 830), (1460, 830), (1460, FY), (1140, FY)], hexc('#2a1e18'))
    p.shape([(1560, 560), (2190, 560), (2190, 600), (1560, 600)], hexc('#9a6a40'), None, 6, 0)   # prateleira alta
    p.stroke([(1300, 0), (1300, 300)], 8)
    p.shape([(1200, 300), (1400, 300), (1350, 380), (1250, 380)], hexc('#ffd56a'), None, 7, 0)
    for x, cor in ((1640, '#e06a55'), (1760, '#f4b63f'), (2080, '#5aa36f')):   # potes e caixas na prateleira alta
        p.shape([(x - 45, 430), (x + 45, 430), (x + 45, 560), (x - 45, 560)], hexc(cor), mul(hexc(cor), .8), 6, 6)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    relogio(c, 3, 40, 1940, 480, 70)
    # objetos esquecidos
    put_img(c, caderno_img(200), 240, 640); put_img(c, pipa_img(190), 560, 640, rot=-8); put_img(c, ursinho_img(170), 840, 640)
    put_img(c, camisa_img(280), 560, 980); bola(c, 250, 925, 52, .6); put_img(c, carrinho_img(200, True), 840, 980)
    put_img(c, ursinho_img(230), 330, 1320)
    if carrinho: put_img(c, carrinho_img(270, True), 660, 1320)
    put_img(c, caderno_img(170), 880, 1320)
    put_img(c, bicicleta_img(380), 1700, FY + 60)
    g = Image.new('RGBA', (SW, SH), (0, 0, 0, 0)); d = ImageDraw.Draw(g)   # poeira nas prateleiras + teias
    for y in (640, 980, 1320): d.rectangle((100, y - 300, 970, y), fill=(200, 196, 186, 40))
    for cx, cy, a0 in ((100, 400, 0), (970, 400, 90)):
        for k in range(4):
            a = math.radians(a0) + k * .45
            d.line((cx, cy, cx + 160 * math.cos(a), cy + 160 * math.sin(a)), fill=(240, 240, 240, 170), width=3)
        for r in (50, 100, 150): d.arc((cx - r, cy - r, cx + r, cy + r), a0, a0 + 90, fill=(240, 240, 240, 170), width=3)
    c.alpha_composite(g)
    return c


@lru_cache(maxsize=1)
def balcao_frente():
    p = Pen(SW, SH)
    p.shape([(1560, 1230), (2220, 1230), (2220, 1290), (1560, 1290)], hexc('#9a6a40'), None, 7, 0)
    p.shape([(1580, 1285), (2220, 1285), (2220, FY + 40), (1580, FY + 40)], hexc('#b07a48'), hexc('#8a5a32'), 7, 16)
    for x in range(1640, 2200, 140): p.shape([(x, 1330), (x + 100, 1330), (x + 100, FY - 10), (x, FY - 10)], hexc('#a06c3c'), None, 5, 0)
    p.shape([(2060, 1150), (2190, 1150), (2190, 1232), (2060, 1232)], hexc('#5a5a62'), None, 6, 0)   # caixa registradora
    p.shape([(2080, 1110), (2170, 1110), (2170, 1150), (2080, 1150)], hexc('#7a7a84'), None, 5, 0)
    p.dot(1680, 1215, 22, hexc('#f4d48a'), 5)   # sininho
    return p.img.resize((SW, SH), Image.LANCZOS)


def porta_fundo(c, f, abre=.12, luz_forte=0.0):
    """porta do fundo entreaberta com luz amarela; abre 0..1."""
    x0, x1, y0, y1 = 1140, 1460, 830, FY
    gap = lerp(30, x1 - x0, clamp(abre))
    pul = .85 + .15 * math.sin(f * .12)
    g = Image.new('RGBA', (SW, SH), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    d.polygon([(x0, y1), (x0 + gap, y1), (x0 + gap + 300 + 700 * abre, SH), (x0 - 200 - 500 * abre, SH)], fill=(255, 220, 120, int(90 * pul)))
    d.ellipse((x0 - 200, y0 - 150, x0 + gap + 200, y1 + 150), fill=(255, 220, 120, int(70 * pul + 80 * luz_forte)))
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(40)))
    d = ImageDraw.Draw(c)
    d.rectangle((x0, y0, x0 + gap, y1), fill=(255, 226, 140, 255))
    if gap < x1 - x0 - 10:
        d.polygon([(x0 + gap, y0 - 10), (x1, y0), (x1, y1), (x0 + gap, y1 + 10)], fill=(138, 90, 50, 255), outline=INK + (255,))
        d.line([(x0 + gap, y0 - 10), (x1, y0), (x1, y1), (x0 + gap, y1 + 10), (x0 + gap, y0 - 10)], fill=INK + (255,), width=7)
        d.ellipse((x0 + gap + 30, 1180, x0 + gap + 58, 1208), fill=(244, 212, 138, 255), outline=INK + (255,), width=4)
    particulas(c, f, x0 - 150, y0, x0 + gap + 250, y1, 18, seed=7)


def loja(f, carrinho=True, abre=.12, luz_forte=0.0):
    c = loja_bg(carrinho).copy()
    porta_fundo(c, f, abre, luz_forte)
    particulas(c, f, 120, 420, 960, 1500, 22, (235, 230, 215), 3)
    return c


# ---------------------------------------------------------------- a sala das poltronas
XS = (430, 880, 1330, 1780)
POLT = ('#5aa36f', '#c96b4a', '#4d79b3', '#d4a03a')
ASSENTO = 1350; HS = 900; FEET_S = ASSENTO + .28 * HS


@lru_cache(maxsize=2)
def sala_esp_bg(luz='tarde'):
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = _base('#efd9b0', '#e6cc9c')
    p.shape([(100, 440), (640, 440), (640, 1000), (100, 1000)], hexc('#fbf7ee'), hexc('#ddd6c6'), 7, 8)
    _piso(p, '#b98a58')
    p.shape(ell_pts(1104, 1900, 980, 190, 60), hexc('#9b6bb5'), hexc('#7a4f94'), 7, 14)
    from fabula import _quadro
    _quadro(p, 1480, 480, 260, 200, '#8fd6a0'); _quadro(p, 1840, 560, 200, 160, '#f2a65a')
    for x, col in zip(XS, POLT):
        p.shape([(x - 200, 1030), (x + 200, 1030), (x + 220, 1360), (x - 220, 1360)], hexc(col), mul(hexc(col), .8), 8, 18)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    sky = ceu_fab('tarde' if luz == 'tarde' else 'dia').crop((130, 250, 610, 780)); c.alpha_composite(sky, (130, 470))
    q = Pen(SW, SH)
    q.stroke([(370, 470), (370, 970)], 14, hexc('#fbf7ee')); q.stroke([(130, 720), (610, 720)], 14, hexc('#fbf7ee'))
    q.stroke([(130, 470), (610, 470), (610, 970), (130, 970), (130, 470)], 7)
    q.shape([(80, 1000), (660, 1000), (660, 1040), (80, 1040)], hexc('#fbf7ee'), None, 6, 0)
    c.alpha_composite(q.img.resize((SW, SH), Image.LANCZOS))
    return _escuro(c, luz)


@lru_cache(maxsize=1)
def poltronas_frente():
    p = Pen(SW, SH)
    for x, col in zip(XS, POLT):
        cc = hexc(col)
        p.shape([(x - 215, 1340), (x + 215, 1340), (x + 215, 1585), (x - 215, 1585)], mul(cc, 1.08), cc, 8, 16)
        for x0 in (x - 265, x + 175):
            p.shape([(x0, 1200), (x0 + 90, 1200), (x0 + 90, 1585), (x0, 1585)], cc, mul(cc, .8), 8, 12)
        for xx in (x - 230, x + 230): p.shape([(xx - 16, 1585), (xx + 16, 1585), (xx + 10, 1630), (xx - 10, 1630)], hexc('#6a4428'), None, 5, 0)
    return p.img.resize((SW, SH), Image.LANCZOS)


def sala_esp(f, vo_expr='neutro', vo_look=0.0, exprs=('neutro', 'preocupado', 'neutro'), looks=(0, 0, 0), trico_=True, luz='tarde'):
    c = sala_esp_bg(luz).copy()
    relogio(c, 17, int(f / 10) % 60, 1104, 470, 90)
    pessoa(c, XS[0], FEET_S, HS, f, VOC, seed=6, expr=vo_expr, look=vo_look)
    for i, (x, cr_) in enumerate(zip(XS[1:], VELHOS)):
        pessoa(c, x, FEET_S, HS, f, cr_, seed=8 + i, expr=exprs[i], look=looks[i])
    c.alpha_composite(poltronas_frente())
    if trico_: trico_azul(c, XS[0], FEET_S - .3 * HS, f)
    return c


def trico_azul(c, x, y, f):
    """agulhas + cachecol azul comprido nas mãos da vó."""
    d = ImageDraw.Draw(c); a = math.sin(f * .4) * 12
    d.line((x - 80, y - 60 + a, x + 20, y + 30), fill=(200, 200, 205, 255), width=10)
    d.line((x + 80, y - 60 - a, x - 20, y + 30), fill=(200, 200, 205, 255), width=10)
    im = cachecol_img(360).rotate(-80, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2 + 30), int(y)))


def cachecol_corpo(c, x, feet, h, flip=False):
    """cachecol azul no pescoço de quem está em (x, feet, h) (personagem de put_menino)."""
    k = h / 1000; sg = -1 if flip else 1
    X = lambda sx: x + sg * (sx - 300) * k
    Y = lambda sy: feet + .025 * h - h + sy * k
    d = ImageDraw.Draw(c)
    band = [(X(232), Y(440)), (X(368), Y(440)), (X(378), Y(512)), (X(222), Y(512))]
    tail = [(X(318), Y(490)), (X(374), Y(490)), (X(384), Y(668)), (X(328), Y(668))]
    for pts in (tail, band):
        d.polygon(pts, fill=hexc(AZUL_C) + (255,)); d.line(pts + [pts[0]], fill=INK + (255,), width=max(4, int(8 * k)))
    for sy in (540, 600):
        d.line((X(322), Y(sy), X(378), Y(sy)), fill=hexc(AZUL_CL) + (255,), width=max(4, int(14 * k)))


def cachecol_close(bg, f, s, dx=0):
    """cachecol azul no pescoço do close_fab (mesma posição do rosto)."""
    BW_, BH_ = kit.BW, kit.BH
    hh = int((1300 if HOR else 1700) * s); k = hh / 1700; w = int(hh * 1000 / 1700)
    px, py = BW_ / 2 + dx - w / 2, BH_ - hh * .95 + 6 * math.sin(f * .11)
    P_ = lambda pts: [(px + x * k, py + y * k) for x, y in pts]
    d = ImageDraw.Draw(bg)
    tail = P_([(555, 1060), (665, 1060), (690, 1500), (580, 1500)])
    band = P_([(320, 950), (680, 950), (705, 1110), (295, 1110)])
    for pts in (tail, band):
        d.polygon(pts, fill=hexc(AZUL_C) + (255,)); d.line(pts + [pts[0]], fill=INK + (255,), width=int(12 * k) + 2)
    for y in (1180, 1300):
        a, b = P_([(570, y), (680, y)]); d.line((a, b), fill=hexc(AZUL_CL) + (255,), width=int(26 * k))
    for x in range(360, 680, 90):
        a, b = P_([(x, 975), (x + 40, 1090)]); d.line((a, b), fill=hexc(AZUL_CL) + (255,), width=int(20 * k))


# ---------------------------------------------------------------- lembrança: a casa da vó (de 28/11)
@lru_cache(maxsize=1)
def _base_vo():
    p = Pen(SW, SH)
    p.poly([(0, 0), (SW, 0), (SW, FY), (0, FY)], hexc('#f7e3c8'))
    for y in range(80, FY - 60, 150):
        for x in range(60 + (y // 150 % 2) * 75, SW, 150):
            for k in range(5): p.dot(x + 12 * math.cos(k * 1.256), y + 12 * math.sin(k * 1.256), 9, hexc('#f2b8b0'))
            p.dot(x, y, 6, hexc('#f4b63f'))
    p.shape([(0, FY - 60), (SW, FY - 60), (SW, FY), (0, FY)], hexc('#d9b48a'), None, 5, 0)
    p.shape([(270, 680), (790, 680), (790, 1170), (270, 1170)], hexc('#fbf7ee'), hexc('#ddd6c6'), 7, 8)
    p.shape([(1260, 560), (1520, 560), (1520, 860), (1260, 860)], hexc('#8a5a32'), None, 7, 0)
    p.poly([(1285, 585), (1495, 585), (1495, 835), (1285, 835)], hexc('#f4e1a1'))
    p.dot(1390, 680, 50, hexc('#e8bd96'), 5); p.shape([(1320, 835), (1460, 835), (1440, 760), (1340, 760)], hexc('#9b6bb5'), None, 5, 0)
    _piso(p, '#b98a58')
    p.shape(ell_pts(1104, 1920, 760, 170, 60), hexc('#e06a55'), hexc('#b8432a'), 7, 14)
    p.shape([(1120, 1050), (1680, 1050), (1700, 1360), (1100, 1360)], hexc('#5aa36f'), hexc('#3f8a52'), 8, 18)
    return p.img.resize((SW, SH), Image.LANCZOS)


@lru_cache(maxsize=2)
def salinha_fab(luz='tarde'):
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    c.alpha_composite(_base_vo())
    sky = ceu_fab('tarde' if luz == 'tarde' else 'dia').crop((300, 300, 760, 750)); c.alpha_composite(sky, (300, 700))
    q = Pen(SW, SH)
    q.stroke([(530, 700), (530, 1150)], 14, hexc('#fbf7ee')); q.stroke([(300, 925), (760, 925)], 14, hexc('#fbf7ee'))
    q.stroke([(300, 700), (760, 700), (760, 1150), (300, 1150), (300, 700)], 7)
    q.shape([(270, 1150), (790, 1150), (790, 1190), (270, 1190)], hexc('#fbf7ee'), None, 6, 0)
    c.alpha_composite(q.img.resize((SW, SH), Image.LANCZOS))
    return _escuro(c, luz)


@lru_cache(maxsize=1)
def poltrona_frente():
    p = Pen(SW, SH)
    p.shape([(1090, 1340), (1710, 1340), (1710, 1580), (1090, 1580)], hexc('#6ab57e'), hexc('#4a9a60'), 8, 16)
    for x0 in (1030, 1650):
        p.shape([(x0, 1200), (x0 + 120, 1200), (x0 + 120, 1580), (x0, 1580)], hexc('#5aa36f'), hexc('#3f8a52'), 8, 12)
    for x in (1120, 1680): p.shape([(x - 18, 1580), (x + 18, 1580), (x + 12, 1630), (x - 12, 1630)], hexc('#6a4428'), None, 5, 0)
    return p.img.resize((SW, SH), Image.LANCZOS)


def bolo(c, x, y, s=1.0, f=0):
    d = ImageDraw.Draw(c)
    d.ellipse((x - 200 * s, y - 40 * s, x + 200 * s, y + 20 * s), fill=(250, 250, 246, 255), outline=INK + (255,), width=6)
    d.rectangle((x - 150 * s, y - 150 * s, x + 150 * s, y - 20 * s), fill=(236, 186, 80, 255))
    d.ellipse((x - 150 * s, y - 60 * s, x + 150 * s, y + 10 * s), fill=(236, 186, 80, 255), outline=INK + (255,), width=6)
    d.line((x - 150 * s, y - 150 * s, x - 150 * s, y - 25 * s), fill=INK + (255,), width=6); d.line((x + 150 * s, y - 150 * s, x + 150 * s, y - 25 * s), fill=INK + (255,), width=6)
    d.ellipse((x - 150 * s, y - 190 * s, x + 150 * s, y - 110 * s), fill=(246, 206, 110, 255), outline=INK + (255,), width=6)
    d.ellipse((x - 36 * s, y - 166 * s, x + 36 * s, y - 134 * s), fill=(160, 110, 50, 255), outline=INK + (255,), width=5)
    for k in range(3):
        a = (f * .03 + k / 3) % 1
        d.arc((x - 60 * s + k * 50 * s, y - 330 * s - a * 120 * s, x - 20 * s + k * 50 * s, y - 230 * s - a * 120 * s), 90, 270, fill=(255, 255, 255, int(220 * (1 - a))), width=6)


def lipe_chao(c, x, f, expr='sorriso', look=.75, y=1820, flip=False):
    pessoa(c, x, y + .3 * KID, KID, f, LIPE, seed=2, expr=expr, look=look, flip=flip)
    d = ImageDraw.Draw(c)
    d.ellipse((x - 300, y - 30, x + 300, y + 140), fill=(224, 106, 85, 255), outline=INK + (255,), width=8)


def livro(c, x, y, s=1.0):
    d = ImageDraw.Draw(c)
    for sg in (-1, 1):
        pts = [(x, y), (x + sg * 130 * s, y - 20 * s), (x + sg * 130 * s, y + 120 * s), (x, y + 140 * s)]
        d.polygon(pts, fill=(250, 246, 232, 255)); d.line(pts + [pts[0]], fill=INK + (255,), width=6)
        for k in range(4): d.line((x + sg * 20 * s, y + (15 + k * 28) * s, x + sg * 110 * s, y + (-2 + k * 28) * s), fill=(120, 120, 150, 255), width=4)
    d.polygon([(x - 140 * s, y + 120 * s), (x, y + 150 * s), (x + 140 * s, y + 120 * s), (x + 140 * s, y + 135 * s), (x, y + 165 * s), (x - 140 * s, y + 135 * s)], fill=(77, 121, 179, 255))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = loja(0)
        c = close_fab(c, f, 1104, 1200, expr='choque', look=0, s=V(.9, .95), dx=V(0, 480), **LIPE)
        if HOR: put_img(c, ursinho_img(330), 480, 1180)
        else: put_img(c, ursinho_img(300), 220, 2190, rot=6)
        return c, cam_close(f, 1.04, 1.0), 'vivo'
    g = f - CAPA
    lo = wt(0, 'loja') - 4
    c = rua_loja(f)
    t = smooth(ramp(g, 0, lo - CAPA + 20))
    bx = lerp(150, PORTA_X - 60, t)
    if t < .98:
        bola(c, bx, 1720 - 60 * abs(math.sin(g * .25)) * (1 - t), 50, g * .3)
        put_img(c, pipa_img(170), lerp(200, PORTA_X, t), lerp(900, 1500, t), lerp(1, .6, t), rot=20 * math.sin(g * .1))
    pessoa(c, 320 + g * 1.5, 1770, ADU, f, GENTE[1], walk=1, seed=3, expr='neutro', look=.75)
    k = smooth(ramp(f, lo - 10, lo + 16))
    return c, cam(lerp(V(650, 1104), V(1104, 1104), k), lerp(V(1350, 1250), V(1150, 1100), k), lerp(1.3, 1.1, k) * (1 + .0006 * f), lerp(1.15, 1.0, k) * (1 + .0006 * f)), 'vivo'


def s1(f):
    bi, ca = wt(1, 'bicicleta') - 3, wt(1, 'caderno') - 3
    if f < bi:
        c = quarto_fab('dia').copy()
        put_img(c, ursinho_img(340), 480, 1760, rot=12)
        d = ImageDraw.Draw(c)
        for k in range(4): d.line((100, FY - 40, 100 + 260 * math.cos(-k * .4), FY - 40 + 260 * math.sin(-k * .4)), fill=(250, 250, 250, 200), width=4)
        return c, cam(560, V(1500, 1350), zf(1.7, f, .002), zf(1.35, f, .002), -2), 'vivo'
    if f < ca:
        g = f - bi
        c = quintal_fab('dia').copy()
        put_img(c, bicicleta_img(360), 1200, 1640, rot=4)
        pessoa(c, 820, 1780, KID, f, LIPE, seed=2, expr='curioso', look=.75)
        return c, cam(1050, V(1350, 1250), zf(1.35, g, .002), zf(1.1, g, .002)), 'vivo'
    g = f - ca
    c = sala_fab('dia').copy()
    c.alpha_composite(sofa_frente())
    put_img(c, caderno_img(260), 1000, 1360, rot=-75)
    particulas(c, f, 800, 1000, 1300, 1400, 14, (235, 230, 215), 5)
    return c, cam(1000, V(1300, 1250), zf(1.6, g, .002), zf(1.3, g, .002), 2), 'vivo'


def s2(f):
    so, ap = wt(2, 'some') - 3, wt(2, 'aparece') - 4
    if f < ap:
        c = quarto_fab('dia').copy()
        al = 1 - ramp(f, so, so + 24)
        put_img(c, ursinho_img(340), 700, 1760, alpha=al, rot=12)
        if f >= so: faiscas(c, 700, 1600, f, 160 * (1 + ramp(f, so, so + 24)), 7, 1.5)
        pessoa(c, 1130, 1790, KID, f, LIPE, seed=2, expr='preocupado' if f >= so else 'neutro', look=-.5, walk=0)
        return c, cam(880, V(1450, 1300), zf(1.45, f, .0015), zf(1.15, f, .0015)), 'vivo'
    g = f - ap; es = wt(2, 'esquecidos') - 4
    c = rua_loja(f, urso=ramp(g, 0, 12) if g < 12 else 1.0)
    k = smooth(ramp(f, es - 8, es + 12))
    return c, cam(lerp(1104 - 550 + 400, 1104, k), lerp(1210, 1000, k), lerp(V(2.0, 1.7), V(1.25, 1.05), k) * (1 + .0015 * g), lerp(1.7, 1.05, k) * (1 + .0015 * g)), 'vivo'


def s3(f):
    su, fo = wt(3, 'sumiu') - 3, wt(3, 'foi') - 3
    if f < fo:
        c = quarto_fab('dia').copy()
        d = ImageDraw.Draw(c)
        d.rounded_rectangle((1250, 860, 1520, 980), 20, outline=(200, 190, 170, 255), width=8)   # marca de poeira onde estava o carrinho
        for x in range(1270, 1510, 30): d.line((x, 975, x + 14, 975), fill=(210, 200, 185, 255), width=6)
        put_img(c, pipa_img(140), 1100, 980); bola(c, 1640, 935, 44, .4)
        pessoa(c, 960, 1780, KID, f, LIPE, seed=2, expr='choque' if f >= su else 'curioso', look=.75)
        t = easeOut(ramp(f, su, su + 10))
        return c, cam(lerp(1104, 1200, t), lerp(V(1300, 1250), V(1150, 1100), t), lerp(1.2, 1.55, t) * (1 + .0008 * f), lerp(1.0, 1.25, t) * (1 + .0008 * f)), 'vivo'
    g = f - fo
    c = rua_fab(f, scroll=g * 14, luz='dia')
    pessoa(c, 1104, 1780, KID, f, LIPE, walk=1, seed=2, expr='desconfiado', look=.75)
    return c, cam(1104, V(1350, 1250), zf(1.3, g, .002), zf(1.08, g, .002)), 'vivo'


def s4(f):
    ur, cm = wt(4, 'ursinho') - 3, wt(4, 'camisa') - 3; ac = wt(4, 'achou') - 3
    c = loja(f)
    pessoa(c, 1120, 1790, KID, f, LIPE, seed=2, expr='curioso' if f < ur else 'sorriso', look=-.75)
    if f >= ac: faiscas(c, 660, 1230, f, 150, 5, 1.2 * ramp(f, ac, ac + 6))
    if f < ur: cx, cy, z = 760, 1250, 1.65
    elif f < cm: cx, cy, z = 520, 1200, 1.75
    else: cx, cy, z = 620, 950, 1.75
    k = easeOut(ramp(f, ur, ur + 10)) if f < cm else easeOut(ramp(f, cm, cm + 10))
    pz = 1 + .0012 * f
    return c, cam(cx, cy, z * pz, z * .78 * pz), 'vivo'


def s5(f):
    c = loja(f, carrinho=False)
    pessoa(c, 760, 1790, KID, f, LIPE, seed=2, expr='preocupado', look=-.5)
    c = close_fab(c, f, 700, 1150, expr='preocupado', look=V(-.5, -.25), s=V(.95, .95), dx=V(0, 380), **LIPE)
    bx = kit.BW / 2 + V(0, 380); by = kit.BH - V(60, 30)
    put_img(c, carrinho_img(V(560, 460)), bx, by + 4 * math.sin(f * .2))
    return c, cam_close(f, 1.15, 1.0), 'vivo'


def lipe_com_carrinho(c, x, feet, f, **kw):
    pessoa(c, x, feet, KID, f, LIPE, seed=2, **kw)
    hx, hy = mao_dir(x, feet, KID)
    put_img(c, carrinho_img(170), hx, hy + 40)


def s6(f):
    so = wt(6, 'sorriu') - 3; dv = wt(6, 'devagarinho') - 3
    c = loja(f, carrinho=False)
    pessoa(c, 1900, 1650, ADU, f, VEND, seed=9, expr='sorriso' if f >= so else 'neutro', look=-.75)
    c.alpha_composite(balcao_frente())
    lipe_com_carrinho(c, 1330, 1800, f, expr='curioso', look=.75)
    k = easeOut(ramp(f, dv, dv + 14))
    return c, cam(lerp(1650, 1800, k), lerp(V(1250, 1150), V(1150, 1100), k), lerp(1.3, 1.75, k) * (1 + .0008 * f), lerp(1.08, 1.4, k) * (1 + .0008 * f)), 'vivo'


def s7(f):
    ve = wt(7, 'vendedor') - 3
    c = loja(f, carrinho=False)
    pessoa(c, 1900, 1650, ADU, f, VEND, seed=9, expr='sorriso' if f >= ve else 'neutro', look=-.75 if f >= ve else -1)
    c.alpha_composite(balcao_frente())
    lipe_com_carrinho(c, 900, 1800, f, expr='curioso', look=.75)
    if f < ve:
        return c, cam(1250, V(1250, 1200), zf(1.25, f, .0025), zf(1.05, f, .002)), 'vivo'
    g = f - ve
    return c, cam(1550, V(1200, 1150), zf(1.45, g, .0015), zf(1.15, g, .0012)), 'vivo'


def s8(f):
    em, en = wt(8, 'empurrou') - 3, wt(8, 'entrou') - 3
    ab = lerp(.12, 1.0, smooth(ramp(f, em, en)))
    c = loja(f, carrinho=False, abre=ab, luz_forte=ramp(f, en, en + 12))
    x = lerp(980, 1300, smooth(ramp(f, en - 4, en + 16)))
    lipe_com_carrinho(c, x, 1800, f, expr='curioso', look=.75, walk=1 if f >= en - 4 else 0)
    if f >= en:
        c.alpha_composite(Image.new('RGBA', c.size, (255, 236, 180, int(230 * ramp(f, en + 4, en + 18)))))
    return c, cam(1300, V(1250, 1200), zf(1.5, f, .002), zf(1.2, f, .002)), 'vivo'


def s9(f):
    po = wt(9, 'porta') - 3
    c = sala_esp(f, vo_expr='neutro', looks=(0, 0, 0), exprs=('neutro', 'preocupado', 'neutro'))
    t = smooth(ramp(f, 0, 120))
    return c, cam(lerp(V(880, 1104), V(1104, 1104), t), V(1250, 1200), lerp(1.7, V(1.2, 1.0), t) * (1 + .0006 * f), lerp(1.3, 1.0, t) * (1 + .0006 * f)), 'tarde'


def s10(f):
    c = sala_esp(f, vo_expr='preocupado', vo_look=0, exprs=('preocupado', 'neutro', 'preocupado'), looks=(.25, 0, -.25))
    t = smooth(ramp(f, 0, 150))
    return c, cam(lerp(1780, 880, t), V(1150, 1150), zf(1.75, f, .0008), zf(1.45, f, .0008)), 'tarde'


def s11(f):
    le = wt(11, 'levantou') - 3; ca = wt(11, 'cachecol') - 3
    c = sala_esp(f, vo_expr='curioso' if f >= le else 'neutro', vo_look=0 if f >= le else .25)
    k = easeOut(ramp(f, ca, ca + 14))
    kk = kick(f, le + 2, .5)
    return c, cam(lerp(600, 480, k), lerp(V(1200, 1150), V(1180, 1150), k) + kk * 10, lerp(1.45, 2.0, k) * (1 + .0008 * f), lerp(1.2, 1.6, k) * (1 + .0008 * f)), 'tarde'


def s12(f):
    c = sala_esp(f, vo_expr='sorriso', vo_look=0, trico_=False)
    c = close_fab(c, f, 600, 1150, expr='sorriso', look=V(0, .25), s=V(.95, .95), dx=V(0, -380), **VOC)
    bx = kit.BW / 2 + V(0, -380); by = kit.BH - V(40, 10)
    put_img(c, cachecol_img(V(820, 700)), bx, by + 4 * math.sin(f * .15), rot=4)
    return c, cam_close(f, 1.12, 1.0), 'tarde'


def s13(f):
    bo, hi = wt(13, 'bolo') - 3, wt(13, 'historias') - 3
    if f < hi:
        c = salinha_fab('tarde').copy()
        pessoa(c, 1400, 1350 + .28 * 1000, 1000, f, VOC, seed=6, expr='sorriso', look=-.5)
        c.alpha_composite(poltrona_frente())
        if f >= bo: bolo(c, 1240, 1520, .8 * (back(ramp(f, bo, bo + 10)) if f < bo + 10 else 1), f)
        lipe_chao(c, 760, f, expr='sorriso', look=.75)
        t = smooth(ramp(f, 0, hi))
        return c, cam(lerp(V(1000, 1104), V(1150, 1104), t), V(1300, 1300), zf(1.2, f, .0012), zf(1.0, f, .0008)), 'tarde'
    g = f - hi
    c = quarto_fab('noite').copy()
    pessoa(c, 1860, 1290 + .28 * KID, KID, f, LIPE_PIJAMA, seed=2, expr='sorriso', look=-.75)
    d = ImageDraw.Draw(c)
    cob = [(1600, 1390), (2110, 1370), (2110, 1575), (1600, 1575)]
    d.polygon(cob, fill=(244, 212, 138, 255)); d.line(cob + [cob[0]], fill=INK + (255,), width=8)
    for x in range(1660, 2100, 110): d.ellipse((x - 18, 1460, x + 18, 1496), fill=(224, 106, 85, 255))
    vf = 1360 + .28 * 950
    pessoa(c, 1330, vf, 950, f, VOC, seed=6, expr='sorriso', look=.75)
    d.rectangle((1170, 1350, 1500, 1600), fill=(154, 106, 64, 255), outline=INK + (255,), width=7)
    hx, hy = mao_dir(1330, vf, 950); livro(c, hx - 40, hy - 70, .9)
    return c, cam(1600, V(1250, 1200), zf(1.35, g, .0015), zf(1.15, g, .0012)), 'noite_fab'


def s14(f):
    te = wt(14, 'tempo') - 3
    c = sala_esp(f, vo_expr='neutro', vo_look=.5, exprs=('neutro', 'neutro', 'neutro'), looks=(-.5, -.75, -.75), trico_=False)
    put_img(c, cachecol_img(420), XS[0], FEET_S - .32 * HS + 60, rot=-6)
    pessoa(c, 900, 1840, KID, f, LIPE, seed=2, expr='preocupado', look=-.75)
    k = smooth(ramp(f, te - 10, te + 30))
    return c, cam(lerp(V(700, 1104), V(680, 900), k), V(1250, 1250), lerp(1.4, 1.7, k) * (1 + .0006 * f), lerp(1.1, 1.35, k) * (1 + .0006 * f)), 'tarde'


def s15(f):
    c = sala_esp(f, trico_=False)
    pessoa(c, 900, 1840, KID, f, LIPE, seed=2, expr='preocupado', look=-.75)
    c = close_fab(c, f, 800, 1250, expr='preocupado', look=V(-.25, -.5), s=V(.95, .95), dx=V(0, 380), lagrima=(f / 45) % 1, **LIPE)
    return c, cam_close(f, 1.15, 1.0), 'tarde'


def s16(f):
    c = sala_esp(f, vo_expr='sorriso', trico_=False)
    c = close_fab(c, f, 600, 1150, expr='sorriso', look=V(.25, .5), s=V(.95, .95), dx=V(0, -380), **VOC)
    bx = kit.BW / 2 + V(0, -380); by = kit.BH - V(40, 10)
    put_img(c, cachecol_img(V(820, 700)), bx, by, rot=4)
    return c, cam_close(f, 1.06, 1.0), 'tarde'


def dupla(c, x, f, walk=0, flip=False, expr='sorriso', look_l=.75, look_v=.75):
    """vó (à esquerda) e Lipe (à direita) de mãos dadas, Lipe com o cachecol."""
    pessoa(c, x, 1720, ADU, f, VOC, seed=6, walk=walk, flip=flip, expr=expr, look=look_v)
    lx = x + 280
    pessoa(c, lx, 1740, KID, f, LIPE, seed=2, walk=walk, flip=flip, expr=expr, look=look_l)
    cachecol_corpo(c, lx, 1740, KID, flip)
    d = ImageDraw.Draw(c)
    hy = 1740 - .27 * KID
    d.ellipse((x + 140 - 30, hy - 30, x + 140 + 30, hy + 30), fill=hexc(LIPE['pele']) + (255,), outline=INK + (255,), width=6)


def s17(f):
    ca = wt(17, 'cachecol') - 3
    c = rua_loja(f)
    x = lerp(PORTA_X - 200, 450, smooth(ramp(f, 0, ca)))
    dupla(c, x, f, walk=1 if f < ca else 0, flip=True, look_l=-.75, look_v=-.75)
    if f < ca:
        return c, cam(lerp(1200, 800, smooth(ramp(f, 0, ca))), V(1300, 1200), zf(1.25, f, .0008), zf(1.05, f, .0008)), 'vivo'
    g = f - ca
    lx = x + 280
    return c, cam(lx, 1740 - .55 * KID, lerp(1.6, 2.6, easeOut(ramp(g, 0, 14))) * (1 + .001 * g), lerp(1.3, 2.0, easeOut(ramp(g, 0, 14))) * (1 + .001 * g)), 'vivo'


def s18(f):
    mu, le = wt(18, 'mudou') - 3, wt(18, 'lembrados') - 3; pl = wt(18, 'placa') - 3
    t = ramp(f, mu, mu + 14)
    placa = 'ESQUECIDOS' if t < .5 else 'LEMBRADOS'
    c = rua_loja(f, placa=placa, vira=abs(math.cos(math.pi * t)))
    if t > 0 and t < 1: faiscas(c, 1104, 640, f, 380, 8, 2.0)
    dupla(c, 760, f, look_l=.5, look_v=.5)
    if f >= le + 14:
        c = close_fab(c, f, 1040, 1250, expr='sorriso', look=0, s=V(.95, .95), dx=V(0, 300), **LIPE)
        cachecol_close(c, f, V(.95, .95), V(0, 300))
        return c, cam_close(f, 1.15, 1.0, le + 14), 'vivo'
    k = smooth(ramp(f, pl - 6, pl + 14))
    return c, cam(1104, lerp(V(1300, 1200), V(900, 900), k), lerp(1.15, 1.4, k) * (1 + .0008 * f), lerp(1.0, 1.2, k) * (1 + .0008 * f)), 'vivo'


def s19(f):
    c = rua_loja(f, 'tarde', placa='LEMBRADOS')
    dupla(c, 760, f, look_l=-.5, look_v=.5)
    return c, cam(1104, V(1200, 1150), zf(1.12, f, .0006), zf(1.0, f, .0006)), 'tarde'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19]


def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0 and f < CAPA:
        if HOR: capa_txt(im, ['NESTA CIDADE, O QUE', 'VOCÊ PARA DE *AMAR*', 'VAI PRA UMA *LOJA*'], size=104, y=200)
        else: capa_txt(im, ['NESTA CIDADE, O QUE', 'VOCÊ PARA DE *AMAR*', 'VAI PRA UMA *LOJA*'], size=96)
    elif si == 3:
        su = wt(3, 'sumiu') - 3
        if f < wt(3, 'foi') - 3: selo_txt(im, 'SUMIU!', V(540, 960), V(330, 140), ramp(f, su, su + 8), V(80, 76))
    elif si == 12:
        tr = wt(12, 'tres') - 3
        selo_txt(im, '3 ANIVERSÁRIOS', V(540, 1400), V(330, 160), ramp(f, tr, tr + 8), V(72, 68), cor=(77, 121, 179))
    elif si == 13:
        selo_txt(im, 'LEMBRANÇA', V(540, 960), V(300, 130), ramp(f, 0, 8), V(64, 60), cor=(214, 150, 40))
    elif si == 19:
        e2, vi = wt(19, 'esquece', 1) - 3, wt(19, 'visite') - 3
        if HOR:
            moral_txt(im, ['NINGUÉM ESQUECE DE QUEM AMA DE UMA VEZ.'] + (['ESQUECE AOS *POUQUINHOS*.'] if f >= e2 else []) + (['*VISITE* ENQUANTO DÁ.'] if f >= vi else []), ramp(f, 0, 8))
        else:
            moral_txt(im, ['NINGUÉM ESQUECE', 'DE QUEM AMA', 'DE UMA VEZ.'] + (['ESQUECE AOS', '*POUQUINHOS*.'] if f >= e2 else []) + (['*VISITE*', 'ENQUANTO DÁ.'] if f >= vi else []), ramp(f, 0, 8))
    return im.convert('RGB')
