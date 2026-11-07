"""Um Café com o Mundo — O MUNDO EXPLICADO (sábado 07/11/2026, 09h).
Tema: EUA atacam defesa antiaérea na ilha de Qeshm (estreito de Ormuz), 1º ataque desde a eleição americana.
Fontes (conferidas em 07/11/2026):
- Al Jazeera/AP, 07/11/2026 "Trump confirms new US strikes on Iran's Qeshm island": Trump confirmou na sexta (06/11), em
  West Palm Beach, "minor strikes" contra defesa antiaérea; "knocked it out in about 15 minutes, maybe five"; mídia estatal
  do Irã: 2 mísseis na área de Suza; IRIB: Irã diz ter derrubado drone MQ-9 (não confirmado pelos EUA); CENTCOM oferece até
  US$ 20 milhões por informações sobre o programa nuclear; 1º ataque desde as eleições de 03/11; Catar nega fracasso da
  negociação; Trump: "They want to make a deal".
- Jerusalem Post/Reuters, 07/11/2026: Tasnim/IRNA, dois projéteis em Suza, Qeshm; Catar diz que mediação continua.
Personagens genéricos (sem traços de pessoas reais). Tom sério, luz 'dusk', sem violência mostrada."""
from kit import *
import kit

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




VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Os Estados Unidos voltaram a atacar o Irã, numa ilha no meio do estreito de Ormuz.",
    "Na sexta-feira, Donald Trump confirmou: o alvo foi a defesa antiaérea iraniana na ilha de Qeshm.",
    "Ele chamou de ataques pequenos, e disse que o equipamento foi destruído em uns quinze minutos.",
    "A mídia do Irã fala em dois mísseis, e diz ter derrubado um drone americano. Os Estados Unidos não confirmaram.",
    "Os militares americanos também oferecem até vinte milhões de dólares por informações sobre o programa nuclear do Irã.",
    "Por que isso importa? Foi o primeiro ataque desde a eleição americana, e Ormuz é a rota de boa parte do petróleo do mundo.",
    "Enquanto isso, o Catar diz que a negociação continua, e Trump afirma que o Irã quer um acordo.",
]
CAPTXT = [
    "Os Estados Unidos voltaram a atacar o Irã,|numa ilha no meio do estreito de Ormuz.",
    "Na sexta-feira, Donald Trump confirmou:|o alvo foi a defesa antiaérea iraniana|na ilha de Qeshm.",
    "Ele chamou de ataques pequenos, e disse que|o equipamento foi destruído em uns 15 minutos.",
    "A mídia do Irã fala em 2 mísseis,|e diz ter derrubado um drone americano.|Os Estados Unidos não confirmaram.",
    "Os militares americanos também oferecem|até 20 milhões de dólares por informações|sobre o programa nuclear do Irã.",
    "Por que isso importa? Foi o primeiro ataque|desde a eleição americana, e Ormuz é a rota|de boa parte do petróleo do mundo.",
    "Enquanto isso, o Catar diz que a negociação continua,|e Trump afirma que o Irã quer um acordo.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'atacar', 4), (0, 'ilha', 4), (0, 'Ormuz', 4), (1, 'sexta-feira', 4), (1, 'antiaerea', 4), (1, 'Qeshm', 6),
         (2, 'pequenos', 4), (2, 'quinze', 6), (3, 'dois', 6), (3, 'drone', 6), (3, 'confirmaram', 6),
         (4, 'vinte', 6), (4, 'nuclear', 6), (5, 'eleicao', 6), (5, 'petroleo', 6), (6, 'Catar', 4), (6, 'acordo', 6)]

ISLAND = [(880, 905), (940, 880), (1020, 872), (1100, 880), (1150, 900), (1120, 925), (1040, 935), (960, 935), (900, 925)]
ISL_C = (1015, 905)


@lru_cache(maxsize=2)
def mapa_qeshm():
    im = mapa_img().copy()
    d = ImageDraw.Draw(im)
    d.polygon([(x, y + 10) for x, y in ISLAND], fill=SAND_D)
    d.polygon(ISLAND, fill=SAND, outline=INK, width=6)
    return im


