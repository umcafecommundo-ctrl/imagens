"""Um Café com o Mundo — NO SEU BOLSO (sexta 13/11/2026, 10h).
Tema: ouro cai ao menor preço em 1 ano com juros americanos de 10 anos acima de 5% e apostas de alta do Fed; dólar sobe e no Brasil fecha a R$ 5,65.
Fontes (conferidas em 13/11/2026):
- Saxo Asia Market Quick Take, 13/11/2026: ouro na mínima de 1 ano, caiu até 3,4% para abaixo de US$ 3.860/onça na quinta (12/11),
  vindo de acima de US$ 4.100 no começo da semana; Treasury de 10 anos volta acima de 5% pela 1ª vez desde 22/10; mercado precifica
  ~88 pontos-base de alta do Fed até meados de 2027; índice do dólar na máxima de 18 meses.
- Rio Times, Global Economy Briefing 13/11/2026: 10 anos em 5,13%; ouro US$ 3.881 (-2,46%); apostas em alta (e não corte) do Fed;
  ouro não rende juros, sofre com juros altos e dólar firme.
- O Tempo / Estadão Conteúdo, 12/11/2026: dólar fecha a R$ 5,65 (+1,6%), maior nível desde 2/6/2025; pesaram juros dos EUA e
  dúvidas sobre o pacote fiscal do governo.
- Decisão do Fed em 8-9/12 (Fox Business, 10/11/2026).
Personagens genéricos (sem traços de pessoas reais)."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'NO SEU BOLSO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O ouro caiu para o menor preço em um ano.",
    "Na quinta, a onça ficou abaixo de três mil e novecentos dólares. No começo da semana, passava de quatro mil e cem.",
    "O motivo: os juros americanos de dez anos voltaram a passar de cinco por cento, e o mercado aposta em alta de juros por lá.",
    "Por que importa? O ouro não rende juros, então o dinheiro corre para o dólar.",
    "Aqui, o dólar fechou a cinco reais e sessenta e cinco, o maior valor desde junho do ano passado.",
    "A próxima decisão de juros lá sai nos dias oito e nove de dezembro.",
]
CAPTXT = [
    "O ouro caiu para o menor preço em 1 ano.",
    "Na quinta, a onça ficou abaixo de US$ 3.900.|No começo da semana,|passava de US$ 4.100.",
    "O motivo: os juros americanos de 10 anos|voltaram a passar de 5%,|e o mercado aposta em alta de juros por lá.",
    "Por que importa? O ouro não rende juros,|então o dinheiro corre para o dólar.",
    "Aqui, o dólar fechou a R$ 5,65,|o maior valor desde junho do ano passado.",
    "A próxima decisão de juros lá|sai nos dias 8 e 9 de dezembro.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'menor', 6), (0, 'ano', 6), (1, 'tres', 8), (1, 'quatro', 8), (2, 'dez', 6), (2, 'cinco', 6), (2, 'alta', 6),
         (3, 'juros', 6), (3, 'dolar', 8), (4, 'cinco', 8), (4, 'junho', 6), (5, 'oito', 6)]

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



# ------------------------------------------------------------------ desenhos novos (13/11)
@lru_cache(maxsize=2)
def barra_ouro():
    """barra de ouro em trapézio com brilho. 520x300"""
    p = Pen(520, 300)
    p.shape([(20, 280), (500, 280), (430, 60), (90, 60)], GOLD, GOLD_D, 7, 14)
    p.shape([(90, 60), (430, 60), (400, 20), (120, 20)], hexc('#f8dc78'), GOLD_D, 5, 4)
    p.poly([(150, 110), (370, 110), (390, 170), (130, 170)], hexc('#f8dc78'))
    p.stroke([(130, 230), (200, 230)], 5)
    return fin(p)


def ouro(c, x, y, w, rot=0, s=1.0):
    if s <= .02: return
    im = barra_ouro().resize((int(w * s), int(w * s * 300 / 520)))
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    paste_c(c, im, x, y, 1)


def brilho(c, x, y, f, r=40):
    d = ImageDraw.Draw(c)
    a = (f * .25) % 6.28
    k = r * (0.6 + 0.4 * math.sin(f * .3))
    for ang in (a, a + 1.57):
        dx, dy = k * math.cos(ang), k * math.sin(ang)
        d.line([(x - dx, y - dy), (x + dx, y + dy)], fill=WHITE, width=8)


def grafico_cai(c, x0, y0, w, h, f, f0, dur=40):
    """linha do ouro caindo, desenhada aos poucos."""
    if f < f0: return
    d = ImageDraw.Draw(c)
    d.rectangle([x0 - 20, y0 - h - 20, x0 + w + 20, y0 + 20], fill=(255, 255, 255), outline=INK, width=6)
    vals = [.85, .90, .82, .86, .70, .74, .55, .48, .30, .12]
    t = easeOut(ramp(f, f0, f0 + dur))
    n = max(2, int(2 + t * (len(vals) - 2)))
    pts = [(x0 + w * i / (len(vals) - 1), y0 - h * v) for i, v in enumerate(vals[:n])]
    d.line([(px + 5, py + 5) for px, py in pts], fill=INK, width=16)
    d.line(pts, fill=GOLD, width=12)
    px, py = pts[-1]
    d.ellipse([px - 16, py - 16, px + 16, py + 16], fill=GOLD, outline=INK, width=5)


def s0(f):
    c = CEN('cidade', 'day').copy()
    m0 = wt(0, 'menor') - 3
    a0 = wt(0, 'ano') - 3
    fall = easeOut(ramp(f, 0, 16))
    y = lerp(420, 720, fall) + 10 * math.sin(f * .12)
    ouro(c, 640, y, 560, -6 + 3 * math.sin(f * .1), back(ramp(f, 0, 8)))
    brilho(c, 520, y - 60, f)
    seta(c, 1000, 780, 240, up=False, col=RED, s=back(ramp(f, 3, 12)))
    num(c, 'OURO', 640, 430 if f > 16 else 9999, f, 2, 120, -4)
    num(c, 'MENOR PREÇO', 640, 990, f, m0, 100, -3)
    num(c, 'EM 1 ANO', 640, 1110, f, a0, 110, 3)
    put_pol(c, 200, 1650, 440, f, 2, skin=0, hair='#3a2a20', tie='#f0c541', suit='#2c3550',
            expr='shock' if f > m0 else 'neutral', arms='up' if f > m0 + 3 else 'hang', look=1)
    put_pol(c, 1060, 1660, 440, f, 3, skin=2, hair='#2a221e', tie='#2f6fd6', suit='#4a4f63',
            expr='nervous' if f > a0 else 'shock', arms='cheek', look=-1)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, 12) + kick(f, m0, .6)
    return c, (640, 1040 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    num(c, 'QUINTA, 12/11', 640, 360, f, 0, 86, -3)
    t0 = wt(1, 'tres') - 3
    q0 = wt(1, 'quatro') - 3
    grafico_cai(c, 220, 1200, 780, 520, f, 0, max(20, t0))
    num(c, 'US$ 3.900', 640, 1330, f, t0, 130, 3)
    num(c, 'ABAIXO DE', 640, 1220 if f > t0 else 9999, f, t0, 60, -2)
    num(c, 'ERA US$ 4.100', 640, 480, f, q0, 96, -3)
    num(c, 'POR ONÇA', 900, 820, f, wt(1, 'onca') - 3, 70, 4)
    ouro(c, 1050, 1080, 220, 8, back(ramp(f, 4, 12)))
    t = smooth(ramp(f, 0, 140))
    k = kick(f, t0, .8)
    return c, (640, lerp(960, 1020, t) + k * 8, lerp(1.16, 1.04, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, banco().resize((820, 624)), 640, 1150, 1)
    num(c, 'EUA', 640, 1040, f, 0, 90, 0)
    d0 = wt(2, 'dez') - 3
    c0 = wt(2, 'cinco') - 3
    a0 = wt(2, 'alta') - 3
    num(c, 'JUROS DE 10 ANOS', 640, 380, f, wt(2, 'juros') - 3, 80, -3)
    num(c, '5%', 420, 600, f, c0, 220, -4)
    num(c, 'ACIMA DE', 420, 470 if f > c0 else 9999, f, c0, 60, 2)
    seta(c, 720, 660, 230, up=True, col=RED, s=back(ramp(f, c0 + 2, c0 + 10)))
    num(c, 'ALTA DE JUROS?', 790, 830, f, a0, 80, 4)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, c0, .8)
    return c, (640, 1040 + k * 8, z, k), 'dusk'


def s3(f):
    c = CEN('escritorio', 'dusk').copy()
    j0 = wt(3, 'juros') - 3
    d0 = wt(3, 'dolar') - 3
    ouro(c, 380, 1180, 340, -4 + 2 * math.sin(f * .08), 1)
    num(c, 'NÃO RENDE JUROS', 640, 620, f, j0, 80, -3)
    num(c, '0%', 380, 980, f, j0 + 2, 120, 3)
    paste_c(c, nota('#5aa66a').resize((300, 150)).rotate(6, expand=True, resample=Image.BICUBIC), 860, 1160, back(ramp(f, d0 - 10, d0)))
    num(c, 'US$', 860, 1160, f, d0 - 6, 100, 6)
    num(c, 'DÓLAR', 860, 800, f, d0, 100, 4)
    for i in range(8):
        st = d0 - 14 + i * 3
        t = (f - st) / 26
        if t > 0: nota_voando(c, 400, 1100, 860, 1120, t % 1, 130, ('#5aa66a', '#3aa66a')[i % 2], i * 20)
    num(c, 'POR QUE IMPORTA?', 640, 430, f, 0, 86, -3)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, d0, .7)
    return c, (640 + 15 * math.sin(f * .03), lerp(1000, 1060, t) + k * 6, lerp(1.04, 1.12, t) * (1 + .0004 * f), lerp(0, 1.5, t) + k), 'dusk'


def s4(f):
    c = CEN('mapa', 'dusk').copy()
    c0 = wt(4, 'cinco') - 3
    j0 = wt(4, 'junho') - 3
    num(c, 'BRASIL', 820, 1180, f, 0, 110, 3)
    paste_c(c, carteira().resize((300, 216)), 820, 1360, back(ramp(f, 2, 10)))
    num(c, 'R$ 5,65', 560, 560, f, c0, 160, -4)
    seta(c, 930, 760, 180, up=True, col=GREEN, s=back(ramp(f, c0 + 2, c0 + 10)))
    num(c, 'MAIOR DESDE', 600, 760, f, wt(4, 'maior') - 3, 80, 3)
    num(c, 'JUNHO DE 2025', 600, 870, f, j0, 90, -3)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, c0, .8)
    return c, (640 + 20 * math.sin(f * .03), lerp(1000, 1080, t) + k * 6, lerp(1.05, 1.12, t) * (1 + .0004 * f), lerp(0, -1.5, t) + k), 'dusk'


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
    s.thunk(12, 160, .9)
    s.ting(s.W(0, 'menor') - 3, .3)
    s.thunk(s.W(1, 'tres') - 3, 140, 1.0)
    s.ting(s.W(1, 'quatro') - 3, .3)
    s.thunk(s.W(2, 'cinco') - 3, 150, .9)
    s.whoosh(s.W(2, 'alta') - 3, .3, .5)
    s.patter(s.W(3, 'dolar') - 14, s.W(3, 'dolar') + 20, 8, .12)
    s.thunk(s.W(4, 'cinco') - 3, 200, .8)
    s.ting(s.W(5, 'oito') - 3, .3)
