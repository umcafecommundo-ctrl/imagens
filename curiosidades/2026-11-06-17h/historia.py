"""Formato DESENHO: na Roma antiga a roupa era lavada com xixi (Curiosidades da IA, 06/11/2026, 17h). Categoria: HISTÓRIA.
Fatos: Amusing Planet, "Pecunia Non Olet: The Urine Tax of Ancient Rome" (2025): os lavadeiros romanos (fullones) usavam a
amônia da urina para limpar e branquear roupas de lã como a toga; um imperador (Vespasiano, 69-79 d.C.) cobrou imposto de
quem recolhia urina dos banheiros públicos para vender; segundo o historiador Suetônio, o filho reclamou e o imperador pôs
uma moeda no nariz dele e perguntou se cheirava: daí 'pecunia non olet' (dinheiro não tem cheiro).
History Skills, "Liquid Gold: the ways the ancient Romans used urine": a urina era recolhida em grandes tinas; nas
lavanderias (fullonicae) às vezes trabalhadores pisavam a roupa em tinas de urina velha e fermentada; a amônia tirava gordura.
(Sem nomes de pessoas reais na narração: 'um imperador' e 'o filho dele'.)"""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h18 = _load('h18', '2026-11-06-18h')
jovem = _h18.jovem

LINES = [
    "Na Roma antiga, a roupa era lavada com xixi.",
    "As lavanderias juntavam o xixi em grandes tinas, e às vezes os trabalhadores pisavam a roupa lá dentro.",
    "O xixi velho solta amônia, que tira a gordura e deixa a lã branquinha.",
    "O negócio era tão bom que um imperador resolveu cobrar imposto de quem recolhia xixi.",
    "O filho dele achou nojento. Então o imperador pôs uma moeda no nariz do filho e perguntou: tá fedendo?",
    "Você vê, daí veio a frase em latim pecúnia nôn ólet: dinheiro não tem cheiro.",
    "Ou seja: a lavanderia mais chique de Roma... tinha cheiro de banheiro.",
]
CAPTXT = [
    "Na Roma antiga, a roupa era lavada com xixi.",
    "As lavanderias juntavam o xixi em grandes tinas,|e às vezes os trabalhadores pisavam a roupa lá dentro.",
    "O xixi velho solta amônia,|que tira a gordura e deixa a lã branquinha.",
    "O negócio era tão bom que um imperador|resolveu cobrar imposto de quem recolhia xixi.",
    "O filho dele achou nojento. Então o imperador pôs uma moeda|no nariz do filho e perguntou: tá fedendo?",
    "Você vê, daí veio a frase em latim pecunia non olet:|dinheiro não tem cheiro.",
    "Ou seja: a lavanderia mais chique de Roma...|tinha cheiro de banheiro.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [3]
CHECK = [(0, 'xixi', 4), (1, 'tinas', 4), (1, 'pisavam', 6), (2, 'amonia', 4), (2, 'branquinha', 4), (3, 'imposto', 4),
         (4, 'nojento', 4), (4, 'fedendo', 4), (5, 'cheiro', 4), (6, 'banheiro', 8)]

XIXI, XIXID = hexc('#f2d34a'), hexc('#cfae2a')
TOGA = '#f3efe2'; ROXO = '#7b3f9e'


def put_jovem(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'jovem', x, feet, h, f, seed, **kw)


def coroa_louro(c, x, y, w):
    p = Pen(300, 140)
    for s in (-1, 1):
        for i in range(6):
            a = math.pi * (.95 - i * .08) if s < 0 else math.pi * (.05 + i * .08)
            cx, cy = 150 + 120 * math.cos(a), 110 - 70 * math.sin(a)
            p.shape(ell_pts(cx, cy, 22, 11, 16, a + (math.pi / 2 if s < 0 else -math.pi / 2)), hexc('#7fb24a'), hexc('#5b8a32'), 3, 3)
    paste_c(c, p.img.resize((int(w), int(w * 140 / 300)), Image.LANCZOS), x, y)


@lru_cache(maxsize=2)
def roma_bg():
    W, H, fy = BW, BH, 1640
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, fy), (0, fy)], hexc('#9cc9ea'))
    p.shape([(0, 520), (W, 520), (W, fy), (0, fy)], hexc('#ecd3a6'), hexc('#cdb07c'), 6, 16)
    for x in (120, 520, 920):
        p.shape([(x, 760), (x + 200, 760), (x + 200, fy), (x, fy)], hexc('#b98b59'), None, 5)
        p.shape(ell_pts(x + 100, 760, 100, 100, 40), hexc('#b98b59'), None, 0)
    for x in (60, 460, 860, 1180):
        p.shape([(x - 34, 560), (x + 34, 560), (x + 34, fy), (x - 34, fy)], hexc('#f6ead2'), hexc('#d8c6a0'), 5, 10)
        for k in range(3): p.stroke([(x - 16 + k * 16, 600), (x - 16 + k * 16, fy - 20)], 3, hexc('#d8c6a0'))
        p.shape([(x - 54, 520), (x + 54, 520), (x + 54, 566), (x - 54, 566)], hexc('#f6ead2'), hexc('#d8c6a0'), 5, 4)
    p.shape([(-20, 480), (W + 20, 480), (W + 20, 524), (-20, 524)], hexc('#c86b4a'), hexc('#9a4e33'), 5, 6)
    p.poly([(0, fy), (W, fy), (W, H), (0, H)], hexc('#c9b089'))
    for y in range(fy + 60, H, 100):
        for x in range((y // 100) % 2 * 90, W, 180): p.stroke([(x, y), (x + 150, y)], 3, hexc('#ab9470'))
    p.stroke([(0, fy), (W, fy)], 7)
    return p.img.resize((W, H), Image.LANCZOS)


@lru_cache(maxsize=4)
def tina_img(front=True):
    p = Pen(700, 420)
    if not front:
        p.shape(ell_pts(350, 110, 320, 80, 48), hexc('#8a5f35'), hexc('#65452a'), 6, 8)
        p.shape(ell_pts(350, 118, 290, 64, 48), XIXI, XIXID, 4, 10)
        return p.img.resize((700, 420), Image.LANCZOS)
    p.shape([(30, 110), (670, 110), (620, 400), (80, 400)], hexc('#a06d3e'), hexc('#7a5230'), 6, 18)
    for y in (180, 320): p.line([(50, y), (650, y)], hexc('#5b5b5b'), 14, 4)
    return p.img.resize((700, 420), Image.LANCZOS)


def tina(c, x, y, w=700):
    s = w / 700
    back_ = tina_img(False); fr = tina_img(True)
    if s != 1:
        back_ = back_.resize((int(700 * s), int(420 * s)), Image.LANCZOS); fr = fr.resize((int(700 * s), int(420 * s)), Image.LANCZOS)
    return back_, fr, (int(x - 350 * s), int(y - 210 * s))


def toga(c, x, y, w=260, rot=0, white=1.0):
    col = tuple(int(lerp(a, b, white)) for a, b in zip(hexc('#d6c48e'), hexc('#fbfaf5')))
    p = Pen(300, 200)
    p.shape([(20, 40), (280, 20), (260, 180), (40, 170)], col, mul(col, .85), 5, 10)
    for k in range(3): p.stroke([(60 + k * 60, 50), (80 + k * 60, 160)], 4, mul(col, .8))
    im = p.img.resize((int(w), int(w * 2 / 3)), Image.LANCZOS)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def moeda(c, x, y, r=90, face_=False):
    p = Pen(240, 240)
    p.shape(ell_pts(120, 120, 100, 100, 48), hexc('#ffd24a'), hexc('#e0a92a'), 6, 14)
    p.arc(120, 120, 74, 74, 0, 360, 5, hexc('#c98f1e'))
    if face_:
        for dx in (-30, 30): p.dot(120 + dx, 110, 16, (255, 255, 255), 4); p.dot(120 + dx + 4, 112, 7, INK)
        p.arc(124, 140, 26, 12, 20, 160, 6)
    paste_c(c, p.img.resize((int(r * 2.4), int(r * 2.4)), Image.LANCZOS), x, y)


def SFX(s):
    s.thunk(s.W(0, 'xixi') - 2, 160, .7)
    s.splash(s.W(1, 'tinas') - 2, .4)
    for i in range(4): s.splash(s.W(1, 'pisavam') + i * 7, .3)
    s.ting(s.W(2, 'amonia'), .3); s.trill(s.W(2, 'branquinha'), .5, .25)
    for i in range(5): s.ting(s.W(3, 'imposto') + i * 3, .2)
    s.thunk(s.W(4, 'nojento') - 2, 200, .6)
    s.thunk(s.W(4, 'fedendo') - 2, 140, .7)
    s.ting(s.W(5, 'cheiro'), .35)
    s.trill(s.W(6, 'banheiro'), .8, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = roma_bg().copy()
    k = wt(0, 'xixi') - 3
    bk, fr, pos = tina(c, 780, 1640, 800)
    c.alpha_composite(bk, pos)
    toga(c, 780, 1480 + 8 * math.sin(f * .2), 260, 6 * math.sin(f * .1))
    c.alpha_composite(fr, pos)
    put_jovem(c, 280, 2100, 1050, f, 1, arms='hang' if f < k else 'cheek', expr='neutral' if f < k else 'shock', look=1, shirt=TOGA, skin=1)
    if f >= k: paste_c(c, txt('COM XIXI?!', 120, -6), 700, 1000, back(ramp(f, k, k + 8)))
    kk = kick(f, k + 2)
    t = easeOut(ramp(f, 0, 40))
    return c, (lerp(700, 620, t), 1350 + kk * 10, lerp(1.4, 1.08, t), kk), 'golden'


def s1(f):
    c = roma_bg().copy()
    t0 = wt(1, 'tinas') - 3
    p0 = wt(1, 'pisavam') - 3
    bk, fr, pos = tina(c, 640, 1600, 1000)
    c.alpha_composite(bk, pos)
    if f >= p0:
        jump = abs(math.sin((f - p0) * .35)) * 90
        put_jovem(c, 640, 1760 - jump, 1000, f, 2, arms='up', expr='grin', look=0, shirt=TOGA, skin=3)
        for i in range(4):
            a = (f - p0 + i * 5) % 20
            p = Pen(40, 40); p.dot(20, 20, 12, XIXI, 3)
            if a < 14: paste_c(c, p.img, 640 + (i - 1.5) * 120 + a * (i - 1.5) * 4, 1480 - a * 14 + a * a * .9)
    else:
        toga(c, 640, 1470, 260, 4 * math.sin(f * .1))
    c.alpha_composite(fr, pos)
    if t0 <= f < p0: paste_c(c, txt('TINAS DE XIXI', 100, -5), 640, 640, back(ramp(f, t0, t0 + 8)))
    if f >= p0: paste_c(c, txt('PISA, PISA!', 120, 5), 640, 640, back(ramp(f, p0, p0 + 8)))
    z = lerp(1.05, 1.15, smooth(f / 150))
    return c, (640, 1300, z, 0), 'golden'


def s2(f):
    c = roma_bg().copy()
    a0 = wt(2, 'amonia') - 3
    b0 = wt(2, 'branquinha') - 3
    bk, fr, pos = tina(c, 640, 1560, 900)
    c.alpha_composite(bk, pos)
    wh = smooth(ramp(f, b0 - 4, b0 + 6))
    toga(c, 640, 1080 - 20 * wh, 420, 0, wh)
    if f >= a0:
        for i in range(6):
            u = ((f - a0) * 3 + i * 40) % 240
            p = Pen(60, 60); p.shape(ell_pts(30, 30, 20, 20, 20), hexc('#e8f6ff'), hexc('#b9dcef'), 3, 4)
            paste_c(c, p.img, 420 + i * 85, 1450 - u * 1.6)
        paste_c(c, txt('AMÔNIA', 120, -5), 640, 640, back(ramp(f, a0, a0 + 8)))
    if f >= b0:
        for i in range(5):
            a = i * 1.26 + f * .1
            paste_c(c, txt('*', 90), 640 + 260 * math.cos(a), 1080 + 150 * math.sin(a), .6 + .4 * math.sin(f * .3 + i))
    c.alpha_composite(fr, pos)
    z = lerp(1.08, 1.2, smooth(f / 120))
    return c, (640, 1150, z, 0), 'golden'


def s3(f):
    c = roma_bg().copy()
    i0 = wt(3, 'imperador') - 3
    t0 = wt(3, 'imposto') - 3
    put_jovem(c, 640, 2100, 1150 * back(ramp(f, i0 - 4, i0 + 6)) if f >= i0 - 4 else 0, f, 5, arms='hang' if f < t0 else 'up', expr='smug' if f < t0 else 'grin',
              look=0, shirt=ROXO, skin=0, hair='#6b4a2f')
    if f >= i0: coroa_louro(c, 640, 2100 - 1150 * .86 + 10, 330)
    if f >= t0:
        for i in range(8):
            u = f - t0 - i * 2
            if u > 0: moeda(c, 300 + i * 90, 600 + min(u * 30, 900) + (i % 2) * 40, 45)
        paste_c(c, txt('IMPOSTO!', 130, -6), 640, 640, back(ramp(f, t0, t0 + 8)))
    kk = kick(f, t0 + 2)
    return c, (640, 1300 + kk * 10, 1.1 + .0008 * f, kk), 'day'


def s4(f):
    c = roma_bg().copy()
    n0 = wt(4, 'nojento') - 3
    m0 = wt(4, 'moeda') - 3
    fd = wt(4, 'fedendo') - 3
    put_jovem(c, 330, 2100, 1100, f, 5, arms='hang' if f < m0 else 'point', expr='smug', look=1, shirt=ROXO, skin=0, hair='#6b4a2f')
    coroa_louro(c, 330, 2100 - 1100 * .86 + 10, 320)
    put_jovem(c, 930, 2120, 960, f, 6, arms='hang' if f < n0 else 'cheek', expr='neutral' if f < n0 else 'pained', look=-1, shirt=TOGA, skin=0, hair='#3b2a1e')
    if n0 <= f < m0: paste_c(c, txt('ECA!', 140, 6), 930, 760, back(ramp(f, n0, n0 + 8)))
    if f >= m0:
        u = smooth(ramp(f, m0, m0 + 14))
        moeda(c, lerp(560, 860, u), lerp(1240, 1260, u), 60)
    if f >= fd: paste_c(c, txt('TÁ FEDENDO?', 110, -5), 640, 760, back(ramp(f, fd, fd + 8)))
    z = lerp(1.05, 1.15, smooth(f / 200))
    return c, (640, 1320, z, 0), 'day'


def s5(f):
    c = roma_bg().copy()
    l0 = wt(5, 'latim') - 3
    ch = wt(5, 'dinheiro') - 3
    moeda(c, 640, 1350, 200 + 6 * math.sin(f * .2), face_=True)
    if f >= l0:
        paste_c(c, txt('PECUNIA', 120, -4), 640, 620, back(ramp(f, l0, l0 + 8)))
        paste_c(c, txt('NON OLET', 120, -4), 640, 780, back(ramp(f, l0 + 4, l0 + 12)))
    if f >= ch: paste_c(c, txt('DINHEIRO NÃO TEM CHEIRO', 54, 3), 640, 960, back(ramp(f, ch, ch + 8)))
    z = lerp(1.05, 1.2, smooth(f / 150))
    return c, (640, 1150, z, lerp(0, -2, smooth(f / 150))), 'dusk'


def s6(f):
    c = roma_bg().copy()
    k = wt(6, 'banheiro') - 3
    ch = wt(6, 'chique') - 3
    put_jovem(c, 640, 2100, 1150, f, 2, arms='hang' if f < k else 'cheek', expr='grin' if f < k else 'pained', look=0, shirt=TOGA, skin=3)
    if ch <= f < k: paste_c(c, txt('CHIQUE!', 120, -6), 640, 800, back(ramp(f, ch, ch + 8)))
    if f >= k:
        for i in range(3):
            a = (f - k + i * 10) % 30
            p = Pen(80, 120); p.stroke([(40, 110), (20, 80), (60, 50), (30, 10)], 8, hexc('#9bc25a'))
            paste_c(c, p.img, 470 + i * 160, 860 - a * 6, 1 - a / 30)
        paste_c(c, txt('CHEIRINHO...', 96, 5), 640, 800, back(ramp(f, k, k + 8)))
    z = lerp(1.05, 1.28, easeOut(ramp(f, 0, 70)))
    return c, (640, 1300, z, lerp(0, 2.5, smooth(ramp(f, 0, 70)))), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
