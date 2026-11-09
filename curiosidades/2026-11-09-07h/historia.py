"""Formato DESENHO: o pinguim que vive caçando pedrinha (Curiosidades da IA, 09/11/2026, 07h). Categoria: ANIMAIS.
Fatos: BBC Wildlife / Discover Wildlife ("Do penguins really 'propose' with pebbles?"): pinguins-gentoo, de-adélia e de-barbicha
usam pedrinhas para o ninho, quase o único material disponível na Antártida; as pedras deixam os ovos longe do chão gelado;
os machos fazem a maior parte do ninho e roubam pedras dos vizinhos. Africa Check (citando o WWF): o macho de adélia junta
pedrinhas com o bico; as pedras deixam os ovos acima da água quando o ninho alaga com a neve derretendo; adélias roubam
pedras do ninho do vizinho. O mito do "pedido de casamento com a pedra perfeita" NÃO é usado."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h16 = _load('h16p', '2026-11-08-16h')
pinguim = _h16.pinguim
kit.pinguim = pinguim
import art as _art; _art.pinguim = pinguim
put_ping = _h16.put_ping

LINES = [
    "Na Antártida, tem pinguim que vive caçando pedrinha.",
    "Lá quase não tem graveto nem folha, então o ninho é feito de pedra.",
    "O macho junta uma por uma, carregando cada pedrinha no bico.",
    "Você vê, o montinho deixa o ovo longe do chão gelado e da água da neve que derrete.",
    "E quando as pedras acabam... ele pega do ninho do vizinho.",
]
CAPTXT = [
    "Na Antártida, tem pinguim que vive caçando pedrinha.",
    "Lá quase não tem graveto nem folha,|então o ninho é feito de pedra.",
    "O macho junta uma por uma,|carregando cada pedrinha no bico.",
    "Você vê, o montinho deixa o ovo longe do chão gelado|e da água da neve que derrete.",
    "E quando as pedras acabam... ele pega do ninho do vizinho.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'pedrinha', 4), (1, 'graveto', 4), (1, 'pedra', 6), (2, 'bico', 4), (3, 'ovo', 4), (3, 'derrete', 6),
         (4, 'acabam', 4), (4, 'vizinho', 8)]

PED = [hexc('#8d8a86'), hexc('#a39b8f'), hexc('#7b7f86'), hexc('#9b8f84')]


@lru_cache(maxsize=16)
def pedra_img(size, k=0):
    p = Pen(120, 100)
    col = PED[k % 4]
    p.shape(ell_pts(60, 55, 50, 36, 30, .2 * (k % 3)), col, mul(col, .78), 5, 8)
    p.dot(45, 42, 7, mul(col, 1.18))
    return p.img.resize((size, int(size * 100 / 120)), Image.LANCZOS)


@lru_cache(maxsize=8)
def ninho_img(n, w=420):
    """monte de n pedrinhas (para o ninho)."""
    im = Image.new('RGBA', (w, w // 2 + 40), (0, 0, 0, 0))
    rnd = random.Random(3)
    pos = []
    for i in range(n):
        row = 0 if i < 9 else 1 if i < 15 else 2
        k = i if row == 0 else i - 9 if row == 1 else i - 15
        cols = 9 if row == 0 else 6 if row == 1 else 4
        x = w / 2 + (k - (cols - 1) / 2) * (w / 10.5) * (1 - row * .12) + rnd.uniform(-6, 6)
        y = w // 2 + 20 - row * 34 + rnd.uniform(-4, 4)
        pos.append((x, y, i))
    for x, y, i in sorted(pos, key=lambda t: t[1]):
        s = pedra_img(70, i)
        im.alpha_composite(s, (int(x - 35), int(y - 29)))
    return im


@lru_cache(maxsize=2)
def ovo_img(size=150):
    p = Pen(200, 240)
    p.shape(ell_pts(100, 128, 76, 100, 40), hexc('#f3efe2'), hexc('#d8d2bf'), 5, 12)
    return p.img.resize((size, int(size * 1.2)), Image.LANCZOS)


def pedra(c, x, y, size, k=0, s=1.0):
    if size * s < 8: return
    paste_c(c, pedra_img(int(size), k), x, y, s)


def bico_ped(c, x, feet, h, k=0):
    """pedrinha no bico do pinguim (sprite de frente 400x560; bico em ~ (200,255))."""
    pedra(c, x, feet - h * (560 - 262) / 560, h * .16, k)


# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 neve (Antártida: pinguim com pedrinha) | s1 neve (sem graveto/folha, só pedra) | s2 neve (macho levando pedrinha no bico
# até o ninho) | s3 neve ao entardecer (close no ninho com ovo; água da neve derretendo em volta) | s4 neve ao entardecer (vizinho)

def SFX(s):
    s.ting(s.W(0, 'pedrinha'), .3)
    s.thunk(s.W(1, 'graveto') - 2, 260, .4); s.thunk(s.W(1, 'pedra') - 2, 180, .7)
    for i in range(3): s.thunk(s.W(2, 'uma') + i * 10, 240, .4)
    s.thunk(s.W(3, 'ovo') - 2, 300, .5); s.splash(s.W(3, 'derrete') - 2, .4)
    s.whoosh(s.W(4, 'pega') - 4, .5, .5); s.trill(s.W(4, 'vizinho'), 1.0, .3)


def s0(f):
    c = CEN('neve', 'day').copy()
    k = wt(0, 'pedrinha') - 3
    put_ping(c, 620, 1680, 760, f, 1, look=.0, expr='smug' if f >= k else 'calm')
    if f >= k: bico_ped(c, 620, 1680 + 4 * math.sin((f + 5) * .15), 760, 1)
    if f >= k: paste_c(c, txt('ACHEI!', 110, 8), 900, 1000, back(ramp(f, k, k + 8)))
    z = lerp(1.35, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1300, z, 0), 'day'


def s1(f):
    c = CEN('neve', 'day').copy()
    g = wt(1, 'graveto') - 3
    pe = wt(1, 'pedra') - 3
    if f >= g:
        a = back(ramp(f, g, g + 8))
        paste_c(c, txt('GRAVETO?', 70, -6), 420, 880, a)
        paste_c(c, txt('FOLHA?', 70, 6), 850, 900, back(ramp(f, g + 8, g + 16)))
        if f >= pe - 6:
            paste_c(c, txt('NADA!', 90, -4), 620, 1060, back(ramp(f, pe - 6, pe + 2)))
    for i, x in enumerate((230, 450, 780, 1010)):
        if f >= pe: pedra(c, x, 1560 + (i % 2) * 40, 90, i, back(ramp(f, pe + i * 3, pe + i * 3 + 8)))
    put_ping(c, 620, 1660, 600, f, 2, look=.6 * math.sin(f * .08))
    z = 1.1 * (1 + .0009 * f)
    return c, (lerp(560, 680, smooth(ramp(f, 0, 90))), 1300, z, 0), 'day'


def s2(f):
    c = CEN('neve', 'day').copy()
    u = wt(2, 'uma')
    nest_n = 6 + min(8, max(0, (f - u) // 10))
    paste_c(c, ninho_img(int(nest_n)), 930, 1600)
    per = 40
    t = ((f - 0) % per) / per
    x = lerp(260, 720, t) if (f // per) % 2 == 0 else lerp(720, 260, t)
    carrying = (f // per) % 2 == 0
    hop = 14 * abs(math.sin(f * .5))
    put_ping(c, x, 1640 - hop, 560, f, 3, look=.6 if carrying else -.6)
    if carrying: bico_ped(c, x, 1640 - hop + 4 * math.sin((f + 15) * .15), 560, f // per)
    b = wt(2, 'bico') - 3
    if f >= b: paste_c(c, txt('NO BICO!', 90, -6), 600, 1050, back(ramp(f, b, b + 8)))
    for i in range(4): pedra(c, 110 + i * 45, 1680 + (i % 2) * 20, 70, i + 2)
    z = 1.05 * (1 + .0009 * f)
    return c, (621, 1320, z, 0), 'day'


def s3(f):
    c = CEN('neve', 'dusk').copy()
    m = wt(3, 'derrete') - 3
    o = wt(3, 'ovo') - 3
    # água da neve derretendo em volta
    wl = easeOut(ramp(f, m - 10, m + 20))
    if wl > 0:
        d = ImageDraw.Draw(c)
        w = 200 + 380 * wl
        d.ellipse((621 - w, 1560 - 40 - 50 * wl, 621 + w, 1560 + 40 + 50 * wl), fill=(120, 175, 220, 210), outline=(36, 23, 38), width=5)
    if f >= o: paste_c(c, ovo_img(150), 621, 1495, back(ramp(f, o, o + 8)))
    paste_c(c, ninho_img(19, 520), 621, 1520)
    put_ping(c, 990, 1560, 520, f, 4, look=-.8)
    if f >= m: paste_c(c, txt('SEQUINHO!', 80, 5), 621, 1130, back(ramp(f, m + 6, m + 14)))
    z = lerp(1.1, 1.35, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    return c, (lerp(700, 680, smooth(ramp(f, 0, 120))), lerp(1250, 1320, smooth(ramp(f, 0, 120))), z, 0), 'dusk'


def s4(f):
    c = CEN('neve', 'dusk').copy()
    p = wt(4, 'pega') - 4
    v = wt(4, 'vizinho') - 3
    paste_c(c, ninho_img(19, 360), 300, 1600)
    stolen = f >= p + 14
    paste_c(c, ninho_img(14 if stolen else 12, 360), 950, 1600)
    # vizinho dormindo, de costas pra ação
    put_ping(c, 300, 1560, 480, f, 5, look=0, blink=1)
    if f < v + 6:
        for i in range(3):
            a = (f + i * 14) % 42
            paste_c(c, txt('Z', 70 + i * 14), 400 + a * 2 + i * 30, 1060 - a * 4 - i * 40, 1 - a / 42)
    # ladrão
    t = smooth(ramp(f, p, p + 14))
    x = lerp(860, 520, t) if f < p + 16 else lerp(520, 860, smooth(ramp(f, p + 16, p + 32)))
    put_ping(c, x, 1620, 520, f, 6, look=-.8 if f < p + 16 else .8, expr='smug' if f >= p else 'calm')
    if f >= p + 14: bico_ped(c, x, 1620, 520, 3)
    if f >= v: paste_c(c, txt('PSIU...', 80, -6), 760, 1000, back(ramp(f, v, v + 8)))
    k = kick(f, v, .6)
    z = lerp(1.05, 1.25, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1350 + k * 10, z, k + lerp(0, -2, smooth(ramp(f, 0, 90)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
