"""Um Café com o Mundo — RESUMO DA SEMANA (sexta 06/11/2026, 18h).
Tema: eleições de meio de mandato dos EUA (3/11/2026) — democratas viram Câmara e Senado.
Fontes (conferidas em 06/11/2026):
- Yahoo News live (atualizado 06/11 15:54 UTC): Câmara 253 D x 157 R às 10h ET de sexta, 25 sem resultado,
  a caminho da maior maioria desde 2008; Senado 54 D x 44 R (sete viradas), Alasca e Mississippi ainda em contagem;
  Trump diz que vai trabalhar com os democratas nos 2 anos que restam, mas vai usar o veto quando precisar;
  novos parlamentares tomam posse no começo de janeiro; Aguilar: maioria permite investigar o governo.
- CNN (05/11): democratas projetados com mais de 250 cadeiras na Câmara.
- NBC/AP/CBS (04/11): democratas vencem a Câmara e o Senado.
Personagens genéricos (sem traços de pessoas reais). Cores azul/vermelho = cores dos partidos, sem logotipos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'RESUMO DA SEMANA  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Em uma semana, o presidente dos Estados Unidos perdeu o Congresso inteiro.",
    "Na terça, os americanos votaram nas eleições de meio de mandato, e os democratas viraram as duas casas.",
    "Na Câmara, eles já passam de duzentas e cinquenta cadeiras, a maior maioria desde dois mil e oito.",
    "No Senado, já são cinquenta e quatro de cem, e o Alasca e o Mississippi ainda contam votos.",
    "Por que isso importa? A partir de janeiro, quase nenhuma lei passa sem os democratas, e eles prometem investigar o governo.",
    "Trump diz que vai trabalhar com eles, mas que vai usar o veto quando precisar. Agora, cada lei vira uma negociação.",
]
CAPTXT = [
    "Em uma semana, o presidente dos Estados Unidos|perdeu o Congresso inteiro.",
    "Na terça, os americanos votaram nas eleições de meio de mandato,|e os democratas viraram as duas casas.",
    "Na Câmara, eles já passam de 250 cadeiras,|a maior maioria desde 2008.",
    "No Senado, já são 54 de 100,|e o Alasca e o Mississippi ainda contam votos.",
    "Por que isso importa? A partir de janeiro,|quase nenhuma lei passa sem os democratas,|e eles prometem investigar o governo.",
    "Trump diz que vai trabalhar com eles,|mas que vai usar o veto quando precisar.|Agora, cada lei vira uma negociação.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Congresso', 4), (1, 'votaram', 4), (1, 'viraram', 6), (2, 'duzentas', 6), (2, 'dois', 4),
         (3, 'cinquenta', 6), (3, 'Alasca', 4), (4, 'janeiro', 4), (4, 'investigar', 4), (5, 'veto', 4), (5, 'negociacao', 6)]

BLUE = hexc('#2f6fd6'); BLUE_D = hexc('#1f4f9e'); RED = hexc('#d8443c'); RED_D = hexc('#a02c26')
STONE = hexc('#f1ece2'); STONE_D = hexc('#c9c0b0')


# ------------------------------------------------------------------ desenhos novos
def capitolio(tint=0.0):
    """prédio genérico de governo com cúpula (sem marca). 1000x800, base y~790. tint 0=vermelho 1=azul (bandeirinha)."""
    p = Pen(1000, 800)
    # escadaria
    for i in range(5):
        y = 790 - i * 14
        p.shape([(90 + i * 20, y - 14), (910 - i * 20, y - 14), (910 - i * 20, y), (90 + i * 20, y)], STONE, STONE_D, 4, 3)
    # corpo
    p.shape([(80, 470), (920, 470), (920, 720), (80, 720)], STONE, STONE_D, 6, 14)
    for x in range(120, 900, 52):
        p.shape([(x - 12, 500), (x + 12, 500), (x + 12, 712), (x - 12, 712)], hexc('#fbf8f2'), STONE_D, 3, 4)
    p.shape([(60, 450), (940, 450), (940, 482), (60, 482)], STONE, STONE_D, 5, 4)
    # frontão
    p.shape([(330, 450), (500, 380), (670, 450)], STONE, STONE_D, 5, 6)
    # tambor + cúpula
    p.shape([(370, 300), (630, 300), (630, 380), (370, 380)], STONE, STONE_D, 5, 8)
    for x in range(390, 630, 30): p.stroke([(x, 308), (x, 372)], 3, STONE_D)
    dome = [(380 + 240 * (1 - math.cos(a)) / 2, 300 - 190 * math.sin(a)) for a in [i * math.pi / 30 for i in range(31)]]
    p.shape(dome, hexc('#fbf8f2'), STONE_D, 6, 16)
    for k in (-1, 0, 1): p.stroke(curve((500 + k * 60, 300), (500 + k * 40, 180), (500, 112), 8), 3, STONE_D)
    p.shape([(486, 112), (514, 112), (514, 60), (486, 60)], STONE, STONE_D, 4, 3)
    # mastro + bandeirinha do partido (cor lisa)
    p.stroke([(500, 60), (500, -10 + 20)], 5)
    col = tuple(int(RED[i] * (1 - tint) + BLUE[i] * tint) for i in range(3))
    wave = [(502, 12), (580, 20), (590, 42), (502, 44)]
    p.shape(wave, col, mul(col, .75), 4, 4)
    return p.img


def politico(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=0, hair='#6b6b70', tie='#d8443c', suit='#2c3550'):
    """pessoa genérica de terno (personagem 'feijão'). 600x1000, pés y~975."""
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


def put_pol(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'politico', x, feet, h, f, seed, **kw)


def urna(fill=0.0):
    p = Pen(500, 520)
    p.shape([(60, 160), (440, 160), (420, 500), (80, 500)], hexc('#eef2f7'), hexc('#b9c3d1'), 6, 16)
    p.shape([(40, 120), (460, 120), (460, 170), (40, 170)], hexc('#dfe6ef'), hexc('#a9b4c4'), 5, 6)
    p.poly([(180, 136), (320, 136), (320, 152), (180, 152)], INK)
    p.shape(ell_pts(250, 330, 70, 70, 40), BLUE, BLUE_D, 5, 6)
    p.stroke([(215, 330), (242, 358), (290, 300)], 12, (255, 255, 255))
    return p.img


def cedula():
    p = Pen(160, 210)
    p.shape([(10, 10), (150, 10), (150, 200), (10, 200)], (255, 255, 255), hexc('#cfd6df'), 4, 4)
    for y in (50, 90, 130):
        p.poly([(28, y - 10), (48, y - 10), (48, y + 10), (28, y + 10)], (255, 255, 255), 3)
        p.stroke([(60, y), (130, y)], 4, hexc('#9aa4b4'))
    p.stroke([(30, 90), (38, 100), (52, 78)], 5, BLUE)
    return p.img


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def cap_img(tint, h=760):
    im = sprite('capitolio', ('tint', round(tint * 8) / 8), h, 1.25, False)
    return im


def put_cap(c, x, base, h, tint):
    put_sprite(c, 'capitolio', x, base, h, 1.25, False, {'tint': 8}, tint=tint)


def hemiciclo(c, cx, cy, n, nblue, f, f0, r0=170, r1=470, rows=None, unk=(), dot=None):
    """assentos em semicírculo; pinta de azul em sequência a partir de f0."""
    d = ImageDraw.Draw(c)
    rows = rows or (8 if n > 200 else 5)
    seats = []
    radii = [r0 + (r1 - r0) * i / (rows - 1) for i in range(rows)]
    tot = sum(radii)
    for r in radii:
        k = max(2, round(n * r / tot))
        for j in range(k): seats.append((math.pi * (1 - j / (k - 1)), r))
    seats = sorted(seats[:n], key=lambda s: -s[0])
    dot = dot or (14 if n > 200 else 22)
    shown = int(clamp((f - f0) / 26) * nblue)
    for i, (a, r) in enumerate(seats):
        x = cx + r * math.cos(a); y = cy - r * math.sin(a)
        if i in unk: col = hexc('#e8d36a')
        elif i < shown: col = BLUE
        elif i < nblue: col = hexc('#d9dde3')
        else: col = RED if i >= len(seats) - (n - nblue - len(unk)) else hexc('#d9dde3')
        d.ellipse([x - dot, y - dot, x + dot, y + dot], fill=col, outline=INK, width=4)
    return seats


# ------------------------------------------------------------------ cenas
def s0(f):
    c = BG('day').copy()
    k0 = wt(0, 'perdeu') - 3
    tint = smooth(ramp(f, k0, k0 + 14))
    put_cap(c, 640, 1250, 760, tint)
    put_pol(c, 980, 1780, 820, f, 2, arms='hang' if f < k0 else 'cheek', expr='neutral' if f < k0 else 'shock', look=-1, hair='#9a9aa0')
    num(c, 'EUA', 640, 560, f, 0, 130, -3)
    num(c, 'CONGRESSO', 600, 730, f, wt(0, 'Congresso') - 3, 120, -4)
    num(c, 'PERDIDO!', 640, 890, f, wt(0, 'inteiro') - 3, 110, 4)
    z = lerp(1.35, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, k0)
    return c, (640, 1200 + k * 10, z, k), 'day'


def s1(f):
    c = BG('day').copy()
    put_cap(c, 640, 1080, 480, 0)
    v0 = wt(1, 'votaram') - 3
    paste_c(c, urna(), 640, 1350, back(ramp(f, v0 - 6, v0 + 4)) * .9)
    ced = cedula()
    for i in range(8):
        t0 = v0 + i * 6
        tt = clamp((f - t0) / 14)
        if 0 < tt < 1:
            x = lerp(200 + (i % 4) * 280, 640, tt); y = lerp(900, 1260, tt * tt)
            paste_c(c, ced.rotate(20 * math.sin(i + f * .2), expand=True), x, y, .8)
    for i, (x, sk, hr) in enumerate(((200, 1, '#3b2a1e'), (1060, 2, '#1e1a18'), (420, 3, '#7a4a2a'), (870, 0, '#c9a35a'))):
        put_pol(c, x, 1830 + (i // 2) * 40, 520, f, 10 + i, skin=sk, hair=hr, suit=['#5a6b4a', '#7a4a5a', '#4a5a7a', '#8a6a3a'][i], tie='#e8d36a',
                arms='up' if f >= wt(1, 'viraram') - 3 else 'hang', expr='grin' if f >= wt(1, 'viraram') - 3 else 'neutral')
    r0 = wt(1, 'viraram') - 3
    num(c, 'CÂMARA', 310, 660, f, r0, 80, -5)
    num(c, 'SENADO', 950, 660, f, r0 + 6, 80, 5)
    num(c, 'ELEIÇÕES 3/11', 640, 480, f, wt(1, 'eleicoes') - 3, 90, -3)
    t = smooth(ramp(f, 0, 60))
    k = kick(f, r0, .8)
    return c, (640, lerp(1300, 1250, t) + k * 8, lerp(1.2, 1.06, t) * (1 + .0005 * f), k), 'day'


def s2(f):
    c = BG('day').copy()
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([60, 700, 1182, 1560], 40, fill=hexc('#f6f1e6'), outline=INK, width=6)
    f0 = wt(2, 'duzentas') - 6
    hemiciclo(c, 621, 1420, 435, 253, f, f0, r0=200, r1=500, rows=9, unk=set(range(253, 278)), dot=12)
    num(c, 'CÂMARA', 621, 620, f, 0, 100, -3)
    num(c, '250+', 621, 1270, f, wt(2, 'duzentas') - 3, 170, -3)
    num(c, 'MAIOR DESDE 2008', 621, 520, f, wt(2, 'dois') - 3, 90, 4)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 90))) * (1 + .0003 * f)
    return c, (640, 1150, z, 0), 'day'


def s3(f):
    c = BG('day').copy()
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([60, 700, 1182, 1560], 40, fill=hexc('#f6f1e6'), outline=INK, width=6)
    f0 = wt(3, 'cinquenta') - 8
    hemiciclo(c, 621, 1440, 100, 54, f, f0, r0=200, r1=470, rows=5, unk={54, 55} if f >= wt(3, 'Alasca') - 3 else set(), dot=22)
    num(c, 'SENADO', 621, 620, f, 0, 100, -3)
    num(c, '54 DE 100', 621, 1300, f, wt(3, 'cinquenta') - 3, 130, -3)
    a0 = wt(3, 'Alasca') - 3
    num(c, 'ALASCA ?', 340, 820, f, a0, 66, -5)
    num(c, 'MISSISSIPPI ?', 880, 820, f, wt(3, 'Mississippi') - 3, 66, 5)
    z = lerp(1.12, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0003 * f)
    return c, (640, lerp(1150, 1080, smooth(ramp(f, a0 - 10, a0 + 10))), z, 0), 'day'


def s4(f):
    c = BG('dusk').copy()
    put_cap(c, 640, 1200, 540, 1)
    j0 = wt(4, 'janeiro') - 3
    num(c, 'JANEIRO', 640, 600, f, j0, 120, -4)
    # porta-lei: pilha de papéis com carimbo azul
    l0 = wt(4, 'lei') - 3
    if f >= l0:
        for i in range(3):
            paste_c(c, cedula().resize((220, 290)), 380 + i * 30, 1330 - i * 16, back(ramp(f, l0 + i * 3, l0 + i * 3 + 8)))
        if f >= wt(4, 'democratas') - 3:
            paste_c(c, txt('SÓ COM ELES', 70, -8), 430, 1150, back(ramp(f, wt(4, 'democratas') - 3, wt(4, 'democratas') + 5)))
    i0 = wt(4, 'investigar') - 3
    put_pol(c, 980, 1820, 640, f, 5, skin=2, hair='#1e1a18', tie='#2f6fd6', arms='point' if f >= i0 else 'hang', expr='stern' if f >= i0 else 'neutral', look=-1)
    if f >= i0:
        g = Pen(260, 260); g.dot(110, 110, 80, hexc('#cfe3f5'), 10); g.line([(170, 170), (240, 240)], hexc('#6b4a2f'), 22, 5)
        paste_c(c, g.img.resize((260, 260)), 600 + 20 * math.sin(f * .2), 1350, back(ramp(f, i0, i0 + 8)))
        num(c, 'INVESTIGAR', 600, 1580, f, i0, 100, 4)
    z = lerp(1.0, 1.14, smooth(ramp(f, 0, 120))) + .0006 * f
    return c, (640, 1200, z, lerp(0, 2, smooth(ramp(f, 0, 120)))), 'dusk'


def s5(f):
    c = BG('dusk').copy()
    d = ImageDraw.Draw(c)
    v0 = wt(5, 'veto') - 3
    put_pol(c, 360, 1820, 760, f, 2, hair='#9a9aa0', arms='point' if f >= v0 else 'hang', expr='stern' if f >= v0 else 'neutral', look=1)
    put_pol(c, 900, 1820, 740, f, 5, skin=2, hair='#1e1a18', tie='#2f6fd6', expr='nervous' if f >= v0 else 'neutral', look=-1)
    if f >= wt(5, 'trabalhar') - 3:
        num(c, 'TRABALHAR JUNTOS', 640, 600, f, wt(5, 'trabalhar') - 3, 84, -3)
    num(c, 'VETO', 640, 800, f, v0, 190, 6)
    n0 = wt(5, 'negociacao') - 3
    if f >= n0:
        # cabo: papel puxado pelos dois lados
        x = 640 + 40 * math.sin(f * .25)
        paste_c(c, cedula().resize((200, 260)).rotate(90, expand=True), x, 1300, back(ramp(f, n0 - 6, n0 + 4)))
        num(c, 'NEGOCIAÇÃO', 640, 1010, f, n0, 110, -4)
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 150)))
    k = kick(f, v0)
    return c, (640, 1200 + k * 8, z, k - .01 * f), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def SFX(s):
    s.thunk(s.W(0, 'perdeu') - 3, 140, 1.0)
    s.ting(s.W(0, 'Congresso') - 3, .25)
    for i in range(4): s.thunk(s.W(1, 'votaram') - 3 + i * 6, 260, .35)
    s.ting(s.W(1, 'viraram') - 3, .35)
    s.patter(s.W(2, 'duzentas') - 6, s.W(2, 'duzentas') + 22, 10, .12)
    s.thunk(s.W(2, 'dois') - 3, 160, .6)
    s.patter(s.W(3, 'cinquenta') - 8, s.W(3, 'cinquenta') + 20, 10, .12)
    s.ting(s.W(3, 'Alasca') - 3, .25)
    s.thunk(s.W(4, 'janeiro') - 3, 160, .6)
    s.thunk(s.W(4, 'investigar') - 3, 200, .5)
    s.thunk(s.W(5, 'veto') - 3, 120, 1.0)
    s.whoosh(s.W(5, 'negociacao') - 3, .3, .5)
