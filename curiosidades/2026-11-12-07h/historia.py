"""Formato DESENHO: no espaço a lágrima não cai (Curiosidades da IA, 12/11/2026, 07h). Categoria: ESPAÇO.
Fatos: Space.com, "How Astronauts Cry In Space (Video)" (2013): demonstração gravada na Estação Espacial Internacional
por um astronauta da Agência Espacial Canadense, que espirrou água no próprio olho; na microgravidade a lágrima não cai,
forma uma bola de água sobre o olho que vai crescendo e pode atravessar o nariz até o outro olho; pode se soltar em
gotinhas que flutuam. ScienceABC / facts.museum: sem gravidade, a água fica grudada no rosto por tensão superficial."""
from kit import *
import kit

LINES = [
    "No espaço, a lágrima não cai.",
    "Na estação espacial, um astronauta testou: espirrou água no próprio olho.",
    "A água não escorreu. Virou uma bola grudada no olho, que só crescia.",
    "Você vê, sem gravidade, nada puxa a lágrima pra baixo. Ela fica grudada no rosto.",
    "E se crescer demais, atravessa o nariz e vai parar no outro olho.",
    "Ou seja: no espaço, chorar é fácil. Difícil é enxergar depois.",
]
CAPTXT = [
    "No espaço, a lágrima não cai.",
    "Na estação espacial, um astronauta testou:|espirrou água no próprio olho.",
    "A água não escorreu.|Virou uma bola grudada no olho, que só crescia.",
    "Você vê, sem gravidade, nada puxa a lágrima pra baixo.|Ela fica grudada no rosto.",
    "E se crescer demais, atravessa o nariz|e vai parar no outro olho.",
    "Ou seja: no espaço, chorar é fácil.|Difícil é enxergar depois.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'lagrima', 4), (0, 'cai', 6), (1, 'testou', 4), (1, 'espirrou', 4), (1, 'olho', 6), (2, 'bola', 4), (2, 'crescia', 8),
         (3, 'gravidade', 4), (3, 'baixo', 6), (4, 'nariz', 4), (4, 'outro', 6), (5, 'facil', 4), (5, 'enxergar', 8)]

AGUA, AGUA_D = hexc('#bfe6ff'), hexc('#7fc0ec')


# ------------------------------------------------------------------ personagens e objetos novos
def astro(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=1, bola=0.0, cruza=0.0):
    """astronauta sem capacete, de camisa polo azul (600x1000, pés em y≈975). bola 0..1 = bola de água no olho;
    cruza 0..1 = a bola atravessa o nariz e cobre os dois olhos."""
    p = Pen(600, 1000)
    sh, shd = hexc('#2f5fb3'), hexc('#22457f')
    for s in (-1, 1):
        top = (300 + s * 40, 690); ft = (300 + s * 44, 950)
        p.line([top, (top[0] + s * 4, 820), ft], hexc('#5b6270'), 24, 4)
        p.shape(ell_pts(ft[0] + 12, ft[1] + 10, 36, 18), hexc('#f2f2f2'), hexc('#c9c9c9'), 4, 4)
    p.shape([(212, 640), (388, 640), (396, 712), (204, 712)], hexc('#5b6270'), hexc('#41464f'), 5, 8)
    p.line([(300, 350), (300, 430)], SKINS[skin], 40, 4)
    tc = (300 + tilt * 3, 560)
    p.shape(ell_pts(tc[0], tc[1], 112, 140, 56, math.radians(tilt), 0.12), sh, shd, 5, 16)
    p.poly([(262, 424), (338, 424), (300, 470)], hexc('#f4f4f2'), 3)          # gola
    p.dot(245, 500, 16, hexc('#e3262b'), 3); p.dot(245, 500, 7, hexc('#ffffff'))   # emblema
    shL, shR = (205, 470), (395, 470)
    A = {'hang': [((185, 560), (190, 650)), ((415, 560), (410, 650))],
         'float': [((140, 470), (90, 400)), ((460, 470), (510, 400))],
         'bottle': [((185, 560), (190, 650)), ((470, 430), (430, 300))],
         'up': [((150, 380), (140, 240)), ((450, 380), (460, 240))],
         'grope': [((120, 420), (70, 330)), ((480, 400), (540, 290))]}[arms]
    for s_, (el, hd) in zip((shL, shR), A):
        p.line(curve(s_, el, hd, 10), sh if True else SKINS[skin], 16, 4)
        p.dot(hd[0], hd[1], 17, SKINS[skin], 4)
    hc = (300 + tilt * 6, 262)
    hcol = hexc('#3b2a1e')
    p.shape(ell_pts(hc[0], hc[1], 118, 106, 56, math.radians(tilt * 1.5), 0.08, 2.4), SKINS[skin], mul(SKINS[skin], .86), 5, 16)
    p.dot(hc[0] - 112, hc[1] + 10, 16, SKINS[skin], 4); p.dot(hc[0] + 112, hc[1] + 10, 16, SKINS[skin], 4)
    fr = [(hc[0] - 122, hc[1] - 6), (hc[0] - 116, hc[1] - 84), (hc[0] - 50, hc[1] - 118), (hc[0] + 50, hc[1] - 118), (hc[0] + 116, hc[1] - 84),
          (hc[0] + 122, hc[1] - 10), (hc[0] + 80, hc[1] - 56), (hc[0] + 20, hc[1] - 74), (hc[0] - 50, hc[1] - 60), (hc[0] - 96, hc[1] - 36)]
    p.shape(fr, hcol, mul(hcol, .7), 5, 8)
    face(p, hc[0], hc[1] + 10, expr, blink, look)
    if bola > .02:
        ex = hc[0] + 31
        cx = lerp(ex, hc[0], cruza); cy = hc[1] + 10
        r = lerp(16 + 30 * bola, 78, cruza)
        rx = r * lerp(1.0, 1.25, cruza)
        p.shape(ell_pts(cx, cy, rx, r * .95, 48), AGUA, AGUA_D, 4, 8)
        p.dot(cx - rx * .4, cy - r * .4, max(3, r * .18), (255, 255, 255))
        p.dot(cx + rx * .35, cy + r * .3, max(2, r * .08), (255, 255, 255))
    return p.img


