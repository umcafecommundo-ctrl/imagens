"""Estação espacial no traço MISTÉRIO (história "As batidas das três", 23/11/2026).
corredor_bg(luz): corredor com a janela redonda grande (centro JAN=(900, 980), raio 185). luz 'dia' ou 'noite'.
cabine_bg(luz): quarto/cabine com beliche e a janelinha redonda (centro JANI=(880, 820), raio 120).
casco_bg(): lado de fora: espaço com estrelas, casco da estação e a janelinha acesa.
sonda(c, x, y, s, f, antena=1.0, olho=(0,0), luz_olho): robozinho redondo com antena (antena<1 = quebrada/torta).
porta_regra(c, x, y, s): placa 'NUNCA BATA DE VOLTA'.
"""
from kit import *
import kit
from sombrio import *

JAN = (900, 980)
JANI = (880, 820)


def _noite(c, a=120):
    c.alpha_composite(Image.new('RGBA', c.size, (10, 16, 40, a)))


@lru_cache(maxsize=4)
def corredor_bg(luz='dia'):
    c = CEN('estacao', 'day').copy().convert('RGBA')
    if luz == 'noite':
        _noite(c, 140)
        d = ImageDraw.Draw(c)
        for y in (560, 1620): d.line((60, y, 1180, y), fill=(120, 200, 255, 255), width=10)
    p = Pen(W_, H_)
    p.poly([(0, 1640), (W_, 1640), (W_, H_), (0, H_)], hexc('#8a93a3') if luz == 'dia' else hexc('#3a4258'))
    p.stroke([(0, 1640), (W_, 1640)], 6)
    for x in range(0, W_, 200): p.stroke([(x, 1640), (x - 120, H_)], 3, hexc('#6f7888') if luz == 'dia' else hexc('#2c3346'))
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    return c


@lru_cache(maxsize=4)
def cabine_bg(luz='dia'):
    p = Pen(W_, H_)
    par = hexc('#dfe3ea')
    p.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], par)
    for x in range(0, W_, 207):
        for y in range(0, 1560, 260):
            p.shape([(x + 10, y + 10), (x + 197, y + 10), (x + 197, y + 250), (x + 10, y + 250)], mul(par, .96), mul(par, .9), 3, 6)
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], hexc('#8a93a3'))
    p.stroke([(0, 1560), (W_, 1560)], 6)
    # beliche à esquerda
    p.shape([(30, 1100), (520, 1100), (520, 1250), (30, 1250)], hexc('#4a78c8'), hexc('#3a5f9e'), 6, 8)
    p.shape([(30, 1250), (520, 1250), (520, 1300), (30, 1300)], hexc('#9aa1ad'), None, 6, 0)
    for x in (40, 500): p.shape([(x, 900), (x + 20, 900), (x + 20, 1560), (x, 1560)], hexc('#9aa1ad'), None, 5, 0)
    p.shape([(60, 1060), (200, 1060), (200, 1110), (60, 1110)], hexc('#f4f1ea'), None, 5, 0)
    # janelinha redonda
    x, y = JANI
    p.shape(ell_pts(x, y, 150, 150, 64), hexc('#9aa1ad'), hexc('#6f7683'), 6, 10)
    p.poly(ell_pts(x, y, 120, 120, 64), hexc('#0e1433'))
    rnd = random.Random(2)
    for i in range(14):
        a, r = rnd.uniform(0, 6.28), rnd.uniform(0, 105)
        p.dot(x + r * math.cos(a), y + r * math.sin(a), rnd.choice((3, 4, 5)), (255, 255, 230))
    for k in range(6):   # parafusos
        a = k * math.pi / 3
        p.dot(x + 136 * math.cos(a), y + 136 * math.sin(a), 7, hexc('#5a616d'))
    c = p.img.resize((W_, H_), Image.LANCZOS)
    if luz == 'noite':
        _noite(c, 150)
        d = ImageDraw.Draw(c)
        d.ellipse((x - 118, y - 118, x + 118, y + 118), outline=(120, 200, 255, 180), width=6)
    return c


