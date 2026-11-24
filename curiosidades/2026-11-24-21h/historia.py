"""Formato MISTÉRIO: "O boneco de neve que anda", PARTE 2 (24/11/2026, 21h). História inventada.
Narradora: a mesma da parte 1 (cabelo ruivo comprido, pele clara, casaco azul, calça escura).
Resolução: ela segue o olhar do boneco e sobe o morro; lá no alto há uma casinha com fumaça na chaminé, e ninguém da
vila sabia que alguém morava ali; na janela uma senhora tricota um cachecol vermelho igual ao do boneco; ela fez o
primeiro boneco da vila há sessenta anos e hoje não consegue mais descer o morro; os presentes de lã eram dela e dessa vez
o boneco foi buscar uma visita; fim: a narradora sobe o morro todo domingo e este ano o boneco não derreteu.
Cenários/cores: s0 CAPA close (vila fria com o morro) -> portão de manhã, boneco de costas (frio) | s1 subindo o morro à
tarde (tarde) | s2 a casinha com fumaça (tarde) | s3 a janela com a senhora tricotando + CLOSE (tarde) | s4 dentro da
casinha, lareira (tarde) | s5 cesto de lã, presentes (tarde) | s6 morro de dia com sol, boneco na porta + CLOSE final (vivo)."""
from kit import *
import kit
from sombrio import *
from neve_vila import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='longo', cabelo='#c0622f', pele='#e6c8ad', roupa='#3a7bd5', calca='#2d2f32')
SRA = dict(penteado='coque', cabelo='#e8e8e8', pele='#e6c8ad', roupa='#7a5aa8', calca='#3a3340', velho=True)

LINES = [
    "Na parte um, o boneco de neve parou no meu portão, de costas, olhando pro alto do morro.",
    "Eu segui o olhar dele e subi o morro, afundando na neve até o joelho.",
    "Lá no alto, tinha uma casinha com fumaça na chaminé. Ninguém na vila sabia que alguém morava ali.",
    "Na janela, uma senhora tricotava um cachecol vermelho. Igual ao do boneco.",
    "Ela fez o primeiro boneco da vila, há sessenta anos. Hoje, não consegue mais descer o morro.",
    "Os presentes de lã eram dela. E dessa vez, o boneco foi buscar uma visita.",
    "Agora eu subo o morro todo domingo. E este ano, o boneco não derreteu.",
]
FALA_TIKTOK = "Você subiria o morro? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 5
FLASH = []
CHECK = [(0, 'portao', 6), (0, 'morro', 6), (1, 'subi', 6), (2, 'casinha', 6), (2, 'ninguem', 6), (3, 'senhora', 6),
         (3, 'igual', 8), (4, 'sessenta', 6), (4, 'descer', 6), (5, 'presentes', 6), (5, 'visita', 8), (6, 'domingo', 6),
         (6, 'derreteu', 10)]
CAM = {}
CAPA = 36
CASA_X, CASA_Y, CASA_S = 121, 640, 1000   # casinha grande (s2/s6)


