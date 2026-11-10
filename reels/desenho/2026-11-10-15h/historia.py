"""Um Café com o Mundo — O MUNDO EXPLICADO (terça 10/11/2026, 15h).
Tema: França acusa a Guarda Revolucionária do Irã pelo ataque hacker às geladeiras de supermercados.
Fontes (conferidas em 10/11/2026):
- Al Jazeera, 09/11/2026 ("France accuses Iran of cyberattack on supermarket fridges"): ministro Jean-Noël Barrot disse em 09/11
  que o ataque "foi realizado pela Guarda Revolucionária Islâmica do Irã"; ataques de 11 e 12/10/2026 a supermercados franceses
  (Intermarché 300+ lojas, Coopérative U 100+, Carrefour 80, Monoprix ~25, E-Leclerc); temperaturas elevadas a distância até
  50 °C durante a noite; milhões de euros em comida estragada; em alguns casos, fogo ou equipamento derretido; investigadores:
  uso de persa (farsi) e endereços IP ligados a aparelhos no Irã; Ministério Público de Paris investiga a unidade Shahid Kaveh e
  pediu mandados de prisão internacionais contra o chefe e dois auxiliares; Barrot: primeiro ciberataque de grande escala com fins
  de sabotagem em solo francês; sanções em nível europeu.
- Reuters (via SRN News), 10/11/2026: embaixador do Irã convocado na manhã de terça (10/11); França vai pedir sanções da UE e pode
  responder com medidas próprias; Irã costuma negar operações cibernéticas maliciosas; missão do Irã na ONU não respondeu.
Tom sério; personagens genéricos; sem pessoas reais desenhadas."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O MUNDO EXPLICADO  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "A França diz que já sabe quem fez as geladeiras dos supermercados esquentarem até cinquenta graus.",
    "Em outubro, hackers invadiram pela internet a refrigeração de centenas de mercados franceses.",
    "De madrugada, milhões de euros em comida estragaram, e em alguns lugares teve até fogo.",
    "Nesta segunda, o governo francês apontou o culpado: um grupo de hackers da Guarda Revolucionária do Irã.",
    "Os investigadores acharam rastros em persa e endereços de internet do Irã, e a Justiça pediu a prisão do chefe.",
    "Por que isso importa? Segundo a França, foi o primeiro grande ataque hacker de sabotagem no país.",
    "Nesta terça, o embaixador do Irã foi chamado para se explicar, e a França quer sanções na Europa. O Irã costuma negar.",
]
CAPTXT = [
    "A França diz que já sabe quem fez as geladeiras|dos supermercados esquentarem até 50 graus.",
    "Em outubro, hackers invadiram pela internet|a refrigeração de centenas|de mercados franceses.",
    "De madrugada, milhões de euros|em comida estragaram,|e em alguns lugares teve até fogo.",
    "Nesta segunda, o governo francês apontou o culpado:|um grupo de hackers da Guarda Revolucionária do Irã.",
    "Os investigadores acharam rastros em persa|e endereços de internet do Irã,|e a Justiça pediu a prisão do chefe.",
    "Por que isso importa? Segundo a França,|foi o primeiro grande ataque hacker|de sabotagem no país.",
    "Nesta terça, o embaixador do Irã foi chamado|para se explicar, e a França quer|sanções na Europa. O Irã costuma negar.",
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Franca', 4), (0, 'geladeiras', 4), (0, 'cinquenta', 4), (1, 'outubro', 4), (1, 'hackers', 4), (1, 'centenas', 4),
         (2, 'madrugada', 4), (2, 'milhoes', 4), (2, 'fogo', 4), (3, 'governo', 4), (3, 'culpado', 4), (3, 'Ira', 4),
         (4, 'persa', 4), (4, 'enderecos', 4), (4, 'prisao', 4), (5, 'importa', 4), (5, 'primeiro', 4),
         (6, 'embaixador', 4), (6, 'sancoes', 4), (6, 'negar', 4)]

RED = hexc('#e0393e'); RED_D = hexc('#a82a2e'); WHITE = (255, 255, 255)
GOLD = hexc('#f2c14e'); GOLD_D = hexc('#b8862a'); DARK = hexc('#2b2d3a')
GLASS = hexc('#bfe3f2'); FRIDGE = hexc('#e9eef3'); FRIDGE_D = hexc('#b9c3cd')
EUB = hexc('#2445a8'); STONE = hexc('#e8e1d2'); STONE_D = hexc('#c2b8a3')
IRG = hexc('#2f9a55'); IRR = hexc('#d8382f'); CODE = hexc('#5cf08a')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


def escurece(c, a, col=(20, 18, 40)):
    if a <= 0: return
    c.alpha_composite(Image.new('RGBA', c.size, col + (int(a),)))


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


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


# ------------------------------------------------------------------ cenário: supermercado
@lru_cache(maxsize=4)
def mercado(light='day'):
    """corredor de supermercado: parede, fileira de geladeiras com porta de vidro e produtos, piso xadrez. 1242x2208"""
    W, H = BW, BH
    img = Image.new('RGBA', (W, H), hexc('#f1e6d2') + (255,))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 330], fill=hexc('#dfe8ee'))
    for x in range(60, W, 300):  # luminárias
        d.rounded_rectangle([x, 70, x + 200, 100], 10, fill=WHITE, outline=INK, width=4)
    d.rectangle([0, 330, W, 380], fill=hexc('#3f8a5a'), outline=INK, width=5)  # faixa verde
    floor = 1560
    # piso xadrez
    for r in range(8):
        y0 = floor + r * 90
        for k in range(-2, 16):
            if (r + k) % 2: continue
            x0 = k * 110 - r * 10
            d.polygon([(x0, y0), (x0 + 110, y0), (x0 + 110 - 10, y0 + 90), (x0 - 10, y0 + 90)], fill=hexc('#d9d3c6'))
    d.line([(0, floor), (W, floor)], fill=INK, width=6)
    # geladeiras
    rnd = random.Random(3)
    cols = ['#e0393e', '#f2c14e', '#2f6fd6', '#7ccf5a', '#ffffff', '#f08a3c', '#b56ad6']
    for u in range(4):
        x0 = 20 + u * 305; x1 = x0 + 295
        d.rectangle([x0, 430, x1, floor], fill=FRIDGE, outline=INK, width=7)
        d.rectangle([x0, 430, x1, 500], fill=hexc('#3f8a5a'), outline=INK, width=5)
        gx0, gx1 = x0 + 22, x1 - 22
        d.rectangle([gx0, 530, gx1, floor - 70], fill=hexc('#dff2fa'), outline=INK, width=5)
        for s in range(5):
            sy = 640 + s * 175
            d.line([(gx0, sy), (gx1, sy)], fill=hexc('#8fa5b4'), width=6)
            x = gx0 + 10
            while x < gx1 - 40:
                w = rnd.randint(32, 52); h = rnd.randint(60, 120)
                col = hexc(rnd.choice(cols))
                d.rounded_rectangle([x, sy - h, x + w, sy - 3], 6, fill=col, outline=INK, width=3)
                x += w + 6
        d.line([(gx1 - 30, 800), (gx1 - 30, 1100)], fill=hexc('#8fa5b4'), width=10)
        for k in range(3):  # reflexo do vidro
            d.line([(gx0 + 30 + k * 30, 560), (gx0 + 110 + k * 30, 760)], fill=(255, 255, 255), width=8)
    if light != 'day':
        img.alpha_composite(Image.new('RGBA', (W, H), (25, 20, 60, 120 if light == 'dusk' else 70)))
    return img


@lru_cache(maxsize=10)
def termometro(lvl=0):
    """termômetro de 0 a 8 níveis. 200x700"""
    p = Pen(200, 700)
    p.shape([(70, 40), (130, 40), (130, 560), (70, 560)], WHITE, hexc('#c9c9d2'), 6, 6)
    p.shape(ell_pts(100, 600, 70, 70, 36), RED, RED_D, 6, 6)
    top = 560 - 500 * lvl / 8
    if lvl > 0: p.poly([(84, top), (116, top), (116, 570), (84, 570)], RED)
    for y in range(80, 560, 60): p.stroke([(130, y), (150, y)], 4)
    return fin(p)


def put_termo(c, x, y, f, lvl, s=1.0):
    im = termometro(int(round(clamp(lvl, 0, 8))))
    paste_c(c, im, x, y, s)


@lru_cache(maxsize=2)
def notebook():
    """notebook aberto com código verde. 760x560"""
    p = Pen(760, 560)
    p.shape([(90, 20), (670, 20), (670, 420), (90, 420)], hexc('#3a3d4d'), hexc('#26283a'), 7, 8)
    p.poly([(120, 50), (640, 50), (640, 390), (120, 390)], hexc('#101418'))
    rnd = random.Random(7)
    for k in range(9):
        y = 80 + k * 34
        x = 145 + rnd.randint(0, 3) * 30
        p.stroke([(x, y), (x + rnd.randint(140, 420), y)], 12, CODE)
    p.shape([(20, 430), (740, 430), (700, 540), (60, 540)], hexc('#8d93a0'), hexc('#5f6470'), 7, 8)
    return fin(p)


def wifi(c, x, y, f, s=1.0, col=None):
    d = ImageDraw.Draw(c)
    col = col or RED
    for i in range(3):
        a = (f * .15 + i) % 3
        r = (40 + i * 45) * s
        d.arc([x - r, y - r, x + r, y + r], 225, 315, fill=col, width=int(14 * s))
    d.ellipse([x - 12 * s, y - 12 * s, x + 12 * s, y + 12 * s], fill=col, outline=INK, width=3)


def fumaca(c, x, y, f, seed=0, s=1.0, col=(150, 150, 160)):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(7):
        t = ((f * .6 + i * 15 + seed * 7) % 100) / 100
        r = (40 + 80 * t) * s
        xx = x + 60 * math.sin(t * 5 + seed + i) * s; yy = y - 300 * t * s
        a = int(150 * (1 - t))
        d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=col + (a,))


@lru_cache(maxsize=2)
def caixa_leite(stink=0):
    """caixa de leite estufada. 220x360"""
    p = Pen(220, 360)
    p.shape([(30, 110), (190, 110), (196, 340), (24, 340)], WHITE, hexc('#c9d0d8'), 6, 8)
    p.shape([(30, 110), (110, 30), (190, 110)], hexc('#cfe3f5'), hexc('#9fb7cf'), 6, 4)
    p.shape([(40, 180), (180, 180), (180, 260), (40, 260)], hexc('#2f6fd6'), hexc('#1f4f9e'), 4, 3)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_fr():
    """bandeira da França (país). 600x400"""
    p = Pen(600, 400)
    for i, cc in enumerate(('#2f4fb5', '#ffffff', '#e0393e')):
        p.poly([(10 + i * 193, 10), (10 + (i + 1) * 193, 10), (10 + (i + 1) * 193, 390), (10 + i * 193, 390)], hexc(cc))
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def bandeira_ir():
    """bandeira do Irã simplificada (país): faixas verde, branca e vermelha. 600x400"""
    p = Pen(600, 400)
    for i, cc in enumerate((IRG, WHITE, IRR)):
        p.poly([(10, 10 + i * 127), (590, 10 + i * 127), (590, 10 + (i + 1) * 127), (10, 10 + (i + 1) * 127)], cc)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


def _estrela(cx, cy, r, rot=0.0):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + rot + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .4
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


@lru_cache(maxsize=2)
def bandeira_ue():
    """bandeira da União Europeia: 12 estrelas em círculo. 600x400"""
    p = Pen(600, 400)
    p.poly([(10, 10), (590, 10), (590, 390), (10, 390)], EUB)
    for k in range(12):
        a = k * math.pi / 6
        p.poly(_estrela(300 + 120 * math.sin(a), 200 - 120 * math.cos(a), 22), GOLD)
    p.stroke([(10, 10), (590, 10), (590, 390), (10, 390), (10, 10)], 6)
    return fin(p)


def put_band(c, im, x, y, w, f, s=1.0, pole=True):
    if s <= .02: return
    ww = int(w * s); hh = int(w * .66 * s)
    im = im.resize((ww, hh)).rotate(3 * math.sin(f * .12), expand=True, resample=Image.BICUBIC)
    if pole:
        d = ImageDraw.Draw(c)
        d.line([(x - ww / 2 - 4, y - hh / 2), (x - ww / 2 - 4, y + hh * 1.6)], fill=INK, width=10)
    paste_c(c, im, x, y, 1)


@lru_cache(maxsize=2)
def podio():
    """púlpito genérico. 520x560, base y~550"""
    p = Pen(520, 560)
    p.shape([(60, 60), (460, 60), (420, 550), (100, 550)], hexc('#7a4e33'), hexc('#57361f'), 7, 14)
    p.shape([(30, 20), (490, 20), (490, 80), (30, 80)], hexc('#8e5d3e'), hexc('#57361f'), 6, 6)
    p.shape(ell_pts(260, 300, 70, 70, 36), GOLD, GOLD_D, 5, 6)
    p.stroke([(240, 20), (220, -40)], 6)
    return fin(p)


@lru_cache(maxsize=2)
def lupa():
    p = Pen(400, 400)
    p.stroke([(250, 250), (370, 370)], 34, hexc('#6b4a2e'))
    p.shape(ell_pts(170, 170, 130, 130, 40), hexc('#c9e6f5'), hexc('#8fb8d0'), 10, 6)
    return fin(p)


@lru_cache(maxsize=2)
def documento():
    """papel oficial com selo. 460x600"""
    p = Pen(460, 600)
    p.shape([(20, 20), (440, 30), (430, 580), (30, 570)], hexc('#f6f1e4'), hexc('#cfc6b2'), 6, 10)
    for k in range(8):
        y = 150 + k * 44
        p.stroke([(70, y), (390, y + 3)], 9, hexc('#8a8590'))
    p.shape(ell_pts(330, 500, 55, 55, 30), RED, RED_D, 5, 4)
    return fin(p)


def carimbo(c, s, x, y, sc, size=74):
    if sc <= .05: return
    t = txt(s, size, 0)
    im = Image.new('RGBA', (t.size[0] + 80, t.size[1] + 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([8, 8, im.size[0] - 8, im.size[1] - 8], 24, outline=RED, width=14)
    im.alpha_composite(t, (40, 30))
    im = im.rotate(-8, expand=True, resample=Image.BICUBIC)
    paste_c(c, im, x, y, sc)


@lru_cache(maxsize=2)
def predio():
    """prédio oficial genérico com colunas e bandeira francesa. 1000x620, base y~610."""
    p = Pen(1000, 620)
    for i in range(4):
        y = 610 - i * 14
        p.shape([(60 + i * 18, y - 14), (940 - i * 18, y - 14), (940 - i * 18, y), (60 + i * 18, y)], STONE, STONE_D, 4, 3)
    p.shape([(70, 150), (930, 150), (930, 560), (70, 560)], STONE, STONE_D, 6, 14)
    p.shape([(40, 110), (960, 110), (960, 170), (40, 170)], STONE, STONE_D, 6, 6)
    for x in range(120, 900, 62):
        p.shape([(x - 16, 190), (x + 16, 190), (x + 16, 548), (x - 16, 548)], hexc('#fbf8f2'), STONE_D, 3, 4)
    p.stroke([(500, 110), (500, 10)], 6)
    for i, cc in enumerate(('#2f4fb5', '#ffffff', '#e0393e')):
        p.poly([(503 + i * 33, 12), (536 + i * 33, 12), (536 + i * 33, 72), (503 + i * 33, 72)], hexc(cc))
    p.stroke([(503, 12), (602, 12), (602, 72), (503, 72), (503, 12)], 4)
    return fin(p)


# ------------------------------------------------------------------ cenas
def s0(f):
    """gancho: corredor de geladeiras, termômetro sobe até 50 °C."""
    c = mercado('day').copy()
    g0 = wt(0, 'geladeiras') - 3
    c0 = wt(0, 'cinquenta') - 3
    num(c, 'FRANÇA', 640, 470, f, wt(0, 'Franca') - 3, 120, -4)
    lvl = 1 + 7 * smooth(ramp(f, g0, c0))
    if f >= g0 - 6:
        put_termo(c, 640, 1060, f, lvl, back(ramp(f, g0 - 6, g0 + 2)) * 1.1)
    if f >= c0:
        escurece(c, 60 * smooth(ramp(f, c0, c0 + 10)), (200, 40, 20))
        num(c, '50 °C', 900, 820, f, c0, 150, 6)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0007 * f)
    k = kick(f, c0, .9)
    return c, (640 + 10 * math.sin(f * .05), 1080 + k * 8, z, k), 'day'


def s1(f):
    """11 e 12/10: notebook com código manda sinal para as geladeiras."""
    c = CEN('escritorio', 'dusk').copy()
    escurece(c, 90)
    o0 = wt(1, 'outubro') - 3
    h0 = wt(1, 'hackers') - 3
    i0 = wt(1, 'internet') - 3
    ce0 = wt(1, 'centenas') - 3
    num(c, 'OUTUBRO', 640, 450, f, o0, 130, -3)
    paste_c(c, notebook(), 380, 1180, back(ramp(f, h0, h0 + 8)) * .75)
    if f >= h0:
        num(c, 'HACKERS', 380, 860, f, h0, 90, 3)
    if f >= i0:
        d = ImageDraw.Draw(c)
        t = smooth(ramp(f, i0, i0 + 14))
        for k in range(3):
            y = 1050 + k * 90
            xe = lerp(640, 900, t)
            d.line([(640, 1150), (xe, y)], fill=RED, width=8)
        wifi(c, 640, 1110, f, 1.0)
    if f >= ce0:
        for i in range(9):
            s = back(ramp(f, ce0 + i * 2, ce0 + i * 2 + 8))
            if s > .05:
                x = 880 + (i % 3) * 110; y = 940 + (i // 3) * 170
                d = ImageDraw.Draw(c)
                w, h = 45 * s, 70 * s
                d.rectangle([x - w, y - h, x + w, y + h], fill=FRIDGE, outline=INK, width=5)
                d.rectangle([x - w + 10, y - h + 20, x + w - 10, y + h - 10], fill=GLASS, outline=INK, width=3)
        num(c, 'CENTENAS DE MERCADOS', 640, 1460, f, ce0, 64, -2)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200))) * (1 + .0004 * f)
    k = kick(f, h0, .6)
    return c, (640 + lerp(-20, 20, smooth(ramp(f, 0, 200))), 1060 + k * 6, z, k), 'dusk'


def s2(f):
    """madrugada: calor, comida estraga, fumaça."""
    c = mercado('dusk').copy()
    t0 = wt(2, 'madrugada') - 3
    m0 = wt(2, 'milhoes') - 3
    f0 = wt(2, 'fogo') - 3
    lvl = 3 + 5 * smooth(ramp(f, t0, t0 + 20))
    put_termo(c, 960, 1000, f, lvl, .8)
    if f >= t0:
        escurece(c, 50 * smooth(ramp(f, t0, t0 + 20)), (220, 60, 20))
    if f >= m0:
        for i, x in enumerate((300, 520, 740)):
            s = back(ramp(f, m0 + i * 3, m0 + i * 3 + 8))
            if s > .05:
                im = caixa_leite()
                im = im.rotate(8 * math.sin(f * .2 + i), expand=True, resample=Image.BICUBIC)
                paste_c(c, im, x, 1330, s * .9)
                d = ImageDraw.Draw(c)
                for k in range(3):
                    yy = 1150 - ((f * 2 + k * 20 + i * 7) % 60)
                    d.arc([x - 30 + k * 20, yy - 20, x + k * 20, yy + 20], 200, 340, fill=hexc('#7ccf5a'), width=6)
        num(c, 'MILHÕES DE EUROS', 500, 620, f, m0, 68, -3)
        num(c, 'EM COMIDA', 500, 740, f, m0 + 6, 66, 3)
    if f >= f0:
        fumaca(c, 1010, 720, f, 1, 1.0)
        num(c, 'FOGO', 900, 470, f, f0, 90, 4)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 160))) * (1 + .0005 * f)
    k = kick(f, m0, .7)
    return c, (640, 1080 + k * 8, z, k + .6 * math.sin(f * .04)), 'dusk'


def s3(f):
    """segunda: autoridade francesa no púlpito; culpado: Guarda Revolucionária do Irã."""
    c = CEN('cidade', 'day').copy()
    g0 = wt(3, 'governo') - 3
    cu0 = wt(3, 'culpado') - 3
    ir0 = wt(3, 'Ira') - 3
    num(c, 'SEGUNDA, 9/11', 640, 450, f, 0, 80, -2)
    put_band(c, bandeira_fr(), 330, 760, 300, f, back(ramp(f, g0 - 6, g0 + 2)))
    put_p(c, 420, 1560, 640, f, 3, hair='#5a4636', tie='#2f4fb5', suit='#2c3550',
          expr='stern', arms='point' if f >= cu0 else 'hang', look=1)
    paste_c(c, podio(), 420, 1420, .6)
    if f >= ir0:
        put_band(c, bandeira_ir(), 900, 900, 300, f, back(ramp(f, ir0, ir0 + 8)), pole=False)
        num(c, 'GUARDA', 900, 1140, f, ir0 - 6, 76, -3)
        num(c, 'REVOLUCIONÁRIA', 880, 1240, f, ir0 - 3, 54, 2)
    if f >= cu0:
        num(c, 'CULPADO?', 880, 640, f, cu0, 90, 4)
    z = lerp(1.08, 1.0, smooth(ramp(f, 0, 80))) * (1 + .0007 * f)
    k = kick(f, ir0, .8)
    return c, (640 + lerp(-10, 30, smooth(ramp(f, 0, 160))), 1060 + k * 6, z, k), 'day'


def s4(f):
    """pistas: lupa sobre a tela (PERSA, IP: IRÃ) e pedido de prisão."""
    c = CEN('escritorio', 'dusk').copy()
    p0 = wt(4, 'persa') - 3
    e0 = wt(4, 'enderecos') - 3
    pr0 = wt(4, 'prisao') - 3
    paste_c(c, notebook(), 640, 950, .9)
    lx = lerp(420, 860, smooth(ramp(f, p0 - 10, e0)))
    paste_c(c, lupa(), lx, 880, .7)
    num(c, 'PISTAS', 640, 450, f, 0, 100, -3)
    num(c, 'PERSA', 420, 640, f, p0, 90, -4)
    num(c, 'IP: IRÃ', 860, 640, f, e0, 90, 4)
    if f >= pr0:
        paste_c(c, documento(), 640, 1180, back(ramp(f, pr0, pr0 + 8)) * .75)
        carimbo(c, 'PRISÃO', 640, 1200, back(ramp(f, pr0 + 4, pr0 + 12)) * .8, 80)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 200))) * (1 + .0004 * f)
    k = kick(f, pr0 + 4, .8)
    return c, (640, 1040 + k * 8, z, k), 'dusk'


def s5(f):
    """virada: por que importa — 1º grande ataque de sabotagem; mapa da França com alvo."""
    c = mercado('dusk').copy()
    escurece(c, 70)
    i0 = wt(5, 'importa') - 3
    p0 = wt(5, 'primeiro') - 3
    s0_ = wt(5, 'sabotagem') - 3
    num(c, 'POR QUE IMPORTA?', 640, 470, f, i0, 90, -3)
    if f >= p0:
        num(c, '1º', 640, 760, f, p0, 260, 3)
        num(c, 'GRANDE ATAQUE', 640, 980, f, p0 + 6, 90, -2)
    if f >= s0_:
        carimbo(c, 'SABOTAGEM', 640, 1230, back(ramp(f, s0_, s0_ + 8)) * .9, 90)
    put_band(c, bandeira_fr(), 640, 1450, 200, f, .9, pole=False)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 60))) * (1 + .0008 * f)
    k = kick(f, p0, .9)
    return c, (640, 1060 + k * 8, z, k), 'dusk'


def s6(f):
    """fim: embaixador chamado ao ministério; sanções na Europa; Irã nega."""
    c = CEN('cidade', 'dusk').copy()
    e0 = wt(6, 'embaixador') - 3
    s0_ = wt(6, 'sancoes') - 3
    n0 = wt(6, 'negar') - 3
    num(c, 'TERÇA, 10/11', 640, 440, f, 0, 80, -2)
    paste_c(c, predio(), 640, 1180, .95)
    if f >= e0:
        x = lerp(1180, 820, smooth(ramp(f, e0, e0 + 60)))
        put_p(c, x, 1580, 520, f, 8, hair='#2a2a30', tie='#2f9a55', suit='#3a3a44', expr='stern', look=-1, arms='hang')
        num(c, 'EMBAIXADOR DO IRÃ', 640, 590, f, e0, 66, 3)
    if f >= s0_:
        put_band(c, bandeira_ue(), 400, 820, 280, f, back(ramp(f, s0_, s0_ + 8)), pole=False)
        num(c, 'SANÇÕES?', 420, 1040, f, s0_ + 2, 80, -3)
    if f >= n0:
        num(c, 'IRÃ COSTUMA NEGAR', 640, 1420, f, n0, 64, -2)
    z = lerp(1.2, 1.0, smooth(ramp(f, 0, 80))) * (1 + .0006 * f)
    k = kick(f, s0_, .5)
    return c, (640, 1080 + k * 6, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'cinquenta') - 3, 140, .8)
    s.ting(s.W(1, 'outubro') - 3, .25)
    s.whoosh(s.W(1, 'internet') - 3, .3, .5)
    s.thunk(s.W(2, 'milhoes') - 3, 160, .6)
    s.thunk(s.W(3, 'Ira') - 3, 150, .7)
    s.ting(s.W(4, 'persa') - 3, .25)
    s.thunk(s.W(4, 'prisao') + 1, 140, .7)
    s.thunk(s.W(5, 'primeiro') - 3, 140, .8)
    s.ting(s.W(6, 'sancoes') - 3, .25)