def marcador(c, x, y, f, f0, s=1.0):
    if f < f0: return
    sc = back(ramp(f, f0, f0 + 8)) * s
    d = ImageDraw.Draw(c)
    pr = 26 + 14 * ((f - f0) % 30) / 30
    d.ellipse([x - pr * 2 * s, y - pr * s, x + pr * 2 * s, y + pr * s], outline=RED, width=5)
    r = 34 * sc
    d.polygon([(x - r, y - 1.6 * r), (x + r, y - 1.6 * r), (x, y)], fill=INK)
    d.ellipse([x - r - 5, y - 2.6 * r - 5, x + r + 5, y - 0.6 * r + 5], fill=INK)
    d.polygon([(x - r * .8, y - 1.6 * r), (x + r * .8, y - 1.6 * r), (x, y - 8)], fill=RED)
    d.ellipse([x - r, y - 2.6 * r, x + r, y - 0.6 * r], fill=RED)
    d.ellipse([x - r * .4, y - 2 * r, x + r * .4, y - 1.2 * r], fill=WHITE)


@lru_cache(maxsize=4)
def radar(broken=0):
    """antena de radar genérica sobre um caminhão-base. 420x420"""
    p = Pen(420, 420)
    g = hexc('#7d8a6a'); gd = hexc('#5a6650')
    p.shape([(40, 300), (380, 300), (380, 380), (40, 380)], g, gd, 5, 8)
    for x in (100, 320): p.shape(ell_pts(x, 385, 34, 34, 20), hexc('#2a2a33'), hexc('#1a1a20'), 4, 3)
    p.shape([(190, 300), (230, 300), (225, 200), (195, 200)], gd, mul(gd, .7), 4, 3)
    if broken:
        p.shape([(110, 230), (210, 200), (300, 250), (280, 290), (130, 290)], hexc('#5b5b62'), hexc('#3d3d44'), 5, 4)
    else:
        p.shape([(80, 60), (340, 110), (310, 210), (110, 190), (60, 120)], hexc('#d9dde3'), hexc('#a9b0ba'), 5, 8)
        p.stroke([(210, 150), (250, 40)], 6)
        p.dot(252, 36, 14, RED, 3)
    return fin(p)


