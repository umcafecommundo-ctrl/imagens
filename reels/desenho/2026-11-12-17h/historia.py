"""Um Café com o Mundo — CURIOSIDADE 12/11/2026 17h.
Fatos: estudo publicado na revista Science em 12/11/2026 (Live Science, Haaretz, 12/11/2026):
sítio 'Uruq Aljelibah, no Rub al-Khali (Quarteirão Vazio), sul da Arábia Saudita; antigo lago de água doce de ~340 km2
e até 29 m de profundidade, ~125 mil anos; mais de 5.500 artefatos de pedra + fibras, resinas e madeira; pontas com
danos de impacto de caça a animais grandes e restos de tecido animal; resíduos químicos ligados à árvore de veneno de
flecha Acokanthera schimperi (usada historicamente por caçadores africanos); fósseis de hipopótamos, búfalos,
avestruzes, camelos, gazelas e órix; possivelmente a evidência mais antiga de armas envenenadas (anterior: pontas de
~60 mil anos na África do Sul). Ressalva (Jeffrey Rose): artefatos coletados na superfície, a data é do lago (idade
máxima das pedras); ainda não se sabe como o veneno era preparado. Autor principal: Chris Clarkson (Max Planck / Griffith)."""
from kit import *
import kit
from PIL import ImageDraw

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Cento e vinte e cinco mil anos atrás, alguém já caçava com armas envenenadas.",
    "As pistas apareceram no Quarteirão Vazio, um enorme deserto de areia na Arábia Saudita.",
    "Só que, naquela época, ali existia um lago enorme, cheio de hipopótamos, búfalos e avestruzes.",
    "Os cientistas acharam mais de cinco mil e quinhentas peças de pedra, e algumas pontas tinham marcas de caça a bichos grandes.",
    "Nas pontas, havia restos químicos de uma árvore venenosa, usada por caçadores africanos nas flechas.",
    "Por que isso importa? Pode ser a prova mais antiga de armas com veneno. A anterior, no sul da África, tinha uns sessenta mil anos.",
    "Agora, falta descobrir como esse veneno era preparado, e a idade exata das pedras.",
]
CAPTXT = [
    "125 mil anos atrás, alguém já caçava com armas envenenadas.",
    "As pistas apareceram no Quarteirão Vazio,|um enorme deserto de areia na Arábia Saudita.",
    "Só que, naquela época, ali existia um lago enorme,|cheio de hipopótamos, búfalos e avestruzes.",
    "Os cientistas acharam mais de 5.500 peças de pedra,|e algumas pontas tinham marcas de caça a bichos grandes.",
    "Nas pontas, havia restos químicos de uma árvore venenosa,|usada por caçadores africanos nas flechas.",
    "Por que isso importa? Pode ser a prova mais antiga de armas com veneno.|A anterior, no sul da África, tinha uns 60 mil anos.",
    "Agora, falta descobrir como esse veneno era preparado,|e a idade exata das pedras.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'envenenadas', 4), (1, 'Arabia', 4), (2, 'hipopotamos', 4), (2, 'avestruzes', 6), (3, 'quinhentas', 4),
         (4, 'venenosa', 4), (5, 'sessenta', 6), (6, 'pedras', 4)]

STONE = hexc('#c9b08a'); STONED = hexc('#9c8462'); POIS = hexc('#6fbf3a'); POISD = hexc('#3f8a22')
WOOD = hexc('#8a5a3a')


# ------------------------------------------------------------------ objetos e bichos
@lru_cache(maxsize=4)
def ponta(veneno=0):
    """ponta de pedra lascada presa numa haste (aponta p/ cima). 300x900."""
    p = Pen(300, 900)
    p.line([(150, 330), (150, 880)], WOOD, 22, 5)
    for y in (330, 360, 390): p.stroke([(130, y), (170, y + 14)], 6, hexc('#5e3c24'))
    pts = [(150, 20), (205, 140), (215, 250), (185, 340), (115, 340), (85, 250), (95, 140)]
    p.shape(pts, STONE, STONED, 6, 14)
    for a, b in (((150, 60), (120, 200)), ((150, 60), (185, 210)), ((110, 250), (150, 320)), ((190, 250), (150, 320))):
        p.stroke([a, b], 4, STONED)
    if veneno:
        p.shape([(150, 22), (190, 115), (200, 170), (150, 150), (102, 170), (110, 115)], POIS, POISD, 5, 6)
    return p.img


def gota(c, x, y, s=1.0):
    d = ImageDraw.Draw(c)
    r = 16 * s
    d.polygon([(x, y - 2.2 * r), (x - r, y), (x + r, y)], fill=POIS)
    d.ellipse([x - r, y - r, x + r, y + r], fill=POIS, outline=INK, width=4)


