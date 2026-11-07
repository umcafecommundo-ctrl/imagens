"""Um Café com o Mundo — CURIOSIDADE em desenho (07/11/2026 17h).
Fontes: PNAS vol. 123, n. 46 (02/11/2026), 'Heme signatures in mineralized red blood cells within vascular canals of a
115-million-year-old dinosaur bone', DOI 10.1073/pnas.2614248123; comunicado da Curtin University (via ScienceDaily, 06/11/2026);
Sci.News (02/11/2026). Fatos: Aratasaurus museunacionali, terópode carnívoro de ~115 milhões de anos, Mina Pedra Branca,
Formação Romualdo (Bacia do Araripe), Nordeste do Brasil. Estruturas elipsoidais de ~23 x 20 micrômetros nos canais vasculares
dos ossos das pernas; heme B detectado; mineral hausmanita (óxido de manganês) ajudou a preservar. NÃO é sangue/proteína intacta.
Equipe internacional de 27 autores, liderada por Kliti Grice (Curtin), com Museu Nacional (Kellner), Universidade Regional do Cariri,
JAMSTEC e Johns Hopkins. Desafia a ideia de que moléculas da hemoglobina não sobrevivem tanto tempo."""
from kit import *
import kit
from art import ik2

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Cientistas acharam sinais de sangue num dinossauro de cento e quinze milhões de anos. E ele é brasileiro!",
    "É o Aratassauro, um dinossauro carnívoro que viveu no Nordeste do Brasil, na Bacia do Araripe.",
    "Nos canais dos ossos das pernas, havia bolinhas minúsculas: glóbulos vermelhos fossilizados.",
    "E a química achou heme, uma parte da hemoglobina, que leva oxigênio no sangue.",
    "Mas calma: não é sangue fresco. Um mineral chamado hausmanita virou uma cápsula do tempo e protegeu essas células.",
    "Por que isso importa? Muitos cientistas achavam que essas moléculas não duravam tanto tempo.",
    "O estudo teve o Museu Nacional e a Universidade Regional do Cariri. E outros fósseis podem guardar segredos assim.",
]
CAPTXT = [
    "Cientistas acharam sinais de sangue num dinossauro|de 115 milhões de anos.|E ele é brasileiro!",
    "É o Aratasaurus, um dinossauro carnívoro|que viveu no Nordeste do Brasil,|na Bacia do Araripe.",
    "Nos canais dos ossos das pernas,|havia bolinhas minúsculas:|glóbulos vermelhos fossilizados.",
    "E a química achou heme,|uma parte da hemoglobina,|que leva oxigênio no sangue.",
    "Mas calma: não é sangue fresco.|Um mineral chamado hausmanita virou uma cápsula|do tempo e protegeu essas células.",
    "Por que isso importa? Muitos cientistas achavam|que essas moléculas não duravam tanto tempo.",
    "O estudo teve o Museu Nacional|e a Universidade Regional do Cariri.|E outros fósseis podem guardar segredos assim.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'quinze', 6), (0, 'brasileiro', 8), (1, 'carnivoro', 6), (1, 'Araripe', 6), (2, 'canais', 6), (2, 'globulos', 8),
         (3, 'hemoglobina', 6), (3, 'heme', 6), (4, 'fresco', 6), (4, 'capsula', 6), (5, 'importa', 6), (5, 'tempo', 6), (6, 'Nacional', 6), (6, 'assim', 8)]

DG = hexc('#74b45c'); DGD = hexc('#4f8a3f'); BELLY = hexc('#eadba0')
BONE = hexc('#eee3c3'); BONED = hexc('#c5b48a')
RED = hexc('#d9433b'); REDD = hexc('#a42c27'); REDL = hexc('#f27b70')
MN = hexc('#5b5f73'); MNL = hexc('#a7b3d6')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


