"""Formato DESENHO: no cavalo-marinho quem fica grávido é o pai (Curiosidades da IA, 18/11/2026, 07h).
Categoria: ANIMAIS.
Fatos: National Geographic, "Seahorse Fathers Take Reins in Childbirth" (2002): o macho tem uma bolsa na barriga;
a fêmea deposita os ovos na bolsa dele; a gestação dura de 10 a 25 dias conforme a espécie; o macho solta os filhotes
com contrações musculares; até 2.000 filhotes de uma vez. Science News ("How male seahorses tap into their mothering side").
Cenários: s0 fundo do mar (Professor aponta o pai barrigudo) | s1 fundo do mar (mãe põe os ovos na bolsinha dele) |
s2 fundo do mar, luz dourada = tempo passando (a barriga cresce, 25 dias) | s3 fundo do mar ao entardecer (parto: filhotes) |
s4 fundo do mar ao entardecer (Professor entrega o presente de Dia das Mães ao pai)."""
from kit import *
from functools import lru_cache

LINES = [
    "No cavalo-marinho, quem fica grávido é o pai.",
    "A mãe coloca os ovos numa bolsinha na barriga dele.",
    "E ele carrega os filhotes por até vinte e cinco dias.",
    "Você vê, na hora do parto, a barriga se aperta e solta até dois mil filhotes de uma vez.",
    "Ou seja: no cavalo-marinho, o presente de Dia das Mães... vai pro pai.",
]
CAPTXT = [
    "No cavalo-marinho, quem fica grávido é o pai.",
    "A mãe coloca os ovos|numa bolsinha na barriga dele.",
    "E ele carrega os filhotes|por até 25 dias.",
    "Você vê, na hora do parto, a barriga se aperta|e solta até 2 mil filhotes de uma vez.",
    "Ou seja: no cavalo-marinho,|o presente de Dia das Mães... vai pro pai.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'gravido', 4), (0, 'pai', 6), (1, 'ovos', 6), (1, 'bolsinha', 4), (2, 'vinte', 6),
         (3, 'aperta', 4), (3, 'solta', 4), (3, 'mil', 6), (4, 'presente', 6), (4, 'pai', 8)]

GOLD = hexc('#f2a93b'); GOLDD = hexc('#c97a1f')
PINK = hexc('#ec7f9b'); PINKD = hexc('#c2566f')


def SFX(s):
    s.patter(0, 70, 6, .06)
    s.ting(s.W(0, 'gravido'), .3); s.thunk(s.W(0, 'pai') - 2, 160, .8)
    for i in range(6): s.thunk(s.W(1, 'ovos') - 2 + i * 3, 320, .35)
    s.ting(s.W(1, 'bolsinha'), .25)
    s.patter(s.W(2, 'carrega'), s.W(2, 'carrega') + 50, 8, .08)
    s.ting(s.W(2, 'vinte'), .3)
    s.thunk(s.W(3, 'aperta') - 2, 140, .8)
    s.splash(s.W(3, 'solta') - 2)
    s.patter(s.W(3, 'solta'), s.W(3, 'solta') + 40, 14, .12)
    s.thunk(s.W(4, 'presente') - 2, 260, .6); s.trill(s.W(4, 'pai'), 1.0, .3)


