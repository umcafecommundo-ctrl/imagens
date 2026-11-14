"""Um Café com o Mundo — CURIOSIDADE (sábado 14/11/2026, 12h).
Tema: telescópio espacial Euclid (ESA) divulga a 1ª grande leva de dados do seu mapa 3D do universo (DR1-Foundation).
Fontes (conferidas em 14/11/2026):
- ESA, 12/11/2026 "Euclid lays the foundation for its best-ever 3D map of the Universe": DR1-Foundation, ~13 meses
  de observação; mais de 1 bilhão de objetos; área igual a 9.500 luas cheias (1.900 graus quadrados; antes ~60);
  ~14% da área total que o Euclid vai mapear; ~1,7 milhão de GB; mais de 900 milhões de galáxias; ~15.000
  candidatas a lentes gravitacionais fortes; mais de 60 milhões de candidatos a quasar; espectros de mais de
  160 milhões de fontes; estuda matéria escura e energia escura; últimos 10 bilhões de anos; teia cósmica;
  DR1 completo em meados de 2027. Lançado em julho de 2023.
- Live Science / ESA (2024): matéria escura e energia escura somam cerca de 95% do universo.
- Phys.org e Starlust, 12-13/11/2026 (mesmos números).
Telescópio, galáxias e Lua genéricos; sem logotipos nem pessoas."""
from kit import *
import kit
from PIL import ImageChops

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um telescópio espacial acabou de catalogar mais de novecentos milhões de galáxias. E é só o começo.",
    "É o Euclid, da Agência Espacial Europeia: em treze meses, ele fotografou um pedaço do céu igual a nove mil e quinhentas luas cheias.",
    "No pacote, tem mais de um bilhão de objetos e quinze mil lentes gravitacionais, que entortam a luz como uma lupa.",
    "São um milhão e setecentos mil gigabytes.",
    "Por que importa? Uns noventa e cinco por cento do universo são matéria e energia escuras, que ninguém consegue ver.",
    "Mapeando galáxias de até dez bilhões de anos atrás, o Euclid quer descobrir o que é essa parte invisível.",
    "E isso é só catorze por cento do que ele vai mapear. A próxima leva sai em dois mil e vinte e sete.",
]
CAPTXT = [
    "Um telescópio espacial acabou de catalogar|mais de 900 milhões de galáxias.|E é só o começo.",
    "É o Euclid, da Agência Espacial Europeia: em 13 meses,|ele fotografou um pedaço do céu|igual a 9.500 luas cheias.",
    "No pacote, tem mais de 1 bilhão de objetos|e 15 mil lentes gravitacionais,|que entortam a luz como uma lupa.",
    "São 1,7 milhão de gigabytes.",
    "Por que importa? Uns 95% do universo|são matéria e energia escuras,|que ninguém consegue ver.",
    "Mapeando galáxias de até 10 bilhões de anos atrás,|o Euclid quer descobrir o que é essa parte invisível.",
    "E isso é só 14% do que ele vai mapear.|A próxima leva sai em 2027.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'novecentos', 4), (0, 'comeco', 4), (1, 'euclid', 4), (1, 'treze', 4), (1, 'luas', 6), (2, 'bilhao', 4),
         (2, 'lupa', 6), (3, 'milhao', 6), (4, 'noventa', 6), (4, 'ver', 4), (5, 'dez', 4), (5, 'invisivel', 6),
         (6, 'catorze', 6), (6, 'vinte', 6)]

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





# ------------------------------------------------------------------ desenhos novos (Euclid)
GAL_COLS = [(hexc('#b9a6ff'), hexc('#7d62e0')), (hexc('#ffd28a'), hexc('#e8954a')), (hexc('#9fd8ff'), hexc('#4f8fe0')),
            (hexc('#ffb0d0'), hexc('#d0608f'))]
LUA = hexc('#e6e3da'); LUA_D = hexc('#b9b4a6')
DARK = hexc('#2a2350')