# ------------------------------------------------------------------ desenhos novos
def dino(phase=0.0, mouth=0.0, blink=0, expr='calm', look=0.4, fossil=0):
    """terópode de lado olhando p/ direita. 800x600, pés y~585. fossil=1 -> esqueleto de museu."""
    p = Pen(800, 600)
    two = 2 * math.pi
    bob = 6 * abs(math.sin(two * phase))
    body, dark = (BONE, BONED) if fossil else (DG, DGD)
    hip = (330, 360 + bob)
    legs = []
    for k in (1, 0):
        ph = phase + k * .5
        foot = (hip[0] + (-10 if k else 20) + 70 * math.cos(two * ph), 575 - 28 * max(0, math.sin(two * ph)))
        legs.append((hip, ik2(hip, foot, 125, 130), foot))

    def leg(L, far):
        h, kn, ft = L
        col = mul(body, .82) if far else body
        if fossil:
            p.line([h, kn, ft], col, 18, 4)
        else:
            p.line([h, kn], col, 52, 5); p.line([kn, ft], col, 30, 5)
        for dx in (36, 18, -10):
            p.line([ft, (ft[0] + dx, ft[1] + 8)], col, 9, 3)
    leg(legs[0], True)
    sway = 10 * math.sin(two * phase)
    tail = curve((250, 300 + bob), (110, 250 + sway), (10, 230 + sway * 2), 14)
    tail2 = curve((15, 245 + sway * 2), (120, 300 + sway), (260, 385 + bob), 14)
    if fossil:
        p.line(curve((250, 330 + bob), (110, 270 + sway), (15, 240 + sway * 2), 14), BONE, 14, 4)
        for x, y in curve((240, 330 + bob), (110, 270 + sway), (30, 245 + sway * 2), 10)[1:]:
            p.line([(x, y - 14), (x, y + 14)], BONE, 8, 3)
        p.line([(250, 330 + bob), (480, 280 + bob)], BONE, 16, 4)
        for i in range(6):
            x = 290 + i * 32
            p.line(curve((x, 322 + bob - i * 6), (x + 18, 380 + bob), (x + 4, 420 + bob - i * 4), 8), BONE, 10, 3)
        p.shape(ell_pts(320, 360 + bob, 46, 30, 24), BONE, BONED, 5, 6)
    else:
        p.shape(tail + tail2, body, dark, 6, 16)
        p.shape(ell_pts(370, 330 + bob, 155, 100, 48, -.15), body, dark, 6, 22)
        p.shape(ell_pts(400, 380 + bob, 110, 45, 32, -.15), BELLY, None, 0)
        for i in range(6):
            x = 300 + i * 34
            p.stroke([(x, 252 + bob - i * 4), (x + 12, 270 + bob - i * 4)], 4, dark)
    # pescoço
    nb = (470, 300 + bob); hd = (590, 165 + bob * .5)
    if fossil:
        for t in range(5):
            x = lerp(nb[0], hd[0] - 30, t / 4); y = lerp(nb[1], hd[1] + 30, t / 4)
            p.shape(ell_pts(x, y, 20, 16, 16), BONE, BONED, 4, 4)
    else:
        p.line(curve(nb, (540, 260 + bob), (hd[0] - 20, hd[1] + 40), 10), body, 72, 6)
    # braço
    sh = (480, 340 + bob)
    p.line([sh, (505, 390 + bob), (535, 385 + bob)], mul(body, .9), 14 if not fossil else 9, 4)
    leg(legs[1], False)
    # cabeça: maxila + mandíbula
    hx, hy = hd; m = mouth * .45
    jaw = [(hx - 70, hy + 20), (hx + 120, hy + 30), (hx + 115, hy + 52), (hx - 50, hy + 60)]
    jc, js = math.cos(m), math.sin(m)
    jaw = [(hx - 60 + (x - hx + 60) * jc - (y - hy - 20) * js, hy + 20 + (x - hx + 60) * js + (y - hy - 20) * jc) for x, y in jaw]
    if mouth > .05:
        p.poly([(hx - 40, hy + 20), (hx + 125, hy + 22), jaw[2], jaw[3]], hexc('#7a2430'))
        for i in range(5):
            x = hx - 10 + i * 26
            p.poly([(x, hy + 20), (x + 12, hy + 20), (x + 6, hy + 38)], (255, 255, 255), 2)
    p.shape(jaw, body, dark, 6, 8)
    up = [(hx - 80, hy - 20), (hx - 20, hy - 62), (hx + 80, hy - 48), (hx + 135, hy - 8), (hx + 130, hy + 24), (hx - 70, hy + 30)]
    p.shape(up, body, dark, 6, 12)
    if mouth <= .05 and not fossil:
        for i in range(4):
            x = hx + 10 + i * 26
            p.poly([(x, hy + 22), (x + 10, hy + 22), (x + 5, hy + 34)], (255, 255, 255), 2)
    p.stroke([(hx + 112, hy - 14), (hx + 122, hy - 8)], 4)
    ec = (hx + 5, hy - 22); er = 24 if expr == 'shock' else 21
    if fossil:
        p.dot(ec[0], ec[1], 22, hexc('#5a4a3a'), 3)
        p.dot(hx + 60, hy - 10, 14, hexc('#5a4a3a'), 3)
    else:
        p.dot(ec[0], ec[1], er, (255, 255, 255), 4)
        if blink < .75:
            lk = max(-1, min(1, look))
            p.dot(ec[0] + lk * (er - 10), ec[1] + 2, 9, INK)
            p.dot(ec[0] + lk * (er - 10) - 3, ec[1] - 2, 3, (255, 255, 255))
        else:
            p.poly([(ec[0] - er - 1, ec[1] - er - 2), (ec[0] + er + 1, ec[1] - er - 2), (ec[0] + er + 1, ec[1] + er), (ec[0] - er - 1, ec[1] + er)], body)
            p.stroke([(ec[0] - er, ec[1] + 4), (ec[0] + er, ec[1] + 4)], 4)
        p.stroke([(ec[0] - 24, ec[1] - 30), (ec[0] + 26, ec[1] - 24)], 6 if expr != 'shock' else 4)
    return fin(p)


