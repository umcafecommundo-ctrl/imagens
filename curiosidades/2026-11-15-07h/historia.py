"""Formato DESENHO: o vombate faz cocô em formato de cubo (Curiosidades da IA, 15/11/2026, 07h).
Categoria: ANIMAIS.
Fatos: Smithsonian Magazine (2021, "Scientists Have Solved the Mystery of How Wombats Poop Cubes", estudo de
Yang et al., Soft Matter 2021, Georgia Tech/Univ. da Tasmânia) e Science News: vombates vivem na Austrália;
fazem até ~100 cubos por dia, de ~2 cm; espalham os cubos pelo território, em cima de pedras e troncos, e o
formato ajuda a não rolar; o intestino tem partes mais duras e mais elásticas que contraem diferente e formam
as quinas.
Cenários: s0 floresta da Austrália (Professor + vombate) | s1 floresta (cubos) | s2 floresta (pedra e tronco) |
s3 dentro do corpo (intestino moldando o cubo) | s4 floresta (bolinha rola, cubo fica) | s5 floresta ao entardecer
(Professor reage)."""
from kit import *

LINES = [
    "O vombate, um bicho da Austrália, faz cocô em formato de cubo.",
    "São até cem cubinhos por dia, de uns dois centímetros.",
    "Ele espalha o cocô em cima de pedras e troncos, pra marcar território.",
    "Você vê, no intestino dele, partes duras e partes moles apertam diferente e fazem as quinas.",
    "E o cubo, ao contrário de uma bolinha, não sai rolando da pedra.",
    "Ou seja: ele marca território... com dadinhos.",
]
CAPTXT = [
    "O vombate, um bicho da Austrália,|faz cocô em formato de cubo.",
    "São até 100 cubinhos por dia,|de uns 2 centímetros.",
    "Ele espalha o cocô em cima de pedras e troncos,|pra marcar território.",
    "Você vê, no intestino dele, partes duras e partes moles|apertam diferente e fazem as quinas.",
    "E o cubo, ao contrário de uma bolinha,|não sai rolando da pedra.",
    "Ou seja: ele marca território... com dadinhos.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'cubo', 6), (1, 'cem', 6), (2, 'pedras', 4), (2, 'troncos', 4), (3, 'duras', 4), (3, 'quinas', 6),
         (4, 'bolinha', 4), (4, 'rolando', 6), (5, 'dadinhos', 8)]

VB = '#9a7454'; VBD = '#6f5038'; NOSE = '#3a2a24'; COCO = '#6b4428'; COCOD = '#4a2e1a'


def vombate(expr='calm', blink=0, look=0.4, step=0.0):
    """vombate de lado olhando p/ direita (700x500), pés em y≈490."""
    p = Pen(700, 500)
    for i, x in enumerate((190, 260, 470, 540)):
        dx = 12 * math.sin(step * 6.28 + i * 1.6)
        p.shape([(x - 30, 360), (x + 30, 360), (x + 34 + dx, 488), (x - 30 + dx, 488)], hexc(VBD), None, 5, 0)
    p.shape(ell_pts(340, 320, 270, 160, 64, 0, .05), hexc(VB), hexc(VBD), 6, 18)
    # cabeça
    p.shape(ell_pts(530, 270, 120, 105, 48), hexc(VB), hexc(VBD), 6, 12)
    for ex_, ey_ in ((470, 165), (545, 160)):
        p.shape(ell_pts(ex_, ey_, 30, 36, 24), hexc(VB), hexc(VBD), 5, 4)
    p.shape(ell_pts(630, 290, 42, 38, 32), hexc(NOSE), None, 5, 0)
    p.dot(620, 280, 7, hexc('#7a6a64'))
    ex, ey = 550, 240
    if blink: p.stroke([(ex - 20, ey), (ex + 20, ey)], 6)
    else:
        r = 30 if expr == 'shock' else 24
        p.dot(ex, ey, r, (255, 255, 255), 5)
        p.dot(ex + look * 9, ey + 2, 11, INK); p.dot(ex + look * 9 - 4, ey - 3, 3.5, (255, 255, 255))
        if expr == 'smug':
            p.poly([(ex - r - 4, ey - r - 4), (ex + r + 4, ey - r - 4), (ex + r + 4, ey - 4), (ex - r - 4, ey - 4)], hexc(VB))
            p.stroke([(ex - r, ey - 4), (ex + r, ey - 4)], 6)
    if expr == 'smug': p.arc(580, 335, 30, 12, 20, 160, 6)
    elif expr == 'shock': p.dot(585, 345, 12, hexc('#7a2e2e'), 4)
    else: p.stroke([(565, 340), (600, 342)], 5)
    return p.img


