"""Um Café com o Mundo — O MUNDO EXPLICADO (segunda 09/11/2026, 09h).
Tema: começa a COP31, conferência do clima da ONU, em Antália (Turquia), sem delegação oficial dos EUA.
Fontes (conferidas em 09/11/2026):
- AFP via Asharq Al-Awsat, 09/11/2026 "COP31 Opens as Climate and Geopolitical Pressures Mount": abre segunda 09/11, duas
  semanas, negociadores de quase 200 países, mais de 100 mil pessoas esperadas, Antalya Expo Center; Turquia preside e a
  Austrália conduz as negociações; Trump tirou os EUA do Acordo de Paris e não mandou funcionários; ONU avisou em setembro
  que a temperatura caminha para passar de 1,5 °C; meta turca: eletricidade de ~20% para 35% da demanda de energia até 2035;
  países em desenvolvimento cobram promessas de financiamento; alto funcionário da UE: "no political will" para novas
  promessas; COP30 (Brasil) terminou com acordo sem menção explícita a combustíveis fósseis.
- ABC News, 09/11/2026 "What to know about COP31": sem delegação oficial do governo Trump pelo 2º ano; meta "just over 20%"
  em 2024 para 35% até 2035.
- AP via 10 Things Global News, 09/11/2026: COP31 de 9 a 20 de novembro; EUA, 2º maior emissor do mundo, ausentes.
Pessoas genéricas, sem logotipos. Tom neutro, sem opinião."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Quase duzentos países discutem o clima a partir de hoje, e os Estados Unidos, segundo maior poluidor, não mandaram delegação oficial.",
    "É a COP trinta e um, da ONU, em Antália, na Turquia, com mais de cem mil pessoas esperadas.",
    "A ONU avisa: o planeta caminha para passar de um grau e meio de aquecimento, o limite do Acordo de Paris.",
    "A Turquia quer que a eletricidade passe de vinte para trinta e cinco por cento da energia mundial até dois mil e trinta e cinco.",
    "Mas a briga é por dinheiro: países pobres cobram a ajuda prometida, e a Europa diz não ter vontade política de dar mais.",
    "Por que importa? A COP passada, no Brasil, terminou sem citar petróleo nem carvão no acordo.",
    "Até vinte de novembro, o mundo vai ver se a Turquia vai mais longe.",
]
CAPTXT = [
    "Quase 200 países discutem o clima a partir de hoje,|e os Estados Unidos, segundo maior poluidor,|não mandaram delegação oficial.",
    "É a COP31, da ONU, em Antália, na Turquia,|com mais de 100 mil pessoas esperadas.",
    "A ONU avisa: o planeta caminha para passar|de 1,5 grau de aquecimento,|o limite do Acordo de Paris.",
    "A Turquia quer que a eletricidade passe|de 20% para 35% da energia mundial|até 2035.",
    "Mas a briga é por dinheiro: países pobres|cobram a ajuda prometida, e a Europa diz|não ter vontade política de dar mais.",
    "Por que importa? A COP passada,|no Brasil, terminou sem citar|petróleo nem carvão no acordo.",
    "Até 20 de novembro, o mundo vai ver|se a Turquia vai mais longe.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'duzentos', 6), (0, 'Estados', 4), (0, 'delegacao', 6), (1, 'COP', 4), (1, 'Antalia', 4), (1, 'cem', 6),
         (2, 'grau', 6), (2, 'limite', 4), (3, 'vinte', 6), (3, 'trinta', 6), (3, 'dois', 6), (4, 'dinheiro', 4),
         (4, 'prometida', 4), (4, 'vontade', 6), (5, 'Brasil', 4), (5, 'petroleo', 4), (5, 'carvao', 4), (6, 'novembro', 4), (6, 'longe', 4)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); BLUE = hexc('#2f5fd0'); WHITE = (255, 255, 255)
GOLD = hexc('#f0c541'); GOLD_D = hexc('#c99a22'); GREEN = hexc('#3aa66a'); GRAY = hexc('#9aa4b4')
YEL = hexc('#f6d33c'); BLUEB = hexc('#2a4fa8'); TR = hexc('#e30a17')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def pessoa(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', coat='#2c3550'):
    """pessoa genérica de terno/casaco (feijão). 600x1000, pés y~975."""
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(coat); P.COAT_D = mul(hexc(coat), .7)
    try:
        img = P.scientist(expr=expr, arms=arms, blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
    finally:
        P.COAT, P.COAT_D = oc, od
    return img


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


COATS = ['#2c3550', '#6b4a6b', '#3a6b5a', '#8a5a3a', '#3a3a44', '#2f6fd6', '#a0463c', '#4a4f63']
HAIRS = ['#3a2a20', '#6b5a4a', '#2a221e', '#8a5a3a', '#c9a060', '#1e1a18']
FLAGC = [('#2f6fd6', '#ffffff'), ('#3aa66a', '#f6d33c'), ('#d8443c', '#ffffff'), ('#f39a6b', '#3aa66a'),
         ('#ffffff', '#2f6fd6'), ('#1e1a18', '#d8443c'), ('#7fd0c4', '#ffffff'), ('#f6d33c', '#2f6fd6')]


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def barra(c, x, base, w, h, col, f, f0, top_lab=None):
    if f < f0: return
    d = ImageDraw.Draw(c)
    hh = h * easeOut(ramp(f, f0, f0 + 14))
    d.rectangle([x - w / 2 + 8, base - hh + 8, x + w / 2 + 8, base + 8], fill=INK)
    d.rectangle([x - w / 2, base - hh, x + w / 2, base], fill=col, outline=INK, width=6)
    if top_lab: paste_c(c, txt(top_lab, 90, -3), x, base - hh - 70, back(ramp(f, f0 + 6, f0 + 14)))


# ------------------------------------------------------------------ objetos
@lru_cache(maxsize=2)
def bandeira_tr():
    """bandeira da Turquia (país): vermelha com lua crescente e estrela brancas. 600x400"""
    p = Pen(600, 400)
    p.poly([(10, 10), (590, 10), (590, 390), (10, 390)], TR)
    p.poly(ell_pts(225, 200, 100, 100, 60), WHITE)
    p.poly(ell_pts(250, 200, 80, 80, 60), TR)
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = 52 if i % 2 == 0 else 21
        pts.append((365 + r * math.cos(a), 200 + r * math.sin(a)))
    p.poly(pts, WHITE)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_br():
    p = Pen(600, 420)
    p.poly([(10, 10), (590, 10), (590, 410), (10, 410)], GREEN)
    p.poly([(300, 45), (555, 210), (300, 375), (45, 210)], YEL)
    p.dot(300, 210, 105, BLUEB)
    p.stroke(curve((200, 190), (300, 170), (400, 230), 10), 10, WHITE)
    p.stroke([(10, 10), (590, 10), (590, 410), (10, 410), (10, 10)], 6)
    return fin(p)


def put_band(c, im, x, y, w, f, s=1.0):
    if s <= .02: return
    ww = int(w * s); hh = int(w * .68 * s)
    im = im.resize((ww, hh)).rotate(3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    d = ImageDraw.Draw(c)
    d.line([(x - ww / 2 - 4, y - hh / 2), (x - ww / 2 - 4, y + hh * 1.7)], fill=INK, width=10)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=8)
def bandeirinha(k):
    """bandeirinha genérica de mesa (2 faixas). 200x260"""
    a, b = FLAGC[k % len(FLAGC)]
    p = Pen(200, 260)
    p.stroke([(30, 20), (30, 250)], 8, hexc('#6b6b70'))
    p.poly([(34, 20), (190, 20), (190, 70), (34, 70)], hexc(a), 4)
    p.poly([(34, 70), (190, 70), (190, 120), (34, 120)], hexc(b), 4)
    p.stroke([(34, 20), (190, 20), (190, 120), (34, 120)], 5)
    p.shape([(5, 240), (60, 240), (60, 255), (5, 255)], hexc('#6b6b70'), None, 4, 0)
    return fin(p)


@lru_cache(maxsize=2)
def mesa():
    """mesa longa de conferência. 1300x260"""
    p = Pen(1300, 260)
    p.shape([(0, 20), (1300, 20), (1300, 90), (0, 90)], hexc('#8a5a3a'), hexc('#5e3c24'), 6, 10)
    p.shape([(20, 90), (1280, 90), (1280, 250), (20, 250)], hexc('#2c4a7a'), hexc('#1e3456'), 6, 12)
    return fin(p)


@lru_cache(maxsize=2)
def cadeira():
    """cadeira vazia. 300x520"""
    p = Pen(300, 520)
    p.shape([(50, 20), (250, 20), (250, 300), (50, 300)], hexc('#3a3a44'), hexc('#24242c'), 6, 10)
    p.shape([(30, 290), (270, 290), (270, 340), (30, 340)], hexc('#4a4a55'), hexc('#2e2e36'), 6, 6)
    p.stroke([(60, 340), (50, 510)], 12); p.stroke([(240, 340), (250, 510)], 12)
    return fin(p)


@lru_cache(maxsize=2)
def placa_eua():
    p = Pen(330, 130)
    p.shape([(10, 20), (320, 20), (300, 120), (30, 120)], WHITE, hexc('#c9c9d2'), 5, 5)
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


@lru_cache(maxsize=4)
def sol(angry=0, blink=0):
    """Sol com cara. 700x700."""
    p = Pen(700, 700)
    for i in range(14):
        a = i * 2 * math.pi / 14
        r1 = 230 + (60 if angry else 30) * (i % 2)
        p.poly([(350 + 190 * math.cos(a - .14), 350 + 190 * math.sin(a - .14)), (350 + (r1 + 70) * math.cos(a), 350 + (r1 + 70) * math.sin(a)),
                (350 + 190 * math.cos(a + .14), 350 + 190 * math.sin(a + .14))], hexc('#f6a733'), 4)
    p.shape(ell_pts(350, 350, 210, 210, 60), hexc('#f7d046'), hexc('#e0a92a'), 7, 28)
    for s in (-1, 1):
        ex, ey = 350 + s * 75, 320
        p.dot(ex, ey, 34, WHITE, 5)
        if blink < .6: p.dot(ex - s * 4, ey + 6, 15, INK)
        if angry: p.stroke([(ex - 46, ey - 40 + s * 18), (ex + 46, ey - 40 - s * 18)], 9)
    if angry: p.arc(350, 450, 60, 22, 200, 340, 8)
    else: p.arc(350, 410, 60, 30, 20, 160, 8)
    return fin(p)


def raio(seed=0):
    p = Pen(300, 700)
    r = random.Random(seed); pts = [(150, 0)]
    for i in range(1, 8): pts.append((150 + (r.random() - .5) * 160, i * 95))
    p.line(pts, hexc('#fff6a8'), 16, 4)
    return fin(p)


@lru_cache(maxsize=2)
def moeda():
    p = Pen(160, 160)
    p.shape(ell_pts(80, 80, 64, 64, 32), GOLD, GOLD_D, 5, 6)
    p.arc(80, 80, 42, 42, 0, 360, 4, GOLD_D)
    p.stroke([(62, 70), (98, 70)], 5, GOLD_D); p.stroke([(80, 52), (80, 108)], 5, GOLD_D)
    return fin(p)


@lru_cache(maxsize=2)
def barril():
    """barril de petróleo. 300x420"""
    p = Pen(300, 420)
    p.shape([(30, 30), (270, 30), (270, 400), (30, 400)], hexc('#2a2a33'), hexc('#16161c'), 6, 14)
    for y in (130, 300): p.stroke([(30, y), (270, y)], 8, hexc('#55555f'))
    p.shape(ell_pts(150, 215, 50, 60, 24, .1), hexc('#f0c541'), None, 4)
    return fin(p)


@lru_cache(maxsize=2)
def carvao():
    """monte de carvão. 380x260"""
    p = Pen(380, 260)
    rnd = random.Random(4)
    for i in range(11):
        x = 60 + (i % 5) * 65 + rnd.random() * 20; y = 220 - (i // 5) * 60 - rnd.random() * 15
        p.shape(ell_pts(x, y, 46 + rnd.random() * 12, 34, 9, rnd.random()), hexc('#3a3a44'), hexc('#1e1e24'), 5, 5)
    return fin(p)


@lru_cache(maxsize=2)
def globo():
    """Terra (globo simples). 700x700"""
    p = Pen(700, 700)
    p.shape(ell_pts(350, 350, 300, 300, 80), hexc('#3a7fd0'), hexc('#2a5fa4'), 7, 26)
    for lx, ly, rx, ry, rot in ((250, 240, 110, 80, .3), (430, 330, 120, 150, -.2), (230, 470, 80, 60, .5), (480, 160, 60, 40, 0)):
        p.shape(ell_pts(lx, ly, rx, ry, 30, rot, .15), hexc('#7fb05a'), hexc('#5f8a40'), 5, 8)
    return fin(p)


@lru_cache(maxsize=2)
def calendario():
    p = Pen(500, 520)
    p.shape([(20, 60), (480, 60), (480, 500), (20, 500)], WHITE, hexc('#c9c9d2'), 6, 10)
    p.shape([(20, 60), (480, 60), (480, 160), (20, 160)], RED, RED_D, 6, 6)
    for x in (120, 380): p.shape([(x - 14, 20), (x + 14, 20), (x + 14, 100), (x - 14, 100)], hexc('#6b6b70'), hexc('#4a4a50'), 4, 3)
    return fin(p)


def xis(c, x, y, size, t):
    if t <= 0: return
    d = ImageDraw.Draw(c)
    a = size * min(1, t)
    for s in (1, -1):
        d.line([(x - a, y - s * a), (x + a, y + s * a)], fill=INK, width=34)
        d.line([(x - a, y - s * a), (x + a, y + s * a)], fill=RED, width=22)


def chuva_moedas(c, f, f0, x0, x1, y0, y1, n=10):
    if f < f0: return
    rnd = random.Random(7)
    for i in range(n):
        st = f0 + i * 2
        if f < st: continue
        x = lerp(x0, x1, rnd.random()); t = ((f - st) * 22)
        y = y0 + t % (y1 - y0)
        paste_c(c, moeda().rotate((f * 9 + i * 40) % 360), x, y, .7)


# ------------------------------------------------------------------ cenas
def delegados(c, f, feet, seed, expr='neutral', vazio=None):
    xs = (130, 330, 530, 730, 930, 1130)
    for i, x in enumerate(xs):
        if i == vazio: continue
        put_p(c, x, feet, 540, f, seed + i, skin=i % 4, hair=HAIRS[i % len(HAIRS)], coat=COATS[i % len(COATS)],
              expr=expr if i % 2 else 'neutral', look=(i % 3 - 1) * .5)
    paste_c(c, mesa().resize((1300, 260)), 621, feet - 90, 1)
    for i, x in enumerate(xs):
        if i == vazio: continue
        paste_c(c, bandeirinha(i + seed).resize((110, 143)), x - 40, feet - 270, 1)


def s0(f):
    c = CEN('escritorio', 'day').copy()
    d0 = wt(0, 'duzentos') - 3
    e0 = wt(0, 'Estados') - 3
    v0 = wt(0, 'delegacao') - 3
    paste_c(c, cadeira().resize((260, 450)), 930, 1270, 1)
    delegados(c, f, 1500, 0, 'neutral', vazio=4)
    if f >= e0:
        paste_c(c, placa_eua().resize((240, 95)), 930, 1360, back(ramp(f, e0, e0 + 8)))
        paste_c(c, txt('EUA', 60, 0), 930, 1360, back(ramp(f, e0, e0 + 8)))
    num(c, 'QUASE 200 PAÍSES', 640, 470, f, d0, 96, -4)
    num(c, 'CLIMA', 640, 610, f, wt(0, 'clima') - 3, 96, 3)
    num(c, 'EUA: SEM DELEGAÇÃO', 640, 750, f, v0, 70, -2)
    if f >= v0:
        paste_c(c, txt('?', 180, 8), 930, 930, back(ramp(f, v0, v0 + 8)))
    z = lerp(1.15, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, d0)
    return c, (640 + 15 * math.sin(f * .03), 1020 + k * 8, z + .05 * smooth(ramp(f, v0 - 10, v0 + 30)), k), 'day'


def s1(f):
    c = CEN('praia', 'day').copy()
    c0 = wt(1, 'COP') - 3
    a0 = wt(1, 'Antalia') - 3
    m0 = wt(1, 'cem') - 3
    put_band(c, bandeira_tr(), 900, 900, 330, f, back(ramp(f, a0, a0 + 8)) if f >= a0 else 0)
    for i in range(7):
        if f < m0 + i * 2: continue
        x = 120 + i * 170
        put_p(c, x, 1650 - (i % 2) * 40, 400 - (i % 2) * 30, f, 40 + i, skin=i % 4, hair=HAIRS[i % 6], coat=COATS[(i + 2) % 8],
              expr='neutral', look=(i % 3 - 1) * .5)
    num(c, 'COP31', 640, 460, f, c0, 170, -5)
    num(c, 'CONFERÊNCIA DO CLIMA DA ONU', 620, 640, f, c0 + 8, 58, 2)
    num(c, 'ANTÁLIA, TURQUIA', 620, 760, f, a0, 84, -3)
    num(c, '+100 MIL PESSOAS', 620, 1150, f, m0, 96, 3)
    t = smooth(ramp(f, 0, 150))
    k = kick(f, c0, .6)
    return c, (640 + 30 * math.sin(f * .025), lerp(980, 1060, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0005 * f), lerp(-1, 1, t)), 'day'


def s2(f):
    c = CEN('cidade', 'golden').copy()
    g0 = wt(2, 'grau') - 3
    l0 = wt(2, 'limite') - 3
    rise = smooth(ramp(f, 0, g0 + 6))
    paste_c(c, sol(angry=1 if f >= g0 else 0, blink=blinkAt(f, 3)).resize((520, 520)), 360, lerp(1000, 820, rise), 1)
    lvl = int(round(lerp(2, 7.6, smooth(ramp(f, 4, g0 + 4)))))
    paste_c(c, termometro(lvl).resize((200, 700)), 960, 1150, 1)
    num(c, 'ALERTA DA ONU', 620, 400, f, 0, 96, -3)
    num(c, '+1,5 GRAU', 640, 560, f, g0, 120, 4)
    num(c, 'LIMITE DO ACORDO DE PARIS', 620, 1500, f, l0, 62, -2)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, g0, .7)
    return c, (640, lerp(1060, 1000, t) + k * 6, lerp(1.0, 1.05, t) * (1 + .0005 * f), lerp(1.5, -1.5, t)), 'golden'


def s3(f):
    c = CEN('cidade', 'day').copy()
    v0 = wt(3, 'vinte') - 3
    t0 = wt(3, 'trinta') - 3
    a0 = wt(3, 'dois') - 3
    num(c, 'ELETRICIDADE', 640, 420, f, wt(3, 'eletricidade') - 3, 110, -3)
    barra(c, 380, 1420, 240, 300, GRAY, f, v0, '20%')
    barra(c, 860, 1420, 240, 540, GOLD, f, t0, '35%')
    if f >= t0:
        r = raio(f // 4 % 3).resize((150, 350))
        paste_c(c, r, 860, 1200, back(ramp(f, t0 + 4, t0 + 12)))
    num(c, 'HOJE', 380, 1490, f, v0 + 4, 60, 0)
    num(c, 'META 2035', 860, 1490, f, a0, 60, 0)
    if f >= t0:
        d = ImageDraw.Draw(c)
        tt = ramp(f, t0, t0 + 14)
        d.line([(500, 1100), (lerp(500, 720, tt), lerp(1100, 960, tt))], fill=INK, width=18)
        d.line([(500, 1100), (lerp(500, 720, tt), lerp(1100, 960, tt))], fill=GREEN, width=10)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, t0, .6)
    return c, (640, lerp(1080, 1020, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0006 * f), k), 'day'


def s4(f):
    c = CEN('escritorio', 'dusk').copy()
    d0 = wt(4, 'dinheiro') - 3
    p0 = wt(4, 'prometida') - 3
    v0 = wt(4, 'vontade') - 3
    chuva_moedas(c, f, d0, 450, 800, 700, 1300, 9)
    put_p(c, 330, 1600, 620, f, 61, skin=2, hair=HAIRS[2], coat='#3a6b5a', expr='stern' if f > p0 else 'neutral',
          arms='point' if f > p0 else 'hang', look=.6)
    put_p(c, 930, 1600, 620, f, 62, skin=0, hair=HAIRS[4], coat='#2c3550', expr='nervous' if f > v0 else 'neutral',
          arms='up' if f > v0 else 'hang', look=-.6)
    num(c, 'A BRIGA: DINHEIRO', 640, 420, f, d0, 84, -3)
    num(c, 'CADÊ A AJUDA?', 380, 580, f, p0, 64, -4)
    num(c, 'PAÍSES POBRES', 380, 680, f, wt(4, 'pobres') - 3, 56, 0)
    num(c, 'SEM VONTADE', 900, 820, f, v0, 64, 4)
    num(c, 'EUROPA', 900, 920, f, wt(4, 'Europa') - 3, 56, 0)
    t = smooth(ramp(f, 0, 140))
    k = kick(f, d0, .6)
    cx = lerp(620, 660, smooth(ramp(f, v0 - 20, v0 + 20)))
    return c, (cx, lerp(1040, 1080, t) + k * 6, lerp(1.06, 1.0, t) * (1 + .0006 * f), lerp(-1.5, 1.5, t)), 'dusk'


def s5(f):
    c = CEN('floresta', 'dusk').copy()
    b0 = wt(5, 'Brasil') - 3
    p0 = wt(5, 'petroleo') - 3
    k0 = wt(5, 'carvao') - 3
    num(c, 'POR QUE IMPORTA?', 640, 400, f, 0, 84, -3)
    put_band(c, bandeira_br(), 640, 720, 300, f, back(ramp(f, b0, b0 + 8)) if f >= b0 else 0)
    num(c, 'COP30 NO BRASIL', 640, 560, f, b0, 76, 3)
    if f >= p0:
        paste_c(c, barril().resize((240, 336)), 380, 1360, back(ramp(f, p0, p0 + 8)))
        num(c, 'PETRÓLEO', 380, 1130, f, p0, 64, -3)
        xis(c, 380, 1360, 120, ramp(f, p0 + 10, p0 + 16))
    if f >= k0:
        paste_c(c, carvao().resize((340, 233)), 900, 1420, back(ramp(f, k0, k0 + 8)))
        num(c, 'CARVÃO', 900, 1230, f, k0, 64, 3)
        xis(c, 900, 1400, 120, ramp(f, k0 + 10, k0 + 16))
    num(c, 'FORA DO ACORDO FINAL', 640, 1500, f, wt(5, 'acordo') - 3, 60, -2)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, p0, .6)
    return c, (640 + 15 * math.sin(f * .04), lerp(1000, 1060, t) + k * 6, lerp(1.0, 1.03, t) * (1 + .0006 * f), lerp(0, 1.5, t)), 'dusk'


def s6(f):
    c = CEN('praia', 'dusk').copy()
    n0 = wt(6, 'novembro') - 3
    l0 = wt(6, 'longe') - 3
    paste_c(c, globo().rotate(-f * .4, resample=Image.BICUBIC), 640, 1050, .9)
    put_band(c, bandeira_tr(), 1000, 760, 240, f, 1)
    if f >= n0:
        paste_c(c, calendario().resize((280, 291)), 260, 780, back(ramp(f, n0, n0 + 8)))
        paste_c(c, txt('20/11', 74, 0), 260, 830, back(ramp(f, n0, n0 + 8)))
    num(c, 'VAI MAIS LONGE?', 640, 470, f, l0 - 6, 92, -4)
    z = lerp(1.0, 1.06, smooth(ramp(f, 0, 90))) + .0003 * f
    return c, (640 - 20 * math.sin(f * .03), 1060, z, lerp(0, -1.5, smooth(ramp(f, 0, 90)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'duzentos') - 3, 140, .8)
    s.ting(s.W(0, 'delegacao') - 3, .25)
    s.ting(s.W(1, 'COP') - 3, .3)
    s.whoosh(s.W(1, 'Antalia') - 3, .3, .5)
    s.thunk(s.W(2, 'grau') - 3, 140, .7)
    s.thunk(s.W(3, 'vinte') - 3, 200, .5)
    s.thunk(s.W(3, 'trinta') - 3, 160, .7)
    s.ting(s.W(4, 'dinheiro') - 3, .3)
    s.thunk(s.W(4, 'vontade') - 3, 150, .6)
    s.thunk(s.W(5, 'petroleo') + 7, 160, .5)
    s.thunk(s.W(5, 'carvao') + 7, 160, .5)
    s.ting(s.W(6, 'novembro') - 3, .3)
