"""Formato DESENHO: o país que fica inteiro dentro de outro e acima de mil metros (Lesoto) (Curiosidades da IA, 06/11/2026, 16h).
Categoria: LUGARES E GEOGRAFIA.
Fatos: WorldAtlas "Top 10 interesting facts about Lesotho" e Wikipedia "Geography of Lesotho": o Lesoto é cercado por todos os
lados pela África do Sul (um dos três países enclavados, com San Marino e Vaticano); o ponto mais baixo fica a cerca de
1.400 m, o 'ponto mais baixo mais alto' de qualquer país; mais de 80% do território fica acima de 1.800 m; é o único país
inteiramente acima de 1.000 m; apelido 'Reino do Céu'. Ponto mais alto dos Países Baixos (Holanda): Vaalserberg, 322 m
(no Caribe, Mount Scenery, 887 m) — ambos abaixo de 1.400 m."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10', '2026-11-06-10h')
cor = _h10.cor

LINES = [
    "Existe um país inteirinho dentro de outro país.",
    "É o Lesoto, no sul da África: ele é cercado por todos os lados pela África do Sul.",
    "Só que o Lesoto não fica lá embaixo. Ele fica lá em cima, nas montanhas.",
    "O lugar mais baixo do país fica a cerca de mil e quatrocentos metros de altura. E mais de oitenta por cento dele passa de mil e oitocentos.",
    "Não é à toa que o apelido dele é Reino do Céu.",
    "Você vê, ele é o único país do mundo que fica inteirinho acima de mil metros.",
    "Ou seja: o ponto mais baixo do Lesoto... é mais alto que o ponto mais alto da Holanda.",
]
CAPTXT = [
    "Existe um país inteirinho dentro de outro país.",
    "É o Lesoto, no sul da África:|ele é cercado por todos os lados pela África do Sul.",
    "Só que o Lesoto não fica lá embaixo.|Ele fica lá em cima, nas montanhas.",
    "O lugar mais baixo do país fica a cerca de 1.400 metros de altura.|E mais de 80% dele passa de 1.800.",
    "Não é à toa que o apelido dele é Reino do Céu.",
    "Você vê, ele é o único país do mundo|que fica inteirinho acima de 1.000 metros.",
    "Ou seja: o ponto mais baixo do Lesoto...|é mais alto que o ponto mais alto da Holanda.",
]
FALA_TIKTOK = "Você já tinha ouvido falar do Lesoto? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [2, 6]
CHECK = [(0, 'dentro', 4), (1, 'lesoto', 4), (1, 'cercado', 6), (2, 'montanhas', 4), (3, 'quatrocentos', 4), (3, 'oitenta', 6),
         (4, 'ceu', 6), (5, 'mil', 4), (6, 'holanda', 8)]

VERDE, VERDED = hexc('#9ccf6a'), hexc('#79a94c')
LES = hexc('#5aa9e6'); HOL = hexc('#f5922a')


def put_pais(c, x, y, size, col, f, seed=0, expr='calm', look=.6, flip=False, crown=False):
    b = 1 if blinkAt(f, seed + 3) > .6 else 0
    put_sprite(c, 'cor', x, y + size / 2, size, 1.0, flip, None, col=col, expr=expr, blink=b, look=round(look * 2) / 2)
    if crown:
        p = Pen(200, 130)
        p.shape([(20, 120), (20, 40), (60, 80), (100, 20), (140, 80), (180, 40), (180, 120)], hexc('#ffd84a'), hexc('#e0b52a'), 5, 8)
        for x_ in (60, 100, 140): p.dot(x_, 100, 9, hexc('#e8423a'), 3)
        paste_c(c, p.img.resize((int(size * .55), int(size * .36)), Image.LANCZOS), x, y - size * .52)


@lru_cache(maxsize=2)
def mapa_bg():
    W, H = BW, BH
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc('#5fa8d8'))
    rnd = random.Random(4)
    for i in range(30):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        p.stroke([(x, y), (x + 40, y - 6), (x + 80, y)], 4, hexc('#7cbde6'))
    # África do Sul (forma arredondada)
    pts = [(120, 520), (420, 380), (760, 400), (1120, 560), (1180, 900), (1060, 1300), (760, 1560), (420, 1600), (180, 1380), (90, 980)]
    sm = []
    for i in range(len(pts)):
        a, b, cc = pts[i - 1], pts[i], pts[(i + 1) % len(pts)]
        sm += curve(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), b, ((b[0] + cc[0]) / 2, (b[1] + cc[1]) / 2), 8)
    p.shape(sm, hexc('#e9c46a'), hexc('#c9a24a'), 7, 22)
    return p.img.resize((W, H), Image.LANCZOS)


@lru_cache(maxsize=2)
def montanha_bg():
    """céu + planalto alto à direita (Lesoto) + planície baixa à esquerda."""
    c = BG('day').copy()
    p = Pen(BW, BH)
    p.shape([(-20, 1600), (330, 1600), (520, 900), (700, 760), (1000, 720), (1262, 760), (1262, 2228), (-20, 2228)], hexc('#8a9e6a'), hexc('#6d7f50'), 7, 26)
    for x, y in ((640, 820), (820, 760), (1080, 770)):
        p.shape([(x - 90, y + 30), (x, y - 80), (x + 90, y + 30)], hexc('#a6b483'), hexc('#7f8d5f'), 5, 10)
    p.shape([(-20, 1600), (330, 1600), (360, 2228), (-20, 2228)], hexc('#d9c27a'), hexc('#b9a25a'), 6, 10)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


@lru_cache(maxsize=8)
def regua(h=1100, marks=()):
    p = Pen(200, h + 40)
    p.shape([(40, 20), (140, 20), (140, h + 20), (40, h + 20)], hexc('#ffe08a'), hexc('#e0b84a'), 5, 8)
    for i, y in enumerate(range(20, h + 20, 50)): p.stroke([(40, y), (80 if i % 2 else 110, y)], 4)
    return p.img


def nuvem(c, x, y, s=1.0):
    p = Pen(400, 200)
    for dx, dy, r in ((120, 120, 70), (200, 90, 85), (290, 120, 65), (200, 140, 70)): p.dot(dx, dy, r + 5, INK)
    for dx, dy, r in ((120, 120, 70), (200, 90, 85), (290, 120, 65), (200, 140, 70)): p.dot(dx, dy, r, (255, 255, 255))
    paste_c(c, p.img, x, y, s)


def SFX(s):
    s.thunk(s.W(0, 'dentro') - 2, 160, .7)
    s.ting(s.W(1, 'lesoto'), .3)
    for i in range(4): s.thunk(s.W(1, 'cercado') + i * 5, 260, .35)
    s.whoosh(s.W(2, 'montanhas') - 6, .6, .45)
    s.ting(s.W(3, 'quatrocentos'), .35); s.ting(s.W(3, 'oitenta'), .3)
    s.trill(s.W(4, 'ceu'), .7, .25)
    s.thunk(s.W(5, 'mil') - 2, 150, .7)
    s.thunk(s.W(6, 'holanda') - 2, 120, .8)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = mapa_bg().copy()
    d0 = wt(0, 'dentro') - 3
    put_pais(c, 560, 1080, 600, hexc('#f4d27a'), f, 1, 'calm' if f < d0 else 'shock', look=1)
    if f >= d0:
        put_pais(c, 900, 1150, 230 * back(ramp(f, d0, d0 + 8)), LES, f, 2, 'grin', look=-1)
        paste_c(c, txt('PAÍS DENTRO DE PAÍS?!', 72, -5), 640, 560, back(ramp(f, d0, d0 + 8)))
    t = easeOut(ramp(f, 0, 40))
    kk = kick(f, d0 + 2)
    return c, (640, 1100 + kk * 10, lerp(1.4, 1.1, t), kk), 'day'


def s1(f):
    c = mapa_bg().copy()
    l0 = wt(1, 'lesoto') - 3
    c0 = wt(1, 'cercado') - 3
    a0 = wt(1, 'sul', 1) - 3
    put_pais(c, 520, 1060, 560, hexc('#f4d27a'), f, 1, 'grin' if f >= a0 else 'calm', look=1)
    put_pais(c, 880, 1170, 240, LES, f, 2, 'grin' if f < c0 else 'shock', look=-1)
    if f >= l0: paste_c(c, txt('LESOTO', 80, 4), 880, 1360, back(ramp(f, l0, l0 + 8)))
    if f >= c0:
        d = ImageDraw.Draw(c)
        n = int(24 * ramp(f, c0, c0 + 14))
        for i in range(n):
            a = i * math.pi / 12 + f * .02
            x, y = 880 + 175 * math.cos(a), 1170 + 175 * math.sin(a)
            d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=(227, 38, 43, 255))
    if f >= a0: paste_c(c, txt('ÁFRICA DO SUL', 80, -4), 560, 620, back(ramp(f, a0, a0 + 8)))
    z = lerp(1.1, 1.2, smooth(f / 150))
    return c, (680, 1100, z, 0), 'day'


def s2(f):
    c = montanha_bg().copy()
    m0 = wt(2, 'montanhas') - 3
    e0 = wt(2, 'embaixo') - 3
    put_pais(c, 170, 1490, 220, hexc('#f4d27a'), f, 1, 'shock' if f >= m0 else 'calm', look=1)
    u = smooth(ramp(f, m0 - 20, m0 + 6))
    x, y = lerp(260, 820, u), lerp(1490, 600, u)
    put_pais(c, x, y, 230, LES, f, 2, 'grin', look=1 if u < 1 else -1)
    if e0 <= f < m0 - 6: paste_c(c, txt('EMBAIXO?', 100, -5), 560, 1150, back(ramp(f, e0, e0 + 8)))
    if f >= m0: paste_c(c, txt('LÁ EM CIMA!', 110, 5), 640, 360, back(ramp(f, m0, m0 + 8)))
    t = smooth(ramp(f, m0 - 24, m0 + 10))
    return c, (lerp(560, 700, t), lerp(1300, 900, t), 1.25, 0), 'day'


def s3(f):
    c = montanha_bg().copy()
    q0 = wt(3, 'quatrocentos') - 3
    o0 = wt(3, 'oitenta') - 3
    paste_c(c, regua(), 300, 1340)
    put_pais(c, 760, 900, 230, LES, f, 2, 'calm' if f < q0 else 'grin', look=-1)
    if f >= q0: paste_c(c, txt('1.400 m', 110, -4), 760, 400, back(ramp(f, q0, q0 + 8)))
    if f >= o0: paste_c(c, txt('80% > 1.800 m', 76, 4), 700, 560, back(ramp(f, o0, o0 + 8)))
    z = lerp(1.15, 1.25, smooth(f / 200))
    return c, (640, 1000, z, 0), 'day'


def s4(f):
    c = montanha_bg().copy()
    k = wt(4, 'ceu') - 3
    r0 = wt(4, 'reino') - 3
    for i, (x, y) in enumerate(((300, 420), (980, 380), (640, 300))):
        pass
    for i, (x, y) in enumerate(((180, 600), (1120, 560))):
        nuvem(c, x + 20 * math.sin(f * .03 + i), y, .7)
    put_pais(c, 760, 860, 260, LES, f, 2, 'smug' if f < r0 else 'grin', look=-1, crown=f >= r0)
    if f >= k: paste_c(c, txt('REINO DO CÉU', 90, -5), 680, 470, back(ramp(f, k, k + 8)))
    z = lerp(1.3, 1.45, smooth(f / 120))
    return c, (680, 800, z, 0), 'golden'


def s5(f):
    c = montanha_bg().copy()
    m0 = wt(5, 'mil') - 3
    u0 = wt(5, 'unico') - 3
    put_pais(c, 760, 860, 230, LES, f, 2, 'grin', look=-1, crown=True)
    put_pais(c, 170, 1500, 200, hexc('#f4d27a'), f, 1, 'calm', look=1)
    if f >= m0:
        d = ImageDraw.Draw(c)
        w = int(1242 * ramp(f, m0, m0 + 12))
        for x in range(0, w, 60): d.line([(x, 1150), (x + 34, 1150)], fill=(227, 38, 43, 255), width=10)
        paste_c(c, txt('1.000 m', 76, 0), 900, 1230, back(ramp(f, m0, m0 + 8)))
    if f >= u0: paste_c(c, txt('O ÚNICO!', 110, 5), 640, 420, back(ramp(f, u0, u0 + 8)))
    z = lerp(1.0, 1.1, smooth(f / 160))
    return c, (640, 1150, z, 0), 'dusk'


def s6(f):
    c = montanha_bg().copy()
    h0 = wt(6, 'holanda') - 3
    b0 = wt(6, 'baixo') - 3
    put_pais(c, 780, 1000, 260, LES, f, 2, 'calm' if f < h0 else 'smug', look=-1, crown=True)
    if f >= b0: paste_c(c, txt('LESOTO: 1.400 m', 70, 0), 760, 760, back(ramp(f, b0, b0 + 8)))
    put_pais(c, 270, 1480, 230 * back(ramp(f, h0 - 6, h0 + 4)), HOL, f, 5, 'shock', look=1)
    if f >= h0: paste_c(c, txt('HOLANDA: < 1.000 m', 62, 0), 520, 1260, back(ramp(f, h0, h0 + 8)))
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 70)))
    return c, (640, 1250, z, lerp(0, 1.5, smooth(ramp(f, 0, 70)))), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
