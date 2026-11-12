"""Um Café com o Mundo — CURIOSIDADE em desenho (12/11/2026 12h).
Fontes: anúncio de Adelaide University / Queensland Museum / James Cook University (via Scimex, 09/11/2026),
ScienceAlert (11/11/2026, entrevista com JP Hobbs e Peter Cowman), The Scuba News (12/11/2026), WION (11/11/2026).
Fatos: colônia de coral-rosa (gênero Pachyseris) de 1,56 km (mais de 1,5 km, "100 ônibus enfileirados") na encosta externa
do recife das Ilhas Cocos (Keeling), território australiano no Oceano Índico; de 14 a 65 m de profundidade.
Colônias de Pachyseris costumam ter ~2 m de diâmetro. O operador de mergulho local Dieter Gerhard via trechos dela
há ~30 anos (mais de três décadas). O biólogo JP Hobbs (Adelaide University) mapeou em 12 mergulhos e coletou amostras
de 50 pontos para DNA (Queensland Museum, Peter Cowman). Ainda não se sabe se é um organismo só ou várias colônias
que se juntaram; se for um só, pode ter centenas ou até milhares de anos (Cowman). Corais rasos da região sofreram com
branqueamento; o fundo parece mais seguro e pode servir de refúgio quando o raso sofre."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um coral do tamanho de cem ônibus enfileirados foi mapeado no meio do Oceano Índico.",
    "Ele fica nas Ilhas Cocos, da Austrália, e passa de um quilômetro e meio.",
    "É um coral rosa, que costuma ter uns dois metros. Esse desce de catorze a sessenta e cinco metros de fundo.",
    "Um instrutor de mergulho da ilha já via pedaços dele há uns trinta anos.",
    "Agora, cientistas mapearam tudo: doze mergulhos e cinquenta amostras de DNA.",
    "Mas ninguém sabe ainda se é um ser só, ou vários corais grudados.",
    "Se for um só, pode ter até milhares de anos. E, lá no fundo, pode ser um refúgio quando o raso esquenta.",
]
CAPTXT = [
    "Um coral do tamanho de 100 ônibus enfileirados|foi mapeado no meio do Oceano Índico.",
    "Ele fica nas Ilhas Cocos, da Austrália,|e passa de 1,5 km.",
    "É um coral-rosa, que costuma ter uns 2 metros.|Esse desce de 14 a 65 metros de fundo.",
    "Um instrutor de mergulho da ilha|já via pedaços dele há uns 30 anos.",
    "Agora, cientistas mapearam tudo:|12 mergulhos e 50 amostras de DNA.",
    "Mas ninguém sabe ainda se é um ser só,|ou vários corais grudados.",
    "Se for um só, pode ter até milhares de anos.|E, lá no fundo, pode ser um refúgio|quando o raso esquenta.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'cem', 6), (0, 'oceano', 6), (1, 'cocos', 6), (1, 'quilometro', 6), (2, 'dois', 6), (2, 'catorze', 6),
         (2, 'sessenta', 6), (3, 'instrutor', 6), (3, 'trinta', 6), (4, 'doze', 6), (4, 'cinquenta', 6), (5, 'so', 6),
         (5, 'grudados', 6), (6, 'milhares', 6), (6, 'refugio', 8)]

ROSA = hexc('#ee8fae'); ROSAD = hexc('#c25f82'); ROSAL = hexc('#f8c3d4')
SUIT = hexc('#2b6f86'); SUITD = hexc('#1d4b5c')
YEL = hexc('#f2c230'); YELD = hexc('#c99a14')
SKIN = hexc('#f1c28f'); SKIND = hexc('#d39a66')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


# ------------------------------------------------------------------ desenhos novos
def placa(seed=0):
    """placa de coral-rosa (Pachyseris): leque em camadas com sulcos. 400x320, base y~310."""
    p = Pen(400, 320); r = random.Random(seed)
    for k in range(2):
        cx = 200 + (r.random() - .5) * 60 + (k - .5) * 90; rx = 150 - k * 30; ry = 210 - k * 50
        pts = [(cx + rx * math.cos(a), 300 - ry * math.sin(a) * (1 + .08 * math.sin(a * 5 + seed)))
               for a in np.linspace(0, math.pi, 30)]
        p.shape(pts, ROSA if k == 0 else mul(ROSA, 1.04), ROSAD, 6, 12)
        for j in range(1, 4):
            q = j / 4
            p.stroke([(cx + rx * q * math.cos(a), 300 - ry * q * math.sin(a)) for a in np.linspace(.15, math.pi - .15, 18)], 5, ROSAD)
    p.stroke([(120, 120), (170, 92)], 6, ROSAL)
    return fin(p)


def onibus():
    """ônibus amarelo de lado. 400x220, rodas em y~210."""
    p = Pen(400, 220)
    p.shape([(20, 40), (370, 40), (385, 60), (385, 180), (20, 180)], YEL, YELD, 6, 10)
    for x in range(40, 330, 62): p.shape([(x, 60), (x + 48, 60), (x + 48, 110), (x, 110)], hexc('#bfe8ff'), None, 5)
    p.shape([(340, 60), (378, 64), (378, 120), (340, 120)], hexc('#bfe8ff'), None, 5)
    p.stroke([(20, 140), (385, 140)], 6, YELD)
    for x in (90, 300): p.dot(x, 182, 32, INK); p.dot(x, 182, 15, hexc('#9aa3ad'))
    return fin(p)


def mergulhador(blink=0, look=1, arm=0):
    """mergulhador nadando de lado, olhando para a direita. 700x420; centro do corpo ~(350,230)."""
    p = Pen(700, 420)
    for dy, ang in ((-20, -.25), (25, .25)):  # pernas e nadadeiras
        p.line([(240, 240 + dy * .5), (120, 230 + dy)], SUIT, 46, 5)
        x0, y0 = 120, 230 + dy
        p.shape([(x0 + 10, y0 - 22), (x0 - 110, y0 - 60 + dy), (x0 - 120, y0 + 40 + dy), (x0 + 10, y0 + 22)], YEL, YELD, 5, 6)
    p.shape(ell_pts(360, 235, 175, 92, 30), SUIT, SUITD, 6, 14)
    p.shape([(250, 120), (430, 120), (450, 140), (450, 172), (250, 172), (232, 146)], YEL, YELD, 5, 8)
    p.stroke([(450, 150), (540, 240), (590, 268)], 8, INK)
    ax = 470 + 70 * math.cos(arm); ay = 290 + 40 * math.sin(arm)
    p.line([(450, 260), (ax, ay)], SUIT, 34, 5); p.dot(ax, ay, 22, SKIN)
    p.shape(ell_pts(570, 215, 88, 86, 28), SKIN, SKIND, 6, 10)
    p.shape(ell_pts(578, 168, 92, 46, 24), SUITD, None, 5)  # touca
    p.shape([(560, 182), (668, 182), (672, 236), (560, 240)], hexc('#bfe8ff'), hexc('#8cc8ea'), 6, 0)
    ey = 210
    if blink: p.stroke([(600, ey), (640, ey)], 6, INK)
    else:
        p.dot(620, ey, 22, (255, 255, 255)); p.dot(620 + 8 * look, ey + 2, 10, INK)
    p.stroke([(566, 192), (590, 190)], 5, (255, 255, 255))
    p.dot(590, 268, 18, INK); p.dot(590, 268, 9, hexc('#555555'))
    return fin(p)


def tubo(cor=0):
    """tubinho de amostra com tampa. 120x300."""
    p = Pen(120, 300)
    p.shape([(30, 50), (90, 50), (90, 240), (60, 285), (30, 240)], hexc('#e8f6ff'), hexc('#b6d6ea'), 5, 6)
    p.shape([(36, 170), (84, 170), (84, 238), (60, 276), (36, 238)], ROSA, ROSAD, 4, 4)
    p.shape([(22, 20), (98, 20), (98, 56), (22, 56)], hexc('#5aa0e0') if cor % 2 else hexc('#e8574a'), None, 5)
    return fin(p)


def dna():
    """fita de DNA. 300x620."""
    p = Pen(300, 620)
    for k in range(13):
        y = 30 + k * 46; a = k * .55
        x1 = 150 + 100 * math.sin(a); x2 = 150 - 100 * math.sin(a)
        p.stroke([(x1, y), (x2, y)], 10, hexc('#f2a541') if k % 2 else hexc('#5aa0e0'))
    for s in (1, -1):
        p.line([(150 + s * 100 * math.sin(k * .55 / 4), 30 + k * 46 / 4) for k in range(49)], ROSA, 22, 5)
    return fin(p)


@lru_cache(maxsize=2)
def mapa_bg(luz='day'):
    """mar com a costa oeste da Austrália à direita e o atol das Ilhas Cocos no meio."""
    base = Image.new('RGBA', (BW, BH), hexc('#4f9fd6') + (255,)); p = Pen(BW, BH); rnd = random.Random(5)
    for i in range(34):
        x, y = rnd.randint(0, BW), rnd.randint(0, BH)
        p.stroke([(x, y), (x + 40, y - 6), (x + 80, y)], 4, hexc('#79b9e6'))
    land = [(1000, 300), (1150, 380), (1300, 400), (1300, 2000), (1180, 1900), (1080, 1700), (1020, 1400), (960, 1150),
            (930, 900), (980, 700), (940, 520)]
    p.shape(land, hexc('#d9b36a'), hexc('#b8914c'), 7, 0)
    for x, y, r in ((1120, 700, 70), (1180, 1250, 90)): p.poly(ell_pts(x, y, r * 1.3, r, 20), hexc('#c7a058'), 4)
    cx, cy = 430, 1000
    p.shape(ell_pts(cx, cy, 140, 170, 30), hexc('#7fe0d6'), None, 5)
    for i in range(16):
        a = -math.pi * .2 + i * (math.pi * 1.6 / 15)
        x = cx + 150 * math.cos(a); y = cy + 180 * math.sin(a)
        p.shape(ell_pts(x, y, 30, 18, 12), hexc('#8ccf5a'), hexc('#6aa83e'), 4, 4)
    return Image.alpha_composite(base, p.img.resize((BW, BH), Image.LANCZOS))


def put_img(c, fn, x, feet, h, aspect, flip=False, **kw):
    put_sprite(c, fn, x, feet, h, aspect, flip, {}, **kw)


def num(c, s, x, y, f, f0, size=150, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def peixe(c, x, y, f, s=1.0, flip=False, cor='#f2a541'):
    from PIL import ImageDraw
    d = ImageDraw.Draw(c); w = 60 * s; t = 10 * math.sin(f * .3)
    dirn = -1 if flip else 1
    d.ellipse([x - w, y - w * .45, x + w, y + w * .45], fill=hexc(cor), outline=INK, width=4)
    d.polygon([(x - dirn * w, y), (x - dirn * (w + 40 * s), y - 30 * s + t), (x - dirn * (w + 40 * s), y + 30 * s + t)], fill=mul(hexc(cor), .85), outline=INK)
    d.ellipse([x + dirn * w * .5 - 9, y - 14, x + dirn * w * .5 + 9, y + 4], fill=(255, 255, 255), outline=INK, width=3)


def cardume(c, f, ys=(620, 860, 1120), sp=3):
    for i, y in enumerate(ys):
        peixe(c, (200 + i * 380 + f * (sp if i % 2 == 0 else -sp)) % 1500 - 120, y + 20 * math.sin(f * .05 + i), f + i * 7, .8, i % 2 == 1,
              ('#f2a541', '#f4d35e', '#7fd1c7')[i % 3])


def faixa_coral(c, y, f, reveal=1.0, h=260, step=150):
    """fileira de placas de coral ao longo do recife (revela da esquerda para a direita)."""
    n = int(BW / step) + 2
    for i in range(n):
        if i / n > reveal: break
        sw = 6 * math.sin(f * .05 + i)
        put_img(c, 'placa', i * step - 40, y + (i % 2) * 40, h + sw, 400 / 320, False, seed=i % 5)


def bolhas(c, x, y, f, f0=0):
    from PIL import ImageDraw
    d = ImageDraw.Draw(c)
    for k in range(4):
        t = ((f - f0) * 4 + k * 40) % 160
        r = 8 + k * 3
        d.ellipse([x + 10 * math.sin(t * .1 + k) - r, y - t - r, x + 10 * math.sin(t * .1 + k) + r, y - t + r], fill=hexc('#d8f1ff'), outline=INK, width=3)


def diver(c, x, y, h, f, flip=False, seed=0, arm=None):
    bl = 1 if (f + seed * 13) % 70 < 3 else 0
    a = arm if arm is not None else .5 * math.sin(f * .12 + seed)
    put_sprite(c, 'mergulhador', x, y + 12 * math.sin(f * .07 + seed), h, 700 / 420, flip, {'arm': 8}, blink=bl, look=1, arm=a)
    bolhas(c, x + (-1 if flip else 1) * h * .55, y - h * .25, f, seed * 9)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('fundo_mar', 'day').copy()
    cardume(c, f)
    faixa_coral(c, 1560, f, ramp(f, 0, 25), 250)
    b0 = wt(0, 'cem') - 3
    for i in range(6):
        s = back(ramp(f, b0 + i * 2, b0 + i * 2 + 8))
        if s > .05: paste_c(c, sprite('onibus', (), 120, 400 / 220, False), 170 + i * 180, 1250, s)
    num(c, '100 ÔNIBUS!', 640, 700, f, b0, 160, -5)
    num(c, 'OCEANO ÍNDICO', 640, 900, f, wt(0, 'oceano') - 3, 90, 3)
    z = lerp(1.5, 1.08, easeOut(ramp(f, 0, 45))) * (1 + .0005 * f)
    k = kick(f, b0)
    return c, (640, lerp(1500, 1250, easeOut(ramp(f, 0, 45))) + k * 10, z, k), 'day'


def s1(f):
    c = mapa_bg('day').copy()
    c0 = wt(1, 'cocos') - 3
    if f >= c0:
        from PIL import ImageDraw
        d = ImageDraw.Draw(c); r = 200 + 40 * ((f - c0) % 30) / 30
        d.ellipse([430 - r, 1000 - r * 1.15, 430 + r, 1000 + r * 1.15], outline=hexc('#e8574a'), width=12)
    num(c, 'ILHAS COCOS', 560, 690, f, c0, 84, -4)
    num(c, 'AUSTRÁLIA', 860, 1560, f, wt(1, 'australia') - 3, 66, -8)
    num(c, '+ DE 1,5 KM', 520, 1330, f, wt(1, 'quilometro') - 4, 120, 3)
    t = smooth(ramp(f, 0, 110))
    k = kick(f, c0, .6)
    return c, (lerp(700, 560, t), lerp(1150, 1050, t) + k * 8, lerp(1.0, 1.25, t), k), 'day'


def s2(f):
    e0 = wt(2, 'esse') - 2
    if f < e0:
        c = CEN('fundo_mar', 'day').copy()
        cardume(c, f, (700, 950), 2)
        put_img(c, 'placa', 520, 1640, 300, 400 / 320, False, seed=2)
        diver(c, 930, 1470, 300, f, True, 1)
        d0 = wt(2, 'dois') - 3
        if f >= d0:
            from PIL import ImageDraw
            s = clamp((f - d0) / 10); d = ImageDraw.Draw(c)
            x0, x1 = 520 - 190 * s, 520 + 190 * s
            d.line([(x0, 1700), (x1, 1700)], fill=(255, 255, 255), width=10)
            for x in (x0, x1): d.line([(x, 1665), (x, 1735)], fill=(255, 255, 255), width=10)
        num(c, 'CORAL-ROSA', 640, 760, f, 0, 120, -4)
        num(c, '~2 METROS', 520, 1180, f, d0, 110, 3)
        t = smooth(ramp(f, 0, e0))
        return c, (640, lerp(1300, 1350, t), lerp(1.12, 1.25, t), 0), 'day'
    # descida pela parede de coral
    g = f - e0
    c = Image.new('RGBA', (BW, BH), (0, 0, 0, 255))
    dark = clamp(g / 120)
    top = tuple(int(lerp(a, b, dark)) for a, b in zip(hexc('#3f9fd6'), hexc('#123d6a')))
    bot = tuple(int(lerp(a, b, dark)) for a, b in zip(hexc('#1d5f96'), hexc('#071c3a')))
    arr = np.linspace(0, 1, BH)[:, None, None]
    c = Image.fromarray(np.uint8(np.array(top)[None, None, :] * (1 - arr) + np.array(bot)[None, None, :] * arr).repeat(BW, 1)).convert('RGBA')
    off = (g * 9) % 280
    for j in range(-1, 10):
        y = j * 280 - off + 280
        for i, x in enumerate((180, 420, 860, 1080)):
            if (j + i) % 3 == 0: continue
            put_img(c, 'placa', x, y, 230, 400 / 320, i % 2 == 1, seed=(j + i) % 5)
    for j in range(-1, 10):  # parede de coral central
        put_img(c, 'placa', 640, j * 280 - off + 280, 300, 400 / 320, j % 2 == 1, seed=(j * 3) % 5)
    diver(c, 640, 1000 + 10 * math.sin(g * .1), 330, f, False, 2, arm=-1.2)
    s0_ = wt(2, 'catorze') - 3; s1_ = wt(2, 'sessenta') - 3
    dep = 14 if f < s1_ else int(lerp(14, 65, smooth(ramp(f, s1_, s1_ + 20))))
    if f >= s0_: paste_c(c, txt(f'{dep} METROS', 130, -3), 640, 620, back(ramp(f, s0_, s0_ + 8)))
    num(c, 'DE FUNDO!', 640, 1450, f, wt(2, 'fundo') - 3, 110, 4)
    return c, (640, 1250, 1.08 + .0006 * g, 2 * math.sin(g * .03)), 'day'


def s3(f):
    c = CEN('fundo_mar', 'golden').copy()
    faixa_coral(c, 1600, f, 1, 240)
    cardume(c, f, (640,), 2)
    x = lerp(-200, 520, easeOut(ramp(f, 0, 50)))
    diver(c, x, 1150, 360, f, False, 3)
    t0 = wt(3, 'trinta') - 3
    num(c, 'INSTRUTOR DE MERGULHO', 640, 760, f, wt(3, 'instrutor') - 3, 50, -3)
    num(c, 'HÁ ~30 ANOS', 680, 1400, f, t0, 120, 4)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, t0, .5)
    return c, (lerp(520, 680, t), 1280 + k * 8, lerp(1.2, 1.1, t) * (1 + .0004 * f), k), 'golden'


def s4(f):
    c = CEN('fundo_mar', 'day').copy()
    faixa_coral(c, 1620, f, 1, 230)
    m0 = wt(4, 'mapearam') - 3
    diver(c, 330, 1230, 300, f, False, 4, arm=.0)
    diver(c, 950, 1280, 300, f, True, 5, arm=.0)
    if f >= m0:
        from PIL import ImageDraw
        d = ImageDraw.Draw(c); s = clamp((f - m0) / 12)
        d.line([(330 + 190, 1290), (330 + 190 + (950 - 190 - 520) * s, 1340)], fill=(255, 255, 255), width=8)
    d0 = wt(4, 'doze') - 3; a0 = wt(4, 'cinquenta') - 3
    num(c, '12 MERGULHOS', 640, 640, f, d0, 105, -4)
    num(c, '50 AMOSTRAS', 640, 800, f, a0, 105, 4)
    for i in range(5):
        s = back(ramp(f, a0 + i * 2, a0 + i * 2 + 8))
        if s > .05: paste_c(c, sprite('tubo', (('cor', i),), 170, 120 / 300, False), 400 + i * 120, 1440 - 8 * math.sin(f * .1 + i), s)
    num(c, 'DNA', 640, 1050, f, wt(4, 'dna') - 3, 110, -6)
    t = smooth(ramp(f, 0, 110))
    k = kick(f, d0, .6)
    return c, (640, lerp(1200, 1280, t) + k * 8, lerp(1.06, 1.16, t), k), 'day'


def s5(f):
    c = CEN('lab', 'dusk').copy()
    s0_ = wt(5, 'so') - 3; v0 = wt(5, 'varios') - 3
    put_sci(c, 330, 1760, 860, f, 2, arms='point' if f >= s0_ else 'cheek', expr='shock' if f >= v0 else 'nervous', skin=2, look=1, glasses=True)
    paste_c(c, sprite('dna', (), 480, 300 / 620, False), 860, 1180 + 10 * math.sin(f * .1))
    num(c, 'UM SER SÓ?', 790, 620, f, s0_, 92, -4)
    num(c, 'OU VÁRIOS?', 790, 780, f, v0, 92, 4)
    if f >= v0:
        for i in range(3):
            s = back(ramp(f, v0 + i * 3, v0 + i * 3 + 8))
            put_img(c, 'placa', 700 + i * 160, 1560, int(150 * s) + 1, 400 / 320, False, seed=i)
    t = smooth(ramp(f, 0, 90))
    return c, (640, lerp(1150, 1250, t), lerp(1.2, 1.08, t) * (1 + .0005 * f), lerp(0, 2.5, t)), 'dusk'


def s6(f):
    c = CEN('fundo_mar', 'dusk').copy()
    faixa_coral(c, 1450, f, 1, 300, 140)
    faixa_coral(c, 1640, f + 30, 1, 260, 170)
    m0 = wt(6, 'milhares') - 3; r0 = wt(6, 'refugio') - 3
    num(c, 'ATÉ MILHARES', 640, 620, f, m0, 110, -3); num(c, 'DE ANOS?', 640, 760, f, m0 + 4, 110, 3)
    diver(c, lerp(1000, 760, smooth(ramp(f, 0, 200))), 960, 230, f, True, 6)
    if f >= r0:
        for i in range(4):
            x = lerp(1300 + i * 80, 380 + i * 160, easeOut(ramp(f, r0 + i * 3, r0 + i * 3 + 30)))
            peixe(c, x, 1360 + (i % 2) * 50, f + i * 5, .7, True, ('#f2a541', '#f4d35e', '#7fd1c7', '#f28a8a')[i])
    num(c, 'REFÚGIO', 640, 1240, f, r0, 130, 4)
    z = lerp(1.0, 1.14, easeOut(ramp(f, 0, 60))) * (1 + .0005 * max(0, f - 60))
    return c, (640, lerp(1150, 1250, smooth(ramp(f, 0, 80))), z, lerp(0, -2, smooth(ramp(f, 0, 60))) - .01 * max(0, f - 60)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'cem') - 3, 150, .8)
    s.patter(s.W(0, 'cem') - 2, s.W(0, 'cem') + 12, 6, .14)
    s.ting(s.W(0, 'oceano') - 3, .3)
    s.ting(s.W(1, 'cocos') - 3, .35)
    s.thunk(s.W(1, 'quilometro') - 3, 140, .7)
    s.ting(s.W(2, 'dois') - 3, .3)
    s.whoosh(s.W(2, 'esse') - 2, .4, .5)
    s.thunk(s.W(2, 'sessenta') - 3, 120, .8)
    s.splash(s.W(3, 'instrutor') - 6, .35)
    s.thunk(s.W(3, 'trinta') - 3, 160, .6)
    s.thunk(s.W(4, 'doze') - 3, 200, .5)
    s.patter(s.W(4, 'cinquenta') - 3, s.W(4, 'cinquenta') + 12, 5, .14)
    s.ting(s.W(4, 'dna') - 3, .35)
    s.thunk(s.W(6, 'milhares') - 3, 130, .8)
    s.ting(s.W(6, 'refugio') - 3, .4)
