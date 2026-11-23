"""Rua com a casa 27 no traço MISTÉRIO (história "A nuvem da casa 27", 23/11/2026).
rua27_bg(luz, casas): céu pela luz, casinhas ao fundo, 3 casas grandes na frente (base y=1560), calçada e rua.
  casas = tupla de (cor, número, janela_acesa) para as posições esquerda/centro/direita (centro x≈621).
nuvem(c, x, y, s, f, chove): nuvenzinha cinza-clara com chuva até o chão (y_chao).
vaso(c, x, y, s, murcha, flor): vasinho com plantinha (murcha 0..1, flor 0..1).
"""
from kit import *
import kit
from sombrio import *

CASA_X = (190, 621, 1052)   # centro das 3 casas da frente


@lru_cache(maxsize=32)
def casa_img(cor, num='', acesa=False, escuro=1.0):
    """casa de frente 440x760 (base em y=740)."""
    col = mul(hexc(cor), escuro)
    p = Pen(460, 780)
    p.shape([(30, 740), (30, 320), (430, 320), (430, 740)], col, mul(col, .84), 7, 14)
    p.shape([(14, 330), (230, 120), (446, 330)], mul(hexc('#b8574a'), escuro), mul(hexc('#8f4038'), escuro), 7, 10)
    jan = hexc('#f2e2a0') if acesa else mul(hexc('#cfe0e6'), escuro)
    for x0 in (70, 290):
        p.shape([(x0, 400), (x0 + 100, 400), (x0 + 100, 510), (x0, 510)], jan, None, 6, 0)
        p.stroke([(x0 + 50, 400), (x0 + 50, 510)], 5); p.stroke([(x0, 455), (x0 + 100, 455)], 5)
    p.shape([(180, 560), (280, 560), (280, 740), (180, 740)], mul(hexc('#6a4a32'), escuro), None, 6, 0)
    p.dot(262, 650, 7, mul(hexc('#e0c070'), escuro))
    im = p.img.resize((460, 780), Image.LANCZOS)
    if num:
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((300, 560, 410, 640), 10, fill=(244, 241, 234, 255), outline=(36, 30, 32, 255), width=5)
        fnt = font(F_STAMP, 56); tw = d.textlength(num, font=fnt)
        d.text((355 - tw / 2, 562), num, font=fnt, fill=(40, 60, 110))
    return im


CEU_R = {'dia': 'dia', 'tarde': 'tarde', 'neblina': 'neblina', 'noite': 'noite', 'frio': 'neblina'}


@lru_cache(maxsize=16)
def rua27_bg(luz='dia', casas=(('#e8b4b8', '', False), ('#f4d35e', '27', False), ('#a8d0e6', '', False))):
    c = ceu(CEU_R[luz]).copy()
    if luz == 'frio': c.alpha_composite(Image.new('RGBA', c.size, (190, 210, 235, 70)))
    cs = casas_strip(CEU_R[luz] if luz != 'frio' else 'neblina')
    c.alpha_composite(cs.crop((300, 0, 300 + W_, 700)), (0, 700))
    esc = .6 if luz == 'noite' else (.85 if luz in ('neblina', 'frio') else 1.0)
    for (cor, num, acesa), x in zip(casas, CASA_X):
        im = casa_img(cor, num, acesa, esc)
        c.alpha_composite(im, (int(x - 230), 1560 - 740))
    d = ImageDraw.Draw(c)
    calc = {'dia': (196, 196, 188), 'tarde': (200, 182, 160), 'neblina': (150, 156, 154), 'noite': (70, 74, 78), 'frio': (176, 184, 190)}[luz]
    rua_ = {'dia': (110, 116, 120), 'tarde': (112, 104, 100), 'neblina': (82, 88, 90), 'noite': (40, 44, 46), 'frio': (96, 104, 112)}[luz]
    d.rectangle((0, 1560, W_, 1760), fill=calc + (255,))
    d.line((0, 1560, W_, 1560), fill=(36, 30, 38, 255), width=6)
    d.rectangle((0, 1760, W_, H_), fill=rua_ + (255,))
    d.line((0, 1760, W_, 1760), fill=(36, 30, 38, 255), width=6)
    for x in range(0, W_, 300): d.rectangle((x + 60, 1980, x + 210, 1996), fill=(200, 204, 204, 255))
    if luz == 'neblina':
        nb = neblina_img(1.0); c.alpha_composite(nb.crop((0, 0, W_, 420)), (0, 1200))
    return c


