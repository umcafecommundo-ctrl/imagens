"""Formato DESENHO: por que Marte é vermelho (Curiosidades da IA, 16/11/2026, 21h).
Categoria: ESPAÇO.
Fatos: NASA/JPL via Space.com ("Red Planet Mars Not So Red Beneath the Surface", 20/02/2013) e Smithsonian
("The Red Planet Is Only Red on the Outside"): a cor vermelha vem de uma camada de poeira de óxido de ferro (ferro
que enferrujou/oxidou) que cobre a superfície; tempestades de poeira espalham esse pó pelo planeta; em fevereiro de 2013 o
jipe-robô Curiosity fez o primeiro furo numa rocha de Marte (alvo "John Klein", cratera Gale, ~6,4 cm) e o pó de dentro
saiu cinza, não vermelho.
Cenários: s0 estação espacial (Professor flutuando, Marte na janela) | s1 Marte (chão com ferro + prego enferrujando) |
s2 Marte (vento espalha o pó vermelho) | s3 Marte ao entardecer (jipe-robô fura a pedra, pó cinza) |
s4 estação espacial ao entardecer (Professor: vermelho só por fora)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h = _load('h0610m', '2026-11-06-10h')
marte_bg = _h.marte_bg
rover = _h.rover

LINES = [
    "Marte é vermelho porque está enferrujado.",
    "O chão de lá tem muito ferro, e esse ferro reagiu com oxigênio, igual a um prego velho.",
    "Essa ferrugem virou um pó fininho, que o vento espalha pelo planeta inteiro.",
    "Mas em dois mil e treze, um robô furou uma pedra de lá, e o pó de dentro saiu cinza.",
    "Ou seja: o planeta vermelho... só é vermelho por fora.",
]
CAPTXT = [
    "Marte é vermelho porque está enferrujado.",
    "O chão de lá tem muito ferro, e esse ferro reagiu|com oxigênio, igual a um prego velho.",
    "Essa ferrugem virou um pó fininho,|que o vento espalha pelo planeta inteiro.",
    "Mas em 2013, um robô furou uma pedra de lá,|e o pó de dentro saiu cinza.",
    "Ou seja: o planeta vermelho...|só é vermelho por fora.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'enferrujado', 6), (1, 'ferro', 4), (1, 'prego', 6), (2, 'vento', 4), (2, 'inteiro', 6),
         (3, 'furou', 4), (3, 'cinza', 6), (4, 'fora', 8)]

VERM = '#c9562f'; VERMD = '#94381c'


@lru_cache(maxsize=8)
def marte_img(size, face_=''):
    p = Pen(400, 400)
    p.shape(ell_pts(200, 200, 180, 180, 64), hexc(VERM), hexc(VERMD), 6, 24)
    for cx, cy, r in ((130, 140, 26), (260, 110, 18), (240, 270, 34), (120, 280, 16), (300, 200, 14)):
        p.shape(ell_pts(cx, cy, r, r * .8), hexc('#a8452a'), None, 4, 0)
    p.shape(ell_pts(200, 40, 60, 16), hexc('#f4f4f4'), None, 3, 0)
    if face_: face(p, 200, 210, face_, 0, .3, u=2.6)
    return p.img.resize((size, size), Image.LANCZOS)


def janela_marte(c, f, s=1.0, face_=''):
    ImageDraw.Draw(c).ellipse((898 - 182, 980 - 182, 898 + 182, 980 + 182), fill=(14, 18, 48, 255))
    paste_c(c, marte_img(300, face_), 898 + 6 * math.sin(f * .05), 980, s)


@lru_cache(maxsize=16)
def prego_img(h, rust):
    p = Pen(200, 700)
    g = tuple(int(lerp(a, b, rust)) for a, b in zip(hexc('#b9c0c8'), hexc('#c4602c')))
    gd = mul(g, .75)
    p.shape([(20, 20), (180, 20), (170, 70), (30, 70)], g, gd, 6, 6)
    p.shape([(80, 70), (120, 70), (115, 600), (100, 690), (85, 600)], g, gd, 6, 8)
    if rust > .3:
        rnd = random.Random(3)
        for i in range(9):
            p.dot(100 + rnd.randint(-12, 12), rnd.randint(100, 580), rnd.randint(6, 12), hexc('#8a3a18'))
    return p.img.resize((max(1, int(h * 200 / 700)), h), Image.LANCZOS)


@lru_cache(maxsize=4)
def pedra_img(w, aberta=0):
    p = Pen(500, 300)
    p.shape([(20, 290), (60, 120), (180, 60), (340, 70), (460, 140), (490, 290)], hexc('#7d7470'), hexc('#5e5653'), 6, 14)
    p.shape([(60, 120), (180, 60), (340, 70), (460, 140), (440, 160), (330, 100), (180, 92), (75, 150)], hexc(VERM), hexc(VERMD), 4, 4)
    if aberta: p.shape(ell_pts(250, 110, 26, 14), hexc('#3a3436'), None, 4, 0)
    return p.img.resize((w, int(w * 300 / 500)), Image.LANCZOS)


def po(c, x, y, f, f0, cor, n=14, spread=1.0):
    if f < f0: return
    d = ImageDraw.Draw(c); rnd = random.Random(9)
    a = f - f0
    for i in range(n):
        vx, vy = rnd.uniform(-6, 6) * spread, rnd.uniform(-9, -3)
        t = (a + i * 3) % 30
        px, py = x + vx * t, y + vy * t + .25 * t * t
        r = 9 + (i % 3) * 3
        d.ellipse((px - r, py - r, px + r, py + r), fill=cor + (230,), outline=INK + (255,), width=3)


def put_rover(c, x, feet, h, f, **kw):
    kw['blink'] = 1 if blinkAt(f, 5) > .6 else 0
    put_sprite(c, 'rover', x, feet, h, 700 / 560, False, {'wheel': 4}, **kw)


def SFX(s):
    s.ting(s.W(0, 'vermelho'), .3)
    s.thunk(s.W(0, 'enferrujado') - 2, 150, .8)
    s.thunk(s.W(1, 'ferro') - 2, 220, .6)
    s.ting(s.W(1, 'prego') - 2, .3)
    s.whoosh(s.W(2, 'vento') - 6, .7, .6); s.whoosh(s.W(2, 'inteiro') - 6, .5, .5)
    s.engine(s.W(3, 'robo') - 4, s.W(3, 'furou') + 20)
    for i in range(6): s.thunk(s.W(3, 'furou') - 2 + i * 4, 300, .35)
    s.thunk(s.W(3, 'cinza') - 2, 160, .8)
    s.thunk(s.W(4, 'fora') - 2, 140, .9); s.trill(s.W(4, 'fora') + 6, 1.0, .3)


def s0(f):
    c = CEN('estacao', 'day').copy()
    k = wt(0, 'enferrujado') - 3
    v = wt(0, 'vermelho') - 3
    janela_marte(c, f, back(ramp(f, v - 6, v + 4)) if f < v + 4 else 1.0, 'smug' if f >= k else '')
    put_prof(c, 420, 1820 + 18 * math.sin(f * .08), 960, f, expr='shock' if f >= k else 'grin', arms='point', look=1)
    if f >= k: paste_c(c, txt('ENFERRUJADO!', 104, -5), 640, 620, back(ramp(f, k, k + 8)))
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1250 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = marte_bg(0.0).copy()
    fe = wt(1, 'ferro') - 3
    ox = wt(1, 'oxigenio') - 3
    pr = wt(1, 'prego') - 3
    if f >= fe: paste_c(c, txt('FERRO', 110, -5), 380, 640, back(ramp(f, fe, fe + 8)))
    if f >= ox: paste_c(c, txt('+ OXIGÊNIO', 90, 5), 700, 800, back(ramp(f, ox, ox + 8)))
    rust = ramp(f, pr - 4, pr + 30)
    paste_c(c, prego_img(700, round(rust * 8) / 8), 621, 1250 + 8 * math.sin(f * .1), back(ramp(f, pr - 6, pr + 4)) if f >= pr - 6 else 0)
    if f >= pr + 20: paste_c(c, txt('FERRUGEM', 100, -4), 621, 1700, back(ramp(f, pr + 20, pr + 28)))
    t = smooth(ramp(f, 0, 100))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (621, 1200 + kick(f, pr, .5) * 8, z, 0), 'day'


def s2(f):
    c = marte_bg(0.0).copy()
    v = wt(2, 'vento') - 3
    it = wt(2, 'inteiro') - 3
    po_on = f >= wt(2, 'po') - 3
    put_rover(c, 760, 1640, 420, f, look=-.6, expr='shock' if f >= v else 'calm')
    if po_on:
        d = ImageDraw.Draw(c); rnd = random.Random(2)
        for i in range(40):
            sp = 18 if f >= v else 2
            x = (rnd.randint(0, 1242) + (f - v) * sp * (1 + i % 3) * .5 if f >= v else rnd.randint(0, 1242)) % 1300 - 30
            y = rnd.randint(900, 1600) + 10 * math.sin(f * .2 + i)
            r = rnd.choice((8, 10, 14))
            d.ellipse((x - r, y - r, x + r, y + r), fill=(214, 112, 70, 220))
    if f >= v: paste_c(c, txt('FIUUU!', 110, 6), 420, 700, back(ramp(f, v, v + 8)) * (1 - ramp(f, it - 4, it)))
    if f >= it: paste_c(c, txt('NO PLANETA TODO', 84, -4), 621, 700, back(ramp(f, it, it + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.15, 1.02, t) * (1 + .0009 * f)
    return c, (lerp(700, 621, t), 1250, z, lerp(0, 2, t)), 'day'


def s3(f):
    c = marte_bg(0.0).copy()
    fu = wt(3, 'furou') - 3
    ci = wt(3, 'cinza') - 3
    ml = wt(3, 'mil') - 3
    paste_c(c, pedra_img(520, f >= fu + 10), 870, 1530)
    put_rover(c, 450, 1660, 440, f, look=.8, expr='shock' if f >= ci else 'calm')
    d = ImageDraw.Draw(c)
    drill = clamp((f - fu) / 10)
    d.line([(630, 1380), (lerp(660, 850, drill), lerp(1400, 1420, drill))], fill=INK + (255,), width=26)
    d.line([(630, 1380), (lerp(660, 850, drill), lerp(1400, 1420, drill))], fill=(170, 170, 170, 255), width=14)
    if fu <= f < ci + 60:
        po(c, 870, 1420, f, fu, (214, 112, 70) if f < ci else (150, 150, 155), 12)
    if ml <= f < fu: paste_c(c, txt('2013', 130, -5), 621, 660, back(ramp(f, ml, ml + 8)))
    if f >= fu and f < ci: paste_c(c, txt('FUROU!', 110, 5), 621, 660, back(ramp(f, fu, fu + 8)))
    if f >= ci:
        paste_c(c, Image.new('RGBA', (1, 1)), 0, 0)
        pile = Pen(300, 140); pile.shape([(10, 130), (150, 10), (290, 130)], hexc('#9a9aa0'), hexc('#77777d'), 5, 8)
        paste_c(c, pile.img, 1000, 1700, .55 * back(ramp(f, ci, ci + 8)))
        paste_c(c, txt('CINZA?!', 130, -6), 621, 660, back(ramp(f, ci, ci + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.05, 1.25, t) * (1 + .0009 * f)
    return c, (lerp(621, 680, t), lerp(1250, 1300, t) + kick(f, ci, .7) * 10, z, 0), 'dusk'


def s4(f):
    c = CEN('estacao', 'dusk').copy()
    v = wt(4, 'vermelho') - 3
    fo = wt(4, 'fora') - 3
    janela_marte(c, f, 1.0, 'nervous' if f >= fo else '')
    put_prof(c, 470, 1820 + 18 * math.sin(f * .08), 960, f, expr='smug' if f < fo else 'grin',
             arms='chin' if f < fo else 'shrug', look=1)
    if v <= f < fo: paste_c(c, txt('VERMELHO...', 96, 5), 640, 620, back(ramp(f, v, v + 8)))
    if f >= fo: paste_c(c, txt('SÓ POR FORA!', 104, -5), 640, 620, back(ramp(f, fo, fo + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (650, lerp(1250, 1180, t) + kick(f, fo, .7) * 12, z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