@lru_cache(maxsize=2)
def casco_bg():
    c = CEN('espaco', 'day').copy().convert('RGBA')
    p = Pen(W_, H_)
    cas = hexc('#c9ced8')
    p.shape([(-40, 1000), (W_ + 40, 860), (W_ + 40, H_ + 40), (-40, H_ + 40)], cas, mul(cas, .85), 7, 0)
    for k in range(5):
        y = 1150 + k * 230
        p.stroke([(0, y + 40 - k * 4), (W_, y - 100 - k * 4)], 4, mul(cas, .8))
    for x in range(60, W_, 180):
        for y in (1100, 1500, 1900): p.dot(x, y - x * .1, 6, mul(cas, .7))
    x, y = 621, 1300
    p.shape(ell_pts(x, y, 160, 160, 64), hexc('#9aa1ad'), hexc('#6f7683'), 6, 10)
    p.poly(ell_pts(x, y, 128, 128, 64), hexc('#f2e2a0'))
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    return c


@lru_cache(maxsize=32)
def sonda_img(antena=1.0, olho=(0, 0), luz_olho=1.0):
    p = Pen(400, 460)
    # antena (torta quando quebrada)
    ang = (1 - antena) * 70
    ax = 200 + 150 * math.sin(math.radians(ang)); ay = 150 - 150 * math.cos(math.radians(ang)) + 20
    p.stroke([(200, 150), (ax, ay)], 9)
    p.dot(ax, ay, 16, hexc('#e8574a') if antena > .5 else hexc('#7a5a58'), 5)
    # braços
    for sd in (-1, 1): p.line([(200 + sd * 120, 290), (200 + sd * 175, 360)], hexc('#9aa1ad'), 22, 6)
    # corpo redondo
    p.shape(ell_pts(200, 280, 135, 125, 48), hexc('#e9a23b'), hexc('#c47f22'), 7, 16)
    p.shape(ell_pts(200, 270, 78, 70, 40), hexc('#1e2433'), None, 6, 0)
    ox, oy = olho
    cor = mul((140, 230, 255), .35 + .65 * luz_olho)
    p.dot(200 + ox * 22, 268 + oy * 18, 34, cor)
    p.dot(200 + ox * 22 + 10, 258 + oy * 18, 9, (255, 255, 255))
    for k in range(3): p.dot(150 + k * 50, 385, 8, hexc('#7a4a12'))
    return p.img.resize((400, 460), Image.LANCZOS)


def sonda(c, x, y, s, f=0, antena=1.0, olho=(0, 0), luz_olho=1.0, rot=0):
    """robozinho centrado em (x, y); s=1 => 460 px de altura."""
    if s <= .03: return
    im = sonda_img(round(antena, 1), (round(olho[0], 1), round(olho[1], 1)), round(luz_olho, 1))
    im = im.resize((max(4, int(400 * s)), max(4, int(460 * s))), Image.LANCZOS)
    r = rot + 3 * math.sin(f * .08)
    im = im.rotate(r, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2 + 10 * math.sin(f * .06))))


@lru_cache(maxsize=4)
def placa_img(t1='NUNCA BATA', t2='DE VOLTA'):
    im = Image.new('RGBA', (560, 260), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((6, 6, 554, 254), 20, fill=(240, 196, 74, 255), outline=(36, 30, 32, 255), width=8)
    fnt = font(F_STAMP, 84)
    for i, t in enumerate((t1, t2)):
        tw = d.textlength(t, font=fnt); d.text((280 - tw / 2, 18 + i * 110), t, font=fnt, fill=(36, 30, 32))
    return im


def placa(c, x, y, s=1.0):
    if s <= .03: return
    im = placa_img().resize((max(4, int(560 * s)), max(4, int(260 * s))), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))
