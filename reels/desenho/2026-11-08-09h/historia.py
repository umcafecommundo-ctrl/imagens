"""Um Café com o Mundo — O MUNDO EXPLICADO (domingo 08/11/2026, 09h).
Tema: EUA imobilizam o cargueiro Huda no golfo de Omã por furar o bloqueio naval ao Irã; nova força-tarefa contra rotas terrestres.
Fontes (conferidas em 08/11/2026):
- Gulf News, 08/11/2026 05:09: M/V Huda, bandeira de São Cristóvão (St Kitts), golfo de Omã; avião militar dos EUA disparou
  munição de precisão contra a popa; CENTCOM: tripulação ignorou avisos; bloqueio impediu mais de US$ 25 bi em exportação de
  petróleo; força-tarefa de ~20 civis e militares em Tampa, Flórida, ordenada em 07/11 pelo alm. Brad Cooper: rotas terrestres e mar Cáspio.
- Tribune (ANI) e Marine Insight, 08/11/2026: ataque em 07/11; navio saía de porto iraniano; tripulação orientada a sair das
  partes atingidas; desde julho 147 navios deram meia-volta; 5 navios mercantes imobilizados (incluindo o Huda).
- Asharq Al-Awsat (AFP), 08/11/2026: força-tarefa de 20 pessoas na Flórida; EUA e Irã em guerra há 8 meses; restrições em
  Ormuz apertaram o abastecimento global de energia.
Personagens genéricos (sem traços de pessoas reais). Tom sério, luz 'dusk', sem violência mostrada (só fumaça)."""
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



