"""Formato DESENHO: a borboleta sente o gosto com os pés (Curiosidades da IA, 19/11/2026, 07h).
Categoria: ANIMAIS.
Fatos: Carleton University, Biology FAQ "Do butterflies really taste through their feet?" (as borboletas têm
quimiorreceptores de contato nos pés e sentem os químicos das plantas como nós com a língua; a fêmea "batuca"
(drum) as folhas com os pés para soltar o suco da planta e, se os químicos forem os certos, põe os ovos ali:
ela prova a folha para saber se a planta serve para as lagartas, não para comer).
Birds Outside My Window (2015), "Butterflies taste with their feet" (mesmo comportamento).
Cenários: s0 floresta (Professor se espanta com a borboleta) | s1 floresta, borboleta numa flor, pés brilham |
s2 floresta, fêmea na folha batucando com os pés | s3 floresta ao entardecer, balão com a lagarta comendo a folha |
s4 floresta ao entardecer (Professor ri: pisa na comida antes de servir)."""
from kit import *
from functools import lru_cache

LINES = [
    "A borboleta sente o gosto da comida com os pés.",
    "Nas patinhas, ela tem sensores de sabor, parecidos com os da nossa língua.",
    "A fêmea pousa numa folha e fica batucando com os pés.",
    "Você vê, ela está provando a planta, pra saber se serve de comida pros filhotes.",
    "Ou seja: a mãe borboleta pisa na comida... antes de servir.",
]
CAPTXT = [
    "A borboleta sente o gosto da comida com os pés.",
    "Nas patinhas, ela tem sensores de sabor,|parecidos com os da nossa língua.",
    "A fêmea pousa numa folha|e fica batucando com os pés.",
    "Você vê, ela está provando a planta,|pra saber se serve de comida pros filhotes.",
    "Ou seja: a mãe borboleta pisa na comida... antes de servir.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'pes', 4), (1, 'sabor', 4), (1, 'lingua', 6), (2, 'batucando', 6), (3, 'provando', 6),
         (3, 'filhotes', 6), (4, 'servir', 8)]

WING = hexc('#f39a1e'); WINGD = hexc('#c46a0a'); BODY = hexc('#4a3326'); BODYD = hexc('#2f2018')
LEAF = hexc('#5cb84a'); LEAFD = hexc('#3d8a33')


def SFX(s):
    for i in range(4): s.whoosh(s.W(0, 'borboleta') - 8 + i * 9, .12, .2)
    s.thunk(s.W(0, 'pes') - 2, 300, .8)
    s.ting(s.W(1, 'sabor'), .3); s.ting(s.W(1, 'lingua'), .25)
    s.thunk(s.W(2, 'pousa') - 2, 240, .4)
    for i in range(8): s.thunk(s.W(2, 'batucando') - 2 + i * 5, 520, .35)
    s.patter(s.W(3, 'provando'), s.W(3, 'provando') + 30, 10, .1)
    s.ting(s.W(3, 'filhotes'), .3)
    s.trill(s.W(4, 'servir'), 1.0, .3)


