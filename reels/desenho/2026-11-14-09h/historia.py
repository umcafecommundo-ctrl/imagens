"""Um Café com o Mundo — O MUNDO EXPLICADO (sábado 14/11/2026, 09h).
Tema: EUA param todas as decolagens do país (ground stop nacional da FAA) na sexta 13/11/2026.
Fontes (conferidas em 14/11/2026):
- Al Jazeera, 14/11/2026 "FAA ground stop lifted: Why were US flights grounded, and what's next?": emitido 15h54 ET
  (17h54 Brasília) de sexta 13/11, suspenso 20h15 ET (mais de 4 horas); aviões no ar puderam pousar; causa: pane de
  telecomunicações nos centros de controle de rota; segundo o secretário Sean Duffy, switches e roteadores ficaram
  sobrecarregados de dados e caíram; Markwayne Mullin (Segurança Interna): não foi ataque cibernético; FlightRadar24:
  mais de 4.700 cancelamentos e 10.000 atrasos na sexta; relatório do GAO de setembro/2026 alertou para cabos de cobre
  antigos dos anos 1960; Duffy espera operação normal até o Dia de Ação de Graças (26/11), um dos períodos de mais viagens.
- Al Jazeera, 13/11/2026 "US flights resume after FAA lifts hours-long nationwide ground stop": 1ª parada nacional desde
  janeiro de 2023; a anterior foi depois dos atentados de 11 de setembro de 2001.
- CNBC, 13/11/2026 (manchete): "FAA lifts ground stop after more than four hours, but flight cancellations will stretch into the weekend".
Personagens genéricos; aviões sem logotipo nem nome de companhia."""
from kit import *
import kit
from cenarios import _ceu, _janela, _piso_azulejo, _nuvens, _done, CEUS

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Os Estados Unidos mandaram parar todas as decolagens do país.",
    "Foi na sexta, no fim da tarde: uma pane de comunicação no controle aéreo travou os voos por mais de quatro horas.",
    "Uma parada nacional assim não acontecia desde dois mil e vinte e três. Antes disso, só depois do Onze de Setembro.",
    "Mais de quatro mil e setecentos voos foram cancelados, e dez mil atrasaram.",
    "A causa? Equipamentos de rede ficaram sobrecarregados e caíram. O governo diz que não foi ataque hacker.",
    "Por que importa? Um relatório de setembro já alertava para cabos de cobre dos anos sessenta no sistema.",
    "Os voos voltam aos poucos, e o governo quer tudo normal até o feriado de Ação de Graças, no fim do mês.",
]
CAPTXT = [
    "Os Estados Unidos mandaram parar|todas as decolagens do país.",
    "Foi na sexta, no fim da tarde:|uma pane de comunicação no controle aéreo|travou os voos por mais de 4 horas.",
    "Uma parada nacional assim|não acontecia desde 2023.|Antes disso, só depois do 11 de Setembro.",
    "Mais de 4.700 voos foram cancelados,|e 10 mil atrasaram.",
    "A causa? Equipamentos de rede|ficaram sobrecarregados e caíram.|O governo diz que não foi ataque hacker.",
    "Por que importa? Um relatório de setembro|já alertava para cabos de cobre|dos anos 60 no sistema.",
    "Os voos voltam aos poucos, e o governo|quer tudo normal até o feriado|de Ação de Graças, no fim do mês.",
]
FALA_TIKTOK = "Você já ficou preso num aeroporto? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'parar', 6), (0, 'pais', 6), (1, 'pane', 6), (1, 'quatro', 6), (2, 'vinte', 6), (2, 'Setembro', 6),
         (3, 'setecentos', 4), (3, 'dez', 6), (4, 'sobrecarregados', 6), (4, 'hacker', 6), (5, 'cobre', 6),
         (5, 'sessenta', 6), (6, 'poucos', 6), (6, 'Graças', 6)]

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