def cavalo(belly=0.0, mom=False, expr='calm', look=0.4, blink=0, fin=0.0, squeeze=0.0):
    """cavalo-marinho de lado olhando para a direita, 600x800 (cauda enrolada embaixo)."""
    col, dk = (PINK, PINKD) if mom else (GOLD, GOLDD)
    p = Pen(600, 800)
    # cauda enrolada
    pts = []
    for i in range(14):
        t = i / 13
        a = -0.4 + t * 4.2
        r = 120 * (1 - t * .75)
        pts.append((250 + r * math.cos(a) * .9 - 60 * (1 - t), 600 + r * math.sin(a) * .9 + 40 * (1 - t)))
    for i, (x, y) in enumerate(pts):
        p.shape(ell_pts(x, y, 44 - i * 2.4, 40 - i * 2.2, 22), col, dk, 5, 4)
    # nadadeira dorsal (nas costas, esquerda) que treme
    fw = 10 * math.sin(fin)
    p.shape([(200, 330), (120 + fw, 300), (110 - fw, 400), (130 + fw, 470), (205, 460)], hexc('#fde3a7') if not mom else hexc('#fbd0dc'), dk, 4, 4)
    # corpo
    p.shape(ell_pts(270, 410, 105, 170, 44, .12), col, dk, 6, 16)
    # barriga (bolsinha)
    bw = 55 + 75 * belly
    bh = 70 + 70 * belly
    if not mom:
        sq = 1 - .25 * squeeze
        p.shape(ell_pts(330 + bw * .35, 470, bw * sq, bh * sq, 40), mul(col, 1.12), dk, 6, 10)
        p.arc(330 + bw * .35, 470, bw * .6 * sq, bh * .6 * sq, -40, 60, 4, mul(dk, .9))
    # gomos do corpo
    for y in range(290, 560, 45):
        p.arc(250, y, 85, 14, 200, 330, 4, dk)
    # cabeça
    hx, hy = 330, 170
    p.shape(ell_pts(hx, hy, 92, 78, 40), col, dk, 6, 12)
    # focinho comprido (tubo)
    p.shape([(hx + 50, hy - 6), (hx + 210, hy + 8), (hx + 215, hy + 46), (hx + 50, hy + 56)], col, dk, 6, 6)
    p.shape(ell_pts(hx + 214, hy + 27, 14, 22, 16), mul(col, .9), dk, 5, 0)
    # coroa (espinhos)
    p.shape([(hx - 50, hy - 55), (hx - 30, hy - 120), (hx - 5, hy - 70), (hx + 10, hy - 130), (hx + 30, hy - 66), (hx + 40, hy - 50)], col, dk, 5, 4)
    # olho
    ex, ey, er = hx + 18, hy - 8, 34 if expr == 'shock' else 30
    if blink:
        p.arc(ex, ey, er * .8, 10, 20, 160, 6)
    else:
        p.dot(ex, ey, er, (255, 255, 255), 5)
        lk = max(-1, min(1, look))
        p.dot(ex + lk * (er - 13), ey + 2, 14 if expr != 'shock' else 10, INK)
        p.dot(ex + lk * (er - 13) - 4, ey - 3, 4.5, (255, 255, 255))
        if expr in ('smug', 'pained'):
            p.poly([(ex - er - 3, ey - er - 3), (ex + er + 3, ey - er - 3), (ex + er + 3, ey - 6), (ex - er - 3, ey - 6)], col)
            p.stroke([(ex - er, ey - 6), (ex + er, ey - 6)], 5)
    if mom:  # cílios
        for a in (-40, -10, 20):
            r = math.radians(a - 90)
            p.stroke([(ex + er * math.cos(r), ey + er * math.sin(r)), (ex + (er + 16) * math.cos(r), ey + (er + 16) * math.sin(r))], 4)
    # bochecha
    p.dot(hx - 10, hy + 40, 14, mul(col, 1.15))
    return p.img


def put_cavalo(c, x, feet, h, f, seed=0, flip=False, **kw):
    if h < 8: return
    kw.setdefault('blink', 1 if blinkAt(f, seed + 3) > .6 else 0)
    kw.setdefault('fin', (f * .5 + seed) % 6.28)
    put_sprite(c, 'cavalo', x, feet, h, 600 / 800, flip, {'belly': 8, 'fin': 3, 'squeeze': 4, 'look': 4}, **kw)


def bolhas(c, f, seed=1, n=10):
    d = ImageDraw.Draw(c); rnd = random.Random(seed)
    for i in range(n):
        x = rnd.randint(60, 1180); sp = rnd.uniform(3, 6); r = rnd.randint(8, 18)
        y = 1900 - ((f * sp + rnd.randint(0, 1800)) % 1800)
        d.ellipse((x - r, y - r, x + r, y + r), outline=(220, 245, 255, 200), width=4)


@lru_cache(maxsize=1)
def presente():
    p = Pen(300, 300)
    p.shape([(40, 120), (260, 120), (260, 280), (40, 280)], hexc('#e4473b'), hexc('#b02f26'), 6, 10)
    p.shape([(25, 85), (275, 85), (275, 135), (25, 135)], hexc('#f0594c'), hexc('#b02f26'), 6, 6)
    p.shape([(130, 85), (170, 85), (170, 280), (130, 280)], hexc('#ffd24a'), hexc('#d9a520'), 4, 0)
    p.shape(ell_pts(110, 60, 45, 28, 24, .4), hexc('#ffd24a'), hexc('#d9a520'), 5, 4)
    p.shape(ell_pts(190, 60, 45, 28, 24, -.4), hexc('#ffd24a'), hexc('#d9a520'), 5, 4)
    return p.img


