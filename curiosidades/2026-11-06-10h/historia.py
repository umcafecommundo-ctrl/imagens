"""Formato DESENHO: por que o céu é azul? (Curiosidades da IA, 06/11/2026, 10h). Categoria: CIÊNCIA DO DIA A DIA.
Fatos: EarthDate (Univ. do Texas, "Blue Sky, Blue Sunset"): a luz do sol tem todas as cores e parece branca; o ar
(nitrogênio e oxigênio) espalha muito mais as cores curtas (azul) que o vermelho; ao entardecer a luz atravessa muito mais
atmosfera, o azul se espalha no caminho e sobram laranja e vermelho; em Marte o céu de dia é avermelhado (poeira) e o
pôr do sol é azul (fotos dos jipes Curiosity, Spirit e Opportunity). NASA Space Place "Why is the sky blue?" (mesma explicação)."""
from kit import *
import kit

LINES = [
    "A luz do sol é branquinha. Então por que o céu é azul?",
    "Porque essa luz branca é, na verdade, todas as cores misturadas, viajando juntas até a Terra.",
    "Quando chega aqui, ela esbarra em bilhões de partículas minúsculas do ar.",
    "E o azul é o mais bagunceiro: ele ricocheteia pra todo lado, muito mais que o vermelho.",
    "Você vê, pra qualquer lugar que você olha no céu, tem luz azul quicando na sua direção.",
    "No fim da tarde, a luz atravessa muito mais ar. O azul se perde no caminho, e sobra o laranja e o vermelho.",
    "E em Marte é o contrário: o céu é avermelhado... e o pôr do sol é azul.",
]
CAPTXT = [
    "A luz do sol é branquinha.|Então por que o céu é azul?",
    "Porque essa luz branca é, na verdade, todas as cores misturadas,|viajando juntas até a Terra.",
    "Quando chega aqui, ela esbarra em bilhões de partículas minúsculas do ar.",
    "E o azul é o mais bagunceiro:|ele ricocheteia pra todo lado, muito mais que o vermelho.",
    "Você vê, pra qualquer lugar que você olha no céu,|tem luz azul quicando na sua direção.",
    "No fim da tarde, a luz atravessa muito mais ar.|O azul se perde no caminho, e sobra o laranja e o vermelho.",
    "E em Marte é o contrário: o céu é avermelhado...|e o pôr do sol é azul.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [5, 6]
CHECK = [(0, 'azul', 4), (1, 'cores', 6), (1, 'terra', 4), (2, 'bilhoes', 6), (3, 'ricocheteia', 6), (3, 'vermelho', 4),
         (4, 'direcao', 4), (5, 'perde', 6), (5, 'vermelho', 4), (6, 'avermelhado', 4), (6, 'azul', 8)]

CORES = [hexc('#e8423a'), hexc('#f5922a'), hexc('#ffd84a'), hexc('#4cc36a'), hexc('#2f7de1'), hexc('#8e5bd6')]
AZUL = 4


# ------------------------------------------------------------------ personagens e objetos novos
def cor(col=(255, 255, 255), expr='calm', blink=0, look=0.6):
    """bolinha de luz com carinha (300x300), olhando para a direita."""
    p = Pen(300, 300)
    p.shape(ell_pts(150, 160, 120, 112, 48, 0, .06, 2.2), col, mul(col, .78), 6, 18)
    p.dot(112, 118, 18, mul(col, 1.25) if max(col) < 220 else (255, 255, 255))  # brilho
    for dx in (-34, 34):
        ex, ey = 170 + dx, 150
        if blink > .6:
            p.stroke([(ex - 18, ey), (ex + 18, ey)], 6)
        elif expr == 'dizzy':
            p.dot(ex, ey, 24, (255, 255, 255), 5)
            p.arc(ex, ey, 12, 12, 0, 300, 5)
        else:
            r = 28 if expr == 'shock' else 24
            p.dot(ex, ey, r, (255, 255, 255), 5)
            p.dot(ex + look * 9, ey + 2, 11 if expr != 'shock' else 8, INK)
            p.dot(ex + look * 9 - 3, ey - 3, 3.5, (255, 255, 255))
    if expr in ('grin', 'dizzy'):
        p.poly([(140, 200), (210, 200), (196, 232), (154, 232)], hexc('#7a2e2e'), 4)
    elif expr == 'shock':
        p.dot(175, 218, 16, hexc('#7a2e2e'), 4)
    else:
        p.arc(175, 196, 26, 16, 20, 160, 6)
    return p.img


def put_cor(c, x, y, size, k, expr='calm', look=.6, f=0, seed=0, flip=False):
    """bolinha de cor k (0..5, ou -1 = branca) centrada em (x, y)."""
    col = (255, 252, 240) if k < 0 else CORES[k]
    b = 1 if blinkAt(f, seed + 3) > .6 else 0
    put_sprite(c, 'cor', x, y + size / 2, size, 1.0, flip, None, col=col, expr=expr, blink=b, look=round(look * 2) / 2)


@lru_cache(maxsize=4)
def sol_img(size=420, warm=0):
    p = Pen(500, 500)
    col = hexc('#fff6c8') if not warm else hexc('#ffb347')
    for i in range(12):
        a = i * math.pi / 6
        p.line([(250 + 150 * math.cos(a), 250 + 150 * math.sin(a)), (250 + 215 * math.cos(a), 250 + 215 * math.sin(a))], hexc('#ffd84a'), 14, 4)
    p.shape(ell_pts(250, 250, 130, 130, 56), col, hexc('#ffd25e') if not warm else hexc('#e07a2a'), 6, 18)
    return p.img.resize((size, size), Image.LANCZOS)


@lru_cache(maxsize=2)
def space_bg():
    W, H = BW, BH
    y = np.linspace(0, 1, H)[:, None, None]
    a = np.array(hexc('#0b1030')) * (1 - y) + np.array(hexc('#1d2a66')) * y
    im = Image.fromarray(np.broadcast_to(a, (H, W, 3)).astype(np.uint8)).convert('RGBA')
    d = ImageDraw.Draw(im); rnd = random.Random(7)
    for i in range(160):
        x, yy, r = rnd.randint(0, W), rnd.randint(0, H), rnd.choice((2, 2, 3, 4))
        d.ellipse([x - r, yy - r, x + r, yy + r], fill=(255, 255, 230, 255))
    return im


@lru_cache(maxsize=2)
def terra_img(size=520):
    p = Pen(400, 400)
    p.shape(ell_pts(200, 200, 170, 170, 64), hexc('#3a86e0'), hexc('#2458a8'), 6, 22)
    for cx, cy, rx, ry, rot in ((160, 150, 62, 48, .5), (275, 265, 58, 44, -.4), (130, 270, 30, 22, .2)):
        p.shape(ell_pts(cx, cy, rx, ry, 32, rot, .25), hexc('#5cc46f'), hexc('#3c9a50'), 4, 8)
    return p.img.resize((size, size), Image.LANCZOS)


@lru_cache(maxsize=2)
def ar_img():
    """bilhões de partículas do ar (bolinhas cinza-claro), camada 1242x1300."""
    p = Pen(1242, 1300); rnd = random.Random(11)
    for i in range(70):
        p.dot(rnd.randint(30, 1210), rnd.randint(30, 1270), rnd.choice((9, 11, 13)), hexc('#e9eef7'), 3)
    return p.img.resize((1242, 1300), Image.LANCZOS)


@lru_cache(maxsize=8)
def marte_bg(glow=0.0):
    W, H, hz = BW, BH, 1300
    y = np.linspace(0, 1, hz)[:, None, None]
    top, hor = np.array(hexc('#9a5a3c')), np.array(hexc('#e7b27e'))
    a = top * (1 - y) + hor * y
    im = Image.new('RGBA', (W, H)); im.paste(Image.fromarray(np.broadcast_to(a, (hz, W, 3)).astype(np.uint8)), (0, 0))
    if glow > 0:  # brilho azul em volta do sol baixo
        g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
        for r, al in ((520, .25), (380, .45), (250, .7), (150, .9)):
            d.ellipse([620 - r, 1180 - r * .8, 620 + r, 1180 + r * .8], fill=(110, 170, 235, int(255 * al * glow)))
        im.alpha_composite(g)
    p = Pen(W, H - hz + 40)
    p.shape([(-20, 40), (W + 20, 20), (W + 20, H - hz + 40), (-20, H - hz + 40)], hexc('#b65a34'), hexc('#8a3f22'), 5, 20)
    rnd = random.Random(4)
    for i in range(26):
        x, yy, r = rnd.randint(0, W), rnd.randint(120, H - hz), rnd.randint(12, 46)
        p.shape(ell_pts(x, yy, r * 1.4, r * .8, 24), hexc('#8c4a2e'), hexc('#6a341f'), 4, 6)
    ground = p.img.resize((W, H - hz + 40), Image.LANCZOS)
    im.alpha_composite(ground, (0, hz - 40))
    d = ImageDraw.Draw(im)
    d.ellipse([620 - 46, 1180 - 46, 620 + 46, 1180 + 46], fill=(255, 250, 235, 255))  # sol pequeno e baixo
    im.alpha_composite(ground.crop((0, 0, W, 140)), (0, hz - 40))  # sol meio escondido no horizonte
    return im


def rover(expr='calm', blink=0, look=0.5, wheel=0.0):
    """jipe-robô de lado (700x560), 'olho' de câmera no mastro."""
    p = Pen(700, 560)
    G, Gd = hexc('#e6e1d6'), hexc('#b9b2a2')
    p.line([(200, 380), (350, 330), (500, 380)], hexc('#8a8a8a'), 12, 4)
    for wx in (150, 350, 550):
        p.dot(wx, 470, 62, hexc('#3a3236'), 5); p.dot(wx, 470, 26, hexc('#a7a7a0'), 4)
        for k in range(3):
            a = wheel + k * math.pi / 1.5
            p.stroke([(wx, 470), (wx + 50 * math.cos(a), 470 + 50 * math.sin(a))], 5)
    p.shape([(110, 260), (590, 260), (610, 360), (90, 360)], G, Gd, 6, 14)
    p.shape([(170, 230), (560, 230), (560, 262), (170, 262)], hexc('#3b5ea8'), hexc('#2a4580'), 4, 6)
    p.line([(520, 232), (520, 120)], hexc('#8a8a8a'), 14, 4)
    p.shape([(450, 40), (610, 40), (620, 140), (440, 140)], G, Gd, 5, 10)
    ex, ey = 545, 90
    r = 40 if expr == 'shock' else 34
    p.dot(ex, ey, r, (255, 255, 255), 5)
    if blink > .6: p.stroke([(ex - 30, ey), (ex + 30, ey)], 7)
    else:
        p.dot(ex + look * 12, ey + 2, 14, INK); p.dot(ex + look * 12 - 4, ey - 4, 4, (255, 255, 255))
    return p.img


def put_rover(c, x, feet, h, f, **kw):
    kw['blink'] = 1 if blinkAt(f, 5) > .6 else 0
    put_sprite(c, 'rover', x, feet, h, 700 / 560, False, {'wheel': 4}, **kw)


def SFX(s):
    s.ting(s.W(0, 'branquinha'), .3)
    s.thunk(s.W(0, 'azul') - 2, 160, .8)
    for i in range(6): s.ting(s.W(1, 'cores') + i * 3, .18)
    s.whoosh(s.W(1, 'viajando') - 4, .6, .4)
    for i in range(6): s.thunk(s.W(2, 'bilhoes') - 2 + i * 3, 300, .35)
    for i in range(5): s.thunk(s.W(3, 'ricocheteia') + i * 7, 260, .45)
    s.whoosh(s.W(3, 'vermelho') - 4, .4, .4)
    s.ting(s.W(4, 'direcao'), .35)
    s.whoosh(s.W(5, 'perde') - 4, .5, .4)
    s.thunk(s.W(5, 'vermelho') - 2, 150, .6)
    s.thunk(s.W(6, 'contrario') - 2, 140, .7)
    s.trill(s.W(6, 'azul'), 1.0, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = BG('day').copy()
    paste_c(c, sol_img(360), 880, 520, 1 + .03 * math.sin(f * .15))
    b = wt(0, 'branquinha') - 3
    a = wt(0, 'azul') - 3
    if b <= f < a: paste_c(c, txt('BRANCA!', 100, -6), 820, 800, back(ramp(f, b, b + 8)))
    put_sci(c, 520, 2080, 1150, f, 2, arms='point' if f < a else 'cheek', expr='neutral' if f < a else 'shock', look=1, glasses=False,
            hair='#2b2b2b', skin=1)
    if f >= a: paste_c(c, txt('AZUL?!', 130, 6), 860, 860, back(ramp(f, a, a + 8)))
    kk = kick(f, a + 2)
    t = easeOut(ramp(f, 0, 50))
    return c, (lerp(850, 660, t), lerp(700, 1250, t) + kk * 10, lerp(1.6, 1.08, t), kk), 'day'


def s1(f):
    c = space_bg().copy()
    paste_c(c, sol_img(560), 120, 1050)
    k = wt(1, 'cores') - 3
    tr = wt(1, 'terra') - 3
    x0 = min(520, 330 + f * 3)
    if f < k:
        put_cor(c, x0, 1050, 260, -1, 'calm', 1, f, 1)
    else:
        sp = easeOut(ramp(f, k, k + 10))
        for i in range(6):
            yy = 1050 + (i - 2.5) * 150 * sp + 14 * math.sin(f * .3 + i)
            put_cor(c, x0 + 40 * math.sin(i * 1.3) * sp, yy, lerp(260, 140, sp), i, 'grin', 1, f, i)
        if f < tr: paste_c(c, txt('TODAS AS CORES!', 80, -5), 621, 560, back(ramp(f, k, k + 8)))
    if f >= tr:
        paste_c(c, terra_img(340), 920, 1050, back(ramp(f, tr, tr + 10)))
        paste_c(c, txt('TERRA', 90, 4), 880, 800, back(ramp(f, tr + 4, tr + 12)))
    return c, (621, 1080, 1.05, 0), 'day'


def s2(f):
    c = BG('day').copy()
    b = wt(2, 'bilhoes') - 3
    if f >= b:
        layer = ar_img()
        s = back(ramp(f, b, b + 10))
        if s < 1: layer = layer.resize((1242, max(1, int(1300 * s))))
        c.alpha_composite(layer, (0, 80))
        paste_c(c, txt('BILHÕES!', 120, -6), 640, 420, back(ramp(f, b, b + 8)))
    for i in range(6):
        u = easeOut(ramp(f, i * 2, b))
        x = lerp(-200, 380, u) + i * 90
        y = lerp(200, 760, u) + (i % 2) * 90
        if b <= f:  # esbarrou: todos tremem
            x += 6 * math.sin(f * 2 + i); y += 6 * math.cos(f * 2 + i)
        put_cor(c, x, y, 150, i, 'shock' if f >= b else 'grin', 1, f, i)
    m = wt(2, 'minusculas') - 3
    kk = kick(f, m)
    z = lerp(1.3, 1.4, smooth(f / 100))
    return c, (640, 780 + kk * 10, z, kk), 'day'


def s3(f):
    c = BG('day').copy(); c.alpha_composite(ar_img(), (0, 80))
    r0 = wt(3, 'ricocheteia') - 3
    v0 = wt(3, 'vermelho') - 6
    # vermelho segue reto, calmo
    xr = 330 + max(0, f - v0) * 22
    put_cor(c, xr, 1150, 170, 0, 'calm', 1, f, 1)
    # azul quica pra todo lado
    pts = [(420, 820), (900, 420), (960, 1050), (330, 560), (720, 1200), (940, 360), (360, 1000), (880, 760)]
    if f < r0:
        bx, by = 420, 820; ex = 'grin'
    else:
        t = (f - r0) / 7
        i = int(t) % (len(pts) - 1); u = t - int(t)
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        bx, by = lerp(x1, x2, u), lerp(y1, y2, u)
        ex = 'dizzy' if (f - r0) % 28 < 14 else 'grin'
        if u < .25: paste_c(c, txt('TOIN!', 70, 8 - 16 * (i % 2)), x1, y1 - 120, 1 - u * 3)
    put_cor(c, bx, by, 190, AZUL, ex, -1 if f % 14 < 7 else 1, f, 2)
    a = wt(3, 'azul') - 3
    if a <= f < r0 + 6: paste_c(c, txt('BAGUNCEIRO!', 90, -6), 640, 260, back(ramp(f, a, a + 8)))
    z = 1.28 + .0006 * f
    return c, (640, 800, z, 2 * math.sin(f * .04)), 'day'


def s4(f):
    c = BG('day').copy()
    d0 = wt(4, 'direcao') - 3
    put_sci(c, 640, 2080, 1100, f, 2, arms='hang' if f < d0 else 'up', expr='neutral' if f < d0 else 'grin', look=0, glasses=False,
            hair='#2b2b2b', skin=1)
    rnd = random.Random(3)
    eye = (640, 1330)
    for i in range(14):
        a = math.pi * (1.05 + rnd.random() * .9)
        R = 1100
        sx, sy = eye[0] + R * math.cos(a), eye[1] + R * math.sin(a) * .9
        per = 40 + rnd.randint(0, 20)
        u = ((f + rnd.randint(0, per)) % per) / per
        x, y = lerp(sx, eye[0], u), lerp(sy, eye[1] - 150, u)
        if u < .85: put_cor(c, x, y, 120, AZUL, 'grin', 1 if x < 640 else -1, f, i)
    if f >= d0: paste_c(c, txt('TUDO AZUL!', 120, 5), 640, 560, back(ramp(f, d0, d0 + 8)))
    z = lerp(1.0, 1.15, smooth(f / 150))
    return c, (640, 1180, z, 0), 'dusk'


def s5(f):
    c = BG('golden').copy()
    sx, sy = 894, 900
    p0 = wt(5, 'perde') - 3
    v0 = wt(5, 'laranja') - 3
    put_sci(c, 330, 2080, 1000, f, 2, arms='hang', expr='neutral' if f < v0 else 'grin', look=1, glasses=False, hair='#2b2b2b', skin=1)
    # caminho longo do sol até a pessoa
    D = max(30, v0 + 6)
    pos = lambda i, ff: (lerp(980, 470, clamp((ff - i * 13) / D)), lerp(930, 1380, clamp((ff - i * 13) / D)))
    for i in range(6):
        if i >= 2 and f >= p0 + (i - 2) * 3:  # amarelo, verde, azul e violeta se perdem no caminho
            g = f - p0 - (i - 2) * 3
            x, y = pos(i, p0 + (i - 2) * 3)
            y += g * g * 1.2; x += g * 2
            if y > 2300: continue
            put_cor(c, x, y, 130, i, 'dizzy', -1, f, i, flip=True)
        else:
            x, y = pos(i, f)
            if f < i * 13: continue
            put_cor(c, x, y + 14 * math.sin(f * .25 + i), 150, i, 'grin' if f >= v0 else 'calm', -1, f, i, flip=True)
    a0 = wt(5, 'atravessa') - 3
    if a0 <= f < p0: paste_c(c, txt('MUITO MAIS AR', 84, -5), 640, 520, back(ramp(f, a0, a0 + 8)))
    if f >= p0 and f < v0: paste_c(c, txt('TCHAU, AZUL!', 90, 5), 640, 520, back(ramp(f, p0, p0 + 8)))
    if f >= v0:
        paste_c(c, txt('LARANJA E', 90, -4), 640, 450, back(ramp(f, v0, v0 + 8)))
        paste_c(c, txt('VERMELHO!', 110, -4), 640, 580, back(ramp(f, v0 + 3, v0 + 11)))
    z = lerp(1.0, 1.12, smooth(f / 160))
    return c, (620, 1180, z, 0), 'golden'


def s6(f):
    a0 = wt(6, 'azul') - 6
    g = smooth(ramp(f, a0, a0 + 16))
    c = marte_bg(round(g * 8) / 8).copy()
    m0 = wt(6, 'marte') - 3
    if m0 <= f < a0: paste_c(c, txt('MARTE', 120, -5), 640, 500, back(ramp(f, m0, m0 + 8)))
    av = wt(6, 'avermelhado') - 3
    put_rover(c, 420 + 0.4 * f, 1720, 520, f, expr='shock' if f >= a0 else 'calm', look=1, wheel=f * .08)
    if f >= a0: paste_c(c, txt('AZUL?!', 140, 6), 640, 760, back(ramp(f, a0, a0 + 8)))
    t = smooth(ramp(f, a0 - 10, a0 + 30))
    return c, (lerp(560, 620, t), lerp(1350, 1300, t), lerp(1.05, 1.35, t), lerp(0, -2.5, t)), 'day' if f < a0 else 'dusk'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
