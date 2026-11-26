"""Cenários da história "A lousa da sala quatro" (26/11/2026): corredor da escola com a porta da SALA 4 (vidro),
lousa grande em close com letra de giz torta, papel dobrado. Palco 1242x2208."""
from functools import lru_cache
from kit import *
import kit
from sombrio import *

DOOR = (640, 760, 1060, 1560)       # porta da sala 4 (x0, y0, x1, y1) no palco
VIDRO = (720, 860, 980, 1120)       # vidro da porta


def _lousinha(p, x0, y0, x1, y1, luz):
    p.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], hexc('#2f5d4a' if luz != 'noite' else '#1f3a30'))
    for i in range(3):
        p.stroke([(x0 + 30, y0 + 50 + i * 55), (x0 + 120 + i * 30, y0 + 45 + i * 55)], 5, hexc('#d6e6dc'))


@lru_cache(maxsize=8)
def corredor_bg(luz='dia'):
    """corredor: parede com faixa, armários azuis à esquerda, porta da SALA 4 (vidro) e janela à direita; chão y≈1560."""
    W, H = W_, H_
    p = Pen(W, H)
    par = {'dia': '#f4e6c4', 'tarde': '#efcf9e', 'frio': '#d9e0e6', 'noite': '#5a5650'}[luz]
    fai = {'dia': '#e0745a', 'tarde': '#d26a4c', 'frio': '#8fa6bd', 'noite': '#6a4a40'}[luz]
    p.poly([(0, 0), (W, 0), (W, 1560), (0, 1560)], hexc(par))
    p.poly([(0, 1180), (W, 1180), (W, 1250), (0, 1250)], hexc(fai))
    # janela alta no fundo (céu conforme a luz)
    ceu = {'dia': '#8fd0f2', 'tarde': '#f4ac72', 'frio': '#b9c8d8', 'noite': '#1b2240'}[luz]
    p.shape([(1110, 300), (1240, 300), (1240, 900), (1110, 900)], hexc(ceu), None, 7, 0)
    # armários
    arm = {'dia': '#4f8fd6', 'tarde': '#4a7fbf', 'frio': '#6d8cab', 'noite': '#34465c'}[luz]
    for k in range(4):
        x = 20 + k * 140
        p.shape([(x, 1560), (x, 820), (x + 130, 820), (x + 130, 1560)], hexc(arm), mul(hexc(arm), .82), 5, 0)
        for yy in (870, 900, 930): p.stroke([(x + 30, yy), (x + 100, yy)], 5, mul(hexc(arm), .6))
        p.dot(x + 108, 1180, 9, hexc('#e8e2d0'), 3)
    # porta da sala 4
    x0, y0, x1, y1 = DOOR
    p.shape([(x0 - 26, y1), (x0 - 26, y0 - 26), (x1 + 26, y0 - 26), (x1 + 26, y1)], hexc('#f3f1ea'), None, 6, 0)
    p.shape([(x0, y1), (x0, y0), (x1, y0), (x1, y1)], hexc('#a8683c'), hexc('#8a532e'), 6, 0)
    vx0, vy0, vx1, vy1 = VIDRO
    sala = {'dia': '#cfe6ee', 'tarde': '#ecd2ae', 'frio': '#c4d2dc', 'noite': '#2a3036'}[luz]
    p.shape([(vx0, vy0), (vx1, vy0), (vx1, vy1), (vx0, vy1)], hexc(sala), None, 6, 0)
    _lousinha(p, vx0 + 25, vy0 + 50, vx1 - 25, vy0 + 220, luz)
    p.dot(x1 - 50, 1200, 16, hexc('#e3c35a'), 4)
    # plaquinha
    p.shape([(770, 690), (930, 690), (930, 750), (770, 750)], hexc('#2e3a4a'), None, 4, 0)
    # chão
    chao = {'dia': '#d8cdb6', 'tarde': '#cfb68f', 'frio': '#b9c0c6', 'noite': '#45423e'}[luz]
    p.poly([(0, 1560), (W, 1560), (W, H), (0, H)], hexc(chao))
    for y in (1640, 1760, 1920, 2120): p.stroke([(0, y), (W, y)], 4, mul(hexc(chao), .85))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    d = ImageDraw.Draw(im); fnt = font(F_STAMP, 44); t = 'SALA 4'
    d.text((850 - d.textlength(t, font=fnt) / 2, 692), t, font=fnt, fill=(240, 236, 220))
    return im


