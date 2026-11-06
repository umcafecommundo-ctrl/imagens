"""TESTE Um Café com o Mundo em formato desenho — CURIOSIDADE (05/11/2026).
Fatos: estudo da Monash University + Zoological Society of London, Proceedings of the Royal Society B,
divulgado em 05/11/2026 (phys.org, AZO Life Sciences, Scimex/Monash): 141 espécies de aves e mamíferos
que caíram para menos de 50 indivíduos na natureza desde 1950; das 51 com ação direta de conservação
(controle de predadores invasores, restauração de habitat, criação em cativeiro, translocação) 61%
voltaram a 100+; sem ajuda direta 37% foram extintas e só 2% chegaram a 100+.
Galinha-d'água de Lord Howe (Lord Howe woodhen), Austrália: 23 aves no fim dos anos 1970 -> mais de 1.600 hoje."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'  # sem @: o mesmo vídeo vai para Instagram, Facebook e TikTok (@ diferentes)
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Só restavam vinte e três aves dessa espécie no mundo inteiro.",
    "Era o fim dos anos setenta, numa ilha da Austrália, e quase todo mundo achava que o fim era certo.",
    "Um estudo divulgado nesta quinta olhou cento e quarenta e uma espécies de aves e mamíferos que caíram para menos de cinquenta animais.",
    "Sem ajuda, trinta e sete por cento sumiram de vez. Só dois por cento voltaram a passar de cem.",
    "Mas, com ajuda de verdade, controle de predadores, criação em cativeiro e mudança de lugar, sessenta e um por cento se recuperaram.",
    "E aquelas vinte e três aves? Hoje, são mais de mil e seiscentas.",
]
CAPTXT = [
    "Só restavam 23 aves dessa espécie no mundo inteiro.",
    "Era o fim dos anos 70, numa ilha da Austrália,|e quase todo mundo achava que o fim era certo.",
    "Um estudo divulgado nesta quinta olhou 141 espécies|de aves e mamíferos que caíram para menos de 50 animais.",
    "Sem ajuda, 37% sumiram de vez.|Só 2% voltaram a passar de 100.",
    "Mas, com ajuda de verdade,|controle de predadores, criação em cativeiro e mudança de lugar,|61% se recuperaram.",
    "E aquelas 23 aves? Hoje, são mais de 1.600.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'vinte', 6), (1, 'certo', 2), (2, 'cinquenta', 4), (3, 'dois', 6), (4, 'predadores', 4), (4, 'sessenta', 8), (5, 'mil', 8)]


# ------------------------------------------------------------------ personagens novos
WH = dict(body=hexc('#7a5a3a'), bodyD=hexc('#56402a'), wing=hexc('#5f4630'), streak=hexc('#a07a52'),
          head=hexc('#6e5236'), beak=hexc('#c9a79a'), leg=hexc('#d39a8a'))


def woodhen(blink=0, expr='calm', look=.3, peck=0.0, step=0.0, seed=1, scared=0.0):
    """galinha-d'água de Lord Howe: ave gordinha marrom que não voa, bico comprido, olho vermelho. 600x800, pés y~780."""
    p = Pen(600, 800)
    bc = (300, 560 - scared * 30)
    for k, dx in ((0, -22), (1, 24)):
        lift = max(0, math.sin(step * 2 * math.pi + k * math.pi)) * 34 if step else 0
        top = (bc[0] + dx, bc[1] + 90); ft = (bc[0] + dx + lift * .5, 768 - lift)
        col = mul(WH['leg'], .82) if k == 0 else WH['leg']
        p.line([top, ((top[0] + ft[0]) / 2 - 6, (top[1] + ft[1]) / 2), ft], col, 13, 4)
        for tx, ty in ((40, 4), (28, -4), (-18, 2)): p.line([ft, (ft[0] + tx, ft[1] + ty)], col, 7, 3)
    # tail tuft
    p.shape([(bc[0] - 160, bc[1] - 50), (bc[0] - 225, bc[1] - 100), (bc[0] - 210, bc[1] - 20), (bc[0] - 150, bc[1] + 20)], WH['bodyD'], None, 5)
    body = ell_pts(bc[0], bc[1], 175, 125, 64, -.05 - peck * .15, .12)
    p.shape(body, WH['body'], WH['bodyD'], 6, 22)
    rnd = random.Random(seed)
    for i in range(14):
        x = bc[0] - 120 + rnd.random() * 220; y = bc[1] - 60 + rnd.random() * 110
        p.stroke([(x, y), (x - 20, y + 16)], 4, WH['streak'] if i % 2 else WH['bodyD'])
    wing = ell_pts(bc[0] - 20, bc[1] + 4, 100, 60, 40, -.2)
    p.shape(wing, WH['wing'], mul(WH['wing'], .75), 5, 10)
    for i in range(4): p.stroke([(bc[0] - 80 + i * 30, bc[1] + 20), (bc[0] - 94 + i * 30, bc[1] + 50)], 4, mul(WH['wing'], .6))
    # neck + head
    hx = bc[0] + 150 + peck * 60; hy = bc[1] - 150 + peck * 170 - scared * 20
    ha = peck * .9 - scared * .2
    p.shape(curve((bc[0] + 70, bc[1] - 70), (hx - 40, hy + 30), (hx - 20, hy), 8) + curve((hx + 30, hy + 20), (hx + 40, hy + 90), (bc[0] + 160, bc[1] - 10), 8), WH['head'], mul(WH['head'], .8), 6, 10)
    H = lambda dx, dy: (hx + dx * math.cos(ha) - dy * math.sin(ha), hy + dx * math.sin(ha) + dy * math.cos(ha))
    p.shape(ell_pts(hx, hy, 52, 46, 36, ha), WH['head'], mul(WH['head'], .8), 6, 10)
    # long slightly down-curved beak
    beak = curve(H(36, -12), H(90, -6), H(128, 20), 8) + curve(H(124, 26), H(86, 8), H(36, 12), 8)
    p.poly(beak, WH['beak'], 5)
    ec = H(10, -10); er = 22 if expr == 'shock' else 17
    p.dot(ec[0], ec[1], er, (255, 255, 255), 4)
    p.dot(ec[0], ec[1], er - 6, hexc('#d8382f'))  # red iris
    lid = .5 if expr in ('side', 'sad') else .42 if expr == 'smug' else 0
    L = max(lid, blink)
    if L < .75:
        lk = max(-1, min(1, look))
        p.dot(ec[0] + lk * (er - 9), ec[1] + 1, 5 if expr == 'shock' else 6.5, INK)
        p.dot(ec[0] + lk * (er - 9) - 2, ec[1] - 2, 2.2, (255, 255, 255))
    if L > .02:
        top = ec[1] - er; yb = top + 2 * er * L
        p.poly([(ec[0] - er - 1, top - 2), (ec[0] + er + 1, top - 2), (ec[0] + er + 1, yb), (ec[0] - er - 1, yb)], WH['head'])
        p.stroke([(ec[0] - er, yb), (ec[0] + er, yb)], 4)
    if expr in ('smug', 'side'): p.stroke([H(-8, -34), H(28, -28)], 5)
    if expr == 'sad': p.stroke([H(-10, -26), H(26, -34)], 5)
    if expr == 'shock': p.arc(ec[0], ec[1] - 30, 14, 5, 200, 340, 4)
    return p.img


