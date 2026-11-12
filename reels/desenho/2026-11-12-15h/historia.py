"""Um Café com o Mundo — NO SEU BOLSO (quinta 12/11/2026, 15h).
Tema: Jensen Huang renuncia ao comando da Nvidia após 33 anos; ações despencam.
Fontes (conferidas em 12/11/2026):
- Yahoo Finance (live updates, 12/11/2026): conselho anuncia na quinta 12/11 a renúncia de Huang com efeito imediato;
  CFO Colette Kress (na empresa desde 2013) é CEO interina; Huang cofundou a Nvidia em abril de 1993, CEO por 33 anos;
  balanço mantido para terça 17/11. Ações chegaram a cair ~13-14% na abertura.
- Suno Notícias (12/11/2026): queda máxima de 14,35% (US$ 148,80) pela manhã; comunicado oficial ~12h54 de Brasília;
  empresa não atribuiu oficialmente a saída; conselho diz não ter razão para crer que informação confidencial ou a
  segurança nacional dos EUA tenham sido comprometidas.
- CBS News (11/11/2026): Nvidia abriu investigação sobre Huang, anunciada em 8/11; ele admitiu caso extraconjugal.
- TV Sim Brasil / Painel Político (12/11/2026): BDR NVDC34 cai mais de 8% (10,5%) na B3.
- Tickmill (12/11/2026): bolsas da Ásia caem 0,9%, Taiex -2,6% com TSMC; futuros da Nasdaq -1%.
Personagens genéricos (sem traços de pessoas reais); sem logotipo."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'NO SEU BOLSO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "A empresa dos chips da inteligência artificial perdeu o chefe de repente, e as ações despencaram.",
    "Nesta quinta, Jensen Huang, que fundou a Nvidia em mil novecentos e noventa e três, renunciou após trinta e três anos no comando.",
    "A saída veio após uma investigação interna, aberta no dia oito, e reportagens sobre a vida pessoal dele.",
    "As ações chegaram a cair catorze por cento, e a diretora financeira, Colette Kress, virou chefe interina.",
    "Por que importa? Os chips da Nvidia movem a corrida da inteligência artificial, e o tombo mexe com as bolsas do mundo.",
    "Aqui no Brasil, o papel da Nvidia negociado na bolsa também caiu mais de oito por cento.",
    "O próximo teste é na terça, dezessete, com o balanço da empresa.",
]
CAPTXT = [
    "A empresa dos chips da inteligência artificial|perdeu o chefe de repente,|e as ações despencaram.",
    "Nesta quinta, Jensen Huang,|que fundou a Nvidia em 1993,|renunciou após 33 anos no comando.",
    "A saída veio após uma investigação interna,|aberta no dia 8,|e reportagens sobre a vida pessoal dele.",
    "As ações chegaram a cair 14%,|e a diretora financeira, Colette Kress,|virou chefe interina.",
    "Por que importa? Os chips da Nvidia|movem a corrida da inteligência artificial,|e o tombo mexe com as bolsas do mundo.",
    "Aqui no Brasil, o papel da Nvidia|negociado na bolsa também caiu mais de 8%.",
    "O próximo teste é na terça, 17,|com o balanço da empresa.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'chips', 6), (0, 'despencaram', 6), (1, 'mil', 6), (1, 'trinta', 6), (2, 'investigacao', 6), (2, 'oito', 6),
         (3, 'catorze', 6), (3, 'Kress', 8), (4, 'chips', 6), (4, 'bolsas', 6), (5, 'Brasil', 6), (5, 'oito', 6), (6, 'dezessete', 6)]

GREEN = hexc('#3aa66a'); GREEN_D = hexc('#287a4c'); RED = hexc('#d8443c'); RED_D = hexc('#a02c26')
BLUE = hexc('#2f6fd6'); BLUE_D = hexc('#1f4f9e'); GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e')
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); WHITE = (255, 255, 255)


# ------------------------------------------------------------------ desenhos novos
def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def politico(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550', bun=False):
    """pessoa genérica de terno. 600x1000, pés y~975."""
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(suit); P.COAT_D = mul(hexc(suit), .7)
    try:
        img = P.scientist(expr=expr, arms=arms if arms != 'clip' else 'hang', blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False, bun=bun)
    finally:
        P.COAT, P.COAT_D = oc, od
    p = Pen(600, 1000); p.img = img; p.d = ImageDraw.Draw(img)
    p.poly([(270, 418), (330, 418), (300, 470)], WHITE, 3)
    if tie: p.shape([(290, 430), (310, 430), (318, 540), (300, 566), (282, 540)], hexc(tie), mul(hexc(tie), .75), 3, 3)
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


# ------------------------------------------------------------------ desenhos novos (12/11)
@lru_cache(maxsize=2)
def chip():
    """chip genérico (sem marca). 600x600"""
    p = Pen(600, 600)
    for i in range(6):
        o = 130 + i * 68
        for (x0, y0, x1, y1) in ((o - 14, 20, o + 14, 110), (o - 14, 490, o + 14, 580), (20, o - 14, 110, o + 14), (490, o - 14, 580, o + 14)):
            p.shape([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], GOLD, GOLD_D, 4, 3)
    p.shape([(90, 90), (510, 90), (510, 510), (90, 510)], hexc('#2e3138'), hexc('#1c1e23'), 7, 16)
    p.shape([(170, 170), (430, 170), (430, 430), (170, 430)], GREEN, GREEN_D, 6, 10)
    for k in range(3):
        y = 220 + k * 80
        p.stroke([(200, y), (400, y)], 6, hexc('#a8e6be'))
    return fin(p)


@lru_cache(maxsize=2)
def sede():
    """prédio de escritórios de vidro genérico. 700x1000, base y~990"""
    p = Pen(700, 1000)
    p.shape([(80, 120), (620, 120), (620, 990), (80, 990)], hexc('#8fb8d0'), hexc('#5f8aa6'), 7, 18)
    for r in range(9):
        for k in range(5):
            x, y = 120 + k * 100, 160 + r * 90
            p.poly([(x, y), (x + 70, y), (x + 70, y + 60), (x, y + 60)], hexc('#c9e6f5') if (r + k) % 3 else hexc('#e8f6fc'))
    p.shape([(280, 860), (420, 860), (420, 990), (280, 990)], hexc('#3a3a44'), hexc('#24242c'), 5, 4)
    p.shape([(60, 90), (640, 90), (640, 130), (60, 130)], hexc('#6b7a8a'), hexc('#4a5664'), 5, 4)
    return fin(p)


@lru_cache(maxsize=2)
def lupa():
    p = Pen(400, 400)
    p.stroke([(250, 250), (370, 370)], 34, hexc('#6b4a2e'))
    p.shape(ell_pts(170, 170, 130, 130, 40), hexc('#c9e6f5'), hexc('#8fb8d0'), 10, 6)
    return fin(p)


@lru_cache(maxsize=2)
def pasta():
    """pasta de documentos. 460x360"""
    p = Pen(460, 360)
    p.shape([(20, 40), (190, 40), (220, 80), (440, 80), (440, 340), (20, 340)], hexc('#e0a84a'), hexc('#b07e2a'), 6, 10)
    p.shape([(50, 110), (410, 110), (410, 330), (50, 330)], WHITE, hexc('#c9c9d2'), 5, 4)
    for y in range(150, 320, 40): p.stroke([(80, y), (380, y)], 5, hexc('#9aa3b0'))
    return fin(p)


@lru_cache(maxsize=2)
def cadeira():
    """cadeira vazia de chefe. 300x520"""
    p = Pen(300, 520)
    p.shape([(50, 20), (250, 20), (250, 300), (50, 300)], hexc('#3a3a44'), hexc('#24242c'), 6, 10)
    p.shape([(30, 290), (270, 290), (270, 340), (30, 340)], hexc('#4a4a55'), hexc('#2e2e36'), 6, 6)
    p.stroke([(60, 340), (50, 510)], 12); p.stroke([(240, 340), (250, 510)], 12)
    return fin(p)


def queda(c, x0, y0, w, h, f, f0, dur=40):
    """linha de ações caindo, desenhada aos poucos."""
    if f < f0: return
    d = ImageDraw.Draw(c)
    d.rectangle([x0 - 20, y0 - h - 20, x0 + w + 20, y0 + 20], fill=(255, 255, 255), outline=INK, width=6)
    vals = [.80, .84, .78, .82, .76, .70, .72, .55, .40, .12]
    t = easeOut(ramp(f, f0, f0 + dur))
    n = max(2, int(2 + t * (len(vals) - 2)))
    pts = [(x0 + w * i / (len(vals) - 1), y0 - h * v) for i, v in enumerate(vals[:n])]
    d.line([(px + 5, py + 5) for px, py in pts], fill=INK, width=16)
    d.line(pts, fill=RED, width=12)
    px, py = pts[-1]
    d.ellipse([px - 16, py - 16, px + 16, py + 16], fill=RED, outline=INK, width=5)


def chip_voando(c, x0, y0, x1, y1, t, w=140, rot=0):
    if t <= 0 or t >= 1: return
    im = chip().resize((w, w)).rotate(rot + 25 * math.sin(t * 6), expand=True, resample=Image.BICUBIC)
    paste_c(c, im, lerp(x0, x1, t), lerp(y0, y1, t) - 200 * math.sin(t * math.pi), 1)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('escritorio', 'day').copy()
    c0 = wt(0, 'chips') - 3
    d0 = wt(0, 'despencaram') - 3
    s = back(ramp(f, c0 - 6, c0 + 6))
    paste_c(c, chip().resize((460, 460)).rotate(-6 + 3 * math.sin(f * .1), expand=True, resample=Image.BICUBIC), 640, 760 - 20 * math.sin(f * .1), max(s, 0.03) if f >= c0 - 6 else 0)
    num(c, 'INTELIGÊNCIA ARTIFICIAL', 640, 420, f, wt(0, 'inteligencia') - 3, 62, -3)
    p0 = wt(0, 'chefe') - 3
    if f >= p0:
        paste_c(c, cadeira().resize((240, 416)), 330, 1340, back(ramp(f, p0, p0 + 8)))
        num(c, 'SEM CHEFE', 400, 1090, f, p0 + 2, 68, 4)
    num(c, 'AÇÕES', 780, 900, f, d0, 96, -3)
    seta(c, 780, 1080, 220, up=False, col=RED, s=back(ramp(f, d0, d0 + 10)))
    put_pol(c, 1030, 1640, 460, f, 3, skin=2, hair='#2a221e', tie='#2f6fd6', suit='#4a4f63',
            expr='shock' if f > d0 else 'neutral', arms='up' if f > d0 + 3 else 'hang', look=-1)
    z = lerp(1.35, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, d0)
    return c, (640, 1040 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('cidade', 'day').copy()
    paste_c(c, sede().resize((560, 800)), 420, 1110, 1)
    num(c, 'QUINTA, 12/11', 640, 360, f, 0, 90, -3)
    num(c, 'FUNDOU EM 1993', 760, 560, f, wt(1, 'mil') - 3, 76, 3)
    t0 = wt(1, 'trinta') - 3
    num(c, '33 ANOS', 800, 760, f, t0, 140, -4)
    num(c, 'NO COMANDO', 800, 900, f, t0 + 4, 76, 3)
    r0 = wt(1, 'renunciou') - 3
    # executivo genérico sai do prédio, de pasta na mão
    x = 430 + 520 * smooth(ramp(f, r0, r0 + 60))
    put_pol(c, x, 1600, 470, f, 5, skin=1, hair='#2a2a2a', tie='#d8443c', suit='#2c2c34',
            expr='neutral' if f < r0 else 'stern', arms='hang', look=1)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, t0, .7)
    return c, (640 + 30 * t, lerp(1080, 1020, t) + k * 8, lerp(1.06, 1.12, t) * (1 + .0006 * f), k), 'day'


def s2(f):
    c = CEN('escritorio', 'golden').copy()
    i0 = wt(2, 'investigacao') - 3
    paste_c(c, pasta().resize((520, 407)), 560, 1000, back(ramp(f, i0 - 4, i0 + 6)))
    num(c, 'INVESTIGAÇÃO INTERNA', 640, 420, f, i0, 66, -3)
    if f >= i0 + 4:
        a = (f - i0) * .07
        paste_c(c, lupa().resize((300, 300)), 600 + 140 * math.sin(a), 960 + 60 * math.cos(a * 1.3), back(ramp(f, i0 + 4, i0 + 12)))
    o0 = wt(2, 'oito') - 3
    paste_c(c, calendario().resize((300, 312)), 980, 700, back(ramp(f, o0 - 2, o0 + 6)) if f >= o0 - 2 else 0)
    num(c, 'DIA 8', 980, 760, f, o0, 100, 3)
    r0 = wt(2, 'reportagens') - 3
    if f >= r0:
        for i in range(3):
            st = r0 + i * 5
            if f >= st:
                paste_c(c, txt('NOTÍCIA', 60, (-8, 6, -3)[i]), (250, 640, 1010)[i], (1250, 1330, 1250)[i], back(ramp(f, st, st + 8)))
    t = smooth(ramp(f, 0, 150))
    k = kick(f, o0, .5)
    return c, (640 + 15 * math.sin(f * .03), lerp(980, 1040, t) + k * 6, lerp(1.04, 1.1, t) * (1 + .0004 * f), lerp(0, 2, t) + k), 'golden'


def s3(f):
    c = CEN('escritorio', 'dusk').copy()
    q0 = wt(3, 'catorze') - 3
    queda(c, 200, 1000, 640, 440, f, 0, max(16, q0))
    num(c, '-14%', 520, 720, f, q0, 180, -4)
    num(c, 'NA QUINTA DE MANHÃ', 560, 470, f, q0 + 6, 56, 3)
    k0 = wt(3, 'Kress') - 3
    d0 = wt(3, 'diretora') - 3
    if f >= d0 - 4:
        x = 1300 - 320 * easeOut(ramp(f, d0 - 4, d0 + 14))
        put_pol(c, x, 1600, 520, f, 8, skin=0, hair='#c9a46a', tie=None, suit='#5a3a6a', bun=True,
                expr='neutral' if f < k0 else 'proud', arms='hang' if f < k0 + 6 else 'point', look=-1)
    num(c, 'CEO INTERINA', 760, 1180, f, wt(3, 'interina') - 3, 84, -3)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, q0, .9)
    return c, (lerp(560, 700, smooth(ramp(f, d0 - 10, d0 + 20))), 1020 + k * 8, lerp(1.12, 1.04, t) * (1 + .0005 * f), k), 'dusk'


def s4(f):
    c = CEN('mapa', 'dusk').copy()
    c0 = wt(4, 'chips') - 3
    paste_c(c, chip().resize((300, 300)).rotate(4 * math.sin(f * .08), expand=True, resample=Image.BICUBIC), 640, 860, back(ramp(f, c0 - 4, c0 + 6)) if f >= c0 - 4 else 0)
    num(c, 'CORRIDA DA IA', 640, 470, f, wt(4, 'corrida') - 3, 110, -3)
    b0 = wt(4, 'bolsas') - 3
    for i, (x, y, lab) in enumerate(((340, 640, 'EUA'), (920, 640, 'ÁSIA'), (640, 1150, 'EUROPA'))):
        st = b0 + i * 4
        if f >= st:
            num(c, lab, x, y, f, st, 76, (-4, 4, -2)[i])
            seta(c, x, y + 170, 150, up=False, col=RED, s=back(ramp(f, st, st + 8)))
    m0 = wt(4, 'inteligencia') - 3
    for i in range(6):
        st = m0 + i * 4
        t = (f - st) / 34
        if t > 0 and f < b0: chip_voando(c, 640, 860, (250, 1050, 900, 350, 1000, 600)[i], (700, 640, 1250, 1200, 1000, 600)[i], min(t, .99), 100, i * 30)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, b0, .7)
    return c, (640 + 20 * math.sin(f * .03), lerp(980, 1050, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0004 * f), lerp(0, -1.5, t) + k), 'dusk'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    num(c, 'BRASIL', 640, 380, f, wt(5, 'Brasil') - 3, 120, -3)
    queda(c, 220, 1050, 560, 380, f, 4, 40)
    num(c, 'BDR NA B3', 500, 560, f, wt(5, 'bolsa') - 3, 90, 3)
    o0 = wt(5, 'oito') - 3
    num(c, '-8%', 500, 800, f, o0, 170, -4)
    num(c, 'MAIS DE', 500, 680, f, wt(5, 'mais') - 3, 70, 3)
    put_pol(c, 1000, 1640, 520, f, 4, skin=1, hair='#6b4a2a', tie='#3aa66a', suit='#3a3a44',
            expr='nervous' if f > o0 else 'neutral', arms='cheek' if f > o0 else 'point', look=-1)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, o0, .8)
    return c, (620, lerp(960, 1020, t) + k * 8, lerp(1.18, 1.05, t) * (1 + .0005 * f), k), 'dusk'


def s6(f):
    c = CEN('escritorio', 'dusk').copy()
    paste_c(c, calendario(), 520, 900, back(ramp(f, 0, 8)))
    num(c, 'TERÇA', 520, 700, f, wt(6, 'terca') - 3, 100, -3)
    num(c, '17', 520, 960, f, wt(6, 'dezessete') - 3, 190, 3)
    num(c, 'BALANÇO', 520, 1230, f, wt(6, 'balanco') - 3, 100, -2)
    put_pol(c, 980, 1660, 680, f, 7, skin=2, hair='#3a2a20', tie='#2f6fd6', suit='#2c3550', expr='neutral', arms='point', look=-1)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 70))) + .0006 * f
    return c, (640, 1050, z, lerp(0, 1.5, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'chips') - 3, 160, .7)
    s.thunk(s.W(0, 'despencaram') - 3, 120, 1.0)
    s.ting(s.W(1, 'mil') - 3, .3)
    s.thunk(s.W(1, 'trinta') - 3, 150, .8)
    s.thunk(s.W(2, 'investigacao') - 3, 200, .5)
    s.ting(s.W(2, 'oito') - 3, .3)
    s.thunk(s.W(3, 'catorze') - 3, 130, 1.0)
    s.whoosh(s.W(3, 'diretora') - 3, .3, .5)
    s.thunk(s.W(4, 'bolsas') - 3, 150, .8)
    s.thunk(s.W(5, 'oito') - 3, 140, .9)
    s.ting(s.W(6, 'dezessete') - 3, .3)
