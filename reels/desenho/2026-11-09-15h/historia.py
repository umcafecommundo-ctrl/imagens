"""Um Café com o Mundo — O MUNDO EXPLICADO (segunda 09/11/2026, 15h).
Tema: África do Sul — eleições municipais; o ANC (Congresso Nacional Africano, partido de Mandela) tem o pior resultado.
Fontes (conferidas em 09/11/2026):
- Reuters (via CNBC Africa), 09/11/2026 ("South Africa's ANC takes a beating in municipal vote, setting up tough
  coalition talks"): ANC 30,76% (45,59% em 2021), DA 24,64%, MK (partido de Zuma) 9,76%; em Joanesburgo DA ~35%,
  ANC ~20%, ActionSA 16%; 14 dias para negociar coalizões antes de formar as câmaras; queda ligada a falhas em
  serviços básicos como água e eletricidade; Mbalula (ANC) chamou o resultado de "catastrófico".
- Mail & Guardian, 08/11/2026 (resultados finais da IEC): 15,6 milhões de eleitores; câmaras sem maioria
  (hung councils) subiram para 142, contra 70 em 2021.
- 10 Things Global News, 09/11/2026: derrota recorde do ANC.
Personagens genéricos (sem traços de pessoas reais). Tom neutro."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O partido de Nelson Mandela acaba de ter o pior resultado da sua história.",
    "Nas eleições municipais da África do Sul, o Congresso Nacional Africano ficou com só trinta e um por cento dos votos.",
    "Em dois mil e vinte e um, eram quase quarenta e seis.",
    "A oposição, a Aliança Democrática, teve vinte e cinco por cento, e ficou na frente em Joanesburgo, a maior cidade do país.",
    "Agora, cento e quarenta e duas câmaras municipais estão sem maioria, o dobro de dois mil e vinte e um.",
    "Por que isso importa? O partido governa o país desde o fim do apartheid, mas a falta de água e de luz pesou no voto.",
    "Os partidos têm catorze dias para fechar alianças e decidir quem governa as cidades.",
]
CAPTXT = [
    "O partido de Nelson Mandela acaba de ter|o pior resultado da sua história.",
    "Nas eleições municipais da África do Sul,|o Congresso Nacional Africano|ficou com só 31% dos votos.",
    "Em 2021, eram quase 46%.",
    "A oposição, a Aliança Democrática, teve 25%,|e ficou na frente em Joanesburgo,|a maior cidade do país.",
    "Agora, 142 câmaras municipais|estão sem maioria,|o dobro de 2021.",
    "Por que isso importa? O partido governa o país|desde o fim do apartheid, mas a falta|de água e de luz pesou no voto.",
    "Os partidos têm 14 dias para fechar alianças|e decidir quem governa as cidades.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Mandela', 4), (0, 'pior', 4), (1, 'Africa', 4), (1, 'trinta', 6), (2, 'quarenta', 6),
         (3, 'vinte', 6), (3, 'Joanesburgo', 4), (4, 'cento', 6), (4, 'dobro', 4), (5, 'apartheid', 4),
         (5, 'agua', 4), (5, 'luz', 4), (6, 'catorze', 6), (6, 'aliancas', 4)]

TEAL = hexc('#2a9d8f'); TEAL_D = hexc('#1d6f65'); ORG = hexc('#e07b2a'); ORG_D = hexc('#a85a1c')
GREEN = hexc('#7ccf5a'); GRAY = hexc('#d9dde3'); FBLUE = hexc('#2f5fd0'); WHITE = (255, 255, 255)
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); RED = hexc('#d8443c')
SAGREEN = hexc('#007a4d'); SAYEL = hexc('#ffb612'); SARED = hexc('#de3831'); SABLUE = hexc('#002395')
DGREEN = hexc('#2e8b57'); DBLUE = hexc('#2f5fd0')
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


def seats_pos(cx, cy, n=131, r0=190, r1=470, rows=6):
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
    """cols: lista de 131 cores (None = cinza). pop: lista de índices que 'saltam'."""
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



def pct_bar(c, x, y, frac, col, w=170, hmax=520):
    d = ImageDraw.Draw(c)
    h = hmax * frac
    d.rounded_rectangle([x - w / 2, y - h, x + w / 2, y], 20, fill=col, outline=INK, width=6)



@lru_cache(maxsize=2)
def sa_flag():
    """bandeira da África do Sul (país, permitido). 600x400"""
    W_, H_ = 600, 400
    p = Pen(W_, H_)
    p.poly([(10, 10), (590, 10), (590, 200), (10, 200)], SARED)
    p.poly([(10, 200), (590, 200), (590, 390), (10, 390)], SABLUE)
    # Y branco
    p.poly([(10, 10), (110, 10), (300, 150), (590, 150), (590, 250), (300, 250), (110, 390), (10, 390)], WHITE)
    # Y verde
    p.poly([(10, 40), (70, 40), (270, 175), (590, 175), (590, 225), (270, 225), (70, 360), (10, 360)], SAGREEN)
    # triângulo amarelo e preto
    p.poly([(10, 75), (190, 200), (10, 325)], SAYEL)
    p.poly([(10, 105), (150, 200), (10, 295)], INK)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def sa_map():
    """silhueta simplificada da África do Sul. 760x620"""
    p = Pen(760, 620)
    pts = [(40, 90), (130, 120), (210, 70), (300, 110), (390, 60), (470, 40), (560, 20), (650, 60), (700, 150),
           (690, 250), (640, 330), (560, 420), (460, 500), (360, 540), (250, 560), (160, 590), (110, 560),
           (90, 470), (60, 360), (30, 230)]
    p.shape(pts, hexc('#e9c46a'), hexc('#c49a3c'), 6, 12)
    return fin(p)


@lru_cache(maxsize=2)
def torneira():
    p = Pen(420, 360)
    p.shape([(20, 60), (260, 60), (260, 140), (20, 140)], hexc('#cfd6df'), hexc('#8f9bab'), 6, 6)
    p.shape([(200, 60), (280, 60), (330, 140), (330, 300), (250, 300), (250, 150)], hexc('#cfd6df'), hexc('#8f9bab'), 6, 8)
    p.shape([(100, 10), (180, 10), (180, 60), (100, 60)], hexc('#cfd6df'), hexc('#8f9bab'), 5, 5)
    return fin(p)


@lru_cache(maxsize=2)
def lampada():
    p = Pen(300, 420)
    p.shape(ell_pts(150, 150, 120, 130), hexc('#9aa0aa'), hexc('#6c727c'), 6, 10)
    p.shape([(95, 260), (205, 260), (195, 340), (105, 340)], hexc('#7d8590'), hexc('#555b64'), 5, 5)
    p.stroke([(110, 300), (190, 300)], 5)
    p.stroke([(120, 160), (150, 120), (180, 160)], 6, hexc('#4a4f58'))
    return fin(p)


def municipios(c, n_cinza, show, x0=150, y0=820, cols_=16):
    """213 quadradinhos: n_cinza 'sem maioria' (cinza) e o resto colorido. show 0..1 aparece."""
    d = ImageDraw.Draw(c)
    total = 213
    k = int(total * show)
    for i in range(k):
        r, q = divmod(i, cols_)
        x = x0 + q * 59; y = y0 + r * 50
        col = GRAY if i < n_cinza else (TEAL if i % 3 else ORG)
        d.rounded_rectangle([x, y, x + 46, y + 40], 8, fill=col, outline=INK, width=3)


def s0(f):
    c = CEN('cidade', 'day').copy()
    m_ = wt(0, 'Mandela') - 3
    p_ = wt(0, 'pior') - 3
    paste_c(c, urna(), 640, 1300, back(ramp(f, 0, 8)) * .9)
    ced = cedula()
    for i in range(5):
        tt = clamp((f - 4 - i * 7) / 14)
        if 0 < tt < 1: paste_c(c, ced, lerp(150 + i * 230, 640, tt), lerp(650, 1130, tt * tt), .8)
    num(c, 'PARTIDO DE MANDELA', 640, 560, f, m_, 80, -3)
    if f >= p_:
        num(c, 'PIOR RESULTADO', 640, 740, f, p_, 100, 3)
        num(c, 'DA HISTÓRIA', 640, 860, f, p_ + 4, 100, -3)
        d = ImageDraw.Draw(c)
        yy = 960 + 60 * smooth(ramp(f, p_, p_ + 14))
        d.polygon([(980, yy + 120), (920, yy), (1040, yy)], fill=RED, outline=INK, width=5)
    z = lerp(1.35, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, p_, .8)
    return c, (640, 1120 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('mapa', 'day').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#3f8fd6'))
    for yy in range(450, 1650, 120):
        ImageDraw.Draw(c).arc([100 + (yy * 7) % 600, yy, 220 + (yy * 7) % 600, yy + 40], 200, 340, fill=hexc('#8cc4f0'), width=6)
    a0 = wt(1, 'Africa') - 3
    t0 = wt(1, 'trinta') - 3
    paste_c(c, sa_map(), 640 + 6 * math.sin(f * .05), 1150, back(ramp(f, 0, 10)) * 1.1)
    if f >= a0:
        paste_c(c, sa_flag(), 640, 1150, back(ramp(f, a0, a0 + 8)) * .45)
    num(c, 'ÁFRICA DO SUL', 640, 560, f, a0, 110, -3)
    num(c, 'ELEIÇÃO MUNICIPAL', 640, 700, f, wt(1, 'municipais') - 3, 70, 3)
    if f >= t0:
        paste_c(c, txt('30,8%', 200, -4), 640, 900, back(ramp(f, t0, t0 + 8)))
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140))) * (1 + .0009 * f)
    k = kick(f, t0, .6)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 140))), 1100 + k * 6, z, k + lerp(0, -1.5, smooth(ramp(f, 0, 140)))), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    painel(c)
    q0 = wt(2, 'quarenta') - 3
    num(c, '2021', 430, 1470, f, 0, 70, 0)
    num(c, '2026', 830, 1470, f, 0, 70, 0)
    h1 = .46 * smooth(ramp(f, 0, 16))
    pct_bar(c, 430, 1410, h1, SAGREEN, w=200, hmax=1100)
    pct_bar(c, 830, 1410, .308 * smooth(ramp(f, 0, 16)), SAGREEN, w=200, hmax=1100)
    num(c, '30,8%', 830, 1410 - 1100 * .308 - 70, f, 6, 80, 3)
    num(c, '~46%', 430, 1410 - 1100 * h1 - 70, f, q0, 90, -4)
    if f >= q0 + 10:
        num(c, '-15 PONTOS', 640, 560, f, q0 + 10, 110, -3)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 60))) * (1 + .0008 * f)
    k = kick(f, q0, .6)
    return c, (640 + 10 * math.sin(f * .05), 1120 + k * 6, z, k), 'day'


def s3(f):
    c = CEN('cidade', 'day').copy()
    v0 = wt(3, 'vinte') - 3
    j0 = wt(3, 'Joanesburgo') - 3
    put_pol(c, 300, 1800, 620, f, 2, hair='#2a221e', tie='#2f5fd0', suit='#2c3550', look=1, skin=3,
            expr='smug' if f >= j0 else 'neutral', arms='up' if f >= j0 else 'hang')
    put_pol(c, 960, 1800, 620, f, 6, skin=3, hair='#2a221e', tie='#d8443c', suit='#3a3a44', look=-1,
            expr='nervous' if f >= v0 else 'neutral')
    num(c, 'OPOSIÇÃO', 420, 560, f, wt(3, 'oposicao') - 3, 90, -3)
    if f >= v0:
        num(c, '24,6%', 420, 700, f, v0, 120, -4)
    if f >= j0:
        num(c, 'NA FRENTE EM', 640, 860, f, j0, 70, 3)
        num(c, 'JOANESBURGO', 640, 960, f, j0 + 3, 100, -3)
    z = lerp(1.06, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0008 * f)
    k = kick(f, j0, .6)
    return c, (640 + 15 * math.sin(f * .05), 1150 + k * 6, z, k + .5 * math.sin(f * .06)), 'day'


def s4(f):
    c = CEN('cidade', 'day').copy()
    painel(c)
    c0 = wt(4, 'cento') - 4
    d0 = wt(4, 'dobro') - 3
    municipios(c, 142, smooth(ramp(f, 0, 20)), x0=165, y0=760)
    if f >= c0:
        num(c, '142', 640, 1080, f, c0, 200, -4)
        num(c, 'SEM MAIORIA', 640, 1250, f, c0 + 4, 90, 3)
    if f >= d0:
        num(c, 'EM 2021: 70', 640, 680, f, d0 - 6, 64, -3)
        num(c, 'O DOBRO!', 640, 560, f, d0, 110, 4)
    z = lerp(1.1, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0006 * f)
    k = kick(f, d0, .6)
    return c, (640, 1120 + k * 6, z, k), 'day'


def s5(f):
    c = CEN('cidade', 'dusk').copy()
    a0 = wt(5, 'apartheid') - 3
    g0 = wt(5, 'agua') - 3
    l0 = wt(5, 'luz') - 3
    num(c, 'POR QUE IMPORTA?', 640, 560, f, 0, 90, -3)
    if f >= a0:
        num(c, 'NO PODER DESDE 1994', 640, 700, f, a0, 72, 3)
    if f >= g0:
        paste_c(c, torneira(), 380, 1050, back(ramp(f, g0, g0 + 8)) * 1.0)
        if (f // 10) % 3 == 0:
            ImageDraw.Draw(c).ellipse([420, 1170, 446, 1206], fill=hexc('#8cc4f0'), outline=INK, width=3)
        num(c, 'ÁGUA', 380, 1300, f, g0, 90, -4)
    if f >= l0:
        paste_c(c, lampada(), 880, 1040, back(ramp(f, l0, l0 + 8)) * 1.0)
        num(c, 'LUZ', 880, 1300, f, l0, 90, 4)
    z = lerp(1.0, 1.14, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    k = kick(f, g0, .6)
    return c, (640, 1100 + k * 6, z, k), 'dusk'


def s6(f):
    c = CEN('cidade', 'dusk').copy()
    c0 = wt(6, 'catorze') - 3
    a0 = wt(6, 'aliancas') - 3
    put_pol(c, 300, 1800, 600, f, 2, hair='#2a221e', tie='#2f5fd0', suit='#2c3550', look=1, skin=3,
            expr='nervous', arms='cheek' if f >= a0 else 'hang')
    put_pol(c, 960, 1800, 600, f, 6, skin=3, hair='#2a221e', tie='#d8443c', suit='#3a3a44', look=-1,
            expr='nervous', arms='point' if f >= a0 else 'hang')
    if f >= c0:
        calendario(c, 640, 880, 14, sz=back(ramp(f, c0, c0 + 8)) * 1.1, col=SAGREEN)
        num(c, 'DIAS', 640, 1100, f, c0 + 3, 80, -3)
    if f >= a0:
        paste_c(c, txt('ALIANÇAS?', 110, -5), 640, 600, back(ramp(f, a0, a0 + 8)))
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    k = kick(f, a0, .6)
    return c, (640, 1150 + k * 6, z, k - .006 * f), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'pior') - 3, 160, .6)
    s.ting(s.W(1, 'Africa') - 3, .25)
    s.thunk(s.W(1, 'trinta') - 3, 150, .5)
    s.ting(s.W(2, 'quarenta') - 3, .3)
    s.ting(s.W(3, 'Joanesburgo') - 3, .3)
    s.patter(s.W(4, 'cento') - 4, s.W(4, 'cento') + 20, 10, .12)
    s.thunk(s.W(4, 'dobro') - 3, 140, .6)
    s.ting(s.W(5, 'agua') - 3, .25)
    s.ting(s.W(5, 'luz') - 3, .25)
    s.thunk(s.W(6, 'aliancas') - 3, 140, .7)
