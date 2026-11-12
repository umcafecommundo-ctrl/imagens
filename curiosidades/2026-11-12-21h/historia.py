"""Formato DESENHO: por que o xixi é amarelo (Curiosidades da IA, 12/11/2026, 21h). Categoria: CORPO HUMANO.
Fatos: EurekAlert! / Universidade de Maryland, 03/01/2024, e News-Medical (estudo na Nature Microbiology, Universidade de
Maryland e NIH): as hemácias velhas se desmancham e liberam bilirrubina, um pigmento laranja; ela chega ao intestino, onde
bactérias usam a enzima bilirrubina redutase para transformá-la em urobilinogênio (sem cor), que se degrada sozinho em
urobilina, o pigmento amarelo do xixi; a enzima foi identificada nesse estudo de 2024 (a pergunta estava aberta havia mais
de um século)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10e', '2026-11-08-10h')
pessoa = _h10.pessoa
_h6 = _load('h6e', '2026-11-06-10h')
cor = _h6.cor

LINES = [
    "O xixi é amarelo por causa do sangue.",
    "Quando uma hemácia, a célula vermelha do sangue, fica velha, ela se desmancha e solta um pigmento laranja.",
    "Esse pigmento vai parar no intestino, e lá as bactérias transformam ele.",
    "Você vê, o que sobra vira um pigmento amarelo, que o corpo joga fora no xixi.",
    "E a enzima das bactérias que faz isso só foi descoberta em dois mil e vinte e quatro.",
    "Ou seja: o seu xixi amarelo... é trabalho em equipe.",
]
CAPTXT = [
    "O xixi é amarelo por causa do sangue.",
    "Quando uma hemácia, a célula vermelha do sangue, fica velha,|ela se desmancha e solta um pigmento laranja.",
    "Esse pigmento vai parar no intestino,|e lá as bactérias transformam ele.",
    "Você vê, o que sobra vira um pigmento amarelo,|que o corpo joga fora no xixi.",
    "E a enzima das bactérias que faz isso|só foi descoberta em 2024.",
    "Ou seja: o seu xixi amarelo...|é trabalho em equipe.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = [4]
CHECK = [(0, 'amarelo', 4), (0, 'sangue', 6), (1, 'hemacia', 4), (1, 'velha', 4), (1, 'desmancha', 4), (1, 'laranja', 6),
         (2, 'intestino', 4), (2, 'bacterias', 4), (2, 'transformam', 6), (3, 'amarelo', 4), (3, 'xixi', 6),
         (4, 'enzima', 4), (4, 'quatro', 6), (5, 'equipe', 8)]

RED = hexc('#e3262b'); ORG = hexc('#ff9a2e'); GRN = hexc('#6cc46a'); YEL = hexc('#ffd84a'); WHT = (250, 248, 240)


def put_c(c, x, y, size, col, f=0, seed=0, expr='calm', look=.6, flip=False):
    if size < 8: return
    b = 1 if blinkAt(f, seed + 3) > .6 else 0
    put_sprite(c, 'cor', x, y + size / 2, size, 1.0, flip, None, col=tuple(col), expr=expr, blink=b, look=round(look * 2) / 2)


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


@lru_cache(maxsize=2)
def tubo_img():
    """intestino em zigue-zague (1242x700)."""
    p = Pen(1242, 700)
    pts = [(-40, 120), (1100, 120), (1180, 220), (1100, 320), (140, 320), (60, 420), (140, 520), (1282, 520)]
    p.line(pts, hexc('#f28a9a'), 130, 6)
    p.line(pts, hexc('#ffb6c1'), 92, 0)
    return p.img.resize((1242, 700), Image.LANCZOS)


TPTS = [(-40, 120), (1100, 120), (1180, 220), (1100, 320), (140, 320), (60, 420), (140, 520), (1282, 520)]
def tubo_pos(u):
    L = [math.dist(TPTS[i], TPTS[i + 1]) for i in range(len(TPTS) - 1)]
    d = clamp(u) * sum(L)
    for i, l in enumerate(L):
        if d <= l: t = d / l; return lerp(TPTS[i][0], TPTS[i + 1][0], t), lerp(TPTS[i][1], TPTS[i + 1][1], t)
        d -= l
    return TPTS[-1]


@lru_cache(maxsize=2)
def gota_img(h=300):
    p = Pen(240, 320)
    p.shape([(120, 10), (200, 170), (210, 220), (180, 280), (120, 305), (60, 280), (30, 220), (40, 170)], YEL, hexc('#e0b030'), 6, 10)
    p.dot(85, 210, 14, (255, 255, 255))
    return p.img.resize((240, 320), Image.LANCZOS).resize((int(h * .75), h), Image.LANCZOS)


def SFX(s):
    s.ting(s.W(0, 'amarelo'), .3); s.thunk(s.W(0, 'sangue') - 2, 150, .8)
    s.thunk(s.W(1, 'hemacia') - 2, 220, .5)
    s.thunk(s.W(1, 'desmancha') - 2, 120, .8)
    for i in range(4): s.thunk(s.W(1, 'laranja') - 2 + i * 3, 300, .3)
    s.whoosh(s.W(2, 'intestino') - 6, .6, .4)
    for i in range(3): s.thunk(s.W(2, 'transformam') - 2 + i * 5, 260, .4)
    s.ting(s.W(3, 'amarelo'), .35); s.whoosh(s.W(3, 'xixi') - 6, .5, .4)
    s.thunk(s.W(4, 'enzima') - 2, 200, .5); s.ting(s.W(4, 'quatro'), .35)
    s.trill(s.W(5, 'equipe'), .9, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    """banheiro: a pessoa descobre que o amarelo vem do sangue."""
    c = CEN('banheiro', 'day').copy()
    a0 = wt(0, 'amarelo') - 3
    s0_ = wt(0, 'sangue') - 3
    put_pessoa(c, 420, 2080, 1450, f, 1, expr='shock' if f >= s0_ else 'neutral', arms='cheek' if f >= s0_ else 'hang', look=1)
    if f >= a0: paste_c(c, gota_img(260), 900, 1150 + 10 * math.sin(f * .2), back(ramp(f, a0, a0 + 8)))
    if f >= s0_:
        put_c(c, 900, 820 + 8 * math.sin(f * .15), 230 * back(ramp(f, s0_, s0_ + 8)), RED, f, 1, 'grin', -1)
        paste_c(c, txt('SANGUE?!', 110, -6), 640, 450, back(ramp(f, s0_, s0_ + 8)))
    kk = kick(f, s0_ + 2)
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.35, 1.1, t) * (1 + .0009 * f)
    return c, (640, 1200 + kk * 10, z, kk), 'day'


def s1(f):
    """dentro do corpo: hemácia velha se desmancha em pigmento laranja."""
    c = CEN('corpo', 'day').copy()
    h0 = wt(1, 'hemacia') - 3
    v0 = wt(1, 'velha') - 3
    d0 = wt(1, 'desmancha') - 3
    l0 = wt(1, 'laranja') - 3
    if f < d0:
        sz = 520 * back(ramp(f, 0, 8))
        put_c(c, 621, 1050 + 10 * math.sin(f * .1), sz, RED, f, 2, 'calm' if f < v0 else 'dizzy', .6)
        if f >= h0: paste_c(c, txt('HEMÁCIA', 100, -5), 621, 600, back(ramp(f, h0, h0 + 8)))
        if f >= v0: paste_c(c, txt('VELHINHA...', 84, 6), 700, 1450, back(ramp(f, v0, v0 + 8)))
    else:
        rnd = random.Random(4)
        for i in range(7):
            a = rnd.random() * 6.28; r = 120 + rnd.random() * 220
            e = easeOut(ramp(f, d0, d0 + 14))
            col = RED if f < l0 else ORG
            put_c(c, 621 + math.cos(a) * r * e, 1050 + math.sin(a) * r * e, 150, col, f, 10 + i, 'grin' if f >= l0 else 'shock', math.cos(a))
        put_dust(c, 621, 1100, 160, f - d0)
        if f >= l0: paste_c(c, txt('LARANJA!', 110, -6), 621, 600, back(ramp(f, l0, l0 + 8)))
    z = lerp(1.08, 1.2, smooth(f / 150)) * (1 + .0009 * f)
    return c, (621, 1100, z, 0), 'day'


def s2(f):
    """dentro do corpo: intestino; bactérias transformam o pigmento laranja (ele perde a cor)."""
    c = CEN('corpo', 'day').copy()
    c.alpha_composite(tubo_img(), (0, 700))
    i0 = wt(2, 'intestino') - 3
    b0 = wt(2, 'bacterias') - 3
    t0 = wt(2, 'transformam') - 3
    u = .1 + .45 * smooth(ramp(f, i0, t0))
    x, y = tubo_pos(u)
    col = ORG if f < t0 else tuple(int(lerp(a, b, smooth(ramp(f, t0, t0 + 14)))) for a, b in zip(ORG, WHT))
    put_c(c, x, 700 + y - 20, 210, col, f, 3, 'shock' if f >= t0 else 'grin', 1 if u < .3 else -1)
    if f >= i0: paste_c(c, txt('INTESTINO', 90, -5), 621, 640, back(ramp(f, i0, i0 + 8)))
    for k, uu in enumerate((.44, .5, .56, .62)):
        if f >= b0 + k * 3:
            bx, by = tubo_pos(uu)
            put_c(c, bx + (0 if k % 2 else 10), 700 + by - 110 + 8 * math.sin(f * .3 + k), 160 * back(ramp(f, b0 + k * 3, b0 + k * 3 + 8)), GRN, f, 20 + k,
                  'grin' if f >= t0 else 'calm', 1 if bx < x else -1)
    if f >= t0: paste_c(c, txt('TRANSFORMA!', 90, 6), 621, 1450, back(ramp(f, t0, t0 + 8)))
    z = lerp(1.3, 1.18, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1050, z, 0), 'day'


def s3(f):
    """dentro do corpo (dusk): o que sobra fica amarelo e vai embora no xixi."""
    c = CEN('corpo', 'dusk').copy()
    a0 = wt(3, 'amarelo') - 3
    x0 = wt(3, 'xixi') - 3
    col = tuple(int(lerp(a, b, smooth(ramp(f, a0, a0 + 10)))) for a, b in zip(WHT, YEL))
    yy = 1000 + 600 * easeIn(ramp(f, x0 + 4, x0 + 30)) if 'easeIn' in globals() else 1000 + 600 * smooth(ramp(f, x0 + 4, x0 + 30))
    put_c(c, 621, yy + 10 * math.sin(f * .12), 420, col, f, 4, 'grin' if f >= a0 else 'calm', 0)
    if f >= a0: paste_c(c, txt('AMARELO!', 100, -6), 621, 640, back(ramp(f, a0, a0 + 8)))
    if f >= x0: paste_c(c, gota_img(220), 950, 900, back(ramp(f, x0, x0 + 8)))
    if f >= x0: paste_c(c, txt('TCHAU!', 90, 6), 400, 900, back(ramp(f, x0, x0 + 8)))
    z = lerp(1.08, 1.2, smooth(f / 150)) * (1 + .0009 * f)
    return c, (621, 1100, z, -1.5 * smooth(f / 150)), 'dusk'


def s4(f):
    """laboratório: cientistas descobrem a enzima das bactérias em 2024."""
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    e0 = wt(4, 'enzima') - 3
    q0 = wt(4, 'quatro') - 3
    put_sci(c, 330, 1950, 1150, f, 1, arms='point' if f >= q0 else 'clip', expr='proud' if f >= q0 else 'neutral', look=1)
    put_sci(c, 980, 1950, 1100, f, 2, arms='clip', bun=True, expr='shock' if f >= q0 else 'neutral', look=-1, skin=3)
    if f >= e0:
        put_c(c, 660, 1100 + 8 * math.sin(f * .2), 260 * back(ramp(f, e0, e0 + 8)), GRN, f, 5, 'grin', -1)
        paste_c(c, txt('ENZIMA', 90, -6), 660, 820, back(ramp(f, e0, e0 + 8)))
    if f >= q0: paste_c(c, txt('2024!', 140, 6), 640, 520, back(ramp(f, q0, q0 + 8)))
    kk = kick(f, q0 + 2)
    z = lerp(1.2, 1.08, smooth(ramp(f, 0, 50))) * (1 + .0009 * f)
    return c, (640, 1250 + kk * 10, z, kk), 'day'


def s5(f):
    """banheiro (dusk): a equipe toda junta."""
    c = CEN('banheiro', 'dusk').copy()
    e0 = wt(5, 'equipe') - 3
    for i, (x, col, sd) in enumerate(((330, RED, 1), (530, ORG, 2), (730, GRN, 3), (930, YEL, 4))):
        s = back(ramp(f, 4 + i * 5, 12 + i * 5))
        put_c(c, x, 1250 + 12 * math.sin(f * .12 + i), 190 * s, col, f, sd, 'grin' if f >= e0 else 'calm', .6 if i < 2 else -.6)
    if f >= e0: paste_c(c, txt('EQUIPE!', 120, -6), 640, 700, back(ramp(f, e0, e0 + 8)))
    z = lerp(1.05, 1.25, easeOut(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (640, 1200, z, lerp(0, -3, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
