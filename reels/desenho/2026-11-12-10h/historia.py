"""Um Café com o Mundo — O MUNDO EXPLICADO (quinta 12/11/2026, 10h; TikTok curto).
Tema: Espanha tem a 1ª greve geral em 14 anos (quarta 11/11/2026), por moradia, salários e preços.
Fontes (conferidas em 12/11/2026):
- Al Jazeera, 11/11/2026 "Workers across Spain stage first general strike in 14 years": convocada por UGT e CCOO, 24 horas
  desde a meia-noite de quarta; sindicatos falam em 90% de adesão em montadoras e portos, patronal CEOE diz adesão baixa;
  aluguel médio quase dobrou em 10 anos; apê de 50 m2 em Madri custa em média 1.170 euros/mês em outubro (Idealista);
  Conselho da Juventude: jovem precisaria de 98,7% do salário para alugar sozinho; eleição antecipada em 29/11.
- Al Jazeera, 11/11/2026 "'It's just too expensive'": Banco da Espanha diz que são precisas 750 mil casas novas
  (podendo chegar a 1 milhão); Espanha construiu 92 mil em 2025; eleição em 29/11.
- CNN, 11/11/2026 "Millions of Spaniards stage first general strike in 14 years as anger rages over housing".
- Euronews / Open Chronicle brief 12/11/2026: protestos em Madri, Barcelona e outras cidades.
Pessoas genéricas, sem logotipos. Tom neutro, sem opinião."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Milhões de espanhóis cruzaram os braços nesta quarta: a primeira greve geral da Espanha em catorze anos.",
    "O motivo é a moradia. Em dez anos, o aluguel quase dobrou.",
    "Em Madri, um apartamento de cinquenta metros quadrados custa em média mil cento e setenta euros por mês.",
    "E um jovem precisaria de quase noventa e nove por cento do salário pra morar sozinho.",
    "Por que isso importa? Segundo o Banco da Espanha, faltam setecentas e cinquenta mil casas no país.",
    "E a eleição antecipada já tem data: vinte e nove de novembro.",
]
CAPTXT = [
    "Milhões de espanhóis cruzaram os braços nesta quarta:|a primeira greve geral da Espanha em 14 anos.",
    "O motivo é a moradia.|Em 10 anos, o aluguel quase dobrou.",
    "Em Madri, um apartamento de 50 m²|custa em média 1.170 euros por mês.",
    "E um jovem precisaria de quase 99%|do salário pra morar sozinho.",
    "Por que isso importa? Segundo o Banco da Espanha,|faltam 750 mil casas no país.",
    "E a eleição antecipada já tem data:|29 de novembro.",
]
FALA_TIKTOK = "Aqui no Brasil o aluguel também pesa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Milhoes', 4), (0, 'greve', 4), (0, 'catorze', 4), (1, 'moradia', 4), (1, 'dobrou', 4), (2, 'Madri', 4),
         (2, 'cinquenta', 4), (2, 'mil', 6), (3, 'noventa', 6), (3, 'sozinho', 4), (4, 'setecentas', 6), (5, 'vinte', 6)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); BLUE = hexc('#2f5fd0'); WHITE = (255, 255, 255)
GOLD = hexc('#f0c541'); GREEN = hexc('#3aa66a'); GRAY = hexc('#9aa4b4'); STEEL = hexc('#5b6573'); STEEL_D = hexc('#3e4652')
SIGNS = ['#f0c541', '#ffffff', '#7fd0c4', '#f39a6b', '#c9b6ff', '#9fe07a']


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def pessoa(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', coat='#2c3550'):
    """pessoa genérica de casaco (feijão). 600x1000, pés y~975."""
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(coat); P.COAT_D = mul(hexc(coat), .7)
    try:
        img = P.scientist(expr=expr, arms=arms, blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
    finally:
        P.COAT, P.COAT_D = oc, od
    return img


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def placa(c, x, feet, h, col, mark, bob=0.0):
    """cartaz num cabo, atrás da pessoa"""
    d = ImageDraw.Draw(c)
    top = feet - h * 1.28 + bob
    w = h * .42; hh = h * .26
    d.line([(x + 6, top + hh), (x + 6, feet - h * .45)], fill=INK, width=max(6, int(h * .022)))
    d.line([(x, top + hh), (x, feet - h * .45)], fill=hexc('#a8794e'), width=max(4, int(h * .014)))
    d.rectangle([x - w / 2 + 8, top + 8, x + w / 2 + 8, top + hh + 8], fill=INK)
    d.rectangle([x - w / 2, top, x + w / 2, top + hh], fill=hexc(col), outline=INK, width=6)
    if mark: paste_c(c, txt(mark, int(hh * .62), 0), x, top + hh / 2, 1)


COATS = ['#2c3550', '#6b4a6b', '#3a6b5a', '#8a5a3a', '#3a3a44', '#2f6fd6', '#a0463c', '#4a4f63']
HAIRS = ['#3a2a20', '#6b5a4a', '#2a221e', '#8a5a3a', '#c9a060', '#1e1a18']
MARKS = ['€', '!', '€€', '!!', '?', '€']


def multidao(c, f, feet, h, n, x0, x1, seed=0, march=0.0, expr='stern', sign=True, rows=2):
    """multidão de pessoas genéricas com cartazes. linhas de trás menores."""
    for r in range(rows - 1, -1, -1):
        hh = h * (1 - .18 * r); ff = feet - 120 * r
        for i in range(n):
            k = i + r * 7 + seed
            x = lerp(x0, x1, (i + .5 * (r % 2)) / max(1, n - 1)) + march * 40
            bob = 10 * math.sin(f * .25 + k * 1.7) * (1 if march else .3)
            if sign and (k % 2 == 0):
                placa(c, x + 30 * ((k % 3) - 1), ff + bob, hh, SIGNS[k % len(SIGNS)], MARKS[k % len(MARKS)], 0)
            put_p(c, x, ff + bob, hh, f, k + 3, skin=k % 4, hair=HAIRS[k % len(HAIRS)], coat=COATS[k % len(COATS)],
                  expr=expr if k % 3 else 'neutral', arms='up' if (sign and k % 2 == 0) else 'hang', look=(k % 3 - 1) * .5)


@lru_cache(maxsize=2)
def torre():
    """torre de ferro (monumento) genérica. 500x1100"""
    p = Pen(500, 1100)
    col = hexc('#8a6a4a'); cd = hexc('#5e462e')
    p.shape([(30, 1090), (130, 1090), (215, 560), (285, 560), (370, 1090), (470, 1090), (330, 520), (300, 160), (250, 20), (200, 160), (170, 520)], col, cd, 6, 14)
    p.poly([(150, 1090), (350, 1090), (300, 860), (200, 860)], hexc('#b7d4ea'))
    p.shape(ell_pts(250, 905, 95, 70, 30), hexc('#b7d4ea'), hexc('#b7d4ea'), 0, 0)
    for y, w in ((560, 150), (820, 230), (300, 70)):
        p.shape([(250 - w, y - 18), (250 + w, y - 18), (250 + w, y + 18), (250 - w, y + 18)], col, cd, 5, 3)
    for y in range(600, 1060, 60):
        k = (y - 560) / 530
        p.stroke([(215 - 85 * k, y), (285 + 85 * k, y + 50)], 4, cd)
        p.stroke([(285 + 85 * k, y), (215 - 85 * k, y + 50)], 4, cd)
    p.stroke([(250, 20), (250, -10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_fr():
    """bandeira da França (país). 600x400"""
    p = Pen(600, 400)
    for i, cc in enumerate(('#2f4fb5', '#ffffff', '#e0393e')):
        p.poly([(10 + i * 193, 10), (10 + (i + 1) * 193, 10), (10 + (i + 1) * 193, 390), (10 + i * 193, 390)], hexc(cc))
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


def put_band(c, x, y, w, f, s=1.0):
    if s <= .02: return
    im = bandeira_fr()
    ww = int(w * s); hh = int(w * .66 * s)
    im = im.resize((ww, hh)).rotate(3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    d = ImageDraw.Draw(c)
    d.line([(x - ww / 2 - 4, y - hh / 2), (x - ww / 2 - 4, y + hh * 1.6)], fill=INK, width=10)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=2)
def bomba():
    p = Pen(300, 520)
    p.shape([(40, 60), (220, 60), (220, 500), (40, 500)], hexc('#3aa66a'), hexc('#287a4c'), 6, 12)
    p.shape([(70, 100), (190, 100), (190, 220), (70, 220)], WHITE, hexc('#c9c9d2'), 4, 4)
    p.poly([(90, 130), (170, 130), (170, 160), (90, 160)], hexc('#2a2a33'))
    p.shape([(20, 490), (240, 490), (240, 515), (20, 515)], hexc('#6b6b70'), hexc('#4a4a50'), 4, 3)
    p.stroke([(220, 260), (270, 260), (280, 420), (250, 440)], 10, hexc('#2a2a33'))
    p.shape([(240, 230), (275, 230), (275, 290), (240, 290)], hexc('#2a2a33'), hexc('#1a1a20'), 3, 3)
    return fin(p)


@lru_cache(maxsize=2)
def carrinho():
    p = Pen(460, 380)
    p.stroke([(10, 40), (70, 40), (110, 260), (400, 260)], 12, INK)
    p.shape([(80, 80), (440, 80), (410, 230), (105, 230)], hexc('#d9dde3'), hexc('#a9b2bd'), 6, 8)
    for x in (150, 230, 310, 380): p.stroke([(x, 85), (x - 8, 225)], 4, hexc('#a9b2bd'))
    p.shape(ell_pts(150, 330, 32, 32, 20), hexc('#2a2a33'), INK, 4, 2)
    p.shape(ell_pts(370, 330, 32, 32, 20), hexc('#2a2a33'), INK, 4, 2)
    return fin(p)


@lru_cache(maxsize=2)
def urna():
    p = Pen(500, 520)
    p.shape([(60, 160), (440, 160), (420, 500), (80, 500)], hexc('#eef2f7'), hexc('#b9c3d1'), 6, 16)
    p.shape([(40, 120), (460, 120), (460, 170), (40, 170)], hexc('#dfe6ef'), hexc('#a9b4c4'), 5, 6)
    p.poly([(180, 136), (320, 136), (320, 152), (180, 152)], INK)
    p.shape(ell_pts(250, 330, 70, 70, 40), BLUE, mul(BLUE, .7), 5, 6)
    p.stroke([(215, 330), (242, 358), (290, 300)], 12, (255, 255, 255))
    return fin(p)


@lru_cache(maxsize=2)
def cedula():
    p = Pen(160, 210)
    p.shape([(10, 10), (150, 10), (150, 200), (10, 200)], (255, 255, 255), hexc('#cfd6df'), 4, 4)
    for y in (50, 90, 130):
        p.poly([(28, y - 10), (48, y - 10), (48, y + 10), (28, y + 10)], (255, 255, 255), 3)
        p.stroke([(60, y), (130, y)], 4, hexc('#9aa4b4'))
    return fin(p)


@lru_cache(maxsize=2)
def escudo():
    """escudo de policial genérico. 220x420"""
    p = Pen(220, 420)
    p.shape([(20, 20), (200, 20), (200, 330), (110, 405), (20, 330)], hexc('#cfe3f2'), hexc('#9fb8cc'), 6, 10)
    p.stroke([(40, 120), (180, 120)], 8, hexc('#2c3550'))
    return fin(p)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def fumaca(c, x, y, f, seed=0, s=1.0, col=(200, 200, 205)):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(7):
        t = ((f * .6 + i * 15 + seed * 7) % 100) / 100
        r = (40 + 80 * t) * s
        xx = x + 60 * math.sin(t * 5 + seed + i) * s; yy = y - 300 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=col + (a,))


def seta(c, x, y, size, up=True, col=None, s=1.0):
    if s <= .02: return
    col = col or (RED if up else GREEN)
    d = ImageDraw.Draw(c)
    k = 1 if up else -1
    w = size * .32 * s; hh = size * s
    pts = [(x - w, y + k * hh * .1), (x - w, y - k * hh * .25), (x - w * 2, y - k * hh * .25), (x, y - k * hh * .8), (x + w * 2, y - k * hh * .25), (x + w, y - k * hh * .25), (x + w, y + k * hh * .1)]
    d.polygon([(px + 6, py + 6) for px, py in pts], fill=INK)
    d.polygon(pts, fill=col, outline=INK, width=6)


def barra(c, x, base, w, h, col, f, f0, top_lab=None):
    if f < f0: return
    d = ImageDraw.Draw(c)
    hh = h * easeOut(ramp(f, f0, f0 + 14))
    d.rectangle([x - w / 2 + 8, base - hh + 8, x + w / 2 + 8, base + 8], fill=INK)
    d.rectangle([x - w / 2, base - hh, x + w / 2, base], fill=col, outline=INK, width=6)
    if top_lab: paste_c(c, txt(top_lab, 90, -3), x, base - hh - 70, back(ramp(f, f0 + 6, f0 + 14)))


def rachadura(c, x, y, s=1.0, t=1.0):
    d = ImageDraw.Draw(c)
    pts = [(x, y), (x + 30 * s, y + 60 * s), (x - 10 * s, y + 120 * s), (x + 40 * s, y + 190 * s), (x + 10 * s, y + 260 * s)]
    n = max(2, int(len(pts) * t))
    d.line(pts[:n], fill=INK, width=8)



YEL = hexc('#f2c230')


@lru_cache(maxsize=2)
def bandeira_es():
    """bandeira da Espanha simplificada (vermelho, amarelo, vermelho). 600x400"""
    p = Pen(600, 400)
    p.poly([(10, 10), (590, 10), (590, 105), (10, 105)], hexc('#c8302a'))
    p.poly([(10, 105), (590, 105), (590, 295), (10, 295)], YEL)
    p.poly([(10, 295), (590, 295), (590, 390), (10, 390)], hexc('#c8302a'))
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


def put_band(c, x, y, w, f, s=1.0):
    if s <= .02: return
    im = bandeira_es()
    ww = int(w * s); hh = int(w * .66 * s)
    im = im.resize((ww, hh)).rotate(3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    d = ImageDraw.Draw(c)
    d.line([(x - ww / 2 - 4, y - hh / 2), (x - ww / 2 - 4, y + hh * 1.6)], fill=INK, width=10)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=4)
def casa(col='#f39a6b'):
    """casinha simples. 400x400"""
    p = Pen(400, 400)
    p.shape([(60, 180), (340, 180), (340, 390), (60, 390)], hexc(col), mul(hexc(col), .75), 6, 12)
    p.shape([(30, 190), (200, 40), (370, 190)], hexc('#a0463c'), hexc('#7a3029'), 6, 8)
    p.shape([(170, 270), (230, 270), (230, 390), (170, 390)], hexc('#6b4a2f'), hexc('#4a321f'), 5, 4)
    for x in (90, 260):
        p.shape([(x, 220), (x + 50, 220), (x + 50, 270), (x, 270)], hexc('#cfe8f7'), hexc('#a9c8de'), 4, 3)
    return fin(p)


@lru_cache(maxsize=2)
def etiqueta():
    """etiqueta de preço. 520x300"""
    p = Pen(520, 300)
    p.shape([(70, 20), (500, 20), (500, 280), (70, 280), (10, 150)], hexc('#fff4c9'), hexc('#e6d38f'), 6, 10)
    p.dot(70, 150, 18, hexc('#a0463c'), 4)
    return fin(p)


@lru_cache(maxsize=2)
def carteira():
    p = Pen(360, 260)
    p.shape([(20, 40), (340, 40), (340, 240), (20, 240)], hexc('#6b4a2f'), hexc('#4a321f'), 6, 10)
    p.shape([(200, 100), (350, 100), (350, 180), (200, 180)], hexc('#8a5a3a'), hexc('#6b4a2f'), 5, 4)
    p.dot(240, 140, 12, YEL, 4)
    return fin(p)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('cidade', 'day').copy()
    n0 = wt(0, 'Milhoes') - 3
    multidao(c, f, 1640, 470, 6, 120, 1120, 0, march=ramp(f, 0, 200), expr='stern', rows=2)
    put_band(c, 210, 1000, 210, f, back(ramp(f, wt(0, 'espanhois') - 3, wt(0, 'espanhois') + 5)))
    num(c, 'MILHÕES', 640, 560, f, n0, 160, -5)
    num(c, 'DE BRAÇOS CRUZADOS', 640, 700, f, wt(0, 'bracos') - 3, 76, 3)
    g0 = wt(0, 'greve') - 3
    num(c, '1ª GREVE GERAL', 640, 840, f, g0, 92, -3)
    num(c, 'EM 14 ANOS', 640, 970, f, wt(0, 'catorze') - 3, 100, 3)
    z = lerp(1.35, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, n0)
    return c, (640 + 25 * math.sin(f * .03), 1080 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('cidade', 'golden').copy()
    m0 = wt(1, 'moradia') - 3
    paste_c(c, casa().resize((240, 240)), 640, 690, back(ramp(f, m0, m0 + 8)) if f >= m0 else .01)
    num(c, 'MORADIA', 640, 470, f, m0, 120, -3)
    a0 = wt(1, 'aluguel') - 3
    barra(c, 400, 1420, 220, 170, GRAY, f, a0, '1x')
    num(c, 'HÁ 10 ANOS', 400, 1490, f, a0 + 3, 50, 0)
    d0 = wt(1, 'dobrou') - 3
    barra(c, 860, 1420, 220, 330, RED, f, d0, '2x')
    num(c, 'HOJE', 860, 1490, f, d0 + 3, 56, 0)
    num(c, 'QUASE O DOBRO', 640, 880, f, d0 + 4, 80, -3)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, d0, .6)
    return c, (640 + 15 * math.sin(f * .04), lerp(1000, 1060, t) + k * 6, lerp(1.12, 1.02, t), k), 'golden'


def s2(f):
    c = CEN('sala', 'day').copy()
    m0 = wt(2, 'Madri') - 3
    num(c, 'MADRI', 640, 400, f, m0, 120, -3)
    q0 = wt(2, 'cinquenta') - 3
    num(c, '50 m²', 330, 600, f, q0, 120, 4)
    put_p(c, 820, 1640, 640, f, 7, skin=2, hair=HAIRS[2], coat='#3a6b5a',
          expr='shock' if f >= wt(2, 'mil') - 3 else 'neutral', arms='cheek' if f >= wt(2, 'mil') - 3 else 'hang', look=-.6)
    e0 = wt(2, 'mil') - 4
    if f >= e0:
        paste_c(c, etiqueta().resize((470, 271)), 400, 900, back(ramp(f, e0, e0 + 8)))
        num(c, '€ 1.170', 420, 870, f, e0 + 2, 100, 0)
        num(c, 'POR MÊS', 420, 950, f, wt(2, 'mes') - 3, 50, 0)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, e0, .7)
    return c, (640 + 15 * math.sin(f * .05), lerp(1080, 1040, t) + k * 6, lerp(1.0, 1.1, t) * (1 + .0008 * f), lerp(0, 1.5, t) + k), 'day'


def s3(f):
    c = CEN('quarto', 'dusk').copy()
    n0 = wt(3, 'noventa') - 3
    put_p(c, 380, 1640, 620, f, 11, skin=1, hair=HAIRS[4], coat='#2f6fd6',
          expr='pained' if f >= n0 else 'neutral', arms='cheek' if f >= n0 else 'hang', look=.6)
    paste_c(c, carteira().resize((260, 188)), 860, 1300, 1)
    d = ImageDraw.Draw(c)
    x0, x1, y0 = 680, 1100, 1000
    d.rectangle([x0 + 8, y0 + 8, x1 + 8, y0 + 90 + 8], fill=INK)
    d.rectangle([x0, y0, x1, y0 + 90], fill=(255, 255, 255), outline=INK, width=6)
    fill = .987 * easeOut(ramp(f, n0, n0 + 24))
    if fill > 0: d.rectangle([x0 + 6, y0 + 6, x0 + 6 + (x1 - x0 - 12) * fill, y0 + 84], fill=RED)
    num(c, 'SALÁRIO', 890, 930, f, 2, 60, 0)
    num(c, '98,7%', 890, 720, f, n0, 170, -4)
    num(c, 'PRA ALUGAR SOZINHO', 640, 480, f, wt(3, 'sozinho') - 3, 70, 3)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, n0, .7)
    return c, (640 + 15 * math.sin(f * .05), lerp(1040, 1000, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0006 * f), lerp(-1, 1.5, t)), 'dusk'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    num(c, 'POR QUE IMPORTA?', 640, 420, f, 0, 96, -3)
    s0_ = wt(4, 'setecentas') - 3
    xs = [(200, '#f39a6b'), (450, '#7fd0c4'), (700, '#f0c541'), (950, '#c9b6ff')]
    for i, (x, col) in enumerate(xs):
        if i < 2:
            paste_c(c, casa(col).resize((260, 260)), x, 1250, 1)
        else:
            d = ImageDraw.Draw(c)
            a = back(ramp(f, s0_ + (i - 2) * 3, s0_ + 8 + (i - 2) * 3)) if f >= s0_ else 0
            if a > .05:
                r = 120 * a
                for k in range(0, 12):
                    ang = k / 12 * 2 * math.pi
                    d.arc([x - r, 1250 - r, x + r, 1250 + r], math.degrees(ang), math.degrees(ang) + 18, fill=INK, width=8)
                paste_c(c, txt('?', int(140 * a), 0), x, 1250, 1)
    num(c, 'FALTAM', 640, 720, f, s0_ - 4, 90, 3)
    num(c, '750 MIL CASAS', 640, 870, f, s0_, 105, -4)
    num(c, 'BANCO DA ESPANHA', 640, 580, f, wt(4, 'Banco') - 3, 56, 0)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, s0_, .7)
    return c, (640, lerp(1060, 1020, t) + k * 6, lerp(1.0, 1.1, t) * (1 + .0006 * f), lerp(1, -1, t)), 'dusk'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    e0 = wt(5, 'eleicao') - 3
    v0 = wt(5, 'vinte') - 3
    paste_c(c, urna().resize((420, 437)), 420, 1250, back(ramp(f, e0, e0 + 8)) if f >= e0 else .01)
    if f >= e0:
        y = lerp(720, 1080, ramp(f, e0 + 4, e0 + 18))
        if y < 1060: paste_c(c, cedula(), 420, y, 1)
    num(c, 'ELEIÇÃO ANTECIPADA', 640, 520, f, e0, 70, -3)
    num(c, '29 DE NOVEMBRO', 640, 680, f, v0, 86, 3)
    put_band(c, 920, 1060, 220, f, back(ramp(f, v0, v0 + 8)) if f >= v0 else 0)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, v0, .6)
    return c, (640 + 15 * math.sin(f * .04), lerp(1000, 1040, t) + k * 6, lerp(1.0, 1.05, t) * (1 + .0004 * f), lerp(0, 1.5, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    s.thunk(s.W(0, 'Milhoes') - 3, 140, .9)
    s.ting(s.W(0, 'catorze') - 3, .25)
    s.thunk(s.W(1, 'moradia') - 3, 200, .5)
    s.thunk(s.W(1, 'dobrou') - 3, 140, .7)
    s.ting(s.W(2, 'Madri') - 3, .25)
    s.thunk(s.W(2, 'mil') - 4, 160, .7)
    s.whoosh(s.W(3, 'noventa') - 3, .3, .5)
    s.thunk(s.W(4, 'setecentas') - 3, 140, .8)
    s.ting(s.W(5, 'vinte') - 3, .3)