def mar_bg():
    c = Image.new('RGBA', (BW, BH), SEA + (255,))
    d = ImageDraw.Draw(c)
    for y in range(300, 2100, 90):
        for x in range(40 + (y // 90 % 2) * 100, BW, 200):
            d.line([(x, y), (x + 40, y - 8), (x + 80, y)], fill=SEA_D, width=5)
    return c


def cargueiro():
    """navio de carga com contêineres, proa à direita. 800x340"""
    p = Pen(800, 340)
    h = hexc('#2f5d8a')
    p.shape([(20, 190), (790, 190), (730, 320), (70, 320)], h, mul(h, .7), 5, 10)
    p.shape([(50, 280), (750, 280), (730, 320), (70, 320)], hexc('#a02c26'), hexc('#7a201b'), 4, 3)
    p.shape([(40, 60), (170, 60), (170, 192), (40, 192)], WHITE, hexc('#c9c9d2'), 5, 6)
    for x in (58, 98, 138): p.poly([(x, 80), (x + 22, 80), (x + 22, 102), (x, 102)], hexc('#7fb6e0'), 3)
    p.shape([(90, 10), (130, 10), (130, 62), (90, 62)], hexc('#d8443c'), hexc('#a02c26'), 4, 3)
    cols = ['#e07b39', '#3aa66a', '#d8443c', '#f0c541', '#5b8fd6', '#e07b39', '#3aa66a', '#d8443c']
    for i, x in enumerate(range(200, 720, 65)):
        for j, y in enumerate((130, 75)):
            if j == 1 and i % 3 == 2: continue
            cc = hexc(cols[(i + j * 3) % len(cols)])
            p.shape([(x, y), (x + 60, y), (x + 60, y + 58), (x, y + 58)], cc, mul(cc, .72), 4, 4)
    return p.img


def carg(c, x, y, w, bob=0.0, flip=False):
    im = sprite('cargueiro', (), int(w * 340 / 800), 800 / 340, flip)
    paste_c(c, im, x, y + 6 * math.sin(bob))


@lru_cache(maxsize=2)
def jato():
    """avião militar genérico de lado, voando p/ direita. 640x240"""
    p = Pen(640, 240)
    g = hexc('#8f96a0'); gd = hexc('#656b74')
    p.shape([(60, 40), (130, 40), (200, 110), (120, 110)], g, gd, 4, 4)
    p.shape([(30, 120), (480, 100), (620, 122), (480, 145), (30, 140)], g, gd, 5, 8)
    p.shape([(400, 96), (480, 100), (500, 112), (410, 114)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 2)
    p.shape([(220, 128), (360, 128), (250, 215), (190, 215)], gd, mul(gd, .7), 4, 3)
    p.dot(40, 130, 14, hexc('#f0a040'), 3)
    return fin(p)


def put_jato(c, x, y, w=420):
    paste_c(c, jato().resize((w, int(w * 240 / 640))), x, y)


def aviso(c, s, x, y, f, f0, size=90, rot=-4):
    if f < f0: return
    sc = back(ramp(f, f0, f0 + 8))
    paste_c(c, txt(s, size, rot), x, y, sc)


VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um avião americano atirou num navio de carga, de propósito, só para ele parar no meio do mar.",
    "Foi no sábado, no golfo de Omã. O navio Huda tinha saído de um porto do Irã.",
    "Os americanos dizem que a tripulação ignorou os avisos, e foi orientada a sair da parte atingida.",
    "Desde julho, os Estados Unidos bloqueiam os portos do Irã. Cento e quarenta e sete navios deram meia-volta, e cinco foram imobilizados.",
    "Segundo eles, o Irã já deixou de vender mais de vinte e cinco bilhões de dólares em petróleo.",
    "E agora o bloqueio chega à terra: uma força-tarefa de vinte pessoas vai tentar fechar as rotas por estradas e pelo mar Cáspio.",
    "Por que importa? A guerra já dura oito meses, e o petróleo do Golfo pesa no combustível do mundo todo.",
]
CAPTXT = [
    "Um avião americano atirou num navio de carga,|de propósito, só para ele parar no meio do mar.",
    "Foi no sábado, no golfo de Omã.|O navio Huda tinha saído|de um porto do Irã.",
    "Os americanos dizem que a tripulação ignorou|os avisos, e foi orientada a sair|da parte atingida.",
    "Desde julho, os Estados Unidos bloqueiam os portos do Irã.|147 navios deram meia-volta,|e 5 foram imobilizados.",
    "Segundo eles, o Irã já deixou de vender|mais de 25 bilhões de dólares em petróleo.",
    "E agora o bloqueio chega à terra: uma força-tarefa|de 20 pessoas vai tentar fechar as rotas|por estradas e pelo mar Cáspio.",
    "Por que importa? A guerra já dura 8 meses,|e o petróleo do Golfo pesa|no combustível do mundo todo.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'atirou', 4), (0, 'parar', 4), (1, 'sabado', 4), (1, 'Oma', 4), (1, 'Huda', 4), (1, 'Ira', 4),
         (2, 'avisos', 4), (2, 'atingida', 4), (3, 'julho', 4), (3, 'cento', 6), (3, 'cinco', 6),
         (4, 'vinte', 6), (4, 'petroleo', 4), (5, 'terra', 4), (5, 'vinte', 6), (5, 'estradas', 4), (5, 'Caspio', 4),
         (6, 'oito', 6), (6, 'combustivel', 6)]

STRAIT = (705, 1060)
OMA = (1040, 1250)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = mar_bg()
    a0 = wt(0, 'atirou') - 3
    carg(c, 640, 1150, 820, f * .15)
    jx = lerp(-300, 1500, ramp(f, a0 - 30, a0 + 40))
    if -300 < jx < 1500: put_jato(c, jx, 560 + 30 * math.sin(f * .05))
    if f >= a0 + 4:
        fumaca(c, 300, 1080, f - a0, 1, 1.0)
    aviso(c, 'DE PROPÓSITO', 640, 760, f, wt(0, 'proposito') - 3, 100, -3)
    aviso(c, 'PARADO!', 640, 420, f, wt(0, 'parar') - 3, 150, 4)
    z = lerp(1.45, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, a0 + 4)
    return c, (640, 1000 + k * 8, z, k), 'dusk'


def s1(f):
    c = mapa_img().copy()
    num(c, 'IRÃ', 420, 640, f, 0, 110, -3)
    num(c, 'SÁBADO', 640, 400, f, wt(1, 'sabado') - 3, 110, 3)
    num(c, 'GOLFO DE OMÃ', 740, 1560, f, wt(1, 'Oma') - 3, 80, -3)
    h0 = wt(1, 'Huda') - 3
    t = smooth(ramp(f, h0 - 10, wt(1, 'Ira') + 20))
    carg(c, lerp(STRAIT[0] - 120, OMA[0], t), lerp(1080, OMA[1], t), 300, f * .2)
    num(c, 'NAVIO HUDA', 780, 790, f, h0, 90, 3)
    marcador(c, 560, 960, f, wt(1, 'porto') - 3, .7)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140)))
    return c, (700, lerp(980, 1080, smooth(ramp(f, 0, 140))), z, lerp(-1.5, 1, smooth(ramp(f, 0, 140)))), 'dusk'