def bandeira():
    p = Pen(420, 300)
    p.shape([(10, 10), (410, 10), (410, 290), (10, 290)], hexc('#1f9a48'), None, 6)
    p.poly([(210, 35), (385, 150), (210, 265), (35, 150)], hexc('#f8d231'))
    p.dot(210, 150, 72, hexc('#27408b'))
    p.arc(210, 175, 92, 50, 205, 335, 9, (255, 255, 255))
    return fin(p)


def osso_corte(cells=0.0, glow=0.0, shield=0.0):
    """corte de osso visto no microscópio: disco com canais; células vermelhas aparecem (cells 0-1). 700x700."""
    p = Pen(700, 700)
    p.shape(ell_pts(350, 350, 320, 320, 64), BONE, BONED, 7, 26)
    rnd = random.Random(4)
    pts = [(350, 350), (190, 230), (500, 220), (220, 480), (480, 470), (350, 150), (350, 560), (130, 360), (570, 350)]
    n = int(round(cells * len(pts) * 3))
    for i, (x, y) in enumerate(pts):
        r = 62 if i == 0 else 42
        p.dot(x, y, r + 6, BONED); p.dot(x, y, r, hexc('#7a5c46'))
        if shield: p.arc(x, y, r + 2, r + 2, 0, 360, 8, MNL)
        for j in range(3):
            if i * 3 + j < n:
                a = j * 2.1 + i; rr = r * .45
                cx, cy = x + rr * math.cos(a), y + rr * math.sin(a)
                p.shape(ell_pts(cx, cy, 15, 12, 20), REDL if glow else RED, REDD, 3, 4)
    for i in range(30):
        x = 60 + rnd.random() * 580; y = 60 + rnd.random() * 580
        if math.hypot(x - 350, y - 350) < 290: p.stroke([(x, y), (x + 14, y + 4)], 3, BONED)
    return fin(p)


def hemacia(o2=0.0):
    """glóbulo vermelho grande (disco com covinha). 500x400."""
    p = Pen(500, 400)
    p.shape(ell_pts(250, 200, 210, 150, 48), RED, REDD, 7, 20)
    p.shape(ell_pts(250, 195, 110, 70, 40), REDD, None, 0)
    p.stroke(curve((150, 120), (210, 85), (290, 92), 8), 10, REDL)
    return fin(p)


