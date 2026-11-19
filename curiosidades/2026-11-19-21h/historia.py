"""Formato DESENHO: o lugar onde o sol fica 4 meses sem se pôr (Curiosidades da IA, 19/11/2026, 21h).
Categoria: LUGARES E GEOGRAFIA.
Fatos: yr.no (instituto meteorológico da Noruega + NRK), "Polar nights and midnight sun": em Longyearbyen (Svalbard),
sol da meia-noite de 20/4 a 22/8; noite polar a partir de 26/10, o sol volta em 16/2.
Spitsbergen-Svalbard.com: sol da meia-noite de 20/4 até ~20/8; período escuro (sol abaixo do horizonte) de 26/10 a 15/2.
Britannica, "midnight Sun": causado pela inclinação do eixo da Terra em relação ao plano da órbita.
Svalbard = arquipélago da Noruega no oceano Ártico, entre a Noruega continental e o Polo Norte.
Cenários: s0 neve com montanhas (Professor espantado, sol alto) | s1 mapa do Ártico (Svalbard, Noruega, Polo Norte) |
s2 neve, meia-noite com sol (relógio 12h) | s3 espaço (Terra inclinada girando, o topo sempre no sol) |
s4 neve à noite (Professor: a noite também dura quase 4 meses)."""
from kit import *
from functools import lru_cache

LINES = [
    "Tem um lugar onde o sol passa uns quatro meses sem se pôr.",
    "É Svalbard, umas ilhas da Noruega, lá perto do Polo Norte.",
    "Meia-noite... e o sol continua lá no céu.",
    "Você vê, a Terra é inclinada: no verão, aquele pedacinho fica virado pro sol, mesmo com a Terra girando.",
    "Ou seja: lá o dia dura quase quatro meses... e a noite também.",
]
CAPTXT = [
    "Tem um lugar onde o sol passa|uns 4 meses sem se pôr.",
    "É Svalbard, umas ilhas da Noruega,|lá perto do Polo Norte.",
    "Meia-noite... e o sol continua lá no céu.",
    "Você vê, a Terra é inclinada: no verão, aquele pedacinho|fica virado pro sol, mesmo com a Terra girando.",
    "Ou seja: lá o dia dura quase 4 meses... e a noite também.",
]
FALA_TIKTOK = "Você aguentaria? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = [4]
CHECK = [(0, 'sol', 4), (0, 'quatro', 6), (1, 'svalbard', 4), (1, 'norte', 6), (2, 'meianoite', 4), (2, 'ceu', 6),
         (3, 'inclinada', 4), (3, 'girando', 6), (4, 'dia', 4), (4, 'tambem', 8)]


def SFX(s):
    s.ting(s.W(0, 'sol'), .3); s.thunk(s.W(0, 'quatro') - 2, 240, .7)
    s.whoosh(s.W(1, 'svalbard') - 6, .4, .4); s.thunk(s.W(1, 'svalbard') - 1, 300, .5); s.ting(s.W(1, 'norte'), .25)
    for i in range(6): s.thunk(s.W(2, 'meianoite') - 2 + i * 6, 700, .3)
    s.ting(s.W(2, 'ceu'), .35)
    s.thunk(s.W(3, 'inclinada') - 2, 200, .6); s.whoosh(s.W(3, 'girando') - 4, .5, .4)
    s.trill(s.W(4, 'tambem'), 1.0, .3)


@lru_cache(maxsize=8)
def sol_img(size):
    p = Pen(300, 300)
    for a in range(0, 360, 30):
        r = math.radians(a)
        p.line([(150 + 95 * math.cos(r), 150 + 95 * math.sin(r)), (150 + 135 * math.cos(r), 150 + 135 * math.sin(r))], hexc('#ffb52e'), 12, 4)
    p.shape(ell_pts(150, 150, 82, 82, 40), hexc('#ffd84a'), hexc('#f0a81c'), 6, 14)
    p.dot(125, 140, 9, INK); p.dot(175, 140, 9, INK); p.arc(150, 165, 22, 14, 20, 160, 5)
    s = max(4, int(size))
    return p.img.resize((s, s), Image.LANCZOS)


def sol(c, x, y, size, f):
    if size < 8: return
    s = int(round(size * (1 + .03 * math.sin(f * .2)) / 6) * 6)
    paste_c(c, sol_img(s).rotate(f * .6 % 30, Image.BICUBIC), x, y)


