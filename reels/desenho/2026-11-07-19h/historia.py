"""Um Café com o Mundo — O MUNDO EXPLICADO (sábado 07/11/2026, 19h).
Tema: ataque a tiros na Praça do Mercado (Rynek Główny) de Cracóvia, Polônia, sábado 07/11/2026 por volta das 15h locais.
Fontes (conferidas em 07/11/2026, ~18h de Brasília):
- Al Jazeera (07/11/2026, "At least six people killed in shooting in Poland's Krakow"): ~15h locais (14:00 GMT), Praça do
  Mercado no centro; pelo menos 6 mortos (4 mulheres e 2 homens); 15 feridos, entre eles 2 policiais, um em estado crítico
  (ministro do Interior Marcin Kierwinski); suspeito polonês que agiu sozinho, entrou de carro na praça e "começou a atirar
  em pessoas ao acaso de dentro do carro"; policiais atiraram nele, foi detido e levado ao hospital; motivo não informado;
  tiroteios fatais são muito raros na Polônia; país em alerta após série de esfaqueamentos em outubro;
  condolências de Tusk, Nawrocki, Kallas (UE), Zelensky e embaixador dos EUA.
- Euronews (07/11/2026, "Six people killed and 15 injured in shooting in Kraków, Polish authorities say"): Praça Principal,
  basílica de Santa Maria, atirador disparou de um carro (bombeiros à Polsat), baleado pela polícia e levado ao hospital.
Fato em andamento: números "até a última atualização". Personagens genéricos, sem pessoas reais. Tom sério, sem violência
mostrada (só símbolos: sirene, marcador, números)."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um ataque a tiros no centro histórico de Cracóvia, na Polônia, deixou pelo menos seis mortos.",
    "Foi neste sábado, por volta das três da tarde, na Praça do Mercado, no coração da cidade.",
    "Segundo a polícia, um homem entrou de carro na praça e começou a atirar contra pessoas ao acaso.",
    "Até a última atualização, quinze pessoas ficaram feridas, entre elas dois policiais, e um deles está em estado grave.",
    "A polícia atirou no suspeito, um polonês que agiu sozinho. Ele foi detido e levado ao hospital.",
    "Por que isso importa? Ataques a tiros assim são muito raros na Polônia, que já estava em alerta por uma série de esfaqueamentos em outubro.",
    "Agora, a polícia investiga o motivo, e líderes de toda a Europa enviaram condolências.",
]
CAPTXT = [
    "Um ataque a tiros no centro histórico de Cracóvia,|na Polônia, deixou pelo menos 6 mortos.",
    "Foi neste sábado, por volta das 3 da tarde,|na Praça do Mercado,|no coração da cidade.",
    "Segundo a polícia, um homem entrou de carro na praça|e começou a atirar contra pessoas ao acaso.",
    "Até a última atualização, 15 pessoas ficaram feridas,|entre elas 2 policiais,|e um deles está em estado grave.",
    "A polícia atirou no suspeito,|um polonês que agiu sozinho.|Ele foi detido e levado ao hospital.",
    "Por que isso importa? Ataques a tiros assim|são muito raros na Polônia,|que já estava em alerta|por uma série de esfaqueamentos em outubro.",
    "Agora, a polícia investiga o motivo,|e líderes de toda a Europa enviaram condolências.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = []
CHECK = [(0, 'Cracovia', 4), (0, 'seis', 6), (1, 'tres', 6), (1, 'Mercado', 6), (2, 'carro', 6), (2, 'acaso', 4),
         (3, 'quinze', 6), (3, 'policiais', 6), (3, 'grave', 6), (4, 'sozinho', 4), (4, 'detido', 6),
         (5, 'raros', 6), (5, 'outubro', 4), (6, 'motivo', 6), (6, 'condolencias', 6)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); BLUE = hexc('#2f6fd6'); BLUE_D = hexc('#1f4f9e')
GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e'); WHITE = (255, 255, 255)
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); GRAY = hexc('#9aa4b4'); GRAY_D = hexc('#6f788a')
BRICK = hexc('#c46a4a'); BRICK_D = hexc('#94492f'); ROOF = hexc('#5a6b5e'); ROOF_D = hexc('#3e4b41')
CREAM = hexc('#efd9a8'); CREAM_D = hexc('#c4ab78'); NAVY = '#1f2e4a'


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


@lru_cache(maxsize=2)
def praca():
    """casario antigo genérico de praça europeia + torre de igreja. 1242x1100, base y~1090."""
    p = Pen(1242, 1100)
    # torre gótica genérica
    p.shape([(780, 260), (900, 260), (900, 1090), (780, 1090)], BRICK, BRICK_D, 7, 14)
    p.shape([(770, 260), (840, 40), (910, 260)], ROOF, ROOF_D, 6, 8)
    p.stroke([(840, 40), (840, -10)], 8)
    for y in (360, 520, 680):
        p.shape([(815, y), (865, y), (865, y + 90), (815, y + 90)], hexc('#3a3150'), hexc('#2a2340'), 4, 2)
    cols = [(CREAM, CREAM_D), (hexc('#e7b9a0'), hexc('#bb8c74')), (hexc('#cfe0c4'), hexc('#9fb594')), (hexc('#f3e3c0'), hexc('#c8b48a'))]
    xs = [(0, 200, 600), (200, 400, 520), (400, 600, 640), (600, 780, 560), (900, 1060, 600), (1060, 1242, 540)]
    for i, (x0, x1, top) in enumerate(xs):
        col, cd = cols[i % 4]
        p.shape([(x0, top), (x1, top), (x1, 1090), (x0, 1090)], col, cd, 6, 10)
        p.shape([(x0 - 6, top), ((x0 + x1) / 2, top - 110), (x1 + 6, top)], BRICK, BRICK_D, 6, 6)
        for r in range(3):
            for k in range(2):
                wx = x0 + 40 + k * ((x1 - x0) - 120) / 1 * .5 + k * 20
                wy = top + 60 + r * 130
                if wy + 80 < 1060:
                    p.shape([(wx, wy), (wx + 50, wy), (wx + 50, wy + 76), (wx, wy + 76)], hexc('#f7d77a'), GOLD_D, 4, 2)
    return fin(p)


@lru_cache(maxsize=2)
def carro():
    """carro genérico de lado (escuro). 600x300, rodas y~290."""
    p = Pen(600, 300)
    p.shape([(30, 250), (30, 170), (130, 160), (200, 80), (420, 80), (500, 160), (575, 175), (575, 250)], hexc('#4a4f63'), hexc('#33374a'), 7, 10)
    p.shape([(220, 100), (300, 100), (300, 160), (165, 160)], hexc('#9fb8d0'), hexc('#6f8aa6'), 4, 3)
    p.shape([(320, 100), (405, 100), (470, 160), (320, 160)], hexc('#9fb8d0'), hexc('#6f8aa6'), 4, 3)
    for x in (140, 460):
        p.dot(x, 250, 46, hexc('#2a2a30'), 6)
        p.dot(x, 250, 18, GRAY, 4)
    p.dot(560, 200, 12, GOLD, 3)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira():
    """bandeira da Polônia (país, permitido). 600x380"""
    p = Pen(600, 380)
    p.shape([(10, 10), (590, 10), (590, 370), (10, 370)], WHITE, hexc('#d6dbe6'), 6, 8)
    p.poly([(10, 190), (590, 190), (590, 370), (10, 370)], hexc('#dc143c'))
    p.stroke([(10, 10), (590, 10), (590, 370), (10, 370), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def hospital():
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
    p = Pen(200, 280)
    p.shape([(100, 272), (30, 120), (40, 60), (100, 20), (160, 60), (170, 120)], RED, RED_D, 6, 8)
    p.dot(100, 100, 34, WHITE, 5)
    return fin(p)


@lru_cache(maxsize=2)
def vela():
    """vela acesa de homenagem. 160x320, base y~310"""
    p = Pen(160, 320)
    p.shape([(40, 120), (120, 120), (120, 310), (40, 310)], WHITE, hexc('#d9d4ca'), 5, 6)
    p.stroke([(80, 120), (80, 96)], 5)
    p.shape([(80, 20), (104, 70), (80, 100), (56, 70)], GOLD, hexc('#e8902e'), 4, 4)
    return fin(p)


@lru_cache(maxsize=2)
def lupa():
    p = Pen(400, 400)
    p.stroke([(250, 250), (370, 370)], 34, hexc('#6b4a2e'))
    p.shape(ell_pts(170, 170, 130, 130, 40), hexc('#c9e6f5'), hexc('#8fb8d0'), 10, 6)
    return fin(p)


@lru_cache(maxsize=2)
def faixa():
    """faixa de isolamento listrada. 1242x80"""
    p = Pen(1242, 80)
    p.shape([(0, 10), (1242, 10), (1242, 70), (0, 70)], GOLD, GOLD_D, 5, 4)
    for x in range(0, 1242, 90):
        p.poly([(x, 10), (x + 40, 10), (x + 10, 70), (x - 30, 70)], hexc('#2a2a30'))
    return fin(p)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def sirene(c, x, y, f, f0, r=34):
    if f < f0: return
    d = ImageDraw.Draw(c)
    on = (f // 8) % 2 == 0
    col = BLUE if on else RED
    d.ellipse([x - r - 30, y - r - 30, x + r + 30, y + r + 30], fill=mul(col, .55) if on else mul(col, .6))
    d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=INK, width=5)


def cenario_praca(luz):
    c = CEN('cidade', luz).copy()
    paste_c(c, praca(), 621, 1560 - 550, 1)
    d = ImageDraw.Draw(c)
    d.rectangle([0, 1560, BW, BH], fill=hexc('#b9ae9c'))
    for x in range(0, BW, 110):
        d.line([(x, 1560), (x - 60, BH)], fill=hexc('#a39886'), width=4)
    return c


# ------------------------------------------------------------------ cenas
def s0(f):
    c = cenario_praca('dusk')
    k0 = wt(0, 'Cracovia') - 3
    if f >= k0 - 4:
        paste_c(c, marcador(), 640, 820, back(ramp(f, k0 - 4, k0 + 6)))
    num(c, 'CRACÓVIA', 640, 430, f, k0, 120, -3)
    num(c, 'POLÔNIA', 640, 560, f, wt(0, 'Polonia') - 3, 80, 3)
    s0_ = wt(0, 'seis') - 3
    num(c, 'PELO MENOS 6 MORTOS', 640, 1240, f, s0_, 82, -2)
    sirene(c, 260, 1420, f, 0)
    sirene(c, 1000, 1420, f + 4, 0)
    z = lerp(1.35, 1.04, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, s0_, .6)
    return c, (640, 980 + k * 6, z, k * .5), 'dusk'


def s1(f):
    c = cenario_praca('golden')
    t0 = wt(1, 'tres') - 3
    if f >= t0:
        paste_c(c, clock_img(1.5708, 0.0, 300), 330, 560, back(ramp(f, t0, t0 + 8)))
    num(c, 'SÁBADO', 330, 360, f, wt(1, 'sabado') - 3, 80, -3)
    num(c, '15H', 330, 790, f, t0 + 2, 110, 3)
    m0 = wt(1, 'Mercado') - 3
    num(c, 'PRAÇA DO MERCADO', 640, 1300, f, m0, 66, -2)
    t = smooth(ramp(f, 0, 120))
    return c, (lerp(560, 700, t), lerp(960, 1000, t), lerp(1.12, 1.02, t) * (1 + .0005 * f), lerp(-1, 1, t)), 'golden'


def s2(f):
    c = cenario_praca('dusk')
    c0 = wt(2, 'carro') - 6
    if f >= c0:
        tt = easeOut(ramp(f, c0, c0 + 40))
        x = lerp(-300, 560, tt)
        im = carro().resize((520, 260))
        c.paste(im, (int(x - 260), 1520 - 250), im)
    num(c, 'POLÍCIA:', 640, 430, f, 0, 70, -2)
    num(c, 'ENTROU DE CARRO', 640, 560, f, c0 + 3, 86, -3)
    a0 = wt(2, 'acaso') - 3
    num(c, '!', 960, 1100, f, wt(2, 'atirar') - 3, 220, 6)
    num(c, 'AO ACASO', 640, 720, f, a0, 86, 3)
    t = ramp(f, 0, 240)
    k = kick(f, wt(2, 'atirar') - 3, .5)
    return c, (640 + 24 * math.sin(f * .05), 1000 + 10 * math.cos(f * .04) + k * 6, lerp(1.0, 1.14, t) + .0004 * f, lerp(0, -2, t) + k * .5), 'dusk'


def s3(f):
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, hospital().resize((760, 760)), 640, 1180, 1)
    q0 = wt(3, 'quinze') - 3
    num(c, '15 FERIDOS', 640, 440, f, q0, 120, -4)
    num(c, '2 POLICIAIS', 440, 640, f, wt(3, 'policiais') - 3, 72, 3)
    g0 = wt(3, 'grave') - 3
    num(c, '1 EM ESTADO GRAVE', 780, 760, f, g0, 54, -2)
    sirene(c, 640, 860, f, q0)
    t = ramp(f, 0, 220)
    return c, (640 + 14 * math.sin(f * .04), lerp(1000, 1040, t), lerp(1.0, 1.1, t) * (1 + .0003 * f), lerp(0, 1.2, t)), 'dusk'


def s4(f):
    c = cenario_praca('dusk')
    paste_c(c, faixa(), 621, 1500, 1)
    put_pol(c, 380, 1640, 620, f, 5, skin=1, hair='#2a221e', tie=NAVY, suit=NAVY, expr='stern', arms='hang', look=1)
    put_pol(c, 880, 1640, 600, f, 9, skin=3, hair='#5a4030', tie=NAVY, suit=NAVY, expr='stern', arms='hang', look=-1)
    num(c, 'POLÍCIA', 380, 900, f, 0, 70, -3)
    num(c, 'POLÍCIA', 880, 920, f, 4, 70, 3)
    s0_ = wt(4, 'sozinho') - 3
    num(c, 'AGIU SOZINHO', 640, 450, f, s0_, 92, -3)
    d0 = wt(4, 'detido') - 3
    num(c, 'SUSPEITO DETIDO', 640, 600, f, d0, 80, 2)
    sirene(c, 160, 1300, f, 0, 28)
    sirene(c, 1090, 1300, f + 4, 0, 28)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, d0, .6)
    return c, (640, lerp(1060, 1000, t) + k * 6, lerp(1.1, 1.0, t) * (1 + .0005 * f), k * .5), 'dusk'


def s5(f):
    c = CEN('mapa', 'dusk').copy()
    paste_c(c, bandeira().resize((420, 266)), 640, 640, back(ramp(f, 0, 10)))
    num(c, 'POLÔNIA', 640, 450, f, 0, 100, -3)
    r0 = wt(5, 'raros') - 3
    num(c, 'MUITO RARO', 640, 900, f, r0, 110, -3)
    a0 = wt(5, 'alerta') - 3
    num(c, 'PAÍS JÁ EM ALERTA', 640, 1100, f, a0, 72, 2)
    o0 = wt(5, 'outubro') - 3
    num(c, 'OUTUBRO: ESFAQUEAMENTOS', 640, 1270, f, o0 - 6, 52, -2)
    z = lerp(1.2, 1.02, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640 + 12 * math.sin(f * .03), 1000, z, 0), 'dusk'


def s6(f):
    c = cenario_praca('dusk')
    m0 = wt(6, 'motivo') - 3
    if f >= m0:
        paste_c(c, lupa().resize((260, 260)), 640 + 20 * math.sin(f * .06), 640, back(ramp(f, m0, m0 + 8)))
    num(c, 'MOTIVO?', 640, 420, f, m0, 100, -3)
    c0 = wt(6, 'condolencias') - 3
    num(c, 'CONDOLÊNCIAS', 640, 1000, f, c0, 80, 3)
    for i, x in enumerate([400, 540, 740, 880]):
        st = wt(6, 'lideres') - 3 + i * 3
        if f >= st:
            paste_c(c, vela().resize((110, 220)), x, 1440, back(ramp(f, st, st + 8)))
    num(c, 'EUROPA', 640, 850, f, wt(6, 'Europa') - 3, 80, -2)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 100))) + .0004 * f
    return c, (640, 1020, z, lerp(0, 1.2, smooth(ramp(f, 0, 100)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'seis') - 3, 140, .6)
    s.ting(s.W(1, 'tres') - 3, .2)
    s.thunk(s.W(3, 'quinze') - 3, 140, .6)
    s.thunk(s.W(4, 'detido') - 3, 160, .5)
    s.ting(s.W(5, 'raros') - 3, .2)
    s.ting(s.W(6, 'condolencias') - 3, .2)
