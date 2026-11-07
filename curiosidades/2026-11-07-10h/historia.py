"""Formato DESENHO: por que a gente se arrepia (Curiosidades da IA, 07/11/2026, 10h). Categoria: CORPO HUMANO.
Fatos: Live Science, "Why do we get goosebumps?" (músculos eretores do pelo, um para cada pelo, ficam sob a pele; ao
contrair levantam o pelo e fazem o calombinho; nos mamíferos o pelo em pé prende calor e, quando ameaçados, faz o
bicho parecer maior; nos humanos é um traço vestigial, útil nos antepassados peludos, que nunca sumiu; acontece no frio
e em emoções fortes); Why Evolution Is True (os mesmos músculos arrepiam o gato); Science News 2020 (estudo de Harvard
em camundongos: os nervos desses músculos também ativam células-tronco do pelo)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h18 = _load('h18', '2026-11-06-18h')
jovem = _h18.jovem

LINES = [
    "Todo arrepio é o seu corpo tentando ficar peludo.",
    "Embaixo de cada pelo tem um músculo minúsculo, que no frio puxa o pelo pra cima.",
    "Cada pelo em pé levanta um montinho na pele: é a tal pele de galinha.",
    "Num gato, o mesmo truque deixa o pelo fofo, prendendo ar quentinho perto do corpo.",
    "E no susto, o pelo arrepiado deixa o gato com cara de bicho maior.",
    "Você vê, nossos antepassados eram bem mais peludos, e o arrepio funcionava como um casaco.",
    "A gente perdeu quase todo o pelo... mas o músculo ficou.",
    "Ou seja: no frio, seu corpo ainda tenta vestir um casaco... que não existe mais.",
]
CAPTXT = [
    "Todo arrepio é o seu corpo tentando ficar peludo.",
    "Embaixo de cada pelo tem um músculo minúsculo,|que no frio puxa o pelo pra cima.",
    "Cada pelo em pé levanta um montinho na pele:|é a tal pele de galinha.",
    "Num gato, o mesmo truque deixa o pelo fofo,|prendendo ar quentinho perto do corpo.",
    "E no susto, o pelo arrepiado deixa o gato|com cara de bicho maior.",
    "Você vê, nossos antepassados eram bem mais peludos,|e o arrepio funcionava como um casaco.",
    "A gente perdeu quase todo o pelo...|mas o músculo ficou.",
    "Ou seja: no frio, seu corpo ainda tenta vestir um casaco...|que não existe mais.",
]
FALA_TIKTOK = "Você se arrepiou só de ouvir? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'arrepio', 4), (0, 'peludo', 6), (1, 'musculo', 4), (1, 'puxa', 6), (2, 'galinha', 6), (3, 'gato', 4),
         (3, 'quentinho', 6), (4, 'susto', 4), (4, 'maior', 6), (5, 'peludos', 4), (5, 'casaco', 6), (6, 'perdeu', 4),
         (6, 'ficou', 6), (7, 'casaco', 4), (7, 'existe', 8)]

PELE, PELED = hexc('#f5c9a0'), hexc('#d9a77a')
CINZA, CINZAD = hexc('#f0a35a'), hexc('#cf7f3a')   # gato laranja
MUSC, MUSCD = hexc('#e8737f'), hexc('#c4525f')


def put_jovem(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'jovem', x, feet, h, f, seed, **kw)


# ------------------------------------------------------------------ personagens novos
def gato(puff=0.0, expr='calm', blink=0, look=0.5):
    """gato de lado (olha p/ direita), 700x600, pés em y≈580; puff 0..1 arrepia o pelo."""
    p = Pen(700, 600)
    pf = puff
    # rabo
    tail = [(150, 380), (95, 300), (90, 200), (120, 120)] if pf < .5 else [(150, 360), (110, 260), (120, 150), (150, 60)]
    p.line(tail, CINZA, 34 + 50 * pf, 5)
    # pernas
    for x in (215, 255, 400, 440):
        p.line([(x, 420), (x, 570)], CINZA if x in (215, 400) else CINZAD, 34, 5)
        p.shape(ell_pts(x + 8, 572, 26, 12), CINZA, CINZAD, 4, 3)
    # corpo (arrepiado = contorno de pontas e arqueado)
    cx, cy, rx, ry = 320, 380 - 40 * pf, 180 + 30 * pf, 95 + 55 * pf
    pts = ell_pts(cx, cy, rx, ry, 72, 0, 0, 2.2)
    if pf > .05:
        pts = [(cx + (x - cx) * (1 + .09 * pf * (i % 2)), cy + (y - cy) * (1 + .12 * pf * (i % 2))) for i, (x, y) in enumerate(pts)]
    p.shape(pts, CINZA, CINZAD, 6, 20)
    for k in range(3):
        p.stroke([(cx - 60 + k * 50, cy - ry + 20), (cx - 40 + k * 50, cy - ry + 55)], 7, CINZAD)
    # cabeça
    hx, hy = 500 + 10 * pf, 250 - 30 * pf
    hp = ell_pts(hx, hy, 110 + 15 * pf, 95 + 12 * pf, 48)
    if pf > .05:
        hp = [(hx + (x - hx) * (1 + .08 * pf * (i % 2)), hy + (y - hy) * (1 + .08 * pf * (i % 2))) for i, (x, y) in enumerate(hp)]
    for s in (-1, 1):
        ex0 = hx + s * 55
        p.shape([(ex0 - 35, hy - 60), (ex0 + s * 10, hy - 150 - 15 * pf), (ex0 + 40, hy - 55)], CINZA, CINZAD, 5, 6)
        p.poly([(ex0 - 18, hy - 70), (ex0 + s * 8, hy - 125 - 15 * pf), (ex0 + 22, hy - 68)], hexc('#f7b3bd'))
    p.shape(hp, CINZA, CINZAD, 6, 14)
    p.dot(hx + 95, hy + 20, 13, hexc('#e8737f'), 3)  # nariz
    for s in (-1, 1):
        p.stroke([(hx + 70, hy + 30 + s * 8), (hx + 150, hy + 22 + s * 22)], 3)
    ex, ey = hx + 40, hy - 15
    if blink > .6:
        p.stroke([(ex - 22, ey), (ex + 22, ey)], 7)
    else:
        r = 40 if expr == 'shock' else 32
        p.dot(ex, ey, r, (255, 255, 255), 5)
        p.dot(ex + look * 10, ey + 2, 10 if expr == 'shock' else 15, INK)
        p.dot(ex + look * 10 - 4, ey - 4, 4, (255, 255, 255))
        if expr == 'side': p.poly([(ex - r - 2, ey - r - 4), (ex + r + 2, ey - r - 4), (ex + r + 2, ey - 8), (ex - r - 2, ey - 8)], CINZA); p.stroke([(ex - r, ey - 8), (ex + r, ey - 8)], 6)
    if expr == 'shock': p.dot(hx + 70, hy + 60, 15, hexc('#7a2e2e'), 4)
    elif expr == 'happy': p.arc(hx + 72, hy + 48, 18, 10, 20, 160, 5)
    else: p.arc(hx + 78, hy + 50, 12, 7, 20, 160, 5)
    return p.img


def put_gato(c, x, feet, h, f, seed=1, flip=False, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'puff' in kw: kw['puff'] = round(kw['puff'] * 8) / 8
    put_sprite(c, 'gato', x, feet, h, 700 / 600, flip, **kw)


def peludo(puff=0.0, expr='neutral', blink=0, look=0.0, tilt=0.0):
    """antepassado bem peludo (600x1000, pés em y≈975); puff afofa o pelo."""
    p = Pen(600, 1000)
    fur, furd = hexc('#8a5a3a'), hexc('#6a4228')
    for s in (-1, 1):
        p.line([(300 + s * 50, 760), (300 + s * 55, 955)], fur, 40, 5)
        p.shape(ell_pts(300 + s * 55 + 14, 962, 40, 18), PELE, PELED, 4, 4)
    cx, cy = 300, 560
    rx, ry = 170 + 40 * puff, 260 + 30 * puff
    pts = ell_pts(cx, cy, rx, ry, 90, 0, .05)
    pts = [(cx + (x - cx) * (1 + (.05 + .07 * puff) * (i % 2)), cy + (y - cy) * (1 + (.03 + .05 * puff) * (i % 2))) for i, (x, y) in enumerate(pts)]
    p.shape(pts, fur, furd, 6, 22)
    rnd = random.Random(4)
    for i in range(26):
        x, y = rnd.uniform(cx - rx * .7, cx + rx * .7), rnd.uniform(cy - ry * .5, cy + ry * .8)
        p.stroke([(x, y), (x + 8, y + 26)], 5, furd)
    hc = (300 + tilt * 6, 330)
    p.shape(ell_pts(hc[0], hc[1], 105, 100, 48), PELE, PELED, 5, 14)
    face(p, hc[0], hc[1] + 6, expr, blink, look)
    return p.img


def put_peludo(c, x, feet, h, f, seed, **kw):
    if 'puff' in kw: kw['puff'] = round(kw['puff'] * 6) / 6
    kit._bean(c, 'peludo', x, feet, h, f, seed, **kw)


def pele(pull=0.0, expr='calm', blink=0, n=1, hair=True):
    """corte da pele: camada de pele em cima, pelo atravessando, músculo com carinha puxando (900x800)."""
    p = Pen(900, 800)
    top = 260
    bump = 90 * pull
    surf = [(0, top)] + [(x, top - bump * math.exp(-((x - 450) / 110) ** 2)) for x in range(0, 901, 30)] + [(900, top)]
    p.poly(surf + [(900, 800), (0, 800)], hexc('#f6c7a4'))
    p.poly([(0, top + 120), (900, top + 120), (900, 800), (0, 800)], hexc('#f4b7a0'))
    p.stroke(surf[1:-1], 7)
    # raiz do pelo (folículo) inclinada; o pelo gira até ficar em pé
    a = math.radians(lerp(55, 88, pull))
    rx, ry = 450 - 150 * math.cos(a), top + 300 * math.sin(a) - 80
    sx, sy = 450, top - bump
    p.shape(ell_pts(rx, ry, 40, 60, 32, -(math.pi / 2 - a)), hexc('#e8a48a'), hexc('#cc8a72'), 5, 8)
    if hair:
        L = 300
        ha = math.radians(lerp(155, 95, pull))
        p.line([(rx, ry), (sx, sy), (sx + L * math.cos(ha), sy - L * math.sin(ha))], hexc('#4a3326'), 12, 4)
    # músculo: vai do pé do pelo até a pele à direita; encurta com pull
    mx0, my0 = rx + 30, ry - 30
    mx1, my1 = 760, top + 70
    mc = ((mx0 + mx1) / 2, (my0 + my1) / 2 + 20 * (1 - pull))
    ang = math.atan2(my1 - my0, mx1 - mx0)
    ln = math.hypot(mx1 - mx0, my1 - my0)
    p.shape(ell_pts(mc[0], mc[1], ln / 2 * (1 - .12 * pull), 46 + 22 * pull, 48, ang), MUSC, MUSCD, 5, 10)
    for dx in (-26, 26):
        ex, ey = mc[0] + dx, mc[1] - 6
        if blink > .6: p.stroke([(ex - 12, ey), (ex + 12, ey)], 5)
        elif expr == 'strain': p.stroke([(ex - 12, ey - 6), (ex + 10, ey), (ex - 12, ey + 6)] if dx < 0 else [(ex + 12, ey - 6), (ex - 10, ey), (ex + 12, ey + 6)], 5)
        else: p.dot(ex, ey, 14, (255, 255, 255), 4); p.dot(ex + 4, ey + 1, 6, INK)
    if expr == 'smug': p.arc(mc[0], mc[1] + 20, 18, 9, 20, 160, 5)
    elif expr == 'strain': p.stroke([(mc[0] - 16, mc[1] + 22), (mc[0] + 16, mc[1] + 22)], 5)
    else: p.arc(mc[0], mc[1] + 18, 12, 7, 20, 160, 5)
    return p.img


def put_pele(c, x, y, w, f, seed=1, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'pull' in kw: kw['pull'] = round(kw['pull'] * 8) / 8
    im = sprite('pele', tuple(sorted(kw.items())), int(w * 800 / 900), 900 / 800, False)
    paste_c(c, im, x, y)


def braco(bumps=0.0):
    """close no antebraço com pelinhos e calombos (1000x500)."""
    p = Pen(1000, 500)
    p.shape([(-20, 120), (1020, 80), (1020, 420), (-20, 460)], PELE, PELED, 6, 24)
    rnd = random.Random(7)
    for i in range(34):
        x = rnd.uniform(40, 960); y = rnd.uniform(150, 390) - x * .04
        r = 22 * bumps
        if r > 2:
            p.dot(x + 4, y + 5, r + 2, hexc('#c98f62')); p.dot(x, y, r, hexc('#fbdcbc')); p.arc(x, y, r, r, 20, 160, 3, hexc('#b07a50'))
        ang = math.radians(lerp(160, 95, bumps) + rnd.uniform(-8, 8))
        p.stroke([(x, y), (x + 34 * math.cos(ang) * -1, y - 34 * math.sin(ang))], 4, hexc('#6a4a36'))
    return p.img


def put_braco(c, x, y, w, bumps):
    im = sprite('braco', (('bumps', round(bumps * 6) / 6),), int(w / 2), 2.0, False)
    paste_c(c, im, x, y)


def vento(c, x, y, f, k=1.0):
    """linhas de vento frio entrando pela janela."""
    p = Pen(500, 400)
    for i in range(4):
        o = ((f * 9 + i * 60) % 260)
        yy = 60 + i * 80
        p.stroke([(o, yy), (o + 120, yy - 10), (o + 180, yy + 10)], 8, hexc('#cfe8ff'))
    paste_c(c, p.img.resize((500, 400), Image.LANCZOS), x, y, k)


def ar_quente(c, x, y, f, k=1.0):
    for i in range(6):
        a = (f * 2 + i * 23) % 70
        r = 18 + 6 * (i % 3)
        ang = i * math.pi / 3 + f * .02
        paste_c(c, txt('~', int(60 + 10 * (i % 2))), x + 220 * math.cos(ang) * k, y + 140 * math.sin(ang) * k - a * .3, k * (1 - a / 90))


def SFX(s):
    s.whoosh(s.W(0, 'arrepio') - 6, .5, .4)
    s.thunk(s.W(0, 'peludo') - 2, 160, .6)
    s.ting(s.W(1, 'musculo'), .3)
    s.thunk(s.W(1, 'puxa') - 2, 260, .6)
    for i in range(5): s.thunk(s.W(2, 'montinho') - 2 + i * 3, 380, .3)
    s.ting(s.W(2, 'galinha'), .3)
    s.ting(s.W(3, 'gato'), .25)
    s.thunk(s.W(4, 'susto') - 2, 120, .9)
    s.whoosh(s.W(4, 'maior') - 6, .4, .5)
    s.ting(s.W(5, 'casaco'), .3)
    s.thunk(s.W(6, 'ficou') - 2, 200, .6)
    s.trill(s.W(7, 'existe'), .9, .3)


# ---------------------------------------------------------------- cenas (cenário de cada uma)
# s0 quarto (pessoa com frio na janela) | s1 corpo (corte da pele) | s2 quarto (close no braço) | s3 sala (gato no frio)
# s4 sala (gato leva susto) | s5 floresta (antepassado peludo) | s6 corpo (músculo que ficou) | s7 quarto (pessoa com frio)
def s0(f):
    c = CEN('quarto', 'day').copy()
    a0 = wt(0, 'arrepio') - 3
    p0 = wt(0, 'peludo') - 3
    vento(c, 900, 430, f)
    sh = 6 * math.sin(f * 1.7) if f >= a0 else 0
    put_jovem(c, 560 + sh, 1900, 1000, f, 1, arms='cheek' if f >= a0 else 'hang', expr='nervous' if f < p0 else 'shock',
              shirt='#7fb3e6', look=.6)
    if a0 <= f < p0: paste_c(c, txt('BRRR!', 110, -6), 560, 640, back(ramp(f, a0, a0 + 8)))
    if f >= p0:
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        cont.alpha_composite(sprite('peludo', (('blink', 0), ('expr', 'grin'), ('look', 0.0), ('puff', 1.0), ('tilt', 0.0)), 260, .6, False), (80, 20))
        thought(c, 830, 620, 200, back(ramp(f, p0 - 4, p0 + 6)), cont)
    t = easeOut(ramp(f, 0, 40))
    kk = kick(f, a0 + 2)
    return c, (lerp(600, 640, t), 1250 + kk * 10, lerp(1.45, 1.1, t), kk), 'day'


def s1(f):
    c = corpo().copy()
    m0 = wt(1, 'musculo') - 3
    p0 = wt(1, 'puxa') - 3
    pull = easeOut(ramp(f, p0, p0 + 14))
    put_pele(c, 620, 1150, 1100, f, 1, pull=pull, expr='strain' if f >= p0 else ('calm' if f >= m0 else 'calm'))
    if m0 <= f < p0: paste_c(c, txt('MÚSCULO', 100, -5), 840, 1560, back(ramp(f, m0, m0 + 8)))
    if f >= p0: paste_c(c, txt('PUXA!', 120, 6), 840, 1560, back(ramp(f, p0, p0 + 8)))
    if f < m0: paste_c(c, txt('PELE', 90, -4), 300, 560, back(ramp(f, 2, 10)))
    t = smooth(ramp(f, 0, 60))
    return c, (lerp(640, 660, t), lerp(1000, 1180, t), lerp(1.0, 1.15, t), 0), 'day'


@lru_cache(maxsize=1)
def corpo():
    return CEN('corpo', 'day')


def s2(f):
    c = CEN('quarto', 'day').copy()
    m0 = wt(2, 'montinho') - 3
    g0 = wt(2, 'galinha') - 3
    put_braco(c, 700, 1180, 1100, easeOut(ramp(f, m0, m0 + 14)))
    if f >= g0: paste_c(c, txt('PELE DE GALINHA', 72, -4), 700, 860, back(ramp(f, g0, g0 + 8)))
    t = smooth(ramp(f, 0, 50))
    return c, (700, lerp(1150, 1180, t), lerp(1.2, 1.45, t), 0), 'day'


def s3(f):
    c = CEN('sala', 'day').copy()
    g0 = wt(3, 'gato') - 3
    q0 = wt(3, 'quentinho') - 3
    fofo = wt(3, 'fofo') - 3
    vento(c, 380, 560, f, .8)
    pf = .55 * easeOut(ramp(f, fofo, fofo + 12))
    put_gato(c, 640, 1700, 620 * back(ramp(f, g0 - 4, g0 + 6)) if f < g0 + 6 else 620, f, 2, puff=pf, expr='happy' if f >= q0 else 'calm', look=.3)
    if f >= q0: ar_quente(c, 640, 1380, f, easeOut(ramp(f, q0, q0 + 10)))
    if f >= fofo and f < q0: paste_c(c, txt('FOFO!', 110, 6), 640, 830, back(ramp(f, fofo, fofo + 8)))
    if f >= q0: paste_c(c, txt('QUENTINHO', 100, -5), 640, 830, back(ramp(f, q0, q0 + 8)))
    t = smooth(ramp(f, 0, 70))
    return c, (640, lerp(1150, 1300, t), lerp(1.05, 1.25, t), 0), 'day'


def s4(f):
    c = CEN('sala', 'day').copy()
    s0_ = wt(4, 'susto') - 3
    m0 = wt(4, 'maior') - 3
    pf = .55 if f < s0_ else lerp(.55, 1.0, easeOut(ramp(f, s0_, s0_ + 6)))
    sz = 620 if f < m0 else lerp(620, 840, back(ramp(f, m0, m0 + 10)))
    put_gato(c, 620, 1700, sz, f, 2, puff=pf, expr='shock' if f >= s0_ else 'calm', look=1)
    if s0_ <= f < m0: paste_c(c, txt('SUSTO!', 120, -6), 640, 760, back(ramp(f, s0_, s0_ + 6)))
    if f >= m0: paste_c(c, txt('MAIOR!', 140, 6), 640, 700, back(ramp(f, m0, m0 + 8)))
    kk = kick(f, s0_ + 2)
    z = 1.2 * (1 - .12 * easeOut(ramp(f, m0, m0 + 14)))
    return c, (640, 1250 + kk * 10, z, kk * 2), 'day'


def s5(f):
    c = CEN('floresta', 'golden').copy()
    p0 = wt(5, 'peludos') - 3
    k0 = wt(5, 'casaco') - 3
    put_peludo(c, 600, 1900, 1050, f, 3, puff=easeOut(ramp(f, k0, k0 + 10)), expr='neutral' if f < k0 else 'grin', look=.4)
    if p0 <= f < k0: paste_c(c, txt('PELUDOS!', 110, -5), 640, 640, back(ramp(f, p0, p0 + 8)))
    if f >= k0:
        paste_c(c, txt('= CASACO', 120, 5), 640, 640, back(ramp(f, k0, k0 + 8)))
        ar_quente(c, 600, 1300, f, 1.3 * easeOut(ramp(f, k0, k0 + 10)))
    t = smooth(ramp(f, 0, 90))
    return c, (640, lerp(1300, 1220, t), lerp(1.05, 1.22, t), lerp(0, -2, t)), 'golden'


def s6(f):
    c = corpo().copy()
    p0 = wt(6, 'perdeu') - 3
    k0 = wt(6, 'ficou') - 3
    hair = f < p0 + 6
    put_pele(c, 620, 1150, 1100, f, 4, pull=.0 if f < k0 else .5 + .5 * math.sin(f * .3) ** 2, hair=hair, expr='smug' if f >= k0 else 'calm')
    if p0 <= f < p0 + 12:
        u = ramp(f, p0, p0 + 12)
        paste_c(c, txt('TCHAU, PELO!', 80, -5), 640, 520, back(ramp(f, p0, p0 + 6)))
    if f >= k0: paste_c(c, txt('FIQUEI!', 120, 6), 840, 1560, back(ramp(f, k0, k0 + 8)))
    t = smooth(ramp(f, 0, 60))
    return c, (lerp(620, 700, t), lerp(1100, 1250, t), lerp(1.05, 1.3, t), 0), 'dusk'


def s7(f):
    c = CEN('quarto', 'dusk').copy()
    k0 = wt(7, 'casaco') - 3
    e0 = wt(7, 'existe') - 3
    vento(c, 900, 430, f)
    sh = 5 * math.sin(f * 1.7)
    put_jovem(c, 560 + sh, 1900, 1000, f, 1, arms='cheek', expr='nervous' if f < e0 else 'shock', shirt='#7fb3e6', look=.6)
    if f >= k0 and f < e0:
        # casaco "fantasma" tentando aparecer
        a = .5 + .3 * math.sin(f * .4)
        paste_c(c, txt('CASACO?', 110, -5), 600, 620, back(ramp(f, k0, k0 + 8)))
    if f >= e0: paste_c(c, txt('NADA!', 130, 6), 600, 620, back(ramp(f, e0, e0 + 8)))
    t = easeOut(ramp(f, 0, 80))
    return c, (600, 1250, lerp(1.1, 1.35, t), lerp(0, 2.5, t)), 'dusk'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6, s7)]