def s0(f):
    c = CEN('fundo_mar', 'day').copy()
    g = wt(0, 'gravido') - 3
    pa = wt(0, 'pai') - 3
    bl = back(ramp(f, g, g + 10)) if f >= g else 0
    put_cavalo(c, 860, 1450 + 18 * math.sin(f * .1), 820, f, belly=bl, expr='shock' if f >= pa else 'calm', look=-.6)
    put_prof(c, 330, 1880, 960, f, expr='grin' if f < g else 'shock', arms='point', look=1)
    bolhas(c, f, 2, 8)
    if f >= pa: paste_c(c, txt('O PAI?!', 120, -6), 760, 560, back(ramp(f, pa, pa + 8)))
    z = lerp(1.3, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1240 + kick(f, pa, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('fundo_mar', 'day').copy()
    o = wt(1, 'ovos') - 3
    b = wt(1, 'bolsinha') - 3
    bob = 15 * math.sin(f * .1)
    put_cavalo(c, 340, 1500 + bob, 800, f, 1, mom=True, look=.8)
    put_cavalo(c, 900, 1500 - bob, 800, f, 2, flip=True, belly=.15 + .25 * ramp(f, o, o + 40), look=.8,
               expr='shock' if f >= b else 'calm')
    d = ImageDraw.Draw(c)
    if f >= o:
        for i in range(10):
            t = clamp((f - o - i * 3) / 16)
            if 0 < t < 1:
                x = lerp(470, 770, t); y = lerp(1180, 1180, t) - 90 * math.sin(t * math.pi) + (i % 3) * 20
                d.ellipse((x - 16, y - 16, x + 16, y + 16), fill=(255, 170, 60, 255), outline=INK + (255,), width=4)
    if f >= b:
        paste_c(c, txt('BOLSINHA', 96, 5), 700, 620, back(ramp(f, b, b + 8)))
    bolhas(c, f, 3, 8)
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.15, 1.35, t) * (1 + .0009 * f)
    return c, (lerp(600, 700, t), 1150, z, 0), 'day'


def s2(f):
    c = CEN('fundo_mar', 'golden').copy()
    v = wt(2, 'vinte') - 3
    T = ramp(f, 4, v + 10)
    dia = 1 + int(24 * T)
    put_cavalo(c, 640, 1560 + 20 * math.sin(f * .08), 1000, f, 2, belly=.4 + .6 * T, expr='pained' if T > .6 else 'calm', look=.5)
    label = f'DIA {dia}' if f < v else '25 DIAS!'
    paste_c(c, txt(label, 110 if f < v else 130, -4), 640, 500, 1.0 if f < v else back(ramp(f, v, v + 8)))
    bolhas(c, f, 4, 10)
    t = smooth(ramp(f, 0, 100))
    z = lerp(1.05, 1.22, t) * (1 + .0009 * f)
    return c, (640, lerp(1100, 1180, t), z, math.sin(f * .05) * 1.5), 'golden'


def s3(f):
    c = CEN('fundo_mar', 'dusk').copy()
    a = wt(3, 'aperta') - 3
    s_ = wt(3, 'solta') - 3
    m = wt(3, 'mil') - 3
    sq = pulse(f, a, max(4, s_ - a - 4)) if f < s_ else 0
    belly = 1.0 if f < s_ else max(.2, 1 - (f - s_) / 25)
    put_cavalo(c, 470, 1600, 1000, f, 2, belly=belly, squeeze=sq, expr='pained' if sq > .3 else ('smug' if f >= s_ + 20 else 'calm'), look=.6)
    if f >= s_:
        rnd = random.Random(7)
        for i in range(36):
            t0 = s_ + i * .9
            age = f - t0
            if age < 0: continue
            ang = rnd.uniform(-1.2, 1.0); sp = rnd.uniform(14, 24)
            dist = sp * age * (1 - min(age, 60) / 140)
            x = 720 + dist * math.cos(ang); y = 1280 + dist * math.sin(ang) - age * 1.5
            if -80 < x < 1320 and -80 < y < 2300:
                put_cavalo(c, x, y, rnd.uniform(140, 200), f + i, i, look=rnd.uniform(-1, 1))
    if a <= f < s_: paste_c(c, txt('APERTA!', 100, -5), 700, 600, back(ramp(f, a, a + 8)))
    if f >= m: paste_c(c, txt('2.000!', 150, 6), 760, 560, back(ramp(f, m, m + 8)))
    t = easeOut(ramp(f, s_ - 6, s_ + 20))
    z = lerp(1.35, 1.05, t) * (1 + .0009 * f)
    return c, (lerp(560, 640, t), lerp(1150, 1150, t) + kick(f, s_, .8) * 12, z, lerp(2, 0, t)), 'dusk'


def s4(f):
    c = CEN('fundo_mar', 'dusk').copy()
    pr = wt(4, 'presente') - 3
    pa = wt(4, 'pai') - 3
    put_cavalo(c, 850, 1380 + 15 * math.sin(f * .1), 760, f, 2, flip=True, belly=.2,
               expr='shock' if pr <= f < pa else ('smug' if f >= pa else 'calm'), look=.8)
    rnd = random.Random(3)
    for i in range(7):
        put_cavalo(c, 560 + rnd.randint(0, 420), 1000 + rnd.randint(-120, 120) + 10 * math.sin(f * .15 + i), 110, f + i, i + 9, flip=True)
    put_prof(c, 340, 1880, 980, f, expr='grin' if f >= pa else 'smug', arms='point' if f >= pr else 'chin', look=1)
    if f >= pr:
        tx = lerp(520, 640, easeOut(ramp(f, pr, pa)))
        paste_c(c, presente(), tx, 1420, back(ramp(f, pr, pr + 8)) * .55)
    if f >= pa:
        paste_c(c, txt('FELIZ DIA', 92, -5), 640, 700, back(ramp(f, pa, pa + 8)))
        paste_c(c, txt('DAS MÃES, PAI!', 92, -5), 660, 820, back(ramp(f, pa + 3, pa + 11)))
    bolhas(c, f, 5, 8)
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (620, lerp(1250, 1200, t) + kick(f, pa, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
