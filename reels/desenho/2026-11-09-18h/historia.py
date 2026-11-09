"""Um Café com o Mundo — O MUNDO EXPLICADO (segunda 09/11/2026, 18h).
Tema: ataques russos à rede elétrica da Ucrânia deixam ~850 mil sem luz; usina nuclear de Zaporíjia só com geradores a diesel;
negociações de paz em Abu Dhabi na terça e quarta (10-11/11).
Fontes (conferidas em 09/11/2026):
- Al Jazeera, 08/11/2026 ("Russian strikes on Ukraine leave hundreds of thousands without electricity"): mais de 600 mil sem luz em
  Dnipropetrovsk (DTEK); ~250 mil em Kharkiv no domingo; total ~850 mil; negociações trilaterais mediadas pelos EUA em Abu Dhabi
  na terça e na quarta; Rússia diz que seguirá atacando instalações de energia.
- Euromaidan Press, 08/11/2026: ataque da madrugada de 08/11 com 3 mísseis Kh-59/69 e 164 drones tipo Shahed; hospitais de
  Dnipropetrovsk passaram a geradores (Oleksandr Hanzha); usina de Zaporíjia (ocupada pela Rússia) perdeu a última linha externa às
  02h36 de 08/11 e funciona só com geradores a diesel, 16º apagão total do ano; Energoatom alerta que, se os geradores falharem,
  o resfriamento do combustível fica em risco.
- 10 Things Global News, 09/11/2026 (Politico Europe, Al Jazeera): ~850 mil sem luz; conversas em Abu Dhabi em 10-11/11.
Tom sério; sem violência mostrada; personagens genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Quase oitocentas e cinquenta mil pessoas ficaram sem luz na Ucrânia em um só dia.",
    "No domingo, a Rússia lançou cento e sessenta e quatro drones e três mísseis contra a rede de energia.",
    "Em Dnipropetrovsk, mais de seiscentas mil pessoas ficaram no escuro, e hospitais passaram a usar geradores.",
    "Em Kharkiv, foram mais duzentas e cinquenta mil.",
    "E a usina nuclear de Zaporíjia, ocupada pela Rússia, perdeu a última linha de energia de fora, e agora depende só de geradores a diesel.",
    "Por que isso importa? Se os geradores falharem, o resfriamento do combustível nuclear fica em risco. É o décimo sexto apagão da usina este ano.",
    "E tudo isso dias antes de novas negociações de paz, marcadas para terça e quarta, em Abu Dhabi.",
]
CAPTXT = [
    "Quase 850 mil pessoas ficaram sem luz|na Ucrânia em um só dia.",
    "No domingo, a Rússia lançou 164 drones|e 3 mísseis contra|a rede de energia.",
    "Em Dnipropetrovsk, mais de 600 mil|pessoas ficaram no escuro, e hospitais|passaram a usar geradores.",
    "Em Kharkiv, foram mais 250 mil.",
    "E a usina nuclear de Zaporíjia, ocupada pela Rússia,|perdeu a última linha de energia de fora,|e agora depende só de geradores a diesel.",
    "Por que isso importa? Se os geradores falharem,|o resfriamento do combustível nuclear fica em risco.|É o 16º apagão da usina este ano.",
    "E tudo isso dias antes de novas negociações|de paz, marcadas para terça e quarta,|em Abu Dhabi.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'oitocentas', 6), (0, 'luz', 4), (0, 'Ucrania', 4), (1, 'cento', 6), (1, 'tres', 4), (1, 'energia', 4),
         (2, 'Dnipropetrovsk', 4), (2, 'seiscentas', 6), (2, 'geradores', 4), (3, 'Kharkiv', 4), (3, 'duzentas', 6),
         (4, 'usina', 4), (4, 'ultima', 4), (4, 'diesel', 4), (5, 'resfriamento', 4), (5, 'decimo', 6),
         (6, 'negociacoes', 4), (6, 'terca', 4), (6, 'Abu', 4)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); BLUE = hexc('#2f6fd6'); BLUE_D = hexc('#1f4f9e')
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); WHITE = (255, 255, 255)
UBLUE = hexc('#0057b7'); UYEL = hexc('#ffd700'); LIT = hexc('#ffd65a'); DARK = hexc('#2b2d3a'); DARK2 = hexc('#3a3d4d')
GEN = hexc('#e0a23a'); GEN_D = hexc('#a8741e'); TEAL = hexc('#2a9d8f'); NIGHT = hexc('#1b2140'); NIGHT2 = hexc('#2c3561')


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
    p.poly([(270, 418), (330, 418), (300, 470)], (255, 255, 255), 3)
    p.shape([(290, 430), (310, 430), (318, 540), (300, 566), (282, 540)], hexc(tie), mul(hexc(tie), .75), 3, 3)
    return p.img


def put_pol(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'politico', x, feet, h, f, seed, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def noite(c):
    """céu noturno sobre o cenário (cobre o céu até y~1500)."""
    d = ImageDraw.Draw(c)
    for i in range(16):
        y0 = i * 100
        col = tuple(int(NIGHT[k] + (NIGHT2[k] - NIGHT[k]) * i / 15) for k in range(3))
        d.rectangle([0, y0, 1242, y0 + 100], fill=col)
    for i in range(30):
        x = (i * 397) % 1242; y = 330 + (i * 211) % 700
        d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(230, 230, 255))
    d.rectangle([0, 1500, 1242, 2208], fill=hexc('#3b3f52'))
    d.rectangle([0, 1500, 1242, 1520], fill=hexc('#2a2d3c'))


def predio(c, x, base, w, h, lit, seed=0, col=None):
    """prédio com janelas; lit 0..1 = fração de janelas acesas (as que apagam primeiro variam pela seed)."""
    d = ImageDraw.Draw(c)
    col = col or hexc(['#8d7f9c', '#7a8aa6', '#9b8d84', '#7f9a93'][seed % 4])
    d.rounded_rectangle([x - w / 2, base - h, x + w / 2, base], 10, fill=col, outline=INK, width=6)
    cols = max(2, int(w // 80)); rows = max(2, int(h // 95))
    k = 0
    for r in range(rows):
        for q in range(cols):
            wx = x - w / 2 + 25 + q * (w - 50) / cols; wy = base - h + 30 + r * (h - 60) / rows
            order = ((k * 37 + seed * 11) % 97) / 97
            on = order < lit
            d.rectangle([wx + 6, wy, wx + (w - 50) / cols - 6, wy + (h - 60) / rows - 22], fill=LIT if on else DARK, outline=INK, width=3)
            k += 1


@lru_cache(maxsize=2)
def ucrania():
    """silhueta simplificada da Ucrânia (país). 1000x640"""
    p = Pen(1000, 640)
    pts = [(30, 250), (90, 180), (170, 150), (260, 120), (350, 90), (450, 100), (540, 60), (620, 80), (700, 110), (780, 130),
           (860, 170), (950, 230), (985, 300), (940, 360), (860, 390), (790, 430), (720, 470), (640, 470), (590, 520),
           (520, 560), (470, 540), (420, 470), (360, 470), (300, 520), (250, 480), (200, 420), (140, 380), (70, 330)]
    p.shape(pts, UYEL, hexc('#c9a400'), 6, 12)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 140), (10, 140)], UBLUE)
    p.poly([(10, 140), (410, 140), (410, 270), (10, 270)], UYEL)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
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


@lru_cache(maxsize=2)
def marcador():
    p = Pen(200, 280)
    p.shape([(100, 272), (30, 120), (40, 60), (100, 20), (160, 60), (170, 120)], RED, RED_D, 6, 8)
    p.dot(100, 100, 34, WHITE, 5)
    return fin(p)


@lru_cache(maxsize=4)
def hospital(lit=True):
    """prédio de hospital (placa com cruz). 900x900, base y~890."""
    p = Pen(900, 900)
    p.shape([(120, 260), (780, 260), (780, 890), (120, 890)], STONE, STONE_D, 7, 16)
    p.shape([(100, 230), (800, 230), (800, 270), (100, 270)], hexc('#d6d0c4'), STONE_D, 5, 4)
    for r in range(4):
        for k in range(4):
            x, y = 190 + k * 150, 310 + r * 120
            on = lit or (r + k) % 3 == 0
            p.shape([(x, y), (x + 90, y), (x + 90, y + 72), (x, y + 72)], LIT if on else DARK, mul(LIT, .8) if on else DARK2, 4, 3)
    p.shape([(370, 760), (530, 760), (530, 890), (370, 890)], hexc('#7cc4e8'), hexc('#4f8fb8'), 5, 4)
    p.shape([(330, 40), (570, 40), (570, 230), (330, 230)], RED, RED_D, 6, 8)
    p.shape([(425, 70), (475, 70), (475, 200), (425, 200)], WHITE, hexc('#dfe6f0'), 3, 2)
    p.shape([(385, 110), (515, 110), (515, 160), (385, 160)], WHITE, hexc('#dfe6f0'), 3, 2)
    return fin(p)


@lru_cache(maxsize=2)
def gerador():
    """gerador a diesel. 520x380"""
    p = Pen(520, 380)
    p.shape([(30, 90), (490, 90), (490, 340), (30, 340)], GEN, GEN_D, 6, 10)
    p.shape([(60, 130), (300, 130), (300, 300), (60, 300)], hexc('#f3c66a'), GEN_D, 4, 4)
    for y in range(150, 300, 30):
        p.stroke([(80, y), (280, y)], 6, GEN_D)
    p.shape([(340, 140), (460, 140), (460, 220), (340, 220)], hexc('#3a3d4d'), INK, 4, 3)
    p.dot(400, 270, 26, hexc('#7ccf5a'), 4)
    p.shape([(400, 20), (440, 20), (440, 90), (400, 90)], hexc('#8a8f99'), hexc('#5d626b'), 4, 3)
    p.shape([(50, 340), (110, 340), (110, 370), (50, 370)], INK, INK, 3, 0)
    p.shape([(410, 340), (470, 340), (470, 370), (410, 370)], INK, INK, 3, 0)
    return fin(p)


def fumaca(c, x, y, f, seed=0, s=1.0, cor=(150, 150, 160)):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(6):
        t = ((f * .8 + i * 17 + seed * 7) % 100) / 100
        r = (20 + 50 * t) * s
        xx = x + 40 * math.sin(t * 5 + seed) * s; yy = y - 240 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=cor + (a,))


@lru_cache(maxsize=2)
def usina():
    """usina nuclear genérica: 2 cúpulas de reator + prédio + chaminé. 1000x700, base y~690"""
    p = Pen(1000, 700)
    p.shape([(60, 380), (940, 380), (940, 690), (60, 690)], hexc('#d9dde3'), hexc('#a9b0bb'), 7, 14)
    for cx in (290, 690):
        p.shape([(cx - 150, 690), (cx - 150, 330)] + [(cx + 150 * math.cos(a), 330 - 150 * math.sin(a)) for a in [math.pi * (1 - i / 20) for i in range(21)]] + [(cx + 150, 690)],
                hexc('#eef1f5'), hexc('#bcc4cf'), 7, 14)
        p.stroke([(cx - 150, 420), (cx + 150, 420)], 5)
    p.shape([(470, 60), (530, 60), (540, 380), (460, 380)], hexc('#e6e9ee'), hexc('#b0b8c4'), 6, 8)
    p.shape([(470, 100), (530, 100), (531, 130), (469, 130)], RED, RED_D, 3, 2)
    for k in range(5):
        x = 120 + k * 180
        p.shape([(x, 560), (x + 90, 560), (x + 90, 620), (x, 620)], hexc('#9fd0ee'), hexc('#6aa6cc'), 4, 3)
    return fin(p)


def torre(c, x, base, h, col=hexc('#7d8590')):
    """torre de transmissão simples (treliça)."""
    d = ImageDraw.Draw(c)
    top = base - h
    d.line([(x - h * .22, base), (x, top)], fill=INK, width=12); d.line([(x + h * .22, base), (x, top)], fill=INK, width=12)
    d.line([(x - h * .22, base), (x, top)], fill=col, width=6); d.line([(x + h * .22, base), (x, top)], fill=col, width=6)
    for k in range(1, 5):
        yy = base - h * k / 5; ww = h * .22 * (1 - k / 5)
        d.line([(x - ww, yy), (x + ww, yy)], fill=INK, width=6)
    for yy, ww in ((top + h * .12, h * .3), (top + h * .3, h * .24)):
        d.line([(x - ww, yy), (x + ww, yy)], fill=INK, width=10)
    return [(x - h * .3, top + h * .12), (x + h * .3, top + h * .12)]


def raio(c, x, y, s=1.0, col=UYEL):
    d = ImageDraw.Draw(c)
    pts = [(0, -90), (-40, 10), (-5, 10), (-25, 90), (45, -20), (8, -20), (30, -90)]
    d.polygon([(x + px * s, y + py * s) for px, py in pts], fill=col, outline=INK, width=5)


def calendario(c, x, y, s, sz=1.0, col=TEAL):
    sz = max(.08, sz)
    d = ImageDraw.Draw(c)
    w, h = 300 * sz, 280 * sz
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], 22 * sz, fill=WHITE, outline=INK, width=6)
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y - h / 2 + 70 * sz], 22 * sz, fill=col, outline=INK, width=6)
    paste_c(c, txt(s, int(90 * sz), 0), x, y + 30 * sz, 1)


def mesa(c, cx, y):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([cx - 420, y, cx + 420, y + 60], 14, fill=hexc('#a8744a'), outline=INK, width=6)
    d.rectangle([cx - 380, y + 60, cx - 340, y + 260], fill=hexc('#7d5534'), outline=INK, width=5)
    d.rectangle([cx + 340, y + 60, cx + 380, y + 260], fill=hexc('#7d5534'), outline=INK, width=5)


# ------------------------------------------------------------------ cenas
CIDADE = [(150, 300, 620, 0), (430, 240, 820, 1), (700, 280, 560, 2), (980, 300, 760, 3), (1180, 200, 600, 0)]


def s0(f):
    """gancho: cidade à noite, as janelas vão apagando."""
    c = CEN('cidade', 'dusk').copy(); noite(c)
    o0 = wt(0, 'oitocentas') - 3
    l0 = wt(0, 'luz') - 3
    u0 = wt(0, 'Ucrania') - 3
    lit = 1 - smooth(ramp(f, l0 - 4, l0 + 16)) * .93
    for x, w, h, sd in CIDADE:
        predio(c, x, 1530, w, h, lit, sd)
    num(c, '850 MIL', 640, 520, f, o0, 210, -4)
    num(c, 'SEM LUZ', 640, 740, f, l0, 120, 3)
    if f >= u0:
        paste_c(c, bandeira(), 640, 1100, back(ramp(f, u0, u0 + 8)) * .6)
        num(c, 'UCRÂNIA', 640, 1260, f, u0 + 2, 90, -3)
    z = lerp(1.35, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, l0, .8)
    return c, (640, 1100 + k * 8, z, k), 'dusk'


def s1(f):
    """mapa da Ucrânia; drones e mísseis aparecem como números."""
    c = CEN('mapa', 'dusk').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#35507a'))
    c0 = wt(1, 'cento') - 3
    t0 = wt(1, 'tres') - 3
    e0 = wt(1, 'energia') - 3
    paste_c(c, ucrania(), 640, 1180, back(ramp(f, 0, 10)) * 1.15)
    if f >= c0:
        for i in range(6):
            tt = clamp((f - c0 - i * 6) / 50)
            if 0 < tt < 1:
                paste_c(c, drone().resize((180, 66)), lerp(1300, 300 + i * 90, tt), 820 + i * 55 + 20 * math.sin(f * .2 + i), 1)
        num(c, '164 DRONES', 640, 540, f, c0, 120, -3)
    num(c, '+ 3 MÍSSEIS', 640, 680, f, t0, 90, 3)
    if f >= e0:
        for i, (x, y) in enumerate([(820, 1080), (700, 1260), (920, 1200)]):
            raio(c, x, y, .8 * back(ramp(f, e0 + i * 3, e0 + i * 3 + 8)), col=RED if (f // 8) % 2 else UYEL)
        num(c, 'REDE DE ENERGIA', 640, 1500, f, e0, 70, -2)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    k = kick(f, c0, .6)
    return c, (640 + lerp(-15, 25, smooth(ramp(f, 0, 160))), 1080 + k * 6, z, k - 1.0 * smooth(ramp(f, 0, 160))), 'dusk'


def s2(f):
    """Dnipropetrovsk: prédios apagam; hospital liga gerador."""
    c = CEN('cidade', 'dusk').copy(); noite(c)
    d0 = wt(2, 'Dnipropetrovsk') - 3
    s0_ = wt(2, 'seiscentas') - 3
    g0 = wt(2, 'geradores') - 3
    lit = 1 - smooth(ramp(f, s0_, s0_ + 14)) * .95
    predio(c, 150, 1530, 280, 760, lit, 1)
    predio(c, 1110, 1530, 260, 640, lit, 2)
    paste_c(c, hospital(f >= g0), 640, 1100, .9)
    if f >= g0:
        paste_c(c, gerador(), 980, 1420, back(ramp(f, g0, g0 + 8)) * .7)
        fumaca(c, 1010, 1300, f, 1, .8)
        put_dust(c, 980, 1460, 120, f - g0)
    num(c, 'DNIPROPETROVSK', 640, 470, f, d0, 90, -3)
    num(c, '+600 MIL', 640, 610, f, s0_, 140, 3)
    if f >= g0:
        num(c, 'GERADORES', 640, 1560, f, g0, 70, -2)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 70))) * (1 + .0008 * f)
    k = kick(f, s0_, .6)
    return c, (640 + 10 * math.sin(f * .05), 1080 + k * 6, z, k), 'dusk'


def s3(f):
    """Kharkiv: mais prédios apagando, morador com lanterna na janela."""
    c = CEN('cidade', 'dusk').copy(); noite(c)
    k0 = wt(3, 'Kharkiv') - 3
    d0 = wt(3, 'duzentas') - 3
    lit = 1 - smooth(ramp(f, d0, d0 + 12)) * .95
    for x, w, h, sd in [(180, 320, 700, 3), (620, 340, 860, 0), (1060, 320, 680, 1)]:
        predio(c, x, 1530, w, h, lit, sd)
    if f >= d0 + 8:
        dd = ImageDraw.Draw(c, 'RGBA')
        lx = 620 + 60 * math.sin(f * .07)
        dd.polygon([(620, 1000), (lx - 120, 1500), (lx + 120, 1500)], fill=(255, 240, 170, 70))
    num(c, 'KHARKIV', 640, 500, f, k0, 120, -3)
    num(c, '+250 MIL', 640, 660, f, d0, 150, 3)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) * (1 + .0008 * f)
    k = kick(f, d0, .6)
    return c, (640, 1100 + k * 6, z, k + .5 * math.sin(f * .05)), 'dusk'


def s4(f):
    """usina nuclear: a linha de fora se rompe; geradores a diesel."""
    c = CEN('cidade', 'dusk').copy(); noite(c)
    u0 = wt(4, 'usina') - 3
    o0 = wt(4, 'ocupada') - 3
    l0 = wt(4, 'ultima') - 3
    d0 = wt(4, 'diesel') - 3
    paste_c(c, usina(), 560, 1200, back(ramp(f, 0, 10)) * 1.0)
    ends = torre(c, 1100, 1530, 640)
    d = ImageDraw.Draw(c)
    cut = f >= l0 + 6
    for ex, ey in ends:
        if not cut:
            d.line([(ex, ey), (ex - 200, ey + 140), (880, 1040)], fill=INK, width=6)
        else:
            sag = 120 * smooth(ramp(f, l0 + 6, l0 + 18))
            d.line([(ex, ey), (ex - 120, ey + 120 + sag)], fill=INK, width=6)
    if cut and f < l0 + 30:
        raio(c, 960, 960, .7 * back(ramp(f, l0 + 6, l0 + 12)), col=RED)
    if f >= d0:
        paste_c(c, gerador(), 330, 1440, back(ramp(f, d0, d0 + 8)) * .62)
        paste_c(c, gerador(), 680, 1450, back(ramp(f, d0 + 3, d0 + 11)) * .62)
        fumaca(c, 350, 1360, f, 2, .45); fumaca(c, 700, 1370, f, 4, .45)
        num(c, 'SÓ DIESEL', 640, 950, f, d0, 90, -3)
    num(c, 'USINA NUCLEAR', 640, 460, f, u0, 100, -3)
    num(c, 'ZAPORÍJIA', 640, 590, f, u0 + 6, 100, 3)
    num(c, 'OCUPADA PELA RÚSSIA', 640, 710, f, o0, 60, -2)
    if f >= l0 + 6:
        num(c, 'SEM ENERGIA DE FORA', 640, 820, f, l0 + 6, 62, 2)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 200))) * (1 + .0005 * f)
    k = kick(f, l0 + 6, .9)
    return c, (640 + lerp(20, -20, smooth(ramp(f, 0, 200))), 1100 + k * 8, z, k), 'dusk'


def s5(f):
    """por que importa: geradores x resfriamento; 16º apagão."""
    c = CEN('cidade', 'dusk').copy(); noite(c)
    g0 = wt(5, 'geradores') - 3
    r0 = wt(5, 'resfriamento') - 3
    d0 = wt(5, 'decimo') - 3
    num(c, 'POR QUE IMPORTA?', 640, 480, f, 0, 88, -3)
    paste_c(c, usina(), 640, 1230, .75)
    if f >= g0:
        paste_c(c, gerador(), 400, 1450, .55)
        if (f // 9) % 2 == 0 and f >= g0 + 8:
            num(c, '?', 400, 1260, f, g0 + 8, 120, 6)
    if f >= r0:
        # termômetro subindo
        d = ImageDraw.Draw(c)
        h = 260 * smooth(ramp(f, r0, r0 + 30))
        d.rounded_rectangle([930, 920, 990, 1300], 30, fill=WHITE, outline=INK, width=6)
        d.rounded_rectangle([942, 1288 - h, 978, 1300], 18, fill=RED)
        d.ellipse([910, 1270, 1010, 1370], fill=RED, outline=INK, width=6)
        num(c, 'RESFRIAMENTO EM RISCO', 640, 620, f, r0, 62, 2)
    if f >= d0:
        num(c, '16º APAGÃO', 640, 790, f, d0, 120, -3)
        num(c, 'EM 2026', 640, 920, f, d0 + 5, 70, 3)
    z = lerp(1.0, 1.06, smooth(ramp(f, 0, 220))) * (1 + .0005 * f)
    k = kick(f, d0, .7)
    return c, (640, 1080 + k * 6, z, k - .004 * f), 'dusk'


def s6(f):
    """negociações de paz em Abu Dhabi, terça e quarta."""
    c = CEN('escritorio', 'dusk').copy()
    n0 = wt(6, 'negociacoes') - 3
    t0 = wt(6, 'terca') - 3
    q0 = wt(6, 'quarta') - 3
    a0 = wt(6, 'Abu') - 3
    put_pol(c, 280, 1500, 600, f, 2, hair='#5a4636', tie='#0057b7', suit='#2c3550', look=1, expr='stern', arms='hang')
    put_pol(c, 1000, 1500, 600, f, 6, hair='#3a3a3a', tie='#d8443c', suit='#3a3a44', look=-1, expr='stern', arms='hang')
    mesa(c, 640, 1280)
    num(c, 'NEGOCIAÇÕES DE PAZ', 640, 490, f, n0, 68, -3)
    if f >= t0:
        calendario(c, 520, 720, 'TER', sz=back(ramp(f, t0, t0 + 8)) * .8, col=UBLUE)
    if f >= q0:
        calendario(c, 760, 720, 'QUA', sz=back(ramp(f, q0, q0 + 8)) * .8, col=UBLUE)
    if f >= a0:
        paste_c(c, marcador(), 640, 870, back(ramp(f, a0, a0 + 8)) * .45)
        num(c, 'ABU DHABI', 640, 980, f, a0, 90, -3)
    z = lerp(1.0, 1.06, smooth(ramp(f, 0, 140))) * (1 + .0004 * f)
    k = kick(f, a0, .5)
    return c, (640, 1080 + k * 6, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'luz') - 3, 140, .7)
    s.ting(s.W(0, 'Ucrania') - 3, .25)
    s.engine(s.W(1, 'cento') - 6, s.W(1, 'cento') + 50, .08)
    s.thunk(s.W(1, 'energia') - 3, 150, .5)
    s.thunk(s.W(2, 'seiscentas') - 3, 140, .6)
    s.engine(s.W(2, 'geradores') - 3, s.W(2, 'geradores') + 40, .08)
    s.thunk(s.W(3, 'duzentas') - 3, 140, .6)
    s.thunk(s.W(4, 'ultima') + 3, 160, .8)
    s.engine(s.W(4, 'diesel') - 3, s.W(4, 'diesel') + 40, .08)
    s.ting(s.W(5, 'decimo') - 3, .3)
    s.ting(s.W(6, 'Abu') - 3, .3)
