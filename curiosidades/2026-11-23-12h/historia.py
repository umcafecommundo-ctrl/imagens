"""Formato MISTÉRIO: "A nuvem da casa 27", PARTE 2 (23/11/2026, 12h). História inventada.
Narradora: a mesma da parte 1 (coque castanho, pele morena, blusa amarela, calça azul).
Resolução: a nuvem passa o dia parada em cima da casa dela, sem chover; às quatro da tarde vai pro quintal e chove num
cantinho perto do muro; lá está o vaso que Dona Zica deu quando se mudou ("cuida dela pra mim"), esquecido e quase seco;
virada: a nuvem nunca foi da casa 27, ela cuidava das plantas de Dona Zica; fim: a plantinha abre a primeira flor e
toda terça, às quatro, chove no quintal dela.
Cenários/cores: s0 CAPA close (rua fria com a nuvem) -> rua de manhã fria, nuvem na casa 12 (frio) | s1 rua de dia, esperando (vivo) |
s2 quintal fim de tarde, nuvem chegando (tarde) | s3 quintal, chuva no cantinho (tarde) | s4 vaso murcho + CLOSE (tarde) |
s5 lembrança: Dona Zica entrega o vaso (tarde) | s6 quintal, chuva no vaso, planta se levanta (vivo) | s7 flor + CLOSE final (vivo)."""
from kit import *
import kit
from sombrio import *
from chuva27 import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='coque', cabelo='#5a3a22', pele='#c99a72', roupa='#f2c14e', calca='#3d5a80')
ZICA = dict(penteado='coque', cabelo='#d8d8d8', pele='#e6c8ad', roupa='#b07aa8', calca='#3a3340', velho=True)
RUA = (('#e8b4b8', '', False), ('#f4d35e', '27', False), ('#a8d0e6', '', False))
MINHA = (('#e8b4b8', '', False), ('#7fb3d5', '12', True), ('#c9e2b3', '', False))
VX, VY = 980, 1630   # vaso no quintal

