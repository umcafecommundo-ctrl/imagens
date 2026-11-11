"""Um Café com o Mundo — O MUNDO EXPLICADO (quarta 11/11/2026, 09h).
Tema: oficial do Exército dos EUA preso na Inglaterra suspeito de espionar para a Rússia.
Fontes (conferidas em 11/11/2026):
- CBS News, 10-11/11/2026 ("U.S. soldier accused of spying linked to Russia arrested in the U.K."): soldado do Exército dos
  EUA, 41 anos, preso na terça (10/11) perto de Gloucester, ~100 milhas (~160 km) a oeste de Londres; segundo autoridade dos EUA,
  oficial sênior baseado em Imjin Barracks, sede do Corpo Aliado de Reação Rápida da Otan (ARRC); suspeita pelas seções 1
  (obter/revelar informação protegida) e 3 (ajudar serviço de inteligência estrangeiro) da Lei de Segurança Nacional de 2023;
  Polícia Metropolitana: atividade ligada à Rússia; Counter Terrorism Policing; dois endereços revistados em Gloucestershire;
  detido numa delegacia de Londres; a prisão ocorreu quando EUA, Rússia e Ucrânia iniciavam conversas em Abu Dhabi.
- ABC News, 11/11/2026: nome não divulgado (deve sair depois da acusação formal); Kash Patel (FBI): alegações de espionagem
  "da maior preocupação para os Estados Unidos e nossos aliados"; Brig. Gen. Sean Stinchon (contrainteligência do Exército);
  investigação em andamento.
- CNBC 11/11/2026 e Yahoo News UK confirmam a prisão.
Tom sério; personagens genéricos; sem pessoas reais desenhadas."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um oficial do Exército dos Estados Unidos foi preso na Inglaterra, suspeito de espionar para a Rússia.",
    "Foi nesta terça, perto de Gloucester, a cerca de cento e sessenta quilômetros de Londres.",
    "Ele tem quarenta e um anos e servia no quartel de Imjin, sede de um comando da Otan.",
    "A polícia antiterrorismo revistou dois endereços, e ele ficou detido numa delegacia de Londres.",
    "A suspeita é de obter informações protegidas e de ajudar um serviço de inteligência estrangeiro.",
    "Por que isso importa? O FBI diz que o caso é da maior preocupação para os Estados Unidos e aliados.",
    "E a prisão veio no mesmo dia em que americanos, russos e ucranianos voltaram a negociar a paz.",
    "O nome dele ainda não foi divulgado. E a investigação continua.",
]
CAPTXT = [
    "Um oficial do Exército dos Estados Unidos|foi preso na Inglaterra, suspeito|de espionar para a Rússia.",
    "Foi nesta terça, perto de Gloucester,|a cerca de 160 km de Londres.",
    "Ele tem 41 anos e servia no quartel de Imjin,|sede de um comando da Otan.",
    "A polícia antiterrorismo revistou|2 endereços, e ele ficou detido|numa delegacia de Londres.",
    "A suspeita é de obter informações protegidas|e de ajudar um serviço de inteligência|estrangeiro.",
    "Por que isso importa? O FBI diz que o caso|é da maior preocupação para os|Estados Unidos e aliados.",
    "E a prisão veio no mesmo dia em que americanos,|russos e ucranianos voltaram|a negociar a paz.",
    "O nome dele ainda não foi divulgado.|E a investigação continua.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Exercito', 4), (0, 'preso', 4), (0, 'Inglaterra', 4), (0, 'Russia', 4),
         (1, 'terca', 4), (1, 'Gloucester', 4), (1, 'cento', 6), (1, 'Londres', 4),
         (2, 'quarenta', 6), (2, 'Imjin', 4), (2, 'Otan', 4),
         (3, 'policia', 4), (3, 'dois', 4), (3, 'delegacia', 4),
         (4, 'obter', 4), (4, 'ajudar', 4), (4, 'estrangeiro', 4),
         (5, 'FBI', 4), (5, 'preocupacao', 4), (5, 'aliados', 4),
         (6, 'mesmo', 4), (6, 'russos', 4), (6, 'paz', 4), (7, 'nome', 4), (7, 'investigacao', 4)]

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


GRN = hexc('#2f8a4f'); GRN_D = hexc('#1f6236'); STEEL = hexc('#9aa3ad'); STEEL_D = hexc('#666e78'); NAVY = hexc('#012169')


@lru_cache(maxsize=2)
def bandeira_uk():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 270), (10, 270)], NAVY)
    p.stroke([(10, 10), (410, 270)], 46, WHITE); p.stroke([(410, 10), (10, 270)], 46, WHITE)
    p.stroke([(10, 10), (410, 270)], 14, US_R); p.stroke([(410, 10), (10, 270)], 14, US_R)
    p.poly([(10, 112), (410, 112), (410, 168), (10, 168)], WHITE)
    p.poly([(182, 10), (238, 10), (238, 270), (182, 270)], WHITE)
    p.poly([(10, 124), (410, 124), (410, 156), (10, 156)], US_R)
    p.poly([(194, 10), (226, 10), (226, 270), (194, 270)], US_R)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def lupa():
    p = Pen(400, 400)
    p.stroke([(250, 250), (370, 370)], 34, hexc('#6b4a2e'))
    p.shape(ell_pts(170, 170, 130, 130, 40), hexc('#c9e6f5'), hexc('#8fb8d0'), 10, 6)
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


@lru_cache(maxsize=2)
def algema():
    """algemas. 520x260"""
    p = Pen(520, 260)
    for cx in (130, 390):
        pts = ell_pts(cx, 140, 95, 95, 40)
        p.stroke(pts + [pts[0]], 30, INK)
        p.stroke(pts + [pts[0]], 16, STEEL)
    p.stroke([(225, 140), (295, 140)], 24, INK); p.stroke([(225, 140), (295, 140)], 10, STEEL)
    return fin(p)


def sirene(c, x, y, f, r=34):
    d = ImageDraw.Draw(c)
    on = (f // 8) % 2 == 0
    col = BLUE if on else RED
    d.ellipse([x - r - 30, y - r - 30, x + r + 30, y + r + 30], fill=mul(col, .55))
    d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=INK, width=5)


def placa_estrada(c, x, y, s, sc):
    if sc <= .05: return
    t = txt(s, 64, 0)
    im = Image.new('RGBA', (t.size[0] + 80, t.size[1] + 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([4, 4, im.size[0] - 4, im.size[1] - 4], 18, fill=GRN, outline=INK, width=8)
    d.rounded_rectangle([16, 16, im.size[0] - 16, im.size[1] - 16], 12, outline=WHITE, width=5)
    im.alpha_composite(t, (40, 30))
    dd = ImageDraw.Draw(c)
    dd.rectangle([x - 12, y, x + 12, 1560], fill=STEEL, outline=INK, width=4)
    paste_c(c, im, x, y, sc)


def quartel(c, x, base, w, h, seed=0):
    d = ImageDraw.Draw(c)
    col = hexc(['#b9a27f', '#a8946f', '#c2ad8a'][seed % 3])
    d.rectangle([x - w / 2, base - h, x + w / 2, base], fill=col, outline=INK, width=6)
    d.polygon([(x - w / 2 - 20, base - h), (x + w / 2 + 20, base - h), (x + w / 2 - 10, base - h - 70), (x - w / 2 + 10, base - h - 70)],
              fill=hexc('#6b4f45'), outline=INK)
    for q in range(int(w // 90)):
        wx = x - w / 2 + 30 + q * 90
        d.rectangle([wx, base - h + 50, wx + 50, base - h + 120], fill=LIT, outline=INK, width=3)


def cerca(c, y0, y1):
    d = ImageDraw.Draw(c)
    for x in range(0, 1242, 70):
        d.line([(x, y0), (x, y1)], fill=STEEL_D, width=6)
    for yy in (y0 + 10, (y0 + y1) / 2, y1 - 10):
        d.line([(0, yy), (1242, yy)], fill=STEEL_D, width=4)


def s0(f):
    """gancho: oficial na cidade inglesa, sirenes, algemas e a bandeira russa."""
    c = CEN('cidade', 'dusk').copy()
    e0 = wt(0, 'Exercito') - 3; p0 = wt(0, 'preso') - 3; i0 = wt(0, 'Inglaterra') - 3
    es0 = wt(0, 'espionar') - 3; r0 = wt(0, 'Russia') - 3
    mastro(c, 120, 1520, bandeira_uk(), f, 1, .55)
    if f >= i0: num(c, 'INGLATERRA', 330, 1250, f, i0, 50, -3)
    put_soldier(c, 640, 1520, 560, f, 4, expr='nervous' if f >= p0 else 'stern', arms='hang', skin=1)
    if f >= p0:
        sirene(c, 380, 1000, f); sirene(c, 900, 1000, f + 4)
        paste_c(c, algema(), 640, 1350, back(ramp(f, p0, p0 + 8)) * .45)
    num(c, 'OFICIAL DOS EUA', 640, 430, f, e0, 84, -3)
    num(c, 'PRESO', 640, 610, f, p0, 170, 3)
    num(c, 'ESPIONAGEM?', 640, 800, f, es0, 90, -2)
    if f >= r0:
        paste_c(c, bandeira_ru(), 1050, 1150, back(ramp(f, r0, r0 + 8)) * .45)
        num(c, 'RÚSSIA', 1050, 1300, f, r0, 60, 3)
    z = lerp(1.3, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, p0, .7)
    return c, (640, 1080 + k * 8, z, k), 'dusk'


def s1(f):
    """estrada no interior da Inglaterra, placa para Londres."""
    c = CEN('pasto', 'dusk').copy()
    t0 = wt(1, 'terca') - 3; g0 = wt(1, 'Gloucester') - 3; k0 = wt(1, 'cento') - 3; l0 = wt(1, 'Londres') - 3
    d = ImageDraw.Draw(c)
    d.polygon([(300, 2208), (940, 2208), (660, 1300), (620, 1300)], fill=hexc('#6b6f7a'), outline=INK)
    for i in range(8):
        t = ((i + f * .03) % 8) / 8
        y = lerp(1300, 2208, t * t); w = lerp(3, 18, t * t); hh = lerp(6, 60, t * t)
        d.rectangle([640 - w, y, 640 + w, y + hh], fill=WHITE)
    if f >= t0: calendario(c, 300, 560, 'TER', sz=back(ramp(f, t0, t0 + 8)) * .7, col=TEAL)
    if f >= g0:
        paste_c(c, marcador(), 640, 1180, back(ramp(f, g0, g0 + 8)) * .5)
        num(c, 'GLOUCESTER', 680, 820, f, g0, 100, -3)
    if f >= k0:
        placa_estrada(c, 940, 1150, 'LONDRES 160 KM', back(ramp(f, k0, k0 + 8)) * .62)
    if f >= l0: num(c, 'INGLATERRA', 640, 450, f, l0, 80, 2)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 200))) * (1 + .0005 * f)
    k = kick(f, g0, .5)
    return c, (640 + lerp(-20, 30, smooth(ramp(f, 0, 200))), 1060 + k * 6, z, k), 'dusk'


def s2(f):
    """o quartel: prédios baixos atrás da cerca, o oficial, textos 41 anos / Otan."""
    c = CEN('cidade', 'dusk').copy()
    q0 = wt(2, 'quarenta') - 3; i0 = wt(2, 'Imjin') - 3; o0 = wt(2, 'Otan') - 3
    for x, w, h, sd in ((210, 360, 330, 0), (640, 380, 380, 1), (1060, 340, 320, 2)):
        quartel(c, x, 1520, w, h, sd)
    cerca(c, 1400, 1520)
    mastro(c, 1180, 1520, bandeira_us(), f, 2, .4)
    put_soldier(c, 600, 1560, 520, f, 4, expr='neutral', arms='hang', skin=1, look=1)
    num(c, '41 ANOS', 640, 420, f, q0, 130, -3)
    num(c, 'QUARTEL DE IMJIN', 640, 590, f, i0, 84, 2)
    num(c, 'OTAN', 640, 760, f, o0, 140, -3)
    num(c, 'COMANDO DE REAÇÃO RÁPIDA', 640, 900, f, o0 + 6, 66, 2)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0006 * f)
    k = kick(f, o0, .5)
    return c, (lerp(560, 700, smooth(ramp(f, 0, 200))), 1080 + k * 6, z, .6 * math.sin(f * .04)), 'dusk'


def s3(f):
    """polícia revista endereços; sirene; delegacia em Londres."""
    c = CEN('cidade', 'dusk').copy()
    p0 = wt(3, 'policia') - 3; d0 = wt(3, 'dois') - 3; dl0 = wt(3, 'delegacia') - 3
    predio(c, 330, 1520, 360, 520, .5, 1)
    predio(c, 930, 1520, 360, 600, .3, 2)
    sirene(c, 630, 1010, f)
    put_pol(c, 330, 1560, 520, f, 2, hair='#3a3a3a', tie='#2c3550', suit='#22263a', expr='stern', look=1)
    put_pol(c, 930, 1560, 520, f, 5, hair='#7a5a3a', tie='#2c3550', suit='#22263a', expr='stern', look=-1, skin=2)
    if f >= p0:
        sx = lerp(420, 840, .5 + .5 * math.sin(f * .05))
        paste_c(c, lupa(), sx, 1240, .5)
    num(c, 'POLÍCIA ANTITERRORISMO', 640, 430, f, p0, 64, -3)
    num(c, '2 ENDEREÇOS', 640, 590, f, d0, 120, 3)
    if f >= dl0:
        num(c, 'DETIDO EM LONDRES', 640, 770, f, dl0, 76, -2)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    k = kick(f, d0, .6)
    return c, (640, 1080 + k * 6, z, k), 'dusk'


def s4(f):
    """a suspeita: papel oficial, lupa, bandeira estrangeira."""
    c = CEN('escritorio', 'dusk').copy()
    o0 = wt(4, 'obter') - 3; a0 = wt(4, 'ajudar') - 3; e0 = wt(4, 'estrangeiro') - 3
    mesa(c, 640, 1400)
    paste_c(c, documento(), 640, 1180, .85)
    if f >= o0:
        paste_c(c, lupa(), lerp(520, 760, smooth(ramp(f, o0, o0 + 60))), lerp(1080, 1250, smooth(ramp(f, o0, o0 + 60))), .55)
    num(c, 'A SUSPEITA', 640, 420, f, 0, 96, -3)
    num(c, 'OBTER INFORMAÇÕES', 640, 560, f, o0, 70, 2)
    num(c, 'PROTEGIDAS', 640, 650, f, o0 + 4, 70, -2)
    num(c, 'AJUDAR INTELIGÊNCIA', 640, 770, f, a0, 70, -2)
    num(c, 'ESTRANGEIRA', 640, 860, f, a0 + 4, 70, 2)
    if f >= e0:
        paste_c(c, bandeira_ru(), 1030, 1080, back(ramp(f, e0, e0 + 8)) * .38)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140))) * (1 + .0005 * f)
    k = kick(f, a0, .5)
    return c, (640, lerp(1080, 1040, smooth(ramp(f, 0, 140))) + k * 6, z, k), 'dusk'


def s5(f):
    """por que importa: agente do FBI, bandeira dos EUA, aliados."""
    c = CEN('escritorio', 'dusk').copy()
    fb0 = wt(5, 'FBI') - 3; p0 = wt(5, 'preocupacao') - 3; a0 = wt(5, 'aliados') - 3
    mastro(c, 1060, 1520, bandeira_us(), f, 3, .5)
    num(c, 'POR QUE IMPORTA?', 640, 420, f, 0, 88, -3)
    if f >= fb0 - 6:
        put_pol(c, 560, 1560, 560, f, 3, hair='#4a3a2a', tie='#3c3b6e', suit='#1f2433', expr='stern', arms='point' if f >= p0 else 'hang')
    num(c, 'FBI', 640, 590, f, fb0, 140, 3)
    num(c, 'MAIOR PREOCUPAÇÃO', 640, 760, f, p0, 84, -2)
    if f >= a0:
        num(c, 'EUA E ALIADOS', 640, 900, f, a0, 64, 2)
        paste_c(c, bandeira_uk(), 200, 1150, back(ramp(f, a0, a0 + 8)) * .35)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 240))) * (1 + .0004 * f)
    k = kick(f, fb0, .7)
    return c, (640, 1080 + k * 6, z, k - .003 * f), 'dusk'


def s6(f):
    """no mesmo dia: mesa de negociação com as três bandeiras."""
    c = CEN('escritorio', 'dusk').copy()
    m0 = wt(6, 'mesmo') - 3; a0 = wt(6, 'americanos') - 3; r0 = wt(6, 'russos') - 3
    u0 = wt(6, 'ucranianos') - 3; p0 = wt(6, 'paz') - 3
    mesa(c, 640, 1290)
    for x, im, k0 in ((260, bandeira_us(), a0), (640, bandeira_ru(), r0), (1020, bandeira(), u0)):
        if f >= k0:
            paste_c(c, im, x, 1120, back(ramp(f, k0, k0 + 8)) * .62)
    num(c, 'NO MESMO DIA', 640, 480, f, m0, 120, -3)
    num(c, 'EUA', 260, 1300, f, a0, 60, -3)
    num(c, 'RÚSSIA', 640, 1300, f, r0, 54, 2)
    num(c, 'UCRÂNIA', 1020, 1300, f, u0, 54, -2)
    num(c, 'NEGOCIAÇÃO DE PAZ', 640, 680, f, p0, 80, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, p0, .5)
    return c, (640 + lerp(-30, 30, smooth(ramp(f, 0, 160))), 1080 + k * 6, z, k), 'dusk'


def s7(f):
    """fim: silhueta com interrogação, lupa procurando."""
    c = CEN('cidade', 'dusk').copy()
    n0 = wt(7, 'nome') - 3; i0 = wt(7, 'investigacao') - 3
    d = ImageDraw.Draw(c, 'RGBA')
    d.rectangle([0, 0, 1242, 2208], fill=(20, 18, 40, 110))
    sil = sprite('soldier', (('blink', 0), ('expr', 'neutral'), ('tilt', 0)), 680, .6, False).copy()
    a = np.array(sil); a[..., :3] = (40, 36, 60); sil = Image.fromarray(a)
    put(c, sil, 640, 1540 + 4 * math.sin(f * .1))
    paste_c(c, txt('?', 240, 0), 640, 1080, 1 + .05 * math.sin(f * .15))
    num(c, 'NOME NÃO DIVULGADO', 640, 520, f, n0, 62, -3)
    if f >= i0:
        num(c, 'INVESTIGAÇÃO CONTINUA', 640, 660, f, i0, 58, 3)
        paste_c(c, lupa(), lerp(300, 950, .5 + .5 * math.sin((f - i0) * .06)), 860, .5)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 120))) * (1 + .0005 * f)
    return c, (640, lerp(1150, 1030, smooth(ramp(f, 0, 120))), z, .5 * math.sin(f * .05)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'preso') - 3, 140, .5)
    s.ting(s.W(0, 'Russia') - 3, .25)
    s.ting(s.W(1, 'Gloucester') - 3, .25)
    s.thunk(s.W(2, 'Otan') - 3, 140, .4)
    s.thunk(s.W(3, 'dois') - 3, 150, .5)
    s.ting(s.W(4, 'ajudar') - 3, .25)
    s.thunk(s.W(5, 'FBI') - 3, 140, .5)
    s.ting(s.W(6, 'paz') - 3, .3)
    s.ting(s.W(7, 'investigacao') - 3, .25)