@lru_cache(maxsize=4)
def pedrinha(k=0):
    p = Pen(200, 140)
    rnd = random.Random(k)
    pts = [(100 + math.cos(a) * (80 + rnd.random() * 15), 75 + math.sin(a) * (45 + rnd.random() * 12)) for a in [i * math.pi / 5 for i in range(10)]]
    p.shape(pts, mul(STONE, .9 + .2 * rnd.random()), STONED, 5, 6)
    p.stroke([(70, 60), (120, 90)], 4, STONED)
    return p.img


def hippo(blink=0, mouth=0.0, buf=0, look=.3, bob=0.0):
    """hipopótamo (ou búfalo se buf=1) de lado olhando p/ direita. 700x500, pés y~485."""
    p = Pen(700, 500)
    if buf:
        col, dk = hexc('#5a4a44'), hexc('#3e322e')
    else:
        col, dk = hexc('#8e86a8'), hexc('#6a6384')
    by = 300 + bob * 8
    for x in (190, 260, 430, 500):
        p.shape([(x - 28, by + 60), (x + 28, by + 60), (x + 26, 485), (x - 26, 485)], mul(col, .9 if x in (260, 500) else .8), None, 5)
    p.stroke([(110, by - 10), (70, by + 60)], 7, dk)
    p.shape(ell_pts(330, by, 240, 135, 60, 0, .1), col, dk, 6, 22)
    if buf:
        p.shape(ell_pts(450, by - 100, 90, 60, 30), col, dk, 5, 8)
    hx, hy = 560, by - 30 - mouth * 20
    if buf:
        p.shape(ell_pts(hx + 20, hy + 20, 85, 70, 40), col, dk, 6, 12)
        for s in (-1, 1):
            p.line(curve((hx - 10, hy - 40), (hx - 30 + s * 0, hy - 110), (hx + 40 + s * 20, hy - 120), 8), hexc('#e8dcc0'), 14, 4)
        ex, ey = hx + 20, hy - 5
    else:
        p.shape([(hx - 70, hy - 70), (hx + 60, hy - 60), (hx + 120, hy - 10), (hx + 125, hy + 60 + mouth * 30), (hx + 40, hy + 85), (hx - 70, hy + 60)], col, dk, 6, 12)
        if mouth > .1:
            p.shape([(hx + 20, hy + 40), (hx + 125, hy + 45), (hx + 120, hy + 50 + mouth * 60), (hx + 20, hy + 70)], hexc('#e58aa0'), None, 4)
            p.poly([(hx + 95, hy + 45), (hx + 108, hy + 45), (hx + 102, hy + 70)], (255, 255, 255), 3)
        p.dot(hx + 100, hy - 25, 7, INK)
        p.dot(hx - 40, hy - 78, 18, mul(col, 1.05), 4)
        ex, ey = hx + 5, hy - 50
    er = 20
    p.dot(ex, ey, er, (255, 255, 255), 4)
    if blink < .6:
        p.dot(ex + look * 8, ey + 1, 8, INK); p.dot(ex + look * 8 - 2, ey - 2, 3, (255, 255, 255))
    else:
        p.stroke([(ex - er, ey), (ex + er, ey)], 5)
    return p.img