def borboleta(flap=0.0, drum=0.0, blink=0, look=0.3, expr='calm'):
    """borboleta de lado, 600x600, pés em y≈580, olhando para a direita. flap 0 = asas fechadas p/ cima, 1 = abertas."""
    p = Pen(600, 600)
    sc = 1 - .72 * flap  # asa "gira" para a frente: achata na vertical
    ax, ay = 290, 400
    def wing(cx, cy, rx, ry, col, dk, off=0):
        pts = ell_pts(cx + off, ay - (ay - cy) * sc, rx, ry * sc + 6, 40)
        p.shape([(ax, ay)] + [pts[i % 40] for i in range(13, 43)] + [(ax + 30, ay)], col, dk, 6, 12)
    # asa de trás (mais escura)
    wing(270, 200, 130, 170, mul(WING, .78), mul(WINGD, .8), -30)
    wing(220, 320, 100, 80, mul(WING, .78), mul(WINGD, .8), -30)
    # pernas
    fx = 365 + (0 if drum == 0 else 0)
    legs = [(230, 425, 205, 580), (300, 430, 300, 580), (360, 425, 400 + 10 * drum, 580 - 60 * drum)]
    for x0, y0, x1, y1 in legs:
        p.line([(x0, y0), ((x0 + x1) / 2 + 10, (y0 + y1) / 2 - 20), (x1, y1)], BODY, 7, 3)
    # corpo
    p.shape(ell_pts(290, 415, 125, 36, 40), BODY, BODYD, 6, 10)
    for x in (220, 260, 300):
        p.arc(x, 415, 10, 30, -70, 70, 4, BODYD)
    # cabeça
    p.shape(ell_pts(440, 395, 54, 50, 36), BODY, BODYD, 6, 10)
    # antenas
    for dx in (0, 34):
        p.line([(450 + dx * .3, 352), (480 + dx, 280), (500 + dx, 215)], BODY, 6, 3)
        p.dot(500 + dx, 212, 14, BODY, 4)
    # olho grande
    if blink > .6:
        p.stroke([(440, 390), (478, 390)], 6)
    else:
        er = 27 if expr != 'shock' else 31
        p.dot(458, 388, er, (255, 255, 255), 5)
        p.dot(462 + look * 9, 390, 12, INK); p.dot(458 + look * 9, 384, 4, (255, 255, 255))
        if expr == 'smug': p.stroke([(432, 372), (484, 372)], 7)
    # boca (sorrisinho)
    p.arc(470, 420, 14, 8, 20, 160, 4)
    # asa da frente
    wing(280, 190, 135, 175, WING, WINGD)
    wing(225, 320, 105, 85, WING, WINGD)
    # manchas
    yy = ay - (ay - 150) * sc
    p.dot(250, yy, 26 * max(.4, sc), (255, 245, 220), 4)
    p.dot(300, ay - (ay - 230) * sc, 16 * max(.4, sc), (255, 245, 220), 4)
    p.dot(200, ay - (ay - 320) * sc, 14 * max(.4, sc), INK)
    return p.img.resize((600, 600), Image.LANCZOS)


def put_bb(c, x, feet, h, flap=0.0, flip=False, **kw):
    put_sprite(c, 'borboleta', x, feet, h, 1.0, flip, {'flap': 6, 'drum': 4, 'look': 4}, flap=flap, **kw)


@lru_cache(maxsize=4)
def folha_img(w):
    p = Pen(800, 400)
    pts = [(40, 200)] + [(40 + 720 * t, 200 - 170 * math.sin(math.pi * t) ** .8) for t in np.linspace(0, 1, 20)] + \
          [(40 + 720 * t, 200 + 150 * math.sin(math.pi * t) ** .8) for t in np.linspace(1, 0, 20)]
    p.shape(pts, LEAF, LEAFD, 7, 16)
    p.stroke([(40, 200), (760, 200)], 6, LEAFD)
    for t in (.25, .45, .65):
        x = 40 + 720 * t
        p.stroke([(x, 200), (x + 90, 110)], 4, LEAFD); p.stroke([(x, 200), (x + 90, 285)], 4, LEAFD)
    return p.img.resize((int(w), int(w / 2)), Image.LANCZOS)


@lru_cache(maxsize=4)
def flor_img(w):
    p = Pen(400, 700)
    p.line([(200, 690), (210, 420), (200, 240)], LEAFD, 16, 4)
    p.shape(ell_pts(140, 520, 70, 28, 30, rot=-.5), LEAF, LEAFD, 5, 8)
    for a in range(0, 360, 60):
        r = math.radians(a)
        p.shape(ell_pts(200 + 80 * math.cos(r), 210 + 80 * math.sin(r), 62, 62, 30), hexc('#f06aa0'), hexc('#c94780'), 5, 10)
    p.shape(ell_pts(200, 210, 55, 55, 30), hexc('#ffd23f'), hexc('#e0a81c'), 5, 10)
    return p.img.resize((int(w), int(w * 700 / 400)), Image.LANCZOS)


