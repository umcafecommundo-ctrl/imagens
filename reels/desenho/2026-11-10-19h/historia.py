"""Um Café com o Mundo — O MUNDO EXPLICADO (terça 10/11/2026, 19h).
Tema: o Brasil apresenta na COP31 (Antália, Turquia) o "mapa do caminho" para deixar os combustíveis fósseis.
Fontes (conferidas em 10/11/2026):
- AP (Seth Borenstein/Melina Walling), 10/11/2026, "Brazil presents road map away from fossil fuels and toward renewable
  energies at UN climate talks" (via Sentinel Colorado, 2news, The Wire): apresentado na terça 10/11 na COP31 em Antália;
  Brasil comandou a conferência do ano passado e prometeu o mapa; o mundo concordou com "transition away from fossil
  fuels" há 3 anos sem dizer como; "alavancas" que cada país escolhe; duas básicas: parar de construir novas usinas e
  infraestrutura de combustível fóssil e acabar com subsídios que barateiam os fósseis; Ana Toni (CEO da COP30); Brasil é
  grande exportador de combustíveis fósseis e a maior parte da energia doméstica vem das hidrelétricas; o Brasil também
  apresenta mapas sobre desmatamento e sobre os US$ 1,3 trilhão de financiamento climático prometidos a países pobres;
  EUA ausentes pelo 2º ano.
- Just Security Early Edition 10/11/2026 (AP): Brasil lança na COP31 seu mapa para "transition away from fossil fuels".
Pessoas genéricas, sem logotipos. Tom neutro, sem opinião."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O Brasil acaba de entregar ao mundo um mapa para largar o petróleo, o carvão e o gás.",
    "Foi hoje, na COP trinta e um, a conferência do clima da ONU, em Antália, na Turquia.",
    "Há três anos, os países combinaram abandonar os combustíveis fósseis, mas ninguém disse como.",
    "O Brasil, que comandou a COP do ano passado, prometeu esse guia, e agora ele chegou.",
    "São alavancas que cada país escolhe, como não construir usinas novas a combustível fóssil e cortar os subsídios que barateiam esses combustíveis.",
    "Mas tem um detalhe: o Brasil é um grande exportador de petróleo, embora a maior parte da nossa eletricidade venha das hidrelétricas.",
    "E vem mais: guias contra o desmatamento e para o um vírgula três trilhão de dólares prometido aos países pobres.",
]
CAPTXT = [
    "O Brasil acaba de entregar ao mundo|um mapa para largar o petróleo,|o carvão e o gás.",
    "Foi hoje, na COP31, a conferência|do clima da ONU,|em Antália, na Turquia.",
    "Há 3 anos, os países combinaram|abandonar os combustíveis fósseis,|mas ninguém disse como.",
    "O Brasil, que comandou a COP|do ano passado, prometeu esse guia,|e agora ele chegou.",
    "São alavancas que cada país escolhe, como|não construir usinas novas a combustível fóssil|e cortar os subsídios que barateiam|esses combustíveis.",
    "Mas tem um detalhe: o Brasil é um grande|exportador de petróleo, embora a maior parte|da nossa eletricidade venha das hidrelétricas.",
    "E vem mais: guias contra o desmatamento|e para o US$ 1,3 trilhão|prometido aos países pobres.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Brasil', 4), (0, 'mapa', 6), (0, 'petroleo', 4), (0, 'carvao', 4), (0, 'gas', 4), (1, 'COP', 4), (1, 'Antalia', 4),
         (2, 'tres', 6), (2, 'fosseis', 4), (2, 'como', 4), (3, 'Brasil', 4), (3, 'chegou', 4), (4, 'alavancas', 4), (4, 'usinas', 4),
         (4, 'subsidios', 4), (5, 'exportador', 4), (5, 'hidreletricas', 4), (6, 'desmatamento', 4), (6, 'trilhao', 6), (6, 'pobres', 4)]

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


def delegados(c, f, feet, seed, expr='neutral', arms='hang', h=540):
    xs = (130, 330, 530, 730, 930, 1130)
    for i, x in enumerate(xs):
        put_p(c, x, feet, h, f, seed + i, skin=i % 4, hair=HAIRS[i % len(HAIRS)], coat=COATS[i % len(COATS)],
              expr=expr if i % 2 else 'neutral', arms=arms, look=(i % 3 - 1) * .5)
    paste_c(c, mesa().resize((1300, 260)), 621, feet - 90, 1)
    for i, x in enumerate(xs):
        paste_c(c, bandeirinha(i + seed).resize((110, 143)), x - 40, feet - 190, 1)


@lru_cache(maxsize=4)
def mapa_doc(prog=8):
    """mapa do caminho aberto: papel creme com trilha pontilhada de um barril (esq) até sol+cata-vento (dir). 1000x620.
    prog = 0..8 quanto da trilha já está desenhada."""
    p = Pen(1000, 620)
    p.shape([(20, 40), (980, 20), (970, 590), (30, 600)], hexc('#f6ecd0'), hexc('#d9c89c'), 7, 12)
    for x in (340, 660):
        p.stroke([(x, 30), (x + 5, 595)], 4, hexc('#d9c89c'))
    # barril pequeno
    p.shape([(90, 330), (190, 330), (190, 480), (90, 480)], hexc('#2a2a33'), hexc('#16161c'), 5, 6)
    p.stroke([(90, 380), (190, 380)], 5, hexc('#55555f'))
    # sol e cata-vento
    p.shape(ell_pts(860, 170, 60, 60, 30), hexc('#f7d046'), hexc('#e0a92a'), 5, 6)
    p.stroke([(830, 520), (845, 300), (860, 520)], 7, hexc('#ffffff'))
    p.stroke([(830, 520), (845, 300), (860, 520)], 3)
    for a in (-90, 30, 150):
        r = math.radians(a)
        p.stroke([(845, 300), (845 + 110 * math.cos(r), 300 + 110 * math.sin(r))], 12, hexc('#ffffff'))
    p.dot(845, 300, 14, hexc('#c9c9d2'), 4)
    pts = curve((200, 420), (500, 120), (800, 420), 40)
    n = int(len(pts) * prog / 8)
    for i in range(0, n, 3):
        p.dot(pts[i][0], pts[i][1], 9, RED)
    if prog >= 8:
        p.stroke([(770, 400), (800, 420), (770, 445)], 9, RED)
    return fin(p)


def put_mapa(c, x, y, w, f, f0):
    if f < f0: return
    t = ramp(f, f0, f0 + 16)
    im = mapa_doc(int(round(8 * ramp(f, f0 + 6, f0 + 30))))
    ww = int(w * lerp(.15, 1, easeOut(t))); hh = int(w * .62)
    im = im.resize((max(8, ww), hh)).rotate(2 * math.sin(f * .08), expand=True, resample=Image.BICUBIC)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=2)
def chama():
    """chama de gás azul. 240x320"""
    p = Pen(240, 320)
    p.shape([(120, 20), (200, 180), (190, 260), (120, 300), (50, 260), (40, 180)], hexc('#3a7fd0'), hexc('#2a5fa4'), 6, 8)
    p.shape([(120, 120), (160, 210), (150, 260), (120, 275), (90, 260), (80, 210)], hexc('#9fd0ee'), None, 4)
    return fin(p)


@lru_cache(maxsize=2)
def usina_fossil():
    """usina térmica genérica: prédio + 2 chaminés. 700x700, base y~690"""
    p = Pen(700, 700)
    for x in (430, 560):
        p.shape([(x - 45, 120), (x + 45, 120), (x + 60, 500), (x - 60, 500)], hexc('#b8bec8'), hexc('#8a919c'), 6, 10)
        p.shape([(x - 45, 150), (x + 45, 150), (x + 46, 185), (x - 46, 185)], RED, RED_D, 3, 2)
    p.shape([(40, 380), (660, 380), (660, 690), (40, 690)], hexc('#8a7a6a'), hexc('#5e5246'), 7, 14)
    p.shape([(40, 300), (300, 300), (300, 380), (40, 380)], hexc('#8a7a6a'), hexc('#5e5246'), 6, 8)
    for k in range(4):
        x = 90 + k * 150
        p.shape([(x, 500), (x + 80, 500), (x + 80, 570), (x, 570)], hexc('#f0c541'), hexc('#c99a22'), 4, 3)
    return fin(p)


def fumaca(c, x, y, f, s=1.0, seed=0, cor=(90, 90, 100)):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(6):
        t = ((f * .02 + i / 6 + seed * .13) % 1)
        r = (25 + 60 * t) * s
        xx = x + 50 * math.sin(t * 4 + seed) * s; yy = y - 300 * t * s
        a = int(170 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=cor + (a,))


def alavanca(c, x, y, ang, s=1.0):
    """alavanca de painel: base + haste que gira (ang em graus, -35..35)."""
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([x - 120 * s, y, x + 120 * s, y + 70 * s], 18, fill=hexc('#4a4f63'), outline=INK, width=6)
    r = math.radians(ang - 90)
    ex, ey = x + 190 * s * math.cos(r), y + 190 * s * math.sin(r)
    d.line([(x, y + 10), (ex, ey)], fill=INK, width=int(30 * s))
    d.line([(x, y + 10), (ex, ey)], fill=hexc('#c9c9d2'), width=int(18 * s))
    d.ellipse([ex - 42 * s, ey - 42 * s, ex + 42 * s, ey + 42 * s], fill=RED, outline=INK, width=6)


def cata_vento(c, x, base, h, f, spd=.08):
    d = ImageDraw.Draw(c)
    top = base - h
    d.polygon([(x - h * .05, base), (x - h * .02, top), (x + h * .02, top), (x + h * .05, base)], fill=WHITE, outline=INK, width=6)
    for k in range(3):
        a = f * spd + k * 2 * math.pi / 3
        ex, ey = x + h * .55 * math.cos(a), top + h * .55 * math.sin(a)
        nx, ny = -math.sin(a) * h * .045, math.cos(a) * h * .045
        d.polygon([(x, top), (x + nx * .5 + (ex - x) * .3, top + ny * .5 + (ey - top) * .3), (ex, ey), (x - nx * .3, top - ny * .3)],
                  fill=WHITE, outline=INK, width=5)
    d.ellipse([x - h * .05, top - h * .05, x + h * .05, top + h * .05], fill=hexc('#c9c9d2'), outline=INK, width=5)


@lru_cache(maxsize=2)
def petroleiro():
    """navio petroleiro genérico de lado. 900x380, linha d'água y~300"""
    p = Pen(900, 380)
    p.shape([(20, 170), (880, 170), (820, 330), (80, 330)], hexc('#b8433a'), hexc('#7e2c26'), 7, 12)
    p.shape([(20, 170), (880, 170), (870, 215), (30, 215)], hexc('#2a2a33'), None, 5)
    p.shape([(680, 40), (820, 40), (820, 170), (680, 170)], WHITE, hexc('#c9c9d2'), 6, 8)
    for k in range(3): p.dot(710 + k * 45, 90, 14, hexc('#9fd0ee'), 4)
    p.shape([(740, 0), (775, 0), (775, 40), (740, 40)], hexc('#2a2a33'), None, 4)
    for k in range(5):
        x = 100 + k * 110
        p.shape([(x, 110), (x + 80, 110), (x + 80, 170), (x, 170)], hexc('#2a2a33'), hexc('#16161c'), 4, 4)
    return fin(p)


