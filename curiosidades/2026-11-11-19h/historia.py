"""Formato DESENHO: Baarle, a cidade onde a fronteira passa no meio das casas (Curiosidades da IA, 11/11/2026, 19h).
Categoria: LUGARES E GEOGRAFIA.
Fatos: Wanderlust ("The town that straddles Belgium and the Netherlands"): 22 enclaves belgas dentro dos Países Baixos e 7
contraenclaves holandeses dentro deles; a linha é marcada no chão com cruzes brancas/pinos e passa por ruas, estacionamentos
e prédios; uma loja fica em cima da fronteira; a porta da frente define o município (e o país) da casa; donos já mudaram a
porta de lugar; as fronteiras vêm de acordos medievais de terras entre os senhores de Breda e de Brabante.
Focus on Belgium ("Beer in Belgium, toilet in the Netherlands"): "a localização da porta da frente determina a nacionalidade
da casa"; em 1198 o duque de Brabante cedeu parte de Baarle ao senhor de Breda; café com o balcão cortado pela fronteira.
Como as contagens variam entre fontes, a narração diz "uns vinte pedacinhos"."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10d', '2026-11-08-10h')
pessoa = _h10.pessoa
kit.pessoa = pessoa
import art as _art; _art.pessoa = pessoa


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


LINES = [
    "Tem uma cidade onde a fronteira entre dois países passa no meio das casas.",
    "É Baarle, na Europa: uns vinte pedacinhos da Bélgica espalhados no meio da Holanda.",
    "E dentro desses pedacinhos... ainda tem pedacinhos da Holanda.",
    "A linha da fronteira é marcada no chão: atravessa rua, loja e até café.",
    "Você vê, isso vem de acordos de terras de mais de oitocentos anos, entre os senhores da região.",
    "E pra saber de que país é cada casa, vale onde fica a porta da frente.",
    "Ou seja: tem casa que já trocou de país... só mudando a porta de lugar.",
]
CAPTXT = [
    "Tem uma cidade onde a fronteira entre dois países|passa no meio das casas.",
    "É Baarle, na Europa: uns vinte pedacinhos da Bélgica|espalhados no meio da Holanda.",
    "E dentro desses pedacinhos...|ainda tem pedacinhos da Holanda.",
    "A linha da fronteira é marcada no chão:|atravessa rua, loja e até café.",
    "Você vê, isso vem de acordos de terras de mais de 800 anos,|entre os senhores da região.",
    "E pra saber de que país é cada casa,|vale onde fica a porta da frente.",
    "Ou seja: tem casa que já trocou de país...|só mudando a porta de lugar.",
]
FALA_TIKTOK = "Você moraria lá? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'casas', 4), (1, 'belgica', 4), (1, 'holanda', 6), (2, 'holanda', 6), (3, 'chao', 4), (3, 'cafe', 6),
         (4, 'oitocentos', 4), (5, 'porta', 4), (6, 'pais', 4), (6, 'porta', 6)]

# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 cidade (rua com casa cortada pela linha da fronteira) | s1 mapa (manchas da Bélgica no meio da Holanda)
# s2 mapa com zoom (manchinha da Holanda dentro da da Bélgica) | s3 cidade (linha de cruzes brancas passando pela rua,
# por uma loja e por um café) | s4 mapa dourado (pergaminho antigo com acordo de terras, 800 anos)
# s5 cidade ao entardecer (casa com a porta: bandeira muda conforme a porta) | s6 cidade ao entardecer (pessoa leva a porta)

BEL = [(30, 30, 34), (250, 210, 40), (220, 40, 50)]
NED = [(200, 40, 50), (250, 250, 250), (40, 70, 160)]


def bandeira(c, x, y, w, kind, s=1.0):
    if s <= 0 or w * s < 8: return
    w = w * s; h = w * .66
    d = ImageDraw.Draw(c)
    cols = BEL if kind == 'bel' else NED
    for i, col in enumerate(cols):
        if kind == 'bel': d.rectangle((x - w / 2 + i * w / 3, y - h / 2, x - w / 2 + (i + 1) * w / 3, y + h / 2), fill=col + (255,))
        else: d.rectangle((x - w / 2, y - h / 2 + i * h / 3, x + w / 2, y - h / 2 + (i + 1) * h / 3), fill=col + (255,))
    d.rectangle((x - w / 2, y - h / 2, x + w / 2, y + h / 2), outline=(36, 23, 38, 255), width=5)


@lru_cache(maxsize=8)
def casa_img(door=0.3, kind='', w=760):
    """casa de tijolinho (760x760) com porta em x=door (0..1 da largura)."""
    p = Pen(760, 760)
    p.shape([(40, 260), (720, 260), (720, 740), (40, 740)], hexc('#c96b4a'), hexc('#9a4e33'), 6, 14)
    p.shape([(10, 270), (380, 40), (750, 270)], hexc('#6b4a3a'), hexc('#4e352a'), 6, 10)
    for x in (100, 520):
        p.shape([(x, 330), (x + 150, 330), (x + 150, 470), (x, 470)], hexc('#cfe6f7'), hexc('#a9c9e0'), 5, 6)
        p.stroke([(x + 75, 330), (x + 75, 470)], 4); p.stroke([(x, 400), (x + 150, 400)], 4)
    dx = 40 + door * 680
    p.shape([(dx - 70, 520), (dx + 70, 520), (dx + 70, 740), (dx - 70, 740)], hexc('#3d5a8a'), hexc('#2c4266'), 5, 8)
    p.dot(dx + 45, 640, 9, hexc('#f2c84a'), 3)
    return p.img.resize((w, w), Image.LANCZOS)


def casa(c, x, feet, w, door=0.3):
    im = casa_img(round(door * 20) / 20, '', int(w))
    c.alpha_composite(im, (int(x - w / 2), int(feet - w)))
    return x - w / 2 + (40 + door * 680) * w / 760


def linha_fronteira(c, x0, y0, x1, y1, a=1.0, n=12):
    """linha de cruzes brancas no chão."""
    if a <= 0: return
    d = ImageDraw.Draw(c)
    for i in range(int(n * a) + 1):
        t = i / n
        x, y = lerp(x0, x1, t), lerp(y0, y1, t)
        r = 22
        d.line((x - r, y - r, x + r, y + r), fill=(250, 250, 250, 255), width=12)
        d.line((x - r, y + r, x + r, y - r), fill=(250, 250, 250, 255), width=12)


def linha_vertical(c, x, y0, y1, a=1.0):
    if a <= 0: return
    d = ImageDraw.Draw(c)
    y = y0
    while y < lerp(y0, y1, a):
        d.line((x, y, x, min(y + 40, y1)), fill=(250, 250, 250, 255), width=14)
        d.line((x, y, x, min(y + 40, y1)), fill=(36, 23, 38, 120), width=2)
        y += 70


@lru_cache(maxsize=4)
def mapa_baarle(luz='day'):
    im = CEN('mapa', luz).copy()
    p = Pen(1242, 2208)
    p.shape(ell_pts(621, 1150, 560, 620, 60, .2), hexc('#f0a050'), hexc('#d08030'), 6, 16)  # Holanda (laranja)
    rnd = random.Random(4)
    for i in range(14):
        cx, cy = 621 + rnd.uniform(-380, 380), 1150 + rnd.uniform(-420, 420)
        r = rnd.uniform(45, 95)
        p.shape(ell_pts(cx, cy, r, r * .8, 30, rnd.uniform(0, 3)), hexc('#f7dc5a'), hexc('#d8bc3a'), 5, 6)  # Bélgica
    p.shape(ell_pts(621, 1150, 170, 140, 40, .4), hexc('#f7dc5a'), hexc('#d8bc3a'), 5, 8)
    im.alpha_composite(p.img.resize((1242, 2208), Image.LANCZOS))
    return im


def ponto_holanda(c, s):
    if s <= 0.02: return
    d = ImageDraw.Draw(c)
    for (x, y, r) in ((590, 1130, 50), (680, 1190, 32)):
        r = r * s
        d.ellipse((x - r, y - r * .8, x + r, y + r * .8), fill=(240, 160, 80, 255), outline=(36, 23, 38, 255), width=5)


@lru_cache(maxsize=2)
def pergaminho(w=620):
    p = Pen(620, 760)
    p.shape([(60, 60), (560, 60), (560, 700), (60, 700)], hexc('#f1e0b0'), hexc('#d6c08a'), 6, 14)
    for y in (60, 700): p.shape(ell_pts(310, y, 290, 34, 30), hexc('#e3cc90'), hexc('#c4ab70'), 5, 6)
    for y in range(160, 520, 60): p.stroke([(120, y), (500 - (y % 120), y)], 6, hexc('#8a6a4a'))
    p.shape(ell_pts(420, 600, 60, 60, 30), hexc('#c0392b'), hexc('#922b21'), 5, 6)
    return p.img.resize((w, int(w * 760 / 620)), Image.LANCZOS)


def SFX(s):
    s.ting(s.W(0, 'casas'), .3)
    s.thunk(s.W(1, 'belgica') - 2, 260, .5)
    for i in range(5): s.thunk(s.W(1, 'espalhados') + i * 4, 300, .3)
    s.ting(s.W(2, 'holanda'), .3)
    s.whoosh(s.W(3, 'chao') - 4, .4, .4)
    for w in ('rua', 'loja', 'cafe'): s.thunk(s.W(3, w) - 2, 260, .4)
    s.thunk(s.W(4, 'oitocentos') - 2, 160, .6)
    s.thunk(s.W(5, 'porta') - 2, 220, .6)
    s.whoosh(s.W(6, 'mudando') - 4, .5, .5); s.trill(s.W(6, 'lugar'), 1.0, .3)


def s0(f):
    c = CEN('cidade', 'day').copy()
    casa(c, 621, 1560, 820, .3)
    k = wt(0, 'fronteira') - 3
    linha_vertical(c, 640, 760, 2208, ramp(f, k, k + 14))
    if f >= k:
        bandeira(c, 420, 640, 180, 'bel', back(ramp(f, k + 6, k + 14)))
        bandeira(c, 850, 640, 180, 'ned', back(ramp(f, k + 9, k + 17)))
    ca = wt(0, 'casas') - 3
    if f >= ca: paste_c(c, txt('NO MEIO!', 100, -6), 640, 520, back(ramp(f, ca, ca + 8)))
    z = lerp(1.35, 1.05, easeOut(ramp(f, 0, 50))) * (1 + .0009 * f)
    return c, (621, lerp(1150, 1250, easeOut(ramp(f, 0, 50))), z, 0), 'day'


def s1(f):
    c = mapa_baarle('day').copy()
    b = wt(1, 'belgica') - 3
    h = wt(1, 'holanda') - 3
    ba = wt(1, 'baarle') - 3
    if f >= ba: paste_c(c, txt('BAARLE', 100, -4), 621, 1150, back(ramp(f, ba, ba + 8)))
    if f >= b:
        bandeira(c, 300, 520, 170, 'bel', back(ramp(f, b, b + 8)))
        paste_c(c, txt('BÉLGICA', 64, 0), 300, 660, back(ramp(f, b, b + 8)))
        ImageDraw.Draw(c).ellipse((90, 630, 140, 690), fill=(247, 220, 90, 255), outline=(36, 23, 38, 255), width=5)
    if f >= h:
        bandeira(c, 940, 520, 170, 'ned', back(ramp(f, h, h + 8)))
        paste_c(c, txt('HOLANDA', 64, 0), 940, 660, back(ramp(f, h, h + 8)))
        ImageDraw.Draw(c).ellipse((1100, 630, 1150, 690), fill=(240, 160, 80, 255), outline=(36, 23, 38, 255), width=5)
    z = lerp(1.05, .95, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    return c, (621, 1250, z, 0), 'day'


def s2(f):
    c = mapa_baarle('day').copy()
    h = wt(2, 'holanda') - 3
    ponto_holanda(c, back(ramp(f, h, h + 8)))
    if f >= h: paste_c(c, txt('DE NOVO?!', 64, 6), 621, 960, back(ramp(f, h, h + 8)))
    t = smooth(ramp(f, 0, 50))
    z = lerp(1.0, 2.3, t) * (1 + .0009 * f)
    return c, (621, lerp(1250, 1100, t), z, 0), 'day'


def s3(f):
    c = CEN('cidade', 'day').copy()
    ch = wt(3, 'chao') - 3
    linha_fronteira(c, 100, 2150, 1150, 1360, ramp(f, ch, ch + 20), 14)
    labels = [('rua', 'RUA', 300, 1640), ('loja', 'LOJA', 700, 820), ('cafe', 'CAFÉ', 1000, 960)]
    for w, t_, x, y in labels:
        k = wt(3, w) - 3
        if f >= k: paste_c(c, txt(t_ + '!', 90, -5), x, y, back(ramp(f, k, k + 8)))
    put_pessoa(c, 560, 1900, 760, f, 2, shirt='#2fa38a', pants='#3b3f4a', pocket=False, skin=1, hair='#3b2a1e',
               expr='grin' if f >= ch else 'neutral', arms='point' if f >= ch else 'hang', look=-1)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 150))) * (1 + .0009 * f)
    return c, (lerp(560, 700, smooth(ramp(f, 0, 150))), 1350, z, 0), 'day'


def s4(f):
    c = mapa_baarle('golden').copy()
    o = wt(4, 'oitocentos') - 3
    se = wt(4, 'senhores') - 3
    paste_c(c, pergaminho(560), 621, 1150, back(ramp(f, 0, 10)))
    if f >= o: paste_c(c, txt('800 ANOS', 120, -6), 621, 560, back(ramp(f, o, o + 8)))
    if f >= se:
        for i, (x, sd, col) in enumerate(((260, 3, '#8e44ad'), (980, 4, '#2e86c1'))):
            put_pessoa(c, x, 1900, 760 * back(ramp(f, se + i * 4, se + i * 4 + 9)), f, sd, shirt=col, pants='#3b3f4a',
                       pocket=False, skin=i + 1, hair='#5a3a2a', expr='smug', arms='point', look=1 if i == 0 else -1)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 140))) * (1 + .0009 * f)
    return c, (621, 1300, z, 0), 'golden'


def s5(f):
    c = CEN('cidade', 'dusk').copy()
    po = wt(5, 'porta') - 3
    dx = casa(c, 621, 1560, 820, .3)
    linha_vertical(c, 700, 760, 2208)
    bandeira(c, 420, 640, 160, 'bel'); bandeira(c, 900, 640, 160, 'ned')
    if f >= po:
        d = ImageDraw.Draw(c)
        a = back(ramp(f, po, po + 8))
        r = max(2, 150 * a)
        d.ellipse((dx - r, 1460 - r * 1.2, dx + r, 1460 + r * 1.2), outline=(255, 230, 80, 255), width=12)
        paste_c(c, txt('A PORTA!', 100, -6), dx + 80, 1150, a)
    t = smooth(ramp(f, po - 20, po + 10))
    z = lerp(1.05, 1.5, t) * (1 + .0009 * f)
    return c, (lerp(621, dx + 60, t), lerp(1250, 1300, t), z, 0), 'dusk'


def s6(f):
    c = CEN('cidade', 'dusk').copy()
    m = wt(6, 'mudando') - 3
    lu = wt(6, 'lugar') - 3
    door = lerp(.3, .72, smooth(ramp(f, m, lu + 6)))
    dx = casa(c, 621, 1560, 820, door)
    linha_vertical(c, 700, 760, 2208)
    side_ned = door * 680 + 40 > (700 - 621 + 410) * 760 / 820
    bandeira(c, 621, 640, 200, 'ned' if side_ned else 'bel', 1 + .1 * math.sin(f * .3) if f > lu else 1)
    p = wt(6, 'pais') - 3
    if f >= p: paste_c(c, txt('TROCOU!', 100, 6), 621, 480, back(ramp(f, p, p + 8)))
    put_pessoa(c, dx + 190, 1900, 700, f, 5, shirt='#f28c28', pants='#3b3f4a', pocket=False, skin=0, hair='#d8b25a',
               expr='smug' if f >= lu else 'grin', arms='up' if m <= f < lu + 6 else 'shrug', look=1)
    z = lerp(1.05, 1.2, smooth(ramp(f, 0, 90))) * (1 + .0012 * f)
    return c, (621, 1250, z, lerp(0, 2, smooth(ramp(f, 0, 90)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
