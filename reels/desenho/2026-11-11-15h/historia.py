"""Um Café com o Mundo — O MUNDO EXPLICADO (quarta 11/11/2026, 15h).
Tema: drones invadem o céu dos países bálticos; Lituânia, Letônia e Estônia mandam moradores se abrigar (madrugada 10->11/11).
Fontes (conferidas em 11/11/2026):
- Reuters (via Cyprus Mail, 11/11/2026, "NATO jets scrambled as drone alerts sweep Baltic states"): Lituânia, Letônia e
  Estônia emitiram de madrugada alertas para a população se abrigar de drones não identificados vindos da Rússia ou de
  Belarus, retirados horas depois; um alerta cobriu Kaunas, 2ª maior cidade da Lituânia, ~300 mil moradores; o
  primeiro-ministro lituano Mindaugas Sinkevicius disse que 4 drones foram detectados na região; caças da Otan foram
  acionados; houve tentativa de derrubar um drone sobre o norte da Lituânia (não se sabe se foi atingido); restos de um
  míssil da Otan foram achados no chão; sem feridos; Finlândia restringiu por um tempo o ar e o mar no leste do Golfo da
  Finlândia; Kiev diz que interferência russa de sinal desviou alguns de seus drones; Moscou acusa Kiev de usar o espaço
  aéreo da Otan como cobertura; negociações Rússia-Ucrânia em Abu Dhabi (2 dias, desde terça).
- Just Security Early Edition 11/11/2026 (resumo Reuters: pelo menos 4 drones de ataques ucranianos à Rússia entraram no
  espaço aéreo báltico, caças da Otan decolaram, alertas nos 3 países, sem feridos).
Tom sério; sem violência mostrada; personagens genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Nesta madrugada, três países da Otan mandaram a população se abrigar por causa de drones.",
    "Os alertas soaram na Lituânia, na Letônia e na Estônia, contra drones vindos da Rússia ou de Belarus.",
    "Um deles cobriu Kaunas, a segunda maior cidade lituana, com cerca de trezentos mil moradores.",
    "Quatro drones foram detectados na região, e caças da Otan decolaram.",
    "Houve uma tentativa de derrubar um deles, e restos de um míssil da Otan foram achados no chão. Ninguém se feriu.",
    "Por que isso importa? A Ucrânia diz que bloqueios de sinal russos desviam seus drones, e Moscou acusa Kiev de usar o céu da Otan como escudo.",
    "E tudo isso enquanto Rússia e Ucrânia negociam a paz em Abu Dhabi.",
]
CAPTXT = [
    "Nesta madrugada, 3 países da Otan|mandaram a população se abrigar|por causa de drones.",
    "Os alertas soaram na Lituânia, na Letônia e na Estônia,|contra drones vindos da Rússia ou de Belarus.",
    "Um deles cobriu Kaunas, a 2ª maior cidade lituana,|com cerca de 300 mil moradores.",
    "4 drones foram detectados na região,|e caças da Otan decolaram.",
    "Houve uma tentativa de derrubar um deles,|e restos de um míssil da Otan foram achados no chão.|Ninguém se feriu.",
    "Por que isso importa? A Ucrânia diz que bloqueios de sinal russos|desviam seus drones, e Moscou acusa Kiev|de usar o céu da Otan como escudo.",
    "E tudo isso enquanto Rússia e Ucrânia|negociam a paz em Abu Dhabi.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'tres', 4), (0, 'abrigar', 4), (1, 'Lituania', 4), (1, 'Estonia', 4), (1, 'Belarus', 4), (2, 'Kaunas', 4),
         (2, 'trezentos', 4), (3, 'Quatro', 4), (3, 'cacas', 6), (4, 'tentativa', 4), (4, 'restos', 4), (4, 'Ninguem', 4),
         (5, 'bloqueios', 4), (5, 'escudo', 4), (6, 'paz', 4)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); BLUE = hexc('#2f6fd6'); WHITE = (255, 255, 255)
SEA = hexc('#3d7fb8'); SEA_D = hexc('#2c6396')
NATO = hexc('#7fb77e'); NATO_D = hexc('#5a8f5a'); FIN = hexc('#a9d3a0'); FIN_D = hexc('#7fae76')
RUS = hexc('#d9a7a0'); RUS_D = hexc('#b07e77'); BLR = hexc('#e8b86c'); BLR_D = hexc('#b98c45'); POL = hexc('#e2d4b4'); POL_D = hexc('#b9aa88')
LIT = hexc('#ffd65a'); DARK = hexc('#2b2d3a'); NIGHT = hexc('#1b2140'); NIGHT2 = hexc('#2c3561')
UBLUE = hexc('#0057b7'); UYEL = hexc('#ffd700'); RU_R = hexc('#d52b1e'); RU_B = hexc('#0039a6'); TEAL = hexc('#2a9d8f')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def morador(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#3b2a1e', shirt='#3f7fbf'):
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


def noite(c, chao=1500, solo='#4a5a48'):
    d = ImageDraw.Draw(c)
    for i in range(16):
        y0 = i * 100
        col = tuple(int(NIGHT[k] + (NIGHT2[k] - NIGHT[k]) * i / 15) for k in range(3))
        d.rectangle([0, y0, 1242, y0 + 100], fill=col)
    for i in range(30):
        x = (i * 397) % 1242; y = 330 + (i * 211) % 700
        d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(230, 230, 255))
    d.rectangle([0, chao, 1242, 2208], fill=hexc(solo))
    d.rectangle([0, chao, 1242, chao + 20], fill=mul(hexc(solo), .8))


def predio(c, x, base, w, h, seed=0, lit=.7, telhado=False):
    """prédio europeu genérico (telhado pontudo opcional)."""
    d = ImageDraw.Draw(c)
    col = hexc(['#c9a98f', '#a9b4c2', '#d4c2a0', '#b5a3b8'][seed % 4])
    d.rounded_rectangle([x - w / 2, base - h, x + w / 2, base], 8, fill=col, outline=INK, width=6)
    if telhado:
        d.polygon([(x - w / 2 - 10, base - h), (x, base - h - w * .55), (x + w / 2 + 10, base - h)], fill=hexc('#a0473c'), outline=INK, width=6)
    cols = max(2, int(w // 80)); rows = max(2, int(h // 95))
    k = 0
    for r in range(rows):
        for q in range(cols):
            wx = x - w / 2 + 25 + q * (w - 50) / cols; wy = base - h + 30 + r * (h - 60) / rows
            on = ((k * 37 + seed * 11) % 97) / 97 < lit
            d.rectangle([wx + 6, wy, wx + (w - 50) / cols - 6, wy + (h - 60) / rows - 22], fill=LIT if on else DARK, outline=INK, width=3)
            k += 1


CIDADE = [(120, 250, 560, 0, True), (370, 230, 760, 1, False), (630, 240, 640, 2, True), (890, 240, 820, 3, False), (1140, 230, 600, 1, True)]


def cidade(c, lit=.7):
    noite(c, 1520, '#5b5b62')
    for x, w, h, sd, tl in CIDADE:
        predio(c, x, 1540, w, h, sd, lit, tl)


def sirene(c, x, y, f, f0, r=34):
    if f < f0: return
    d = ImageDraw.Draw(c, 'RGBA')
    on = (f // 8) % 2 == 0
    col = RED if on else BLUE
    d.ellipse([x - r - 40, y - r - 40, x + r + 40, y + r + 40], fill=col + (90,))
    d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=INK, width=5)


def clarao(c, x, y, t, s=1.0):
    if t <= 0 or t >= 1: return
    d = ImageDraw.Draw(c, 'RGBA')
    r = (40 + 160 * easeOut(t)) * s
    a = int(230 * (1 - t))
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 220, 120, a // 2))
    r2 = r * .55
    d.ellipse([x - r2, y - r2, x + r2, y + r2], fill=(255, 250, 220, a))


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
def drone():
    """drone genérico de lado, voando p/ direita. 600x220"""
    p = Pen(600, 220)
    gr = hexc('#9aa0a8'); grd = hexc('#6e747c')
    p.shape([(220, 60), (300, 20), (360, 20), (380, 60)], gr, grd, 4, 4)
    p.shape([(40, 110), (520, 95), (580, 112), (520, 135), (40, 130)], gr, grd, 5, 8)
    p.shape([(470, 92), (540, 94), (560, 108), (480, 112)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 2)
    p.shape([(40, 110), (10, 60), (40, 60), (80, 112)], gr, grd, 4, 3)
    p.shape([(40, 128), (10, 180), (40, 180), (80, 128)], gr, grd, 4, 3)
    p.shape([(220, 112), (330, 112), (300, 200), (260, 200)], grd, mul(grd, .7), 4, 3)
    return fin(p)


@lru_cache(maxsize=16)
def drone_w(w, flip=False):
    im = drone().resize((w, int(w * 220 / 600)), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im


@lru_cache(maxsize=2)
def jato():
    """caça genérico de lado, voando p/ direita. 640x240"""
    p = Pen(640, 240)
    g = hexc('#8f96a0'); gd = hexc('#656b74')
    p.shape([(60, 40), (130, 40), (200, 110), (120, 110)], g, gd, 4, 4)
    p.shape([(30, 120), (480, 100), (620, 122), (480, 145), (30, 140)], g, gd, 5, 8)
    p.shape([(400, 96), (480, 100), (500, 112), (410, 114)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 2)
    p.shape([(220, 128), (360, 128), (250, 215), (190, 215)], gd, mul(gd, .7), 4, 3)
    p.dot(40, 130, 14, hexc('#f0a040'), 3)
    return fin(p)


@lru_cache(maxsize=8)
def jato_w(w):
    return jato().resize((w, int(w * 240 / 640)), Image.LANCZOS)


@lru_cache(maxsize=2)
def marcador():
    p = Pen(200, 280)
    p.shape([(100, 272), (30, 120), (40, 60), (100, 20), (160, 60), (170, 120)], RED, RED_D, 6, 8)
    p.dot(100, 100, 34, WHITE, 5)
    return fin(p)


def marca(c, x, y, f, f0, s=.45):
    if f >= f0: paste_c(c, marcador(), x, y - 60 * s, back(ramp(f, f0, f0 + 8)) * s)


@lru_cache(maxsize=2)
def mapa_baltico():
    """mapa simples: Finlândia em cima, Golfo da Finlândia, Estônia, Letônia, Lituânia (verde = Otan),
    Rússia à direita, Belarus embaixo à direita, Kaliningrado (Rússia) e Polônia embaixo à esquerda, mar Báltico à esquerda."""
    S = 2
    im = Image.new('RGBA', (BW * S, BH * S), SEA + (255,))
    d = ImageDraw.Draw(im)
    for y in range(420, 1500, 70):
        for x in range(60 + (y // 70 % 2) * 90, 600, 180):
            d.line([(x * S, y * S), ((x + 40) * S, (y - 8) * S), ((x + 80) * S, y * S)], fill=SEA_D, width=4 * S)

    def land(pts, col, cold):
        P2 = [(x * S, y * S) for x, y in pts]
        d.polygon([(x, y + 14 * S) for x, y in P2], fill=INK)
        d.polygon([(x, y + 8 * S) for x, y in P2], fill=cold)
        d.polygon(P2, fill=col)
        d.line(P2 + [P2[0]], fill=INK, width=5 * S)

    land([(-20, -20), (BW + 20, -20), (BW + 20, 1700), (1000, 1700), (960, 1280), (900, 1080), (930, 860), (880, 660), (860, 560), (1000, 520), (BW + 20, 480)], RUS, RUS_D)
    land([(200, -20), (840, -20), (860, 300), (900, 470), (800, 530), (640, 540), (480, 510), (330, 470), (260, 380), (220, 200)], FIN, FIN_D)
    land([(420, 640), (600, 610), (780, 620), (860, 640), (880, 660), (850, 760), (860, 820), (700, 800), (560, 830), (450, 790), (380, 720)], NATO, NATO_D)
    land([(330, 900), (400, 840), (450, 860), (500, 920), (560, 840), (700, 820), (860, 830), (930, 860), (920, 980), (880, 1040), (700, 1010), (520, 1030), (360, 1030), (320, 960)], NATO, NATO_D)
    land([(360, 1040), (520, 1040), (700, 1020), (880, 1050), (900, 1080), (860, 1170), (780, 1250), (660, 1300), (540, 1290), (440, 1240), (380, 1160)], NATO, NATO_D)
    land([(860, 1170), (900, 1080), (960, 1280), (1000, 1700), (560, 1700), (620, 1420), (660, 1300), (780, 1250)], BLR, BLR_D)
    land([(-20, 1330), (300, 1300), (440, 1300), (540, 1300), (660, 1310), (620, 1420), (560, 1700), (-20, 1700)], POL, POL_D)
    land([(250, 1230), (330, 1200), (430, 1230), (440, 1290), (300, 1300), (240, 1280)], RUS, RUS_D)
    return im.resize((BW, BH), Image.LANCZOS)


LIT_C = (620, 1150); LET_C = (640, 925); EST_C = (640, 715); KAUNAS = (560, 1200); NORTE_LT = (640, 1080)
RUS_C = (1080, 900); BLR_C = (800, 1460); FIN_C = (560, 300); GOLFO = (740, 580)


@lru_cache(maxsize=2)
def bandeira_ua():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 140), (10, 140)], UBLUE)
    p.poly([(10, 140), (410, 140), (410, 270), (10, 270)], UYEL)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_ru():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 96), (10, 96)], WHITE)
    p.poly([(10, 96), (410, 96), (410, 183), (10, 183)], RU_B)
    p.poly([(10, 183), (410, 183), (410, 270), (10, 270)], RU_R)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def escudo():
    p = Pen(400, 480)
    p.shape([(200, 20), (370, 80), (360, 260), (300, 380), (200, 460), (100, 380), (40, 260), (30, 80)], TEAL, mul(TEAL, .7), 7, 12)
    p.stroke([(130, 240), (185, 300), (285, 170)], 22, WHITE)
    return fin(p)


@lru_cache(maxsize=2)
def destrocos():
    """pedaços de metal retorcido no chão (restos de míssil, sem explosão). 520x200"""
    p = Pen(520, 200)
    g = hexc('#8a9099'); gd = hexc('#5d636b')
    p.shape([(30, 170), (90, 120), (200, 110), (230, 150), (180, 185), (60, 190)], g, gd, 5, 6)
    p.shape([(250, 180), (290, 90), (360, 70), (390, 120), (350, 185)], g, gd, 5, 6)
    p.shape([(400, 185), (430, 140), (500, 150), (490, 190)], gd, mul(gd, .7), 4, 4)
    p.stroke([(110, 150), (170, 140)], 6, hexc('#c3cad2'))
    p.stroke([(320, 110), (350, 100)], 6, hexc('#c3cad2'))
    return fin(p)


def mesa(c, cx, y):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([cx - 420, y, cx + 420, y + 60], 14, fill=hexc('#a8744a'), outline=INK, width=6)
    d.rectangle([cx - 380, y + 60, cx - 340, y + 260], fill=hexc('#7d5534'), outline=INK, width=5)
    d.rectangle([cx + 340, y + 60, cx + 380, y + 260], fill=hexc('#7d5534'), outline=INK, width=5)


def seta(c, pts, t, cor=RED, w=14):
    d = ImageDraw.Draw(c)
    n = max(2, int(len(pts) * t))
    sub = pts[:n]
    for k in range(0, len(sub) - 1, 2):
        d.line([sub[k], sub[k + 1]], fill=cor, width=w)


def curva(a, b, bend=120, n=30):
    return [(lerp(a[0], b[0], k / n) + bend * math.sin(math.pi * k / n), lerp(a[1], b[1], k / n)) for k in range(n + 1)]


# ------------------------------------------------------------------ cenas
def s0(f):
    """gancho: cidade báltica à noite, sirenes, drones cruzando o céu."""
    c = CEN('cidade', 'dusk').copy()
    cidade(c, .6)
    t0 = wt(0, 'tres') - 3; o0 = wt(0, 'Otan') - 3; a0 = wt(0, 'abrigar') - 3; d0 = wt(0, 'drones') - 3
    for i, x in enumerate((230, 640, 1050)):
        sirene(c, x, 1500, f + i * 4, a0 - 2, 28)
    for i, (y, dt) in enumerate(((440, 0), (580, 25))):
        tt = ramp(f, dt - 10, dt + 130)
        if 0 < tt < 1:
            paste_c(c, drone_w(240, True), lerp(1350, -150, tt), y + 20 * math.sin(f * .1 + i), 1)
    num(c, '3 PAÍSES DA OTAN', 640, 760, f, t0, 88, -3)
    num(c, 'MADRUGADA', 640, 900, f, 0, 70, 2)
    num(c, 'ABRIGUE-SE!', 640, 1140, f, a0, 130, 3)
    z = lerp(1.3, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, a0, .8)
    return c, (640, 1000 + k * 8, z, k), 'dusk'


def s1(f):
    """mapa: os 3 países acendem; setas da Rússia e de Belarus com drones."""
    c = mapa_baltico().copy()
    l0 = wt(1, 'Lituania') - 3; le0 = wt(1, 'Letonia') - 3; e0 = wt(1, 'Estonia') - 3
    r0 = wt(1, 'Russia') - 3; b0 = wt(1, 'Belarus') - 3
    num(c, 'RÚSSIA', 1040, 1180, f, 0, 56, -3)
    num(c, 'FINLÂNDIA', FIN_C[0], FIN_C[1], f, 0, 56, 2)
    num(c, 'LITUÂNIA', LIT_C[0], LIT_C[1], f, l0, 66, -2)
    num(c, 'LETÔNIA', LET_C[0], LET_C[1], f, le0, 66, 2)
    num(c, 'ESTÔNIA', EST_C[0], EST_C[1], f, e0, 66, -2)
    if f >= r0:
        t = smooth(ramp(f, r0, r0 + 24))
        pts = curva((1100, 1010), (830, 940), -50)
        seta(c, pts, t)
        x, y = pts[min(len(pts) - 1, int(30 * t))]
        paste_c(c, drone_w(120, True), x, y - 50, 1)
    if f >= b0:
        num(c, 'BELARUS', 800, 1500, f, b0, 60, 3)
        t = smooth(ramp(f, b0, b0 + 24))
        pts = curva((830, 1420), (700, 1190), 50)
        seta(c, pts, t)
        x, y = pts[min(len(pts) - 1, int(30 * t))]
        paste_c(c, drone_w(120, True), x, y - 50, 1)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 160))) * (1 + .0005 * f)
    cy = lerp(880, 1020, smooth(ramp(f, r0 - 10, b0 + 10)))
    k = kick(f, l0, .4)
    return c, (660, cy + k * 6, z, k), 'dusk'


def s2(f):
    """Kaunas: cidade à noite, marcador, morador com alerta no celular, 300 mil."""
    c = CEN('cidade', 'dusk').copy()
    cidade(c, .7)
    k0 = wt(2, 'Kaunas') - 3; s0_ = wt(2, 'segunda') - 3; t0 = wt(2, 'trezentos') - 3
    if f >= k0:
        paste_c(c, marcador(), 640, 360, back(ramp(f, k0, k0 + 8)) * .5)
        num(c, 'KAUNAS', 640, 520, f, k0, 140, -3)
    num(c, '2ª MAIOR CIDADE DA LITUÂNIA', 640, 680, f, s0_, 56, 2)
    if f >= t0:
        num(c, '300 MIL', 640, 860, f, t0, 150, -3)
        num(c, 'MORADORES', 640, 1010, f, t0 + 6, 70, 2)
    put_mor(c, 380, 1580, 560, f, 3, expr='nervous', arms='cheek', look=1, hair='#c9a46a', shirt='#3f7fbf')
    paste_c(c, celular(), 840, 1260, .62 + .01 * math.sin(f * .3))
    num(c, 'ALERTA', 840, 1460, f, 0, 60, -3)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    cy = lerp(880, 1060, smooth(ramp(f, t0 - 10, t0 + 30)))
    k = kick(f, t0, .5)
    return c, (640, cy + k * 6, z, k), 'dusk'


def s3(f):
    """céu noturno: 4 drones aparecem; caças da Otan decolam e cruzam."""
    c = CEN('neve', 'dusk').copy()
    noite(c, 1480, '#c9d3dc')
    q0 = wt(3, 'Quatro') - 3; r0 = wt(3, 'regiao') - 3; c0 = wt(3, 'cacas') - 3; d0 = wt(3, 'decolaram') - 3
    for i, (x, y) in enumerate(((260, 460), (560, 380), (840, 500), (1060, 410))):
        if f >= q0 + i * 4:
            s = back(ramp(f, q0 + i * 4, q0 + i * 4 + 8))
            paste_c(c, drone_w(220, True), x + 10 * math.sin(f * .08 + i), y + 8 * math.sin(f * .1 + i), s)
            dd = ImageDraw.Draw(c, 'RGBA')
            rr = 120 + 10 * math.sin(f * .2 + i)
            dd.ellipse([x - rr, y - rr, x + rr, y + rr], outline=(255, 90, 80, 200), width=6)
    num(c, '4 DRONES', 640, 700, f, q0, 150, -3)
    num(c, 'DETECTADOS', 640, 860, f, q0 + 8, 70, 2)
    if f >= c0 - 4:
        tt = ramp(f, c0 - 4, c0 + 50)
        for i, dy in enumerate((0, 110)):
            paste_c(c, jato_w(420), lerp(-300, 1500, tt) - i * 220, 1180 - 260 * tt + dy, 1)
        num(c, 'CAÇAS DA OTAN', 640, 1020, f, c0, 100, 3)
    z = lerp(1.04, 1.0, smooth(ramp(f, 0, 50))) * (1 + .0007 * f)
    k = kick(f, c0, .6)
    return c, (640, 960 + k * 6, z, k), 'dusk'


def s4(f):
    """norte da Lituânia: caça no céu, clarão distante; restos no chão; sem feridos."""
    c = CEN('floresta', 'dusk').copy()
    noite(c, 1480, '#4d6a46')
    d = ImageDraw.Draw(c)
    for i, x in enumerate(range(40, 1300, 150)):
        h = 260 + (i * 53) % 120
        d.polygon([(x - 70, 1490), (x, 1490 - h), (x + 70, 1490)], fill=hexc('#2f5a3a'), outline=INK, width=5)
    t0 = wt(4, 'tentativa') - 3; r0 = wt(4, 'restos') - 3; ch0 = wt(4, 'chao') - 3; n0 = wt(4, 'Ninguem') - 3
    if f >= t0 - 20:
        tt = ramp(f, t0 - 20, t0 + 40)
        paste_c(c, jato_w(380), lerp(-250, 1500, tt), 520 - 80 * tt, 1)
        paste_c(c, drone_w(150, True), 900 - 2 * (f - t0), 400, 1) if f < t0 + 30 else None
        clarao(c, 880, 420, (f - t0 - 18) / 24, .5)
    num(c, 'NORTE DA LITUÂNIA', 640, 300, f, 0, 64, -2)
    num(c, 'TENTATIVA DE DERRUBAR', 640, 700, f, t0, 76, 3)
    if f >= r0:
        paste_c(c, destrocos(), 640, 1440, back(ramp(f, r0, r0 + 8)) * .9)
        num(c, 'RESTOS DE MÍSSIL', 640, 900, f, r0, 84, -3)
        num(c, 'DA OTAN', 640, 1020, f, r0 + 6, 70, 2)
    if f >= n0:
        num(c, 'SEM FERIDOS', 640, 1200, f, n0, 110, -2)
    z = lerp(1.0, 1.07, smooth(ramp(f, 0, 200))) * (1 + .0004 * f)
    cy = lerp(860, 1080, smooth(ramp(f, r0 - 10, r0 + 30)))
    k = kick(f, r0, .5)
    return c, (640, cy + k * 6, z, k), 'dusk'


def s5(f):
    """por que importa: ondas de bloqueio de sinal desviam o drone; Rússia acusa: escudo da Otan."""
    c = mapa_baltico().copy()
    b0 = wt(5, 'bloqueios') - 3; dv0 = wt(5, 'desviam') - 3; m0 = wt(5, 'Moscou') - 3; e0 = wt(5, 'escudo') - 3
    num(c, 'POR QUE IMPORTA?', 640, 360, f, 0, 90, -3)
    d = ImageDraw.Draw(c, 'RGBA')
    if f >= b0:
        for k in range(4):
            r = ((f - b0) * 6 + k * 70) % 280
            d.ellipse([1020 - r, 1000 - r, 1020 + r, 1000 + r], outline=(255, 255, 255, int(200 * (1 - r / 280))), width=8)
        num(c, 'SINAL BLOQUEADO', 900, 1180, f, b0, 52, 2)
    num(c, 'UCRÂNIA DIZ:', 480, 540, f, wt(5, 'Ucrania') - 3, 60, -2)
    # drone ucraniano vindo do sul rumo à Rússia, desviado para a Letônia
    if f >= dv0 - 20:
        t = smooth(ramp(f, dv0 - 20, dv0 + 30))
        pts = [(lerp(940, 980, k / 15), lerp(1600, 1150, k / 15)) for k in range(16)] + \
              [(lerp(980, 700, k / 15), lerp(1150, 900, k / 15) - 60 * math.sin(math.pi * k / 15)) for k in range(1, 16)]
        seta(c, pts, t, hexc('#ffd65a'), 12)
        x, y = pts[min(len(pts) - 1, int((len(pts) - 1) * t))]
        paste_c(c, drone_w(120, True), x, y - 40, 1)
        num(c, 'DRONE DESVIADO', 560, 660, f, dv0, 56, -2)
    if f >= m0:
        num(c, 'RÚSSIA ACUSA:', 640, 1290, f, m0, 60, 3)
    if f >= e0:
        paste_c(c, escudo(), 620, 1000, back(ramp(f, e0, e0 + 8)) * .55)
        num(c, 'CÉU DA OTAN COMO ESCUDO', 660, 1390, f, e0, 50, -2)
    z = lerp(1.0, 1.06, smooth(ramp(f, 0, 220))) * (1 + .0004 * f)
    cy = lerp(880, 1000, smooth(ramp(f, b0, e0)))
    k = kick(f, e0, .6)
    return c, (660, cy + k * 6, z, k), 'dusk'


def s6(f):
    """fim: mesa de negociação em Abu Dhabi com as bandeiras; drone pequeno lá fora pela janela."""
    c = CEN('escritorio', 'dusk').copy()
    r0 = wt(6, 'Russia') - 3; u0 = wt(6, 'Ucrania') - 3; p0 = wt(6, 'paz') - 3; a0 = wt(6, 'Abu') - 3
    if f >= r0:
        paste_c(c, bandeira_ru(), 940, 760, back(ramp(f, r0, r0 + 8)) * .5)
        put_pol(c, 1030, 1520, 600, f, 6, hair='#8a8a90', tie='#d52b1e', suit='#2c2c38', expr='stern', look=-1)
    if f >= u0:
        paste_c(c, bandeira_ua(), 260, 760, back(ramp(f, u0, u0 + 8)) * .5)
        put_pol(c, 210, 1520, 600, f, 2, hair='#3a3a3a', tie='#0057b7', suit='#3a4a3a', expr='stern', look=1)
    mesa(c, 640, 1330)
    num(c, 'NEGOCIAÇÃO DE PAZ', 640, 420, f, p0, 84, -3)
    num(c, 'ABU DHABI', 640, 560, f, a0, 100, 2)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0007 * f)
    return c, (640, 1000, z, .6 * math.sin(f * .04)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'tres') - 3, 140, .5)
    s.ting(s.W(0, 'abrigar') - 3, .35)
    s.engine(s.W(0, 'drones') - 6, s.W(0, 'drones') + 50, .07)
    s.ting(s.W(1, 'Lituania') - 3, .2)
    s.ting(s.W(1, 'Letonia') - 3, .2)
    s.ting(s.W(1, 'Estonia') - 3, .2)
    s.thunk(s.W(2, 'Kaunas') - 3, 140, .4)
    s.thunk(s.W(2, 'trezentos') - 3, 150, .5)
    s.ting(s.W(3, 'Quatro') - 3, .3)
    s.engine(s.W(3, 'cacas') - 6, s.W(3, 'cacas') + 50, .09)
    s.thunk(s.W(4, 'tentativa') - 3, 130, .4)
    s.thunk(s.W(4, 'restos') - 3, 150, .4)
    s.ting(s.W(4, 'Ninguem') - 3, .3)
    s.ting(s.W(5, 'bloqueios') - 3, .25)
    s.thunk(s.W(5, 'escudo') - 3, 150, .5)
    s.ting(s.W(6, 'paz') - 3, .3)
