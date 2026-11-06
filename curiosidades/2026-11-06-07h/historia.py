"""Formato DESENHO: a avestruz não enterra a cabeça na areia (Curiosidades da IA, 06/11/2026, post extra).
Fatos: Live Science "Do ostriches really bury their heads in the sand?" (mito; ninho = buraco raso na areia;
os pais viram os ovos várias vezes por dia; ameaçada, deita com o pescoço esticado no chão; até 70 km/h segundo
o Smithsonian's National Zoo; mito provavelmente vem do naturalista romano Plínio, o Velho, em História Natural, séc. I);
Science World (viram os ovos com o bico; mito desde a Roma Antiga; 70 km/h)."""
from kit import *
import kit
from PIL import ImageDraw

LINES = [
    "A avestruz não enterra a cabeça na areia.",
    "Essa ideia tem quase dois mil anos: um sábio romano escreveu que ela escondia a cabeça pra ficar invisível.",
    "Só que, na vida real, nenhuma avestruz faz isso.",
    "Ela cava um buraco raso no chão, que é o ninho, e bota os ovos lá dentro.",
    "E várias vezes por dia, abaixa a cabeça no buraco pra virar os ovos com o bico.",
    "Você vê, de longe, parece mesmo que a cabeça sumiu na areia.",
    "E quando se assusta? Deita e estica o pescoço no chão. Ou foge a setenta quilômetros por hora.",
    "Ou seja: nessa história, quem enterrou a cabeça na areia... fomos nós.",
]
CAPTXT = [
    "A avestruz não enterra a cabeça na areia.",
    "Essa ideia tem quase 2 mil anos:|um sábio romano escreveu que ela escondia a cabeça pra ficar invisível.",
    "Só que, na vida real, nenhuma avestruz faz isso.",
    "Ela cava um buraco raso no chão, que é o ninho,|e bota os ovos lá dentro.",
    "E várias vezes por dia, abaixa a cabeça no buraco|pra virar os ovos com o bico.",
    "Você vê, de longe, parece mesmo que a cabeça sumiu na areia.",
    "E quando se assusta? Deita e estica o pescoço no chão.|Ou foge a 70 quilômetros por hora.",
    "Ou seja: nessa história, quem enterrou a cabeça na areia... fomos nós.",
]
FALA_TIKTOK = "Você acreditava nessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'nao', 4), (1, 'invisivel', 4), (2, 'nenhuma', 6), (3, 'ovos', 6), (4, 'bico', 4), (5, 'sumiu', 4), (6, 'deita', 8), (6, 'setenta', 6), (7, 'nos', 6)]

# ------------------------------------------------------------------ personagens novos
OST = dict(body=hexc('#2e2626'), bodyDk=hexc('#171214'), streak=hexc('#544846'), neck=hexc('#e9b9a6'), neckDk=hexc('#c58e7c'),
           head=hexc('#dca493'), beak=hexc('#ecc89c'), leg=hexc('#e1a593'), legDk=hexc('#b57c6c'))
SAND, SANDD, HOLE = hexc('#ecd29a'), hexc('#c9a865'), hexc('#6b4c32')


def ostrich(phase=0.0, run=0.0, peck=0.0, blink=0, expr='calm', look=0.3, seed=1, lie=0):
    """avestruz de lado olhando p/ direita (corpo preto, cauda branca, pescoço rosado). 600x800, pés y~780."""
    old = art.EMU; art.EMU = OST
    try:
        body = art.emu(phase=phase, run=run, peck=peck, blink=blink, expr=expr, look=look, seed=seed)
    finally:
        art.EMU = old
    p = Pen(600, 800)
    two = 2 * math.pi
    bob = run * 16 * abs(math.sin(two * phase)) + (1 - run) * 3 * math.sin(seed * 3.1)
    lean = run * .16 + peck * .12
    bx, by = 290 - 150, 432 + bob - 30 + lean * 120
    tx, ty = 290 - 165, 432 + bob - 40 + lean * 60
    for dx, dy, rx, ry, rt in ((-10, 26, 74, 24, -.15), (0, 0, 80, 26, -.55), (-6, -28, 66, 22, -.95)):
        p.shape(ell_pts(tx + dx, ty + dy, rx, ry, 30, rt), (250, 248, 242), (214, 210, 204), 5, 6)
    im = p.img
    im.alpha_composite(body)
    if lie:
        a = np.array(im); Hh, Ww = a.shape[:2]
        a[int(Hh * .74):, :int(Ww * .783), 3] = 0
        sh = int(Hh * .231)
        out = np.zeros_like(a); out[sh:] = a[:-sh]
        im = Image.fromarray(out)
    return im


