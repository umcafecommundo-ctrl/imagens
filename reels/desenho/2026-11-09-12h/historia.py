"""Um Café com o Mundo — CURIOSIDADE em desenho (09/11/2026 12h).
Fontes: Kokugakuin University / Prefeitura de Matsuura (anúncio de 28/10/2026, via RKB e KTN News),
Fukuoka Now (30/10/2026), Archaeology Magazine (06/11/2026, citando The Mainichi), Arkeonews (06/11/2026).
Fatos: 3º navio afundado da invasão mongol de 1281 (Batalha de Koan, frota da dinastia Yuan de Kublai Khan, neto de
Gengis Khan, com forças da China e da Coreia) ao largo da ilha de Takashima, Matsuura, Nagasaki. Tufão em agosto de 1281
destruiu boa parte da frota. Navios achados em 2011, 2015 e 2023. Escavação de outubro de 2026 (Yoshifumi Ikeda):
5 dados (~1 cm) e 29 pecinhas (~3 cm) de um jogo chinês, consideradas precursoras das peças do mahjong; 1ª vez que
peças de jogo aparecem nesses naufrágios. Estrutura de ~15 m sugere navio de ~30 m, entre os maiores achados lá.
Faca e espinhas de peixe no mesmo trecho (cozinha); hipótese de que cozinheiros jogavam nas folgas. Nova escavação em 2027."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Dados de jogo passaram quase setecentos e cinquenta anos no fundo do mar do Japão.",
    "Eles estavam num navio da frota de Kublai Khan, neto de Gengis Khan, que tentou invadir o Japão em mil duzentos e oitenta e um.",
    "Mas um tufão afundou boa parte dos navios, perto da ilha de Takashima, em Nagasaki.",
    "Agora, arqueólogos acharam ali cinco dados e vinte e nove pecinhas de um jogo chinês, consideradas antepassadas do mahjong.",
    "É a primeira vez que peças de jogo aparecem nesses naufrágios. E esse navio pode ter tido uns trinta metros.",
    "Perto delas, havia uma faca e espinhas de peixe. Talvez os cozinheiros jogassem nas horas de folga.",
    "Ou seja: no meio de uma invasão, ainda sobrava tempo pra uma partidinha.",
]
CAPTXT = [
    "Dados de jogo passaram quase 750 anos|no fundo do mar do Japão.",
    "Eles estavam num navio da frota de Kublai Khan,|neto de Gengis Khan,|que tentou invadir o Japão em 1281.",
    "Mas um tufão afundou boa parte dos navios,|perto da ilha de Takashima, em Nagasaki.",
    "Agora, arqueólogos acharam ali 5 dados e 29 pecinhas|de um jogo chinês,|consideradas antepassadas do mahjong.",
    "É a primeira vez que peças de jogo aparecem nesses naufrágios.|E esse navio pode ter tido uns 30 metros.",
    "Perto delas, havia uma faca e espinhas de peixe.|Talvez os cozinheiros jogassem nas horas de folga.",
    "Ou seja: no meio de uma invasão,|ainda sobrava tempo pra uma partidinha.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'setecentos', 6), (0, 'japao', 6), (1, 'kublai', 6), (1, 'um', 8), (2, 'tufao', 6), (2, 'nagasaki', 6),
         (3, 'cinco', 6), (3, 'vinte', 6), (3, 'mahjong', 8), (4, 'primeira', 6), (4, 'trinta', 8), (5, 'faca', 6), (5, 'folga', 6), (6, 'partidinha', 8)]

WOOD = hexc('#8a5a34'); WOODD = hexc('#5e3c22')
SAIL = hexc('#c0703f'); SAILD = hexc('#8e4c26')
IVORY = hexc('#f4ecd8'); IVORYD = hexc('#cfc3a6')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


# ------------------------------------------------------------------ desenhos novos
def dado(face=5, glow=0):
    """dado de osso visto meio de cima. 300x300, base y~290."""
    p = Pen(300, 300)
    top = [(60, 90), (170, 50), (250, 95), (140, 135)]
    p.shape([(60, 90), (140, 135), (140, 280), (60, 235)], IVORYD, None, 6)
    p.shape([(140, 135), (250, 95), (250, 240), (140, 280)], mul(IVORY, .92), IVORYD, 6, 8)
    p.shape(top, IVORY, None, 6)
    pts = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
           5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}[face]
    for a, b in pts:
        x = 195 + a * 30; y = 168 + b * 40 - a * 10
        p.dot(x, y, 10, hexc('#c0392b') if face == 1 else INK)
    for a, b in ((-1, -1), (1, 1)):
        p.dot(100 + a * 18, 185 + b * 30, 9, INK)
    if glow: p.stroke([(80, 80), (110, 66)], 6, (255, 255, 255))
    return fin(p)


def peca(seed=0):
    """pecinha retangular de jogo (antepassada do mahjong). 200x300, base y~290."""
    p = Pen(200, 300)
    p.shape([(30, 30), (170, 30), (170, 285), (30, 285)], IVORY, IVORYD, 6, 10)
    r = random.Random(seed)
    for i in range(1 + seed % 4):
        p.dot(100 + (i % 2) * 34 - 17 * (seed % 4 > 0), 80 + i * 52, 13, hexc('#c0392b') if (i + seed) % 2 else INK)
    p.stroke([(48, 50), (80, 50)], 5, (255, 255, 255))
    return fin(p)


def junco(wreck=0):
    """navio chinês (junco) de lado, proa à direita, velas de esteira. 900x800, linha d'água y~700."""
    p = Pen(900, 800)
    hull = [(30, 500), (180, 560), (760, 560), (880, 470), (820, 720), (110, 720)]
    p.shape(hull, mul(WOOD, .8) if wreck else WOOD, WOODD, 6, 16)
    p.shape([(30, 430), (200, 450), (200, 560), (30, 500)], hexc('#9d6a40'), WOODD, 5, 4)
    for x in range(150, 760, 80): p.stroke([(x, 590), (x + 50, 590)], 6, WOODD)
    p.stroke([(120, 650), (800, 650)], 5, WOODD)
    if wreck: return fin(p)
    for mx, top, w, hh in ((300, 120, 230, 400), (580, 60, 260, 470), (790, 260, 120, 230)):
        p.line([(mx, 560), (mx, top - 20)], hexc('#6b4426'), 16, 4)
        sail = [(mx - w * .55, top), (mx + w * .45, top + 10), (mx + w * .5, top + hh), (mx - w * .5, top + hh)]
        p.shape(sail, SAIL, SAILD, 5, 14)
        for k in range(1, 6):
            y = top + hh * k / 6
            p.stroke([(mx - w * .53, y), (mx + w * .48, y + 4)], 5, SAILD)
    p.poly([(580, 40), (580, 0), (640, 18)], hexc('#d8443c'), 3)
    return fin(p)