def SFX(s):
    s.whoosh(2, .5, .15)
    s.thunk(s.W(0, 'portao') - 2, 60, .5)
    for k in range(5): s.thunk(s.W(1, 'subi') + k * 10, 35, .3)
    s.ting(s.W(2, 'casinha'), .3); s.thunk(s.W(2, 'ninguem') - 2, 80, .5)
    s.ting(s.W(3, 'senhora'), .25); s.thunk(s.W(3, 'igual') + 4, 90, .8)
    s.ting(s.W(4, 'sessenta'), .3)
    s.ting(s.W(5, 'presentes'), .3); s.ting(s.W(5, 'visita'), .35)
    s.ting(s.W(6, 'derreteu'), .4)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def casa_grande(c, f, luz_fumaca=True):
    ch = casinha_img().resize((CASA_S, CASA_S), Image.LANCZOS)
    c.alpha_composite(ch, (CASA_X, CASA_Y))
    if luz_fumaca: fumaca(c, CASA_X + CASA_S * 300 / 420, CASA_Y + CASA_S * 40 / 420, f, 2)


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = vila_bg('frio', True).copy(); portao(c, 621, 1900, 1.3); put_boneco(c, 621, 1840, 760, costas=True)
        c = put_close(c, f, expr='preocupado', look=0, shake=.15, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'frio'
    g = f - CAPA
    c = vila_bg('frio', True).copy()
    portao(c, 621, 1900, 1.3); put_boneco(c, 621, 1840, 760, costas=True)
    mo = wt(0, 'morro') - 3
    t = smooth(ramp(g, 0, 40)); t2 = smooth(ramp(f, mo - 10, mo + 14))
    cam = (lerp(621, 900, t2), lerp(lerp(1250, 1300, t), 820, t2), lerp(lerp(1.2, 1.05, t), 1.5, t2) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'frio'


def s1(f):
    c = vila_bg('tarde', True).copy()
    flocos(c, f, 80, 3)
    t = smooth(ramp(f, 0, 150))
    x = lerp(380, 820, t); feet = lerp(1600, 1150, t)
    pegadas(c, [(lerp(380, 820, k), lerp(1600, 1150, k) + 10 * ((i % 2) * 2 - 1)) for i, k in enumerate([j / 12 for j in range(13)]) if k < t - .05], 16)
    eu(c, x, f, feet=feet, h=520, walk=1, expr='neutro', look=.75)
    cam = (lerp(450, 800, t), lerp(1350, 950, t), 1.35 * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'tarde'


def s2(f):
    c = vila_bg('tarde').copy()
    casa_grande(c, f)
    eu(c, 990, f, feet=1960, h=760, expr='preocupado' if f >= wt(2, 'ninguem') - 3 else 'neutro', look=-.75, flip=True)
    ca = wt(2, 'casinha') - 3
    t = smooth(ramp(f, 0, ca + 10))
    cam = (621, lerp(1000, 1150, t), lerp(1.25, 1.02, t) * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    ig = wt(3, 'igual') - 3
    c = Image.new('RGBA', (W_, H_), (250, 214, 150, 255))
    put_menino(c, 621, 1750, 1100, f, expr='sorriso', look=.25, seed=4, **SRA)
    trico(c, 640 + 6 * math.sin(f * .4), 1200, 1.0)
    c.alpha_composite(parede_janela('tarde'))
    if f >= ig + 2:   # CLOSE descoberta
        c = put_close(c, f, expr='choque', look=-.25, shake=.2, **EU)
        cam = (621, 1104, lerp(1.2, 1.05, easeOut(ramp(f, ig + 2, ig + 10))) * (1 + .0009 * f), 0); CAM[3] = cam
        return c, cam, 'tarde'
    t = smooth(ramp(f, 0, ig))
    cam = (621, lerp(1000, 900, t), lerp(1.0, 1.35, t) * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = interior_bg('tarde').copy()
    put_menino(c, 820, 1900, 860, f, expr='sorriso', look=-.75, flip=True, seed=4, **SRA)
    eu(c, 300, f, expr='neutro', look=.75)
    se = wt(4, 'sessenta') - 3
    t = smooth(ramp(f, 0, 160))
    cam = (lerp(560, 640, t), lerp(1150, 1200, t), lerp(1.05, 1.15, t) * (1 + .0009 * f) + .04 * kick(f, se, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = interior_bg('tarde').copy()
    pr = wt(5, 'presentes') - 3
    cesto_la(c, 960, 1900, 1.4)
    put_menino(c, 620, 1900, 860, f, expr='sorriso', look=.5, seed=4, **SRA)
    eu(c, 250, f, expr='sorriso' if f >= wt(5, 'visita') - 3 else 'neutro', look=.75)
    t = smooth(ramp(f, 0, pr + 10))
    cam = (lerp(621, 850, t), lerp(1150, 1500, t), lerp(1.0, 1.5, t) * (1 + .0009 * f), 0)
    vi = wt(5, 'visita') - 3
    if f > vi - 10:
        u = smooth(ramp(f, vi - 10, vi + 10))
        cam = (lerp(cam[0], 450, u), lerp(cam[1], 1150, u), lerp(cam[2], 1.1, u), 0)
    CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = vila_bg('dia').copy()
    casa_grande(c, f)
    put_boneco(c, 980, 1880, 700, look=-1)
    de = wt(6, 'derreteu') - 3
    if f >= de + 4:   # CLOSE final sorrindo
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.25, 1.06, easeOut(ramp(f, de + 4, de + 12))) * (1 + .0012 * (f - de)), 0); CAM[6] = cam
        return c, cam, 'vivo'
    put_menino(c, 640, 1900, 820, f, expr='sorriso', look=-.5, flip=True, seed=4, **SRA)
    eu(c, 260, f, expr='sorriso', look=.75)
    t = smooth(ramp(f, 0, de))
    cam = (621, lerp(1250, 1150, t), lerp(1.15, 1.02, t) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 2', 540, 100, 1, 64, big=True)
            gancho(im, ['QUEM MORA NO', 'ALTO DO MORRO?'], 180, 1, 100)
        else:
            stamp(im, 'NA PARTE 1', 540, 210, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
    elif si == 1:
        su = wt(1, 'subi') - 3; jo = wt(1, 'joelho') - 3
        stamp(im, 'MORRO ACIMA', 540, 210, back(ramp(f, su, su + 8)), 76)
        burst(im, 'PLOFT', 820, 430, back(ramp(f, jo, jo + 8)) if f >= jo else 0, 54)
    elif si == 2:
        ca = wt(2, 'casinha') - 3; n = wt(2, 'ninguem') - 3
        if f < n: card(im, 'Lá no alto', 'fumaça na chaminé', 330, 230, ramp(f, ca, ca + 10))
        else: card(im, 'Ninguém sabia', 'que alguém morava ali', 330, 230, ramp(f, n, n + 10))
    elif si == 3:
        se = wt(3, 'senhora') - 3; ig = wt(3, 'igual') - 3
        if f < ig + 2: card(im, 'Na janela', 'um cachecol vermelho', 540, 200, ramp(f, se, se + 10))
        else: stamp(im, 'IGUAL AO DO BONECO', 540, 250, back(ramp(f, ig + 4, ig + 12)), 66, rot=3)
    elif si == 4:
        se = wt(4, 'sessenta') - 3; de = wt(4, 'descer') - 3
        painel(im, 'O 1º BONECO, HÁ', '60 ANOS', 540, 230, ramp(f, se, se + 10), w=520)
        card(im, 'Hoje', 'não desce mais o morro', 540, 450, ramp(f, de, de + 10))
    elif si == 5:
        pr = wt(5, 'presentes') - 3; vi = wt(5, 'visita') - 3
        if f < vi - 6: card(im, 'Os presentes de lã', 'eram dela', 400, 240, ramp(f, pr, pr + 10))
        else: stamp(im, 'FOI BUSCAR UMA VISITA', 540, 250, back(ramp(f, vi - 4, vi + 4)), 64)
    elif si == 6:
        do = wt(6, 'domingo') - 3; de = wt(6, 'derreteu') - 3
        if f < de + 4: painel(im, 'TODO', 'DOMINGO', 540, 230, ramp(f, do, do + 10), w=560)
        else: stamp(im, 'NÃO DERRETEU', 540, 250, back(ramp(f, de + 8, de + 16)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
