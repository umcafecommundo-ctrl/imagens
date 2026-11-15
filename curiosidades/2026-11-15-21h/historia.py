"""Formato DESENHO: por que a maçã cortada fica marrom (Curiosidades da IA, 15/11/2026, 21h).
Categoria: CIÊNCIA DO DIA A DIA.
Fatos: Britannica ("Why Do Sliced Apples Turn Brown?") e Scientific American ("Fruits Gone Bad: Discover Enzymatic
Browning"): cortar rompe as células e expõe a polpa ao oxigênio; a enzima polifenol oxidase oxida os polifenóis e os
compostos formados viram melaninas, pigmento marrom; o suco de limão (ácido e antioxidante) desacelera a reação.
O escurecimento é uma reação química, não é a maçã estragando.
Cenários: s0 cozinha (Professor corta a maçã) | s1 cozinha, lupa nas células (enzima encontra oxigênio) |
s2 cozinha (melanina deixa a maçã marrom, Professor compara o braço) | s3 cozinha ao entardecer (limão) |
s4 cozinha ao entardecer (maçã "bronzeada" de óculos escuros; Professor reage)."""
from kit import *

LINES = [
    "A maçã cortada fica marrom, mas não é porque estragou.",
    "A faca rompe as células, e uma enzima de dentro delas encontra o oxigênio do ar.",
    "Juntos, eles fabricam melanina, o mesmo tipo de pigmento que dá cor à nossa pele.",
    "Você vê, um pouco de limão atrapalha essa reação, e a maçã fica clarinha.",
    "Ou seja: a maçã não estragou... ela só pegou um bronzeado.",
]
CAPTXT = [
    "A maçã cortada fica marrom, mas não é porque estragou.",
    "A faca rompe as células, e uma enzima de dentro delas|encontra o oxigênio do ar.",
    "Juntos, eles fabricam melanina,|o mesmo tipo de pigmento que dá cor à nossa pele.",
    "Você vê, um pouco de limão atrapalha essa reação,|e a maçã fica clarinha.",
    "Ou seja: a maçã não estragou... ela só pegou um bronzeado.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'marrom', 4), (0, 'estragou', 6), (1, 'faca', 4), (1, 'enzima', 4), (1, 'oxigenio', 6),
         (2, 'melanina', 4), (2, 'pele', 4), (3, 'limao', 4), (3, 'clarinha', 6), (4, 'bronzeado', 8)]


@lru_cache(maxsize=64)
def maca_img(w, marrom=0.0, face_='', blink=0, oculos=False):
    """meia maçã cortada, vista de frente (600x600)."""
    p = Pen(600, 600)
    p.shape(ell_pts(300, 330, 250, 230, 64, 0, -.05), hexc('#d8322f'), hexc('#a8201f'), 7, 16)   # casca
    m = marrom
    pol = tuple(int(a * (1 - m) + b * m) for a, b in zip(hexc('#fff3c8'), hexc('#b77a3e')))
    pold = tuple(int(a * (1 - m) + b * m) for a, b in zip(hexc('#f1dfa0'), hexc('#8f5a2a')))
    p.shape(ell_pts(300, 335, 222, 202, 64, 0, -.05), pol, pold, 0, 10)
    for dx in ((-30, 30) if not face_ else ()):
        p.shape(ell_pts(300 + dx, 330, 14, 26, 20, dx * .01), hexc('#5a3418'), None, 3, 0)  # sementes
    p.line([(300, 110), (310, 50)], hexc('#6b4428'), 16, 4)
    p.shape(ell_pts(370, 70, 50, 22, 24, -.4), hexc('#5bb04a'), hexc('#3e8a35'), 5, 4)
    if face_:
        face(p, 300, 330, face_, blink, .2, u=4.2)
    if oculos:
        for s in (-1, 1):
            p.shape(ell_pts(300 + s * 58, 325, 52, 36), hexc('#1d1d24'), None, 5, 0)
        p.line([(250, 320), (350, 320)], hexc('#1d1d24'), 10, 3)
    return p.img.resize((w, w), Image.LANCZOS)


