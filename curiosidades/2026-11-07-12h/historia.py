"""Formato DESENHO: o polvo tem três corações e sangue azul (Curiosidades da IA, 07/11/2026, 12h). Categoria: ANIMAIS.
Fatos: Live Science, "How many hearts does an octopus have?" (3 corações: 2 branquiais, um para cada guelra, empurram o
sangue pelas guelras; o sistêmico, o maior, manda o sangue para o corpo; sangue azul por causa da hemocianina, proteína
com cobre; ao nadar o coração sistêmico para por instantes, e por isso o polvo prefere andar a nadar);
Smithsonian Ocean (o coração sistêmico para quando ele nada, o que explica a preferência por rastejar: nadar o cansa);
nosso sangue usa hemoglobina, com ferro (enciclopédias)."""
from kit import *
import kit

LINES = [
    "O polvo tem três corações, e o sangue dele é azul.",
    "Dois corações ficam do lado das guelras, e só servem pra empurrar o sangue por elas.",
    "O terceiro, o maior, manda o sangue pro resto do corpo.",
    "E o sangue é azul porque carrega o oxigênio usando cobre, e não ferro, como o nosso.",
    "Você vê, quando o polvo sai nadando, o coração principal para de bater por uns instantes.",
    "Por isso nadar cansa tanto, e o polvo prefere ir andando pelo fundo do mar.",
    "Ou seja: o bicho tem três corações... e mesmo assim prefere ir a pé.",
]
CAPTXT = [
    "O polvo tem três corações,|e o sangue dele é azul.",
    "Dois corações ficam do lado das guelras,|e só servem pra empurrar o sangue por elas.",
    "O terceiro, o maior,|manda o sangue pro resto do corpo.",
    "E o sangue é azul porque carrega o oxigênio usando cobre,|e não ferro, como o nosso.",
    "Você vê, quando o polvo sai nadando,|o coração principal para de bater por uns instantes.",
    "Por isso nadar cansa tanto,|e o polvo prefere ir andando pelo fundo do mar.",
    "Ou seja: o bicho tem três corações...|e mesmo assim prefere ir a pé.",
]
FALA_TIKTOK = "Você sabia dos três corações? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [3]
CHECK = [(0, 'tres', 4), (0, 'azul', 6), (1, 'guelras', 4), (1, 'empurrar', 6), (2, 'maior', 4), (2, 'corpo', 6),
         (3, 'cobre', 4), (3, 'ferro', 6), (4, 'nadando', 4), (4, 'para', 6), (5, 'cansa', 4), (5, 'andando', 6),
         (6, 'tres', 4), (6, 'pe', 8)]

PV, PVD = hexc('#e8735a'), hexc('#c4523f')
AZUL = hexc('#3d7bea')
CORA, CORAD = hexc('#ff5a6e'), hexc('#cc3b50')


def heart_pts(cx, cy, s):
    pts = []
    for i in range(40):
        t = i / 40 * 2 * math.pi
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((cx + x * s, cy - y * s))
    return pts


