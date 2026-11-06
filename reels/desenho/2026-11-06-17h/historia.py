"""Um Café com o Mundo — CURIOSIDADE em desenho (06/11/2026 17h).
Fontes: Arkeonews (05-06/11/2026, a partir do relatório da Associação de Museus de Almaty / gurk.kz),
The History Blog (06/11/2026), samaraonline24 (05/11/2026).
Fatos: cemitério de Karagayly (Karagaily), distrito de Nauryzbay, Almaty, Cazaquistão. Kurgan (monte funerário)
da época saca, datado de forma preliminar dos séculos 4-3 a.C. (~2.300 anos), ~25-26 m de diâmetro e 2,5 m de altura.
Saqueado na Antiguidade: cratera de saqueadores de ~3 m no centro; restos e objetos espalhados. Os saqueadores
deixaram um pequeno urso de ouro fundido, em pé nas patas de trás, segurando um vaso com as patas da frente, sobre
uma placa com furinhos (provavelmente costurado num adorno de cabeça). A diretora Lyazzat Sagyndykova: inédito,
nenhum urso de ouro parecido tinha sido achado no Cazaquistão. Análise preliminar: 4 adultos e 3 crianças;
montes desse tamanho costumam ter 1 ou 2 pessoas (Marat Nurpeisov). Escavação continua; peças principais irão
para exposição no museu de Almaty."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Ladrões saquearam um túmulo de dois mil e trezentos anos... e esqueceram um urso de ouro.",
    "Foi no Cazaquistão, perto de Almaty: um monte funerário do povo saca, nômades das estepes, com vinte e cinco metros.",
    "No meio dele, os arqueólogos acharam uma cratera de três metros, aberta por saqueadores ainda na Antiguidade.",
    "Eles bagunçaram tudo... mas não viram um ursinho de ouro, em pé, segurando um vaso com as duas patas.",
    "Os furinhos na placa mostram que ele era costurado num chapéu. E nunca tinham achado um urso de ouro assim no Cazaquistão.",
    "Mas tem outro mistério: o túmulo pode ter guardado sete pessoas, quando o normal era uma ou duas.",
    "As escavações continuam. E o urso que os ladrões não viram deve ir para o museu de Almaty.",
]
CAPTXT = [
    "Ladrões saquearam um túmulo de 2.300 anos...|e esqueceram um urso de ouro.",
    "Foi no Cazaquistão, perto de Almaty:|um monte funerário do povo saca, nômades das estepes,|com 25 metros.",
    "No meio dele, os arqueólogos acharam uma cratera de 3 metros,|aberta por saqueadores ainda na Antiguidade.",
    "Eles bagunçaram tudo... mas não viram um ursinho de ouro,|em pé, segurando um vaso com as duas patas.",
    "Os furinhos na placa mostram que ele era costurado num chapéu.|E nunca tinham achado um urso de ouro assim no Cazaquistão.",
    "Mas tem outro mistério: o túmulo pode ter guardado 7 pessoas,|quando o normal era uma ou duas.",
    "As escavações continuam.|E o urso que os ladrões não viram deve ir para o museu de Almaty.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [3]
CHECK = [(0, 'ouro', 6), (1, 'cazaquistao', 4), (1, 'metros', 6), (2, 'metros', 4), (3, 'vaso', 6), (4, 'chapeu', 6), (5, 'sete', 6), (6, 'museu', 8)]

GOLD = hexc('#f2c23a'); GOLDD = hexc('#c48a1a'); GOLDL = hexc('#fff0a0')
DIRT = hexc('#c79a62'); DIRTD = hexc('#9c7444')
CLAY = hexc('#b9825a'); CLAYD = hexc('#8a5a3a')


# ------------------------------------------------------------------ urso de ouro (figurinha em placa)
def gbear(blink=0, shine=0.0, look=0.0, plate=1):
    """urso de ouro em pé segurando vaso, sobre placa furada. 500x700, base y~690."""
    p = Pen(500, 700)
    if plate:
        p.shape([(60, 600), (440, 600), (440, 690), (60, 690)], GOLDD, mul(GOLDD, .8), 5, 8)
        for x in (100, 180, 320, 400):
            p.dot(x, 645, 13, hexc('#5a3a10'), 3)
    # pernas
    p.shape(ell_pts(185, 560, 55, 60, 30), GOLD, GOLDD, 5, 10)
    p.shape(ell_pts(315, 560, 55, 60, 30), GOLD, GOLDD, 5, 10)
    # corpo
    p.shape(ell_pts(250, 420, 140, 165, 50), GOLD, GOLDD, 6, 22)
    p.shape(ell_pts(250, 450, 85, 110, 40), GOLDL, None, 0)
    # vaso
    p.shape([(195, 360), (305, 360), (320, 400), (300, 470), (200, 470), (180, 400)], CLAY, CLAYD, 5, 10)
    p.shape(ell_pts(250, 360, 58, 14, 24), mul(CLAY, .7), None, 4)
    p.stroke([(190, 420), (310, 420)], 4, CLAYD)
    # bracos segurando o vaso
    p.shape(ell_pts(170, 410, 42, 60, 24, .5), GOLD, GOLDD, 5, 8)
    p.shape(ell_pts(330, 410, 42, 60, 24, -.5), GOLD, GOLDD, 5, 8)
    # cabeca
    p.shape(ell_pts(165, 140, 38, 38, 24), GOLD, GOLDD, 5, 8)
    p.shape(ell_pts(335, 140, 38, 38, 24), GOLD, GOLDD, 5, 8)
    p.dot(165, 140, 16, GOLDD); p.dot(335, 140, 16, GOLDD)
    p.shape(ell_pts(250, 210, 120, 105, 48), GOLD, GOLDD, 6, 16)
    p.shape(ell_pts(250, 255, 52, 38, 30), GOLDL, None, 4)
    p.dot(250, 238, 14, hexc('#5a3a10'))
    p.arc(250, 262, 18, 10, 20, 160, 4)
    for ex in (205, 295):
        p.dot(ex, 195, 24, (255, 255, 255), 4)
        if blink:
            p.arc(ex, 195, 22, 8, 0, 180, 5)
        else:
            p.dot(ex + look * 8, 198, 12, INK)
            p.dot(ex + look * 8 - 4, 193, 4, (255, 255, 255))
    if shine > 0:
        p.stroke([(140, 330), (160, 300)], 10, (255, 255, 255))
        p.stroke([(140, 180), (155, 160)], 8, (255, 255, 255))
    return p.img


def hat(bear=1):
    """chapéu pontudo de feltro com urso costurado. 500x800, base y~790."""
    p = Pen(500, 800)
    p.shape([(250, 30), (420, 640), (80, 640)], hexc('#c0392b'), hexc('#8e2a20'), 6, 24)
    p.shape([(50, 620), (450, 620), (470, 700), (30, 700)], hexc('#e8d9b0'), hexc('#c4b48a'), 6, 10)
    for i in range(9):
        p.dot(70 + i * 45, 660, 9, GOLD, 3)
    p.dot(250, 30, 18, GOLD, 4)
    return p.img


def shovel():
    p = Pen(200, 600)
    p.line([(100, 20), (100, 420)], hexc('#8a5a34'), 22, 4)
    p.shape([(50, 400), (150, 400), (150, 500), (100, 580), (50, 500)], hexc('#9aa3ad'), hexc('#6c757f'), 5, 10)
    return p.img


def pot(seed=1):
    p = Pen(300, 300)
    p.shape([(80, 40), (220, 40), (270, 160), (220, 290), (80, 290), (30, 160)], CLAY, CLAYD, 5, 14)
    p.stroke([(40, 150), (260, 150)], 4, CLAYD)
    return p.img


def shard(seed=1):
    r = random.Random(seed)
    p = Pen(200, 160)
    pts = [(20 + r.random() * 30, 30 + r.random() * 30), (100, 10 + r.random() * 20), (180 - r.random() * 30, 40 + r.random() * 30),
           (150, 140 - r.random() * 20), (40, 130)]
    p.shape(pts, CLAY, CLAYD, 4, 8)
    return p.img


def person(kid=0):
    """ícone simples de pessoa (silhueta clara). 200x400."""
    p = Pen(200, 400)
    col = hexc('#f6ecd2'); dk = hexc('#d8c8a0')
    if kid:
        p.shape(ell_pts(100, 250, 55, 80, 30), col, dk, 5, 8)
        p.shape(ell_pts(100, 140, 45, 45, 30), col, dk, 5, 8)
    else:
        p.shape(ell_pts(100, 250, 70, 140, 30), col, dk, 5, 8)
        p.shape(ell_pts(100, 70, 55, 55, 30), col, dk, 5, 8)
    return p.img


def tape(w=900):
    p = Pen(w, 120)
    p.line([(20, 60), (w - 20, 60)], hexc('#ffd84a'), 14, 4)
    p.poly([(10, 60), (60, 20), (60, 100)], hexc('#ffd84a'), 4)
    p.poly([(w - 10, 60), (w - 60, 20), (w - 60, 100)], hexc('#ffd84a'), 4)
    return p.img


def mound(dig=0.0):
    """kurgan (monte funerário) com cratera no topo. 1242x700, base y~700."""
    p = Pen(1242, 700)
    p.shape(curve((-40, 690), (620, 0), (1282, 690), 30) + [(1282, 700), (-40, 700)], hexc('#a9b85a'), hexc('#7d8a3e'), 6, 26)
    for k, y in enumerate((330, 450, 570)):
        p.stroke(curve((200 + k * 40, y + 50), (620, y - 60), (1040 - k * 40, y + 50), 20), 4, hexc('#7d8a3e'))
    if dig > 0:
        w = 150 * dig
        p.shape(ell_pts(620, 330, w, 50 * dig, 30), hexc('#6a4a2a'), None, 5, 0)
        p.shape(ell_pts(620, 322, w * .8, 34 * dig, 30), hexc('#3e2a18'), None, 0, 0)
    return p.img


@lru_cache(maxsize=2)
def star():
    p = Pen(120, 120)
    pts = [(60 + (55 if i % 2 == 0 else 22) * math.cos(math.radians(-90 + i * 36)), 60 + (55 if i % 2 == 0 else 22) * math.sin(math.radians(-90 + i * 36))) for i in range(10)]
    p.shape(pts, hexc('#fff3a0'), hexc('#e0a92a'), 4, 6)
    return p.img


def case_():
    p = Pen(600, 900)
    p.shape([(110, 520), (490, 520), (490, 890), (110, 890)], hexc('#e9e2d4'), hexc('#c7bfae'), 6, 16)
    p.shape([(90, 480), (510, 480), (510, 530), (90, 530)], hexc('#d4cab6'), None, 5)
    p.stroke([(110, 120), (490, 120), (490, 480), (110, 480), (110, 120)], 6, hexc('#9fc6d6'))
    p.stroke([(150, 160), (220, 200)], 8, (255, 255, 255))
    return p.img


@lru_cache(maxsize=2)
def museum_bg():
    from PIL import ImageDraw
    S = 2; W, H = BW * S, BH * S
    img = Image.new('RGB', (W, H), hexc('#3d3a5c')); d = ImageDraw.Draw(img)
    fl = 1640 * S
    d.rectangle([0, fl, W, H], fill=hexc('#6a5a4a')); d.line([(0, fl), (W, fl)], fill=INK, width=6 * S)
    for x in range(0, W, 160 * S): d.line([(x, fl), (x - 200 * S, H)], fill=hexc('#5a4a3c'), width=4 * S)
    d.polygon([(470 * S, 0), (770 * S, 0), (1000 * S, fl), (240 * S, fl)], fill=hexc('#5a5680'))
    return img.resize((BW, BH), Image.LANCZOS).convert('RGBA')


@lru_cache(maxsize=2)
def pit_bg():
    """dentro da cratera: terra em camadas."""
    from PIL import ImageDraw
    S = 2; W, H = BW * S, BH * S
    img = Image.new('RGB', (W, H), hexc('#8a6440')); d = ImageDraw.Draw(img)
    for i, col in enumerate(('#a37a50', '#946c46', '#7d5a3a', '#6e4e32', '#5e422a')):
        y = (300 + i * 300) * S
        d.rectangle([0, y, W, y + 300 * S], fill=hexc(col))
        d.line([(0, y), (W, y + 30 * S)], fill=mul(hexc(col), .8), width=5 * S)
    r = random.Random(4)
    for _ in range(60):
        x = r.random() * W; y = r.random() * H; rr = (6 + r.random() * 14) * S
        d.ellipse([x - rr, y - rr * .7, x + rr, y + rr * .7], fill=hexc('#b89a74'))
    return img.resize((BW, BH), Image.LANCZOS).convert('RGBA')


def put_bear(c, x, feet, h, f=0, seed=1, shine=0.0, look=0.0, plate=1):
    put_sprite(c, 'gbear', x, feet, h, 500 / 700, False, {'look': 4, 'shine': 2},
               blink=1 if blinkAt(f, seed) > .6 else 0, shine=shine, look=look, plate=plate)


def put_img(c, fn, x, feet, h, aspect, flip=False, **kw):
    put_sprite(c, fn, x, feet, h, aspect, flip, {'dig': 8}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def sparkle(c, x, y, f, f0, n=5, r=230):
    if f < f0: return
    for i in range(n):
        a = i * 2 * math.pi / n + f * .04
        s = .6 + .4 * math.sin(f * .3 + i)
        paste_c(c, star(), x + r * math.cos(a), y + r * .8 * math.sin(a), s * back(ramp(f, f0 + i, f0 + i + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = BG('golden').copy()
    put_img(c, 'mound', 621, 1680, 760, 1242 / 700, dig=1.0)
    ou = wt(0, 'ouro') - 3
    ur = wt(0, 'urso') - 3
    # pás voando (saqueadores) no começo
    if f < ur:
        for i, x in enumerate((470, 780)):
            a = math.sin(f * .35 + i * 2) * 25
            sh = shovel().resize((150, 450)).rotate(a + (20 if i else -20), expand=True, resample=Image.BICUBIC)
            paste_c(c, sh, x, 1100 + 30 * math.sin(f * .35 + i), 1)
        if f % 8 < 5: put_dust(c, 620, 1200, 90, f % 14, 14)
    if f >= ur:
        s = back(ramp(f, ur, ur + 10))
        put_bear(c, 640, 1240 - 120 * s, 380 * s, f=f, seed=1, shine=1)
        sparkle(c, 640, 1060, f, ou, 6, 260)
    num(c, '2.300 ANOS', 640, 560, f, wt(0, 'dois') - 3, 130)
    num(c, 'OURO!', 640, 760, f, ou, 150, 6)
    z = lerp(1.35, 1.05, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, ur + 2)
    return c, (640, 1220 + k * 10, z, k), 'golden'


def s1(f):
    c = BG('day').copy()
    put_img(c, 'mound', 621, 1680, 600, 1242 / 700)
    put_sci(c, 230, 1700, 300, f, 3, arms='point', skin=1, expr='neutral', look=1)
    num(c, 'CAZAQUISTÃO', 640, 660, f, wt(1, 'cazaquistao') - 3, 120)
    num(c, 'ALMATY', 640, 820, f, wt(1, 'almaty') - 3, 100, 3)
    sa = wt(1, 'saca') - 3
    if f >= sa:
        put_img(c, 'hat', 1040, 1300, 300 * back(ramp(f, sa, sa + 8)), 500 / 800)
        num(c, 'POVO SACA', 640, 960, f, sa, 90, -3)
    la = wt(1, 'vinte') - 3
    if f >= la:
        paste_c(c, tape(1000), 621, 1740, back(ramp(f, la, la + 8)))
        num(c, '25 METROS', 640, 1380, f, la, 110, -2)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 200))) * (1 + .0007 * f)
    return c, (lerp(600, 680, ramp(f, 0, 200)), 1250, z, 0), 'day'


def s2(f):
    c = BG('day').copy()
    cr = wt(2, 'cratera') - 3
    put_img(c, 'mound', 621, 1700, 900, 1242 / 700, dig=smooth(ramp(f, cr - 4, cr + 8)))
    put_sci(c, 330, 1330, 300, f, 4, arms='point', bun=True, skin=2, expr='shock' if f >= cr else 'neutral', look=1)
    put_sci(c, 930, 1330, 300, f, 5, arms='cheek', skin=0, expr='neutral', look=-1)
    num(c, '3 METROS', 640, 640, f, wt(2, 'tres') - 3, 130)
    sq = wt(2, 'saqueadores') - 3
    num(c, 'SAQUEADORES', 640, 830, f, sq, 100, 4)
    if f >= sq:
        for i, x in enumerate((540, 740)):
            a = math.sin(f * .4 + i * 2) * 25
            sh = shovel().resize((110, 330)).rotate(a + (20 if i else -20), expand=True, resample=Image.BICUBIC)
            paste_c(c, sh, x, 1060 + 20 * math.sin(f * .4 + i), back(ramp(f, sq, sq + 8)))
        if f % 8 < 5: put_dust(c, 640, 1110, 120, f % 14, 14)
    z = lerp(1.0, 1.25, smooth(ramp(f, cr - 10, cr + 30))) * (1 + .0004 * f)
    k = kick(f, cr)
    return c, (640, lerp(1250, 1150, smooth(ramp(f, cr - 10, cr + 30))) + k * 8, z, k), 'day'


def s3(f):
    c = pit_bg().copy()
    for i, (x, y) in enumerate(((240, 1500), (1000, 1450), (300, 900), (980, 1000))):
        paste_c(c, shard(i + 1).resize((170, 136)).rotate(math.sin(f * .05 + i) * 6 + i * 40, expand=True), x, y, 1)
    ur = wt(3, 'ursinho') - 3
    va = wt(3, 'vaso') - 3
    if f >= ur:
        s = back(ramp(f, ur, ur + 10))
        put_bear(c, 640, 1500, 760 * s, f=f, seed=2, shine=1, look=lerp(-1, 1, smooth(ramp(f, ur, va))))
        sparkle(c, 640, 1150, f, ur + 4, 6, 380)
    num(c, 'BAGUNÇA', 640, 560, f, wt(3, 'baguncaram') - 3, 110, -4)
    if f >= va:
        num(c, 'VASO!', 1020, 980, f, va, 90, 8)
    z = lerp(1.0, 1.18, smooth(ramp(f, ur, ur + 60))) * (1 + .0004 * f)
    k = kick(f, ur)
    return c, (640, lerp(1200, 1180, ramp(f, 0, 200)) + k * 8, z, k), 'day'


def s4(f):
    c = BG('day').copy()
    ch = wt(4, 'chapeu') - 3
    fu = wt(4, 'furinhos') - 3
    hs = smooth(ramp(f, ch - 4, ch + 8))
    if f >= ch - 4:
        put_img(c, 'hat', 640, 1560, 1000 * back(ramp(f, ch - 4, ch + 6)), 500 / 800)
    bx = lerp(640, 640, hs); bf = lerp(1460, 1140, hs); bh = lerp(700, 260, hs)
    put_bear(c, bx, bf, bh, f=f, seed=3, shine=1 if f < fu + 20 else 0)
    if fu <= f < ch:
        for i, x in enumerate((-.3, -.14, .14, .3)):
            paste_c(c, txt('o', 60), bx + x * bh * 500 / 700 * 1.3, bf - 20, 1)
    na = wt(4, 'nunca') - 3
    num(c, 'FURINHOS', 640, 560, f, fu, 100, -3)
    if f >= na:
        num(c, 'INÉDITO NO PAÍS', 640, 720, f, na, 90, 3)
        sparkle(c, 640, 1000, f, na, 5, 330)
    z = lerp(1.15, 1.0, smooth(ramp(f, ch - 6, ch + 20))) * (1 + .0005 * f)
    return c, (640, 1200, z, 0), 'day'


def s5(f):
    c = BG('dusk').copy()
    put_img(c, 'mound', 621, 1700, 520, 1242 / 700, dig=1.0)
    se = wt(5, 'sete') - 3
    if f >= se:
        xs = [200, 340, 480, 620, 780, 910, 1040]
        for i, x in enumerate(xs):
            kid = i >= 4
            paste_c(c, person(kid).resize((150, 300)), x, 1120, back(ramp(f, se + i * 2, se + i * 2 + 8)))
        num(c, '7 PESSOAS', 640, 600, f, se, 130)
        num(c, '4 ADULTOS + 3 CRIANÇAS', 640, 800, f, se + 16, 64, 2)
    no = wt(5, 'normal') - 3
    num(c, 'NORMAL: 1 OU 2', 640, 1360, f, no, 80, -3)
    mi = wt(5, 'misterio') - 3
    num(c, '?', 1060, 460, f, mi, 200, 10)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 180))) * (1 + .0007 * f)
    k = kick(f, se)
    return c, (640, 1150 + k * 8, z, lerp(0, 2, smooth(ramp(f, se, se + 20))) + k), 'dusk'


def s6(f):
    c = museum_bg().copy()
    put_img(c, 'case_', 640, 1720, 950, 600 / 900)
    put_bear(c, 640, 1170, 320, f=f, seed=4, shine=1)
    mu = wt(6, 'museu') - 3
    sparkle(c, 640, 1000, f, mu, 6, 250)
    num(c, 'ESCAVAÇÃO CONTINUA', 640, 520, f, wt(6, 'escavacoes') - 3, 80, -3)
    num(c, 'MUSEU DE ALMATY', 640, 700, f, mu, 100, 3)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    k = kick(f, mu)
    return c, (640, 1200 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'saquearam') - 3, 180, .6)
    s.ting(s.W(0, 'ouro') - 3, .35)
    s.ting(s.W(1, 'cazaquistao') - 3, .25)
    s.thunk(s.W(1, 'vinte') - 3, 200, .4)
    s.thunk(s.W(2, 'cratera') - 3, 140, .8)
    s.ting(s.W(3, 'ursinho') - 3, .4)
    s.ting(s.W(4, 'nunca') - 3, .3)
    s.thunk(s.W(5, 'sete') - 3, 160, .6)
    s.ting(s.W(6, 'museu') - 3, .35)