@lru_cache(maxsize=2)
def drone():
    """drone militar genérico de lado, voando p/ direita. 600x220"""
    p = Pen(600, 220)
    gr = hexc('#9aa0a8'); grd = hexc('#6e747c')
    p.shape([(220, 60), (300, 20), (360, 20), (380, 60)], gr, grd, 4, 4)
    p.shape([(40, 110), (520, 95), (580, 112), (520, 135), (40, 130)], gr, grd, 5, 8)
    p.shape([(470, 92), (540, 94), (560, 108), (480, 112)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 2)
    p.shape([(40, 110), (10, 60), (40, 60), (80, 112)], gr, grd, 4, 3)
    p.shape([(40, 128), (10, 180), (40, 180), (80, 128)], gr, grd, 4, 3)
    p.shape([(220, 112), (330, 112), (300, 200), (260, 200)], grd, mul(grd, .7), 4, 3)
    return fin(p)


@lru_cache(maxsize=2)
def maleta():
    """pilha de notas de dinheiro. 360x260"""
    p = Pen(360, 260)
    for i in range(5):
        y = 220 - i * 38
        p.shape([(20, y - 40), (340, y - 40), (340, y), (20, y)], hexc('#5fb06d'), hexc('#3f8a4c'), 4, 4)
        p.dot(180, y - 20, 14, hexc('#d8eecd'), 3)
    return fin(p)


@lru_cache(maxsize=2)
def mic():
    p = Pen(200, 500)
    p.stroke([(100, 140), (100, 480)], 12, hexc('#4a4a50'))
    p.shape([(40, 480), (160, 480), (170, 500), (30, 500)], hexc('#4a4a50'), hexc('#2a2a33'), 4, 3)
    p.shape(ell_pts(100, 80, 46, 70, 24), hexc('#2a2a33'), hexc('#1a1a20'), 5, 4)
    return fin(p)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = mapa_qeshm().copy()
    a0 = wt(0, 'atacar') - 3
    i0 = wt(0, 'ilha') - 3
    if f >= a0: fumaca(c, ISL_C[0] - 30, ISL_C[1] - 10, f - a0, 1, .8)
    marcador(c, ISL_C[0] - 30, ISL_C[1] - 5, f, i0)
    num(c, 'EUA x IRÃ', 620, 520, f, 0, 130, -3)
    num(c, 'IRÃ', 360, 720, f, 6, 100, -3)
    num(c, 'ORMUZ', 760, 1260, f, wt(0, 'Ormuz') - 3, 110, 4)
    nav(c, lerp(200, 520, smooth(ramp(f, 0, 120))), 1080, 260, '#2e7d4f', f * .2)
    z = lerp(1.5, 1.1, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, a0)
    return c, (760, 1020 + k * 8, z, k), 'dusk'


def s1(f):
    c = CEN('cidade', 'dusk').copy()
    s0_ = wt(1, 'confirmou') - 3
    paste_c(c, mic(), 820, 1300, 1)
    put_pol(c, 560, 1560, 720, f, 5, hair='#c9c9cf', tie='#2f6fd6',
            arms='point' if f >= s0_ else 'hang', expr='stern' if f >= s0_ else 'neutral', look=1)
    num(c, 'SEXTA-FEIRA', 640, 400, f, wt(1, 'sexta-feira') - 3, 100, -3)
    a0 = wt(1, 'antiaerea') - 3
    if f >= a0:
        num(c, 'DEFESA ANTIAÉREA', 640, 580, f, a0, 74, 3)
    num(c, 'ILHA DE QESHM', 640, 1000, f, wt(1, 'Qeshm') - 3, 90, -3)
    z = lerp(1.05, 1.16, smooth(ramp(f, 0, 120)))
    k = kick(f, s0_, .6)
    return c, (640, 1050 + k * 6, z, k), 'dusk'


def ilha_close(c):
    d = ImageDraw.Draw(c)
    pts = [(80, 1180), (300, 1080), (700, 1050), (1100, 1080), (1200, 1180), (1050, 1260), (600, 1280), (200, 1260)]
    d.polygon([(x, y + 22) for x, y in pts], fill=SAND_D)
    d.polygon(pts, fill=SAND, outline=INK, width=7)


def mar_bg():
    c = Image.new('RGBA', (BW, BH), SEA + (255,))
    d = ImageDraw.Draw(c)
    for y in range(300, 2100, 90):
        for x in range(40 + (y // 90 % 2) * 100, BW, 200):
            d.line([(x, y), (x + 40, y - 8), (x + 80, y)], fill=SEA_D, width=5)
    return c


def s2(f):
    c = mar_bg(); ilha_close(c)
    p0 = wt(2, 'pequenos') - 3
    q0 = wt(2, 'quinze') - 3
    broken = f >= q0
    paste_c(c, radar(1 if broken else 0), 640, 980, 1)
    if broken:
        fumaca(c, 640, 950, f - q0, 2, 1.0)
    num(c, 'ATAQUES PEQUENOS', 640, 420, f, p0, 76, -3)
    if f >= q0:
        paste_c(c, clock_img(0, int(90 * smooth(ramp(f, q0, q0 + 20))), 240), 860, 640, back(ramp(f, q0, q0 + 8)))
        num(c, '15 MIN', 860, 820, f, q0, 110, 4)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 130))) * (1 + .0004 * f)
    k = kick(f, q0, .8)
    return c, (640, 1000 + k * 8, z, k), 'dusk'


def s3(f):
    c = mapa_qeshm().copy()
    m0 = wt(3, 'dois') - 3
    if f >= m0:
        fumaca(c, ISL_C[0] - 60, ISL_C[1] - 5, f - m0, 3, .7)
        fumaca(c, ISL_C[0] + 40, ISL_C[1] - 5, f - m0, 4, .7)
    num(c, 'MÍDIA DO IRÃ:', 620, 420, f, wt(3, 'midia') - 3, 90, -3)
    num(c, '2 MÍSSEIS', 620, 560, f, m0, 120, 3)
    d0 = wt(3, 'drone') - 3
    if f >= d0 - 10:
        x = lerp(-200, 640, smooth(ramp(f, d0 - 10, d0 + 60)))
        paste_c(c, drone().resize((300, 110)), x, 760 + 10 * math.sin(f * .2), 1)
        num(c, 'DRONE?', 620, 1300, f, d0, 110, -4)
    n0 = wt(3, 'confirmaram') - 4
    num(c, 'EUA NÃO CONFIRMAM', 640, 1440, f, n0, 66, 3)
    z = lerp(1.2, 1.05, smooth(ramp(f, 0, 80))) * (1 + .0006 * f)
    return c, (700 + 20 * math.sin(f * .03), 1000, z, .8 * math.sin(f * .04)), 'dusk'


