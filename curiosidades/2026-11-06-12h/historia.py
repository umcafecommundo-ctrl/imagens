"""Formato DESENHO: por que o astronauta fica mais alto no espaço (Curiosidades da IA, 06/11/2026, 12h). Categoria: ESPAÇO.
Fatos: Scientific American / Space.com "Strange but True: Astronauts Get Taller in Space" (sem a gravidade, as vértebras
se afastam e relaxam; até 3% mais alto, cerca de 5 cm para quem tem 1,80 m; volta ao normal na Terra);
CNN 2016 (astronauta voltou da estação espacial cerca de 5 cm mais alto; "the spine elongates"; volta à altura de antes
pouco depois); Jamaica Hospital Medical Center (de manhã somos cerca de 1 cm mais altos: a gravidade comprime a coluna
durante o dia e ela 'se solta' deitada à noite)."""
from kit import *
import kit

LINES = [
    "Astronauta cresce no espaço. Sério.",
    "Na estação espacial, sem a gravidade puxando pra baixo, a coluna vai se esticando aos pouquinhos.",
    "Os ossinhos das costas, que aqui vivem espremidos, se afastam um pouquinho.",
    "Resultado: o astronauta pode ficar até três por cento mais alto. Uns cinco centímetros!",
    "Você vê, aqui na Terra a gravidade aperta a sua coluna o dia todo. Tanto que, de manhã, você está cerca de um centímetro mais alto que à noite.",
    "Só que, quando o astronauta volta, a gravidade aperta tudo de novo.",
    "Ou seja: o jeito mais caro de ficar mais alto... só dura até voltar pra casa.",
]
CAPTXT = [
    "Astronauta cresce no espaço. Sério.",
    "Na estação espacial, sem a gravidade puxando pra baixo,|a coluna vai se esticando aos pouquinhos.",
    "Os ossinhos das costas, que aqui vivem espremidos,|se afastam um pouquinho.",
    "Resultado: o astronauta pode ficar até 3% mais alto.|Uns 5 centímetros!",
    "Você vê, aqui na Terra a gravidade aperta a sua coluna o dia todo.|Tanto que, de manhã, você está cerca de 1 centímetro mais alto que à noite.",
    "Só que, quando o astronauta volta, a gravidade aperta tudo de novo.",
    "Ou seja: o jeito mais caro de ficar mais alto...|só dura até voltar pra casa.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [5]
CHECK = [(0, 'cresce', 4), (0, 'serio', 4), (1, 'gravidade', 4), (1, 'esticando', 8), (2, 'espremidos', 4), (2, 'afastam', 8),
         (3, 'tres', 4), (3, 'cinco', 6), (4, 'aperta', 4), (4, 'manha', 6), (4, 'noite', 6), (5, 'volta', 6), (5, 'aperta', 6), (6, 'casa', 8)]

SUIT, SUIT_D = hexc('#f4f4f2'), hexc('#c7cbd4')
GREY, GREY_D = hexc('#9aa1ad'), hexc('#6f7683')


# ------------------------------------------------------------------ personagens e objetos novos
def astronaut(expr='neutral', arms='hang', blink=0, look=0.0, stretch=0.0, squash=0.0, skin=1):
    """astronauta (600x1000, pés em y≈975). stretch 0..1 estica o tronco; squash 0..1 achata."""
    p = Pen(600, 1000)
    ex = 70 * stretch - 60 * squash        # quanto o tronco cresce
    hip = 690
    sh_y = 450 - ex
    # pernas
    for s in (-1, 1):
        top = (300 + s * 44, hip); ft = (300 + s * 52, 935)
        p.line([top, (top[0] + s * 6, 820), ft], SUIT, 36, 5)
        p.shape(ell_pts(ft[0] + 10, ft[1] + 12, 48, 26), GREY, GREY_D, 5, 8)
    # mochila (aparece dos lados)
    p.shape([(170, sh_y - 30), (430, sh_y - 30), (440, hip - 30), (160, hip - 30)], GREY, GREY_D, 5, 10)
    # tronco
    p.shape(ell_pts(300, (sh_y + hip) / 2 + 20, 128, (hip - sh_y) / 2 + 70, 56, 0, .1), SUIT, SUIT_D, 6, 18)
    p.shape([(228, (sh_y + hip) / 2 - 10), (372, (sh_y + hip) / 2 - 10), (372, (sh_y + hip) / 2 + 70), (228, (sh_y + hip) / 2 + 70)],
            hexc('#d9dde5'), None, 4)
    for i, col in enumerate(('#e3262b', '#2c6bd6', '#ffd84a')): p.dot(258 + i * 42, (sh_y + hip) / 2 + 30, 11, hexc(col), 3)
    p.dot(205, sh_y + 60, 22, hexc('#2c6bd6'), 4); p.stroke([(197, sh_y + 60), (213, sh_y + 60)], 4, (255, 255, 255))
    # braços
    shL, shR = (190, sh_y + 30), (410, sh_y + 30)
    A = {'hang': [((165, sh_y + 130), (175, sh_y + 220)), ((435, sh_y + 130), (425, sh_y + 220))],
         'up': [((130, sh_y - 60), (120, sh_y - 170)), ((470, sh_y - 60), (480, sh_y - 170))],
         'wave': [((165, sh_y + 130), (175, sh_y + 220)), ((480, sh_y - 30), (520, sh_y - 150))],
         'float': [((110, sh_y + 40), (60, sh_y - 30)), ((490, sh_y + 40), (540, sh_y - 30))],
         'cheek': [((140, sh_y - 40), (190, sh_y - 150)), ((460, sh_y - 40), (410, sh_y - 150))]}[arms]
    for s_, (el, hd) in zip((shL, shR), A):
        p.line(curve(s_, el, hd, 10), SUIT, 32, 5)
        p.dot(hd[0], hd[1], 26, GREY, 5)
    # capacete
    hc = (300, sh_y - 150 + 20 * squash)
    p.shape(ell_pts(hc[0], hc[1], 168, 158, 64), SUIT, SUIT_D, 6, 16)
    p.shape(ell_pts(hc[0], hc[1] + 8, 132, 120, 56), hexc('#2b3550'), None, 5)
    p.shape(ell_pts(hc[0], hc[1] + 18, 112, 98, 56, 0, .06, 2.3), SKINS[skin], mul(SKINS[skin], .86), 4, 12)
    face(p, hc[0], hc[1] + 20, expr, blink, look, u=2.0)
    p.arc(hc[0] - 40, hc[1] - 20, 80, 80, 200, 250, 10, (255, 255, 255))  # reflexo do vidro
    p.stroke([(hc[0] + 70, hc[1] - 80), (hc[0] + 90, hc[1] - 56)], 8, (255, 255, 255))
    return p.img


def put_astro(c, x, feet, h, f, seed=1, rot=0, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('astronaut', tuple(sorted({**kw, 'stretch': round(kw.get('stretch', 0) * 16) / 16,
                                            'squash': round(kw.get('squash', 0) * 8) / 8}.items())), int(h), .6, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    bob = .01 * math.sin((f + seed * 11) * .11) * h
    put(c, im, x, feet + bob + (im.size[1] - int(h)) / 2 + h * .025)


@lru_cache(maxsize=2)
def estacao_bg():
    """interior de um módulo da estação espacial (paredes de painéis, corrimãos, janela redonda com a Terra)."""
    W, H = BW, BH
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc('#d9dde3'))
    for y in range(0, H, 300):
        for x in range(0, W, 310):
            col = hexc('#e8ebef') if ((x // 310) + (y // 300)) % 2 else hexc('#cfd4db')
            p.shape([(x + 12, y + 12), (x + 298, y + 12), (x + 298, y + 288), (x + 12, y + 288)], col, mul(col, .9), 3, 8)
            p.dot(x + 40, y + 40, 6, hexc('#9aa1ad'), 2); p.dot(x + 270, y + 260, 6, hexc('#9aa1ad'), 2)
    for y in (560, 1620):
        p.line([(60, y), (1180, y)], hexc('#f0c24a'), 18, 5)
    # janela redonda
    p.shape(ell_pts(900, 980, 230, 230, 64), hexc('#9aa1ad'), hexc('#6f7683'), 6, 10)
    p.poly(ell_pts(900, 980, 185, 185, 64), hexc('#0e1433'))
    rnd = random.Random(5)
    for i in range(18):
        a, r = rnd.random() * 6.28, rnd.random() * 170
        p.dot(900 + r * math.cos(a), 980 + r * math.sin(a), 3, (255, 255, 230))
    p.shape(ell_pts(920, 1030, 105, 105, 64), hexc('#3a86e0'), hexc('#2458a8'), 4, 12)
    p.shape(ell_pts(895, 995, 42, 28, 32, .4, .2), hexc('#5cc46f'), hexc('#3c9a50'), 3, 6)
    im = p.img.resize((W, H), Image.LANCZOS)
    return im


def vertebra(expr='squish', blink=0):
    """ossinho da coluna com carinha (400x220)."""
    p = Pen(400, 220)
    col = hexc('#f3ead6')
    ry = 52 if expr == 'squish' else 70
    p.shape(ell_pts(200, 110, 170, ry, 48, 0, 0, 2.6), col, hexc('#d8c8a6'), 6, 12)
    p.shape(ell_pts(370, 110, 30, 20, 24), col, hexc('#d8c8a6'), 4, 4)
    for dx in (-36, 36):
        x = 200 + dx
        if blink > .6 or expr == 'squish':
            p.stroke([(x - 14, 104 - (6 if dx < 0 else -6)), (x + 14, 104 + (6 if dx < 0 else -6))], 6) if expr == 'squish' else p.stroke([(x - 14, 100), (x + 14, 100)], 6)
        else:
            p.dot(x, 100, 15, (255, 255, 255), 4); p.dot(x + 3, 102, 7, INK)
    if expr == 'squish':
        pts = [(176 + i * 8, 136 + (4 if i % 2 else -4)) for i in range(7)]; p.stroke(pts, 5)
    else:
        p.arc(200, 128, 22, 12, 20, 160, 6)
    return p.img


def disco(w=300):
    p = Pen(340, 80)
    p.shape(ell_pts(170, 40, 140, 26, 32), hexc('#9fd3ff'), hexc('#6aaedf'), 4, 6)
    return p.img


@lru_cache(maxsize=2)
def regua_img(h=1300):
    p = Pen(160, h)
    p.shape([(20, 0), (140, 0), (140, h), (20, h)], hexc('#ffe08a'), hexc('#e0b84a'), 5, 10)
    for i, y in enumerate(range(20, h, 40)):
        p.stroke([(20, y), (60 if i % 5 else 95, y)], 4)
    return p.img


@lru_cache(maxsize=2)
def seta_img():
    p = Pen(140, 200)
    p.shape([(45, 10), (95, 10), (95, 110), (130, 110), (70, 190), (10, 110), (45, 110)], hexc('#ff6b5a'), hexc('#d24a3c'), 5, 8)
    return p.img


@lru_cache(maxsize=2)
def sol_img(size=240):
    p = Pen(500, 500)
    for i in range(12):
        a = i * math.pi / 6
        p.line([(250 + 150 * math.cos(a), 250 + 150 * math.sin(a)), (250 + 215 * math.cos(a), 250 + 215 * math.sin(a))], hexc('#ffd84a'), 14, 4)
    p.shape(ell_pts(250, 250, 130, 130, 56), hexc('#ffe27a'), hexc('#f5b83a'), 6, 18)
    return p.img.resize((size, size), Image.LANCZOS)


def SFX(s):
    s.thunk(s.W(0, 'cresce') - 2, 150, .8); s.whoosh(s.W(0, 'cresce') - 6, .4, .4)
    s.ting(s.W(0, 'serio'), .3)
    s.whoosh(s.W(1, 'esticando') - 4, .9, .35)
    s.thunk(s.W(2, 'espremidos') - 2, 220, .5)
    s.ting(s.W(2, 'afastam'), .3)
    s.thunk(s.W(3, 'tres') - 2, 160, .7); s.ting(s.W(3, 'cinco'), .35)
    for i in range(3): s.thunk(s.W(4, 'aperta') - 2 + i * 6, 120, .5)
    s.ting(s.W(4, 'manha'), .3)
    s.whoosh(s.W(5, 'volta') - 8, .5, .5); s.thunk(s.W(5, 'volta') + 4, 120, .9)
    s.thunk(s.W(5, 'aperta') - 2, 140, .8)
    s.trill(s.W(6, 'casa'), .9, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = estacao_bg().copy()
    k = wt(0, 'cresce') - 3
    se = wt(0, 'serio') - 3
    st = back(ramp(f, k, k + 8))
    put_astro(c, 520, 1900, 1300, f, 1, rot=6 * math.sin(f * .05), expr='neutral' if f < k else 'shock', arms='float', stretch=clamp(st), look=1)
    if f >= k: paste_c(c, txt('CRESCE?!', 120, -6), 720, 420, back(ramp(f, k, k + 8)))
    if f >= se: paste_c(c, txt('SÉRIO!', 110, 6), 900, 1450, back(ramp(f, se, se + 8)))
    kk = kick(f, k + 2)
    t = easeOut(ramp(f, 0, 40))
    return c, (lerp(560, 640, t), 1200 + kk * 10, lerp(1.35, 1.08, t), kk), 'day'


def s1(f):
    c = estacao_bg().copy()
    g0 = wt(1, 'gravidade') - 3
    e0 = wt(1, 'esticando') - 3
    if f >= g0: paste_c(c, txt('SEM GRAVIDADE', 90, -5), 640, 600, back(ramp(f, g0, g0 + 8)))
    st = .5 + .5 * smooth(ramp(f, e0 - 10, e0 + 30))
    y = 1950 - 60 * math.sin(f * .04)
    put_astro(c, 430, y, 1250, f, 2, rot=-8 + 4 * math.sin(f * .04), expr='grin' if f >= e0 else 'neutral', arms='float', stretch=st if f >= g0 else .5, look=1)
    if f >= e0:
        a = back(ramp(f, e0, e0 + 8))
        paste_c(c, txt('ESTICA...', 90, 8), 860, 1500, a)
    z = lerp(1.05, 1.18, smooth(f / 150))
    return c, (620, 1220, z, 0), 'day'


def s2(f):
    c = BG('lab').copy()
    e0 = wt(2, 'espremidos') - 3
    a0 = wt(2, 'afastam') - 3
    sep = smooth(ramp(f, a0, a0 + 14))
    gap = lerp(118, 190, sep)
    expr = 'squish' if f < a0 else 'calm'
    b = 1 if blinkAt(f, 4) > .6 else 0
    y0 = 1680
    for i in range(6):
        y = y0 - i * gap
        if i < 5: paste_c(c, disco(), 640, y - gap / 2 + 10, lerp(.8, 1.0, sep))
        im = sprite('vertebra', (('blink', b if expr != 'squish' else 0), ('expr', expr)), 200, 2.0, False)
        if f < a0: im = im.resize((400, int(200 * (.9 + .05 * math.sin(f * .6 + i)))))
        paste_c(c, im, 640, y)
    if e0 <= f < a0: paste_c(c, txt('ESPREMIDOS!', 100, -6), 640, 380, back(ramp(f, e0, e0 + 8)))
    if f >= a0: paste_c(c, txt('AAAH...', 110, 6), 640, 380, back(ramp(f, a0, a0 + 8)))
    z = lerp(1.15, 1.05, smooth(ramp(f, a0 - 6, a0 + 20)))
    return c, (640, 1150, z, 0), 'day'


def s3(f):
    c = estacao_bg().copy()
    paste_c(c, regua_img(), 240, 1300)
    t0 = wt(3, 'tres') - 3
    c0 = wt(3, 'cinco') - 3
    st = .5 + .5 * smooth(ramp(f, t0, t0 + 18))
    put_astro(c, 620, 1950, 1250, f, 3, expr='neutral' if f < t0 else 'proud', arms='hang' if f < c0 else 'up', stretch=st, look=-1)
    # marca da altura na régua
    top = 1950 + 1250 * .025 - 1250 + (132 - 70 * st) * 1.25 - 6
    ImageDraw.Draw(c).line([(160, top), (520, top)], fill=(227, 38, 43, 255), width=10)
    if f >= t0: paste_c(c, txt('+3%', 140, -6), 900, 520, back(ramp(f, t0, t0 + 8)))
    if f >= c0: paste_c(c, txt('+5 cm!', 110, 6), 820, 760, back(ramp(f, c0, c0 + 8)))
    kk = kick(f, c0 + 2)
    z = lerp(1.05, 1.15, smooth(f / 120))
    return c, (620, 1200 + kk * 10, z, kk), 'day'


def s4(f):
    c = BG('day').copy()
    a0 = wt(4, 'aperta') - 3
    m0 = wt(4, 'manha') - 3
    n0 = wt(4, 'noite') - 3
    hh = 1150 if f < a0 else lerp(1150, 1110, smooth(ramp(f, a0, a0 + 20)))
    if f >= m0: hh = 1150 if f < n0 else 1110
    put_sci(c, 640, 2080, hh, f, 5, arms='hang' if f < m0 else ('up' if f < n0 else 'hang'), expr='pained' if a0 <= f < m0 else ('grin' if f < n0 else 'neutral'),
            glasses=False, hair='#5b3a22', skin=0, look=0)
    if a0 <= f < m0:
        for i in range(3):
            yy = 420 + ((f - a0) * 9 + i * 120) % 360
            paste_c(c, seta_img(), 400 + i * 220, yy, 1)
        paste_c(c, txt('GRAVIDADE', 100, -4), 640, 760, back(ramp(f, a0, a0 + 8)))
    if m0 <= f < n0:
        paste_c(c, sol_img(240), 960, 600, back(ramp(f, m0, m0 + 10)))
        paste_c(c, txt('MANHÃ: +1 cm', 92, -5), 600, 780, back(ramp(f, m0, m0 + 8)))
    if f >= n0:
        p = Pen(220, 220); p.dot(110, 110, 80, hexc('#fff3c4'), 5)
        for x, y, r in ((80, 90, 16), (135, 130, 12), (120, 70, 9)): p.dot(x, y, r, hexc('#e6d9a8'))
        paste_c(c, p.img.resize((220, 220), Image.LANCZOS), 960, 600, back(ramp(f, n0, n0 + 8)))
        paste_c(c, txt('NOITE', 110, 5), 600, 780, back(ramp(f, n0, n0 + 8)))
    z = lerp(1.05, 1.15, smooth(f / 200))
    return c, (640, 1200, z, 0), 'dusk' if f >= n0 else 'day'


def s5(f):
    c = BG('day').copy()
    v0 = wt(5, 'volta') - 3
    a0 = wt(5, 'aperta') - 3
    land = v0 + 6
    if f < land:
        y = lerp(-200, 2000, easeOut(ramp(f, v0 - 14, land)))
    else:
        y = 2000
    sq = pulse(f, a0, 10) * .8
    put_astro(c, 640, y, 1250, f, 4, expr='shock' if f >= a0 else 'neutral', arms='up' if f < land else 'hang',
              stretch=1.0 if f < a0 else lerp(1.0, 0.0, smooth(ramp(f, a0, a0 + 10))), squash=sq, look=0)
    put_dust(c, 520, 1990, 120, f - land); put_dust(c, 760, 1990, 120, f - land - 2)
    if f >= land: paste_c(c, txt('TUM!', 120, -8), 1000, 1100, back(ramp(f, land, land + 8)))
    if f >= a0: paste_c(c, txt('APERTOU!', 110, 6), 640, 480, back(ramp(f, a0, a0 + 8)))
    kk = kick(f, land) + kick(f, a0, .6)
    return c, (640, 1250 + kk * 10, 1.1, kk), 'day'


def s6(f):
    c = BG('golden').copy()
    k = wt(6, 'casa') - 3
    put_astro(c, 620, 2050, 1150, f, 6, expr='smug' if f < k else 'pained', arms='hang' if f < k else 'cheek', stretch=0, look=0)
    c0 = wt(6, 'caro') - 3
    if c0 <= f < k: paste_c(c, txt('CARO!', 130, -6), 640, 720, back(ramp(f, c0, c0 + 8)))
    if f >= k: paste_c(c, txt('TCHAU, 5 cm!', 100, 6), 640, 720, back(ramp(f, k, k + 8)))
    z = lerp(1.0, 1.15, easeOut(ramp(f, 0, 70)))
    return c, (630, 1300, z, lerp(0, -3, smooth(ramp(f, 0, 70)))), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
