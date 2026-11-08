"""Um Café com o Mundo — O MUNDO EXPLICADO (domingo 08/11/2026, 18h).
Tema: França tem o 4º fim de semana seguido de protestos (sábado 07/11/2026), agora contra o custo de vida e o preço dos combustíveis.
Fontes (conferidas em 08/11/2026):
- Al Jazeera, 07/11/2026 "More than 140,000 rally as new protests against rising costs sweep France": sábado 07/11, 4º fim de
  semana seguido; Ministério do Interior: ~146 mil no país, 46 mil em Paris; sindicatos: 250 mil (75 mil em Paris); protestos
  começaram em setembro por condições ruins e falta de recursos nas escolas de ensino médio e se ampliaram para queixas de
  queda no padrão de vida; custo de vida e combustíveis; ~70 mil agentes de segurança; gás lacrimogêneo em Paris e Lyon;
  eleição presidencial em abril.
- CNBC, 08/11/2026 "France protests draw 146,000 as clashes erupt for fourth straight weekend".
- Wikipedia "2026 French student protests": início em setembro (liceus), falta de professores, prédios deteriorados.
Pessoas genéricas, sem logotipos. Tom neutro, sem opinião."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Cento e quarenta e seis mil pessoas tomaram as ruas da França neste sábado. É o quarto fim de semana seguido.",
    "Tudo começou em setembro, com estudantes do ensino médio protestando contra escolas em mau estado e a falta de professores.",
    "Agora, a revolta cresceu e virou contra o custo de vida e o preço dos combustíveis.",
    "O governo contou quarenta e seis mil só em Paris. Já os sindicatos falam em duzentas e cinquenta mil pessoas no país todo.",
    "Setenta mil policiais foram para as ruas, e houve gás lacrimogêneo em Paris e em Lyon.",
    "Por que isso importa? Os protestos acontecem a poucos meses da eleição para presidente, marcada para abril.",
    "E a pergunta agora é: até onde vai essa onda?",
]
CAPTXT = [
    "146 mil pessoas tomaram as ruas da França|neste sábado. É o quarto|fim de semana seguido.",
    "Tudo começou em setembro, com estudantes|do ensino médio protestando contra escolas|em mau estado e a falta de professores.",
    "Agora, a revolta cresceu e virou|contra o custo de vida|e o preço dos combustíveis.",
    "O governo contou 46 mil só em Paris.|Já os sindicatos falam em 250 mil|pessoas no país todo.",
    "70 mil policiais foram para as ruas,|e houve gás lacrimogêneo|em Paris e em Lyon.",
    "Por que isso importa? Os protestos acontecem|a poucos meses da eleição para presidente,|marcada para abril.",
    "E a pergunta agora é:|até onde vai essa onda?",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'cento', 8), (0, 'Franca', 4), (0, 'quarto', 4), (1, 'setembro', 4), (1, 'escolas', 4), (1, 'professores', 4),
         (2, 'custo', 4), (2, 'combustiveis', 4), (3, 'quarenta', 6), (3, 'duzentas', 6), (4, 'Setenta', 4),
         (4, 'lacrimogeneo', 4), (4, 'Lyon', 4), (5, 'eleicao', 4), (5, 'abril', 4), (6, 'onda', 4)]

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


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('cidade', 'day').copy()
    paste_c(c, torre().resize((330, 726)), 1020, 980, 1)
    n0 = wt(0, 'cento') - 3
    multidao(c, f, 1640, 470, 6, 120, 1120, 0, march=ramp(f, 0, 200), expr='stern', rows=2)
    put_band(c, 200, 1000, 200, f, back(ramp(f, wt(0, 'Franca') - 3, wt(0, 'Franca') + 5)))
    num(c, '146 MIL', 620, 470, f, n0, 210, -5)
    num(c, 'NAS RUAS', 640, 640, f, n0 + 6, 100, 3)
    num(c, '4º FIM DE SEMANA', 640, 790, f, wt(0, 'quarto') - 3, 80, -2)
    z = lerp(1.35, 1.04, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, n0)
    return c, (640 + 25 * math.sin(f * .03), 1080 + k * 8, z, k), 'day'


def s1(f):
    c = CEN('escola', 'day').copy()
    num(c, 'SETEMBRO', 640, 400, f, wt(1, 'setembro') - 3, 120, -3)
    e0 = wt(1, 'escolas') - 3
    if f >= e0: rachadura(c, 300, 560, 1.4, ramp(f, e0, e0 + 10))
    if f >= e0: rachadura(c, 980, 520, 1.1, ramp(f, e0 + 3, e0 + 13))
    num(c, 'ESCOLAS EM MAU ESTADO', 640, 560, f, e0, 64, 3)
    p0 = wt(1, 'professores') - 3
    num(c, 'FALTAM PROFESSORES', 640, 680, f, p0, 70, -3)
    for i, x in enumerate((300, 640, 980)):
        if i == 1 and f >= p0:
            continue
        put_p(c, x, 1620, 500, f, 20 + i, skin=i, hair=HAIRS[i + 1], coat=['#2f6fd6', '#a0463c', '#3a6b5a'][i],
              expr='stern' if f > e0 else 'neutral', arms='point' if (f > e0 and i == 0) else 'hang', look=(1 - i) * .6)
    if f >= p0:
        d = ImageDraw.Draw(c)
        d.ellipse([640 - 120, 1560, 640 + 120, 1610], outline=INK, width=6)
        paste_c(c, txt('?', 160, 0), 640, 1300, back(ramp(f, p0, p0 + 8)))
    t = smooth(ramp(f, 0, 150))
    return c, (640, lerp(980, 1060, t), lerp(1.15, 1.03, t) * (1 + .0005 * f), lerp(-1, 1, t)), 'day'


def s2(f):
    c = CEN('cidade', 'golden').copy()
    c0 = wt(2, 'custo') - 3
    b0 = wt(2, 'combustiveis') - 3
    paste_c(c, carrinho().resize((400, 330)), 330, 1380, back(ramp(f, c0, c0 + 8)) if f >= c0 else .01)
    seta(c, 330, 1060, 220, True, RED, back(ramp(f, c0 + 2, c0 + 10)))
    num(c, 'CUSTO DE VIDA', 420, 640, f, c0, 66, -3)
    paste_c(c, bomba().resize((280, 485)), 930, 1330, back(ramp(f, b0, b0 + 8)) if f >= b0 else .01)
    seta(c, 930, 950, 220, True, RED, back(ramp(f, b0 + 2, b0 + 10)))
    num(c, 'COMBUSTÍVEIS', 860, 760, f, b0, 66, 3)
    num(c, 'A REVOLTA CRESCEU', 640, 450, f, wt(2, 'revolta') - 3, 84, -3)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, b0, .6)
    return c, (640 + 20 * math.sin(f * .04), lerp(1060, 1020, t) + k * 6, lerp(1.0, 1.05, t), k), 'golden'


def s3(f):
    c = CEN('cidade', 'day').copy()
    q0 = wt(3, 'quarenta') - 3
    d0 = wt(3, 'duzentas') - 3
    barra(c, 380, 1380, 230, 260, GRAY, f, q0, '46 MIL')
    num(c, 'GOVERNO:', 380, 1450, f, q0 + 3, 54, 0)
    num(c, 'SÓ EM PARIS', 380, 1520, f, q0 + 5, 46, 0)
    barra(c, 880, 1380, 230, 620, RED, f, d0, '250 MIL')
    num(c, 'SINDICATOS:', 880, 1450, f, d0 + 3, 54, 0)
    num(c, 'PAÍS TODO', 880, 1520, f, d0 + 5, 46, 0)
    num(c, 'QUANTOS FORAM?', 640, 420, f, 2, 96, -3)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, d0, .6)
    return c, (640, lerp(1080, 1020, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0006 * f), k), 'day'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    s0_ = wt(4, 'Setenta') - 3
    g0 = wt(4, 'lacrimogeneo') - 3
    if f >= g0:
        fumaca(c, 300, 1480, f - g0, 1, 1.0)
        fumaca(c, 940, 1460, f - g0, 4, .9)
    for i, x in enumerate((180, 420, 660, 900, 1140)):
        if f < s0_ + i * 2: continue
        put_soldier(c, x, 1620, 520, f, 30 + i, expr='stern', arms='hang', skin=i % 3, mous=False)
        paste_c(c, escudo().resize((130, 248)), x - 70, 1440, 1)
    num(c, '70 MIL POLICIAIS', 640, 430, f, s0_, 96, -3)
    num(c, 'GÁS LACRIMOGÊNEO', 640, 580, f, g0, 76, 3)
    num(c, 'PARIS', 420, 720, f, wt(4, 'Paris') - 3, 80, -3)
    num(c, 'LYON', 860, 720, f, wt(4, 'Lyon') - 3, 80, 3)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, s0_, .7)
    return c, (640, lerp(1040, 1080, t) + k * 6, lerp(1.12, 1.0, t) * (1 + .0006 * f), lerp(-1.5, 1.5, t)), 'dusk'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    e0 = wt(5, 'eleicao') - 3
    a0 = wt(5, 'abril') - 3
    paste_c(c, urna().resize((420, 437)), 420, 1250, back(ramp(f, e0, e0 + 8)) if f >= e0 else .01)
    if f >= e0:
        y = lerp(720, 1080, ramp(f, e0 + 4, e0 + 18))
        if y < 1060: paste_c(c, cedula(), 420, y, 1)
    num(c, 'POR QUE IMPORTA?', 640, 420, f, 0, 96, -3)
    num(c, 'ELEIÇÃO PARA PRESIDENTE', 640, 560, f, e0, 62, 3)
    num(c, 'ABRIL', 900, 800, f, a0, 150, 5)
    put_band(c, 920, 1060, 200, f, back(ramp(f, a0, a0 + 8)) if f >= a0 else 0)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, a0, .6)
    return c, (640 + 15 * math.sin(f * .04), lerp(1000, 1060, t) + k * 6, lerp(1.0, 1.12, t) * (1 + .0008 * f), lerp(0, 1.5, t)), 'dusk'


def s6(f):
    c = CEN('cidade', 'dusk').copy()
    paste_c(c, torre().resize((330, 726)), 220, 980, 1)
    multidao(c, f, 1640, 440, 5, 220, 1100, 5, march=ramp(f, 0, 120), expr='neutral', rows=2)
    o0 = wt(6, 'onda') - 3
    num(c, 'ATÉ ONDE VAI?', 640, 520, f, o0 - 6, 110, -4)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) + .0004 * f
    return c, (640 - 20 * math.sin(f * .03), 1060, z, lerp(0, -1.5, smooth(ramp(f, 0, 90)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'cento') - 3, 140, .9)
    s.ting(s.W(0, 'quarto') - 3, .25)
    s.ting(s.W(1, 'setembro') - 3, .25)
    s.thunk(s.W(1, 'escolas') - 3, 200, .5)
    s.whoosh(s.W(2, 'custo') - 3, .3, .5)
    s.thunk(s.W(2, 'combustiveis') - 3, 160, .6)
    s.thunk(s.W(3, 'quarenta') - 3, 200, .6)
    s.thunk(s.W(3, 'duzentas') - 3, 140, .8)
    s.thunk(s.W(4, 'Setenta') - 3, 120, .6)
    s.ting(s.W(5, 'abril') - 3, .3)
