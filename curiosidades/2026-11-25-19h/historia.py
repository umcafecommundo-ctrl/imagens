"""Formato MISTÉRIO: "A árvore dos bolinhos", PARTE 1 (25/11/2026, 19h). História inventada.
Narrador: menino de cabelo curto preto, pele morena, camiseta amarela e calça azul (mesmas cores na parte 2).
Premissa: na floresta perto de casa há uma árvore enorme com uma portinha no tronco; toda vez que alguém da cidade faz
aniversário aparece um bolinho na portinha com o nome da pessoa; regra: ninguém abre a portinha (trancada por dentro);
ninguém sabe quem faz os bolinhos e a árvore nunca esqueceu ninguém; no aniversário do narrador o bolinho era de chocolate;
hoje cedo apareceu um bolinho com vela de número cem, e ninguém na cidade faz cem anos hoje.
Cenários/cores: s0 CAPA close (floresta de dia) -> floresta de dia, a árvore (vivo) | s1 portinha de perto, bolinho com
nome (vivo) | s2 a regra, vizinho tenta abrir, fim de tarde (tarde) | s3 floresta à noite, portinha com luz (sombrio_noite) |
s4 lembrança do aniversário dele (tarde) | s5 hoje cedo, bolinho de vela 100 + CLOSE choque (frio) | s6 rua de dia
perguntando + CLOSE final (vivo)."""
from kit import *
import kit
from sombrio import *
from arvore import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'; PITCH = '-4Hz'
EU = dict(penteado='curto', cabelo='#1e1712', pele='#8a5a3a', roupa='#f2b134', calca='#2f4a6a')
VIZ = dict(penteado='careca', cabelo='#3a2a22', pele='#e6c8ad', roupa='#5a7fb8', calca='#2d2f32', barba=True)
VIZ2 = dict(penteado='longo', cabelo='#c0622f', pele='#e6c8ad', roupa='#d8423a', calca='#2d2f32')
PX, PB = 621, 1830   # portinha: centro x e base y

