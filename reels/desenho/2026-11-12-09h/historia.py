"""Um Café com o Mundo — O MUNDO EXPLICADO (quinta 12/11/2026, 09h).
Tema: dois superpetroleiros explodem/pegam fogo no estreito de Ormuz na noite de quarta (11/11/2026).
Fontes (conferidas em 12/11/2026):
- Reuters via MarineLink, 12/11/2026 (Jana Choukeir, Elwely Elwelly): Marinha da Guarda Revolucionária do Irã diz que dois
  superpetroleiros foram inutilizados por grandes explosões na noite de quarta depois de ignorar avisos e usar "rota não
  autorizada"; TV estatal diz que bateram em minas navais; nomes não divulgados; sem confirmação independente.
- Al Arabiya, 12/11/2026 (manchete): Irã diz que os dois petroleiros, com mais de 4 milhões de barris, estão em chamas em Ormuz.
- Reuters via GV Wire, 11/11/2026: pelo menos 10 navios atingidos nos 10 primeiros dias de novembro; outubro teve 37 ataques,
  maior total mensal da guerra (Washington Institute); OMI (agência marítima da ONU) confirma 133 incidentes desde o fim de
  fevereiro, com pelo menos 25 marinheiros mortos; vídeo verificado mostra petróleo chegando às praias de Omã; queda do
  petróleo refletia expectativa de desescalada.
Personagens genéricos, sem pessoas reais. Tom sério, luz 'dusk', só fumaça ao longe."""
from kit import *
import kit

SEA = hexc('#3d7fb8'); SEA_D = hexc('#2c6396'); SAND = hexc('#e2c48e'); SAND_D = hexc('#b89a64')
RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); WHITE = (255, 255, 255)
GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e')


# ------------------------------------------------------------------ desenhos novos
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


@lru_cache(maxsize=2)
def barril():
    p = Pen(200, 260)
    p.shape([(30, 30), (170, 30), (178, 130), (170, 230), (30, 230), (22, 130)], hexc('#2f3a4a'), hexc('#1e2633'), 5, 10)
    p.shape(ell_pts(100, 32, 70, 18, 24), hexc('#46566b'), hexc('#2f3a4a'), 4, 3)
    for y in (90, 170): p.stroke([(24, y), (176, y)], 6, hexc('#5c6d84'))
    p.poly([(60, 115), (140, 115), (140, 145), (60, 145)], GOLD, 3)
    return fin(p)


@lru_cache(maxsize=2)
def moeda():
    p = Pen(160, 160)
    p.shape(ell_pts(80, 80, 66, 66, 32), GOLD, GOLD_D, 5, 6)
    p.arc(80, 80, 44, 44, 0, 360, 4, GOLD_D)
    return fin(p)


@lru_cache(maxsize=2)
def envelope():
    p = Pen(300, 210)
    p.shape([(10, 10), (290, 10), (290, 200), (10, 200)], WHITE, hexc('#c9c9d2'), 5, 6)
    p.stroke([(10, 10), (150, 120), (290, 10)], 5)
    p.dot(150, 120, 22, RED, 3)
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


def nav(c, x, y, w, col='#c0392b', bob=0.0):
    im = sprite('navio', (('col', col),), int(w * 300 / 700), 700 / 300, False)
    paste_c(c, im, x, y + 6 * math.sin(bob))


def cancela(c, f, ang):
    """poste no cabo do Irã e braço listrado; ang 0 = fechado (horizontal p/ baixo do canal), 80 = aberto."""
    d = ImageDraw.Draw(c)
    px, py = 705, 985
    d.rounded_rectangle([px - 22, py - 140, px + 22, py + 10], 10, fill=hexc('#6b6b70'), outline=INK, width=5)
    a = math.radians(90 - ang)
    L = 210
    n = 6
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0, y0 = px + L * t0 * math.cos(a), py + L * t0 * math.sin(a)
        x1, y1 = px + L * t1 * math.cos(a), py + L * t1 * math.sin(a)
        d.line([(x0, y0), (x1, y1)], fill=INK, width=30)
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0, y0 = px + L * t0 * math.cos(a), py + L * t0 * math.sin(a)
        x1, y1 = px + L * t1 * math.cos(a), py + L * t1 * math.sin(a)
        d.line([(x0, y0), (x1, y1)], fill=RED if i % 2 == 0 else WHITE, width=20)
    d.ellipse([px - 18, py - 18, px + 18, py + 18], fill=hexc('#4a4a50'), outline=INK, width=4)


