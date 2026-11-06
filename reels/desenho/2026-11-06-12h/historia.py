"""Um Café com o Mundo — CURIOSIDADE em desenho (06/11/2026 12h).
Fontes: The Conversation (Kenny Travouillon, Museu da Austrália Ocidental / Curtin University),
republicado por phys.org e Capital (03/11/2026); Nature World News (05/11/2026). Estudo no
Australian Journal of Taxonomy (doi:10.54102/ajt.3ej9p).
Fatos: investigação de 10 anos (começou em 2016) com medidas de crânios e dentes e DNA de exemplares
de museus, alguns coletados há mais de 100 anos. Duas espécies novas de bandicoot-marrom (gênero Isoodon):
Isoodon microtis (pequeno bandicoot-marrom, sul da Austrália), que se acredita extinto há cerca de um século,
e Isoodon moresbyensis (Nova Guiné), antes tratado como subespécie do bandicoot-marrom-do-norte.
O grupo passa de 5 para 7 espécies. Os autores: taxonomia é a base do planejamento de conservação."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Cientistas descobriram dois bichos novos... dentro de gavetas de museu.",
    "É o bandicoot, um marsupial da Austrália que carrega o filhote numa bolsa, como o canguru.",
    "Por dez anos, uma equipe do Museu da Austrália Ocidental mediu crânios e analisou o DNA de animais guardados, alguns há mais de cem anos.",
    "E achou duas espécies que ninguém tinha reconhecido. Uma vive na Nova Guiné, e era tratada só como uma variação de outra.",
    "Mas a outra, o pequeno bandicoot marrom, do sul da Austrália, provavelmente sumiu há cerca de um século.",
    "Por que isso importa? Saber quantas espécies existem é a base pra decidir quais bichos precisam de proteção.",
    "E esse aí ganhou nome só depois de desaparecer.",
]
CAPTXT = [
    "Cientistas descobriram dois bichos novos...|dentro de gavetas de museu.",
    "É o bandicoot, um marsupial da Austrália|que carrega o filhote numa bolsa, como o canguru.",
    "Por 10 anos, uma equipe do Museu da Austrália Ocidental|mediu crânios e analisou o DNA de animais guardados,|alguns há mais de 100 anos.",
    "E achou duas espécies que ninguém tinha reconhecido.|Uma vive na Nova Guiné,|e era tratada só como uma variação de outra.",
    "Mas a outra, o pequeno bandicoot marrom, do sul da Austrália,|provavelmente sumiu há cerca de um século.",
    "Por que isso importa? Saber quantas espécies existem|é a base pra decidir quais bichos precisam de proteção.",
    "E esse aí ganhou nome só depois de desaparecer.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'gavetas', 6), (1, 'bolsa', 4), (2, 'dez', 4), (2, 'cem', 6), (3, 'guine', 6), (4, 'seculo', 6), (5, 'protecao', 6), (6, 'desaparecer', 8)]

FUR = hexc('#a8794e'); FURD = hexc('#7a5434'); BELLY = hexc('#e2c49a'); NOSE = hexc('#e59a9a')
GH = hexc('#c9cfe0'); GHD = hexc('#9aa3bd')
WOOD = hexc('#9a6a3e'); WOODD = hexc('#6a4526')


def mixc(a, b, t):
    return tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))


# ------------------------------------------------------------------ bandicoot (de lado, olhando p/ direita)
def bandi(phase=0.0, blink=0, expr='calm', look=0.3, ghost=0, joey=0, sniff=0.0):
    """600x460, pés em y~445."""
    p = Pen(600, 460)
    c, d, b = (GH, GHD, hexc('#e6e9f2')) if ghost else (FUR, FURD, BELLY)
    s = math.sin(phase * 2 * math.pi)
    # rabo fino
    p.line(curve((150, 300), (50, 330), (20, 400), 10), d, 12, 4)
    # pernas de trás e da frente
    for k, (x0, y0) in enumerate(((190, 330), (380, 340))):
        for j, dx in enumerate((-14, 14)):
            sw = s * (12 if (j + k) % 2 else -12)
            col = mul(c, .8) if j == 0 else c
            p.line([(x0 + dx, y0), (x0 + dx + sw, 430)], col, 22 if k == 0 else 16, 4)
            p.shape(ell_pts(x0 + dx + sw + 14, 438, 24, 10), col, None, 4)
    # corpo
    p.shape(ell_pts(270, 280, 170, 110, 64, -.05, .1), c, d, 6, 22)
    p.shape(ell_pts(300, 330, 110, 50, 40), b, None, 0)
    if joey and not ghost:
        p.shape(ell_pts(300, 330, 50, 30, 30), mul(b, .9), None, 4)
        p.shape(ell_pts(300, 300, 30, 26, 30), c, d, 4, 6)
        p.dot(310, 296, 6, INK)
        p.shape(ell_pts(326, 306, 14, 8, 20), c, None, 3)
    # cabeça + focinho comprido
    hx, hy = 410, 220 + sniff * 6
    p.shape(curve((420, 170), (500, 175), (560 + sniff * 6, 225), 12) + curve((560 + sniff * 6, 225), (490, 275), (420, 270), 12),
            c, d, 6, 10)
    p.shape(ell_pts(410, 220, 75, 68, 48), c, d, 6, 12)
    p.dot(560 + sniff * 6, 225, 13, NOSE if not ghost else GHD, 4)
    # orelha redonda
    p.shape(ell_pts(395, 145, 30, 40, 30, -.3), c, d, 5, 8)
    p.shape(ell_pts(397, 150, 15, 24, 20, -.3), NOSE if not ghost else GHD, None, 0)
    # olho grande
    p.dot(445, 200, 30, (255, 255, 255), 5)
    if blink or expr == 'sleep':
        p.arc(445, 200, 28, 10, 0, 180, 6)
    else:
        p.dot(445 + look * 12, 202, 15, INK)
        p.dot(440 + look * 12, 195, 5, (255, 255, 255))
        if expr == 'side':
            p.shape([(412, 170), (478, 170), (478, 192), (412, 192)], c, None, 0)
            p.stroke([(414, 192), (476, 192)], 5)
        if expr == 'shock':
            p.arc(445, 160, 26, 8, 200, 340, 5)
    # boca
    p.arc(510, 248, 18, 8, 20, 160, 4)
    return p.img


def cabinet(op=0.0, lab=''):
    """armário de museu com 3 gavetas; a do meio abre (op 0..1). 700x900, base y~890."""
    p = Pen(700, 900)
    p.shape([(60, 60), (640, 60), (640, 890), (60, 890)], WOOD, WOODD, 6, 18)
    for i, y in enumerate((120, 380, 640)):
        dx = op * 120 if i == 1 else 0
        if i == 1 and op > 0:
            p.poly([(90, y + 230), (610, y + 230), (610 + dx, y + 230 + dx * .5), (90 + dx, y + 230 + dx * .5)], WOODD, 4)
        p.shape([(90 + dx * .3, y + dx * .4), (610 + dx * .3, y + dx * .4), (610 + dx * .3, y + 220 + dx * .4), (90 + dx * .3, y + 220 + dx * .4)],
                mixc(WOOD, (255, 255, 255), .08), WOODD, 5, 10)
        p.shape([(290 + dx * .3, y + 90 + dx * .4), (410 + dx * .3, y + 90 + dx * .4), (410 + dx * .3, y + 130 + dx * .4), (290 + dx * .3, y + 130 + dx * .4)],
                hexc('#f3ead6'), None, 4)
        p.line([(320 + dx * .3, y + 175 + dx * .4), (380 + dx * .3, y + 175 + dx * .4)], hexc('#d9b45a'), 10, 3)
    return p.img


def skull():
    """crânio de bandicoot de lado. 500x260, base y~250."""
    p = Pen(500, 260)
    p.shape(curve((40, 200), (60, 40), (260, 70), 14) + curve((260, 70), (420, 110), (480, 190), 10) + [(480, 210), (60, 240)],
            hexc('#f1ead6'), hexc('#cfc4a6'), 6, 14)
    p.dot(170, 130, 40, hexc('#3a2e2a'), 4)
    for i in range(7):
        x = 230 + i * 34
        p.poly([(x, 205), (x + 22, 205), (x + 11, 235)], (255, 255, 255), 3)
    return p.img


def dna(phase=0.0):
    """hélice de DNA. 260x700, base y~690."""
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


def shield():
    p = Pen(400, 460)
    p.shape([(40, 60), (200, 10), (360, 60), (350, 260), (200, 450), (50, 260)], hexc('#4caf6a'), hexc('#2f8048'), 7, 22)
    p.stroke([(120, 230), (185, 300), (290, 160)], 30, (255, 255, 255))
    return p.img


def tag(text='?'):
    p = Pen(520, 200)
    p.shape([(60, 30), (500, 30), (500, 170), (60, 170), (10, 100)], hexc('#f6ecd2'), hexc('#d8c8a0'), 5, 8)
    p.dot(55, 100, 12, INK)
    return p.img


@lru_cache(maxsize=2)
def museum_bg():
    from PIL import ImageDraw
    S = 2; W, H = BW * S, BH * S
    img = Image.new('RGB', (W, H), hexc('#3d3a5c')); d = ImageDraw.Draw(img)
    fl = 1660 * S
    d.rectangle([0, fl, W, H], fill=hexc('#6a5a4a')); d.line([(0, fl), (W, fl)], fill=INK, width=6 * S)
    for x in range(0, W, 160 * S): d.line([(x, fl), (x - 200 * S, H)], fill=hexc('#5a4a3c'), width=4 * S)
    d.polygon([(470 * S, 0), (770 * S, 0), (1000 * S, fl), (240 * S, fl)], fill=hexc('#5a5680'))
    return img.resize((BW, BH), Image.LANCZOS).convert('RGBA')


def put_b(c, x, feet, h, flip=False, f=0, run=0, seed=1, **kw):
    ph = ((f * .08 + seed * .3) % 1) if run else 0
    put_sprite(c, 'bandi', x, feet, h, 600 / 460, flip, {'phase': 8, 'sniff': 4, 'look': 4},
               phase=ph, blink=1 if blinkAt(f, seed) > .6 else 0, **kw)


def put_img(c, fn, x, feet, h, aspect, **kw):
    put_sprite(c, fn, x, feet, h, aspect, False, {'op': 8, 'phase': 12}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = museum_bg().copy()
    g = wt(0, 'gavetas') - 3
    op = smooth(ramp(f, g - 6, g + 6))
    put_img(c, 'cabinet', 640, 1700, 1000, 700 / 900, op=op)
    d = wt(0, 'dois') - 3
    if f >= g:
        s = back(ramp(f, g + 2, g + 10))
        put_b(c, 520, 1130 - 40 * s, 400 * s, f=f, seed=1, expr='shock' if f < g + 30 else 'calm', look=.6)
        put_b(c, 800, 1130 - 40 * s, 340 * s, flip=True, f=f, seed=2, look=.6)
    num(c, '2 BICHOS NOVOS', 640, 600, f, d, 100)
    if f >= g: num(c, '?!', 1000, 820, f, g + 4, 140, 8)
    z = lerp(1.3, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, g + 2)
    return c, (640, 1200 + k * 10, z, k), 'day'


def s1(f):
    c = BG('day').copy()
    x = lerp(300, 700, ramp(f, 0, 150))
    bo = wt(1, 'bolsa') - 3
    put_b(c, x, 1560, 480, f=f, run=1 if f < bo else 0, seed=3, joey=1 if f >= bo else 0, look=.5)
    num(c, 'BANDICOOT', 640, 560, f, wt(1, 'bandicoot') - 3, 140)
    num(c, 'MARSUPIAL', 640, 760, f, wt(1, 'marsupial') - 3, 100, 3)
    num(c, 'AUSTRÁLIA', 640, 940, f, wt(1, 'australia') - 3, 90, -3)
    if f >= bo:
        paste_c(c, txt('BOLSA!', 90, 6), x + 120, 1080, back(ramp(f, bo, bo + 8)))
    k = kick(f, bo)
    return c, (lerp(560, 760, ramp(f, 0, 150)), 1250 + k * 8, lerp(1.0, 1.15, smooth(ramp(f, 0, 120))), k), 'day'


def s2(f):
    c = BG('lab').copy()
    put_sci(c, 330, 1700, 820, f, 1, arms='point' if f >= wt(2, 'mediu') - 3 else 'clip', bun=True, skin=1, expr='neutral', look=1)
    cr = wt(2, 'cranios') - 3
    if f >= cr:
        paste_c(c, skull().resize((420, 218)), 860, 1240, back(ramp(f, cr, cr + 8)))
    dn = wt(2, 'dna') - 3
    if f >= dn:
        s = back(ramp(f, dn, dn + 8))
        put_img(c, 'dna', 1050, 1180, 500 * s, 260 / 700, phase=(f * .02) % 1)
    num(c, '10 ANOS', 760, 640, f, wt(2, 'dez') - 3, 120)
    num(c, '+100 ANOS', 760, 860, f, wt(2, 'cem') - 3, 110, 4)
    cx = lerp(560, 720, smooth(ramp(f, cr - 10, dn + 10)))
    return c, (cx, 1220, lerp(1.05, 1.12, smooth(ramp(f, 0, 200))) * (1 + .0003 * f), 0), 'day'


def s3(f):
    c = BG('day').copy()
    du = wt(3, 'duas') - 3
    s = back(ramp(f, du, du + 8))
    put_b(c, 380, 1500, 380 * s, f=f, seed=4, look=.4)
    put_b(c, 880, 1500, 380 * back(ramp(f, du + 4, du + 12)), flip=True, f=f, seed=5, look=.4)
    num(c, '2 ESPÉCIES', 560, 680, f, du, 110)
    ng = wt(3, 'guine') - 3
    if f >= ng:
        paste_c(c, txt('NOVA GUINÉ', 80, -4), 380, 900, back(ramp(f, ng, ng + 8)))
    va = wt(3, 'variacao') - 3
    if f >= va:
        paste_c(c, txt('= OUTRA?', 70, 4), 380, 1040, back(ramp(f, va, va + 8)))
    cx = lerp(640, 540, smooth(ramp(f, ng - 20, ng + 10)))
    z = lerp(1.0, 1.12, smooth(ramp(f, ng - 20, ng + 10))) * (1 + .0004 * f)
    return c, (cx, 1250, z, 0), 'day'


def s4(f):
    c = BG('golden').copy()
    su = wt(4, 'sumiu') - 3
    put_b(c, 640, 1520, 440, f=f, seed=6, look=-.3, ghost=1 if f >= su else 0, expr='side' if f < su else 'sleep')
    if f >= su: put_dust(c, 640, 1400, 220, f - su, 18)
    num(c, 'SUL DA AUSTRÁLIA', 640, 700, f, wt(4, 'sul') - 3, 76, -3)
    num(c, 'EXTINTO', 640, 880, f, su, 140, 4)
    num(c, '~100 ANOS', 640, 1050, f, wt(4, 'seculo') - 3, 100, -3)
    z = lerp(1.0, 1.2, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, su)
    return c, (640, 1250 + k * 8, z, lerp(0, 2.5, smooth(ramp(f, su, su + 20))) + k), 'golden'


def s5(f):
    c = BG('dusk').copy()
    put_sci(c, 330, 1720, 780, f, 2, arms='point', skin=2, glasses=False, expr='grin', look=1)
    put_b(c, 880, 1600, 340, flip=True, f=f, seed=7, look=-.5)
    sp = wt(5, 'especies') - 3
    if f >= sp:
        for i in range(3):
            put_b(c, 720 + i * 170, 1080, 190 * back(ramp(f, sp + i * 3, sp + 8 + i * 3)), f=f, seed=10 + i)
        num(c, 'QUANTAS?', 880, 800, f, sp, 90, 4)
    pr = wt(5, 'protecao') - 3
    if f >= pr:
        s = back(ramp(f, pr, pr + 8))
        put_img(c, 'shield', 880, 1260, 360 * s, 400 / 460)
        num(c, 'PROTEÇÃO', 640, 640, f, pr, 120)
    k = kick(f, pr)
    return c, (lerp(620, 680, smooth(ramp(f, 0, 150))), 1260 + k * 8, lerp(1.05, 1.15, smooth(ramp(f, 0, 150))), k), 'dusk'


def s6(f):
    c = museum_bg().copy()
    no = wt(6, 'nome') - 3
    de = wt(6, 'desaparecer') - 3
    op = 1 - smooth(ramp(f, de, de + 10))
    put_img(c, 'cabinet', 640, 1720, 1000, 700 / 900, op=op)
    if f < de + 2:
        put_b(c, 640, 1140, 300, f=f, seed=8, ghost=1, expr='sleep')
    else:
        put_dust(c, 640, 1060, 200, f - de - 2, 18)
    if f >= no:
        paste_c(c, tag().resize((420, 162)), 640, 600, back(ramp(f, no, no + 8)))
        paste_c(c, txt('ISOODON MICROTIS', 44, 0), 660, 600, back(ramp(f, no, no + 8)))
    num(c, 'TARDE DEMAIS', 640, 820, f, de, 100, -4)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, de + 8)
    return c, (640, 1200 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60))) + k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'gavetas') - 3, 180, .8)
    s.ting(s.W(0, 'dois') - 3, .3)
    s.patter(s.cut(1), s.W(1, 'bolsa') - 3)
    s.ting(s.W(1, 'bolsa') - 3, .3)
    s.thunk(s.W(2, 'cranios') - 3, 200, .5)
    s.ting(s.W(2, 'dna') - 3, .25)
    s.thunk(s.W(3, 'duas') - 3, 200, .5)
    s.ting(s.W(3, 'guine') - 3, .25)
    s.thunk(s.W(4, 'sumiu') - 3, 120, .8)
    s.ting(s.W(5, 'protecao') - 3, .35)
    s.thunk(s.W(6, 'desaparecer') + 5, 140, .9)