@lru_cache(maxsize=2)
def represa():
    """hidrelétrica: barragem de concreto com água atrás e saída de água. 800x600, base y~590"""
    p = Pen(800, 600)
    p.poly([(0, 160), (300, 160), (300, 590), (0, 590)], hexc('#3a7fd0'))
    p.shape([(260, 80), (420, 80), (560, 590), (240, 590)], hexc('#c9ccd2'), hexc('#9aa0aa'), 7, 14)
    for k in range(3):
        y = 300 + k * 90
        p.shape([(380 + k * 25, y), (430 + k * 25, y), (430 + k * 25, y + 40), (380 + k * 25, y + 40)], hexc('#5a606c'), None, 4)
    p.shape([(560, 500), (800, 520), (800, 590), (540, 590)], hexc('#7fc0f0'), hexc('#3a7fd0'), 5, 4)
    return fin(p)


@lru_cache(maxsize=4)
def arvore(k=0):
    p = Pen(300, 500)
    p.shape([(130, 300), (170, 300), (175, 490), (125, 490)], hexc('#8a5a3a'), hexc('#5e3c24'), 5, 6)
    cols = [('#3aa66a', '#2a7a4e'), ('#4fb85a', '#358a40'), ('#2f8f5a', '#1f6a40')][k % 3]
    p.shape(ell_pts(150, 200, 130, 150, 40), hexc(cols[0]), hexc(cols[1]), 6, 16)
    return fin(p)