def put_astro(c, x, feet, h, f, seed, **kw):
    for k in ('bola', 'cruza'):
        if k in kw: kw[k] = round(kw[k] * 12) / 12
    kit._bean(c, 'astro', x, feet, h, f, seed, **kw)


@lru_cache(maxsize=2)
def garrafa(size=200):
    p = Pen(200, 340)
    p.shape([(60, 110), (140, 110), (150, 320), (50, 320)], hexc('#e9f6ff'), hexc('#b9d8ec'), 5, 8)
    p.poly([(55, 190), (145, 190), (147, 250), (53, 250)], hexc('#ff6b5a'), 3)
    p.shape([(80, 60), (120, 60), (124, 110), (76, 110)], hexc('#9aa1ad'), hexc('#6f7683'), 4, 4)
    p.shape([(94, 10), (106, 10), (108, 60), (92, 60)], hexc('#9aa1ad'), hexc('#6f7683'), 4, 2)
    return p.img.resize((int(size * 200 / 340), size), Image.LANCZOS)


@lru_cache(maxsize=16)
def gota(r=24):
    p = Pen(100, 100)
    p.shape(ell_pts(50, 50, r, r, 32), AGUA, AGUA_D, 3, 4)
    p.dot(50 - r * .35, 50 - r * .35, max(2, r * .2), (255, 255, 255))
    return p.img


@lru_cache(maxsize=2)
def seta_x():
    """seta para baixo riscada (sem gravidade = nada puxa)."""
    p = Pen(260, 340)
    p.shape([(95, 10), (165, 10), (165, 170), (225, 170), (130, 320), (35, 170), (95, 170)], hexc('#9fd3ff'), hexc('#6aaedf'), 5, 8)
    p.line([(20, 40), (240, 300)], hexc('#e3262b'), 26, 5)
    p.line([(240, 40), (20, 300)], hexc('#e3262b'), 26, 5)
    return p.img


@lru_cache(maxsize=4)
def bg(luz='day'):
    return CEN('estacao', luz)


def SFX(s):
    s.thunk(s.W(0, 'cai') - 2, 150, .8)
    s.ting(s.W(0, 'lagrima'), .3)
    s.ting(s.W(1, 'testou'), .3)
    s.splash(s.W(1, 'espirrou') - 2) if hasattr(s, 'splash') else s.whoosh(s.W(1, 'espirrou') - 4, .4, .4)
    s.thunk(s.W(2, 'bola') - 2, 220, .5)
    s.whoosh(s.W(2, 'crescia') - 4, .8, .35)
    s.thunk(s.W(3, 'baixo') - 2, 160, .6)
    s.whoosh(s.W(4, 'nariz') - 6, .5, .4); s.thunk(s.W(4, 'outro') - 2, 260, .6)
    s.ting(s.W(5, 'facil'), .3)
    s.trill(s.W(5, 'enxergar'), .9, .3)


def flutua(f, seed=1, amp=30):
    return amp * math.sin((f + seed * 13) * .06)


# ---------------------------------------------------------------- cenas (todas dentro da estação espacial)
def s0(f):
    c = bg('day').copy()
    l0 = wt(0, 'lagrima') - 3
    k = wt(0, 'cai') - 3
    b = .5 * back(ramp(f, l0, l0 + 8)) if f >= l0 else 0
    put_astro(c, 520, 2080 + flutua(f), 1500, f, 1, expr='pained' if f >= l0 else 'neutral', arms='float', bola=clamp(b), look=1)
    if f >= k: paste_c(c, txt('NÃO CAI!', 120, -6), 720, 560, back(ramp(f, k, k + 8)))
    kk = kick(f, k + 2)
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.4, 1.1, t) * (1 + .0009 * f)
    return c, (lerp(560, 620, t), 1150 + kk * 10, z, kk), 'day'


