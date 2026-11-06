"""Cenários prontos do formato DESENHO (mesmo estilo: cores chapadas, contorno ameixa, sombra em 2 tons).

Use em historia.py:   c = CEN('cozinha').copy()      (ou CEN('praia', 'golden'))
Todos têm 1242x2208 (o palco). O chão fica em y≈1500-1650, então personagens com pés em y≈1950-2120
ficam em pé no chão, como no laboratório. 'luz' muda o céu/janela: 'day', 'golden' ou 'dusk'.

REGRA: o cenário tem que ser o lugar onde a história acontece. O pasto (BG('day')) é só para
histórias de campo/fazenda/bichos do campo. Lista em NOMES; se nenhum servir, desenhe um novo no historia.py.
"""
import math, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw
from art import Pen, INK, ell_pts, curve, hexc, mul

W, H = 1242, 2208
CEUS = {'day': ('#3f86dc', '#cfe6f7'), 'golden': ('#6474c0', '#ffc485'), 'dusk': ('#18234f', '#d18a7c')}

NOMES = {
    'quarto': 'quarto com cama, janela e quadro',
    'sala': 'sala de casa com sofá, TV e tapete',
    'cozinha': 'cozinha com azulejo, fogão, geladeira e balcão',
    'banheiro': 'banheiro com azulejo, pia, espelho e banheira',
    'escola': 'sala de aula com lousa e carteiras',
    'escritorio': 'escritório com mesa, computador e janela com prédios',
    'cidade': 'rua de cidade com prédios, calçada e asfalto',
    'praia': 'praia com mar, areia e guarda-sol',
    'fundo_mar': 'fundo do mar com raios de luz, algas e areia',
    'floresta': 'floresta fechada com árvores grandes',
    'deserto': 'deserto com dunas e sol forte',
    'neve': 'montanhas geladas e chão de neve',
    'montanha': 'montanhas altas com vale',
    'espaco': 'espaço com estrelas e planeta',
    'estacao': 'dentro de uma estação espacial',
    'corpo': 'dentro do corpo (tons de rosa)',
    'antiga': 'cidade antiga com colunas e arcos (Roma/Grécia)',
    'museu': 'museu com quadros e pedestal',
    'mapa': 'mapa: mar com um continente',
    'fabrica': 'fábrica por dentro com esteira e máquinas',
    'lab': 'laboratório (já existia: BG("lab"))',
    'pasto': 'campo/fazenda (já existia: BG("day"))',
}


def _grad(top, bot, h=H, w=W):
    y = np.linspace(0, 1, h)[:, None, None]
    a = np.array(hexc(top)) * (1 - y) + np.array(hexc(bot)) * y
    return Image.fromarray(np.broadcast_to(a, (h, w, 3)).astype(np.uint8)).convert('RGBA')


def _ceu(luz, hz):
    t, b = CEUS.get(luz, CEUS['day'])
    im = Image.new('RGBA', (W, H), hexc(b) + (255,))
    im.paste(_grad(t, b, hz), (0, 0))
    return im


def _done(base, p):
    base.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    return base


def _janela(p, x0, y0, x1, y1, luz='day', predios=False, cruz=True):
    t, b = CEUS.get(luz, CEUS['day'])
    p.shape([(x0 - 22, y0 - 22), (x1 + 22, y0 - 22), (x1 + 22, y1 + 22), (x0 - 22, y1 + 22)], hexc('#f7f7f2'), hexc('#d9d9d0'), 6, 6)
    p.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], hexc(b))
    p.poly([(x0, y0), (x1, y0), (x1, (y0 + y1) / 2), (x0, (y0 + y1) / 2)], hexc(t))
    if predios:
        rnd = random.Random(x0)
        x = x0
        while x < x1:
            w = rnd.randint(50, 90); h = rnd.randint(80, int((y1 - y0) * .7))
            p.poly([(x, y1 - h), (min(x1, x + w), y1 - h), (min(x1, x + w), y1), (x, y1)], hexc('#8e9bb3') if luz == 'day' else hexc('#5a6385'))
            x += w + 6
    if cruz:
        p.stroke([((x0 + x1) / 2, y0), ((x0 + x1) / 2, y1)], 12, hexc('#f7f7f2'))
        p.stroke([(x0, (y0 + y1) / 2), (x1, (y0 + y1) / 2)], 12, hexc('#f7f7f2'))
    p.stroke([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], 5)


