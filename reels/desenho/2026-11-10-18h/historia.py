"""Um Café com o Mundo — O MUNDO EXPLICADO (terça 10/11/2026, 18h).
Tema: Ucrânia, Rússia e EUA voltam a negociar em Abu Dhabi, 1ª rodada a três desde fevereiro.
Fontes (conferidas em 10/11/2026):
- Al Jazeera, 10/11/2026 ("First day of Russia-Ukraine talks in Abu Dhabi 'constructive': Zelenskyy"): conversas na terça em
  Abu Dhabi; EUA com Steve Witkoff e Jared Kushner; Ucrânia com Rustem Umerov; Rússia com Vladimir Medinsky (assessor do Kremlin);
  delegações a três se encontraram pela última vez em Genebra em 18/02; Rússia ocupa cerca de 20% da Ucrânia; Putin quer todo o
  Donbas; funcionário dos EUA: os dois lados mostraram em particular alguma flexibilidade sobre território; garantias de segurança
  centrais, talvez nos moldes do artigo 5 da Otan; Rubio: ainda há "um caminho a percorrer"; invasão em fevereiro de 2022.
- Euronews, 10/11/2026: 1ªs conversas trilaterais desde fevereiro; "um pouco de flexibilidade" (funcionário americano);
  Washington pede para não esperar avanço imediato.
- Just Security Early Edition 10/11/2026 (Reuters): Kushner disse que os contatos "identificaram e estreitaram as diferenças".
Tom sério; personagens genéricos; sem pessoas reais desenhadas."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Pela primeira vez desde fevereiro, Ucrânia, Rússia e Estados Unidos voltaram a negociar o fim da guerra.",
    "Começou nesta terça, em Abu Dhabi, com os enviados americanos Steve Witkoff e Jared Kushner.",
    "A Ucrânia mandou Rustem Umerov. E a Rússia, a equipe de Vladimir Medinsky, assessor do Kremlin.",
    "O ponto mais difícil é o território: a Rússia ocupa cerca de vinte por cento da Ucrânia, e quer todo o Donbas.",
    "Mas, segundo um funcionário americano, os dois lados mostraram, em particular, um pouco de flexibilidade.",
    "Por que isso importa? A guerra já dura quase cinco anos, e na mesa estão garantias de segurança para a Ucrânia, nos moldes da Otan.",
    "Mesmo assim, os Estados Unidos avisam: ainda há um longo caminho até a paz.",
]
CAPTXT = [
    "Pela primeira vez desde fevereiro, Ucrânia,|Rússia e Estados Unidos voltaram|a negociar o fim da guerra.",
    "Começou nesta terça, em Abu Dhabi,|com os enviados americanos|Steve Witkoff e Jared Kushner.",
    "A Ucrânia mandou Rustem Umerov.|E a Rússia, a equipe de Vladimir Medinsky,|assessor do Kremlin.",
    "O ponto mais difícil é o território: a Rússia|ocupa cerca de 20% da Ucrânia,|e quer todo o Donbas.",
    "Mas, segundo um funcionário americano,|os dois lados mostraram, em particular,|um pouco de flexibilidade.",
    "Por que isso importa? A guerra já dura quase|5 anos, e na mesa estão garantias de segurança|para a Ucrânia, nos moldes da Otan.",
    "Mesmo assim, os Estados Unidos avisam:|ainda há um longo caminho até a paz.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'primeira', 4), (0, 'fevereiro', 4), (0, 'Ucrania', 4), (0, 'Russia', 4), (0, 'Unidos', 4),
         (1, 'terca', 4), (1, 'Abu', 4), (1, 'Witkoff', 4), (2, 'Umerov', 4), (2, 'Medinsky', 4),
         (3, 'territorio', 4), (3, 'vinte', 6), (3, 'Donbas', 4), (4, 'flexibilidade', 4),
         (5, 'cinco', 4), (5, 'garantias', 4), (5, 'Otan', 4), (6, 'longo', 4), (6, 'paz', 4)]


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



RU_R = hexc('#d52b1e'); RU_B = hexc('#0039a6'); US_R = hexc('#b22234'); US_B = hexc('#3c3b6e'); SAND = hexc('#e8c98a')


@lru_cache(maxsize=2)
def bandeira_ru():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 96), (10, 96)], WHITE)
    p.poly([(10, 96), (410, 96), (410, 183), (10, 183)], RU_B)
    p.poly([(10, 183), (410, 183), (410, 270), (10, 270)], RU_R)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_us():
    p = Pen(420, 280)
    for i in range(13):
        y0 = 10 + i * 20
        p.poly([(10, y0), (410, y0), (410, y0 + 20), (10, y0 + 20)], US_R if i % 2 == 0 else WHITE)
    p.poly([(10, 10), (190, 10), (190, 150), (10, 150)], US_B)
    for r in range(4):
        for k in range(5):
            p.dot(32 + k * 34, 32 + r * 32, 6, WHITE, 0)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


def mastro(c, x, base, im, f, seed=0, s=.55):
    """bandeira num mastro, balançando de leve."""
    d = ImageDraw.Draw(c)
    d.rectangle([x - 8, base - 620, x + 8, base], fill=hexc('#8a8f99'), outline=INK, width=4)
    d.ellipse([x - 16, base - 640, x + 16, base - 608], fill=UYEL, outline=INK, width=4)
    w = im.resize((int(im.size[0] * s), int(im.size[1] * s * (1 + .03 * math.sin(f * .12 + seed)))))
    c.alpha_composite(w, (int(x + 8), int(base - 600)))


@lru_cache(maxsize=2)
def ucrania_ocupada():
    """Ucrânia com a parte leste ocupada pintada de vermelho (aprox. 20%)."""
    im = ucrania().copy()
    a = np.array(im).astype(np.float32)
    H, W = a.shape[:2]
    xs = np.arange(W)[None, :].repeat(H, 0)
    ys = np.arange(H)[:, None].repeat(W, 1)
    mask = (a[..., 3] > 200) & (xs > 0.79 * W - 0.10 * (ys - 0.25 * H)) & (a[..., 0] > 180)
    a[mask, 0] = 216; a[mask, 1] = 68; a[mask, 2] = 60
    return Image.fromarray(a.astype(np.uint8))


@lru_cache(maxsize=2)
def escudo():
    p = Pen(400, 480)
    p.shape([(200, 20), (370, 80), (360, 260), (300, 380), (200, 460), (100, 380), (40, 260), (30, 80)], TEAL, mul(TEAL, .7), 7, 12)
    p.stroke([(130, 240), (185, 300), (285, 170)], 22, WHITE)
    return fin(p)


def s0(f):
    """gancho: três bandeiras surgem em volta da mesa."""
    c = CEN('escritorio', 'dusk').copy()
    p0 = wt(0, 'primeira') - 3
    fv0 = wt(0, 'fevereiro') - 3
    u0 = wt(0, 'Ucrania') - 3; r0 = wt(0, 'Russia') - 3; e0 = wt(0, 'Unidos') - 3
    mesa(c, 640, 1290)
    for x, im, k0, sd in ((260, bandeira(), u0, 1), (640, bandeira_us(), e0, 2), (1020, bandeira_ru(), r0, 3)):
        if f >= k0:
            paste_c(c, im, x, 1120, back(ramp(f, k0, k0 + 8)) * .62)
    num(c, '1ª VEZ', 640, 500, f, p0, 170, -4)
    num(c, 'DESDE FEVEREIRO', 640, 690, f, fv0, 90, 3)
    num(c, 'UCRÂNIA', 260, 1300, f, u0, 54, -3)
    num(c, 'EUA', 640, 1300, f, e0, 60, 2)
    num(c, 'RÚSSIA', 1020, 1300, f, r0, 54, -2)
    z = lerp(1.3, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, p0, .7)
    return c, (640, 1080 + k * 8, z, k), 'dusk'


def s1(f):
    """Abu Dhabi: prédios no deserto, marcador, dois enviados chegando."""
    c = CEN('deserto', 'dusk').copy()
    t0 = wt(1, 'terca') - 3; a0 = wt(1, 'Abu') - 3; w0 = wt(1, 'Witkoff') - 3
    for x, w, h, sd in ((180, 200, 700, 1), (430, 150, 900, 3), (820, 170, 820, 2), (1080, 210, 640, 0)):
        predio(c, x, 1520, w, h, .7, sd)
    calendario(c, 640, 860, 'TER', sz=back(ramp(f, t0, t0 + 8)) * .7 if f >= t0 else 0, col=TEAL) if f >= t0 else None
    if f >= a0:
        paste_c(c, marcador(), 640, 560, back(ramp(f, a0, a0 + 8)) * .5)
        num(c, 'ABU DHABI', 640, 430, f, a0, 110, -3)
        num(c, 'EMIRADOS ÁRABES', 640, 700, f, a0 + 8, 60, 2)
    w0 = wt(1, 'enviados') - 3
    if f >= w0:
        tt = smooth(ramp(f, w0, w0 + 24))
        put_pol(c, lerp(-150, 430, tt), 1500, 560, f, 3, hair='#c9b38a', tie='#b22234', suit='#2c3550', expr='stern', look=1)
        put_pol(c, lerp(-350, 820, tt), 1500, 580, f, 7, hair='#5a4636', tie='#3c3b6e', suit='#2c3550', expr='neutral', look=1)
        num(c, 'ENVIADOS DOS EUA', 640, 1030, f, w0, 64, -2)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200))) * (1 + .0005 * f)
    k = kick(f, a0, .5)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 200))), 1060 + k * 6, z, k), 'dusk'


def s2(f):
    """delegações: Ucrânia à esquerda, Rússia à direita, bandeiras atrás."""
    c = CEN('escritorio', 'dusk').copy()
    u0 = wt(2, 'Umerov') - 3; m0 = wt(2, 'Medinsky') - 3
    paste_c(c, bandeira(), 330, 760, .5)
    paste_c(c, bandeira_ru(), 940, 760, .5)
    if f >= u0 - 10:
        put_pol(c, 330, 1520, 620, f, 2, hair='#3a3a3a', tie='#0057b7', suit='#3a4a3a', expr='stern', look=1)
        num(c, 'UCRÂNIA', 330, 560, f, u0, 80, -3)
    if f >= m0 - 10:
        put_pol(c, 940, 1520, 620, f, 6, hair='#8a8a90', tie='#d52b1e', suit='#2c2c38', expr='stern', look=-1)
        num(c, 'RÚSSIA', 940, 560, f, m0, 80, 3)
    mesa(c, 640, 1330)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0006 * f)
    cx = lerp(560, 720, smooth(ramp(f, m0 - 20, m0 + 10))) if f >= m0 - 20 else 560
    return c, (cx, 1080, z, .6 * math.sin(f * .04)), 'dusk'


def s3(f):
    """território: mapa com a parte ocupada."""
    c = CEN('mapa', 'dusk').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#35507a'))
    t0 = wt(3, 'territorio') - 3; v0 = wt(3, 'vinte') - 3; d0 = wt(3, 'Donbas') - 3
    im = ucrania_ocupada() if f >= v0 else ucrania()
    paste_c(c, im, 640, 1150, back(ramp(f, 0, 10)) * 1.15)
    num(c, 'TERRITÓRIO', 640, 520, f, t0, 120, -3)
    num(c, '20% OCUPADO', 640, 690, f, v0, 120, 3)
    if f >= d0:
        paste_c(c, marcador(), 1060, 1000, back(ramp(f, d0, d0 + 8)) * .45)
        num(c, 'DONBAS', 1000, 1420, f, d0, 80, -3)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    k = kick(f, v0, .6)
    return c, (640 + lerp(-10, 40, smooth(ramp(f, 0, 160))), 1080 + k * 6, z, k), 'dusk'


def s4(f):
    """flexibilidade: funcionário americano cochicha; os dois lados ao fundo."""
    c = CEN('escritorio', 'dusk').copy()
    fu0 = wt(4, 'funcionario') - 3; fl0 = wt(4, 'flexibilidade') - 3
    put_pol(c, 250, 1480, 520, f, 2, hair='#3a3a3a', tie='#0057b7', suit='#3a4a3a', expr='neutral', look=1)
    put_pol(c, 1000, 1480, 520, f, 6, hair='#8a8a90', tie='#d52b1e', suit='#2c2c38', expr='neutral', look=-1)
    mesa(c, 640, 1300)
    put_pol(c, 640, 1560, 600, f, 3, hair='#c9b38a', tie='#b22234', suit='#2c3550', expr='grin' if f >= fl0 else 'neutral', arms='point' if f >= fu0 else 'hang', look=0)
    num(c, 'FUNCIONÁRIO DOS EUA', 640, 470, f, fu0, 66, -3)
    num(c, 'UM POUCO DE', 640, 620, f, fl0 - 6, 80, 2)
    num(c, 'FLEXIBILIDADE', 640, 760, f, fl0, 110, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140))) * (1 + .0005 * f)
    k = kick(f, fl0, .6)
    return c, (640, lerp(1080, 1040, smooth(ramp(f, 0, 140))) + k * 6, z, k), 'dusk'


def s5(f):
    """por que importa: quase 5 anos; escudo de garantias sobre o mapa."""
    c = CEN('mapa', 'dusk').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#35507a'))
    c0 = wt(5, 'cinco') - 3; g0 = wt(5, 'garantias') - 3; o0 = wt(5, 'Otan') - 3
    num(c, 'POR QUE IMPORTA?', 640, 470, f, 0, 88, -3)
    paste_c(c, ucrania(), 640, 1220, 1.0)
    if f >= c0:
        num(c, 'QUASE 5 ANOS', 640, 640, f, c0, 120, 3)
        num(c, 'DE GUERRA', 640, 780, f, c0 + 5, 70, -2)
    if f >= g0:
        paste_c(c, escudo(), 640, 1180, back(ramp(f, g0, g0 + 10)) * .9)
        num(c, 'GARANTIAS DE SEGURANÇA', 640, 1500, f, g0, 58, -2)
    if f >= o0:
        num(c, 'NOS MOLDES DA OTAN', 640, 930, f, o0, 64, 3)
    z = lerp(1.0, 1.07, smooth(ramp(f, 0, 240))) * (1 + .0004 * f)
    k = kick(f, g0, .7)
    return c, (640, 1080 + k * 6, z, k - .003 * f), 'dusk'


def s6(f):
    """fim: estrada longa até a palavra PAZ no horizonte."""
    c = CEN('deserto', 'dusk').copy()
    l0 = wt(6, 'longo') - 3; p0 = wt(6, 'paz') - 3
    d = ImageDraw.Draw(c)
    d.polygon([(380, 1700), (860, 1700), (660, 1000), (620, 1000)], fill=hexc('#6b6f7a'), outline=INK)
    for i in range(8):
        t = ((i + f * .03) % 8) / 8
        y = lerp(1000, 1700, t * t); w = lerp(3, 18, t * t); hh = lerp(6, 60, t * t)
        d.rectangle([640 - w, y, 640 + w, y + hh], fill=UYEL)
    paste_c(c, bandeira(), 260, 1380, .3)
    paste_c(c, bandeira_ru(), 1000, 1380, .3)
    num(c, 'LONGO CAMINHO', 640, 600, f, l0, 84, -3)
    if f >= p0:
        num(c, 'PAZ?', 640, 880, f, p0, 140, 3)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 120))) * (1 + .0005 * f)
    return c, (640, lerp(1150, 1000, smooth(ramp(f, 0, 120))), z, .5 * math.sin(f * .05)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.ting(s.W(0, 'primeira') - 3, .3)
    s.thunk(s.W(0, 'Unidos') - 3, 140, .4)
    s.ting(s.W(1, 'Abu') - 3, .25)
    s.thunk(s.W(2, 'Medinsky') - 3, 140, .4)
    s.thunk(s.W(3, 'vinte') - 3, 150, .6)
    s.ting(s.W(4, 'flexibilidade') - 3, .3)
    s.thunk(s.W(5, 'garantias') - 3, 140, .5)
    s.ting(s.W(6, 'paz') - 3, .3)