# ------------------------------------------------------------------ desenhos novos (14/11)
@lru_cache(maxsize=4)
def aeroporto(luz='day'):
    """pátio de aeroporto: céu, terminal comprido ao fundo, grama, asfalto com faixa. chão y~1300-2208."""
    W, H = BW, BH
    hz = 1250; base = _ceu(luz, hz); p = Pen(W, H)
    _nuvens(p, 5, 150, 520, 3, (255, 255, 255) if luz == 'day' else mul(hexc(CEUS[luz][1]), 1.05))
    # terminal
    p.shape([(-20, hz - 230), (W + 20, hz - 230), (W + 20, hz + 20), (-20, hz + 20)], hexc('#c9d3de'), hexc('#9eabb9'), 6, 10)
    for x in range(10, W, 70):
        p.poly([(x, hz - 200), (x + 54, hz - 200), (x + 54, hz - 40), (x, hz - 40)], hexc('#fff3b0') if luz == 'dusk' and (x // 70) % 3 == 0 else hexc('#8fb8d0'))
    p.shape([(-20, hz - 260), (W + 20, hz - 260), (W + 20, hz - 225), (-20, hz - 225)], hexc('#7d8a99'), hexc('#5f6b78'), 5, 4)
    g = hexc('#7fb05a') if luz == 'day' else mul(hexc('#7fb05a'), .75)
    p.poly([(0, hz + 20), (W, hz + 20), (W, hz + 110), (0, hz + 110)], g)
    asf = hexc('#6b6d74') if luz == 'day' else mul(hexc('#6b6d74'), .8)
    p.poly([(0, hz + 110), (W, hz + 110), (W, H), (0, H)], asf)
    p.stroke([(0, hz + 110), (W, hz + 110)], 6)
    for x in range(-40, W, 200): p.poly([(x, 1760), (x + 120, 1760), (x + 120, 1782), (x, 1782)], hexc('#f2f2f2'))
    p.poly([(0, 1440), (W, 1440), (W, 1452), (0, 1452)], hexc('#f0c541'))
    return _done(base, p)


@lru_cache(maxsize=4)
def terminal(luz='day'):
    """saguão do aeroporto: parede clara, janelão para o pátio, piso. chão y~1500."""
    W, H = BW, BH
    base = Image.new('RGBA', (W, H), hexc('#e3e6ec') + (255,)); p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, 1500), (0, 1500)], hexc('#e3e6ec'))
    _janela(p, 60, 1050, W - 60, 1440, luz, predios=False, cruz=False)
    for x in range(60, W - 60, 280): p.stroke([(x, 1050), (x, 1440)], 10, hexc('#f7f7f2'))
    _piso_azulejo(p, 1500, '#d9dde4', '#c7ccd5')
    return _done(base, p)


@lru_cache(maxsize=8)
def aviao(col='#2f6fd6'):
    """avião de passageiros de lado, nariz para a direita, sem marca. 1000x420, rodas y~405."""
    p = Pen(1000, 420)
    c = hexc(col)
    # cauda
    p.shape([(70, 170), (40, 20), (110, 20), (230, 170)], c, mul(c, .75), 6, 6)
    p.shape([(60, 205), (10, 190), (10, 225), (150, 230)], c, mul(c, .75), 5, 4)
    # fuselagem
    body = [(70, 160), (800, 150)] + curve((800, 150), (985, 170), (950, 275), 10) + [(120, 285), (60, 240)]
    p.shape(body, hexc('#f7f7f4'), hexc('#cfd3da'), 7, 18)
    p.poly([(90, 235), (950, 235), (940, 255), (110, 258)], c)
    for x in range(200, 820, 52): p.dot(x, 195, 12, hexc('#5f7a99'), 3)
    p.poly([(890, 178), (945, 182), (955, 205), (895, 205)], hexc('#5f7a99'), 4)
    # asa e motor
    p.shape([(420, 245), (600, 245), (430, 355), (370, 355)], hexc('#c9ced8'), hexc('#9aa1ae'), 6, 6)
    p.shape(ell_pts(520, 312, 70, 30, 30), hexc('#9aa1ae'), hexc('#6b7380'), 5, 4)
    # rodas
    for x in (300, 820):
        p.stroke([(x, 280), (x, 370)], 10, hexc('#6b6d74'))
        p.dot(x, 385, 22, hexc('#2a2a30'), 4)
    return fin(p)


