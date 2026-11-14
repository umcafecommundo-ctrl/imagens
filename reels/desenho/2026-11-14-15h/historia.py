"""Um Café com o Mundo — O MUNDO EXPLICADO (sábado 14/11/2026, 15h).
Tema: Trump, Xi e Putin terão a 1ª reunião a três, em Shenzhen (China), à margem da cúpula da APEC.
Fontes (conferidas em 14/11/2026):
- Al Jazeera, 14/11/2026 ("Trump, Xi and Putin to hold first three-way summit in China"): Casa Branca confirmou; reunião
  "sem precedentes" na APEC em Shenzhen na próxima semana; New START expirou em fevereiro, deixando os dois maiores arsenais
  sem limite pela 1ª vez em mais de 50 anos; Trump quer acordo novo que inclua a China; Irã na pauta, Ucrânia fora;
  funcionário dos EUA à Reuters: não esperam acordo, é o começo de uma conversa; Peskov rejeita comparação com Yalta (1945).
- Al Jazeera, 14/11/2026 ("Trump-Xi-Putin trilateral meeting at APEC: what to expect"): APEC 18-19/11; New START assinado em
  2010; Rússia tem mais ogivas, depois EUA, depois China, que amplia o arsenal rapidamente; chancelaria chinesa: pedir que a
  China entre agora seria "injusto e irrealista"; Piotr Tolstoi (Duma) fala em "nova Yalta".
- Times of Israel (liveblog 14/11/2026): Casa Branca diz que o encontro a três será na quinta-feira (19/11) em Shenzhen.
Tom sério; personagens genéricos (sem traços das pessoas reais); nomes só na narração e na legenda."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Estados Unidos, China e Rússia vão se reunir a três, pela primeira vez.",
    "Trump, Xi Jinping e Putin se encontram nesta quinta, em Shenzhen, na China.",
    "O tema: armas nucleares. Em fevereiro, acabou o tratado que limitava os arsenais americano e russo.",
    "Pela primeira vez em mais de cinquenta anos, os dois maiores arsenais estão sem limite. E o da China cresce rápido.",
    "Trump quer um acordo novo, com a China. Pequim diz que, agora, é irrealista.",
    "A guerra no Irã entra na pauta. A Ucrânia, não.",
    "Por que isso importa? Na Rússia, já falam em uma nova Yalta, a conferência de mil novecentos e quarenta e cinco que repartiu a Europa.",
    "Mas a Casa Branca não espera nenhum acordo. É só o começo da conversa.",
]
CAPTXT = [
    "Estados Unidos, China e Rússia vão se reunir|a três, pela primeira vez.",
    "Trump, Xi Jinping e Putin se encontram|nesta quinta, em Shenzhen, na China.",
    "O tema: armas nucleares.|Em fevereiro, acabou o tratado que limitava|os arsenais americano e russo.",
    "Pela primeira vez em mais de 50 anos,|os dois maiores arsenais estão sem limite.|E o da China cresce rápido.",
    "Trump quer um acordo novo, com a China.|Pequim diz que, agora, é irrealista.",
    "A guerra no Irã entra na pauta.|A Ucrânia, não.",
    "Por que isso importa? Na Rússia, já falam|em uma nova Yalta, a conferência de 1945|que repartiu a Europa.",
    "Mas a Casa Branca não espera nenhum acordo.|É só o começo da conversa.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'Unidos', 4), (0, 'China', 4), (0, 'Russia', 4), (0, 'primeira', 4),
         (1, 'quinta', 4), (1, 'Shenzhen', 4), (2, 'nucleares', 4), (2, 'acabou', 4),
         (3, 'cinquenta', 6), (3, 'limite', 4), (3, 'rapido', 4), (4, 'acordo', 4), (4, 'irrealista', 4),
         (5, 'Ira', 4), (5, 'Ucrania', 4), (6, 'Yalta', 4), (6, 'quarenta', 6), (7, 'nenhum', 4), (7, 'comeco', 4)]


RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); WHITE = (255, 255, 255)
UBLUE = hexc('#0057b7'); UYEL = hexc('#ffd700'); TEAL = hexc('#2a9d8f')
RU_R = hexc('#d52b1e'); RU_B = hexc('#0039a6'); US_R = hexc('#b22234'); US_B = hexc('#3c3b6e')
CNR = hexc('#de2910'); YEL = hexc('#f6d33c'); PAPER = hexc('#f4efe1'); PAPER_D = hexc('#d2c8ae')
GRAY = hexc('#c9ced6'); GRAY_D = hexc('#8e96a3'); GREEN = hexc('#3aa66a')


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


# três presidentes genéricos (sem traços das pessoas reais)
PUS = dict(hair='#d9c9a0', tie='#b22234', suit='#2c3550', skin=0)
PCN = dict(hair='#2a2a2e', tie='#de2910', suit='#3a3a44', skin=1)
PRU = dict(hair='#9a9aa2', tie='#0039a6', suit='#2c2c38', skin=0)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def _estrela(cx, cy, r, rot=0.0):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + rot + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .4
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


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


@lru_cache(maxsize=2)
def bandeira_cn():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 270), (10, 270)], CNR)
    p.poly(_estrela(80, 80, 42), YEL)
    for (x, y) in ((150, 36), (178, 66), (178, 106), (150, 136)):
        p.poly(_estrela(x, y, 15, .4), YEL)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_ua():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 140), (10, 140)], UBLUE)
    p.poly([(10, 140), (410, 140), (410, 270), (10, 270)], UYEL)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_ir():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 96), (10, 96)], hexc('#239f40'))
    p.poly([(10, 96), (410, 96), (410, 183), (10, 183)], WHITE)
    p.poly([(10, 183), (410, 183), (410, 270), (10, 270)], hexc('#da0000'))
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def missil():
    """míssil genérico de pé. 240x760"""
    p = Pen(240, 760)
    p.shape([(80, 700), (30, 750), (30, 660), (80, 600)], RED, RED_D, 5, 4)
    p.shape([(160, 700), (210, 750), (210, 660), (160, 600)], RED, RED_D, 5, 4)
    p.shape([(80, 210), (160, 210), (160, 740), (80, 740)], GRAY, GRAY_D, 6, 10)
    p.shape([(80, 214), (120, 40), (160, 214)], RED, RED_D, 6, 6)
    p.stroke([(80, 330), (160, 330)], 5)
    p.stroke([(80, 600), (160, 600)], 5)
    p.dot(120, 450, 22, UYEL, 4)
    return fin(p)


def pilha(c, x, base, n, w=90, gap=16, f=0, f0=-99):
    """fileira de mísseis (n pode ser fracionário: o último sobe)."""
    full = int(n); fr = n - full
    tot = math.ceil(n)
    x0 = x - (tot - 1) * (w + gap) / 2
    im = missil()
    for i in range(tot):
        s = 1.0 if i < full else fr
        if s <= .02: continue
        h = w * 760 / 240
        mi = im.resize((int(w), int(h)))
        y = base - h / 2 + (1 - s) * h * .4
        paste_c(c, mi, x0 + i * (w + gap), y + 4 * math.sin(f * .1 + i), s if i >= full else 1.0)


@lru_cache(maxsize=2)
def tratado():
    """folha de tratado. 520x660"""
    p = Pen(520, 660)
    p.shape([(30, 30), (490, 30), (490, 630), (30, 630)], PAPER, PAPER_D, 6, 12)
    for y in range(200, 520, 46):
        p.stroke([(80, y), (440, y)], 8, hexc('#b7ad95'))
    p.stroke(curve((300, 580), (360, 540), (430, 585), 10), 6, hexc('#2b3d7a'))
    p.stroke(curve((90, 580), (150, 540), (210, 585), 10), 6, hexc('#2b3d7a'))
    return fin(p)


def tratado_rasgado(c, x, y, s, t):
    """t 0..1: as duas metades se afastam."""
    im = tratado()
    W, H = im.size
    a = im.crop((0, 0, W // 2, H)); b = im.crop((W // 2, 0, W, H))
    a = a.rotate(8 * t, expand=True, resample=Image.BICUBIC); b = b.rotate(-8 * t, expand=True, resample=Image.BICUBIC)
    paste_c(c, a, x - W * s / 4 - 90 * t, y + 30 * t, s)
    paste_c(c, b, x + W * s / 4 + 90 * t, y + 50 * t, s)


@lru_cache(maxsize=2)
def marcador():
    p = Pen(200, 280)
    p.shape([(100, 272), (30, 120), (40, 60), (100, 20), (160, 60), (170, 120)], RED, RED_D, 6, 8)
    p.dot(100, 100, 34, WHITE, 5)
    return fin(p)


def mesa(c, cx, y, w=420):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([cx - w, y, cx + w, y + 60], 14, fill=hexc('#a8744a'), outline=INK, width=6)
    d.rectangle([cx - w + 40, y + 60, cx - w + 80, y + 260], fill=hexc('#7d5534'), outline=INK, width=5)
    d.rectangle([cx + w - 80, y + 60, cx + w - 40, y + 260], fill=hexc('#7d5534'), outline=INK, width=5)


def calendario(c, x, y, s, sz=1.0, col=TEAL):
    sz = max(.08, sz)
    d = ImageDraw.Draw(c)
    w, h = 300 * sz, 280 * sz
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], 22 * sz, fill=WHITE, outline=INK, width=6)
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y - h / 2 + 70 * sz], 22 * sz, fill=col, outline=INK, width=6)
    paste_c(c, txt(s, int(90 * sz), 0), x, y + 30 * sz, 1)


def predio(c, x, base, w, h, seed=0):
    d = ImageDraw.Draw(c)
    col = hexc(['#8d7f9c', '#7a8aa6', '#9b8d84', '#7f9a93'][seed % 4])
    d.rounded_rectangle([x - w / 2, base - h, x + w / 2, base], 10, fill=col, outline=INK, width=6)
    cols = max(2, int(w // 70)); rows = max(2, int(h // 90))
    for r in range(rows):
        for q in range(cols):
            wx = x - w / 2 + 22 + q * (w - 44) / cols; wy = base - h + 28 + r * (h - 56) / rows
            on = ((r * 7 + q * 3 + seed) % 5) != 0
            d.rectangle([wx + 6, wy, wx + (w - 44) / cols - 6, wy + (h - 56) / rows - 20], fill=hexc('#ffd65a') if on else hexc('#2b2d3a'), outline=INK, width=3)


@lru_cache(maxsize=2)
def europa():
    """mancha simples de continente (Europa genérica) em tom sépia. 900x700"""
    p = Pen(900, 700)
    pts = [(120, 520), (90, 430), (150, 360), (120, 280), (200, 220), (260, 250), (300, 160), (380, 120), (430, 60),
           (520, 80), (560, 160), (650, 140), (760, 180), (830, 260), (800, 360), (720, 420), (660, 520), (560, 560),
           (520, 640), (440, 600), (380, 650), (320, 590), (240, 620), (180, 580)]
    p.shape(pts, hexc('#d9c38f'), hexc('#a8915e'), 6, 12)
    p.stroke([(450, 70), (430, 300), (470, 620)], 7, hexc('#8a3b2e'))
    return fin(p)


def sala(c):
    """sala de reunião neutra por cima do escritório (cobre monitor, janela e planta do fundo)."""
    d = ImageDraw.Draw(c)
    d.rectangle([0, 0, 1242, 1505], fill=hexc('#c8c2da'))
    for x in range(60, 1242, 160):
        d.rectangle([x, 300, x + 120, 1080], outline=hexc('#b3acc9'), width=6)
    d.rectangle([0, 1120, 1242, 1505], fill=hexc('#a99fc0'))
    d.line([(0, 1120), (1242, 1120)], fill=INK, width=6)
    d.rectangle([0, 1495, 1242, 1510], fill=hexc('#7d7398'))


# ------------------------------------------------------------------ cenas
def s0(f):
    """gancho: três bandeiras surgem em volta da mesa."""
    c = CEN('escritorio', 'dusk').copy(); sala(c)
    u0 = wt(0, 'Unidos') - 3; ch0 = wt(0, 'China') - 3; r0 = wt(0, 'Russia') - 3; p0 = wt(0, 'primeira') - 3
    mesa(c, 640, 1290)
    for x, im, k0 in ((260, bandeira_us(), u0), (640, bandeira_cn(), ch0), (1020, bandeira_ru(), r0)):
        if f >= k0:
            paste_c(c, im, x, 1120, back(ramp(f, k0, k0 + 8)) * .62)
    num(c, 'EUA', 260, 1300, f, u0, 60, -3)
    num(c, 'CHINA', 640, 1300, f, ch0, 60, 2)
    num(c, 'RÚSSIA', 1020, 1300, f, r0, 56, -2)
    num(c, 'A TRÊS', 640, 520, f, p0 - 12, 130, 3)
    num(c, '1ª VEZ', 640, 720, f, p0, 170, -4)
    z = lerp(1.3, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, p0, .7)
    return c, (640, 1080 + k * 8, z, k), 'dusk'


def s1(f):
    """Shenzhen: prédios, marcador, calendário QUINTA, três presidentes genéricos chegando."""
    c = CEN('cidade', 'dusk').copy()
    q0 = wt(1, 'quinta') - 3; sz0 = wt(1, 'Shenzhen') - 3; cu0 = wt(1, 'China') + 6
    t0 = wt(1, 'Trump') - 3; x0 = wt(1, 'Xi') - 3; pu0 = wt(1, 'Putin') - 3
    for x, w, h, sd in ((150, 190, 760, 1), (380, 150, 980, 3), (870, 170, 900, 2), (1100, 200, 700, 0)):
        predio(c, x, 1520, w, h, sd)
    if f >= q0:
        calendario(c, 1000, 520, 'QUI', sz=back(ramp(f, q0, q0 + 8)) * .7)
    if f >= sz0:
        paste_c(c, marcador(), 620, 560, back(ramp(f, sz0, sz0 + 8)) * .5)
        num(c, 'SHENZHEN', 620, 400, f, sz0, 110, -3)
        num(c, 'CHINA', 620, 730, f, sz0 + 6, 70, 2)
    num(c, 'CÚPULA APEC', 640, 880, f, cu0, 80, -2)
    for kx, k0, kw, sd in ((300, t0, PUS, 3), (640, x0, PCN, 5), (980, pu0, PRU, 7)):
        if f >= k0:
            tt = smooth(ramp(f, k0, k0 + 14))
            put_pol(c, kx, lerp(1900, 1520, tt), 520, f, sd, expr='neutral', look=0, **kw)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200))) * (1 + .0005 * f)
    k = kick(f, sz0, .5)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 200))), 1060 + k * 6, z, k), 'dusk'


def s2(f):
    """armas nucleares: mísseis; depois o tratado se rasga."""
    c = CEN('lab', 'dusk').copy()
    n0 = wt(2, 'nucleares') - 3; fe0 = wt(2, 'fevereiro') - 3; a0 = wt(2, 'acabou') - 3; ar0 = wt(2, 'arsenais') - 3
    num(c, 'ARMAS NUCLEARES', 640, 470, f, n0, 96, -3)
    if f < fe0:
        if f >= n0:
            pilha(c, 640, 1500, min(5, 5 * smooth(ramp(f, n0, n0 + 18)) + .001), 140, 24, f)
    else:
        num(c, 'FEVEREIRO', 640, 630, f, fe0, 90, 3)
        t = smooth(ramp(f, a0, a0 + 12)) if f >= a0 else 0
        tratado_rasgado(c, 640, 1130, .95, t)
        if f >= a0:
            num(c, 'FIM DO TRATADO', 640, 1480, f, a0, 76, -2)
        if f >= ar0:
            paste_c(c, bandeira_us(), 250, 800, back(ramp(f, ar0, ar0 + 8)) * .4)
            paste_c(c, bandeira_ru(), 1030, 800, back(ramp(f, ar0 + 6, ar0 + 14)) * .4)
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 200))) * (1 + .0004 * f)
    k = kick(f, a0, .8)
    return c, (640, 1060 + k * 8, z, k), 'dusk'


def s3(f):
    """sem limite há 50 anos: duas fileiras de mísseis enormes e a China crescendo."""
    c = CEN('mapa', 'dusk').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#35507a'))
    c0 = wt(3, 'cinquenta') - 3; l0 = wt(3, 'limite') - 3; ch0 = wt(3, 'China') - 3; ra0 = wt(3, 'rapido') - 3
    num(c, '+ DE 50 ANOS', 640, 470, f, c0, 110, -3)
    num(c, 'SEM LIMITE', 640, 640, f, l0, 120, 3)
    paste_c(c, bandeira_us(), 300, 860, .5); paste_c(c, bandeira_ru(), 940, 860, .5)
    gr = 3 + (2.0 * smooth(ramp(f, l0, l0 + 20)) if f >= l0 else 0)
    pilha(c, 300, 1440, gr, 84, 12, f)
    pilha(c, 940, 1440, gr, 84, 12, f)
    if f >= ch0:
        paste_c(c, bandeira_cn(), 640, 1040, back(ramp(f, ch0, ch0 + 8)) * .45)
        pilha(c, 640, 1440, .999 + 1.0 * smooth(ramp(f, ch0, ra0 + 18)), 60, 10, f)
    if f >= ra0:
        num(c, 'CRESCENDO', 640, 1560, f, ra0, 64, -2)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 240))) * (1 + .0004 * f)
    k = kick(f, l0, .7)
    return c, (640, lerp(1100, 1060, smooth(ramp(f, 0, 240))) + k * 6, z, k), 'dusk'


def s4(f):
    """acordo novo com a China: o americano aponta o papel; o chinês recusa."""
    c = CEN('escritorio', 'dusk').copy(); sala(c)
    a0 = wt(4, 'acordo') - 3; d0 = wt(4, 'China') - 3; pq0 = wt(4, 'Pequim') - 3; ir0 = wt(4, 'irrealista') - 3
    put_pol(c, 330, 1480, 560, f, 3, expr='grin' if f >= a0 else 'neutral', arms='point' if f >= a0 else 'hang', look=1, **PUS)
    put_pol(c, 940, 1480, 560, f, 5, expr='stern' if f >= pq0 else 'neutral', arms='hang', look=-1, **PCN)
    mesa(c, 640, 1300)
    paste_c(c, tratado(), 640, 1230, .32)
    num(c, 'ACORDO NOVO?', 640, 470, f, a0, 110, -3)
    num(c, 'COM A CHINA', 640, 630, f, d0, 80, 2)
    num(c, 'IRREALISTA', 640, 790, f, ir0, 120, -4)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160))) * (1 + .0005 * f)
    cx = lerp(560, 720, smooth(ramp(f, pq0 - 10, pq0 + 14))) if f >= pq0 - 10 else 560
    k = kick(f, ir0, .6)
    return c, (cx, 1060 + k * 6, z, k), 'dusk'


def s5(f):
    """pauta: Irã entra; Ucrânia fica de fora."""
    c = CEN('escritorio', 'dusk').copy(); sala(c)
    i0 = wt(5, 'Ira') - 3; u0 = wt(5, 'Ucrania') - 3; n0 = wt(5, 'nao') - 3
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([170, 380, 1070, 1480], 26, fill=hexc('#f4efe1'), outline=INK, width=8)
    paste_c(c, txt('PAUTA', 96, 0), 620, 490, 1)
    if f >= i0:
        paste_c(c, bandeira_ir(), 420, 780, back(ramp(f, i0, i0 + 8)) * .5)
        num(c, 'IRÃ', 820, 760, f, i0, 100, -2)
        num(c, 'SIM', 820, 880, f, i0 + 6, 70, 3)
    if f >= u0:
        paste_c(c, bandeira_ua(), 420, 1180, back(ramp(f, u0, u0 + 8)) * .5)
        num(c, 'UCRÂNIA', 820, 1160, f, u0, 84, -2)
    if f >= n0:
        num(c, 'FORA', 820, 1290, f, n0, 90, 4)
        t = smooth(ramp(f, n0, n0 + 8))
        d.line([(300, 1080), (lerp(300, 540, t), lerp(1080, 1280, t))], fill=RED, width=22)
        d.line([(540, 1080), (lerp(540, 300, t), lerp(1080, 1280, t))], fill=RED, width=22)
    z = lerp(1.02, 1.12, smooth(ramp(f, 0, 140))) * (1 + .0005 * f)
    k = kick(f, n0, .6)
    return c, (620, lerp(900, 1060, smooth(ramp(f, i0 - 10, u0 + 10))) + k * 6, z, k), 'dusk'


def s6(f):
    """por que importa: nova Yalta? mapa sépia da Europa de 1945 dividido."""
    c = CEN('mapa', 'golden').copy()
    ImageDraw.Draw(c).rectangle([0, 380, 1242, 1700], fill=hexc('#6b5a44'))
    y0 = wt(6, 'Yalta') - 3; q0 = wt(6, 'quarenta') - 3; rp0 = wt(6, 'repartiu') - 3
    num(c, 'POR QUE IMPORTA?', 640, 470, f, 0, 88, -3)
    paste_c(c, europa(), 640, 1150, back(ramp(f, 0, 10)) * 1.05)
    num(c, 'NOVA YALTA?', 640, 640, f, y0, 120, 3)
    if f >= q0:
        calendario(c, 1040, 860, '1945', sz=back(ramp(f, q0, q0 + 8)) * .75, col=hexc('#8a3b2e'))
    if f >= rp0:
        num(c, 'EUROPA REPARTIDA', 640, 1530, f, rp0, 70, -2)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 240))) * (1 + .0004 * f)
    k = kick(f, y0, .7)
    return c, (640, 1080 + k * 6, z, k - .003 * f), 'golden'


def s7(f):
    """fim: os três à mesa; NENHUM ACORDO / SÓ O COMEÇO."""
    c = CEN('escritorio', 'dusk').copy(); sala(c)
    n0 = wt(7, 'nenhum') - 3; co0 = wt(7, 'comeco') - 3
    paste_c(c, bandeira_us(), 260, 720, .35); paste_c(c, bandeira_cn(), 640, 720, .35); paste_c(c, bandeira_ru(), 1020, 720, .35)
    put_pol(c, 260, 1470, 500, f, 3, expr='neutral', look=1, **PUS)
    put_pol(c, 640, 1470, 500, f, 5, expr='neutral', look=0, **PCN)
    put_pol(c, 1020, 1470, 500, f, 7, expr='neutral', look=-1, **PRU)
    mesa(c, 640, 1320, 520)
    num(c, 'NENHUM ACORDO', 640, 440, f, n0, 100, -3)
    num(c, 'SÓ O COMEÇO', 640, 590, f, co0, 110, 3)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 150))) * (1 + .0004 * f)
    return c, (640, lerp(1000, 1060, smooth(ramp(f, 0, 150))), z, .5 * math.sin(f * .05)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.ting(s.W(0, 'primeira') - 3, .3)
    s.thunk(s.W(0, 'Russia') - 3, 140, .4)
    s.ting(s.W(1, 'Shenzhen') - 3, .25)
    s.thunk(s.W(2, 'acabou') - 3, 150, .6)
    s.thunk(s.W(3, 'limite') - 3, 150, .6)
    s.thunk(s.W(4, 'irrealista') - 3, 140, .5)
    s.thunk(s.W(5, 'nao') - 3, 140, .5)
    s.ting(s.W(7, 'comeco') - 3, .3)