def s2(f):
    c = mar_bg()
    carg(c, 640, 1200, 900, f * .15)
    v0 = wt(2, 'avisos') - 3
    for i, (x, y, r) in enumerate(((330, 520, -5), (900, 640, 4), (520, 800, -2))):
        aviso(c, 'AVISO!', x, y, f, v0 + i * 6, 100, r)
    if f >= v0: rings(c, 640, 980, f, v0, 40, 1.4)
    a0 = wt(2, 'sair') - 3
    if f >= a0:
        d = ImageDraw.Draw(c)
        d.rounded_rectangle([200, 1060, 470, 1280], 20, outline=RED, width=10)
        aviso(c, 'SAIAM DAQUI', 640, 380, f, a0, 90, 3)
    z = lerp(1.0, 1.14, smooth(ramp(f, 0, 130))) * (1 + .0004 * f)
    return c, (640, 1000, z, .8 * math.sin(f * .04)), 'dusk'


def s3(f):
    c = mapa_img().copy()
    num(c, 'DESDE JULHO', 640, 380, f, wt(3, 'julho') - 3, 100, -3)
    b0 = wt(3, 'bloqueiam') - 3
    if f >= b0:
        d = ImageDraw.Draw(c)
        L = int(400 * smooth(ramp(f, b0, b0 + 15)))
        for yy in range(1000, 1000 + L, 50):
            d.line([(820, yy), (820, yy + 28)], fill=RED, width=14)
        num(c, 'BLOQUEIO', 880, 900, f, b0, 80, 4)
    c0 = wt(3, 'cento') - 3
    if f >= c0 - 10:
        for i in range(4):
            tt = ((f - c0 + 10) * .02 + i * .25) % 1
            x = 1150 - 280 * math.sin(tt * math.pi)
            paste_c(c, sprite('cargueiro', (), 70, 800 / 340, tt > .5), x, 1150 + i * 70)
    num(c, '147 MEIA-VOLTA', 620, 560, f, c0, 100, 3)
    num(c, '5 IMOBILIZADOS', 620, 720, f, wt(3, 'cinco') - 3, 96, -3)
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 160)))
    return c, (680 + 20 * math.sin(f * .03), 1000, z, .6 * math.sin(f * .04)), 'dusk'


