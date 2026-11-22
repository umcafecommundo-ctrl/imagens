"""Ilha com farol no traço MISTÉRIO (história "O farol sem faroleiro", 22/11/2026).
ilha_bg(luz): céu, mar, ilhota de pedra com o farol (x≈880, lanterna em LANT), casinha azul à esquerda; chão de areia/pedra em y≈1560+.
facho(c, ang, cor, s): facho de luz saindo da lanterna (ang em graus, 180 = para a esquerda).
escada_bg(luz): dentro do farol, escada em caracol; sala_lanterna_bg(luz): sala do topo com a lente; engrenagem(c, x, y, r, ang, cor).
pacote(c, x, y, s), chave(c, x, y, s, rot), caderno(c, x, y, s, linhas).
"""
from kit import *
import kit
from sombrio import *

LANT = (700, 330)   # centro da lanterna do farol (palco)
MAR_F = {'dia': ('#3f9ccc', '#2a7aa8'), 'tarde': ('#c98a6a', '#8a6a7a'), 'neblina': ('#7f9a9e', '#62797d'),
         'noite': ('#22344a', '#16243a'), 'frio': ('#7fa9c4', '#5c86a3')}
CHAO_F = {'dia': '#e6d3a4', 'tarde': '#d9b48a', 'neblina': '#b9b39e', 'noite': '#4e4a44', 'frio': '#d0ccbe'}


@lru_cache(maxsize=8)
def ilha_bg(luz='dia'):
    c = ceu({'frio': 'neblina'}.get(luz, luz)).copy()
    if luz == 'frio': c.alpha_composite(Image.new('RGBA', c.size, (190, 210, 235, 70)))
    noite = luz == 'noite'
    e = .55 if noite else 1.0
    p = Pen(W_, H_)
    m1, m2 = MAR_F[luz]
    p.poly([(0, 1120), (W_, 1120), (W_, 1600), (0, 1600)], hexc(m1))
    for k in range(7):
        y = 1160 + k * 60
        for x in range(-40 + (k % 2) * 90, W_, 180): p.stroke([(x, y), (x + 70, y)], 5, hexc(m2))
    base0 = p.img.resize((W_, H_), Image.LANCZOS); c.alpha_composite(base0)
    p = Pen(W_, H_)
    # ilhota de pedra com o farol (desenhada em x+180 e colada 180 px à esquerda)
    p.shape([(600, 1250), (660, 1150), (760, 1110), (980, 1100), (1100, 1140), (1180, 1250)], mul(hexc('#7a7f82'), e), mul(hexc('#5c6164'), e), 7, 14)
    # farol (listras vermelhas e brancas)
    x0, x1, y0, y1 = 800, 960, 1130, 420
    for k in range(6):
        ya = y0 - (y0 - y1) * k / 6; yb = y0 - (y0 - y1) * (k + 1) / 6
        wa = 80 - 22 * k / 6; wb = 80 - 22 * (k + 1) / 6
        col = hexc('#d9534a') if k % 2 == 0 else hexc('#f4f1ea')
        p.poly([(880 - wa, ya), (880 + wa, ya), (880 + wb, yb), (880 - wb, yb)], mul(col, e))
    p.stroke([(800, 1130), (822, 420), (938, 420), (960, 1130)], 7)
    p.shape([(800, 400), (960, 400), (960, 430), (800, 430)], mul(hexc('#3b4042'), 1), None, 6, 0)
    p.shape([(830, 260), (930, 260), (930, 400), (830, 400)], hexc('#f2e2a0') if noite else hexc('#cfe0e6'), None, 6, 0)
    p.stroke([(880, 260), (880, 400)], 5)
    p.shape([(812, 262), (880, 200), (948, 262)], mul(hexc('#d9534a'), e), None, 6, 0)
    p.shape([(860, 1030), (900, 1030), (900, 1130), (860, 1130)], mul(hexc('#5b4636'), e), None, 5, 0)   # porta
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS).crop((180, 0, W_, H_)), (0, 0))
    p = Pen(W_, H_)
    # areia/pedras do primeiro plano
    p.poly([(0, 1520)] + [(x, 1540 + 30 * math.sin(x / 130)) for x in range(0, W_ + 1, 40)] + [(W_, H_), (0, H_)], mul(hexc(CHAO_F[luz]), 1))
    rnd = random.Random(8)
    for i in range(30):
        x, y = rnd.randint(0, W_), rnd.randint(1640, 2200)
        p.dot(x, y, rnd.randint(4, 9), mul(hexc(CHAO_F[luz]), .82))
    # casinha azul à esquerda
    az = mul(hexc('#4f8fc0'), e)
    p.shape([(20, 1560), (20, 1220), (330, 1220), (330, 1560)], az, mul(az, .82), 7, 14)
    p.shape([(0, 1230), (175, 1080), (350, 1230)], mul(hexc('#f4f1ea'), e), None, 7, 0)
    p.shape([(120, 1400), (220, 1400), (220, 1560), (120, 1560)], mul(hexc('#f0c050'), e), None, 6, 0)
    p.shape([(230, 1290), (310, 1290), (310, 1370), (230, 1370)], hexc('#f2e2a0') if noite else hexc('#cfe0e6'), None, 6, 0)
    im = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(im)
    if luz == 'neblina':
        nb = neblina_img(1.0); c.alpha_composite(nb.crop((0, 0, W_, 420)), (0, 980))
    return c


