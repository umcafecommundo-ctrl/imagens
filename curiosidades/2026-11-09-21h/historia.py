"""Formato DESENHO: para que serve o furinho da tampa da caneta (Curiosidades da IA, 09/11/2026, 21h). Categoria: INVENÇÕES E OBJETOS.
Fatos: Snopes, "Holes in pen caps prevent choking?" (verdadeiro): o furo na tampa serve para reduzir o risco de sufocamento se
alguém, principalmente criança, aspirar a tampa (o fabricante diz que as tampas ventiladas buscam "minimizar o risco para as
crianças de inalação acidental"); a norma internacional ISO 11540 (1993; revisões 2014 e 2021) traz requisitos para reduzir
esse risco em tampas de canetas e marcadores; o furo no corpo da caneta é outra coisa: deixa o ar entrar para equilibrar a
pressão e a tinta sair. Mental Floss e ScienceAlert confirmam o mesmo."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10c', '2026-11-08-10h')
pessoa = _h10.pessoa

LINES = [
    "O furinho na tampa da caneta não é pra caneta. É pra você.",
    "Muita gente, principalmente criança, fica mordendo a tampa enquanto pensa.",
    "E às vezes, sem querer, a tampa escorrega pra garganta.",
    "Você vê, o furinho deixa o ar passar mesmo assim, e tem até regra internacional pedindo isso.",
    "Ou seja: a tampa foi desenhada sabendo que você ia mordê-la.",
]
CAPTXT = [
    "O furinho na tampa da caneta não é pra caneta.|É pra você.",
    "Muita gente, principalmente criança,|fica mordendo a tampa enquanto pensa.",
    "E às vezes, sem querer,|a tampa escorrega pra garganta.",
    "Você vê, o furinho deixa o ar passar mesmo assim,|e tem até regra internacional pedindo isso.",
    "Ou seja: a tampa foi desenhada|sabendo que você ia mordê-la.",
]
FALA_TIKTOK = "Você morde a tampa da caneta? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'furinho', 4), (0, 'voce', 6), (1, 'mordendo', 4), (2, 'garganta', 4), (3, 'ar', 4), (3, 'regra', 6),
         (4, 'morde-la', 8)]

AZ, AZD = hexc('#2f6fd0'), hexc('#1f4f9e')


# ------------------------------------------------------------------ objetos novos
def tampa(expr='calm', blink=0, look=0.0, face=1):
    """tampa de caneta em pé com furinho no topo e carinha (300x700)."""
    p = Pen(300, 700)
    p.shape([(70, 120), (230, 120), (215, 690), (85, 690)], AZ, AZD, 6, 14)
    p.shape(ell_pts(150, 120, 80, 70, 40), AZ, AZD, 6, 10)
    p.shape([(220, 200), (260, 210), (258, 560), (230, 590)], AZ, AZD, 5, 6)  # clipe
    p.dot(150, 80, 22, hexc('#11203d'), 5)  # furinho
    if face:
        ey = 300
        for dx in (-34, 34):
            if blink: p.stroke([(150 + dx - 16, ey), (150 + dx + 16, ey)], 5)
            else:
                r = 26 if expr == 'shock' else 22
                p.dot(150 + dx, ey, r, (255, 255, 255), 4); p.dot(150 + dx + look * 8, ey + 3, 10, INK)
                if expr == 'smug':
                    p.poly([(150 + dx - r - 3, ey - r - 3), (150 + dx + r + 3, ey - r - 3), (150 + dx + r + 3, ey - 4), (150 + dx - r - 3, ey - 4)], AZ)
                    p.stroke([(150 + dx - r, ey - 4), (150 + dx + r, ey - 4)], 5)
        if expr == 'shock': p.dot(150, ey + 60, 14, INK)
        else: p.arc(150, ey + 50, 22, 10, 20, 160, 5)
    return p.img


def put_tampa(c, x, y, h, f, seed=1, rot=0, **kw):
    """y = centro."""
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('tampa', tuple(sorted(kw.items())), int(h), 300 / 700, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y + 6 * math.sin((f + seed * 5) * .12))


@lru_cache(maxsize=4)
def caneta_img(w=900):
    """corpo da caneta deitado, sem tampa (900x160), ponta à direita."""
    p = Pen(900, 160)
    p.shape([(20, 40), (720, 40), (720, 120), (20, 120)], hexc('#eef5fb'), hexc('#cfdce8'), 6, 8)
    p.line([(40, 80), (700, 80)], AZ, 14, 0)
    p.shape([(720, 45), (840, 72), (840, 88), (720, 115)], hexc('#e6e6e6'), hexc('#bdbdbd'), 5, 4)
    p.dot(860, 80, 12, hexc('#9a9a9a'), 4)
    p.shape([(0, 50), (30, 50), (30, 110), (0, 110)], AZ, AZD, 5, 4)
    return p.img.resize((w, int(w * 160 / 900)), Image.LANCZOS)


@lru_cache(maxsize=1)
def garganta_bg():
    """garganta por dentro (tubo rosa) no cenário corpo."""
    c = CEN('corpo').copy()
    p = Pen(BW, BH)
    p.shape([(400, -40), (842, -40), (842, BH + 40), (400, BH + 40)], hexc('#f4b7bf'), hexc('#e09aa5'), 7, 24)
    for y in range(120, BH, 260): p.stroke([(420, y), (822, y + 30)], 5, hexc('#e8a3ad'))
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


def seta(c, x, y, s=1.0, rot=0):
    paste_c(c, txt('↑', int(90 * s), rot), x, y)


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 escola (tampa gigante na carteira, zoom no furinho) | s1 escola (criança na carteira mordendo a tampa, pensando)
# s2 escola (a tampa some, criança assustada; corte para a garganta) | s3 corpo (garganta por dentro: tampa entalada, ar passando
# pelo furinho; texto "ISO") | s4 escola ao entardecer (tampa com cara de esperta, marcas de dente)

def SFX(s):
    s.ting(s.W(0, 'furinho'), .3); s.thunk(s.W(0, 'voce') - 2, 260, .6)
    for i in range(3): s.thunk(s.W(1, 'mordendo') + i * 8, 420, .35)
    s.whoosh(s.W(2, 'escorrega') - 4, .5, .5); s.thunk(s.W(2, 'garganta') - 2, 200, .7)
    s.whoosh(s.W(3, 'ar') - 4, .4, .5); s.ting(s.W(3, 'regra'), .3)
    s.trill(s.W(4, 'morde-la') + 2, 1.0, .3)


def s0(f):
    c = CEN('escola').copy()
    fu = wt(0, 'furinho') - 3
    vo = wt(0, 'voce') - 3
    put_tampa(c, 621, 1100, 900, f, 1, expr='smug' if f >= vo else 'calm', look=.2)
    if f >= fu: paste_c(c, txt('FURINHO', 80, -6), 621, 470, back(ramp(f, fu, fu + 8)))
    if f >= vo: paste_c(c, txt('É PRA VOCÊ!', 100, 5), 621, 1640, back(ramp(f, vo, vo + 8)))
    t = smooth(ramp(f, fu - 6, fu + 14))
    z = lerp(1.0, 1.5, t) if f < vo - 6 else lerp(1.5, 1.0, smooth(ramp(f, vo - 6, vo + 6)))
    cy = lerp(1200, 900, t) if f < vo - 6 else lerp(900, 1250, smooth(ramp(f, vo - 6, vo + 6)))
    return c, (621, cy, z, 0), 'day'


def mesa_esc(c):
    d = ImageDraw.Draw(c)
    d.rectangle((260, 1500, 980, 1560), fill=(201, 138, 74, 255), outline=(36, 23, 38), width=6)
    d.rectangle((300, 1560, 330, 1800), fill=(107, 111, 120, 255)); d.rectangle((910, 1560, 940, 1800), fill=(107, 111, 120, 255))


def s1(f):
    c = CEN('escola').copy()
    m = wt(1, 'mordendo') - 3
    pe = wt(1, 'pensa') - 3
    put_pessoa(c, 621, 1720, 820, f, 2, expr='neutral', arms='cheek', shirt='#f4a261', hair='#5a3a22', look=.6)
    mesa_esc(c)
    # tampa na boca (mordendo)
    chew = 6 * math.sin(f * 1.1) if f >= m else 0
    put_tampa(c, 690, 1180 + chew, 150, f, 3, rot=-65, face=0)
    if f >= m:
        for i in range(2):
            a = (f - m + i * 10) % 20
            paste_c(c, txt('NHAC', 50, 10), 820 + a * 2, 1080 - a * 3 - i * 30, 1 - a / 20)
    if f >= pe:
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        cont.alpha_composite(txt('?', 200), (100, 30))
        thought(c, 380, 820, 150, back(ramp(f, pe, pe + 8)), cont)
    z = lerp(1.15, 1.35, smooth(ramp(f, 0, 90)))
    return c, (640, 1200, z, 0), 'day'


def s2(f):
    k = wt(2, 'escorrega') - 3
    g = wt(2, 'garganta') - 3
    if f < g - 2:
        c = CEN('escola').copy()
        gone = f >= k
        put_pessoa(c, 621, 1720, 820, f, 2, expr='shock' if gone else 'neutral', arms='cheek', shirt='#f4a261', hair='#5a3a22', look=0)
        mesa_esc(c)
        if not gone: put_tampa(c, 690, 1180, 150, f, 3, rot=-65, face=0)
        else: paste_c(c, txt('GLUP!', 100, -6), 900, 860, back(ramp(f, k, k + 8)))
        return c, (640, 1150 + kick(f, k) * 10, 1.3 + .003 * f, kick(f, k)), 'day'
    c = garganta_bg().copy()
    y = lerp(500, 1150, easeOut(ramp(f, g - 2, g + 12)))
    put_tampa(c, 621, y, 600, f, 4, expr='shock', look=0)
    return c, (621, 1150, 1.15, 0), 'day'


def s3(f):
    c = garganta_bg().copy()
    a = wt(3, 'ar') - 3
    r = wt(3, 'regra') - 3
    put_tampa(c, 621, 1150, 620, f, 4, expr='calm' if f >= a + 10 else 'shock', look=0)
    if f >= a:
        for i in range(5):
            t = ((f - a) * 14 + i * 110) % 550
            y = 1750 - t * 1.6
            dx = 0
            if not (850 < y < 1450) or y < 900: seta(c, 621 + dx, y, 1.2)
        paste_c(c, txt('O AR PASSA!', 90, -5), 621, 420, back(ramp(f, a + 6, a + 14)))
    if f >= r:
        p = Image.new('RGBA', (520, 300), (0, 0, 0, 0))
        d = ImageDraw.Draw(p)
        d.rounded_rectangle((10, 10, 510, 290), 30, fill=(255, 253, 246, 255), outline=(36, 23, 38), width=8)
        tt = txt('REGRA', 70); p.alpha_composite(tt, (260 - tt.size[0] // 2, 40))
        tt = txt('ISO 11540', 70); p.alpha_composite(tt, (260 - tt.size[0] // 2, 150))
        paste_c(c, p, 621, 650, back(ramp(f, r, r + 8)))
    z = lerp(1.1, 1.0, smooth(ramp(f, 0, 90)))
    return c, (621, 1100, z, 0), 'dusk'


def s4(f):
    c = CEN('escola', 'dusk').copy()
    mesa_esc(c)
    put_tampa(c, 621, 1150, 760, f, 5, expr='smug', look=-.3)
    d = wt(4, 'morde-la') - 3
    if f >= d:
        paste_c(c, txt('NHAC?', 100, 6), 621, 560, back(ramp(f, d, d + 8)))
    z = lerp(1.05, 1.3, easeOut(ramp(f, 0, 70)))
    return c, (621, 1150, z, lerp(0, -2.5, smooth(ramp(f, 0, 70)))), 'dusk'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4)]