def s1(f):
    c = bg('day').copy()
    t0 = wt(1, 'testou') - 3
    e0 = wt(1, 'espirrou') - 3
    o0 = wt(1, 'olho') - 3
    hold = f >= t0
    x, feet, h = 560, 2020 + flutua(f, 2, 20), 1400
    put_astro(c, x, feet, h, f, 2, expr='grin' if f < e0 else 'shock', arms='bottle' if hold else 'float',
              bola=.35 * smooth(ramp(f, o0 - 2, o0 + 8)), look=.6)
    s = h / 1000
    hx, hy = x - 300 * s + 430 * s, feet - 975 * s + 300 * s
    if hold: paste_c(c, garrafa(int(220 * s / 1.4)), hx + 20, hy - 40, back(ramp(f, t0, t0 + 8)))
    if e0 <= f < e0 + 16:
        for i in range(4):
            a = (f - e0) / 16
            paste_c(c, gota(14), lerp(hx, x + 40 * s, a) - i * 12, lerp(hy - 140, feet - 975 * s + 272 * s, a) + i * 10)
    if f >= t0: paste_c(c, txt('TESTE!', 110, 6), 420, 560, back(ramp(f, t0, t0 + 8)))
    z = lerp(1.1, 1.3, smooth(f / 150)) * (1 + .0009 * f)
    return c, (600, 1150, z, 0), 'day'


def s2(f):
    c = bg('day').copy()
    b0 = wt(2, 'bola') - 3
    g0 = wt(2, 'crescia') - 3
    bola = .35 + .25 * smooth(ramp(f, b0, b0 + 10)) + .4 * smooth(ramp(f, g0, g0 + 30))
    put_astro(c, 620, 2500 + flutua(f, 3, 12), 2300, f, 3, expr='shock', arms='hang', bola=bola, look=-.4)
    if f >= b0: paste_c(c, txt('BOLA!', 110, -6), 420, 450, back(ramp(f, b0, b0 + 8)))
    if f >= g0: paste_c(c, txt('CRESCE...', 80, 6), 860, 450, back(ramp(f, g0, g0 + 8)))
    z = lerp(1.05, 1.25, smooth(f / 120)) * (1 + .0009 * f)
    return c, (640, 1050, z, 0), 'day'


def s3(f):
    c = bg('dusk').copy()
    g0 = wt(3, 'gravidade') - 3
    b0 = wt(3, 'baixo') - 3
    r0 = wt(3, 'rosto') - 3
    put_astro(c, 460, 2150 + flutua(f, 4, 15), 1700, f, 4, expr='neutral' if f < r0 else 'smug', arms='float', bola=1.0, look=1)
    if f >= g0: paste_c(c, txt('SEM GRAVIDADE', 80, -5), 640, 480, back(ramp(f, g0, g0 + 8)))
    if f >= b0: paste_c(c, seta_x(), 820, 1220, back(ramp(f, b0, b0 + 8)))
    if f >= r0: paste_c(c, txt('GRUDA!', 100, 6), 860, 820, back(ramp(f, r0, r0 + 8)))
    z = lerp(1.08, 1.22, smooth(f / 150)) * (1 + .0009 * f)
    return c, (640, 1150, z, -1.5 * smooth(f / 150)), 'dusk'


def s4(f):
    c = bg('day').copy()
    n0 = wt(4, 'nariz') - 3
    o0 = wt(4, 'outro') - 3
    cr = smooth(ramp(f, n0, o0 + 6))
    put_astro(c, 620, 2500 + flutua(f, 5, 12), 2300, f, 5, expr='shock' if f >= n0 else 'nervous', arms='hang', bola=1.0, cruza=cr, look=0)
    if f >= o0: paste_c(c, txt('OUTRO OLHO!', 96, -6), 640, 420, back(ramp(f, o0, o0 + 8)))
    kk = kick(f, o0 + 2)
    z = lerp(1.15, 1.3, smooth(f / 120)) * (1 + .0009 * f)
    return c, (640, 1050 + kk * 10, z, kk), 'day'


def s5(f):
    c = bg('dusk').copy()
    fa = wt(5, 'facil') - 3
    e0 = wt(5, 'enxergar') - 3
    put_astro(c, 600, 2080 + flutua(f, 6, 25), 1500, f, 6, expr='nervous', arms='grope' if f >= e0 else 'float', bola=1.0, cruza=1.0)
    rnd = random.Random(7)
    for i in range(6):
        x0, y0 = rnd.randint(150, 1100), rnd.randint(350, 1300)
        paste_c(c, gota(rnd.randint(12, 26)), x0 + 20 * math.sin(f * .05 + i), y0 + 25 * math.cos(f * .04 + i))
    if f >= fa: paste_c(c, txt('FÁCIL!', 100, -6), 420, 540, back(ramp(f, fa, fa + 8)))
    if f >= e0: paste_c(c, txt('CADÊ?', 100, 6), 800, 720, back(ramp(f, e0, e0 + 8)))
    z = lerp(1.05, 1.2, easeOut(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (630, 1150, z, -2 * smooth(f / 120)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
