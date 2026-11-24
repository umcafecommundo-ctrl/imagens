"""Vila na serra com neve (história "O boneco que anda", 24/11/2026).
vila_bg(luz, morro): 'dia' | 'tarde' | 'noite' | 'frio'; casinhas com telhado de neve no horizonte (base y≈1420),
  chão de neve; morro=True põe um morro à direita com a casinha do alto (chaminé em CHAMINE).
boneco_img(h, costas, cachecol): boneco de neve (largura .7h, base em y=h); costas=True = de costas (sem rosto).
put_boneco(c, x, base, h, ...). portao(c, x, base, s): portão de madeira. flocos(c, f, n): neve caindo.
casinha_img(): casinha do morro com janela acesa. pegadas(c, pts): pegadas redondas na neve.
"""
from kit import *
import kit
from sombrio import *
import cenarios

TINT = {'dia': None, 'tarde': ((255, 170, 110), 55), 'noite': ((16, 22, 50), 150), 'frio': ((160, 190, 220), 60)}
CASAS_V = ['#e8b4b8', '#a8d0e6', '#f4d35e', '#c9e2b3', '#f2c6a0']
CHAMINE = (1010, 700)


@lru_cache(maxsize=4)
def _casas():
    p = Pen(W_, 520); rnd = random.Random(5)
    x = -40
    i = 0
    while x < W_ + 40:
        w = rnd.randint(170, 230); h = rnd.randint(150, 210); col = hexc(CASAS_V[i % len(CASAS_V)])
        y1 = 500
        p.shape([(x, y1), (x, y1 - h), (x + w, y1 - h), (x + w, y1)], col, mul(col, .85), 5, 0)
        p.shape([(x - 14, y1 - h + 4), (x + w / 2, y1 - h - 90), (x + w + 14, y1 - h + 4)], hexc('#f6f8fb'), hexc('#d6dde6'), 5, 0)
        for jx in (x + 30, x + w - 80):
            p.shape([(jx, y1 - h + 50), (jx + 50, y1 - h + 50), (jx + 50, y1 - h + 105), (jx, y1 - h + 105)], hexc('#f2e2a0'), None, 4, 0)
        x += w + rnd.randint(10, 40); i += 1
    return p.img.resize((W_, 520), Image.LANCZOS)


@lru_cache(maxsize=2)
def casinha_img():
    p = Pen(420, 420)
    p.shape([(60, 400), (60, 200), (360, 200), (360, 400)], hexc('#b07a52'), hexc('#8a5a38'), 6, 0)
    p.shape([(30, 210), (210, 70), (390, 210)], hexc('#f6f8fb'), hexc('#d6dde6'), 6, 0)
    p.shape([(280, 120), (320, 120), (320, 40), (280, 40)], hexc('#8a4a3a'), None, 5, 0)
    p.shape([(110, 250), (190, 250), (190, 330), (110, 330)], hexc('#ffd77a'), None, 5, 0)
    p.shape([(240, 270), (310, 270), (310, 400), (240, 400)], hexc('#6a4a32'), None, 5, 0)
    return p.img.resize((420, 420), Image.LANCZOS)


@lru_cache(maxsize=16)
def vila_bg(luz='dia', morro=False):
    base = cenarios.cenario('neve', 'day' if luz in ('dia', 'frio') else 'dusk').convert('RGBA').copy()
    if morro:
        p = Pen(W_, H_)
        p.shape([(380, 1460), (700, 900), (960, 760), (1300, 740), (1300, 1460)], hexc('#f2f5f9'), hexc('#d3dbe5'), 6, 0)
        base.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
        ch = casinha_img().resize((300, 300), Image.LANCZOS)
        base.alpha_composite(ch, (CHAMINE[0] - 210, CHAMINE[1] - 30))
    base.alpha_composite(_casas(), (0, 1420 - 500))
    d = ImageDraw.Draw(base)
    d.rectangle((0, 1420, W_, H_), fill=(244, 247, 250, 255))
    d.line((0, 1420, W_, 1420), fill=(36, 30, 32, 255), width=6)
    t = TINT[luz]
    if t: base.alpha_composite(Image.new('RGBA', base.size, t[0] + (t[1],)))
    return base


