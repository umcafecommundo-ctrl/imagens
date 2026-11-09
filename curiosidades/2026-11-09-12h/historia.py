"""Formato DESENHO: por que a gente soluça (Curiosidades da IA, 09/11/2026, 12h). Categoria: CORPO HUMANO.
Fatos: Smithsonian Magazine, "The Curious Case of Charles Osborne, Who Hiccuped for 68 Years Straight" (2024): o soluço é uma
contração involuntária do diafragma, o músculo entre o peito e a barriga; logo depois as cordas vocais se fecham de repente e
fazem o "hic"; gatilhos comuns: comer demais, bebida com gás, engolir ar; o recorde do Guinness é de um homem nos EUA que
soluçou por cerca de 68 anos (1922-1990).
UCL News (12/11/2019), "Newborn baby hiccups could be key to brain development": o soluço começa no útero por volta de
9 semanas de gestação; em 13 recém-nascidos, cada soluço provocou uma grande onda de atividade no cérebro, que pode ajudar o
bebê a aprender a controlar os músculos da respiração; segundo a pesquisadora, no adulto o soluço pode ser um reflexo que
sobrou da infância."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10b', '2026-11-08-10h'); _h12 = _load('h12p', '2026-11-08-12h')
pessoa = _h10.pessoa; cerebro = _h12.cerebro

LINES = [
    "O soluço é um músculo levando um susto dentro de você.",
    "Embaixo dos pulmões fica o diafragma, o músculo que puxa o ar pra dentro.",
    "Comer muito rápido ou tomar refrigerante pode irritar ele, e ele dá um puxão sem avisar.",
    "O ar entra correndo, as cordas vocais fecham de repente, e sai aquele barulhinho.",
    "Um homem nos Estados Unidos soluçou por sessenta e oito anos seguidos.",
    "Você vê, o bebê já soluça na barriga da mãe, e cientistas acham que cada soluço ensina o cérebro dele a controlar a respiração.",
    "Ou seja: no adulto, o soluço é um treino de bebê... que ninguém desligou.",
]
CAPTXT = [
    "O soluço é um músculo levando um susto dentro de você.",
    "Embaixo dos pulmões fica o diafragma,|o músculo que puxa o ar pra dentro.",
    "Comer muito rápido ou tomar refrigerante pode irritar ele,|e ele dá um puxão sem avisar.",
    "O ar entra correndo, as cordas vocais fecham de repente,|e sai aquele barulhinho.",
    "Um homem nos Estados Unidos soluçou por 68 anos seguidos.",
    "Você vê, o bebê já soluça na barriga da mãe,|e cientistas acham que cada soluço ensina o cérebro dele|a controlar a respiração.",
    "Ou seja: no adulto, o soluço é um treino de bebê...|que ninguém desligou.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [4]
CHECK = [(0, 'susto', 4), (1, 'diafragma', 4), (1, 'ar', 6), (2, 'refrigerante', 4), (2, 'puxao', 6), (3, 'fecham', 4),
         (3, 'barulhinho', 6), (4, 'anos', 4), (5, 'barriga', 4), (5, 'cerebro', 6), (6, 'bebe', 4), (6, 'desligou', 8)]

MUS, MUSD = hexc('#e8737e'), hexc('#c4525e')
PUL, PULD = hexc('#f7a9b4'), hexc('#de8796')


# ------------------------------------------------------------------ personagens e objetos novos
def diafragma(expr='calm', blink=0, pull=0.0, look=0.0):
    """diafragma = cúpula de músculo com carinha (800x420). pull 0..1 = puxão (achata e desce)."""
    p = Pen(800, 420)
    top = 90 + 90 * pull
    pts = [(60, 380)] + [(400 + 340 * math.cos(a), 380 - (380 - top) * math.sin(a)) for a in [i * math.pi / 30 for i in range(31)]][::-1][:-1] + [(740, 380)]
    pts = [(400 + 340 * math.cos(a), 380 - (380 - top) * math.sin(a)) for a in [math.pi - i * math.pi / 30 for i in range(31)]]
    inner = [(400 + 300 * math.cos(a), 400 - (380 - top - 40) * math.sin(a)) for a in [i * math.pi / 30 for i in range(31)]]
    p.shape(pts + inner, MUS, MUSD, 6, 14)
    for k in range(5):
        a = math.pi * (k + 1) / 6
        p.stroke([(400 + 330 * math.cos(a), 380 - (370 - top) * math.sin(a)), (400 + 305 * math.cos(a), 398 - (340 - top) * math.sin(a))], 4, MUSD)
    ey = top + 70
    for dx in (-70, 70):
        ex = 400 + dx
        if blink: p.stroke([(ex - 22, ey), (ex + 22, ey)], 6)
        else:
            r = 34 if expr == 'shock' else 28
            p.dot(ex, ey, r, (255, 255, 255), 5)
            p.dot(ex + look * 10, ey + 3, 12, INK)
    if expr == 'shock': p.dot(400, ey + 60, 18, INK)
    elif expr == 'smug': p.arc(400, ey + 48, 26, 12, 20, 160, 5)
    else: p.arc(400, ey + 44, 22, 10, 20, 160, 5)
    return p.img


def put_dia(c, x, y, w, f, seed=1, **kw):
    """y = base da cúpula."""
    if w < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    kw['pull'] = round(kw.get('pull', 0) * 6) / 6
    im = sprite('diafragma', tuple(sorted(kw.items())), int(w * 420 / 800), 800 / 420, False)
    put(c, im, x, y)


@lru_cache(maxsize=8)
def pulmoes_img(fill=0.0, w=700):
    p = Pen(800, 760)
    s = 1 + .12 * fill
    p.line([(400, 0), (400, 200)], hexc('#f0c7cc'), 60, 6)  # traqueia
    for k in range(5): p.stroke([(372, 30 + k * 36), (428, 30 + k * 36)], 4, hexc('#c9959c'))
    p.stroke([(400, 200), (300, 290)], 30, hexc('#f0c7cc')); p.stroke([(400, 200), (500, 290)], 30, hexc('#f0c7cc'))
    for sx in (-1, 1):
        pts = ell_pts(400 + sx * 185, 470, 165 * s, 270 * s, 48, sx * .12)
        p.shape(pts, PUL, PULD, 6, 18)
        for i in range(3):
            p.stroke([(400 + sx * 120, 330 + i * 30), (400 + sx * (200 + i * 20), 420 + i * 80)], 4, PULD)
    return p.img.resize((w, int(w * 760 / 800)), Image.LANCZOS)


@lru_cache(maxsize=4)
def copo_img(w=220):
    p = Pen(260, 400)
    p.stroke([(170, 10), (140, 200)], 14, hexc('#ff6f6f'))  # canudo
    p.shape([(30, 90), (230, 90), (205, 390), (55, 390)], hexc('#e8f4fb'), hexc('#cfe2ee'), 6, 6)
    p.shape([(40, 150), (220, 150), (203, 380), (57, 380)], hexc('#7a3f1d'), hexc('#5c2e14'), 0, 6)
    rnd = random.Random(2)
    for i in range(12): p.dot(rnd.randint(70, 190), rnd.randint(170, 370), rnd.choice((5, 7, 9)), hexc('#c98b5a'))
    return p.img.resize((w, int(w * 400 / 260)), Image.LANCZOS)


def cordas(closed=0.0, w=600):
    """garganta por dentro: tubo com as duas pregas (cordas vocais) que fecham. 600x800."""
    return _cordas(round(closed * 6) / 6, w)


@lru_cache(maxsize=16)
def _cordas(closed, w):
    p = Pen(600, 800)
    p.shape([(140, 0), (460, 0), (460, 800), (140, 800)], hexc('#f4b7bf'), hexc('#e09aa5'), 6, 18)
    gap = 120 * (1 - closed)
    p.shape([(150, 360), (300 - gap / 2, 470), (150, 520)], MUS, MUSD, 6, 6)
    p.shape([(450, 360), (300 + gap / 2, 470), (450, 520)], MUS, MUSD, 6, 6)
    return p.img.resize((w, int(w * 800 / 600)), Image.LANCZOS)


def bebe(blink=0, expr='calm', hic=0):
    """bebê sentado de frente (400x460), fralda branca."""
    p = Pen(400, 460)
    sk, skd = hexc('#f2c29b'), hexc('#d9a27a')
    p.shape(ell_pts(200, 350, 120, 100, 40), hexc('#fbfbf7'), hexc('#dcdcd2'), 6, 10)  # fralda/corpo
    for sx in (-1, 1): p.shape(ell_pts(200 + sx * 130, 300, 36, 50, 24, sx * .4), sk, skd, 5, 6)  # braços
    for sx in (-1, 1): p.shape(ell_pts(200 + sx * 70, 440, 50, 26, 24), sk, skd, 5, 4)  # pés
    p.shape(ell_pts(200, 160, 130, 125, 48), sk, skd, 6, 14)  # cabeça
    p.stroke([(190, 40), (205, 20), (220, 42)], 6)  # topete
    for dx in (-45, 45):
        if blink: p.stroke([(200 + dx - 14, 160), (200 + dx + 14, 160)], 5)
        else: p.dot(200 + dx, 160, 22 if hic else 18, (255, 255, 255), 4); p.dot(200 + dx, 163, 9, INK)
    if hic: p.dot(200, 220, 14, INK)
    else: p.arc(200, 210, 22, 12, 20, 160, 5)
    p.dot(140, 200, 14, hexc('#f4a3a3')); p.dot(260, 200, 14, hexc('#f4a3a3'))
    return p.img


def put_bebe(c, x, feet, h, f, seed=1, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('bebe', tuple(sorted(kw.items())), int(h), 400 / 460, False)
    put(c, im, x, feet - (16 if kw.get('hic') else 0))


@lru_cache(maxsize=2)
def berco_img(w=620):
    p = Pen(620, 360)
    wood, woodd = hexc('#c99a64'), hexc('#a77a48')
    p.shape([(20, 40), (600, 40), (600, 80), (20, 80)], wood, woodd, 5, 4)
    for x in range(60, 600, 70): p.shape([(x - 10, 80), (x + 10, 80), (x + 10, 300), (x - 10, 300)], wood, woodd, 4, 2)
    p.shape([(20, 290), (600, 290), (600, 330), (20, 330)], wood, woodd, 5, 4)
    for x in (30, 590): p.shape([(x - 16, 20), (x + 16, 20), (x + 16, 360), (x - 16, 360)], wood, woodd, 5, 4)
    return p.img.resize((w, int(w * 360 / 620)), Image.LANCZOS)


@lru_cache(maxsize=8)
def folha_cal(k, w=200):
    p = Pen(200, 220)
    p.shape([(10, 20), (190, 20), (190, 210), (10, 210)], hexc('#fffdf6'), hexc('#e6e0cf'), 5, 6)
    p.poly([(10, 20), (190, 20), (190, 70), (10, 70)], hexc('#e76f51'))
    p.stroke([(10, 70), (190, 70)], 5)
    for dx in (60, 140): p.dot(dx, 22, 9, INK)
    im = p.img
    d = ImageDraw.Draw(im)
    return im.resize((w, int(w * 1.1)), Image.LANCZOS)


def hic(c, x, y, f, f0, size=110, rot=-8):
    if 0 <= f - f0 < 16:
        paste_c(c, txt('HIC!', size, rot), x, y - 2 * (f - f0), back(ramp(f, f0, f0 + 6)) * (1 - ramp(f, f0 + 12, f0 + 16)))


def jolt(f, f0):
    return -22 * (1 - ramp(f, f0 + 2, f0 + 7)) * (1 if f >= f0 else 0)


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 corpo (diafragma levando susto) | s1 corpo (pulmões em cima, diafragma embaixo puxando o ar) | s2 cozinha (pessoa comendo
# rápido + refrigerante, puxão) | s3 corpo (garganta por dentro: ar sobe, cordas vocais fecham, HIC) | s4 sala (homem idoso
# soluçando, folhas de calendário voando: 68 ANOS) | s5 lab/berçário (bebê no berço soluçando, cérebro acende) |
# s6 escritorio ao entardecer (adulto soluçando na mesa, "treino de bebê")

def SFX(s):
    s.thunk(s.W(0, 'susto') - 2, 320, .8)
    s.whoosh(s.W(1, 'ar') - 6, .4, .4)
    s.patter(s.W(2, 'refrigerante'), s.W(2, 'refrigerante') + 20, 10, .1); s.thunk(s.W(2, 'puxao') - 2, 300, .8)
    s.whoosh(s.W(3, 'correndo') - 6, .5, .4); s.thunk(s.W(3, 'fecham') - 2, 340, .9); s.ting(s.W(3, 'barulhinho'), .3)
    for i in range(4): s.thunk(s.W(4, 'anos') - 2 + i * 9, 320, .5)
    s.ting(s.W(5, 'cerebro'), .3); s.thunk(s.W(5, 'barriga') - 2, 320, .5)
    s.thunk(s.W(6, 'desligou') - 2, 320, .7); s.trill(s.W(6, 'desligou') + 4, 1.0, .3)


def s0(f):
    c = CEN('corpo').copy()
    k = wt(0, 'susto') - 3
    pull = pulse(f, k, 6)
    put_dia(c, 621, 1500 + 40 * pull, 1000, f, 1, expr='shock' if f >= k else 'calm', pull=pull, look=0)
    hic(c, 621, 900, f, k, 150)
    if f >= k + 16: paste_c(c, txt('SUSTO!', 110, 6), 621, 900, back(ramp(f, k + 16, k + 24)))
    z = lerp(1.35, 1.08, easeOut(ramp(f, 0, 40)))
    return c, (621, 1250 + kick(f, k) * 10, z, kick(f, k)), 'day'


def s1(f):
    c = CEN('corpo').copy()
    a = wt(1, 'ar') - 3
    br = .5 + .5 * math.sin((f - a) * .18) if f >= a else 0
    paste_c(c, pulmoes_img(round(br * 4) / 4, 760), 621, 900)
    put_dia(c, 621, 1520 + 30 * br, 900, f, 2, pull=br, look=-.2)
    d = wt(1, 'diafragma') - 3
    if f >= d: paste_c(c, txt('DIAFRAGMA', 90, -4), 621, 1620, back(ramp(f, d, d + 8)))
    pu = wt(1, 'pulmoes') - 3
    if f >= pu and f < d: paste_c(c, txt('PULMÕES', 90, 4), 621, 480, back(ramp(f, pu, pu + 8)))
    t = smooth(ramp(f, 0, 60))
    return c, (621, lerp(950, 1250, t), lerp(1.25, 1.05, t), 0), 'day'


def s2(f):
    c = CEN('cozinha').copy()
    r = wt(2, 'refrigerante') - 3
    p = wt(2, 'puxao') - 3
    paste_c(c, copo_img(200), 900, 1430 if f < r else 1400, back(ramp(f, r, r + 8)) if f >= r - 30 else 0)
    j = jolt(f, p)
    chew = (f // 5) % 2 if f < p else 0
    put_pessoa(c, 500, 1640 + j, 900, f, 3, expr='shock' if f >= p else ('grin' if chew else 'smug'), arms='cheek' if f < p else 'up', shirt='#5aa9e6', hair='#2b2b2b')
    if f < r:
        for i in range(3):
            a = (f + i * 9) % 27
            paste_c(c, txt('NHAC', 60, -10 + i * 8), 700 + a * 2, 900 - a * 4 - i * 30, 1 - a / 27)
    if f >= p: hic(c, 760, 760, f, p, 120)
    if f >= p: paste_c(c, txt('PUXÃO!', 90, 6), 500, 520, back(ramp(f, p + 14, p + 22)))
    z = lerp(1.1, 1.22, smooth(ramp(f, 0, 100)))
    return c, (621, 1200 + kick(f, p) * 10, z, kick(f, p)), 'day'


def s3(f):
    c = CEN('corpo').copy()
    cr = wt(3, 'correndo') - 3
    fe = wt(3, 'fecham') - 3
    cl = easeOut(ramp(f, fe, fe + 3))
    paste_c(c, _cordas(round(cl * 6) / 6, 700), 621, 1100)
    # ar subindo (setas) até as cordas fecharem
    if cr <= f:
        for i in range(4):
            a = ((f - cr) * 18 + i * 120) % 480
            y = 1560 - a
            if f >= fe: y = max(y, 1260)
            paste_c(c, txt('↑', 90), 621 + (i % 2) * 60 - 30, y, 1)
    if f >= fe: paste_c(c, txt('FECHOU!', 90, 6), 621, 650, back(ramp(f, fe, fe + 8)))
    b = wt(3, 'barulhinho') - 3
    hic(c, 800, 880, f, b, 110)
    z = lerp(1.05, 1.3, smooth(ramp(f, 0, 70)))
    return c, (621, 1150 + kick(f, fe) * 10, z, kick(f, fe)), 'day'


def s4(f):
    c = CEN('sala').copy()
    a = wt(4, 'anos') - 3
    per = 22
    h0 = (f % per == 0)
    ph = f % per
    put_pessoa(c, 621, 1640 + jolt(ph, 0), 900, f, 4, expr='shock' if ph < 6 else 'pained', arms='cheek', hair='#d9d9d9', shirt='#7c9a6b', mous=True)
    hic(c, 880, 980, ph, 0, 90)
    if f >= a:
        for i in range(8):
            t = (f - a - i * 6) / 30
            if 0 <= t < 1:
                paste_c(c, folha_cal(i, 150), 330 + i * 70 + 200 * t, 820 - 250 * t + 200 * t * t, 1 - t * .5)
        paste_c(c, txt('68 ANOS!', 105, -6), 621, 640, back(ramp(f, a, a + 8)))
    z = lerp(1.1, 1.2, smooth(ramp(f, 0, 90)))
    return c, (621, 1220, z, 0), 'golden'


def s5(f):
    c = CEN('lab', 'dusk').copy()
    b = wt(5, 'barriga') - 3
    ce = wt(5, 'cerebro') - 3
    ph = (f - b) % 26 if f >= b else 99
    paste_c(c, berco_img(640), 520, 1480)
    put_bebe(c, 520, 1560, 380, f, 5, hic=1 if ph < 6 else 0)
    if f >= b: hic(c, 760, 1050, ph, 0, 90)
    if f >= ce:
        g = .5 + .5 * math.sin((f - ce) * .3)
        cont = Image.new('RGBA', (330, 300), (0, 0, 0, 0))
        br = cerebro(300)
        cont.alpha_composite(br, (15, 30))
        thought(c, 840, 800, 220, back(ramp(f, ce, ce + 8)), cont)
        if ph < 8: paste_c(c, txt('ZAP!', 70, 8), 1000, 640, 1)
    put_sci(c, 1050, 1640, 760, f, 2, arms='clip', bun=True, expr='grin', look=-1)
    z = lerp(1.05, 1.2, smooth(ramp(f, 0, 150)))
    return c, (700, 1200, z, 0), 'dusk'


def s6(f):
    c = CEN('escritorio', 'dusk').copy()
    bb = wt(6, 'bebe') - 3
    d = wt(6, 'desligou') - 3
    ph = (f - 4) % 30
    put_pessoa(c, 560, 1640 + jolt(ph, 0), 960, f, 6, expr='shock' if ph < 6 else 'nervous', arms='shrug', shirt='#ff8a5c')
    hic(c, 300, 860, ph, 0, 90)
    if f >= bb:
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        cont.alpha_composite(bebe(0, 'calm', 0).resize((230, 264), Image.LANCZOS), (35, 20))
        thought(c, 940, 780, 180, back(ramp(f, bb, bb + 8)), cont)
    if f >= d: paste_c(c, txt('TREINO DE BEBÊ', 76, -4), 600, 1430, back(ramp(f, d, d + 8)))
    z = lerp(1.05, 1.3, easeOut(ramp(f, 0, 80)))
    return c, (640, 1150, z, lerp(0, -2.5, smooth(ramp(f, 0, 80)))), 'dusk'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
