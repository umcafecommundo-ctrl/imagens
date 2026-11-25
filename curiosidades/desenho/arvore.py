"""Cenários da história "A árvore dos bolinhos" (25/11/2026): floresta com a árvore enorme de portinha no tronco,
bolinho com vela/nome, e o lado de dentro da árvore. Palco 1242x2208."""
from functools import lru_cache
from kit import *
import kit
from sombrio import *

LUZ_CEN = {'dia': 'day', 'tarde': 'golden', 'noite': 'dusk', 'frio': 'day'}
TRONCO, TRONCOD = hexc('#7a5234'), hexc('#5e3e26')


@lru_cache(maxsize=8)
def arvore_img(flor=False, aberta=False, noite=False):
    """árvore enorme 1100x1700 (base do tronco em y=1680); portinha centrada em x=550, base y=1600, 170x260."""
    p = Pen(1100, 1700)
    folha = hexc('#3f8a46') if not noite else hexc('#2c5a3a')
    folhad = mul(folha, .8)
    for (cx, cy, r) in [(550, 420, 380), (260, 560, 260), (840, 560, 260), (400, 260, 240), (720, 250, 250), (550, 640, 280)]:
        p.shape(ell_pts(cx, cy, r, r * .85, 40), folha, folhad, 7, 16)
    # tronco largo com raízes
    p.shape([(300, 1690), (380, 1560), (400, 800), (440, 640), (660, 640), (700, 800), (720, 1560), (800, 1690)], TRONCO, TRONCOD, 7, 22)
    for k in range(5):
        y = 900 + k * 140
        p.arc(550 + (k % 2) * 60 - 30, y, 60, 18, 200, 340, 6, TRONCOD)
    # portinha
    porta = hexc('#3a2416') if aberta else hexc('#c0703a')
    pts = [(465, 1600), (465, 1440)] + [(550 - 85 * math.cos(a), 1440 - 85 * math.sin(a)) for a in [i * math.pi / 16 for i in range(17)]] + [(635, 1600)]
    p.shape(pts, porta, None, 7, 0)
    if aberta:
        p.poly([(465, 1600), (440, 1610), (440, 1440), (465, 1440)], hexc('#c0703a'))
    else:
        p.dot(612, 1530, 10, hexc('#e0c060'), 4)
        p.dot(550, 1440, 22, hexc('#f2d98a'), 5)
    if flor:
        rnd = random.Random(5)
        for i in range(70):
            a = rnd.random() * 2 * math.pi; r = rnd.random() ** .5
            cx = 550 + math.cos(a) * 520 * r; cy = 450 + math.sin(a) * 330 * r
            for k in range(5):
                b = k * 2 * math.pi / 5
                p.dot(cx + 14 * math.cos(b), cy + 14 * math.sin(b), 11, hexc('#f6a6c1'), 0)
            p.dot(cx, cy, 7, hexc('#f4d35e'), 0)
    return p.img.resize((1100, 1700), Image.LANCZOS)


@lru_cache(maxsize=12)
def floresta_arvore(luz='dia', flor=False, aberta=False):
    """floresta + árvore enorme no centro (portinha em x≈621, base y≈1830)."""
    c = CEN('floresta', LUZ_CEN[luz]).copy()
    c.alpha_composite(arvore_img(flor, aberta, luz == 'noite'), (621 - 550, 1830 - 1600))
    if luz == 'noite':
        c.alpha_composite(Image.new('RGBA', c.size, (10, 14, 40, 90)))
    return c