def maca(c, x, y, w, f=0, s=1.0, **kw):
    w = int(w * s)
    if w < 10: return
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    if 'marrom' in kw: kw['marrom'] = round(kw['marrom'] * 10) / 10
    paste_c(c, maca_img(w, **kw), x, y)


@lru_cache(maxsize=4)
def faca_img(w):
    p = Pen(700, 200)
    p.shape([(20, 70), (300, 60), (300, 140), (20, 130)], hexc('#3b2a22'), None, 6, 0)
    p.shape([(300, 50), (680, 90), (300, 150)], hexc('#dfe4ea'), hexc('#aab3bd'), 6, 8)
    return p.img.resize((w, int(w * 200 / 700)), Image.LANCZOS)


@lru_cache(maxsize=32)
def bola_img(w, cor, rotulo='', expr='neutral', blink=0):
    p = Pen(300, 300)
    p.shape(ell_pts(150, 160, 120, 120), hexc(cor), mul(hexc(cor), .8), 6, 12)
    face(p, 150, 160, expr, blink, .3, u=2.6)
    return p.img.resize((w, w), Image.LANCZOS)


@lru_cache(maxsize=4)
def limao_img(w):
    p = Pen(400, 300)
    p.shape(ell_pts(200, 150, 170, 120, 48, 0, 0, 2.2), hexc('#ffe14a'), hexc('#d9b81f'), 6, 14)
    p.shape(ell_pts(370, 150, 22, 30), hexc('#ffe14a'), hexc('#d9b81f'), 5, 4)
    return p.img.resize((w, int(w * .75)), Image.LANCZOS)


@lru_cache(maxsize=4)
def lupa_img(w):
    p = Pen(600, 600)
    p.line([(420, 420), (570, 570)], hexc('#3b2a22'), 50, 6)
    p.dot(260, 260, 230, hexc('#c9d0d8'), 6)
    p.dot(260, 260, 200, hexc('#fff3c8'), 5)
    # células (hexágonos claros), algumas rompidas
    for i in range(-2, 3):
        for j in range(-2, 3):
            x = 260 + i * 70 + (j % 2) * 35; y = 260 + j * 60
            if (x - 260) ** 2 + (y - 260) ** 2 < 170 ** 2:
                pts = [(x + 30 * math.cos(a), y + 30 * math.sin(a)) for a in [k * math.pi / 3 for k in range(6)]]
                if (i + j) % 3 == 0:
                    p.stroke(pts[:4], 4, hexc('#c9a24a'))
                else:
                    p.stroke(pts + [pts[0]], 4, hexc('#c9a24a'))
    return p.img.resize((w, w), Image.LANCZOS)


def SFX(s):
    s.thunk(s.W(0, 'marrom') - 2, 220, .6); s.ting(s.W(0, 'estragou'), .3)
    s.whoosh(s.W(1, 'faca') - 4, .5, .4); s.thunk(s.W(1, 'rompe') - 2, 260, .7)
    s.thunk(s.W(1, 'oxigenio') - 2, 200, .5)
    s.ting(s.W(2, 'melanina'), .35)
    s.splash(s.W(3, 'limao') - 2) if hasattr(s, 'splash') else s.whoosh(s.W(3, 'limao') - 4, .4, .4)
    s.ting(s.W(3, 'clarinha'), .3)
    s.trill(s.W(4, 'bronzeado'), 1.0, .3)


