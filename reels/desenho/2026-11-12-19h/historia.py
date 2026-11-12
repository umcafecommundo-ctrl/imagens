"""Um Café com o Mundo — O MUNDO EXPLICADO (quinta 12/11/2026, 19h).
Tema: vice-presidente da Indonésia, Gibran Rakabuming Raka, renuncia por causa da disputa sobre o diploma do ensino médio.
Fontes (conferidas em 12/11/2026):
- Al Jazeera, 12/11/2026 "Indonesia vice president resigns amid dispute over eligibility": renúncia entregue na quinta 12/11
  a Prabowo e ao Parlamento; Prabowo aceitou "com o coração pesado"; Gibran tem 39 anos, filho mais velho do ex-presidente
  Joko Widodo; deixa o cargo após 2 dos 5 anos do mandato; Corte Constitucional e Suprema Corte decidiram em outubro que os
  documentos de educação não cumpriam as exigências eleitorais; na quarta 11/11, 120 deputados de 8 partidos pediram o
  início de um processo que pode levar ao impeachment; a Assembleia Consultiva do Povo (MPR) escolhe o substituto em até
  60 dias entre 2 nomes indicados pelo presidente; não há nova eleição.
- ABC News (Austrália), 12/11/2026: Corte Constitucional não achou "prova convincente" de que ele tinha diploma do ensino
  médio, exigido por lei para concorrer; Suprema Corte considerou inválido um certificado de equivalência; renúncia veio
  horas antes de a Câmara se reunir sobre a petição de mais de 120 políticos; aliança entre Jokowi e Prabowo estremecida.
- Channel News Asia (via resumo Open Chronicle, 12/11/2026).
Indonésia = 4º país mais populoso do mundo. Personagens genéricos (sem traços de pessoas reais). Tom neutro."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O vice-presidente da Indonésia renunciou nesta quinta, por causa de um diploma do ensino médio.",
    "Gibran Rakabuming Raka tem trinta e nove anos e é filho do ex-presidente Joko Widodo.",
    "Em outubro, a Corte Constitucional não viu prova de que ele tinha o diploma, exigido por lei pra se candidatar.",
    "E a Suprema Corte disse que o certificado de equivalência dele não valia.",
    "Na quarta, cento e vinte deputados de oito partidos pediram o impeachment. Ele saiu horas antes da reunião.",
    "Por que importa? A Indonésia é o quarto país mais populoso do mundo, e ele deixa o cargo com só dois dos cinco anos de mandato.",
    "Agora, o Congresso tem até sessenta dias pra escolher o novo vice, entre dois nomes do presidente.",
]
CAPTXT = [
    "O vice-presidente da Indonésia renunciou nesta quinta,|por causa de um diploma do ensino médio.",
    "Gibran Rakabuming Raka tem 39 anos|e é filho do ex-presidente Joko Widodo.",
    "Em outubro, a Corte Constitucional não viu prova|de que ele tinha o diploma,|exigido por lei pra se candidatar.",
    "E a Suprema Corte disse que o certificado|de equivalência dele não valia.",
    "Na quarta, 120 deputados de 8 partidos|pediram o impeachment.|Ele saiu horas antes da reunião.",
    "Por que importa? A Indonésia é o 4º país|mais populoso do mundo, e ele deixa o cargo|com só 2 dos 5 anos de mandato.",
    "Agora, o Congresso tem até 60 dias|pra escolher o novo vice,|entre 2 nomes do presidente.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Indonesia', 6), (0, 'diploma', 6), (1, 'trinta', 6), (1, 'Widodo', 6), (2, 'Constitucional', 6), (2, 'diploma', 6),
         (3, 'Suprema', 6), (3, 'valia', 6), (4, 'cento', 6), (4, 'impeachment', 6), (4, 'horas', 6), (5, 'quarto', 6),
         (5, 'dois', 6), (6, 'sessenta', 6), (6, 'dois', 6)]

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




# ------------------------------------------------------------------ desenhos novos (12/11 19h)
@lru_cache(maxsize=2)
def bandeira_id():
    """bandeira da Indonésia (país): vermelho em cima, branco embaixo. 600x400"""
    p = Pen(600, 400)
    p.poly([(10, 10), (590, 10), (590, 200), (10, 200)], RED)
    p.poly([(10, 200), (590, 200), (590, 390), (10, 390)], WHITE)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=4)
def diploma(ok=True):
    """diploma enrolado com fita. 560x300"""
    p = Pen(560, 300)
    p.shape([(60, 60), (500, 60), (500, 240), (60, 240)], hexc('#f6f1e4'), hexc('#cfc6b2'), 6, 8)
    p.shape(ell_pts(60, 150, 40, 95, 30), hexc('#efe7d4'), hexc('#cfc6b2'), 6, 4)
    p.shape(ell_pts(500, 150, 40, 95, 30), hexc('#efe7d4'), hexc('#cfc6b2'), 6, 4)
    p.shape([(250, 60), (310, 60), (310, 240), (250, 240)], RED, RED_D, 4, 3)
    p.shape([(262, 230), (298, 230), (310, 295), (280, 270), (250, 295)], RED, RED_D, 4, 3)
    p.dot(280, 150, 34, GOLD, 5)
    return fin(p)


def xis(c, x, y, size, s):
    if s <= .02: return
    d = ImageDraw.Draw(c)
    r = size * s / 2
    for a, b in (((x - r, y - r), (x + r, y + r)), ((x + r, y - r), (x - r, y + r))):
        d.line([(a[0] + 8, a[1] + 8), (b[0] + 8, b[1] + 8)], fill=INK, width=int(46 * s))
        d.line([a, b], fill=RED, width=int(34 * s))


def interroga(c, x, y, f, f0, size=220):
    if f >= f0: paste_c(c, txt('?', size, 8 * math.sin(f * .1)), x, y + 10 * math.sin(f * .15), back(ramp(f, f0, f0 + 8)))


def multidao(c, x0, x1, feet, h, n, f, f0, seed=0):
    """fileira de deputados genéricos surgindo um a um."""
    for i in range(n):
        st = f0 + i * 2
        if f < st: continue
        x = lerp(x0, x1, i / max(1, n - 1))
        suits = ('#2c3550', '#3a3a44', '#4a4f63', '#2c2c34', '#5a3a6a')
        ties = ('#d8443c', '#2f6fd6', '#3aa66a', '#f0c541', None)
        put_pol(c, x, feet + (i % 2) * 30, h, f, seed + i, skin=(i * 7) % 3, hair=('#2a221e', '#3a2a20', '#1c1c1c')[i % 3],
                tie=ties[i % 5], suit=suits[(i * 3) % 5], bun=(i % 4 == 1), expr='stern', arms='point' if i % 3 == 0 else 'hang', look=(-1 if x > 640 else 1))


# ------------------------------------------------------------------ cenas
def s0(f):
    """gancho: palácio, bandeira, vice sai; diploma com X."""
    c = CEN('cidade', 'day').copy()
    paste_c(c, banco().resize((760, 578)), 640, 1120, 1)
    put_band(c, bandeira_id(), 640, 560, 220, f, back(ramp(f, 0, 8)), pole=False)
    num(c, 'INDONÉSIA', 640, 380, f, max(0, wt(0, 'Indonesia') - 3), 100, -3)
    r0 = wt(0, 'renunciou') - 3
    x = 520 + 520 * smooth(ramp(f, r0, r0 + 70))
    put_pol(c, x, 1600, 470, f, 5, skin=1, hair='#1c1c1c', tie='#d8443c', suit='#2c2c34',
            expr='neutral' if f < r0 else 'stern', arms='hang', look=1)
    num(c, 'RENUNCIOU', 640, 800, f, r0, 120, 4)
    d0 = wt(0, 'diploma') - 3
    if f >= d0:
        paste_c(c, diploma().resize((420, 225)).rotate(-6 + 3 * math.sin(f * .1), expand=True, resample=Image.BICUBIC), 400, 1080, back(ramp(f, d0, d0 + 8)))
        num(c, 'ENSINO MÉDIO', 400, 1260, f, wt(0, 'ensino') - 3, 72, -3)
        xis(c, 400, 1080, 260, back(ramp(f, d0 + 8, d0 + 16)))
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, d0 + 8, .8)
    return c, (640, 1020 + k * 8, z, k), 'day'


def s1(f):
    """quem: vice jovem e o pai, ex-presidente."""
    c = CEN('escritorio', 'day').copy()
    num(c, 'GIBRAN RAKABUMING RAKA', 640, 380, f, 0, 62, -2)
    t0 = wt(1, 'trinta') - 3
    num(c, '39 ANOS', 480, 600, f, t0, 120, -4)
    put_pol(c, 470, 1600, 600, f, 2, skin=1, hair='#1c1c1c', tie='#d8443c', suit='#2c2c34', expr='neutral', arms='hang', look=1)
    p0 = wt(1, 'filho') - 3
    if f >= p0 - 4:
        x = lerp(1400, 830, easeOut(ramp(f, p0 - 4, p0 + 14)))
        put_pol(c, x, 1600, 620, f, 9, skin=1, hair='#6b6b70', tie='#f0c541', suit='#3a3a44', expr='grin', arms='hang', look=-1)
    num(c, 'PAI: EX-PRESIDENTE', 760, 760, f, wt(1, 'ex-presidente') - 3, 66, 3)
    num(c, 'JOKO WIDODO', 760, 880, f, wt(1, 'Joko') - 3, 76, -3)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, t0, .6)
    return c, (lerp(560, 680, t), 1020 + k * 6, lerp(1.12, 1.04, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    """Corte Constitucional: sem prova do diploma."""
    c = CEN('escritorio', 'golden').copy()
    num(c, 'OUTUBRO', 640, 360, f, 0, 90, -3)
    c0 = wt(2, 'Constitucional') - 3
    if f >= c0 - 6:
        paste_c(c, banco().resize((620, 471)), 640, 760, back(ramp(f, c0 - 6, c0 + 4)))
        num(c, 'CORTE CONSTITUCIONAL', 640, 500, f, c0, 64, 3)
    d0 = wt(2, 'diploma') - 3
    if f >= d0:
        paste_c(c, diploma().resize((400, 214)).rotate(4 * math.sin(f * .1), expand=True, resample=Image.BICUBIC), 470, 1150, back(ramp(f, d0, d0 + 8)))
        interroga(c, 760, 1110, f, d0 + 4, 230)
    p0 = wt(2, 'prova') - 3
    num(c, 'SEM PROVA', 640, 960, f, p0, 110, -4)
    l0 = wt(2, 'lei') - 3
    num(c, 'EXIGIDO POR LEI', 640, 1340, f, l0, 70, 3)
    t = smooth(ramp(f, 0, 150))
    k = kick(f, p0, .6)
    return c, (640 + 15 * math.sin(f * .03), lerp(960, 1030, t) + k * 6, lerp(1.04, 1.1, t) * (1 + .0004 * f), lerp(0, 2, t) + k), 'golden'


def s3(f):
    """Suprema Corte: certificado inválido."""
    c = CEN('escritorio', 'golden').copy()
    s0_ = wt(3, 'Suprema') - 3
    num(c, 'SUPREMA CORTE', 640, 400, f, s0_, 100, -3)
    c0 = wt(3, 'certificado') - 3
    if f >= c0 - 4:
        paste_c(c, documento().resize((400, 522)).rotate(-4 + 2 * math.sin(f * .08), expand=True, resample=Image.BICUBIC), 600, 940, back(ramp(f, c0 - 4, c0 + 6)))
        num(c, 'CERTIFICADO DE EQUIVALÊNCIA', 640, 600, f, c0 + 2, 52, 2)
    v0 = wt(3, 'valia') - 3
    if f >= v0:
        carimbo(c, 'INVÁLIDO', 620, 960, back(ramp(f, v0, v0 + 8)), 100)
    put_pol(c, 900, 1640, 480, f, 6, skin=0, hair='#3a2a20', tie='#2f6fd6', suit='#2c3550', expr='stern', arms='point', look=-1)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, v0, .9)
    return c, (640, lerp(1000, 960, t) + k * 8, lerp(1.0, 1.1, t) * (1 + .0005 * f), k), 'golden'


def s4(f):
    """120 deputados, 8 partidos, impeachment; ele sai horas antes."""
    c = CEN('escritorio', 'dusk').copy()
    num(c, 'QUARTA, 11/11', 640, 360, f, 0, 80, -3)
    c0 = wt(4, 'cento') - 3
    multidao(c, 230, 1050, 1560, 300, 9, f, c0 - 4, 20)
    num(c, '120 DEPUTADOS', 640, 560, f, c0, 100, -4)
    num(c, '8 PARTIDOS', 640, 720, f, wt(4, 'oito') - 3, 90, 3)
    i0 = wt(4, 'impeachment') - 3
    if f >= i0:
        paste_c(c, pasta().resize((400, 313)), 640, 1000, back(ramp(f, i0, i0 + 8)))
        num(c, 'IMPEACHMENT', 640, 880, f, i0, 90, -3)
    h0 = wt(4, 'horas') - 3
    if f >= h0:
        paste_c(c, clock_img(11, (f * 2) % 60, 240), 920, 1000, back(ramp(f, h0, h0 + 8)))
        num(c, 'HORAS ANTES', 860, 1180, f, h0, 70, 3)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, i0, .7)
    return c, (640 + 20 * math.sin(f * .03), lerp(1020, 980, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0004 * f), k), 'dusk'


def s5(f):
    """por que importa: 4º país mais populoso; 2 de 5 anos."""
    c = CEN('mapa', 'dusk').copy()
    put_band(c, bandeira_id(), 640, 560, 240, f, back(ramp(f, 0, 8)), pole=False)
    q0 = wt(5, 'quarto') - 3
    num(c, '4º PAÍS', 640, 820, f, q0, 160, -4)
    num(c, 'MAIS POPULOSO DO MUNDO', 640, 990, f, wt(5, 'populoso') - 3, 52, 3)
    d0 = wt(5, 'dois') - 3
    if f >= d0 - 2:
        for i in range(5):
            x = 400 + i * 120
            on = i < 2
            st = d0 - 2 + i * 3
            if f < st: continue
            d = ImageDraw.Draw(c)
            s = back(ramp(f, st, st + 8))
            w = 96 * s; h = 120 * s
            d.rectangle([x - w / 2 + 8, 1250 - h / 2 + 8, x + w / 2 + 8, 1250 + h / 2 + 8], fill=INK)
            d.rectangle([x - w / 2, 1250 - h / 2, x + w / 2, 1250 + h / 2], fill=GREEN if on else (225, 225, 232), outline=INK, width=6)
        num(c, '2 DE 5 ANOS', 640, 1420, f, wt(5, 'cinco') - 3, 90, -3)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, q0, .8)
    return c, (640 + 30 * math.sin(f * .04), lerp(960, 1040, t) + k * 6 + 10 * math.sin(f * .05), lerp(1.1, 1.0, t) * (1 + .0015 * f), lerp(0, -1.5, t) + k + .8 * math.sin(f * .03)), 'dusk'


def s6(f):
    """o que vem: 60 dias, 2 nomes, cadeira vazia."""
    c = CEN('escritorio', 'dusk').copy()
    paste_c(c, calendario().resize((380, 395)), 480, 820, back(ramp(f, 0, 8)))
    num(c, '60 DIAS', 480, 860, f, wt(6, 'sessenta') - 3, 120, -3)
    paste_c(c, cadeira().resize((240, 416)), 900, 1300, 1)
    num(c, 'NOVO VICE?', 840, 1000, f, wt(6, 'vice') - 3, 80, 3)
    n0 = wt(6, 'nomes') - 3
    if f >= n0 - 4:
        for i, x in enumerate((300, 560)):
            st = n0 - 4 + i * 4
            if f >= st:
                put_pol(c, x, 1620, 380, f, 30 + i, skin=i, hair=('#2a221e', '#1c1c1c')[i], tie=('#2f6fd6', '#3aa66a')[i],
                        suit=('#4a4f63', '#3a3a44')[i], bun=(i == 1), expr='neutral', arms='hang', look=1)
        num(c, '2 NOMES', 430, 1150, f, n0, 90, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 80))) + .0006 * f
    return c, (640, 1050, z, lerp(0, 1.5, smooth(ramp(f, 0, 80)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'renunciou') - 3, 150, .8)
    s.thunk(s.W(0, 'diploma') + 5, 120, 1.0)
    s.thunk(s.W(1, 'trinta') - 3, 160, .6)
    s.ting(s.W(1, 'Joko') - 3, .3)
    s.thunk(s.W(2, 'prova') - 3, 140, .8)
    s.thunk(s.W(3, 'valia') - 3, 120, 1.0)
    s.thunk(s.W(4, 'cento') - 3, 150, .8)
    s.ting(s.W(4, 'horas') - 3, .3)
    s.thunk(s.W(5, 'quarto') - 3, 140, .8)
    s.ting(s.W(6, 'sessenta') - 3, .3)
