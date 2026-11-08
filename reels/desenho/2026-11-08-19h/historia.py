"""Um Café com o Mundo — ESPORTE (domingo 08/11/2026, 19h).
Tema: GP de São Paulo de F1 (Interlagos, domingo 08/11/2026): dois brasileiros no grid pela 1ª vez desde 2016.
Fontes (conferidas em 08/11/2026):
- Total Motorsport / PlanetF1 / Motorsport Week (08/11/2026), classificação: 1º Lando Norris (McLaren), 2º Max Verstappen
  (Red Bull) +14,602 s, 3º Isack Hadjar; Gabriel Bortoleto (Audi) 16º; Rafael Câmara (Haas) 20º. Motorsport Week: tempo
  instável ("changeable weather"), Verstappen largou da última fila ("started from the back row").
- Reuters via Devdiscourse (06/11/2026): última vez com dois brasileiros no grid foi 2016 (Felipe Massa e Felipe Nasr);
  Câmara tem 21 anos e estreia pela Haas no lugar de Esteban Ocon; Bortoleto, 22, 2ª temporada.
- Grande Prêmio (03/11/2026) e Metrópoles: Haas tirou Ocon do carro no GP do México e oficializou a saída antecipada;
  Câmara (pernambucano) já tinha contrato para substituir Ocon na Haas em 2027 e só estrearia em 2027.
Personagens e carros genéricos, sem rosto de ninguém real, sem logotipos nem números de carro."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'ESPORTE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Pela primeira vez em dez anos, dois brasileiros largaram juntos numa corrida de Fórmula Um.",
    "Foi neste domingo, em Interlagos, com a estreia do pernambucano Rafael Câmara, de vinte e um anos.",
    "Ele só ia estrear em dois mil e vinte e sete. Mas a Haas tirou o francês Esteban Ocon do carro e chamou o brasileiro antes.",
    "Ao lado dele, Gabriel Bortoleto, da Audi. A última dupla brasileira foi Massa e Nasr, em dois mil e dezesseis.",
    "Com tempo instável, Lando Norris venceu, catorze segundos à frente de Max Verstappen, que largou lá do fundo.",
    "Bortoleto terminou em décimo sexto, e Câmara em vigésimo, na primeira corrida da vida dele.",
    "E isso é só o começo: o Rafa já tem vaga garantida na Haas no ano que vem.",
]
CAPTXT = [
    "Pela primeira vez em 10 anos, dois brasileiros|largaram juntos numa corrida de Fórmula 1.",
    "Foi neste domingo, em Interlagos,|com a estreia do pernambucano|Rafael Câmara, de 21 anos.",
    "Ele só ia estrear em 2027. Mas a Haas|tirou o francês Esteban Ocon do carro|e chamou o brasileiro antes.",
    "Ao lado dele, Gabriel Bortoleto, da Audi.|A última dupla brasileira foi|Massa e Nasr, em 2016.",
    "Com tempo instável, Lando Norris venceu,|14 segundos à frente de Max Verstappen,|que largou lá do fundo.",
    "Bortoleto terminou em 16º, e Câmara em 20º,|na primeira corrida da vida dele.",
    "E isso é só o começo:|o Rafa já tem vaga garantida|na Haas no ano que vem.",
]
FALA_TIKTOK = "Você assistiu à corrida? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'dez', 4), (0, 'dois', 4), (1, 'Interlagos', 4), (1, 'vinte', 6), (2, 'dois', 6), (2, 'Ocon', 4), (2, 'antes', 4),
         (3, 'Bortoleto', 4), (3, 'dezesseis', 4), (4, 'Norris', 4), (4, 'catorze', 4), (4, 'fundo', 4),
         (5, 'sexto', 4), (5, 'vigesimo', 4), (6, 'garantida', 4)]

FONTB = kit.FONT.path
WHITE = (255, 255, 255); RED = hexc('#d8443c'); GOLD = hexc('#f0c541'); GREEN = hexc('#2f9a55'); YEL = hexc('#f5d33a')
BLUEB = hexc('#2a4fa8'); ORANGE = hexc('#f08a2c'); NAVY = hexc('#26325e'); GRAYC = hexc('#d9dde3')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


# ------------------------------------------------------------------ cenário: autódromo
CEUS = {'day': ('#3f86dc', '#cfe6f7'), 'golden': ('#6474c0', '#ffc485'), 'dusk': ('#18234f', '#d18a7c'), 'rain': ('#5d6b80', '#b9c3cf')}


@lru_cache(maxsize=6)
def pista(luz='day'):
    import numpy as np
    W, H = BW, BH
    t, b = CEUS[luz]
    hz = 1000
    y = np.linspace(0, 1, hz)[:, None, None]
    sky = np.array(hexc(t)) * (1 - y) + np.array(hexc(b)) * y
    base = Image.new('RGBA', (W, H), hexc(b) + (255,))
    base.paste(Image.fromarray(np.broadcast_to(sky, (hz, W, 3)).astype(np.uint8)).convert('RGBA'), (0, 0))
    p = Pen(W, H); rnd = random.Random(7)
    dark = luz in ('dusk', 'rain')
    # nuvens
    for i in range(4):
        cx, cy = rnd.randint(0, W), rnd.randint(150, 520)
        col = hexc('#8e98a8') if luz == 'rain' else (WHITE if luz == 'day' else mul(hexc(b), 1.05))
        for dx, dy, r in ((-70, 10, 55), (0, -15, 75), (75, 8, 55), (0, 25, 60)): p.dot(cx + dx, cy + dy, r + 5, INK)
        for dx, dy, r in ((-70, 10, 55), (0, -15, 75), (75, 8, 55), (0, 25, 60)): p.dot(cx + dx, cy + dy, r, col)
    # prédios ao longe (São Paulo)
    x = -30
    while x < W:
        w = rnd.randint(70, 130); h = rnd.randint(120, 330)
        p.poly([(x, 1000 - h), (x + w, 1000 - h), (x + w, 1000), (x, 1000)], hexc('#8e9bb3') if not dark else hexc('#5a6385'), 3)
        x += w + 8
    # arquibancada
    p.shape([(-20, 760), (W + 20, 820), (W + 20, 1290), (-20, 1290)], hexc('#b9bec8') if not dark else hexc('#7d8292'), hexc('#8f95a2'), 6, 10)
    p.shape([(-20, 720), (W + 20, 780), (W + 20, 800), (-20, 740)], hexc('#e05a4c'), None, 5, 0)
    cols = ['#f5d33a', '#2f9a55', '#ffffff', '#2a4fa8', '#e05a4c', '#f08a2c', '#3a3a44']
    for row in range(7):
        yy = 860 + row * 58
        for i in range(30):
            xx = i * 43 + (row % 2) * 20 + rnd.randint(-4, 4)
            p.dot(xx, yy + xx * .045, 15, hexc(rnd.choice(cols)), 3)
    # muro + zebra
    p.shape([(-20, 1290), (W + 20, 1290), (W + 20, 1390), (-20, 1390)], WHITE, hexc('#c9ced8'), 6, 6)
    for xx in range(0, W, 160): p.poly([(xx, 1300), (xx + 80, 1300), (xx + 80, 1380), (xx, 1380)], hexc('#e05a4c'))
    p.stroke([(-20, 1290), (W + 20, 1290)], 6); p.stroke([(-20, 1390), (W + 20, 1390)], 6)
    # asfalto
    asf = hexc('#5b5d66') if not dark else hexc('#4a4c55')
    p.poly([(0, 1390), (W, 1390), (W, H), (0, H)], asf)
    for xx in range(0, W, 120):
        p.poly([(xx, 1390), (xx + 60, 1390), (xx + 60, 1430), (xx, 1430)], hexc('#e05a4c'))
        p.poly([(xx + 60, 1390), (xx + 120, 1390), (xx + 120, 1430), (xx + 60, 1430)], WHITE)
    p.stroke([(0, 1430), (W, 1430)], 5)
    for xx in range(0, W, 260): p.poly([(xx, 1790), (xx + 150, 1790), (xx + 150, 1808), (xx, 1808)], hexc('#e9e9e9'))
    if luz == 'rain':
        for i in range(40):
            xx, yy = rnd.randint(0, W), rnd.randint(1460, 2150)
            p.stroke([(xx, yy), (xx + 70, yy)], 4, hexc('#7b8090'))
    return _done(base, p)


def _done(base, p):
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


def chuva(c, f, n=70, a=150):
    d = ImageDraw.Draw(c, 'RGBA'); rnd = random.Random(3)
    for i in range(n):
        x = (rnd.random() * 1500 - f * 9) % 1400 - 80
        y = (rnd.random() * 2300 + f * 55) % 2300 - 60
        d.line([(x, y), (x - 14, y + 60)], fill=(220, 230, 245, a), width=5)


# ------------------------------------------------------------------ carro de corrida genérico (de lado, frente p/ direita)
@lru_cache(maxsize=64)
def carro(col='#2f9a55', col2='#f5d33a', helm='#f5d33a', wheel=0):
    p = Pen(1000, 330)
    C, C2 = hexc(col), hexc(col2)
    # asa traseira
    p.shape([(40, 60), (150, 60), (150, 90), (40, 90)], C, mul(C, .7), 5, 4)
    p.shape([(95, 90), (125, 90), (135, 200), (105, 200)], hexc('#2a2a33'), None, 4, 0)
    # corpo
    body = [(70, 200), (260, 150), (430, 130), (520, 110), (600, 140), (860, 190), (980, 225), (980, 245), (70, 255)]
    p.shape(body, C, mul(C, .72), 6, 16)
    p.poly([(300, 205), (900, 220), (900, 236), (300, 236)], C2, 3)
    # asa dianteira
    p.shape([(860, 250), (995, 250), (995, 272), (860, 272)], C2, mul(C2, .7), 5, 3)
    # entrada de ar + cockpit
    p.shape([(420, 125), (500, 70), (540, 70), (540, 120)], mul(C, .8), mul(C, .6), 5, 4)
    p.dot(600, 118, 40, hexc(helm), 5)
    p.poly([(605, 100), (640, 104), (638, 122), (606, 120)], hexc('#2a2a33'), 3)
    p.stroke([(560, 80), (640, 74), (700, 140)], 9, hexc('#3a3a44'))  # halo
    # rodas
    for wx, r in ((210, 82), (800, 70)):
        p.dot(wx, 250, r, hexc('#24242c'), 6)
        p.dot(wx, 250, r * .45, hexc('#9aa0aa'), 4)
        for k in range(3):
            a = wheel * math.pi / 6 + k * 2 * math.pi / 3
            p.stroke([(wx, 250), (wx + r * .42 * math.cos(a), 250 + r * .42 * math.sin(a))], 6, INK)
    return fin(p)


def put_car(c, x, y, w, f=0, col='#2f9a55', col2='#f5d33a', helm='#f5d33a', flip=False, spin=True, s=1.0):
    if s <= .02: return
    im = carro(col, col2, helm, (f // 1) % 4 if spin else 0)
    ww = int(w * s); hh = int(ww * .33)
    im = im.resize((ww, hh), Image.LANCZOS)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    d = ImageDraw.Draw(c, 'RGBA')
    d.ellipse([x - ww * .48, y - 14, x + ww * .48, y + 14], fill=(30, 20, 30, 90))
    c.alpha_composite(im, (int(x - ww / 2), int(y - hh)))


# ------------------------------------------------------------------ piloto genérico (macacão + capacete na mão)
def piloto(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#3a2a20', suit='#2f9a55'):
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(suit); P.COAT_D = mul(hexc(suit), .7)
    try:
        img = P.scientist(expr=expr, arms=arms, blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
    finally:
        P.COAT, P.COAT_D = oc, od
    return img


def put_pil(c, x, feet, h, f, seed, helm=None, **kw):
    kit._bean(c, 'piloto', x, feet, h, f, seed, **kw)
    if helm and kw.get('arms', 'hang') == 'hang':
        im = capacete(helm).resize((int(h * .2), int(h * .18)), Image.LANCZOS)
        paste_c(c, im, x + h * .19, feet - h * .34, 1)


@lru_cache(maxsize=8)
def capacete(col='#f5d33a', col2='#2f9a55'):
    p = Pen(400, 360)
    p.shape(ell_pts(200, 190, 170, 150, 48), hexc(col), mul(hexc(col), .75), 6, 14)
    p.poly([(60, 150), (330, 150), (330, 220), (60, 220)], hexc('#2a2a33'), 5)
    p.stroke([(50, 270), (350, 270)], 14, hexc(col2))
    p.shape([(70, 300), (330, 300), (320, 345), (80, 345)], hexc('#3a3a44'), None, 5, 0)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_br():
    p = Pen(600, 420)
    p.poly([(10, 10), (590, 10), (590, 410), (10, 410)], GREEN)
    p.poly([(300, 45), (555, 210), (300, 375), (45, 210)], YEL)
    p.dot(300, 210, 105, BLUEB)
    p.stroke(curve((200, 190), (300, 170), (400, 230), 10), 10, WHITE)
    p.stroke([(10, 10), (590, 10), (590, 410), (10, 410), (10, 10)], 6)
    return fin(p)


def put_band(c, x, y, w, f, s=1.0):
    if s <= .02: return
    ww = int(w * s); hh = int(w * .7 * s)
    im = bandeira_br().resize((ww, hh)).rotate(3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    d = ImageDraw.Draw(c)
    d.line([(x - ww / 2 - 4, y - hh / 2), (x - ww / 2 - 4, y + hh * 1.7)], fill=INK, width=10)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=2)
def quadriculada():
    p = Pen(560, 400)
    for i in range(7):
        for j in range(5):
            p.poly([(10 + i * 77, 10 + j * 76), (10 + (i + 1) * 77, 10 + j * 76), (10 + (i + 1) * 77, 10 + (j + 1) * 76), (10 + i * 77, 10 + (j + 1) * 76)],
                   (INK if (i + j) % 2 else WHITE))
    p.stroke([(10, 10), (549, 10), (549, 390), (10, 390), (10, 10)], 6)
    return fin(p)


def put_quad(c, x, y, w, f, s=1.0):
    if s <= .02: return
    ww = int(w * s)
    im = quadriculada().resize((ww, int(ww * .71))).rotate(10 * math.sin(f * .35), expand=True, resample=Image.BICUBIC)
    d = ImageDraw.Draw(c)
    d.line([(x - ww / 2, y), (x - ww / 2 - 30, y + ww * 1.2)], fill=INK, width=12)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=8)
def calend(ano):
    p = Pen(420, 400)
    p.shape([(20, 50), (400, 50), (400, 380), (20, 380)], WHITE, hexc('#dcdcdc'), 6, 12)
    p.shape([(20, 50), (400, 50), (400, 140), (20, 140)], RED, None, 6)
    for x in (110, 310): p.line([(x, 20), (x, 90)], hexc('#8a8f9e'), 14, 4)
    d = ImageDraw.Draw(p.img)
    fo = ImageFont.truetype(FONTB, 130 * 2); tw = d.textlength(ano, font=fo)
    d.text((420 - tw / 2, 170 * 2), ano, font=fo, fill=INK + (255,))
    return fin(p)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def xis(c, x, y, r, t):
    if t <= 0: return
    d = ImageDraw.Draw(c)
    a = min(1, t * 2); b = max(0, t * 2 - 1)
    d.line([(x - r, y - r), (x - r + 2 * r * a, y - r + 2 * r * a)], fill=RED, width=26)
    if b: d.line([(x + r, y - r), (x + r - 2 * r * b, y - r + 2 * r * b)], fill=RED, width=26)


# ------------------------------------------------------------------ cenas
BR1 = dict(col='#2f9a55', col2='#f5d33a', helm='#f5d33a')   # carro do Câmara (genérico, verde e amarelo)
BR2 = dict(col='#f5d33a', col2='#2f9a55', helm='#2f9a55')   # carro do Bortoleto (genérico)


def s0(f):
    c = pista('day').copy()
    x1 = 1500 - f * 16; x2 = 1950 - f * 16
    x1 = max(x1, 460); x2 = max(x2, 820)
    put_car(c, x1, 1540, 760, f, **BR1, flip=True)
    put_car(c, x2, 1790, 860, f, **BR2, flip=True)
    put_band(c, 980, 560, 280, f, back(ramp(f, wt(0, 'brasileiros') - 3, wt(0, 'brasileiros') + 5)))
    num(c, '10 ANOS', 560, 760, f, wt(0, 'dez') - 3, 170, -5)
    num(c, '2 BRASILEIROS', 640, 1150, f, wt(0, 'dois') - 3, 110, 3)
    z = lerp(1.35, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0005 * f)
    k = kick(f, wt(0, 'dez') - 3)
    return c, (640, 1300 + k * 10, z, k), 'day'


def s1(f):
    c = pista('day').copy()
    paste_c(c, txt('INTERLAGOS', 120, -3), 640, 640, back(ramp(f, wt(1, 'Interlagos') - 3, wt(1, 'Interlagos') + 6)))
    num(c, 'GP DE SÃO PAULO', 640, 800, f, wt(1, 'Interlagos') + 6, 80, 2)
    put_car(c, 380, 1640, 700, 0, **BR1, spin=False)
    e0 = wt(1, 'estreia') - 3
    put_pil(c, 900, 2000, 880, f, 2, suit='#2f9a55', helm='#f5d33a', skin=1, expr='grin' if f >= e0 else 'neutral',
            arms='up' if f >= e0 else 'hang', look=-.4)
    num(c, 'ESTREIA!', 900, 1000, f, e0, 110, -6)
    num(c, '21 ANOS', 380, 1180, f, wt(1, 'vinte') - 3, 110, 4)
    t = smooth(ramp(f, 0, 90))
    return c, (640, lerp(1200, 1320, t), lerp(1.12, 1.03, t) * (1 + .0004 * f), 0), 'day'


def s2(f):
    c = pista('golden').copy()
    a0 = wt(2, 'dois') - 3
    if f >= a0:
        paste_c(c, calend('2027').resize((300, 286)), 400, 760, back(ramp(f, a0, a0 + 8)))
    m0 = wt(2, 'Mas') - 3
    xis(c, 400, 780, 120, ramp(f, m0, m0 + 10))
    put_car(c, 640, 1560, 600, 0, col='#d9dde3', col2='#d8443c', helm='#d9dde3', spin=False)
    paste_c(c, txt('HAAS', 80, 0), 640, 1180, 1 if f >= wt(2, 'Haas') - 3 else 0)
    o0 = wt(2, 'Ocon') - 3
    ox = 380 - max(0, f - o0) * 14
    put_pil(c, ox, 2000, 820, f, 5, suit='#3a3a44', skin=0, hair='#5a4636', expr='neutral', look=-1)
    b0 = wt(2, 'brasileiro') - 3
    if f >= b0:
        bx = lerp(1400, 930, easeOut(ramp(f, b0, b0 + 14)))
        put_pil(c, bx, 2000, 860, f, 2, suit='#2f9a55', helm='#f5d33a', skin=1, expr='grin', arms='up', look=-.5)
    num(c, 'ANTES!', 880, 900, f, wt(2, 'antes') - 3, 150, 5)
    return c, (640, 1320, 1.03 + .0005 * f, 0), 'golden'


def s3(f):
    c = pista('day').copy()
    put_band(c, 640, 560, 340, f, 1)
    put_pil(c, 380, 1980, 860, f, 2, suit='#2f9a55', helm='#f5d33a', skin=1, expr='grin', arms='hang', look=.5)
    b0 = wt(3, 'Bortoleto') - 3
    s = back(ramp(f, b0, b0 + 8))
    if s > .05:
        put_pil(c, 880, 1980, 860 * s, f, 8, suit='#f5d33a', helm='#2f9a55', skin=0, hair='#2a221e', expr='grin', arms='hang', look=-.5)
        num(c, 'AUDI', 880, 980, f, b0 + 4, 80, 3)
    num(c, 'HAAS', 380, 980, f, wt(3, 'Bortoleto') - 3, 80, -3)
    l0 = wt(3, 'ultima') - 3
    if f >= l0:
        a = int(120 * ramp(f, l0, l0 + 8))
        c.alpha_composite(Image.new('RGBA', c.size, (24, 20, 40, a)))
        paste_c(c, calend('2016').resize((360, 343)), 640, 700, back(ramp(f, wt(3, 'dezesseis') - 6, wt(3, 'dezesseis') + 2)))
        num(c, 'MASSA + NASR', 640, 1010, f, wt(3, 'Massa') - 3, 110, -3)
    t = smooth(ramp(f, 0, 80))
    return c, (640, lerp(1250, 1150, t), lerp(1.12, 1.02, t) * (1 + .0004 * f), 0), 'day'


def s4(f):
    c = pista('rain').copy()
    n0 = wt(4, 'Norris') - 3
    lead = 760 + 10 * math.sin(f * .2)
    put_car(c, lead, 1590, 760, f, col='#f08a2c', col2='#26325e', helm='#ffffff')
    v0 = wt(4, 'Verstappen') - 3
    vx = lerp(-500, 260, easeOut(ramp(f, v0 - 10, v0 + 30)))
    put_car(c, vx, 1820, 720, f, col='#26325e', col2='#d8443c', helm='#f5d33a')
    chuva(c, f)
    num(c, '1º', 760, 1080, f, n0, 170, -6)
    num(c, 'NORRIS', 760, 1250, f, n0 + 4, 100, 3)
    num(c, '+14 SEGUNDOS', 620, 760, f, wt(4, 'catorze') - 3, 100, -3)
    fu = wt(4, 'fundo') - 3
    num(c, 'LÁ DO FUNDO!', 380, 1480, f, fu, 80, 5)
    if f >= n0: put_quad(c, 1000, 520, 220, f, back(ramp(f, n0, n0 + 8)))
    x = lerp(660, 620, smooth(ramp(f, 0, 140)))
    return c, (x, 1380, 1.03 + .0004 * f, -1.5 + .006 * f), 'golden'


def s5(f):
    c = pista('golden').copy()
    d = ImageDraw.Draw(c)
    d.rectangle([150 + 10, 420 + 10, 1092 + 10, 1060 + 10], fill=INK)
    d.rectangle([150, 420, 1092, 1060], fill=hexc('#26325e'), outline=INK, width=8)
    paste_c(c, txt('RESULTADO', 80, 0), 621, 500, 1)
    a0 = wt(5, 'sexto') - 3; b0 = wt(5, 'vigesimo') - 3
    if f >= a0: paste_c(c, txt('16º  BORTOLETO', 86, 0), 621, 680, back(ramp(f, a0, a0 + 8)))
    if f >= b0: paste_c(c, txt('20º  CÂMARA', 86, 0), 621, 870, back(ramp(f, b0, b0 + 8)))
    p0 = wt(5, 'primeira') - 3
    put_pil(c, 380, 2000, 820, f, 8, suit='#f5d33a', helm='#2f9a55', skin=0, hair='#2a221e', expr='grin', arms='hang', look=.5)
    put_pil(c, 860, 2000, 820, f, 2, suit='#2f9a55', skin=1, expr='grin' if f >= p0 else 'neutral', arms='up' if f >= p0 else 'hang', look=-.5, helm='#f5d33a')
    num(c, '1ª CORRIDA!', 640, 1150, f, p0, 100, -5)
    t = smooth(ramp(f, 0, 100))
    return c, (640, lerp(1100, 1300, t), lerp(1.12, 1.04, t), 0), 'golden'


def s6(f):
    c = pista('dusk').copy()
    put_band(c, 330, 700, 240, f, 1)
    g0 = wt(6, 'garantida') - 3
    paste_c(c, calend('2027').resize((300, 286)), 900, 760, back(ramp(f, wt(6, 'Haas') - 6, wt(6, 'Haas') + 2)) if f >= wt(6, 'Haas') - 6 else 0)
    put_car(c, 420, 1620, 700, 0, col='#d9dde3', col2='#d8443c', helm='#f5d33a', spin=False)
    put_pil(c, 880, 2020, 880, f, 2, suit='#2f9a55', skin=1, expr='proud' if f >= g0 else 'grin', arms='up' if f >= g0 else 'hang', look=0, helm='#f5d33a')
    num(c, 'VAGA GARANTIDA!', 630, 1080, f, g0, 80, -4)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * max(0, f - 60))
    return c, (640, 1340, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.engine(0, s.W(0, 'juntos'), .12)
    s.thunk(s.W(0, 'dez') - 3, 140, 1.0)
    s.thunk(s.W(0, 'dois') - 3, 200, .6)
    s.ting(s.W(1, 'Interlagos') - 3, .25)
    s.thunk(s.W(1, 'estreia') - 3, 200, .6)
    s.thunk(s.W(2, 'Mas') - 3, 200, .5)
    s.whoosh(s.W(2, 'Ocon') - 3, .3, .5)
    s.thunk(s.W(2, 'antes') - 3, 160, .7)
    s.thunk(s.W(3, 'dezesseis') - 3, 200, .5)
    s.patter(s.W(4, 'Com') - 3, s.W(4, 'fundo') + 10, 10, .08)
    s.thunk(s.W(4, 'Norris') - 3, 140, .8)
    s.thunk(s.W(5, 'sexto') - 3, 220, .5)
    s.thunk(s.W(5, 'vigesimo') - 3, 220, .5)
    s.ting(s.W(6, 'garantida') - 3, .35)