def lagarta(chew=0.0, blink=0):
    p = Pen(600, 300)
    for i in range(6):
        x = 120 + i * 62; y = 210 - 18 * math.sin(i * .9)
        p.shape(ell_pts(x, y, 46, 46, 30), hexc('#8fd14f'), hexc('#5fa02f'), 5, 10)
        p.dot(x, y - 20, 6, hexc('#ffd23f'))
    hx, hy = 500, 175
    p.shape(ell_pts(hx, hy, 58, 56, 30), hexc('#8fd14f'), hexc('#5fa02f'), 6, 10)
    if blink > .6: p.stroke([(490, 160), (530, 160)], 6)
    else:
        p.dot(512, 160, 20, (255, 255, 255), 4); p.dot(518, 162, 8, INK)
    p.dot(520, 200 + 4 * chew, 10 + 6 * chew, hexc('#7a2e2e'), 3)
    for dx in (-10, 16):
        p.line([(hx + dx, hy - 50), (hx + dx + 10, hy - 95)], INK, 4, 0)
    return p.img.resize((600, 300), Image.LANCZOS)


def glow(c, x, y, r, a):
    if a <= 0 or r < 2: return
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(4):
        rr = r * (1 + k * .45)
        d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(255, 230, 90, int(120 * a / (k + 1))))
    c.alpha_composite(lay)


