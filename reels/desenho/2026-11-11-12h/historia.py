"""Um Café com o Mundo — CURIOSIDADE em desenho (11/11/2026 12h).
Fontes: Inrap (comunicado de 06/11/2026), Live Science (08/11/2026, Kristina Killgrove), The History Blog (07/11/2026),
Archaeology Magazine (10/11/2026).
Fatos: Horbourg-Wihr, perto de Colmar, Alsácia, nordeste da França, a poucos km do Reno (antiga fronteira/limes romano).
Escavação preventiva do Inrap antes de um conjunto habitacional. Vila galo-romana dos séculos 1 a 3; no 2º metade do
século 5 (c. 450-500 d.C.) parte do lugar virou cemitério: 11 túmulos de adultos, 3 de crianças e 2 cavalos enterrados
com os arreios. Dois homens com espada (bainha de madeira parcialmente preservada), escudo, angon (lança de arremesso) e
scramasax (espada curta germânica) com enfeites de ouro e granada (cloisonné) -> típicos de chefes ou mercenários
germânicos. Duas mulheres com broches de prata em forma de pássaro, colares de contas de vidro e pente de osso.
Poucos sítios da região documentam povoamento germânico nessa época, quando o Império Romano do Ocidente desmoronava.
Os esqueletos ainda serão estudados (ferimentos de lâmina; ver se foram de combate)."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Dois cavalos de guerra foram enterrados com os arreios, ao lado de chefes guerreiros de mais de mil e quinhentos anos.",
    "Foi na França, na Alsácia, perto do rio Reno, a antiga fronteira do Império Romano.",
    "Num pequeno cemitério, arqueólogos acharam onze adultos, três crianças e os dois cavalos.",
    "Dois homens tinham espada, escudo, lança e enfeites de ouro com pedras vermelhas, as granadas.",
    "Duas mulheres levavam broches de prata em forma de pássaro, colares de vidro e um pente de osso.",
    "Por que isso importa? Eles viveram quando o Império Romano do Ocidente desmoronava. E quase não se acham vilas germânicas dessa época.",
    "Agora, os ossos vão contar quem eram esses chefes e como eles viveram.",
]
CAPTXT = [
    "Dois cavalos de guerra foram enterrados com os arreios,|ao lado de chefes guerreiros de mais de 1.500 anos.",
    "Foi na França, na Alsácia, perto do rio Reno,|a antiga fronteira do Império Romano.",
    "Num pequeno cemitério, arqueólogos acharam|11 adultos, 3 crianças e os 2 cavalos.",
    "Dois homens tinham espada, escudo, lança|e enfeites de ouro com pedras vermelhas, as granadas.",
    "Duas mulheres levavam broches de prata em forma de pássaro,|colares de vidro e um pente de osso.",
    "Por que isso importa? Eles viveram quando|o Império Romano do Ocidente desmoronava.|E quase não se acham vilas germânicas dessa época.",
    "Agora, os ossos vão contar quem eram esses chefes|e como eles viveram.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [3]
CHECK = [(0, 'arreios', 4), (0, 'mil', 6), (1, 'franca', 4), (1, 'reno', 6), (2, 'onze', 4), (2, 'cavalos', 6),
         (3, 'escudo', 4), (3, 'granadas', 6), (4, 'passaro', 4), (4, 'pente', 6), (5, 'desmoronava', 4), (6, 'chefes', 6)]

GOLD = hexc('#f2c23a'); GOLDD = hexc('#c48a1a'); GAR = hexc('#c0263a'); GARD = hexc('#851626')
SILV = hexc('#d6dbe2'); SILVD = hexc('#9aa3ad'); STEEL = hexc('#b4bcc6'); STEELD = hexc('#7a838e')
WOOD = hexc('#8a5a34'); WOODD = hexc('#5e3c20'); RED = hexc('#b8322a'); REDD = hexc('#82211b')
DIRT = hexc('#c79a62'); DIRTD = hexc('#9c7444')

HC = [dict(b=hexc('#a8653a'), d=hexc('#74411f'), m=hexc('#3b2416'), hoof=hexc('#3a2a20')),
      dict(b=hexc('#e6ddcf'), d=hexc('#b9ad9a'), m=hexc('#8d8577'), hoof=hexc('#4a3e34'))]


# ------------------------------------------------------------------ cavalo de guerra com arreios
def horse(blink=0, look=.3, step=0.0, nod=0.0, coat=0, harness=1, expr='calm'):
    """cavalo de lado olhando p/ direita, com arreios (cabeçada, rédea, manta com ouro). 900x800, cascos y~780."""
    C = HC[coat]
    p = Pen(900, 800)
    two = 2 * math.pi
    bx, by = 400, 420
    # pernas (as de trás mais escuras)
    legs = [(-170, 0, .5), (150, 0, 0), (-130, 1, 0), (190, 1, .5)]
    for dx, front, ph in legs:
        sw = math.sin(two * (step + ph)) * 40 if step else 0
        lift = max(0, math.sin(two * (step + ph))) * 30 if step else 0
        col = mul(C['b'], .8) if front == 0 else C['b']
        top = (bx + dx, by + 70); kn = (bx + dx + sw * .4, 640 - lift * .5); ft = (bx + dx + sw, 760 - lift)
        p.line([top, kn, ft], col, 34, 5)
        p.shape(ell_pts(ft[0] + 4, ft[1] + 6, 24, 16, 20), C['hoof'], None, 4, 0)
    # rabo
    sw = math.sin(step * two) * 12 if step else 0
    tail = curve((bx - 220, by - 50), (bx - 330 + sw, by + 40), (bx - 290 + sw, by + 230), 10) + curve((bx - 250 + sw, by + 230), (bx - 270, by + 40), (bx - 200, by - 10), 10)
    p.shape(tail, C['m'], None, 5, 0)
    # corpo
    p.shape(ell_pts(bx, by, 250, 125, 64, 0, .05), C['b'], C['d'], 6, 24)
    # pescoço + cabeça
    hx, hy = bx + 300, 200 + nod * 40
    ha = .55 + nod * .25
    neck = [(bx + 130, by - 90), (hx - 70, hy - 50), (hx - 10, hy - 10), (hx + 10, hy + 60), (bx + 220, by + 30)]
    p.shape(neck, C['b'], C['d'], 6, 14)
    H = lambda dx, dy: (hx + dx * math.cos(ha) - dy * math.sin(ha), hy + dx * math.sin(ha) + dy * math.cos(ha))
    p.shape(ell_pts(H(70, 0)[0], H(70, 0)[1], 120, 58, 40, ha, .15), C['b'], C['d'], 6, 12)
    p.dot(H(170, 6)[0], H(170, 6)[1], 9, mul(C['d'], .8))  # narina
    # orelhas
    for ox in (-30, -6):
        e0 = H(ox - 10, -50); e1 = H(ox - 40, -105); e2 = H(ox + 18, -52)
        p.shape([e0, e1, e2], C['b'], C['d'], 5, 4)
    # crina
    mane = []
    for i in range(7):
        t = i / 6
        x = lerp(hx - 50, bx + 120, t); y = lerp(hy - 50, by - 100, t)
        mane += [(x, y), (x - 30, y - 34 + 8 * math.sin(i))]
    mane += [(bx + 140, by - 70), (hx - 30, hy - 20)]
    p.shape(mane, C['m'], None, 5, 0)
    # olho grande
    ec = H(20, -14); er = 24 if expr == 'shock' else 20
    p.dot(ec[0], ec[1], er, (255, 255, 255), 4)
    if blink < .6:
        lk = max(-1, min(1, look))
        p.dot(ec[0] + lk * (er - 10), ec[1] + 2, 8, INK)
        p.dot(ec[0] + lk * (er - 10) - 3, ec[1] - 2, 3, (255, 255, 255))
    else:
        p.stroke([(ec[0] - er, ec[1]), (ec[0] + er, ec[1])], 5)
    if expr == 'proud': p.stroke([(ec[0] - er, ec[1] - er - 6), (ec[0] + er, ec[1] - er + 2)], 5)
    if harness:
        # cabeçada (correias) + rédea
        p.stroke([H(-35, -50), H(-25, 52)], 9, REDD)
        p.stroke([H(120, -52), H(130, 52)], 9, REDD)
        p.stroke([H(60, 30), H(126, 30)], 7, REDD)
        p.dot(H(128, 40)[0], H(128, 40)[1], 11, GOLD, 4)
        p.dot(H(-30, 0)[0], H(-30, 0)[1], 9, GOLD, 3)
        p.stroke([H(128, 40), (bx + 170, by - 60), (bx + 60, by - 110)], 6, WOODD)
        # peitoral
        p.stroke([(bx + 200, by - 40), (bx + 250, by + 40), (bx + 160, by + 90)], 10, REDD)
        for k in range(3): p.dot(bx + 210 + k * 16, by + 10 + k * 22, 8, GOLD, 3)
        # manta com borda dourada
        bl = [(bx - 90, by - 118), (bx + 70, by - 118), (bx + 85, by + 10), (bx - 105, by + 10)]
        p.shape(bl, RED, REDD, 5, 8)
        p.stroke([(bx - 103, by + 2), (bx + 83, by + 2)], 9, GOLD)
        for k in range(5): p.dot(bx - 80 + k * 38, by + 2, 7, GAR, 3)
    return p.img


@lru_cache(maxsize=2)
def espada():
    p = Pen(200, 700)
    p.shape([(100, 20), (125, 80), (125, 520), (75, 520), (75, 80)], STEEL, STEELD, 5, 10)
    p.stroke([(100, 70), (100, 500)], 4, STEELD)
    p.shape([(20, 520), (180, 520), (180, 556), (20, 556)], GOLD, GOLDD, 5, 6)
    for x in (45, 100, 155): p.dot(x, 538, 11, GAR, 3)
    p.shape([(82, 556), (118, 556), (118, 650), (82, 650)], WOOD, WOODD, 5, 4)
    p.dot(100, 668, 26, GOLD, 5); p.dot(100, 668, 12, GAR, 0)
    return p.img


@lru_cache(maxsize=2)
def escudo_r():
    p = Pen(500, 500)
    p.shape(ell_pts(250, 250, 225, 225, 60), hexc('#3f6fa8'), hexc('#2c5079'), 6, 18)
    for a in range(0, 360, 45):
        r = math.radians(a)
        p.stroke([(250 + 60 * math.cos(r), 250 + 60 * math.sin(r)), (250 + 210 * math.cos(r), 250 + 210 * math.sin(r))], 6, hexc('#2c5079'))
    p.shape(ell_pts(250, 250, 70, 70, 36), STEEL, STEELD, 5, 10)
    p.dot(230, 228, 16, (255, 255, 255))
    return p.img


@lru_cache(maxsize=2)
def lanca():
    p = Pen(160, 800)
    p.line([(80, 200), (80, 780)], WOOD, 16, 4)
    p.shape([(80, 10), (110, 80), (96, 210), (64, 210), (50, 80)], STEEL, STEELD, 5, 8)
    p.stroke([(68, 100), (60, 60)], 5, STEELD); p.stroke([(92, 100), (100, 60)], 5, STEELD)
    return p.img


@lru_cache(maxsize=2)
def joia():
    """enfeite de ouro com granadas (cloisonné). 400x260."""
    p = Pen(400, 260)
    p.shape([(30, 130), (110, 30), (290, 30), (370, 130), (290, 230), (110, 230)], GOLD, GOLDD, 6, 12)
    for (x, y) in ((140, 90), (200, 90), (260, 90), (110, 150), (170, 160), (230, 160), (290, 150)):
        p.shape([(x - 22, y), (x, y - 26), (x + 22, y), (x, y + 26)], GAR, GARD, 4, 4)
    p.dot(160, 70, 8, (255, 240, 200))
    return p.img


@lru_cache(maxsize=2)
def broche():
    """broche de prata em forma de pássaro (de lado, olhando p/ direita). 400x300."""
    p = Pen(400, 300)
    p.shape([(110, 170), (20, 110), (40, 160), (10, 200), (110, 200)], SILV, SILVD, 5, 6)
    p.shape(ell_pts(180, 190, 110, 62, 40, -.15), SILV, SILVD, 6, 12)
    p.shape(ell_pts(290, 110, 54, 50, 30), SILV, SILVD, 6, 8)
    p.shape([(334, 96), (392, 116), (334, 132)], GOLD, GOLDD, 4, 4)
    p.shape(ell_pts(170, 185, 64, 30, 24, -.3), mul(SILV, .88), SILVD, 4, 4)
    p.dot(300, 102, 15, GAR, 4); p.dot(296, 97, 4, (255, 230, 230))
    for x in (160, 210): p.stroke([(x, 248), (x, 290)], 7, SILVD)
    return p.img


@lru_cache(maxsize=2)
def colar():
    p = Pen(500, 400)
    cols = [hexc('#3fa0c8'), hexc('#e2b23a'), hexc('#5bb36a'), hexc('#d65a4a'), hexc('#f0f0ea')]
    for i in range(17):
        a = math.radians(200 + i * 140 / 16)
        x = 250 + 210 * math.cos(a); y = 60 - 300 * math.sin(a) * .9
        p.dot(x, y, 20, cols[i % 5], 4)
        p.dot(x - 6, y - 6, 5, (255, 255, 255))
    return p.img


@lru_cache(maxsize=2)
def pente():
    p = Pen(500, 260)
    p.shape([(30, 40), (470, 40), (470, 120), (30, 120)], hexc('#efe3c2'), hexc('#c9b78e'), 6, 8)
    for x in range(50, 470, 30):
        p.shape([(x, 118), (x + 16, 118), (x + 12, 240), (x + 4, 240)], hexc('#efe3c2'), hexc('#c9b78e'), 4, 0)
    for x in (110, 250, 390): p.arc(x, 80, 26, 20, 0, 360, 4, hexc('#a8936a'))
    return p.img


def cova(kind=0):
    """cova vista de cima (retângulo de terra escura). kind 0 adulto, 1 criança, 2 cavalo."""
    w, h = ((180, 420), (130, 240), (380, 300))[kind]
    p = Pen(w + 40, h + 40)
    p.shape([(20, 20), (w + 20, 20), (w + 20, h + 20), (20, h + 20)], hexc('#6e4e32'), hexc('#4e3622'), 5, 8)
    p.poly([(34, 34), (w + 6, 34), (w + 6, h + 6), (34, h + 6)], hexc('#5a3f28'))
    return p.img


@lru_cache(maxsize=2)
def coluna(broken=0):
    p = Pen(260, 900)
    top = 160 if broken else 60
    p.shape([(40, 820), (220, 820), (220, 880), (40, 880)], hexc('#e8e0cc'), hexc('#c4b99f'), 5, 6)
    if broken:
        p.shape([(60, 820), (200, 820), (200, 220), (150, 170), (110, 230), (60, 190)], hexc('#efe8d6'), hexc('#cfc4aa'), 5, 14)
    else:
        p.shape([(60, 820), (200, 820), (200, 120), (60, 120)], hexc('#efe8d6'), hexc('#cfc4aa'), 5, 14)
        p.shape([(20, 60), (240, 60), (240, 120), (20, 120)], hexc('#e8e0cc'), hexc('#c4b99f'), 5, 6)
    for x in (95, 130, 165): p.stroke([(x, top + 80 if broken else 130), (x, 810)], 4, hexc('#cfc4aa'))
    return p.img


def put_horse(c, x, feet, h, flip=False, f=0, seed=1, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    put_sprite(c, 'horse', x, feet, h, 900 / 800, flip, {'step': 8, 'nod': 4, 'look': 4}, **kw)


def put_img(c, fn, x, feet, h, aspect, flip=False, **kw):
    put_sprite(c, fn, x, feet, h, aspect, flip, {}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


@lru_cache(maxsize=2)
def pit_bg(light='day'):
    """área de escavação: terra em camadas."""
    from PIL import ImageDraw
    S = 2; W, H = BW * S, BH * S
    k = 1.0 if light == 'day' else .78
    img = Image.new('RGB', (W, H), mul(hexc('#8a6440'), k)); d = ImageDraw.Draw(img)
    for i, col in enumerate(('#b08a5a', '#a37a50', '#946c46', '#86603e', '#7d5a3a', '#6e4e32')):
        y = (i * 380) * S
        d.rectangle([0, y, W, y + 380 * S], fill=mul(hexc(col), k))
        d.line([(0, y), (W, y + 30 * S)], fill=mul(hexc(col), .8 * k), width=5 * S)
    r = random.Random(4)
    for _ in range(70):
        x = r.random() * W; y = r.random() * H; rr = (6 + r.random() * 14) * S
        d.ellipse([x - rr, y - rr * .7, x + rr, y + rr * .7], fill=mul(hexc('#c2a47c'), k))
    return img.resize((BW, BH), Image.LANCZOS).convert('RGBA')


def sparkle(c, x, y, f, f0, n=5, r=230):
    if f < f0: return
    for i in range(n):
        a = i * 2 * math.pi / n + f * .04
        s = .6 + .4 * math.sin(f * .3 + i)
        paste_c(c, txt('*', 70), x + r * math.cos(a), y + r * .8 * math.sin(a), s * back(ramp(f, f0 + i, f0 + i + 8)))


def pop(c, fn, x, y, h, aspect, f, f0, rot=0.0):
    if f < f0: return
    s = back(ramp(f, f0, f0 + 9))
    bob = 10 * math.sin((f - f0) * .08)
    im = sprite(fn, (), int(h), aspect, False)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    paste_c(c, im, x, y + bob, s)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = pit_bg('golden').copy()
    a = wt(0, 'arreios') - 3
    put_horse(c, 300, 1500, 600, f=f, seed=1, look=.4)
    put_horse(c, 950, 1500, 600, True, f=f, seed=2, coat=1, look=.4, nod=.5 + .5 * math.sin(f * .05))
    pop(c, 'espada', 625, 1640, 480, 200 / 700, f, wt(0, 'chefes') - 3, 90)
    sparkle(c, 625, 1640, f, wt(0, 'chefes'), 5, 200)
    num(c, 'ARREIOS!', 640, 640, f, a, 120, -4)
    num(c, '1.500+ ANOS', 640, 820, f, wt(0, 'mil') - 3, 130, 3)
    z = lerp(1.4, 1.05, easeOut(ramp(f, 0, 50))) * (1 + .0005 * f)
    k = kick(f, wt(0, 'mil') - 3)
    return c, (640, 1200 + k * 10, z, k), 'golden'


def s1(f):
    c = CEN('mapa', 'day').copy()
    rn = wt(1, 'reno') - 3
    t = smooth(ramp(f, rn, rn + 20))
    if f >= rn:
        pts = [(980 + 40 * math.sin(i * .5), 420 + i * 70) for i in range(int(2 + 15 * t))]
        if len(pts) > 1:
            from PIL import ImageDraw
            d = ImageDraw.Draw(c); d.line(pts, fill=hexc('#2f6fb0'), width=22, joint='curve')
        num(c, 'RIO RENO', 1000, 1500, f, rn, 70, 4)
    num(c, 'FRANÇA', 520, 560, f, wt(1, 'franca') - 3, 120, -4)
    al = wt(1, 'alsacia') - 3
    if f >= al:
        s = back(ramp(f, al, al + 8))
        paste_c(c, txt('V', 120), 860, 960 - 40 * abs(math.sin(f * .15)), s)
        num(c, 'ALSÁCIA', 760, 1110, f, al, 80, -3)
    fr = wt(1, 'imperio') - 3
    if f >= fr:
        put_img(c, 'coluna', 260, 1450, 420 * back(ramp(f, fr, fr + 8)), 260 / 900)
        num(c, 'FRONTEIRA DE ROMA', 640, 760, f, fr, 72, 3)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 160))) * (1 + .0004 * f)
    return c, (lerp(640, 760, smooth(ramp(f, 0, 160))), 1050, z, 0), 'day'


def s2(f):
    c = pit_bg('day').copy()
    on = wt(2, 'onze') - 3; tr = wt(2, 'tres') - 3; ca = wt(2, 'cavalos') - 3
    put_sci(c, 1080, 1690, 420, f, 3, arms='point', skin=1, expr='shock' if f >= on else 'neutral', look=-1)
    for i in range(11):
        x = 150 + (i % 6) * 150; y = 1050 + (i // 6) * 300
        if f >= on + i: paste_c(c, sprite('cova', (('kind', 0),), 230, 220 / 460, False), x, y, back(ramp(f, on + i, on + i + 6)))
    for i in range(3):
        if f >= tr + i * 2: paste_c(c, sprite('cova', (('kind', 1),), 150, 170 / 280, False), 830 + i * 120, 1340, back(ramp(f, tr + i * 2, tr + i * 2 + 6)))
    for i in range(2):
        if f >= ca + i * 3:
            paste_c(c, sprite('cova', (('kind', 2),), 220, 420 / 340, False), 300 + i * 360, 1560, back(ramp(f, ca + i * 3, ca + i * 3 + 6)))
    num(c, '11 ADULTOS', 560, 560, f, on, 100, -4)
    num(c, '3 CRIANÇAS', 880, 700, f, tr, 90, 4)
    num(c, '2 CAVALOS', 520, 840, f, ca, 110, -3)
    z = lerp(1.25, 1.05, smooth(ramp(f, 0, 90))) * (1 + .0005 * f)
    return c, (640, 1150, z, 0), 'day'


def s3(f):
    c = CEN('museu', 'day').copy()
    es = wt(3, 'espada') - 3; sc = wt(3, 'escudo') - 3; la = wt(3, 'lanca') - 3; ou = wt(3, 'ouro') - 3
    pop(c, 'escudo_r', 640, 1080, 520, 1, f, sc)
    pop(c, 'espada', 290, 1080, 700, 200 / 700, f, es, 12)
    pop(c, 'lanca', 990, 1050, 760, .2, f, la, -10)
    if f >= ou:
        pop(c, 'joia', 640, 1450, 230, 400 / 260, f, ou)
        sparkle(c, 640, 1450, f, ou + 2, 6, 230)
    num(c, 'OURO', 420, 560, f, ou, 110, -5)
    num(c, 'GRANADAS', 800, 640, f, wt(3, 'granadas') - 3, 100, 4)
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 70))) * (1 + .0006 * f)
    k = kick(f, ou)
    return c, (640, 1150 + k * 8, z, k), 'day'


def s4(f):
    c = CEN('museu', 'day').copy()
    br = wt(4, 'broches') - 3; co = wt(4, 'colares') - 3; pe = wt(4, 'pente') - 3
    pop(c, 'broche', 640, 920, 330, 4 / 3, f, br)
    num(c, 'PRATA', 640, 620, f, wt(4, 'prata') - 3, 100, -4)
    pop(c, 'colar', 360, 1350, 300, 1.25, f, co)
    num(c, 'VIDRO', 360, 1130, f, wt(4, 'vidro') - 3, 80, 3)
    pop(c, 'pente', 920, 1380, 200, 500 / 260, f, pe)
    num(c, 'OSSO', 920, 1170, f, wt(4, 'osso') - 3, 80, -3)
    cx = lerp(640, 640, 0) + 30 * math.sin(f * .02)
    return c, (cx, lerp(1000, 1150, smooth(ramp(f, br, pe))), lerp(1.3, 1.08, smooth(ramp(f, br, co))), 0), 'day'


def s5(f):
    c = CEN('antiga', 'dusk').copy()
    de = wt(5, 'desmoronava') - 3; qu = wt(5, 'quase') - 3
    for i, x in enumerate((230, 1010)):
        broken = f >= de + i * 4
        put_img(c, 'coluna', x, 1600, 640, 260 / 900, broken=1 if broken else 0)
        put_dust(c, x, 1050, 140, f - de - i * 4, 18)
    num(c, 'ANOS 450 A 500', 640, 660, f, wt(5, 'viveram') - 3, 100, -3)
    num(c, 'IMPÉRIO ROMANO', 640, 820, f, wt(5, 'imperio') - 3, 90, 3)
    num(c, 'RARO!', 640, 1000, f, qu, 150, -5)
    hx = lerp(-200, 640, smooth(ramp(f, qu - 30, qu + 20)))
    put_horse(c, hx, 1620, 460, f=f, seed=5, step=(f * .05) % 1 if f < qu + 20 else 0, look=.3)
    k = kick(f, de)
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 200))) * (1 + .0003 * f)
    return c, (640, 1200 + k * 10, z, k * 2), 'dusk'


def s6(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    put_sci(c, 330, 1650, 780, f, 1, arms='point', bun=True, skin=1, expr='neutral', look=1)
    put_horse(c, 900, 1650, 520, True, f=f, seed=6, coat=1, expr='proud', look=-.5, nod=.5 + .5 * math.sin(f * .06))
    num(c, 'OS OSSOS', 640, 680, f, wt(6, 'ossos') - 3, 110, -4)
    num(c, '?', 900, 820, f, wt(6, 'chefes') - 3, 200, 6)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 120))) * (1 + .0004 * f)
    return c, (640, 1200, z, lerp(0, -2, smooth(ramp(f, 0, 120)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'arreios') - 3, 160, .8)
    s.ting(s.W(0, 'chefes') - 3, .3)
    s.thunk(s.W(0, 'mil') - 3, 120, 1.0)
    s.thunk(s.W(1, 'franca') - 3, 220, .5)
    s.splash(s.W(1, 'reno') - 3, .3)
    for w in ('onze', 'tres', 'cavalos'): s.thunk(s.W(2, w) - 3, 200, .6)
    for w in ('espada', 'escudo', 'lanca'): s.thunk(s.W(3, w) - 3, 240, .5)
    s.ting(s.W(3, 'ouro') - 3, .4)
    for w in ('broches', 'colares', 'pente'): s.ting(s.W(4, w) - 3, .25)
    s.thunk(s.W(5, 'desmoronava') - 3, 110, 1.0)
    s.patter(s.W(5, 'quase') - 30, s.W(5, 'quase') + 20, 10, .12)
    s.ting(s.W(6, 'chefes') - 3, .3)
