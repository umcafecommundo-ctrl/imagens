"""Um Café com o Mundo — O MUNDO EXPLICADO (sexta 13/11/2026, 09h).
Tema: papa Leão XIV volta ao Peru, onde viveu cerca de 20 anos; hoje (13/11) vai a Chiclayo.
Fontes (conferidas em 13/11/2026):
- OSV News / Catholic Courier, 11-12/11/2026 "3 million people give Pope Leo XIV a warm welcome as he arrives in Peru":
  pousou na Base Aérea de Callao, Lima, em 11/11 ~17h; Santa Sé estimou 3 milhões de pessoas nas ruas; chegou ao Peru como
  padre missionário em 1985; bispo de Chiclayo de 2015 a 2023; cidadania peruana em 2015; disse "também volto à minha pátria";
  pediu a autoridades "honestidade, integridade"; viagem de 6 a 17/11 (Uruguai, Argentina, Peru), volta a Roma em 17/11;
  depois de Lima: Chiclayo (grande missa ao ar livre), Cusco e Pucallpa (Amazônia); taxa de homicídios 10,7 por 100 mil,
  contra 5,8 cinco anos antes (AP).
- CBS News / AP, 11/11/2026: nasceu em Chicago; cantou o hino nacional do Peru no palácio; primeiro papa com dupla cidadania
  EUA-Peru; sexta (13/11) chega a Chiclayo.
- EWTN News (live updates), 12-13/11/2026: vigília com jovens no Estádio Nacional de Lima, "mais de 50 mil" (manchete: 60 mil);
  sexta de manhã sai de Lima para Chiclayo, diocese que dirigiu de 2015 a 2023; missa às 10h30 em Pimentel.
Personagem do papa = figura genérica de batina branca (sem traços da pessoa real). Tom neutro."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Três milhões de pessoas foram às ruas de Lima, no Peru, pra receber um homem só.",
    "É o papa Leão Catorze. Ele nasceu nos Estados Unidos, mas disse que voltou à sua pátria.",
    "Ele chegou ao Peru como padre missionário em mil novecentos e oitenta e cinco, e depois foi bispo de Chiclayo.",
    "Em dois mil e quinze, virou cidadão peruano. É o primeiro papa com as duas cidadanias, americana e peruana.",
    "Em Lima, cantou o hino do Peru e reuniu mais de cinquenta mil jovens num estádio.",
    "Por que importa? No Peru, a taxa de homicídios quase dobrou em cinco anos, e o papa pediu honestidade aos políticos.",
    "Hoje, ele volta a Chiclayo, a cidade onde foi bispo. Depois, Cusco e a Amazônia, e Roma na terça.",
]
CAPTXT = [
    "3 milhões de pessoas foram às ruas de Lima, no Peru,|pra receber um homem só.",
    "É o papa Leão XIV. Ele nasceu nos Estados Unidos,|mas disse que voltou à sua pátria.",
    "Ele chegou ao Peru como padre missionário em 1985,|e depois foi bispo de Chiclayo.",
    "Em 2015, virou cidadão peruano.|É o primeiro papa com as duas cidadanias,|americana e peruana.",
    "Em Lima, cantou o hino do Peru|e reuniu mais de 50 mil jovens num estádio.",
    "Por que importa? No Peru, a taxa de homicídios|quase dobrou em 5 anos,|e o papa pediu honestidade aos políticos.",
    "Hoje, ele volta a Chiclayo, a cidade onde foi bispo.|Depois, Cusco e a Amazônia, e Roma na terça.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Tres', 6), (0, 'Lima', 6), (1, 'Catorze', 6), (1, 'Estados', 6), (1, 'patria', 6), (2, 'mil', 6),
         (2, 'Chiclayo', 6), (3, 'quinze', 6), (3, 'duas', 6), (4, 'hino', 6), (4, 'cinquenta', 6), (5, 'dobrou', 6),
         (5, 'honestidade', 6), (6, 'Chiclayo', 6), (6, 'Cusco', 6), (6, 'Roma', 6)]

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




def xis(c, x, y, size, s):
    if s <= .02: return
    d = ImageDraw.Draw(c)
    r = size * s / 2
    for a, b in (((x - r, y - r), (x + r, y + r)), ((x + r, y - r), (x - r, y + r))):
        d.line([(a[0] + 8, a[1] + 8), (b[0] + 8, b[1] + 8)], fill=INK, width=int(46 * s))
        d.line([a, b], fill=RED, width=int(34 * s))


def interroga(c, x, y, f, f0, size=220):
    if f >= f0: paste_c(c, txt('?', size, 8 * math.sin(f * .1)), x, y + 10 * math.sin(f * .15), back(ramp(f, f0, f0 + 8)))



# ------------------------------------------------------------------ desenhos novos (13/11 09h)
@lru_cache(maxsize=2)
def bandeira_pe():
    """bandeira do Peru (país), sem brasão: vermelho | branco | vermelho. 600x400"""
    p = Pen(600, 400)
    p.poly([(10, 10), (203, 10), (203, 390), (10, 390)], RED)
    p.poly([(203, 10), (397, 10), (397, 390), (203, 390)], WHITE)
    p.poly([(397, 10), (590, 10), (590, 390), (397, 390)], RED)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_us():
    """bandeira dos EUA simplificada: listras + cantão azul com pontos. 600x400"""
    p = Pen(600, 400)
    for i in range(13):
        y0 = 10 + i * 380 / 13
        p.poly([(10, y0), (590, y0), (590, y0 + 380 / 13 + 1), (10, y0 + 380 / 13 + 1)], RED if i % 2 == 0 else WHITE)
    p.poly([(10, 10), (270, 10), (270, 215), (10, 215)], BLUE_D)
    for r in range(5):
        for k in range(6):
            p.dot(35 + k * 42 + (r % 2) * 18, 35 + r * 40, 7, WHITE)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


def papa(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, padre=False):
    """figura GENÉRICA de papa (batina branca, solidéu branco, cruz dourada) ou padre (preto, colarinho). 600x1000"""
    if padre:
        img = politico(expr=expr, arms=arms, blink=blink, look=look, tilt=tilt, skin=0, hair='#4a3a2e', tie=None, suit='#2c2c34')
        p = Pen(600, 1000); p.img = img; p.d = ImageDraw.Draw(img)
        p.poly([(258, 408), (342, 408), (300, 530)], hexc('#2c2c34'))
        p.poly([(325, 460), (372, 460), (372, 530), (325, 530)], hexc('#2c2c34'))
        p.shape([(284, 410), (316, 410), (316, 428), (284, 428)], WHITE, None, 3, 0)
        return p.img
    img = politico(expr=expr, arms=arms, blink=blink, look=look, tilt=tilt, skin=0, hair='#9a9aa2', tie=None, suit='#f2efe8')
    p = Pen(600, 1000); p.img = img; p.d = ImageDraw.Draw(img)
    p.poly([(258, 408), (342, 408), (300, 530)], hexc('#f2efe8'))
    p.poly([(325, 460), (372, 460), (372, 530), (325, 530)], hexc('#f2efe8'))
    hx = 300 + tilt * 6
    p.shape(ell_pts(hx, 160, 66, 28, 32), WHITE, hexc('#d9d6ce'), 5, 4)
    p.stroke([(300, 430), (300, 500)], 5, GOLD_D)
    p.shape([(292, 480), (308, 480), (308, 560), (292, 560)], GOLD, GOLD_D, 4, 2)
    p.shape([(272, 500), (328, 500), (328, 514), (272, 514)], GOLD, GOLD_D, 4, 2)
    return p.img


def put_papa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'papa', x, feet, h, f, seed, **kw)


@lru_cache(maxsize=2)
def igreja():
    """igreja colonial genérica com 2 torres. 900x900, base y~890"""
    p = Pen(900, 900)
    W1 = hexc('#f5e6b8'); W1D = hexc('#d4bf84')
    for x0 in (60, 640):
        p.shape([(x0, 260), (x0 + 200, 260), (x0 + 200, 890), (x0, 890)], W1, W1D, 6, 10)
        p.shape([(x0 - 10, 240), (x0 + 210, 240), (x0 + 210, 270), (x0 - 10, 270)], WHITE, hexc('#dddddd'), 5, 3)
        p.shape([(x0 + 20, 240), (x0 + 100, 120), (x0 + 180, 240)], hexc('#c96a4a'), hexc('#9a4a30'), 5, 6)
        p.shape([(x0 + 70, 300), (x0 + 130, 300), (x0 + 130, 400), (x0 + 70, 400)], hexc('#4a3a5a'), None, 4, 0)
        p.stroke([(x0 + 100, 120), (x0 + 100, 60)], 7); p.stroke([(x0 + 78, 84), (x0 + 122, 84)], 7)
    p.shape([(250, 420), (650, 420), (650, 890), (250, 890)], W1, W1D, 6, 12)
    p.shape([(240, 430), (450, 300), (660, 430)], W1, W1D, 6, 8)
    p.shape([(390, 640), (510, 640), (510, 890), (390, 890)], hexc('#7a4e33'), hexc('#57361f'), 5, 6)
    p.shape(ell_pts(450, 640, 60, 50, 30), hexc('#7a4e33'), hexc('#57361f'), 5, 4)
    p.dot(450, 500, 46, hexc('#7fb6e0'), 5)
    return fin(p)


def povo(c, x0, x1, feet, h, n, f, f0, seed=0, wave=True, flags=0):
    """multidão genérica com roupas coloridas, braços para cima, algumas bandeirinhas do Peru."""
    cols = ('#e0583c', '#3a86c8', '#f0c541', '#5aa66a', '#c85a9a', '#f2efe8', '#7a5ac8')
    for i in range(n):
        st = f0 + i * 2
        if f < st: continue
        x = lerp(x0, x1, i / max(1, n - 1))
        up = wave and ((f // 12 + i) % 3 != 0)
        put_pol(c, x, feet + (i % 2) * 40, h * (1 - (i % 2) * .08), f, seed + i, skin=(i * 7) % 3,
                hair=('#2a221e', '#3a2a20', '#1c1c1c')[i % 3], tie=None, suit=cols[(i * 3) % len(cols)],
                bun=(i % 3 == 1), expr='grin', arms='up' if up else 'hang', look=(-1 if x > 640 else 1))
    for k in range(flags):
        x = lerp(x0, x1, (k + .5) / flags)
        put_band(c, bandeira_pe(), x + 40, feet - h * 1.05 - 20 * math.sin(f * .2 + k), 150, f + k * 7, back(ramp(f, f0 + 6, f0 + 14)))


def arquibancada(c, f, y0, y1, seed=1):
    """arquibancada de estádio cheia (cabeças coloridas) com 'ola'."""
    d = ImageDraw.Draw(c)
    d.rectangle([0, y0 - 40, BW, y1 + 30], fill=hexc('#3a3550'))
    rnd = random.Random(seed)
    cols = [hexc(x) for x in ('#e0583c', '#f2efe8', '#d8443c', '#f0c541', '#3a86c8', '#ffffff', '#5aa66a')]
    rows = int((y1 - y0) / 46)
    for r in range(rows):
        y = y0 + r * 46
        d.line([(0, y + 26), (BW, y + 26)], fill=hexc('#4c4664'), width=6)
        for k in range(30):
            x = k * 43 + (r % 2) * 20 + rnd.random() * 6
            ola = max(0, math.sin((x / BW) * 6 - f * .18)) ** 6 * 26
            col = cols[rnd.randrange(len(cols))]
            d.ellipse([x - 14, y - 14 - ola, x + 14, y + 14 - ola], fill=col, outline=INK, width=3)
    for lx in (120, 1120):
        d.rectangle([lx - 8, y0 - 420, lx + 8, y0 - 40], fill=hexc('#6b6b70'))
        d.rectangle([lx - 70, y0 - 470, lx + 70, y0 - 410], fill=hexc('#fff6c0'), outline=INK, width=5)


def notas_musica(c, x, y, f, f0):
    if f < f0: return
    for i in range(3):
        age = (f - f0 + i * 10) % 30
        paste_c(c, txt('♪', 90, 10 * math.sin(f * .2 + i)), x + i * 70 - 70 + age * 2, y - age * 6, clamp(1 - age / 30) * back(ramp(f, f0, f0 + 6)))


def pino(c, x, y, s):
    if s <= .02: return
    d = ImageDraw.Draw(c)
    r = 34 * s
    d.polygon([(x - r * .8, y - r * 1.2), (x + r * .8, y - r * 1.2), (x, y)], fill=RED, outline=INK)
    d.ellipse([x - r, y - r * 2.2, x + r, y - r * .2], fill=RED, outline=INK, width=6)
    d.ellipse([x - r * .4, y - r * 1.6, x + r * .4, y - r * .8], fill=WHITE)


# ------------------------------------------------------------------ cenas
def s0(f):
    """gancho: multidão em Lima recebe o papa."""
    c = CEN('cidade', 'day').copy()
    t0 = max(0, wt(0, 'Tres') - 3)
    povo(c, 110, 400, 1640, 420, 5, f, 0, 1, flags=2)
    povo(c, 880, 1170, 1640, 420, 5, f, 0, 11, flags=2)
    r0 = wt(0, 'receber') - 3
    put_papa(c, 640, 1720, 700, f, 3, expr='grin' if f >= r0 else 'neutral', arms='up' if f >= r0 else 'hang', look=0)
    num(c, '3 MILHÕES', 640, 500, f, t0, 140, -4)
    num(c, 'LIMA, PERU', 640, 680, f, wt(0, 'Lima') - 3, 90, 3)
    z = lerp(1.35, 1.04, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, t0, .8)
    return c, (640, 1030 + k * 8, z, k), 'day'


def s1(f):
    """quem: papa Leão XIV, nasceu nos EUA, 'voltou à sua pátria'."""
    c = CEN('mapa', 'day').copy()
    num(c, 'PAPA LEÃO XIV', 640, 380, f, max(0, wt(1, 'papa') - 3), 100, -3)
    e0 = wt(1, 'Estados') - 3
    put_band(c, bandeira_us(), 420, 640, 240, f, back(ramp(f, e0, e0 + 8)), pole=False)
    num(c, 'NASCEU NOS EUA', 420, 820, f, e0, 52, -3)
    p0 = wt(1, 'patria') - 4
    put_band(c, bandeira_pe(), 860, 640, 240, f, back(ramp(f, p0 - 6, p0 + 2)), pole=False)
    num(c, '"MINHA PÁTRIA"', 860, 940, f, p0, 56, 3)
    put_papa(c, 640, 1760, 760, f, 4, expr='grin' if f >= p0 else 'neutral', arms='hang', look=(-1 if f < p0 else 1))
    t = smooth(ramp(f, 0, 120))
    k = kick(f, p0, .6)
    return c, (640 + 10 * math.sin(f * .04), 1030 + k * 6, lerp(1.12, 1.03, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    """passado: padre missionário em 1985, depois bispo de Chiclayo."""
    c = CEN('cidade', 'golden').copy()
    paste_c(c, igreja().resize((700, 700)), 640, 1170, 1)
    m0 = wt(2, 'mil') - 3
    num(c, '1985', 640, 420, f, m0, 170, -4)
    num(c, 'PADRE MISSIONÁRIO', 640, 600, f, wt(2, 'missionario') - 3, 72, 3)
    b0 = wt(2, 'bispo') - 3
    bispo = f >= b0
    put_papa(c, lerp(360, 440, smooth(ramp(f, 0, 90))), 1720, 680, f, 5, padre=True, expr='grin', arms='hang', look=1)
    if bispo:
        put_dust(c, 900, 1500, 90, f - b0)
        put_band(c, bandeira_pe(), 900, 1040, 200, f, back(ramp(f, b0, b0 + 8)), pole=True)
    num(c, 'BISPO DE CHICLAYO', 640, 780, f, wt(2, 'Chiclayo') - 3, 72, -3)
    t = smooth(ramp(f, 0, 150))
    k = kick(f, m0, .6)
    return c, (640 + 15 * math.sin(f * .03), lerp(1000, 1040, t) + k * 6, lerp(1.02, 1.1, t) * (1 + .0004 * f), lerp(0, 1.5, t) + k), 'golden'


def s3(f):
    """2015: cidadão peruano; 1º papa com as 2 cidadanias."""
    c = CEN('escritorio', 'day').copy()
    q0 = wt(3, 'quinze') - 3
    num(c, '2015', 640, 380, f, max(0, wt(3, 'dois') - 3), 150, -4)
    paste_c(c, documento().resize((360, 470)).rotate(-4 + 2 * math.sin(f * .08), expand=True, resample=Image.BICUBIC), 470, 800, back(ramp(f, 0, 8)))
    cz = wt(3, 'cidadao') - 3
    if f >= cz: carimbo(c, 'CIDADÃO PERUANO', 500, 820, back(ramp(f, cz, cz + 8)), 58)
    d0 = wt(3, 'duas') - 3
    put_band(c, bandeira_us(), 300, 1160, 200, f, back(ramp(f, d0, d0 + 8)), pole=False)
    put_band(c, bandeira_pe(), 580, 1160, 200, f, back(ramp(f, d0 + 4, d0 + 12)), pole=False)
    num(c, '2 CIDADANIAS', 440, 1330, f, d0, 72, 3)
    put_papa(c, 920, 1800, 700, f, 6, expr='grin', arms='hang', look=0)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, cz, .8)
    return c, (640, lerp(980, 1040, t) + k * 6, lerp(1.0, 1.08, t) * (1 + .0005 * f), k), 'day'


def s4(f):
    """Lima: hino e estádio com 50 mil jovens."""
    c = CEN('cidade', 'dusk').copy()
    arquibancada(c, f, 660, 1380, 3)
    h0 = wt(4, 'hino') - 3
    put_band(c, bandeira_pe(), 950, 1220, 240, f, back(ramp(f, max(0, h0 - 6), h0 + 2)), pole=True)
    put_papa(c, 540, 1760, 680, f, 7, expr='grin', arms='up' if f >= wt(4, 'reuniu') - 3 else 'hang', look=1)
    notas_musica(c, 620, 1000, f, h0)
    num(c, 'HINO DO PERU', 640, 420, f, h0, 90, -3)
    c0 = wt(4, 'cinquenta') - 3
    num(c, '+50 MIL JOVENS', 640, 590, f, c0, 100, 3)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, c0, .8)
    return c, (640 + 25 * math.sin(f * .03), lerp(1040, 990, t) + k * 6, lerp(1.1, 1.0, t) * (1 + .0006 * f), k), 'dusk'


def s5(f):
    """por que importa: homicídios quase dobraram; pedido de honestidade."""
    c = CEN('cidade', 'dusk').copy()
    num(c, 'HOMICÍDIOS NO PERU', 640, 360, f, 0, 76, -3)
    a0 = max(0, wt(5, 'taxa') - 3)
    barra(c, 440, 1080, 170, 180, (150, 150, 165), '', f, a0, '5,8')
    d0 = wt(5, 'dobrou') - 3
    barra(c, 800, 1080, 170, 330, RED, '', f, d0 - 4, '10,7')
    num(c, 'HÁ 5 ANOS', 440, 1150, f, wt(5, 'cinco') - 3, 50, 0)
    num(c, 'HOJE', 800, 1150, f, d0, 54, 0)
    o0 = wt(5, 'honestidade') - 3
    if f < o0: num(c, 'QUASE DOBROU', 640, 520, f, d0, 96, 4)
    if f >= o0 - 10:
        s = back(ramp(f, o0 - 10, o0))
        put_papa(c, 300, 1820, 520 * s, f, 8, expr='stern', arms='point', look=1)
        for i, x in enumerate((820, 1040)):
            put_pol(c, x, 1820, 500 * s, f, 40 + i, skin=i, hair=('#2a221e', '#1c1c1c')[i], tie=('#2f6fd6', '#d8443c')[i],
                    suit=('#2c3550', '#3a3a44')[i], expr='nervous', arms='hang', look=-1)
        num(c, 'HONESTIDADE', 640, 520, f, o0, 100, -3)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, d0, .8)
    return c, (640 + 20 * math.sin(f * .03), lerp(960, 1020, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0008 * f), lerp(0, -1.5, t) + k), 'dusk'


def s6(f):
    """o que vem: hoje Chiclayo, depois Cusco e Amazônia, Roma na terça."""
    c = CEN('mapa', 'golden').copy()
    put_band(c, bandeira_pe(), 640, 400, 200, f, back(ramp(f, 0, 8)), pole=False)
    paradas = [('HOJE: CHICLAYO', 'Chiclayo', 640, 640), ('CUSCO', 'Cusco', 380, 870), ('AMAZÔNIA', 'Amazonia', 900, 870), ('TERÇA: ROMA', 'Roma', 640, 1090)]
    for i, (lab, w, x, y) in enumerate(paradas):
        w0 = wt(6, w) - 3
        pino(c, x, y - 40, back(ramp(f, w0, w0 + 8)))
        num(c, lab, x, y + 20, f, w0, 64 if i else 70, (-3, 3)[i % 2])
    put_papa(c, 640, 1800, 620, f, 9, expr='grin', arms='up' if (f // 20) % 2 else 'hang', look=0)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) + .0006 * f
    return c, (640, 1030, z, lerp(0, 1.5, smooth(ramp(f, 0, 90)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'Tres') - 3, 140, 1.0)
    s.ting(s.W(0, 'Lima') - 3, .3)
    s.thunk(s.W(1, 'Estados') - 3, 180, .6)
    s.ting(s.W(1, 'patria') - 4, .35)
    s.thunk(s.W(2, 'mil') - 3, 150, .7)
    s.ting(s.W(2, 'Chiclayo') - 3, .3)
    s.thunk(s.W(3, 'cidadao') - 3, 120, 1.0)
    s.ting(s.W(3, 'duas') - 3, .3)
    s.ting(s.W(4, 'hino') - 3, .35)
    s.thunk(s.W(4, 'cinquenta') - 3, 140, .8)
    s.thunk(s.W(5, 'dobrou') - 3, 130, .9)
    s.thunk(s.W(5, 'honestidade') - 3, 170, .6)
    for w in ('Chiclayo', 'Cusco', 'Amazonia', 'Roma'): s.ting(s.W(6, w) - 3, .25)