def s4(f):
    c = CEN('deserto', 'dusk').copy()
    v0 = wt(4, 'vender') - 3
    b = barril()
    for i in range(8):
        r, k = divmod(i, 4)
        x = 300 + k * 210 + r * 105; y = 1440 - r * 170
        if r > 1: continue
        paste_c(c, b, x, y, back(ramp(f, v0 + i * 2, v0 + i * 2 + 8)) * .85)

    n0 = wt(4, 'vinte') - 3
    num(c, 'MAIS DE US$ 25', 640, 520, f, n0, 92, -3)
    num(c, 'BILHÕES', 640, 680, f, n0 + 4, 120, 3)
    p0 = wt(4, 'petroleo') - 3
    if f >= p0:
        d = ImageDraw.Draw(c)
        s = back(ramp(f, p0, p0 + 8))
        d.line([(640 - 300 * s, 1000 - 300 * s), (640 + 300 * s, 1000 + 300 * s)], fill=RED, width=26)
        d.line([(640 + 300 * s, 1000 - 300 * s), (640 - 300 * s, 1000 + 300 * s)], fill=RED, width=26)
        num(c, 'SEM VENDA', 640, 840, f, p0, 80, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) + .0003 * f
    k = kick(f, n0, .6)
    return c, (640, 1050 + k * 6, z, k), 'dusk'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    t0 = wt(5, 'terra') - 3
    v0 = wt(5, 'vinte') - 3
    put_soldier(c, 280, 1560, 680, f, 4, arms='point' if f >= v0 else 'hang', expr='stern')
    num(c, 'BLOQUEIO EM TERRA', 640, 400, f, t0, 76, -3)
    num(c, 'FORÇA-TAREFA', 760, 600, f, wt(5, 'forca-tarefa') - 3, 90, 3)
    num(c, '20 PESSOAS', 760, 760, f, v0, 100, -3)
    e0 = wt(5, 'estradas') - 3
    if f >= e0:
        paste_c(c, art.truck(f * .3).resize((380, 220)), lerp(1300, 760, smooth(ramp(f, e0, e0 + 20))), 1340, 1)
        num(c, 'ESTRADAS', 820, 1000, f, e0, 80, 3)
    num(c, 'MAR CÁSPIO', 820, 1420, f, wt(5, 'Caspio') - 3, 80, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 150))) + .0003 * f
    k = kick(f, v0, .6)
    return c, (640, 1050 + k * 6, z, k), 'dusk'


def s6(f):
    c = mapa_img().copy()
    if f < wt(6, 'guerra') - 3:
        paste_c(c, txt('POR QUE IMPORTA?', 110, -4), 620, 560, back(ramp(f, 0, 8)))
    num(c, '8 MESES DE GUERRA', 620, 480, f, wt(6, 'oito') - 3, 90, -3)
    p0 = wt(6, 'petroleo') - 3
    b = barril().resize((110, 143))
    if f >= p0:
        for i in range(7):
            t = ((f - p0) * .012 + i / 7) % 1
            paste_c(c, b, lerp(80, 1180, t), 1075 + 10 * math.sin(f * .2 + i), back(ramp(f, p0 + i * 2, p0 + i * 2 + 8)))
    q0 = wt(6, 'combustivel') - 3
    if f >= q0:
        paste_c(c, bomba(), 640, 1290, back(ramp(f, q0, q0 + 8)) * .7)
        num(c, 'COMBUSTÍVEL', 640, 640, f, q0, 100, 3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140)))
    k = kick(f, q0, .5)
    return c, (660, lerp(1000, 1060, smooth(ramp(f, 0, 140))) + k * 6, z, lerp(-1.5, 1, smooth(ramp(f, 0, 140)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.engine(s.W(0, 'atirou') - 30, s.W(0, 'atirou') + 30, .12)
    s.thunk(s.W(0, 'atirou') + 1, 140, .7)
    s.ting(s.W(0, 'parar') - 3, .25)
    s.ting(s.W(1, 'sabado') - 3, .2)
    s.whoosh(s.W(1, 'Huda') - 6, .4, .3)
    s.ting(s.W(2, 'avisos') - 3, .25)
    s.ting(s.W(3, 'julho') - 3, .2)
    s.thunk(s.W(3, 'cinco') - 3, 130, .5)
    s.ting(s.W(4, 'vinte') - 3, .3)
    s.thunk(s.W(4, 'petroleo') - 3, 120, .5)
    s.ting(s.W(5, 'vinte') - 3, .25)
    s.engine(s.W(5, 'estradas') - 3, s.W(5, 'estradas') + 40, .1)
    s.thunk(s.W(6, 'combustivel') - 3, 160, .5)