@lru_cache(maxsize=16)
def bolinho_img(vela=None, nome=None, cor='#7a4a2c'):
    """cupcake 400x520 (base y=500). vela: texto na vela-número ('100') ou None; nome: texto no papel."""
    p = Pen(400, 520)
    p.shape([(70, 300), (330, 300), (300, 500), (100, 500)], hexc('#e8655a'), hexc('#c24f46'), 6, 0)
    for x in range(110, 320, 45): p.stroke([(x, 310), (x - 8 + (x - 200) * .1, 490)], 4, hexc('#c24f46'))
    p.shape(ell_pts(200, 280, 150, 70, 30), hexc(cor), mul(hexc(cor), .8), 6, 10)
    p.shape(ell_pts(200, 235, 110, 60, 30), hexc(cor), mul(hexc(cor), .8), 6, 10)
    p.dot(200, 180, 26, hexc('#d8423a'), 5)
    im = p.img.resize((400, 520), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    if vela:
        fnt = font(F_STAMP, 120); tw = d.textlength(vela, font=fnt)
        d.text((200 - tw / 2, 20), vela, font=fnt, fill=(120, 190, 240), stroke_width=6, stroke_fill=(30, 26, 36))
        d.polygon([(200, 0), (186, 20), (200, 34), (214, 20)], fill=(255, 190, 60))
    if nome:
        fnt = font(F_STAMP, 52); tw = d.textlength(nome, font=fnt)
        d.text((200 - tw / 2, 380), nome, font=fnt, fill=(250, 240, 220), stroke_width=4, stroke_fill=(60, 30, 30))
    return im


def put_bolinho(c, x, base, h=200, s=1.0, **kw):
    if s <= .03: return
    hh = max(6, int(h * s))
    im = bolinho_img(**kw).resize((max(4, int(hh * 400 / 520)), hh), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height)))


@lru_cache(maxsize=4)
def dentro_arvore(luz='tarde'):
    """sala redonda dentro do tronco: paredes de madeira, fogãozinho, prateleira de forminhas, mesa com caderno."""
    W, H = W_, H_
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc('#8a5a38'))
    for x in range(-200, W + 200, 90):
        p.stroke([(x, 0), (x + 40 * math.sin(x * .01), H)], 5, hexc('#6f4529'))
    p.shape(ell_pts(621, 1000, 560, 800, 60), hexc('#a8754a'), None, 0, 0)
    for k in range(9):
        p.arc(621, 1000, 120 + k * 50, 80 + k * 70, 0, 360, 4, hexc('#93643d'))
    # prateleira com forminhas
    p.shape([(140, 700), (620, 700), (620, 730), (140, 730)], hexc('#5e3e26'), None, 5, 0)
    for k in range(6):
        x = 170 + k * 75
        p.shape([(x, 700), (x + 55, 700), (x + 45, 650), (x + 10, 650)], hexc('#e8655a'), None, 4, 0)
    # fogãozinho de ferro
    p.shape([(760, 1600), (760, 1180), (1100, 1180), (1100, 1600)], hexc('#3b4042'), hexc('#2c3032'), 6, 0)
    p.shape([(810, 1480), (810, 1300), (1050, 1300), (1050, 1480)], hexc('#ffb04a'), None, 6, 0)
    p.shape([(900, 1180), (900, 760), (960, 760), (960, 1180)], hexc('#3b4042'), None, 5, 0)
    # chão
    p.poly([(0, 1600), (W, 1600), (W, H), (0, H)], hexc('#6b4a2f'))
    # mesinha com caderno
    p.shape([(160, 1600), (180, 1380), (600, 1380), (620, 1600)], hexc('#c0703a'), hexc('#a35d2f'), 6, 0)
    p.shape([(240, 1380), (300, 1320), (560, 1320), (520, 1380)], hexc('#f4ecd6'), None, 5, 0)
    c = Image.new('RGBA', (W, H)); c.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    gl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
    dg.ellipse((620, 1050, 1240, 1750), fill=(255, 170, 70, 110))
    c.alpha_composite(gl.filter(ImageFilter.GaussianBlur(70)))
    return c


@lru_cache(maxsize=4)
def caderno_img(linhas=('Ana', 'Téo', 'Lia', 'Dona Rosa', 'Malu')):
    p = Pen(700, 860)
    p.shape([(20, 840), (20, 20), (680, 20), (680, 840)], hexc('#f6efd9'), hexc('#ded4b8'), 7, 0)
    for y in range(150, 800, 90): p.stroke([(60, y), (640, y)], 3, hexc('#b9c8d8'))
    im = p.img.resize((700, 860), Image.LANCZOS); d = ImageDraw.Draw(im)
    fnt = font(F_STAMP, 58)
    for i, l in enumerate(linhas):
        d.text((80, 90 + i * 90), l, font=fnt, fill=(70, 60, 90))
    return im
