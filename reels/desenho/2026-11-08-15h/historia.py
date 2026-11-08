"""Um Café com o Mundo — NO SEU BOLSO (domingo 08/11/2026, 15h).
Tema: petróleo Brent tem a maior queda semanal desde 2020 (semana até sexta 06/11/2026) e por que isso não chega igual à bomba no Brasil.
Fontes (conferidas em 08/11/2026):
- FinanceFeeds, 07/11/2026 (com dados CNBC / Business Recorder / Reuters): Brent fechou sexta 06/11 a US$ 98,32; caiu mais de 16%
  na semana, a maior queda semanal desde 2020; fechamento da sexta anterior US$ 117,64; Democratas venceram as duas casas do
  Congresso em 03/11 e o mercado passou a ver mais pressão por fim da guerra/acordo EUA-Irã; Irã mandou proposta via Catar, sem
  acordo formal; ataques a petroleiros continuam em Ormuz; reunião ministerial da Opep+ em 29/11.
- Demócrata (Espanha), 07/11/2026: Brent de US$ 117,64 (30/10) para ~US$ 97, queda de ~17% em 5 pregões.
- O Povo / Agência Estado (Broadcast), 08/11/2026: setor diz que sem a ação do governo os combustíveis custariam ~o dobro;
  Petrobras vende abaixo do preço internacional; PIS/Cofins e Cide da gasolina zerados; subsídios ao diesel; Abicom espera
  retirada gradual dos subsídios.
Elo com o Brasil só com o que as fontes dizem; sem previsão de preço. Personagens genéricos, sem logotipos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'NO SEU BOLSO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O petróleo despencou dezesseis por cento em uma semana, a maior queda desde dois mil e vinte.",
    "O barril do tipo Brent fechou a sexta-feira a noventa e oito dólares. Uma semana antes, custava cento e dezessete.",
    "O motivo: depois da eleição americana, o mercado passou a apostar mais num acordo para encerrar a guerra com o Irã.",
    "Mas nada foi assinado ainda, e os petroleiros continuam sofrendo ataques no estreito de Ormuz.",
    "E no Brasil? A Petrobras já vende abaixo do preço lá de fora, a gasolina está sem impostos federais, e o diesel tem subsídio.",
    "Segundo o setor, sem essas medidas, o combustível poderia custar quase o dobro na bomba.",
    "Agora, o mercado olha para a negociação com o Irã e para a reunião da Opep, no fim do mês.",
]
CAPTXT = [
    "O petróleo despencou 16% em uma semana,|a maior queda desde 2020.",
    "O barril do tipo Brent fechou a sexta-feira|a US$ 98. Uma semana antes,|custava US$ 117.",
    "O motivo: depois da eleição americana,|o mercado passou a apostar mais num acordo|para encerrar a guerra com o Irã.",
    "Mas nada foi assinado ainda,|e os petroleiros continuam sofrendo ataques|no estreito de Ormuz.",
    "E no Brasil? A Petrobras já vende abaixo|do preço lá de fora, a gasolina está sem impostos|federais, e o diesel tem subsídio.",
    "Segundo o setor, sem essas medidas,|o combustível poderia custar|quase o dobro na bomba.",
    "Agora, o mercado olha para a negociação|com o Irã e para a reunião da Opep,|no fim do mês.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'dezesseis', 6), (0, 'dois', 6), (1, 'noventa', 6), (1, 'cento', 6), (2, 'eleicao', 4), (2, 'acordo', 4),
         (2, 'Ira', 4), (3, 'assinado', 4), (3, 'Ormuz', 4), (4, 'Brasil', 4), (4, 'abaixo', 4), (4, 'impostos', 4),
         (4, 'subsidio', 4), (5, 'dobro', 6), (6, 'Ira', 4), (6, 'Opep', 4)]

SEA = hexc('#3d7fb8'); SEA_D = hexc('#2c6396'); SAND = hexc('#e2c48e'); SAND_D = hexc('#b89a64')
GREEN = hexc('#3aa66a'); GREEN_D = hexc('#287a4c'); RED = hexc('#d8443c'); RED_D = hexc('#a02c26')
BLUE = hexc('#2f6fd6'); GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e'); WHITE = (255, 255, 255)
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0')


# ------------------------------------------------------------------ desenhos
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


@lru_cache(maxsize=2)
def barril():
    p = Pen(200, 260)
    p.shape([(30, 30), (170, 30), (178, 130), (170, 230), (30, 230), (22, 130)], hexc('#2f3a4a'), hexc('#1e2633'), 5, 10)
    p.shape(ell_pts(100, 32, 70, 18, 24), hexc('#46566b'), hexc('#2f3a4a'), 4, 3)
    for y in (90, 170): p.stroke([(24, y), (176, y)], 6, hexc('#5c6d84'))
    p.poly([(60, 115), (140, 115), (140, 145), (60, 145)], GOLD, 3)
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


def fumaca(c, x, y, f, seed=0, s=1.0):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(6):
        t = ((f * .6 + i * 17 + seed * 7) % 100) / 100
        r = (30 + 60 * t) * s
        xx = x + 40 * math.sin(t * 5 + seed) * s; yy = y - 260 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=(110, 110, 120, a))


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


def aviso(c, s, x, y, f, f0, size=90, rot=-4):
    if f < f0: return
    sc = back(ramp(f, f0, f0 + 8))
    paste_c(c, txt(s, size, rot), x, y, sc)


@lru_cache(maxsize=2)
def carteira():
    p = Pen(360, 260)
    p.shape([(20, 40), (340, 40), (340, 250), (20, 250)], hexc('#8a5a3a'), hexc('#6a4228'), 6, 12)
    p.shape([(200, 110), (350, 110), (350, 190), (200, 190)], hexc('#9b6a46'), hexc('#6a4228'), 5, 6)
    p.dot(240, 150, 14, GOLD, 4)
    return fin(p)


@lru_cache(maxsize=2)
def calendario():
    p = Pen(500, 520)
    p.shape([(20, 60), (480, 60), (480, 500), (20, 500)], WHITE, hexc('#c9c9d2'), 6, 10)
    p.shape([(20, 60), (480, 60), (480, 160), (20, 160)], RED, RED_D, 6, 6)
    for x in (120, 380): p.shape([(x - 14, 20), (x + 14, 20), (x + 14, 100), (x - 14, 100)], hexc('#6b6b70'), hexc('#4a4a50'), 4, 3)
    for r in range(4):
        for k in range(5):
            x, y = 70 + k * 90, 210 + r * 75
            p.poly([(x, y), (x + 50, y), (x + 50, y + 40), (x, y + 40)], hexc('#e6e9ef'), 3)
    return fin(p)


def seta(c, x, y, size, up=True, col=None, s=1.0):
    if s <= .02: return
    col = col or (GREEN if up else RED)
    d = ImageDraw.Draw(c)
    k = 1 if up else -1
    w = size * .32 * s; hh = size * s
    pts = [(x - w, y + k * hh * .1), (x - w, y - k * hh * .25), (x - w * 2, y - k * hh * .25), (x, y - k * hh * .8), (x + w * 2, y - k * hh * .25), (x + w, y - k * hh * .25), (x + w, y + k * hh * .1)]
    d.polygon([(px + 6, py + 6) for px, py in pts], fill=INK)
    d.polygon(pts, fill=col, outline=INK, width=6)


def barra(c, x, base, w, h, col, lab, f, f0, top_lab=None):
    if f < f0: return
    d = ImageDraw.Draw(c)
    hh = h * easeOut(ramp(f, f0, f0 + 14))
    d.rectangle([x - w / 2 + 8, base - hh + 8, x + w / 2 + 8, base + 8], fill=INK)
    d.rectangle([x - w / 2, base - hh, x + w / 2, base], fill=col, outline=INK, width=6)
    if top_lab: paste_c(c, txt(top_lab, 90, -3), x, base - hh - 70, back(ramp(f, f0 + 6, f0 + 14)))


# ------------------------------------------------------------------ cenas
def barris(c, x, y, f, f0, n=3, w=200):
    for i in range(n):
        s = back(ramp(f, f0 + i * 3, f0 + i * 3 + 8))
        if s > .02:
            im = barril().resize((int(w * s), int(w * 1.3 * s)))
            paste_c(c, im, x + (i - (n - 1) / 2) * w * .95, y, 1)


def s0(f):
    c = CEN('deserto', 'golden').copy()
    d0 = wt(0, 'dezesseis') - 3
    # barril grande que "despenca"
    yb = lerp(700, 1250, easeOut(ramp(f, d0 - 10, d0 + 6)))
    im = barril().resize((420, 546))
    paste_c(c, im.rotate(-8 * ramp(f, d0 - 10, d0 + 6), expand=True, resample=Image.BICUBIC), 620, yb, 1)
    if f >= d0 + 6: put_dust(c, 620, 1520, 160, f - d0 - 6)
    num(c, '-16%', 480, 470, f, d0, 220, -5)
    seta(c, 1020, 900, 280, up=False, col=RED, s=back(ramp(f, d0 + 2, d0 + 10)))
    num(c, 'EM 1 SEMANA', 560, 660, f, wt(0, 'semana') - 3, 90, 3)
    num(c, 'MAIOR QUEDA', 640, 800, f, wt(0, 'maior') - 3, 80, -2)
    num(c, 'DESDE 2020', 640, 910, f, wt(0, 'dois') - 3, 80, 2)
    put_pol(c, 220, 1600, 520, f, 3, skin=1, hair='#3a2a20', tie='#f0c541', suit='#3a3a44',
            expr='shock' if f > d0 else 'neutral', arms='cheek' if f > d0 + 3 else 'hang', look=1)
    z = lerp(1.4, 1.06, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, d0 + 6)
    return c, (640, 1050 + k * 8, z, k), 'golden'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    num(c, 'BARRIL TIPO BRENT', 640, 400, f, 0, 86, -3)
    n0 = wt(1, 'noventa') - 3
    c0 = wt(1, 'cento') - 3
    barra(c, 880, 1300, 220, 420, RED, '', f, n0, 'US$ 98')
    barra(c, 380, 1300, 220, 520, hexc('#9aa4b4'), '', f, c0, 'US$ 117')
    num(c, 'SEXTA, 6/11', 880, 1370, f, n0 + 4, 50, 0)
    num(c, 'SEMANA ANTES', 380, 1370, f, c0 + 4, 50, 0)
    if f >= c0 + 10:
        seta(c, 640, 640, 170, up=False, col=RED, s=back(ramp(f, c0 + 10, c0 + 18)))
    paste_c(c, barril().resize((150, 195)), 640, 1200, back(ramp(f, 2, 10)))
    t = smooth(ramp(f, 0, 110))
    k = kick(f, n0, .7)
    return c, (640, lerp(950, 1020, t) + k * 8, lerp(1.2, 1.04, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    e0 = wt(2, 'eleicao') - 3
    num(c, 'ELEIÇÃO NOS EUA', 640, 420, f, e0, 90, -3)
    a0 = wt(2, 'acordo') - 3
    # dois negociadores genéricos se aproximam
    t = smooth(ramp(f, a0 - 12, a0 + 10))
    put_pol(c, lerp(260, 420, t), 1580, 600, f, 4, skin=0, hair='#6b5a4a', tie='#2f6fd6', suit='#2c3550',
            expr='neutral', arms='point' if f > a0 else 'hang', look=1)
    put_pol(c, lerp(1000, 840, t), 1580, 600, f, 8, skin=2, hair='#2a221e', tie='#3aa66a', suit='#4a4f63',
            expr='neutral', arms='point' if f > a0 else 'hang', look=-1)
    num(c, 'ACORDO?', 640, 640, f, a0, 150, 4)
    num(c, 'EUA', 360, 860, f, wt(2, 'guerra') - 3, 90, -3)
    num(c, 'IRÃ', 920, 860, f, wt(2, 'Ira') - 3, 90, 3)
    z = lerp(1.12, 1.02, smooth(ramp(f, 0, 90))) * (1 + .0006 * f)
    return c, (640 + 20 * math.sin(f * .03), 1060, z, .6 * math.sin(f * .04)), 'day'


def s3(f):
    c = mapa_img().copy()
    num(c, 'IRÃ', 420, 640, f, 0, 110, -3)
    o0 = wt(3, 'Ormuz') - 3
    a0 = wt(3, 'assinado') - 3
    num(c, 'NADA ASSINADO', 640, 400, f, a0, 100, 3)
    carg(c, lerp(300, 900, ramp(f, 0, 150)), 1110, 300, f * .2)
    at0 = wt(3, 'ataques') - 3
    if f >= at0: fumaca(c, 860, 1180, f - at0, 2, .9)
    num(c, 'ESTREITO DE ORMUZ', 700, 1560 - 160, f, o0, 70, -3)
    z = lerp(1.0, 1.14, smooth(ramp(f, 0, 140)))
    return c, (700, lerp(980, 1060, smooth(ramp(f, 0, 140))), z, lerp(-1.5, 1, smooth(ramp(f, 0, 140)))), 'dusk'


def s4(f):
    c = CEN('cidade', 'day').copy()
    b0 = wt(4, 'Brasil') - 3
    num(c, 'E NO BRASIL?', 640, 380, f, b0, 120, -3)
    paste_c(c, bomba().resize((330, 572)), 360, 1300, back(ramp(f, b0, b0 + 8)) if f >= b0 else .01)
    ab0 = wt(4, 'abaixo') - 3
    num(c, 'ABAIXO DO PREÇO', 760, 580, f, ab0, 62, 3)
    num(c, 'LÁ DE FORA', 760, 670, f, ab0 + 3, 62, 3)
    z0 = wt(4, 'impostos') - 3
    num(c, 'SEM IMPOSTO', 760, 810, f, z0, 66, -3)
    num(c, 'FEDERAL', 760, 900, f, z0 + 3, 62, -3)
    s0_ = wt(4, 'subsidio') - 3
    num(c, '+ SUBSÍDIO', 760, 1040, f, s0_, 74, 3)
    put_pol(c, 900, 1600, 520, f, 9, skin=1, hair='#8a5a3a', tie='#d8443c', suit='#6b4a6b',
            expr='grin' if f > ab0 else 'neutral', arms='point' if f > ab0 else 'hang', look=-1)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, b0, .6)
    return c, (620, 1040 + k * 6, z, k), 'day'


def s5(f):
    c = CEN('cidade', 'golden').copy()
    d0 = wt(5, 'dobro') - 3
    sc = 1 + .5 * easeOut(ramp(f, d0 - 4, d0 + 10))
    paste_c(c, bomba().resize((int(300 * sc), int(520 * sc))), 400, 1280 - 120 * (sc - 1), 1)
    num(c, 'QUASE O DOBRO', 640, 420, f, d0, 96, -4)
    num(c, 'x2', 920, 700, f, d0 + 2, 200, 5)
    num(c, 'SEM AS MEDIDAS', 640, 560, f, wt(5, 'medidas') - 3, 76, 3)
    put_pol(c, 930, 1600, 540, f, 11, skin=2, hair='#2a221e', tie='#2f6fd6', suit='#3a3a44',
            expr='shock' if f > d0 else 'nervous', arms='cheek' if f > d0 else 'hang', look=-1)
    t = smooth(ramp(f, 0, 110))
    k = kick(f, d0 + 2, .8)
    return c, (640 + 15 * math.sin(f * .04), lerp(1000, 1060, t) + k * 6, lerp(1.0, 1.12, t) * (1 + .0008 * f), lerp(0, 1.5, t) + k), 'golden'


def s6(f):
    c = CEN('escritorio', 'dusk').copy()
    paste_c(c, calendario(), 470, 1040, back(ramp(f, 0, 8)))
    num(c, 'NEGOCIAÇÃO', 640, 420, f, wt(6, 'negociacao') - 3, 80, -3)
    num(c, 'COM O IRÃ', 640, 520, f, wt(6, 'Ira') - 3, 80, 3)
    num(c, 'OPEP: 29/11', 470, 700, f, wt(6, 'Opep') - 3, 90, -3)
    put_pol(c, 980, 1640, 640, f, 7, skin=0, hair='#3a2a20', tie='#f0c541', suit='#2c3550', expr='neutral', arms='point', look=-1)
    z = lerp(1.0, 1.07, smooth(ramp(f, 0, 70))) + .0004 * f
    return c, (640, 1050, z, lerp(0, 1.5, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'dezesseis') - 3, 140, 1.0)
    s.ting(s.W(0, 'dois') - 3, .25)
    s.thunk(s.W(1, 'noventa') - 3, 200, .7)
    s.thunk(s.W(1, 'cento') - 3, 150, .7)
    s.whoosh(s.W(2, 'acordo') - 3, .3, .5)
    s.thunk(s.W(3, 'ataques') - 3, 120, .5)
    s.ting(s.W(4, 'Brasil') - 3, .3)
    s.thunk(s.W(4, 'impostos') - 3, 220, .5)
    s.thunk(s.W(5, 'dobro') - 3, 140, .9)
    s.ting(s.W(6, 'Opep') - 3, .3)