LINES = [
    "Na floresta perto da minha casa, tem uma árvore enorme com uma portinha no tronco.",
    "Toda vez que alguém da cidade faz aniversário, aparece um bolinho na portinha. Com o nome da pessoa.",
    "A regra é uma só: ninguém abre a portinha. Quem tentou, achou ela trancada por dentro.",
    "Ninguém sabe quem faz os bolinhos. E em todos esses anos, a árvore nunca esqueceu ninguém.",
    "No meu aniversário, o meu bolinho estava lá. De chocolate, do jeitinho que eu gosto.",
    "Mas hoje cedo apareceu um bolinho diferente. Com uma vela de número cem.",
    "Eu perguntei na cidade inteira. E ninguém aqui... faz cem anos hoje.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "EU ABRO A PORTINHA?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 5
FLASH = []
CHECK = [(0, 'arvore', 6), (0, 'portinha', 6), (1, 'aniversario', 6), (1, 'nome', 6), (2, 'regra', 4), (2, 'trancada', 6),
         (3, 'ninguem', 6), (3, 'esqueceu', 6), (4, 'chocolate', 6), (5, 'vela', 6), (5, 'cem', 8), (6, 'cidade', 6),
         (6, 'hoje', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    s.ting(s.W(0, 'portinha'), .3)
    s.ting(s.W(1, 'aniversario'), .3); s.ting(s.W(1, 'nome'), .3)
    s.thunk(s.W(2, 'regra') - 2, 90, .7); s.thunk(s.W(2, 'trancada'), 60, .5); s.thunk(s.W(2, 'trancada') + 7, 60, .4)
    s.trill(s.W(3, 'ninguem'), .2)
    s.ting(s.W(4, 'chocolate'), .3)
    s.whoosh(s.W(5, 'hoje') - 3, .6, .2); s.ting(s.W(5, 'vela'), .35); s.thunk(s.W(5, 'cem') - 2, 80, .7)
    s.thunk(s.W(6, 'hoje') + 4, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=2040, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def brilho(c, x, y, a):
    if a <= 0: return
    gl = Image.new('RGBA', c.size, (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
    dg.ellipse((x - 200, y - 200, x + 200, y + 200), fill=(255, 210, 120, int(150 * a)))
    c.alpha_composite(gl.filter(ImageFilter.GaussianBlur(50)))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = floresta_arvore('dia').copy()
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0012 * f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    c = floresta_arvore('dia').copy()
    po = wt(0, 'portinha') - 3
    eu(c, 260, f, walk=1 if f < po else 0, expr='neutro' if f < po else 'curioso', look=.8)
    t = smooth(ramp(g, 0, po - CAPA + 10))
    cam = (lerp(621, 560, t), lerp(900, 1450, t), lerp(1.15, 1.2, t) * (1 + .0012 * f) + .05 * kick(f, po, .6), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = floresta_arvore('dia').copy()
    bo = wt(1, 'bolinho') - 3; no = wt(1, 'nome') - 3
    put_bolinho(c, PX, PB + 10, 230, back(ramp(f, bo, bo + 8)) if f >= bo else 0, nome='MALU' if f >= no else None)
    t = smooth(ramp(f, 0, 140))
    cam = (PX, lerp(1650, 1700, t), lerp(2.0, 2.3, t) * (1 + .0012 * f) + .06 * kick(f, bo, .6) + .05 * kick(f, no, .6), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = floresta_arvore('tarde').copy()
    tr = wt(2, 'trancada') - 3; r = wt(2, 'regra') - 3
    sh = 6 * math.sin(f * 2) * ramp(f, tr, tr + 4) * (1 - ramp(f, tr + 16, tr + 20))
    put_menino(c, 470 + sh, 2000, 880, f, expr='neutro' if f < tr else 'preocupado', look=.9, seed=5, **VIZ)
    cam = (580, 1400, lerp(1.15, 1.3, smooth(ramp(f, 0, 160))) * (1 + .0012 * f) + .05 * kick(f, r, .6) + .04 * kick(f, tr, .5), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    c = floresta_arvore('noite').copy()
    brilho(c, PX, PB - 120, .6 + .4 * math.sin(f * .15))
    t = smooth(ramp(f, 0, 170))
    cam = (621, lerp(1100, 1500, t), lerp(1.0, 1.5, t) * (1 + .0012 * f), 0); CAM[3] = cam
    return c, cam, 'sombrio_noite'


def s4(f):
    c = floresta_arvore('tarde').copy()
    ch = wt(4, 'chocolate') - 3; bo = wt(4, 'bolinho') - 3
    put_bolinho(c, PX + 40, PB + 10, 230, back(ramp(f, bo, bo + 8)) if f >= bo else 0, nome='PARABÉNS')
    eu(c, 330, f, expr='curioso' if f < ch else 'sorriso', look=.9)
    t = smooth(ramp(f, 0, 150))
    cam = (lerp(480, 560, t), 1500, lerp(1.25, 1.35, t) * (1 + .0012 * f) + .05 * kick(f, ch, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = floresta_arvore('frio').copy()
    ve = wt(5, 'vela') - 3; ce = wt(5, 'cem') - 3; bo = wt(5, 'bolinho') - 3
    put_bolinho(c, PX, PB + 10, 260, back(ramp(f, bo, bo + 8)) if f >= bo else 0, vela='100' if f >= ve else None, cor='#f0e2c8')
    if f >= ce + 8:   # CLOSE choque
        c = put_close(c, f, expr='choque', look=.3, shake=.3, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, ce + 8, ce + 16))) * (1 + .0012 * f), 0); CAM[5] = cam
        return c, cam, 'frio'
    eu(c, 150, f, expr='curioso', look=.9)
    t = smooth(ramp(f, 0, ve))
    cam = (lerp(480, PX, t), lerp(1450, 1620, t), lerp(1.1, 2.0, t) * (1 + .0012 * f) + .06 * kick(f, ve, .6) + .06 * kick(f, ce, .6), 0); CAM[5] = cam
    return c, cam, 'frio'


def s6(f):
    c = rua(f, 200 + f * 3, luz='dia', neb=0)
    ho = wt(6, 'hoje') - 3; ni = wt(6, 'ninguem') - 3
    fim = ho + 2
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.3, suor=1, shake=.2, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[6] = cam
        return c, cam, 'vivo'
    eu(c, 300, f, feet=1960, expr='neutro' if f < ni else 'preocupado', look=.8)
    put_menino(c, 700, 1960, 880, f, expr='curioso' if f < ni else 'preocupado', look=-.8, flip=True, seed=5, **VIZ)
    put_menino(c, 1000, 1960, 860, f, expr='curioso' if f < ni else 'preocupado', look=-.8, flip=True, seed=7, **VIZ2)
    t = smooth(ramp(f, 0, fim))
    cam = (lerp(560, 680, t), 1350, lerp(1.0, 1.1, t) * (1 + .0012 * f) + .05 * kick(f, ni, .6), 0); CAM[6] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['UM BOLINHO DE', '100 ANOS'], 170, 1, 104)
            stamp(im, 'PARTE 1', 880, 1240, 1, 46)
        else:
            stamp(im, 'NA FLORESTA', 540, 200, back(ramp(f, CAPA + 2, CAPA + 10)), 72)
    elif si == 1:
        an = wt(1, 'aniversario') - 3; no = wt(1, 'nome') - 3
        if f < no: stamp(im, 'ANIVERSÁRIO', 540, 230, back(ramp(f, an, an + 8)), 80)
        else: card(im, 'Com o nome', 'da pessoa', 540, 230, ramp(f, no, no + 10))
    elif si == 2:
        r = wt(2, 'regra') - 3; tr = wt(2, 'trancada') - 3
        stamp(im, 'A REGRA', 540, 200, back(ramp(f, r, r + 8)), 100, big=True)
        if f < tr: card(im, 'Ninguém abre', 'a portinha', 540, 420, ramp(f, r + 10, r + 20))
        else: burst(im, 'TRANCADA', 760, 440, back(ramp(f, tr, tr + 8)), 56)
    elif si == 3:
        ni = wt(3, 'ninguem') - 3; es = wt(3, 'esqueceu') - 3
        if f < es: interrog(im, 540, 260, f, ramp(f, ni, ni + 8))
        else: painel(im, 'ESQUECEU', '0 VEZES', 540, 270, ramp(f, es, es + 10), w=420)
    elif si == 4:
        an = wt(4, 'aniversario') - 3; ch = wt(4, 'chocolate') - 3
        if f < ch: stamp(im, 'MEU ANIVERSÁRIO', 540, 230, back(ramp(f, an, an + 8)), 70)
        else: card(im, 'De chocolate', 'do jeitinho que eu gosto', 540, 240, ramp(f, ch, ch + 10))
    elif si == 5:
        ho = wt(5, 'hoje') - 3; ve = wt(5, 'vela') - 3; ce = wt(5, 'cem') - 3
        if f < ve: painel(im, 'HOJE', '06:30', 540, 260, ramp(f, ho, ho + 10), w=360)
        elif f < ce + 8: burst(im, '100?!', 540, 280, back(ramp(f, ve, ve + 8)), 90)
        else: stamp(im, 'VELA DE 100', 540, 250, back(ramp(f, ce + 8, ce + 16)), 80)
    elif si == 6:
        ci = wt(6, 'cidade') - 3; ho = wt(6, 'hoje') - 3
        if f < ho + 2: card(im, 'Quem faz', '100 anos hoje?', 540, 230, ramp(f, ci, ci + 10))
        else: stamp(im, 'NINGUÉM', 540, 250, back(ramp(f, ho + 4, ho + 12)), 90, rot=3)
    return grao(im.convert('RGB'), lf)
