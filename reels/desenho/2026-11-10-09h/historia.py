"""Um Café com o Mundo — O MUNDO EXPLICADO (terça 10/11/2026, 09h).
Tema: Arábia Saudita intercepta mísseis dos houthis contra Riad; míssil no sul e drone na Província Oriental;
oleoduto Leste-Oeste atacado de novo na segunda (09/11); ataques aéreos relatados em Sanaa.
Fontes (conferidas em 10/11/2026):
- Reuters (via TimesLIVE, 10/11/2026, "Saudi coalition says it intercepted Houthi missiles over Riyadh"): coalizão
  interceptou 2 mísseis lançados contra Riad (1 balístico e 1 de cruzeiro); outro míssil balístico destruído no sul
  (alertas em Abha e Khamis Mushait); drone interceptado sobre a Província Oriental, que tem a maior parte das reservas
  de petróleo e gás do reino; agência Saba (houthi) relata ataques sauditas à estação de gás al-Mufazir (Jadar, norte de
  Sanaa) e a um prédio da estatal de petróleo no sul de Sanaa, não confirmados pelos sauditas; houthis não reivindicaram
  de imediato.
- AFP (via Yahoo News, 10/11/2026, "Saudi Arabia downs missiles fired at Riyadh after Houthi attack on pipeline"): várias
  explosões ouvidas em Riad; moradores receberam alerta de texto para se abrigar; porta-voz da coalizão Turki al-Maliki
  culpa os "houthis apoiados pelo Irã"; oleoduto Leste-Oeste (região de Medina) atacado de novo na segunda: "incêndio
  limitado", apagado, operações não afetadas, sem feridos; oleoduto vital para exportações porque o Irã restringiu Ormuz.
Tom sério; sem violência mostrada; personagens genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Riad, a capital da Arábia Saudita, acordou com explosões no céu nesta madrugada.",
    "A defesa aérea derrubou dois mísseis sobre a cidade, e os moradores receberam um alerta no celular para se proteger.",
    "Outro míssil foi derrubado no sul do país, e um drone no leste, onde fica a maior parte do petróleo saudita.",
    "Os sauditas culpam os houthis, um grupo armado do Iêmen apoiado pelo Irã.",
    "Um dia antes, o oleoduto Leste-Oeste foi atacado de novo, mas o fogo foi apagado e o petróleo seguiu passando.",
    "Por que isso importa? Com o Irã restringindo o estreito de Ormuz, esse oleoduto até o Mar Vermelho virou uma saída vital para o petróleo.",
    "E a imprensa dos houthis diz que aviões sauditas atacaram instalações de gás e petróleo em Sanaa, no Iêmen.",]
CAPTXT = [
    "Riad, a capital da Arábia Saudita,|acordou com explosões no céu|nesta madrugada.",
    "A defesa aérea derrubou 2 mísseis|sobre a cidade, e os moradores|receberam um alerta no celular para se proteger.",
    "Outro míssil foi derrubado no sul do país,|e um drone no leste, onde fica|a maior parte do petróleo saudita.",
    "Os sauditas culpam os houthis,|um grupo armado do Iêmen|apoiado pelo Irã.",
    "Um dia antes, o oleoduto Leste-Oeste|foi atacado de novo, mas o fogo foi apagado|e o petróleo seguiu passando.",
    "Por que isso importa? Com o Irã restringindo|o estreito de Ormuz, esse oleoduto até o Mar Vermelho|virou uma saída vital para o petróleo.",
    "E a imprensa dos houthis diz que aviões sauditas|atacaram instalações de gás e petróleo|em Sanaa, no Iêmen.",]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Riad', 4), (0, 'explosoes', 4), (1, 'dois', 4), (1, 'alerta', 4), (2, 'sul', 4), (2, 'drone', 4),
         (2, 'petroleo', 4), (3, 'houthis', 4), (3, 'Ira', 4), (4, 'oleoduto', 4), (4, 'apagado', 4),
         (5, 'Ormuz', 4), (5, 'Vermelho', 4), (5, 'vital', 4), (6, 'avioes', 4), (6, 'Sanaa', 4)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); WHITE = (255, 255, 255)
SEA = hexc('#3d7fb8'); SEA_D = hexc('#2c6396'); SAND = hexc('#e2c48e'); SAND_D = hexc('#b89a64')
KSA = hexc('#7fb77e'); KSA_D = hexc('#5a8f5a'); YEM = hexc('#e8a05c'); YEM_D = hexc('#b8773a')
IRN = hexc('#c9b6e0'); IRN_D = hexc('#9a86b3'); LIT = hexc('#ffd65a'); DARK = hexc('#2b2d3a')
NIGHT = hexc('#1b2140'); NIGHT2 = hexc('#2c3561'); GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e')
PIPE = hexc('#9aa3ad'); PIPE_D = hexc('#69717b'); FIRE = hexc('#ff8a2a'); FIRE2 = hexc('#ffd24a')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def morador(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#3b2a1e', shirt='#3f7fbf'):
    """morador genérico de camisa (feijão). 600x1000, pés y~975."""
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(shirt); P.COAT_D = mul(hexc(shirt), .72)
    try:
        img = P.scientist(expr=expr, arms=arms, blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
    finally:
        P.COAT, P.COAT_D = oc, od
    return img


def put_mor(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'morador', x, feet, h, f, seed, **kw)


def politico(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550'):
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(suit); P.COAT_D = mul(hexc(suit), .7)
    try:
        img = P.scientist(expr=expr, arms=arms, blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
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


def noite(c, chao=1500):
    d = ImageDraw.Draw(c)
    for i in range(16):
        y0 = i * 100
        col = tuple(int(NIGHT[k] + (NIGHT2[k] - NIGHT[k]) * i / 15) for k in range(3))
        d.rectangle([0, y0, 1242, y0 + 100], fill=col)
    for i in range(30):
        x = (i * 397) % 1242; y = 330 + (i * 211) % 700
        d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(230, 230, 255))
    d.rectangle([0, chao, 1242, 2208], fill=hexc('#6b5a45'))
    d.rectangle([0, chao, 1242, chao + 20], fill=hexc('#55473a'))


def predio(c, x, base, w, h, seed=0, lit=.7, torre=False):
    d = ImageDraw.Draw(c)
    col = hexc(['#c9b38f', '#b9a582', '#d4c2a0', '#a99877'][seed % 4])
    if torre:
        d.polygon([(x - w / 2, base), (x - w * .22, base - h), (x + w * .22, base - h), (x + w / 2, base)], fill=col, outline=INK, width=6)
        d.ellipse([x - w * .22, base - h - 30, x + w * .22, base - h + 30], fill=col, outline=INK, width=6)
        for k in range(8):
            yy = base - h + 70 + k * (h - 120) / 8
            ww = w * (.22 + .28 * (yy - (base - h)) / h)
            d.line([(x - ww + 20, yy), (x + ww - 20, yy)], fill=LIT if (k + seed) % 3 else DARK, width=10)
        return
    d.rounded_rectangle([x - w / 2, base - h, x + w / 2, base], 8, fill=col, outline=INK, width=6)
    cols = max(2, int(w // 80)); rows = max(2, int(h // 95))
    k = 0
    for r in range(rows):
        for q in range(cols):
            wx = x - w / 2 + 25 + q * (w - 50) / cols; wy = base - h + 30 + r * (h - 60) / rows
            on = ((k * 37 + seed * 11) % 97) / 97 < lit
            d.rectangle([wx + 6, wy, wx + (w - 50) / cols - 6, wy + (h - 60) / rows - 22], fill=LIT if on else DARK, outline=INK, width=3)
            k += 1


def clarao(c, x, y, t, s=1.0):
    """clarão de interceptação no céu (símbolo, sem violência). t 0..1"""
    if t <= 0 or t >= 1: return
    d = ImageDraw.Draw(c, 'RGBA')
    r = (40 + 160 * easeOut(t)) * s
    a = int(230 * (1 - t))
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 220, 120, a // 2))
    r2 = r * .55
    d.ellipse([x - r2, y - r2, x + r2, y + r2], fill=(255, 250, 220, a))
    for k in range(10):
        an = k * math.pi / 5
        d.line([(x + r * .6 * math.cos(an), y + r * .6 * math.sin(an)), (x + r * 1.1 * math.cos(an), y + r * 1.1 * math.sin(an))],
               fill=(255, 235, 160, a), width=int(8 * s))


def rastro(c, x0, y0, x1, y1, t, cor=(255, 255, 255)):
    """rastro de fumaça de um míssil indo de (x0,y0) a (x1,y1); t 0..1"""
    if t <= 0: return
    d = ImageDraw.Draw(c, 'RGBA')
    n = 18
    for i in range(n):
        u = i / n * t
        x = lerp(x0, x1, u); y = lerp(y0, y1, u) - 120 * math.sin(math.pi * u)
        r = 10 + 10 * (1 - u / max(t, 1e-3))
        d.ellipse([x - r, y - r, x + r, y + r], fill=cor + (int(160 * (u / max(t, 1e-3))),))
    x = lerp(x0, x1, t); y = lerp(y0, y1, t) - 120 * math.sin(math.pi * t)
    d.ellipse([x - 12, y - 12, x + 12, y + 12], fill=(255, 210, 120, 255))


@lru_cache(maxsize=2)
def celular():
    """celular com alerta na tela. 360x640"""
    p = Pen(360, 640)
    p.shape([(20, 20), (340, 20), (340, 620), (20, 620)], hexc('#2b2d3a'), hexc('#1a1b24'), 7, 10)
    p.poly([(44, 70), (316, 70), (316, 560), (44, 560)], hexc('#f4f1ea'), 3)
    p.shape([(180, 120), (280, 290), (80, 290)], RED, RED_D, 5, 4)
    p.shape([(170, 170), (190, 170), (186, 240), (174, 240)], WHITE, WHITE, 2, 0)
    p.dot(180, 262, 10, WHITE, 2)
    p.dot(180, 595, 14, hexc('#4a4d5c'), 3)
    return fin(p)


@lru_cache(maxsize=2)
def mapa_arabia():
    """mapa simples: península Arábica (Arábia Saudita verde, Iêmen laranja), Irã lilás em cima, Golfo e Mar Vermelho."""
    S = 2
    im = Image.new('RGBA', (BW * S, BH * S), SEA + (255,))
    d = ImageDraw.Draw(im)
    for y in range(420, 1500, 70):
        for x in range(60 + (y // 70 % 2) * 90, BW, 180):
            d.line([(x * S, y * S), ((x + 40) * S, (y - 8) * S), ((x + 80) * S, y * S)], fill=SEA_D, width=4 * S)

    def land(pts, col, cold):
        P2 = [(x * S, y * S) for x, y in pts]
        d.polygon([(x, y + 14 * S) for x, y in P2], fill=INK)
        d.polygon([(x, y + 8 * S) for x, y in P2], fill=cold)
        d.polygon(P2, fill=col)
        d.line(P2 + [P2[0]], fill=INK, width=5 * S)

    land([(-20, -20), (BW + 20, -20), (BW + 20, 560), (1170, 560), (1100, 530), (1000, 470), (900, 410), (780, 380), (-20, 380)], IRN, IRN_D)
    land([(120, 380), (780, 380), (860, 560), (940, 700), (1020, 720), (1080, 640), (1140, 610), (1200, 760), (1160, 940),
          (1040, 1120), (820, 1240), (600, 1330), (520, 1360), (470, 1260), (400, 1100), (300, 920), (200, 720)], KSA, KSA_D)
    land([(390, 1080), (560, 1090), (760, 1070), (900, 1180), (820, 1240), (600, 1330), (520, 1360), (470, 1260)], YEM, YEM_D)
    land([(900, 1180), (1040, 1120), (1160, 940), (1200, 760), (1150, 700), (1060, 900), (960, 1060)], SAND, SAND_D)
    # faixa de terra ao norte (só para fechar o mapa) já está no polígono de cima
    return im.resize((BW, BH), Image.LANCZOS)


RIAD = (700, 800); SANAA = (530, 1230); SUL = (450, 1010); LESTE = (950, 760); YANBU = (290, 760); ORMUZ = (1155, 585)


@lru_cache(maxsize=2)
def marcador():
    p = Pen(200, 280)
    p.shape([(100, 272), (30, 120), (40, 60), (100, 20), (160, 60), (170, 120)], RED, RED_D, 6, 8)
    p.dot(100, 100, 34, WHITE, 5)
    return fin(p)


def marca(c, x, y, f, f0, s=.45):
    if f >= f0: paste_c(c, marcador(), x, y - 60 * s, back(ramp(f, f0, f0 + 8)) * s)


@lru_cache(maxsize=2)
def barril():
    p = Pen(200, 260)
    p.shape([(30, 30), (170, 30), (178, 130), (170, 230), (30, 230), (22, 130)], hexc('#2f3a4a'), hexc('#1e2633'), 5, 10)
    p.shape(ell_pts(100, 32, 70, 18, 24), hexc('#46566b'), hexc('#2f3a4a'), 4, 3)
    for y in (90, 170): p.stroke([(24, y), (176, y)], 6, hexc('#5c6d84'))
    p.poly([(60, 115), (140, 115), (140, 145), (60, 145)], GOLD, 3)
    return fin(p)


@lru_cache(maxsize=2)
def drone():
    p = Pen(600, 220)
    gr = hexc('#9aa0a8'); grd = hexc('#6e747c')
    p.shape([(220, 60), (300, 20), (360, 20), (380, 60)], gr, grd, 4, 4)
    p.shape([(40, 110), (520, 95), (580, 112), (520, 135), (40, 130)], gr, grd, 5, 8)
    p.shape([(470, 92), (540, 94), (560, 108), (480, 112)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 2)
    p.shape([(40, 110), (10, 60), (40, 60), (80, 112)], gr, grd, 4, 3)
    p.shape([(40, 128), (10, 180), (40, 180), (80, 128)], gr, grd, 4, 3)
    return fin(p)


def navio():
    """petroleiro de lado, proa à direita. 700x300."""
    p = Pen(700, 300)
    h = hexc('#c0392b')
    p.shape([(20, 150), (690, 150), (640, 270), (60, 270)], h, mul(h, .7), 5, 10)
    p.shape([(40, 230), (660, 230), (640, 270), (60, 270)], hexc('#2a2a33'), hexc('#1a1a20'), 4, 3)
    p.shape([(30, 132), (680, 132), (690, 152), (20, 152)], hexc('#e9e4da'), hexc('#bdb6a8'), 4, 3)
    p.shape([(60, 40), (190, 40), (190, 134), (60, 134)], WHITE, hexc('#c9c9d2'), 5, 6)
    for x in (80, 115, 150): p.poly([(x, 60), (x + 22, 60), (x + 22, 80), (x, 80)], hexc('#7fb6e0'), 3)
    p.shape([(140, 0), (180, 0), (180, 42), (140, 42)], h, mul(h, .7), 4, 3)
    return p.img


def fumaca(c, x, y, f, seed=0, s=1.0, cor=(110, 110, 120)):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(6):
        t = ((f * .7 + i * 17 + seed * 7) % 100) / 100
        r = (26 + 55 * t) * s
        xx = x + 40 * math.sin(t * 5 + seed) * s; yy = y - 250 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=cor + (a,))


def fogo(c, x, y, f, s=1.0):
    if s <= .03: return
    d = ImageDraw.Draw(c)
    for k, (col, sc) in enumerate(((FIRE, 1.0), (FIRE2, .6))):
        w = 70 * s * sc; h = (150 + 20 * math.sin(f * .6 + k)) * s * sc
        pts = [(x - w, y), (x - w * .6, y - h * .5), (x - w * .3, y - h * .75), (x, y - h), (x + w * .3, y - h * .7),
               (x + w * .6, y - h * .45), (x + w, y)]
        d.polygon(pts, fill=col, outline=INK if k == 0 else None, width=5 if k == 0 else 0)


def oleoduto(c, y, f, x0=-40, x1=1290):
    d = ImageDraw.Draw(c)
    for x in range(int(x0) + 80, int(x1), 260):
        d.rectangle([x - 14, y + 30, x + 14, y + 120], fill=PIPE_D, outline=INK, width=5)
    d.rounded_rectangle([x0, y - 45, x1, y + 45], 40, fill=PIPE, outline=INK, width=7)
    d.rectangle([x0 + 10, y - 30, x1 - 10, y - 16], fill=hexc('#c3cad2'))
    for x in range(int(x0) + 200, int(x1), 260):
        d.rectangle([x - 18, y - 52, x + 18, y + 52], fill=PIPE_D, outline=INK, width=5)
    # gotas de petróleo correndo dentro (setas)
    for i in range(5):
        xx = x0 + ((f * 6 + i * 280) % (x1 - x0))
        d.polygon([(xx, y - 14), (xx + 40, y), (xx, y + 14)], fill=hexc('#2f3a4a'))


# ------------------------------------------------------------------ cenas
CIDADE = [(120, 260, 520, 0, False), (360, 220, 700, 1, False), (640, 260, 980, 2, True), (900, 240, 620, 3, False), (1150, 240, 760, 1, False)]


def cidade_riad(c, lit=.7):
    noite(c, 1520)
    for x, w, h, sd, tw in CIDADE:
        predio(c, x, 1540, w, h, sd, lit, tw)


def s0(f):
    """gancho: Riad à noite, clarões no céu."""
    c = CEN('cidade', 'dusk').copy()
    cidade_riad(c)
    r0 = wt(0, 'Riad') - 3
    e0 = wt(0, 'explosoes') - 3
    m0 = wt(0, 'madrugada') - 3
    for i, (x, y, dt) in enumerate([(300, 420, 0), (900, 360, 7), (620, 300, 15), (1040, 560, 24)]):
        tt = (f - e0 - dt) / 26
        clarao(c, x, y, tt, .9)
        clarao(c, x, y, (f - e0 - dt - 60) / 26, .7)
    num(c, 'RIAD', 640, 1010, f, r0, 190, -4)
    num(c, 'ARÁBIA SAUDITA', 640, 1180, f, r0 + 8, 90, 3)
    num(c, 'EXPLOSÕES NO CÉU', 640, 640, f, e0 + 4, 80, -2)
    num(c, 'MADRUGADA DE TERÇA', 640, 1340, f, m0, 62, -2)
    z = lerp(1.3, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, e0, .8)
    return c, (640, 1000 + k * 8, z, k), 'dusk'


def s1(f):
    """defesa aérea derruba 2 mísseis; morador recebe alerta no celular."""
    c = CEN('cidade', 'dusk').copy()
    cidade_riad(c, .5)
    d0 = wt(1, 'derrubou') - 3
    n0 = wt(1, 'dois') - 3
    a0 = wt(1, 'alerta') - 3
    p0 = wt(1, 'proteger') - 3
    # 2 mísseis vindo da esquerda e interceptados
    for i, (yy, xx) in enumerate([(380, 760), (500, 980)]):
        t = ramp(f, d0 - 20 + i * 6, d0 + 6 + i * 6)
        if t < 1:
            rastro(c, -60, yy + 200, xx, yy, t)
        clarao(c, xx, yy - 0, (f - d0 - 6 - i * 6) / 24, .8)
    num(c, '2 MÍSSEIS', 640, 560, f, n0, 140, -3)
    num(c, 'DERRUBADOS', 640, 720, f, n0 + 6, 90, 3)
    if f >= a0:
        put_mor(c, 360, 1560, 560, f, 3, expr='shock', arms='cheek', look=1, hair='#2a2020', shirt='#e9e4da')
        paste_c(c, celular(), 820, 1180, back(ramp(f, a0, a0 + 8)) * .85)
        num(c, 'ALERTA', 820, 1460, f, a0 + 2, 80, -3)
        if f >= p0:
            num(c, 'PROTEJA-SE', 820, 940, f, p0, 72, 3)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    k = kick(f, d0 + 6, .7)
    cy = lerp(950, 1120, smooth(ramp(f, a0 - 10, a0 + 20)))
    return c, (640, cy + k * 6, z, k), 'dusk'


def s2(f):
    """mapa: míssil no sul, drone no leste, região do petróleo."""
    c = mapa_arabia().copy()
    s0_ = wt(2, 'sul') - 3
    dr0 = wt(2, 'drone') - 3
    l0 = wt(2, 'leste') - 3
    pe0 = wt(2, 'petroleo') - 3
    num(c, 'ARÁBIA SAUDITA', 600, 600, f, 0, 70, -2)
    marca(c, *RIAD, f, 0, .35)
    num(c, 'RIAD', RIAD[0], RIAD[1] + 50, f, 0, 50, 0)
    if f >= s0_:
        marca(c, *SUL, f, s0_, .45)
        clarao(c, SUL[0], SUL[1] - 160, (f - s0_ - 4) / 22, .6)
        num(c, 'SUL: 1 MÍSSIL', SUL[0] + 30, SUL[1] + 30, f, s0_ + 2, 56, -2)
    if f >= dr0:
        tt = ramp(f, dr0 - 4, dr0 + 22)
        if tt < 1:
            paste_c(c, drone().resize((160, 58)), lerp(1250, LESTE[0] + 40, tt), LESTE[1] - 200, 1)
        clarao(c, LESTE[0] + 40, LESTE[1] - 200, (f - dr0 - 22) / 22, .6)
        num(c, 'LESTE: 1 DRONE', 920, 900, f, l0, 52, 2)
    if f >= pe0:
        for i, (bx, by) in enumerate([(930, 1010), (1030, 1020), (980, 1080)]):
            paste_c(c, barril(), bx, by, back(ramp(f, pe0 + i * 3, pe0 + i * 3 + 8)) * .42)
        num(c, 'MAIOR PARTE DO PETRÓLEO', 640, 1430, f, pe0, 56, -2)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 150))) * (1 + .0005 * f)
    cx = lerp(640, 700, smooth(ramp(f, dr0 - 10, dr0 + 30)))
    k = kick(f, s0_, .5)
    return c, (cx, 950 + k * 6, z, k), 'dusk'


def s3(f):
    """culpa: seta do Iêmen até Riad; Irã apoia."""
    c = mapa_arabia().copy()
    co0 = wt(3, 'sauditas') - 3
    h0 = wt(3, 'houthis') - 3
    y0 = wt(3, 'Iemen') - 3
    i0 = wt(3, 'Ira') - 3
    marca(c, *RIAD, f, 0, .35)
    num(c, 'RIAD', RIAD[0], RIAD[1] + 50, f, 0, 50, 0)
    if f >= h0:
        t = ramp(f, h0, h0 + 24)
        d = ImageDraw.Draw(c)
        pts = []
        for k in range(int(30 * t) + 1):
            u = k / 30
            pts.append((lerp(SANAA[0], RIAD[0], u) - 160 * math.sin(math.pi * u), lerp(SANAA[1], RIAD[1] + 40, u)))
        for k in range(0, len(pts) - 1, 2):
            d.line([pts[k], pts[k + 1]], fill=RED, width=14)
    num(c, 'SAUDITAS CULPAM:', 560, 560, f, co0, 58, -2)
    num(c, 'HOUTHIS', SANAA[0] + 40, SANAA[1] - 20, f, h0, 80, -3)
    num(c, 'IÊMEN', SANAA[0] + 40, SANAA[1] + 80, f, y0, 56, 2)
    if f >= i0:
        num(c, 'APOIADOS PELO IRÃ', 760, 330, f, i0, 64, 2)
        d = ImageDraw.Draw(c)
        a = int(60 * (0.5 + .5 * math.sin(f * .3)))
    z = lerp(1.04, 1.0, smooth(ramp(f, 0, 60))) * (1 + .0006 * f)
    cy = lerp(1000, 820, smooth(ramp(f, i0 - 10, i0 + 20)))
    k = kick(f, h0, .5)
    return c, (640, cy + k * 6, z, k), 'dusk'


def s4(f):
    """oleoduto no deserto: pequeno incêndio que se apaga; petróleo segue."""
    c = CEN('deserto', 'dusk').copy()
    o0 = wt(4, 'oleoduto') - 3
    n0 = wt(4, 'novo') - 3
    a0 = wt(4, 'apagado') - 3
    p0 = wt(4, 'passando') - 3
    oleoduto(c, 1320, f)
    fs = back(ramp(f, n0, n0 + 8)) * (1 - smooth(ramp(f, a0, a0 + 14)))
    if f >= n0:
        fogo(c, 760, 1275, f, fs)
        fumaca(c, 760, 1150, f, 3, .9 if f < a0 + 30 else .5)
    num(c, 'SEGUNDA-FEIRA', 640, 460, f, 0, 70, -3)
    num(c, 'OLEODUTO LESTE-OESTE', 640, 600, f, o0, 72, 2)
    num(c, 'ATACADO DE NOVO', 640, 740, f, n0, 70, -2)
    if f >= a0:
        num(c, 'FOGO APAGADO', 640, 900, f, a0, 80, 3)
    if f >= p0:
        num(c, 'PETRÓLEO SEGUE', 640, 1040, f, p0, 66, -2)
    z = lerp(1.02, 1.1, smooth(ramp(f, 0, 200))) * (1 + .0004 * f)
    k = kick(f, n0, .7)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 200))), 1000 + k * 6, z, k), 'dusk'


def s5(f):
    """por que importa: Ormuz restrito; rota pelo oleoduto até o Mar Vermelho."""
    c = mapa_arabia().copy()
    o0 = wt(5, 'Ormuz') - 3
    ol0 = wt(5, 'oleoduto') - 3
    v0 = wt(5, 'Vermelho') - 3
    vi0 = wt(5, 'vital') - 3
    num(c, 'POR QUE IMPORTA?', 640, 300, f, 0, 84, -3)
    d = ImageDraw.Draw(c)
    if f >= o0:
        s = back(ramp(f, o0, o0 + 8))
        r = 60 * s
        d.line([(ORMUZ[0] - r, ORMUZ[1] - r), (ORMUZ[0] + r, ORMUZ[1] + r)], fill=INK, width=30)
        d.line([(ORMUZ[0] - r, ORMUZ[1] + r), (ORMUZ[0] + r, ORMUZ[1] - r)], fill=INK, width=30)
        d.line([(ORMUZ[0] - r, ORMUZ[1] - r), (ORMUZ[0] + r, ORMUZ[1] + r)], fill=RED, width=18)
        d.line([(ORMUZ[0] - r, ORMUZ[1] + r), (ORMUZ[0] + r, ORMUZ[1] - r)], fill=RED, width=18)
        num(c, 'ORMUZ', 1060, 460, f, o0, 64, -3)
    if f >= ol0:
        t = smooth(ramp(f, ol0, ol0 + 30))
        xe = lerp(LESTE[0], YANBU[0], t)
        d.line([(LESTE[0], LESTE[1]), (xe, lerp(LESTE[1], YANBU[1], t))], fill=INK, width=30)
        d.line([(LESTE[0], LESTE[1]), (xe, lerp(LESTE[1], YANBU[1], t))], fill=PIPE, width=18)
        for i in range(4):
            u = ((f * .02 + i * .25) % 1) * t
            bx = lerp(LESTE[0], YANBU[0], u)
            d.polygon([(bx + 16, LESTE[1] - 10), (bx - 14, LESTE[1]), (bx + 16, LESTE[1] + 10)], fill=hexc('#2f3a4a'))
    if f >= v0:
        num(c, 'MAR', 240, 1130, f, v0, 50, -4); num(c, 'VERMELHO', 260, 1200, f, v0 + 2, 50, -4)
        tt = smooth(ramp(f, v0, v0 + 70))
        im = sprite('navio', (), 70, 700 / 300, True)
        paste_c(c, im, lerp(YANBU[0] - 40, 150, tt), lerp(YANBU[1] + 40, 560, tt), 1)
    if f >= vi0:
        num(c, 'SAÍDA VITAL', 640, 1420, f, vi0, 90, 3)
    z = lerp(1.0, 1.06, smooth(ramp(f, 0, 220))) * (1 + .0004 * f)
    k = kick(f, o0, .6)
    return c, (640, 900 + k * 6, z, k), 'dusk'


def s6(f):
    """Sanaa: fumaça ao longe, versão dos houthis, não confirmada."""
    c = CEN('cidade', 'dusk').copy()
    noite(c, 1520)
    for x, w, h, sd in [(160, 280, 560, 2), (430, 240, 440, 0), (820, 260, 520, 3), (1100, 240, 420, 1)]:
        predio(c, x, 1540, w, h, sd, .6)
    i0 = wt(6, 'imprensa') - 3
    av0 = wt(6, 'avioes') - 3
    g0 = wt(6, 'gas') - 3
    s0_ = wt(6, 'Sanaa') - 3
    if f >= g0:
        fumaca(c, 640, 1100, f, 2, 1.3, (95, 95, 110))
        fumaca(c, 980, 1150, f, 5, 1.0, (95, 95, 110))
    if f >= av0:
        t = ramp(f, av0, av0 + 40)
        d = ImageDraw.Draw(c)
        x = lerp(-100, 1350, t)
        d.polygon([(x, 520), (x - 120, 500), (x - 160, 470), (x - 140, 520), (x - 170, 540), (x - 60, 540)], fill=hexc('#4a4d5c'), outline=INK, width=4)
    num(c, 'SEGUNDO OS HOUTHIS', 640, 420, f, i0, 66, -2)
    num(c, 'GÁS E PETRÓLEO', 640, 700, f, g0, 84, 3)
    num(c, 'SANAA, IÊMEN', 640, 860, f, s0_, 96, -3)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 160))) * (1 + .0004 * f)
    k = kick(f, g0, .5)
    return c, (640, 1000 + k * 6, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'explosoes') - 3, 140, .6)
    s.ting(s.W(0, 'Riad') - 3, .25)
    s.whoosh(s.W(1, 'derrubou') - 20, .3) if hasattr(s, 'whoosh') else None
    s.thunk(s.W(1, 'dois') - 3, 150, .5)
    s.ting(s.W(1, 'alerta') - 3, .35)
    s.thunk(s.W(2, 'sul') - 3, 140, .4)
    s.engine(s.W(2, 'drone') - 6, s.W(2, 'drone') + 30, .07)
    s.ting(s.W(3, 'houthis') - 3, .25)
    s.thunk(s.W(4, 'novo') - 3, 140, .5)
    s.ting(s.W(4, 'apagado') - 3, .3)
    s.thunk(s.W(5, 'Ormuz') - 3, 150, .6)
    s.ting(s.W(5, 'vital') - 3, .3)
    s.engine(s.W(6, 'avioes') - 3, s.W(6, 'avioes') + 40, .08)
