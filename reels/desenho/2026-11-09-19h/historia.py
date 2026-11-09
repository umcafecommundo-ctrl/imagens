"""Um Café com o Mundo — O MUNDO EXPLICADO (segunda 09/11/2026, 19h).
Tema: o jornal russo Novaya Gazeta fecha a redação em Moscou (09/11/2026), citando pressão do governo.
Fontes (conferidas em 09/11/2026):
- Al Jazeera, 09/11/2026 ("Russian investigative newspaper Novaya Gazeta closes citing gov't clampdown"): última reunião de pauta
  e fechamento da redação na segunda 09/11; declarado "agente estrangeiro" em setembro de 2026; bancos pararam de processar as
  doações dos leitores; ordem de deixar o escritório até 09/11; cofundado por Gorbachev e financiado com dinheiro do Nobel da Paz
  dele (1990); Kremlin: "ciclo normal de mudança"; Volker Turk (ONU): "golpe devastador".
- AP via ABC News / Washington Post, 09/11/2026: fundado em 1993; último grande veículo independente crítico ao Kremlin ainda ativo na
  Rússia; seis jornalistas mortos, entre eles Anna Politkovskaya (2006); Dmitry Muratov dividiu o Nobel da Paz de 2021; governo
  bloqueou as plataformas online, tomou a gráfica, cassou o registro e fechou o sistema de doações; placa nova no prédio:
  "Aqui viveu o Novaya Gazeta"; editor-chefe Sergei Sokolov diz acreditar que o jornal voltará "com força renovada".
Tom sério; personagens genéricos; sem pessoas reais desenhadas."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O último grande jornal independente da Rússia fechou as portas nesta segunda-feira.",
    "O Novaya Gazeta nasceu em Moscou, em mil novecentos e noventa e três, com ajuda do dinheiro do Nobel da Paz de Mikhail Gorbachev.",
    "Investigou corrupção e abusos, e perdeu seis jornalistas assassinados, entre eles Anna Politkovskaya.",
    "Em dois mil e vinte e um, o editor Dmitry Muratov também ganhou o Nobel da Paz.",
    "Mas, depois da invasão da Ucrânia, o governo bloqueou o site, tomou a gráfica, e em setembro chamou o jornal de agente estrangeiro.",
    "Os bancos cortaram as doações dos leitores, e a redação foi despejada.",
    "Na porta, ficou uma placa: aqui viveu o Novaya Gazeta. O editor diz que um dia o jornal vai voltar.",
]
CAPTXT = [
    "O último grande jornal independente|da Rússia fechou as portas|nesta segunda-feira.",
    "O Novaya Gazeta nasceu em Moscou, em 1993,|com ajuda do dinheiro do Nobel da Paz|de Mikhail Gorbachev.",
    "Investigou corrupção e abusos, e perdeu|6 jornalistas assassinados,|entre eles Anna Politkovskaya.",
    "Em 2021, o editor Dmitry Muratov|também ganhou o Nobel da Paz.",
    "Mas, depois da invasão da Ucrânia, o governo|bloqueou o site, tomou a gráfica, e em setembro|chamou o jornal de agente estrangeiro.",
    "Os bancos cortaram as doações dos leitores,|e a redação foi despejada.",
    "Na porta, ficou uma placa: aqui viveu|o Novaya Gazeta. O editor diz que|um dia o jornal vai voltar.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'ultimo', 4), (0, 'Russia', 4), (0, 'segundafeira', 4), (1, 'Moscou', 4), (1, 'mil', 6), (1, 'Nobel', 4),
         (2, 'corrupcao', 4), (2, 'seis', 4), (3, 'dois', 6), (3, 'Nobel', 4), (4, 'site', 4), (4, 'grafica', 4),
         (4, 'agente', 4), (5, 'bancos', 4), (5, 'despejada', 4), (6, 'placa', 4), (6, 'voltar', 4)]

RED = hexc('#d8443c'); RED_D = hexc('#a02c26'); WHITE = (255, 255, 255)
PAPER = hexc('#f4efe3'); PAPER_D = hexc('#cfc6b2'); GOLD = hexc('#f2c14e'); GOLD_D = hexc('#b8862a')
RUS_B = hexc('#1c57a5'); DARK = hexc('#2b2d3a'); WALL = hexc('#c9b8a6'); WALL_D = hexc('#a08f7e')
DOOR = hexc('#7a4e33'); DOOR_D = hexc('#57361f')


def escurece(c, a):
    if a <= 0: return
    c.alpha_composite(Image.new('RGBA', c.size, (20, 18, 40, int(a))))


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def pessoa(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550'):
    """pessoa genérica de terno. 600x1000, pés y~975."""
    oc, od = P.COAT, P.COAT_D
    P.COAT = hexc(suit); P.COAT_D = mul(hexc(suit), .7)
    try:
        img = P.scientist(expr=expr, arms=arms if arms != 'clip' else 'hang', blink=blink, look=look, tilt=tilt, skin=skin, hair=hair, glasses=False)
    finally:
        P.COAT, P.COAT_D = oc, od
    p = Pen(600, 1000); p.img = img; p.d = ImageDraw.Draw(img)
    p.poly([(270, 418), (330, 418), (300, 470)], (255, 255, 255), 3)
    p.shape([(290, 430), (310, 430), (318, 540), (300, 566), (282, 540)], hexc(tie), mul(hexc(tie), .75), 3, 3)
    return p.img


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


@lru_cache(maxsize=2)
def jornal():
    """jornal dobrado genérico (sem nome real). 640x820"""
    p = Pen(640, 820)
    p.shape([(30, 30), (610, 50), (600, 800), (40, 790)], PAPER, PAPER_D, 7, 16)
    p.shape([(70, 80), (570, 92), (568, 190), (70, 180)], DARK, INK, 4, 0)
    for k in range(3):
        y = 240 + k * 40
        p.stroke([(80, y), (560, y + 6)], 14, hexc('#55505a'))
    p.shape([(80, 380), (300, 384), (298, 600), (80, 596)], hexc('#9fb7cf'), hexc('#7891ab'), 4, 3)
    for k in range(9):
        y = 390 + k * 42
        p.stroke([(330, y), (560, y + 3)], 8, hexc('#8a8590'))
    for k in range(4):
        y = 640 + k * 38
        p.stroke([(80, y), (560, y + 3)], 8, hexc('#8a8590'))
    return fin(p)


@lru_cache(maxsize=2)
def medalha():
    """medalha dourada genérica com fita. 360x520"""
    p = Pen(360, 520)
    p.shape([(110, 10), (170, 10), (200, 240), (150, 260)], RED, RED_D, 5, 4)
    p.shape([(250, 10), (190, 10), (160, 240), (210, 260)], hexc('#2f6fd6'), hexc('#1f4f9e'), 5, 4)
    p.shape(ell_pts(180, 360, 140, 140), GOLD, GOLD_D, 7, 14)
    p.shape(ell_pts(180, 360, 95, 95), hexc('#f7d77a'), GOLD_D, 4, 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_rus():
    p = Pen(420, 280)
    p.poly([(10, 10), (410, 10), (410, 96), (10, 96)], WHITE)
    p.poly([(10, 96), (410, 96), (410, 183), (10, 183)], RUS_B)
    p.poly([(10, 183), (410, 183), (410, 270), (10, 270)], RED)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def grafica():
    """máquina de impressão genérica (rolos). 760x520, base y~510"""
    p = Pen(760, 520)
    p.shape([(40, 200), (720, 200), (720, 510), (40, 510)], hexc('#7d8590'), hexc('#5b626c'), 7, 14)
    for cx in (200, 380, 560):
        p.shape(ell_pts(cx, 200, 80, 80), hexc('#a9b0bb'), hexc('#7d8590'), 6, 8)
        p.dot(cx, 200, 22, INK, 0)
    p.shape([(60, 330), (700, 330), (700, 360), (60, 360)], PAPER, PAPER_D, 4, 2)
    return fin(p)


def tela(c, x, y, f, blocked):
    """computador com site do jornal; bloqueado = tela vermelha com cadeado."""
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([x - 260, y - 190, x + 260, y + 150], 20, fill=hexc('#3a3d4d'), outline=INK, width=7)
    d.rectangle([x - 230, y - 160, x + 230, y + 120], fill=(RED if blocked else WHITE), outline=INK, width=4)
    if not blocked:
        d.rectangle([x - 210, y - 140, x + 210, y - 90], fill=DARK)
        for k in range(5):
            d.line([(x - 200, y - 60 + k * 32), (x + 200, y - 60 + k * 32)], fill=hexc('#8a8590'), width=10)
    else:
        d.rounded_rectangle([x - 60, y - 40, x + 60, y + 70], 12, fill=GOLD, outline=INK, width=6)
        d.arc([x - 45, y - 110, x + 45, y - 10], 180, 360, fill=INK, width=14)
    d.rectangle([x - 30, y + 150, x + 30, y + 220], fill=hexc('#3a3d4d'), outline=INK, width=5)
    d.rounded_rectangle([x - 140, y + 210, x + 140, y + 240], 10, fill=hexc('#3a3d4d'), outline=INK, width=5)


def carimbo(c, s, x, y, sc):
    if sc <= .05: return
    im = Image.new('RGBA', (900, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([10, 10, 890, 210], 24, outline=RED, width=14)
    t = txt(s, 74, 0)
    im.alpha_composite(t, (450 - t.size[0] // 2, 110 - t.size[1] // 2))
    im = im.rotate(-8, expand=True, resample=Image.BICUBIC)
    paste_c(c, im, x, y, sc)


def vela(c, x, y, f, i):
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([x - 26, y - 150, x + 26, y], 8, fill=hexc('#f6f1e4'), outline=INK, width=5)
    fl = 1 + .12 * math.sin(f * .5 + i * 1.7)
    d.ellipse([x - 16 * fl, y - 210 * fl + (fl - 1) * 150, x + 16 * fl, y - 156], fill=GOLD, outline=INK, width=4)
    d.ellipse([x - 7, y - 185, x + 7, y - 162], fill=WHITE)


def predio(c, x, base, w, h, f, plaque=0.0):
    """fachada com porta (redação)."""
    d = ImageDraw.Draw(c)
    d.rectangle([x - w / 2, base - h, x + w / 2, base], fill=WALL, outline=INK, width=7)
    for r in range(2):
        for q in range(3):
            wx = x - w / 2 + 60 + q * (w - 120) / 3; wy = base - h + 60 + r * 200
            d.rectangle([wx + 10, wy, wx + (w - 120) / 3 - 10, wy + 130], fill=DARK, outline=INK, width=5)
    d.rectangle([x - 110, base - 330, x + 110, base], fill=DOOR, outline=INK, width=7)
    d.ellipse([x + 60, base - 180, x + 84, base - 156], fill=GOLD, outline=INK, width=3)
    return d


# ------------------------------------------------------------------ cenas
def s0(f):
    """gancho: redação; jornal cai na mesa, luz apaga, porta fecha."""
    c = CEN('escritorio', 'dusk').copy()
    u0 = wt(0, 'ultimo') - 3
    r0 = wt(0, 'Russia') - 3
    p0 = wt(0, 'portas') - 3
    s0_ = wt(0, 'segundafeira') - 3
    paste_c(c, jornal(), 640, 1080, back(ramp(f, u0, u0 + 10)) * .75)
    num(c, 'ÚLTIMO JORNAL', 640, 470, f, u0, 120, -4)
    num(c, 'INDEPENDENTE', 640, 610, f, u0 + 6, 90, 3)
    if f >= r0:
        paste_c(c, bandeira_rus(), 1010, 820, back(ramp(f, r0, r0 + 8)) * .55)
    if f >= p0:
        escurece(c, 130 * smooth(ramp(f, p0, p0 + 14)))
        carimbo(c, 'FECHADO', 640, 1360, back(ramp(f, p0, p0 + 8)) * .85)
    num(c, 'SEGUNDA, 9/11', 640, 1530, f, s0_, 70, -2)
    z = lerp(1.3, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, p0, .8)
    return c, (640, 1080 + k * 8, z, k), 'dusk'


def s1(f):
    """1993, Moscou; medalha do Nobel vira jornal."""
    c = CEN('cidade', 'golden').copy()
    m0 = wt(1, 'Moscou') - 3
    a0 = wt(1, 'mil') - 3
    n0 = wt(1, 'Nobel') - 3
    num(c, 'MOSCOU', 640, 470, f, m0, 110, -3)
    num(c, '1993', 640, 640, f, a0, 190, 3)
    if f >= n0:
        paste_c(c, medalha(), 400, 1120, back(ramp(f, n0, n0 + 8)) * .9)
        num(c, 'NOBEL DA PAZ', 640, 1440, f, n0 + 2, 80, -2)
        paste_c(c, jornal(), 880, 1120, back(ramp(f, n0 + 10, n0 + 20)) * .5)
        num(c, '+', 640, 1120, f, n0 + 6, 120, 0)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 180))) * (1 + .0005 * f)
    k = kick(f, a0, .5)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 180))), 1080 + k * 6, z, k), 'golden'


def s2(f):
    """investigações; seis velas pelos jornalistas mortos (sério)."""
    c = CEN('escritorio', 'dusk').copy()
    c0 = wt(2, 'corrupcao') - 3
    s0_ = wt(2, 'seis') - 3
    a0 = wt(2, 'Anna') - 3
    paste_c(c, jornal(), 640, 900, .45)
    num(c, 'CORRUPÇÃO', 640, 470, f, c0, 100, -3)
    num(c, 'ABUSOS', 640, 600, f, c0 + 10, 90, 3)
    if f >= s0_:
        escurece(c, 110 * smooth(ramp(f, s0_, s0_ + 12)))
        for i in range(6):
            if f >= s0_ + i * 3:
                vela(c, 290 + i * 132, 1480, f, i)
        num(c, '6 JORNALISTAS', 640, 1120, f, s0_, 100, -2)
        num(c, 'ASSASSINADOS', 640, 1240, f, s0_ + 6, 80, 2)
    if f >= a0:
        num(c, 'ANNA POLITKOVSKAYA', 640, 740, f, a0, 60, -2)
        num(c, '2006', 640, 830, f, a0 + 4, 60, 2)
    z = lerp(1.0, 1.07, smooth(ramp(f, 0, 160))) * (1 + .0004 * f)
    return c, (640, 1080, z, -.8 * smooth(ramp(f, 0, 160))), 'dusk'


def s3(f):
    """2021: o editor (personagem genérico) com a medalha."""
    c = CEN('escritorio', 'day').copy()
    d0 = wt(3, 'dois') - 3
    n0 = wt(3, 'Nobel') - 3
    put_p(c, 640, 1500, 640, f, 4, hair='#9a9aa0', tie='#2f6fd6', suit='#3a3a44', expr='proud', arms='hang')
    num(c, '2021', 640, 470, f, d0, 170, -3)
    if f >= n0:
        paste_c(c, medalha(), 640, 1080, back(ramp(f, n0, n0 + 8)) * .5)
        num(c, 'NOBEL DA PAZ', 640, 640, f, n0, 90, 3)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 80))) * (1 + .0008 * f)
    k = kick(f, n0, .5)
    return c, (640, 1080 + k * 6, z, k), 'day'


def s4(f):
    """virada: site bloqueado, gráfica tomada, carimbo AGENTE ESTRANGEIRO."""
    c = CEN('escritorio', 'dusk').copy()
    i0 = wt(4, 'invasao') - 3
    b0 = wt(4, 'site') - 3
    g0 = wt(4, 'grafica') - 3
    a0 = wt(4, 'agente') - 3
    num(c, 'GUERRA NA UCRÂNIA', 640, 460, f, i0, 70, -3)
    tela(c, 360, 1000, f, f >= b0)
    if f >= b0:
        num(c, 'BLOQUEADO', 360, 690, f, b0, 70, 3)
    if f >= g0:
        paste_c(c, grafica(), 880, 1060, back(ramp(f, g0, g0 + 8)) * .5)
        d = ImageDraw.Draw(c)
        cc = smooth(ramp(f, g0 + 4, g0 + 12))
        if cc > 0:
            d.line([(700, 960), (700 + 360 * cc, 1180)], fill=hexc('#5b626c'), width=22)
            d.line([(1060, 960), (1060 - 360 * cc, 1180)], fill=hexc('#5b626c'), width=22)
        num(c, 'GRÁFICA TOMADA', 850, 800, f, g0, 54, -3)
    if f >= a0:
        carimbo(c, 'AGENTE ESTRANGEIRO', 640, 1380, back(ramp(f, a0, a0 + 8)) * .66)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 220))) * (1 + .0004 * f)
    k = kick(f, a0, .9)
    return c, (640, 1060 + k * 8, z, k + .8 * math.sin(f * .04)), 'dusk'


def s5(f):
    """doações cortadas; caixas de mudança, despejo."""
    c = CEN('escritorio', 'dusk').copy()
    b0 = wt(5, 'bancos') - 3
    l0 = wt(5, 'leitores') - 3
    d0 = wt(5, 'despejada') - 3
    d = ImageDraw.Draw(c)
    # moedas caindo num cofrinho de doações; depois um X
    d.rounded_rectangle([470, 820, 810, 1080], 30, fill=hexc('#7ccf5a'), outline=INK, width=7)
    d.rectangle([590, 820, 690, 845], fill=INK)
    num(c, 'DOAÇÕES', 640, 1140, f, 0, 70, -2)
    stop = f >= b0
    for i in range(4):
        t = ((f + i * 12) % 48) / 48
        if not stop or t < .2:
            yy = 560 + 250 * t
            d.ellipse([620 - 30 + (i - 1.5) * 20, yy - 30, 660 - 10 + (i - 1.5) * 20 + 20, yy + 30], fill=GOLD, outline=INK, width=5)
    num(c, 'BANCOS', 640, 470, f, b0, 100, -3)
    if f >= l0:
        k = back(ramp(f, l0, l0 + 8))
        d.line([(480 - 40 * (k - 1), 800), (480 + 340 * k, 1100)], fill=RED, width=30)
        d.line([(800 + 40 * (k - 1), 800), (800 - 340 * k, 1100)], fill=RED, width=30)
    if f >= d0:
        for i, (x, y) in enumerate([(250, 1460), (1010, 1460), (1010, 1330)]):
            s = back(ramp(f, d0 + i * 3, d0 + i * 3 + 8))
            if s > .05:
                d.rectangle([x - 110 * s, y - 120 * s, x + 110 * s, y], fill=hexc('#c99a5b'), outline=INK, width=6)
                d.line([(x - 110 * s, y - 70 * s), (x + 110 * s, y - 70 * s)], fill=hexc('#9a7240'), width=8)
        num(c, 'DESPEJADA', 640, 1300, f, d0, 90, 3)
    z = lerp(1.0, 1.07, smooth(ramp(f, 0, 140))) * (1 + .0006 * f)
    k = kick(f, l0, .6)
    return c, (640, 1080 + k * 6, z, k), 'dusk'


def s6(f):
    """fachada com placa; fim: 'vai voltar?'"""
    c = CEN('cidade', 'dusk').copy()
    p0 = wt(6, 'placa') - 3
    v0 = wt(6, 'voltar') - 3
    e0 = wt(6, 'editor') - 3
    d = predio(c, 640, 1540, 900, 900, f)
    if f >= p0:
        s = back(ramp(f, p0, p0 + 8))
        pl = Image.new('RGBA', (640, 260), (0, 0, 0, 0))
        dp = ImageDraw.Draw(pl)
        dp.rounded_rectangle([8, 8, 632, 252], 18, fill=hexc('#e8e2d2'), outline=INK, width=8)
        for i, lin in enumerate(['AQUI VIVEU O', 'NOVAYA GAZETA']):
            t = P.bubble_text(lin, 62, rot=0)
            pl.alpha_composite(t, (320 - t.size[0] // 2, 70 + i * 100 - t.size[1] // 2))
        paste_c(c, pl, 640, 1040, s * 1.1)
    if f >= e0:
        put_p(c, 1060, 1560, 420, f, 7, hair='#5a4636', tie='#2f6fd6', suit='#2c3550', expr='stern', look=-1, arms='hang')
    if f >= v0:
        num(c, 'VAI VOLTAR?', 640, 520, f, v0, 120, -3)
    z = lerp(1.25, 1.0, smooth(ramp(f, 0, 70))) * (1 + .0007 * f)
    k = kick(f, p0, .5)
    return c, (640, 1120 + k * 6, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'portas') - 3, 140, .7)
    s.ting(s.W(1, 'Nobel') - 3, .3)
    s.ting(s.W(3, 'Nobel') - 3, .3)
    s.thunk(s.W(4, 'site') - 3, 150, .5)
    s.thunk(s.W(4, 'agente') - 3, 160, .8)
    s.thunk(s.W(5, 'despejada') - 3, 140, .6)
    s.ting(s.W(6, 'placa') - 3, .25)
