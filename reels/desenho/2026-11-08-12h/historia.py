"""Um Café com o Mundo — CURIOSIDADE (domingo 08/11/2026, 12h).
Tema: o telescópio espacial Swift, da NASA, caiu e queimou na atmosfera sobre o norte de Sumatra (Indonésia).
Fontes (conferidas em 08/11/2026):
- NASA APOD 06/11/2026 "A Farewell to Swift": reentrada em 04/11/2026 às 7h39 (hora de Nova York) sobre a região
  do norte de Sumatra, Indonésia; quase 22 anos de operação; atividade solar maior acelerou a queda da órbita;
  missão de resgate para elevar a órbita "não teve sucesso"; dados seguem gerando descobertas por anos.
- CBS News: cerca de 3.200 libras (1,5 t); lançado em 20/11/2004 para missão de 2 anos; mais de 2.000 explosões
  de raios gama e 1.400 estrelas explodindo; robô de resgate de três braços "Link" (Katalyst Space) teve problema
  logo após o lançamento e nunca chegou a menos de 7 milhas (~11 km) do telescópio; risco 1 em 2.100.
- Live Science 04/11/2026: 1.450 kg; ciência encerrada em 20/10; arrasto da atmosfera aumentado pela atividade solar;
  sem danos ou feridos relatados; cerca de 7.000 estudos com dados do Swift.
Sem logotipos (nada de logo da NASA desenhado); telescópio e robô genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Um telescópio da NASA, de uma tonelada e meia, caiu do céu nesta semana.",
    "Foi na quarta, dia quatro, sobre o norte de Sumatra, na Indonésia, e quase tudo queimou antes de chegar ao chão.",
    "Ele se chamava Swift. Foi lançado em dois mil e quatro para durar dois anos, e trabalhou quase vinte e dois.",
    "Nesse tempo, flagrou mais de duas mil explosões de raios gama, as mais fortes do universo.",
    "Mas o Sol ficou mais agitado, o ar lá em cima inchou, e foi freando o telescópio.",
    "Um robô de resgate, com três braços, foi mandado para empurrá-lo para cima, mas nunca chegou a menos de onze quilômetros dele.",
    "Os dados ainda vão render descobertas por anos. Mas o céu perdeu um dos seus vigias mais rápidos.",
]
CAPTXT = [
    "Um telescópio da NASA, de 1,5 tonelada,|caiu do céu nesta semana.",
    "Foi na quarta, dia 4, sobre o norte de Sumatra, na Indonésia,|e quase tudo queimou antes de chegar ao chão.",
    "Ele se chamava Swift. Foi lançado em 2004 para durar 2 anos,|e trabalhou quase 22.",
    "Nesse tempo, flagrou mais de 2.000 explosões de raios gama,|as mais fortes do universo.",
    "Mas o Sol ficou mais agitado, o ar lá em cima inchou,|e foi freando o telescópio.",
    "Um robô de resgate, com 3 braços, foi mandado para empurrá-lo para cima,|mas nunca chegou a menos de 11 km dele.",
    "Os dados ainda vão render descobertas por anos.|Mas o céu perdeu um dos seus vigias mais rápidos.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'tonelada', 4), (1, 'sumatra', 4), (2, 'dois', 4), (2, 'vinte', 6), (3, 'duas', 4), (4, 'sol', 4), (5, 'onze', 6), (6, 'vigias', 6)]

WHITE = (255, 255, 255)
GOLD = hexc('#e8b440'); GOLD_D = hexc('#b8862a')
SILV = hexc('#dfe3ea'); SILV_D = hexc('#a9b0bd')
PANEL = hexc('#3b5fb0'); PANEL_D = hexc('#26407c')
RED = hexc('#d8443c')


# ------------------------------------------------------------------ desenhos novos
def satelite(look=0.0, expr='calm', blink=0, fire=0.0):
    """telescópio espacial genérico (corpo dourado, tubo branco à direita, 2 painéis solares). 800x500, centro (400,250)."""
    p = Pen(800, 500)
    if fire > 0:
        for i, (col, s) in enumerate(((hexc('#f7d046'), 1.0), (hexc('#f08a2c'), .78), (hexc('#fff3c0'), .5))):
            L = 330 * fire * s
            p.poly(curve((250, 250 - 120 * s), (250 - L * .6, 250 - 60 * s), (250 - L, 250), 10) +
                   curve((250 - L, 250), (250 - L * .6, 250 + 60 * s), (250, 250 + 120 * s), 10), col, 0 if i else 4)
    # painéis solares (atrás, em cima e embaixo)
    for y0, y1 in ((20, 150), (350, 480)):
        p.shape([(230, y0), (430, y0), (430, y1), (230, y1)], PANEL, PANEL_D, 5, 8)
        for x in (280, 330, 380): p.stroke([(x, y0 + 6), (x, y1 - 6)], 3, hexc('#8fb0e8'))
        p.stroke([(236, (y0 + y1) / 2), (424, (y0 + y1) / 2)], 3, hexc('#8fb0e8'))
        p.stroke([(330, y1 if y0 < 200 else y0), (330, 175 if y0 < 200 else 325)], 8, hexc('#6b6b70'))
    # tubo do telescópio
    p.shape([(400, 185), (700, 175), (700, 325), (400, 315)], SILV, SILV_D, 6, 14)
    p.shape(ell_pts(705, 250, 34, 78, 30), hexc('#2b2f3e'), None, 6)
    p.dot(705, 250, 22, hexc('#556a9a'))
    p.stroke([(470, 182), (470, 318)], 4, SILV_D); p.stroke([(600, 178), (600, 322)], 4, SILV_D)
    # corpo dourado
    p.shape([(230, 160), (430, 160), (430, 340), (230, 340)], GOLD, GOLD_D, 6, 16)
    for i in range(5): p.stroke([(245 + i * 38, 175), (262 + i * 38, 325)], 3, hexc('#f4d27a'))
    # olho
    ex, ey, er = 330, 240, 48 if expr == 'shock' else 42
    p.dot(ex, ey, er, WHITE, 5)
    L = .5 if expr == 'sad' else 0
    L = max(L, blink)
    if L < .75:
        lk = max(-1, min(1, look))
        p.dot(ex + lk * (er - 20), ey + 2, 13 if expr == 'shock' else 17, INK)
        p.dot(ex + lk * (er - 20) - 5, ey - 4, 5, WHITE)
    if L > .02:
        top = ey - er; yb = top + 2 * er * L
        p.poly([(ex - er - 1, top - 2), (ex + er + 1, top - 2), (ex + er + 1, yb), (ex - er - 1, yb)], GOLD)
        p.stroke([(ex - er, yb), (ex + er, yb)], 5)
    if expr == 'shock': p.arc(ex, ey - 64, 26, 10, 200, 340, 5)
    if expr == 'sad': p.stroke([(ex - 34, ey - 58), (ex + 30, ey - 70)], 5)
    if expr == 'proud': p.stroke([(ex - 34, ey - 66), (ex + 30, ey - 58)], 5)
    return p.img


def robo(look=0.0, blink=0, sad=0, arm=0.0):
    """robô de resgate genérico de 3 braços. 600x600, centro (300,300)."""
    p = Pen(600, 600)
    c0 = (300, 300)
    for k, a0 in enumerate((-60, 60, 180)):
        a = math.radians(a0 + arm * 25 * (1 if k != 1 else -1))
        x1, y1 = c0[0] + 170 * math.cos(a), c0[1] + 170 * math.sin(a)
        x2, y2 = c0[0] + 250 * math.cos(a + .3), c0[1] + 250 * math.sin(a + .3)
        p.line([c0, (x1, y1), (x2, y2)], hexc('#8a8f99'), 18, 5)
        for s in (-1, 1):
            p.line([(x2, y2), (x2 + 34 * math.cos(a + .3 + s * .6), y2 + 34 * math.sin(a + .3 + s * .6))], hexc('#6b6b70'), 10, 4)
        p.dot(x1, y1, 12, hexc('#6b6b70'), 4)
    hexa = [(c0[0] + 120 * math.cos(math.radians(30 + 60 * i)), c0[1] + 120 * math.sin(math.radians(30 + 60 * i))) for i in range(6)]
    p.shape(hexa, hexc('#e9e4da'), hexc('#bdb6a8'), 6, 14)
    p.shape(ell_pts(300, 300, 70, 70, 36), hexc('#2b2f3e'), None, 5)
    er = 46; ex, ey = 300, 300
    p.dot(ex, ey, er, WHITE)
    if blink < .6:
        lk = max(-1, min(1, look))
        p.dot(ex + lk * 20, ey + 2, 18, hexc('#2f8fd8'))
        p.dot(ex + lk * 20, ey + 2, 9, INK)
    else:
        p.stroke([(ex - er, ey), (ex + er, ey)], 5)
    if sad: p.stroke([(ex - 40, ey - 62), (ex + 34, ey - 50)], 6)
    return p.img


def sol(angry=0, blink=0):
    """Sol com cara. 700x700, centro (350,350)."""
    p = Pen(700, 700)
    for i in range(14):
        a = i * 2 * math.pi / 14
        r1 = 230 + (60 if angry else 30) * (i % 2)
        p.poly([(350 + 190 * math.cos(a - .14), 350 + 190 * math.sin(a - .14)), (350 + (r1 + 70) * math.cos(a), 350 + (r1 + 70) * math.sin(a)),
                (350 + 190 * math.cos(a + .14), 350 + 190 * math.sin(a + .14))], hexc('#f6a733'), 4)
    p.shape(ell_pts(350, 350, 210, 210, 60), hexc('#f7d046'), hexc('#e0a92a'), 7, 28)
    for s in (-1, 1):
        ex, ey = 350 + s * 75, 320
        p.dot(ex, ey, 34, WHITE, 5)
        if blink < .6: p.dot(ex - s * 4, ey + 6, 15, INK)
        if angry:
            p.stroke([(ex - 46, ey - 40 + s * 18), (ex + 46, ey - 40 - s * 18)], 9)
    if angry:
        p.arc(350, 450, 60, 22, 200, 340, 8)
    else:
        p.arc(350, 410, 60, 30, 20, 160, 8)
    return p.img


def explosao(col='#b48cff', k=0):
    """estouro de raios gama: estrela de pontas. 500x500."""
    p = Pen(500, 500)
    rnd = random.Random(k)
    n = 10
    pts = []
    for i in range(n * 2):
        a = i * math.pi / n + rnd.random() * .1
        r = 230 if i % 2 == 0 else 95
        r *= .8 + rnd.random() * .25
        pts.append((250 + r * math.cos(a), 250 + r * math.sin(a)))
    p.shape(pts, hexc(col), mul(hexc(col), .75), 6, 10)
    p.shape(ell_pts(250, 250, 70, 70, 30), hexc('#fff6d8'), None, 0)
    return p.img


@lru_cache(maxsize=4)
def orbita_bg(atm=0):
    """espaço com estrelas e a Terra grande embaixo (oceano + terra), faixa de atmosfera azul clara. palco inteiro."""
    p = Pen(BW, BH)
    base = Image.new('RGBA', (BW, BH), hexc('#0e1436') + (255,))
    rnd = random.Random(11)
    for i in range(190):
        p.dot(rnd.randint(0, BW), rnd.randint(0, 1700), rnd.choice((2, 2, 3, 4)), (255, 255, 230))
    cx, cy, R = 621, 3300, 1650
    glow = 40 + atm * 70
    p.poly(ell_pts(cx, cy, R + glow, R + glow, 160), hexc('#7fc3ff') if not atm else hexc('#a8d6ff'))
    p.shape(ell_pts(cx, cy, R, R, 160), hexc('#3a7fd0'), hexc('#2a5fa4'), 7, 40)
    for lx, ly, rx, ry in ((300, 1760, 260, 120), (880, 1820, 220, 150), (620, 2000, 300, 140)):
        p.shape(ell_pts(lx, ly, rx, ry, 40, .2), hexc('#7fb05a'), hexc('#5f8a40'), 5, 12)
    for wx, wy in ((150, 1900), (520, 1700), (1050, 1950)):
        p.shape(ell_pts(wx, wy, 120, 34, 30), WHITE, hexc('#dfe6ef'), 0, 6)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


@lru_cache(maxsize=2)
def mapa_sumatra():
    """mar com a ilha de Sumatra na diagonal (noroeste-sudeste) e um pedaço da península à direita."""
    p = Pen(BW, BH)
    base = Image.new('RGBA', (BW, BH), hexc('#5fa8d8') + (255,))
    rnd = random.Random(3)
    for i in range(34):
        x, y = rnd.randint(0, BW), rnd.randint(0, BH)
        p.stroke([(x, y), (x + 40, y - 6), (x + 80, y)], 4, hexc('#7cbde6'))
    ilha = [(80, 420), (210, 380), (380, 560), (560, 760), (760, 980), (960, 1220), (1120, 1440), (1160, 1560),
            (1060, 1600), (900, 1480), (700, 1300), (500, 1080), (320, 860), (150, 640), (60, 500)]
    sm = []
    for i in range(len(ilha)):
        a, b, c = ilha[i - 1], ilha[i], ilha[(i + 1) % len(ilha)]
        sm += curve(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), b, ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2), 8)
    p.shape(sm, hexc('#9ccf6a'), hexc('#79a94c'), 7, 22)
    pen = [(820, -40), (1000, 120), (1150, 380), (1300, 520), (1300, -40)]
    p.shape(pen, hexc('#9ccf6a'), hexc('#79a94c'), 7, 16)
    for mx, my in ((300, 620), (520, 860), (760, 1110)):
        p.shape([(mx - 60, my + 40), (mx, my - 50), (mx + 60, my + 40)], hexc('#7e9a55'), hexc('#5f7a40'), 4, 6)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


def put_sat(c, x, y, w, rot=0, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    if 'fire' in kw: kw['fire'] = round(kw['fire'] * 6) / 6
    im = sprite('satelite', tuple(sorted(kw.items())), int(w * 500 / 800), 800 / 500, False)
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def put_robo(c, x, y, w, rot=0, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    if 'arm' in kw: kw['arm'] = round(kw['arm'] * 6) / 6
    im = sprite('robo', tuple(sorted(kw.items())), int(w), 1.0, False)
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def bola_fogo(c, x, y, f, s=1.0, ang=-35):
    """meteoro/rastro de fogo descendo (cabeça em x,y; rastro para cima-esquerda)."""
    d = ImageDraw.Draw(c, 'RGBA')
    a = math.radians(ang)
    for i in range(14):
        t = i / 14
        r = (60 - 40 * t) * s * (1 + .1 * math.sin(f * .7 + i))
        xx = x - math.cos(a) * 520 * t * s; yy = y + math.sin(a) * 520 * t * s
        col = (255, int(240 - 140 * t), int(120 - 100 * t), int(240 * (1 - t)))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=col)
    d.ellipse([x - 34 * s, y - 34 * s, x + 34 * s, y + 34 * s], fill=(255, 250, 220, 255))


def estrelas(c, f, seed=5, n=60, y1=1300):
    d = ImageDraw.Draw(c, 'RGBA'); rnd = random.Random(seed)
    for i in range(n):
        x, y = rnd.randint(0, BW), rnd.randint(0, y1)
        r = 2 + 2 * (0.5 + 0.5 * math.sin(f * .15 + i))
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 230, 220))


# ------------------------------------------------------------------ cenas
def s0(f):
    # gancho: o telescópio pegando fogo e caindo em direção à Terra
    c = orbita_bg(0).copy()
    t0 = wt(0, 'caiu') - 3
    t = ramp(f, t0 - 10, t0 + 50)
    x = lerp(560, 760, smooth(t)); y = lerp(820, 1120, smooth(t))
    fire = ramp(f, t0 - 6, t0 + 10)
    put_sat(c, x, y, 900, rot=-8 - 22 * smooth(t) + 2 * math.sin(f * .3) * fire, look=.6 if f < t0 else 1,
            expr='shock' if f >= t0 - 4 else 'calm', blink=0 if f >= t0 - 4 else blinkAt(f, 2), fire=fire)
    num(c, '1,5 TONELADA', 620, 420, f, wt(0, 'tonelada') - 4, 120, -4)
    z = lerp(1.45, 1.1, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, t0)
    return c, (640 + 10 * math.sin(f * .05), 1050 + k * 10, z, k + lerp(0, -2, smooth(t))), 'day'


def s1(f):
    # mapa: Sumatra, marcador e bola de fogo
    c = mapa_sumatra().copy()
    num(c, 'QUARTA, 4/11', 600, 360, f, wt(1, 'quarta') - 3, 100, -3)
    m0 = wt(1, 'sumatra') - 3
    num(c, 'SUMATRA', 600, 960, f, m0, 110, -42)
    num(c, 'INDONÉSIA', 680, 1330, f, wt(1, 'indonesia') - 3, 90, -4)
    if f >= m0:
        sc = back(ramp(f, m0, m0 + 8))
        d = ImageDraw.Draw(c)
        x, y = 300, 640
        pr = 26 + 14 * ((f - m0) % 30) / 30
        d.ellipse([x - pr * 2, y - pr, x + pr * 2, y + pr], outline=RED, width=5)
        r = 34 * sc
        d.ellipse([x - r - 5, y - 2.6 * r - 5, x + r + 5, y - .6 * r + 5], fill=INK)
        d.polygon([(x - r * .8, y - 1.6 * r), (x + r * .8, y - 1.6 * r), (x, y - 8)], fill=RED)
        d.ellipse([x - r, y - 2.6 * r, x + r, y - .6 * r], fill=RED)
        d.ellipse([x - r * .4, y - 2 * r, x + r * .4, y - 1.2 * r], fill=WHITE)
    q0 = wt(1, 'queimou') - 3
    tt = ramp(f, q0 - 25, q0 + 25)
    if 0 < tt < 1 or f >= q0 - 25:
        fx = lerp(-100, 330, smooth(tt)); fy = lerp(150, 560, smooth(tt))
        bola_fogo(c, fx, fy, f, lerp(1.0, .3, smooth(ramp(f, q0, q0 + 30))))
    t = smooth(ramp(f, 0, 70))
    k = kick(f, m0, .6)
    return c, (lerp(640, 560, t), lerp(900, 980, t) + k * 10, lerp(1.0, 1.15, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    # o Swift em órbita, orgulhoso: 2004 -> 2 anos? -> 22 anos!
    c = CEN('espaco', 'day').copy()
    put_sat(c, 640, 1000 + 14 * math.sin(f * .08), 950, rot=4 * math.sin(f * .03), look=-.3,
            expr='proud' if f >= wt(2, 'vinte') - 3 else 'calm', blink=blinkAt(f, 4))
    num(c, 'SWIFT', 640, 430, f, wt(2, 'swift') - 3, 150, -3)
    num(c, '2004', 300, 660, f, wt(2, 'dois') - 3, 110, -6)
    d0 = wt(2, 'durar') - 2
    if f >= d0 and f < wt(2, 'vinte') - 3:
        paste_c(c, txt('2 ANOS?', 100, 5), 920, 660, back(ramp(f, d0, d0 + 8)))
    num(c, 'QUASE 22 ANOS!', 640, 1380, f, wt(2, 'vinte') - 3, 100, 3)
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 90)))
    k = kick(f, wt(2, 'vinte') - 3, .6)
    return c, (640, 1000 + k * 10, z, k), 'day'


def s3(f):
    # explosões de raios gama pipocando; o telescópio vira para cada uma
    c = CEN('espaco', 'day').copy()
    e0 = wt(3, 'explosoes') - 6
    spots = [(250, 450, '#b48cff'), (1000, 560, '#ff7ab6'), (330, 250, '#7fe0ff'), (1060, 1150, '#ffd25a'), (640, 380, '#ff9b5a'), (180, 950, '#9bffb0')]
    lk = -.3
    for i, (x, y, col) in enumerate(spots):
        b0 = e0 - 30 + i * 9
        if f >= b0:
            age = f - b0
            s = back(ramp(f, b0, b0 + 7)) * (1 - .35 * ramp(age, 20, 60))
            im = sprite('explosao', (('col', col), ('k', i)), int(260 * s) + 1, 1.0, False)
            paste_c(c, im.rotate((f * 2 + i * 40) % 360, resample=Image.BICUBIC), x, y)
            lk = 1 if x > 640 else -1
    put_sat(c, 640, 900, 820, rot=3 * math.sin(f * .05), look=lk, expr='shock' if f >= e0 - 30 else 'calm', blink=0)
    num(c, '+ DE 2.000', 640, 1280, f, wt(3, 'duas') - 3, 140, -3)
    num(c, 'RAIOS GAMA', 640, 1440, f, wt(3, 'raios') - 3, 90, 3)
    z = lerp(1.2, 1.05, smooth(ramp(f, 0, 80)))
    return c, (640 + 14 * math.sin(f * .04), 980, z * (1 + .0005 * f), 0), 'day'


def s4(f):
    # o Sol agitado; atmosfera incha; telescópio desce
    s0_ = wt(4, 'sol') - 3
    i0 = wt(4, 'inchou') - 3
    c = orbita_bg(1 if f >= i0 else 0).copy()
    sc = back(ramp(f, s0_, s0_ + 10))
    if sc > .05:
        im = sprite('sol', (('angry', 1 if f >= wt(4, 'agitado') - 3 else 0), ('blink', 0)), int(460 * sc), 1.0, False)
        paste_c(c, im.rotate(f * 1.5 % 360, resample=Image.BICUBIC), 1000, 380)
    fr = wt(4, 'freando') - 3
    t = ramp(f, i0, fr + 40)
    put_sat(c, lerp(420, 520, t), lerp(900, 1150, smooth(t)), 720, rot=-10 * smooth(t), look=1 if f >= s0_ else 0,
            expr='shock' if f >= fr else ('sad' if f >= i0 else 'calm'), blink=0 if f >= fr else blinkAt(f, 5))
    if f >= fr:
        d = ImageDraw.Draw(c)
        x, y = 240, 1000 + 20 * math.sin(f * .2)
        d.line([(x, y - 140), (x, y + 60)], fill=INK, width=34)
        d.line([(x, y - 140), (x, y + 60)], fill=RED, width=22)
        d.polygon([(x - 56, y + 40), (x + 56, y + 40), (x, y + 130)], fill=RED, outline=INK, width=6)
    num(c, 'FREIO!', 640, 1430, f, fr, 140, 4)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 100)))
    k = kick(f, s0_, .7)
    return c, (680, 1000 + k * 10, z, k), 'dusk'


def s5(f):
    # robô de resgate tenta chegar, engasga e fica longe
    c = CEN('espaco', 'dusk').copy()
    r0 = wt(5, 'robo') - 3
    m0 = wt(5, 'mas') - 3
    rx = lerp(-200, 380, smooth(ramp(f, r0, r0 + 45)))
    ry = 1050 + 30 * math.sin(f * .1)
    stuck = f >= m0
    rot = (8 * math.sin(f * .6) if stuck else 0)
    if stuck: rx -= 40 * smooth(ramp(f, m0, m0 + 40))
    if f >= r0 and not stuck:
        bola = ImageDraw.Draw(c, 'RGBA')
        for i in range(5):
            bola.ellipse([rx - 230 - i * 40, ry - 30 + i * 3, rx - 170 - i * 40, ry + 30 - i * 3], fill=(255, 200, 90, 200 - i * 35))
    if stuck:
        for i in range(4):
            age = (f - m0 + i * 9) % 36
            rr = 20 + age * 2
            ImageDraw.Draw(c, 'RGBA').ellipse([rx - 160 - age * 4 - rr, ry - 120 - age * 3 - rr, rx - 160 - age * 4 + rr, ry - 120 - age * 3 + rr], fill=(120, 120, 130, max(0, 180 - age * 5)))
    put_robo(c, rx, ry, 540, rot=rot, look=1, blink=blinkAt(f, 7) if not stuck else 0, sad=1 if stuck else 0,
             arm=.5 + .5 * math.sin(f * .2))
    put_sat(c, 960, 760 + 10 * math.sin(f * .07), 500, rot=-6, look=-1, expr='sad' if stuck else 'calm', blink=blinkAt(f, 9))
    num(c, '3 BRAÇOS', 380, 760, f, wt(5, 'tres') - 3, 100, -4)
    o0 = wt(5, 'onze') - 3
    if f >= o0:
        s = back(ramp(f, o0, o0 + 8))
        d = ImageDraw.Draw(c)
        y = 1300
        x0, x1 = rx + 180, 1000
        d.line([(x0, y), (x1, y)], fill=INK, width=int(18 * s) + 1)
        d.line([(x0, y), (x1, y)], fill=WHITE, width=int(10 * s) + 1)
        for xx, sg in ((x0, 1), (x1, -1)):
            d.polygon([(xx, y), (xx + sg * 40, y - 26), (xx + sg * 40, y + 26)], fill=WHITE, outline=INK, width=5)
        paste_c(c, txt('11 KM', 130, -3), (x0 + x1) / 2, y - 110, s)
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 90))) * (1 + .0005 * f)
    k = kick(f, m0, .6)
    return c, (640, 1020 + k * 10, z, k + (-2 * smooth(ramp(f, m0, m0 + 20)))), 'dusk'


def s6(f):
    # fim: cientista no alto da montanha, à noite, olha o céu; uma estrela cadente passa
    c = CEN('montanha', 'dusk').copy()
    estrelas(c, f, 5, 70, 900)
    d0 = wt(6, 'descobertas') - 3
    if f < wt(6, 'mas') - 3: num(c, 'DESCOBERTAS POR ANOS', 640, 720, f, d0, 62, -3)
    v0 = wt(6, 'vigias') - 3
    tt = ramp(f, v0 - 20, v0 + 30)
    if 0 < tt < 1:
        bola_fogo(c, lerp(1300, 300, tt), lerp(520, 900, tt), f, .45, ang=-20)
    put_sci(c, 600, 1720, 760, f, 3, arms='point' if f >= v0 - 20 else 'clip', skin=2, glasses=True,
            expr='neutral', look=1 if f < v0 else -1)
    z = lerp(1.15, 1.3, smooth(ramp(f, 0, 140)))
    return c, (640, lerp(1080, 1180, smooth(ramp(f, 0, 140))), z, lerp(0, -2, smooth(ramp(f, v0 - 20, v0 + 30)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.whoosh(s.W(0, 'caiu') - 3, .5, .6)
    s.thunk(s.W(0, 'tonelada') - 4, 140, .9)
    s.thunk(s.W(1, 'sumatra') - 3, 200, .7)
    s.whoosh(s.W(1, 'queimou') - 10, .4, .5)
    s.ting(s.W(2, 'swift') - 3, .3)
    s.thunk(s.W(2, 'vinte') - 3, 160, .8)
    for i in range(6): s.ting(s.W(3, 'explosoes') - 36 + i * 9, .18)
    s.thunk(s.W(3, 'duas') - 3, 140, .8)
    s.thunk(s.W(4, 'sol') - 3, 120, .6)
    s.whoosh(s.W(4, 'freando') - 3, .4, .5)
    s.engine(s.W(5, 'robo') - 3, s.W(5, 'mas') - 3, .2)
    s.thunk(s.W(5, 'onze') - 3, 180, .8)
    s.whoosh(s.W(6, 'vigias') - 20, .35, .5)