def rat(phase=0.0, run=0.0, expr='smug', blink=0):
    """rato invasor (vilão fofinho), de lado olhando p/ direita. 600x400, pés y~385."""
    p = Pen(600, 400)
    two = 2 * math.pi; bob = run * 10 * abs(math.sin(two * phase))
    bc = (290, 270 - bob)
    tail = curve((bc[0] - 130, bc[1] + 20), (bc[0] - 260, bc[1] + 60 + 30 * math.sin(two * phase)), (bc[0] - 280, bc[1] - 60), 12)
    p.line(tail, hexc('#d9a0a0'), 10, 4)
    for k in (0, 1):
        ph = phase + k * .5
        fx = bc[0] + (-70 if k else 60) + run * 40 * math.cos(two * ph); fy = 382 - run * 26 * max(0, math.sin(two * ph))
        p.line([(fx - 5, bc[1] + 60), (fx, fy)], hexc('#d9a0a0'), 10, 4)
    p.shape(ell_pts(bc[0], bc[1], 150, 95, 56, 0, .1), hexc('#8d8c94'), hexc('#66656d'), 6, 18)
    hx, hy = bc[0] + 140, bc[1] - 30
    p.shape([(hx - 50, hy - 50), (hx + 90, hy + 10), (hx - 40, hy + 55)], hexc('#8d8c94'), hexc('#66656d'), 6, 10)
    p.dot(hx + 92, hy + 10, 12, hexc('#e58aa0'), 4)
    p.dot(hx - 30, hy - 60, 34, hexc('#9d9ca4'), 5); p.dot(hx - 30, hy - 60, 18, hexc('#e8b0bd'))
    ex, ey = hx + 10, hy - 8
    p.dot(ex, ey, 15, (255, 255, 255), 4)
    if blink < .6: p.dot(ex + 6, ey + 1, 6, INK)
    if expr == 'smug': p.poly([(ex - 16, ey - 16), (ex + 16, ey - 16), (ex + 16, ey - 2), (ex - 16, ey - 2)], hexc('#8d8c94')); p.stroke([(ex - 15, ey - 2), (ex + 15, ey - 2)], 4)
    if expr == 'shock': p.arc(ex, ey - 26, 12, 5, 200, 340, 4)
    for s in (-1, 1): p.stroke([(hx + 70, hy + 14), (hx + 120, hy + 14 + s * 16)], 3)
    return p.img