@lru_cache(maxsize=32)
def lousa_bg(linhas=(), luz='dia', forca=0, estrela=False):
    """lousa grande (moldura de madeira), texto de giz torto centralizado. forca: 0 = nada, 1 = forca pequena no canto,
    2 = forca grande com 7 risquinhos (parte 2)."""
    W, H = W_, H_
    p = Pen(W, H)
    par = {'dia': '#f1e2bd', 'tarde': '#e9c896', 'frio': '#d5dde3', 'noite': '#4a4640'}[luz]
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc(par))
    p.shape([(40, 520), (1202, 520), (1202, 1660), (40, 1660)], hexc('#8a5f35'), None, 7, 0)
    verde = {'dia': '#2f6450', 'tarde': '#2c5a46', 'frio': '#2b544a', 'noite': '#1d3a30'}[luz]
    p.poly([(80, 560), (1162, 560), (1162, 1620), (80, 1620)], hexc(verde))
    p.shape([(40, 1660), (1202, 1660), (1202, 1700), (40, 1700)], hexc('#a07a4a'), None, 4, 0)
    # apagador e giz na canaleta
    p.shape([(840, 1625), (990, 1625), (990, 1665), (840, 1665)], hexc('#3a3d44'), None, 4, 0)
    p.shape([(300, 1640), (380, 1640), (380, 1660), (300, 1660)], (250, 250, 245), None, 3, 0)
    # chão
    p.poly([(0, 1900), (W, 1900), (W, H), (0, H)], mul(hexc(par), .8))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    # manchas de giz
    sm = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sm); rnd = random.Random(7)
    for i in range(9):
        x, y = rnd.randint(150, 1050), rnd.randint(620, 1550)
        ds.ellipse((x - 120, y - 40, x + 120, y + 40), fill=(220, 235, 225, 26))
    im.alpha_composite(sm.filter(ImageFilter.GaussianBlur(25)))
    giz = (238, 242, 232)
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    n = len(linhas)
    for i, (txt, sz) in enumerate(linhas):
        fnt = font(F_MAO, sz)
        y = 1090 - (n - 1) * 95 + i * 190
        tw = ImageDraw.Draw(lay).textlength(txt, font=fnt)
        x = 621 - tw / 2
        rr = random.Random(i * 13 + len(txt))
        for ch in txt:
            g = Image.new('RGBA', (sz * 2, sz * 2), (0, 0, 0, 0)); dg = ImageDraw.Draw(g)
            dg.text((sz * .5, sz * .3), ch, font=fnt, fill=giz)
            g = g.rotate(rr.uniform(-9, 9), resample=Image.BICUBIC)
            lay.alpha_composite(g, (int(x - sz * .5), int(y - sz * .3 + rr.uniform(-10, 10))))
            x += ImageDraw.Draw(lay).textlength(ch, font=fnt)
    dl = ImageDraw.Draw(lay)
    if forca == 1:   # forca pequena no canto de baixo
        ox, oy = 960, 1330
        for seg in [((ox, oy + 230), (ox + 160, oy + 230)), ((ox + 40, oy + 230), (ox + 40, oy)), ((ox + 40, oy), (ox + 130, oy)),
                    ((ox + 130, oy), (ox + 130, oy + 35))]:
            dl.line(seg, fill=giz, width=7)
    if forca == 2:
        ox, oy = 190, 640
        for seg in [((ox, oy + 330), (ox + 220, oy + 330)), ((ox + 60, oy + 330), (ox + 60, oy)), ((ox + 60, oy), (ox + 190, oy)),
                    ((ox + 190, oy), (ox + 190, oy + 50))]:
            dl.line(seg, fill=giz, width=8)
    if estrela:
        cx, cy, r = 980, 1430, 70
        pts = [(cx + (r if k % 2 == 0 else r * .42) * math.sin(k * math.pi / 5), cy - (r if k % 2 == 0 else r * .42) * math.cos(k * math.pi / 5)) for k in range(10)]
        dl.line(pts + [pts[0]], fill=(250, 224, 120), width=7)
    lay = lay.filter(ImageFilter.GaussianBlur(.8))
    im.alpha_composite(lay)
    return im


def put_risquinhos(c, n, x0=380, y0=1450, s=1.0):
    """risquinhos da forca (palavra) na lousa grande, no palco."""
    d = ImageDraw.Draw(c)
    for k in range(n):
        x = x0 + k * 70
        d.line((x, y0, x + 50, y0), fill=(238, 242, 232, int(255 * s)), width=7)


@lru_cache(maxsize=4)
def papel_img(w=220):
    p = Pen(260, 200)
    p.shape([(20, 40), (240, 20), (235, 170), (25, 185)], (252, 250, 240), hexc('#dcd6c4'), 5, 8)
    p.stroke([(60, 80), (190, 70)], 5, hexc('#7a8aa8')); p.stroke([(60, 115), (170, 108)], 5, hexc('#7a8aa8'))
    return p.img.resize((w, int(w * 200 / 260)), Image.LANCZOS)