@lru_cache(maxsize=16)
def gal_img(ci, size):
    """galáxia espiral genérica (2 braços de pontinhos), vista um pouco inclinada."""
    col, cd = GAL_COLS[ci % len(GAL_COLS)]
    S = 400
    p = Pen(S, S)
    for r, a in ((150, .18), (110, .3), (70, .5)):
        pass
    p.poly(ell_pts(200, 200, 150, 150, 50), mul(cd, .45))
    p.poly(ell_pts(200, 200, 105, 105, 50), mul(cd, .7))
    for arm in (0, math.pi):
        for i in range(70):
            t = i / 70
            ang_ = arm + t * 3.6
            rr = 18 + 170 * t
            x, y = 200 + rr * math.cos(ang_), 200 + rr * math.sin(ang_)
            p.dot(x, y, max(3, 15 * (1 - t) + 3), col if i % 3 else WHITE)
    p.dot(200, 200, 40, (255, 248, 225))
    p.dot(200, 200, 24, WHITE)
    im = p.img.resize((size, int(size * .62)), Image.LANCZOS)
    return im


def galaxia(c, x, y, size, ci=0, rot=0, s=1.0):
    if size * s < 6: return
    im = gal_img(ci, int(size))
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, y, s)


def lua(c, x, y, r):
    p = Pen(int(2 * r + 20), int(2 * r + 20)); q = r + 10
    p.shape(ell_pts(q, q, r, r, 40), LUA, LUA_D, max(3, int(r / 14)), max(4, int(r / 6)))
    for lx, ly, rr in ((-.3, -.25, .2), (.35, .1, .15), (-.05, .4, .13)):
        p.dot(q + lx * r, q + ly * r, rr * r, LUA_D)
    paste_c(c, p.img.resize((int(2 * r + 20), int(2 * r + 20)), Image.LANCZOS), x, y)


def flash_cam(c, x, y, f, f0, w=1242):
    """faixa de luz da 'foto' do telescópio."""
    if f < f0 or f > f0 + 10: return
    a = int(160 * (1 - (f - f0) / 10))
    d = ImageDraw.Draw(c, 'RGBA')
    d.polygon([(x, y - 30), (x, y + 30), (w, y + 300), (w, y - 300)], fill=(255, 255, 230, a))


def anel_lente(c, x, y, r, f, s=1.0):
    """lente gravitacional: galáxia no meio e a luz de trás virando um anel."""
    if s <= .02: return
    d = ImageDraw.Draw(c, 'RGBA')
    R = r * s
    for k, al in ((1.25, 60), (1.12, 110), (1.0, 230)):
        d.ellipse([x - R * k, y - R * k * .92, x + R * k, y + R * k * .92], outline=(150, 200, 255, al), width=int(max(4, 22 * s)))
    galaxia(c, x, y, int(r * 1.1 * s) + 2, 1, f * .5)


def lupa(c, x, y, h, s=1.0):
    if s <= .02: return
    p = Pen(400, 400)
    p.line([(250, 250), (370, 370)], hexc('#8a5a3a'), 34, 6)
    p.dot(160, 160, 130, INK)
    p.dot(160, 160, 118, hexc('#dff0ff'))
    p.arc(130, 130, 70, 70, 190, 260, 10, WHITE)
    im = p.img.resize((int(h * s) or 1, int(h * s) or 1), Image.LANCZOS)
    paste_c(c, im, x, y)


def cubo(c, x, y, a, col=hexc('#4f8fe0')):
    p = Pen(200, 200)
    p.shape([(30, 60), (130, 60), (130, 170), (30, 170)], col, mul(col, .7), 5, 8)
    p.shape([(30, 60), (70, 25), (170, 25), (130, 60)], mul(col, 1.25), None, 5, 0)
    p.shape([(130, 60), (170, 25), (170, 135), (130, 170)], mul(col, .8), None, 5, 0)
    p.stroke([(45, 100), (115, 100)], 5, WHITE); p.stroke([(45, 125), (100, 125)], 5, WHITE)
    paste_c(c, p.img.resize((int(a), int(a)), Image.LANCZOS), x, y)


@lru_cache(maxsize=2)
def teia_pts(seed=5):
    rnd = random.Random(seed)
    nodes = [(rnd.randint(80, 1160), rnd.randint(380, 1500)) for _ in range(26)]
    edges = []
    for i, a in enumerate(nodes):
        ds = sorted(range(len(nodes)), key=lambda j: (nodes[j][0] - a[0]) ** 2 + (nodes[j][1] - a[1]) ** 2)
        for j in ds[1:4]:
            if (j, i) not in edges: edges.append((i, j))
    return nodes, edges


