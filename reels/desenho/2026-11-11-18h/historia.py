"""Um Café com o Mundo — O MUNDO EXPLICADO (quarta 11/11/2026, 18h).
Tema: fim das conversas de Abu Dhabi: Rússia e Ucrânia combinam grande troca de prisioneiros; sem cessar-fogo; enviados dos EUA vão a Putin.
Fontes (conferidas em 11/11/2026):
- Euronews, 11/11/2026 ("Abu Dhabi peace talks end with prisoner exchange agreement as US envoys prepare to meet Putin"):
  2 dias de conversas mediadas pelos EUA terminaram na quarta; acordo em princípio para grande troca de prisioneiros, único
  resultado concreto; sem avanço em cessar-fogo nem território; números finais a definir; Kushner: "a maior libertação humanitária
  de prisioneiros"; Zelensky disse que se discutiu 1.000 de cada lado, podendo chegar a 1.500; 1ª negociação direta Kiev-Moscou em
  9 meses; Rússia exige que a Ucrânia saia do Donbas; Kushner e Witkoff vão a Moscou na quinta encontrar Putin e depois a Dublin
  falar com Zelensky.
- Kyiv Independent, 11/11/2026: Umerov: "o principal resultado é o acordo sobre uma troca de prisioneiros em grande escala";
  TASS citando o general russo Alexander Zorin: "será a maior de todas, com mais de 1.000 pessoas de cada lado"; tamanho e data
  não divulgados; Zelensky em Dublin em 13/11 (reunião informal de líderes da UE).
- Just Security Early Edition 11/11/2026; NPR/AP 11/11/2026 ("talks end with no big breakthrough").
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


VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Rússia e Ucrânia acabam de combinar uma troca de prisioneiros que, segundo Moscou, vai ser a maior da guerra.",
    "O acordo saiu nesta quarta, no fim de dois dias de conversas em Abu Dhabi, com mediação dos Estados Unidos.",
    "Os números finais ainda não saíram, mas um general russo fala em mais de mil pessoas de cada lado. Zelensky citou até mil e quinhentos.",
    "Só que a parte mais difícil não andou: não teve cessar-fogo, e a Rússia segue exigindo que a Ucrânia saia do Donbas.",
    "Por que isso importa? Foi o único resultado concreto da primeira negociação direta entre Kiev e Moscou em nove meses.",
    "E agora? Os enviados de Trump vão a Moscou nesta quinta, para encontrar Putin.",
    "Depois, seguem para Dublin, para contar tudo a Zelensky.",
]
CAPTXT = [
    "Rússia e Ucrânia acabam de combinar|uma troca de prisioneiros que, segundo Moscou,|vai ser a maior da guerra.",
    "O acordo saiu nesta quarta, no fim de 2 dias|de conversas em Abu Dhabi,|com mediação dos Estados Unidos.",
    "Os números finais ainda não saíram, mas um general russo|fala em mais de 1.000 pessoas de cada lado.|Zelensky citou até 1.500.",
    "Só que a parte mais difícil não andou:|não teve cessar-fogo, e a Rússia segue|exigindo que a Ucrânia saia do Donbas.",
    "Por que isso importa? Foi o único resultado concreto|da 1ª negociação direta entre Kiev e Moscou|em 9 meses.",
    "E agora? Os enviados de Trump vão a Moscou|nesta quinta, para encontrar Putin.",
    "Depois, seguem para Dublin,|para contar tudo a Zelensky.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'troca', 4), (0, 'prisioneiros', 4), (0, 'maior', 4), (1, 'quarta', 4), (1, 'dois', 4), (1, 'Abu', 4), (1, 'Unidos', 4),
         (2, 'general', 4), (2, 'mil', 4), (2, 'quinhentos', 4), (3, 'cessar-fogo', 4), (3, 'Donbas', 4),
         (4, 'unico', 4), (4, 'nove', 4), (5, 'Moscou', 4), (5, 'quinta', 4), (5, 'Putin', 4), (6, 'Dublin', 4), (6, 'Zelensky', 4)]


def fila(c, x0, dx, n, base, h, f, f0, seed0, look, walk_to=0, t=1.0):
    """fila de pessoas (prisioneiros genéricos, sem capacete) entrando."""
    for i in range(n):
        if f < f0 + i * 3: continue
        x = x0 + i * dx + walk_to * t
        P_ = put_pol
        put_pol(c, x, base, h, f, seed0 + i, hair=['#3a3a3a', '#6b5a48', '#8a8a90', '#2b2b2b'][i % 4], tie='#7a7f88',
                suit=['#5d6b52', '#6a6f78', '#55606e', '#6b5f52'][i % 4], expr='neutral', look=look)


def s0(f):
    """gancho: duas filas de pessoas caminhando uma em direção à outra, bandeiras dos dois lados."""
    c = CEN('neve', 'dusk').copy()
    t0 = wt(0, 'troca') - 3; m0 = wt(0, 'maior') - 3
    mastro(c, 120, 1500, bandeira(), f, 1, .5)
    mastro(c, 1100, 1500, bandeira_ru(), f, 2, .5)
    t = smooth(ramp(f, 0, 150))
    for i in range(3):
        put_pol(c, lerp(-80, 360, t) - i * 150, 1520 + i * 6, 600, f, 10 + i, hair='#3a3a3a', tie='#7a7f88', suit='#5d6b52', expr='neutral', look=1)
        put_pol(c, lerp(1320, 880, t) + i * 150, 1520 + i * 6, 600, f, 20 + i, hair='#6b5a48', tie='#7a7f88', suit='#6a6f78', expr='neutral', look=-1)
    num(c, 'TROCA DE PRISIONEIROS', 640, 560, f, t0, 66, -3)
    num(c, 'A MAIOR DA GUERRA', 640, 720, f, m0, 80, 3)
    num(c, 'SEGUNDO MOSCOU', 640, 840, f, m0 + 8, 54, -2)
    z = lerp(1.25, 1.0, easeOut(ramp(f, 0, 45))) * (1 + .0008 * f)
    k = kick(f, m0, .7)
    return c, (640, 1120 + k * 8, z, k), 'dusk'


def s1(f):
    """Abu Dhabi: prédios no deserto, calendário, mesa."""
    c = CEN('deserto', 'dusk').copy()
    q0 = wt(1, 'quarta') - 3; d0 = wt(1, 'dois') - 3; a0 = wt(1, 'Abu') - 3; u0 = wt(1, 'Unidos') - 3
    for x, w, h, sd in ((180, 200, 700, 1), (430, 150, 900, 3), (820, 170, 820, 2), (1080, 210, 640, 0)):
        predio(c, x, 1520, w, h, .7, sd)
    if f >= q0:
        calendario(c, 300, 900, 'QUA', sz=back(ramp(f, q0, q0 + 8)) * .7, col=TEAL)
    num(c, '2 DIAS', 940, 900, f, d0, 110, 3)
    if f >= a0:
        paste_c(c, marcador(), 640, 560, back(ramp(f, a0, a0 + 8)) * .5)
        num(c, 'ABU DHABI', 640, 410, f, a0, 110, -3)
    if f >= u0:
        paste_c(c, bandeira_us(), 640, 1180, back(ramp(f, u0, u0 + 8)) * .5)
        num(c, 'MEDIAÇÃO DOS EUA', 640, 1340, f, u0, 60, -2)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200))) * (1 + .0005 * f)
    k = kick(f, a0, .5)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 200))), 1060 + k * 6, z, k), 'dusk'


def s2(f):
    """números: mais de 1.000 de cada lado, até 1.500."""
    c = CEN('neve', 'dusk').copy()
    g0 = wt(2, 'general') - 3; m0 = wt(2, 'mil') - 3; q0 = wt(2, 'quinhentos') - 3
    paste_c(c, bandeira(), 280, 1130, .4)
    paste_c(c, bandeira_ru(), 960, 1130, .4)
    for i in range(4):
        if f >= m0 + i * 3:
            put_pol(c, 110 + i * 110, 1520 + (i % 2) * 20, 430, f, 30 + i, hair='#3a3a3a', tie='#7a7f88', suit='#5d6b52', expr='neutral', look=1)
            put_pol(c, 1130 - i * 110, 1520 + (i % 2) * 20, 430, f, 40 + i, hair='#6b5a48', tie='#7a7f88', suit='#6a6f78', expr='neutral', look=-1)
    num(c, 'NÚMEROS AINDA EM ABERTO', 640, 470, f, 0, 60, -2)
    num(c, '+1.000', 640, 680, f, m0, 170, -4)
    num(c, 'DE CADA LADO', 640, 850, f, m0 + 6, 70, 2)
    num(c, 'ATÉ 1.500?', 640, 1020, f, q0, 110, -3)
    z = lerp(1.06, 1.0, smooth(ramp(f, 0, 100))) * (1 + .0006 * f)
    k = kick(f, m0, .6)
    return c, (640, 1060 + k * 6, z, k), 'dusk'


def s3(f):
    """sem cessar-fogo; mapa com Donbas."""
    c = CEN('mapa', 'dusk').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#35507a'))
    c0 = wt(3, 'cessar-fogo') - 3; d0 = wt(3, 'Donbas') - 3
    paste_c(c, ucrania_ocupada(), 640, 1150, back(ramp(f, 0, 10)) * 1.15)
    num(c, 'SEM CESSAR-FOGO', 640, 560, f, c0, 86, -3)
    if f >= d0:
        paste_c(c, marcador(), 1060, 1000, back(ramp(f, d0, d0 + 8)) * .45)
        num(c, 'DONBAS', 1000, 1420, f, d0, 80, -3)
        num(c, 'RÚSSIA EXIGE', 640, 730, f, d0 - 4, 70, 2)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    k = kick(f, c0, .6)
    return c, (640 + lerp(-10, 40, smooth(ramp(f, 0, 160))), 1080 + k * 6, z, k), 'dusk'


def s4(f):
    """por que importa: delegações frente a frente, 9 meses."""
    c = CEN('escritorio', 'dusk').copy()
    u0 = wt(4, 'unico') - 3; n0 = wt(4, 'nove') - 3
    paste_c(c, bandeira(), 130, 1000, .3)
    paste_c(c, bandeira_ru(), 1110, 1000, .3)
    put_pol(c, 330, 1520, 600, f, 2, hair='#3a3a3a', tie='#0057b7', suit='#3a4a3a', expr='stern', look=1)
    put_pol(c, 940, 1520, 600, f, 6, hair='#8a8a90', tie='#d52b1e', suit='#2c2c38', expr='stern', look=-1)
    mesa(c, 640, 1330)
    num(c, 'POR QUE IMPORTA?', 640, 420, f, 0, 88, -3)
    num(c, 'ÚNICO RESULTADO CONCRETO', 640, 740, f, u0, 58, 2)
    num(c, '1ª EM 9 MESES', 640, 580, f, n0, 110, -3)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0006 * f)
    k = kick(f, u0, .6)
    return c, (640, 1060 + k * 6, z, k + .4 * math.sin(f * .04)), 'dusk'


def s5(f):
    """Moscou na quinta: dois enviados caminham pela cidade nevada."""
    c = CEN('neve', 'dusk').copy()
    m0 = wt(5, 'Moscou') - 3; q0 = wt(5, 'quinta') - 3; p0 = wt(5, 'Putin') - 3
    for x, w, h, sd in ((160, 200, 620, 2), (420, 160, 760, 1), (860, 180, 700, 3), (1100, 200, 560, 0)):
        predio(c, x, 1480, w, h, .6, sd)
    paste_c(c, bandeira_us(), 640, 470, .0 if f < 2 else .32)
    if f >= m0:
        paste_c(c, marcador(), 640, 760, back(ramp(f, m0, m0 + 8)) * .45)
        num(c, 'MOSCOU', 640, 620, f, m0, 120, -3)
    if f >= q0:
        calendario(c, 1000, 960, 'QUI', sz=back(ramp(f, q0, q0 + 8)) * .6, col=TEAL)
    t = smooth(ramp(f, 0, 90))
    put_pol(c, lerp(-150, 380, t), 1520, 540, f, 3, hair='#c9b38a', tie='#b22234', suit='#2c3550', expr='stern', look=1)
    put_pol(c, lerp(-350, 600, t), 1520, 560, f, 7, hair='#5a4636', tie='#3c3b6e', suit='#2c3550', expr='neutral', look=1)
    num(c, 'ENCONTRO COM PUTIN', 640, 1100, f, p0, 66, 2)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 140))) * (1 + .0005 * f)
    k = kick(f, m0, .5)
    return c, (640, 1060 + k * 6, z, k), 'dusk'


def s6(f):
    """fim: estrada até Dublin; PAZ? no horizonte."""
    c = CEN('deserto', 'dusk').copy()
    d0 = wt(6, 'Dublin') - 3; z0 = wt(6, 'Zelensky') - 3
    d = ImageDraw.Draw(c)
    d.polygon([(380, 1700), (860, 1700), (660, 1000), (620, 1000)], fill=hexc('#6b6f7a'), outline=INK)
    for i in range(8):
        t = ((i + f * .03) % 8) / 8
        y = lerp(1000, 1700, t * t); w = lerp(3, 18, t * t); hh = lerp(6, 60, t * t)
        d.rectangle([640 - w, y, 640 + w, y + hh], fill=UYEL)
    paste_c(c, bandeira(), 260, 1380, .3)
    paste_c(c, bandeira_ru(), 1000, 1380, .3)
    num(c, 'DEPOIS: DUBLIN', 640, 560, f, d0, 90, -3)
    num(c, 'CONVERSA COM ZELENSKY', 640, 720, f, z0, 62, 2)
    num(c, 'PAZ?', 640, 900, f, z0 + 14, 130, 3)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 120))) * (1 + .0005 * f)
    return c, (640, lerp(1150, 1000, smooth(ramp(f, 0, 120))), z, .5 * math.sin(f * .05)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.ting(s.W(0, 'troca') - 3, .3)
    s.thunk(s.W(0, 'maior') - 3, 140, .5)
    s.ting(s.W(1, 'Abu') - 3, .25)
    s.thunk(s.W(2, 'mil') - 3, 150, .5)
    s.thunk(s.W(3, 'cessar-fogo') - 3, 140, .5)
    s.ting(s.W(4, 'nove') - 3, .3)
    s.thunk(s.W(5, 'Moscou') - 3, 140, .4)
    s.ting(s.W(6, 'Dublin') - 3, .3)
