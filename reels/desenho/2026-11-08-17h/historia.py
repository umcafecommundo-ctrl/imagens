"""Um Café com o Mundo — CURIOSIDADE em desenho (08/11/2026 17h).
Fontes: Universidade de Salford (comunicado de 04/11/2026, "Scientists discover two new species of
howler monkey"); AZoLifeSciences (05/11/2026). Estudo na Communications Biology.
Fatos: duas espécies novas de bugio (gênero Alouatta): Alouatta iroi e Alouatta matogrossensis
(bugio-ruivo do Mato Grosso, sul da Amazônia). Genomas de 11 espécies de bugio da América do Sul e
Central + dados de exemplares de museus. Rios Amazonas, Branco e Xingu funcionaram como barreiras por
milhões de anos. Última espécie de bugio descrita antes: Alouatta puruensis (1941), 84 anos antes.
O habitat do A. matogrossensis é uma das regiões que mais perdem floresta no mundo. Batista: entender
quais espécies existem é o primeiro passo para protegê-las."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Cientistas acharam dois macacos novos na Amazônia... e um deles leva o nome de um estado brasileiro.",
    "É o bugio, ou guariba, o macaco famoso pelo ronco que se ouve de longe.",
    "Uma equipe da Universidade de Salford, na Inglaterra, comparou os genes de onze espécies de bugio.",
    "E viu que grandes rios, como o Amazonas, o Branco e o Xingu, separaram esses macacos por milhões de anos.",
    "Assim surgiram duas espécies: o Alouatta iroi, e o bugio ruivo do Mato Grosso, no sul da Amazônia.",
    "São as primeiras espécies novas de bugio descritas em oitenta e quatro anos.",
    "Por que isso importa? O bugio do Mato Grosso vive numa das regiões que mais perdem floresta no mundo.",
    "E só dá pra proteger um bicho... quando a gente sabe que ele existe.",
]
CAPTXT = [
    "Cientistas acharam dois macacos novos na Amazônia...|e um deles leva o nome de um estado brasileiro.",
    "É o bugio, ou guariba,|o macaco famoso pelo ronco que se ouve de longe.",
    "Uma equipe da Universidade de Salford, na Inglaterra,|comparou os genes de 11 espécies de bugio.",
    "E viu que grandes rios, como o Amazonas, o Branco e o Xingu,|separaram esses macacos por milhões de anos.",
    "Assim surgiram duas espécies: o Alouatta iroi,|e o bugio-ruivo do Mato Grosso, no sul da Amazônia.",
    "São as primeiras espécies novas de bugio descritas em 84 anos.",
    "Por que isso importa? O bugio do Mato Grosso vive|numa das regiões que mais perdem floresta no mundo.",
    "E só dá pra proteger um bicho... quando a gente sabe que ele existe.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'estado', 6), (1, 'ronco', 4), (2, 'onze', 4), (3, 'xingu', 6), (4, 'grosso', 6), (5, 'quatro', 6), (6, 'floresta', 6), (7, 'existe', 8)]

RUIVO = hexc('#b8572c'); RUIVOD = hexc('#7f3518')
ESC = hexc('#5c4636'); ESCD = hexc('#3c2c22')
FACE = hexc('#3e2e2a'); FACED = hexc('#2a1e1c')
GH = hexc('#c9cfe0'); GHD = hexc('#9aa3bd')
WOOD = hexc('#9a6a3e'); WOODD = hexc('#6a4526')


# ------------------------------------------------------------------ bugio sentado, de lado (olha p/ direita)
def bugio(phase=0.0, blink=0, expr='calm', look=0.3, howl=0.0, dark=0, sway=0.0):
    """600x800, pés/assento em y~780."""
    p = Pen(600, 800)
    c, d = (ESC, ESCD) if dark else (RUIVO, RUIVOD)
    s = math.sin(phase * 2 * math.pi)
    # rabo preênsil caindo e enrolando
    tx = 150 + s * 10
    p.line(curve((190, 600), (90, 650), (tx - 30, 730), 14) + curve((tx - 30, 730), (150 + s * 10, 790), (100 + s * 8, 760), 8), d, 26, 5)
    # corpo
    p.shape(ell_pts(290, 560, 150, 200, 64, -.15 + sway * .05), c, d, 6, 24)
    # perna dobrada + pé
    p.shape(ell_pts(350, 720, 130, 62, 48, .05), c, d, 6, 14)
    p.shape(ell_pts(460, 770, 50, 22, 30), FACE, None, 5)
    # braço
    ay = 470
    hx, hy = 450, 690 + s * 6
    p.line([(370, ay), (hx, hy)], d, 46, 5)
    p.shape(ell_pts(hx + 6, hy + 10, 30, 22, 30), FACE, None, 5)
    # cabeça (pelo) + barba/papo grande
    p.shape(ell_pts(370, 300, 130, 125, 56), c, d, 6, 16)
    p.shape(ell_pts(420, 410, 95, 80, 48), mul(c, .88), d, 6, 10)
    # rosto escuro e focinho
    p.shape(ell_pts(445, 305, 85, 92, 48), FACE, FACED, 5, 10)
    p.shape(ell_pts(500, 350, 60, 44, 40), mul(FACE, 1.15), None, 5)
    p.dot(540, 335, 9, FACED)
    # olho grande
    p.dot(465, 280, 34, (255, 255, 255), 5)
    if blink or expr == 'sleep':
        p.arc(465, 280, 32, 12, 0, 180, 6, (255, 255, 255))
        p.shape([(430, 246), (500, 246), (500, 280), (430, 280)], FACE, None, 0)
        p.arc(465, 280, 32, 10, 0, 180, 6)
    else:
        p.dot(465 + look * 14, 283, 17, INK)
        p.dot(459 + look * 14, 275, 6, (255, 255, 255))
        if expr == 'side':
            p.shape([(428, 244), (502, 244), (502, 272), (428, 272)], FACE, None, 0)
            p.stroke([(430, 272), (500, 272)], 5, (255, 255, 255))
        if expr == 'shock':
            p.arc(465, 236, 30, 9, 200, 340, 6, hexc('#e8d8c8'))
    # boca
    if howl > .05:
        p.shape(ell_pts(528, 372, 16 + howl * 16, 8 + howl * 30, 30), hexc('#2a0f12'), None, 4)
        p.shape(ell_pts(528, 378 + howl * 14, 10 + howl * 8, 4 + howl * 6, 20), hexc('#c0505a'), None, 0)
    else:
        p.arc(515, 372, 20, 8, 20, 160, 5, hexc('#e8d8c8') if expr == 'grin' else INK)
    # orelha
    p.shape(ell_pts(372, 300, 22, 30, 24), mul(c, .8), d, 4, 6)
    return p.img


def galho():
    """galho horizontal 1242x120."""
    p = Pen(1242, 140)
    p.shape([(-20, 40), (1262, 30), (1262, 100), (-20, 110)], WOOD, WOODD, 6, 18)
    for x in (240, 620, 980):
        p.shape(ell_pts(x, 40, 70, 34, 30, .3), hexc('#4f8a4a'), hexc('#3f7a3c'), 5, 8)
    return p.img


def dna(phase=0.0):
    p = Pen(260, 700)
    pts1 = []; pts2 = []
    for i in range(41):
        y = 20 + i * 16.5
        a = i * .32 + phase * 2 * math.pi
        pts1.append((130 + 90 * math.sin(a), y)); pts2.append((130 - 90 * math.sin(a), y))
    for i in range(0, 41, 3):
        p.line([pts1[i], pts2[i]], hexc('#ffd04a') if (i // 3) % 2 else hexc('#7ad0ff'), 8, 3)
    p.line(pts1, hexc('#ff6a8a'), 14, 4); p.line(pts2, hexc('#6a8aff'), 14, 4)
    return p.img


def cabinet(op=0.0):
    p = Pen(700, 900)
    p.shape([(60, 60), (640, 60), (640, 890), (60, 890)], WOOD, WOODD, 6, 18)
    for i, y in enumerate((120, 380, 640)):
        dx = op * 120 if i == 1 else 0
        p.shape([(90 + dx * .3, y + dx * .4), (610 + dx * .3, y + dx * .4), (610 + dx * .3, y + 220 + dx * .4), (90 + dx * .3, y + 220 + dx * .4)],
                mul(WOOD, 1.08), WOODD, 5, 10)
        p.shape([(290 + dx * .3, y + 90 + dx * .4), (410 + dx * .3, y + 90 + dx * .4), (410 + dx * .3, y + 130 + dx * .4), (290 + dx * .3, y + 130 + dx * .4)],
                hexc('#f3ead6'), None, 4)
    return p.img


def shield():
    p = Pen(400, 460)
    p.shape([(40, 60), (200, 10), (360, 60), (350, 260), (200, 450), (50, 260)], hexc('#4caf6a'), hexc('#2f8048'), 7, 22)
    p.stroke([(120, 230), (185, 300), (290, 160)], 30, (255, 255, 255))
    return p.img


def tag():
    p = Pen(620, 170)
    p.shape([(60, 25), (600, 25), (600, 145), (60, 145), (10, 85)], hexc('#f6ecd2'), hexc('#d8c8a0'), 5, 8)
    p.dot(52, 85, 11, INK)
    return p.img


def toco():
    p = Pen(260, 200)
    p.shape([(40, 60), (220, 60), (230, 190), (30, 190)], hexc('#8a6440'), hexc('#5e4228'), 6, 12)
    p.shape(ell_pts(130, 60, 90, 28, 40), hexc('#d9b98a'), None, 5)
    p.arc(130, 60, 50, 14, 0, 360, 3, hexc('#a8865a'))
    return p.img


RIOS = {
    'amazonas': [(-40, 900), (300, 830), (520, 960), (800, 880), (1290, 960)],
    'branco': [(420, 200), (480, 420), (430, 640), (540, 900)],
    'xingu': [(980, 1700), (900, 1450), (1000, 1200), (900, 950)],
}


@lru_cache(maxsize=2)
def rios_bg():
    p = Pen(BW, BH)
    p.shape([(-20, -20), (BW + 20, -20), (BW + 20, BH + 20), (-20, BH + 20)], hexc('#7fb85a'), hexc('#6a9e48'), 0, 0)
    rnd = random.Random(7)
    for i in range(60):
        x, y = rnd.randint(0, BW), rnd.randint(0, BH)
        p.shape(ell_pts(x, y, 46, 38, 24), hexc('#5f9a48'), None, 0)
    return p.img.resize((BW, BH), Image.LANCZOS)


def rio_pts(nome, t=1.0):
    pts = RIOS[nome]; out = []
    for i in range(len(pts) - 1):
        out += curve(pts[i], ((pts[i][0] + pts[i + 1][0]) / 2 + 40, (pts[i][1] + pts[i + 1][1]) / 2 - 30), pts[i + 1], 10)
    n = max(2, int(len(out) * t))
    return out[:n]


def put_m(c, x, feet, h, flip=False, f=0, seed=1, **kw):
    put_sprite(c, 'bugio', x, feet, h, 600 / 800, flip, {'phase': 8, 'look': 4, 'howl': 6, 'sway': 4},
               phase=(f * .02 + seed * .3) % 1, blink=1 if blinkAt(f, seed) > .6 else 0, sway=math.sin(f * .07 + seed), **kw)


def put_img(c, fn, x, feet, h, aspect, **kw):
    put_sprite(c, fn, x, feet, h, aspect, False, {'op': 8, 'phase': 12}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def floresta_galho(luz='day', y=1150):
    c = CEN('floresta', luz).copy()
    c.alpha_composite(galho(), (0, y - 40))
    return c


# ------------------------------------------------------------------ cenas
def s0(f):
    c = floresta_galho('day', 1150)
    d = wt(0, 'dois') - 3
    for i, (x, fl) in enumerate(((420, False), (840, True))):
        if f >= d + i * 4:
            s = back(ramp(f, d + i * 4, d + i * 4 + 9))
            put_m(c, x, 1150 + 20, 600 * s, flip=fl, f=f, seed=1 + i, dark=i == 0, look=.6,
                  expr='shock' if f >= wt(0, 'estado') - 3 else 'calm')
    num(c, '2 MACACOS NOVOS', 640, 470, f, d, 96)
    es = wt(0, 'estado') - 3
    num(c, 'MATO GROSSO?!', 640, 1420, f, es, 110, 4)
    z = lerp(1.35, 1.0, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, es)
    return c, (640, 1080 + k * 10, z, k), 'day'


def s1(f):
    c = floresta_galho('day', 1250)
    ro = wt(1, 'ronco') - 3
    hw = smooth(ramp(f, ro - 4, ro + 4)) * (1 - smooth(ramp(f, ro + 40, ro + 50)))
    put_m(c, 600, 1270, 780, f=f, seed=3, howl=hw, look=.8, expr='calm')
    if f >= ro:
        rings(c, 920, 960, f, ro, 46, 1.4)
        num(c, 'UOOOOOH!', 640, 1420, f, ro, 110, -3)
    num(c, 'BUGIO', 400, 400, f, wt(1, 'bugio') - 3, 130)
    num(c, 'GUARIBA', 840, 560, f, wt(1, 'guariba') - 3, 110, 4)
    k = kick(f, ro)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 140))) * (1 + .0005 * f)
    return c, (lerp(600, 680, smooth(ramp(f, 0, 140))), 1050 + k * 8, z, k), 'day'


def s2(f):
    c = CEN('lab', 'day').copy()
    put_sci(c, 300, 1700, 820, f, 2, arms='point' if f >= wt(2, 'comparou') - 3 else 'clip', bun=True, skin=1, expr='neutral', look=1)
    ge = wt(2, 'genes') - 3
    if f >= ge:
        put_img(c, 'dna', 900, 1300, 560 * back(ramp(f, ge, ge + 8)), 260 / 700, phase=(f * .02) % 1)
    num(c, 'INGLATERRA', 640, 470, f, wt(2, 'inglaterra') - 3, 100)
    num(c, '11 ESPÉCIES', 760, 660, f, wt(2, 'onze') - 3, 120, 4)
    cx = lerp(560, 680, smooth(ramp(f, ge - 10, ge + 30)))
    return c, (cx, 1180, lerp(1.0, 1.1, smooth(ramp(f, 0, 200))) * (1 + .0003 * f), 0), 'day'


def s3(f):
    c = rios_bg().copy()
    p = Pen(BW, BH)
    for nome, lab, (lx, ly) in (('amazonas', 'AMAZONAS', (300, 1030)), ('branco', 'BRANCO', (620, 330)), ('xingu', 'XINGU', (1000, 1580))):
        w0 = wt(3, nome) - 3
        if f >= w0:
            p.line(rio_pts(nome, smooth(ramp(f, w0, w0 + 14))), hexc('#4a9ad8'), 46, 5)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    for nome, lab, (lx, ly) in (('amazonas', 'AMAZONAS', (330, 1060)), ('branco', 'BRANCO', (680, 330)), ('xingu', 'XINGU', (1000, 1560))):
        num(c, lab, lx, ly, f, wt(3, nome) - 3, 76, -3)
    sp = wt(3, 'separaram') - 3
    put_m(c, 260, 780, 400, f=f, seed=4, look=.5)
    dx = -60 * smooth(ramp(f, sp, sp + 20))
    put_m(c, 760 + dx, 1420, 400, flip=True, f=f, seed=5, dark=1, look=.5)
    num(c, 'MILHÕES DE ANOS', 760, 600, f, wt(3, 'milhoes') - 3, 84, 3)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 180))) * (1 + .0006 * f)
    return c, (640, lerp(1000, 1150, smooth(ramp(f, 0, 180))) + .3 * f, z, 0), 'day'


def s4(f):
    c = floresta_galho('day', 1200)
    io = wt(4, 'iroi') - 3
    mg = wt(4, 'ruivo') - 3
    if f >= io - 6:
        put_m(c, 360, 1220, 620 * back(ramp(f, io - 6, io + 3)), f=f, seed=6, dark=1, look=.4)
    if f >= mg - 4:
        put_m(c, 900, 1220, 640 * back(ramp(f, mg - 4, mg + 5)), flip=True, f=f, seed=7, look=.4, expr='grin')
    if f >= io:
        paste_c(c, tag().resize((560, 154)), 360, 470, back(ramp(f, io, io + 8)))
        paste_c(c, txt('ALOUATTA IROI', 58, 0), 385, 470, back(ramp(f, io, io + 8)))
    gr = wt(4, 'grosso') - 3
    if f >= gr:
        paste_c(c, tag().resize((560, 154)), 880, 660, back(ramp(f, gr, gr + 8)))
        paste_c(c, txt('MATO GROSSO', 64, 0), 905, 660, back(ramp(f, gr, gr + 8)))
    num(c, 'SUL DA AMAZÔNIA', 640, 1430, f, wt(4, 'sul') - 3, 86, -3)
    cx = lerp(480, 800, smooth(ramp(f, io, gr)))
    z = lerp(1.15, 1.05, smooth(ramp(f, 0, 60))) * (1 + .0004 * f)
    return c, (cx, 1050, z, 0), 'day'


def s5(f):
    c = CEN('museu', 'day').copy()
    put_m(c, 640, 1650, 560, f=f, seed=8, look=.6, expr='grin')
    num(c, 'PRIMEIRAS', 640, 520, f, wt(5, 'primeiras') - 3, 110)
    q = wt(5, 'quatro') - 3
    num(c, '84 ANOS', 640, 780, f, q - 6, 200, -4)
    num(c, '1941', 360, 1000, f, q + 4, 90, -6)
    num(c, '2026', 920, 1000, f, q + 4, 90, 6)
    k = kick(f, q - 6)
    z = lerp(1.0, 1.15, easeOut(ramp(f, 0, 90))) * (1 + .0004 * f)
    return c, (640, 1150 + k * 8, z, k), 'day'


def s6(f):
    c = CEN('floresta', 'golden').copy()
    fl = wt(6, 'floresta') - 3
    re = wt(6, 'regioes') - 3
    for i, x in enumerate((180, 420, 860, 1080)):
        if f >= re + i * 3:
            paste_c(c, toco(), x, 1560 + (i % 2) * 70, back(ramp(f, re + i * 3, re + i * 3 + 8)))
            put_dust(c, x, 1500, 120, f - re - i * 3, 14)
    put_m(c, 640, 1500, 480, f=f, seed=9, look=-.2, expr='side' if f >= re else 'calm')
    num(c, 'POR QUE IMPORTA?', 640, 460, f, wt(6, 'importa') - 3, 90)
    num(c, 'MENOS FLORESTA', 640, 680, f, fl, 110, 4)
    k = kick(f, fl)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 160))) * (1 + .0006 * f)
    return c, (640 + .2 * f, 1150 + k * 8, z, lerp(0, 2.5, smooth(ramp(f, re, re + 20))) + k), 'golden'


def s7(f):
    c = floresta_galho('dusk', 1250)
    put_m(c, 600, 1270, 560, f=f, seed=10, look=.7, expr='calm' if f < wt(7, 'existe') - 3 else 'grin')
    pr = wt(7, 'proteger') - 3
    if f >= pr:
        put_img(c, 'shield', 940, 1180, 360 * back(ramp(f, pr, pr + 8)), 400 / 460)
        num(c, 'PROTEÇÃO', 640, 460, f, pr, 120)
    ex = wt(7, 'existe') - 3
    num(c, 'EXISTE!', 640, 680, f, ex, 130, -4)
    z = lerp(1.0, 1.12, easeOut(ramp(f, 0, 80))) * (1 + .0005 * f)
    k = kick(f, ex)
    return c, (lerp(640, 700, smooth(ramp(f, 0, 100))), 1080 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.ting(s.W(0, 'dois') - 3, .3)
    s.thunk(s.W(0, 'estado') - 3, 180, .7)
    s.trill(s.W(1, 'ronco') - 3, .9, .3)
    s.ting(s.W(2, 'genes') - 3, .25)
    s.splash(s.W(3, 'amazonas') - 3, .25)
    s.ting(s.W(4, 'iroi') - 3, .25)
    s.ting(s.W(4, 'grosso') - 3, .3)
    s.thunk(s.W(5, 'quatro') - 9, 160, .8)
    s.thunk(s.W(6, 'regioes') - 3, 120, .7)
    s.ting(s.W(7, 'proteger') - 3, .35)
    s.thunk(s.W(7, 'existe') + 5, 140, .9)