def pizza(c, x, y, R, frac, f, s=1.0):
    """pizza: parte escura (95%) e fatia visível (5%)."""
    d = ImageDraw.Draw(c, 'RGBA')
    R = R * s
    if R < 4: return
    d.ellipse([x - R - 10, y - R - 10, x + R + 10, y + R + 10], fill=INK + (255,))
    d.pieslice([x - R, y - R, x + R, y + R], -90, -90 + 360 * frac, fill=DARK + (255,))
    d.pieslice([x - R, y - R, x + R, y + R], -90 + 360 * frac, 270, fill=hexc('#f2c14e') + (255,))
    rnd = random.Random(3)
    for i in range(40):
        a = rnd.uniform(-math.pi / 2, -math.pi / 2 + 2 * math.pi * frac * .97)
        rr = rnd.uniform(.15, .92) * R
        tw = 2 + 2 * math.sin(f * .2 + i)
        d.ellipse([x + rr * math.cos(a) - tw, y + rr * math.sin(a) - tw, x + rr * math.cos(a) + tw, y + rr * math.sin(a) + tw], fill=(120, 110, 200, 200))


# ------------------------------------------------------------------ cenas
def s0(f):
    # gancho: telescópio no espaço e galáxias pipocando por toda parte
    c = ceu_bg(11).copy()
    n0 = wt(0, 'novecentos') - 3
    c0 = wt(0, 'comeco') - 3
    rnd = random.Random(4)
    spots = [(rnd.randint(100, 1140), rnd.randint(660, 1360), rnd.randint(90, 190), rnd.randint(0, 3), rnd.randint(-40, 40)) for _ in range(34)]
    nshow = int(len(spots) * clamp((f - 4) / max(1, n0 + 10)))
    for i, (gx, gy, gs, ci, rr) in enumerate(spots[:nshow]):
        if abs(gx - 640) < 380 and abs(gy - 980) < 230: continue
        age = f - 4 - i * (n0 + 10) / len(spots)
        galaxia(c, gx, gy, gs, ci, rr + f * .3, back(clamp(age / 8)))
    put_sonda(c, 640, 980 + 12 * math.sin(f * .12), 760, 0, cor='blue', look=math.sin(f * .07),
              blink=blinkAt(f, 3), expr='shock' if f >= n0 else 'calm')
    num(c, '900 MILHÕES', 640, 400, f, n0, 150, -4)
    num(c, 'DE GALÁXIAS!', 640, 560, f, n0 + 4, 110, 3)
    num(c, 'SÓ O COMEÇO...', 640, 1430, f, c0, 110, -3)
    z = lerp(1.35, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, n0)
    return c, (640 + 10 * math.sin(f * .05), 1000 + k * 10, z, k), 'day'


def s1(f):
    # Euclid fotografa; luas cheias se enfileirando
    c = ceu_bg(3).copy()
    e0 = wt(1, 'euclid') - 3
    t0 = wt(1, 'treze') - 3
    l0 = wt(1, 'luas') - 3
    for i in range(6):
        flash_cam(c, 520, 760, f, e0 + 6 + i * 26)
    put_sonda(c, 330, 760 + 10 * math.sin(f * .1), 600, 0, cor='blue', look=1, blink=blinkAt(f, 5),
              expr='proud' if f >= l0 else 'calm')
    num(c, 'EUCLID · ESA', 420, 500, f, e0, 80, -3)
    num(c, '13 MESES', 900, 340, f, t0, 100, 4)
    if f >= l0:
        k = int((f - l0) * 1.5) + 1
        for i in range(min(k, 48)):
            col, row = i % 12, i // 12
            lua(c, 200 + col * 76, 1030 + row * 80, 32)
    num(c, '9.500 LUAS CHEIAS', 640, 1440, f, l0, 98, -3)
    z = lerp(1.0, 1.06, smooth(ramp(f, 0, 170)))
    cx = 640 + 12 * math.sin(f * .04)
    k = kick(f, l0, .5)
    return c, (cx, 980 + k * 8, z, k), 'day'