@lru_cache(maxsize=1)
def mapa_bg():
    p = Pen(1242, 2208)
    p.poly([(0, 0), (1242, 0), (1242, 2208), (0, 2208)], hexc('#5aa6d6'))
    for y in range(120, 2208, 160):
        for x in range((y // 160) % 2 * 120, 1242, 240): p.arc(x + 60, y, 34, 8, 200, 340, 4, hexc('#8cc4e6'))
    # gelo do Polo Norte no topo
    p.shape([(-20, -20), (1262, -20), (1262, 300)] + [(1242 - i * 62, 300 + 40 * math.sin(i * 1.3)) for i in range(21)] + [(-20, 300)],
            hexc('#f4f8fb'), hexc('#cddbe6'), 6, 14)
    # Svalbard (ilhas)
    for cx, cy, rx, ry in ((560, 820, 130, 160), (760, 760, 90, 110), (680, 980, 60, 50)):
        p.shape(ell_pts(cx, cy, rx, ry, 30, egg=.2), hexc('#e9eef2'), hexc('#b9c7d2'), 6, 12)
    # Noruega continental (embaixo à direita)
    p.shape([(1262, 1250), (1100, 1330), (980, 1500), (880, 1700), (760, 1950), (700, 2230), (1262, 2230)],
            hexc('#9bcf6a'), hexc('#76a64a'), 6, 16)
    return p.img.resize((1242, 2208), Image.LANCZOS)


def alfinete(c, x, y, s):
    if s < .05: return
    d = ImageDraw.Draw(c)
    r = 38 * s
    d.polygon([(x - r * .8, y - r * 1.6), (x + r * .8, y - r * 1.6), (x, y)], fill=(230, 60, 60, 255), outline=INK + (255,))
    d.ellipse((x - r, y - r * 2.6, x + r, y - r * .6), fill=(230, 60, 60, 255), outline=INK + (255,), width=max(1, int(6 * s)))
    d.ellipse((x - r * .4, y - r * 2.0, x + r * .4, y - r * 1.2), fill=(255, 255, 255, 255))


def terra(c, cx, cy, R, f, spin):
    """Terra em corte simples: inclinada para o sol (à esquerda); metade da direita na sombra; alfinete no topo gira e fica no sol."""
    if R < 8: return
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=(70, 140, 220, 255))
    tilt = math.radians(-23)
    rnd = random.Random(3)
    for k in range(5):  # continentes que passam com o giro
        lon = (k * 1.25 + spin) % (2 * math.pi)
        if math.cos(lon) < -.1: continue
        lat = rnd.uniform(-.6, .6)
        x = cx + R * .8 * math.sin(lon) * math.cos(lat); y = cy + R * .8 * math.sin(lat)
        rr = R * .22 * max(.3, math.cos(lon))
        d.ellipse((x - rr, y - rr * .8, x + rr, y + rr * .8), fill=(120, 190, 90, 255))
    m = Image.new('L', c.size, 0); ImageDraw.Draw(m).ellipse((cx - R, cy - R, cx + R, cy + R), fill=255)
    out = Image.new('RGBA', c.size, (0, 0, 0, 0)); out.paste(lay, (0, 0), m)
    # sombra: metade da direita
    sh = Image.new('RGBA', c.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle((cx + R * .05, cy - R, cx + R, cy + R), fill=(10, 14, 50, 150))
    sm = Image.new('L', c.size, 0); sm.paste(m, (0, 0))
    out.alpha_composite(Image.composite(sh, Image.new('RGBA', c.size, (0, 0, 0, 0)), sm))
    out = out.rotate(math.degrees(-tilt) * 0, center=(cx, cy))
    c.alpha_composite(out)
    dd = ImageDraw.Draw(c)
    dd.ellipse((cx - R, cy - R, cx + R, cy + R), outline=INK + (255,), width=10)
    # eixo inclinado (topo para o sol, à esquerda)
    ax, ay = math.sin(tilt) * R * 1.35, math.cos(tilt) * R * 1.35
    dd.line([(cx + ax, cy - ay), (cx - ax, cy + ay)], fill=(250, 250, 250, 255), width=8)
    # alfinete de Svalbard: gira num círculo pequeno em volta do topo do eixo, sempre do lado claro
    px = cx + ax * .78 + R * .16 * math.sin(spin); py = cy - ay * .78 + R * .05 * math.cos(spin)
    alfinete(c, px, py, R / 360)


def s0(f):
    c = CEN('neve', 'day').copy()
    so = wt(0, 'sol') - 3
    q_ = wt(0, 'quatro') - 3
    sol(c, 900, 520 - 30 * smooth(ramp(f, 0, 40)), 300 * back(ramp(f, so - 6, so + 4)) if f >= so - 6 else 0, f)
    put_prof(c, 380, 1880, 980, f, expr='shock' if f >= q_ else 'grin', arms='up' if f >= q_ else 'point', look=1)
    if f >= q_: paste_c(c, txt('4 MESES!', 130, -5), 760, 860, back(ramp(f, q_, q_ + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1200 + kick(f, q_, .8) * 12, z, 0), 'day'


def s1(f):
    c = mapa_bg().copy()
    sv = wt(1, 'svalbard') - 3
    nr = wt(1, 'noruega') - 3
    po = wt(1, 'norte') - 3
    alfinete(c, 600, 820, back(ramp(f, sv, sv + 8)) * 1.6 if f >= sv else 0)
    if f >= sv: paste_c(c, txt('SVALBARD', 100, -4), 620, 1120, back(ramp(f, sv, sv + 8)))
    if f >= nr: paste_c(c, txt('NORUEGA', 80, 4), 960, 1700, back(ramp(f, nr, nr + 8)))
    if f >= po: paste_c(c, txt('POLO NORTE', 90, 3), 640, 430, back(ramp(f, po, po + 8)))
    put_prof(c, 300, 1950, 680, f, expr='proud', arms='point', look=1)
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.25, 1.02, t) * (1 + .0009 * f)
    return c, (lerp(640, 640, t), lerp(1000, 1150, t), z, 0), 'day'


def s2(f):
    c = CEN('neve', 'day').copy()
    me = wt(2, 'meianoite') - 3
    ce = wt(2, 'ceu') - 3
    sol(c, 900, 560, 280, f)
    spin = ramp(f, me, me + 20)
    paste_c(c, clock_img(round((11.4 + spin * .6) * 8) / 8, round((48 + spin * 12) * 4) / 4 % 60, 300), 380, 700, back(ramp(f, me - 6, me + 2)) if f >= me - 6 else 0)
    if me <= f < ce: paste_c(c, txt('MEIA-NOITE!', 100, -5), 640, 980, back(ramp(f, me, me + 8)))
    put_prof(c, 420, 1900, 820, f, expr='nervous' if f >= ce else 'neutral', arms='shrug' if f >= ce else 'point', look=1)
    if f >= ce: paste_c(c, txt('E O SOL LÁ NO CÉU!', 84, 5), 660, 980, back(ramp(f, ce, ce + 8)))
    z = lerp(1.1, 1.2, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (640, 1150, z, 0), 'day'


def s3(f):
    c = CEN('espaco', 'dusk').copy()
    inc = wt(3, 'inclinada') - 3
    gi = wt(3, 'girando') - 3
    sol(c, 150, 760, 420, f)
    spin = f * .12
    terra(c, 760, 800, 330, f, spin)
    if f >= inc and f < gi: paste_c(c, txt('INCLINADA!', 96, -5), 760, 330, back(ramp(f, inc, inc + 8)))
    if f >= gi: paste_c(c, txt('SEMPRE NO SOL!', 90, 5), 760, 330, back(ramp(f, gi, gi + 8)))
    put_prof(c, 900, 1900, 720, f, flip=True, expr='grin' if f >= gi else 'neutral', arms='point', look=-1)
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.15, 1.03, t) * (1 + .0009 * f)
    return c, (680, 1100, z, lerp(2, 0, t)), 'dusk'


@lru_cache(maxsize=1)
def noite_neve():
    c = CEN('neve', 'dusk').copy()
    c.alpha_composite(Image.new('RGBA', c.size, (8, 12, 50, 140)))
    return c


def s4(f):
    c = noite_neve().copy()
    di = wt(4, 'dia') - 3
    ta = wt(4, 'tambem') - 3
    if f < ta:
        sol(c, 900, 560, 260, f)
    else:
        lua = Image.new('RGBA', (300, 300), (0, 0, 0, 0)); d = ImageDraw.Draw(lua)
        d.ellipse((40, 40, 260, 260), fill=(245, 240, 210, 255), outline=INK + (255,), width=8)
        d.ellipse((110, 20, 300, 230), fill=(0, 0, 0, 0))
        paste_c(c, lua, 900, 560, back(ramp(f, ta, ta + 8)))
    put_prof(c, 380, 1880, 980, f, expr='pained' if f >= ta else 'smug', arms='shrug' if f >= ta else 'chin', look=1)
    if di <= f < ta: paste_c(c, txt('DIA: 4 MESES', 84, -5), 640, 900, back(ramp(f, di, di + 8)))
    if f >= ta: paste_c(c, txt('NOITE: TAMBÉM!', 80, 5), 640, 900, back(ramp(f, ta, ta + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (640, lerp(1220, 1180, t) + kick(f, ta, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