def polvo(expr='calm', blink=0, look=0.3, xray=0, b1=0.0, b2=0.0, stop=0, swim=0.0, phase=0.0, sweat=0):
    """polvo (700x800, 'pés' em y≈780). xray mostra os 3 corações; b1/b2 = batida dos pequenos/grande."""
    p = Pen(700, 800)
    # braços: 8 tentáculos ondulados; swim junta e estica pra baixo
    for i in range(8):
        base = (210 + i * 40, 420)
        spread = (i - 3.5) * lerp(44, 12, swim)
        pts = []
        for k in range(9):
            u = k / 8
            x = base[0] + spread * u * 1.9 + 28 * math.sin(phase * 2 * math.pi + i * .9 + u * 4) * u * (1 - swim * .6)
            y = base[1] + u * lerp(330, 345, swim) - (40 * u * u if swim < .5 and abs(i - 3.5) > 2 else 0)
            pts.append((x, y))
        p.line(pts, PV if i % 2 else PVD, lerp(46, 26, 1) * (1 + 0 * i), 5)
    # manto (cabeça)
    p.shape(ell_pts(350, 240, 190 - 10 * swim, 225, 64, 0, -.25), PV, PVD, 7, 26)
    for x, y, r in ((270, 120, 18), (420, 150, 14), (330, 200, 10), (450, 80, 10)):
        p.dot(x, y - 20 * swim, r, PVD)
    if xray:
        p.shape(ell_pts(350, 230, 150, 150, 48), hexc('#ffd3c9'), None, 4)
        for s, gx in ((-1, 250), (1, 450)):  # guelras
            for k in range(5):
                p.stroke([(gx, 160 + k * 26), (gx + s * 40, 150 + k * 26)], 7, hexc('#c06a8a'))
            sc = 2.2 * (1 + .25 * b1)
            p.shape(heart_pts(gx + s * 10, 280, sc), CORA, CORAD, 4, 4)
        sc = 3.6 * (1 + .25 * b2)
        col = (hexc('#9a9a9a'), hexc('#777777')) if stop else (CORA, CORAD)
        p.shape(heart_pts(350, 330, sc), *col, 5, 6)
        ey0 = 400
    else:
        ey0 = 330
    # olhos grandes na base do manto
    for dx in (-80, 80):
        ex, ey = 350 + dx, (ey0 if not xray else 420) - 20 * swim
        if blink > .6: p.stroke([(ex - 30, ey), (ex + 30, ey)], 8)
        else:
            r = 52 if expr == 'shock' else 44
            p.dot(ex, ey, r, (255, 255, 255), 6)
            p.dot(ex + look * 14, ey + 4, 14 if expr == 'shock' else 20, INK)
            p.dot(ex + look * 14 - 6, ey - 4, 6, (255, 255, 255))
            if expr in ('tired', 'smug'):
                p.poly([(ex - r - 3, ey - r - 5), (ex + r + 3, ey - r - 5), (ex + r + 3, ey - 6), (ex - r - 3, ey - 6)], PV)
                p.stroke([(ex - r, ey - 6), (ex + r, ey - 6)], 7)
    my = (ey0 if not xray else 420) + 62 - 20 * swim
    if expr in ('grin', 'smug'): p.arc(350, my - 6, 30, 16, 20, 160, 7)
    elif expr == 'shock': p.dot(350, my + 6, 18, hexc('#7a2e2e'), 5)
    elif expr == 'tired': p.stroke([(325, my), (338, my - 6), (350, my), (362, my - 6), (375, my)], 6)
    else: p.arc(350, my - 4, 20, 10, 20, 160, 6)
    if sweat:
        for x, y in ((170, 160), (540, 140)):
            p.shape([(x, y - 30), (x + 16, y), (x, y + 14), (x - 16, y)], hexc('#9fd3ff'), None, 4)
    return p.img