def fumaca(c, x, y, f, seed=0, s=1.0):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(6):
        t = ((f * .6 + i * 17 + seed * 7) % 100) / 100
        r = (30 + 60 * t) * s
        xx = x + 40 * math.sin(t * 5 + seed) * s; yy = y - 260 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=(110, 110, 120, a))


def pais(c, s, x, y, f, f0, col):
    if f < f0: return
    sc = back(ramp(f, f0, f0 + 8))
    paste_c(c, txt(s, 88, -3), x, y - 100 * sc, sc)
    nav(c, x, y + 50, 380 * sc, col, f * .15 + x)




@lru_cache(maxsize=2)
def mapa_qeshm():
    im = mapa_img().copy()
    d = ImageDraw.Draw(im)
    d.polygon([(x, y + 10) for x, y in ISLAND], fill=SAND_D)
    d.polygon(ISLAND, fill=SAND, outline=INK, width=6)
    return im


def marcador(c, x, y, f, f0, s=1.0):
    if f < f0: return
    sc = back(ramp(f, f0, f0 + 8)) * s
    d = ImageDraw.Draw(c)
    pr = 26 + 14 * ((f - f0) % 30) / 30
    d.ellipse([x - pr * 2 * s, y - pr * s, x + pr * 2 * s, y + pr * s], outline=RED, width=5)
    r = 34 * sc
    d.polygon([(x - r, y - 1.6 * r), (x + r, y - 1.6 * r), (x, y)], fill=INK)
    d.ellipse([x - r - 5, y - 2.6 * r - 5, x + r + 5, y - 0.6 * r + 5], fill=INK)
    d.polygon([(x - r * .8, y - 1.6 * r), (x + r * .8, y - 1.6 * r), (x, y - 8)], fill=RED)
    d.ellipse([x - r, y - 2.6 * r, x + r, y - 0.6 * r], fill=RED)
    d.ellipse([x - r * .4, y - 2 * r, x + r * .4, y - 1.2 * r], fill=WHITE)


@lru_cache(maxsize=4)
def radar(broken=0):
    """antena de radar genérica sobre um caminhão-base. 420x420"""
    p = Pen(420, 420)
    g = hexc('#7d8a6a'); gd = hexc('#5a6650')
    p.shape([(40, 300), (380, 300), (380, 380), (40, 380)], g, gd, 5, 8)
    for x in (100, 320): p.shape(ell_pts(x, 385, 34, 34, 20), hexc('#2a2a33'), hexc('#1a1a20'), 4, 3)
    p.shape([(190, 300), (230, 300), (225, 200), (195, 200)], gd, mul(gd, .7), 4, 3)
    if broken:
        p.shape([(110, 230), (210, 200), (300, 250), (280, 290), (130, 290)], hexc('#5b5b62'), hexc('#3d3d44'), 5, 4)
    else:
        p.shape([(80, 60), (340, 110), (310, 210), (110, 190), (60, 120)], hexc('#d9dde3'), hexc('#a9b0ba'), 5, 8)
        p.stroke([(210, 150), (250, 40)], 6)
        p.dot(252, 36, 14, RED, 3)
    return fin(p)


