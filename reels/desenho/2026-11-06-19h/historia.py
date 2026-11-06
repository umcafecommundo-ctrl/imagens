"""Um Café com o Mundo — O MUNDO EXPLICADO (sexta 06/11/2026, 19h).
Tema: estreito de Ormuz — Irã libera navios de 4 países e manda proposta nuclear aos EUA pelo Catar.
Fontes (conferidas em 06/11/2026):
- Al Jazeera, 06/11/2026 "Why is Iran exempting India, China, Qatar, Iraq from Hormuz restrictions?": guerra EUA-Israel x Irã
  começou em 28/02; Irã fechou na prática o estreito; na terça (03/11) Amir Hayat Moqaddam, vice-presidente da comissão de
  Segurança Nacional do Parlamento iraniano, disse à ISNA que navios de Índia, China, Iraque e Catar passam livremente;
  Índia e China pagariam taxa de passagem; em outubro passaram 10,23 milhões de barris/dia de petróleo do Golfo, ~42% para a
  China (Kpler); mais de 120 navios comerciais atingidos na região desde o início da guerra.
- Reuters via Arab News (06/11/2026): alto funcionário iraniano diz que o Irã mandou aos EUA uma proposta nuclear pelo Catar,
  que só será discutida depois que Washington cumprir 7 exigências (fim de sanções, bens congelados, reparações...);
  Trump não descartou retomar operações militares depois das eleições.
Personagens genéricos (sem traços de pessoas reais). Tom sério, luz 'dusk', sem violência mostrada."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O Irã agora escolhe quais navios podem passar pelo estreito de Ormuz.",
    "É a passagem de boa parte do petróleo do mundo, quase fechada desde fevereiro, com a guerra.",
    "Agora, um parlamentar iraniano disse que navios da Índia, da China, do Iraque e do Catar passam, e Índia e China pagariam taxa.",
    "Em outubro, passaram mais de dez milhões de barris por dia, quarenta e dois por cento para a China.",
    "Mas o risco segue: mais de cento e vinte navios já foram atingidos desde o começo da guerra.",
    "E, pelo Catar, o Irã mandou aos Estados Unidos uma proposta nuclear, com sete condições.",
    "Por que isso importa? Ormuz mexe no preço do petróleo e do combustível aqui no Brasil. Agora, o mundo espera a resposta de Trump.",
]
CAPTXT = [
    "O Irã agora escolhe quais navios|podem passar pelo estreito de Ormuz.",
    "É a passagem de boa parte do petróleo do mundo,|quase fechada desde fevereiro, com a guerra.",
    "Agora, um parlamentar iraniano disse que navios da Índia,|da China, do Iraque e do Catar passam,|e Índia e China pagariam taxa.",
    "Em outubro, passaram mais de 10 milhões de barris por dia,|42% para a China.",
    "Mas o risco segue: mais de 120 navios|já foram atingidos desde o começo da guerra.",
    "E, pelo Catar, o Irã mandou aos Estados Unidos|uma proposta nuclear, com 7 condições.",
    "Por que isso importa? Ormuz mexe no preço do petróleo|e do combustível aqui no Brasil.|Agora, o mundo espera a resposta de Trump.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'escolhe', 4), (0, 'Ormuz', 4), (1, 'petroleo', 4), (1, 'fevereiro', 4), (2, 'India', 4), (2, 'Catar', 4),
         (2, 'taxa', 6), (3, 'dez', 6), (3, 'quarenta', 6), (4, 'cento', 6), (5, 'Catar', 4), (5, 'sete', 6),
         (6, 'combustivel', 4), (6, 'Trump', 6)]

SEA = hexc('#3d7fb8'); SEA_D = hexc('#2c6396'); SAND = hexc('#e2c48e'); SAND_D = hexc('#b89a64')
RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); WHITE = (255, 255, 255)
GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e')


# ------------------------------------------------------------------ desenhos novos
def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


@lru_cache(maxsize=2)
def mapa_img():
    """mapa simples do estreito: Irã em cima, península embaixo, golfo à esquerda. palco inteiro."""
    S = 2
    im = Image.new('RGBA', (BW * S, BH * S), SEA + (255,))
    d = ImageDraw.Draw(im)
    for y in range(820, 1600, 70):
        for x in range(60 + (y // 70 % 2) * 90, BW, 180):
            d.line([(x * S, y * S), ((x + 40) * S, (y - 8) * S), ((x + 80) * S, y * S)], fill=SEA_D, width=4 * S)
    top = [(-20, -20), (BW + 20, -20), (BW + 20, 760), (1100, 790), (960, 830), (840, 900), (760, 975), (650, 990),
           (560, 930), (430, 860), (280, 820), (120, 800), (-20, 790)]
    bot = [(-20, BH + 20), (-20, 1430), (180, 1400), (360, 1380), (520, 1330), (620, 1230), (680, 1150), (730, 1140),
           (780, 1200), (820, 1320), (960, 1400), (1100, 1440), (BW + 20, 1450), (BW + 20, BH + 20)]
    for pts, dy in ((top, -18), (bot, 18)):
        P2 = [(x * S, y * S) for x, y in pts]
        d.polygon(P2, fill=INK)
        d.polygon([(x, y - 7 * S if dy < 0 else y + 7 * S) for x, y in P2], fill=SAND_D)
        d.polygon([(x, y + dy * S if dy < 0 else y + dy * S) for x, y in P2], fill=SAND)
    return im.resize((BW, BH), Image.LANCZOS)


def navio(col='#c0392b'):
    """petroleiro de lado, proa à direita. 700x300."""
    p = Pen(700, 300)
    h = hexc(col)
    p.shape([(20, 150), (690, 150), (640, 270), (60, 270)], h, mul(h, .7), 5, 10)
    p.shape([(40, 230), (660, 230), (640, 270), (60, 270)], hexc('#2a2a33'), hexc('#1a1a20'), 4, 3)
    p.shape([(30, 132), (680, 132), (690, 152), (20, 152)], hexc('#e9e4da'), hexc('#bdb6a8'), 4, 3)
    p.shape([(60, 40), (190, 40), (190, 134), (60, 134)], WHITE, hexc('#c9c9d2'), 5, 6)
    for x in (80, 115, 150): p.poly([(x, 60), (x + 22, 60), (x + 22, 80), (x, 80)], hexc('#7fb6e0'), 3)
    p.shape([(140, 0), (180, 0), (180, 42), (140, 42)], h, mul(h, .7), 4, 3)
    for x in range(250, 640, 90): p.stroke([(x, 128), (x, 110), (x + 50, 110), (x + 50, 128)], 5, hexc('#8a8f99'))
    return p.img


@lru_cache(maxsize=2)
def barril():
    p = Pen(200, 260)
    p.shape([(30, 30), (170, 30), (178, 130), (170, 230), (30, 230), (22, 130)], hexc('#2f3a4a'), hexc('#1e2633'), 5, 10)
    p.shape(ell_pts(100, 32, 70, 18, 24), hexc('#46566b'), hexc('#2f3a4a'), 4, 3)
    for y in (90, 170): p.stroke([(24, y), (176, y)], 6, hexc('#5c6d84'))
    p.poly([(60, 115), (140, 115), (140, 145), (60, 145)], GOLD, 3)
    return fin(p)


@lru_cache(maxsize=2)
def moeda():
    p = Pen(160, 160)
    p.shape(ell_pts(80, 80, 66, 66, 32), GOLD, GOLD_D, 5, 6)
    p.arc(80, 80, 44, 44, 0, 360, 4, GOLD_D)
    return fin(p)


@lru_cache(maxsize=2)
def envelope():
    p = Pen(300, 210)
    p.shape([(10, 10), (290, 10), (290, 200), (10, 200)], WHITE, hexc('#c9c9d2'), 5, 6)
    p.stroke([(10, 10), (150, 120), (290, 10)], 5)
    p.dot(150, 120, 22, RED, 3)
    return fin(p)


@lru_cache(maxsize=2)
def bomba():
    """bomba de combustível genérica. 300x520"""
    p = Pen(300, 520)
    p.shape([(40, 60), (220, 60), (220, 500), (40, 500)], hexc('#3aa66a'), hexc('#287a4c'), 6, 12)
    p.shape([(70, 100), (190, 100), (190, 220), (70, 220)], WHITE, hexc('#c9c9d2'), 4, 4)
    p.poly([(90, 130), (170, 130), (170, 160), (90, 160)], hexc('#2a2a33'))
    p.shape([(20, 490), (240, 490), (240, 515), (20, 515)], hexc('#6b6b70'), hexc('#4a4a50'), 4, 3)
    p.stroke([(220, 260), (270, 260), (280, 420), (250, 440)], 10, hexc('#2a2a33'))
    p.shape([(240, 230), (275, 230), (275, 290), (240, 290)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 3)
    return fin(p)


def politico(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550'):
    """pessoa genérica de terno (personagem 'feijão'). 600x1000, pés y~975."""
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(suit); P.COAT_D = mul(hexc(suit), .7)
    try:
        img = P.scientist(expr=expr, arms=arms if arms != 'clip' else 'hang', blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
    finally:
        P.COAT, P.COAT_D = oc, od
    p = Pen(600, 1000); p.img = img; p.d = ImageDraw.Draw(img)
    p.poly([(270, 418), (330, 418), (300, 470)], (255, 255, 255), 3)
    p.shape([(290, 430), (310, 430), (318, 540), (300, 566), (282, 540)], hexc(tie), mul(hexc(tie), .75), 3, 3)
    return p.img


def put_pol(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'politico', x, feet, h, f, seed, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def nav(c, x, y, w, col='#c0392b', bob=0.0):
    im = sprite('navio', (('col', col),), int(w * 300 / 700), 700 / 300, False)
    paste_c(c, im, x, y + 6 * math.sin(bob))


def cancela(c, f, ang):
    """poste no cabo do Irã e braço listrado; ang 0 = fechado (horizontal p/ baixo do canal), 80 = aberto."""
    d = ImageDraw.Draw(c)
    px, py = 705, 985
    d.rounded_rectangle([px - 22, py - 140, px + 22, py + 10], 10, fill=hexc('#6b6b70'), outline=INK, width=5)
    a = math.radians(90 - ang)
    L = 210
    n = 6
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0, y0 = px + L * t0 * math.cos(a), py + L * t0 * math.sin(a)
        x1, y1 = px + L * t1 * math.cos(a), py + L * t1 * math.sin(a)
        d.line([(x0, y0), (x1, y1)], fill=INK, width=30)
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0, y0 = px + L * t0 * math.cos(a), py + L * t0 * math.sin(a)
        x1, y1 = px + L * t1 * math.cos(a), py + L * t1 * math.sin(a)
        d.line([(x0, y0), (x1, y1)], fill=RED if i % 2 == 0 else WHITE, width=20)
    d.ellipse([px - 18, py - 18, px + 18, py + 18], fill=hexc('#4a4a50'), outline=INK, width=4)


def fumaca(c, x, y, f, seed=0, s=1.0):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(6):
        t = ((f * .6 + i * 17 + seed * 7) % 100) / 100
        r = (30 + 60 * t) * s
        xx = x + 40 * math.sin(t * 5 + seed) * s; yy = y - 260 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=(110, 110, 120, a))


def pais(c, s, x, y, f, f0, col):
    if f < f0: return
    sc = back(ramp(f, f0, f0 + 8))
    paste_c(c, txt(s, 88, -3), x, y - 100 * sc, sc)
    nav(c, x, y + 50, 380 * sc, col, f * .15 + x)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = mapa_img().copy()
    e0 = wt(0, 'escolhe') - 3
    # navio 1 parado antes da cancela; cancela abre; navio 2 passa
    ang = 80 * smooth(ramp(f, e0, e0 + 10))
    x2 = lerp(260, 1150, smooth(ramp(f, e0 + 6, e0 + 70)))
    nav(c, lerp(-200, 300, smooth(ramp(f, 0, e0))), 1065, 300, '#2e7d4f', f * .2)
    nav(c, x2, 1065, 300, '#c0392b', f * .2 + 1)
    cancela(c, f, ang)
    num(c, 'IRÃ', 560, 720, f, 0, 120, -3)
    num(c, 'ORMUZ', 820, 1260, f, wt(0, 'Ormuz') - 3, 100, 4)
    num(c, 'QUEM PASSA?', 620, 520, f, wt(0, 'navios') - 3, 100, -3)
    z = lerp(1.45, 1.12, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, e0)
    return c, (680, 1080 + k * 8, z, k), 'dusk'


def s1(f):
    c = mapa_img().copy()
    p0 = wt(1, 'petroleo') - 3
    b = barril().resize((110, 143))
    for i in range(7):
        t = ((f - p0) * .012 + i / 7) % 1
        if f >= p0:
            paste_c(c, b, lerp(80, 1180, t), 1065 + 10 * math.sin(f * .2 + i), back(ramp(f, p0 + i * 2, p0 + i * 2 + 8)))
    g0 = wt(1, 'guerra') - 3
    for k_, (x, y) in enumerate(((380, 760), (980, 730), (560, 1420))):
        if f >= g0: fumaca(c, x, y, f - g0, k_, .9)
    cancela(c, f, 80 * (1 - smooth(ramp(f, wt(1, 'fechada') - 3, wt(1, 'fechada') + 6))))
    num(c, 'PETRÓLEO', 620, 680, f, p0, 110, -3)
    num(c, 'DESDE FEVEREIRO', 620, 520, f, wt(1, 'fevereiro') - 3, 90, 3)
    t = smooth(ramp(f, 0, 120))
    return c, (640, lerp(1150, 1050, t), lerp(1.0, 1.1, t), lerp(0, -1.5, t)), 'dusk'


def s2(f):
    c = BG('dusk').copy()
    d = ImageDraw.Draw(c)
    s0_ = wt(2, 'disse') - 3
    put_pol(c, 230, 1520, 760, f, 3, skin=1, hair='#2a221e', tie='#3aa66a', suit='#3a3a44',
            arms='point' if f >= s0_ else 'hang', expr='stern' if f >= s0_ else 'neutral', look=1)
    pais(c, 'ÍNDIA', 640, 560, f, wt(2, 'India') - 3, '#e07b2a')
    pais(c, 'CHINA', 1010, 560, f, wt(2, 'China') - 3, '#c0392b')
    pais(c, 'IRAQUE', 640, 900, f, wt(2, 'Iraque') - 3, '#2e7d4f')
    pais(c, 'CATAR', 1010, 900, f, wt(2, 'Catar') - 3, '#7a2a4a')
    t0 = wt(2, 'taxa') - 3
    if f >= t0:
        m = moeda()
        for i in range(4):
            tt = clamp((f - t0 - i * 4) / 16)
            if tt > 0: paste_c(c, m.resize((90, 90)), lerp(820, 420 + i * 40, tt), lerp(660, 1200, tt) - 120 * math.sin(tt * math.pi), 1)
        num(c, 'TAXA', 820, 1200, f, t0, 130, 6)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0005 * f)
    k = kick(f, t0, .7)
    return c, (640, 1000 + k * 6, z, k), 'dusk'


def s3(f):
    c = BG('dusk').copy()
    d = ImageDraw.Draw(c)
    d0 = wt(3, 'dez') - 3
    b = barril().resize((150, 195))
    for i in range(10):
        r, col = divmod(i, 4)
        bx = 230 + col * 150 + (r % 2) * 75; by = 1480 - r * 175
        if f >= d0 + i * 2: paste_c(c, b, bx, by - 60 * (1 - back(ramp(f, d0 + i * 2, d0 + i * 2 + 8))), 1)
    num(c, 'OUTUBRO', 560, 480, f, 0, 100, -3)
    num(c, '10 MILHÕES', 560, 640, f, d0, 120, -3)
    num(c, 'DE BARRIS/DIA', 560, 780, f, d0 + 6, 70, 2)
    q0 = wt(3, 'quarenta') - 4
    cx, cy, R = 870, 1260, 190
    if f >= q0 - 4:
        sc = max(.08, back(ramp(f, q0 - 4, q0 + 4)))
        r = R * sc
        d.ellipse([cx - r - 6, cy - r - 6, cx + r + 6, cy + r + 6], fill=INK)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=hexc('#d9dde3'))
        ext = 360 * .42 * smooth(ramp(f, q0, q0 + 18))
        if ext > 1: d.pieslice([cx - r, cy - r, cx + r, cy + r], -90, -90 + ext, fill=RED, outline=INK, width=5)
        num(c, '42%', cx, cy - 300, f, q0, 140, 4)
        num(c, 'CHINA', cx, cy + 260, f, wt(3, 'China') - 3, 90, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 110))) * (1 + .0008 * f)
    return c, (621 + 20 * math.sin(f * .04), 1050, z, .6 * math.sin(f * .05)), 'dusk'


MARKS = [(random.Random(i).uniform(150, 1100), random.Random(i * 7 + 1).choice((1060, 1120, 1000, 1180, 1250, 1300, 900)) + random.Random(i * 3).uniform(-40, 40)) for i in range(36)]


def s4(f):
    c = mapa_img().copy()
    d = ImageDraw.Draw(c)
    m0 = wt(4, 'cento') - 8
    shown = int(clamp((f - m0) / 30) * len(MARKS))
    for i, (x, y) in enumerate(MARKS[:shown]):
        if not (900 < y < 1330) or (y < 1000 and not 300 < x < 900): y = 1060 + (i % 5) * 40
        r = 14 + 4 * math.sin(f * .3 + i)
        d.ellipse([x - r - 4, y - r - 4, x + r + 4, y + r + 4], fill=INK)
        d.ellipse([x - r, y - r, x + r, y + r], fill=RED)
    for k_, (x, y) in enumerate(((300, 1010), (900, 1150))):
        fumaca(c, x, y, f, k_ + 3, .8)
    num(c, 'RISCO', 620, 440, f, wt(4, 'risco') - 3, 120, -4)
    num(c, '120+ NAVIOS', 620, 600, f, wt(4, 'cento') - 3, 120, 3)
    num(c, 'ATINGIDOS', 620, 760, f, wt(4, 'atingidos') - 3, 100, -3)
    z = lerp(1.35, 1.04, easeOut(ramp(f, 0, 70))) * (1 + .0008 * f)
    return c, (640 + 30 * math.sin(f * .03), 1080, z, lerp(2.5, -1.5, smooth(ramp(f, 0, 120)))), 'dusk'


def s5(f):
    c = BG('dusk').copy()
    num(c, 'IRÃ', 220, 760, f, 0, 100, -3)
    c0 = wt(5, 'Catar') - 3
    num(c, 'CATAR', 640, 760, f, c0, 100, 3)
    e0 = wt(5, 'Estados') - 3
    num(c, 'EUA', 1020, 760, f, e0, 100, -3)
    tt = smooth(ramp(f, c0 - 6, c0 + 8)); tt2 = smooth(ramp(f, e0 - 4, e0 + 12))
    if tt2 > 0: ex, ey = lerp(640, 1020, tt2), 620 - 120 * math.sin(tt2 * math.pi)
    else: ex, ey = lerp(220, 640, tt), 620 - 140 * math.sin(tt * math.pi)
    paste_c(c, envelope(), ex, ey, .8)
    num(c, 'PROPOSTA NUCLEAR', 640, 400, f, wt(5, 'proposta') - 3, 84, -3)
    s0_ = wt(5, 'sete') - 3
    if f >= s0_:
        d = ImageDraw.Draw(c)
        sc = max(.08, back(ramp(f, s0_, s0_ + 8)))
        w, h = 520 * sc, 500 * sc; x0, y0 = 640 - w / 2, 1300 - h / 2
        d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 24, fill=hexc('#fbf8f2'), outline=INK, width=6)
        for i in range(7):
            if f >= s0_ + i * 2:
                yy = y0 + (60 + i * 62) * sc
                d.rectangle([x0 + 40 * sc, yy - 18 * sc, x0 + 76 * sc, yy + 18 * sc], outline=INK, width=4)
                d.line([(x0 + 100 * sc, yy), (x0 + (440 - (i % 3) * 50) * sc, yy)], fill=hexc('#9aa4b4'), width=8)
        num(c, '7 CONDIÇÕES', 640, 980, f, s0_, 100, -4)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 110))) + .0004 * f
    return c, (640, 1050, z, 0), 'dusk'


def s6(f):
    c = BG('dusk').copy()
    p0 = wt(6, 'petroleo') - 3
    if f < p0 + 2:
        paste_c(c, txt('POR QUE IMPORTA?', 110, -4), 640, 1100, back(ramp(f, 0, 8)))
    paste_c(c, barril(), 380, 1150, back(ramp(f, p0, p0 + 8)) * 1.3 if f >= p0 else 0)
    num(c, 'PETRÓLEO', 400, 820, f, p0, 90, -4)
    c0 = wt(6, 'combustivel') - 3
    if f >= c0:
        paste_c(c, bomba(), 880, 1150, back(ramp(f, c0, c0 + 8)) * 1.1)
        num(c, 'BRASIL', 880, 780, f, wt(6, 'Brasil') - 3, 100, 4)
    t0 = wt(6, 'Trump') - 3
    if f >= wt(6, 'mundo') - 3:
        put_pol(c, 620, 1560, 600, f, 7, hair='#6b6b70', tie='#2f6fd6', arms='cheek' if f >= t0 else 'hang', expr='nervous' if f >= t0 else 'neutral', look=0)
    num(c, 'RESPOSTA?', 640, 560, f, wt(6, 'resposta') - 3, 130, -4)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 160)))
    k = kick(f, t0, .6)
    return c, (640, 1080 + k * 6, z, k - .008 * f), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'escolhe') - 3, 160, .8)
    s.ting(s.W(0, 'Ormuz') - 3, .25)
    s.whoosh(s.W(1, 'petroleo') - 3, .4, .3)
    s.thunk(s.W(1, 'fechada') - 3, 140, .6)
    for w in ('India', 'China', 'Iraque', 'Catar'): s.ting(s.W(2, w) - 3, .22)
    s.thunk(s.W(2, 'taxa') - 3, 220, .5)
    s.patter(s.W(3, 'dez') - 3, s.W(3, 'dez') + 22, 8, .14)
    s.ting(s.W(3, 'quarenta') - 3, .3)
    s.thunk(s.W(4, 'cento') - 3, 120, .8)
    s.whoosh(s.W(5, 'Catar') - 6, .4, .3)
    s.ting(s.W(5, 'sete') - 3, .3)
    s.thunk(s.W(6, 'Trump') - 3, 140, .6)
