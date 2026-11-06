"""Um Café com o Mundo — CURIOSIDADE em desenho (post extra de 06/11/2026).
Fontes: Anadolu Agency (AA), via HeritageDaily (05/11/2026) e Türkiye Today (05/11/2026).
Fatos: 8 pães carbonizados de ~5.000 anos (1º quarto da Idade do Bronze Antiga; região ~3000 a.C.)
no monte Seyitömer, Kütahya, oeste da Turquia, em escavação de resgate (há uma reserva de lignito/carvão
embaixo do sítio). Estavam numa sala com forno, entre os pés de uma prateleira que desabou, junto com
trigo e lentilha. Um incêndio destruiu o prédio; o fogo carbonizou o material e por isso ele sobreviveu.
Hoje estão no Museu de Arqueologia e Mineração de Kütahya e viraram uma das peças mais populares."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Arqueólogos mostraram oito pães que têm cerca de cinco mil anos.",
    "Eles estavam num monte de terra no oeste da Turquia, que fica em cima de uma reserva de carvão.",
    "Os pães estavam numa sala com um forno, entre os pés de uma prateleira, junto com trigo e lentilha.",
    "Mas como um pão dura tanto tempo? Um incêndio destruiu a casa, e a prateleira desabou.",
    "Você vê, o fogo torrou os pães até virarem carvão. E assim eles não apodreceram.",
    "Hoje, eles estão num museu e viraram uma das peças mais populares. Pão queimado, virando estrela.",
]
CAPTXT = [
    "Arqueólogos mostraram 8 pães que têm cerca de 5 mil anos.",
    "Eles estavam num monte de terra no oeste da Turquia,|que fica em cima de uma reserva de carvão.",
    "Os pães estavam numa sala com um forno,|entre os pés de uma prateleira, junto com trigo e lentilha.",
    "Mas como um pão dura tanto tempo?|Um incêndio destruiu a casa, e a prateleira desabou.",
    "Você vê, o fogo torrou os pães até virarem carvão.|E assim eles não apodreceram.",
    "Hoje, eles estão num museu e viraram uma das peças mais populares.|Pão queimado, virando estrela.",
]
FALA_TIKTOK = "Você comeria um pão de cinco mil anos? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 3
FLASH = [4]
CHECK = [(0, 'cinco', 6), (1, 'carvao', 4), (2, 'prateleira', 4), (2, 'lentilha', 6), (3, 'incendio', 6), (3, 'desabou', 8), (4, 'carvao', 6), (5, 'estrela', 6)]

BREAD = hexc('#d9a35a'); BREADD = hexc('#a8702f'); CHAR = hexc('#2e2420'); CHARD = hexc('#1a1412')
CLAY = hexc('#b9825a'); CLAYD = hexc('#8a5a3a'); WOOD = hexc('#8a5a34'); WOODD = hexc('#5e3c22')


def mixc(a, b, t):
    return tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))


# ------------------------------------------------------------------ objetos novos
def loaf(burn=0.0, seed=1, face=0, blink=0):
    """pão redondo achatado com cortes no topo. 500x320, base y~300. burn 0 = dourado, 1 = carvão. face=1 olhinhos."""
    p = Pen(500, 320)
    c = mixc(BREAD, CHAR, burn); d = mixc(BREADD, CHARD, burn)
    pts = ell_pts(250, 200, 215, 110, 64)
    pts = [(x, min(y, 298)) for x, y in pts]
    p.shape(pts, c, d, 6, 20)
    rnd = random.Random(seed)
    for i in range(3):
        x = 150 + i * 100 + rnd.random() * 20
        p.stroke([(x - 30, 150 + rnd.random() * 10), (x + 30, 130 + rnd.random() * 10)], 6, mixc(BREADD, (20, 15, 12), burn))
    if burn > .5:
        for i in range(10):
            x = 80 + rnd.random() * 340; y = 140 + rnd.random() * 130
            p.dot(x, y, 4 + rnd.random() * 4, mixc(CHARD, (70, 60, 55), .5))
    if face:
        for ex in (205, 295):
            p.dot(ex, 205, 20, (255, 255, 255), 4)
            if blink < .6: p.dot(ex + 4, 208, 8, INK)
        p.arc(250, 238, 26, 14, 20, 160, 5)
    return p.img


def oven(glow=0.0):
    """forno de barro em cúpula. 600x520, base y~500."""
    p = Pen(600, 520)
    dome = sorted([q for q in ell_pts(300, 470, 270, 440, 80) if q[1] <= 470], key=lambda q: q[0])
    p.shape(dome + [(570, 500), (30, 500)], CLAY, CLAYD, 6, 24)
    p.shape([(30, 470), (570, 470), (570, 505), (30, 505)], CLAYD, None, 5)
    mouth = ell_pts(300, 470, 110, 150, 40)
    mouth = [(x, min(y, 470)) for x, y in mouth]
    p.poly(mouth, mixc(hexc('#2a1a14'), hexc('#ff9a3c'), glow), 5)
    return p.img


def shelf(tilt=0.0):
    """prateleira de madeira com 4 pés. 700x720, base y~690. tilt 0..1 = desaba."""
    p = Pen(700, 720)
    a = tilt * .5
    for x in (80, 620):
        top = (x, 200 + (tilt * 380 if x == 620 else tilt * 120)); 
        p.line([(x + (tilt * 60 if x == 620 else 0), 690), top], WOOD, 26, 5)
    y1 = 200 + tilt * 120; y2 = 200 + tilt * 380
    p.shape([(50, y1 - 22), (650, y2 - 22), (650, y2 + 18), (50, y1 + 18)], WOOD, WOODD, 5, 8)
    y1 = 440 + tilt * 120; y2 = 440 + tilt * 250
    p.shape([(50, y1 - 18), (650, y2 - 18), (650, y2 + 16), (50, y1 + 16)], WOOD, WOODD, 5, 8)
    return p.img


def sack(seed=1):
    p = Pen(300, 360)
    p.shape([(60, 120), (240, 120), (270, 340), (30, 340)], hexc('#d8c49a'), hexc('#ad9a72'), 5, 14)
    p.shape([(100, 70), (200, 70), (215, 125), (85, 125)], hexc('#d8c49a'), hexc('#ad9a72'), 5, 6)
    p.stroke([(85, 125), (215, 125)], 6, hexc('#7a5a34'))
    return p.img


def flame(phase=0.0, size=1.0):
    """chama cartoon. 300x420, base y~410."""
    p = Pen(300, 420)
    s = math.sin(phase * 2 * math.pi)
    outer = curve((40, 410), (0, 230), (150 + 30 * s, 20), 14) + curve((150 + 30 * s, 20), (300, 230), (260, 410), 14)
    p.shape(outer, hexc('#ff7a2a'), hexc('#d9481e'), 5, 12)
    inner = curve((90, 405), (70, 280), (150 - 20 * s, 150), 10) + curve((150 - 20 * s, 150), (230, 280), (210, 405), 10)
    p.shape(inner, hexc('#ffd04a'), None, 0)
    return p.img


def wheat():
    p = Pen(200, 500)
    p.line([(100, 490), (110, 160)], hexc('#d6b25a'), 8, 4)
    for i in range(6):
        y = 170 + i * 40
        for s in (-1, 1):
            p.shape(ell_pts(110 + s * 26, y, 22, 34, 20, s * .5), hexc('#e8c46a'), hexc('#c39a3e'), 4, 6)
    p.shape(ell_pts(110, 130, 20, 34, 20), hexc('#e8c46a'), hexc('#c39a3e'), 4, 6)
    return p.img


def lentils(seed=2):
    p = Pen(420, 200)
    p.shape(ell_pts(210, 150, 200, 40, 40), hexc('#8a6a3a'), None, 5)
    rnd = random.Random(seed)
    for i in range(40):
        p.dot(60 + rnd.random() * 300, 115 + rnd.random() * 50, 14, hexc('#c97a3a'), 3)
    return p.img


def mound(dig=0.0):
    """monte de terra (sítio) com trincheira e camada de carvão embaixo. 1242x900, base y~900."""
    p = Pen(1242, 900)
    p.poly([(0, 640), (1242, 640), (1242, 900), (0, 900)], hexc('#3a2e2a'), 5)  # carvão
    for i in range(30):
        r = random.Random(i)
        p.dot(r.random() * 1242, 680 + r.random() * 200, 10 + r.random() * 16, hexc('#15110f'))
    p.shape(curve((-40, 640), (620, -40), (1282, 640), 30) + [(1282, 650), (-40, 650)], hexc('#c79a62'), hexc('#9c7444'), 6, 26)
    for k, y in enumerate((300, 420, 540)):
        p.stroke(curve((160 + k * 40, y + 60), (620, y - 70), (1080 - k * 40, y + 60), 20), 4, hexc('#9c7444'))
    if dig > 0:
        p.poly([(520, 280), (760, 280), (740, 280 + 260 * dig), (540, 280 + 260 * dig)], hexc('#7a5a3a'), 4)
    return p.img


def case_(shine=0.0):
    """pedestal de museu com vitrine. 600x900, base y~890."""
    p = Pen(600, 900)
    p.shape([(110, 520), (490, 520), (490, 890), (110, 890)], hexc('#e9e2d4'), hexc('#c7bfae'), 6, 16)
    p.shape([(90, 480), (510, 480), (510, 530), (90, 530)], hexc('#d4cab6'), None, 5)
    p.poly([(110, 120), (490, 120), (490, 480), (110, 480)], hexc('#bfe3ef'), 6)
    p.stroke([(150, 160), (220, 160 + 40)], 8, (255, 255, 255))
    p.stroke([(150, 200), (180, 220)], 8, (255, 255, 255))
    p.poly([(200, 640), (400, 640), (400, 700), (200, 700)], hexc('#b48a3c'), 4)
    return p.img


def room_bg(light='day'):
    """sala de casa antiga: parede de tijolo de barro, chão de terra."""
    return _room(light)


@lru_cache(maxsize=4)
def _room(light):
    from PIL import ImageDraw
    S = 2; W, H = BW * S, BH * S
    wall = hexc('#d9b48a') if light == 'day' else hexc('#c58a5a') if light == 'golden' else hexc('#7a5a52')
    img = Image.new('RGB', (W, H), wall); d = ImageDraw.Draw(img)
    for row in range(0, 30):
        y = row * 70 * S; off = (row % 2) * 90 * S
        d.line([(0, y), (W, y)], fill=mul(wall, .85), width=3 * S)
        for x in range(-1, 9):
            d.line([(x * 180 * S + off, y), (x * 180 * S + off, y + 70 * S)], fill=mul(wall, .85), width=3 * S)
    fl = 1620 * S
    d.rectangle([0, fl, W, H], fill=mul(wall, .7)); d.line([(0, fl), (W, fl)], fill=INK, width=6 * S)
    return img.resize((BW, BH), Image.LANCZOS).convert('RGBA')


@lru_cache(maxsize=2)
def museum_bg():
    from PIL import ImageDraw
    S = 2; W, H = BW * S, BH * S
    img = Image.new('RGB', (W, H), hexc('#3d3a5c')); d = ImageDraw.Draw(img)
    fl = 1640 * S
    d.rectangle([0, fl, W, H], fill=hexc('#6a5a4a')); d.line([(0, fl), (W, fl)], fill=INK, width=6 * S)
    for x in range(0, W, 160 * S): d.line([(x, fl), (x - 200 * S, H)], fill=hexc('#5a4a3c'), width=4 * S)
    d.polygon([(470 * S, 0), (770 * S, 0), (1000 * S, fl), (240 * S, fl)], fill=hexc('#5a5680'))
    return img.resize((BW, BH), Image.LANCZOS).convert('RGBA')


@lru_cache(maxsize=2)
def star():
    p = Pen(120, 120)
    pts = [(60 + (55 if i % 2 == 0 else 22) * math.cos(math.radians(-90 + i * 36)), 60 + (55 if i % 2 == 0 else 22) * math.sin(math.radians(-90 + i * 36))) for i in range(10)]
    p.shape(pts, hexc('#ffd84a'), hexc('#e0a92a'), 4, 6)
    return p.img


def put_loaf(c, x, feet, h, burn=0.0, seed=1, face=0, blink=0):
    put_sprite(c, 'loaf', x, feet, h, 500 / 320, False, {'burn': 6}, burn=burn, seed=seed, face=face, blink=1 if blink > .6 else 0)


def put_img(c, fn, x, feet, h, aspect, **kw):
    put_sprite(c, fn, x, feet, h, aspect, False, {'tilt': 8, 'glow': 4, 'phase': 8, 'dig': 4, 'shine': 2}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = BG('golden').copy()
    v = wt(0, 'oito') - 3
    put_sci(c, 300, 1760, 820, f, 1, arms='up' if f >= v else 'clip', bun=True, skin=1, expr='shock' if f >= v else 'neutral', look=1)
    pos = [(560, 1500), (760, 1500), (960, 1500), (1140, 1500), (560, 1700), (760, 1700), (960, 1700), (1140, 1700)]
    for i, (x, y) in enumerate(pos):
        s = back(ramp(f, v + i * 2, v + i * 2 + 7))
        if s > .05:
            put_loaf(c, x, y, 120 * s, burn=1, seed=i)
            put_dust(c, x, y - 10, 50, f - v - i * 2)
    num(c, '8 PÃES', 820, 1180, f, v, 110, 4)
    num(c, '5 MIL ANOS', 640, 640, f, wt(0, 'cinco') - 3, 150)
    z = lerp(1.35, 1.08, easeOut(ramp(f, 0, 45))) * (1 + .0005 * f)
    k = kick(f, wt(0, 'cinco') - 3)
    return c, (680, 1300 + k * 10, z, k), 'golden'


def s1(f):
    c = BG('day').copy()
    c.alpha_composite(Image.new('RGBA', (BW, BH - 1400), hexc('#3a2e2a') + (255,)), (0, 1400))
    put_img(c, 'mound', 621, 1500, 900, 1242 / 900, dig=1.0)
    put_sci(c, 900, 985, 480, f, 2, arms='point', bun=False, skin=2, glasses=False, expr='grin', look=-1)
    num(c, 'TURQUIA', 640, 470, f, wt(1, 'turquia') - 3, 130)
    cv = wt(1, 'carvao') - 3
    num(c, 'CARVÃO', 640, 1390, f, cv, 110, 3)
    t = smooth(ramp(f, cv - 30, cv + 4))
    k = kick(f, cv, .6)
    return c, (640, lerp(950, 1150, t) + k * 8, lerp(1.25, 1.05, t) * (1 + .0006 * f), k), 'day'


def s2(f):
    c = room_bg('day').copy()
    fo = wt(2, 'forno') - 3
    if f >= fo:
        paste_c(c, oven(0).resize((480, 416)), 300, 1440, back(ramp(f, fo, fo + 8)))
    pr = wt(2, 'prateleira') - 3
    if f >= pr:
        s = back(ramp(f, pr, pr + 8))
        put_img(c, 'shelf', 820, 1710, 658 * s, 700 / 720, tilt=1.0)
        for i, x in enumerate((680, 820, 960)):
            put_loaf(c, x, 1690, 120 * back(ramp(f, pr + 4 + i * 3, pr + 12 + i * 3)), burn=1, seed=i + 3)
    tr = wt(2, 'trigo') - 3
    if f >= tr:
        for i, x in enumerate((90, 160)):
            put_img(c, 'wheat', x, 1700, 360 * back(ramp(f, tr + i * 3, tr + 8 + i * 3)), .4)
        num(c, 'TRIGO', 360, 900, f, tr, 80, -5)
    le = wt(2, 'lentilha') - 3
    if f >= le:
        put_img(c, 'lentils', 480, 1720, 130 * back(ramp(f, le, le + 8)), 2.1)
        num(c, 'LENTILHA', 860, 900, f, le, 80, 4)
    return c, (640 + 30 * math.sin(f * .02), 1420, lerp(1.22, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0005 * f), 0), 'day'


def s3(f):
    inc = wt(3, 'incendio') - 3
    de = wt(3, 'desabou') - 3
    lt = 'golden' if f < inc else 'dusk'
    c = room_bg(lt).copy()
    paste_c(c, oven(.6 if f >= inc else 0).resize((480, 416)), 300, 1440, 1)
    tl = clamp((f - de) / 8) if f >= de else 0
    put_img(c, 'shelf', 820, 1710, 658, 700 / 720, tilt=round(tl * 8) / 8)
    if tl < .5:
        for i, x in enumerate((640, 800, 960)):
            put_img(c, 'sack', x, 1232, 150, 300 / 360, seed=i)
        for i, x in enumerate((650, 810, 970)):
            put_loaf(c, x, 1450, 100, burn=0, seed=i + 3, face=1 if f < inc else 0, blink=blinkAt(f, i + 2))
    else:
        for i, x in enumerate((640, 800, 960)):
            put_img(c, 'sack', x + 20, 1700, 140, 300 / 360, seed=i)
        for i, x in enumerate((700, 860, 1010)):
            put_loaf(c, x, 1705, 100, burn=.5, seed=i + 3)
        put_dust(c, 840, 1660, 160, f - de - 8, 18)
    if f >= inc:
        for i, (x, y, h) in enumerate(((140, 1640, 380), (560, 1640, 300), (1160, 1640, 420), (380, 1000, 220), (1000, 980, 240))):
            s = back(ramp(f, inc + i * 3, inc + i * 3 + 8))
            if s > .05: put_img(c, 'flame', x, y, h * s, 300 / 420, phase=((f * .09 + i * .3) % 1))
        num(c, 'INCÊNDIO!', 640, 720, f, inc, 130, -5)
    q = wt(3, 'tempo') - 3
    if f < inc: num(c, '?', 840, 900, f, q, 200, 6)
    k = kick(f, de + 8, 1.2) + kick(f, inc, .6)
    roll = lerp(0, 3, smooth(ramp(f, inc, inc + 20)))
    return c, (640, 1400 + k * 10, lerp(1.15, 1.25, smooth(ramp(f, 0, 120))), roll + k), lt


def s4(f):
    c = BG('dusk').copy()
    cv = wt(4, 'carvao') - 3
    b = smooth(ramp(f, wt(4, 'torrou') - 3, cv + 2))
    put_loaf(c, 640, 1520, 420, burn=b, seed=5)
    if f < cv:
        for i, (x, y, h) in enumerate(((300, 1540, 300), (980, 1540, 320), (640, 1180, 200))):
            put_img(c, 'flame', x, y, h, 300 / 420, phase=((f * .09 + i * .3) % 1))
    num(c, 'CARVÃO', 640, 760, f, cv, 150)
    ap = wt(4, 'apodreceram') - 3
    num(c, 'NÃO APODRECE!', 640, 990, f, ap, 82, 3)
    z = lerp(1.0, 1.25, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, cv)
    return c, (640, 1300 + k * 8, z, k), 'dusk'


def s5(f):
    c = museum_bg().copy()
    put_img(c, 'case_', 640, 1720, 900, 600 / 900)
    for i, x in enumerate((560, 640, 720)):
        put_loaf(c, x, 1260, 95, burn=1, seed=i, face=1 if f >= wt(5, 'estrela') - 3 else 0, blink=blinkAt(f, i + 8))
    put_sci(c, 960, 1780, 700, f, 1, arms='up' if f >= wt(5, 'populares') - 3 else 'clip', bun=True, skin=1, expr='proud', look=-1)
    m = wt(5, 'museu') - 3
    num(c, 'MUSEU', 640, 520, f, m, 120)
    po = wt(5, 'populares') - 3
    if f >= po:
        rnd = random.Random(f // 4)
        for i in range(3):
            if (f // 4 + i) % 3 == 0:
                x = 120 + rnd.random() * 1000; y = 700 + rnd.random() * 700
                paste_c(c, star(), x, y, 1)
    es = wt(5, 'estrela') - 3
    num(c, 'ESTRELA!', 640, 760, f, es, 150, 5)
    z = lerp(1.0, 1.15, easeOut(ramp(f, 0, 60))) * (1 + .0005 * max(0, f - 60))
    return c, (640, 1300, z, lerp(0, -2.5, smooth(ramp(f, 0, 60))) - .01 * max(0, f - 60)), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    for i in range(8): s.thunk(s.W(0, 'oito') - 3 + i * 2, 220, .4)
    s.thunk(s.W(0, 'cinco') - 3, 140, 1.0)
    s.ting(s.W(1, 'turquia') - 3, .25)
    s.thunk(s.W(1, 'carvao') - 3, 120, .7)
    s.thunk(s.W(2, 'forno') - 3, 180, .5)
    s.thunk(s.W(2, 'prateleira') - 3, 200, .5)
    s.ting(s.W(2, 'lentilha') - 3, .25)
    s.whoosh(s.W(3, 'incendio') - 3, .4, .6)
    s.thunk(s.W(3, 'desabou') + 5, 110, 1.0)
    s.thunk(s.W(4, 'carvao') - 3, 140, .8)
    s.ting(s.W(5, 'estrela') - 3, .4)
