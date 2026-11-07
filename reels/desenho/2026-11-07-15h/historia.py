"""Um Café com o Mundo — O MUNDO EXPLICADO (sábado 07/11/2026, 15h).
Tema: sarampo nos EUA passa de 5 mil casos em 2026, o maior número desde 1991 (CDC, divulgado sexta 06/11/2026).
Fontes (conferidas em 07/11/2026):
- Reuters (06/11/2026, republicado pelo Honolulu Star-Advertiser "U.S. measles cases top 5,000 for first time since 1991"):
  5.182 casos em 2026; 96% sem vacina ou com vacinação desconhecida; 562 hospitalizados (11%); 43 surtos novos;
  Pensilvânia 1.487 casos; Wisconsin relatou morte de um bebê; comissão da OPAS deve decidir na semana que vem se os EUA
  ainda cumprem os critérios de eliminação do sarampo, status mantido desde 2000.
- AFP (06/11/2026, via Times of Israel): 2.289 casos em todo o ano de 2025; estados relatam ao menos 8 mortes, inclusive
  de crianças muito pequenas; maior número em 35 anos; EUA declararam o sarampo eliminado em 2000.
Personagens genéricos (sem traços de pessoas reais). Tom sério: sem humor."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Os Estados Unidos passaram de cinco mil casos de sarampo este ano, o maior número em trinta e cinco anos.",
    "São cinco mil cento e oitenta e dois casos. No ano passado inteiro, foram dois mil duzentos e oitenta e nove.",
    "Noventa e seis por cento dos doentes não eram vacinados, ou não sabiam se eram.",
    "Quinhentas e sessenta e duas pessoas foram parar no hospital, e estados já relatam mortes, inclusive de crianças pequenas.",
    "O estado mais atingido é a Pensilvânia, com mil quatrocentos e oitenta e sete casos.",
    "Por que isso importa? O sarampo é muito contagioso, e o país era considerado livre da doença desde dois mil.",
    "Agora, a Organização Pan-Americana da Saúde decide, na semana que vem, se os Estados Unidos perdem esse status.",
]
CAPTXT = [
    "Os Estados Unidos passaram de 5 mil casos de sarampo este ano,|o maior número em 35 anos.",
    "São 5.182 casos.|No ano passado inteiro, foram 2.289.",
    "96% dos doentes não eram vacinados,|ou não sabiam se eram.",
    "562 pessoas foram parar no hospital,|e estados já relatam mortes,|inclusive de crianças pequenas.",
    "O estado mais atingido é a Pensilvânia,|com 1.487 casos.",
    "Por que isso importa? O sarampo é muito contagioso,|e o país era considerado livre da doença desde 2000.",
    "Agora, a Organização Pan-Americana da Saúde decide,|na semana que vem,|se os Estados Unidos perdem esse status.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'cinco', 6), (0, 'trinta', 6), (1, 'cento', 6), (1, 'duzentos', 6), (2, 'Noventa', 6), (2, 'vacinados', 6),
         (3, 'Quinhentas', 6), (3, 'hospital', 6), (3, 'mortes', 6), (4, 'Pensilvania', 6), (4, 'quatrocentos', 6),
         (5, 'contagioso', 6), (5, 'dois', 6), (6, 'semana', 6), (6, 'status', 6)]

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


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('cidade', 'golden').copy()
    c0 = wt(0, 'cinco') - 3
    pos = [(250, 600), (990, 560), (420, 980), (880, 1050), (620, 760), (180, 1200), (1080, 1300), (640, 1250)]
    for i, (x, y) in enumerate(pos):
        put_virus(c, x, y, f, c0 - 20 + i * 4, 120 + (i % 3) * 30, i)
    num(c, 'EUA', 640, 420, f, wt(0, 'Estados') - 3, 120, -3)
    num(c, '+5 MIL CASOS', 640, 640, f, c0, 112, -4)
    num(c, 'SARAMPO', 640, 820, f, wt(0, 'sarampo') - 3, 120, 3)
    t0 = wt(0, 'trinta') - 3
    num(c, 'MAIOR EM 35 ANOS', 640, 1000, f, t0, 80, -2)
    z = lerp(1.4, 1.06, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, c0)
    return c, (640, 960 + k * 8, z, k), 'golden'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    num(c, 'CASOS DE SARAMPO NOS EUA', 640, 470, f, 0, 50, -2)
    c0 = wt(1, 'cinco') - 3
    v0 = wt(1, 'duzentos') - 6
    barra(c, 820, 1300, 240, 560, PINK, f, c0, '5.182')
    barra(c, 460, 1300, 240, 248, GRAY, f, v0, '2.289')
    num(c, '2026', 820, 1370, f, c0 + 2, 80, 0)
    num(c, '2025', 460, 1370, f, wt(1, 'passado') - 3, 80, 0)
    t = smooth(ramp(f, 0, 110))
    k = kick(f, c0, .7)
    return c, (640, lerp(960, 1030, t) + k * 6, lerp(1.18, 1.03, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    n0 = wt(2, 'Noventa') - 3
    # grade 5x5 de bonecos: 24 sem vacina (cinza) e 1 azul
    for r in range(5):
        for k in range(5):
            i = r * 5 + k
            st = n0 - 10 + i
            if f < st: continue
            s = back(ramp(f, st, st + 8))
            col = 'blue' if i == 22 else 'gray'
            im = boneco(col)
            paste_c(c, im.resize((int(110 * s) + 1, int(165 * s) + 1)), 360 + k * 130, 760 + r * 160, 1)
    num(c, '96%', 560, 450, f, n0, 170, -4)
    v0 = wt(2, 'vacinados') - 3
    num(c, 'SEM VACINA', 600, 620, f, v0, 84, 3)
    if f >= v0:
        im = seringa().resize((360, 111))
        paste_c(c, im.rotate(-20, expand=True, resample=Image.BICUBIC), 930, 460, back(ramp(f, v0, v0 + 8)))
        d = ImageDraw.Draw(c)
        a = back(ramp(f, v0 + 6, v0 + 14))
        if a > .05:
            d.line([(930 - 110 * a, 460 - 90 * a), (930 + 110 * a, 460 + 90 * a)], fill=RED, width=14)
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 90))) * (1 + .0006 * f)
    k = kick(f, n0, .6)
    return c, (640 + 16 * math.sin(f * .03), 1020 + k * 6, z, k), 'day'


def s3(f):
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, hospital().resize((760, 760)), 640, 1170, 1)
    q0 = wt(3, 'Quinhentas') - 3
    num(c, '562', 380, 470, f, q0, 150, -4)
    num(c, 'NO HOSPITAL', 380, 610, f, wt(3, 'hospital') - 3, 80, 3)
    m0 = wt(3, 'mortes') - 3
    num(c, 'MORTES', 920, 720, f, m0, 84, 3)
    num(c, 'INCLUSIVE CRIANÇAS', 860, 1010, f, wt(3, 'criancas') - 3, 50, -2)
    # sirene piscando
    if f >= q0:
        d = ImageDraw.Draw(c)
        on = (f // 8) % 2 == 0
        d.ellipse([610, 770, 670, 830], fill=RED if on else RED_D, outline=INK, width=5)
    t = ramp(f, 0, 210)
    return c, (640 + 14 * math.sin(f * .04), lerp(1000, 1040, t), lerp(1.0, 1.08, t) * (1 + .0004 * f), lerp(0, 1.2, t)), 'dusk'


def s4(f):
    c = CEN('mapa', 'day').copy()
    num(c, 'EUA', 640, 520, f, 0, 120, -3)
    p0 = wt(4, 'Pensilvania') - 3
    if f >= p0 - 6:
        paste_c(c, marcador(), 860, 820, back(ramp(f, p0 - 6, p0 + 4)))
        rings(c, 860, 940, f, p0, 30, 1.0)
    num(c, 'PENSILVÂNIA', 700, 1080, f, p0, 110, -3)
    q0 = wt(4, 'quatrocentos') - 6
    num(c, '1.487 CASOS', 690, 1260, f, q0, 104, 3)
    for i, (x, y) in enumerate([(380, 900), (480, 1350), (1000, 1150)]):
        put_virus(c, x, y, f, q0 + 4 + i * 4, 110, i + 3)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, p0, .7)
    return c, (lerp(640, 700, t) + 12 * math.sin(f * .05), lerp(980, 1020, t) + k * 6, lerp(1.04, 1.16, ramp(f, 0, 140)) * (1 + .0005 * f), k), 'day'


def s5(f):
    c = CEN('cidade', 'dusk').copy()
    c0 = wt(5, 'contagioso') - 3
    # uma pessoa no centro, o vírus passa para as outras
    put_pol(c, 640, 1560, 620, f, 3, skin=1, hair='#3a2a20', tie='#e2708a', suit='#4a4f63', expr='pained', arms='hang', look=0)
    alvos = [(250, 1000), (1030, 1000), (300, 1350), (980, 1350), (640, 760)]
    for i, (x, y) in enumerate(alvos):
        st = c0 + i * 4
        if f >= st:
            tt = clamp((f - st) / 14)
            put_virus(c, lerp(640, x, tt), lerp(1150, y, tt), f, st, 90, i)
    num(c, 'MUITO CONTAGIOSO', 640, 520, f, c0, 80, -3)
    d0 = wt(5, 'dois') - 3
    if f >= d0:
        paste_c(c, selo_ok().resize((180, 180)), 330, 680, back(ramp(f, d0, d0 + 8)))
        num(c, 'LIVRE DESDE 2000', 720, 680, f, d0, 64, 3)
    z = lerp(1.25, 1.02, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, c0, .8)
    return c, (640, 1010 + k * 8, z, k), 'dusk'


def s6(f):
    c = CEN('escritorio', 'dusk').copy()
    paste_c(c, calendario(), 480, 920, back(ramp(f, 0, 8)))
    num(c, 'OPAS', 480, 560, f, wt(6, 'Organizacao') - 3, 120, -3)
    num(c, 'SEMANA QUE VEM', 560, 1260, f, wt(6, 'semana') - 3, 70, 2)
    s0_ = wt(6, 'status') - 3
    if f >= s0_:
        paste_c(c, selo_ok().resize((200, 200)), 960, 640, back(ramp(f, s0_, s0_ + 8)))
        num(c, '?', 1060, 560, f, s0_ + 3, 150, 6)
    put_sci(c, 980, 1640, 640, f, 7, arms='point', skin=2, hair='#2a221e', expr='neutral', look=-1)
    z = lerp(1.0, 1.14, smooth(ramp(f, 0, 90))) + .0005 * f
    return c, (640, 1040, z, lerp(0, 1.5, smooth(ramp(f, 0, 90)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'cinco') - 3, 160, .8)
    s.thunk(s.W(0, 'trinta') - 3, 200, .5)
    s.thunk(s.W(1, 'cento') - 3, 140, .9)
    s.thunk(s.W(1, 'duzentos') - 3, 260, .5)
    s.thunk(s.W(2, 'Noventa') - 3, 170, .8)
    s.thunk(s.W(3, 'Quinhentas') - 3, 160, .7)
    s.ting(s.W(4, 'Pensilvania') - 3, .25)
    s.whoosh(s.W(5, 'contagioso') - 3, .3, .5)
    s.ting(s.W(5, 'dois') - 3, .25)
    s.ting(s.W(6, 'status') - 3, .25)