LINES = [
    "Na parte um, a nuvem que só chovia na casa vinte e sete parou em cima da minha casa.",
    "Eu fiquei olhando o dia inteiro. Ela não chovia. Parecia esperar alguma coisa.",
    "Às quatro da tarde, ela se mexeu. Foi devagar pro meu quintal.",
    "E começou a chover num cantinho só, perto do muro.",
    "Lá estava o vaso que Dona Zica me deu quando se mudou. Eu tinha esquecido dele.",
    "Ela tinha pedido: cuida dela pra mim. E a plantinha estava quase seca.",
    "A nuvem nunca foi da casa vinte e sete. Ela cuidava das plantas de Dona Zica.",
    "Hoje, a plantinha abriu a primeira flor. E toda terça, às quatro, chove no meu quintal.",
]
FALA_TIKTOK = "Você deixaria a nuvem ficar? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'parou', 6), (0, 'casa', 6), (1, 'chovia', 6), (1, 'esperar', 6), (2, 'quatro', 6), (2, 'quintal', 6),
         (3, 'cantinho', 6), (3, 'muro', 6), (4, 'vaso', 6), (4, 'esquecido', 8), (5, 'cuida', 6), (5, 'seca', 6),
         (6, 'nunca', 6), (6, 'plantas', 6), (7, 'flor', 6), (7, 'quintal', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.thunk(2, 120, .6)
    s.thunk(s.W(0, 'parou') - 2, 120, .6)
    s.ting(s.W(1, 'esperar'), .2)
    s.ting(s.W(2, 'quatro'), .3); s.whoosh(s.W(2, 'devagar') - 4, .8, .3)
    s.patter(s.W(3, 'chover') - 2, s.W(3, 'muro') + 30, 4, .06)
    s.patter(s.W(4, 'la'), s.W(4, 'esquecido'), 4, .04)
    s.thunk(s.W(4, 'esquecido') - 2, 60, 1.0)
    s.trill(s.W(5, 'seca'), .5, .12)
    s.patter(s.W(6, 'nuvem'), s.W(6, 'zica') + 20, 4, .05)
    s.ting(s.W(7, 'flor'), .35)
    s.patter(s.W(7, 'toda'), s.W(7, 'quintal') + 30, 4, .05)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA
        c = rua27_bg('frio', MINHA).copy(); nuvem(c, 621, 640, 1, f, chove=0, cor=(206, 214, 224))
        c = put_close(c, f, expr='medo', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'frio'
    g = f - CAPA
    c = rua27_bg('frio', MINHA).copy()
    nuvem(c, 621, 640, 1, f, chove=0, cor=(206, 214, 224))
    eu(c, 260, f, expr='preocupado', look=.75)
    t = smooth(ramp(g, 0, 120))
    cam = (lerp(520, 621, t), lerp(1350, 1100, t), lerp(1.25, 1.02, easeOut(ramp(g, 0, 16))) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'frio'


def s1(f):
    c = rua27_bg('dia', MINHA).copy()
    nuvem(c, 621, 640 + 6 * math.sin(f * .05), 1, f, chove=0)
    eu(c, 300, f, expr='neutro', look=.75)
    cam = (621, lerp(1150, 1000, smooth(ramp(f, 0, 150))), lerp(1.05, 1.15, smooth(ramp(f, 0, 150))) * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = quintal_bg('tarde').copy()
    me = wt(2, 'mexeu') - 3
    t = smooth(ramp(f, me, wt(2, 'quintal') + 6))
    nuvem(c, lerp(-300, VX, t), 700, .85, f, chove=0)
    vaso(c, VX, VY, .55, murcha=.8)
    eu(c, 480, f, expr='choque' if f >= me else 'neutro', look=.75)
    cam = (lerp(560, 700, t), lerp(1150, 1050, t), 1.05 * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    c = quintal_bg('tarde').copy()
    ch = wt(3, 'chover') - 3
    nuvem(c, VX, 700, .85, f, chove=ramp(f, ch, ch + 8), chao=1600)
    vaso(c, VX, VY, .55, murcha=.8)
    eu(c, lerp(480, 640, smooth(ramp(f, ch, ch + 40))), f, walk=1 if ch < f < ch + 40 else 0, expr='preocupado', look=.75)
    mu = wt(3, 'muro') - 3
    t = smooth(ramp(f, mu - 10, mu + 20))
    cam = (lerp(700, 900, t), lerp(1100, 1350, t), lerp(1.05, 1.35, t) * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = quintal_bg('tarde').copy()
    nuvem(c, VX, 700, .85, f, chao=1600)
    vaso(c, VX, VY, .55, murcha=.8)
    es = wt(4, 'esquecido') - 3
    if f >= es:   # CLOSE descoberta
        c = put_close(c, f, expr='choque', look=.25, shake=.3, **EU)
        cam = (621, 1104, lerp(1.2, 1.04, easeOut(ramp(f, es, es + 10))) * (1 + .0009 * f) + .04 * kick(f, es, .6), 0); CAM[4] = cam
        return c, cam, 'tarde'
    va = wt(4, 'vaso') - 3
    t = smooth(ramp(f, 0, va + 6))
    cam = (VX, lerp(1300, 1450, t), lerp(1.4, 2.0, t) * (1 + .0009 * f), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    sc = wt(5, 'e') - 3
    if f < sc:   # lembrança: Dona Zica entrega o vaso
        c = rua27_bg('tarde').copy()
        put_menino(c, 760, 1880, 860, f, expr='sorriso', look=-.75, flip=True, seed=4, **ZICA)
        eu(c, 400, f, expr='sorriso', look=.75)
        vaso(c, 585, 1500, .45, murcha=0)
        cam = (600, 1250, lerp(1.15, 1.25, smooth(ramp(f, 0, sc))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'tarde'
    c = quintal_bg('neblina').copy()
    vaso(c, VX, VY, .55, murcha=1.0)
    cam = (VX, 1470, lerp(2.2, 2.0, smooth(ramp(f, sc, sc + 40))) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'sombrio'


def s6(f):
    c = quintal_bg('dia').copy()
    nuvem(c, VX, 700, .85, f, chao=1600)
    pl = wt(6, 'plantas') - 3
    vaso(c, VX, VY, .55, murcha=.8 * (1 - smooth(ramp(f, 0, pl + 6))))
    eu(c, 600, f, expr='sorriso' if f >= pl else 'neutro', look=.75)
    nu = wt(6, 'nunca') - 3
    cam = (lerp(760, 800, smooth(ramp(f, 0, 120))), 1100, lerp(1.0, 1.1, smooth(ramp(f, 0, 150))) * (1 + .0009 * f) + .04 * kick(f, nu, .6), 0); CAM[6] = cam
    return c, cam, 'vivo'


def s7(f):
    c = quintal_bg('dia').copy()
    fl = wt(7, 'flor') - 3
    to = wt(7, 'toda') - 3
    nuvem(c, VX, 700, .85, f, chove=ramp(f, to, to + 8), chao=1600)
    vaso(c, VX, VY, .55, murcha=0, flor=back(ramp(f, fl, fl + 10)))
    fim = wt(7, 'quintal') - 2
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.2, 1.06, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[7] = cam
        return c, cam, 'vivo'
    t = smooth(ramp(f, 0, fl + 10))
    cam = (VX, lerp(1300, 1450, t), lerp(1.3, 2.0, t) * (1 + .0009 * f), 0)
    if f > to: cam = (lerp(VX, 800, smooth(ramp(f, to, to + 20))), lerp(1450, 1150, smooth(ramp(f, to, to + 20))), lerp(2.0, 1.1, smooth(ramp(f, to, to + 20))) * (1 + .0009 * f), 0)
    CAM[7] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 2', 540, 100, 1, 64, big=True)
            gancho(im, ['A NUVEM PAROU', 'NA MINHA CASA'], 180, 1, 104)
        else:
            stamp(im, 'PARTE 2', 290, 230, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
    elif si == 1:
        ch = wt(1, 'chovia') - 3; es = wt(1, 'esperar') - 3
        hora = ['08:00', '10:00', '12:00', '14:00', '15:00'][min(4, int(f / 40))]
        painel(im, 'ESPERANDO', hora, 780, 260, ramp(f, 0, 10), w=380)
        card(im, 'Nuvem', 'parada, sem chover', 760, 560, ramp(f, ch, ch + 10))
    elif si == 2:
        q = wt(2, 'quatro') - 3
        painel(im, 'HORA', '16:00', 780, 260, ramp(f, q, q + 10), w=380)
    elif si == 3:
        ca = wt(3, 'cantinho') - 3
        burst(im, 'PLIC PLIC', 300, 300, back(ramp(f, ca, ca + 8)), 50)
    elif si == 4:
        va = wt(4, 'vaso') - 3; es = wt(4, 'esquecido') - 3
        if f < es: card(im, 'O vaso', 'presente da Dona Zica', 300, 300, ramp(f, va, va + 10))
        else: stamp(im, 'EU ESQUECI', 540, 250, back(ramp(f, es + 2, es + 10)), 76)
    elif si == 5:
        cu = wt(5, 'cuida') - 3; se = wt(5, 'seca') - 3
        if f < wt(5, 'e') - 3:
            kit.paste_c(im, bilhete_img('CUIDA DELA|PRA MIM.', 520), 540, 360, back(ramp(f, cu, cu + 8)))
        else:
            stamp(im, 'QUASE SECA', 540, 260, back(ramp(f, se, se + 8)), 80)
    elif si == 6:
        nu = wt(6, 'nunca') - 3; pl = wt(6, 'plantas') - 3
        stamp(im, 'A VERDADE', 300, 230, back(ramp(f, nu, nu + 8)), 100, big=True)
        card(im, 'A nuvem', 'cuida das plantas da Dona Zica', 330, 470, ramp(f, pl, pl + 10))
    elif si == 7:
        fl = wt(7, 'flor') - 3; to = wt(7, 'toda') - 3
        if f < to: stamp(im, '1ª FLOR', 540, 250, back(ramp(f, fl, fl + 8)), 90)
        else: painel(im, 'TODA TERÇA', '16:00', 540, 260, ramp(f, to, to + 10), w=420)
    return grao(im.convert('RGB'), lf)
