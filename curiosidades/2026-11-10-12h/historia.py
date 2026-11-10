"""Formato DESENHO: a coruja não mexe os olhos e gira a cabeça (Curiosidades da IA, 10/11/2026, 12h). Categoria: ANIMAIS.
Fatos: National Geographic ("How Owls Twist Their Heads Almost 360 Degrees"): os olhos da coruja ficam presos nas órbitas e
não giram, por isso ela vira a cabeça, no máximo 270 graus. EurekAlert/Johns Hopkins Medicine (estudo publicado na Science,
2013): 14 vértebras no pescoço; giro de até 270 graus para cada lado; reservatórios de sangue que se expandem perto da base do
crânio guardam sangue para o cérebro e os olhos enquanto ela gira. Humanos têm 7 vértebras no pescoço."""
from kit import *
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coruja import coruja

LINES = [
    "A coruja não consegue mexer os olhos.",
    "Eles são tão grandes que ficam presos no crânio, como dois faróis.",
    "Então, pra olhar pro lado, ela gira a cabeça inteira. Até duzentos e setenta graus!",
    "Cientistas nos Estados Unidos quiseram entender como ela faz isso sem passar mal.",
    "Você vê, a coruja tem catorze vértebras no pescoço. O dobro das nossas.",
    "E guarda um estoque de sangue perto da cabeça, pro cérebro não ficar sem nada enquanto gira.",
    "Ou seja: ela não revira os olhos... revira a cabeça inteira.",
]
CAPTXT = [
    "A coruja não consegue mexer os olhos.",
    "Eles são tão grandes que ficam presos no crânio,|como dois faróis.",
    "Então, pra olhar pro lado, ela gira a cabeça inteira.|Até 270 graus!",
    "Cientistas nos Estados Unidos quiseram entender|como ela faz isso sem passar mal.",
    "Você vê, a coruja tem 14 vértebras no pescoço.|O dobro das nossas.",
    "E guarda um estoque de sangue perto da cabeça,|pro cérebro não ficar sem nada enquanto gira.",
    "Ou seja: ela não revira os olhos...|revira a cabeça inteira.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = []
CHECK = [(0, 'olhos', 4), (1, 'farois', 6), (2, 'gira', 4), (2, 'setenta', 6), (3, 'cientistas', 4), (4, 'catorze', 6),
         (4, 'dobro', 6), (5, 'sangue', 6), (6, 'cabeca', 8)]

# cenários: s0 floresta à noite (coruja no galho) | s1 floresta à noite (close: olhos = faróis) | s2 floresta à noite (gira a
# cabeça, 270°) | s3 laboratório (cientistas e coruja no poleiro) | s4 laboratório (raio-X: 14 vértebras x 7) |
# s5 dentro do corpo (vaso com estoque de sangue inchando) | s6 floresta à noite (coruja revira a cabeça, fim)


def put_owl(c, x, feet, h, f, seed=1, ang=0, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    put_sprite(c, 'coruja', x, feet + .006 * h * math.sin((f + seed * 9) * .1), h, .75, False, None, ang=int(round(ang / 5) * 5), **kw)


@lru_cache(maxsize=4)
def galho_img(w=1242):
    p = Pen(1242, 160)
    p.shape([(-20, 50), (1262, 30), (1262, 110), (-20, 130)], hexc('#6b4a2e'), hexc('#4f3520'), 6, 14)
    for x in (300, 820):
        p.shape([(x, 50), (x + 60, -10), (x + 90, 5), (x + 40, 50)], hexc('#6b4a2e'), None, 5, 0)
    return p.img


def galho(c, y):
    c.alpha_composite(galho_img(), (0, int(y)))


@lru_cache(maxsize=4)
def feixe_img():
    im = Image.new('RGBA', (900, 700), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.polygon([(0, 330), (900, 0), (900, 700), (0, 370)], fill=(255, 240, 160, 90))
    return im


@lru_cache(maxsize=4)
def vertebras_img(n, w=220, col='#f1ead8'):
    hh = 70
    p = Pen(w, n * hh + 20)
    for i in range(n):
        y = 10 + i * hh
        p.shape([(30, y), (w - 30, y), (w - 20, y + hh - 14), (20, y + hh - 14)], hexc(col), mul(hexc(col), .82), 5, 6)
    return p.img


def SFX(s):
    s.ting(s.W(0, 'olhos'), .3)
    s.thunk(s.W(1, 'presos') - 2, 220, .5); s.ting(s.W(1, 'farois'), .35)
    s.whoosh(s.W(2, 'gira') - 4, .6, .5); s.thunk(s.W(2, 'setenta') - 2, 160, .7)
    for i in range(2): s.thunk(s.W(3, 'cientistas') - 3 + i * 5)
    for i in range(4): s.thunk(s.W(4, 'catorze') - 2 + i * 3, 260, .35)
    s.ting(s.W(4, 'dobro'), .3)
    s.splash(s.W(5, 'sangue') - 2, .3)
    s.whoosh(s.W(6, 'revira', 1) - 6, .5, .5); s.trill(s.W(6, 'cabeca') + 2, 1.0, .3)


def s0(f):
    c = CEN('floresta', 'dusk').copy()
    galho(c, 1380)
    o = wt(0, 'olhos') - 3
    put_owl(c, 621, 1450, 900, f, 1, look=.6 * math.sin(f * .08) if f < o else 0)
    if f >= o: paste_c(c, txt('TRAVADOS!', 100, -6), 621, 700, back(ramp(f, o, o + 8)))
    z = lerp(1.35, 1.05, easeOut(ramp(f, 2, 40))) * (1 + .0009 * f)
    return c, (621, 1150, z, 0), 'dusk'


def s1(f):
    c = CEN('floresta', 'dusk').copy()
    galho(c, 1580)
    fa = wt(1, 'farois') - 3
    if f >= fa:
        a = clamp((f - fa) / 6)
        fx = feixe_img().copy()
        fx.putalpha(fx.getchannel('A').point(lambda v: int(v * a)))
        c.alpha_composite(fx, (700, 650))
    put_owl(c, 621, 1650, 1300, f, 2)
    pr = wt(1, 'presos') - 3
    if pr <= f < fa: paste_c(c, txt('PRESOS!', 100, 6), 621, 440, back(ramp(f, pr, pr + 8)))
    if f >= fa: paste_c(c, txt('FARÓIS!', 100, -6), 621, 440, back(ramp(f, fa, fa + 8)))
    z = lerp(1.1, 1.3, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (621, 1050, z, 0), 'dusk'


def s2(f):
    c = CEN('floresta', 'dusk').copy()
    galho(c, 1380)
    g = wt(2, 'gira') - 3
    st = wt(2, 'setenta') - 3
    ang = 270 * smooth(ramp(f, g, st + 4))
    if f >= g:
        d = ImageDraw.Draw(c)
        d.arc((621 - 300, 840 - 300, 621 + 300, 840 + 300), -90, -90 + ang, fill=(255, 220, 90, 255), width=18)
    put_owl(c, 621, 1450, 900, f, 3, ang=ang)
    if f >= st: paste_c(c, txt('270°', 140, -6), 900, 480, back(ramp(f, st, st + 8)))
    k = kick(f, st, .6)
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1100 + k * 10, z, k), 'dusk'


@lru_cache(maxsize=2)
def poleiro_img():
    p = Pen(300, 700)
    p.shape([(135, 60), (165, 60), (165, 660), (135, 660)], hexc('#8a6a4a'), None, 5, 0)
    p.shape([(0, 30), (300, 30), (300, 70), (0, 70)], hexc('#8a6a4a'), hexc('#6b4f35'), 5, 0)
    p.shape([(60, 650), (240, 650), (260, 690), (40, 690)], hexc('#6b4f35'), None, 5, 0)
    return p.img


def s3(f):
    c = CEN('lab', 'day').copy(); c.alpha_composite(P.lamp_glow(1))
    c.alpha_composite(poleiro_img(), (470, 1010))
    put_owl(c, 621, 1060, 560, f, 4, ang=40 * math.sin(f * .06), look=0)
    k = wt(3, 'cientistas') - 3
    for i, (x, sd, kw) in enumerate(((230, 1, dict(arms='clip', hair='#9a9a9a', skin=3, expr='neutral')),
                                     (1010, 2, dict(arms='cheek', bun=True, expr='nervous')))):
        s = back(ramp(f, k + i * 5, k + i * 5 + 9))
        put_sci(c, x, 1720, 820 * s, f, sd, look=1 if i == 0 else -1, **kw)
        put_dust(c, x, 1700, 90, f - k - i * 5)
    m = wt(3, 'mal') - 3
    if f >= m: paste_c(c, txt('COMO?!', 100, 6), 621, 520, back(ramp(f, m, m + 8)))
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1250, z, 0), 'day'


def s4(f):
    c = CEN('lab', 'dusk').copy()
    # quadro de raio-X
    d = ImageDraw.Draw(c)
    d.rounded_rectangle((120, 500, 1122, 1560), 30, fill=(22, 34, 58, 255), outline=INK + (255,), width=8)
    k14 = wt(4, 'catorze') - 3
    db = wt(4, 'dobro') - 3
    n = int(clamp((f - k14 + 14) / 14) * 14) if f >= k14 - 14 else 0
    if n:
        v = vertebras_img(14, 200).resize((156, 780))
        v = v.crop((0, 0, 156, int(8 + n * 54.6)))
        c.alpha_composite(v, (300, 560))
        paste_c(c, txt('CORUJA: %d' % n, 70, 0), 380, 1500, 1)
    if f >= db:
        v7 = vertebras_img(7, 200, '#d9c9b0')
        c.alpha_composite(v7.resize((156, 780 * 7 * 70 // (14 * 70 + 20) + 8)), (800, 560 + 390))
        paste_c(c, txt('NÓS: 7', 70, 0), 860, 1500, back(ramp(f, db, db + 8)))
        paste_c(c, txt('O DOBRO!', 110, -6), 621, 400, back(ramp(f, db, db + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1050, z, 0), 'dusk'


def s5(f):
    c = CEN('corpo', 'dusk').copy()
    sg = wt(5, 'sangue') - 3
    inch = easeOut(ramp(f, sg, sg + 20))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle((540, 200, 700, 2000), 70, fill=(196, 40, 52, 255), outline=INK + (255,), width=8)
    r = 90 + 130 * inch + 6 * math.sin(f * .2) * inch
    d.ellipse((620 - r, 900 - r * 1.2, 620 + r, 900 + r * 1.2), fill=(214, 52, 64, 255), outline=INK + (255,), width=8)
    d.ellipse((620 - r * .5, 900 - r * .9, 620 - r * .2, 900 - r * .5), fill=(240, 120, 128, 255))
    for i in range(6):
        y = (f * 9 + i * 300) % 1800 + 200
        d.ellipse((600, y, 640, y + 26), fill=(240, 100, 110, 255), outline=INK + (255,), width=3)
    if f >= sg: paste_c(c, txt('ESTOQUE', 90, -4), 621, 360, back(ramp(f, sg, sg + 8))); paste_c(c, txt('DE SANGUE', 90, -4), 621, 470, back(ramp(f, sg, sg + 8)))
    ce = wt(5, 'cerebro') - 3
    if f >= ce: paste_c(c, txt('PRO CÉREBRO!', 90, 4), 621, 1300, back(ramp(f, ce, ce + 8)))
    z = lerp(1.1, 1.2, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 950, z, lerp(0, 2, smooth(ramp(f, 0, 90)))), 'dusk'


def s6(f):
    c = CEN('floresta', 'dusk').copy()
    galho(c, 1480)
    r = wt(6, 'revira', 1) - 3
    ang = 270 * smooth(ramp(f, r, r + 16))
    put_owl(c, 621, 1550, 1050, f, 5, ang=ang, expr='smug' if f >= r + 16 else 'calm')
    ol = wt(6, 'olhos') - 3
    if ol <= f < r: paste_c(c, txt('OLHOS? NÃO.', 90, 5), 621, 640, back(ramp(f, ol, ol + 8)))
    if r <= f < r + 55: paste_c(c, txt('CABEÇA!', 120, -6), 621, 640, back(ramp(f, r, r + 8)))
    z = lerp(1.05, 1.25, easeOut(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1150, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
