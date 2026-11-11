"""Um Café com o Mundo — NO SEU BOLSO (quarta 11/11/2026, 10h).
Tema: inflação dos EUA de outubro acima do esperado (divulgada terça 10/11/2026) leva o dólar ao maior valor em 15 meses no Brasil.
Fontes (conferidas em 11/11/2026):
- Fox Business, 10/11/2026 "October CPI": CPI +0,4% no mês (esperado 0,3%, LSEG); núcleo +0,3% (esperado 0,2%); alimentos +0,5%,
  maior alta mensal desde abril; carne bovina +0,9%; FOMC em 8-9/12; CME FedWatch: 87,3% de chance de alta de 0,25 ponto
  (faixa 4%-4,25%) e 12,7% de 0,5 ponto. Sem dado anual oficial (efeito do shutdown de 2025).
- CaixaBank Research, 11/11/2026: CPI acima do esperado; mercado precifica totalmente alta do Fed em dezembro; dólar global +0,6%.
- InfoMoney, 10/11/2026: dólar à vista fecha a R$ 5,5863 (+1,46%), maior valor em 15 meses; também pesou a ata do Copom.
Elo com o Brasil: o próprio fechamento do dólar (InfoMoney) + o mecanismo geral, sem previsão.
Personagens genéricos (sem traços de pessoas reais)."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'NO SEU BOLSO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O dólar bateu o maior valor em quinze meses, por causa dos preços nos Estados Unidos.",
    "Fechou a cinco reais e cinquenta e nove, quase um e meio por cento a mais num dia.",
    "A inflação americana subiu zero vírgula quatro por cento em outubro, acima do esperado, e a comida subiu ainda mais.",
    "Agora, o mercado vê oitenta e sete por cento de chance de juros mais altos por lá em dezembro.",
    "Por que importa? Juros altos lá atraem dinheiro do mundo todo, e o dólar caro encarece importados e viagens.",
    "A decisão sai nos dias oito e nove de dezembro.",
]
CAPTXT = [
    "O dólar bateu o maior valor em 15 meses,|por causa dos preços nos Estados Unidos.",
    "Fechou a R$ 5,59,|quase 1,5% a mais num dia.",
    "A inflação americana subiu 0,4% em outubro,|acima do esperado,|e a comida subiu ainda mais.",
    "Agora, o mercado vê 87% de chance|de juros mais altos por lá em dezembro.",
    "Por que importa? Juros altos lá|atraem dinheiro do mundo todo,|e o dólar caro encarece importados e viagens.",
    "A decisão sai nos dias 8 e 9 de dezembro.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'quinze', 6), (0, 'Estados', 6), (1, 'cinco', 8), (1, 'meio', 6), (2, 'zero', 6), (2, 'comida', 6),
         (3, 'oitenta', 6), (3, 'juros', 6), (4, 'dinheiro', 8), (4, 'viagens', 6), (5, 'oito', 6)]

GREEN = hexc('#3aa66a'); GREEN_D = hexc('#287a4c'); RED = hexc('#d8443c'); RED_D = hexc('#a02c26')
BLUE = hexc('#2f6fd6'); BLUE_D = hexc('#1f4f9e'); GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e')
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); WHITE = (255, 255, 255)


# ------------------------------------------------------------------ desenhos novos
def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def politico(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550'):
    """pessoa genérica de terno. 600x1000, pés y~975."""
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


@lru_cache(maxsize=2)
def nota(col='#5aa66a'):
    """cédula genérica. 300x150"""
    p = Pen(300, 150)
    h = hexc(col)
    p.shape([(8, 8), (292, 8), (292, 142), (8, 142)], h, mul(h, .75), 5, 6)
    p.arc(150, 75, 40, 40, 0, 360, 4, mul(h, .6))
    p.poly([(30, 30), (60, 30), (60, 50), (30, 50)], mul(h, .7))
    p.poly([(240, 100), (270, 100), (270, 120), (240, 120)], mul(h, .7))
    return fin(p)


@lru_cache(maxsize=2)
def carteira():
    p = Pen(360, 260)
    p.shape([(20, 40), (340, 40), (340, 250), (20, 250)], hexc('#8a5a3a'), hexc('#6a4228'), 6, 12)
    p.shape([(200, 110), (350, 110), (350, 190), (200, 190)], hexc('#9b6a46'), hexc('#6a4228'), 5, 6)
    p.dot(240, 150, 14, GOLD, 4)
    return fin(p)


@lru_cache(maxsize=2)
def banco():
    """prédio genérico de banco central (colunas, sem marca). 1000x760, base y~750."""
    p = Pen(1000, 760)
    for i in range(4):
        y = 750 - i * 16
        p.shape([(80 + i * 20, y - 16), (920 - i * 20, y - 16), (920 - i * 20, y), (80 + i * 20, y)], STONE, STONE_D, 4, 3)
    p.shape([(100, 330), (900, 330), (900, 690), (100, 690)], STONE, STONE_D, 6, 14)
    for x in range(150, 880, 100):
        p.shape([(x - 22, 360), (x + 22, 360), (x + 22, 684), (x - 22, 684)], hexc('#fbf8f2'), STONE_D, 4, 6)
    p.shape([(70, 300), (930, 300), (930, 340), (70, 340)], STONE, STONE_D, 5, 4)
    p.shape([(90, 300), (500, 120), (910, 300)], STONE, STONE_D, 6, 10)
    p.dot(500, 230, 40, GOLD, 5)
    return fin(p)


@lru_cache(maxsize=4)
def termometro(lvl=0):
    """termômetro de 0 a 8 níveis. 200x700"""
    p = Pen(200, 700)
    p.shape([(70, 40), (130, 40), (130, 560), (70, 560)], WHITE, hexc('#c9c9d2'), 6, 6)
    p.shape(ell_pts(100, 600, 70, 70, 36), RED, RED_D, 6, 6)
    top = 560 - 500 * lvl / 8
    if lvl > 0: p.poly([(84, top), (116, top), (116, 570), (84, 570)], RED)
    for y in range(80, 560, 60): p.stroke([(130, y), (150, y)], 4)
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


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def nota_voando(c, x0, y0, x1, y1, t, w=170, col='#5aa66a', rot=0):
    if t <= 0 or t >= 1: return
    im = nota(col).resize((w, int(w / 2)))
    im = im.rotate(rot + 30 * math.sin(t * 6), expand=True, resample=Image.BICUBIC)
    paste_c(c, im, lerp(x0, x1, t), lerp(y0, y1, t) - 220 * math.sin(t * math.pi), 1)


def barra(c, x, base, w, h, col, lab, f, f0, top_lab=None):
    if f < f0: return
    d = ImageDraw.Draw(c)
    hh = h * easeOut(ramp(f, f0, f0 + 14))
    d.rectangle([x - w / 2 + 8, base - hh + 8, x + w / 2 + 8, base + 8], fill=INK)
    d.rectangle([x - w / 2, base - hh, x + w / 2, base], fill=col, outline=INK, width=6)
    if top_lab: paste_c(c, txt(top_lab, 90, -3), x, base - hh - 70, back(ramp(f, f0 + 6, f0 + 14)))


# ------------------------------------------------------------------ desenhos novos (11/11)
@lru_cache(maxsize=2)
def mala():
    """mala de viagem. 300x320"""
    p = Pen(300, 320)
    p.shape([(110, 20), (190, 20), (190, 70), (170, 70), (170, 40), (130, 40), (130, 70), (110, 70)], hexc('#4a4a50'), hexc('#2e2e33'), 5, 3)
    p.shape([(30, 70), (270, 70), (270, 300), (30, 300)], hexc('#2f6fd6'), hexc('#1f4f9e'), 6, 14)
    for x in (100, 200): p.stroke([(x, 80), (x, 290)], 5)
    return fin(p)


@lru_cache(maxsize=2)
def caixa():
    """caixa de produto importado. 320x280"""
    p = Pen(320, 280)
    p.shape([(30, 60), (290, 60), (290, 270), (30, 270)], hexc('#c8935a'), hexc('#9a6a3a'), 6, 10)
    p.shape([(30, 60), (290, 60), (260, 20), (60, 20)], hexc('#dcae78'), hexc('#9a6a3a'), 5, 4)
    p.poly([(140, 60), (180, 60), (180, 140), (140, 140)], hexc('#e8c79c'))
    return fin(p)


@lru_cache(maxsize=2)
def carrinho():
    """carrinho de mercado com comida. 520x460"""
    p = Pen(520, 460)
    p.dot(130, 72, 46, hexc('#d8443c'), 5)   # maçã/tomate
    p.shape(ell_pts(250, 80, 70, 52, 30), hexc('#f0c541'), hexc('#b8901e'), 5, 5)   # pão
    p.shape([(320, 40), (420, 30), (430, 110), (330, 120)], hexc('#d8708a'), hexc('#a84a62'), 5, 5)   # carne
    p.shape([(40, 100), (480, 100), (430, 330), (100, 330)], hexc('#c9d2de'), hexc('#8a96a8'), 6, 8)
    for x in range(120, 440, 60): p.stroke([(x, 110), (x - 8 if x < 260 else x + 8, 320)], 4)
    p.stroke([(40, 100), (0, 40)], 8)
    p.stroke([(100, 330), (110, 380), (430, 380)], 6)
    for x in (150, 400): p.dot(x, 410, 34, hexc('#4a4a50'), 5)
    return fin(p)


def grafico(c, x0, y0, w, h, f, f0, dur=40):
    """linha de dólar subindo, desenhada aos poucos."""
    if f < f0: return
    d = ImageDraw.Draw(c)
    d.rectangle([x0 - 20, y0 - h - 20, x0 + w + 20, y0 + 20], fill=(255, 255, 255), outline=INK, width=6)
    pts = []
    vals = [.30, .25, .35, .30, .42, .38, .50, .46, .60, .95]
    t = easeOut(ramp(f, f0, f0 + dur))
    n = max(2, int(2 + t * (len(vals) - 2)))
    for i, v in enumerate(vals[:n]):
        pts.append((x0 + w * i / (len(vals) - 1), y0 - h * v))
    d.line([(px + 5, py + 5) for px, py in pts], fill=INK, width=16)
    d.line(pts, fill=GREEN, width=12)
    px, py = pts[-1]
    d.ellipse([px - 16, py - 16, px + 16, py + 16], fill=GREEN, outline=INK, width=5)


def s0(f):
    c = CEN('cidade', 'day').copy()
    q0 = wt(0, 'quinze') - 3
    e0 = wt(0, 'Estados') - 3
    s = back(ramp(f, 0, 10))
    im = nota('#5aa66a').resize((int(520 * max(s, .05)), int(260 * max(s, .05))))
    im = im.rotate(-8 + 3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    paste_c(c, im, 640, 820 - 30 * math.sin(f * .1), 1)
    num(c, 'US$', 640, 820, f, 2, 150, -8)
    seta(c, 1000, 760, 260, up=True, col=GREEN, s=back(ramp(f, 4, 14)))
    num(c, 'MAIOR VALOR', 600, 470, f, wt(0, 'maior') - 3, 100, -3)
    num(c, 'EM 15 MESES', 600, 600, f, q0, 110, 3)
    num(c, 'EUA', 650, 1130, f, e0, 120, -4)
    put_pol(c, 330, 1560, 520, f, 2, skin=0, hair='#3a2a20', tie='#2f6fd6', suit='#2c3550',
            expr='shock' if f > q0 else 'neutral', arms='up' if f > q0 + 3 else 'hang', look=1)
    put_pol(c, 960, 1580, 520, f, 3, skin=2, hair='#2a221e', tie='#f0c541', suit='#4a4f63',
            expr='nervous' if f > e0 else 'shock', arms='cheek', look=-1)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, q0)
    return c, (640, 1080 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    num(c, 'TERÇA, 10/11', 640, 380, f, 0, 90, -3)
    c0 = wt(1, 'cinco') - 3
    grafico(c, 230, 1200, 780, 520, f, 0, max(20, c0))
    num(c, 'R$ 5,59', 520, 560, f, c0, 170, -4)
    m0 = wt(1, 'meio') - 3
    num(c, '+1,46%', 860, 800, f, m0, 130, 4)
    seta(c, 1060, 640, 200, up=True, col=GREEN, s=back(ramp(f, m0 + 2, m0 + 10)))
    put_pol(c, 1000, 1640, 560, f, 4, skin=1, hair='#6b4a2a', tie='#d8443c', suit='#3a3a44',
            expr='shock' if f > c0 else 'neutral', arms='point', look=-1)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, c0, .8)
    return c, (640, lerp(960, 1020, t) + k * 8, lerp(1.18, 1.04, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = CEN('cozinha', 'golden').copy()
    z0 = wt(2, 'zero') - 3
    lvl = int(round(6 * easeOut(ramp(f, z0 - 6, z0 + 12))))
    paste_c(c, termometro(lvl).resize((170, 595)), 280, 980, 1)
    num(c, 'INFLAÇÃO NOS EUA', 640, 380, f, wt(2, 'inflacao') - 3, 86, -3)
    num(c, '+0,4%', 560, 640, f, z0, 170, 3)
    num(c, 'EM OUTUBRO', 560, 790, f, wt(2, 'outubro') - 3, 80, -3)
    num(c, 'ESPERADO: 0,3%', 600, 920, f, wt(2, 'esperado') - 3, 70, 2)
    k0 = wt(2, 'comida') - 3
    if f >= k0 - 2:
        paste_c(c, carrinho().resize((416, 368)), 870 + 40 * (1 - easeOut(ramp(f, k0 - 2, k0 + 10))), 1300, back(ramp(f, k0 - 2, k0 + 8)))
    num(c, 'COMIDA: +0,5%', 680, 1060, f, k0, 90, -3)
    num(c, 'MAIOR ALTA DESDE ABRIL', 640, 1180, f, k0 + 12, 62, 2)
    t = smooth(ramp(f, 0, 150))
    k = kick(f, z0, .6)
    return c, (640 + 15 * math.sin(f * .03), lerp(1000, 1040, t) + k * 6, lerp(1.04, 1.08, t) * (1 + .0004 * f), lerp(0, 1.5, t) + k), 'golden'


def s3(f):
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, banco().resize((820, 624)), 640, 1110, 1)
    num(c, 'BANCO CENTRAL DOS EUA', 640, 1480, f, wt(3, 'mercado') - 3, 66, 0)
    s0_ = wt(3, 'oitenta') - 3
    num(c, '87%', 380, 560, f, s0_, 170, -4)
    num(c, 'DE CHANCE', 380, 700, f, s0_ + 4, 80, 3)
    j0 = wt(3, 'juros') - 3
    num(c, 'JUROS', 930, 500, f, j0, 110, 4)
    seta(c, 930, 740, 220, up=True, col=RED, s=back(ramp(f, j0 + 2, j0 + 10)))
    num(c, 'DEZEMBRO', 930, 860, f, wt(3, 'dezembro') - 3, 76, -3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, j0, .8)
    return c, (640, 1060 + k * 8, z, k), 'dusk'


def s4(f):
    c = CEN('mapa', 'dusk').copy()
    num(c, 'EUA', 330, 560, f, 0, 130, -4)
    num(c, 'BRASIL', 820, 1180, f, wt(4, 'importa'), 110, 3)
    num(c, 'JUROS MAIS ALTOS', 560, 430, f, wt(4, 'juros') - 3, 80, -3)
    d0 = wt(4, 'dinheiro') - 3
    v0 = wt(4, 'encarece') - 3
    for i in range(10):
        st = d0 + i * 3
        t = ((f - st) / 30)
        if t > 0: nota_voando(c, 900, 1100, 330, 680, t % 1 if f < v0 + 20 else min(t, .99), 150, ('#5aa66a', '#3aa66a')[i % 2], i * 20)
    if f >= v0:
        sc = back(ramp(f, v0, v0 + 8))
        paste_c(c, caixa().resize((240, 210)), 640, 1340, sc)
        num(c, 'US$', 870, 1000, f, v0, 110, 4)
        seta(c, 1030, 1010, 150, up=True, col=RED, s=sc)
    g0 = wt(4, 'viagens') - 3
    if f >= g0:
        paste_c(c, mala().resize((220, 235)), 930, 1350, back(ramp(f, g0, g0 + 8)))
    t = smooth(ramp(f, 0, 160))
    k = kick(f, v0, .7)
    return c, (640 + 20 * math.sin(f * .03), lerp(1000, 1100, t) + k * 6, lerp(1.05, 1.13, t) * (1 + .0004 * f), lerp(0, -1.5, t) + k), 'dusk'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    paste_c(c, calendario(), 520, 900, back(ramp(f, 0, 8)))
    num(c, 'DEZEMBRO', 520, 700, f, wt(5, 'dezembro') - 3, 100, -3)
    num(c, '8 E 9', 520, 960, f, wt(5, 'oito') - 3, 150, 3)
    put_pol(c, 960, 1660, 700, f, 7, skin=1, hair='#3a2a20', tie='#2f6fd6', suit='#2c3550', expr='neutral', arms='point', look=-1)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 70))) + .0006 * f
    return c, (640, 1050, z, lerp(0, 1.5, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    s.thunk(s.W(0, 'quinze') - 3, 160, .8)
    s.ting(s.W(0, 'Estados') - 3, .3)
    s.thunk(s.W(1, 'cinco') - 3, 140, 1.0)
    s.ting(s.W(1, 'meio') - 3, .3)
    s.thunk(s.W(2, 'zero') - 3, 150, .8)
    s.thunk(s.W(2, 'comida') - 3, 220, .5)
    s.thunk(s.W(3, 'oitenta') - 3, 140, .9)
    s.whoosh(s.W(3, 'juros') - 3, .3, .5)
    s.patter(s.W(4, 'dinheiro') - 3, s.W(4, 'dinheiro') + 30, 10, .12)
    s.thunk(s.W(4, 'encarece') - 3, 200, .7)
    s.ting(s.W(5, 'oito') - 3, .3)
