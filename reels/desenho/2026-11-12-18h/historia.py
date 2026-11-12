"""Um Café com o Mundo — O MUNDO EXPLICADO (quinta 12/11/2026, 18h).
Tema: surto de ebola no Congo passa de 11 mil casos, o 2º maior da história.
Fontes (conferidas em 12/11/2026):
- AP (11/11/2026, via WRAL "Congo's Ebola outbreak tops 11,000 cases as disease keeps spreading"): ministério da Saúde
  relatou 11.042 infecções e 5.387 mortes na quarta; surto declarado em meados de maio de 2026; vírus Bundibugyo, sem vacina
  nem tratamento conhecido; 8 das 26 províncias; Ituri (~70% dos casos) e Kivu do Norte (principal foco de transmissão nova)
  segundo o ministro Roger Kamba; chegou a Uganda, Quênia e Nigéria; dois ataques recentes mataram 4 profissionais de saúde
  e mais de 1.000 contatos deixaram de ser acompanhados; o surto da África Ocidental (2014-2016) teve ~28 mil infecções e
  mais de 11 mil mortes, e o atual tem pelo menos 3 vezes os casos e as mortes daquele no mesmo período desde a declaração.
- Reuters (via CNBC Africa, 11/11/2026, "Congo's Ebola cases surpass 11,000, government data show"): 11.042 casos confirmados,
  5.387 mortes; 2º maior e 2º mais mortal da história, atrás só da África Ocidental (mais de 28.600 infecções); sem vacinas
  ou tratamentos aprovados para o Bundibugyo; maior alcance geográfico de um surto de ebola na África.
Personagens genéricos (sem pessoas reais). Tom sério, sem humor, sem violência mostrada."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O ebola já infectou mais de onze mil pessoas no Congo, e matou mais de cinco mil.",
    "É o segundo maior surto da história, atrás só do da África Ocidental, de dois mil e catorze.",
    "E este cresce mais rápido: no mesmo tempo, já tem pelo menos três vezes mais casos.",
    "É um tipo raro do vírus, o Bundibugyo. E contra ele não existe vacina nem remédio aprovado.",
    "Já atingiu oito das vinte e seis províncias do país, e chegou a Uganda, Quênia e Nigéria.",
    "No leste, em zona de conflito, dois ataques mataram quatro profissionais de saúde. E mais de mil contatos de doentes deixaram de ser acompanhados.",
    "Por que importa? Sem vacina, a única arma é achar e isolar cada doente a tempo.",
]
CAPTXT = [
    "O ebola já infectou mais de 11 mil pessoas|no Congo, e matou mais de 5 mil.",
    "É o 2º maior surto da história,|atrás só do da África Ocidental, de 2014.",
    "E este cresce mais rápido: no mesmo tempo,|já tem pelo menos 3 vezes mais casos.",
    "É um tipo raro do vírus, o Bundibugyo.|E contra ele não existe|vacina nem remédio aprovado.",
    "Já atingiu 8 das 26 províncias do país,|e chegou a Uganda, Quênia e Nigéria.",
    "No leste, em zona de conflito, dois ataques|mataram 4 profissionais de saúde.|E mais de mil contatos de doentes|deixaram de ser acompanhados.",
    "Por que importa? Sem vacina, a única arma|é achar e isolar cada doente a tempo.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'onze', 6), (0, 'Congo', 6), (0, 'cinco', 6), (1, 'segundo', 6), (1, 'Ocidental', 6), (2, 'tres', 6),
         (3, 'Bundibugyo', 6), (3, 'vacina', 6), (3, 'remedio', 6), (4, 'oito', 6), (4, 'Uganda', 6), (4, 'Nigeria', 6),
         (5, 'quatro', 6), (5, 'mil', 6), (6, 'vacina', 6), (6, 'isolar', 6)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); BLUE = hexc('#2f6fd6'); BLUE_D = hexc('#1f4f9e')
GREEN = hexc('#3aa66a'); GREEN_D = hexc('#287a4c'); GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e')
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); WHITE = (255, 255, 255); GRAY = hexc('#9aa4b4'); GRAY_D = hexc('#6f788a')
PINK = hexc('#e2708a'); PINK_D = hexc('#b04a64')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def politico(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550'):
    """pessoa genérica de roupa social. 600x1000, pés y~975."""
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(suit); P.COAT_D = mul(hexc(suit), .7)
    try:
        img = P.scientist(expr=expr, arms=arms if arms != 'clip' else 'hang', blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
    finally:
        P.COAT, P.COAT_D = oc, od
    p = Pen(600, 1000); p.img = img; p.d = ImageDraw.Draw(img)
    p.poly([(270, 418), (330, 418), (300, 470)], WHITE, 3)
    p.shape([(290, 430), (310, 430), (318, 540), (300, 566), (282, 540)], hexc(tie), mul(hexc(tie), .75), 3, 3)
    return p.img


def put_pol(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'politico', x, feet, h, f, seed, **kw)


@lru_cache(maxsize=4)
def virus(seed=0):
    """partícula de vírus genérica (bola com espinhos). 300x300"""
    p = Pen(300, 300); rnd = random.Random(seed)
    for i in range(12):
        a = i * math.pi * 2 / 12 + rnd.random() * .2
        x0, y0 = 150 + 88 * math.cos(a), 150 + 88 * math.sin(a)
        x1, y1 = 150 + 128 * math.cos(a), 150 + 128 * math.sin(a)
        p.stroke([(x0, y0), (x1, y1)], 9)
        p.dot(x1, y1, 15, PINK, 4)
    p.shape(ell_pts(150, 150, 96, 96, 40), PINK, PINK_D, 7, 10)
    for i in range(5):
        a = rnd.random() * 6.28; r = rnd.random() * 50
        p.dot(150 + r * math.cos(a), 150 + r * math.sin(a), 10 + rnd.random() * 8, PINK_D, 0)
    return fin(p)


@lru_cache(maxsize=2)
def seringa():
    """seringa de vacina. 520x160"""
    p = Pen(520, 160)
    p.shape([(30, 50), (330, 50), (330, 110), (30, 110)], hexc('#e8f4fb'), hexc('#a9c6d8'), 6, 6)
    p.poly([(34, 56), (200, 56), (200, 104), (34, 104)], hexc('#7cc4e8'))
    for x in range(80, 330, 50): p.stroke([(x, 50), (x, 70)], 4)
    p.shape([(330, 70), (380, 70), (380, 90), (330, 90)], hexc('#c9c9d2'), hexc('#8a8a96'), 5, 3)
    p.stroke([(380, 80), (500, 80)], 6)
    p.shape([(4, 30), (30, 30), (30, 130), (4, 130)], BLUE, BLUE_D, 5, 4)
    return fin(p)


@lru_cache(maxsize=4)
def boneco(col='gray'):
    """ícone simples de pessoa. 120x180"""
    h, d = {'gray': (GRAY, GRAY_D), 'red': (PINK, PINK_D), 'blue': (BLUE, BLUE_D)}[col]
    p = Pen(120, 180)
    p.shape(ell_pts(60, 45, 34, 34, 28), h, d, 5, 5)
    p.shape([(16, 175), (16, 120), (30, 92), (90, 92), (104, 120), (104, 175)], h, d, 5, 6)
    return fin(p)


@lru_cache(maxsize=2)
def hospital():
    """prédio genérico de hospital (placa H). 900x900, base y~890."""
    p = Pen(900, 900)
    p.shape([(120, 260), (780, 260), (780, 890), (120, 890)], STONE, STONE_D, 7, 16)
    p.shape([(100, 230), (800, 230), (800, 270), (100, 270)], hexc('#d6d0c4'), STONE_D, 5, 4)
    for r in range(4):
        for k in range(4):
            x, y = 190 + k * 150, 310 + r * 120
            p.shape([(x, y), (x + 90, y), (x + 90, y + 72), (x, y + 72)], hexc('#9fd0ee'), hexc('#6aa6cc'), 4, 3)
    p.shape([(370, 760), (530, 760), (530, 890), (370, 890)], hexc('#7cc4e8'), hexc('#4f8fb8'), 5, 4)
    p.shape([(330, 40), (570, 40), (570, 230), (330, 230)], BLUE, BLUE_D, 6, 8)
    p.shape([(395, 80), (425, 80), (425, 190), (395, 190)], WHITE, hexc('#dfe6f0'), 3, 2)
    p.shape([(475, 80), (505, 80), (505, 190), (475, 190)], WHITE, hexc('#dfe6f0'), 3, 2)
    p.shape([(420, 120), (480, 120), (480, 150), (420, 150)], WHITE, hexc('#dfe6f0'), 3, 2)
    return fin(p)


@lru_cache(maxsize=2)
def marcador():
    """alfinete de mapa. 200x280, ponta y~270"""
    p = Pen(200, 280)
    p.shape([(100, 272), (30, 120), (40, 60), (100, 20), (160, 60), (170, 120)], RED, RED_D, 6, 8)
    p.dot(100, 100, 34, WHITE, 5)
    return fin(p)


@lru_cache(maxsize=2)
def selo_ok():
    p = Pen(300, 300)
    p.shape(ell_pts(150, 150, 130, 130, 40), GREEN, GREEN_D, 7, 10)
    p.stroke([(90, 155), (135, 200), (215, 105)], 22, WHITE)
    return fin(p)


@lru_cache(maxsize=2)
def calendario():
    p = Pen(500, 520)
    p.shape([(20, 60), (480, 60), (480, 500), (20, 500)], WHITE, hexc('#c9c9d2'), 6, 10)
    p.shape([(20, 60), (480, 60), (480, 160), (20, 160)], BLUE, BLUE_D, 6, 6)
    for x in (120, 380): p.shape([(x - 14, 20), (x + 14, 20), (x + 14, 100), (x - 14, 100)], hexc('#6b6b70'), hexc('#4a4a50'), 4, 3)
    for r in range(4):
        for k in range(5):
            x, y = 70 + k * 90, 210 + r * 75
            p.poly([(x, y), (x + 50, y), (x + 50, y + 40), (x, y + 40)], hexc('#e6e9ef'), 3)
    return fin(p)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def put_virus(c, x, y, f, f0, size=150, seed=0):
    if f < f0: return
    s = back(ramp(f, f0, f0 + 10))
    im = virus(seed % 3).resize((int(size), int(size)))
    im = im.rotate((f * 1.5 + seed * 40) % 360, resample=Image.BICUBIC)
    paste_c(c, im, x + 14 * math.sin(f * .05 + seed), y + 14 * math.cos(f * .045 + seed * 2), s)


def barra(c, x, base, w, h, col, f, f0, top_lab=None):
    if f < f0: return
    d = ImageDraw.Draw(c)
    hh = h * easeOut(ramp(f, f0, f0 + 14))
    d.rectangle([x - w / 2 + 8, base - hh + 8, x + w / 2 + 8, base + 8], fill=INK)
    d.rectangle([x - w / 2, base - hh, x + w / 2, base], fill=col, outline=INK, width=6)
    if top_lab: paste_c(c, txt(top_lab, 90, -3), x, base - hh - 70, back(ramp(f, f0 + 6, f0 + 14)))



@lru_cache(maxsize=2)
def lupa():
    p = Pen(400, 400)
    p.stroke([(250, 250), (370, 370)], 34, hexc('#6b4a2e'))
    p.shape(ell_pts(170, 170, 130, 130, 40), hexc('#c9e6f5'), hexc('#8fb8d0'), 10, 6)
    return fin(p)


def mar_bg():
    c = Image.new('RGBA', (BW, BH), SEA + (255,))
    d = ImageDraw.Draw(c)
    for y in range(300, 2100, 90):
        for x in range(40 + (y // 90 % 2) * 100, BW, 200):
            d.line([(x, y), (x + 40, y - 8), (x + 80, y)], fill=SEA_D, width=5)
    return c


SEA = hexc('#3d6f9e'); SEA_D = hexc('#2c5580'); LAND = hexc('#d9c08a'); LAND_D = hexc('#b09660')


def LL(lon, lat):
    return (140 + (lon + 18) * 14, 500 + (37 - lat) * 14)


AFRICA = [(-17, 21), (-16, 28), (-10, 30), (-6, 36), (10, 37), (11, 33), (20, 31), (25, 32), (32, 31), (34, 28), (38, 18),
          (43, 12), (51, 11.8), (50, 9), (47, 4), (41, -2), (40, -10), (40, -15), (35, -24), (33, -27), (30, -31), (25, -34),
          (20, -35), (18, -33), (15, -27), (12, -18), (13, -12), (12, -5), (9, -1), (9, 4), (5, 6), (1, 6), (-4, 5),
          (-8, 4.5), (-12, 7.5), (-15, 11), (-17, 15)]
MADA = [(44, -25), (47, -25), (50, -15), (49, -12), (44, -17)]
CONGO = [(12.2, -6), (13, -4.6), (16, -4), (17.6, -1), (18, 2.5), (18.6, 4.2), (22, 4.5), (25, 5.2), (27.4, 5), (30, 3.6),
         (31.2, 2.2), (29.6, -1.4), (29.2, -4.5), (30.6, -8), (28.8, -8.5), (29.5, -12.3), (27.3, -12), (25, -11.3),
         (22.4, -11), (21.8, -7.3), (19.4, -8), (17.6, -8), (16.2, -5.9)]
UGANDA = LL(32.5, 1.5); KENYA = LL(37.8, 0.3); NIGERIA = LL(8, 9.5); ITURI = LL(29.6, 1.8); KIVU = LL(28.9, -0.8)
CONGO_C = LL(23.5, -2.5)


@lru_cache(maxsize=2)
def africa_img(red=True):
    c = mar_bg()
    d = ImageDraw.Draw(c)
    for pts in (AFRICA, MADA):
        P2 = [LL(*q) for q in pts]
        d.polygon([(x + 10, y + 12) for x, y in P2], fill=INK)
        d.polygon(P2, fill=LAND, outline=INK, width=6)
    if red:
        P2 = [LL(*q) for q in CONGO]
        d.polygon([(x + 6, y + 8) for x, y in P2], fill=LAND_D)
        d.polygon(P2, fill=PINK, outline=INK, width=6)
    return c


@lru_cache(maxsize=2)
def provincias():
    """Congo dividido em 26 'quadradinhos' (esquemático), 8 em vermelho."""
    c = mar_bg()
    d = ImageDraw.Draw(c)
    return c


def quadro_branco(c):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([150 + 12, 300 + 14, 1092 + 12, 1560 + 14], 30, fill=INK)
    d.rounded_rectangle([150, 300, 1092, 1560], 30, fill=hexc('#f4f1ea'), outline=INK, width=8)


def num2(c, s, x, y, f, f0, size=100, rot=-3):
    num(c, s, x, y, f, f0, size, rot)


def sirene(c, x, y, f, r=34):
    d = ImageDraw.Draw(c)
    on = (f // 7) % 2 == 0
    d.rounded_rectangle([x - r, y - r * .2, x + r, y + r * .9], 8, fill=hexc('#4a4a50'), outline=INK, width=4)
    d.pieslice([x - r, y - r * 1.2, x + r, y + r * .8], 180, 360, fill=RED if on else RED_D, outline=INK, width=5)
    if on:
        dd = ImageDraw.Draw(c, 'RGBA')
        dd.ellipse([x - r * 3, y - r * 3, x + r * 3, y + r * 2], fill=(255, 80, 60, 50))


@lru_cache(maxsize=2)
def remedio():
    """frasco de remédio com comprimidos. 260x340"""
    p = Pen(260, 340)
    p.shape([(40, 90), (220, 90), (220, 320), (40, 320)], hexc('#e8a94a'), hexc('#b97e2c'), 6, 8)
    p.shape([(60, 150), (200, 150), (200, 260), (60, 260)], WHITE, hexc('#d9d9e0'), 4, 3)
    p.stroke([(90, 185), (170, 185)], 6, RED); p.stroke([(90, 220), (150, 220)], 6, GRAY_D)
    p.shape([(30, 30), (230, 30), (230, 92), (30, 92)], WHITE, hexc('#c9c9d2'), 6, 6)
    return fin(p)


def cruz(c, x, y, s, f, f0):
    a = back(ramp(f, f0, f0 + 8))
    if a <= .05: return
    d = ImageDraw.Draw(c)
    r = s * a
    d.line([(x - r, y - r), (x + r, y + r)], fill=INK, width=26); d.line([(x - r, y + r), (x + r, y - r)], fill=INK, width=26)
    d.line([(x - r, y - r), (x + r, y + r)], fill=RED, width=16); d.line([(x - r, y + r), (x + r, y - r)], fill=RED, width=16)


def pin(c, x, y, f, f0, s=.5):
    if f < f0: return
    paste_c(c, marcador().resize((int(200 * s), int(280 * s))), x, y - 130 * s, back(ramp(f, f0, f0 + 8)))
    rings(c, x, y, f, f0, 30, .6 * s / .5)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = africa_img(True).copy()
    c0 = wt(0, 'onze') - 3
    for i in range(9):
        a = i * 2.4; r = 60 + (i % 3) * 70
        put_virus(c, CONGO_C[0] + r * math.cos(a), CONGO_C[1] + r * math.sin(a) * .8, f, c0 - 24 + i * 3, 70 + (i % 3) * 18, i)
    num(c, 'EBOLA', 640, 330, f, wt(0, 'ebola') - 3, 130, -3)
    num(c, '+11 MIL CASOS', 640, 480, f, c0, 100, 3)
    num(c, 'CONGO', 520, 1180, f, wt(0, 'Congo') - 3, 90, -3)
    m0 = wt(0, 'cinco') - 3
    num(c, '+5 MIL MORTES', 640, 1420, f, m0, 96, -3)
    z = lerp(1.5, 1.0, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, c0)
    cy = lerp(1050, 950, easeOut(ramp(f, 0, 60)))
    return c, (640, cy + k * 8, z, k), 'dusk'


def s1(f):
    c = CEN('escritorio', 'dusk').copy()
    quadro_branco(c)
    num(c, '2º MAIOR SURTO', 640, 380, f, wt(1, 'segundo') - 3, 100, -3)
    num(c, 'DA HISTÓRIA', 640, 520, f, wt(1, 'historia') - 3, 84, 3)
    o0 = wt(1, 'Ocidental') - 6
    barra(c, 440, 1380, 260, 600, GRAY, f, o0, '+28 MIL')
    barra(c, 820, 1380, 260, 235, PINK, f, wt(1, 'segundo') - 3, '11 MIL')
    num(c, 'ÁFRICA OCID.', 440, 1440, f, o0, 50, 0)
    num(c, '2014-2016', 440, 1505, f, wt(1, 'catorze') - 3, 44, 0)
    num(c, 'CONGO 2026', 820, 1450, f, wt(1, 'segundo') - 3, 50, 0)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, o0, .6)
    return c, (640, lerp(980, 1000, t) + k * 6, lerp(1.06, 0.98, t) * (1 + .0004 * f), k), 'dusk'


def s2(f):
    c = CEN('escritorio', 'dusk').copy()
    quadro_branco(c)
    paste_c(c, calendario().resize((260, 270)), 640, 640, back(ramp(f, 0, 8)))
    num(c, 'NO MESMO TEMPO', 640, 420, f, wt(2, 'mesmo') - 3, 80, -3)
    put_virus(c, 380, 1050, f, 4, 160, 1)
    num(c, '2014', 380, 1270, f, 4, 70, 0)
    t0 = wt(2, 'tres') - 3
    for i, (x, y) in enumerate(((800, 920), (980, 1000), (880, 1140))):
        put_virus(c, x, y, f, t0 + i * 3, 150, i + 4)
    num(c, '2026', 890, 1300, f, t0, 70, 0)
    num(c, '3X MAIS CASOS', 640, 1460, f, t0 + 4, 92, 3)
    z = lerp(0.98, 1.06, smooth(ramp(f, 0, 120))) + .0003 * f
    k = kick(f, t0, .7)
    return c, (640 + 14 * math.sin(f * .04), 1000 + k * 6, z, k), 'dusk'


def s3(f):
    c = CEN('lab', 'dusk').copy()
    b0 = wt(3, 'Bundibugyo') - 3
    put_virus(c, 640, 860, f, 0, 380, 2)
    num(c, 'TIPO RARO', 640, 380, f, wt(3, 'raro') - 3, 90, -3)
    num(c, 'BUNDIBUGYO', 640, 1150, f, b0, 100, 3)
    v0 = wt(3, 'vacina') - 3
    if f >= v0:
        im = seringa().resize((360, 111)).rotate(-20, expand=True, resample=Image.BICUBIC)
        paste_c(c, im, 380, 1330, back(ramp(f, v0, v0 + 8)))
        cruz(c, 380, 1330, 120, f, v0 + 4)
        num(c, 'SEM VACINA', 380, 1500, f, v0, 60, -2)
    r0 = wt(3, 'remedio') - 3
    if f >= r0:
        paste_c(c, remedio().resize((180, 235)), 900, 1320, back(ramp(f, r0, r0 + 8)))
        cruz(c, 900, 1320, 120, f, r0 + 4)
        num(c, 'SEM REMÉDIO', 900, 1500, f, r0, 60, 2)
    t = smooth(ramp(f, 0, 200))
    k = kick(f, v0, .6)
    return c, (640, lerp(950, 1080, t) + k * 6, lerp(1.2, 1.0, t) * (1 + .0003 * f), k), 'dusk'


def s4(f):
    c = africa_img(True).copy()
    o0 = wt(4, 'oito') - 3
    num(c, '8 DE 26', 640, 330, f, o0, 120, -3)
    num(c, 'PROVÍNCIAS', 640, 470, f, o0 + 4, 80, 3)
    if f >= o0:
        for i, (lo, la) in enumerate(((29.6, 1.8), (28.9, -0.8), (27, 2.5), (25, -1), (28.5, -3.5), (24, 2), (27.5, -6), (21, -2.5))):
            x, y = LL(lo, la)
            if f >= o0 + i * 2:
                d = ImageDraw.Draw(c)
                r = 20 * back(ramp(f, o0 + i * 2, o0 + i * 2 + 8))
                d.ellipse([x - r, y - r, x + r, y + r], fill=RED_D, outline=INK, width=4)
    for k_, (nome, pt, w) in enumerate((('UGANDA', UGANDA, 'Uganda'), ('QUÊNIA', KENYA, 'Quenia'), ('NIGÉRIA', NIGERIA, 'Nigeria'))):
        f0 = wt(4, w) - 3
        pin(c, pt[0], pt[1], f, f0, .45)
        dx = {'UGANDA': 150, 'QUÊNIA': 140, 'NIGÉRIA': 0}[nome]
        dy = {'UGANDA': -150, 'QUÊNIA': 20, 'NIGÉRIA': -170}[nome]
        num(c, nome, pt[0] + dx, pt[1] + dy, f, f0, 60, -2)
    t = smooth(ramp(f, 0, 220))
    k = kick(f, o0, .6)
    return c, (lerp(700, 640, t), lerp(1000, 920, t) + k * 6, lerp(1.25, 1.02, t) * (1 + .0003 * f), lerp(1, -1, t)), 'dusk'


def s5(f):
    c = CEN('cidade', 'dusk').copy()
    m0 = wt(5, 'mil') - 3
    if f < m0 - 2:
        paste_c(c, hospital().resize((720, 720)), 640, 1200, 1)
        sirene(c, 640, 820, f)
        num(c, 'ZONA DE CONFLITO', 640, 360, f, wt(5, 'conflito') - 3, 76, -3)
        q0 = wt(5, 'quatro') - 3
        num(c, '4 PROFISSIONAIS', 640, 520, f, q0, 96, 3)
        num(c, 'DE SAÚDE MORTOS', 640, 650, f, q0 + 4, 80, -2)
        t = ramp(f, 0, m0)
        return c, (640 + 12 * math.sin(f * .04), lerp(1000, 1030, t), lerp(1.0, 1.1, t), lerp(0, 1.5, t)), 'dusk'
    for r in range(4):
        for k in range(5):
            i = r * 5 + k
            st = m0 - 2 + i
            if f < st: continue
            s = back(ramp(f, st, st + 8))
            x, y = 380 + k * 120, 820 + r * 160
            paste_c(c, boneco('gray').resize((int(100 * s) + 1, int(150 * s) + 1)), x, y, 1)
            if i % 3 == 1 and f >= st + 6:
                paste_c(c, txt('?', 60, 6), x + 40, y - 80, back(ramp(f, st + 6, st + 12)))
    num(c, '+1.000 CONTATOS', 640, 420, f, m0, 96, -3)
    num(c, 'SEM ACOMPANHAMENTO', 640, 570, f, wt(5, 'acompanhados') - 3, 66, 3)
    t = ramp(f - m0, 0, 90)
    return c, (640, 1000, lerp(1.12, 1.0, smooth(t)) * (1 + .0005 * f), .6 * math.sin(f * .04)), 'dusk'


def s6(f):
    c = CEN('cidade', 'dusk').copy()
    v0 = wt(6, 'vacina') - 3
    if f < v0:
        paste_c(c, txt('POR QUE IMPORTA?', 90, -4), 640, 520, back(ramp(f, 0, 8)))
    else:
        num(c, 'SEM VACINA', 640, 380, f, v0, 90, -3)
    a0 = wt(6, 'achar') - 3
    num(c, 'ACHAR E ISOLAR', 640, 540, f, a0, 92, 3)
    num(c, 'CADA DOENTE A TEMPO', 640, 680, f, wt(6, 'doente') - 3, 66, -2)
    for i, x in enumerate((780, 900, 1020)):
        paste_c(c, boneco('red' if i == 1 else 'gray').resize((110, 165)), x, 1300, 1)
    if f >= a0:
        tt = smooth(ramp(f, a0, a0 + 30))
        paste_c(c, lupa().resize((220, 220)) if lupa().size[0] > 220 else lupa(), lerp(700, 905, tt), 1250, back(ramp(f, a0, a0 + 8)))
    put_sci(c, 400, 1640, 640, f, 7, arms='point', skin=2, hair='#2a221e', expr='stern', look=1)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) + .0005 * f
    k = kick(f, a0, .5)
    return c, (640, 1040 + k * 6, z, lerp(0, 1.5, smooth(ramp(f, 0, 120)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'onze') - 3, 150, .8)
    s.thunk(s.W(0, 'cinco') - 3, 120, .6)
    s.thunk(s.W(1, 'segundo') - 3, 160, .6)
    s.ting(s.W(1, 'Ocidental') - 3, .2)
    s.thunk(s.W(2, 'tres') - 3, 170, .7)
    s.ting(s.W(3, 'Bundibugyo') - 3, .2)
    s.thunk(s.W(3, 'vacina') - 3, 130, .5)
    s.thunk(s.W(3, 'remedio') - 3, 130, .5)
    s.ting(s.W(4, 'oito') - 3, .25)
    s.ting(s.W(4, 'Uganda') - 3, .15)
    s.ting(s.W(4, 'Quenia') - 3, .15)
    s.ting(s.W(4, 'Nigeria') - 3, .15)
    s.thunk(s.W(5, 'quatro') - 3, 120, .5)
    s.thunk(s.W(5, 'mil') - 3, 150, .5)
    s.whoosh(s.W(6, 'achar') - 3, .3, .4)