@lru_cache(maxsize=2)
def drone():
    """drone militar genérico de lado, voando p/ direita. 600x220"""
    p = Pen(600, 220)
    gr = hexc('#9aa0a8'); grd = hexc('#6e747c')
    p.shape([(220, 60), (300, 20), (360, 20), (380, 60)], gr, grd, 4, 4)
    p.shape([(40, 110), (520, 95), (580, 112), (520, 135), (40, 130)], gr, grd, 5, 8)
    p.shape([(470, 92), (540, 94), (560, 108), (480, 112)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 2)
    p.shape([(40, 110), (10, 60), (40, 60), (80, 112)], gr, grd, 4, 3)
    p.shape([(40, 128), (10, 180), (40, 180), (80, 128)], gr, grd, 4, 3)
    p.shape([(220, 112), (330, 112), (300, 200), (260, 200)], grd, mul(grd, .7), 4, 3)
    return fin(p)


@lru_cache(maxsize=2)
def maleta():
    """pilha de notas de dinheiro. 360x260"""
    p = Pen(360, 260)
    for i in range(5):
        y = 220 - i * 38
        p.shape([(20, y - 40), (340, y - 40), (340, y), (20, y)], hexc('#5fb06d'), hexc('#3f8a4c'), 4, 4)
        p.dot(180, y - 20, 14, hexc('#d8eecd'), 3)
    return fin(p)


@lru_cache(maxsize=2)
def mic():
    p = Pen(200, 500)
    p.stroke([(100, 140), (100, 480)], 12, hexc('#4a4a50'))
    p.shape([(40, 480), (160, 480), (170, 500), (30, 500)], hexc('#4a4a50'), hexc('#2a2a33'), 4, 3)
    p.shape(ell_pts(100, 80, 46, 70, 24), hexc('#2a2a33'), hexc('#1a1a20'), 5, 4)
    return fin(p)



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


@lru_cache(maxsize=2)
def jato():
    """avião militar genérico de lado, voando p/ direita. 640x240"""
    p = Pen(640, 240)
    g = hexc('#8f96a0'); gd = hexc('#656b74')
    p.shape([(60, 40), (130, 40), (200, 110), (120, 110)], g, gd, 4, 4)
    p.shape([(30, 120), (480, 100), (620, 122), (480, 145), (30, 140)], g, gd, 5, 8)
    p.shape([(400, 96), (480, 100), (500, 112), (410, 114)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 2)
    p.shape([(220, 128), (360, 128), (250, 215), (190, 215)], gd, mul(gd, .7), 4, 3)
    p.dot(40, 130, 14, hexc('#f0a040'), 3)
    return fin(p)


def put_jato(c, x, y, w=420):
    paste_c(c, jato().resize((w, int(w * 240 / 640))), x, y)


def aviso(c, s, x, y, f, f0, size=90, rot=-4):
    if f < f0: return
    sc = back(ramp(f, f0, f0 + 8))
    paste_c(c, txt(s, size, rot), x, y, sc)




@lru_cache(maxsize=2)
def mina():
    """mina naval: bola escura com pinos. 300x300"""
    p = Pen(300, 300)
    for a in range(0, 360, 45):
        r = math.radians(a)
        x0, y0 = 150 + 95 * math.cos(r), 150 + 95 * math.sin(r)
        x1, y1 = 150 + 135 * math.cos(r), 150 + 135 * math.sin(r)
        p.stroke([(x0, y0), (x1, y1)], 16, hexc('#3d3d44'))
        p.dot(x1, y1, 14, hexc('#5c5c64'), 3)
    p.shape(ell_pts(150, 150, 100, 100, 32), hexc('#3d3d44'), hexc('#26262b'), 6, 12)
    p.dot(115, 112, 18, hexc('#6e6e78'), 0)
    return fin(p)


@lru_cache(maxsize=2)
def boia():
    """boia salva-vidas. 300x300"""
    p = Pen(300, 300)
    p.shape(ell_pts(150, 150, 130, 130, 40), WHITE, hexc('#c9c9d2'), 6, 8)
    for a in (20, 110, 200, 290):
        pts = [(150 + 132 * math.cos(math.radians(t)), 150 + 132 * math.sin(math.radians(t))) for t in range(a, a + 51, 5)]
        pts += [(150 + 72 * math.cos(math.radians(t)), 150 + 72 * math.sin(math.radians(t))) for t in range(a + 50, a - 1, -5)]
        p.poly(pts, RED, 0)
    p.shape(ell_pts(150, 150, 70, 70, 32), SEA, SEA_D, 6, 0)
    return fin(p)


def mancha(c, x, y, s, f, seed=0):
    """mancha de petróleo escura e brilhante."""
    if s <= 0: return
    d = ImageDraw.Draw(c, 'RGBA')
    pts = []
    for i in range(24):
        a = i / 24 * 2 * math.pi
        r = s * (1 + .18 * math.sin(a * 3 + seed) + .1 * math.sin(a * 5 + f * .05 + seed))
        pts.append((x + r * 1.7 * math.cos(a), y + r * .55 * math.sin(a)))
    d.polygon(pts, fill=(25, 22, 30, 225))
    d.ellipse([x - s * .5, y - s * .12, x + s * .1, y + s * .02], fill=(120, 90, 160, 90))


def fogo(c, x, y, f, s=1.0, seed=0):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(5):
        fl = math.sin(f * .5 + i * 1.7 + seed)
        w = (40 + 10 * fl) * s; h = (110 + 30 * fl) * s
        xx = x + (i - 2) * 34 * s
        d.polygon([(xx - w, y), (xx, y - h), (xx + w, y)], fill=(240, 120, 40, 230))
        d.polygon([(xx - w * .5, y), (xx, y - h * .6), (xx + w * .5, y)], fill=(250, 210, 80, 240))


def tanker_fogo(c, x, y, w, f, on, seed=0):
    nav(c, x, y, w, '#7a3b2e', f * .12 + seed)
    if on:
        fumaca(c, x + w * .1, y - w * .12, f, seed, w / 450)
        fumaca(c, x + w * .25, y - w * .1, f + 40, seed + 3, w / 520)
        fogo(c, x + w * .15, y - w * .1, f, w / 600, seed)


VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Dois superpetroleiros explodiram no meio da noite, no estreito de Ormuz.",
    "Foi na quarta. A Guarda Revolucionária do Irã diz que eles usaram uma rota não autorizada e bateram em minas.",
    "Segundo o Irã, eles levavam mais de quatro milhões de barris de petróleo. Ninguém de fora confirmou ainda.",
    "E não é caso isolado: pelo menos dez navios foram atingidos nos dez primeiros dias de novembro.",
    "Outubro teve trinta e sete ataques, o recorde da guerra. E a agência marítima da ONU já conta vinte e cinco marinheiros mortos desde fevereiro.",
    "Já tem até petróleo chegando às praias de Omã.",
    "Por que importa? O petróleo vinha caindo com a esperança de paz. Mas no mar, a guerra continua, e é por ali que passa o combustível do mundo.",
]
CAPTXT = [
    "Dois superpetroleiros explodiram|no meio da noite,|no estreito de Ormuz.",
    "Foi na quarta. A Guarda Revolucionária do Irã|diz que eles usaram uma rota|não autorizada e bateram em minas.",
    "Segundo o Irã, eles levavam|mais de 4 milhões de barris de petróleo.|Ninguém de fora confirmou ainda.",
    "E não é caso isolado: pelo menos 10 navios|foram atingidos nos 10 primeiros|dias de novembro.",
    "Outubro teve 37 ataques, o recorde da guerra.|E a agência marítima da ONU já conta|25 marinheiros mortos desde fevereiro.",
    "Já tem até petróleo chegando|às praias de Omã.",
    "Por que importa? O petróleo vinha caindo|com a esperança de paz. Mas no mar,|a guerra continua, e é por ali|que passa o combustível do mundo.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'explodiram', 4), (0, 'Ormuz', 6), (1, 'quarta', 4), (1, 'rota', 6), (1, 'minas', 6),
         (2, 'quatro', 6), (2, 'confirmou', 6), (3, 'dez', 6), (3, 'novembro', 6),
         (4, 'trinta', 6), (4, 'recorde', 4), (4, 'vinte', 6), (5, 'praias', 6), (5, 'Oma', 8),
         (6, 'caindo', 6), (6, 'continua', 4), (6, 'combustivel', 6)]

STRAIT = (705, 1060)
OMA = (1040, 1250)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = mar_bg()
    e0 = wt(0, 'explodiram') - 3
    on = f >= e0
    tanker_fogo(c, 380, 1200, 560, f, on, 1)
    tanker_fogo(c, 900, 1000, 440, f, on and f >= e0 + 4, 4)
    num(c, '2 SUPERPETROLEIROS', 640, 540, f, wt(0, 'superpetroleiros') - 3, 74, -3)
    num(c, 'ESTREITO DE ORMUZ', 640, 700, f, wt(0, 'Ormuz') - 3, 74, 3)
    z = lerp(1.4, 1.06, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, e0 + 2)
    return c, (640, 1020 + k * 8, z, k), 'dusk'


def s1(f):
    c = mapa_img().copy()
    num(c, 'IRÃ', 420, 640, f, 0, 110, -3)
    num(c, 'QUARTA À NOITE', 640, 420, f, wt(1, 'quarta') - 3, 96, 3)
    r0 = wt(1, 'rota') - 3
    if f >= r0:
        d = ImageDraw.Draw(c)
        n = int(12 * smooth(ramp(f, r0, r0 + 20)))
        for i in range(n):
            x = 180 + i * 85; y = 1180 - 120 * math.sin(i / 11 * math.pi) * .4 + i * 6
            d.line([(x, y), (x + 45, y + 3)], fill=RED, width=14)
        num(c, 'ROTA NÃO AUTORIZADA', 640, 1500, f, r0, 70, -3)
    m0 = wt(1, 'minas') - 3
    if f >= m0:
        for i, (x, y) in enumerate(((620, 1150), (820, 1205), (980, 1260))):
            if f >= m0 + i * 4:
                paste_c(c, mina(), x, y + 8 * math.sin(f * .1 + i), back(ramp(f, m0 + i * 4, m0 + i * 4 + 8)) * .32)
        num(c, 'MINAS', 820, 960, f, m0, 110, 4)
    marcador(c, STRAIT[0], STRAIT[1] - 10, f, wt(1, 'usaram') - 3, .7)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 150))) + .0006 * f
    return c, (680 + 20 * math.sin(f * .03), lerp(980, 1060, smooth(ramp(f, 0, 150))), z, lerp(-1.5, 1, smooth(ramp(f, 0, 150)))), 'dusk'