@lru_cache(maxsize=4)
def torre_ctrl(ok=1):
    """torre de controle. 400x1100, base y~1090."""
    p = Pen(400, 1100)
    p.shape([(150, 340), (250, 340), (270, 1090), (130, 1090)], hexc('#e8e4dc'), hexc('#c4bdb0'), 6, 10)
    p.shape([(60, 180), (340, 180), (300, 340), (100, 340)], hexc('#5a6b80'), hexc('#3e4b5c'), 6, 8)
    for x in range(85, 320, 50): p.poly([(x, 200), (x + 36, 200), (x + 30, 300), (x + 6, 300)], hexc('#9fd0f0') if ok else hexc('#e8a0a0'))
    p.shape([(40, 150), (360, 150), (360, 185), (40, 185)], hexc('#e8e4dc'), hexc('#c4bdb0'), 5, 4)
    p.stroke([(200, 150), (200, 40)], 10)
    p.dot(200, 34, 18, hexc('#3aa66a') if ok else hexc('#d8443c'), 5)
    return fin(p)


@lru_cache(maxsize=2)
def mala(col='#d8443c'):
    p = Pen(260, 340)
    h = hexc(col)
    p.stroke([(90, 80), (90, 20), (170, 20), (170, 80)], 12, hexc('#555555'))
    p.shape([(20, 80), (240, 80), (240, 300), (20, 300)], h, mul(h, .75), 6, 10)
    for x in (90, 170): p.stroke([(x, 90), (x, 290)], 6, mul(h, .7))
    for x in (50, 210): p.dot(x, 315, 18, hexc('#2a2a30'), 3)
    return fin(p)


@lru_cache(maxsize=2)
def cabo():
    """rolo de cabo de cobre velho. 600x420"""
    p = Pen(600, 420)
    cu = hexc('#c87533'); cud = hexc('#8e4f1f')
    p.shape(ell_pts(300, 220, 230, 160, 60), cu, cud, 7, 12)
    for k in range(5):
        p.arc(300, 220, 200 - k * 34, 135 - k * 24, 0, 360, 10, cud)
    p.shape(ell_pts(300, 220, 50, 34, 30), hexc('#5a3a20'), hexc('#3a2410'), 5, 2)
    pts = curve((500, 260), (580, 330), (520, 400), 10)
    p.line(pts, cu, 22, 5)
    for dx in (-10, 0, 10): p.stroke([(520, 400), (520 + dx * 2, 418)], 4, hexc('#e8a060'))
    return fin(p)


def painel(c, x, y, w, rows, f, c0, step=6):
    """painel de partidas: linhas viram CANCELADO a partir de c0."""
    d = ImageDraw.Draw(c)
    h = 90 * rows + 120
    d.rectangle([x - w / 2 + 10, y + 10, x + w / 2 + 10, y + h + 10], fill=INK)
    d.rectangle([x - w / 2, y, x + w / 2, y + h], fill=hexc('#1e2433'), outline=INK, width=7)
    paste_c(c, txt('PARTIDAS', 54, 0), x, y + 60, 1)
    for r in range(rows):
        ry = y + 120 + r * 90
        d.rectangle([x - w / 2 + 30, ry + 15, x - w / 2 + 160, ry + 60], fill=hexc('#f0c541'))
        d.rectangle([x - w / 2 + 190, ry + 25, x - 40, ry + 50], fill=hexc('#7a8296'))
        st = c0 + r * step
        if f >= st:
            d.rectangle([x + 10, ry + 10, x + w / 2 - 30, ry + 66], fill=hexc('#d8443c'), outline=INK, width=4)
            paste_c(c, txt('CANCELADO', 38, 0), x + w / 4 - 10, ry + 38, back(ramp(f, st, st + 6)))
        else:
            d.rectangle([x + 10, ry + 10, x + w / 2 - 30, ry + 66], fill=hexc('#3aa66a'), outline=INK, width=4)