@lru_cache(maxsize=16)
def nuvem_img(w, cor=(214, 220, 226)):
    h = int(w * .55)
    p = Pen(w + 40, h + 40)
    cx = (w + 40) / 2
    pts = []
    for i in range(48):
        a = 2 * math.pi * i / 48
        r = 1 + .12 * math.sin(5 * a) ** 2
        pts.append((cx + w * .46 * math.cos(a) * r, 20 + h * .55 + h * .4 * math.sin(a) * r * (0.75 if math.sin(a) > 0 else 1.15)))
    p.shape(pts, cor, mul(cor, .86), 7, 12)
    return p.img.resize((w + 40, h + 40), Image.LANCZOS)


def nuvem(c, x, y, s, f, chove=1.0, chao=1560, w=420, cor=(214, 220, 226)):
    """nuvem centrada em (x, y), escala s (0..1 cresce), chuva até y=chao."""
    if s <= .03: return
    ww = max(20, int(w * s) // 8 * 8)
    im = nuvem_img(ww, cor)
    yy = y + 8 * math.sin(f * .07)
    if chove > 0:
        d = ImageDraw.Draw(c); rnd = random.Random(f // 2)
        for i in range(int(46 * chove)):
            rx = x + rnd.uniform(-.42, .42) * ww; ry = rnd.uniform(yy, chao - 60)
            d.line((rx, ry, rx - 10, ry + 70), fill=(190, 210, 235, 200), width=5)
        for i in range(int(8 * chove)):   # respingos no chão
            rx = x + rnd.uniform(-.4, .4) * ww
            d.arc((rx - 22, chao - 14, rx + 22, chao + 6), 200, 340, fill=(210, 225, 240, 220), width=4)
    c.alpha_composite(im, (int(x - im.width / 2), int(yy - im.height / 2)))


@lru_cache(maxsize=16)
def vaso_img(murcha=0.0, flor=0.0):
    p = Pen(400, 520)
    # planta
    caule_top = (200 + 80 * murcha, 170 + 90 * murcha)
    p.stroke([(200, 360), (200, 260), caule_top], 12, mul(hexc('#4f8a3a'), 1 - .3 * murcha))
    folha = mul(hexc('#6fbf4a'), 1 - .35 * murcha)
    if murcha < .5: folha = folha
    p.shape([(200, 300), (120, 250 + 60 * murcha), (90, 290 + 80 * murcha), (190, 320)], folha, None, 6, 0)
    p.shape([(200, 280), (290, 240 + 60 * murcha), (310, 280 + 80 * murcha), (210, 300)], folha, None, 6, 0)
    if flor > .05:
        fx, fy = caule_top
        for k in range(6):
            a = 2 * math.pi * k / 6
            p.shape(ell_pts(fx + 34 * flor * math.cos(a), fy + 34 * flor * math.sin(a), 26 * flor, 26 * flor, 16), hexc('#f28ab2'), None, 5, 0)
        p.dot(fx, fy, 20 * flor, hexc('#f4d35e'), 5)
    # vaso de barro
    p.shape([(110, 350), (290, 350), (265, 500), (135, 500)], hexc('#c96f43'), hexc('#a8552f'), 7, 10)
    p.shape([(96, 330), (304, 330), (304, 370), (96, 370)], hexc('#d9804f'), None, 6, 0)
    return p.img.resize((400, 520), Image.LANCZOS)


def vaso(c, x, y, s=1.0, murcha=0.0, flor=0.0):
    """vaso com base em (x, y); s=1 => 520 px de altura."""
    if s <= .03: return
    im = vaso_img(round(murcha, 1), round(flor, 1))
    im = im.resize((max(4, int(400 * s)), max(4, int(520 * s))), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height)))


