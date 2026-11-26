"""Cenários da história "A estação Girassol" (26/11/2026): vagão do metrô por dentro (porta fechada/aberta para o túnel,
a plataforma ou a estação de girassóis), plataforma comum, estação Girassol, girassol, banca de jornal na rua e mapa do metrô.
Palco 1242x2208; chão em y≈1560."""
from functools import lru_cache
from kit import *
import kit
from sombrio import *

AMA, AMAD, MIOLO = hexc('#f6c531'), hexc('#d9a21c'), hexc('#6b3f1f')


def _girassol(p, x, y, r, haste=0):
    if haste:
        p.stroke([(x, y), (x + 6, y + haste)], max(6, r * .18), hexc('#4f9a45'))
        p.shape(ell_pts(x + r * .9, y + haste * .55, r * .55, r * .22, 18, -.5), hexc('#5cae5e'), None, 3, 0)
    for k in range(12):
        a = k * math.pi / 6
        p.shape(ell_pts(x + math.cos(a) * r * .75, y + math.sin(a) * r * .75, r * .42, r * .17, 14, a), AMA, None, 3, 0)
    p.dot(x, y, r * .45, MIOLO, 3)


def ell_pts(cx, cy, rx, ry, n=18, a=0.0):
    ca, sa = math.cos(a), math.sin(a)
    return [(cx + rx * math.cos(t) * ca - ry * math.sin(t) * sa, cy + rx * math.cos(t) * sa + ry * math.sin(t) * ca)
            for t in [i * 2 * math.pi / n for i in range(n)]]


@lru_cache(maxsize=4)
def girassol_img(h=300):
    p = Pen(300, 560)
    _girassol(p, 150, 150, 120, 380)
    return p.img.resize((int(h * 300 / 560), h), Image.LANCZOS)


def _fora(p, x0, y0, x1, y1, fora, luz):
    """o que se vê pela porta/janela do vagão."""
    if fora == 'tunel':
        p.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], hexc('#23262e'))
        p.stroke([(x0, y0 + (y1 - y0) * .35), (x1, y0 + (y1 - y0) * .35)], 6, hexc('#3a3e48'))
    elif fora == 'plataforma':
        p.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], hexc('#e9e4d6'))
        for yy in range(int(y0) + 40, int(y1), 60): p.stroke([(x0, yy), (x1, yy)], 2, hexc('#cfc8b6'))
        p.poly([(x0, y0 + (y1 - y0) * .2), (x1, y0 + (y1 - y0) * .2), (x1, y0 + (y1 - y0) * .28), (x0, y0 + (y1 - y0) * .28)], hexc('#3f7fc4'))
    else:   # girassol
        p.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], hexc('#ffe58a'))
        rnd = random.Random(int(x0) + 3)
        for i in range(int((x1 - x0) * (y1 - y0) / 9000)):
            _girassol(p, rnd.uniform(x0 + 20, x1 - 20), rnd.uniform(y0 + 20, y1 - 20), rnd.uniform(28, 48))


@lru_cache(maxsize=16)
def vagao_bg(luz='tarde', fora='tunel', aberta=0.0):
    """vagão por dentro: janelas dos lados, porta dupla no meio (x 400..842, y 520..1560). aberta 0..1."""
    W, H = W_, H_
    p = Pen(W, H)
    par = {'dia': '#eef0ea', 'tarde': '#f3e2c4', 'noite': '#b9b8b0', 'frio': '#dfe5ea'}[luz]
    p.poly([(0, 0), (W, 0), (W, 1560), (0, 1560)], hexc(par))
    p.poly([(0, 0), (W, 0), (W, 160), (0, 160)], mul(hexc(par), .9))
    for x in (90, 300, 942, 1152):   # luzes do teto
        p.shape([(x - 70, 70), (x + 70, 70), (x + 70, 110), (x - 70, 110)], (255, 250, 230), None, 4, 0)
    # janelas
    for (a, b) in ((30, 340), (902, 1212)):
        p.shape([(a, 520), (b, 520), (b, 900), (a, 900)], hexc('#8a8f99'), None, 6, 0)
        _fora(p, a + 18, 538, b - 18, 882, 'girassol' if fora == 'girassol' else 'tunel', luz)
    # faixa
    p.poly([(0, 1000), (W, 1000), (W, 1040), (0, 1040)], hexc('#e0574a'))
    # porta
    x0, x1, y0, y1 = 400, 842, 520, 1560
    p.shape([(x0 - 20, y1), (x0 - 20, y0 - 20), (x1 + 20, y0 - 20), (x1 + 20, y1)], hexc('#9aa0aa'), None, 6, 0)
    _fora(p, x0, y0, x1, y1, fora, luz)
    m = (x0 + x1) / 2; ab = aberta * 205
    for (lo, hi) in ((x0, m - ab), (m + ab, x1)):
        if hi - lo < 8: continue
        p.shape([(lo, y1), (lo, y0), (hi, y0), (hi, y1)], hexc('#c7ccd4'), None, 5, 0)
        if hi - lo > 110:
            p.shape([(lo + 40, y0 + 60), (hi - 40, y0 + 60), (hi - 40, y0 + 460), (lo + 40, y0 + 460)],
                    hexc('#2c3038') if fora == 'tunel' else hexc('#9fb4c8'), None, 4, 0)
    # bancos
    for (a, b) in ((0, 360), (882, 1242)):
        p.shape([(a, 1300), (b, 1300), (b, 1420), (a, 1420)], hexc('#3f6fb0'), hexc('#335c94'), 6, 0)
        p.shape([(a, 1420), (b, 1420), (b, 1560), (a, 1560)], hexc('#6b7280'), None, 5, 0)
    for x in (370, 872): p.stroke([(x, 160), (x, 1560)], 16, hexc('#f0c531'))
    p.poly([(0, 1560), (W, 1560), (W, H), (0, H)], hexc('#8a8f99'))
    p.poly([(0, 1560), (W, 1560), (W, 1600), (0, 1600)], hexc('#6f7480'))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    if luz == 'noite':
        im.alpha_composite(Image.new('RGBA', (W, H), (10, 14, 30, 70)))
    return im