def bolha(txt_='O2'):
    p = Pen(160, 160)
    p.shape(ell_pts(80, 80, 66, 66, 32), hexc('#d6f1ff'), hexc('#9fd3ef'), 5, 8)
    fnt = ImageFont.truetype(kit.FONT.path, int(56 * art.K))
    tw = p.d.textlength(txt_, font=fnt)
    p.d.text((80 * art.K - tw / 2, 48 * art.K), txt_, font=fnt, fill=INK + (255,))
    return fin(p)


def capsula(on=1.0):
    """cápsula do tempo de cristal (hausmanita) em volta das células. 600x700."""
    p = Pen(600, 700)
    pts = [(300, 20), (520, 160), (560, 420), (420, 670), (180, 670), (40, 420), (80, 160)]
    p.shape(pts, MN, mul(MN, .7), 7, 24)
    p.shape([(300, 80), (470, 190), (500, 410), (390, 610), (210, 610), (100, 410), (130, 190)], hexc('#2c2f3d'), None, 0)
    for (x, y) in ((260, 300), (350, 360), (270, 440), (360, 470), (300, 380)):
        p.shape(ell_pts(x, y, 40, 32, 24), RED, REDD, 4, 6)
    p.stroke([(130, 190), (300, 80), (470, 190)], 8, MNL)
    p.stroke([(110, 220), (160, 330)], 10, (255, 255, 255))
    return fin(p)


def microscopio():
    p = Pen(500, 800)
    p.shape([(80, 700), (420, 700), (440, 790), (60, 790)], hexc('#3c4c6e'), hexc('#28344d'), 6, 10)
    p.line(curve((330, 700), (420, 450), (300, 230), 10), hexc('#3c4c6e'), 50, 6)
    p.shape([(160, 120), (260, 60), (330, 360), (240, 400)], hexc('#e6ebf2'), hexc('#aeb8c6'), 6, 10)
    p.shape([(120, 520), (380, 520), (380, 560), (120, 560)], hexc('#cfd6de'), None, 5)
    p.shape([(230, 400), (260, 400), (262, 470), (228, 470)], hexc('#8d98a8'), None, 4)
    return fin(p)


def revista():
    p = Pen(500, 650)
    p.shape([(30, 30), (470, 30), (470, 630), (30, 630)], (255, 255, 255), hexc('#d8d8d8'), 6, 12)
    p.shape([(30, 30), (470, 30), (470, 170), (30, 170)], hexc('#1d4f91'), None, 5)
    fnt = ImageFont.truetype(kit.FONT.path, int(100 * art.K))
    tw = p.d.textlength('PNAS', font=fnt)
    p.d.text((250 * art.K - tw / 2, 40 * art.K), 'PNAS', font=fnt, fill=(255, 255, 255, 255))
    p.shape(ell_pts(250, 370, 150, 150, 40), BONE, BONED, 5, 10)
    for x, y in ((210, 330), (290, 340), (250, 410)): p.dot(x, y, 26, RED, 3)
    for y in (560, 595): p.stroke([(80, y), (420, y)], 8, hexc('#c9c9c9'))
    return fin(p)


def put_dino(c, x, feet, h, flip=False, **kw):
    put_sprite(c, 'dino', x, feet, h, 800 / 600, flip, {'phase': 16, 'mouth': 6, 'look': 4}, **kw)