def s2(f):
    # o pacote: contador de objetos, lente gravitacional e a lupa
    c = ceu_bg(9).copy()
    b0 = wt(2, 'bilhao') - 3
    q0 = wt(2, 'quinze') - 3
    e0 = wt(2, 'entortam') - 3
    u0 = wt(2, 'lupa') - 3
    rnd = random.Random(8)
    d = ImageDraw.Draw(c, 'RGBA')
    nd = int(300 * clamp((f - b0 + 30) / 40))
    for i in range(nd):
        x, y = rnd.randint(40, 1200), rnd.randint(330, 1500)
        tw = 3 + 2 * math.sin(f * .3 + i)
        d.ellipse([x - tw, y - tw, x + tw, y + tw], fill=(255, 255, 220, 230))
    num(c, '+1 BILHÃO', 640, 380, f, b0, 140, -4)
    num(c, 'DE OBJETOS', 640, 520, f, b0 + 4, 90, 3)
    if f >= q0:
        s = back(ramp(f, q0, q0 + 10))
        anel_lente(c, 640, 960, 190, f, s)
        num(c, '15 MIL LENTES', 640, 1260, f, q0, 100, -3)
    if f >= e0:
        # raio de luz de trás que entorta
        u = clamp((f - e0) / 30)
        pts = [(80 + 560 * t, 960 - 260 * math.sin(math.pi * t) * (1 if t < .5 else 1)) for t in [i / 30 for i in range(int(30 * u) + 1)]]
        if len(pts) > 1: d.line(pts, fill=(255, 240, 150, 230), width=10)
    if f >= u0:
        lupa(c, 1010, 760, 300, back(ramp(f, u0, u0 + 8)))
        num(c, 'LUPA!', 1010, 1440, f, u0, 110, 4)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 200)))
    k = kick(f, q0, .5)
    return c, (640 + 15 * math.sin(f * .03), 1000 + k * 8, z, k), 'day'


def s3(f):
    # dados: cubos de dados caindo até a Terra
    c = terra_bg().copy()
    m0 = wt(3, 'milhao') - 3
    put_sonda(c, 640, 560 + 8 * math.sin(f * .12), 560, 0, cor='blue', look=0, blink=blinkAt(f, 2), expr='proud')
    for i in range(14):
        t = (f * .025 + i / 14) % 1
        x = 640 + 520 * math.sin(i * 2.3) * t
        y = lerp(720, 1560, t)
        cubo(c, x, y, lerp(50, 130, t), [hexc('#4f8fe0'), hexc('#e8b440'), hexc('#7d62e0')][i % 3])
    num(c, '1,7 MILHÃO', 640, 1000, f, m0, 150, -4)
    num(c, 'DE GIGABYTES', 640, 1150, f, m0 + 4, 100, 3)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 90)))
    k = kick(f, m0, .8)
    return c, (640, 1000 + k * 10, z, k), 'golden'


def s4(f):
    # virada: 95% do universo é invisível
    c = ceu_bg(13).copy()
    n0 = wt(4, 'noventa') - 3
    m0 = wt(4, 'materia') - 3
    v0 = wt(4, 'ver') - 3
    num(c, 'POR QUE IMPORTA?', 640, 400, f, 0, 88, -3)
    if f >= n0 - 6:
        s = back(ramp(f, n0 - 6, n0 + 4))
        pizza(c, 640, 950, 330, .95 * clamp((f - n0 + 6) / 20), f, s)
    num(c, '95%', 560, 900, f, n0, 190, -4)
    num(c, 'INVISÍVEL', 640, 1080, f, n0 + 6, 96, 3)
    num(c, 'MATÉRIA ESCURA', 640, 1370, f, m0, 80, -2)
    num(c, '+ ENERGIA ESCURA', 640, 1470, f, m0 + 12, 80, 2)
    if f >= v0:
        put_sonda(c, 1040, 620 + 8 * math.sin(f * .2), 380, 0, cor='blue', look=-1, blink=0, expr='shock')
        paste_c(c, txt('?', 110, 6 * math.sin(f * .2)), 1140, 460)
    z = lerp(1.12, 1.0, smooth(ramp(f, 0, 120)))
    k = kick(f, n0, .7)
    return c, (640, 980 + k * 8, z, k + lerp(0, 2, smooth(ramp(f, m0, m0 + 30)))), 'dusk'


