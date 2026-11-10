"""Um Café com o Mundo — CURIOSIDADE (terça 10/11/2026, 17h).
Tema: Marte pode ainda estar vulcanicamente vivo — gás saindo de rachaduras novas no vulcão Alba Mons.
Fontes (conferidas em 10/11/2026):
- ESA, comunicado de 04/11/2026 (EurekAlert! 1150079): artigo "Enigmatic HCl detections as a potential signature of
  igneous activity on Mars", Science Advances (doi 10.1126/sciadv.aeb9422), liderado por Alexander Trokhimovskiy;
  co-autor principal Daniel Mège (Centro de Pesquisas Espaciais da Academia Polonesa de Ciências).
  A sonda ExoMars Trace Gas Orbiter (TGO), da ESA, detectou picos de cloreto de hidrogênio (HCl) sobre fissuras
  vulcânicas nos flancos do Alba Mons, no começo do verão do hemisfério norte, quando o HCl normalmente some
  (pico no inverno). A câmera CaSSIS mostrou fissuras novas e estreitas, algumas com centenas de metros.
  Hipótese: gases magmáticos sobem pelas fissuras; o gelo do inverno as sela e a sublimação no começo do verão libera
  o cloro. Sugere câmara de magma adormecida e calor interno até recentemente, talvez até hoje. Nenhuma erupção ou
  lava nova foi observada. Se lava encontrar água subterrânea, pode criar nichos quentes e habitáveis; as fissuras do
  Alba Mons seriam bom lugar para procurar vida.
- BBC Sky at Night Magazine, 05/11/2026; Universe Today, 09/11/2026 (mesmo estudo).
Sem logotipos; sonda, vulcão e planeta genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Marte pode não estar morto: tem gás saindo de rachaduras num vulcão de lá.",
    "Quem viu foi a TGO, uma sonda europeia que fareja o ar de Marte.",
    "Ela achou picos de cloreto de hidrogênio, um gás que vulcões soltam, em cima de rachaduras novas no Alba Mons.",
    "Algumas têm centenas de metros, e o gás aparece no verão, justo quando deveria sumir.",
    "A explicação: no inverno, o gelo tampa as rachaduras; no verão, ele some, e o gás escapa.",
    "Por que isso importa? Mesmo sem nenhuma erupção à vista, pode haver uma câmara de magma adormecida lá embaixo.",
    "E se esse calor encontrar água, pode surgir um cantinho quente: um bom lugar pra procurar vida.",
]
CAPTXT = [
    "Marte pode não estar morto: tem gás saindo|de rachaduras num vulcão de lá.",
    "Quem viu foi a TGO, uma sonda europeia|que fareja o ar de Marte.",
    "Ela achou picos de cloreto de hidrogênio, um gás que vulcões soltam,|em cima de rachaduras novas no Alba Mons.",
    "Algumas têm centenas de metros, e o gás aparece no verão,|justo quando deveria sumir.",
    "A explicação: no inverno, o gelo tampa as rachaduras;|no verão, ele some, e o gás escapa.",
    "Por que isso importa? Mesmo sem nenhuma erupção à vista,|pode haver uma câmara de magma adormecida lá embaixo.",
    "E se esse calor encontrar água, pode surgir um cantinho quente:|um bom lugar pra procurar vida.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'gas', 4), (1, 'sonda', 4), (2, 'picos', 4), (2, 'alba', 4), (3, 'centenas', 4), (3, 'sumir', 4),
         (4, 'inverno', 4), (4, 'escapa', 6), (5, 'magma', 4), (6, 'quente', 4), (6, 'vida', 6)]

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



SKY = hexc('#e9b98c'); SKY2 = hexc('#f3d6b0')
GROUND = hexc('#c4623a'); GROUND_D = hexc('#9c4a2c')
VOLC = hexc('#b8573a'); VOLC_D = hexc('#8e3f2a')
GAS = (214, 236, 196)
ICE = hexc('#dff1ff'); ICE_D = hexc('#a9cde8')
MAGMA = hexc('#ff8a2a'); MAGMA_D = hexc('#e0501f')
WATER = hexc('#4f9be0'); WATER_D = hexc('#2f6fb0')
VX, VBASE, VW, VH = 621, 1460, 1360, 560   # vulcão no palco

FISS = [  # rachaduras nos flancos (palco)
    [(250, 1330), (300, 1300), (330, 1310), (380, 1270), (420, 1262)],
    [(820, 1262), (870, 1280), (900, 1262), (960, 1300), (1010, 1318)],
    [(500, 1390), (560, 1372), (600, 1386), (660, 1366)],
]


def vulcao(eye=0.0, expr='sleep'):
    """vulcão-escudo bem largo (como o Alba Mons) com cara. 1360x600, base em y=600."""
    p = Pen(VW, 600)
    W = VW
    pts = [(0, 600)] + [(W * t, 600 - VH * (1 - (2 * t - 1) ** 4) ** .8 * (1 if abs(2 * t - 1) > .12 else .97)) for t in [i / 60 for i in range(61)]] + [(W, 600)]
    p.shape(pts, VOLC, VOLC_D, 6, 30)
    # caldeira no topo
    p.shape(ell_pts(W / 2, 600 - VH + 34, 150, 22, 40), VOLC_D, None, 5, 0)
    # cara
    for ex in (W / 2 - 120, W / 2 + 120):
        ey, er = 600 - VH + 190, 46
        p.dot(ex, ey, er, WHITE, 5)
        L = 1 - eye
        if L < .8:
            p.dot(ex + 6, ey + 6, 20 if expr == 'shock' else 18, INK)
            p.dot(ex, ey - 2, 6, WHITE)
        if L > .02:
            top = ey - er; yb = top + 2 * er * L
            p.poly([(ex - er - 1, top - 2), (ex + er + 1, top - 2), (ex + er + 1, yb), (ex - er - 1, yb)], VOLC)
            p.stroke([(ex - er + 4, yb), (ex + er - 4, yb)], 5)
    my = 600 - VH + 290
    if expr == 'shock':
        p.shape(ell_pts(W / 2, my, 30, 36, 30), hexc('#5a2418'), None, 5, 0)
    else:
        p.arc(W / 2, my - 20, 40, 18, 20, 160, 5)
    for sx in (-1, 1):  # bochechas
        p.dot(W / 2 + sx * 210, my - 30, 30, hexc('#d77a5a'))
    return p.img


def put_vulcao(c, x, base, w, eye=0.0, expr='sleep'):
    eye = round(clamp(eye) * 4) / 4
    im = sprite('vulcao', (('expr', expr), ('eye', eye)), int(w * 600 / VW), VW / 600, False)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(base - im.size[1])))


@lru_cache(maxsize=2)
def marte_bg():
    """chão de Marte: céu caramelo, morros ao fundo, chão ferrugem com pedrinhas."""
    base = Image.new('RGBA', (BW, BH), SKY + (255,))
    d = ImageDraw.Draw(base)
    for i in range(40):
        t = i / 39
        col = tuple(int(lerp(a, b, t)) for a, b in zip(SKY2, SKY))
        d.rectangle([0, int(t * 1300), BW, int(t * 1300) + 34], fill=col)
    p = Pen(BW, BH)
    p.shape([(-20, 1300), (150, 1180), (330, 1240), (560, 1160), (800, 1230), (1000, 1150), (1262, 1240), (1262, 1500), (-20, 1500)], hexc('#d98a63'), hexc('#c07050'), 0, 16)
    p.shape([(-20, 1440), (1262, 1440), (1262, 2230), (-20, 2230)], GROUND, GROUND_D, 0, 20)
    rnd = random.Random(4)
    for i in range(26):
        x, y = rnd.randint(0, BW), rnd.randint(1480, 2150)
        p.shape(ell_pts(x, y, rnd.randint(14, 34), rnd.randint(8, 18), 20, .3), hexc('#a85234'), GROUND_D, 4, 4)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    planeta(base, 1060, 330, 40, hexc('#cfc6bd'), hexc('#a69c92'))  # luazinha Fobos
    return base


def puff(c, x, y, f, f0, n=5, s=1.0, spread=1.0):
    """baforadas de gás subindo de um ponto (a partir do quadro f0)."""
    if f < f0: return
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(n):
        age = (f - f0 + i * 11) % 55
        if f - f0 + i * 11 < 0: continue
        t = age / 55
        r = (16 + 46 * t) * s
        px = x + spread * 30 * math.sin(i * 2.1 + t * 3)
        py = y - 260 * t * s
        a = int(200 * (1 - t) * min(1, (f - f0) / 6))
        d.ellipse([px - r, py - r, px + r, py + r], fill=GAS + (a,), outline=(80, 110, 70, int(a * .6)), width=3)


def fissuras(c, k=1.0, glow=0.0, pts=FISS, sx=1.0, ox=0, oy=0):
    d = ImageDraw.Draw(c, 'RGBA')
    for fz in pts:
        q = [(ox + x * sx, oy + y * sx) for x, y in fz]
        n = max(2, int(len(q) * clamp(k) + .99))
        if glow > 0: d.line(q[:n], fill=(255, 150, 60, int(160 * glow)), width=int(22 * sx), joint='curve')
        d.line(q[:n], fill=INK + (255,), width=int(11 * sx), joint='curve')


def grafico(c, x, y, w, h, f, f0, spikes=1.0):
    """painel de leitura da sonda: linha baixa com picos."""
    p = Pen(w, h)
    p.shape([(0, 0), (w, 0), (w, h), (0, h)], hexc('#1f2a4a'), hexc('#141c35'), 6, 10)
    pts = []
    for i in range(61):
        t = i / 60
        v = .12 + .04 * math.sin(i * 1.3)
        for cx_, a in ((.35, .7), (.62, .85), (.82, .6)):
            v += a * spikes * math.exp(-((t - cx_) / .035) ** 2)
        pts.append((20 + (w - 40) * t, h - 20 - (h - 50) * min(1, v)))
    n = max(2, int(61 * ramp(f, f0, f0 + 40)))
    p.stroke(pts[:n], 7, hexc('#7dfc9a'))
    paste_c(c, p.img.resize((w, h), Image.LANCZOS), x, y)


@lru_cache(maxsize=2)
def corte_bg(agua=0.0):
    """corte do chão: superfície com vulcão pequeno, camadas de rocha, câmara de magma e água embaixo."""
    c = Image.new('RGBA', (BW, BH), SKY + (255,))
    p = Pen(BW, BH)
    p.shape([(-20, 760), (1262, 760), (1262, 2230), (-20, 2230)], GROUND, GROUND_D, 6, 0)
    p.shape([(-20, 1000), (1262, 1000), (1262, 2230), (-20, 2230)], hexc('#9a4a30'), None, 0, 0)
    p.shape([(-20, 1260), (1262, 1260), (1262, 2230), (-20, 2230)], hexc('#7a3a28'), None, 0, 0)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


@lru_cache(maxsize=1)
def marte_grande():
    c = Image.new('RGBA', (BW, BH), (0, 0, 0, 0))
    d = ImageDraw.Draw(c, 'RGBA')
    d.ellipse([640 - 450, 1250 - 450, 640 + 450, 1250 + 450], fill=(255, 200, 160, 50))
    planeta(c, 640, 1250, 400, MARS, MARS_D, (255, 210, 180))
    return c


# ------------------------------------------------------------------ cenas
def s0(f):
    # gancho: chão de Marte, vulcão dormindo, gás saindo das rachaduras
    c = marte_bg().copy()
    g0 = wt(0, 'gas') - 3
    r0 = wt(0, 'rachaduras') - 3
    m0 = wt(0, 'morto') - 3
    put_vulcao(c, VX, VBASE, VW, eye=.0 if f < r0 + 10 else .5, expr='sleep')
    fissuras(c, 1.0, .5 if f >= g0 else 0)
    for i, fz in enumerate(FISS):
        puff(c, fz[len(fz) // 2][0], fz[len(fz) // 2][1], f, g0 + i * 4, 5, 1.0)
    num(c, 'MARTE', 640, 420, f, 0, 130, -4)
    num(c, 'MORTO?', 640, 600, f, m0, 120, 4)
    num(c, 'GÁS!', 1000, 1000, f, g0, 140, -6)
    z = lerp(1.3, 1.0, easeOut(ramp(f, 0, 60))) * (1 + .0006 * f)
    k = kick(f, g0)
    return c, (640 + 10 * math.sin(f * .05), lerp(1180, 1050, easeOut(ramp(f, 0, 60))) + k * 10, z, k), 'day'


def s1(f):
    # espaço: Marte grande e a sonda TGO em órbita, farejando o ar
    c = ceu_bg(21).copy()
    mx, my = 640, 1250
    d = ImageDraw.Draw(c, 'RGBA')
    c.alpha_composite(marte_grande())
    t = f * .012
    sx, sy = 640 + 300 * math.cos(math.pi * 1.1 - t), 640 + 60 * math.sin(math.pi * 1.1 - t)
    s0_ = wt(1, 'sonda') - 3
    sc = back(ramp(f, s0_ - 30, s0_ - 10)) if f < s0_ + 400 else 1
    put_sonda(c, sx, sy, 560 * max(.01, sc), -8, False, cor='gold', look=-.5 + math.sin(f * .08) * .5, blink=blinkAt(f, 3),
              expr='calm' if f < wt(1, 'fareja') - 3 else 'proud')
    fa = wt(1, 'fareja') - 3
    if f >= fa:  # "farejando": ondinhas para baixo
        for i in range(3):
            a = ((f - fa) * 3 + i * 25) % 75
            r = 30 + a * 2
            d.arc([sx - r, sy + 60 - r * .4, sx + r, sy + 60 + r * .4], 20, 160, fill=(255, 255, 255, int(220 * (1 - a / 75))), width=6)
    num(c, 'TGO', sx + 260, sy - 200, f, s0_, 130, -4)
    num(c, 'SONDA EUROPEIA', 640, 1820 - 300, f, wt(1, 'europeia') - 3, 84, 3)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160)))
    return c, (640, lerp(1000, 960, smooth(ramp(f, 0, 160))), z, lerp(-1.5, 1.5, smooth(ramp(f, 0, 160)))), 'day'


def s2(f):
    # leitura com picos do gás sobre o vulcão Alba Mons
    c = marte_bg().copy()
    p0 = wt(2, 'picos') - 3
    a0 = wt(2, 'alba') - 3
    n0 = wt(2, 'novas') - 3
    put_vulcao(c, VX, VBASE, VW, eye=.5, expr='sleep')
    fissuras(c, ramp(f, n0 - 6, n0 + 10) if f >= n0 - 6 else 0, .6)
    if f >= n0:
        for i, fz in enumerate(FISS):
            puff(c, fz[len(fz) // 2][0], fz[len(fz) // 2][1], f, n0 + i * 3, 4, .9)
    put_sonda(c, 900 + 20 * math.sin(f * .05), 520, 300, -6, True, cor='gold', look=1, blink=blinkAt(f, 6), expr='shock' if f >= p0 else 'calm')
    if f >= p0 - 10:
        grafico(c, 380, 560, 520, 300, f, p0 - 10, smooth(ramp(f, p0 - 4, p0 + 14)))
    num(c, 'PICOS!', 380, 380, f, p0, 120, -5)
    num(c, 'CLORETO DE HIDROGÊNIO', 640, 900 - 60, f, wt(2, 'cloreto') - 3, 64, 2)
    num(c, 'ALBA MONS', 640, 1250, f, a0, 110, -3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 200)))
    k = kick(f, p0, .7)
    return c, (640, 1000 + k * 10, z, k), 'day'


def s3(f):
    # de perto na rachadura da esquerda: centenas de metros; sol do verão; o gás deveria sumir
    c = marte_bg().copy()
    put_vulcao(c, VX, VBASE, VW, eye=.5, expr='sleep')
    c0 = wt(3, 'centenas') - 3
    ve = wt(3, 'verao') - 3
    su = wt(3, 'sumir') - 3
    fissuras(c, 1.0, .6)
    if f >= c0:
        d = ImageDraw.Draw(c)
        s = back(ramp(f, c0, c0 + 10))
        x1 = max(241, lerp(240, 430, s))
        for w_, col in ((16, INK), (7, WHITE)):
            d.line([(240, 1215), (x1, 1215)], fill=col, width=w_)
            d.line([(240, 1195), (240, 1235)], fill=col, width=w_)
        num(c, 'CENTENAS DE METROS', 560, 940, f, c0, 70, -2)
    if f >= ve:
        paste_c(c, sun_icon(200, 1.0), 840, 640, back(ramp(f, ve, ve + 8)))
        num(c, 'VERÃO', 520, 650, f, ve, 100, 4)
        for i, fz in enumerate(FISS):
            puff(c, fz[len(fz) // 2][0], fz[len(fz) // 2][1], f, ve + i * 3, 5, 1.0)
    num(c, 'DEVERIA SUMIR!', 560, 790, f, su, 90, -4)
    z = lerp(1.18, 1.28, smooth(ramp(f, 0, 160)))
    k = kick(f, su, .7)
    return c, (lerp(540, 580, smooth(ramp(f, 0, 160))), 1100 + k * 10, z, k), 'golden'


def s4(f):
    # explicação: inverno (gelo tampa) -> verão (gelo some, gás escapa)
    c = marte_bg().copy()
    i0 = wt(4, 'inverno') - 3
    v0 = wt(4, 'verao') - 3
    e0 = wt(4, 'escapa') - 3
    put_vulcao(c, VX, VBASE, VW, eye=0, expr='sleep')
    fissuras(c, 1.0, 0)
    melt = smooth(ramp(f, v0, v0 + 30))
    d = ImageDraw.Draw(c, 'RGBA')
    if f >= i0 - 6:
        cover = max(0, back(ramp(f, i0 - 6, i0 + 6))) * (1 - melt)
        for fz in FISS:
            xs = [x for x, _ in fz]; ys = [y for _, y in fz]
            cx_, cy_ = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
            rx, ry = (max(xs) - min(xs)) / 2 + 40, 40
            if cover > .02:
                d.ellipse([cx_ - rx * cover, cy_ - ry * cover, cx_ + rx * cover, cy_ + ry * cover], fill=ICE + (240,), outline=INK + (255,), width=6)
        # flocos de neve no inverno
        if melt < .5:
            for i in range(24):
                x = (i * 97 + f * 2) % BW
                y = 300 + (i * 131 + f * 6) % 1100
                d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=(255, 255, 255, int(220 * (1 - 2 * melt))))
    if f < v0: num(c, 'INVERNO: GELO TAMPA', 640, 480, f, i0, 88, -3)
    if f >= v0:
        paste_c(c, sun_icon(220, 1.0), 1060, 640, back(ramp(f, v0, v0 + 8)))
        num(c, 'VERÃO: GELO SOME', 600, 480, f, v0, 88, 3)
    if f >= e0:
        for i, fz in enumerate(FISS):
            puff(c, fz[len(fz) // 2][0], fz[len(fz) // 2][1], f, e0 + i * 2, 6, 1.2)
        num(c, 'O GÁS ESCAPA!', 640, 1000, f, e0, 120, -4)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200)))
    k = kick(f, e0, .6)
    lz = 'day' if f >= v0 else 'golden'
    return c, (640, 1000 + k * 8, z, k), lz


def s5(f):
    # por que importa: corte do chão com câmara de magma adormecida; sem erupção
    c = corte_bg().copy()
    m0 = wt(5, 'magma') - 3
    e0 = wt(5, 'erupcao') - 3
    put_vulcao(c, VX, 770, 900, eye=0, expr='sleep')
    zzz(c, 860, 360, f)
    d = ImageDraw.Draw(c, 'RGBA')
    gl = .5 + .5 * math.sin(f * .12)
    if f >= m0 - 8:
        s = max(.02, back(ramp(f, m0 - 8, m0 + 4)))
        cx_, cy_ = 621, 1330
        for r, a in ((300, 50), (250, 80)):
            d.ellipse([cx_ - r * s * 1.4, cy_ - r * s * .6, cx_ + r * s * 1.4, cy_ + r * s * .6], fill=MAGMA + (int(a * (0.7 + .3 * gl)),))
        p = Pen(700, 320)
        p.shape(ell_pts(350, 160, 320, 130, 40, .15), MAGMA, MAGMA_D, 6, 18)
        for i in range(5):
            p.dot(150 + i * 100, 150 + 30 * math.sin(i * 2 + f * .1), 18, hexc('#ffd04a'))
        paste_c(c, p.img.resize((700, 320), Image.LANCZOS), cx_, cy_, s)
        # caminho até as rachaduras
        d.line([(621, 1180), (560, 1000), (600, 820)], fill=MAGMA + (int(120 + 80 * gl),), width=14)
    num(c, 'POR QUE IMPORTA?', 640, 330, f, 0, 96, -3)
    num(c, 'CÂMARA DE MAGMA', 640, 1530, f, m0, 90, 3)
    if f >= e0:
        num(c, 'SEM ERUPÇÃO', 960, 900, f, e0, 70, -4)
    z = lerp(1.08, .98, smooth(ramp(f, 0, 160)))
    k = kick(f, m0, .6)
    return c, (640, lerp(900, 1050, smooth(ramp(f, 0, 160))) + k * 8, z, k), 'dusk'


def s6(f):
    # calor encontra água: cantinho quente, bom lugar para procurar vida (sonda com lupa)
    c = corte_bg().copy()
    put_vulcao(c, VX, 770, 900, eye=.5, expr='sleep')
    a0 = wt(6, 'agua') - 3
    q0 = wt(6, 'quente') - 3
    v0 = wt(6, 'vida') - 3
    d = ImageDraw.Draw(c, 'RGBA')
    gl = .5 + .5 * math.sin(f * .12)
    p = Pen(700, 320)
    p.shape(ell_pts(350, 160, 320, 130, 40, .15), MAGMA, MAGMA_D, 6, 18)
    paste_c(c, p.img.resize((560, 256), Image.LANCZOS), 420, 1420)
    if f >= a0:
        s = back(ramp(f, a0, a0 + 10))
        q = Pen(600, 260)
        q.shape(ell_pts(300, 130, 280, 100, 40, .2), WATER, WATER_D, 6, 14)
        for i in range(4):
            q.arc(160 + i * 90, 130, 30, 10, 200, 340, 4)
        paste_c(c, q.img.resize((480, 208), Image.LANCZOS), 880, 1160, s)
        num(c, 'ÁGUA', 880, 1160, f, a0, 70, 0)
    if f >= q0:
        s = back(ramp(f, q0, q0 + 10))
        r = max(2, 150 * s)
        d.ellipse([660 - r, 1290 - r * .7, 660 + r, 1290 + r * .7], fill=(255, 190, 90, int(150 + 60 * gl)), outline=INK + (255,), width=6)
        num(c, 'CANTINHO QUENTE', 600, 960, f, q0, 84, 3)
    put_sonda(c, 330 + 15 * math.sin(f * .06), 430, 300, -10, False, cor='gold', look=1, blink=blinkAt(f, 8), expr='proud' if f >= v0 else 'calm')
    num(c, 'VIDA?', 860, 440, f, v0, 150, -5)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 200))) * (1 + .0012 * max(0, f - 120))
    k = kick(f, v0, .7)
    return c, (640 + 25 * math.sin(f * .04), lerp(1000, 1060, smooth(ramp(f, 0, 200))) + k * 8, z, k + .8 * math.sin(f * .03)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.whoosh(s.W(0, 'marte') - 3, .4, .5)
    s.thunk(s.W(0, 'gas') - 3, 140, .8)
    s.ting(s.W(1, 'sonda') - 3, .3)
    s.thunk(s.W(2, 'picos') - 3, 160, .7)
    s.ting(s.W(2, 'alba') - 3, .3)
    s.ting(s.W(3, 'centenas') - 3, .3)
    s.thunk(s.W(3, 'sumir') - 3, 160, .7)
    s.ting(s.W(4, 'inverno') - 3, .3)
    s.whoosh(s.W(4, 'escapa') - 3, .4, .5)
    s.thunk(s.W(5, 'magma') - 3, 150, .8)
    s.ting(s.W(6, 'quente') - 3, .3)
    s.thunk(s.W(6, 'vida') - 3, 180, .7)
