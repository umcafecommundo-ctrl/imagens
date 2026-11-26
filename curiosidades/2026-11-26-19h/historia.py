"""Formato MISTÉRIO: "A estação Girassol", PARTE 1 (26/11/2026, 19h). História inventada.
Narradora: menina de cabelo longo preto, pele morena, blusa rosa e calça azul (mesmas cores na parte 2).
Premissa: no metrô da cidade existe uma estação que não está no mapa, a Girassol; o trem só para lá às 17h e só com o vagão
quase vazio; a porta abre e lá fora é tudo amarelo, girassóis do chão ao teto; regra do metrô: ninguém desce na Girassol;
o seu Jonas, da banca de jornal, desceu uma vez há 40 anos e nunca contou o que viu, mas toda tarde às 17h fecha a banca e
fica olhando a escada do metrô; hoje às 17h ela estava sozinha no vagão, o trem parou e a porta abriu: no meio dos
girassóis o seu Jonas acenava pra ela, mas ela tinha acabado de deixá-lo lá em cima, na banca.
Cenários/cores: s0 CAPA close (vagão de tarde) -> mapa do metrô (vivo) | s1 vagão de tarde, túnel (tarde) | s2 porta abrindo
para os girassóis -> estação Girassol (vivo) | s3 vagão com a porta aberta, regra (tarde) | s4 rua de tarde com a banca e o
seu Jonas (tarde) | s5 a mesma rua, ele olhando a escada + CLOSE curioso (tarde) | s6 vagão sozinha, trem para, porta abre
(tarde) | s7 girassóis com o seu Jonas acenando + CLOSE final (tarde)."""
from kit import *
import kit
from sombrio import *
from girassol import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'; PITCH = '-4Hz'
EU = dict(penteado='longo', cabelo='#1e1a18', pele='#8d5a3c', roupa='#e5739a', calca='#2d4f7a')
JONAS = dict(penteado='careca', velho=True, barba=True, cabelo='#e6e6e6', pele='#c98f65', roupa='#c8553d', calca='#3a3a40')