def s5(f):
    # teia cósmica: as galáxias desenham o esqueleto invisível
    c = ceu_bg(7).copy()
    d0 = wt(5, 'dez') - 3
    i0 = wt(5, 'invisivel') - 3
    nodes, edges = teia_pts()
    d = ImageDraw.Draw(c, 'RGBA')
    u = clamp(f / max(1, i0))
    for k, (i, j) in enumerate(edges[:int(len(edges) * u) + 1]):
        a, b = nodes[i], nodes[j]
        d.line([a, b], fill=(140, 120, 230, 150 if f >= i0 else 90), width=14 if f >= i0 else 8)
    for i, (x, y) in enumerate(nodes[:int(len(nodes) * clamp(f / 40)) + 1]):
        galaxia(c, x, y, 120, i % 4, f * .4 + i * 20)
    num(c, '10 BILHÕES DE ANOS', 640, 420, f, d0, 74, -3)
    if f >= i0:
        num(c, 'O ESQUELETO INVISÍVEL', 640, 1440, f, i0, 80, 3)
    z = lerp(1.18, 1.0, smooth(ramp(f, 0, 160)))
    k = kick(f, i0, .5)
    return c, (lerp(600, 680, smooth(ramp(f, 0, 160))), 980 + k * 8, z, k), 'dusk'


def s6(f):
    # fim: mapa do céu com só 14% pintado; 2027
    c = ceu_bg(15).copy()
    t0 = wt(6, 'catorze') - 3
    a0 = wt(6, 'vinte') - 3
    d = ImageDraw.Draw(c, 'RGBA')
    x0, y0, w, h = 140, 640, 960, 520
    d.ellipse([x0 - 10, y0 - 10, x0 + w + 10, y0 + h + 10], fill=INK + (255,))
    d.ellipse([x0, y0, x0 + w, y0 + h], fill=(60, 66, 100, 255))
    fill = .14 * clamp((f - t0 + 10) / 24)
    if fill > 0:
        m = Image.new('L', (w, h), 0)
        ImageDraw.Draw(m).ellipse([0, 0, w - 1, h - 1], fill=255)
        band = Image.new('L', (w, h), 0)
        ImageDraw.Draw(band).rectangle([0, 0, int(w * fill), h], fill=255)
        m = ImageChops.multiply(m, band)
        col = Image.new('RGBA', (w, h), hexc('#7d62e0') + (255,))
        c.paste(col, (x0, y0), m)
        for i in range(6):
            galaxia(c, x0 + 40 + (i % 2) * 60, y0 + 120 + i * 50, 60, i % 4, f)
    put_sonda(c, 640, 430 + 8 * math.sin(f * .1), 420, 0, cor='blue', look=1, blink=blinkAt(f, 4), expr='proud')
    num(c, 'SÓ 14%', 760, 900, f, t0, 170, -4)
    if f >= a0:
        s = back(ramp(f, a0, a0 + 8))
        q = Pen(300, 300)
        q.shape([(20, 50), (280, 50), (280, 280), (20, 280)], WHITE, hexc('#d6dbe4'), 6, 8)
        q.shape([(20, 50), (280, 50), (280, 110), (20, 110)], RED, mul(RED, .75), 6, 0)
        for gx in (80, 220): q.line([(gx, 20), (gx, 80)], INK, 14, 0)
        paste_c(c, q.img.resize((240, 240), Image.LANCZOS), 1000, 1340, s)
        paste_c(c, txt('2027', 60, 0), 1000, 1380, s)
        num(c, 'PRÓXIMA LEVA:', 520, 1300, f, a0, 84, -3)
        num(c, 'EM 2027', 520, 1420, f, a0 + 4, 100, 3)
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 160))) + .025 * math.sin(f * .035)
    k = kick(f, t0, .5)
    return c, (640 + 30 * math.sin(f * .03), 1000 + k * 8, z, k + math.sin(f * .05)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.whoosh(s.W(0, 'um') - 3, .4, .5)
    s.thunk(s.W(0, 'novecentos') - 3, 140, .9)
    s.ting(s.W(0, 'comeco') - 3, .3)
    s.ting(s.W(1, 'euclid') - 3, .3)
    s.ting(s.W(1, 'treze') - 3, .3)
    s.thunk(s.W(1, 'luas') - 3, 160, .6)
    s.thunk(s.W(2, 'bilhao') - 3, 150, .7)
    s.ting(s.W(2, 'quinze') - 3, .3)
    s.ting(s.W(2, 'lupa') - 3, .4)
    s.thunk(s.W(3, 'milhao') - 3, 170, .8)
    s.thunk(s.W(4, 'noventa') - 3, 170, .7)
    s.ting(s.W(5, 'dez') - 3, .3)
    s.ting(s.W(5, 'invisivel') - 3, .4)
    s.thunk(s.W(6, 'catorze') - 3, 180, .6)
    s.ting(s.W(6, 'vinte') - 3, .4)