def put_aviao(c, x, wheels_y, w, col='#2f6fd6', rot=0, flip=False):
    im = aviao(col).resize((int(w), int(w * .42)), Image.LANCZOS)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(wheels_y - im.size[1] * .97)))


def ondas(c, x, y, f, bad=False):
    d = ImageDraw.Draw(c)
    for k in range(3):
        r = 60 + ((f * 3 + k * 40) % 120)
        col = hexc('#d8443c') if bad else hexc('#3aa66a')
        for s in (-1, 1):
            d.arc([x - r, y - r, x + r, y + r], 200 if s < 0 else -20, 340 if s < 0 else 20, fill=INK, width=12)
            d.arc([x - r, y - r, x + r, y + r], 200 if s < 0 else -20, 340 if s < 0 else 20, fill=col, width=7)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = aeroporto('day').copy()
    p0 = wt(0, 'parar') - 3
    paste_c(c, torre_ctrl(1).resize((240, 660)), 1080, 900, 1)
    put_aviao(c, 330, 1560, 520, '#d8443c')
    put_aviao(c, 930, 1600, 520, '#3aa66a')
    # avião taxiando que freia na palavra 'parar'
    xm = lerp(-200, 560, easeOut(ramp(f, 0, p0)))
    put_aviao(c, xm, 1820, 760, '#2f6fd6')
    num(c, 'EUA', 640, 380, f, 0, 150, -4)
    num(c, 'TODAS AS DECOLAGENS', 640, 560, f, wt(0, 'todas') - 3, 84, 3)
    if f >= p0:
        paste_c(c, txt('PARADAS!', 150, -5), 640, 760, back(ramp(f, p0, p0 + 8)))
        xis(c, 560, 1620, 120, back(ramp(f, p0 + 2, p0 + 10)))
    z = lerp(1.3, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, p0)
    return c, (640, 1120 + k * 8, z, k), 'day'


def s1(f):
    c = aeroporto('golden').copy()
    pn = wt(1, 'pane') - 3
    bad = f >= pn
    paste_c(c, torre_ctrl(0 if bad else 1).resize((280, 770)), 230, 980, 1)
    ondas(c, 230, 670, f, bad)
    if bad: xis(c, 230, 580, 70, back(ramp(f, pn, pn + 8)))
    num(c, 'SEXTA, 13/11', 760, 470, f, 0, 84, -3)
    num(c, 'PANE NO', 760, 640, f, pn + 2, 70, 3)
    num(c, 'CONTROLE AÉREO', 760, 740, f, pn + 4, 64, -2)
    q0 = wt(1, 'quatro') - 3
    if f >= q0 - 10:
        paste_c(c, clock_img(-90 + (f - q0) * 9, -90 + (f - q0) * 40, 260), 780, 960, back(ramp(f, q0 - 10, q0)))
        num(c, '+4 HORAS', 780, 1170, f, q0, 110, -4)
    put_aviao(c, 700, 1650, 520, '#2f6fd6')
    put_aviao(c, 1080, 1820, 480, '#3aa66a', flip=True)
    t = smooth(ramp(f, 0, 150))
    k = kick(f, pn, .8)
    return c, (640 + 10 * math.sin(f * .03), lerp(1060, 1100, t) + k * 8, lerp(1.0, 1.05, t) * (1 + .0003 * f), k), 'golden'