def put_ost(c, x, feet, h, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    put_sprite(c, 'ostrich', x, feet, h, .75, flip, {'phase': 16, 'peck': 6, 'run': 4}, **kw)


def head_pos(x, feet, h, peck=1.0):
    """onde fica a cabeça da avestruz no palco (para o buraco cobrir)."""
    s = h / 800
    hx = 448 * (1 - peck) + 548 * peck; hy = 128 * (1 - peck) + 700 * peck
    return x - 300 * s + hx * s, feet + h * .025 - 800 * s + hy * s


def nest_back(c, cx, cy, w, eggs=0, egg_s=1.0, wob=0.0):
    d = ImageDraw.Draw(c)
    d.ellipse([cx - w * .75, cy - w * .2, cx + w * .75, cy + w * .2], fill=SAND, outline=INK, width=5)
    d.ellipse([cx - w * .5, cy - w * .12, cx + w * .5, cy + w * .12], fill=HOLE, outline=INK, width=5)
    for i in range(eggs):
        ex = cx + (i - (eggs - 1) / 2) * w * .22; ey = cy - w * .02 + (i % 2) * w * .04
        r = w * .085 * egg_s; rot = wob * math.sin(i * 1.7)
        pts = [(ex + r * math.cos(a) * 1.0 * math.cos(rot) - r * 1.25 * math.sin(a) * math.sin(rot),
                ey + r * math.cos(a) * math.sin(rot) + r * 1.25 * math.sin(a) * math.cos(rot)) for a in np.linspace(0, 2 * math.pi, 30)]
        if r > 2: d.polygon(pts, fill=(250, 244, 226), outline=INK, width=4)


def nest_berm(c, cx, cy, w, hgt=1.0):
    """monte de areia na frente do buraco (cobre a cabeça)."""
    if hgt <= .02: return
    d = ImageDraw.Draw(c)
    top = cy - w * .30 * hgt
    bot = cy + w * .15
    pts = [(cx + w * .45 * math.cos(a), bot - (bot - top) * math.sin(a)) for a in np.linspace(math.pi, 0, 24)] + [(cx + w * .45 * math.cos(a), bot + w * .05 * math.sin(a)) for a in np.linspace(0, math.pi, 16)]
    d.polygon(pts, fill=SAND, outline=INK, width=5)
    for i in range(5):
        x = cx - w * .3 + i * w * .15; d.line([(x, cy - w * .02), (x + 14, cy - w * .08)], fill=SANDD, width=4)


def bush(c, cx, cy, r):
    d = ImageDraw.Draw(c)
    for dx, dy, k in ((-.6, .2, .7), (.6, .2, .7), (0, -.25, .85), (-.3, -.1, .8), (.35, -.05, .8)):
        rr = r * k
        d.ellipse([cx + dx * r - rr - 5, cy + dy * r - rr - 5, cx + dx * r + rr + 5, cy + dy * r + rr + 5], fill=INK)
    for dx, dy, k in ((-.6, .2, .7), (.6, .2, .7), (0, -.25, .85), (-.3, -.1, .8), (.35, -.05, .8)):
        rr = r * k
        d.ellipse([cx + dx * r - rr, cy + dy * r - rr, cx + dx * r + rr, cy + dy * r + rr], fill=hexc('#5f8a46'))
    for i in range(7):
        a = i * 0.9; d.ellipse([cx + math.cos(a) * r * .5 - 10, cy + math.sin(a) * r * .4 - 10, cx + math.cos(a) * r * .5 + 10, cy + math.sin(a) * r * .4 + 10], fill=hexc('#77a85a'))


def scroll(txt_lines, w=560):
    p = Pen(w, 380)
    p.shape([(40, 40), (w - 40, 40), (w - 40, 340), (40, 340)], hexc('#f3e3bd'), hexc('#d9c08c'), 5, 8)
    for y in (40, 340):
        p.shape(ell_pts(40, y, 26, 26, 24), hexc('#d9b77a'), hexc('#b8955a'), 4, 4)
        p.shape(ell_pts(w - 40, y, 26, 26, 24), hexc('#d9b77a'), hexc('#b8955a'), 4, 4)
    for i in range(5): p.stroke([(90, 110 + i * 48), (w - 90 - (i % 2) * 70, 110 + i * 48)], 6, hexc('#8a7350'))
    return p.img


def grass_band(c, x0, x1, y_top, y_bot, light='day', seed=2):
    d = ImageDraw.Draw(c)
    L = art.LIGHTS[light]
    rnd = random.Random(seed)
    pts = [(x0, y_bot)]
    x = x0
    while x < x1:
        pts += [(x + 18, y_top - rnd.random() * 40), (x + 36, y_top + 30)]
        x += 36
    pts += [(x1, y_bot)]
    d.polygon(pts, fill=hexc(L['fieldD']), outline=INK, width=4)


def SFX(s):
    s.thunk(s.W(0, 'nao') - 3, 180, .8)
    s.ting(s.W(1, 'romano'), .3)
    s.whoosh(s.W(1, 'invisivel') - 4, .4, .4)
    s.thunk(s.W(2, 'nenhuma') - 2, 160, .8)
    for i in range(4): s.thunk(s.W(3, 'buraco') - 10 + i * 6, 260, .35)
    for i in range(3): s.thunk(s.W(3, 'ovos') - 2 + i * 4, 320, .4)
    s.ting(s.W(4, 'virar'), .25)
    s.ting(s.W(5, 'sumiu'), .3)
    s.thunk(s.W(6, 'deita') - 2, 140, .7)
    s.patter(s.W(6, 'foge'), s.W(6, 'foge') + 45, 5, .3)
    s.thunk(s.W(6, 'setenta') - 2, 120, .9)
    s.trill(s.W(7, 'nos'), 1.0, .3)


# ---------------------------------------------------------------- cenas (f = quadro local)
OX, OF, OH_ = 520, 1960, 1150


def nestpos(x=OX, feet=OF, h=OH_):
    hx, hy = head_pos(x, feet, h, 1)
    return hx + 30, hy + 20


def s0(f):
    c = BG('day').copy()
    k = wt(0, 'nao') - 3
    out = easeOut(ramp(f, k, k + 6))
    nx, ny = nestpos()
    nest_back(c, nx, ny, 560)
    put_ost(c, OX, OF, OH_, peck=1 - out, expr='shock' if out > .5 and f < k + 30 else ('smug' if out > .5 else 'calm'), look=-.2, blink=blinkAt(f, 2) if out > .5 else 0)
    nest_berm(c, nx, ny, 560)
    put_dust(c, nx, ny - 60, 110, f - k)
    if f >= k: paste_c(c, txt('MITO!', 150, -8), 840, 640, back(ramp(f, k, k + 8)))
    z = lerp(1.45, 1.08, easeOut(ramp(f, 0, 36))) * (1 + .0006 * f)
    kk = kick(f, k + 2)
    return c, (lerp(760, 640, easeOut(ramp(f, 0, 36))), 1300 + kk * 10, z, kk), 'day'


def s1(f):
    c = BG('golden').copy()
    pk = .55
    hx, hy = head_pos(560, 1960, 1150, pk)
    put_ost(c, 560, 1960, 1150, peck=pk, look=1)
    bush(c, hx + 20, hy - 10, 190)
    r0 = wt(1, 'romano') - 3
    if f >= r0: paste_c(c, scroll([]), 640, 760, .8 * back(ramp(f, r0, r0 + 9)))
    m0 = wt(1, 'mil') - 3
    if m0 <= f < r0: paste_c(c, txt('2 MIL ANOS', 110, -5), 640, 760, back(ramp(f, m0, m0 + 8)))
    i0 = wt(1, 'invisivel') - 3
    if f >= i0: paste_c(c, txt('INVISÍVEL?', 120, 6), 700, 920, back(ramp(f, i0, i0 + 8)))
    z = lerp(1.08, 1.2, smooth(f / 160))
    return c, (640, 1250, z, lerp(0, -2, smooth(f / 160))), 'golden'


def s2(f):
    c = BG('day').copy()
    k = wt(2, 'nenhuma') - 2
    put_ost(c, 400, 1960, 1150, expr='smug' if f >= k else 'calm', look=1 if f < k else -.3, blink=blinkAt(f, 5))
    put_sci(c, 980, 1960, 950, f, 3, arms='point' if f >= k - 8 else 'clip', expr='stern', look=-1, hair='#6b4a2f')
    if f >= k: paste_c(c, txt('NUNCA!', 140, -6), 700, 600, back(ramp(f, k, k + 8)))
    kk = kick(f, k + 1)
    z = lerp(1.15, 1.06, smooth(f / 60))
    return c, (660, 1260 + kk * 10, z, kk), 'day'


def s3(f):
    c = BG('day').copy()
    b0 = wt(3, 'buraco') - 3
    n0 = wt(3, 'ninho') - 2
    e0 = wt(3, 'ovos') - 3
    nx, ny = nestpos()
    hole = easeOut(ramp(f, b0, n0))
    if hole > .02: nest_back(c, nx, ny, 560 * hole, eggs=3 if f >= e0 else 0, egg_s=back(ramp(f, e0, e0 + 8)))
    dig = f < n0
    pk = (.65 + .35 * math.sin(f * .7)) if dig else lerp(.65, .15, easeOut(ramp(f, n0, n0 + 10)))
    put_ost(c, OX, OF, OH_, peck=pk, look=1, expr='shock' if f >= e0 + 4 and f < e0 + 24 else 'calm', blink=0 if dig else blinkAt(f, 7))
    if dig and f % 6 < 3: put_dust(c, nx + 40, ny - 30, 70, f % 6)
    if dig and (f + 3) % 6 < 3: put_dust(c, nx - 60, ny - 20, 60, (f + 3) % 6)
    t = smooth(ramp(f, 0, 70))
    return c, (lerp(640, nx - 60, t), lerp(1150, ny - 200, t), lerp(1.08, 1.35, t), 0), 'day'


def s4(f):
    c = BG('day').copy()
    nx, ny = nestpos()
    v0 = wt(4, 'virar') - 3
    wob = math.sin((f - v0) * .35) * .5 if f >= v0 else 0
    nest_back(c, nx, ny, 560, eggs=3, wob=wob)
    a0 = wt(4, 'abaixa') - 3
    pk = easeOut(ramp(f, a0, a0 + 10))
    put_ost(c, OX, OF, OH_, peck=pk, look=1, blink=blinkAt(f, 9))
    va = wt(4, 'varias') - 3
    if va <= f < a0 + 30: paste_c(c, txt('VÁRIAS VEZES POR DIA', 60, -4), lerp(700, nx - 20, smooth(ramp(f, a0, a0 + 40))), lerp(760, ny - 520, smooth(ramp(f, a0, a0 + 40))), back(ramp(f, va, va + 8)))
    if f >= v0: paste_c(c, txt('VIRA, VIRA!', 90, 6), nx - 30, ny - 480, back(ramp(f, v0, v0 + 8)))
    t = smooth(ramp(f, a0, a0 + 40))
    return c, (lerp(700, nx - 20, t), lerp(1250, ny - 200, t), lerp(1.1, 1.5, t), 0), 'day'


def s5(f):
    c = BG('dusk').copy()
    x, feet, h = 700, 1420, 430
    hx, hy = head_pos(x, feet, h, 1)
    nest_back(c, hx + 12, hy + 8, 210)
    put_ost(c, x, feet, h, peck=1)
    nest_berm(c, hx + 12, hy + 8, 210)
    k = wt(5, 'sumiu') - 3
    if f >= k: paste_c(c, txt('SUMIU?', 120, -6), 640, 820, back(ramp(f, k, k + 8)))
    l0 = wt(5, 'longe') - 3
    if l0 <= f < k: paste_c(c, txt('DE LONGE...', 90, 4), 640, 820, back(ramp(f, l0, l0 + 8)))
    z = lerp(1.0, 1.22, smooth(f / 120))
    return c, (lerp(640, 680, smooth(f / 120)), lerp(1250, 1200, smooth(f / 120)), z, 0), 'dusk'


def s6(f):
    c = BG('day').copy()
    d0 = wt(6, 'deita') - 3
    g0 = wt(6, 'foge') - 3
    s0_ = wt(6, 'setenta') - 3
    if f < g0:
        down = easeOut(ramp(f, d0, d0 + 8))
        if down < .5: put_ost(c, 470, 1820, 1150, peck=down * 1.5, expr='shock', look=-.5, blink=0)
        else: put_ost(c, 470, 1820, 1150, peck=.75, lie=1, expr='side', look=1, blink=blinkAt(f, 4))
        if f >= d0: put_dust(c, 470, 1800, 140, f - d0)
        if f < d0: paste_c(c, txt('SUSTO!', 110, -6), 820, 650, back(ramp(f, wt(6, 'assusta') - 3, wt(6, 'assusta') + 5)))
        kk = kick(f, d0 + 2)
        return c, (640, 1420 + kk * 10, lerp(1.08, 1.18, smooth(f / 90)), kk), 'day'
    u = f - g0
    x = 360 + u * 17
    put_ost(c, x, 1960, 1100, run=1, phase=(u / 9) % 1, expr='shock', look=1, blink=0)
    for i in range(4): put_dust(c, x - 260 - i * 70, 1930, 70, (u + i * 4) % 14)
    if f >= s0_: paste_c(c, txt('70 KM/H', 130, -8), clamp(x + 100, 640, 1242 - 560), 700, back(ramp(f, s0_, s0_ + 8)))
    kk = kick(f, s0_ + 2)
    return c, (clamp(x + 100, 640, 1242 - 560), 1300 + kk * 10, 1.12, -2 + kk), 'day'


def s7(f):
    c = BG('golden').copy()
    k = wt(7, 'nos') - 3
    e0 = wt(7, 'enterrou') - 3
    put_ost(c, 400, 1960, 1150, expr='smug', look=.8 if f < k else -.1, blink=blinkAt(f, 1))
    put_sci(c, 960, 1960, 950, f, 3, arms='cheek' if f >= k else 'clip', expr='nervous' if f >= k else 'neutral', look=-1, hair='#6b4a2f')
    if f >= k: paste_c(c, txt('OPS!', 150, 8), 960, 720, back(ramp(f, k, k + 8)))
    z = lerp(1.06, 1.22, easeOut(ramp(f, 0, 70)))
    return c, (lerp(640, 760, smooth(ramp(f, e0, k + 10))), 1260, z, lerp(0, 2.5, smooth(ramp(f, 0, 70)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in SCENES]