@lru_cache(maxsize=64)
def boneco_img(h, costas=False, cachecol=True, look=0):
    p = Pen(700, 1000)
    neve, sombra = hexc('#f8fafc'), hexc('#d3dbe5')
    p.stroke([(230, 520), (60, 400)], 12, hexc('#6a4a32')); p.stroke([(110, 440), (80, 380)], 9, hexc('#6a4a32'))
    p.stroke([(470, 520), (640, 410)], 12, hexc('#6a4a32')); p.stroke([(590, 445), (630, 390)], 9, hexc('#6a4a32'))
    p.shape(ell_pts(350, 800, 230, 185, 48), neve, sombra, 6, 18)
    p.shape(ell_pts(350, 530, 170, 145, 48), neve, sombra, 6, 16)
    p.shape(ell_pts(350, 300, 125, 115, 48), neve, sombra, 6, 14)
    if not costas:
        lx = look * 14
        p.dot(305 + lx, 285, 16, hexc('#26241f')); p.dot(395 + lx, 285, 16, hexc('#26241f'))
        p.shape([(350 + lx, 315), (470 + lx, 335), (350 + lx, 345)], hexc('#f28c38'), hexc('#c96a20'), 4, 0)
        for i in range(5): p.dot(300 + i * 25 + lx, 375 + 10 * math.sin(i * .8), 7, hexc('#26241f'))
        for yy in (480, 560): p.dot(350, yy, 13, hexc('#26241f'))
    if cachecol:
        p.shape([(220, 405), (480, 405), (490, 450), (210, 450)], hexc('#d8423a'), hexc('#a83028'), 5, 0)
        p.shape([(400, 440), (450, 440), (470, 600), (420, 605)], hexc('#d8423a'), hexc('#a83028'), 5, 0)
    return p.img.resize((max(4, int(h * .7)), max(4, h)), Image.LANCZOS)


def put_boneco(c, x, base, h, costas=False, cachecol=True, look=0, s=1.0, derrete=0.0):
    if h * s < 8: return
    hh = int(h * s * (1 - .35 * derrete)) // 4 * 4
    if hh < 8: return
    im = boneco_img(hh, costas, cachecol, look)
    if derrete:
        im = im.resize((int(im.width * (1 + .25 * derrete)), im.height))
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height * .97)))


def portao(c, x, base, s=1.0):
    p = Pen(500, 360)
    for xx in range(20, 500, 70):
        p.shape([(xx, 340), (xx, 60), (xx + 25, 30), (xx + 50, 60), (xx + 50, 340)], hexc('#b07a52'), hexc('#8a5a38'), 5, 0)
    p.shape([(5, 120), (495, 120), (495, 160), (5, 160)], hexc('#9a6a40'), None, 5, 0)
    p.shape([(5, 260), (495, 260), (495, 300), (5, 300)], hexc('#9a6a40'), None, 5, 0)
    im = p.img.resize((int(500 * s), int(360 * s)), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height)))


@lru_cache(maxsize=4)
def _flocos_img(n):
    im = Image.new('RGBA', (W_, H_ * 2), (0, 0, 0, 0)); d = ImageDraw.Draw(im); rnd = random.Random(9)
    for _ in range(n):
        x, y, r = rnd.randint(0, W_), rnd.randint(0, H_ * 2), rnd.choice((4, 5, 6, 8))
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, 220))
    return im


def flocos(c, f, n=160, v=4):
    im = _flocos_img(n); o = int(f * v) % H_
    c.alpha_composite(im.crop((0, H_ - o, W_, 2 * H_ - o)))


def pegadas(c, pts, r=26):
    d = ImageDraw.Draw(c)
    for x, y in pts:
        d.ellipse((x - r, y - r * .45, x + r, y + r * .45), fill=(200, 210, 224, 255), outline=(150, 160, 178, 255), width=3)