def put_vomb(c, x, feet, h, f, seed=1, flip=False, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    put_sprite(c, 'vombate', x, feet, h, 700 / 500, flip, {'step': 4, 'look': 4}, **kw)


@lru_cache(maxsize=64)
def cubo_img(w, rot=0, face_=False):
    p = Pen(300, 300)
    p.shape([(60, 110), (190, 110), (190, 250), (60, 250)], hexc(COCO), hexc(COCOD), 6, 10)
    p.shape([(60, 110), (110, 60), (240, 60), (190, 110)], mul(hexc(COCO), 1.25), None, 6, 0)
    p.shape([(190, 110), (240, 60), (240, 200), (190, 250)], hexc(COCOD), None, 6, 0)
    if face_:
        for dx in (95, 155): p.dot(dx, 165, 10, (255, 255, 255))
        for (x, y) in ((140, 85), (175, 78)): p.dot(x, y, 8, (255, 255, 255))
        p.dot(215, 140, 8, (255, 255, 255)); p.dot(215, 180, 8, (255, 255, 255))
    im = p.img.rotate(rot, Image.BICUBIC)
    return im.resize((w, w), Image.LANCZOS)


def cubo(c, x, base, w, rot=0, face_=False):
    if w < 6: return
    im = cubo_img(int(w), int(rot), face_)
    c.alpha_composite(im, (int(x - w / 2), int(base - w * 250 / 300)))


@lru_cache(maxsize=8)
def bola_img(w):
    p = Pen(200, 200)
    p.shape(ell_pts(100, 100, 80, 80), hexc(COCO), hexc(COCOD), 6, 12)
    return p.img.resize((w, w), Image.LANCZOS)


@lru_cache(maxsize=4)
def pedra_img(w):
    p = Pen(600, 360)
    p.shape([(30, 350), (60, 170), (170, 70), (420, 60), (540, 150), (580, 350)], hexc('#a7a39b'), hexc('#7d7a73'), 6, 22)
    return p.img.resize((w, int(w * 360 / 600)), Image.LANCZOS)


@lru_cache(maxsize=4)
def tronco_img(w):
    p = Pen(700, 260)
    p.shape([(40, 60), (620, 60), (620, 230), (40, 230)], hexc('#8a5a34'), hexc('#5e3c22'), 6, 14)
    p.shape(ell_pts(620, 145, 50, 86), hexc('#d7a96e'), hexc('#b0834e'), 6, 4)
    for r in (20, 40, 60): p.arc(620, 145, r * .6, r, 0, 360, 4)
    return p.img.resize((w, int(w * 260 / 700)), Image.LANCZOS)


@lru_cache(maxsize=4)
def tripa_img(w):
    """intestino em corte: tubo rosa horizontal com faixas duras (escuras) e moles (claras)."""
    p = Pen(1100, 520)
    p.shape([(20, 90), (1080, 90), (1080, 430), (20, 430)], hexc('#f29aa6'), hexc('#d06d7c'), 6, 14)
    p.shape([(20, 160), (1080, 160), (1080, 360), (20, 360)], hexc('#5a1f2a'), None, 0, 0)
    for i in range(6):
        x = 60 + i * 170
        col = '#b8455a' if i % 2 == 0 else '#ffc4cc'
        p.shape([(x, 95), (x + 120, 95), (x + 120, 160), (x, 160)], hexc(col), None, 4, 0)
        p.shape([(x, 360), (x + 120, 360), (x + 120, 425), (x, 425)], hexc(col), None, 4, 0)
    return p.img.resize((w, int(w * 520 / 1100)), Image.LANCZOS)


def SFX(s):
    s.thunk(s.W(0, 'cubo') - 2, 180, .8)
    for i in range(5): s.thunk(s.W(1, 'cem') - 2 + i * 4, 260, .4)
    s.thunk(s.W(2, 'pedras') - 2, 200, .6); s.thunk(s.W(2, 'troncos') - 2, 220, .6)
    s.ting(s.W(2, 'territorio'), .3)
    s.patter(s.W(3, 'apertam'), s.W(3, 'quinas'), 10, .12)
    s.thunk(s.W(3, 'quinas') - 2, 160, .7)
    s.whoosh(s.W(4, 'bolinha') - 4, .5, .4)
    s.thunk(s.W(4, 'rolando') - 2, 260, .5)
    s.trill(s.W(5, 'dadinhos'), 1.0, .3)


def s0(f):
    c = CEN('floresta', 'day').copy()
    k = wt(0, 'cubo') - 3
    v = wt(0, 'vombate') - 3
    put_vomb(c, 880, 1720, 420 * back(ramp(f, v, v + 9)), f, 2, flip=True, expr='smug' if f >= k else 'calm', look=1)
    put_dust(c, 880, 1700, 90, f - v)
    put_prof(c, 400, 1760, 900, f, expr='shock' if f >= k else 'grin', arms='point' if f >= v else 'wave', look=1)
    if f >= k:
        cubo(c, 640, 1740, 150 * back(ramp(f, k, k + 8)))
        paste_c(c, txt('CUBO?!', 130, -6), 680, 820, back(ramp(f, k, k + 8)))
    z = lerp(1.35, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1300 + kick(f, k, .7) * 10, z, 0), 'day'


def s1(f):
    c = CEN('floresta', 'day').copy()
    k = wt(1, 'cem') - 3
    d = wt(1, 'dois') - 3
    put_vomb(c, 370, 1720, 320, f, 3, look=.5)
    for i in range(10):
        s = back(ramp(f, k + i * 2, k + i * 2 + 7))
        x = 630 + (i % 5) * 78; y = 1730 - (i // 5) * 110
        cubo(c, x, y, 110 * s)
    if f >= k: paste_c(c, txt('100 POR DIA', 110, -5), 640, 860, back(ramp(f, k, k + 8)))
    if f >= d: paste_c(c, txt('2 cm', 100, 6), 740, 1100, back(ramp(f, d, d + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (640, 1300 + kick(f, k, .5) * 8, z, 0), 'day'


def s2(f):
    c = CEN('floresta', 'day').copy()
    pd = wt(2, 'pedras') - 3
    tr = wt(2, 'troncos') - 3
    tt = wt(2, 'territorio') - 3
    paste_c(c, pedra_img(420), 330, 1600)
    paste_c(c, tronco_img(500), 900, 1640)
    put_vomb(c, 640, 1760, 360, f, 4, look=.2, step=(f % 30) / 30 if f < pd else 0)
    if f >= pd: cubo(c, 330, 1505, 140 * back(ramp(f, pd, pd + 8)))
    if f >= tr: cubo(c, 980, 1580, 140 * back(ramp(f, tr, tr + 8)))
    if f >= tt: paste_c(c, txt('MEU PEDAÇO!', 100, -5), 640, 880, back(ramp(f, tt, tt + 8)))
    z = lerp(1.25, 1.1, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1320 + kick(f, pd, .5) * 8, z, 0), 'day'


def s3(f):
    c = CEN('corpo', 'dusk').copy()
    du = wt(3, 'duras') - 3
    mo = wt(3, 'moles') - 3
    q = wt(3, 'quinas') - 3
    T = tripa_img(1100)
    sq = 1 + .04 * math.sin(f * .5)
    c.alpha_composite(T, (71, 1000))
    prog = ramp(f, 0, q)
    x = 200 + 800 * prog
    rot = 0
    # massa que vira cubo: começa bolinha e ganha quinas
    if f < q - 10:
        paste_c(c, bola_img(int(170 * sq)), x, 1245)
    else:
        cubo(c, x - 10, 1320, 190, 0)
    if f >= du: paste_c(c, txt('DURO', 90, 0), 430, 900, back(ramp(f, du, du + 8)))
    if f >= mo: paste_c(c, txt('MOLE', 90, 0), 820, 900, back(ramp(f, mo, mo + 8)))
    if f >= q: paste_c(c, txt('QUINAS!', 120, -6), 640, 690, back(ramp(f, q, q + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.15, 1.3, t) * (1 + .0009 * f)
    return c, (621, 1200 + kick(f, q, .7) * 10, z, lerp(0, 2, t)), 'dusk'


def s4(f):
    c = CEN('floresta', 'day').copy()
    b = wt(4, 'bolinha') - 3
    r = wt(4, 'rolando') - 3
    paste_c(c, pedra_img(560), 621, 1580)
    cubo(c, 720, 1462, 130)
    if f >= b:
        t = ramp(f, b + 4, b + 30)
        bx = 520 - 380 * t; by = 1400 + 260 * t * t
        if t <= 0: by = 1400
        im = bola_img(110).rotate(-f * 25 if t > 0 else 0)
        paste_c(c, im, bx, by, back(ramp(f, b, b + 6)))
    if f >= r: paste_c(c, txt('O CUBO FICA!', 100, 5), 640, 900, back(ramp(f, r, r + 8)))
    put_vomb(c, 950, 1800, 300, f, 5, flip=True, expr='smug' if f >= r else 'calm', look=1)
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (640, 1320 + kick(f, r, .5) * 8, z, 0), 'day'


def s5(f):
    c = CEN('floresta', 'dusk').copy()
    d = wt(5, 'dadinhos') - 3
    put_prof(c, 330, 1780, 920, f, expr='smug' if f < d else 'grin', arms='chin' if f < d else 'shrug', look=1)
    put_vomb(c, 880, 1760, 400, f, 6, flip=True, expr='smug', look=1)
    if f >= d:
        for i, (x, rt) in enumerate(((620, -12), (700, 18), (780, -4))):
            cubo(c, x, 1760, 100 * back(ramp(f, d + i * 3, d + i * 3 + 8)), rt, True)
        paste_c(c, txt('DADINHOS!', 120, -6), 640, 860, back(ramp(f, d, d + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.25, t) * (1 + .0012 * f)
    return c, (621, lerp(1320, 1280, t), z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
