"""Um Café com o Mundo — NO SEU BOLSO (sábado 07/11/2026, 10h).
Tema: relatório de emprego dos EUA de outubro (divulgado sexta 06/11/2026) e a chance de o Fed subir juros em dezembro.
Fontes (conferidas em 07/11/2026):
- ABC News, 06/11/2026 "Jobs report shows hiring accelerated in October": 165 mil vagas em outubro, contra 29 mil no mês
  anterior; inflação anual de 3,7% em setembro, acima da meta de 2% do Fed; Fed subiu os juros em 1/4 de ponto em setembro,
  1ª alta desde 2023; mercado vê ~68% de chance de nova alta de 1/4 de ponto em dezembro (CME FedWatch).
- Indeed Hiring Lab, 06/11/2026 "October 2026 Jobs Report" (dados do BLS): desemprego caiu para 4,1% (de 4,2%); saúde e
  assistência social = ~60% das vagas criadas nos últimos 12 meses.
- TheStreet, 06/11/2026: 165 mil contra consenso de 59 mil.
Elo com o Brasil: só o mecanismo geral (juros mais altos nos EUA tendem a atrair capital e pressionar moedas emergentes), sem previsão.
Personagens genéricos (sem traços de pessoas reais)."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'NO SEU BOLSO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Uma boa notícia nos Estados Unidos pode acabar chegando no seu bolso.",
    "Em outubro, as empresas americanas criaram cento e sessenta e cinco mil vagas. No mês anterior, tinham sido só vinte e nove mil.",
    "O desemprego caiu para quatro vírgula um por cento, e a saúde puxa boa parte das contratações.",
    "Só que a inflação por lá está em três vírgula sete por cento, bem acima da meta de dois.",
    "Por isso, o mercado vê sessenta e oito por cento de chance de o banco central americano subir os juros de novo em dezembro.",
    "Por que isso importa? Juros mais altos lá costumam atrair dinheiro do mundo todo, e isso pode pressionar o real.",
    "Agora, a decisão sai em dezembro.",
]
CAPTXT = [
    "Uma boa notícia nos Estados Unidos|pode acabar chegando no seu bolso.",
    "Em outubro, as empresas americanas criaram 165 mil vagas.|No mês anterior, tinham sido só 29 mil.",
    "O desemprego caiu para 4,1%,|e a saúde puxa boa parte das contratações.",
    "Só que a inflação por lá está em 3,7%,|bem acima da meta de 2%.",
    "Por isso, o mercado vê 68% de chance|de o banco central americano|subir os juros de novo em dezembro.",
    "Por que isso importa? Juros mais altos lá|costumam atrair dinheiro do mundo todo,|e isso pode pressionar o real.",
    "Agora, a decisão sai em dezembro.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Estados', 4), (0, 'bolso', 6), (1, 'cento', 6), (1, 'vinte', 6), (2, 'quatro', 6), (2, 'saude', 6),
         (3, 'tres', 6), (3, 'dois', 6), (4, 'sessenta', 6), (4, 'juros', 6), (5, 'dinheiro', 8), (5, 'real', 6),
         (6, 'dezembro', 6)]

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


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('cidade', 'day').copy()
    e0 = wt(0, 'Estados') - 3
    num(c, 'EUA', 330, 560, f, e0, 140, -4)
    b0 = wt(0, 'bolso') - 3
    paste_c(c, carteira(), 820, 1240, back(ramp(f, b0 - 8, b0)) if f >= b0 - 8 else 0.01)
    for i in range(5):
        st = e0 + 6 + i * 5
        t = clamp((f - st) / 26)
        nota_voando(c, 330, 760, 820, 1200, t, 170, '#5aa66a', i * 12)
    num(c, 'SEU BOLSO', 800, 980, f, b0, 100, 4)
    put_pol(c, 330, 1540, 560, f, 2, skin=0, hair='#3a2a20', tie='#2f6fd6', suit='#2c3550', expr='grin' if f > e0 else 'neutral', arms='point' if f > e0 + 4 else 'hang', look=1)
    z = lerp(1.4, 1.08, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, b0)
    return c, (640, 1150 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    num(c, 'OUTUBRO', 640, 400, f, 0, 100, -3)
    c0 = wt(1, 'cento') - 3
    v0 = wt(1, 'vinte') - 3
    barra(c, 800, 1250, 230, 540, GREEN, '', f, c0, '165 MIL')
    barra(c, 480, 1250, 230, 100, hexc('#9aa4b4'), '', f, v0, '29 MIL')
    num(c, 'VAGAS NOVAS', 640, 530, f, c0 + 4, 70, 3)
    # trabalhadores surgindo
    for i, x in enumerate((310, 980)):
        st = c0 + 4 + i * 5
        s = back(ramp(f, st, st + 8))
        if s > .05:
            put_pol(c, x, 1560, 420 * s, f, 10 + i, skin=i, hair=('#2a221e', '#8a5a3a')[i], tie=('#3aa66a', '#d8443c')[i], suit=('#4a4f63', '#6b4a6b')[i],
                    expr='grin', arms='up' if i == 0 else 'point', look=1 - 2 * i)
            put_dust(c, x, 1540, 70, f - st)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, c0, .8)
    return c, (640, lerp(950, 1020, t) + k * 8, lerp(1.2, 1.04, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    q0 = wt(2, 'quatro') - 3
    num(c, 'DESEMPREGO', 540, 480, f, wt(2, 'desemprego') - 3, 96, -3)
    num(c, '4,1%', 500, 680, f, q0, 180, 3)
    seta(c, 830, 690, 240, up=False, col=GREEN, s=back(ramp(f, q0 + 2, q0 + 10)))
    s0_ = wt(2, 'saude') - 3
    num(c, 'SAÚDE', 900, 980, f, s0_, 110, -4)
    # profissional de saúde de jaleco
    if f >= s0_ - 2:
        put_sci(c, 900, 1560, 640 * back(ramp(f, s0_ - 2, s0_ + 6)), f, 4, arms='up', skin=2, hair='#2a221e', expr='grin', look=-1)
    put_pol(c, 380, 1560, 620, f, 5, skin=1, hair='#6b4a2a', tie='#f0c541', suit='#3a3a44', expr='grin' if f > q0 else 'neutral', arms='up' if f > q0 + 4 else 'hang', look=1)
    z = lerp(1.12, 1.02, smooth(ramp(f, 0, 90))) * (1 + .0006 * f)
    k = kick(f, q0, .6)
    return c, (640 + 20 * math.sin(f * .03), 1080 + k * 6, z, k), 'day'


def s3(f):
    c = CEN('cidade', 'golden').copy()
    t0 = wt(3, 'tres') - 3
    lvl = int(round(7 * easeOut(ramp(f, t0 - 4, t0 + 12))))
    paste_c(c, termometro(lvl), 440, 1010, 1)
    num(c, 'INFLAÇÃO', 640, 400, f, wt(3, 'inflacao') - 3, 110, -3)
    num(c, '3,7%', 760, 760, f, t0, 190, 4)
    m0 = wt(3, 'meta') - 3
    if f >= m0:
        d = ImageDraw.Draw(c)
        y = 1010 + 350 - 500 * 3.8 / 8  # linha da meta
        d.line([(330, y), (560, y)], fill=INK, width=10)
        d.line([(330, y), (560, y)], fill=GOLD, width=5)
    num(c, 'META: 2%', 820, 1080, f, wt(3, 'dois') - 3, 100, -3)
    put_pol(c, 1060, 1600, 520, f, 6, skin=2, hair='#2a221e', tie='#d8443c', suit='#4a4f63', expr='nervous' if f > t0 else 'neutral', arms='cheek' if f > t0 else 'hang', look=-1)
    t = smooth(ramp(f, 0, 110))
    return c, (640, lerp(1000, 1080, t), lerp(1.0, 1.12, t), lerp(0, 1.5, t)), 'golden'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, banco().resize((820, 624)), 640, 1080, 1)
    num(c, 'BANCO CENTRAL DOS EUA', 640, 1450, f, wt(4, 'banco') - 3, 70, 0)
    s0_ = wt(4, 'sessenta') - 3
    num(c, '68%', 380, 560, f, s0_, 170, -4)
    num(c, 'DE CHANCE', 380, 700, f, s0_ + 4, 80, 3)
    j0 = wt(4, 'juros') - 3
    num(c, 'JUROS', 930, 500, f, j0, 110, 4)
    seta(c, 930, 740, 220, up=True, col=RED, s=back(ramp(f, j0 + 2, j0 + 10)))
    num(c, 'DEZEMBRO', 930, 860, f, wt(4, 'dezembro') - 3, 76, -3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, j0, .8)
    return c, (640, 1050 + k * 8, z, k), 'dusk'


def s5(f):
    c = CEN('mapa', 'dusk').copy()
    num(c, 'EUA', 330, 560, f, 0, 130, -4)
    num(c, 'BRASIL', 820, 1180, f, wt(5, 'importa'), 110, 3)
    d0 = wt(5, 'dinheiro') - 3
    for i in range(10):
        st = d0 + i * 3
        t = ((f - st) / 30)
        if t > 0: nota_voando(c, 900, 1100, 330, 680, t % 1 if f < wt(5, 'real') + 40 else min(t, .99), 150, ('#5aa66a', '#3aa66a')[i % 2], i * 20)
    r0 = wt(5, 'real') - 3
    if f >= r0:
        paste_c(c, txt('R$', 150, 4), 780, 1380, back(ramp(f, r0, r0 + 8)))
        seta(c, 950, 1390, 190, up=False, col=RED, s=back(ramp(f, r0 + 3, r0 + 11)))
    num(c, 'JUROS MAIS ALTOS', 560, 430, f, wt(5, 'juros') - 3, 80, -3)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, r0, .7)
    return c, (640 + 20 * math.sin(f * .03), lerp(1000, 1100, t) + k * 6, lerp(1.05, 1.15, t), lerp(0, -1.5, t) + k), 'dusk'


def s6(f):
    c = CEN('escritorio', 'dusk').copy()
    paste_c(c, calendario(), 520, 900, back(ramp(f, 0, 8)))
    num(c, 'DEZEMBRO', 520, 700, f, wt(6, 'dezembro') - 3, 100, -3)
    put_pol(c, 960, 1660, 700, f, 7, skin=1, hair='#3a2a20', tie='#2f6fd6', suit='#2c3550', expr='neutral', arms='point', look=-1)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 70))) + .0006 * f
    return c, (640, 1050, z, lerp(0, 1.5, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'Estados') - 3, 160, .8)
    s.ting(s.W(0, 'bolso') - 3, .3)
    s.thunk(s.W(1, 'cento') - 3, 140, 1.0)
    s.thunk(s.W(1, 'vinte') - 3, 260, .5)
    s.thunk(s.W(2, 'quatro') - 3, 180, .7)
    s.ting(s.W(2, 'saude') - 3, .25)
    s.thunk(s.W(3, 'tres') - 3, 150, .8)
    s.thunk(s.W(4, 'sessenta') - 3, 140, .9)
    s.whoosh(s.W(4, 'juros') - 3, .3, .5)
    s.patter(s.W(5, 'dinheiro') - 3, s.W(5, 'dinheiro') + 30, 10, .12)
    s.thunk(s.W(5, 'real') - 3, 200, .7)
    s.ting(s.W(6, 'dezembro') - 3, .3)