def crate(open_=0.0):
    p = Pen(500, 360)
    p.shape([(30, 90), (470, 90), (470, 340), (30, 340)], hexc('#b98b59'), hexc('#8e6438'), 6, 12)
    for x in (120, 210, 300, 390): p.stroke([(x, 100), (x, 330)], 4, hexc('#7a5530'))
    p.poly([(60, 140), (440, 140), (440, 170), (60, 170)], hexc('#f3f3ee'), 3)
    lid = [(30, 90 - open_ * 70), (470, 90 - open_ * 10), (470, 60 - open_ * 10), (30, 60 - open_ * 70)]
    p.shape(lid, hexc('#c99a66'), hexc('#9b6f3f'), 5, 6)
    return p.img


@lru_cache(maxsize=4)
def ilha(light='day'):
    """céu + mar + ilha com 2 montanhas (Lord Howe), chão de grama na frente."""
    import numpy as np
    from PIL import ImageDraw
    S = 2; W, H = BW * S, BH * S
    L = art.LIGHTS[light]
    sky_top, hor = np.array(hexc(L['top'])), np.array(hexc(L['hor']))
    hz = 1040 * S
    y = np.linspace(0, 1, H)[:, None]; t = np.clip(y / (hz / H), 0, 1) ** 1.8
    arr = np.broadcast_to((sky_top * (1 - t) + hor * t)[:, None, :], (H, W, 3)).astype(np.uint8).copy()
    img = Image.fromarray(arr); d = ImageDraw.Draw(img)
    rnd = random.Random(4)
    for i in range(6):
        cx = rnd.random() * W; cy = (150 + rnd.random() * 450) * S
        for j in range(5):
            rx = (60 + rnd.random() * 60) * S
            d.ellipse([cx + (j - 2) * 65 * S - rx, cy - rx * .6, cx + (j - 2) * 65 * S + rx, cy + rx * .5], fill=(255, 255, 255) if light == 'day' else mul(hexc(L['hor']), 1.08))
    sea = hexc('#3f8fc4') if light == 'day' else mul(hexc('#3f8fc4'), .75)
    d.rectangle([0, hz, W, H], fill=sea)
    for i in range(40):
        x = rnd.random() * W; yy = hz + rnd.random() * 300 * S
        d.line([(x, yy), (x + 40 * S, yy)], fill=mul(sea, 1.25), width=4 * S)
    # mountains (far)
    mt = mul(hexc('#5f8a5a'), .9 if light == 'day' else .7)
    for cx, w, h in ((380, 260, 520), (650, 220, 430)):
        d.polygon([((cx - w) * S, hz + 40 * S), ((cx - 40) * S, (hz / S - h) * S), ((cx + 30) * S, (hz / S - h + 10) * S), ((cx + w) * S, hz + 40 * S)], fill=mt, outline=INK, width=4 * S)
    # island ground (front)
    g = hexc('#7fb05a') if light == 'day' else mul(hexc('#7fb05a'), .75)
    d.ellipse([-400 * S, 1180 * S, (BW + 400) * S, 3200 * S], fill=g, outline=INK, width=5 * S)
    for i in range(int(BW * 2.5)):
        x = rnd.random() * W; yy = (1300 + rnd.random() ** .8 * 900) * S
        dep = (yy / S - 1300) / 900
        d.line([(x, yy), (x + 4 * S, yy - (8 + 20 * dep) * S)], fill=mul(g, .8 + rnd.random() * .3), width=int((1 + 2 * dep) * S))
    for tx in (90, 1150):
        d.rectangle([(tx - 12) * S, 1060 * S, (tx + 12) * S, 1240 * S], fill=hexc('#6b4a2f'), outline=INK, width=3 * S)
        for k in range(5):
            ox, oy, r = (rnd.random() - .5) * 140, -40 - rnd.random() * 80, 50 + rnd.random() * 20
            d.ellipse([(tx + ox - r) * S, (1060 + oy - r * .8) * S, (tx + ox + r) * S, (1060 + oy + r * .8) * S], fill=mul(g, .75), outline=INK, width=3 * S)
    return img.resize((BW, BH), Image.LANCZOS).convert('RGBA')


