"""Um Café com o Mundo — O MUNDO EXPLICADO (sábado 07/11/2026, 18h).
Tema: Israel — presidente Herzog anuncia que dará a Gadi Eisenkot o mandato para formar o novo governo.
Fontes (conferidas em 07/11/2026):
- Times of Israel, liveblog 07/11/2026: Herzog informou Eisenkot e Netanyahu, na noite de 07/11, que dará a Eisenkot
  a tarefa de formar o governo no domingo (08/11), às 17h; nas consultas, 67 deputados recomendaram Eisenkot e 46 Netanyahu;
  Judaísmo Unido da Torá (7 cadeiras) não recomendou ninguém; 28 dias + até 14 de prorrogação; eleição em 27/10/2026;
  coalizão de Netanyahu ficou com 53 de 120 cadeiras e perdeu a maioria; Ra'am e Lista Conjunta (árabes) têm 19 e apoiam
  Eisenkot; Netanyahu, em vídeo, pediu governo de "união nacional" e criticou um governo apoiado por partidos árabes.
- JTA, 06/11/2026: Knesset tem 120 cadeiras, maioria = 61; se Eisenkot falhar, outro candidato pode tentar ou haverá nova eleição.
- JNS / Ynet / Israel National News: 67 x 46; mandato no domingo.
Eisenkot foi chefe do Estado-Maior do Exército de Israel (2015-2019).
Personagens genéricos (sem traços de pessoas reais). Tom sério e neutro."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Israel está perto de ter um novo primeiro-ministro, e não é Benjamin Netanyahu.",
    "O presidente Isaac Herzog anunciou que vai dar a Gadi Eisenkot, ex-chefe do Exército, a missão de formar o governo.",
    "Na eleição de outubro, o grupo de Netanyahu perdeu a maioria das cento e vinte cadeiras.",
    "Nas consultas, sessenta e sete deputados indicaram Eisenkot, contra quarenta e seis para Netanyahu.",
    "Nesse apoio estão os partidos árabes, com dezenove cadeiras. Netanyahu criticou e pede união nacional.",
    "Por que importa? Netanyahu é quem mais tempo governou Israel, e quem lidera decide sobre Gaza e o Irã.",
    "Agora, Eisenkot tem vinte e oito dias, mais catorze de prorrogação. Se falhar, Israel pode voltar às urnas.",
]
CAPTXT = [
    "Israel está perto de ter um novo primeiro-ministro,|e não é Benjamin Netanyahu.",
    "O presidente Isaac Herzog anunciou|que vai dar a Gadi Eisenkot, ex-chefe do Exército,|a missão de formar o governo.",
    "Na eleição de outubro, o grupo de Netanyahu|perdeu a maioria das 120 cadeiras.",
    "Nas consultas, 67 deputados indicaram Eisenkot,|contra 46 para Netanyahu.",
    "Nesse apoio estão os partidos árabes, com 19 cadeiras.|Netanyahu criticou|e pede união nacional.",
    "Por que importa? Netanyahu é quem mais tempo|governou Israel, e quem lidera|decide sobre Gaza e o Irã.",
    "Agora, Eisenkot tem 28 dias, mais 14 de prorrogação.|Se falhar, Israel pode voltar às urnas.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'novo', 4), (0, 'Netanyahu', 6), (1, 'anunciou', 4), (1, 'Exercito', 4), (1, 'governo', 4),
         (2, 'outubro', 4), (2, 'maioria', 4), (2, 'cento', 8), (3, 'sessenta', 6), (3, 'quarenta', 6),
         (4, 'arabes', 4), (4, 'dezenove', 6), (4, 'nacional', 4), (5, 'tempo', 4), (5, 'Gaza', 4), (5, 'Ira', 4),
         (6, 'vinte', 6), (6, 'catorze', 6), (6, 'urnas', 6)]

TEAL = hexc('#2a9d8f'); TEAL_D = hexc('#1d6f65'); ORG = hexc('#e07b2a'); ORG_D = hexc('#a85a1c')
GREEN = hexc('#7ccf5a'); GRAY = hexc('#d9dde3'); FBLUE = hexc('#2f5fd0'); WHITE = (255, 255, 255)
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); RED = hexc('#d8443c')


# ------------------------------------------------------------------ desenhos novos
def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


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


@lru_cache(maxsize=2)
def bandeira():
    """bandeira de Israel (país, permitido). 600x440"""
    p = Pen(600, 440)
    p.shape([(10, 10), (590, 10), (590, 430), (10, 430)], WHITE, hexc('#d6dbe6'), 6, 8)
    p.poly([(10, 55), (590, 55), (590, 110), (10, 110)], FBLUE)
    p.poly([(10, 330), (590, 330), (590, 385), (10, 385)], FBLUE)
    cx, cy, r = 300, 220, 88
    for rot in (0, math.pi):
        pts = [(cx + r * math.sin(rot + k * 2 * math.pi / 3), cy - r * math.cos(rot + k * 2 * math.pi / 3)) for k in range(3)]
        p.stroke(pts + [pts[0]], 16, FBLUE)
    p.stroke([(10, 10), (590, 10), (590, 430), (10, 430), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def predio():
    """prédio genérico de parlamento, retangular com colunas. 1000x620, base y~610."""
    p = Pen(1000, 620)
    for i in range(4):
        y = 610 - i * 14
        p.shape([(60 + i * 18, y - 14), (940 - i * 18, y - 14), (940 - i * 18, y), (60 + i * 18, y)], STONE, STONE_D, 4, 3)
    p.shape([(70, 150), (930, 150), (930, 560), (70, 560)], STONE, STONE_D, 6, 14)
    p.shape([(40, 110), (960, 110), (960, 170), (40, 170)], STONE, STONE_D, 6, 6)
    for x in range(120, 900, 62):
        p.shape([(x - 16, 190), (x + 16, 190), (x + 16, 548), (x - 16, 548)], hexc('#fbf8f2'), STONE_D, 3, 4)
    p.stroke([(500, 110), (500, 10)], 6)
    p.shape([(503, 12), (600, 12), (600, 72), (503, 72)], WHITE, hexc('#d6dbe6'), 4, 3)
    p.poly([(503, 20), (600, 20), (600, 30), (503, 30)], FBLUE)
    p.poly([(503, 54), (600, 54), (600, 64), (503, 64)], FBLUE)
    return fin(p)


@lru_cache(maxsize=2)
def envelope():
    p = Pen(340, 240)
    p.shape([(10, 10), (330, 10), (330, 230), (10, 230)], WHITE, hexc('#c9c9d2'), 5, 6)
    p.stroke([(10, 10), (170, 130), (330, 10)], 5)
    p.dot(170, 130, 26, FBLUE, 3)
    return fin(p)


@lru_cache(maxsize=2)
def urna():
    p = Pen(500, 520)
    p.shape([(60, 160), (440, 160), (420, 500), (80, 500)], hexc('#eef2f7'), hexc('#b9c3d1'), 6, 16)
    p.shape([(40, 120), (460, 120), (460, 170), (40, 170)], hexc('#dfe6ef'), hexc('#a9b4c4'), 5, 6)
    p.poly([(180, 136), (320, 136), (320, 152), (180, 152)], INK)
    p.shape(ell_pts(250, 330, 70, 70, 40), TEAL, TEAL_D, 5, 6)
    p.stroke([(215, 330), (242, 358), (290, 300)], 12, (255, 255, 255))
    return fin(p)


@lru_cache(maxsize=2)
def cedula():
    p = Pen(160, 210)
    p.shape([(10, 10), (150, 10), (150, 200), (10, 200)], (255, 255, 255), hexc('#cfd6df'), 4, 4)
    for y in (50, 90, 130):
        p.poly([(28, y - 10), (48, y - 10), (48, y + 10), (28, y + 10)], (255, 255, 255), 3)
        p.stroke([(60, y), (130, y)], 4, hexc('#9aa4b4'))
    return fin(p)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def seats_pos(cx, cy, n=120, r0=190, r1=470, rows=6):
    seats = []
    radii = [r0 + (r1 - r0) * i / (rows - 1) for i in range(rows)]
    tot = sum(radii)
    for r in radii:
        k = max(2, round(n * r / tot))
        for j in range(k): seats.append((math.pi * (1 - j / (k - 1)), r))
    seats = sorted(seats[:n], key=lambda s: -s[0])
    while len(seats) < n: seats.append(seats[-1])
    return [(cx + r * math.cos(a), cy - r * math.sin(a)) for a, r in seats]


def hemiciclo(c, cx, cy, cols, dot=20, pop=None):
    """cols: lista de 120 cores (None = cinza). pop: lista de índices que 'saltam'."""
    d = ImageDraw.Draw(c)
    pos = seats_pos(cx, cy)
    for i, (x, y) in enumerate(pos):
        col = cols[i] or GRAY
        r = dot * (1.25 if pop and i in pop else 1)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=INK, width=4)


def painel(c):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([60, 700, 1182, 1530], 40, fill=hexc('#f6f1e6'), outline=INK, width=6)


def calendario(c, x, y, n, sz=1.0, col=TEAL):
    sz = max(.08, sz)
    d = ImageDraw.Draw(c)
    w, h = 300 * sz, 280 * sz
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], 22 * sz, fill=WHITE, outline=INK, width=6)
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y - h / 2 + 70 * sz], 22 * sz, fill=col, outline=INK, width=6)
    paste_c(c, txt(str(n), int(130 * sz), 0), x, y + 30 * sz, 1)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, predio(), 640, 1080, 1.0)
    paste_c(c, bandeira().resize((260, 190)), 1040 + 6 * math.sin(f * .1), 600, back(ramp(f, 0, 8)))
    p0 = wt(0, 'novo') - 3
    n0 = wt(0, 'Netanyahu') - 3
    # cadeira vazia "PREMIÊ" no centro
    d = ImageDraw.Draw(c)
    if f >= p0:
        sc = max(.08, back(ramp(f, p0, p0 + 8)))
        x, y = 640, 1330
        d.rounded_rectangle([x - 110 * sc, y - 230 * sc, x + 110 * sc, y + 10 * sc], 30 * sc, fill=hexc('#7a2a4a'), outline=INK, width=6)
        d.rounded_rectangle([x - 140 * sc, y, x + 140 * sc, y + 70 * sc], 20 * sc, fill=hexc('#8f3a5c'), outline=INK, width=6)
        d.rectangle([x - 120 * sc, y + 70 * sc, x - 100 * sc, y + 190 * sc], fill=INK)
        d.rectangle([x + 100 * sc, y + 70 * sc, x + 120 * sc, y + 190 * sc], fill=INK)
        num(c, 'NOVO PREMIÊ?', 640, 1000, f, p0, 110, -4)
    put_pol(c, 1010, 1820, 700, f, 4, hair='#8a8a90', tie='#6b6b70', suit='#2c3550',
            expr='nervous' if f >= n0 else 'neutral', arms='cheek' if f >= n0 else 'hang', look=-1)
    num(c, 'ISRAEL', 640, 520, f, 0, 130, -3)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, n0, .8)
    return c, (640, 1200 + k * 8, z, k), 'dusk'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    paste_c(c, bandeira().resize((260, 190)), 1040 + 5 * math.sin(f * .1), 560, 1)
    a0 = wt(1, 'anunciou') - 3
    m0 = wt(1, 'missao') - 3
    # presidente (cabelo grisalho) entrega envelope a um ex-militar genérico (cabelo curto escuro)
    put_pol(c, 300, 1800, 760, f, 2, hair='#b0b0b6', tie='#2f5fd0', suit='#3a3a44', look=1,
            arms='point' if f >= a0 else 'hang', expr='stern' if f >= a0 else 'neutral')
    put_pol(c, 960, 1800, 760, f, 6, skin=1, hair='#2a221e', tie='#2a9d8f', suit='#2c3550', look=-1,
            arms='up' if f >= m0 + 10 else 'hang', expr='proud' if f >= m0 else 'neutral')
    if f >= a0:
        tt = smooth(ramp(f, m0 - 6, m0 + 10))
        ex = lerp(450, 820, tt); ey = 1400 - 90 * math.sin(tt * math.pi)
        paste_c(c, envelope(), ex, ey, back(ramp(f, a0, a0 + 8)) * .8)
    num(c, 'PRESIDENTE', 300, 930, f, wt(1, 'presidente') - 3, 60, -4)
    num(c, 'EX-CHEFE DO EXÉRCITO', 880, 1010, f, wt(1, 'Exercito') - 3, 50, 4)
    num(c, 'FORMAR O GOVERNO', 640, 600, f, wt(1, 'governo') - 3, 84, 3)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160)))
    k = kick(f, m0, .6)
    return c, (640 + lerp(-40, 40, smooth(ramp(f, 0, 160))), 1150 + k * 6, z, k), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    painel(c)
    v0 = wt(2, 'outubro') - 3
    c0 = wt(2, 'eleicao') - 3
    m0 = wt(2, 'maioria') - 3
    shown = int(clamp((f - c0) / 24) * 120)
    cols = [None] * 120
    if f >= m0:
        for i in range(53): cols[i] = ORG
    hemiciclo(c, 621, 1420, cols if f >= m0 else [None] * 120, dot=20)
    # cobre os que ainda não apareceram
    d = ImageDraw.Draw(c)
    if shown < 120:
        for i, (x, y) in enumerate(seats_pos(621, 1420)):
            if i >= shown: d.ellipse([x - 24, y - 24, x + 24, y + 24], fill=hexc('#f6f1e6'))
    num(c, 'ELEIÇÃO 27/10', 621, 560, f, v0, 100, -3)
    num(c, '120 CADEIRAS', 621, 1480, f, wt(2, 'cento') - 3, 70, -2)
    if f >= m0:
        d.line([(621, 1420), (621, 880)], fill=INK, width=8)
        num(c, 'MAIORIA = 61', 930, 790, f, m0, 56, 4)
        num(c, 'PERDEU!', 300, 790, f, m0 + 4, 70, -6)
    z = lerp(.98, 1.03, smooth(ramp(f, 0, 110))) * (1 + .0003 * f)
    k = kick(f, m0, .6)
    return c, (640, 1130 + k * 6, z, k), 'day'


def s3(f):
    c = CEN('cidade', 'day').copy()
    painel(c)
    s0_ = wt(3, 'sessenta') - 4
    q0 = wt(3, 'quarenta') - 4
    n67 = int(clamp((f - s0_) / 22) * 67)
    n46 = int(clamp((f - q0) / 18) * 46)
    cols = [None] * 120
    for i in range(n67): cols[119 - i] = TEAL
    for i in range(n46): cols[i] = ORG
    hemiciclo(c, 621, 1420, cols, dot=20)
    num(c, 'QUEM DEVE GOVERNAR?', 621, 560, f, 0, 76, -3)
    num(c, '67', 860, 1300, f, s0_ + 2, 170, 4)
    num(c, 'EISENKOT', 900, 820, f, wt(3, 'Eisenkot') - 3, 70, 4)
    num(c, '46', 380, 1300, f, q0 + 2, 170, -4)
    num(c, 'NETANYAHU', 340, 820, f, wt(3, 'Netanyahu') - 3, 70, -4)
    z = lerp(1.12, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0004 * f)
    return c, (640 + 20 * math.sin(f * .04), 1120, z, .5 * math.sin(f * .05)), 'day'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    painel(c)
    a0 = wt(4, 'arabes') - 3
    d0 = wt(4, 'dezenove') - 3
    cr0 = wt(4, 'criticou') - 3
    cols = [None] * 120
    for i in range(46): cols[i] = ORG
    for i in range(67): cols[119 - i] = TEAL
    pop = set()
    if f >= d0:
        k = int(clamp((f - d0) / 14) * 19)
        for i in range(k): cols[119 - i] = GREEN; pop.add(119 - i)
    if f < cr0 + 4:
        hemiciclo(c, 621, 1420, cols, dot=20, pop=pop)
        num(c, 'PARTIDOS ÁRABES', 621, 560, f, a0, 90, -3)
        num(c, '19', 1000, 1250, f, d0, 150, 5)
        z = lerp(1.0, 1.08, smooth(ramp(f, 0, 80))) * (1 + .0012 * f)
        return c, (640 + 15 * math.sin(f * .05), 1120, z, .6 * math.sin(f * .06)), 'dusk'
    # Netanyahu genérico reage
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, predio(), 640, 1000, .85)
    u0 = wt(4, 'uniao') - 3
    put_pol(c, 640, 1800, 820, f, 4, hair='#8a8a90', tie='#6b6b70', suit='#2c3550', look=0,
            arms='up' if f >= u0 else 'point', expr='stern')
    num(c, 'CRÍTICA', 640, 520, f, cr0 + 4, 110, -4)
    num(c, 'UNIÃO NACIONAL?', 640, 700, f, u0, 100, 3)
    lf = f - cr0 - 4
    z = lerp(1.2, 1.08, easeOut(ramp(lf, 0, 30))) + .0005 * lf
    k = kick(f, u0, .6)
    return c, (640, 1200 + k * 6, z, k), 'dusk'


def s5(f):
    c = CEN('mapa', 'dusk').copy()
    if f < wt(5, 'Netanyahu') + 6:
        paste_c(c, txt('POR QUE IMPORTA?', 110, -4), 640, 900, back(ramp(f, 0, 8)))
    t0 = wt(5, 'tempo') - 3
    if f >= t0:
        put_pol(c, 360, 1800, 700, f, 4, hair='#8a8a90', tie='#6b6b70', suit='#2c3550', look=1, expr='neutral')
        num(c, 'MAIS TEMPO NO CARGO', 640, 560, f, t0, 76, -3)
    g0 = wt(5, 'Gaza') - 3
    i0 = wt(5, 'Ira') - 3
    d = ImageDraw.Draw(c)
    for (x, y, lab, f0) in ((760, 1050, 'GAZA', g0), (1000, 1250, 'IRÃ', i0)):
        if f >= f0:
            sc = max(.08, back(ramp(f, f0, f0 + 8))); r = 34 * sc
            d.ellipse([x - r - 5, y - r - 5, x + r + 5, y + r + 5], fill=INK)
            d.ellipse([x - r, y - r, x + r, y + r], fill=RED)
            num(c, lab, x, y - 110, f, f0, 90, -3)
    l0 = wt(5, 'decide') - 3
    num(c, 'QUEM DECIDE?', 640, 780, f, l0, 90, 4)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 170)))
    return c, (640, 1150, z, lerp(0, -2, smooth(ramp(f, 0, 170)))), 'dusk'


def s6(f):
    c = CEN('cidade', 'dusk').copy()
    v0 = wt(6, 'vinte') - 3
    c0 = wt(6, 'catorze') - 3
    u0 = wt(6, 'urnas') - 3
    put_pol(c, 1020, 1800, 640, f, 6, skin=1, hair='#2a221e', tie='#2a9d8f', suit='#2c3550', look=-1,
            expr='nervous' if f >= wt(6, 'falhar') - 3 else 'stern')
    if f >= v0:
        sc = back(ramp(f, v0, v0 + 8))
        n = int(lerp(1, 28, clamp((f - v0) / 20)))
        calendario(c, 380, 760, n, sz=sc)
        num(c, 'DIAS', 380, 560, f, v0 + 4, 80, -3)
    if f >= c0:
        calendario(c, 760, 760, 14, sz=back(ramp(f, c0, c0 + 8)) * .8, col=ORG)
        num(c, '+', 570, 770, f, c0, 120, 0)
    if f >= u0:
        paste_c(c, urna(), 500, 1300, back(ramp(f, u0, u0 + 8)) * .75)
        ced = cedula()
        for i in range(4):
            tt = clamp((f - u0 - i * 5) / 12)
            if 0 < tt < 1: paste_c(c, ced, lerp(150 + i * 120, 500, tt), lerp(1000, 1180, tt * tt), .7)
        num(c, 'NOVA ELEIÇÃO?', 640, 1010, f, u0, 90, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 150)))
    k = kick(f, u0, .6)
    return c, (640, 1150 + k * 6, z, k - .006 * f), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'novo') - 3, 160, .7)
    s.ting(s.W(0, 'Netanyahu') - 3, .25)
    s.ting(s.W(1, 'presidente') - 3, .25)
    s.whoosh(s.W(1, 'missao') - 6, .4, .3)
    s.patter(s.W(2, 'eleicao') - 3, s.W(2, 'eleicao') + 21, 10, .12)
    s.thunk(s.W(2, 'maioria') - 3, 140, .6)
    s.patter(s.W(3, 'sessenta') - 4, s.W(3, 'sessenta') + 18, 10, .12)
    s.patter(s.W(3, 'quarenta') - 4, s.W(3, 'quarenta') + 14, 8, .12)
    s.ting(s.W(4, 'dezenove') - 3, .3)
    s.thunk(s.W(4, 'uniao') - 3, 160, .5)
    s.ting(s.W(5, 'Gaza') - 3, .25)
    s.ting(s.W(5, 'Ira') - 3, .25)
    s.ting(s.W(6, 'vinte') - 3, .3)
    s.thunk(s.W(6, 'urnas') - 3, 140, .7)
