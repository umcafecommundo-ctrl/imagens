"""Formato DESENHO: só a fêmea do mosquito pica (Curiosidades da IA, 13/11/2026, 21h). Categoria: ANIMAIS.
Fatos: CDC (EUA), "What is a Mosquito?": só as fêmeas picam pessoas e animais, para tomar sangue; elas precisam do sangue
para produzir os ovos; machos e fêmeas se alimentam de néctar de flores e suco de frutas; o macho não pica porque a
'tromba' dele é fraca demais para furar a pele. Science News: em laboratório, machos com muita sede às vezes tentam,
mas mal passam da primeira camada da pele (por isso 'não pica' fica no sentido do dia a dia)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h16 = _load('h0816', '2026-11-08-16h')
mosquito = _h16.mosquito

LINES = [
    "O mosquito macho não pica ninguém.",
    "Quem te pica de noite, e deixa aquela coceira, é sempre a fêmea.",
    "E o mais curioso: os dois se alimentam de suco de flor e de fruta.",
    "Você vê, a fêmea só pica porque precisa do sangue pra conseguir fazer os ovos.",
    "Ou seja: aquele zumbido chato no seu ouvido, de madrugada... é uma futura mamãe.",
]
CAPTXT = [
    "O mosquito macho não pica ninguém.",
    "Quem te pica de noite, e deixa aquela coceira,|é sempre a fêmea.",
    "E o mais curioso: os dois se alimentam|de suco de flor e de fruta.",
    "Você vê, a fêmea só pica porque precisa do sangue|pra conseguir fazer os ovos.",
    "Ou seja: aquele zumbido chato no seu ouvido, de madrugada...|é uma futura mamãe.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'macho', 4), (0, 'ninguem', 6), (1, 'pica', 4), (1, 'femea', 6), (2, 'flor', 4), (2, 'fruta', 6),
         (3, 'sangue', 4), (3, 'ovos', 6), (4, 'zumbido', 4), (4, 'mamae', 8)]

SKIN = SKINS[1]


# ------------------------------------------------------------------ personagens, objetos e cenário novos
def mosquita(expr='calm', blink=0, look=0.4, wing=0.0):
    """a fêmea: o mesmo mosquito com um lacinho rosa na cabeça (600x500)."""
    im = mosquito(expr, blink, look, wing).copy()
    p = Pen(600, 500)
    p.shape([(420, 190), (370, 160), (372, 222)], hexc('#ff6fa8'), hexc('#d94f86'), 4, 4)
    p.shape([(420, 190), (470, 160), (468, 222)], hexc('#ff6fa8'), hexc('#d94f86'), 4, 4)
    p.dot(420, 191, 12, hexc('#ff6fa8'), 4)
    im.alpha_composite(p.img)
    return im


def put_m(c, nome, x, y, h, f, seed=1, flip=False, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    kw['wing'] = (f + seed) % 3 / 2
    im = sprite(nome, tuple(sorted(kw.items())), int(h), 600 / 500, flip)
    paste_c(c, im, x + 6 * math.sin((f + seed * 5) * .2), y + 10 * math.sin((f + seed * 3) * .17))


def dorminhoco(blink=1, expr='neutral', braco=1):
    """pessoa deitada na cama, vista de lado (1242x700): cabeça no travesseiro à esquerda, coberta até o ombro."""
    p = Pen(1242, 700)
    p.shape([(60, 120), (150, 120), (150, 640), (60, 640)], hexc('#8a5f35'), hexc('#65452a'), 6, 8)     # cabeceira
    p.shape([(140, 420), (1180, 420), (1180, 560), (140, 560)], hexc('#f4f4f2'), hexc('#d0d0cc'), 6, 8) # colchão
    p.shape([(140, 560), (1180, 560), (1180, 640), (140, 640)], hexc('#8a5f35'), hexc('#65452a'), 6, 6) # estrado
    p.shape(ell_pts(290, 380, 150, 60, 40), hexc('#ffffff'), hexc('#dcdcdc'), 5, 8)                    # travesseiro
    hc = (300, 290)
    p.shape(ell_pts(hc[0], hc[1], 108, 98, 56), SKIN, mul(SKIN, .86), 5, 14)
    p.shape([(hc[0] - 112, hc[1] - 10), (hc[0] - 100, hc[1] - 80), (hc[0] - 30, hc[1] - 110), (hc[0] + 60, hc[1] - 108),
             (hc[0] + 108, hc[1] - 60), (hc[0] + 60, hc[1] - 56), (hc[0] - 20, hc[1] - 66), (hc[0] - 90, hc[1] - 30)],
            hexc('#3b2a1e'), mul(hexc('#3b2a1e'), .7), 5, 6)
    face(p, hc[0] + 10, hc[1] + 10, expr, blink, .6, u=2.0)
    p.shape([(380, 300), (700, 250), (1000, 260), (1180, 300), (1180, 470), (360, 470)], hexc('#5c8fd6'), hexc('#4470b0'), 6, 16)  # coberta
    if braco:
        p.line([(560, 320), (700, 360), (860, 350)], SKIN, 34, 5)
        p.dot(880, 350, 24, SKIN, 5)
    return p.img.resize((1242, 700), Image.LANCZOS)


@lru_cache(maxsize=8)
def cama(blink=1, expr='neutral'):
    return dorminhoco(blink, expr)


@lru_cache(maxsize=4)
def quarto_bg(luz='dusk'):
    return CEN('quarto', luz)


@lru_cache(maxsize=4)
def jardim_bg(luz='day'):
    c = CEN('floresta', luz).copy()
    p = Pen(BW, BH)
    for (x, y, r, col) in ((300, 1500, 70, '#ff8fb1'), (950, 1560, 60, '#ffd84a'), (180, 1800, 50, '#c58be0'), (1080, 1850, 55, '#ff8fb1')):
        p.line([(x, y + r), (x, y + 260)], hexc('#3c9a50'), 14, 4)
        for k in range(6):
            a = k * math.pi / 3
            p.shape(ell_pts(x + r * .9 * math.cos(a), y + r * .9 * math.sin(a), r * .6, r * .6, 24), hexc(col), mul(hexc(col), .8), 4, 4)
        p.dot(x, y, r * .5, hexc('#ffd84a'), 4)
    # flor grande no meio
    x, y, r = 640, 1250, 150
    p.line([(x, y + r), (x - 30, y + 700)], hexc('#3c9a50'), 26, 5)
    p.shape(ell_pts(x - 120, y + 420, 110, 40, 32, -.5), hexc('#5cc46f'), hexc('#3c9a50'), 5, 6)
    for k in range(8):
        a = k * math.pi / 4
        p.shape(ell_pts(x + r * math.cos(a), y + r * math.sin(a), r * .62, r * .62, 32), hexc('#ff6f61'), hexc('#d9534a'), 5, 8)
    p.shape(ell_pts(x, y, r * .62, r * .62, 40), hexc('#ffd84a'), hexc('#e0b43a'), 5, 10)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


@lru_cache(maxsize=2)
def ovos_img(n=5):
    p = Pen(300, 200)
    for i in range(n):
        p.shape(ell_pts(60 + i * 45, 100 + (i % 2) * 20, 18, 40, 24, .3), hexc('#f4f4f2'), hexc('#cfcfcf'), 4, 4)
    return p.img.resize((300, 200), Image.LANCZOS)


@lru_cache(maxsize=2)
def gota_sangue():
    p = Pen(120, 160)
    p.shape([(60, 10), (100, 90), (95, 120), (60, 150), (25, 120), (20, 90)], hexc('#e3262b'), hexc('#b81d22'), 4, 6)
    return p.img.resize((120, 160), Image.LANCZOS)


def x_vermelho(c, x, y, s):
    if s < .05: return
    d = ImageDraw.Draw(c); r = 90 * s
    d.line([(x - r, y - r), (x + r, y + r)], fill=(227, 38, 43, 255), width=int(22 * s) + 1)
    d.line([(x + r, y - r), (x - r, y + r)], fill=(227, 38, 43, 255), width=int(22 * s) + 1)


def SFX(s):
    s.whoosh(s.W(0, 'macho') - 6, .5, .3)
    s.thunk(s.W(0, 'ninguem') - 2, 180, .7)
    s.thunk(s.W(1, 'pica') - 2, 300, .6)
    s.ting(s.W(1, 'femea'), .3)
    s.ting(s.W(2, 'flor'), .3); s.ting(s.W(2, 'fruta'), .25)
    s.thunk(s.W(3, 'sangue') - 2, 160, .6); s.ting(s.W(3, 'ovos'), .3)
    s.whoosh(s.W(4, 'zumbido') - 6, .8, .3)
    s.trill(s.W(4, 'mamae'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 quarto à noite (macho passa e não pica) | s1 quarto à noite (a fêmea pica o braço) | s2 jardim (os dois no néctar)
# s3 quarto ao entardecer (explicação: sangue -> ovos) | s4 quarto à noite (zumbido no ouvido; futura mamãe)
def s0(f):
    c = quarto_bg('dusk').copy()
    c.alpha_composite(cama(), (0, 1150))
    k = wt(0, 'macho') - 3
    n = wt(0, 'ninguem') - 3
    put_m(c, 'mosquito', lerp(1300, 560, smooth(ramp(f, 0, k + 10))), 1180, 300, f, 1, flip=True, expr='smug' if f >= n else 'calm', look=-.3)
    if f >= k: paste_c(c, txt('MACHO', 100, -5), 560, 760, back(ramp(f, k, k + 8)))
    if f >= n: paste_c(c, txt('NÃO PICA!', 100, 4), 720, 950, back(ramp(f, n, n + 8))); x_vermelho(c, 860, 1500, back(ramp(f, n, n + 8)))
    t = easeOut(ramp(f, 0, 40))
    return c, (lerp(700, 620, t), 1250, lerp(1.4, 1.12, t) * (1 + .0009 * f), 0), 'dusk'


def s1(f):
    c = quarto_bg('dusk').copy()
    c.alpha_composite(cama(), (0, 1150))
    p0 = wt(1, 'pica') - 3
    fe = wt(1, 'femea') - 3
    land = smooth(ramp(f, 0, p0))
    put_m(c, 'mosquita', lerp(1250, 920, land), lerp(900, 1440, land), 300, f, 2, flip=False if True else False, expr='smug' if f >= p0 else 'calm', look=-.5)
    if f >= p0: paste_c(c, txt('PIC!', 90, -6), 900, 1250, back(ramp(f, p0, p0 + 8)) * (1 - ramp(f, p0 + 26, p0 + 32)))
    if f >= fe: paste_c(c, txt('FÊMEA', 110, -4), 820, 980, back(ramp(f, fe, fe + 8)))
    t = smooth(ramp(f, 0, 60))
    return c, (lerp(760, 820, t), lerp(1250, 1330, t), lerp(1.15, 1.5, t) * (1 + .0009 * f), 0), 'dusk'


def s2(f):
    c = jardim_bg('day').copy()
    fl = wt(2, 'flor') - 3
    fr = wt(2, 'fruta') - 3
    put_m(c, 'mosquito', 430, 1080, 280, f, 3, expr='calm', look=.6)
    put_m(c, 'mosquita', 860, 1080, 280, f, 4, flip=True, expr='calm', look=.6)
    if f >= fl: paste_c(c, txt('FLOR', 96, -5), 420, 760, back(ramp(f, fl, fl + 8)))
    if f >= fr:
        p = Pen(220, 220)
        p.shape(ell_pts(110, 125, 85, 85, 40), hexc('#ff6f61'), hexc('#d9534a'), 5, 10)
        p.line([(110, 45), (120, 15)], hexc('#6b3e22'), 10, 3); p.shape(ell_pts(145, 35, 30, 14, 20, -.4), hexc('#5cc46f'), None, 3)
        paste_c(c, p.img.resize((220, 220)), 880, 760, back(ramp(f, fr, fr + 8)))
        paste_c(c, txt('FRUTA', 90, 5), 880, 600, back(ramp(f, fr + 2, fr + 10)))
    z = 1.12 * (1 + .0012 * f)
    return c, (640, 1150, z, 0), 'day'


def s3(f):
    c = quarto_bg('dusk').copy()
    s0_ = wt(3, 'sangue') - 3
    ov = wt(3, 'ovos') - 3
    put_m(c, 'mosquita', 440, 1300, 420, f, 5, expr='smug' if f >= ov else 'calm', look=.6)
    cont = Image.new('RGBA', (420, 300), (0, 0, 0, 0))
    if f >= s0_: cont.alpha_composite(gota_sangue(), (20, 70))
    if f >= ov:
        cont.alpha_composite(ovos_img(), (130, 50))
    thought(c, 860, 820, 260, back(ramp(f, s0_ - 6, s0_ + 4)), cont)
    t = smooth(ramp(f, 0, 140))
    return c, (lerp(600, 680, t), lerp(1150, 1080, t), lerp(1.05, 1.25, t) * (1 + .0009 * f), 0), 'dusk'


def s4(f):
    c = quarto_bg('dusk').copy()
    zb = wt(4, 'zumbido') - 3
    ma = wt(4, 'mamae') - 3
    acorda = f >= zb + 6
    c.alpha_composite(cama(0 if acorda else 1, 'pained' if acorda else 'neutral'), (0, 1150))
    ang = f * .25
    put_m(c, 'mosquita', 300 + 170 * math.cos(ang), 1290 + 80 * math.sin(ang), 220, f, 6, flip=math.sin(ang) > 0, expr='smug' if f >= ma else 'calm', look=0)
    if f >= zb: paste_c(c, txt('ZIIIIIN!', 90, -6), 560, 1060, back(ramp(f, zb, zb + 8)))
    if f >= ma: paste_c(c, txt('FUTURA MAMÃE!', 68, 4), 470, 900, back(ramp(f, ma, ma + 8)))
    t = easeOut(ramp(f, 0, 90))
    return c, (lerp(640, 520, t), lerp(1250, 1220, t), lerp(1.1, 1.45, t) * (1 + .0009 * f), lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