def s2(f):
    c = mar_bg()
    tanker_fogo(c, 640, 1380, 760, f, True, 2)
    q0 = wt(2, 'quatro') - 3
    b = barril()
    for i in range(10):
        r, k = divmod(i, 5)
        if f >= q0 + i * 2:
            paste_c(c, b, 240 + k * 190 + r * 95, 1000 - r * 150, back(ramp(f, q0 + i * 2, q0 + i * 2 + 8)) * .7)
    num(c, 'SEGUNDO O IRÃ', 640, 380, f, wt(2, 'Segundo') - 3, 80, -3)
    num(c, '+4 MILHÕES', 640, 540, f, q0, 120, 3)
    num(c, 'DE BARRIS', 640, 690, f, q0 + 5, 90, -3)
    c0 = wt(2, 'confirmou') - 3
    if f >= c0:
        paste_c(c, txt('SEM CONFIRMAÇÃO', 84, 4), 640, 860, back(ramp(f, c0, c0 + 8)))
    z = 1.0 + .0011 * f
    k = kick(f, q0, .6)
    return c, (640 + 25 * math.sin(f * .03), 1000 + .3 * f + k * 6, z, .8 * math.sin(f * .04)), 'dusk'


SHIPS10 = [(300, 1120), (450, 1250), (560, 1080), (680, 1180), (800, 1110), (900, 1290), (1010, 1180), (1120, 1300),
           (380, 1340), (760, 1330)]