def s0(f):
    c = CEN('floresta', 'day').copy()
    p_ = wt(0, 'pes') - 3
    t = ramp(f, 0, p_)
    bx = lerp(1100, 860, smooth(t)); by = lerp(700, 1000, smooth(t)) + 30 * math.sin(f * .25) * (1 - ramp(f, p_ - 4, p_))
    flap = .5 + .5 * math.sin(f * .9) if f < p_ else .15 * (.5 + .5 * math.sin(f * .2))
    put_bb(c, bx, by, 440, flap, look=-.6 if f >= p_ else .2, flip=True, expr='smug' if f >= p_ else 'calm', blink=blinkAt(f, 2))
    if f >= p_: glow(c, bx - 40, by - 20, 40, pulse(f, p_, 40) * 1.2)
    put_prof(c, 380, 1880, 980, f, expr='shock' if f >= p_ else 'grin', arms='up' if f >= p_ else 'point', look=1)
    if f >= p_: paste_c(c, txt('COM OS PÉS?!', 110, -5), 760, 560, back(ramp(f, p_, p_ + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1230 + kick(f, p_, .8) * 12, z, 0), 'day'


def s1(f):
    c = CEN('floresta', 'day').copy()
    s_ = wt(1, 'sabor') - 3
    l_ = wt(1, 'lingua') - 3
    paste_c(c, flor_img(420), 800, 1450)
    put_bb(c, 810, 1265, 520, .1 + .08 * math.sin(f * .15), look=.2, blink=blinkAt(f, 4))
    if f >= s_:
        a = .6 + .4 * math.sin(f * .3)
        for x in (720, 810, 905):
            glow(c, x, 1255, 26 * back(ramp(f, s_, s_ + 8)), a)
        if f < l_: paste_c(c, txt('SABOR!', 110, -5), 780, 640, back(ramp(f, s_, s_ + 8)))
    put_prof(c, 380, 1840, 700, f, expr='grin' if f >= l_ else 'neutral', arms='point' if f >= l_ else 'chin', look=1)
    if f >= l_: paste_c(c, txt('= LÍNGUA', 110, 5), 760, 640, back(ramp(f, l_, l_ + 8)))
    tz = smooth(ramp(f, 0, 60))
    z = lerp(1.05, 1.18, tz) * (1 + .0009 * f)
    return c, (lerp(640, 680, tz), lerp(1200, 1150, tz), z, 0), 'day'


def s2(f):
    c = CEN('floresta', 'day').copy()
    po = wt(2, 'pousa') - 3
    b_ = wt(2, 'batucando') - 3
    paste_c(c, folha_img(900), 700, 1300)
    t = smooth(ramp(f, 0, po + 4))
    bx = lerp(1150, 780, t); by = lerp(800, 1260, t)
    flap = (.5 + .5 * math.sin(f * .9)) * (1 - ramp(f, po, po + 6)) + .1
    drum = (.5 + .5 * math.sin((f - b_) * 1.25)) if f >= b_ else 0
    put_bb(c, bx, by, 520, flap, drum=drum, look=.5, blink=blinkAt(f, 7))
    if f >= b_:
        paste_c(c, txt('TUM TUM!', 110, 6), 820, 620 + 6 * math.sin(f * 1.25), back(ramp(f, b_, b_ + 8)))
    put_prof(c, 360, 1840, 680, f, expr='shock' if f >= b_ else 'neutral', arms='chin', look=1)
    z = lerp(1.05, 1.16, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (680, 1160 + (4 * math.sin(f * 1.25) if f >= b_ else 0), z, 0), 'day'


def s3(f):
    c = CEN('floresta', 'dusk').copy()
    pr = wt(3, 'provando') - 3
    fi = wt(3, 'filhotes') - 3
    paste_c(c, folha_img(700), 480, 1540)
    drum = .5 + .5 * math.sin(f * 1.25) if f < fi else 0
    put_bb(c, 480, 1500, 400, .1, drum=drum, look=.5, blink=blinkAt(f, 3))
    if pr <= f < fi: paste_c(c, txt('PROVANDO...', 96, -5), 600, 1080, back(ramp(f, pr, pr + 8)))
    if f >= fi - 6:
        cont = Image.new('RGBA', (560, 300), (0, 0, 0, 0))
        fl = folha_img(330); cont.alpha_composite(fl, (10, 100))
        lg = sprite('lagarta', (('blink', 0), ('chew', round(.5 + .5 * math.sin(f * .8), 1))), 170, 2.0, False)
        cont.alpha_composite(lg, (200, 40))
        thought(c, 820, 640, 290, back(ramp(f, fi - 6, fi + 4)), cont)
        paste_c(c, txt('FILHOTES!', 96, 5), 820, 1000, back(ramp(f, fi, fi + 8)))
    put_prof(c, 1000, 1880, 720, f, flip=True, expr='grin' if f >= fi else 'neutral', arms='point', look=-1)
    t = easeOut(ramp(f, 0, 50))
    z = lerp(1.2, 1.08, t) * (1 + .0009 * f)
    return c, (660, 1130, z, lerp(2, 0, t)), 'dusk'


def s4(f):
    c = CEN('floresta', 'dusk').copy()
    pi_ = wt(4, 'pisa') - 3
    sv = wt(4, 'servir') - 3
    paste_c(c, folha_img(560), 880, 1180)
    drum = .5 + .5 * math.sin(f * 1.25) if pi_ <= f < sv else 0
    put_bb(c, 900, 1150, 380, .1 + (.3 * pulse(f, sv, 20)), drum=drum, look=-.5, flip=False,
           expr='smug' if f >= sv else 'calm', blink=blinkAt(f, 5))
    if f >= pi_ and f < sv: paste_c(c, txt('PISA!', 110, -5), 880, 700, back(ramp(f, pi_, pi_ + 8)))
    put_prof(c, 380, 1880, 980, f, expr='grin' if f >= sv else 'smug', arms='shrug' if f >= sv else 'chin', look=1)
    if f >= sv: paste_c(c, txt('BOM APETITE!', 88, 5), 660, 640, back(ramp(f, sv, sv + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (640, lerp(1250, 1200, t) + kick(f, sv, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
