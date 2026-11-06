"""Formato DESENHO: por que a barriga ronca (Curiosidades da IA, 06/11/2026, 15h). Categoria: CORPO HUMANO.
Fatos: Scientific American, "Why does your stomach growl when you are hungry?" (paredes do estômago e do intestino são
músculos; ondas de contração (peristaltismo) empurram comida, gás e líquido, e esse movimento faz o ronco; ronca de barriga
cheia ou vazia, mas vazia se ouve mais porque não há conteúdo abafando; cerca de 2 horas depois que estômago e intestino
esvaziam começam os complexos motores migratórios: ondas que varrem muco, restos de comida e bactérias até o fim do
intestino delgado, duram 10 a 20 minutos e se repetem a cada 1 a 2 horas até a próxima refeição)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h18 = _load('h18', '2026-11-06-18h'); _h10 = _load('h10', '2026-11-06-10h')
jovem = _h18.jovem; quarto_bg = _h18.quarto_bg; mesa = _h18.mesa; cor = _h10.cor

LINES = [
    "A sua barriga ronca até quando está cheia.",
    "A parede da barriga é feita de músculos que apertam o tempo todo, empurrando comida, líquido e gás pelo caminho.",
    "É esse gás e esse líquido sendo espremidos que fazem o barulho.",
    "Umas duas horas depois que a barriga esvazia, começa uma onda de apertos que varre tudo até o fim do intestino.",
    "Ela leva restinhos de comida e bactérias, e se repete a cada uma ou duas horas, até você comer de novo.",
    "Você vê, com a barriga cheia, a comida abafa o som. Vazia, não tem nada pra segurar o barulho.",
    "Ou seja: o ronco não é a barriga pedindo comida... é ela fazendo faxina.",
]
CAPTXT = [
    "A sua barriga ronca até quando está cheia.",
    "A parede da barriga é feita de músculos que apertam o tempo todo,|empurrando comida, líquido e gás pelo caminho.",
    "É esse gás e esse líquido sendo espremidos que fazem o barulho.",
    "Umas 2 horas depois que a barriga esvazia, começa uma onda de apertos|que varre tudo até o fim do intestino.",
    "Ela leva restinhos de comida e bactérias, e se repete a cada 1 ou 2 horas,|até você comer de novo.",
    "Você vê, com a barriga cheia, a comida abafa o som.|Vazia, não tem nada pra segurar o barulho.",
    "Ou seja: o ronco não é a barriga pedindo comida...|é ela fazendo faxina.",
]
FALA_TIKTOK = "Sua barriga ronca muito? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [1, 3]
CHECK = [(0, 'ronca', 4), (0, 'cheia', 4), (1, 'musculos', 4), (1, 'empurrando', 6), (2, 'barulho', 4), (3, 'horas', 4),
         (3, 'varre', 6), (4, 'bacterias', 4), (5, 'abafa', 4), (5, 'vazia', 6), (6, 'faxina', 8)]

ROSA, ROSAD = hexc('#f59aa8'), hexc('#d86f80')


def put_jovem(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'jovem', x, feet, h, f, seed, **kw)


def estomago(expr='calm', blink=0, squeeze=0.0, broom=False, look=0.5):
    """estômago em forma de feijão com carinha (600x600)."""
    p = Pen(600, 600)
    sq = squeeze
    p.line([(170, 60), (190, 150)], ROSA, 50, 6)  # esôfago
    pts = []
    for x, y in ell_pts(300, 320, 220 - 30 * sq, 190 + 20 * sq, 64, -.35, .15):
        pts.append((x, y))
    p.shape(pts, ROSA, ROSAD, 6, 22)
    p.line([(470, 430), (540, 520), (590, 520)], ROSA, 46, 6)  # saída pro intestino
    for dx in (-55, 55):
        ex, ey = 310 + dx, 300
        if blink > .6: p.stroke([(ex - 22, ey), (ex + 22, ey)], 7)
        elif expr == 'squint':
            p.stroke([(ex - 22, ey - 10), (ex + 18, ey), (ex - 22, ey + 10)] if dx < 0 else [(ex + 22, ey - 10), (ex - 18, ey), (ex + 22, ey + 10)], 7)
        else:
            r = 34 if expr == 'shock' else 28
            p.dot(ex, ey, r, (255, 255, 255), 5); p.dot(ex + look * 10, ey + 3, 12, INK); p.dot(ex + look * 10 - 4, ey - 2, 4, (255, 255, 255))
            if expr == 'smug': p.poly([(ex - r - 2, ey - r - 4), (ex + r + 2, ey - r - 4), (ex + r + 2, ey - 6), (ex - r - 2, ey - 6)], ROSA); p.stroke([(ex - r, ey - 6), (ex + r, ey - 6)], 6)
    if expr in ('grin', 'smug'): p.arc(310, 370, 40, 22, 20, 160, 7)
    elif expr in ('shock', 'squint'): p.dot(310, 385, 24 if expr == 'shock' else 18, hexc('#7a2e2e'), 5)
    else: p.arc(310, 375, 30, 14, 20, 160, 7)
    if broom:
        p.line([(470, 160), (360, 520)], hexc('#b07a45'), 16, 5)
        p.shape([(300, 500), (430, 540), (420, 590), (290, 560)], hexc('#ffd84a'), hexc('#e0b52a'), 5, 6)
    return p.img


def put_est(c, x, y, size, f, seed=1, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'squeeze' in kw: kw['squeeze'] = round(kw['squeeze'] * 6) / 6
    im = sprite('estomago', tuple(sorted(kw.items())), int(size), 1.0, False)
    paste_c(c, im, x, y)


@lru_cache(maxsize=2)
def corpo_bg():
    W, H = BW, BH
    y = np.linspace(0, 1, H)[:, None, None]
    a = np.array(hexc('#ffd9dc')) * (1 - y) + np.array(hexc('#f7b3bd')) * y
    im = Image.fromarray(np.broadcast_to(a, (H, W, 3)).astype(np.uint8)).convert('RGBA')
    p = Pen(W, H); rnd = random.Random(3)
    for i in range(24):
        x, yy, r = rnd.randint(0, W), rnd.randint(0, H), rnd.randint(40, 120)
        p.shape(ell_pts(x, yy, r, r * .7, 32, rnd.random()), hexc('#fbc6cd'), None, 0)
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    return im


@lru_cache(maxsize=2)
def tubo_img():
    """intestino em zigue-zague (1242x700)."""
    p = Pen(1242, 700)
    pts = [(-40, 120), (1100, 120), (1180, 220), (1100, 320), (140, 320), (60, 420), (140, 520), (1282, 520)]
    p.line(pts, hexc('#f28a9a'), 130, 6)
    p.line(pts, hexc('#ffb6c1'), 92, 0)
    return p.img


def tubo_pos(u):
    pts = [(-40, 120), (1100, 120), (1180, 220), (1100, 320), (140, 320), (60, 420), (140, 520), (1282, 520)]
    L = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    d = clamp(u) * sum(L)
    for i, l in enumerate(L):
        if d <= l: t = d / l; return lerp(pts[i][0], pts[i + 1][0], t), lerp(pts[i][1], pts[i + 1][1], t)
        d -= l
    return pts[-1]


def migalha(c, x, y, r=22, k=0):
    p = Pen(60, 60)
    p.shape(ell_pts(30, 30, r, r * .8, 16, k), hexc('#c98a4a'), hexc('#9a6430'), 4, 4)
    paste_c(c, p.img, x, y)


def bolha(c, x, y, r=30):
    p = Pen(int(r * 2 + 20), int(r * 2 + 20))
    p.shape(ell_pts(r + 10, r + 10, r, r, 24), hexc('#e8f6ff'), hexc('#b9dcef'), 4, 6)
    p.dot(r * .7 + 10, r * .7 + 10, r * .22, (255, 255, 255))
    paste_c(c, p.img, x, y)


def SFX(s):
    for i in range(3): s.thunk(s.W(0, 'ronca') - 2 + i * 5, 90, .7)
    s.ting(s.W(0, 'cheia'), .3)
    for i in range(4): s.thunk(s.W(1, 'apertam') + i * 9, 140, .45)
    s.whoosh(s.W(1, 'empurrando') - 4, .6, .35)
    for i in range(3): s.thunk(s.W(2, 'barulho') - 2 + i * 6, 80, .8)
    s.ting(s.W(3, 'horas'), .3); s.whoosh(s.W(3, 'varre') - 4, .7, .45)
    for i in range(4): s.thunk(s.W(4, 'bacterias') + i * 4, 320, .3)
    s.thunk(s.W(5, 'vazia') - 2, 90, .8)
    s.trill(s.W(6, 'faxina'), .9, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = quarto_bg().copy(); mesa(c, 1500)
    r0 = wt(0, 'ronca') - 3
    ch = wt(0, 'cheia') - 3
    p = Pen(420, 160); p.shape(ell_pts(210, 80, 190, 60, 40), (255, 255, 255), hexc('#dddddd'), 5, 8); p.shape(ell_pts(210, 72, 120, 30, 32), hexc('#f2e6d0'), None, 3)
    paste_c(c, p.img, 880, 1460)
    put_jovem(c, 460, 2120, 1150, f, 1, arms='hang' if f < r0 else 'cheek', expr='grin' if f < r0 else 'shock', look=1, shirt='#6fbf73')
    if f >= r0:
        rings(c, 660, 1650, f, r0, 40, 1.3)
        paste_c(c, txt('RONC!', 130, -8), 820, 1120, back(ramp(f, r0, r0 + 8)))
    if f >= ch: paste_c(c, txt('DE BARRIGA CHEIA?!', 72, 5), 600, 860, back(ramp(f, ch, ch + 8)))
    kk = kick(f, r0 + 2)
    t = easeOut(ramp(f, 0, 40))
    return c, (lerp(500, 640, t), 1300 + kk * 10, lerp(1.4, 1.08, t), kk), 'day'


def s1(f):
    c = corpo_bg().copy()
    m0 = wt(1, 'musculos') - 3
    e0 = wt(1, 'empurrando') - 3
    sq = .5 + .5 * math.sin(f * .25) if f >= m0 else 0
    put_est(c, 640, 1080, 760, f, 1, expr='squint' if sq > .6 else 'calm', squeeze=sq, look=.6)
    if f >= m0: paste_c(c, txt('MÚSCULOS!', 120, -6), 640, 560, back(ramp(f, m0, m0 + 8)))
    if f >= e0:
        for i in range(5):
            u = ((f - e0) * 2.2 + i * 70) % 420
            x, y = 520 + u * 1.0, 1280 + u * .25
            if i % 2: migalha(c, x, y, 24, i)
            else: bolha(c, x, y, 26)
    z = lerp(1.1, 1.2, smooth(f / 160))
    return c, (640, 1120, z, 0), 'day'


def s2(f):
    c = corpo_bg().copy()
    b0 = wt(2, 'barulho') - 3
    s0_ = wt(2, 'espremidos') - 3
    sq = pulse(f, s0_, 30)
    put_est(c, 640, 1150, 860, f, 2, expr='shock' if f >= b0 else 'squint', squeeze=sq, look=0)
    for i in range(4):
        bolha(c, 1000 + 50 * (i % 2), 1450 - i * 90 - ((f - s0_) * 1.5 * (i + 1) if f >= s0_ else 0), 22 + 8 * (i % 2))
    if f >= b0:
        rings(c, 1010, 1100, f, b0, 40, 1.3)
        paste_c(c, txt('BLURP!', 150, 7), 640, 560, back(ramp(f, b0, b0 + 8)))
    kk = kick(f, b0 + 2)
    return c, (640, 1150 + kk * 10, 1.12, kk), 'day'


def s3(f):
    c = corpo_bg().copy()
    h0 = wt(3, 'horas') - 3
    v0 = wt(3, 'varre') - 3
    spin = ramp(f, 0, h0 + 6)
    paste_c(c, clock_img(round((1 + spin * 2) * 8) / 8, round(spin * 24 * 4) / 4, 260), 640, 420)
    if f >= h0: paste_c(c, txt('2 HORAS', 110, -5), 640, 680, back(ramp(f, h0, h0 + 8)))
    x = 640 if f < v0 else 640 + (f - v0) * 6
    put_est(c, min(x, 1000), 1250, 760, f, 3, expr='calm' if f < v0 else 'grin', broom=f >= v0 - 10, look=1)
    if f >= v0:
        for i in range(5):
            migalha(c, min(x, 1000) + 240 + i * 50 + (f - v0) * 2, 1560 - (i % 2) * 30, 20, i)
        paste_c(c, txt('VARRE!', 110, 6), 900, 900, back(ramp(f, v0, v0 + 8)))
    z = lerp(1.05, 1.15, smooth(f / 150))
    return c, (680, 1150, z, 0), 'golden'


def s4(f):
    c = corpo_bg().copy()
    c.alpha_composite(tubo_img(), (0, 900))
    b0 = wt(4, 'bacterias') - 3
    r0 = wt(4, 'repete') - 3
    k0 = wt(4, 'comer') - 3
    u0 = .32 + f / 300
    for i in range(4):
        x, y = tubo_pos(u0 - i * .04)
        migalha(c, x, y + 900, 30, i)
    for i in range(3):
        if f >= b0 + i * 3:
            x, y = tubo_pos(u0 - .16 - i * .05)
            put_sprite(c, 'cor', x, y + 900 + 60, 120, 1.0, False, None, col=hexc('#7ccf6a'), expr='dizzy', blink=0, look=1.0)
    x, y = tubo_pos(u0 - .3)
    put_est(c, x, y + 790, 340, f, 4, expr='grin', broom=True, look=1)
    if b0 <= f < r0: paste_c(c, txt('TCHAU, BACTÉRIAS!', 62, -4), 640, 700, back(ramp(f, b0, b0 + 8)))
    if r0 <= f < k0: paste_c(c, txt('A CADA 1-2 HORAS', 60, 4), 640, 700, back(ramp(f, r0, r0 + 8)))
    if f >= k0: paste_c(c, txt('ATÉ COMER!', 100, 5), 640, 700, back(ramp(f, k0, k0 + 8)))
    z = 1.45 + .0006 * f
    return c, (640, 1200, z, 0), 'day'


def s5(f):
    c = corpo_bg().copy()
    a0 = wt(5, 'abafa') - 3
    v0 = wt(5, 'vazia') - 3
    full = f < v0
    put_est(c, 640, 1150, 820, f, 5, expr='calm' if full else 'shock', squeeze=.5 + .5 * math.sin(f * .3), look=0)
    if full:
        for i in range(9):
            migalha(c, 560 + (i % 3) * 70 + 10 * math.sin(f * .2 + i), 1120 + (i // 3) * 60, 28, i)
        rings(c, 1000, 1100, f % 30, 0, 30, .5)
        if f >= a0: paste_c(c, txt('ABAFADO...', 100, -5), 640, 560, back(ramp(f, a0, a0 + 8)))
    else:
        rings(c, 1010, 1100, f, v0, 999, 1.5)
        paste_c(c, txt('RONC! RONC!', 100, 5), 640, 560, back(ramp(f, v0, v0 + 8)))
    kk = kick(f, v0 + 2)
    z = lerp(1.1, 1.25, smooth(f / 150))
    return c, (640, 1150 + kk * 10, z, kk + lerp(0, -2, smooth(f / 150))), 'dusk'


def s6(f):
    c = corpo_bg().copy()
    k = wt(6, 'faxina') - 4
    q0 = wt(6, 'pedindo') - 3
    put_est(c, 640 + 40 * math.sin(f * .12) if f >= k else 640, 1150, 860, f, 6, expr='smug' if f < k else 'grin', broom=f >= k - 2, look=1)
    if q0 <= f < k: paste_c(c, txt('FOME?', 120, -6), 640, 560, back(ramp(f, q0, q0 + 8)))
    if f >= k:
        paste_c(c, txt('FAXINA!', 150, 6), 640, 560, back(ramp(f, k, k + 8)))
        for i in range(4): put_dust(c, 560 + i * 90, 1500, 70, (f - k - i * 3) % 18)
    z = lerp(1.05, 1.3, easeOut(ramp(f, 0, 70)))
    return c, (640, 1150, z, lerp(0, 2.5, smooth(ramp(f, 0, 70)))), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
