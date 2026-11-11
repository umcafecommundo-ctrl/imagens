"""Um Café com o Mundo — O MUNDO EXPLICADO (quarta 11/11/2026, 19h).
Tema: Irã declara a Marinha e a Força Aérea da Argentina "organizações terroristas".
Fontes (conferidas em 11/11/2026):
- AFP via La Nación (Argentina) e Emol (Chile), 11/11/2026: em 11/11 o Ministério das Relações Exteriores do Irã, em Teerã,
  designou a Armada e a Força Aérea argentinas como organizações terroristas, pelo "princípio de reciprocidade"; lei iraniana
  de 2019; Irã diz que a Argentina "assumirá a responsabilidade por todas as consequências", sem dizer quais; resposta à decisão
  do governo Milei de classificar a Guarda Revolucionária como organização terrorista (março de 2026); Buenos Aires culpa a
  Guarda Revolucionária de apoiar o Hezbollah, apontado como autor dos atentados à embaixada de Israel (1992, 29 mortos) e à
  AMIA (1994, 85 mortos).
- Aviacionline, 11/11/2026: decisão argentina em 31/03/2026 (Comunicado 143, inclusão no RePET); sem sanções concretas
  detalhadas pelo Irã. Reuters (via Just Security, 11/11/2026) também registra a designação.
Tom sério; personagens genéricos; sem pessoas reais desenhadas."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O Irã acaba de chamar a Marinha e a Força Aérea da Argentina de organizações terroristas.",
    "Nesta quarta, em Teerã, o governo iraniano falou em reciprocidade.",
    "É uma resposta: em março, o governo de Javier Milei pôs a Guarda Revolucionária do Irã na lista de terroristas da Argentina.",
    "A Argentina acusa o Irã de apoiar o Hezbollah, apontado como autor de dois atentados em Buenos Aires.",
    "Vinte e nove mortos na embaixada de Israel, em noventa e dois, e oitenta e cinco na AMIA, em noventa e quatro.",
    "Por que isso importa? A tensão da guerra no Oriente Médio chega à América do Sul, aqui do lado do Brasil.",
    "O Irã avisa que a Argentina vai arcar com as consequências, mas não disse quais. Por enquanto, não há sanção concreta.",
]
CAPTXT = [
    "O Irã acaba de chamar a Marinha e a Força Aérea|da Argentina de organizações terroristas.",
    "Nesta quarta, em Teerã,|o governo iraniano falou em reciprocidade.",
    "É uma resposta: em março, o governo de Javier Milei|pôs a Guarda Revolucionária do Irã|na lista de terroristas da Argentina.",
    "A Argentina acusa o Irã de apoiar o Hezbollah,|apontado como autor de dois atentados|em Buenos Aires.",
    "29 mortos na embaixada de Israel, em 92,|e 85 na AMIA, em 94.",
    "Por que isso importa? A tensão da guerra no Oriente Médio|chega à América do Sul,|aqui do lado do Brasil.",
    "O Irã avisa que a Argentina vai arcar com as consequências,|mas não disse quais.|Por enquanto, não há sanção concreta.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Marinha', 4), (0, 'Aerea', 4), (0, 'terroristas', 4), (1, 'quarta', 4), (1, 'Teera', 4), (1, 'reciprocidade', 4),
         (2, 'marco', 4), (2, 'Milei', 4), (2, 'lista', 4), (3, 'Hezbollah', 4), (3, 'dois', 4), (3, 'Buenos', 4),
         (4, 'Vinte', 4), (4, 'oitenta', 4), (4, 'AMIA', 4), (5, 'importa', 4), (5, 'America', 4), (5, 'Brasil', 4),
         (6, 'consequencias', 4), (6, 'quais', 4), (6, 'sancao', 4)]

RED = hexc('#e0393e'); RED_D = hexc('#a82a2e'); WHITE = (255, 255, 255)
GOLD = hexc('#f2c14e'); GOLD_D = hexc('#b8862a'); DARK = hexc('#2b2d3a')
GLASS = hexc('#bfe3f2'); FRIDGE = hexc('#e9eef3'); FRIDGE_D = hexc('#b9c3cd')
EUB = hexc('#2445a8'); STONE = hexc('#e8e1d2'); STONE_D = hexc('#c2b8a3')
IRG = hexc('#2f9a55'); IRR = hexc('#d8382f'); CODE = hexc('#5cf08a')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def escurece(c, a, col=(20, 18, 40)):
    if a <= 0: return
    c.alpha_composite(Image.new('RGBA', c.size, col + (int(a),)))


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def pessoa(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550'):
    """pessoa genérica de terno. 600x1000, pés y~975."""
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


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


@lru_cache(maxsize=2)
def bandeira_ir():
    """bandeira do Irã simplificada (país): faixas verde, branca e vermelha. 600x400"""
    p = Pen(600, 400)
    for i, cc in enumerate((IRG, WHITE, IRR)):
        p.poly([(10, 10 + i * 127), (590, 10 + i * 127), (590, 10 + (i + 1) * 127), (10, 10 + (i + 1) * 127)], cc)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


def _estrela(cx, cy, r, rot=0.0):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + rot + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .4
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


def put_band(c, im, x, y, w, f, s=1.0, pole=True):
    if s <= .02: return
    ww = int(w * s); hh = int(w * .66 * s)
    im = im.resize((ww, hh)).rotate(3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    if pole:
        d = ImageDraw.Draw(c)
        d.line([(x - ww / 2 - 4, y - hh / 2), (x - ww / 2 - 4, y + hh * 1.6)], fill=INK, width=10)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=2)
def podio():
    """púlpito genérico. 520x560, base y~550"""
    p = Pen(520, 560)
    p.shape([(60, 60), (460, 60), (420, 550), (100, 550)], hexc('#7a4e33'), hexc('#57361f'), 7, 14)
    p.shape([(30, 20), (490, 20), (490, 80), (30, 80)], hexc('#8e5d3e'), hexc('#57361f'), 6, 6)
    p.shape(ell_pts(260, 300, 70, 70, 36), GOLD, GOLD_D, 5, 6)
    p.stroke([(240, 20), (220, -40)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def documento():
    """papel oficial com selo. 460x600"""
    p = Pen(460, 600)
    p.shape([(20, 20), (440, 30), (430, 580), (30, 570)], hexc('#f6f1e4'), hexc('#cfc6b2'), 6, 10)
    for k in range(8):
        y = 150 + k * 44
        p.stroke([(70, y), (390, y + 3)], 9, hexc('#8a8590'))
    p.shape(ell_pts(330, 500, 55, 55, 30), RED, RED_D, 5, 4)
    return fin(p)


def carimbo(c, s, x, y, sc, size=74):
    if sc <= .05: return
    t = txt(s, size, 0)
    im = Image.new('RGBA', (t.size[0] + 80, t.size[1] + 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([8, 8, im.size[0] - 8, im.size[1] - 8], 24, outline=RED, width=14)
    im.alpha_composite(t, (40, 30))
    im = im.rotate(-8, expand=True, resample=Image.BICUBIC)
    paste_c(c, im, x, y, sc)


def fumaca(c, x, y, f, seed=0, s=1.0, col=(150, 150, 160)):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(7):
        t = ((f * .6 + i * 15 + seed * 7) % 100) / 100
        r = (40 + 80 * t) * s
        xx = x + 60 * math.sin(t * 5 + seed + i) * s; yy = y - 300 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=col + (a,))


ARB = hexc('#74acdf'); ARB_D = hexc('#4f86b8'); NAVY = hexc('#8d96a3'); NAVY_D = hexc('#636b77')


@lru_cache(maxsize=2)
def bandeira_ar():
    """bandeira da Argentina (país): azul-claro, branco, azul-claro, sol no meio. 600x400"""
    p = Pen(600, 400)
    for i, cc in enumerate((ARB, WHITE, ARB)):
        p.poly([(10, 10 + i * 127), (590, 10 + i * 127), (590, 10 + (i + 1) * 127), (10, 10 + (i + 1) * 127)], cc)
    for k in range(16):
        a = k * math.pi / 8
        p.stroke([(300 + 30 * math.cos(a), 200 + 30 * math.sin(a)), (300 + 52 * math.cos(a), 200 + 52 * math.sin(a))], 6, GOLD)
    p.shape(ell_pts(300, 200, 30, 30, 30), GOLD, GOLD_D, 4, 3)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def navio_g():
    """navio militar genérico cinza, proa à direita. 800x340"""
    p = Pen(800, 340)
    p.shape([(20, 170), (790, 160), (720, 300), (70, 300)], NAVY, NAVY_D, 6, 10)
    p.shape([(40, 260), (750, 255), (720, 300), (70, 300)], hexc('#3a3d4d'), hexc('#26283a'), 4, 3)
    p.shape([(230, 80), (470, 80), (500, 168), (210, 168)], NAVY, NAVY_D, 5, 6)
    p.shape([(300, 20), (400, 20), (400, 84), (300, 84)], NAVY, NAVY_D, 4, 4)
    for x in (250, 300, 350, 400): p.poly([(x, 105), (x + 30, 105), (x + 30, 125), (x, 125)], hexc('#2a2a33'))
    p.stroke([(350, 20), (350, -10)], 6)
    p.shape([(560, 140), (640, 140), (650, 165), (560, 165)], NAVY_D, mul(NAVY_D, .7), 4, 3)
    p.stroke([(640, 150), (720, 135)], 10, NAVY_D)
    return fin(p)


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


def vela(c, x, y, f, i):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([x - 26, y - 150, x + 26, y], 8, fill=hexc('#f6f1e4'), outline=INK, width=5)
    fl = 1 + .12 * math.sin(f * .5 + i * 1.7)
    d.ellipse([x - 16 * fl, y - 210 * fl + (fl - 1) * 150, x + 16 * fl, y - 156], fill=GOLD, outline=INK, width=4)
    d.ellipse([x - 7, y - 185, x + 7, y - 162], fill=WHITE)


def mar(c, y0, f, col='#3f7fc0'):
    d = ImageDraw.Draw(c)
    d.rectangle([0, y0, BW, BH], fill=hexc(col))
    for r in range(6):
        yy = y0 + 40 + r * 90
        for x in range(-100, BW + 100, 160):
            xx = x + (f * 2 + r * 50) % 160
            d.arc([xx, yy, xx + 120, yy + 40], 200, 340, fill=WHITE, width=5)
    d.line([(0, y0), (BW, y0)], fill=INK, width=6)


def ceu(c, top, bot, y1):
    d = ImageDraw.Draw(c)
    for y in range(0, y1, 8):
        t = y / max(1, y1)
        col = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        d.rectangle([0, y, BW, y + 8], fill=col)


# ------------------------------------------------------------------ cenas
def s0(f):
    """gancho: navio e jato militares argentinos; carimbo TERRORISTAS com a bandeira do Irã."""
    c = Image.new('RGBA', (BW, BH), (0, 0, 0, 255))
    ceu(c, (150, 200, 240), (225, 238, 248), 1300)
    mar(c, 1300, f)
    m0 = wt(0, 'Marinha') - 3
    a0 = wt(0, 'Aerea') - 3
    ar0 = wt(0, 'Argentina') - 3
    t0 = wt(0, 'terroristas') - 3
    put_band(c, bandeira_ir(), 640, 470, 260, f, back(ramp(f, 0, 8)), pole=False)
    num(c, 'IRÃ', 640, 640, f, 2, 90, -3)
    if f >= m0 - 4:
        x = lerp(-300, 470, easeOut(ramp(f, m0 - 4, m0 + 20)))
        paste_c(c, navio_g(), x, 1270 + 8 * math.sin(f * .15), .9)
        put_band(c, bandeira_ar(), x - 40, 1010, 120, f, 1, pole=False)
        num(c, 'MARINHA', x, 1480, f, m0, 80, -2)
    if f >= a0 - 4:
        x = lerp(1500, 840, easeOut(ramp(f, a0 - 4, a0 + 16)))
        jj = jato().transpose(Image.FLIP_LEFT_RIGHT)
        paste_c(c, jj, x, 880 + 10 * math.sin(f * .1), .8)
        num(c, 'FORÇA AÉREA', 860, 1060, f, a0, 70, 3)
    if f >= t0:
        escurece(c, 60 * smooth(ramp(f, t0, t0 + 8)), (120, 20, 20))
        carimbo(c, 'TERRORISTAS?', 640, 850, back(ramp(f, t0, t0 + 8)) * 1.0, 96)
    z = lerp(1.25, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0007 * f)
    k = kick(f, t0, .9)
    return c, (640 + 10 * math.sin(f * .05), 1060 + k * 8, z, k), 'day'


def s1(f):
    """quarta em Teerã: autoridade genérica no púlpito; RECIPROCIDADE."""
    c = CEN('cidade', 'day').copy()
    q0 = wt(1, 'quarta') - 3
    te0 = wt(1, 'Teera') - 3
    r0 = wt(1, 'reciprocidade') - 3
    num(c, 'QUARTA, 11/11', 640, 440, f, q0, 80, -2)
    num(c, 'TEERÃ', 900, 600, f, te0, 100, 4)
    put_band(c, bandeira_ir(), 330, 760, 300, f, back(ramp(f, te0 - 6, te0 + 2)))
    put_p(c, 440, 1560, 640, f, 5, hair='#2a2a30', tie='#2f9a55', suit='#3a3a44', expr='stern', look=1,
          arms='point' if f >= r0 else 'hang')
    paste_c(c, podio(), 440, 1420, .6)
    if f >= r0:
        paste_c(c, documento(), 920, 1060, back(ramp(f, r0 - 6, r0 + 4)) * .7)
        num(c, 'RECIPROCIDADE', 880, 1400, f, r0, 70, -3)
    z = lerp(1.1, 1.0, smooth(ramp(f, 0, 80))) * (1 + .0007 * f)
    k = kick(f, r0, .7)
    return c, (640 + lerp(-10, 30, smooth(ramp(f, 0, 160))), 1060 + k * 6, z, k), 'day'


def s2(f):
    """março, Buenos Aires: governo argentino põe a Guarda Revolucionária na lista de terroristas."""
    c = CEN('cidade', 'golden').copy()
    m0 = wt(2, 'marco') - 3
    mi0 = wt(2, 'Milei') - 3
    g0 = wt(2, 'Guarda') - 3
    l0 = wt(2, 'lista') - 3
    num(c, 'MARÇO DE 2026', 640, 440, f, m0, 80, -2)
    put_band(c, bandeira_ar(), 330, 760, 300, f, back(ramp(f, m0 - 4, m0 + 4)))
    put_p(c, 420, 1560, 640, f, 2, hair='#8a8a90', tie='#74acdf', suit='#2c3550', expr='stern', look=1,
          arms='point' if f >= l0 else 'hang')
    paste_c(c, podio(), 420, 1420, .6)
    num(c, 'ARGENTINA', 420, 620, f, mi0, 70, 3)
    if f >= g0:
        put_band(c, bandeira_ir(), 900, 900, 300, f, back(ramp(f, g0, g0 + 8)), pole=False)
        num(c, 'GUARDA', 900, 1140, f, g0, 76, -3)
        num(c, 'REVOLUCIONÁRIA', 880, 1240, f, g0 + 3, 54, 2)
    if f >= l0:
        carimbo(c, 'LISTA DE TERRORISTAS', 640, 1330, back(ramp(f, l0, l0 + 8)) * .62, 74)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200))) * (1 + .0004 * f)
    k = kick(f, l0, .8)
    return c, (640 + lerp(20, -20, smooth(ramp(f, 0, 200))), 1060 + k * 6, z, k), 'golden'


def s3(f):
    """acusação: Irã -> Hezbollah -> 2 atentados em Buenos Aires (mapa com marcadores)."""
    c = CEN('cidade', 'dusk').copy()
    escurece(c, 80)
    a0 = wt(3, 'acusa') - 3
    h0 = wt(3, 'Hezbollah') - 3
    d0 = wt(3, 'dois') - 3
    b0 = wt(3, 'Buenos') - 3
    put_band(c, bandeira_ir(), 330, 560, 260, f, back(ramp(f, a0 - 4, a0 + 4)), pole=False)
    num(c, 'APOIO?', 640, 470, f, a0 + 6, 70, -3)
    if f >= h0:
        d = ImageDraw.Draw(c)
        t = smooth(ramp(f, h0 - 6, h0 + 6))
        d.line([(470, 600), (lerp(470, 780, t), lerp(600, 740, t))], fill=GOLD, width=10)
        num(c, 'HEZBOLLAH', 900, 760, f, h0, 84, 3)
    if f >= d0:
        num(c, '2 ATENTADOS', 640, 1020, f, d0, 110, -3)
    if f >= b0:
        num(c, 'BUENOS AIRES', 640, 1250, f, b0, 80, 2)
        for i, x in enumerate((470, 810)):
            s = back(ramp(f, b0 + i * 4, b0 + i * 4 + 8))
            if s > .05:
                d = ImageDraw.Draw(c)
                r = 34 * s
                d.ellipse([x - r, 1380 - r, x + r, 1380 + r], fill=RED, outline=INK, width=5)
                d.polygon([(x - r * .7, 1380 + r * .5), (x + r * .7, 1380 + r * .5), (x, 1380 + r * 1.8)], fill=RED, outline=INK)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 70))) * (1 + .0007 * f)
    k = kick(f, d0, .7)
    return c, (640, 1060 + k * 6, z, k), 'dusk'


def s4(f):
    """memória: velas e números das vítimas (sem violência)."""
    c = CEN('cidade', 'dusk').copy()
    escurece(c, 120)
    v0 = wt(4, 'Vinte') - 3
    n0 = wt(4, 'noventa') - 3
    o0 = wt(4, 'oitenta') - 3
    am0 = wt(4, 'AMIA') - 3
    n1 = wt(4, 'noventa', 1) - 3
    for i, x in enumerate(range(160, 1180, 130)):
        vela(c, x, 1520, f, i)
    if f >= v0:
        num(c, '29 MORTOS', 360, 640, f, v0, 64, -3)
        num(c, 'EMBAIXADA', 360, 790, f, v0 + 8, 60, 2)
        num(c, 'DE ISRAEL', 360, 870, f, v0 + 10, 60, -2)
    num(c, '1992', 360, 1020, f, n0, 100, 3)
    if f >= o0:
        num(c, '85 MORTOS', 900, 640, f, o0, 64, 3)
    num(c, 'AMIA', 900, 800, f, am0, 90, -2)
    num(c, '1994', 900, 1020, f, n1, 100, -3)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200))) * (1 + .0004 * f)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 200))), 1060, z, .5 * math.sin(f * .04)), 'dusk'


def s5(f):
    """virada: a tensão do Oriente Médio chega à América do Sul, ao lado do Brasil."""
    c = CEN('mapa', 'dusk').copy()
    escurece(c, 60)
    i0 = wt(5, 'importa') - 3
    g0 = wt(5, 'guerra') - 3
    a0 = wt(5, 'America') - 3
    b0 = wt(5, 'Brasil') - 3
    num(c, 'POR QUE IMPORTA?', 640, 450, f, i0, 90, -3)
    put_band(c, bandeira_ir(), 950, 700, 240, f, back(ramp(f, g0 - 4, g0 + 4)), pole=False)
    num(c, 'ORIENTE MÉDIO', 950, 880, f, g0, 60, 3)
    if f >= g0 + 4:
        d = ImageDraw.Draw(c)
        t = smooth(ramp(f, g0 + 4, a0 + 2))
        for k in range(14):
            u = k / 14
            if u > t: break
            x = lerp(950, 330, u); y = lerp(800, 1180, u) - 260 * math.sin(math.pi * u)
            d.ellipse([x - 12, y - 12, x + 12, y + 12], fill=GOLD, outline=INK, width=3)
    if f >= a0:
        put_band(c, bandeira_ar(), 330, 1180, 240, f, back(ramp(f, a0, a0 + 8)), pole=False)
        num(c, 'AMÉRICA DO SUL', 400, 1360, f, a0 + 2, 60, -2)
    if f >= b0:
        num(c, 'BRASIL AO LADO', 860, 1120, f, b0, 66, 3)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 60))) * (1 + .0008 * f)
    k = kick(f, a0, .8)
    return c, (640, 1060 + k * 8, z, k), 'dusk'


def s6(f):
    """fim: Irã promete consequências, sem dizer quais; nenhuma sanção concreta."""
    c = CEN('cidade', 'dusk').copy()
    co0 = wt(6, 'consequencias') - 3
    q0 = wt(6, 'quais') - 3
    s0_ = wt(6, 'sancao') - 3
    put_band(c, bandeira_ir(), 330, 700, 280, f, 1)
    put_p(c, 440, 1560, 620, f, 5, hair='#2a2a30', tie='#2f9a55', suit='#3a3a44', expr='stern', look=1,
          arms='point' if f >= co0 else 'hang')
    paste_c(c, podio(), 440, 1420, .6)
    if f >= co0:
        num(c, 'CONSEQUÊNCIAS', 880, 560, f, co0, 70, -3)
    if f >= q0:
        num(c, 'QUAIS?', 880, 760, f, q0, 140, 4)
    if f >= s0_:
        paste_c(c, documento(), 900, 1120, back(ramp(f, s0_ - 4, s0_ + 4)) * .6)
        num(c, 'SEM SANÇÃO', 900, 1330, f, s0_, 70, -2)
        num(c, 'POR ENQUANTO', 900, 1430, f, s0_ + 6, 64, 2)
    z = lerp(1.2, 1.0, smooth(ramp(f, 0, 80))) * (1 + .0006 * f)
    k = kick(f, q0, .5)
    return c, (640, 1060 + k * 6, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.whoosh(s.W(0, 'Marinha') - 4, .3, .5)
    s.whoosh(s.W(0, 'Aerea') - 4, .3, .5)
    s.thunk(s.W(0, 'terroristas') - 3, 140, .8)
    s.ting(s.W(1, 'Teera') - 3, .25)
    s.thunk(s.W(1, 'reciprocidade') - 3, 150, .6)
    s.thunk(s.W(2, 'lista') - 3, 140, .7)
    s.ting(s.W(3, 'Hezbollah') - 3, .25)
    s.thunk(s.W(3, 'dois') - 3, 140, .6)
    s.thunk(s.W(5, 'America') - 3, 140, .8)
    s.ting(s.W(6, 'quais') - 3, .25)