def put_wh(c, x, feet, h, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    put_sprite(c, 'woodhen', x, feet, h, .75, flip, {'peck': 6, 'step': 8, 'scared': 4}, **kw)


def put_rat(c, x, feet, h, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    put_sprite(c, 'rat', x, feet, h, 1.5, flip, {'phase': 16, 'run': 2}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = ilha('day').copy()
    v = wt(0, 'vinte') - 3
    pos = [(230, 1700, 420, False, 1), (1010, 1690, 400, True, 3), (600, 1860, 820, False, 2)]
    for x, y, h, fl, sd in pos:
        put_wh(c, x, y, h, fl, blink=blinkAt(f, sd), look=.3 if not fl else -.3, peck=max(0, math.sin((f + sd * 20) * .12)) ** 2 * (sd != 2), seed=sd,
               expr='sad' if f > wt(0, 'inteiro') else 'calm')
    num(c, '23', 640, 820, f, v, 230)
    if f >= wt(0, 'mundo') - 2: paste_c(c, txt('NO MUNDO TODO', 70, -4), 640, 980, back(ramp(f, wt(0, 'mundo') - 2, wt(0, 'mundo') + 6)))
    z = lerp(1.4, 1.08, easeOut(ramp(f, 0, 45))) * (1 + .0005 * f)
    k = kick(f, v)
    return c, (640, 1420 + k * 10, z, k), 'day'


def s1(f):
    c = ilha('day').copy()
    num(c, 'ANOS 70', 640, 420, f, wt(1, 'anos') - 3, 110)
    r0 = wt(1, 'quase') - 4
    for i, (x, y) in enumerate(((200, 1640), (1060, 1620), (880, 1780))):
        s = back(ramp(f, r0 + i * 4, r0 + i * 4 + 8))
        if s > .05:
            put_rat(c, x, y, 260 * s, flip=x > 640, expr='smug', blink=blinkAt(f, 20 + i))
            put_dust(c, x, y - 20, 70, f - r0 - i * 4)
    sc = f >= wt(1, 'certo') - 3
    for x, y, h, fl, sd in ((430, 1760, 600, False, 1), (700, 1800, 640, True, 2)):
        put_wh(c, x, y, h, fl, expr='shock' if sc else 'calm', scared=1 if sc else 0, look=-.5 if not fl else .5, blink=0 if sc else blinkAt(f, sd), seed=sd)
    t = smooth(ramp(f, 0, 60))
    k = kick(f, wt(1, 'certo') - 3, .8)
    return c, (640 + 20 * math.sin(f * .03), lerp(900, 1430, t) + k * 10, lerp(1.25, 1.1, t) * (1 + .0008 * f), k), 'day'


def s2(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    put_sci(c, 360, 1640, 900, f, 1, arms='clip', bun=True, skin=1, expr='neutral' if f < wt(2, 'cinquenta') else 'shock', look=1)
    num(c, '141 ESPÉCIES', 800, 520, f, wt(2, 'cento') - 3, 96, -4)
    num(c, 'AVES + MAMÍFEROS', 800, 680, f, wt(2, 'aves') - 3, 64, -4)
    num(c, 'MENOS DE 50!', 800, 860, f, wt(2, 'cinquenta') - 3, 96, 5)
    if f >= wt(2, 'aves') - 3:
        put_wh(c, 900, 1500, 380, True, look=-.6, blink=blinkAt(f, 7), seed=7)
    return c, (640, 1150, lerp(1.25, 1.12, smooth(f / 120)), 0), 'day'


def s3(f):
    c = ilha('golden').copy()
    a = wt(3, 'sumiram') - 3
    b = wt(3, 'dois') - 2
    xs = [140, 340, 540, 740, 940, 1120]
    for i, x in enumerate(xs):
        gone = i in (1, 3) and f >= a + i * 2
        if gone:
            put_dust(c, x, 1600, 120, f - a - i * 2, 18)
            continue
        last = i == 5
        put_wh(c, x, 1740, 470, i % 2 == 1, expr='sad', look=0, blink=blinkAt(f, i + 1), seed=i + 1, scared=.5 if last and f >= b else 0)
    num(c, '37%', 640, 760, f, wt(3, 'trinta') - 3, 200)
    num(c, 'SÓ 2%', 640, 980, f, b, 130, 4)
    return c, (640, 1430, 1.1 + .0006 * f, 0), 'golden'


def s4(f):
    c = ilha('day').copy()
    p0 = wt(4, 'predadores') - 3
    rx = 700 - max(0, f - p0) * 26
    put_rat(c, rx, 1760, 260, flip=True, run=1 if f >= p0 else 0, phase=(f * .12) % 1, expr='shock' if f >= p0 else 'smug', blink=0)
    put_sci(c, 1000 - max(0, f - p0) * 6, 1780, 760, f, 1, arms='point' if f >= p0 else 'clip', bun=True, skin=1, expr='stern' if f >= p0 else 'neutral', look=-1)
    c0 = wt(4, 'cativeiro') - 3
    if f >= c0:
        im = crate(clamp((f - c0 - 10) / 8)); paste_c(c, im.resize((int(im.size[0] * .6), int(im.size[1] * .6))), 260, 1380, back(ramp(f, c0, c0 + 8)))
    l0 = wt(4, 'lugar') - 3
    if f >= l0:
        put_wh(c, 260 + max(0, f - l0 - 6) * 8, 1460, 300, False, step=((f * .1) % 1) if f > l0 + 6 else 0, look=.5, blink=blinkAt(f, 3), seed=3)
    s0_ = wt(4, 'sessenta') - 3
    num(c, '61%', 640, 760, f, s0_, 220)
    if f >= s0_:
        for i, x in enumerate((180, 460, 760, 1060)):
            s = back(ramp(f, s0_ + 4 + i * 3, s0_ + 12 + i * 3))
            if s > .05: put_wh(c, x, 1800, 420 * s, i % 2 == 1, expr='smug', look=0, blink=blinkAt(f, 30 + i), seed=30 + i)
    t = smooth(ramp(f, s0_ - 10, s0_ + 10))
    return c, (640, 1420, lerp(1.15, 1.06, t), 0), 'day'


def s5(f):
    c = ilha('golden').copy()
    m0 = wt(5, 'mil') - 3
    rnd = random.Random(9)
    birds = sorted([(rnd.random() * 1240, 1350 + rnd.random() ** .9 * 650, rnd.random() < .5, rnd.randint(1, 50)) for _ in range(34)], key=lambda b: b[1])
    for i, (x, y, fl, sd) in enumerate(birds):
        d0 = m0 - 20 + (i * 7) % 28
        s = back(ramp(f, d0, d0 + 8))
        if s > .05: put_wh(c, x, y, (110 + (y - 1350) * .45) * s, fl, peck=max(0, math.sin((f + sd * 9) * .14)) ** 2, look=.3, seed=sd % 7)
    put_wh(c, 600, 1760, 1000, False, expr='smug' if f >= m0 else 'calm', look=-.2, blink=blinkAt(f, 4), seed=4)
    num(c, '23', 330, 700, f, wt(5, 'vinte') - 3, 150, -6)
    num(c, '1.600+', 760, 860, f, m0, 190, 4)
    z = lerp(1.0, 1.15, easeOut(ramp(f, 0, 60))) * (1 + .0005 * max(0, f - 60))
    return c, (640, 1330, z, lerp(0, -2.5, smooth(ramp(f, 0, 60))) - .01 * max(0, f - 60)), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    s.thunk(s.W(0, 'vinte') - 3, 140, 1.0)
    s.ting(s.W(1, 'anos') - 3, .25)
    for i in range(3): s.thunk(s.W(1, 'quase') - 4 + i * 4, 240, .5)
    s.whoosh(s.W(1, 'certo') - 3, .3, .5)
    for w in ('cento', 'aves', 'cinquenta'): s.thunk(s.W(2, w) - 3, 200, .6)
    s.thunk(s.W(3, 'trinta') - 3, 140, .8)
    for i in (1, 3): s.splash(s.W(3, 'sumiram') - 3 + i * 2, .4)
    s.thunk(s.W(3, 'dois') - 2, 260, .5)
    s.patter(s.W(4, 'predadores') - 3, s.W(4, 'predadores') + 40, 12, .14)
    s.thunk(s.W(4, 'cativeiro') - 3, 200, .5)
    s.ting(s.W(4, 'sessenta') - 3, .35)
    s.thunk(s.W(5, 'mil') - 3, 120, 1.0)
