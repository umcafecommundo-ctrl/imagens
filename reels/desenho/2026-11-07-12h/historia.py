"""Um Café com o Mundo — CURIOSIDADE em desenho (07/11/2026 12h).
Fontes: Cardiff University (comunicado 'CT scans help unlock 400-year-old mystery', 03-04/11/2026),
Arkeonews (04/11/2026), Popular Science (04/11/2026), Archaeology Magazine (05/11/2026).
Fatos: cadeado de segredo de latão com 4 anéis giratórios de letras (tipo 'Nuremberg'), 31,8 mm de altura, 28,5 g,
achado por detectorista na praia de Margam (perto de Port Talbot, sul do País de Gales), do naufrágio do navio
mercante Ann Francis: em 28/12/1583, voltando da Espanha para a Inglaterra, pegou uma tempestade e naufragou ali.
Cerca de 870 moedas de ouro e prata (Museu Nacional do País de Gales / Amgueddfa Cymru). Micro-CT (raios X em 3D)
da Cardiff University (David Williams) mostrou como os encaixes se alinhavam às letras: código ANCE; o museu testou
e abriu. Não se sabe o que guardava nem o que a senha significava. Exposto no National Waterfront Museum, Swansea."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um cadeado com senha, de mais de quatrocentos anos, finalmente foi aberto.",
    "Ele estava no Ann Francis, um navio que voltava da Espanha e naufragou numa tempestade em mil quinhentos e oitenta e três, no País de Gales.",
    "Na areia da praia, saíram cerca de oitocentas e setenta moedas de ouro e prata. E esse cadeado de latão, com quatro anéis de letras.",
    "Só que ninguém sabia a combinação. E forçar podia estragar a peça.",
    "Então, cientistas da Universidade de Cardiff usaram tomografia de raios X e viram, por dentro, como cada encaixe batia com as letras.",
    "A senha era: á, ene, cê, é. O museu testou... e abriu!",
    "Hoje ele está num museu no País de Gales. E ninguém sabe o que essa senha queria dizer.",
]
CAPTXT = [
    "Um cadeado com senha, de mais de 400 anos,|finalmente foi aberto.",
    "Ele estava no Ann Francis, um navio que voltava|da Espanha e naufragou numa tempestade|em 1583, no País de Gales.",
    "Na areia da praia, saíram cerca de 870 moedas de ouro e prata.|E esse cadeado de latão, com 4 anéis de letras.",
    "Só que ninguém sabia a combinação.|E forçar podia estragar a peça.",
    "Então, cientistas da Universidade de Cardiff|usaram tomografia de raios X e viram, por dentro,|como cada encaixe batia com as letras.",
    "A senha era: A, N, C, E.|O museu testou... e abriu!",
    "Hoje ele está num museu no País de Gales.|E ninguém sabe o que essa senha queria dizer.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'quatrocentos', 6), (0, 'aberto', 8), (1, 'tempestade', 6), (1, 'tres', 4), (2, 'oitocentas', 6), (2, 'letras', 6),
         (3, 'combinacao', 6), (4, 'raios', 6), (4, 'letras', 6), (5, 'e', 6), (5, 'abriu', 6), (6, 'dizer', 8)]

BRASS = hexc('#d9a93a'); BRASSD = hexc('#a77a1e'); BRASSL = hexc('#f6dc86')
GOLD = hexc('#f0c541'); GOLD_D = hexc('#b8901e'); SILV = hexc('#d9dde3'); SILV_D = hexc('#9aa2ad')
XR = hexc('#1f3d6b'); XRL = hexc('#8fd3ff')
WOOD = hexc('#8a5a34'); WOODD = hexc('#5e3c22')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


# ------------------------------------------------------------------ desenhos novos
def cadeado(letters='????', open_=0.0, xray=0, spin=0):
    """cadeado de segredo: cilindro de 4 anéis com letras e alça em U por cima. 600x620, base y~600."""
    p = Pen(600, 620)
    lift = open_ * 120
    sc = XRL if xray else BRASSD
    # alça (U): esquerda fica, direita sai do encaixe ao abrir
    if lift: p.line([(150, 330), (150, 330 - lift)], BRASS if not xray else XRL, 34, 6)
    p.line(curve((150, 330 - lift), (300, -10 - lift * 1.2), (450, 330 - lift), 20), sc if xray else BRASS, 34, 6)
    if xray:
        bf, bd, rl = XR, mul(XR, .7), XRL
    else:
        bf, bd, rl = BRASS, BRASSD, BRASSL
    # pontas do cilindro
    p.shape([(60, 330), (110, 310), (110, 560), (60, 540)], bd, None, 6)
    p.shape([(490, 310), (540, 330), (540, 540), (490, 560)], bd, None, 6)
    fnt = ImageFont.truetype(kit.FONT.path, int(76 * art.K))
    for i in range(4):
        x0 = 110 + i * 95
        p.shape([(x0, 300), (x0 + 95, 300), (x0 + 95, 570), (x0, 570)], bf, bd, 6, 12)
        p.stroke([(x0 + 10, 330), (x0 + 85, 330)], 5, rl)
        p.stroke([(x0 + 10, 540), (x0 + 85, 540)], 5, bd if not xray else rl)
        if xray:
            # encaixes internos (dentes) que mostram a posição certa
            for k in range(3):
                yy = 380 + k * 55
                p.poly([(x0 + 20, yy), (x0 + 75, yy), (x0 + 75, yy + 26), (x0 + 20, yy + 26)], XRL)
            p.poly([(x0 + 38, 360 + (i * 37) % 120), (x0 + 58, 360 + (i * 37) % 120), (x0 + 58, 520), (x0 + 38, 520)], hexc('#ffffff'))
        else:
            ch = letters[i]
            off = int(spin * 40 * ((i % 2) * 2 - 1))
            tw = p.d.textlength(ch, font=fnt)
            p.d.text(((x0 + 47.5) * art.K - tw / 2, (395 + off) * art.K), ch, font=fnt, fill=INK + (255,))
    return fin(p)


def galeao(tilt=0.0):
    """navio a vela antigo de lado, proa à direita. 800x800, linha d'água y~700."""
    p = Pen(800, 800)
    p.shape([(40, 560), (760, 560), (690, 720), (110, 720)], WOOD, WOODD, 6, 14)
    p.shape([(40, 520), (190, 520), (190, 565), (40, 565)], hexc('#9d6a40'), WOODD, 5, 4)
    for x in range(160, 680, 90): p.dot(x, 620, 14, hexc('#2a1d14'), 4)
    for mx, top, w in ((260, 90, 170), (500, 40, 200)):
        p.line([(mx, 560), (mx, top)], hexc('#6b4426'), 16, 4)
        p.shape(curve((mx - w / 2, top + 50), (mx - w / 2 - 30, top + 200), (mx - w / 2, top + 330), 10) +
                curve((mx + w / 2, top + 330), (mx + w / 2 + 40, top + 200), (mx + w / 2, top + 50), 10), hexc('#f3ead8'), hexc('#cfc3aa'), 5, 12)
    p.poly([(500, 40), (500, 0), (560, 18)], hexc('#d8443c'), 3)
    return fin(p)