def toco(c, x, base):
    d = ImageDraw.Draw(c)
    d.rectangle([x - 30, base - 60, x + 30, base], fill=hexc('#8a5a3a'), outline=INK, width=6)
    d.ellipse([x - 30, base - 76, x + 30, base - 46], fill=hexc('#d9b080'), outline=INK, width=5)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('escritorio', 'day').copy()
    b0 = wt(0, 'Brasil') - 3
    m0 = wt(0, 'mapa') - 3
    p0 = wt(0, 'petroleo') - 3
    k0 = wt(0, 'carvao') - 3
    g0 = wt(0, 'gas') - 3
    put_band(c, bandeira_br(), 640, 470, 260, f, back(ramp(f, b0, b0 + 8)) if f >= b0 else 0)
    put_mapa(c, 640, 840, 820, f, m0)
    num(c, 'O MAPA PARA LARGAR', 640, 640, f, m0 + 4, 70, -3)
    for (x, im, w, fx, lab) in ((300, barril(), 170, p0, 'PETRÓLEO'), (640, carvao(), 250, k0, 'CARVÃO'), (980, chama(), 160, g0, 'GÁS')):
        if f >= fx:
            ii = im.resize((w, int(w * im.size[1] / im.size[0])))
            paste_c(c, ii, x, 1290, back(ramp(f, fx, fx + 8)))
            num(c, lab, x, 1440, f, fx, 56, 0)
            xis(c, x, 1290, 90, ramp(f, fx + 6, fx + 12))
    z = lerp(1.15, 1.0, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, m0)
    return c, (640 + 15 * math.sin(f * .03), lerp(900, 1020, smooth(ramp(f, m0, p0 + 10))) + k * 8, z, k), 'day'


