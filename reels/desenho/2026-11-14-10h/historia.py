"""Um Café com o Mundo — NO SEU BOLSO (sábado 14/11/2026, 10h).
Tema: relatório mensal de novembro da Agência Internacional de Energia (AIE/IEA), publicado na sexta 13/11/2026:
o mercado de petróleo volta a ter sobra (excedente) pela 1ª vez desde o início da guerra no Irã (fim de fevereiro).
Fontes (conferidas em 14/11/2026):
- Reuters via BNN Bloomberg, 13/11/2026: excedente no 4º trimestre (oferta de 105 mi bpd, 1,7 mi acima da demanda), "global oil supplies
  surpassing demand for the first time since the outbreak of the war in Iran"; demanda 2026 cai 2,7 mi bpd para 102,3 mi bpd;
  Golfo restaura exportações por Ormuz com "dark crossings" (petroleiros desligam o sinal de rastreamento para evitar ataques);
  Brent ~US$ 95,71.
- The National (Abu Dhabi), 13/11/2026: 1ª vez com oferta acima da demanda desde o início da guerra no fim de fevereiro; demanda -2,7 mi bpd;
  diesel com "severe tightness" e preço recorde, especialmente nos EUA; ataques a navios continuam sendo o principal risco.
Elo com o Brasil só como mecanismo (diesel move o transporte de comida por caminhão); sem previsão de preço. Personagens genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'NO SEU BOLSO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Pela primeira vez desde o começo da guerra no Irã, está sobrando petróleo no mundo.",
    "Quem diz é a Agência Internacional de Energia, no relatório desta sexta.",
    "O preço alto fez o mundo usar dois vírgula sete milhões de barris a menos por dia este ano.",
    "E os petroleiros voltaram a cruzar Ormuz, muitos com o rastreador desligado.",
    "Mas o diesel segue apertado, com preço recorde lá fora. E é ele que leva a comida de caminhão até o seu mercado.",
    "O maior risco, diz a agência, ainda são os ataques a navios.",
]
CAPTXT = [
    "Pela primeira vez desde o começo da guerra|no Irã, está sobrando petróleo no mundo.",
    "Quem diz é a Agência Internacional|de Energia, no relatório desta sexta.",
    "O preço alto fez o mundo usar 2,7 milhões|de barris a menos por dia este ano.",
    "E os petroleiros voltaram a cruzar Ormuz,|muitos com o rastreador desligado.",
    "Mas o diesel segue apertado, com preço|recorde lá fora. E é ele que leva a comida|de caminhão até o seu mercado.",
    "O maior risco, diz a agência,|ainda são os ataques a navios.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'sobrando', 6), (0, 'guerra', 4), (1, 'Agencia', 4), (2, 'dois', 6), (2, 'menos', 4),
         (3, 'Ormuz', 4), (3, 'rastreador', 4), (4, 'diesel', 4), (4, 'recorde', 4), (4, 'caminhao', 4), (5, 'ataques', 4)]

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



def nav(c, x, y, w, col='#c0392b', bob=0.0):
    im = sprite('navio', (('col', col),), int(w * 300 / 700), 700 / 300, False)
    paste_c(c, im, x, y + 6 * math.sin(bob))




@lru_cache(maxsize=2)
def relatorio():
    """relatório com gráfico. 420x540"""
    p = Pen(420, 540)
    p.shape([(20, 20), (400, 20), (400, 520), (20, 520)], WHITE, hexc('#c9c9d2'), 6, 10)
    p.shape([(20, 20), (400, 20), (400, 110), (20, 110)], hexc('#2f6fd6'), hexc('#1f4f9e'), 6, 4)
    for y in (150, 190, 230): p.stroke([(60, y), (360 - (y % 3) * 30, y)], 10, hexc('#b8bfcc'))
    p.stroke([(60, 470), (360, 470)], 6, INK)
    p.stroke([(60, 470), (60, 280)], 6, INK)
    p.stroke([(70, 300), (150, 340), (230, 420), (300, 400), (360, 360)], 10, RED)
    p.dot(100, 70, 22, GOLD, 4)
    return fin(p)


def tanque_sinal(c, x, y, f, on):
    """antena de rastreador: pontinho com ondas (on) ou X (off)."""
    d = ImageDraw.Draw(c)
    d.ellipse([x - 22, y - 22, x + 22, y + 22], fill=GREEN if on else hexc('#8a8f99'), outline=INK, width=5)
    if on:
        rings(c, x, y - 10, f, (f // 24) * 24, 24, .55)
    else:
        d.line([(x - 30, y - 30), (x + 30, y + 30)], fill=RED, width=12)
        d.line([(x + 30, y - 30), (x - 30, y + 30)], fill=RED, width=12)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('deserto', 'golden').copy()
    d0 = wt(0, 'sobrando') - 3
    g0 = wt(0, 'guerra') - 3
    num(c, '1ª VEZ DESDE', 640, 380, f, wt(0, 'primeira') - 3, 90, -3)
    num(c, 'O COMEÇO DA GUERRA', 640, 490, f, g0, 80, 3)
    num(c, 'NO IRÃ', 640, 590, f, wt(0, 'Ira') - 3, 80, -2)
    im = barril().resize((260, 338))
    spots = [(520, 1500), (770, 1500), (1020, 1500), (645, 1170), (895, 1170)]
    for i, (bx, by) in enumerate(spots):
        t0 = d0 - 12 + i * 4
        if f < t0: continue
        yy = lerp(by - 700, by, easeOut(ramp(f, t0, t0 + 10)))
        paste_c(c, im, bx, yy - 169, 1)
        if f >= t0 + 10: put_dust(c, bx, by - 10, 110, f - t0 - 10)
    num(c, 'SOBRANDO', 680, 700, f, d0, 120, -4)
    num(c, 'PETRÓLEO!', 680, 830, f, d0 + 3, 120, 3)
    put_pol(c, 230, 1620, 560, f, 3, skin=1, hair='#3a2a20', tie='#f0c541', suit='#3a3a44',
            expr='shock' if f > d0 else 'neutral', arms='cheek' if f > d0 + 3 else 'hang', look=1)
    z = lerp(1.35, 1.04, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, d0 + 6)
    return c, (640, 1050 + k * 8, z, k), 'golden'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    a0 = wt(1, 'Agencia') - 3
    num(c, 'AGÊNCIA INTERNACIONAL', 640, 360, f, a0, 62, -3)
    num(c, 'DE ENERGIA (AIE)', 640, 450, f, a0 + 4, 66, 3)
    r0 = wt(1, 'relatorio') - 3
    if f >= r0:
        paste_c(c, relatorio().resize((380, 489)), 830, 1050, back(ramp(f, r0, r0 + 8)))
        num(c, 'RELATÓRIO 13/11', 830, 760, f, r0 + 2, 64, -3)
    put_sci(c, 360, 1600, 620, f, 5, skin=2, hair='#2a221e', glasses=True,
            expr='neutral' if f < r0 else 'proud', arms='point' if f > r0 else 'hang', look=1)
    t = smooth(ramp(f, 0, 90))
    return c, (640, lerp(980, 1040, t), lerp(1.18, 1.04, t) * (1 + .0005 * f), .6 * math.sin(f * .04)), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    p0 = wt(2, 'preco') - 3
    num(c, 'PREÇO ALTO', 420, 480, f, p0, 84, -3)
    paste_c(c, bomba().resize((300, 520)), 250, 1300, back(ramp(f, 0, 8)))
    n0 = wt(2, 'dois') - 3
    num(c, '-2,7 MILHÕES', 700, 630, f, n0, 100, -4)
    num(c, 'DE BARRIS POR DIA', 720, 760, f, wt(2, 'barris') - 3, 66, 3)
    num(c, 'EM 2026', 760, 860, f, wt(2, 'ano') - 3, 66, -2)
    seta(c, 800, 1180, 220, up=False, col=RED, s=back(ramp(f, wt(2, 'menos') - 3, wt(2, 'menos') + 5)))
    put_pol(c, 560, 1620, 480, f, 9, skin=0, hair='#8a5a3a', tie='#3aa66a', suit='#4a4f63',
            expr='pained' if f > p0 and f < n0 else ('shock' if f >= n0 else 'neutral'), arms='hang', look=-1)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, n0, .6)
    return c, (640, 1040 + k * 6, z, k), 'day'


def s3(f):
    c = mapa_img().copy()
    num(c, 'IRÃ', 420, 640, f, 0, 110, -3)
    o0 = wt(3, 'Ormuz') - 3
    num(c, 'ESTREITO DE ORMUZ', 640, 1520, f, o0, 70, -3)
    r0 = wt(3, 'rastreador') - 3
    for i, (x0, y0, col) in enumerate(((150, 1060, '#c0392b'), (-250, 1200, '#2f5d8a'))):
        x = x0 + 3.2 * f
        nav(c, x, y0, 470, col, f * .2 + i)
        tanque_sinal(c, x - 110, y0 - 150, f, f < r0 + i * 6)
    num(c, 'RASTREADOR', 640, 380, f, r0, 90, 3)
    num(c, 'DESLIGADO', 640, 490, f, wt(3, 'desligado') - 3, 100, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140))) + .0007 * f
    return c, (660 + 12 * math.sin(f * .035), lerp(1000, 1040, smooth(ramp(f, 0, 140))), z, .6 * math.sin(f * .03)), 'dusk'


def s4(f):
    c = CEN('cidade', 'golden').copy()
    d0 = wt(4, 'diesel') - 3
    paste_c(c, bomba().resize((300, 520)), 260, 1250, back(ramp(f, d0, d0 + 8)) if f >= d0 else .01)
    num(c, 'DIESEL', 320, 900, f, d0, 90, -3)
    rc0 = wt(4, 'recorde') - 3
    num(c, 'PREÇO RECORDE', 700, 420, f, rc0, 84, -3)
    seta(c, 620, 820, 200, up=True, col=RED, s=back(ramp(f, rc0, rc0 + 8)))
    k0 = wt(4, 'caminhao') - 3
    if f >= k0 - 20:
        x = lerp(-300, 720, easeOut(ramp(f, k0 - 20, k0 + 50)))
        put_sprite(c, 'truck', x, 1600, 380, 900 / 520, False, {'wheel_rot': 8}, wheel_rot=(f * .3) % 6.28)
        num(c, 'COMIDA', x - 80, 1290, f, wt(4, 'comida') - 3, 64, 0)
    num(c, 'ATÉ O SEU MERCADO', 680, 640, f, wt(4, 'mercado') - 3, 76, 3)
    put_pol(c, 1020, 1620, 460, f, 11, skin=1, hair='#2a221e', tie='#2f6fd6', suit='#6b4a6b',
            expr='nervous' if f > rc0 else 'neutral', arms='point' if f > rc0 else 'hang', look=-1)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, rc0, .6)
    return c, (620 + 20 * math.sin(f * .02), 1040 + k * 6, z, k), 'golden'


def s5(f):
    c = mar_bg()
    a0 = wt(5, 'ataques') - 3
    num(c, 'MAIOR RISCO:', 640, 420, f, wt(5, 'risco') - 3, 90, -3)
    num(c, 'ATAQUES A NAVIOS', 640, 540, f, a0, 80, 3)
    nav(c, lerp(200, 900, ramp(f, 0, 300)), 1180, 520, '#c0392b', f * .2)
    if f >= a0: fumaca(c, 980, 1080, f - a0, 2, 1.1)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 140))) + .0003 * f
    return c, (640 + 12 * math.sin(f * .035), 1000, z, lerp(-1.5, 1, smooth(ramp(f, 0, 140)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    s.thunk(s.W(0, 'sobrando') - 3, 140, 1.0)
    s.ting(s.W(1, 'Agencia') - 3, .25)
    s.thunk(s.W(2, 'dois') - 3, 150, .7)
    s.whoosh(s.W(3, 'Ormuz') - 3, .3, .5)
    s.ting(s.W(4, 'recorde') - 3, .3)
    s.engine(s.W(4, 'caminhao') - 20, s.W(4, 'caminhao') + 40, .2)
    s.thunk(s.W(5, 'ataques') - 3, 120, .5)