def s2(f):
    c = aeroporto('dusk').copy()
    d = ImageDraw.Draw(c)
    y = 900
    d.line([(140, y + 6), (1100, y + 6)], fill=INK, width=20); d.line([(140, y), (1100, y)], fill=hexc('#f0c541'), width=12)
    a0 = wt(2, 'Setembro') - 3; b0 = wt(2, 'vinte') - 3
    for x, lab, st in ((260, '2001', a0), (640, '2023', b0), (1000, '2026', 0)):
        marcador(c, x, y - 10, back(ramp(f, st, st + 8)), hexc('#d8443c') if lab == '2026' else None)
        num(c, lab, x, y - 200, f, st, 110, -3)
    num(c, 'PARADA NACIONAL', 640, 420, f, wt(2, 'parada') - 3, 92, -3)
    num(c, '11 DE SETEMBRO', 370, 1060, f, a0, 48, 3)
    put_aviao(c, 640, 1700, 700, '#2f6fd6')
    t = smooth(ramp(f, 0, 180))
    return c, (640 + 20 * math.sin(f * .04), 1060 - .3 * f, lerp(1.06, 1.0, t) * (1 + .0009 * f), lerp(0, -1.5, t) - .006 * f), 'dusk'


def s3(f):
    c = terminal('golden').copy()
    c0 = wt(3, 'quatro') - 6
    painel(c, 640, 300, 900, 6, f, c0, 4)
    num(c, '+4.700 CANCELADOS', 640, 1060, f, wt(3, 'setecentos') - 3, 82, -3)
    num(c, '10 MIL ATRASOS', 640, 1210, f, wt(3, 'dez') - 3, 92, 3)
    sh = f >= c0
    for x, sd, sk, hr, su, fl in ((230, 4, 0, '#3a2a20', '#5a3a6a', 1), (1010, 8, 2, '#1e1a18', '#3a5a4a', -1)):
        paste_c(c, mala('#d8443c' if sd == 4 else '#2f6fd6').resize((150, 196)), x + fl * 150, 1640, 1)
        put_pol(c, x, 1760, 560, f, sd, skin=sk, hair=hr, tie=None, suit=su, bun=sd == 4,
                expr='shock' if sh else 'neutral', arms='cheek' if sh else 'hang', look=0)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, wt(3, 'setecentos') - 3, .8)
    return c, (640 + 15 * math.sin(f * .04), lerp(820, 1000, t) + k * 8 - .4 * f, lerp(1.12, 1.0, t) * (1 + .0012 * f), k + .005 * f), 'golden'


