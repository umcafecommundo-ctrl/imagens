"""Um Café com o Mundo — NO SEU BOLSO (segunda 09/11/2026, 10h).
Tema: China prorroga por mais 2 meses a suspensão da tarifa extra de 24% sobre produtos dos EUA (trégua até janeiro) e o elo com a soja do Brasil.
Fontes (conferidas em 09/11/2026):
- Bloomberg (via Yahoo Finance), 08-09/11/2026: China suspende a tarifa adicional de 24% sobre produtos dos EUA por mais dois meses,
  formalizando a extensão da trégua até janeiro; vale a partir de terça (10/11) às 13h01 de Pequim; tarifa geral de 10% continua;
  trégua acertada em Busan (out/2025), estendida em setembro até 10/01; Trump e Xi devem se encontrar na APEC em Shenzhen ainda
  este mês (3ª cúpula do ano); o representante comercial dos EUA cobrou "ações concretas" em compras agrícolas e terras raras.
- The Tribune / ANI (Pequim), 09/11/2026: 24% suspensa por dois meses, 10% mantida, vigência 10/11 às 13h01; Ministério das Finanças.
Elo com o Brasil: mecanismo geral (China é a maior compradora da soja brasileira; mais compra agrícola dos EUA = concorrência).
Sem previsão de preço. Personagens genéricos, sem logotipos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'NO SEU BOLSO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "A guerra das tarifas entre Estados Unidos e China foi adiada, e isso mexe com a soja do Brasil.",
    "Nesta terça, a China estende por mais dois meses a pausa de uma taxa extra de vinte e quatro por cento sobre produtos americanos.",
    "A taxa de dez por cento continua, e a trégua vai até janeiro.",
    "Em troca, os americanos cobram que a China compre mais da agricultura deles.",
    "E aí entra o Brasil: a China é a maior compradora da nossa soja, e mais soja americana lá é concorrência pro nosso agro.",
    "Ainda este mês, os dois presidentes devem se encontrar de novo.",
]
CAPTXT = [
    "A guerra das tarifas entre EUA e China|foi adiada, e isso mexe|com a soja do Brasil.",
    "Nesta terça, a China estende por mais 2 meses|a pausa de uma taxa extra de 24%|sobre produtos americanos.",
    "A taxa de 10% continua,|e a trégua vai até janeiro.",
    "Em troca, os americanos cobram que a China|compre mais da agricultura deles.",
    "E aí entra o Brasil: a China é a maior compradora|da nossa soja, e mais soja americana lá|é concorrência pro nosso agro.",
    "Ainda este mês, os dois presidentes|devem se encontrar de novo.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'adiada', 6), (0, 'soja', 6), (1, 'dois', 6), (1, 'vinte', 6), (2, 'dez', 6), (2, 'janeiro', 4),
         (3, 'agricultura', 4), (4, 'Brasil', 4), (4, 'maior', 4), (4, 'concorrencia', 4), (5, 'encontrar', 4)]

GREEN = hexc('#3aa66a'); GREEN_D = hexc('#287a4c'); RED = hexc('#d8443c'); RED_D = hexc('#a02c26')
GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e'); WHITE = (255, 255, 255)
YEL = hexc('#f6d33c'); BLUEB = hexc('#2a4fa8'); CNR = hexc('#de2910'); USB = hexc('#2b3d7a'); USR = hexc('#c8323c')
SACO = hexc('#d9b77a'); SACO_D = hexc('#a8864e'); SOY = hexc('#e8c95a'); SOY_D = hexc('#b8962e')


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


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ objetos
@lru_cache(maxsize=2)
def bandeira_br():
    p = Pen(600, 420)
    p.poly([(10, 10), (590, 10), (590, 410), (10, 410)], GREEN)
    p.poly([(300, 45), (555, 210), (300, 375), (45, 210)], YEL)
    p.dot(300, 210, 105, BLUEB)
    p.stroke(curve((200, 190), (300, 170), (400, 230), 10), 10, WHITE)
    p.stroke([(10, 10), (590, 10), (590, 410), (10, 410), (10, 10)], 6)
    return fin(p)


def _estrela(cx, cy, r, rot=0.0):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + rot + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .4
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


@lru_cache(maxsize=2)
def bandeira_cn():
    """bandeira da China (país): vermelha, estrela grande e 4 pequenas amarelas. 600x420"""
    p = Pen(600, 420)
    p.poly([(10, 10), (590, 10), (590, 410), (10, 410)], CNR)
    p.poly(_estrela(110, 115, 62), YEL)
    for (x, y, r) in ((215, 50, 22), (255, 95, 22), (255, 155, 22), (215, 200, 22)):
        p.poly(_estrela(x, y, r, .4), YEL)
    p.stroke([(10, 10), (590, 10), (590, 410), (10, 410), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_us():
    """bandeira dos EUA (país), simplificada: listras e canto azul com estrelinhas. 600x420"""
    p = Pen(600, 420)
    hh = 400 / 13
    for i in range(13):
        p.poly([(10, 10 + i * hh), (590, 10 + i * hh), (590, 10 + (i + 1) * hh), (10, 10 + (i + 1) * hh)], USR if i % 2 == 0 else WHITE)
    p.poly([(10, 10), (260, 10), (260, 10 + 7 * hh), (10, 10 + 7 * hh)], USB)
    for r in range(5):
        for k in range(6):
            x = 32 + k * 40 + (20 if r % 2 else 0)
            if x > 245: continue
            p.poly(_estrela(x, 34 + r * 41, 11), WHITE)
    p.stroke([(10, 10), (590, 10), (590, 410), (10, 410), (10, 10)], 6)
    return fin(p)


def put_band(c, im, x, y, w, f, s=1.0):
    if s <= .02: return
    ww = int(w * s); hh = int(w * .7 * s)
    im = im.resize((ww, hh)).rotate(3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    d = ImageDraw.Draw(c)
    d.line([(x - ww / 2 - 4, y - hh / 2), (x - ww / 2 - 4, y + hh * 1.7)], fill=INK, width=10)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=4)
def saco(cor=0):
    """saco de grãos de soja aberto em cima. 360x420"""
    p = Pen(360, 420)
    base = SACO if cor == 0 else hexc('#c9b08a')
    p.shape([(60, 80), (300, 80), (330, 220), (320, 400), (40, 400), (30, 220)], base, mul(base, .75), 6, 12)
    p.shape(ell_pts(180, 86, 122, 34, 30), SOY, SOY_D, 5, 4)
    for (x, y) in ((140, 76), (180, 70), (215, 82), (160, 96), (200, 96), (120, 92), (240, 92)):
        p.dot(x, y, 13, SOY, 3)
    p.shape(ell_pts(180, 260, 90, 60, 30), WHITE, hexc('#d8d2c4'), 4, 3)
    for (x, y) in ((150, 255), (180, 245), (210, 262)):
        p.dot(x, y, 16, SOY, 3)
    return fin(p)


def put_saco(c, x, y, w, s=1.0, cor=0):
    if s <= .02: return
    im = saco(cor).resize((max(2, int(w * s)), max(2, int(w * 420 / 360 * s))))
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=2)
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


@lru_cache(maxsize=2)
def carimbo():
    """carimbo vermelho redondo 'PAUSA' (só a moldura; o texto vem com txt). 420x420"""
    p = Pen(420, 420)
    p.stroke(ell_pts(210, 210, 190, 190, 60) + [ell_pts(210, 210, 190, 190, 60)[0]], 18, RED)
    p.stroke(ell_pts(210, 210, 160, 160, 60) + [ell_pts(210, 210, 160, 160, 60)[0]], 8, RED)
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


# ------------------------------------------------------------------ cenas
# s0 cidade (dois países frente a frente) | s1 porto/mar (navio com produtos americanos) | s2 escritório (10% + calendário)
# s3 pasto/fazenda (sacos de grãos, negociador cobra) | s4 pasto (Brasil, soja indo para a China) | s5 escritório dusk (encontro)
def s0(f):
    c = CEN('cidade', 'day').copy()
    a0 = wt(0, 'adiada') - 3
    put_band(c, bandeira_us(), 330, 520, 330, f, back(ramp(f, 0, 8)))
    put_band(c, bandeira_cn(), 930, 520, 330, f + 7, back(ramp(f, 3, 11)))
    t = smooth(ramp(f, 0, 30))
    put_pol(c, lerp(150, 330, t), 1600, 560, f, 4, skin=0, hair='#9a8a7a', tie='#d8443c', suit='#2c3550',
            expr='stern' if f < a0 else 'neutral', arms='point' if f < a0 else 'hang', look=1)
    put_pol(c, lerp(1110, 930, t), 1600, 560, f, 8, skin=1, hair='#1f1a18', tie='#c8323c', suit='#3a3a44',
            expr='stern' if f < a0 else 'neutral', arms='point' if f < a0 else 'hang', look=-1)
    num(c, 'TARIFAS', 640, 330, f, wt(0, 'tarifas') - 3, 110, -3)
    num(c, 'ADIADA!', 640, 830, f, a0, 150, 4)
    s0_ = wt(0, 'soja') - 3
    put_saco(c, 640, 1250, 260, back(ramp(f, s0_, s0_ + 8)) if f >= s0_ else 0)
    num(c, 'E A SOJA DO BRASIL?', 640, 985, f, s0_, 70, -2)
    z = lerp(1.35, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0005 * f)
    k = kick(f, a0 + 3)
    return c, (640, 1040 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('mapa', 'day').copy()
    carg(c, lerp(250, 950, ramp(f, 0, 170)), 1150, 380, f * .2)
    put_band(c, bandeira_us(), 240, 560, 200, f, back(ramp(f, 0, 8)))
    put_band(c, bandeira_cn(), 1020, 560, 200, f + 5, back(ramp(f, 4, 12)))
    d0 = wt(1, 'dois') - 3
    v0 = wt(1, 'vinte') - 3
    num(c, '+2 MESES', 640, 380, f, d0, 120, -3)
    num(c, '24%', 640, 720, f, v0, 230, 4)
    if f >= v0 + 10:
        s = back(ramp(f, v0 + 10, v0 + 18))
        paste_c(c, carimbo().resize((int(400 * s) + 2, int(400 * s) + 2)), 640, 720, 1)
        num(c, 'PAUSADA', 640, 900, f, v0 + 12, 90, -6)
    num(c, 'PRODUTOS DOS EUA', 640, 1420, f, wt(1, 'produtos') - 3, 66, 2)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, v0, .7)
    return c, (640, lerp(980, 1040, t) + k * 8, lerp(1.18, 1.04, t) * (1 + .0004 * f), k), 'day'


def s2(f):
    c = CEN('escritorio', 'day').copy()
    d0 = wt(2, 'dez') - 3
    num(c, '10%', 360, 560, f, d0, 230, -4)
    num(c, 'CONTINUA', 360, 760, f, wt(2, 'continua') - 3, 90, 3)
    j0 = wt(2, 'janeiro') - 3
    paste_c(c, calendario().resize((380, 395)), 880, 1080, back(ramp(f, 2, 10)))
    num(c, 'TRÉGUA ATÉ', 880, 820, f, wt(2, 'tregua') - 3, 70, -3)
    num(c, 'JANEIRO', 880, 1120, f, j0, 90, -5)
    put_pol(c, 360, 1620, 520, f, 5, skin=2, hair='#2a221e', tie='#2f6fd6', suit='#4a4f63',
            expr='neutral', arms='point' if f > d0 else 'hang', look=1)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) + .0004 * f
    return c, (640 + 15 * math.sin(f * .04), 1030, z, .8 * math.sin(f * .03)), 'day'


def s3(f):
    c = CEN('pasto', 'day').copy()
    a0 = wt(3, 'agricultura') - 3
    for i, x in enumerate((700, 900, 1100)):
        put_saco(c, x, 1420, 220, back(ramp(f, a0 + i * 3, a0 + i * 3 + 8)) if f >= a0 + i * 3 else 0, cor=1)
    put_band(c, bandeira_us(), 900, 860, 230, f, back(ramp(f, a0, a0 + 8)) if f >= a0 else 0)
    put_pol(c, 330, 1620, 600, f, 4, skin=0, hair='#9a8a7a', tie='#d8443c', suit='#2c3550',
            expr='stern', arms='point' if f > wt(3, 'cobram') - 3 else 'hang', look=1)
    num(c, 'COMPRE MAIS!', 640, 420, f, wt(3, 'compre') - 3, 120, -4)
    num(c, 'GRÃOS DOS EUA', 900, 600, f, a0 + 4, 70, 3)
    t = smooth(ramp(f, 0, 100))
    return c, (lerp(560, 700, t), 1050, lerp(1.05, 1.15, t), lerp(-1, 1, t)), 'day'


def s4(f):
    c = CEN('pasto', 'golden').copy()
    b0 = wt(4, 'Brasil') - 3
    m0 = wt(4, 'maior') - 3
    co0 = wt(4, 'concorrencia') - 3
    put_band(c, bandeira_br(), 300, 520, 260, f, back(ramp(f, b0, b0 + 8)) if f >= b0 else 0)
    put_band(c, bandeira_cn(), 960, 520, 260, f + 4, back(ramp(f, m0, m0 + 8)) if f >= m0 else 0)
    num(c, 'MAIOR COMPRADORA', 790, 820, f, m0, 62, 3)
    num(c, 'DA NOSSA SOJA', 790, 900, f, m0 + 4, 62, -2)
    # sacos de soja do Brasil indo para a China
    for i in range(3):
        tt = ((f - m0) * .012 + i * .33) % 1 if f >= m0 else 0
        if f >= m0:
            put_saco(c, lerp(330, 930, tt), 1180 - 120 * math.sin(tt * math.pi), 150, 1)
    put_saco(c, 320, 1400, 230, back(ramp(f, b0 + 3, b0 + 11)) if f >= b0 + 3 else 0)
    if f >= co0:
        put_saco(c, 980, 1400, 230, back(ramp(f, co0, co0 + 8)), cor=1)
        put_band(c, bandeira_us(), 1080, 1180, 140, f, back(ramp(f, co0, co0 + 8)))
        num(c, 'CONCORRÊNCIA!', 640, 380, f, co0, 110, -4)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, co0, .8)
    return c, (640, 1020 + k * 6, z, k), 'golden'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    put_band(c, bandeira_us(), 330, 470, 230, f, back(ramp(f, 0, 8)))
    put_band(c, bandeira_cn(), 950, 470, 230, f + 6, back(ramp(f, 2, 10)))
    e0 = wt(5, 'encontrar') - 3
    t = smooth(ramp(f, e0 - 14, e0 + 10))
    put_pol(c, lerp(200, 470, t), 1620, 560, f, 4, skin=0, hair='#9a8a7a', tie='#d8443c', suit='#2c3550',
            expr='neutral', arms='point' if f > e0 else 'hang', look=1)
    put_pol(c, lerp(1080, 810, t), 1620, 560, f, 8, skin=1, hair='#1f1a18', tie='#c8323c', suit='#3a3a44',
            expr='neutral', arms='point' if f > e0 else 'hang', look=-1)
    num(c, 'AINDA ESTE MÊS', 640, 700, f, wt(5, 'mes') - 3, 90, -3)
    num(c, 'NOVO ENCONTRO', 640, 820, f, e0, 90, 3)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 70))) + .0004 * f
    return c, (640, 1050, z, lerp(0, 1.5, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    s.thunk(s.W(0, 'adiada') - 3, 140, .9)
    s.ting(s.W(0, 'soja') - 3, .3)
    s.whoosh(s.W(1, 'dois') - 3, .3, .5)
    s.thunk(s.W(1, 'vinte') - 3, 180, .8)
    s.thunk(s.W(2, 'dez') - 3, 200, .6)
    s.ting(s.W(2, 'janeiro') - 3, .3)
    s.ting(s.W(4, 'Brasil') - 3, .3)
    s.thunk(s.W(4, 'concorrencia') - 3, 140, .9)
    s.ting(s.W(5, 'encontrar') - 3, .3)