def s1(f):
    c = CEN('praia', 'day').copy()
    c0 = wt(1, 'COP') - 3
    cl = wt(1, 'clima') - 3
    a0 = wt(1, 'Antalia') - 3
    put_band(c, bandeira_tr(), 900, 900, 330, f, back(ramp(f, a0, a0 + 8)) if f >= a0 else 0)
    for i in range(7):
        if f < cl + i * 2: continue
        x = 120 + i * 170
        put_p(c, x, 1650 - (i % 2) * 40, 400 - (i % 2) * 30, f, 40 + i, skin=i % 4, hair=HAIRS[i % 6], coat=COATS[(i + 2) % 8],
              expr='neutral', look=(i % 3 - 1) * .5)
    num(c, 'HOJE', 640, 330, f, 0, 90, 3)
    num(c, 'COP31', 640, 470, f, c0, 170, -5)
    num(c, 'CONFERÊNCIA DO CLIMA DA ONU', 620, 640, f, cl, 58, 2)
    num(c, 'ANTÁLIA, TURQUIA', 620, 760, f, a0, 84, -3)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, c0, .6)
    return c, (640 + 30 * math.sin(f * .025), lerp(980, 1060, t) + k * 6, lerp(1.08, 1.0, t) * (1 + .0005 * f), lerp(-1, 1, t)), 'day'


def s2(f):
    c = CEN('escritorio', 'golden').copy()
    t0 = wt(2, 'tres') - 3
    fo = wt(2, 'fosseis') - 3
    co = wt(2, 'como') - 3
    if f >= t0:
        paste_c(c, calendario().resize((260, 270)), 640, 520, back(ramp(f, t0, t0 + 8)))
        paste_c(c, txt('2023', 66, 0), 640, 570, back(ramp(f, t0, t0 + 8)))
        num(c, 'HÁ 3 ANOS', 640, 340, f, t0, 70, -3)
    num(c, 'ABANDONAR OS FÓSSEIS', 640, 720, f, fo, 74, 3)
    if f >= co:
        num(c, 'MAS COMO?', 640, 870, f, co, 120, -4)
    delegados(c, f, 1560, 10, expr='nervous' if f >= co else 'neutral', arms='up' if f >= co else 'hang', h=520)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, co, .7)
    return c, (640, lerp(1060, 1010, t) + k * 6, lerp(1.0, 1.06, t) * (1 + .0005 * f), lerp(1.5, -1.5, t) + k), 'golden'