def s4(f):
    c = CEN('escritorio', 'dusk').copy()
    v0 = wt(4, 'vinte') - 3
    put_soldier(c, 300, 1560, 700, f, 4, arms='point' if f >= v0 else 'hang', expr='stern')
    if f >= v0:
        paste_c(c, maleta(), 860, 1240, back(ramp(f, v0, v0 + 8)))
        num(c, 'ATÉ US$ 20', 660, 700, f, v0, 100, -3)
        num(c, 'MILHÕES', 760, 840, f, v0 + 4, 90, 3)
    n0 = wt(4, 'nuclear') - 3
    num(c, 'PROGRAMA NUCLEAR', 640, 420, f, n0, 70, -3)
    num(c, 'RECOMPENSA', 640, 560, f, wt(4, 'oferecem') - 3, 90, 3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) + .0003 * f
    k = kick(f, v0, .6)
    return c, (640, 1050 + k * 6, z, k), 'dusk'


def s5(f):
    c = mapa_qeshm().copy()
    if f < wt(5, 'primeiro') - 3:
        paste_c(c, txt('POR QUE IMPORTA?', 110, -4), 620, 560, back(ramp(f, 0, 8)))
    num(c, '1º ATAQUE', 620, 460, f, wt(5, 'primeiro') - 3, 110, -3)
    num(c, 'APÓS A ELEIÇÃO', 620, 600, f, wt(5, 'eleicao') - 3, 90, 3)
    p0 = wt(5, 'petroleo') - 3
    b = barril().resize((110, 143))
    if f >= p0:
        for i in range(7):
            t = ((f - p0) * .012 + i / 7) % 1
            paste_c(c, b, lerp(80, 1180, t), 1075 + 10 * math.sin(f * .2 + i), back(ramp(f, p0 + i * 2, p0 + i * 2 + 8)))
        num(c, 'PETRÓLEO', 620, 1330, f, p0, 110, -3)
    marcador(c, ISL_C[0] - 30, ISL_C[1] - 5, f, 0, .8)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140)))
    return c, (660, lerp(1000, 1060, smooth(ramp(f, 0, 140))), z, lerp(-1.5, 1, smooth(ramp(f, 0, 140)))), 'dusk'


def s6(f):
    c = CEN('cidade', 'dusk').copy()
    num(c, 'IRÃ', 200, 760, f, 0, 100, -3)
    c0 = wt(6, 'Catar') - 3
    num(c, 'CATAR', 640, 760, f, c0, 100, 3)
    e0 = wt(6, 'Trump') - 3
    num(c, 'EUA', 1040, 760, f, e0, 100, -3)
    tt = smooth(ramp(f, c0 - 6, c0 + 10)); tt2 = smooth(ramp(f, e0 - 4, e0 + 12))
    if tt2 > 0: ex, ey = lerp(640, 1020, tt2), 620 - 120 * math.sin(tt2 * math.pi)
    else: ex, ey = lerp(220, 640, tt), 620 - 140 * math.sin(tt * math.pi)
    paste_c(c, envelope(), ex, ey, .8)
    num(c, 'NEGOCIAÇÃO CONTINUA', 640, 420, f, wt(6, 'negociacao') - 3, 62, -3)
    a0 = wt(6, 'acordo') - 3
    put_pol(c, 640, 1560, 560, f, 9, hair='#6b6b70', tie='#3aa66a', skin=1,
            arms='up' if f >= a0 else 'hang', expr='nervous' if f >= a0 else 'neutral', look=0)
    num(c, 'ACORDO?', 640, 1000, f, a0, 140, -4)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140)))
    k = kick(f, a0, .6)
    return c, (640, 1050 + k * 6, z, k - .006 * f), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'atacar') - 3, 140, .7)
    s.ting(s.W(0, 'ilha') - 3, .25)
    s.ting(s.W(1, 'sexta-feira') - 3, .2)
    s.whoosh(s.W(1, 'antiaerea') - 3, .4, .3)
    s.ting(s.W(2, 'pequenos') - 3, .2)
    s.thunk(s.W(2, 'quinze') - 3, 120, .7)
    s.thunk(s.W(3, 'dois') - 3, 130, .6)
    s.engine(s.W(3, 'drone') - 10, s.W(3, 'drone') + 40, .1)
    s.ting(s.W(4, 'vinte') - 3, .3)
    s.ting(s.W(5, 'primeiro') - 3, .25)
    s.whoosh(s.W(6, 'Catar') - 6, .4, .3)
    s.thunk(s.W(6, 'acordo') - 3, 160, .5)