def put_img(c, fn, x, feet, h, aspect, **kw):
    put_sprite(c, fn, x, feet, h, aspect, False, {'cells': 9, 'glow': 1, 'shield': 4, 'on': 4}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def blk(f, seed):
    return 1 if blinkAt(f, seed) > .6 else 0


# ------------------------------------------------------------------ cenas
def s0(f):
    c = CEN('floresta', 'day').copy()
    q = wt(0, 'quinze') - 3
    b = wt(0, 'brasileiro') - 3
    r = wt(0, 'sangue') - 3
    mo = .9 * math.sin(clamp((f - r) / 22) * math.pi) if f >= r else 0
    put_dino(c, 600 + f * .3, 1640, 720, phase=(f * .025) % 1, mouth=mo, blink=blk(f, 1), expr='shock' if f >= b else 'calm')
    num(c, '115 MILHÕES', 640, 540, f, q, 115, -4)
    num(c, 'DE ANOS', 640, 670, f, q + 4, 95, 3)
    if f >= b:
        s = back(ramp(f, b, b + 10))
        paste_c(c, sprite('bandeira', (), 200, 1.4, False), 640, 830, s)
        num(c, 'BRASILEIRO!', 640, 990, f, b + 2, 100, -5)
    z = lerp(1.35, 1.1, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, b)
    return c, (640, 1150 + k * 10, z, k), 'day'


def s1(f):
    c = CEN('floresta', 'golden').copy()
    cv = wt(1, 'carnivoro') - 3
    ne = wt(1, 'Nordeste') - 3
    ar = wt(1, 'Araripe') - 3
    mo = .9 * math.sin(clamp((f - cv) / 24) * math.pi) if f >= cv else 0
    put_dino(c, 640, 1720, 760, phase=0, mouth=mo, blink=blk(f, 2), look=.6)
    num(c, 'ARATASAURUS', 640, 500, f, wt(1, 'Aratassauro') - 3, 100, -3)
    num(c, 'CARNÍVORO', 640, 630, f, cv, 85, 4)
    num(c, 'NORDESTE DO BRASIL', 640, 760, f, ne, 70, -3)
    if f >= ar:
        paste_c(c, sprite('bandeira', (), 150, 1.4, False), 330, 900, back(ramp(f, ar, ar + 10)))
        num(c, 'BACIA DO ARARIPE', 760, 900, f, ar + 2, 62, 3)
    t = smooth(ramp(f, 0, 80))
    k = kick(f, cv, .6)
    return c, (lerp(600, 680, t), lerp(1250, 1180, t) + k * 8, lerp(1.2, 1.08, t), k + 1.5 * math.sin(f * .05)), 'golden'


def s2(f):
    c = CEN('museu', 'day').copy()
    ca = wt(2, 'canais') - 3
    gl = wt(2, 'globulos') - 3
    bo = wt(2, 'bolinhas') - 3
    if False:
        put_dino(c, 640, 1560, 760, fossil=1)
        num(c, 'OSSOS DAS PERNAS', 640, 600, f, wt(2, 'ossos') - 3, 80, -3)
        t = smooth(ramp(f, 0, ca))
        return c, (lerp(640, 560, t), lerp(1250, 1400, t), lerp(1.05, 1.6, t), 0), 'day'
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    cells = ramp(f, bo, gl + 6)
    put_img(c, 'osso_corte', 640, 1450, 820, 1, cells=round(cells * 9) / 9)
    num(c, 'CANAIS DOS VASOS', 640, 540, f, ca, 72, -3)
    num(c, 'GLÓBULOS VERMELHOS!', 640, 680, f, gl, 66, 4)
    num(c, 'OSSO DA PERNA', 640, 1560, f, wt(2, 'ossos') - 3, 66, -3) if f < gl else None
    z = lerp(1.0, 1.15, smooth(ramp(f, ca, gl + 20))) * (1 + .0015 * f)
    k = kick(f, gl, .6)
    return c, (640, 1150 + k * 8, z, k), 'day'


def s3(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    he = wt(3, 'heme') - 3
    ox = wt(3, 'oxigenio') - 3
    put_img(c, 'microscopio', 330, 1700, 700, 500 / 800)
    put_sci(c, 980, 1720, 780, f, 2, arms='point' if f >= he else 'clip', expr='grin' if f >= he else 'neutral', skin=3, look=-1, glasses=True)
    s = back(ramp(f, 0, 12))
    paste_c(c, sprite('hemacia', (), 300, 1.25, False), 640, 880 + 8 * math.sin(f * .1), s)
    num(c, 'HEMOGLOBINA', 640, 560, f, wt(3, 'hemoglobina') - 3, 110, -4)
    num(c, 'HEME', 560, 1080, f, he, 110, 4)
    if f >= ox:
        for i in range(3):
            d0 = ox + i * 4; ss = back(ramp(f, d0, d0 + 8))
            paste_c(c, sprite('bolha', (), 110, 1, False), 420 + i * 220, 720 - 30 * math.sin(f * .08 + i), ss)
    t = smooth(ramp(f, 0, 120))
    return c, (640, lerp(1100, 1180, t), lerp(1.2, 1.1, t) * (1 + .0004 * f), 0), 'day'


def s4(f):
    c = BG('lab').copy()
    fr = wt(4, 'fresco') - 3
    ha = wt(4, 'hausmanita') - 3
    ca = wt(4, 'capsula') - 3
    if f < ha:
        put_img(c, 'osso_corte', 640, 1450, 820, 1, cells=1)
        if f >= fr: num(c, 'NÃO É SANGUE FRESCO', 640, 560, f, fr, 64, -3)
    else:
        on = back(ramp(f, ha, ha + 10))
        put_img(c, 'capsula', 640, 1500, 860 * on, 600 / 700)
        put_dust(c, 640, 1100, 200, f - ha)
        num(c, 'HAUSMANITA', 640, 520, f, ha + 2, 120, -4)
        num(c, 'CÁPSULA DO TEMPO', 640, 680, f, ca, 70, 3)
    z = lerp(1.1, 1.25, smooth(ramp(f, 0, 160))) * (1 + .0005 * f)
    k = kick(f, ha)
    return c, (640, 1150 + k * 10, z, k), 'dusk'


def s5(f):
    c = CEN('museu', 'dusk').copy()
    im = wt(5, 'importa') - 3
    tp = wt(5, 'tempo') - 3
    put_dino(c, 420, 1560, 700, fossil=1)
    put_sci(c, 960, 1720, 820, f, 1, arms='cheek' if f < tp else 'up', bun=True, skin=1, expr='shock' if f >= tp else 'neutral', look=-1)
    num(c, 'POR QUE IMPORTA?', 640, 560, f, im, 78, -4)
    if f >= wt(5, 'achavam') - 3:
        thought(c, 760, 820, 150, back(ramp(f, wt(5, 'achavam') - 3, wt(5, 'achavam') + 7)), txt('NÃO DURA!', 48))
    num(c, 'DUROU!', 480, 960, f, tp, 120, 5)
    k = kick(f, tp)
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0004 * f)
    return c, (640, 1200 + k * 10, z, k), 'dusk'


def s6(f):
    c = CEN('museu', 'dusk').copy()
    pn = wt(6, 'estudo') - 3
    mn = wt(6, 'Nacional') - 3
    ur = wt(6, 'Cariri') - 3
    ou = wt(6, 'outros') - 3
    put_dino(c, 760, 1600, 680, fossil=1)
    put_img(c, 'revista', 300, 1640, 560, 500 / 650)
    num(c, 'ESTUDO', 380, 980, f, pn, 85, -4)
    num(c, 'MUSEU NACIONAL', 640, 540, f, mn, 72, 3)
    num(c, 'UNIV. REGIONAL DO CARIRI', 640, 660, f, ur, 50, -3)
    if f >= ou:
        thought(c, 900, 880, 140, back(ramp(f, ou, ou + 10)), txt('???', 64))
    z = lerp(1.0, 1.12, easeOut(ramp(f, 0, 80))) * (1 + .0006 * f)
    return c, (640 + .12 * f, 1260, z, lerp(0, -2, smooth(ramp(f, ou, ou + 40)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'quinze') - 3, 140, .9)
    s.ting(s.W(0, 'brasileiro') - 3, .4)
    s.thunk(s.W(1, 'carnivoro') - 3, 120, .7)
    s.whoosh(s.W(2, 'canais') - 3, .4, .6)
    for i in range(5): s.ting(s.W(2, 'bolinhas') - 3 + i * 5, .12)
    s.ting(s.W(3, 'heme') - 3, .3)
    s.thunk(s.W(4, 'hausmanita') - 3, 200, .6)
    s.thunk(s.W(5, 'tempo') - 3, 180, .6)
    s.ting(s.W(6, 'Nacional') - 3, .25)