def guarda_chuva(c, x, y, s=1.0, cor='#5a7fb8'):
    """guarda-chuva fechado (em pé), ponta em (x, y)."""
    if s <= .03: return
    p = Pen(120, 520)
    p.shape([(60, 500), (30, 140), (60, 90), (90, 140)], hexc(cor), mul(hexc(cor), .8), 6, 8)
    p.stroke([(60, 90), (60, 20)], 8); p.arc(40, 24, 20, 18, 180, 360, 8)
    im = p.img.resize((max(4, int(120 * s)), max(4, int(520 * s))), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height)))


@lru_cache(maxsize=8)
def quintal_bg(luz='dia'):
    """quintal da narradora: céu pela luz, muro de tijolo ao fundo (topo y≈1150), parede azul da casa à esquerda,
    grama a partir de y≈1500, cantinho de terra à direita (x≈980, y≈1600) onde fica o vaso."""
    c = ceu(CEU_R[luz]).copy()
    if luz == 'frio': c.alpha_composite(Image.new('RGBA', c.size, (190, 210, 235, 70)))
    esc = .6 if luz == 'noite' else (.85 if luz in ('neblina', 'frio') else 1.0)
    p = Pen(W_, H_)
    tij = mul(hexc('#c47a5a'), esc)
    p.shape([(-20, 1500), (-20, 1150), (W_ + 20, 1150), (W_ + 20, 1500)], tij, mul(tij, .86), 7, 0)
    for k, y in enumerate(range(1150, 1500, 50)):
        p.stroke([(0, y), (W_, y)], 3, mul(tij, .78))
        for x in range(-60 + (k % 2) * 60, W_, 120): p.stroke([(x, y), (x, y + 50)], 3, mul(tij, .78))
    # varal atrás do muro
    for x in (560, 1180): p.stroke([(x, 1150), (x, 880)], 12, mul(hexc('#6a6a6a'), esc))
    p.arc(870, 870, 310, 50, 0, 180, 5, mul(hexc('#3a3a3a'), esc))
    # parede da casa azul à esquerda
    az = mul(hexc('#7fb3d5'), esc)
    p.shape([(-20, 1560), (-20, 500), (330, 500), (330, 1560)], az, mul(az, .84), 7, 0)
    p.shape([(140, 1180), (260, 1180), (260, 1560), (140, 1560)], mul(hexc('#6a4a32'), esc), None, 6, 0)
    p.shape([(90, 760), (250, 760), (250, 920), (90, 920)], hexc('#f2e2a0') if luz == 'noite' else mul(hexc('#cfe0e6'), esc), None, 6, 0)
    # grama
    gr = {'dia': '#8cc46a', 'tarde': '#a8b46a', 'neblina': '#7f9a78', 'noite': '#3e5a3e', 'frio': '#9ab89a'}[luz]
    p.poly([(0, 1500), (W_, 1500), (W_, H_), (0, H_)], hexc(gr))
    p.stroke([(0, 1500), (W_, 1500)], 6)
    rnd = random.Random(4)
    for i in range(60):
        x, y = rnd.randint(0, W_), rnd.randint(1540, 2200)
        p.stroke([(x, y), (x - 8, y - 26)], 4, mul(hexc(gr), .8)); p.stroke([(x, y), (x + 8, y - 24)], 4, mul(hexc(gr), .8))
    # cantinho de terra
    p.shape(ell_pts(980, 1610, 170, 50, 30), mul(hexc('#8a6a4a'), esc), None, 6, 0)
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    if luz == 'neblina':
        nb = neblina_img(1.0); c.alpha_composite(nb.crop((0, 0, W_, 420)), (0, 1250))
    return c