def s3(f):
    c = mapa_img().copy()
    d0 = wt(3, 'dez') - 3
    for i, (x, y) in enumerate(SHIPS10):
        fi = d0 - 20 + i * 4
        paste_c(c, sprite('navio', (('col', '#7a3b2e'),), 60, 700 / 300, False), x, y)
        if f >= fi:
            fumaca(c, x, y - 20, f - fi, i, .45)
            if f < fi + 10: rings(c, x, y, f, fi, 10, .4)
    num(c, '10 NAVIOS', 640, 480, f, d0, 130, -3)
    num(c, 'EM 10 DIAS', 640, 650, f, wt(3, 'novembro') - 12, 100, 3)
    z = lerp(1.05, 1.16, smooth(ramp(f, 0, 160)))
    return c, (680 + 20 * math.sin(f * .03), 1000, z, .6 * math.sin(f * .04)), 'dusk'


def s4(f):
    c = mar_bg()
    t0 = wt(4, 'trinta') - 3
    d = ImageDraw.Draw(c)
    # calendario de outubro
    sc = max(.05, back(ramp(f, 0, 10)))
    x0, y0 = 640 - 360 * sc, 920 - 360 * sc
    d.rounded_rectangle([x0, y0, 640 + 360 * sc, 920 + 360 * sc], 24, fill=WHITE, outline=INK, width=6)
    d.rectangle([x0, y0, 640 + 360 * sc, y0 + 90 * sc], fill=RED, outline=INK, width=6)
    if sc > .9:
        paste_c(c, txt('OUTUBRO', 70, 0), 640, y0 + 46, 1)
        n = 0 if f < t0 else min(37, int((f - t0) * 2.2))
        for i in range(n):
            r, k = divmod(i, 7)
            cx, cy = 361 + k * 93, 720 + r * 92
            fogo(c, cx, cy + 30, f, .3, i)
            d.ellipse([cx - 30, cy + 22, cx + 30, cy + 40], fill=hexc('#7a3b2e'), outline=INK, width=3)
    num(c, '37 ATAQUES', 640, 340, f, t0, 120, -3)
    num(c, 'RECORDE', 640, 480, f, wt(4, 'recorde') - 3, 90, 8)
    v0 = wt(4, 'vinte') - 3
    if f >= v0:
        c2 = mar_bg()
        a = back(ramp(f, v0, v0 + 8))
        paste_c(c2, boia(), 640, 1180 + 12 * math.sin(f * .08), a * 1.1)
        paste_c(c2, txt('25 MARINHEIROS', 100, -3), 640, 620, a)
        paste_c(c2, txt('MORTOS', 90, 3), 640, 780, a)
        if f >= wt(4, 'fevereiro') - 3:
            num(c2, 'DESDE FEVEREIRO', 640, 1460, f, wt(4, 'fevereiro') - 3, 70, -2)
        c = c2
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 200))) + .0002 * f
    k = kick(f, t0, .6)
    return c, (640, 1000 + k * 6, z, k), 'dusk'


