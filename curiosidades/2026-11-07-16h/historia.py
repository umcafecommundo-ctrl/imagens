"""Formato DESENHO: em Vênus um dia dura mais que um ano (Curiosidades da IA, 07/11/2026, 16h). Categoria: ESPAÇO.
Fatos: NASA Space Place, "All About Venus" (Vênus leva cerca de 243 dias terrestres para girar uma vez em torno de si;
leva 225 dias terrestres para dar a volta no Sol; gira no sentido contrário ao da Terra e da maioria dos planetas, então o
Sol nasce no oeste e se põe no leste; nuvens grossas); NASA Venus Fact Sheet / Wikipedia (rotação retrógrada de −243,02 d;
velocidade de rotação no equador de 6,52 km/h; conta: 2π × 6.052 km ÷ (243 × 24 h) ≈ 6,5 km/h, ritmo de caminhada)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h12 = _load('h12', '2026-11-06-12h'); _h10 = _load('h10', '2026-11-06-10h')
astronaut = _h12.astronaut; put_astro = _h12.put_astro
sol_img = _h10.sol_img; space_bg = _h10.space_bg

LINES = [
    "Em Vênus, um dia dura mais que um ano inteiro.",
    "Vênus leva duzentos e vinte e cinco dias pra dar a volta completa no Sol. Esse é o ano de lá.",
    "Mas pra dar um único giro em torno de si mesmo, ele leva duzentos e quarenta e três dias.",
    "E ainda gira ao contrário: lá, o Sol nasce no oeste e se põe no leste.",
    "Você vê, Vênus gira tão devagar que o chão, no meio do planeta, anda a uns seis quilômetros e meio por hora.",
    "É a mesma velocidade de alguém caminhando.",
    "Ou seja: em Vênus, o ano acaba... antes de o dia terminar.",
]
CAPTXT = [
    "Em Vênus, um dia dura mais que um ano inteiro.",
    "Vênus leva 225 dias pra dar a volta completa no Sol.|Esse é o ano de lá.",
    "Mas pra dar um único giro em torno de si mesmo,|ele leva 243 dias.",
    "E ainda gira ao contrário:|lá, o Sol nasce no oeste e se põe no leste.",
    "Você vê, Vênus gira tão devagar que o chão, no meio do planeta,|anda a uns 6,5 quilômetros por hora.",
    "É a mesma velocidade de alguém caminhando.",
    "Ou seja: em Vênus, o ano acaba...|antes de o dia terminar.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [3]
CHECK = [(0, 'dia', 4), (0, 'ano', 6), (1, 'sol', 4), (1, 'ano', 6), (2, 'giro', 4), (2, 'tres', 6), (3, 'contrario', 4),
         (3, 'oeste', 4), (3, 'leste', 6), (4, 'devagar', 4), (4, 'hora', 6), (5, 'caminhando', 6), (6, 'acaba', 4), (6, 'terminar', 8)]

VE, VED = hexc('#f2c46b'), hexc('#d39a3e')


def venus(expr='calm', blink=0, look=0.4, rot=0.0, hat=0):
    """Vênus com carinha (600x600); rot gira as faixas de nuvem."""
    p = Pen(600, 600)
    p.shape(ell_pts(300, 300, 250, 250, 72), VE, VED, 7, 30)
    for k in range(5):
        y = 150 + k * 70
        off = (rot * 260 + k * 90) % 520 - 260
        hw = math.sqrt(max(0, 250 ** 2 - (y - 300) ** 2)) - 25
        x0, x1 = max(300 - hw, 300 + off - 120), min(300 + hw, 300 + off + 120)
        if x1 > x0 + 10: p.stroke([(x0, y), (x1, y)], 16, hexc('#f8dc9a'))
    for dx in (-70, 70):
        ex, ey = 300 + dx, 290
        if blink > .6: p.stroke([(ex - 26, ey), (ex + 26, ey)], 8)
        else:
            r = 46 if expr == 'shock' else 38
            p.dot(ex, ey, r, (255, 255, 255), 6); p.dot(ex + look * 12, ey + 3, 15, INK); p.dot(ex + look * 12 - 5, ey - 3, 5, (255, 255, 255))
            if expr in ('sleepy', 'smug'):
                p.poly([(ex - r - 3, ey - r - 5), (ex + r + 3, ey - r - 5), (ex + r + 3, ey - 2), (ex - r - 3, ey - 2)], VE); p.stroke([(ex - r, ey - 2), (ex + r, ey - 2)], 7)
    if expr in ('grin', 'smug'): p.arc(300, 370, 44, 24, 20, 160, 8)
    elif expr == 'shock': p.dot(300, 385, 22, hexc('#7a2e2e'), 5)
    else: p.arc(300, 375, 28, 12, 20, 160, 7)
    if hat:
        p.shape([(220, 80), (380, 80), (300, -60 + 60)], hexc('#ff5a9e'), hexc('#d63f7f'), 5, 6)
        p.dot(300, 6, 22, hexc('#ffd84a'), 4)
    return p.img


def put_venus(c, x, y, size, f, seed=1, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'rot' in kw: kw['rot'] = round((kw['rot'] % 1) * 24) / 24
    im = sprite('venus', tuple(sorted(kw.items())), int(size), 1.0, False)
    paste_c(c, im, x, y)


@lru_cache(maxsize=4)
def venus_chao(luz='day'):
    """superfície de Vênus: céu amarelo-alaranjado de nuvens grossas e chão de rocha."""
    W, H, fy = BW, BH, 1500
    y = np.linspace(0, 1, H)[:, None, None]
    top, bot = (hexc('#e8a64a'), hexc('#f7d58a')) if luz != 'dusk' else (hexc('#a8642e'), hexc('#d9a35e'))
    a = np.array(top) * (1 - y) + np.array(bot) * y
    im = Image.fromarray(np.broadcast_to(a, (H, W, 3)).astype(np.uint8)).convert('RGBA')
    p = Pen(W, H); rnd = random.Random(5)
    for i in range(9):
        cx, cy = rnd.randint(0, W), rnd.randint(80, 900)
        p.shape(ell_pts(cx, cy, rnd.randint(180, 320), rnd.randint(40, 70), 40), hexc('#f4c977'), None, 0)
    p.shape([(0, fy - 60), (220, fy - 160), (420, fy - 80), (700, fy - 200), (980, fy - 90), (1242, fy - 150), (1242, fy + 40), (0, fy + 40)],
            hexc('#b5733e'), hexc('#8f5629'), 6, 20)
    p.poly([(0, fy), (W, fy), (W, H), (0, H)], hexc('#9b6236'))
    p.stroke([(0, fy), (W, fy)], 7)
    for i in range(22):
        x, yy = rnd.randint(0, W), rnd.randint(fy + 60, H - 40)
        r = rnd.randint(20, 60)
        p.shape(ell_pts(x, yy, r, r * .55, 24), hexc('#7d4a28'), hexc('#5e3519'), 4, 6)
    im.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    return im


def placa(c, x, y, s, f0=0):
    paste_c(c, txt(s, 70), x, y)


def SFX(s):
    s.ting(s.W(0, 'venus'), .3)
    s.thunk(s.W(0, 'ano') - 2, 140, .8)
    s.whoosh(s.W(1, 'volta') - 6, .6, .4)
    s.ting(s.W(1, 'ano'), .3)
    s.thunk(s.W(2, 'giro') - 2, 200, .5)
    s.thunk(s.W(2, 'tres') - 2, 120, .8)
    s.whoosh(s.W(3, 'contrario') - 6, .5, .4)
    s.ting(s.W(3, 'oeste'), .3)
    s.thunk(s.W(4, 'devagar') - 2, 220, .5)
    for i in range(6): s.thunk(s.W(5, 'caminhando') + i * 8, 380, .25)
    s.trill(s.W(6, 'terminar'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 espaço (Vênus) | s1 espaço (Vênus em volta do Sol) | s2 espaço (Vênus girando devagar) | s3 chão de Vênus (Sol no oeste)
# s4 chão de Vênus (chão andando) | s5 chão de Vênus (astronauta caminhando junto) | s6 espaço (ano novo antes do dia acabar)
def s0(f):
    c = space_bg().copy()
    d0 = wt(0, 'dia') - 3
    a0 = wt(0, 'ano') - 3
    put_venus(c, 620, 1180, 760 * back(ramp(f, 0, 12)), f, 1, expr='shock' if f >= a0 else 'calm', rot=f / 300)
    if f >= d0: paste_c(c, txt('1 DIA', 110, -5), 380, 640, back(ramp(f, d0, d0 + 8)))
    if f >= a0: paste_c(c, txt('> 1 ANO', 110, 5), 860, 640, back(ramp(f, a0, a0 + 8)))
    t = easeOut(ramp(f, 0, 40))
    return c, (620, 1150, lerp(1.5, 1.1, t), 0), 'day'


def s1(f):
    c = space_bg().copy()
    paste_c(c, sol_img(420), 620, 1100)
    ang = -math.pi / 2 + 2 * math.pi * smooth(ramp(f, 6, wt(1, 'esse') - 2))
    R = 400
    for k in range(48):  # órbita pontilhada
        a = k * 2 * math.pi / 48
        p = Pen(20, 20); p.dot(10, 10, 5, (255, 255, 255))
        paste_c(c, p.img.resize((20, 20)), 620 + R * math.cos(a), 1100 + R * .6 * math.sin(a))
    put_venus(c, 620 + R * math.cos(ang), 1100 + R * .6 * math.sin(ang), 220, f, 2, expr='grin', rot=f / 300, look=.3)
    n = int(225 * smooth(ramp(f, 6, wt(1, 'esse') - 2)))
    paste_c(c, txt(f'{n} DIAS', 110, -4), 620, 560)
    a0 = wt(1, 'ano') - 3
    if f >= a0: paste_c(c, txt('= 1 ANO', 110, 4), 620, 1650 - 200, back(ramp(f, a0, a0 + 8)))
    t = smooth(ramp(f, 0, 90))
    return c, (620, 1080, lerp(1.05, 1.15, t), 0), 'day'


def s2(f):
    c = space_bg().copy()
    g0 = wt(2, 'giro') - 3
    t0 = wt(2, 'tres') - 3
    put_venus(c, 620, 1150, 760, f, 3, expr='sleepy' if f >= g0 else 'calm', rot=f / 600, look=0)
    # seta curva girando devagar
    if f >= g0:
        p = Pen(900, 300)
        p.arc(450, 60, 420, 140, 20, 160, 14, hexc('#9fd3ff'))
        p.shape([(60, 110), (20, 40), (110, 60)], hexc('#9fd3ff'), None, 4)
        paste_c(c, p.img.resize((900, 300), Image.LANCZOS), 620, 1560, back(ramp(f, g0, g0 + 8)))
    if f >= t0: paste_c(c, txt('243 DIAS', 120, -4), 620, 560, back(ramp(f, t0, t0 + 8)))
    t = smooth(ramp(f, 0, 100))
    return c, (620, 1130, lerp(1.1, 1.25, t), lerp(0, -2, t)), 'day'


def s3(f):
    c = venus_chao('day').copy()
    o0 = wt(3, 'oeste') - 3
    l0 = wt(3, 'leste') - 3
    # o Sol sobe pela ESQUERDA (oeste) e desce pela direita (leste)
    u = smooth(ramp(f, o0 - 10, l0 + 30))
    sx = lerp(200, 1050, u); sy = 1350 - 650 * math.sin(math.pi * u)
    paste_c(c, sol_img(260, 1), sx, sy)
    c.alpha_composite(venus_chao('day').crop((0, 1340, BW, BH)), (0, 1340))
    if f >= o0: paste_c(c, txt('OESTE', 90, -4), 340, 1580, back(ramp(f, o0, o0 + 8)))
    if f >= l0: paste_c(c, txt('LESTE', 90, 4), 900, 1580, back(ramp(f, l0, l0 + 8)))
    c0 = wt(3, 'contrario') - 3
    if c0 <= f < o0 + 4: paste_c(c, txt('AO CONTRÁRIO!', 90, -5), 620, 520, back(ramp(f, c0, c0 + 8)))
    t = smooth(ramp(f, 0, 120))
    return c, (620, lerp(1150, 1100, t), lerp(1.0, 1.08, t), 0), 'golden'


def s4(f):
    c = venus_chao('dusk').copy()
    d0 = wt(4, 'devagar') - 3
    h0 = wt(4, 'hora') - 3
    # pedras do chão deslizando devagar
    off = (f * 1.2) % BW
    strip = venus_chao('dusk').crop((0, 1500, BW, BH))
    c.alpha_composite(strip, (int(off), 1500)); c.alpha_composite(strip, (int(off) - BW, 1500))
    if f >= d0: paste_c(c, txt('DEVAGAR...', 100, -5), 620, 700, back(ramp(f, d0, d0 + 8)))
    if f >= h0: paste_c(c, txt('6,5 KM/H', 140, 5), 620, 920, back(ramp(f, h0, h0 + 8)))
    p = Pen(500, 160); p.line([(20, 80), (420, 80)], hexc('#ffd84a'), 24, 5); p.shape([(400, 20), (490, 80), (400, 140)], hexc('#ffd84a'), None, 5)
    paste_c(c, p.img.resize((500, 160), Image.LANCZOS), 620 + 60 * math.sin(f * .08), 1470)
    t = smooth(ramp(f, 0, 120))
    return c, (620, lerp(1250, 1300, t), lerp(1.05, 1.2, t), 0), 'dusk'


def s5(f):
    c = venus_chao('dusk').copy()
    k0 = wt(5, 'caminhando') - 3
    off = (f * 4) % BW
    strip = venus_chao('dusk').crop((0, 1500, BW, BH))
    c.alpha_composite(strip, (int(off), 1500)); c.alpha_composite(strip, (int(off) - BW, 1500))
    step = math.sin(f * .3)
    put_astro(c, 620, 1700 - 12 * abs(step), 950, f, 2, arms='wave' if f >= k0 else 'hang', expr='grin', look=1, rot=3 * step)
    if f >= k0: paste_c(c, txt('= CAMINHADA', 100, -4), 620, 560, back(ramp(f, k0, k0 + 8)))
    t = smooth(ramp(f, 0, 70))
    return c, (620, 1200, lerp(1.1, 1.2, t), 0), 'dusk'


def s6(f):
    c = space_bg().copy()
    a0 = wt(6, 'acaba') - 3
    t0 = wt(6, 'terminar') - 3
    put_venus(c, 620, 1150, 760, f, 4, expr='grin' if f < t0 else 'smug', hat=1 if f >= a0 else 0, rot=f / 600, look=.3)
    if f >= a0:
        if f < t0: paste_c(c, txt('FELIZ ANO NOVO!', 86, -5), 620, 560, back(ramp(f, a0, a0 + 8)))
        rnd = random.Random(f // 3)
        for i in range(10):
            a, d = rnd.uniform(0, 2 * math.pi), rnd.uniform(420, 560)
            x, y = 620 + d * math.cos(a), 1150 + d * math.sin(a)
            p = Pen(40, 40); p.dot(20, 20, 12, hexc(rnd.choice(('#ffd84a', '#ff5a9e', '#5cc46f', '#9fd3ff'))), 3)
            paste_c(c, p.img.resize((40, 40)), x, y)
    if f >= t0:
        paste_c(c, txt('E O DIA?', 100, 4), 620, 540, back(ramp(f, t0, t0 + 8)))
        paste_c(c, txt('NÃO ACABOU!', 90, -3), 620, 690, back(ramp(f, t0 + 4, t0 + 12)))
    t = easeOut(ramp(f, 0, 80))
    return c, (620, 1150, lerp(1.1, 1.3, t), lerp(0, 2.5, t)), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
