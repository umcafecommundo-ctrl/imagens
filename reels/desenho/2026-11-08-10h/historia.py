"""Um Café com o Mundo — O MUNDO EXPLICADO (domingo 08/11/2026, 10h).
Tema: Nova Zelândia — eleição geral de 07/11/2026 sem vencedor definido ("eleição do supermercado").
Fontes (conferidas em 08/11/2026):
- Al Jazeera, 07/11/2026 ("New Zealand's governing coalition holds slim majority in preliminary count"):
  contagem preliminar dá à coalizão de Christopher Luxon (National, ACT, NZ First) 67 de 131 cadeiras projetadas,
  uma a mais que as 66 necessárias; National e Labour com pouco menos de 30% cada; cerca de 14% dos votos (a maioria
  votos especiais) ainda por contar, que historicamente favorecem a esquerda; resultado final em 27/11;
  campanha apelidada de "eleição do supermercado" por causa do preço dos alimentos; Luxon: "apertado demais para cravar";
  Chris Hipkins (Labour) é o líder da oposição; coalizão segue como governo provisório.
- CNN, 07/11/2026: "Nova Zelândia em suspense político após votação apertada".
- AP (via Yahoo), 2026: eleição em 07/11; custo de vida e moradia como temas principais.
Personagens genéricos (sem traços de pessoas reais). Tom neutro."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um país inteiro votou pensando no preço do supermercado, e ninguém sabe quem ganhou.",
    "Na Nova Zelândia, a eleição de sábado ganhou o apelido de eleição do supermercado.",
    "Os dois maiores partidos ficaram com quase trinta por cento cada.",
    "O grupo do primeiro-ministro Christopher Luxon tem sessenta e sete de cento e trinta e uma cadeiras, só uma acima da maioria.",
    "Mas ainda faltam catorze por cento dos votos, que costumam favorecer a esquerda.",
    "O resultado final sai só no dia vinte e sete. Até lá, suspense.",
]
CAPTXT = [
    "Um país inteiro votou pensando|no preço do supermercado,|e ninguém sabe quem ganhou.",
    "Na Nova Zelândia, a eleição de sábado|ganhou o apelido de|eleição do supermercado.",
    "Os dois maiores partidos ficaram|com quase 30% cada.",
    "O grupo do primeiro-ministro Christopher Luxon|tem 67 de 131 cadeiras,|só uma acima da maioria.",
    "Mas ainda faltam 14% dos votos,|que costumam favorecer a esquerda.",
    "O resultado final sai só no dia 27.|Até lá, suspense.",
]
FALA_TIKTOK = "Quem você acha que leva? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'supermercado', 4), (0, 'ganhou', 4), (1, 'Zelandia', 4), (1, 'supermercado', 4),
         (2, 'trinta', 6), (3, 'sessenta', 6), (3, 'cento', 8), (3, 'maioria', 4),
         (4, 'catorze', 6), (4, 'esquerda', 4), (5, 'vinte', 6), (5, 'suspense', 6)]

TEAL = hexc('#2a9d8f'); TEAL_D = hexc('#1d6f65'); ORG = hexc('#e07b2a'); ORG_D = hexc('#a85a1c')
GREEN = hexc('#7ccf5a'); GRAY = hexc('#d9dde3'); FBLUE = hexc('#2f5fd0'); WHITE = (255, 255, 255)
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); RED = hexc('#d8443c')
NZBLUE = hexc('#1f3a8a'); NZRED = hexc('#d22b2b')

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



@lru_cache(maxsize=2)
def carrinho():
    """carrinho de supermercado com compras. 700x620, rodas y~600"""
    p = Pen(700, 620)
    # compras saindo do carrinho
    p.shape(ell_pts(250, 190, 70, 80), hexc('#f2c14e'), hexc('#c9952a'), 5, 6)   # pão
    p.shape([(330, 90), (400, 90), (410, 250), (320, 250)], hexc('#f4f4f4'), hexc('#c9c9d2'), 5, 6)  # leite
    p.poly([(330, 140), (405, 140), (407, 175), (326, 175)], FBLUE)
    p.shape(ell_pts(470, 200, 60, 60), hexc('#e2453c'), hexc('#a8322b'), 5, 6)  # maçã
    p.stroke([(470, 140), (480, 110)], 6)
    p.shape([(150, 140), (215, 140), (220, 250), (145, 250)], hexc('#7ccf5a'), hexc('#4e9a35'), 5, 6)  # pacote
    # cesto
    p.shape([(90, 230), (640, 230), (580, 470), (160, 470)], hexc('#c9d3df'), hexc('#8f9bab'), 6, 10)
    for x in range(150, 620, 60):
        p.stroke([(x, 240), (x - 10 + (x - 360) * .1, 460)], 4, hexc('#8f9bab'))
    for y in (300, 370, 430):
        p.stroke([(110 + (y - 230) * .25, y), (625 - (y - 230) * .22, y)], 4, hexc('#8f9bab'))
    p.stroke([(640, 230), (690, 120), (700, 110)], 10)
    p.stroke([(160, 470), (180, 540), (580, 540)], 8)
    p.dot(210, 580, 30, hexc('#3a3a44'), 5)
    p.dot(540, 580, 30, hexc('#3a3a44'), 5)
    return fin(p)


@lru_cache(maxsize=2)
def etiqueta():
    p = Pen(360, 220)
    p.shape([(40, 10), (350, 10), (350, 210), (40, 210), (10, 110)], hexc('#ffd84a'), hexc('#d9ad1f'), 6, 6)
    p.dot(55, 110, 14, WHITE, 4)
    return fin(p)


@lru_cache(maxsize=2)
def nz_map():
    """duas ilhas genéricas da Nova Zelândia (silhueta simplificada). 520x800"""
    p = Pen(520, 800)
    north = [(300, 20), (340, 90), (330, 160), (420, 230), (470, 300), (420, 350), (380, 420), (320, 400),
             (300, 330), (250, 280), (270, 200), (230, 120), (260, 60)]
    south = [(260, 430), (300, 450), (270, 520), (220, 600), (170, 690), (110, 770), (40, 760), (60, 690),
             (120, 610), (180, 530), (220, 470)]
    p.shape(north, hexc('#7ccf5a'), hexc('#4e9a35'), 6, 10)
    p.shape(south, hexc('#7ccf5a'), hexc('#4e9a35'), 6, 10)
    return fin(p)


def pct_bar(c, x, y, frac, col, w=170, hmax=520):
    d = ImageDraw.Draw(c)
    h = hmax * frac
    d.rounded_rectangle([x - w / 2, y - h, x + w / 2, y], 20, fill=col, outline=INK, width=6)


def s0(f):
    c = CEN('cidade', 'day').copy()
    s_ = wt(0, 'supermercado') - 3
    g_ = wt(0, 'ganhou') - 3
    # carrinho chega deslizando
    cx = lerp(-300, 640, easeOut(ramp(f, 0, 14)))
    paste_c(c, carrinho(), cx, 1270, .9)
    if f >= s_:
        paste_c(c, etiqueta(), 900 + 4 * math.sin(f * .2), 900, back(ramp(f, s_, s_ + 8)))
        paste_c(c, txt('$$$', 90, -6), 920, 900, back(ramp(f, s_ + 2, s_ + 10)))
    num(c, 'PREÇO DO MERCADO', 640, 600, f, s_, 70, -3)
    if f >= g_:
        paste_c(c, txt('QUEM GANHOU?', 90, 4), 600, 740, back(ramp(f, g_, g_ + 8)))
    z = lerp(1.35, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, g_, .8)
    return c, (640, 1150 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('mapa', 'day').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#3f8fd6'))
    for yy in range(450, 1650, 120):
        ImageDraw.Draw(c).arc([100 + (yy * 7) % 600, yy, 220 + (yy * 7) % 600, yy + 40], 200, 340, fill=hexc('#8cc4f0'), width=6)
    paste_c(c, nz_map(), 680 + 6 * math.sin(f * .05), 1080, back(ramp(f, 0, 10)) * 1.15)
    z0 = wt(1, 'Zelandia') - 3
    num(c, 'NOVA ZELÂNDIA', 640, 540, f, z0, 110, -3)
    a0 = wt(1, 'apelido') - 3
    sp = wt(1, 'supermercado', 0) - 3
    if f >= a0:
        paste_c(c, carrinho(), 330, 1300, back(ramp(f, a0, a0 + 8)) * .5)
    num(c, '"ELEIÇÃO DO', 640, 740, f, sp - 4, 84, 3)
    num(c, 'SUPERMERCADO"', 640, 840, f, sp, 84, 3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140))) * (1 + .0009 * f)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 140))), 1100, z, lerp(0, -1.5, smooth(ramp(f, 0, 140)))), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    t0 = wt(2, 'trinta') - 3
    fr = .55 * smooth(ramp(f, t0 - 6, t0 + 12))
    put_pol(c, 330, 1800, 640, f, 2, hair='#5a4a3e', tie='#2f5fd0', suit='#2c3550', look=1,
            expr='nervous' if f >= t0 else 'neutral')
    put_pol(c, 950, 1800, 640, f, 6, skin=1, hair='#2a221e', tie='#d8443c', suit='#3a3a44', look=-1,
            expr='nervous' if f >= t0 else 'neutral')
    if fr > .03:
        pct_bar(c, 520, 1500, fr, NZBLUE)
        pct_bar(c, 760, 1500, fr, NZRED)
    num(c, '~30%', 500, 1500 - 520 * fr - 70, f, t0, 64, -4)
    num(c, '~30%', 780, 1500 - 520 * fr - 150, f, t0 + 2, 64, 4)
    num(c, 'EMPATE?', 640, 560, f, t0 + 10, 110, -3)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0008 * f)
    return c, (640 + 15 * math.sin(f * .05), 1150, z, .5 * math.sin(f * .06)), 'day'


def s3(f):
    c = CEN('cidade', 'day').copy()
    painel(c)
    s0_ = wt(3, 'sessenta') - 4
    c0 = wt(3, 'cento') - 3
    m0 = wt(3, 'maioria') - 3
    n67 = int(clamp((f - s0_) / 22) * 67)
    cols = [None] * 131
    for i in range(n67): cols[130 - i] = TEAL
    hemiciclo(c, 621, 1420, cols, dot=18)
    num(c, 'GRUPO DO PREMIÊ', 621, 560, f, wt(3, 'grupo') - 3, 84, -3)
    num(c, '67', 980, 1010, f, s0_ + 2, 150, 4)
    num(c, 'DE 131', 621, 1500, f, c0, 64, -2)
    if f >= m0:
        d = ImageDraw.Draw(c)
        d.line([(621, 1420), (621, 880)], fill=INK, width=8)
        num(c, 'MAIORIA = 66', 380, 790, f, m0, 60, -4)
        num(c, 'POR 1!', 900, 790, f, m0 + 4, 90, 6)
    z = lerp(1.1, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0004 * f)
    k = kick(f, m0, .6)
    return c, (640, 1120 + k * 6, z, k), 'day'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    c0 = wt(4, 'catorze') - 3
    e0 = wt(4, 'esquerda') - 3
    paste_c(c, urna(), 640, 1250, back(ramp(f, 0, 8)) * .95)
    ced = cedula()
    for i in range(6):
        tt = clamp((f - c0 - i * 6) / 14)
        if 0 < tt < 1: paste_c(c, ced, lerp(150 + i * 170, 640, tt), lerp(700, 1080, tt * tt), .8)
    num(c, 'AINDA FALTAM', 640, 540, f, wt(4, 'faltam') - 3, 90, -3)
    num(c, '14%', 640, 760, f, c0, 190, 4)
    if f >= e0:
        num(c, 'ESQUERDA?', 900, 960, f, e0, 80, 6)
        d = ImageDraw.Draw(c)
        xa = 900 - 30 * smooth(ramp(f, e0, e0 + 10))
        d.polygon([(xa - 160, 1010), (xa - 80, 980), (xa - 80, 1040)], fill=RED, outline=INK)
    z = lerp(1.0, 1.14, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    k = kick(f, c0, .6)
    return c, (640, 1120 + k * 6, z, k), 'dusk'


def s5(f):
    c = CEN('cidade', 'dusk').copy()
    v0 = wt(5, 'vinte') - 3
    s_ = wt(5, 'suspense') - 3
    put_pol(c, 330, 1800, 600, f, 2, hair='#5a4a3e', tie='#2f5fd0', suit='#2c3550', look=1,
            expr='nervous', arms='cheek' if f >= s_ else 'hang')
    put_pol(c, 950, 1800, 600, f, 6, skin=1, hair='#2a221e', tie='#d8443c', suit='#3a3a44', look=-1,
            expr='nervous', arms='cheek' if f >= s_ else 'hang')
    if f >= v0:
        calendario(c, 640, 900, 27, sz=back(ramp(f, v0, v0 + 8)) * 1.1, col=NZRED)
        num(c, 'NOVEMBRO', 640, 700, f, v0 + 3, 70, -3)
    num(c, 'RESULTADO FINAL', 640, 540, f, wt(5, 'resultado') - 3, 90, -3)
    if f >= s_:
        paste_c(c, txt('SUSPENSE...', 120, -5), 640, 1180, back(ramp(f, s_, s_ + 8)))
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    k = kick(f, s_, .6)
    return c, (640, 1150 + k * 6, z, k - .006 * f), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    s.ting(s.W(0, 'supermercado') - 3, .3)
    s.thunk(s.W(0, 'ganhou') - 3, 160, .6)
    s.ting(s.W(1, 'Zelandia') - 3, .25)
    s.ting(s.W(2, 'trinta') - 3, .3)
    s.patter(s.W(3, 'sessenta') - 4, s.W(3, 'sessenta') + 18, 10, .12)
    s.thunk(s.W(3, 'maioria') - 3, 140, .6)
    s.patter(s.W(4, 'catorze') - 3, s.W(4, 'catorze') + 30, 8, .12)
    s.ting(s.W(5, 'vinte') - 3, .3)
    s.thunk(s.W(5, 'suspense') - 3, 140, .7)