def s3(f):
    c = CEN('floresta', 'day').copy()
    b0 = wt(3, 'Brasil') - 3
    cm = wt(3, 'comandou') - 3
    pr = wt(3, 'prometeu') - 3
    ch = wt(3, 'chegou') - 3
    put_band(c, bandeira_br(), 640, 520, 320, f, back(ramp(f, b0, b0 + 8)) if f >= b0 else 0)
    num(c, 'COMANDOU A COP30', 640, 330, f, cm, 76, -3)
    num(c, 'PROMESSA', 640, 800, f, pr, 90, 3)
    put_p(c, 300, 1660, 700, f, 71, skin=1, hair=HAIRS[0], coat='#3a6b5a', expr='grin' if f >= ch else 'neutral',
              arms='up' if f >= ch else 'hang', look=.5)
    if f >= pr:
        y = lerp(1600, 1150, easeOut(ramp(f, pr, pr + 20)))
        im = mapa_doc(8).resize((640, 397))
        paste_c(c, im, 830, y, 1)
    if f >= ch:
        carimbo_ok(c, 'CHEGOU!', 830, 1150, back(ramp(f, ch, ch + 8)))
    t = smooth(ramp(f, 0, 120))
    k = kick(f, ch, .7)
    return c, (640 + 20 * math.sin(f * .03), lerp(950, 1050, t) + k * 6, lerp(1.06, 1.0, t) * (1 + .0005 * f), k), 'day'