def put_polvo(c, x, feet, h, f, seed=1, flip=False, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    for k, n in (('b1', 4), ('b2', 4), ('swim', 6), ('phase', 12)):
        if k in kw: kw[k] = round(kw[k] * n) / n
    if 'phase' in kw: kw['phase'] %= 1
    put_sprite(c, 'polvo', x, feet, h, 700 / 800, flip, **kw)


def gota(azul=True, expr='calm', blink=0):
    """gota de sangue com carinha (400x500)."""
    p = Pen(400, 500)
    col, dk = (AZUL, hexc('#285bb8')) if azul else (hexc('#e23b3b'), hexc('#b02424'))
    pts = [(200, 30)] + [(200 + 160 * math.cos(a), 320 + 150 * math.sin(a)) for a in np.linspace(-.35, math.pi + .35, 30)][::-1]
    p.shape(pts, col, dk, 6, 18)
    for dx in (-50, 50):
        ex, ey = 200 + dx, 320
        if blink > .6: p.stroke([(ex - 18, ey), (ex + 18, ey)], 6)
        else: p.dot(ex, ey, 24, (255, 255, 255), 5); p.dot(ex + 6, ey + 2, 10, INK)
    if expr == 'grin': p.arc(200, 380, 30, 16, 20, 160, 7)
    else: p.arc(200, 385, 20, 10, 20, 160, 6)
    return p.img


def put_gota(c, x, y, h, f, seed, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('gota', tuple(sorted(kw.items())), int(h), .8, False)
    paste_c(c, im, x, y)


def bolhas(c, x, y, f, n=5):
    for i in range(n):
        a = (f * 3 + i * 37) % 160
        p = Pen(60, 60); p.dot(30, 30, 18, (220, 240, 255), 4)
        paste_c(c, p.img.resize((60, 60), Image.LANCZOS), x + 30 * math.sin(f * .1 + i), y - a * 3, (1 - a / 160) * (.6 + .1 * (i % 3)))


def setas_azuis(c, cx, cy, f, k=1.0):
    """pontinhos de sangue azul correndo pra fora."""
    for i in range(8):
        ang = i * math.pi / 4 + .3
        d = (f * 6 + i * 13) % 160 + 120
        p = Pen(50, 50); p.dot(25, 25, 16, AZUL, 4)
        paste_c(c, p.img.resize((50, 50), Image.LANCZOS), cx + d * math.cos(ang) * k, cy + d * math.sin(ang) * k * 1.2, k)


@lru_cache(maxsize=4)
def mar(luz='day'):
    return CEN('fundo_mar', luz)


def SFX(s):
    s.splash(s.W(0, 'polvo') - 4, .3)
    for i in range(3): s.thunk(s.W(0, 'tres') - 2 + i * 5, 200, .5)
    s.ting(s.W(0, 'azul'), .3)
    for i in range(3): s.thunk(s.W(1, 'empurrar') - 2 + i * 9, 160, .45)
    s.thunk(s.W(2, 'maior') - 2, 110, .8)
    s.ting(s.W(3, 'cobre'), .3); s.thunk(s.W(3, 'ferro') - 2, 220, .5)
    s.whoosh(s.W(4, 'nadando') - 6, .5, .5)
    s.thunk(s.W(4, 'para') - 2, 90, 1.0)
    s.thunk(s.W(5, 'cansa') - 2, 140, .6)
    for i in range(4): s.thunk(s.W(5, 'andando') + i * 6, 380, .25)
    s.trill(s.W(6, 'pe'), .9, .3)


# ---------------------------------------------------------------- cenas: todas no fundo do mar (onde o polvo vive)
def s0(f):
    c = mar('day').copy()
    t0 = wt(0, 'tres') - 3
    a0 = wt(0, 'azul') - 3
    bolhas(c, 900, 1300, f)
    put_polvo(c, 620, 1720, 1000 * back(ramp(f, 0, 10)), f, 1, expr='grin' if f >= a0 else 'calm', phase=f / 40, look=.2)
    if t0 <= f: paste_c(c, txt('3 CORAÇÕES', 110, -5), 640, 520, back(ramp(f, t0, t0 + 8)))
    if f >= a0: paste_c(c, txt('SANGUE AZUL', 100, 5), 640, 680, back(ramp(f, a0, a0 + 8)))
    t = easeOut(ramp(f, 0, 40))
    return c, (640, lerp(1300, 1250, t), lerp(1.4, 1.1, t), 0), 'day'


def s1(f):
    c = mar('day').copy()
    g0 = wt(1, 'guelras') - 3
    e0 = wt(1, 'empurrar') - 3
    b1 = pulse(f % 18, 0, 4) if f >= e0 else 0
    put_polvo(c, 620, 1760, 1150, f, 2, xray=1, b1=b1, expr='calm', phase=f / 40, look=0)
    if f >= g0: paste_c(c, txt('GUELRAS', 90, -5), 620, 520, back(ramp(f, g0, g0 + 8)))
    if f >= e0: paste_c(c, txt('TUM-TUM', 80, 5), 620, 660, back(ramp(f, e0, e0 + 8)))
    t = smooth(ramp(f, 0, 80))
    return c, (620, lerp(1250, 1100, t), lerp(1.05, 1.3, t), 0), 'day'


def s2(f):
    c = mar('day').copy()
    m0 = wt(2, 'maior') - 3
    k0 = wt(2, 'corpo') - 3
    b2 = pulse(f % 20, 0, 5) if f >= m0 else 0
    put_polvo(c, 620, 1760, 1150, f, 2, xray=1, b1=pulse(f % 18, 0, 4), b2=b2, expr='grin' if f >= k0 else 'calm', phase=f / 40, look=0)
    if f >= k0: setas_azuis(c, 620, 1200, f, easeOut(ramp(f, k0, k0 + 10)))
    if f >= m0: paste_c(c, txt('O MAIOR', 100, -5), 620, 520, back(ramp(f, m0, m0 + 8)))
    t = smooth(ramp(f, 0, 70))
    return c, (620, lerp(1100, 1180, t), lerp(1.3, 1.15, t), 0), 'day'


def s3(f):
    c = mar('day').copy()
    c0 = wt(3, 'cobre') - 3
    fe0 = wt(3, 'ferro') - 3
    bolhas(c, 200, 1400, f, 4)
    put_gota(c, 420, 1150, 520 * back(ramp(f, 2, 12)), f, 1, azul=True, expr='grin' if f >= c0 else 'calm')
    if f >= c0: paste_c(c, txt('COBRE', 100, -5), 420, 760, back(ramp(f, c0, c0 + 8)))
    if f >= fe0:
        put_gota(c, 860, 1150, 520 * back(ramp(f, fe0, fe0 + 10)), f, 2, azul=False)
        paste_c(c, txt('FERRO', 100, 5), 860, 760, back(ramp(f, fe0, fe0 + 8)))
        paste_c(c, txt('O NOSSO', 70, 5), 860, 1500, back(ramp(f, fe0 + 6, fe0 + 14)))
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(520, 640, t), 1150, lerp(1.25, 1.12, t), 0), 'day'


def s4(f):
    c = mar('dusk').copy()
    n0 = wt(4, 'nadando') - 3
    p0 = wt(4, 'para') - 3
    sw = easeOut(ramp(f, n0, n0 + 10))
    y = 1760 - 300 * smooth(ramp(f, n0, n0 + 50))
    put_polvo(c, 620, y, 1000, f, 3, xray=1, swim=sw, stop=1 if f >= p0 else 0, b1=pulse(f % 18, 0, 4), b2=pulse(f % 20, 0, 5) if f < p0 else 0,
              expr='shock' if f >= p0 else 'calm', phase=f / 25, look=0)
    bolhas(c, 620, y + 100, f, 6)
    if f >= p0: paste_c(c, txt('PAROU!', 130, -6), 640, y - 1070, back(ramp(f, p0, p0 + 6)))
    kk = kick(f, p0 + 2)
    t = smooth(ramp(f, n0, n0 + 50))
    return c, (620, lerp(1250, 1060, t) + kk * 10, 1.15, kk * 2), 'dusk'


def s5(f):
    c = mar('dusk').copy()
    c0 = wt(5, 'cansa') - 3
    a0 = wt(5, 'andando') - 3
    if f < a0:
        y = lerp(1300, 1760, easeOut(ramp(f, 0, 25)))
        put_polvo(c, 620, y, 1050, f, 4, swim=1 - easeOut(ramp(f, 0, 25)), expr='tired', sweat=1 if f >= c0 else 0, phase=f / 30, look=0)
        if f >= c0: paste_c(c, txt('UFA!', 130, -5), 640, 560, back(ramp(f, c0, c0 + 8)))
        x = 620
    else:
        x = 620 - 6 * (f - a0)
        put_polvo(c, x, 1760 - 14 * abs(math.sin((f - a0) * .25)), 1050, f, 4, expr='grin', phase=(f - a0) / 14, look=-1, flip=False)
        paste_c(c, txt('ANDANDO', 110, 5), 640, 560, back(ramp(f, a0, a0 + 8)))
    t = smooth(f / 120)
    return c, (lerp(640, 600, t) if f < a0 else lerp(640, 600, t), 1250, lerp(1.1, 1.2, t), 0), 'dusk'


def s6(f):
    c = mar('golden').copy()
    t0 = wt(6, 'tres') - 3
    p0 = wt(6, 'pe') - 3
    x = 720 - 1.5 * f
    put_polvo(c, x, 1760 - 14 * abs(math.sin(f * .25)), 1050, f, 5, xray=1 if t0 <= f < p0 else 0, b1=pulse(f % 18, 0, 4), b2=pulse(f % 20, 0, 5),
              expr='smug' if f >= p0 else 'grin', phase=f / 14, look=-1)
    if t0 <= f < p0: paste_c(c, txt('3 CORAÇÕES...', 90, -5), 640, 560, back(ramp(f, t0, t0 + 8)))
    if f >= p0: paste_c(c, txt('A PÉ!', 150, 6), 640, 560, back(ramp(f, p0, p0 + 8)))
    t = easeOut(ramp(f, 0, 80))
    return c, (lerp(700, 600, t), 1220, lerp(1.1, 1.3, t), lerp(0, -2.5, t)), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