def s5(f):
    c = CEN('praia', 'dusk').copy()
    p0 = wt(5, 'petroleo') - 3
    t = smooth(ramp(f, p0 - 6, p0 + 50))
    for i, (x, y, s) in enumerate(((380, 1520, 150), (800, 1560, 190), (600, 1640, 120), (1000, 1500, 110))):
        mancha(c, x, y, s * t, f, i)
    num(c, 'PETRÓLEO NA PRAIA', 640, 520, f, wt(5, 'praias') - 3, 86, -3)
    num(c, 'OMÃ', 640, 700, f, wt(5, 'Oma') - 3, 140, 3)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 90))) + .0004 * f
    return c, (640, lerp(1150, 1100, smooth(ramp(f, 0, 90))), z, .6 * math.sin(f * .05)), 'dusk'


def s6(f):
    c = mapa_img().copy()
    cai0 = wt(6, 'caindo') - 3
    if f < cai0:
        paste_c(c, txt('POR QUE IMPORTA?', 90, -4), 640, 560, back(ramp(f, 0, 8)))
    co0 = wt(6, 'continua') - 3
    if cai0 <= f < co0:
        num(c, 'PETRÓLEO CAINDO', 640, 480, f, cai0, 92, -3)
        d = ImageDraw.Draw(c)
        s = back(ramp(f, cai0, cai0 + 8))
        d.polygon([(560, 600), (720, 600), (720, 700), (790, 700), (640, 860 * s + 700 * (1 - s)), (490, 700), (560, 700)], fill=hexc('#3aa66a'), outline=INK)
        num(c, 'ESPERANÇA DE PAZ', 640, 1500, f, wt(6, 'paz') - 3, 70, 3)
    if f >= co0:
        num(c, 'NO MAR, A GUERRA', 640, 440, f, co0, 90, -3)
        num(c, 'CONTINUA', 640, 590, f, co0 + 4, 110, 3)
        fumaca(c, STRAIT[0], STRAIT[1], f - co0, 2, 1.0)
    p0 = wt(6, 'passa') - 3
    b = barril().resize((110, 143))
    if f >= p0:
        for i in range(7):
            tt = ((f - p0) * .012 + i / 7) % 1
            paste_c(c, b, lerp(80, 1180, tt), 1075 + 10 * math.sin(f * .2 + i), back(ramp(f, p0 + i * 2, p0 + i * 2 + 8)))
    q0 = wt(6, 'combustivel') - 3
    if f >= q0:
        paste_c(c, bomba(), 1000, 1320, back(ramp(f, q0, q0 + 8)) * .6)
        num(c, 'COMBUSTÍVEL', 640, 760, f, q0, 100, 3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 200))) + .0005 * f
    k = kick(f, co0, .5)
    return c, (660, lerp(1000, 1060, smooth(ramp(f, 0, 200))) + k * 6, z, lerp(-1.5, 1, smooth(ramp(f, 0, 200)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'explodiram') - 1, 140, .7)
    s.thunk(s.W(0, 'explodiram') + 4, 110, .5)
    s.ting(s.W(0, 'Ormuz') - 3, .2)
    s.ting(s.W(1, 'quarta') - 3, .2)
    s.whoosh(s.W(1, 'rota') - 6, .4, .3)
    s.thunk(s.W(1, 'minas') - 3, 130, .5)
    s.ting(s.W(2, 'quatro') - 3, .3)
    s.thunk(s.W(3, 'dez') - 3, 120, .5)
    s.ting(s.W(4, 'trinta') - 3, .25)
    s.ting(s.W(4, 'vinte') - 3, .15)
    s.splash(s.W(5, 'petroleo') - 3, .25) if hasattr(s, 'splash') else None
    s.thunk(s.W(6, 'combustivel') - 3, 160, .5)