@lru_cache(maxsize=4)
def estacao_girassol_bg(luz='dia'):
    """a estação Girassol: plataforma velha tomada por girassóis, luz amarela, placa GIRASSOL. chão y≈1560."""
    W, H = W_, H_
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, 1560), (0, 1560)], hexc('#ffe9a6' if luz == 'dia' else '#f6cf8a'))
    for x in range(0, W, 120): p.stroke([(x, 0), (x, 1560)], 3, hexc('#efd48a'))
    p.shape([(300, 300), (942, 300), (942, 440), (300, 440)], hexc('#2f6c9e'), None, 6, 0)
    rnd = random.Random(5)
    for i in range(46):
        x = rnd.uniform(-20, W + 20); y = rnd.uniform(560, 1500)
        _girassol(p, x, y, rnd.uniform(40, 70), rnd.choice([0, 0, 160]))
    p.poly([(0, 1560), (W, 1560), (W, H), (0, H)], hexc('#c9b07a'))
    p.poly([(0, 1560), (W, 1560), (W, 1610), (0, 1610)], hexc('#f0c531'))
    for i in range(14):
        _girassol(p, rnd.uniform(0, W), rnd.uniform(1750, 2150), rnd.uniform(45, 70))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    d = ImageDraw.Draw(im); fnt = font(F_STAMP, 96); t = 'GIRASSOL'
    d.text((621 - d.textlength(t, font=fnt) / 2, 312), t, font=fnt, fill=(250, 246, 230))
    gl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse((200, -300, 1050, 700), fill=(255, 250, 200, 90))
    im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(60)))
    return im


@lru_cache(maxsize=4)
def plataforma_bg(luz='tarde'):
    """plataforma comum do metrô, azulejo, placa CENTRO, faixa amarela; chão y≈1560."""
    W, H = W_, H_
    p = Pen(W, H)
    par = {'dia': '#e9f0f2', 'tarde': '#f0e0c2', 'frio': '#d8e0e6'}[luz]
    p.poly([(0, 0), (W, 0), (W, 1560), (0, 1560)], hexc(par))
    for y in range(60, 1560, 80): p.stroke([(0, y), (W, y)], 2, mul(hexc(par), .92))
    p.poly([(0, 820), (W, 820), (W, 880), (0, 880)], hexc('#3f7fc4'))
    p.shape([(340, 420), (902, 420), (902, 560), (340, 560)], hexc('#2b3440'), None, 6, 0)
    p.shape([(80, 1200), (300, 1200), (300, 1260), (80, 1260)], hexc('#8a5a38'), None, 5, 0)   # banco
    for x in (100, 280): p.stroke([(x, 1260), (x, 1400)], 10, hexc('#555a62'))
    p.poly([(0, 1560), (W, 1560), (W, H), (0, H)], hexc('#9ea2a8'))
    p.poly([(0, 1560), (W, 1560), (W, 1600), (0, 1600)], hexc('#f0c531'))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    d = ImageDraw.Draw(im); fnt = font(F_STAMP, 90); t = 'CENTRO'
    d.text((621 - d.textlength(t, font=fnt) / 2, 432), t, font=fnt, fill=(240, 240, 230))
    return im


@lru_cache(maxsize=4)
def banca_img(w=620, luz='tarde'):
    p = Pen(620, 760)
    p.shape([(30, 750), (30, 200), (590, 200), (590, 750)], hexc('#3f8a5a'), hexc('#326f48'), 6, 0)
    p.shape([(0, 120), (620, 120), (600, 230), (20, 230)], hexc('#e8574a'), None, 6, 0)
    rnd = random.Random(2)
    for row in range(3):
        for k in range(5):
            col = rnd.choice(['#f6c531', '#4f8fd6', '#e8574a', '#f4f0e6', '#9a6ad6'])
            x = 70 + k * 100; y = 270 + row * 140
            p.shape([(x, y), (x + 80, y), (x + 80, y + 110), (x, y + 110)], hexc(col), None, 3, 0)
    return p.img.resize((w, int(w * 760 / 620)), Image.LANCZOS)


@lru_cache(maxsize=2)
def mapa_bg():
    """mapa do metrô numa parede: 3 linhas coloridas com estações (bolinhas)."""
    W, H = W_, H_
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc('#e9e4d6'))
    p.shape([(60, 420), (1182, 420), (1182, 1700), (60, 1700)], (252, 252, 248), None, 7, 0)
    linhas = [('#e0574a', [(140, 700), (420, 700), (620, 900), (900, 900), (1100, 1100)]),
              ('#3f7fc4', [(200, 1500), (420, 1300), (620, 900), (620, 600), (900, 520)]),
              ('#4fa86a', [(140, 1200), (400, 1100), (620, 1100), (850, 1350), (1100, 1450)])]
    for col, pts in linhas:
        p.line(pts, hexc(col), 26, 0)
        for (x, y) in pts: p.dot(x, y, 22, (255, 255, 255), 6)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    d = ImageDraw.Draw(im); fnt = font(F_B, 34)
    for t, (x, y) in (('CENTRO', (620, 900)), ('PRAÇA', (420, 700)), ('LAGO', (1100, 1100)), ('PORTO', (200, 1500)), ('FEIRA', (850, 1350))):
        d.text((x + 30, y - 52), t, font=fnt, fill=(40, 40, 50))
    return im
