"""Formato DESENHO: por que astronauta não consegue arrotar direito no espaço (Curiosidades da IA, 14/11/2026, 21h).
Categoria: ESPAÇO.
Fatos: Live Science ("Can you burp in space?") e ScienceAlert: na Terra a gravidade separa o gás (que sobe) do
líquido e da comida (que ficam embaixo), e o arroto sai só com ar; sem gravidade não há em cima nem embaixo, o gás
fica misturado e um arroto pode trazer líquido e comida junto ("arroto molhado"); o truque contado por um
astronauta da NASA é empurrar a parede: a aceleração faz o papel da gravidade e separa o gás por um instante,
mas é preciso arrotar durante o impulso.
Cenários: s0 estação espacial | s1 corpo (estômago na Terra: gás em cima) | s2 corpo ao entardecer (estômago sem
gravidade: tudo misturado) | s3 estação (arroto com comida junto) | s4 estação (empurra a parede e arrota) |
s5 estação ao entardecer (o empurrãozinho)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1207', '2026-11-12-07h')
astro = _m.astro
put_astro, flutua = _m.put_astro, _m.flutua

LINES = [
    "No espaço, arrotar é uma péssima ideia.",
    "Na Terra, o gás sobe no estômago e sai sozinho, porque a comida fica embaixo.",
    "Você vê, sem gravidade não tem em cima nem embaixo: o gás fica misturado com a comida.",
    "Se o astronauta arrota, sai ar... com comida junto.",
    "O truque é empurrar a parede e arrotar durante o impulso.",
    "Ou seja: no espaço, até o arroto precisa de um empurrãozinho.",
]
CAPTXT = [
    "No espaço, arrotar é uma péssima ideia.",
    "Na Terra, o gás sobe no estômago e sai sozinho,|porque a comida fica embaixo.",
    "Você vê, sem gravidade não tem em cima nem embaixo:|o gás fica misturado com a comida.",
    "Se o astronauta arrota, sai ar... com comida junto.",
    "O truque é empurrar a parede|e arrotar durante o impulso.",
    "Ou seja: no espaço,|até o arroto precisa de um empurrãozinho.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 2
FLASH = []
CHECK = [(0, 'pessima', 6), (1, 'sobe', 4), (1, 'embaixo', 6), (2, 'gravidade', 4), (2, 'misturado', 6),
         (3, 'junto', 6), (4, 'empurrar', 4), (4, 'impulso', 6), (5, 'empurraozinho', 8)]

GAS = '#e8f6ff'; LIQ = '#e7a24a'; LIQD = '#c47f2c'; EST = '#f08a8a'; ESTD = '#c96464'


@lru_cache(maxsize=32)
def estomago_img(w, modo, ph):
    """estômago em corte. modo 'terra' = líquido embaixo e bolhas em cima; 'espaco' = tudo misturado."""
    p = Pen(600, 600)
    out = ell_pts(300, 320, 250, 200, 64, 0.0, 0.15)
    p.shape(out, hexc(EST), hexc(ESTD), 8, 18)
    p.shape(ell_pts(300, 320, 205, 158, 64, 0.0, 0.15), hexc('#fff3ea'), None, 5, 0)
    p.shape([(230, 120), (290, 120), (300, 40), (240, 40)], hexc(EST), hexc(ESTD), 6, 0)
    rnd = random.Random(7)
    if modo == 'terra':
        pts = [pt for pt in ell_pts(300, 320, 200, 152, 64, 0.0, 0.15) if pt[1] >= 330]
        pts = sorted(pts, key=lambda q: q[0])
        p.poly([(pts[0][0], 330)] + pts[::-1] + [(pts[-1][0], 330)], hexc(LIQ))
        for i in range(7):
            x = 150 + i * 45 + rnd.uniform(-10, 10)
            p.shape(ell_pts(x, 390 + rnd.uniform(-20, 60), 18, 14), hexc('#8d5a2b'), None, 3, 0)
        for i in range(6):
            x = 170 + i * 50; y = 290 - ((ph * 9 + i * 23) % 100)
            p.shape(ell_pts(x, y, 20, 20), hexc(GAS), hexc('#b9dcef'), 4, 0)
    else:
        for i in range(16):
            a = rnd.uniform(0, 6.28) + ph * .08 * (1 if i % 2 else -1)
            rr = rnd.uniform(10, 165)
            x = 300 + rr * math.cos(a) * 1.25; y = 320 + rr * math.sin(a) * .9
            if i % 3 == 0: p.shape(ell_pts(x, y, 22, 22), hexc(GAS), hexc('#b9dcef'), 4, 0)
            elif i % 3 == 1: p.shape(ell_pts(x, y, 30, 24), hexc(LIQ), hexc(LIQD), 4, 0)
            else: p.shape(ell_pts(x, y, 16, 12), hexc('#8d5a2b'), None, 3, 0)
    return p.img.resize((w, w), Image.LANCZOS)


def blob(c, x, y, r, kind):
    d = ImageDraw.Draw(c)
    col = {'gas': (232, 246, 255), 'liq': (231, 162, 74), 'com': (141, 90, 43)}[kind]
    d.ellipse((x - r, y - r, x + r, y + r), fill=col + (255,), outline=INK + (255,), width=4)


def SFX(s):
    s.thunk(s.W(0, 'pessima') - 2, 180, .6)
    for i in range(3): s.thunk(s.W(1, 'sobe') - 2 + i * 5, 300, .3)
    s.ting(s.W(1, 'sozinho'), .3)
    s.whoosh(s.W(2, 'misturado') - 6, .5, .4)
    s.thunk(s.W(3, 'arrota') - 2, 120, .9)
    s.thunk(s.W(3, 'junto') - 2, 200, .6)
    s.whoosh(s.W(4, 'empurrar') - 6, .7, .5); s.thunk(s.W(4, 'impulso') - 2, 140, .8)
    s.trill(s.W(5, 'empurraozinho'), 1.0, .3)


def s0(f):
    c = CEN('estacao', 'day').copy()
    k = wt(0, 'pessima') - 3
    put_astro(c, 520, 2000 + flutua(f), 1350, f, 1, arms='float', expr='nervous' if f >= k else 'neutral', look=1)
    if f >= k: paste_c(c, txt('ARROTO? NÃO!', 100, -6), 640, 560, back(ramp(f, k, k + 8)))
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.4, 1.1, t) * (1 + .0009 * f)
    return c, (lerp(560, 620, t), 1150 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('corpo', 'day').copy()
    k = wt(1, 'sobe') - 3
    e = wt(1, 'embaixo') - 3
    so = wt(1, 'sozinho') - 3
    paste_c(c, estomago_img(900, 'terra', (f // 2) % 14 if f >= k else 0), 621, 1150, back(ramp(f, 0, 9)))
    paste_c(c, txt('NA TERRA', 90, -4), 621, 560, back(ramp(f, 2, 10)))
    if f >= so: paste_c(c, txt('BURP!', 120, 6), 540, 760, back(ramp(f, so, so + 8)))
    if f >= e: paste_c(c, txt('COMIDA EMBAIXO', 70, 3), 621, 1560, back(ramp(f, e, e + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 100))) * (1 + .0009 * f)
    return c, (621, 1120, z, 0), 'day'


def s2(f):
    c = CEN('corpo', 'dusk').copy()
    g = wt(2, 'gravidade') - 3
    m = wt(2, 'misturado') - 3
    paste_c(c, estomago_img(900, 'terra' if f < g else 'espaco', (f // 2) % 40), 621, 1150)
    if f >= g: paste_c(c, txt('SEM GRAVIDADE', 84, -4), 621, 560, back(ramp(f, g, g + 8)))
    if f >= m: paste_c(c, txt('MISTURADO!', 100, 5), 621, 1560, back(ramp(f, m, m + 8)))
    t = smooth(ramp(f, 0, 120))
    z = lerp(1.08, 1.2, t) * (1 + .0009 * f)
    return c, (621, 1120 + kick(f, g, .6) * 10, z, lerp(0, 3, t)), 'dusk'


def s3(f):
    c = CEN('estacao', 'day').copy()
    a = wt(3, 'arrota') - 3
    j = wt(3, 'junto') - 3
    put_astro(c, 460, 2000 + flutua(f), 1300, f, 1, arms='float',
              expr='shock' if f >= j else ('pained' if f >= a else 'neutral'), look=1)
    mx, my = 520, 1200
    if f >= a:
        paste_c(c, txt('BURP!', 120, 6), 780, 680, back(ramp(f, a, a + 8)))
        for i in range(8):
            age = f - (a if i < 3 else j) - i * 2
            if age < 0: continue
            kind = 'gas' if i < 3 else ('liq' if i % 2 else 'com')
            x = mx + 60 + age * (4 + i % 3) + 10 * math.sin(age * .2 + i)
            y = my + (i - 4) * 14 + 25 * math.sin(age * .1 + i)
            blob(c, x, y, 24 + i % 3 * 6, kind)
    if f >= j: paste_c(c, txt('COM COMIDA!', 90, -5), 760, 860, back(ramp(f, j, j + 8)))
    z = lerp(1.1, 1.25, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (680, 1150 + kick(f, j, .7) * 10, z, 0), 'day'


def s4(f):
    c = CEN('estacao', 'day').copy()
    e = wt(4, 'empurrar') - 3
    i_ = wt(4, 'impulso') - 3
    d = easeOut(ramp(f, e, e + 30)) * 520
    put_astro(c, 280 + d, 2000 + flutua(f) * (0 if f >= e else 1), 1150, f, 1, arms='up' if f < e + 4 else 'float',
              expr='grin' if f >= i_ else 'neutral', look=1)
    d_ = ImageDraw.Draw(c)
    if f >= e:
        for k in range(4):
            y = 1050 + k * 90
            x0 = 230 + d - 260
            d_.line([(x0, y), (x0 - 160, y)], fill=(255, 255, 255, 200), width=10)
        paste_c(c, txt('EMPURRA!', 96, -5), 500, 620, back(ramp(f, e, e + 8)) if f < i_ else 0)
    if f >= i_:
        paste_c(c, txt('BURP!', 120, 6), 760, 640, back(ramp(f, i_, i_ + 8)))
        for k in range(3):
            age = f - i_ - k * 3
            if age >= 0: blob(c, 280 + d + 90 + age * 5, 1000 + k * 24, 26, 'gas')
    cx = lerp(560, 700, smooth(ramp(f, e, e + 40)))
    z = 1.1 * (1 + .0009 * f)
    return c, (cx, 1150 + kick(f, i_, .6) * 10, z, 0), 'day'


def s5(f):
    c = CEN('estacao', 'dusk').copy()
    k = wt(5, 'empurraozinho') - 3
    put_astro(c, 600, 2000 + flutua(f), 1350, f, 1, arms='up' if f >= k else 'float', expr='grin' if f >= k else 'smug', look=-.3)
    if f >= k: paste_c(c, txt('EMPURRÃOZINHO!', 72, -5), 630, 640, back(ramp(f, k, k + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.03, 1.16, t) * (1 + .0009 * f)
    return c, (630, lerp(1200, 1150, t), z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