def moeda(prata=0):
    p = Pen(160, 160)
    a, b = (SILV, SILV_D) if prata else (GOLD, GOLD_D)
    p.shape(ell_pts(80, 80, 64, 64, 32), a, b, 5, 6)
    p.arc(80, 80, 42, 42, 0, 360, 4, b)
    p.stroke([(62, 70), (98, 70)], 5, b); p.stroke([(80, 52), (80, 108)], 5, b)
    return fin(p)


def tomografo(glow=0.0):
    """aparelho de tomografia: anel grande em pé sobre base. 900x900, base y~880."""
    p = Pen(900, 900)
    p.shape([(140, 760), (760, 760), (800, 880), (100, 880)], hexc('#cfd6de'), hexc('#9aa5b2'), 6, 12)
    p.shape(ell_pts(450, 420, 360, 360, 64), hexc('#e9eef3'), hexc('#b7c2ce'), 7, 22)
    p.shape(ell_pts(450, 420, 210, 210, 48), mul(hexc('#7fd0ff'), .5 + .5 * glow) if glow else hexc('#33415a'), None, 6)
    p.stroke(curve((290, 230), (450, 150), (610, 230), 10), 10, hexc('#ffffff'))
    p.dot(450, 690, 18, hexc('#3fd16b') if glow else hexc('#8a8f99'), 4)
    return fin(p)