def s4(f):
    c = CEN('fabrica', 'dusk').copy()
    s0_ = wt(4, 'sobrecarregados') - 3
    o0 = wt(4, 'cairam') - 3
    h0 = wt(4, 'hacker') - 3
    num(c, 'EQUIPAMENTOS DE REDE', 640, 440, f, wt(4, 'equipamentos') - 3, 66, -3)
    for i in range(4):
        x = 220 + i * 270
        hot = f >= s0_ and f < o0 + i * 3
        off = f >= o0 + i * 3
        jit = 4 * math.sin(f * 1.7 + i) if hot else 0
        paste_c(c, rack(0 if off else 1, 1 if hot else 0).resize((200, 500)), x + jit, 1000 + 4 * math.sin(f * .2 + i), 1)
    num(c, 'SOBRECARGA!', 640, 600, f, s0_, 100, 3)
    if f < h0 - 6: num(c, 'CAÍRAM', 640, 1340, f, o0, 100, -3)
    if f >= h0 - 6:
        paste_c(c, cadeado().resize((240, 304)), 640, 980, back(ramp(f, h0 - 6, h0 + 2)))
        check(c, 640, 1030, 70, back(ramp(f, h0, h0 + 8)))
        num(c, 'NÃO FOI ATAQUE HACKER', 640, 1330, f, h0, 70, -2)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, o0, .8)
    return c, (640 + 12 * math.sin(f * .05), lerp(1060, 1100, t) + k * 8, lerp(1.0, 1.04, t) * (1 + .0003 * f), lerp(0, -1.5, t) + k), 'dusk'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    num(c, 'POR QUE IMPORTA?', 640, 360, f, 0, 96, -3)
    r0 = wt(5, 'relatorio') - 3
    if f >= r0:
        paste_c(c, pasta().resize((340, 266)), 330, 720, back(ramp(f, r0, r0 + 8)))
        num(c, 'SETEMBRO', 330, 560, f, wt(5, 'setembro') - 3, 64, -3)
    a0 = wt(5, 'alertava') - 3
    num(c, 'ALERTA!', 330, 900, f, a0, 80, 4)
    c0 = wt(5, 'cabos') - 3
    if f >= c0:
        paste_c(c, cabo().resize((440, 308)), 880, 780, back(ramp(f, c0, c0 + 8)))
        num(c, 'CABOS DE COBRE', 860, 580, f, wt(5, 'cobre') - 3, 56, 3)
    num(c, 'ANOS 60', 880, 1000, f, wt(5, 'sessenta') - 3, 100, -4)
    put_pol(c, 640, 1700, 560, f, 11, skin=1, hair='#6b6b70', tie='#2f6fd6', suit='#3a3a44',
            expr='nervous' if f >= c0 else 'neutral', arms='point' if f >= a0 else 'hang', look=1 if f >= c0 else -1)
    t = smooth(ramp(f, 0, 160))
    k = kick(f, wt(5, 'sessenta') - 3, .6)
    return c, (640, lerp(1000, 1040, t) + k * 6, lerp(1.0, 1.05, t) * (1 + .0003 * f), lerp(0, 1.5, t) + k), 'dusk'


def s6(f):
    c = aeroporto('golden').copy()
    paste_c(c, torre_ctrl(1).resize((260, 715)), 140, 880, 1)
    p0 = wt(6, 'poucos') - 3
    for i in range(3):
        st = 5 + i * 45
        t = ramp(f, st, st + 95)
        x = lerp(200, 1500, t ** 1.6); y = 1700 - 900 * max(0, t - .35) ** 1.5
        rot = 12 * smooth(ramp(t, .3, .5))
        put_aviao(c, x, y, 560, ('#2f6fd6', '#d8443c', '#3aa66a')[i], rot)
    num(c, 'VOLTANDO AOS POUCOS', 640, 400, f, p0, 76, -3)
    g0 = wt(6, 'Gracas') - 3
    if f >= g0 - 6:
        paste_c(c, calendario().resize((300, 312)), 640, 820, back(ramp(f, g0 - 6, g0 + 2)))
        num(c, 'FERIADO DE', 640, 1040, f, g0 - 2, 64, 3)
        num(c, 'AÇÃO DE GRAÇAS', 640, 1150, f, g0, 84, -3)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 120))) + .0004 * f
    return c, (640, 1080, z, lerp(0, 1.5, smooth(ramp(f, 0, 120)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.engine(0, s.W(0, 'parar') - 3, .2)
    s.thunk(s.W(0, 'parar') - 3, 140, 1.0)
    s.thunk(s.W(1, 'pane') - 3, 150, .8)
    s.ting(s.W(1, 'quatro') - 3, .3)
    s.ting(s.W(2, 'vinte') - 3, .25)
    s.ting(s.W(2, 'Setembro') - 3, .25)
    s.thunk(s.W(3, 'setecentos') - 3, 130, 1.0)
    s.thunk(s.W(3, 'dez') - 3, 160, .7)
    s.thunk(s.W(4, 'cairam') - 3, 120, .9)
    s.thunk(s.W(4, 'hacker') - 3, 150, .6)
    s.ting(s.W(5, 'cabos') - 3, .3)
    s.thunk(s.W(5, 'sessenta') - 3, 140, .7)
    s.whoosh(s.W(6, 'poucos') - 3, .3, .5)
    s.ting(s.W(6, 'Gracas') - 3, .4)