def _piso_madeira(p, fy, col='#b48a5a', lin='#9a7347'):
    p.poly([(0, fy), (W, fy), (W, H), (0, H)], hexc(col))
    for y in range(fy + 70, H, 110): p.stroke([(0, y), (W, y)], 4, hexc(lin))
    rnd = random.Random(fy)
    for y in range(fy, H, 110):
        for _ in range(3):
            x = rnd.randint(0, W); p.stroke([(x, y), (x, y + 110)], 3, hexc(lin))
    p.stroke([(0, fy), (W, fy)], 8)


def _piso_azulejo(p, fy, a='#e6e2d8', b='#d2cdbf'):
    for yy in range(fy, H, 100):
        k = (yy - fy) // 100
        for xx in range(0, W, 150):
            p.poly([(xx, yy), (xx + 150, yy), (xx + 150, yy + 100), (xx, yy + 100)], hexc(a) if (xx // 150 + k) % 2 else hexc(b))
    p.stroke([(0, fy), (W, fy)], 8)


def _parede(p, fy, col, listra=None):
    p.poly([(0, 0), (W, 0), (W, fy), (0, fy)], hexc(col))
    if listra:
        for x in range(0, W, 90): p.stroke([(x, 0), (x, fy)], 4, hexc(listra))


def _nuvens(p, seed, y0=150, y1=700, n=4, col=(255, 255, 255)):
    rnd = random.Random(seed)
    for i in range(n):
        cx, cy = rnd.randint(0, W), rnd.randint(y0, y1)
        for dx, dy, r in ((-70, 10, 55), (0, -15, 75), (75, 8, 55), (0, 25, 60)):
            p.dot(cx + dx, cy + dy, r + 5, INK)
        for dx, dy, r in ((-70, 10, 55), (0, -15, 75), (75, 8, 55), (0, 25, 60)):
            p.dot(cx + dx, cy + dy, r, col)


def _sol(p, x, y, r=90):
    for i in range(12):
        a = i * math.pi / 6
        p.line([(x + (r + 20) * math.cos(a), y + (r + 20) * math.sin(a)), (x + (r + 70) * math.cos(a), y + (r + 70) * math.sin(a))], hexc('#ffd84a'), 12, 4)
    p.shape(ell_pts(x, y, r, r, 48), hexc('#ffe27a'), hexc('#f5b83a'), 6, 14)


# ------------------------------------------------------------------ interiores
def quarto(luz='day'):
    fy = 1560; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#f3e3c3', '#ead5ae')
    _janela(p, 790, 380, 1130, 760, luz)
    p.shape([(140, 420), (420, 420), (420, 640), (140, 640)], hexc('#8a5a3a'), None, 6)
    p.poly([(165, 445), (395, 445), (395, 615), (165, 615)], hexc('#8fd6a0'))
    p.poly([(165, 615), (260, 520), (330, 580), (395, 500), (395, 615)], hexc('#4c9a5c'))
    _piso_madeira(p, fy)
    # cama ao fundo, à esquerda
    p.shape([(40, 1180), (110, 1180), (110, 1600), (40, 1600)], hexc('#8a5f35'), hexc('#65452a'), 5, 6)
    p.shape([(60, 1380), (560, 1380), (560, 1560), (60, 1560)], hexc('#7fa6d9'), hexc('#5b80b3'), 6, 12)
    p.shape([(90, 1320), (260, 1320), (260, 1390), (90, 1390)], (255, 255, 255), hexc('#dcdcdc'), 5, 6)
    return _done(base, p)


def sala(luz='day'):
    fy = 1560; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#d9e7d3', '#cbdcc3')
    _janela(p, 120, 380, 460, 760, luz)
    p.shape([(700, 520), (1160, 520), (1160, 800), (700, 800)], hexc('#2b2b30'), None, 6)  # TV
    p.poly([(725, 545), (1135, 545), (1135, 775), (725, 775)], hexc('#3b4a6b'))
    p.shape([(880, 800), (980, 800), (1000, 860), (860, 860)], hexc('#2b2b30'), None, 4)
    p.shape([(640, 1200), (1200, 1200), (1200, 1520), (640, 1520)], hexc('#c96b4a'), hexc('#9a4e33'), 6, 14)  # sofá
    p.shape([(600, 1260), (680, 1260), (680, 1540), (600, 1540)], hexc('#b85d3e'), None, 5)
    _piso_madeira(p, fy, '#c49a68', '#a77f50')
    p.shape(ell_pts(620, 1880, 520, 150, 48), hexc('#e9c46a'), hexc('#c9a24a'), 5, 10)  # tapete
    return _done(base, p)


def cozinha(luz='day'):
    fy = 1600; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#fbf3e4')
    for y in range(900, 1320, 70):  # azulejos atrás do balcão
        for x in range(0, W, 90): p.poly([(x + 3, y + 3), (x + 87, y + 3), (x + 87, y + 67), (x + 3, y + 67)], hexc('#cfe8ef'))
    _janela(p, 470, 380, 780, 700, luz)
    p.shape([(60, 260), (420, 260), (420, 620), (60, 620)], hexc('#e9a35a'), hexc('#c9813a'), 6, 10)  # armário
    p.shape([(850, 260), (1180, 260), (1180, 620), (850, 620)], hexc('#e9a35a'), hexc('#c9813a'), 6, 10)
    for x in (240, 1015): p.stroke([(x, 300), (x, 580)], 4)
    p.shape([(940, 700), (1200, 700), (1200, 1600), (940, 1600)], hexc('#e6edf2'), hexc('#c3ccd4'), 6, 14)  # geladeira
    p.stroke([(940, 1000), (1200, 1000)], 5); p.line([(970, 780), (970, 920)], hexc('#9aa1ad'), 10, 3); p.line([(970, 1060), (970, 1240)], hexc('#9aa1ad'), 10, 3)
    p.shape([(40, 1320), (920, 1320), (920, 1600), (40, 1600)], hexc('#c98a4a'), hexc('#9a6430'), 6, 12)  # balcão
    p.shape([(30, 1290), (930, 1290), (930, 1330), (30, 1330)], hexc('#8b8f99'), hexc('#6b6f78'), 5, 4)
    p.shape([(500, 1230), (820, 1230), (820, 1292), (500, 1292)], hexc('#3b3b40'), None, 5)  # fogão
    for x in (580, 740): p.shape(ell_pts(x, 1232, 60, 14, 24), hexc('#2a2a2e'), None, 4)
    for x in (120, 320): p.dot(x + 60, 1460, 10, hexc('#7a5230'), 3)
    _piso_azulejo(p, fy)
    return _done(base, p)


def banheiro(luz='day'):
    fy = 1600; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#e8f3f6')
    for y in range(0, fy, 120):
        for x in range(0, W, 120): p.poly([(x + 3, y + 3), (x + 117, y + 3), (x + 117, y + 117), (x + 3, y + 117)], hexc('#d6ebf0'))
    p.shape([(780, 420), (1100, 420), (1100, 860), (780, 860)], hexc('#cfe9f5'), hexc('#a9d2e6'), 6, 8)  # espelho
    p.stroke([(820, 480), (900, 400)], 8, (255, 255, 255))
    p.shape([(760, 1080), (1120, 1080), (1080, 1200), (800, 1200)], (255, 255, 255), hexc('#dcdcdc'), 6, 8)  # pia
    p.shape([(900, 1200), (980, 1200), (980, 1600), (900, 1600)], (255, 255, 255), hexc('#dcdcdc'), 5, 6)
    p.shape([(40, 1260), (620, 1260), (580, 1600), (80, 1600)], (255, 255, 255), hexc('#dcdcdc'), 6, 14)  # banheira
    p.line([(560, 1260), (560, 1150), (500, 1150)], hexc('#9aa1ad'), 14, 4)
    _piso_azulejo(p, fy, '#f2f2f2', '#dfe6ea')
    return _done(base, p)


def escola(luz='day'):
    fy = 1560; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#f2e1b8')
    p.shape([(120, 330), (1120, 330), (1120, 880), (120, 880)], hexc('#8a5f35'), None, 6)
    p.poly([(150, 360), (1090, 360), (1090, 850), (150, 850)], hexc('#2f5d4a'))
    for i in range(4): p.stroke([(200 + i * 40, 420 + i * 60), (520 + i * 30, 420 + i * 60)], 5, hexc('#cfe3da'))
    p.shape([(120, 880), (1120, 880), (1120, 910), (120, 910)], hexc('#a07a4a'), None, 4)
    for x in (140, 520, 900):  # carteiras ao fundo
        p.shape([(x, 1300), (x + 240, 1300), (x + 240, 1340), (x, 1340)], hexc('#c98a4a'), hexc('#9a6430'), 5, 4)
        for lx in (x + 20, x + 220): p.stroke([(lx, 1340), (lx, 1520)], 10, hexc('#6b6f78'))
    _piso_azulejo(p, fy, '#e3d6bf', '#d3c4a8')
    return _done(base, p)


def escritorio(luz='day'):
    fy = 1560; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#e6e9ee')
    _janela(p, 660, 300, 1160, 900, luz, predios=True)
    p.shape([(80, 1240), (640, 1240), (640, 1290), (80, 1290)], hexc('#8a6a52'), hexc('#6a4f3c'), 5, 6)
    for x in (110, 610): p.stroke([(x, 1290), (x, 1560)], 12, hexc('#6a4f3c'))
    p.shape([(200, 960), (520, 960), (520, 1180), (200, 1180)], hexc('#2b2b30'), None, 6)
    p.poly([(220, 980), (500, 980), (500, 1160), (220, 1160)], hexc('#8fc1ff'))
    p.shape([(330, 1180), (390, 1180), (410, 1240), (310, 1240)], hexc('#2b2b30'), None, 4)
    p.shape([(1000, 1360), (1140, 1360), (1120, 1560), (1020, 1560)], hexc('#c96b4a'), hexc('#9a4e33'), 5, 6)  # vaso
    for a in (-1.1, -.5, 0, .5, 1.1):
        p.shape(ell_pts(1070 + 90 * math.sin(a), 1260 - 60 * math.cos(a), 34, 80, 24, a), hexc('#5cae5e'), hexc('#3e8a42'), 4, 6)
    _piso_azulejo(p, fy, '#cfd3da', '#bfc4cc')
    return _done(base, p)


def fabrica(luz='day'):
    fy = 1580; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#c9cdd4')
    for x in range(0, W, 200): p.stroke([(x, 0), (x, fy)], 10, hexc('#b3b8c1'))
    for x in (140, 540, 940): _janela(p, x, 200, x + 220, 420, luz)
    p.shape([(60, 1250), (1180, 1250), (1180, 1330), (60, 1330)], hexc('#3b3b40'), None, 6)  # esteira
    for x in range(100, 1180, 90): p.dot(x, 1290, 22, hexc('#8b8f99'), 4)
    for x in (120, 1080): p.stroke([(x, 1330), (x, 1580)], 18, hexc('#6b6f78'))
    p.shape([(780, 760), (1100, 760), (1100, 1250), (780, 1250)], hexc('#f0b23a'), hexc('#c98d1e'), 6, 14)  # máquina
    p.dot(940, 900, 60, hexc('#e8423a'), 5); p.shape([(820, 1050), (1060, 1050), (1060, 1110), (820, 1110)], hexc('#3b3b40'), None, 4)
    _piso_azulejo(p, fy, '#9aa1ad', '#8b929e')
    return _done(base, p)


def museu(luz='day'):
    fy = 1560; p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    _parede(p, fy, '#7d2f3a')
    p.shape([(0, fy - 70), (W, fy - 70), (W, fy), (0, fy)], hexc('#5a1f28'), None, 5)
    for x0, y0, w, h, col in ((90, 420, 320, 400, '#8fd6a0'), (520, 360, 260, 300, '#9fd3ff'), (880, 420, 280, 360, '#ffd25e')):
        p.shape([(x0 - 26, y0 - 26), (x0 + w + 26, y0 - 26), (x0 + w + 26, y0 + h + 26), (x0 - 26, y0 + h + 26)], hexc('#d9b44a'), hexc('#b08a2a'), 6, 8)
        p.poly([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)], hexc(col))
        p.dot(x0 + w * .6, y0 + h * .4, min(w, h) * .18, mul(hexc(col), .7))
    p.shape([(500, 1150), (760, 1150), (760, 1560), (500, 1560)], hexc('#f2efe6'), hexc('#cfc9b8'), 6, 12)  # pedestal
    p.shape([(470, 1120), (790, 1120), (790, 1160), (470, 1160)], hexc('#f2efe6'), hexc('#cfc9b8'), 5, 4)
    _piso_madeira(p, fy, '#8a5f35', '#6b4a2a')
    return _done(base, p)


def estacao(luz='day'):
    p = Pen(W, H); base = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc('#d9dde3'))
    for y in range(0, H, 300):
        for x in range(0, W, 310):
            col = hexc('#e8ebef') if ((x // 310) + (y // 300)) % 2 else hexc('#cfd4db')
            p.shape([(x + 12, y + 12), (x + 298, y + 12), (x + 298, y + 288), (x + 12, y + 288)], col, mul(col, .9), 3, 8)
    for y in (560, 1620): p.line([(60, y), (1180, y)], hexc('#f0c24a'), 18, 5)
    p.shape(ell_pts(900, 980, 230, 230, 64), hexc('#9aa1ad'), hexc('#6f7683'), 6, 10)
    p.poly(ell_pts(900, 980, 185, 185, 64), hexc('#0e1433'))
    p.shape(ell_pts(920, 1030, 105, 105, 64), hexc('#3a86e0'), hexc('#2458a8'), 4, 12)
    p.shape(ell_pts(895, 995, 42, 28, 32, .4, .2), hexc('#5cc46f'), hexc('#3c9a50'), 3, 6)
    return _done(base, p)


def corpo(luz='day'):
    base = _grad('#ffd9dc', '#f7b3bd'); p = Pen(W, H); rnd = random.Random(3)
    for i in range(24):
        x, yy, r = rnd.randint(0, W), rnd.randint(0, H), rnd.randint(40, 120)
        p.shape(ell_pts(x, yy, r, r * .7, 32, rnd.random()), hexc('#fbc6cd'), None, 0)
    return _done(base, p)


# ------------------------------------------------------------------ exteriores
def cidade(luz='day'):
    hz = 1300; base = _ceu(luz, hz); p = Pen(W, H); rnd = random.Random(9)
    _nuvens(p, 2, 150, 500, 3, (255, 255, 255) if luz == 'day' else mul(hexc(CEUS[luz][1]), 1.05))
    x = -40
    cols = ['#e9a35a', '#8fb3d9', '#d97a6c', '#b9b0d9', '#9cc9a0', '#e6d38a']
    while x < W:
        w = rnd.randint(200, 300); h = rnd.randint(500, 900); col = hexc(rnd.choice(cols))
        p.shape([(x, hz - h), (x + w, hz - h), (x + w, hz + 40), (x, hz + 40)], col, mul(col, .82), 6, 14)
        for wy in range(hz - h + 50, hz - 40, 110):
            for wx in range(x + 30, x + w - 50, 80):
                p.poly([(wx, wy), (wx + 46, wy), (wx + 46, wy + 60), (wx, wy + 60)], hexc('#fff3b0') if luz == 'dusk' and rnd.random() < .5 else hexc('#cfe6f7'), 3)
        x += w + 10
    p.shape([(-20, hz + 40), (W + 20, hz + 40), (W + 20, hz + 260), (-20, hz + 260)], hexc('#c9c4bb'), hexc('#a8a297'), 6, 8)  # calçada
    for xx in range(0, W, 160): p.stroke([(xx, hz + 40), (xx - 40, hz + 260)], 3, hexc('#a8a297'))
    p.poly([(0, hz + 260), (W, hz + 260), (W, H), (0, H)], hexc('#5b5b62'))
    for xx in range(0, W, 220): p.poly([(xx, 1950), (xx + 120, 1950), (xx + 120, 1972), (xx, 1972)], hexc('#f2f2f2'))
    p.stroke([(0, hz + 260), (W, hz + 260)], 7)
    p.line([(1100, hz + 60), (1100, hz - 380)], hexc('#5b5b62'), 14, 4); p.dot(1060, hz - 380, 26, hexc('#fff3b0'), 5)
    return _done(base, p)


def praia(luz='day'):
    hz = 1100; base = _ceu(luz, hz); p = Pen(W, H)
    _nuvens(p, 4, 150, 450, 3, (255, 255, 255) if luz == 'day' else mul(hexc(CEUS[luz][1]), 1.05))
    _sol(p, 980, 330, 80)
    p.poly([(0, hz), (W, hz), (W, 1560), (0, 1560)], hexc('#2f8fcf'))
    for y in range(hz + 60, 1540, 90):
        for x in range((y // 90) % 2 * 120, W, 240): p.arc(x + 60, y, 50, 14, 200, 340, 5, hexc('#8fd0f5'))
    p.stroke([(0, hz), (W, hz)], 6)
    pts = [(-20, 1560)] + [(x, 1540 + 30 * math.sin(x / 110)) for x in range(0, W + 60, 60)] + [(W + 20, H), (-20, H)]
    p.shape(pts, hexc('#f2d79a'), hexc('#d9b874'), 6, 14)
    p.line([(1000, 1980), (1000, 1360)], hexc('#8a5f35'), 14, 4)  # guarda-sol
    for i, col in enumerate(('#e8423a', '#ffffff', '#e8423a', '#ffffff')):
        a0, a1 = math.pi + i * math.pi / 4, math.pi + (i + 1) * math.pi / 4
        p.shape([(1000, 1360)] + [(1000 + 260 * math.cos(a), 1400 + 110 * math.sin(a)) for a in np.linspace(a0, a1, 8)], hexc(col), mul(hexc(col), .85), 5, 4)
    rnd = random.Random(2)
    for i in range(14): p.dot(rnd.randint(0, W), rnd.randint(1650, H), 6, hexc('#c9a865'))
    return _done(base, p)


def fundo_mar(luz='day'):
    base = _grad('#3fa0d8', '#0d3a66'); p = Pen(W, H); rnd = random.Random(6)
    for i in range(6):
        x = 100 + i * 210
        p.poly([(x, 0), (x + 90, 0), (x + 260, 1500), (x + 80, 1500)], hexc('#5fb6e3') if i % 2 else hexc('#4aa6d9'))
    pts = [(-20, 1700)] + [(x, 1660 + 40 * math.sin(x / 140)) for x in range(0, W + 60, 60)] + [(W + 20, H), (-20, H)]
    p.shape(pts, hexc('#e6cf94'), hexc('#c4ab6e'), 6, 16)
    for x in (80, 260, 980, 1160):
        top = rnd.randint(1050, 1300)
        p.line([(x + 30 * math.sin(y / 60), y) for y in range(top, 1720, 30)], hexc('#3fa35a'), 26, 5)
    for x, y, r in ((420, 1760, 60), (760, 1800, 46)): p.shape(ell_pts(x, y, r * 1.4, r, 24), hexc('#9b8f86'), hexc('#7a6f67'), 5, 8)
    for i in range(18):
        x, y, r = rnd.randint(0, W), rnd.randint(100, 1500), rnd.choice((8, 12, 16))
        p.dot(x, y, r + 4, INK); p.dot(x, y, r, hexc('#d8f1ff'))
    return _done(base, p)


def floresta(luz='day'):
    hz = 1350; base = _ceu(luz, hz); p = Pen(W, H); rnd = random.Random(12)
    for row, (y, s, col) in enumerate(((hz - 50, .8, '#4f8a4a'), (hz + 40, 1.0, '#3f7a3c'))):
        for i in range(9):
            x = i * 150 + rnd.randint(-40, 40) + row * 70
            p.shape([(x - 22 * s, y), (x + 22 * s, y), (x + 22 * s, y - 300 * s), (x - 22 * s, y - 300 * s)], hexc('#6b4a2f'), None, 5)
            for k in range(4):
                p.shape(ell_pts(x + rnd.randint(-60, 60) * s, y - (360 + rnd.randint(0, 200)) * s, 130 * s, 110 * s, 32), hexc(col), mul(hexc(col), .8), 5, 12)
    p.shape([(-20, hz + 30), (W + 20, hz + 30), (W + 20, H), (-20, H)], hexc('#6f9a4a'), hexc('#557a36'), 6, 12)
    for i in range(90):
        x, y = rnd.randint(0, W), rnd.randint(hz + 80, H)
        p.stroke([(x, y), (x + 6, y - 26)], 4, hexc('#4e7a32'))
    for x in (120, 1120):  # troncos grandes na frente
        p.shape([(x - 70, 300), (x + 70, 300), (x + 90, H), (x - 90, H)], hexc('#7a5536'), hexc('#5a3d24'), 7, 18)
    for x, y, r in ((60, 220, 260), (300, 120, 220), (640, 60, 240), (960, 120, 230), (1200, 220, 260)):
        p.shape(ell_pts(x, y, r, r * .75, 40), hexc('#3f7a3c'), hexc('#2f5f2c'), 6, 20)
    return _done(base, p)


def deserto(luz='day'):
    hz = 1150; base = _ceu(luz, hz); p = Pen(W, H)
    _sol(p, 950, 380, 110)
    for y0, col in ((hz, '#e9b96a'), (hz + 200, '#f0c77a'), (hz + 450, '#f5d38c')):
        pts = [(-20, H), (-20, y0 + 60)] + [(x, y0 + 80 * math.sin(x / 260 + y0)) for x in range(0, W + 60, 60)] + [(W + 20, H)]
        p.shape(pts, hexc(col), mul(hexc(col), .85), 6, 16)
    rnd = random.Random(1)
    for i in range(10): p.dot(rnd.randint(0, W), rnd.randint(1700, H), 8, hexc('#c9985a'))
    return _done(base, p)


def neve(luz='day'):
    hz = 1250; base = _ceu(luz, hz); p = Pen(W, H)
    for cx, h, w in ((250, 650, 420), (700, 820, 520), (1100, 600, 380)):
        p.shape([(cx - w, hz + 20), (cx, hz - h), (cx + w, hz + 20)], hexc('#8aa0b8'), hexc('#6b8098'), 6, 18)
        p.shape([(cx - w * .32, hz - h * .68), (cx, hz - h), (cx + w * .32, hz - h * .68), (cx + w * .12, hz - h * .6), (cx, hz - h * .7), (cx - w * .14, hz - h * .6)], (255, 255, 255), hexc('#dfe8f0'), 5, 6)
    pts = [(-20, H), (-20, hz + 40)] + [(x, hz + 40 + 30 * math.sin(x / 200)) for x in range(0, W + 60, 60)] + [(W + 20, H)]
    p.shape(pts, hexc('#f4f8fb'), hexc('#d3e0ea'), 6, 18)
    rnd = random.Random(8)
    for i in range(50):
        x, y = rnd.randint(0, W), rnd.randint(50, hz)
        p.dot(x, y, 6, (255, 255, 255))
    return _done(base, p)


def montanha(luz='day'):
    hz = 1350; base = _ceu(luz, hz); p = Pen(W, H)
    _nuvens(p, 7, 150, 450, 3, (255, 255, 255) if luz == 'day' else mul(hexc(CEUS[luz][1]), 1.05))
    for cx, h, w, col in ((200, 700, 460, '#7f8d5f'), (720, 950, 560, '#6d7f50'), (1150, 650, 400, '#8a9e6a')):
        p.shape([(cx - w, hz + 20), (cx, hz - h), (cx + w, hz + 20)], hexc(col), mul(hexc(col), .8), 6, 20)
        p.shape([(cx - w * .2, hz - h * .8), (cx, hz - h), (cx + w * .2, hz - h * .8), (cx, hz - h * .85)], (255, 255, 255), None, 4)
    p.shape([(-20, hz), (W + 20, hz), (W + 20, H), (-20, H)], hexc('#8fae6a'), hexc('#6f8f4e'), 6, 14)
    p.line([(560, H), (600, 1700), (700, 1500), (640, hz + 20)], hexc('#5fa8d8'), 40, 5)  # rio
    return _done(base, p)


def espaco(luz='day'):
    base = _grad('#0b1030', '#1d2a66'); p = Pen(W, H); rnd = random.Random(7)
    for i in range(170):
        p.dot(rnd.randint(0, W), rnd.randint(0, H), rnd.choice((2, 2, 3, 4)), (255, 255, 230))
    p.shape(ell_pts(1040, 1900, 360, 360, 64), hexc('#c96b4a'), hexc('#9a4e33'), 6, 30)
    for k in range(3): p.arc(1040, 1900, 520 + k * 30, 90 + k * 8, 180, 360, 8, hexc('#e9c46a'))
    p.shape(ell_pts(200, 400, 90, 90, 48), hexc('#9fd3ff'), hexc('#6aaedf'), 5, 12)
    return _done(base, p)


def antiga(luz='day'):
    fy = 1640; base = _ceu(luz, 520); p = Pen(W, H)
    p.shape([(0, 520), (W, 520), (W, fy), (0, fy)], hexc('#ecd3a6'), hexc('#cdb07c'), 6, 16)
    for x in (120, 520, 920):
        p.shape([(x, 760), (x + 200, 760), (x + 200, fy), (x, fy)], hexc('#b98b59'), None, 5)
        p.shape(ell_pts(x + 100, 760, 100, 100, 40), hexc('#b98b59'), None, 0)
    for x in (60, 460, 860, 1180):
        p.shape([(x - 34, 560), (x + 34, 560), (x + 34, fy), (x - 34, fy)], hexc('#f6ead2'), hexc('#d8c6a0'), 5, 10)
        p.shape([(x - 54, 520), (x + 54, 520), (x + 54, 566), (x - 54, 566)], hexc('#f6ead2'), hexc('#d8c6a0'), 5, 4)
    p.shape([(-20, 480), (W + 20, 480), (W + 20, 524), (-20, 524)], hexc('#c86b4a'), hexc('#9a4e33'), 5, 6)
    p.poly([(0, fy), (W, fy), (W, H), (0, H)], hexc('#c9b089'))
    for y in range(fy + 60, H, 100):
        for x in range((y // 100) % 2 * 90, W, 180): p.stroke([(x, y), (x + 150, y)], 3, hexc('#ab9470'))
    p.stroke([(0, fy), (W, fy)], 7)
    return _done(base, p)


def mapa(luz='day'):
    base = Image.new('RGBA', (W, H), hexc('#5fa8d8') + (255,)); p = Pen(W, H); rnd = random.Random(4)
    for i in range(30):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        p.stroke([(x, y), (x + 40, y - 6), (x + 80, y)], 4, hexc('#7cbde6'))
    pts = [(120, 520), (420, 380), (760, 400), (1120, 560), (1180, 900), (1060, 1300), (760, 1560), (420, 1600), (180, 1380), (90, 980)]
    sm = []
    for i in range(len(pts)):
        a, b, c = pts[i - 1], pts[i], pts[(i + 1) % len(pts)]
        sm += curve(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), b, ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2), 8)
    p.shape(sm, hexc('#9ccf6a'), hexc('#79a94c'), 7, 22)
    return _done(base, p)


@lru_cache(maxsize=48)
def cenario(nome, luz='day'):
    import art, personagens
    if nome == 'pasto': return art.background(luz)
    if nome == 'lab': return personagens.lab_bg()
    fn = globals().get(nome)
    if fn is None or nome not in NOMES: raise KeyError(f"cenário '{nome}' não existe. Opções: {', '.join(NOMES)}")
    return fn(luz).convert('RGBA')
