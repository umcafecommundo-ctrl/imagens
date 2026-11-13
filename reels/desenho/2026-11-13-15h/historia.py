"""Um Café com o Mundo — O MUNDO EXPLICADO (sexta 13/11/2026, 15h).
Tema: apagão global da Microsoft (Outlook, Teams, Copilot) que durou quase 1 dia.
Fontes (conferidas em 13/11/2026):
- TechRadar (live, 12-13/11/2026): começou na tarde de quinta 12/11 (Américas); pico de mais de 131 mil queixas no
  Downdetector para o Outlook nos EUA; Outlook, Microsoft 365, Copilot e Teams; causa segundo a Microsoft: muitos
  servidores ficaram indisponíveis de repente ("elevated load") e depois "problema numa atualização anterior de
  capacidade da rede"; "não relacionado a ataque cibernético"; na sexta de manhã prefeituras e polícia do Reino Unido
  avisaram de problemas; às ~10h40 ET de 13/11 filas de e-mail "se aproximando do normal"; relatório pós-incidente prometido.
- SecurityWeek (12/11/2026): grande número de servidores indisponíveis, restantes sobrecarregados; Exchange Online,
  Outlook, Teams, SharePoint, Copilot; sem sinal de ataque.
- CNN (13/11/2026): "Email service is 'approaching normal levels' following widespread global outage".
Personagens genéricos; sem logotipos nem nomes de marca desenhados."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Uma falha na Microsoft deixou empresas do mundo todo quase um dia sem e-mail.",
    "Começou na tarde de quinta, nas Américas: o Outlook, o Teams e o assistente Copilot pararam de funcionar.",
    "Só nos Estados Unidos, foram mais de cento e trinta mil queixas, e o problema se espalhou por outros países.",
    "A causa? Muitos servidores saíram do ar de repente, e os que sobraram não deram conta.",
    "A Microsoft diz que foi um erro numa atualização da rede, e não um ataque hacker.",
    "Por que importa? Empresas e governos dependem da mesma nuvem; no Reino Unido, até prefeituras e a polícia relataram problemas.",
    "Quase vinte e quatro horas depois, os e-mails voltavam ao normal, e a empresa promete um relatório.",
]
CAPTXT = [
    "Uma falha na Microsoft deixou empresas|do mundo todo quase um dia sem e-mail.",
    "Começou na tarde de quinta, nas Américas:|o Outlook, o Teams e o assistente Copilot|pararam de funcionar.",
    "Só nos Estados Unidos,|foram mais de 130 mil queixas,|e o problema se espalhou por outros países.",
    "A causa? Muitos servidores saíram do ar de repente,|e os que sobraram não deram conta.",
    "A Microsoft diz que foi um erro|numa atualização da rede,|e não um ataque hacker.",
    "Por que importa? Empresas e governos|dependem da mesma nuvem; no Reino Unido,|até prefeituras e a polícia relataram problemas.",
    "Quase 24 horas depois,|os e-mails voltavam ao normal,|e a empresa promete um relatório.",
]
FALA_TIKTOK = "O seu e-mail parou também? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'falha', 6), (0, 'dia', 6), (1, 'quinta', 6), (1, 'Copilot', 8), (2, 'cento', 6), (2, 'paises', 6),
         (3, 'servidores', 6), (3, 'sobraram', 8), (4, 'atualizacao', 6), (4, 'hacker', 6), (5, 'nuvem', 6),
         (5, 'policia', 6), (6, 'vinte', 6), (6, 'relatorio', 6)]

GREEN = hexc('#3aa66a'); GREEN_D = hexc('#287a4c'); RED = hexc('#d8443c'); RED_D = hexc('#a02c26')
BLUE = hexc('#2f6fd6'); BLUE_D = hexc('#1f4f9e'); GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e')
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0'); WHITE = (255, 255, 255)
CODE = hexc('#5fd08a')
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


# ------------------------------------------------------------------ desenhos novos (13/11)
@lru_cache(maxsize=4)
def notebook(err=0):
    """notebook aberto; err=1 tela vermelha de erro. 760x560"""
    p = Pen(760, 560)
    p.shape([(90, 20), (670, 20), (670, 420), (90, 420)], hexc('#3a3d4d'), hexc('#26283a'), 7, 8)
    p.poly([(120, 50), (640, 50), (640, 390), (120, 390)], hexc('#3a1418') if err else hexc('#eaf1fb'))
    if not err:
        for k in range(5):
            y = 80 + k * 60
            p.poly([(150, y), (190, y), (190, y + 34), (150, y + 34)], BLUE)
            p.stroke([(210, y + 10), (560, y + 10)], 10, hexc('#9aa3b0'))
            p.stroke([(210, y + 28), (440, y + 28)], 7, hexc('#c4cad3'))
    p.shape([(20, 430), (740, 430), (700, 540), (60, 540)], hexc('#8d93a0'), hexc('#5f6470'), 7, 8)
    return fin(p)


@lru_cache(maxsize=2)
def envelope():
    p = Pen(340, 240)
    p.shape([(10, 10), (330, 10), (330, 230), (10, 230)], WHITE, hexc('#c9c9d2'), 5, 6)
    p.stroke([(10, 10), (170, 130), (330, 10)], 5)
    p.dot(170, 130, 26, BLUE, 3)
    return fin(p)


@lru_cache(maxsize=4)
def balao(col='#7b6ad8'):
    """balão de conversa (chamada/chat). 300x260"""
    p = Pen(300, 260)
    h = hexc(col)
    p.shape(ell_pts(150, 110, 130, 95, 40), h, mul(h, .7), 6, 8)
    p.shape([(80, 180), (60, 250), (140, 195)], h, mul(h, .7), 5, 4)
    for x in (100, 150, 200): p.dot(x, 110, 16, WHITE, 3)
    return fin(p)


@lru_cache(maxsize=2)
def estrela():
    """ícone de assistente (estrela de 4 pontas). 300x300"""
    p = Pen(300, 300)
    pts = []
    for i in range(8):
        a = i * math.pi / 4 - math.pi / 2
        r = 140 if i % 2 == 0 else 45
        pts.append((150 + r * math.cos(a), 150 + r * math.sin(a)))
    p.shape(pts, GOLD, GOLD_D, 6, 6)
    return fin(p)


@lru_cache(maxsize=8)
def rack(on=1, hot=0):
    """armário de servidores; on=0 apagado (luzes vermelhas); hot=1 suando/sobrecarregado. 360x900, base y~890"""
    p = Pen(360, 900)
    p.shape([(30, 20), (330, 20), (330, 890), (30, 890)], hexc('#3a3d4d'), hexc('#26283a'), 7, 12)
    for k in range(8):
        y = 60 + k * 102
        p.shape([(55, y), (305, y), (305, y + 80), (55, y + 80)], hexc('#555a6b') if on else hexc('#2e3038'), hexc('#3a3d4d'), 4, 3)
        for j in range(3):
            p.stroke([(80, y + 20 + j * 20), (200, y + 20 + j * 20)], 5, hexc('#7a8090') if on else hexc('#3a3d4a'))
        led = (hexc('#ff8a3a') if hot else CODE) if on else RED
        p.dot(270, y + 40, 13, led, 3)
    return fin(p)


@lru_cache(maxsize=2)
def nuvem():
    """nuvem simples. 700x420"""
    p = Pen(700, 420)
    blob = []
    for i in range(80):
        a = i / 80 * 2 * math.pi
        r = 1 + .12 * math.sin(a * 5)
        blob.append((350 + 300 * r * math.cos(a), 240 + 150 * r * math.sin(a)))
    p.shape(blob, hexc('#ffffff'), hexc('#c9d6e8'), 7, 14)
    return fin(p)


@lru_cache(maxsize=2)
def chave():
    """chave inglesa. 520x200"""
    p = Pen(520, 200)
    p.shape([(140, 80), (500, 80), (500, 120), (140, 120)], hexc('#9aa3b0'), hexc('#6b7380'), 6, 6)
    p.shape([(60, 40), (170, 40), (170, 160), (60, 160)], hexc('#9aa3b0'), hexc('#6b7380'), 6, 6)
    p.shape([(10, 20), (80, 20), (80, 70), (10, 70)], hexc('#9aa3b0'), hexc('#6b7380'), 6, 4)
    p.shape([(10, 130), (80, 130), (80, 180), (10, 180)], hexc('#9aa3b0'), hexc('#6b7380'), 6, 4)
    return fin(p)


@lru_cache(maxsize=2)
def cadeado():
    """cadeado fechado (seguro). 300x380"""
    p = Pen(300, 380)
    p.arc(150, 140, 90, 100, 180, 360, 26, hexc('#9aa3b0'))
    p.stroke([(60, 140), (60, 180)], 26, hexc('#9aa3b0')); p.stroke([(240, 140), (240, 180)], 26, hexc('#9aa3b0'))
    p.shape([(30, 170), (270, 170), (270, 360), (30, 360)], GOLD, GOLD_D, 7, 12)
    p.dot(150, 250, 26, INK, 0)
    p.stroke([(150, 250), (150, 310)], 16)
    return fin(p)


@lru_cache(maxsize=2)
def globo():
    """Terra (globo simples). 700x700"""
    p = Pen(700, 700)
    p.shape(ell_pts(350, 350, 300, 300, 80), hexc('#3a7fd0'), hexc('#2a5fa4'), 7, 26)
    for lx, ly, rx, ry, rot in ((250, 240, 110, 80, .3), (430, 330, 120, 150, -.2), (230, 470, 80, 60, .5), (480, 160, 60, 40, 0)):
        p.shape(ell_pts(lx, ly, rx, ry, 30, rot, .15), hexc('#7fb05a'), hexc('#5f8a40'), 5, 8)
    return fin(p)


def xis(c, x, y, size, t):
    if t <= 0: return
    d = ImageDraw.Draw(c)
    a = size * min(1, t)
    for s in (1, -1):
        d.line([(x - a, y - s * a), (x + a, y + s * a)], fill=INK, width=34)
        d.line([(x - a, y - s * a), (x + a, y + s * a)], fill=RED, width=22)


def check(c, x, y, size, t):
    if t <= 0: return
    d = ImageDraw.Draw(c)
    a = size * min(1, t)
    pts = [(x - a, y), (x - a * .3, y + a * .7), (x + a, y - a * .8)]
    d.line(pts, fill=INK, width=36); d.line(pts, fill=GREEN, width=24)


def marcador(c, x, y, s=1.0, col=None):
    if s <= .02: return
    d = ImageDraw.Draw(c)
    col = col or RED
    r = 34 * s
    pts = [(x, y), (x - r, y - r * 1.6), (x + r, y - r * 1.6)]
    d.polygon(pts, fill=col, outline=INK, width=5)
    d.ellipse([x - r, y - r * 2.6, x + r, y - r * .6], fill=col, outline=INK, width=6)
    d.ellipse([x - r * .38, y - r * 1.98, x + r * .38, y - r * 1.22], fill=WHITE)


def env_voando(c, x0, y0, x1, y1, t, w=150, rot=0):
    if t <= 0 or t >= 1: return
    im = envelope().resize((w, int(w * .7))).rotate(rot + 20 * math.sin(t * 6), expand=True, resample=Image.BICUBIC)
    paste_c(c, im, lerp(x0, x1, t), lerp(y0, y1, t) - 160 * math.sin(t * math.pi), 1)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('escritorio', 'day').copy()
    f0 = wt(0, 'falha') - 3
    err = f >= f0
    paste_c(c, notebook(1 if err else 0).resize((640, 472)), 560, 900, 1)
    if not err:
        for i in range(4):
            t = ((f + i * 9) % 36) / 36
            env_voando(c, 1200, 500, 560, 860, t, 120, i * 20)
    xis(c, 560, 860, 110, back(ramp(f, f0, f0 + 8)))
    num(c, 'SEM E-MAIL', 560, 420, f, f0 + 4, 120, -3)
    d0 = wt(0, 'dia') - 3
    num(c, 'QUASE 1 DIA', 600, 1240, f, d0, 100, 3)
    put_pol(c, 900, 1660, 500, f, 3, skin=1, hair='#2a221e', tie='#2f6fd6', suit='#4a4f63',
            expr='shock' if err else 'neutral', arms='up' if f > f0 + 4 else 'hang', look=-1)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, f0)
    return c, (640, 1020 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('mapa', 'day').copy()
    num(c, 'QUINTA, 12/11', 640, 380, f, 0, 96, -3)
    a0 = wt(1, 'Americas') - 3
    num(c, 'AMÉRICAS', 380, 600, f, a0, 90, 3)
    marcador(c, 380, 820, back(ramp(f, a0, a0 + 8)))
    items = [('outlook', envelope().resize((220, 155)), 'E-MAIL'), ('teams', balao().resize((200, 173)), 'CHAMADAS'),
             ('copilot', estrela().resize((190, 190)), 'ASSISTENTE')]
    p0 = wt(1, 'pararam') - 3
    for i, (w, im, lab) in enumerate(items):
        st = wt(1, w) - 3
        x = 330 + i * 310; y = 1120
        if f >= st:
            paste_c(c, im, x, y + 8 * math.sin(f * .12 + i), back(ramp(f, st, st + 8)))
            paste_c(c, txt(lab, 42, (-3, 3, -2)[i]), x, y + 150, back(ramp(f, st + 2, st + 10)))
        xis(c, x, y, 80, back(ramp(f, p0 + i * 3, p0 + i * 3 + 8)))
    t = smooth(ramp(f, 0, 150))
    k = kick(f, p0, .7)
    return c, (640 + 20 * math.sin(f * .03), lerp(1000, 960, t) + k * 8, lerp(1.06, 1.12, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = CEN('escritorio', 'golden').copy()
    q0 = wt(2, 'cento') - 3
    num(c, 'SÓ NOS EUA', 640, 380, f, wt(2, 'Estados') - 3, 84, 3)
    num(c, '+130 MIL', 640, 560, f, q0, 180, -4)
    num(c, 'QUEIXAS', 640, 720, f, wt(2, 'queixas') - 3, 100, 3)
    p0 = wt(2, 'espalhou') - 3
    gs = back(ramp(f, p0 - 6, p0 + 4)) if f >= p0 - 6 else 0
    if gs > 0:
        paste_c(c, globo().resize((520, 520)), 640, 1100, gs)
        for i, (dx, dy) in enumerate(((-150, -120), (60, -170), (170, -20), (-60, 40), (-180, 100), (110, 160), (20, -60))):
            st = p0 + i * 4
            marcador(c, 640 + dx, 1100 + dy, back(ramp(f, st, st + 8)) * .8)
    else:
        put_pol(c, 640, 1600, 520, f, 6, skin=2, hair='#3a2a20', tie='#d8443c', suit='#3a3a44', expr='shock', arms='cheek')
    num(c, 'OUTROS PAÍSES', 640, 1450, f, wt(2, 'paises') - 3, 80, -3)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, q0, .9)
    return c, (640 + 22 * math.sin(f * .05), lerp(900, 1040, t) + k * 8, lerp(1.12, 1.0, t) * (1 + .0010 * f), lerp(0, 1.5, t) + k), 'golden'


def s3(f):
    c = CEN('fabrica', 'dusk').copy()
    s0_ = wt(3, 'servidores') - 3
    o0 = wt(3, 'repente') - 3
    b0 = wt(3, 'sobraram') - 3
    num(c, 'SERVIDORES', 640, 380, f, s0_, 110, -3)
    for i in range(5):
        x = 180 + i * 220
        off = f >= o0 + i * 3 and i != 2
        hot = (i == 2 and f >= b0)
        jit = 4 * math.sin(f * 1.7) if hot else 0
        paste_c(c, rack(0 if off else 1, 1 if hot else 0).resize((200, 500)), x + jit, 1180 + 4 * math.sin(f * .2 + i), 1)
    num(c, 'FORA DO AR', 640, 560, f, o0, 100, 3)
    if f >= b0:
        paste_c(c, txt('NÃO DEU CONTA!', 76, -4), 620, 820, back(ramp(f, b0 + 2, b0 + 10)))
        d = ImageDraw.Draw(c)
        for k in range(3):
            y = 940 - ((f - b0) * 4 + k * 40) % 120
            d.ellipse([600 + k * 20 - 12, y - 18, 600 + k * 20 + 12, y + 18], fill=(170, 210, 245), outline=INK, width=4)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, o0, .8)
    return c, (lerp(640, 660, t) + 25 * math.sin(f * .05), lerp(1000, 1060, t) + k * 8, (1.0 + .0012 * f) * lerp(1.0, 1.08, t), lerp(0, -2, t) + k + .8 * math.sin(f * .04)), 'dusk'


def s4(f):
    c = CEN('escritorio', 'dusk').copy()
    a0 = wt(4, 'atualizacao') - 3
    h0 = wt(4, 'hacker') - 3
    n0 = wt(4, 'nao') - 3
    num(c, 'ERRO NA ATUALIZAÇÃO', 640, 400, f, wt(4, 'erro') - 3, 74, -3)
    num(c, 'DA REDE', 640, 520, f, a0, 74, 3)
    if f >= a0:
        im = chave().resize((420, 162)).rotate(15 * math.sin(f * .25), expand=True, resample=Image.BICUBIC)
        paste_c(c, im, 400, 820, back(ramp(f, a0, a0 + 8)))
    if f >= n0 - 2:
        paste_c(c, cadeado().resize((240, 304)), 900, 860, back(ramp(f, n0 - 2, n0 + 6)))
        check(c, 900, 1060, 70, back(ramp(f, h0, h0 + 8)))
    num(c, 'NÃO FOI ATAQUE HACKER', 640, 1250, f, h0, 70, -2)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, h0, .6)
    return c, (640 + 15 * math.sin(f * .03), lerp(860, 900, t) + k * 6, lerp(1.0, 1.08, t) * (1 + .0004 * f), k), 'dusk'


def s5(f):
    c = CEN('cidade', 'dusk').copy()
    n0 = wt(5, 'nuvem') - 3
    ns = back(ramp(f, n0 - 4, n0 + 6)) if f >= n0 - 4 else 0
    num(c, 'POR QUE IMPORTA?', 640, 360, f, 0, 96, -3)
    if ns > 0:
        paste_c(c, nuvem().resize((520, 312)), 640, 610 + 10 * math.sin(f * .08), ns)
        num(c, 'NUVEM', 640, 610, f, n0, 80, 0)
        d = ImageDraw.Draw(c)
        for x in (300, 640, 980):
            d.line([(640, 740), (x, 1000)], fill=INK, width=8)
    for i, (x, w) in enumerate(((300, 260), (640, 300), (980, 260))):
        paste_c(c, sede().resize((w, int(w * 1.43))), x, 1300, 1)
    r0 = wt(5, 'Reino') - 3
    num(c, 'REINO UNIDO', 640, 920, f, r0, 84, 3)
    pf = wt(5, 'prefeituras') - 3
    pc = wt(5, 'policia') - 3
    num(c, 'PREFEITURAS', 360, 1060, f, pf, 54, -4)
    num(c, 'POLÍCIA', 930, 1060, f, pc, 62, 4)
    marcador(c, 300, 1290, back(ramp(f, pf, pf + 8)))
    marcador(c, 980, 1290, back(ramp(f, pc, pc + 8)))
    t = smooth(ramp(f, 0, 200))
    k = kick(f, pc, .6)
    return c, (640, lerp(1000, 950, t) + k * 6, lerp(1.0, 1.06, t) * (1 + .0004 * f), lerp(0, 1.5, t) + k), 'dusk'


def s6(f):
    c = CEN('escritorio', 'dusk').copy()
    v0 = wt(6, 'vinte') - 3
    num(c, 'QUASE 24 HORAS', 640, 380, f, v0, 104, -3)
    nm = wt(6, 'normal') - 3
    paste_c(c, notebook(0 if f >= nm else 1).resize((560, 413)), 520, 880, 1)
    if f >= nm - 10:
        for i in range(4):
            t = ((f - nm + 10 + i * 9) % 36) / 36
            env_voando(c, 1150, 500, 520, 850, t, 110, i * 20)
    check(c, 520, 830, 80, back(ramp(f, nm, nm + 8)))
    r0 = wt(6, 'relatorio') - 3
    if f >= r0:
        paste_c(c, pasta().resize((300, 235)), 520, 1260, back(ramp(f, r0, r0 + 8)))
        num(c, 'RELATÓRIO', 520, 1150, f, r0 + 2, 70, -3)
    put_pol(c, 1010, 1660, 600, f, 7, skin=0, hair='#c9a46a', tie=None, suit='#5a3a6a', bun=True,
            expr='proud' if f >= nm else 'nervous', arms='point' if f >= nm + 4 else 'hang', look=-1)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 90))) + .0005 * f
    return c, (640, 1040, z, lerp(0, 1.5, smooth(ramp(f, 0, 90)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'falha') - 3, 140, 1.0)
    s.ting(s.W(0, 'dia') - 3, .3)
    s.ting(s.W(1, 'Americas') - 3, .3)
    s.thunk(s.W(1, 'pararam') - 3, 150, .8)
    s.thunk(s.W(2, 'cento') - 3, 130, 1.0)
    s.whoosh(s.W(2, 'espalhou') - 3, .3, .5)
    s.thunk(s.W(3, 'repente') - 3, 120, .9)
    s.ting(s.W(4, 'atualizacao') - 3, .3)
    s.thunk(s.W(4, 'hacker') - 3, 150, .7)
    s.ting(s.W(5, 'nuvem') - 3, .3)
    s.thunk(s.W(5, 'policia') - 3, 140, .7)
    s.ting(s.W(6, 'normal') - 3, .4)