def put_hippo(c, x, feet, h, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    put_sprite(c, 'hippo', x, feet, h, 1.4, flip, {'mouth': 4, 'bob': 6}, **kw)


@lru_cache(maxsize=2)
def arvore_veneno():
    """arbusto de folhas escuras com frutinhas roxas (árvore do veneno de flecha). 700x800, base y~790."""
    p = Pen(700, 800)
    p.shape([(320, 450), (380, 450), (395, 790), (305, 790)], WOOD, hexc('#5e3c24'), 6, 8)
    p.line([(350, 520), (230, 400)], WOOD, 22, 5); p.line([(350, 500), (480, 380)], WOOD, 22, 5)
    rnd = random.Random(3)
    for cx, cy, r in ((350, 260, 210), (190, 340, 150), (510, 330, 160), (350, 400, 170)):
        p.shape(ell_pts(cx, cy, r, r * .8, 40), hexc('#2f6b3a'), hexc('#1f4a28'), 6, 14)
    for i in range(26):
        x = 160 + rnd.random() * 380; y = 160 + rnd.random() * 300
        p.dot(x, y, 15, hexc('#5a2a6a'), 4); p.dot(x - 4, y - 4, 4, hexc('#b27ac2'))
    return p.img


@lru_cache(maxsize=4)
def lago_bg(light='day'):
    c = CEN('deserto', light).copy()
    d = ImageDraw.Draw(c)
    water = hexc('#4aa3d6') if light == 'day' else mul(hexc('#4aa3d6'), .8)
    d.ellipse([-300, 1230, 1540, 1720], fill=water, outline=INK, width=6)
    rnd = random.Random(5)
    for i in range(30):
        x = rnd.random() * 1242; y = 1300 + rnd.random() * 350
        d.line([(x, y), (x + 50, y)], fill=mul(water, 1.2), width=5)
    for i in range(40):
        x = rnd.random() * 1242; y = 1700 + rnd.random() * 400
        d.line([(x, y), (x + (rnd.random() - .5) * 20, y - 60 - rnd.random() * 60)], fill=hexc('#6a9a3a'), width=6)
    for tx in (90, 1160):
        d.line([(tx, 1500), (tx + 20, 1050)], fill=hexc('#7a5530'), width=26)
        for a in range(-150, -20, 26):
            r = math.radians(a)
            d.line([(tx + 20, 1050), (tx + 20 + 200 * math.cos(r), 1050 + 200 * math.sin(r) + 60)], fill=hexc('#3f8a3a'), width=22)
    return c


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def pimg(c, im, x, y, w, s=1.0, rot=0):
    if s <= .02: return
    ii = im.resize((max(2, int(w * s)), max(2, int(w * s * im.size[1] / im.size[0]))))
    if rot: ii = ii.rotate(rot, expand=True, resample=Image.BICUBIC)
    c.alpha_composite(ii, (int(x - ii.size[0] / 2), int(y - ii.size[1] / 2)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('deserto', 'golden').copy()
    e0 = wt(0, 'envenenadas') - 3
    pimg(c, ponta(1 if f >= e0 else 0), 640, 1150, 300, 1, 6 * math.sin(f * .05))
    if f >= e0:
        for i in range(2):
            t = ((f - e0) * .04 + i * .5) % 1
            gota(c, 640 + 20, 900 + t * 300, 1.0)
        num(c, 'VENENO!', 640, 1450, f, e0, 120, 5)
    num(c, '125.000 ANOS', 640, 640, f, wt(0, 'cento') - 3, 105, -4)
    z = lerp(1.5, 1.1, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, e0)
    return c, (640, 1150 + k * 10, z, k), 'golden'


def s1(f):
    c = CEN('deserto', 'day').copy()
    num(c, 'QUARTEIRÃO VAZIO', 640, 600, f, wt(1, 'Quarteirao') - 3, 78, -3)
    num(c, 'ARÁBIA SAUDITA', 640, 760, f, wt(1, 'Arabia') - 3, 78, 3)
    # camelo? não: só um avestruz curioso nas dunas
    put_emu(c, 900, 1560, 520, True, look=-.4, blink=blinkAt(f, 2), peck=max(0, math.sin(f * .08)) ** 4)
    t = smooth(ramp(f, 0, 70))
    return c, (640 + 30 * math.sin(f * .02), lerp(900, 1250, t), lerp(1.25, 1.08, t) * (1 + .0006 * f), 0), 'day'


def s2(f):
    c = lago_bg('day').copy()
    l0 = wt(2, 'lago') - 3
    h0 = wt(2, 'hipopotamos') - 3
    b0 = wt(2, 'bufalos') - 3
    a0 = wt(2, 'avestruzes') - 3
    num(c, 'LAGO DE 340 KM²', 640, 700, f, l0, 80, -3)
    if f >= h0:
        s = back(ramp(f, h0, h0 + 8))
        put_hippo(c, 420, 1560 + (1 - s) * 200, 420, False, mouth=max(0, math.sin((f - h0) * .1)), blink=blinkAt(f, 4), bob=math.sin(f * .1))
        put_hippo(c, 860, 1500 + (1 - s) * 200, 300, True, blink=blinkAt(f, 6), bob=math.sin(f * .1 + 1))
    if f >= b0:
        s = back(ramp(f, b0, b0 + 8))
        if s > .05: put_hippo(c, 300, 1900, 420 * s, False, buf=1, blink=blinkAt(f, 8), look=.6)
    if f >= a0:
        s = back(ramp(f, a0, a0 + 8))
        if s > .05: put_emu(c, 1020, 1960, 620 * s, True, look=-.3, blink=blinkAt(f, 9), run=0)
    t = smooth(ramp(f, 0, 90))
    return c, (640, lerp(1350, 1450, t), lerp(1.2, 1.02, t), 0), 'day'


def s3(f):
    c = CEN('deserto', 'day').copy()
    q0 = wt(3, 'cinco') - 3
    put_sci(c, 330, 1700, 900, f, 2, arms='point' if f >= wt(3, 'pontas') - 3 else 'clip', glasses=True, skin=2, look=1,
            expr='shock' if f >= wt(3, 'grandes') - 3 else 'neutral')
    if f >= q0:
        for i in range(14):
            s = back(ramp(f, q0 + i * 2, q0 + i * 2 + 8))
            x = 700 + (i % 5) * 110 + (i // 5) * 40; y = 1660 - (i // 5) * 60
            pimg(c, pedrinha(i), x, y, 130, s)
        num(c, '5.500+ PEDRAS', 760, 620, f, q0, 76, -4)
    p0 = wt(3, 'pontas') - 3
    if f >= p0:
        pimg(c, ponta(0), 900, 1000, 200, back(ramp(f, p0, p0 + 8)), -20)
        num(c, 'CAÇA GRANDE', 800, 780, f, wt(3, 'grandes') - 3, 70, 4)
    z = lerp(1.1, 1.2, smooth(f / 150))
    return c, (680, 1250, z, 0), 'day'


def s4(f):
    c = CEN('deserto', 'day').copy()
    a0 = wt(4, 'arvore') - 4
    if f >= a0:
        s = back(ramp(f, a0, a0 + 10))
        im = arvore_veneno(); w = int(700 * s)
        if w > 4:
            ii = im.resize((w, int(w * 800 / 700))); c.alpha_composite(ii, (int(380 - w / 2), int(1700 - ii.size[1])))
    v0 = wt(4, 'quimicos') - 3
    pimg(c, ponta(1 if f >= v0 else 0), 900, 1150, 240, 1, -8 + 4 * math.sin(f * .06))
    if f >= v0:
        gota(c, 640, 1000 + ((f - v0) * 6) % 220, 1.2)
        num(c, 'VENENO NA PONTA', 640, 640, f, v0, 74, 4)
    num(c, 'ÁRVORE VENENOSA', 640, 800, f, wt(4, 'venenosa') - 3, 74, -4)
    t = smooth(ramp(f, 0, 80))
    k = kick(f, v0, .6)
    return c, (lerp(600, 680, t), 1250 + k * 8, 1.1 + .0006 * f, k), 'day'


def s5(f):
    c = CEN('museu', 'dusk').copy()
    a0 = wt(5, 'antiga') - 3
    s0_ = wt(5, 'sessenta') - 3
    pimg(c, ponta(1), 820, 1180, 230, back(ramp(f, 0, 10)), 4 * math.sin(f * .05))
    num(c, 'A MAIS ANTIGA?', 640, 600, f, a0, 84, -3)
    num(c, '125 MIL ANOS', 820, 800, f, a0 + 4, 56, 3)
    if f >= s0_:
        pimg(c, ponta(1), 440, 1250, 170, back(ramp(f, s0_, s0_ + 8)), -4)
        num(c, '60 MIL ANOS', 440, 920, f, s0_, 56, -3)
        num(c, 'SUL DA ÁFRICA', 440, 1010, f, wt(5, 'Africa') - 3, 46, 0)
    z = lerp(1.2, 1.05, smooth(ramp(f, 0, 60))) * (1 + .0004 * f)
    return c, (640, 1150, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


def s6(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    put_sci(c, 380, 1700, 950, f, 2, arms='clip', glasses=True, skin=2, look=1, expr='neutral')
    pimg(c, ponta(1), 880, 1150, 220, 1, 10 * math.sin(f * .04))
    num(c, 'COMO ERA FEITO?', 700, 640, f, wt(6, 'preparado') - 3, 72, -4)
    num(c, 'QUAL A IDADE?', 700, 800, f, wt(6, 'idade') - 3, 72, 4)
    z = lerp(1.05, 1.22, smooth(f / 120))
    return c, (680, 1200, z, -.01 * f), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'cento') - 3, 140, 1.0)
    s.ting(s.W(0, 'envenenadas') - 3, .35)
    s.thunk(s.W(1, 'Quarteirao') - 3, 220, .5)
    s.thunk(s.W(1, 'Arabia') - 3, 220, .5)
    s.splash(s.W(2, 'hipopotamos') - 3, .5)
    s.thunk(s.W(2, 'bufalos') - 3, 160, .5)
    s.trill(s.W(2, 'avestruzes') - 3, .25)
    for i in range(5): s.thunk(s.W(3, 'cinco') - 3 + i * 5, 260, .35)
    s.ting(s.W(4, 'quimicos') - 3, .3)
    s.thunk(s.W(5, 'sessenta') - 3, 160, .7)
    s.ting(s.W(6, 'idade') - 3, .25)
