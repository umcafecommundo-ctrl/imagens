"""Um Café com o Mundo — CURIOSIDADE (quarta 11/11/2026, 17h).
Tema: pela 1ª vez astrônomos veem as passagens (trânsitos) de um planeta sumirem: TOI-2535 b.
Fontes (conferidas em 11/11/2026):
- UCLA / EurekAlert, 09/11/2026 "First known 'disappearing planet' has a neighbor that makes it wobble like a top":
  TOI-2535 b, Júpiter quente a ~1.000 anos-luz; órbita de 8,25 dias; TESS (NASA) observou de abr/2019 a mar/2026;
  trânsitos adiantavam/atrasavam até 6 h, ficaram mais curtos e rasos e pararam de aparecer em 2026; causa: um
  planeta vizinho ainda não visto, de órbita inclinada, faz as órbitas balançarem e tira o planeta da nossa linha
  de visão; próximo trânsito esperado em 30 a 50 anos; telescópio WIYN 3,5 m (Kitt Peak); Astrophysical Journal
  Letters; Samuel Yee e Erik Petigura (UCLA).
- Sci.News, 10/11/2026: 1º planeta confirmado ao redor de uma única estrela cujos trânsitos foram vistos sumir;
  estrela anã laranja (tipo K) antiga, constelação do Corvo; trajeto foi do meio do disco para a beirada (rasante)
  e sumiu; vizinho proposto (massa de Saturno ou mais) ainda não confirmado.
Planetas, estrela e telescópio genéricos; sem logotipos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Pela primeira vez, astrônomos viram um planeta gigante simplesmente sumir da frente da sua estrela.",
    "Ele é um Júpiter quente, a uns mil anos-luz daqui, e dá uma volta na estrela em pouco mais de oito dias.",
    "Desde dois mil e dezenove, o telescópio TESS, da NASA, via a estrela escurecer um pouquinho a cada passagem.",
    "Mas, ano após ano, ele passava mais pela beirada, até que, em dois mil e vinte e seis, as passagens pararam.",
    "O motivo? Um planeta vizinho, que ninguém viu ainda, deve estar puxando e inclinando a órbita dele, como um pião que balança.",
    "O planeta continua lá. Só não passa mais na nossa frente.",
    "E a próxima passagem só deve acontecer daqui a trinta a cinquenta anos. Então, anota na agenda.",
]
CAPTXT = [
    "Pela primeira vez, astrônomos viram um planeta gigante|simplesmente sumir da frente da sua estrela.",
    "Ele é um Júpiter quente, a uns 1.000 anos-luz daqui,|e dá uma volta na estrela em pouco mais de 8 dias.",
    "Desde 2019, o telescópio TESS, da NASA, via a estrela|escurecer um pouquinho a cada passagem.",
    "Mas, ano após ano, ele passava mais pela beirada,|até que, em 2026, as passagens pararam.",
    "O motivo? Um planeta vizinho, que ninguém viu ainda,|deve estar puxando e inclinando a órbita dele,|como um pião que balança.",
    "O planeta continua lá.|Só não passa mais na nossa frente.",
    "E a próxima passagem só deve acontecer|daqui a 30 a 50 anos. Então, anota na agenda.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'sumir', 4), (1, 'mil', 4), (1, 'oito', 4), (2, 'tess', 4), (2, 'escurecer', 6), (3, 'beirada', 6),
         (3, 'pararam', 6), (4, 'vizinho', 4), (4, 'piao', 6), (5, 'continua', 4), (6, 'trinta', 4), (6, 'agenda', 6)]

WHITE = (255, 255, 255)
GOLD = hexc('#e8b440'); GOLD_D = hexc('#b8862a')
BLUE = hexc('#4f8fe0'); BLUE_D = hexc('#2f63a8')
PANEL = hexc('#2b3f7a'); PANEL_D = hexc('#1c2a55')
RED = hexc('#d8443c')
MARS = hexc('#d9653a'); MARS_D = hexc('#a8452a')
SUN = hexc('#f7c948'); SUN_D = hexc('#e09a2a')


# ------------------------------------------------------------------ desenhos novos
def sonda(cor='gold', look=1.0, blink=0, expr='calm', fire=0.0):
    """sonda genérica de lado, olhando para a direita: corpo-caixa com olho grande, 2 painéis solares, bocal atrás.
    800x480, centro em (400, 240)."""
    p = Pen(800, 480)
    C, CD = (GOLD, GOLD_D) if cor == 'gold' else (BLUE, BLUE_D)
    # chama do motor (à esquerda)
    if fire > 0:
        for i, (col, s) in enumerate(((hexc('#f7d046'), 1.0), (hexc('#f08a2c'), .7), (hexc('#fff3c0'), .4))):
            L = 230 * fire * s
            p.poly([(270, 240 - 50 * s), (270, 240 + 50 * s), (270 - L * .6, 240 + 22 * s), (270 - L, 240), (270 - L * .6, 240 - 22 * s)], col, 0 if i else 4)
    # bocal
    p.shape([(300, 200), (300, 280), (255, 300), (255, 180)], hexc('#8a8f99'), hexc('#6b6b70'), 5, 6)
    # painéis solares (cima e baixo)
    for s in (-1, 1):
        y0, y1 = (240 + s * 120, 240 + s * 225)
        p.line([(400, 240 + s * 95), (400, y0)], hexc('#8a8f99'), 14, 4)
        p.shape([(300, min(y0, y1)), (500, min(y0, y1)), (500, max(y0, y1)), (300, max(y0, y1))], PANEL, PANEL_D, 5, 8)
        for gx in (350, 400, 450): p.stroke([(gx, min(y0, y1) + 6), (gx, max(y0, y1) - 6)], 3, hexc('#6f88c8'))
        p.stroke([(306, (y0 + y1) / 2), (494, (y0 + y1) / 2)], 3, hexc('#6f88c8'))
    # corpo
    p.shape([(300, 140), (520, 140), (540, 160), (540, 330), (520, 345), (300, 345)], C, CD, 6, 16)
    # antena prato na frente
    p.line([(540, 200), (600, 180)], hexc('#6b6b70'), 8, 4)
    p.shape(ell_pts(612, 176, 22, 46, 30, .3), hexc('#f2f4f8'), hexc('#c9ced8'), 5, 6)
    # olho
    ex, ey, er = 440, 238, 64 if expr == 'shock' else 58
    p.dot(ex, ey, er, WHITE, 5)
    L = max(.45 if expr in ('proud', 'sleep') else 0, blink, .7 if expr == 'sleep' else 0)
    if L < .75:
        lk = max(-1, min(1, look))
        p.dot(ex + lk * (er - 24), ey + 4, 16 if expr == 'shock' else 22, INK)
        p.dot(ex + lk * (er - 24) - 6, ey - 4, 6, WHITE)
    if L > .02:
        top = ey - er; yb = top + 2 * er * L
        p.poly([(ex - er - 1, top - 2), (ex + er + 1, top - 2), (ex + er + 1, yb), (ex - er - 1, yb)], C)
        p.stroke([(ex - er, yb), (ex + er, yb)], 5)
    if expr == 'shock': p.arc(ex, ey - 84, 30, 10, 200, 340, 5)
    if expr == 'proud': p.arc(ex, ey + 92, 24, 12, 20, 160, 5)
    return p.img


def put_sonda(c, x, y, w, rot=0, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    if 'fire' in kw: kw['fire'] = round(kw['fire'] * 6) / 6
    if 'look' in kw: kw['look'] = round(kw['look'] * 4) / 4
    if w < 8: return
    im = sprite('sonda', tuple(sorted(kw.items())), int(w * 480 / 800), 800 / 480, flip)
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def planeta(c, x, y, r, col, cold, ring=None):
    p = Pen(int(2 * r + 40), int(2 * r + 40))
    q = r + 20
    if ring: p.poly(ell_pts(q, q, r + 16, r + 16, 60), ring)
    p.shape(ell_pts(q, q, r, r, 60), col, cold, max(4, int(r / 25)), max(6, int(r / 8)))
    if col == hexc('#3a7fd0'):
        for lx, ly, rx, ry in ((-.35, -.2, .35, .22), (.3, .25, .3, .2), (.1, -.5, .2, .1)):
            p.shape(ell_pts(q + lx * r, q + ly * r, rx * r, ry * r, 30, .2), hexc('#7fb05a'), hexc('#5f8a40'), max(3, int(r / 40)), 4)
    if col == MARS:
        for lx, ly, rr in ((-.3, -.2, .14), (.35, .2, .1), (0, .45, .12), (.2, -.45, .08)):
            p.dot(q + lx * r, q + ly * r, rr * r, MARS_D)
        p.shape(ell_pts(q, q - r * .86, r * .32, r * .1, 30), WHITE, None, 0, 0)
    paste_c(c, p.img.resize((int(2 * r + 40), int(2 * r + 40)), Image.LANCZOS), x, y)


def sol(c, x, y, r, f):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(12):
        a = i * math.pi / 6 + f * .01
        r1, r2 = r + 20, r + 60 + 10 * math.sin(f * .2 + i)
        d.line([(x + r1 * math.cos(a), y + r1 * math.sin(a)), (x + r2 * math.cos(a), y + r2 * math.sin(a))], fill=SUN + (255,), width=16)
    planeta(c, x, y, r, SUN, SUN_D, (255, 230, 140))


@lru_cache(maxsize=2)
def ceu_bg(seed=11):
    base = Image.new('RGBA', (BW, BH), hexc('#0e1436') + (255,))
    p = Pen(BW, BH)
    rnd = random.Random(seed)
    for i in range(200):
        p.dot(rnd.randint(0, BW), rnd.randint(0, BH), rnd.choice((2, 2, 3, 4)), (255, 255, 230))
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


@lru_cache(maxsize=2)
def terra_bg():
    """espaço com a Terra grande embaixo."""
    p = Pen(BW, BH)
    base = ceu_bg(7).copy()
    cx, cy, R = 621, 3300, 1650
    p.poly(ell_pts(cx, cy, R + 40, R + 40, 160), hexc('#7fc3ff'))
    p.shape(ell_pts(cx, cy, R, R, 160), hexc('#3a7fd0'), hexc('#2a5fa4'), 7, 40)
    for lx, ly, rx, ry in ((300, 1760, 260, 120), (880, 1820, 220, 150), (620, 2000, 300, 140)):
        p.shape(ell_pts(lx, ly, rx, ry, 40, .2), hexc('#7fb05a'), hexc('#5f8a40'), 5, 12)
    for wx, wy in ((150, 1900), (520, 1700), (1050, 1950)):
        p.shape(ell_pts(wx, wy, 120, 34, 30), WHITE, hexc('#dfe6ef'), 0, 6)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def trilha(c, pts, upto, col=(255, 255, 255, 170), w=6):
    n = max(2, int(len(pts) * clamp(upto)))
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(0, n - 1, 2):
        d.line([pts[i], pts[i + 1]], fill=col, width=w)


def ang(a, b):
    return -math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))



STAR = hexc('#f59a3c'); STAR_D = hexc('#cf6f27')
JUP = hexc('#e6b47c'); JUP_D = hexc('#b9824e'); BAND = hexc('#c98a54')
GHOST = hexc('#3a3f63'); GHOST_D = hexc('#262a47')


def jup(look=1.0, blink=0, expr='calm'):
    """Júpiter quente com olho grande: 600x600, centro (300, 300)."""
    p = Pen(600, 600)
    R = 250
    p.shape(ell_pts(300, 300, R, R, 72), JUP, JUP_D, 6, 30)
    for yy in (160, 235, 360, 440):
        rx = math.sqrt(max(0, R * R - (yy - 300) ** 2)) * .9
        p.poly(ell_pts(300, yy, rx, 20, 40), BAND)
    p.shape(ell_pts(190, 400, 46, 24, 30), hexc('#d4703a'), None, 0, 0)
    ex, ey, er = 330, 250, (96 if expr == 'shock' else 86)
    if expr == 'sleep':
        p.arc(ex, ey, 56, 26, 20, 160, 8)
        p.arc(320, 410, 26, 10, 20, 160, 6)
        return p.img
    p.dot(ex, ey, er, WHITE, 6)
    L = max(.45 if expr in ('proud', 'smug') else 0, blink, .8 if expr == 'sleep' else 0)
    if L < .75:
        lk = max(-1, min(1, look))
        p.dot(ex + lk * (er - 32), ey + 6, 22 if expr == 'shock' else 30, INK)
        p.dot(ex + lk * (er - 32) - 8, ey - 4, 9, WHITE)
    if L > .02:
        top = ey - er; yb = top + 2 * er * L
        p.poly([(ex - er - 1, top - 2), (ex + er + 1, top - 2), (ex + er + 1, yb), (ex - er - 1, yb)], JUP)
        p.stroke([(ex - er, yb), (ex + er, yb)], 6)
    if expr == 'shock':
        p.arc(ex, ey - 120, 40, 12, 200, 340, 6)
        p.dot(320, 420, 30, INK)
    elif expr in ('proud', 'smug'):
        p.arc(320, 400, 50, 22, 20, 160, 7)
    elif expr == 'sleep':
        p.arc(320, 410, 26, 10, 20, 160, 6)
    else:
        p.arc(320, 405, 36, 14, 20, 160, 6)
    return p.img


def put_jup(c, x, y, w, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    if 'look' in kw: kw['look'] = round(kw['look'] * 4) / 4
    if w < 8: return
    paste_c(c, sprite('jup', tuple(sorted(kw.items())), int(w), 1.0, flip), x, y)


def estrela(c, x, y, r, f):
    d = ImageDraw.Draw(c, 'RGBA')
    for i, a in enumerate((40, 28, 18)):
        rr = r * (1.18 + .14 * i) + 6 * math.sin(f * .12 + i)
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(255, 190, 110, a))
    planeta(c, x, y, r, STAR, STAR_D, (255, 205, 130))


def vizinho(c, x, y, r, f):
    d = ImageDraw.Draw(c, 'RGBA')
    p = Pen(int(2 * r + 40), int(2 * r + 40)); q = r + 20
    p.shape(ell_pts(q, q, r, r, 50), GHOST, GHOST_D, max(4, int(r / 20)), max(6, int(r / 8)))
    paste_c(c, p.img, x, y)
    paste_c(c, txt('?', int(r * 1.2), 6 * math.sin(f * .1)), x, y)


def elipse_rot(cx, cy, rx, ry, rot, n=80):
    a = math.radians(rot); out = []
    for i in range(n + 1):
        t = i / n * 2 * math.pi
        px, py = rx * math.cos(t), ry * math.sin(t)
        out.append((cx + px * math.cos(a) - py * math.sin(a), cy + px * math.sin(a) + py * math.cos(a)))
    return out


def orbita_pos(cx, cy, rx, ry, rot, t):
    a = math.radians(rot)
    px, py = rx * math.cos(t), ry * math.sin(t)
    return cx + px * math.cos(a) - py * math.sin(a), cy + px * math.sin(a) + py * math.cos(a)


def piao(c, x, y, h, f, s=1.0):
    p = Pen(400, 500)
    p.line([(200, 20), (200, 110)], hexc('#8a5a3a'), 18, 5)
    p.shape([(60, 150), (340, 150), (200, 470)], hexc('#d8443c'), hexc('#a8302a'), 6, 14)
    p.shape(ell_pts(200, 150, 140, 44, 40), hexc('#f2c14e'), hexc('#c99a30'), 6, 6)
    for k in (-1, 1): p.stroke([(200 + 80 * k, 190), (200 + 25 * k, 400)], 6, WHITE)
    im = p.img.resize((int(h * .8 * s) or 1, int(h * s) or 1), Image.LANCZOS).rotate(14 * math.sin(f * .25), resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def curva(c, x0, y0, w, h, prog, dips, depth=60):
    d = ImageDraw.Draw(c, 'RGBA')
    d.rounded_rectangle([x0 - 20, y0 - 20, x0 + w + 20, y0 + h + 20], 30, fill=(250, 250, 255, 235), outline=INK + (255,), width=8)
    pts = []
    n = 160
    for i in range(int(n * clamp(prog)) + 1):
        u = i / n
        yy = y0 + h * .35
        for dc in dips:
            if abs(u - dc) < .035: yy += depth * (1 - (abs(u - dc) / .035) ** 2)
        pts.append((x0 + w * u, yy))
    if len(pts) > 1: d.line(pts, fill=hexc('#2f63a8') + (255,), width=10)


# ------------------------------------------------------------------ cenas
def s0(f):
    # gancho: planeta passa na frente da estrela e some
    c = ceu_bg(11).copy()
    estrela(c, 640, 1000, 330, f)
    s0_ = wt(0, 'sumir') - 3
    p0 = wt(0, 'primeira') - 3
    x = lerp(150, 700, smooth(ramp(f, 0, s0_)))
    sc = 1 - ramp(f, s0_, s0_ + 7)
    if sc > 0:
        put_jup(c, x, 960 + 12 * math.sin(f * .15), 360 * sc, look=-1 if f < s0_ - 25 else 1,
                blink=blinkAt(f, 3), expr='shock' if f >= s0_ - 18 else 'calm')
    if f >= s0_: put_dust(c, x, 960, 170, f - s0_, 16)
    num(c, '1ª VEZ!', 640, 380, f, p0, 150, -5)
    num(c, 'SUMIU!', 640, 1450, f, s0_, 160, 4)
    z = lerp(1.3, 1.0, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, s0_)
    return c, (640 + 10 * math.sin(f * .05), 1000 + k * 10, z, k), 'day'


def s1(f):
    # estrela laranja com o planeta girando rápido em volta
    c = ceu_bg(3).copy()
    cx, cy = 640, 1000
    a = f * .09
    x, y = orbita_pos(cx, cy, 430, 150, -6, a)
    d = ImageDraw.Draw(c, 'RGBA')
    d.line(elipse_rot(cx, cy, 430, 150, -6), fill=(255, 255, 255, 90), width=5)
    atras = math.sin(a) < 0
    if atras: put_jup(c, x, y, 190, math.cos(a) > 0, look=1, blink=blinkAt(f, 4), expr='proud')
    estrela(c, cx, cy, 170, f)
    if not atras: put_jup(c, x, y, 230, math.cos(a) > 0, look=1, blink=blinkAt(f, 4), expr='proud')
    num(c, 'JÚPITER QUENTE', 640, 380, f, wt(1, 'jupiter') - 3, 105, -3)
    num(c, '1.000 ANOS-LUZ', 640, 540, f, wt(1, 'mil') - 3, 100, 3)
    num(c, '8 DIAS POR VOLTA', 640, 1440, f, wt(1, 'oito') - 3, 92, -3)
    num(c, 'TOI-2535 b', 640, 1290, f, 6, 64, 0)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 150)))
    return c, (640, 1000, z, lerp(-1, 2, smooth(ramp(f, 0, 150)))), 'day'


def s2(f):
    # telescópio TESS olhando a estrela; gráfico do brilho com quedas
    c = ceu_bg(9).copy()
    t0 = wt(2, 'tess') - 3
    e0 = wt(2, 'escurecer') - 3
    sx, sy = 930, 720
    estrela(c, sx, sy, 150, f)
    per = 70
    u = (f % per) / per
    put_jup(c, lerp(sx - 260, sx + 260, u), sy + 10, 120, look=1, blink=blinkAt(f, 6))
    if f >= t0:
        s = back(ramp(f, t0, t0 + 8))
        put_sonda(c, 280, 720 + 10 * math.sin(f * .1), 420 * s, 0, cor='gold', look=1, blink=blinkAt(f, 2),
                  expr='shock' if f >= e0 else 'calm')
    num(c, 'TESS · NASA', 350, 470, f, t0, 80, -3)
    num(c, '2019', 640, 360, f, wt(2, 'dezenove') - 3, 120, 3)
    prog = ramp(f, t0, e0 + 60)
    curva(c, 170, 1060, 900, 300, prog, (.2, .45, .7, .95), 90)
    num(c, 'BRILHO DA ESTRELA', 640, 1010, f, t0, 56, 0)
    if f >= e0:
        d = ImageDraw.Draw(c, 'RGBA')
        s = back(ramp(f, e0, e0 + 8))
        for dc in (.2, .45):
            xx = 170 + 900 * dc
            d.ellipse([xx - 50 * s, 1230 - 50 * s, xx + 50 * s, 1230 + 50 * s], outline=hexc('#d8443c') + (255,), width=9)
    num(c, 'ESCURECE!', 640, 1490, f, e0, 110, -3)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 120)))
    k = kick(f, e0, .6)
    return c, (640 + 20 * math.sin(f * .03), 1000 + k * 8, z, k), 'day'


def s3(f):
    # visto daqui: cada ano o planeta passa mais perto da beirada, até não passar mais
    c = ceu_bg(5).copy()
    cx, cy, R = 640, 980, 360
    estrela(c, cx, cy, R, f)
    b0 = wt(3, 'beirada') - 3
    p0 = wt(3, 'pararam') - 3
    anos = (('2019', 0.0), ('2022', .5), ('2024', .85), ('2026', 1.3))
    D = max(28, p0 / 4)
    kk = min(3, int(f // D))
    u = (f - kk * D) / D if kk < 3 else (f - 3 * D) / (D * 1.8)
    d = ImageDraw.Draw(c, 'RGBA')
    for k in range(kk):
        y = cy - anos[k][1] * R
        for xx in range(120, 1160, 60): d.line([(xx, y), (xx + 30, y)], fill=(255, 255, 255, 140), width=5)
        num(c, anos[k][0], 1080, y - 70, f, 0, 56, 0)
    y = cy - anos[kk][1] * R
    x = lerp(60, 1220, clamp(u, 0, 1.2) / 1.0)
    look = 1 if kk < 3 else -1
    put_jup(c, x, y, 170, look=1, blink=blinkAt(f, 5), expr='shock' if kk == 3 else 'calm')
    num(c, anos[kk][0], x, y - 140, f, kk * D, 80, 0)
    num(c, 'BEIRADA', 640, 1420, f, b0, 100, -3)
    num(c, 'PARARAM!', 640, 1420, f, p0, 140, 4) if f >= p0 else None
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 160)))
    k = kick(f, p0, .7)
    return c, (640, 960 + k * 8, z, k), 'golden'


def s4(f):
    # por quê: vizinho escondido puxa e inclina a órbita, como pião
    c = ceu_bg(13).copy()
    cx, cy = 600, 1080
    v0 = wt(4, 'vizinho') - 3
    i0 = wt(4, 'inclinando') - 3
    q0 = wt(4, 'piao') - 3
    rot = 18 * math.sin(max(0, f - i0) * .06) if f >= i0 else 0
    d = ImageDraw.Draw(c, 'RGBA')
    d.line(elipse_rot(cx, cy, 380, 120, rot), fill=(255, 255, 255, 110), width=5)
    a = f * .07
    x, y = orbita_pos(cx, cy, 380, 120, rot, a)
    atras = math.sin(a) < 0
    if atras: put_jup(c, x, y, 160, math.cos(a) > 0, look=1, blink=blinkAt(f, 8), expr='shock' if f >= i0 else 'calm')
    estrela(c, cx, cy, 120, f)
    if not atras: put_jup(c, x, y, 190, math.cos(a) > 0, look=1, blink=blinkAt(f, 8), expr='shock' if f >= i0 else 'calm')
    if f >= v0:
        s = back(ramp(f, v0, v0 + 8))
        vx, vy = 1030, 720
        vizinho(c, vx, vy, int(110 * s) + 1, f)
        if f >= i0:
            for k in range(6):
                tt = ((f * .04 + k / 6) % 1)
                px, py = lerp(vx, x, tt), lerp(vy, y, tt)
                d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=(200, 210, 255, 200))
    num(c, 'O MOTIVO?', 640, 330, f, 0, 100, -3)
    num(c, 'VIZINHO ESCONDIDO', 560, 460, f, v0, 80, 3)
    if f >= q0:
        s = back(ramp(f, q0, q0 + 8))
        piao(c, 1030, 1380, 230, f, s)
        num(c, 'PIÃO!', 780, 1430, f, q0, 110, -4)
    z = lerp(1.12, 1.0, smooth(ramp(f, 0, 120)))
    k = kick(f, v0, .6)
    return c, (640, 1000 + k * 8, z, k + lerp(0, 2, smooth(ramp(f, i0, i0 + 30)))), 'dusk'


def s5(f):
    # visão de lado: nosso telescópio olha a estrela, mas o planeta passa por cima
    c = ceu_bg(7).copy()
    c0 = wt(5, 'continua') - 3
    fr0 = wt(5, 'frente') - 3
    sx, sy = 880, 1050
    d = ImageDraw.Draw(c, 'RGBA')
    for xx in range(260, sx - 120, 50): d.line([(xx, sy), (xx + 25, sy)], fill=(255, 240, 160, 200), width=6)
    a = f * .06
    x, y = orbita_pos(sx, sy, 300, 90, -28, a)
    d.line(elipse_rot(sx, sy, 300, 90, -28), fill=(255, 255, 255, 100), width=5)
    atras = math.sin(a) < 0
    if atras: put_jup(c, x, y, 170, math.cos(a) > 0, look=-1, blink=blinkAt(f, 3), expr='smug' if f >= c0 else 'calm')
    estrela(c, sx, sy, 110, f)
    if not atras: put_jup(c, x, y, 200, math.cos(a) > 0, look=-1, blink=blinkAt(f, 3), expr='smug' if f >= c0 else 'calm')
    put_sonda(c, 190, sy + 8 * math.sin(f * .1), 300, 0, cor='gold', look=1, blink=blinkAt(f, 9),
              expr='shock' if f >= fr0 else 'calm')
    num(c, 'AINDA ESTÁ LÁ', 640, 420, f, c0, 105, -3)
    num(c, 'NOSSA VISTA', 420, 1180, f, 8, 52, 0)
    num(c, 'NÃO PASSA NA FRENTE', 640, 1450, f, fr0, 82, 3)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 120)))
    k = kick(f, fr0, .5)
    return c, (lerp(600, 680, smooth(ramp(f, 0, 120))), 1000 + k * 8, z, k), 'dusk'


def s6(f):
    # fim: 30 a 50 anos, planeta dormindo, calendário
    c = ceu_bg(15).copy()
    t0 = wt(6, 'trinta') - 3
    a0 = wt(6, 'agenda') - 3
    put_jup(c, 560, 1000 + 14 * math.sin(f * .08), 560, look=1, blink=blinkAt(f, 4),
            expr='sleep' if f >= t0 else 'calm')
    if f >= t0: zzz(c, 820, 700, f - t0)
    num(c, '30 A 50 ANOS', 600, 380, f, t0, 130, -4)
    if f >= a0:
        s = back(ramp(f, a0, a0 + 8))
        q = Pen(300, 300)
        q.shape([(20, 50), (280, 50), (280, 280), (20, 280)], WHITE, hexc('#d6dbe4'), 6, 8)
        q.shape([(20, 50), (280, 50), (280, 110), (20, 110)], RED, mul(RED, .75), 6, 0)
        for gx in (80, 220): q.line([(gx, 20), (gx, 80)], INK, 14, 0)
        paste_c(c, q.img.resize((240, 240), Image.LANCZOS), 1010, 1330, s)
        paste_c(c, txt('20??', 64, 0), 1010, 1360, s)
        num(c, 'ANOTA NA AGENDA!', 560, 1480, f, a0, 92, 3)
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 140)))
    k = kick(f, a0, .5)
    return c, (640, 1000 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.whoosh(s.W(0, 'pela') - 3, .4, .5)
    s.thunk(s.W(0, 'sumir') - 3, 140, .9)
    s.ting(s.W(1, 'mil') - 3, .3)
    s.ting(s.W(1, 'oito') - 3, .3)
    s.ting(s.W(2, 'tess') - 3, .3)
    s.thunk(s.W(2, 'escurecer') - 3, 160, .6)
    s.thunk(s.W(3, 'pararam') - 3, 150, .8)
    s.thunk(s.W(4, 'vizinho') - 3, 170, .7)
    s.ting(s.W(4, 'piao') - 3, .4)
    s.ting(s.W(5, 'continua') - 3, .3)
    s.thunk(s.W(6, 'trinta') - 3, 180, .6)
    s.ting(s.W(6, 'agenda') - 3, .4)