def carimbo_ok(c, s, x, y, sc, size=80):
    if sc <= .05: return
    t = txt(s, size, 0)
    im = Image.new('RGBA', (t.size[0] + 80, t.size[1] + 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([8, 8, im.size[0] - 8, im.size[1] - 8], 24, outline=GREEN, width=14)
    im.alpha_composite(t, (40, 30))
    im = im.rotate(-8, expand=True, resample=Image.BICUBIC)
    paste_c(c, im, x, y, sc)


def s4(f):
    c = CEN('cidade', 'day').copy()
    a0 = wt(4, 'alavancas') - 3
    e0 = wt(4, 'escolhe') - 3
    u0 = wt(4, 'usinas') - 3
    s0_ = wt(4, 'subsidios') - 3
    b0 = wt(4, 'barateiam') - 3
    num(c, 'ALAVANCAS', 640, 330, f, a0, 110, -3)
    num(c, 'CADA PAÍS ESCOLHE', 640, 470, f, e0, 66, 2)
    if f >= a0:
        ang = lerp(-35, 35, smooth(ramp(f, u0 - 10, u0 + 4)))
        ang2 = lerp(-35, 35, smooth(ramp(f, s0_ - 10, s0_ + 4)))
        alavanca(c, 330, 1450, ang, .8)
        alavanca(c, 950, 1450, ang2, .8)
    if f >= u0:
        paste_c(c, usina_fossil().resize((420, 420)), 330, 980, back(ramp(f, u0, u0 + 8)))
        if f < u0 + 14: fumaca(c, 390, 830, f, .7, 1)
        num(c, 'USINAS NOVAS', 330, 700, f, u0, 58, -3)
        xis(c, 330, 990, 150, ramp(f, u0 + 12, u0 + 18))
    if f >= s0_:
        for i in range(5):
            paste_c(c, moeda().resize((130, 130)), 870 + (i % 3) * 70, 1150 - i * 55 - (i % 2) * 20, back(ramp(f, s0_ + i, s0_ + i + 8)))
        num(c, 'SUBSÍDIOS', 950, 700, f, s0_, 64, 3)
        xis(c, 950, 1050, 150, ramp(f, s0_ + 12, s0_ + 18))
    if f >= b0:
        num(c, 'FÓSSIL MAIS BARATO', 950, 820, f, b0, 46, -2)
    t = smooth(ramp(f, 0, 160))
    cx = lerp(600, 680, smooth(ramp(f, u0 + 10, s0_ + 5)))
    z = lerp(1.0, 1.05, smooth(ramp(f, a0 + 10, u0))) - .05 * smooth(ramp(f, s0_ + 20, b0 + 20))
    k = kick(f, u0 + 12, .6) + kick(f, s0_ + 12, .6)
    return c, (cx, 1000 + k * 6, z * (1 + .0004 * f), lerp(-1, 1, t)), 'day'


def s5(f):
    c = CEN('praia', 'dusk').copy()
    m0 = wt(5, 'detalhe') - 3
    e0 = wt(5, 'exportador') - 3
    p0 = wt(5, 'petroleo') - 3
    h0 = wt(5, 'hidreletricas') - 3
    el = wt(5, 'eletricidade') - 3
    num(c, 'UM DETALHE...', 640, 330, f, m0, 90, -3)
    if f >= e0:
        x = lerp(-300, 380, easeOut(ramp(f, e0, e0 + 30))) + .6 * f
        paste_c(c, petroleiro().resize((620, 262)), x, 1240, 1)
        put_band(c, bandeira_br(), 640, 520, 200, f, back(ramp(f, e0, e0 + 8)))
        num(c, 'GRANDE EXPORTADOR', 640, 700, f, e0, 72, 3)
        num(c, 'DE PETRÓLEO', 640, 810, f, p0, 72, -2)
    if f >= el:
        paste_c(c, represa().resize((520, 390)), 870, 1180, back(ramp(f, el, el + 8)))
        r = raio(f // 4 % 3).resize((110, 260))
        paste_c(c, r, 980, 990, back(ramp(f, h0, h0 + 8)) if f >= h0 else 0)
        num(c, 'ELETRICIDADE:', 840, 1420, f, el, 56, -2)
        num(c, 'HIDRELÉTRICAS', 840, 1510, f, h0, 64, 2)
    t = smooth(ramp(f, 0, 160))
    cx = lerp(600, 660, smooth(ramp(f, el - 10, el + 30)))
    k = kick(f, p0, .6)
    return c, (cx, lerp(1000, 1040, t) + k * 6, lerp(1.06, 1.0, t) * (1 + .0005 * f), lerp(1.5, -1.5, t)), 'dusk'


def s6(f):
    c = CEN('floresta', 'dusk').copy()
    m0 = wt(6, 'mais') - 3
    d0 = wt(6, 'desmatamento') - 3
    t0 = wt(6, 'trilhao') - 3
    p0 = wt(6, 'pobres') - 3
    num(c, 'E VEM MAIS', 640, 330, f, m0, 100, -3)
    if f >= d0:
        for i, x in enumerate((180, 400, 620, 840, 1060)):
            paste_c(c, arvore(i).resize((220, 367)), x, 1300 - (i % 2) * 30, back(ramp(f, d0 + i, d0 + i + 8)))
        num(c, 'DESMATAMENTO', 640, 560, f, d0, 84, 3)
    chuva_moedas(c, f, t0, 300, 1000, 650, 1250, 10)
    num(c, 'US$ 1,3 TRILHÃO', 640, 760, f, t0, 104, -3)
    num(c, 'PARA PAÍSES POBRES', 640, 900, f, p0, 64, 2)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 140))) + .0003 * f
    k = kick(f, t0, .6)
    return c, (640 - 20 * math.sin(f * .03), 1020 + k * 6, z, lerp(0, -1.5, smooth(ramp(f, 0, 90)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.ting(s.W(0, 'Brasil') - 3, .3)
    s.whoosh(s.W(0, 'mapa') - 3, .3, .5)
    s.thunk(s.W(0, 'petroleo') + 3, 160, .5)
    s.thunk(s.W(0, 'carvao') + 3, 160, .5)
    s.thunk(s.W(0, 'gas') + 3, 160, .5)
    s.ting(s.W(1, 'COP') - 3, .3)
    s.whoosh(s.W(1, 'Antalia') - 3, .3, .5)
    s.thunk(s.W(2, 'como') - 3, 140, .7)
    s.ting(s.W(3, 'chegou') - 3, .35)
    s.thunk(s.W(4, 'usinas') + 9, 160, .5)
    s.thunk(s.W(4, 'subsidios') + 9, 160, .5)
    s.thunk(s.W(5, 'petroleo') - 3, 140, .6)
    s.ting(s.W(5, 'hidreletricas') - 3, .3)
    s.ting(s.W(6, 'trilhao') - 3, .35)