def vitrine():
    p = Pen(600, 900)
    p.shape([(110, 520), (490, 520), (490, 890), (110, 890)], hexc('#e9e2d4'), hexc('#c7bfae'), 6, 16)
    p.shape([(90, 480), (510, 480), (510, 530), (90, 530)], hexc('#d4cab6'), None, 5)
    p.stroke([(110, 120), (490, 120), (490, 480), (110, 480), (110, 120)], 6, hexc('#9fc6d6'))
    p.stroke([(150, 160), (220, 200)], 8, (255, 255, 255))
    return fin(p)


def raio(seed=0):
    p = Pen(300, 700)
    r = random.Random(seed); pts = [(150, 0)]
    for i in range(1, 8): pts.append((150 + (r.random() - .5) * 160, i * 95))
    p.line(pts, hexc('#fff6a8'), 16, 4)
    return fin(p)


@lru_cache(maxsize=2)
def mar_bg():
    """mar de tempestade à noite."""
    from PIL import ImageDraw
    c = Image.new('RGBA', (BW, BH), hexc('#2b3550') + (255,)); d = ImageDraw.Draw(c)
    d.rectangle([0, 0, BW, 900], fill=hexc('#3b4566'))
    rnd = random.Random(3)
    for i in range(7):
        cx = rnd.random() * BW; cy = 150 + rnd.random() * 500
        for j in range(4):
            rx = 120 + rnd.random() * 90
            d.ellipse([cx + (j - 2) * 110 - rx, cy - rx * .5, cx + (j - 2) * 110 + rx, cy + rx * .45], fill=hexc('#55607f'), outline=INK, width=4)
    d.rectangle([0, 1050, BW, BH], fill=hexc('#24507a'))
    for y in range(1080, 2200, 80):
        for x in range(-40 + (y // 80 % 2) * 90, BW, 180):
            d.line([(x, y), (x + 45, y - 22), (x + 90, y)], fill=hexc('#5f8fbf'), width=7)
    return c


def put_img(c, fn, x, feet, h, aspect, flip=False, **kw):
    put_sprite(c, fn, x, feet, h, aspect, flip, {'open_': 10, 'spin': 4, 'glow': 4, 'tilt': 8}, **kw)


def put_lock(c, x, feet, h, **kw):
    put_img(c, 'cadeado', x, feet, h, 600 / 620, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('museu', 'dusk').copy()
    q = wt(0, 'quatrocentos') - 3
    a = wt(0, 'aberto') - 3
    op = easeOut(ramp(f, a, a + 10))
    shake = 6 * math.sin(f * 1.3) if q <= f < a else 0
    put_lock(c, 640 + shake, 1420, 760, letters='????', open_=op, spin=0)
    num(c, '400+ ANOS', 640, 700, f, q, 150, -4)
    if f >= a: num(c, 'CLIC!', 980, 1000, f, a + 2, 110, 8)
    z = lerp(1.35, 1.1, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, a)
    return c, (640, 1150 + k * 10, z, k), 'dusk'


def s1(f):
    c = mar_bg().copy()
    t0 = wt(1, 'tempestade') - 3
    ano = wt(1, 'mil') - 3
    if f >= t0 and (f - t0) % 24 < 5: paste_c(c, raio(f // 24), 300 + 500 * ((f // 24) % 2), 600, 1)
    tilt = 4 * math.sin(f * .09) + (8 * math.sin(f * .2) if f >= t0 else 0)
    im = sprite('galeao', (), 760, 1, False).rotate(tilt, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, 620 + max(0, f - t0) * .8, 1040 + 14 * math.sin(f * .12) + max(0, f - t0) * .5)
    d = ImageDraw.Draw(c)
    for y in range(1400, 1600, 70):
        d.line([(0, y + 10 * math.sin(f * .1 + y)), (BW, y - 10 * math.sin(f * .1 + y))], fill=hexc('#24507a'), width=60)
    num(c, 'VINHA DA ESPANHA', 640, 440, f, wt(1, 'Espanha') - 3, 90, -3)
    num(c, '1583', 640, 570, f, ano, 170, 4)
    t = smooth(ramp(f, 0, 90))
    k = kick(f, t0, .7)
    return c, (640 + 30 * math.sin(f * .02), lerp(1050, 1200, t) + k * 10, lerp(1.25, 1.1, t), k + 1.5 * math.sin(f * .05)), 'dusk'


def s2(f):
    c = CEN('praia', 'day').copy()
    m0 = wt(2, 'oitocentas') - 3
    rnd = random.Random(5)
    for i in range(18):
        x = 140 + rnd.random() * 960; y = 1380 + rnd.random() * 300
        d0 = m0 - 6 + i * 2
        s = back(ramp(f, d0, d0 + 8))
        if s > .05:
            im = sprite('moeda', (('prata', i % 2),), int(110 * s), 1, False)
            paste_c(c, im, x, y - 30 * math.sin(clamp((f - d0) / 10) * math.pi))
    num(c, '870 MOEDAS', 640, 720, f, m0, 130, -4)
    num(c, 'OURO E PRATA', 640, 860, f, wt(2, 'ouro') - 3, 80, 3)
    l0 = wt(2, 'cadeado') - 3
    if f >= l0:
        s = back(ramp(f, l0, l0 + 10))
        put_lock(c, 640, 1660, 560 * s, letters='?' * 4)
        put_dust(c, 640, 1600, 120, f - l0)
    num(c, '4 ANÉIS', 640, 1000, f, wt(2, 'quatro') - 3, 80, 6)
    t = smooth(ramp(f, l0 - 6, l0 + 12))
    return c, (640, lerp(1300, 1250, t), lerp(1.1, 1.2, t) * (1 + .0005 * f), 0), 'day'


def s3(f):
    c = CEN('museu', 'day').copy()
    c0 = wt(3, 'combinacao') - 3
    fo = wt(3, 'forcar') - 3
    put_sci(c, 360, 1700, 900, f, 2, arms='cheek' if f < fo else 'up', expr='nervous' if f >= fo else 'neutral', skin=2, look=1, glasses=True)
    sp = (f * .12) % 1 if f >= c0 else 0
    lets = ''.join('ABCDEFGHIJKLMNOPRST'[(int(f * .4) + i * 5) % 19] for i in range(4)) if f >= c0 and f < fo else '????'
    put_lock(c, 880, 1500, 460, letters=lets, spin=round(sp * 4) / 4)
    if f < fo: num(c, '???', 880, 640, f, c0, 130, 5)
    if f >= fo: num(c, 'CUIDADO!', 640, 600, f, fo, 100, -4)
    k = kick(f, fo, .6)
    return c, (640, 1250 + k * 8, lerp(1.08, 1.18, smooth(f / 120)), k), 'day'


def s4(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    r0 = wt(4, 'tomografia') - 3
    x0 = wt(4, 'dentro') - 3
    g = clamp((f - r0) / 6)
    put_img(c, 'tomografo', 760, 1600, 860, 1, glow=round(g * 4) / 4)
    put_lock(c, 760, 1260, 300, xray=1 if f >= r0 else 0, letters='????')
    put_sci(c, 250, 1700, 860, f, 1, arms='point' if f >= x0 else 'clip', bun=True, skin=1, expr='grin' if f >= x0 else 'neutral', look=1)
    num(c, 'CARDIFF', 640, 600, f, wt(4, 'Cardiff') - 3, 100, -4)
    num(c, 'RAIOS X', 760, 760, f, wt(4, 'raios') - 3, 120, 4)
    num(c, 'POR DENTRO!', 760, 1500, f, x0, 80, -3)
    t = smooth(ramp(f, x0 - 6, x0 + 20))
    return c, (lerp(600, 680, t), lerp(1150, 1250, t), lerp(1.1, 1.25, t) * (1 + .0004 * f), 0), 'day'


def s5(f):
    c = CEN('museu', 'dusk').copy()
    ks = [wt(5, 'a', 1) - 3, wt(5, 'ene') - 3, wt(5, 'ce') - 3, wt(5, 'e', 0) - 3]
    lets = ''.join(L if f >= k else '?' for L, k in zip('ANCE', ks))
    a = wt(5, 'abriu') - 3
    op = easeOut(ramp(f, a, a + 10))
    put_lock(c, 640, 1500, 760, letters=lets, open_=op)
    for i, (L, k) in enumerate(zip('ANCE', ks)):
        num(c, L, 300 + i * 227, 560, f, k, 180, (-6, 4, -3, 6)[i])
    if f >= a:
        num(c, 'ABRIU!', 640, 820, f, a + 1, 150, -5)
        put_dust(c, 640, 960, 160, f - a)
    k = kick(f, a)
    z = lerp(1.1, 1.22, smooth(ramp(f, 0, a))) * (1 + .0005 * f)
    return c, (640, 1150 + k * 10, z, k + lerp(0, -2, smooth(ramp(f, a, a + 20)))), 'dusk'


def s6(f):
    c = CEN('museu', 'dusk').copy()
    put_img(c, 'vitrine', 640, 1640, 1000, 600 / 900)
    put_lock(c, 640, 1240, 330, letters='ANCE', open_=1)
    put_sci(c, 1030, 1720, 760, f, 3, arms='cheek' if f >= wt(6, 'ninguem') - 3 else 'hang', expr='neutral', skin=0, look=-1)
    n0 = wt(6, 'ninguem') - 3
    if f >= n0:
        thought(c, 820, 800, 150, back(ramp(f, n0, n0 + 10)), txt('ANCE = ?', 52))
    num(c, 'PAÍS DE GALES', 500, 640, f, wt(6, 'Gales') - 3, 80, -4)
    z = lerp(1.0, 1.15, easeOut(ramp(f, 0, 60))) * (1 + .0005 * max(0, f - 60))
    return c, (640, 1250, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'quatrocentos') - 3, 140, .9)
    s.ting(s.W(0, 'aberto') - 3, .4)
    s.whoosh(s.W(1, 'tempestade') - 3, .4, .6)
    s.splash(s.W(1, 'naufragou') - 3, .4)
    s.thunk(s.W(1, 'mil') - 3, 160, .7)
    for i in range(6): s.ting(s.W(2, 'oitocentas') - 6 + i * 4, .12)
    s.thunk(s.W(2, 'cadeado') - 3, 200, .6)
    s.thunk(s.W(3, 'forcar') - 3, 220, .5)
    s.ting(s.W(4, 'raios') - 3, .3)
    for w, n in (('a', 1), ('ene', 0), ('ce', 0), ('e', 0)): s.thunk(s.W(5, w, n) - 3, 240, .6)
    s.ting(s.W(5, 'abriu') - 3, .45)