LINES = [
    "No metrô da minha cidade, tem uma estação que não está no mapa. A estação Girassol.",
    "O trem só para lá às cinco da tarde. E só quando o vagão está quase vazio.",
    "A porta abre, e lá fora é tudo amarelo. Girassol do chão até o teto.",
    "E a regra do metrô é uma só: ninguém desce na Girassol.",
    "O seu Jonas, da banca de jornal, desceu lá uma vez, há quarenta anos. Ele nunca contou o que viu.",
    "Mas toda tarde, às cinco, ele fecha a banca e fica olhando pra escada do metrô.",
    "Hoje, às cinco, eu estava sozinha no vagão. O trem parou. E a porta abriu.",
    "No meio dos girassóis, alguém acenava pra mim. Era o seu Jonas... mas eu tinha acabado de deixar ele na banca.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "EU DESÇO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 7
FLASH = []
CHECK = [(0, 'mapa', 6), (0, 'girassol', 8), (1, 'cinco', 6), (1, 'vazio', 6), (2, 'abre', 6), (2, 'amarelo', 6),
         (2, 'teto', 6), (3, 'regra', 4), (3, 'desce', 6), (4, 'jonas', 6), (4, 'quarenta', 6), (5, 'fecha', 6),
         (5, 'escada', 6), (6, 'parou', 6), (6, 'abriu', 8), (7, 'acenava', 6), (7, 'jonas', 8), (7, 'banca', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    s.ting(s.W(0, 'mapa'), .3); s.thunk(s.W(0, 'girassol') - 2, 80, .5)
    s.ting(s.W(1, 'cinco'), .3)
    s.whoosh(s.W(2, 'abre') - 3, .6, .25); s.ting(s.W(2, 'amarelo'), .35)
    s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.ting(s.W(4, 'jonas'), .3); s.thunk(s.W(4, 'quarenta') - 2, 70, .5)
    s.thunk(s.W(5, 'fecha') - 2, 60, .4)
    s.thunk(s.W(6, 'parou') - 2, 90, .8); s.whoosh(s.W(6, 'abriu') - 3, .6, .25)
    s.ting(s.W(7, 'acenava'), .3); s.thunk(s.W(7, 'banca') + 4, 60, 1.0)


def eu(c, x, f, feet=1960, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def jonas(c, x, f, feet=2000, h=960, **kw):
    put_menino(c, x, feet, h, f, seed=5, **dict(JONAS, **kw))


def rz(f):
    return 1 + .0012 * f


def rua_banca(luz='tarde'):
    return _rua_banca(luz)


from functools import lru_cache


@lru_cache(maxsize=4)
def _rua_banca(luz):
    c = rua(0, 300, luz=luz, neb=0).copy()
    c.alpha_composite(banca_img(620, luz), (560, 1545 - 760))
    # entrada do metrô (escada) à esquerda
    p = Pen(W_, H_)
    p.shape([(40, 1545), (40, 1330), (420, 1330), (420, 1545)], hexc('#3f7fc4'), None, 6, 0)
    p.shape([(80, 1545), (80, 1400), (380, 1400), (380, 1545)], hexc('#2b3440'), None, 5, 0)
    for y in (1430, 1465, 1500): p.stroke([(90, y), (370, y)], 5, hexc('#6b7280'))
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    d = ImageDraw.Draw(c); fnt = font(F_STAMP, 56)
    d.text((230 - d.textlength('METRÔ', font=fnt) / 2, 1336), 'METRÔ', font=fnt, fill=(250, 250, 240))
    return c


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = vagao_bg('tarde', 'girassol', 1).copy()
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * rz(f), 0); CAM[0] = cam
        return c, cam, 'tarde'
    c = mapa_bg().copy()
    gi = wt(0, 'girassol') - 3
    if f >= gi:
        g = girassol_img(260); c.alpha_composite(g, (930, int(lerp(560, 500, ramp(f, gi, gi + 8)))))
    t = smooth(ramp(f, CAPA, gi))
    cam = (lerp(560, 760, t) if f < gi else 900, lerp(1100, 1000, t) if f < gi else 760,
           lerp(1.3, 1.1, easeOut(ramp(f, CAPA, CAPA + 14))) * rz(f) if f < gi else 1.7 * rz(f) + .07 * kick(f, gi, .7), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = vagao_bg('tarde', 'tunel', 0).copy()
    eu(c, 300, f, expr='neutro', look=.6)
    va = wt(1, 'vazio') - 3
    t = smooth(ramp(f, 0, va))
    cam = (lerp(420, 621, t), lerp(1300, 1200, t), lerp(1.3, 1.05, t) * rz(f) + .05 * kick(f, va, .6), .6 * math.sin(f * .5)); CAM[1] = cam
    return c, cam, 'tarde'


def s2(f):
    te = wt(2, 'teto') - 3; ab = wt(2, 'abre') - 3; ch = wt(2, 'chao') - 3
    if f < ch:
        c = vagao_bg('tarde', 'girassol', round(easeOut(ramp(f, ab, ab + 12)) * 8) / 8).copy()
        eu(c, 300, f, expr='curioso', look=.6)
        cam = (540, 1200, lerp(1.1, 1.3, smooth(ramp(f, 0, ch))) * rz(f), 0); CAM[2] = cam
        return c, cam, 'tarde'
    c = estacao_girassol_bg('dia').copy()
    t = smooth(ramp(f, ch, te + 6))
    cam = (621, lerp(1500, 800, t), 1.15 * rz(f) + .05 * kick(f, te, .6), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = vagao_bg('tarde', 'girassol', 1).copy()
    de = wt(3, 'desce') - 3
    eu(c, lerp(300, 260, ramp(f, de, de + 10)), f, expr='curioso' if f < de else 'preocupado', look=.7)
    cam = (lerp(520, 560, ramp(f, 0, de)), 1300, lerp(1.1, 1.25, smooth(ramp(f, 0, de))) * rz(f) + .06 * kick(f, de, .6), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = rua_banca('tarde').copy()
    nu = wt(4, 'nunca') - 3
    jonas(c, 760, f, expr='sorriso' if f < nu else 'desconfiado', look=-.4)
    qu = wt(4, 'quarenta') - 3
    cam = (lerp(700, 760, smooth(ramp(f, 0, nu))), 1420, lerp(1.25, 1.45, smooth(ramp(f, 0, nu))) * rz(f) + .05 * kick(f, qu, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    es = wt(5, 'escada') - 3; fe = wt(5, 'fecha') - 3
    c = rua_banca('tarde').copy()
    if f >= es + 14:   # CLOSE curioso da narradora
        eu(c, 620, f, expr='curioso', look=.6)
        c = put_close(c, f, expr='curioso', look=.75, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, es + 14, es + 24))) * rz(f - es), 0); CAM[5] = cam
        return c, cam, 'tarde'
    jonas(c, 620, f, expr='neutro', look=-1, flip=True)
    t = smooth(ramp(f, 0, es + 6))
    cam = (lerp(600, 380, t), lerp(1420, 1420, t), 1.2 * rz(f) + .05 * kick(f, fe, .6), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    pa = wt(6, 'parou') - 3; ab = wt(6, 'abriu') - 3
    fora = 'tunel' if f < pa else 'girassol'
    c = vagao_bg('tarde', fora, round(easeOut(ramp(f, ab, ab + 12)) * 8) / 8 if f >= ab else 0).copy()
    eu(c, 300, f, expr='neutro' if f < pa else 'curioso', look=.6)
    sh = 6 * math.sin(f * 2.1) * (1 - ramp(f, pa, pa + 10)) if f >= pa else 0
    cam = (lerp(440, 560, smooth(ramp(f, 0, ab))) + sh, 1280, lerp(1.25, 1.05, smooth(ramp(f, 0, ab))) * rz(f) + .07 * kick(f, pa, .8), 0); CAM[6] = cam
    return c, cam, 'tarde'


def s7(f):
    ba = wt(7, 'banca') - 3; jo = wt(7, 'jonas') - 3
    fim = ba + 14
    if f >= fim:
        c = vagao_bg('tarde', 'girassol', 1).copy()
        c = put_close(c, f, expr='medo', look=0, escurece=.25, suor=1, shake=.3, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * rz(f - fim), 0); CAM[7] = cam
        return c, cam, 'tarde'
    c = vagao_bg('tarde', 'girassol', 1).copy()
    jonas(c, 621, f, feet=1555 - 18 * abs(math.sin(f * .25)), h=760, expr='sorriso', look=0)
    z = 1.3 if f < jo else 1.7
    cam = (621, 1200 if f < jo else 1080, z * rz(f) + .08 * kick(f, jo, .8), 0); CAM[7] = cam
    return c, cam, 'tarde'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['A ESTAÇÃO QUE', 'NÃO ESTÁ NO MAPA'], 170, 1, 100)
            stamp(im, 'PARTE 1', 880, 1240, 1, 46)
        else:
            gi = wt(0, 'girassol') - 3
            if f < gi: stamp(im, 'NO METRÔ DA MINHA CIDADE', 540, 230, back(ramp(f, CAPA + 2, CAPA + 10)), 58)
            else: card(im, 'Estação Girassol', 'fora do mapa', 540, 260, ramp(f, gi, gi + 10))
    elif si == 1:
        ci = wt(1, 'cinco') - 3; va = wt(1, 'vazio') - 3
        painel(im, 'SÓ ÀS', '17:00', 540, 280, ramp(f, ci, ci + 10), w=360)
        if f >= va: card(im, 'Vagão', 'quase vazio', 540, 520, ramp(f, va, va + 10))
    elif si == 2:
        am = wt(2, 'amarelo') - 3; ch = wt(2, 'chao') - 3
        if f < ch: burst(im, 'UAU', 540, 280, back(ramp(f, am, am + 8)), 70, cor=(240, 190, 60)) if f >= am else None
        else: stamp(im, 'DO CHÃO ATÉ O TETO', 540, 250, back(ramp(f, ch, ch + 8)), 66)
    elif si == 3:
        r = wt(3, 'regra') - 3; de = wt(3, 'desce') - 3
        stamp(im, 'A REGRA', 540, 230, back(ramp(f, r, r + 8)), 100, big=True)
        card(im, 'Ninguém desce', 'na Girassol', 540, 450, ramp(f, de - 4, de + 6))
    elif si == 4:
        jo = wt(4, 'jonas') - 3; qu = wt(4, 'quarenta') - 3; nu = wt(4, 'nunca') - 3
        if f < qu: card(im, 'Seu Jonas', 'o da banca', 540, 240, ramp(f, jo, jo + 10))
        elif f < nu: painel(im, 'DESCEU HÁ', '40 ANOS', 540, 280, ramp(f, qu, qu + 10), w=420)
        else: burst(im, 'SEGREDO', 540, 280, back(ramp(f, nu, nu + 8)), 64)
    elif si == 5:
        ci = wt(5, 'cinco') - 3; es = wt(5, 'escada') - 3
        if f < es + 14: painel(im, 'TODA TARDE', '17:00', 760, 300, ramp(f, ci, ci + 10), w=400)
        else: interrog(im, 540, 260, f, ramp(f, es + 14, es + 22))
    elif si == 6:
        so = wt(6, 'sozinha') - 3; pa = wt(6, 'parou') - 3; ab = wt(6, 'abriu') - 3
        if f < pa: card(im, 'Hoje, 17:00', 'sozinha no vagão', 540, 250, ramp(f, so, so + 10))
        elif f < ab: burst(im, 'TSSS', 540, 280, back(ramp(f, pa, pa + 6)), 70, cor=(150, 160, 175))
        else: stamp(im, 'GIRASSOL', 540, 250, back(ramp(f, ab, ab + 8)), 96, big=True)
    elif si == 7:
        ac = wt(7, 'acenava') - 3; jo = wt(7, 'jonas') - 3; ba = wt(7, 'banca') - 3; fim = ba + 14
        if f < jo: burst(im, 'OI!', 540, 260, back(ramp(f, ac, ac + 6)), 80, cor=(240, 190, 60)) if f >= ac else None
        elif f < fim: card(im, 'Seu Jonas?!', 'ele estava na banca', 540, 250, ramp(f, jo, jo + 8))
        else: stamp(im, 'COMO ASSIM?', 540, 250, back(ramp(f, fim + 2, fim + 10)), 84, rot=3)
    return grao(im.convert('RGB'), lf)