def facho(c, ang, cor=(255, 236, 150), s=1.0, L=1500, abert=9):
    if s <= .02: return
    g = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    x, y = LANT
    a0, a1 = math.radians(ang - abert), math.radians(ang + abert)
    d.polygon([(x, y), (x + L * math.cos(a0), y + L * math.sin(a0)), (x + L * math.cos(a1), y + L * math.sin(a1))], fill=cor + (int(110 * s),))
    d.ellipse((x - 70, y - 70, x + 70, y + 70), fill=cor + (int(200 * s),))
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(10)))


@lru_cache(maxsize=4)
def escada_bg(luz='sombrio'):
    p = Pen(W_, H_)
    parede = hexc('#8a929a') if luz != 'noite' else hexc('#4a5258')
    p.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], parede)
    for y in range(0, H_, 90):
        off = 0 if (y // 90) % 2 else 70
        for x in range(-off, W_, 140): p.stroke([(x, y), (x + 140, y)], 3, mul(parede, .85)); p.stroke([(x, y), (x, y + 90)], 3, mul(parede, .85))
    # janelinha redonda
    p.shape(ell_pts(950, 500, 90, 90), hexc('#cfe0e6'), None, 8, 0)
    p.stroke([(860, 500), (1040, 500)], 6); p.stroke([(950, 410), (950, 590)], 6)
    # escada em caracol: degraus em zigue-zague
    for k in range(14):
        y = 2150 - k * 150
        lado = k % 2
        xa, xb = (150, 700) if lado == 0 else (540, 1090)
        p.shape([(xa, y), (xb, y), (xb, y + 40), (xa, y + 40)], hexc('#9a6a40'), hexc('#6f4a2a'), 6, 8)
    p.stroke([(620, 0), (620, H_)], 18, hexc('#5a5f62'))
    im = p.img.resize((W_, H_), Image.LANCZOS)
    return im


@lru_cache(maxsize=4)
def sala_lanterna_bg(luz='sombrio'):
    """topo do farol: vidros em volta mostrando o céu, piso de ferro, lente grande no centro (621, 900)."""
    c = ceu({'sombrio': 'neblina', 'frio': 'neblina'}.get(luz, luz)).copy()
    p = Pen(W_, H_)
    for x in (0, 410, 830, 1242):
        p.stroke([(x, 0), (x, 1500)], 26, hexc('#3b4042'))
    p.stroke([(0, 300), (W_, 300)], 18, hexc('#3b4042'))
    p.poly([(0, 1500), (W_, 1500), (W_, H_), (0, H_)], hexc('#5a5f62'))
    for x in range(0, W_, 80): p.stroke([(x, 1500), (x - 200, H_)], 3, hexc('#4a4e50'))
    p.stroke([(0, 1500), (W_, 1500)], 7)
    # parapeito
    p.shape([(0, 1240), (W_, 1240), (W_, 1290), (0, 1290)], hexc('#3b4042'), None, 6, 0)
    im = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(im)
    return c


@lru_cache(maxsize=256)
def _gear(r, ang, cor):
    n = max(8, int(r / 14))
    p = Pen(int(2 * r + 40), int(2 * r + 40))
    cx = cy = r + 20
    pts = []
    for i in range(n * 4):
        a = math.radians(ang) + 2 * math.pi * i / (n * 4)
        rr = r if (i % 4) in (1, 2) else r * .82
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    p.shape(pts, hexc(cor), mul(hexc(cor), .8), 5, 8)
    p.dot(cx, cy, r * .28, mul(hexc(cor), .7), 5)
    p.dot(cx, cy, r * .1, (40, 36, 34))
    return p.img.resize((int(2 * r + 40), int(2 * r + 40)), Image.LANCZOS)


def engrenagem(c, x, y, r, ang, cor='#c9a24a'):
    im = _gear(int(r), int(ang) % 360 // 3 * 3, cor)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def lente(c, x, y, r, cor=(255, 236, 150), brilho=1.0):
    g = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    if brilho > 0:
        d.ellipse((x - r * 2, y - r * 2, x + r * 2, y + r * 2), fill=cor + (int(90 * brilho),))
        g = g.filter(ImageFilter.GaussianBlur(r * .5)); d = ImageDraw.Draw(g)
    d.rectangle((x - r * .9, y - r * 1.2, x + r * .9, y + r * 1.2), fill=(36, 30, 32, 255))
    d.rectangle((x - r * .82, y - r * 1.12, x + r * .82, y + r * 1.12), fill=tuple(int(v * (.55 + .45 * brilho)) for v in cor) + (255,))
    for k in range(5):
        yy = y - r * 1.12 + k * r * .56
        d.line((x - r * .82, yy, x + r * .82, yy), fill=(36, 30, 32, 200), width=5)
    c.alpha_composite(g)


def pacote(c, x, y, s=1.0):
    if s <= .05: return
    w, h = 300 * s, 220 * s
    p = Pen(int(w + 40), int(h + 40))
    p.shape([(20, 20), (w + 20, 20), (w + 20, h + 20), (20, h + 20)], hexc('#c9a06a'), hexc('#a8804a'), 6, 10)
    p.stroke([(20 + w / 2, 20), (20 + w / 2, h + 20)], 10 * s, hexc('#7a3a2a')); p.stroke([(20, 20 + h / 2), (w + 20, 20 + h / 2)], 10 * s, hexc('#7a3a2a'))
    c.alpha_composite(p.img.resize((int(w + 40), int(h + 40)), Image.LANCZOS), (int(x - w / 2 - 20), int(y - h / 2 - 20)))


def chave(c, x, y, s=1.0, rot=0):
    if s <= .05: return
    p = Pen(400, 160)
    p.shape(ell_pts(80, 80, 60, 60), hexc('#b0703a'), hexc('#8a5228'), 6, 10)
    p.dot(80, 80, 24, (0, 0, 0, 0)) if False else None
    p.line([(140, 80), (360, 80)], hexc('#b0703a'), 26, 6)
    p.line([(300, 80), (300, 130)], hexc('#b0703a'), 22, 6); p.line([(340, 80), (340, 120)], hexc('#b0703a'), 22, 6)
    im = p.img.resize((400, 160), Image.LANCZOS)
    d = ImageDraw.Draw(im); d.ellipse((60, 60, 100, 100), fill=(0, 0, 0, 0)); d.ellipse((60, 60, 100, 100), outline=(36, 30, 32, 255), width=5)
    im = im.resize((max(4, int(400 * s)), max(4, int(160 * s))), Image.LANCZOS)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


F_MAO_F = GF + 'ofl/comicrelief/ComicRelief-Bold.ttf'


def caderno(c, x, y, s=1.0, linhas=(), t=1.0):
    if s <= .05: return
    W, H = 700, 480
    im = Image.new('RGBA', (W + 20, H + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle((10, 10, W + 10, H + 10), fill=(36, 30, 32, 255))
    d.rectangle((18, 18, W / 2 + 6, H + 2), fill=(246, 238, 214, 255)); d.rectangle((W / 2 + 14, 18, W + 2, H + 2), fill=(246, 238, 214, 255))
    for k in range(10):
        yy = 70 + k * 40; d.line((30, yy, W / 2, yy), fill=(200, 190, 170, 255), width=2); d.line((W / 2 + 20, yy, W - 10, yy), fill=(200, 190, 170, 255), width=2)
    fnt = font(F_MAO_F, 30)
    tot = sum(len(l) for l in linhas); n = int(round(tot * clamp(t)))
    for i, l in enumerate(linhas):
        vis = l[:max(0, n)]; n -= len(l)
        col = 0 if i < 5 else 1; row = i % 5
        d.text((40 + col * (W / 2), 34 + row * 80), vis, font=fnt, fill=(60, 44, 36, 255))
    im = im.resize((int((W + 20) * s), int((H + 20) * s)), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))