def faca():
    p = Pen(500, 200)
    p.shape([(40, 90), (300, 70), (330, 100), (300, 120), (40, 110)], hexc('#b9c0c8'), hexc('#8a929c'), 5, 6)
    p.shape([(320, 85), (470, 85), (470, 120), (320, 120)], WOOD, WOODD, 5, 4)
    return fin(p)


def espinha():
    p = Pen(500, 240)
    p.stroke([(60, 120), (400, 120)], 9, IVORY)
    for x in range(110, 380, 45):
        p.stroke([(x, 120), (x - 20, 60)], 6, IVORY); p.stroke([(x, 120), (x - 20, 180)], 6, IVORY)
    p.shape([(400, 70), (470, 120), (400, 170)], IVORY, IVORYD, 5, 4)
    p.shape([(20, 80), (70, 120), (20, 160)], IVORY, IVORYD, 5, 4)
    p.dot(430, 112, 8, INK)
    return fin(p)


def raio(seed=0):
    p = Pen(300, 700)
    r = random.Random(seed); pts = [(150, 0)]
    for i in range(1, 8): pts.append((150 + (r.random() - .5) * 160, i * 95))
    p.line(pts, hexc('#fff6a8'), 16, 4)
    return fin(p)


@lru_cache(maxsize=2)
def mar_bg(storm=1):
    from PIL import ImageDraw
    top, sky, cl, sea, wave = (('#2b3550', '#3b4566', '#55607f', '#24507a', '#5f8fbf') if storm else
                               ('#7cc4ee', '#bfe5f7', '#ffffff', '#2f7fb8', '#7fb8e0'))
    c = Image.new('RGBA', (BW, BH), hexc(top) + (255,)); d = ImageDraw.Draw(c)
    d.rectangle([0, 0, BW, 1050], fill=hexc(sky))
    rnd = random.Random(3)
    for i in range(7):
        cx = rnd.random() * BW; cy = 150 + rnd.random() * 500
        for j in range(4):
            rx = 120 + rnd.random() * 90
            d.ellipse([cx + (j - 2) * 110 - rx, cy - rx * .5, cx + (j - 2) * 110 + rx, cy + rx * .45], fill=hexc(cl), outline=INK, width=4)
    d.rectangle([0, 1050, BW, BH], fill=hexc(sea))
    for y in range(1080, 2200, 80):
        for x in range(-40 + (y // 80 % 2) * 90, BW, 180):
            d.line([(x, y), (x + 45, y - 22), (x + 90, y)], fill=hexc(wave), width=7)
    return c


@lru_cache(maxsize=2)
def convés(light='golden'):
    """convés de madeira do navio ao entardecer: céu, mar ao fundo, amurada e tábuas."""
    from PIL import ImageDraw
    L = art.LIGHTS[light]
    c = Image.new('RGBA', (BW, BH), hexc(L['top']) + (255,)); d = ImageDraw.Draw(c)
    d.rectangle([0, 600, BW, 1000], fill=hexc(L['hor']))
    d.rectangle([0, 1000, BW, 1150], fill=hexc('#2f6f9f'))
    d.rectangle([0, 1100, BW, 1200], fill=mul(WOOD, .9), outline=INK, width=5)
    for x in range(40, BW, 150): d.rectangle([x, 1020, x + 26, 1110], fill=WOODD, outline=INK, width=4)
    d.rectangle([0, 1005, BW, 1035], fill=WOOD, outline=INK, width=5)
    d.rectangle([0, 1200, BW, BH], fill=WOOD)
    for y in range(1200, BH, 70): d.line([(0, y), (BW, y)], fill=WOODD, width=5)
    rnd = random.Random(2)
    for y in range(1200, BH, 70):
        for k in range(3):
            x = rnd.random() * BW; d.line([(x, y), (x, y + 70)], fill=WOODD, width=4)
    d.line([(980, 0), (980, 1100)], fill=hexc('#6b4426'), width=30)
    d.polygon([(800, 80), (1242, 60), (1242, 760), (800, 780)], fill=SAIL, outline=INK)
    for k in range(1, 7): d.line([(800, 80 + k * 100), (1242, 60 + k * 100)], fill=SAILD, width=7)
    return c


def put_img(c, fn, x, feet, h, aspect, flip=False, **kw):
    put_sprite(c, fn, x, feet, h, aspect, flip, {}, **kw)


def ship_rot(c, x, y, h, ang, flip=False, wreck=0):
    im = sprite('junco', (('wreck', wreck),), int(h), 900 / 800, flip)
    im = im.rotate(ang, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def peixe(c, x, y, f, s=1.0, flip=False):
    from PIL import ImageDraw
    d = ImageDraw.Draw(c); w = 60 * s; t = 10 * math.sin(f * .3)
    dirn = -1 if flip else 1
    d.ellipse([x - w, y - w * .45, x + w, y + w * .45], fill=hexc('#f2a541'), outline=INK, width=4)
    d.polygon([(x - dirn * w, y), (x - dirn * (w + 40 * s), y - 30 * s + t), (x - dirn * (w + 40 * s), y + 30 * s + t)], fill=hexc('#e08a2a'), outline=INK)
    d.ellipse([x + dirn * w * .5 - 9, y - 14, x + dirn * w * .5 + 9, y + 4], fill=(255, 255, 255), outline=INK, width=3)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('fundo_mar', 'day').copy()
    for i, (x, y) in enumerate(((200, 700), (1050, 900), (400, 1100))):
        peixe(c, (x + f * (3 if i % 2 == 0 else -3)) % 1400 - 80, y + 20 * math.sin(f * .05 + i), f + i * 7, .9, i % 2 == 1)
    d0 = wt(0, 'dados') - 3
    for i, (x, fc) in enumerate(((470, 5), (680, 3), (860, 1))):
        s = back(ramp(f, d0 + i * 3, d0 + i * 3 + 8))
        if s > .05:
            im = sprite('dado', (('face', fc), ('glow', 1)), int(230 * s), 1, False)
            paste_c(c, im, x, 1480 - 14 * math.sin(f * .08 + i))
    num(c, 'QUASE 750 ANOS', 640, 760, f, wt(0, 'setecentos') - 3, 110, -4)
    num(c, 'NO FUNDO DO MAR', 640, 920, f, wt(0, 'fundo') - 3, 80, 3)
    z = lerp(1.45, 1.12, easeOut(ramp(f, 0, 50))) * (1 + .0005 * f)
    k = kick(f, d0)
    return c, (640, 1300 + k * 10, z, k), 'day'


def s1(f):
    c = mar_bg(0).copy()
    for i, (x, y, h) in enumerate(((240, 1260, 360), (980, 1240, 340), (620, 1380, 520), (120, 1560, 600), (1060, 1600, 640))):
        bob = 12 * math.sin(f * .08 + i)
        paste_c(c, sprite('junco', (('wreck', 0),), h, 900 / 800, False), x + f * 1.5, y + bob)
    s0_ = wt(1, 'soldados') if False else wt(1, 'frota') - 3
    num(c, 'FROTA DE KUBLAI KHAN', 640, 640, f, s0_, 72, -3)
    num(c, 'NETO DE GENGIS KHAN', 640, 760, f, wt(1, 'neto') - 3, 64, 3)
    num(c, '1281', 640, 930, f, wt(1, 'mil') - 3, 200, -5)
    num(c, 'INVASÃO DO JAPÃO', 640, 1080, f, wt(1, 'invadir') - 3, 72, 4)
    t = smooth(ramp(f, 0, 90))
    k = kick(f, wt(1, 'mil') - 3, .7)
    return c, (640 + 30 * math.sin(f * .02), lerp(1350, 1250, t) + k * 8, lerp(1.2, 1.08, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = mar_bg(1).copy()
    t0 = wt(2, 'tufao') - 3
    if f >= t0 and (f - t0) % 22 < 5:
        paste_c(c, sprite('raio', (('seed', (f - t0) // 22 % 3),), 600, 300 / 700, False), 300 + 500 * (((f - t0) // 22) % 2), 500)
    for i, (x, y, h) in enumerate(((300, 1300, 460), (900, 1340, 500), (620, 1560, 620))):
        sink = clamp((f - t0 - 10 - i * 12) / 60) if f >= t0 else 0
        ang = 6 * math.sin(f * .15 + i) + sink * (40 if i % 2 else -40)
        ship_rot(c, x, y + sink * 260, h, ang)
    num(c, 'TUFÃO!', 640, 720, f, t0, 170, -6)
    num(c, 'TAKASHIMA, NAGASAKI', 640, 900, f, wt(2, 'takashima') - 3, 70, 3)
    k = kick(f, t0, 1.2)
    return c, (640 + 14 * math.sin(f * .2) * (f >= t0), 1250 + k * 12, 1.12 + .0008 * f, k + 3 * math.sin(f * .07)), 'dusk'


def s3(f):
    c = CEN('museu', 'day').copy()
    put_sci(c, 330, 1700, 900, f, 2, arms='point' if f >= wt(3, 'cinco') - 3 else 'clip', expr='grin' if f >= wt(3, 'mahjong') - 3 else 'neutral', skin=2, look=1, glasses=True)
    d0 = wt(3, 'cinco') - 3
    for i in range(5):
        s = back(ramp(f, d0 + i * 2, d0 + i * 2 + 8))
        if s > .05: paste_c(c, sprite('dado', (('face', i + 1), ('glow', 0)), int(120 * s), 1, False), 640 + i * 110, 1180)
    p0 = wt(3, 'vinte') - 3
    for i in range(10):
        s = back(ramp(f, p0 + i, p0 + i + 8))
        if s > .05: paste_c(c, sprite('peca', (('seed', i),), int(130 * s), 200 / 300, False), 640 + (i % 5) * 110, 1370 + (i // 5) * 150)
    num(c, '5 DADOS', 880, 560, f, d0, 110, -4)
    num(c, '29 PEÇAS', 880, 720, f, p0, 110, 4)
    num(c, 'MAHJONG?', 880, 900, f, wt(3, 'mahjong') - 3, 100, -3)
    t = smooth(ramp(f, 0, 100))
    return c, (700, lerp(1250, 1150, t), lerp(1.08, 1.18, t) * (1 + .0006 * f), 0), 'day'


def s4(f):
    c = CEN('fundo_mar', 'day').copy()
    peixe(c, (200 + f * 3) % 1400 - 80, 700, f, .8)
    ship_rot(c, 640, 1500, 700, 0, wreck=1)
    p0 = wt(4, 'primeira') - 3
    num(c, '1ª VEZ!', 640, 820, f, p0, 150, -5)
    m0 = wt(4, 'trinta') - 3
    if f >= m0:
        from PIL import ImageDraw
        s = clamp((f - m0) / 10); d = ImageDraw.Draw(c)
        x0, x1 = 640 - 440 * s, 640 + 440 * s
        d.line([(x0, 1650), (x1, 1650)], fill=(255, 255, 255), width=10)
        for x in (x0, x1): d.line([(x, 1610), (x, 1690)], fill=(255, 255, 255), width=10)
    num(c, '~30 METROS', 640, 1000, f, m0, 130, 3)
    for i in range(3):
        s = back(ramp(f, p0 + 4 + i * 3, p0 + 12 + i * 3))
        if s > .05: paste_c(c, sprite('dado', (('face', 6 - i), ('glow', 1)), int(110 * s), 1, False), 520 + i * 120, 1420)
    t = smooth(ramp(f, 0, 120))
    k = kick(f, p0, .6)
    return c, (640 + 15 * math.sin(f * .03), lerp(1350, 1280, t) + k * 8, lerp(1.25, 1.08, t) * (1 + .0009 * f), k), 'day'


def s5(f):
    c = convés('golden').copy()
    k0 = wt(5, 'faca') - 3; e0 = wt(5, 'espinhas') - 3; j0 = wt(5, 'jogassem') - 3
    put_soldier(c, 300, 1800, 820, f, 3, arms='point' if f >= j0 else 'hang', expr='grin' if f >= j0 else 'neutral', mous=True, skin=1)
    put_soldier(c, 960, 1820, 820, f, 5, arms='thumb' if f >= j0 else 'hang', expr='smug' if f >= j0 else 'neutral', skin=3)
    if f >= k0: paste_c(c, sprite('faca', (), 200, 500 / 200, False), 420, 950, back(ramp(f, k0, k0 + 8)))
    if f >= e0: paste_c(c, sprite('espinha', (), 230, 500 / 240, False), 850, 950, back(ramp(f, e0, e0 + 8)))
    if f >= j0:
        for i, fc in enumerate((4, 2)):
            ang = (f - j0) * 25 * (1 - clamp((f - j0) / 20))
            im = sprite('dado', (('face', fc), ('glow', 0)), 130, 1, False).rotate(ang, expand=True)
            paste_c(c, im, 580 + i * 140, 1560 - 120 * abs(math.sin(clamp((f - j0) / 20) * math.pi)))
    num(c, 'HORA DA FOLGA?', 640, 820, f, wt(5, 'folga') - 3, 100, -4)
    t = smooth(ramp(f, 0, 120))
    return c, (640, lerp(1100, 1300, t), lerp(1.2, 1.06, t) * (1 + .0004 * f), 0), 'golden'


def s6(f):
    c = convés('dusk').copy()
    p0 = wt(6, 'partidinha') - 3
    put_soldier(c, 300, 1800, 820, f, 3, arms='salute' if f >= p0 else 'cheek', expr='grin' if f >= p0 else 'neutral', mous=True, skin=1)
    put_soldier(c, 960, 1820, 820, f, 5, arms='shrug', expr='shock' if f >= p0 else 'nervous', skin=3)
    for i, fc in enumerate((6, 6)):
        paste_c(c, sprite('dado', (('face', fc), ('glow', 0)), 140, 1, False), 570 + i * 150, 1560)
    for i in range(4): paste_c(c, sprite('peca', (('seed', i + 3),), 120, 200 / 300, False), 470 + i * 100, 1720)
    num(c, 'INVASÃO?', 640, 660, f, wt(6, 'invasao') - 3, 110, -4)
    num(c, 'PARTIDINHA!', 640, 840, f, p0, 115, 4)
    z = lerp(1.0, 1.15, easeOut(ramp(f, 0, 60))) * (1 + .0005 * max(0, f - 60))
    return c, (640, 1300, z, lerp(0, -2.5, smooth(ramp(f, 0, 60))) - .01 * max(0, f - 60)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'dados') - 3, 160, .8)
    s.ting(s.W(0, 'setecentos') - 3, .3)
    s.thunk(s.W(1, 'mil') - 3, 140, .9)
    s.whoosh(s.W(2, 'tufao') - 3, .4, .6)
    s.splash(s.W(2, 'navios') - 2, .5)
    s.thunk(s.W(3, 'cinco') - 3, 220, .5)
    s.patter(s.W(3, 'vinte') - 3, s.W(3, 'vinte') + 14, 6, .14)
    s.ting(s.W(3, 'mahjong') - 3, .35)
    s.thunk(s.W(4, 'primeira') - 3, 140, .8)
    s.thunk(s.W(5, 'faca') - 3, 220, .5)
    s.patter(s.W(5, 'jogassem') - 3, s.W(5, 'jogassem') + 18, 5, .2)
    s.thunk(s.W(6, 'partidinha') - 3, 120, 1.0)