def s0(f):
    c = CEN('cozinha', 'day').copy()
    k = wt(0, 'marrom') - 3
    e = wt(0, 'estragou') - 3
    br = 0.0 if f < k else ramp(f, k, k + 18)
    maca(c, 820, 1360, 470, f, back(ramp(f, 2, 10)), marrom=br, face_='shock' if f >= k else 'neutral', blink=blinkAt(f, 2))
    put_prof(c, 330, 1780, 920, f, expr='shock' if f >= k and f < e else ('stern' if f >= e else 'grin'), arms='point', look=1)
    if f >= e: paste_c(c, txt('NÃO ESTRAGOU!', 96, -5), 640, 680, back(ramp(f, e, e + 8)))
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('cozinha', 'day').copy()
    fc = wt(1, 'faca') - 3
    en = wt(1, 'enzima') - 3
    ox = wt(1, 'oxigenio') - 3
    paste_c(c, lupa_img(820), 650, 1200)
    tx = lerp(1300, 860, easeOut(ramp(f, fc - 8, fc + 2)))
    if f < en: paste_c(c, faca_img(520), tx, 760 + 10 * math.sin(f * .5))
    if f >= en:
        s = back(ramp(f, en, en + 8))
        meet = easeOut(ramp(f, ox, ox + 12))
        paste_c(c, bola_img(int(170 * s) or 1, '#5bb04a', '', 'grin', 1 if blinkAt(f, 3) > .6 else 0), lerp(420, 540, meet), 1150)
        paste_c(c, txt('ENZIMA', 60, 0), 420, 960, s)
    if f >= ox:
        s = back(ramp(f, ox, ox + 8))
        paste_c(c, bola_img(int(150 * s) or 1, '#59a8e6', '', 'grin', 0), lerp(820, 680, easeOut(ramp(f, ox, ox + 12))), 1150)
        paste_c(c, txt('OXIGÊNIO', 60, 0), 820, 960, s)
    t = smooth(ramp(f, 0, 80))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (621, 1200 + kick(f, fc, .6) * 10, z, 0), 'day'


def s2(f):
    c = CEN('cozinha', 'day').copy()
    m = wt(2, 'melanina') - 3
    pl = wt(2, 'pele') - 3
    br = ramp(f, m - 6, m + 14)
    maca(c, 820, 1360, 470, f, 1.0, marrom=br, face_='nervous' if f >= m else 'neutral', blink=blinkAt(f, 4))
    put_prof(c, 330, 1780, 920, f, expr='proud' if f >= pl else 'neutral', arms='up' if f >= pl else 'chin', look=1)
    if f >= m: paste_c(c, txt('MELANINA', 110, -5), 640, 660, back(ramp(f, m, m + 8)))
    if f >= pl: paste_c(c, txt('= COR DA PELE', 80, 4), 640, 800, back(ramp(f, pl, pl + 8)))
    z = lerp(1.06, 1.16, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, m, .6) * 10, z, 0), 'day'


def s3(f):
    c = CEN('cozinha', 'dusk').copy()
    l = wt(3, 'limao') - 3
    cl = wt(3, 'clarinha') - 3
    dr = ramp(f, l, l + 14)
    paste_c(c, limao_img(300), lerp(1200, 860, easeOut(ramp(f, l - 10, l))), 760)
    for i in range(4):
        dy = ((f - l) * 18 + i * 50) % 260 if f >= l else -1
        if dy >= 0 and f < cl + 20: paste_c(c, bola_img(40, '#ffe14a', '', 'neutral', 1), 820 + i * 8, 880 + dy)
    br = 1.0 - .9 * ramp(f, cl - 8, cl + 6) if f < cl + 30 else 0.1
    maca(c, 700, 1300, 520, f, 1.0, marrom=br, face_='grin' if f >= cl else 'neutral', blink=blinkAt(f, 5))
    if l <= f < cl: paste_c(c, txt('LIMÃO!', 110, -5), 460, 700, back(ramp(f, l, l + 8)))
    if f >= cl: paste_c(c, txt('CLARINHA', 100, 5), 560, 700, back(ramp(f, cl, cl + 8)))
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (640, 1220 + kick(f, l, .6) * 10, z, lerp(0, 2, t)), 'dusk'


def s4(f):
    c = CEN('cozinha', 'dusk').copy()
    b = wt(4, 'bronzeado') - 3
    put_prof(c, 320, 1780, 920, f, expr='smug' if f < b else 'grin', arms='chin' if f < b else 'shrug', look=1)
    maca(c, 840, 1340, 460, f, 1.0, marrom=.8, face_='smug', blink=0, oculos=f >= b)
    if f >= b: paste_c(c, txt('BRONZEADA!', 110, -6), 640, 720, back(ramp(f, b, b + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.03, 1.15, t) * (1 + .0006 * f)
    return c, (621, lerp(1300, 1260, t), z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
