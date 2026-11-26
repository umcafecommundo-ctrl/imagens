"""Formato MISTÉRIO: "A estação Girassol", PARTE 2 (26/11/2026, 21h). História inventada.
Narradora: menina de cabelo longo preto, pele morena, blusa rosa e calça azul (as mesmas cores da parte 1).
Premissa: ela desce na estação Girassol e o homem que acenava diz "finalmente alguém desceu"; tem a cara do seu Jonas, mas é
o Elias, irmão gêmeo dele; há 40 anos os dois desceram juntos e o Elias quis ficar cuidando dos girassóis; o Jonas ficou
bravo, voltou sozinho e inventou a regra "ninguém desce na Girassol"; o Elias dá a ela um girassol: "leva pro meu irmão,
fala que eu ainda espero o trem das cinco"; lá em cima ela entrega a flor e o seu Jonas fica calado olhando pra ela;
fim: hoje às 17h o trem parou na Girassol e quem desceu primeiro foi o seu Jonas.
Cenários/cores: s0 CAPA close (estação Girassol, vivo) -> estação com o Elias acenando (vivo) | s1 Elias de perto + CLOSE
choque (vivo) | s2 lembrança: os dois jovens na estação (tarde) | s3 vagão de tarde com o Jonas jovem bravo (tarde) |
s4 estação, Elias dá o girassol (vivo) | s5 rua de tarde com a banca + CLOSE do seu Jonas (tarde) | s6 vagão com a porta
aberta, o Jonas desce + CLOSE final sorriso (vivo)."""
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
ELIAS = dict(penteado='careca', velho=True, barba=True, cabelo='#e6e6e6', pele='#c98f65', roupa='#5a8f4a', calca='#6b4a2e')
JONAS_J = dict(penteado='curto', cabelo='#2b1d14', pele='#c98f65', roupa='#c8553d', calca='#3a3a40')
ELIAS_J = dict(penteado='curto', cabelo='#2b1d14', pele='#c98f65', roupa='#5a8f4a', calca='#6b4a2e')

LINES = [
    "Eu desci na estação Girassol. E o homem que acenava sorriu: finalmente alguém desceu!",
    "Ele tinha a cara do seu Jonas, a mesma barba branca. Mas o nome dele era Elias. O irmão gêmeo.",
    "Quarenta anos atrás, os dois desceram juntos. E o Elias quis ficar, cuidando dos girassóis.",
    "O Jonas ficou bravo, voltou sozinho... e inventou a regra: ninguém desce na Girassol.",
    "O Elias me deu um girassol. Leva pro meu irmão. Fala que eu ainda espero o trem das cinco.",
    "Lá em cima, eu entreguei a flor. O seu Jonas ficou muito tempo calado, olhando pra ela.",
    "Hoje, às cinco, o trem parou na Girassol. E quem desceu primeiro... foi o seu Jonas.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "VOCÊ DESCERIA?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 1
FLASH = []
CHECK = [(0, 'desci', 6), (0, 'finalmente', 6), (1, 'jonas', 6), (1, 'elias', 6), (1, 'gemeo', 10), (2, 'quarenta', 6),
         (2, 'girassois', 6), (3, 'bravo', 6), (3, 'regra', 6), (4, 'girassol', 6), (4, 'irmao', 6), (4, 'cinco', 6),
         (5, 'flor', 6), (5, 'calado', 8), (6, 'parou', 6), (6, 'jonas', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    s.ting(s.W(0, 'finalmente'), .35)
    s.ting(s.W(1, 'elias'), .3); s.thunk(s.W(1, 'gemeo') - 2, 90, .8)
    s.whoosh(s.W(2, 'quarenta') - 3, .6, .2)
    s.thunk(s.W(3, 'bravo') - 2, 70, .5); s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.ting(s.W(4, 'girassol'), .35); s.ting(s.W(4, 'cinco'), .3)
    s.ting(s.W(5, 'flor'), .3)
    s.thunk(s.W(6, 'parou') - 2, 80, .6); s.ting(s.W(6, 'jonas') + 2, .5)


def eu(c, x, f, feet=1960, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def pessoa(c, x, f, d, feet=2000, h=960, seed=5, **kw):
    put_menino(c, x, feet, h, f, seed=seed, **dict(d, **kw))


def rz(f):
    return 1 + .0012 * f


def flor(c, x, y, h=300, s=1.0):
    if s <= .02: return
    g = girassol_img(max(10, int(h * s))); c.alpha_composite(g, (int(x - g.width / 2), int(y - g.height)))


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
        c = estacao_girassol_bg('dia').copy()
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * rz(f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    c = estacao_girassol_bg('dia').copy()
    eu(c, 320, f, expr='curioso', look=.8)
    pessoa(c, 900, f, ELIAS, feet=2000 - 18 * abs(math.sin(f * .25)), expr='sorriso', look=-.6)
    fi = wt(0, 'finalmente') - 3
    t = smooth(ramp(f, CAPA, fi))
    cam = (lerp(520, 640, t), lerp(1350, 1400, t), lerp(1.25, 1.1, easeOut(ramp(f, CAPA, CAPA + 14))) * rz(f) + .05 * kick(f, fi, .6), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    ge = wt(1, 'gemeo') - 3; el = wt(1, 'elias') - 3
    c = estacao_girassol_bg('dia').copy()
    if f >= ge:   # CLOSE choque
        c = put_close(c, f, expr='choque', look=.3, shake=.2, **EU)
        cam = (621, 1104, lerp(1.3, 1.06, easeOut(ramp(f, ge, ge + 10))) * rz(f - ge), 0); CAM[1] = cam
        return c, cam, 'vivo'
    pessoa(c, 621, f, ELIAS, expr='sorriso' if f < el else 'neutro', look=0)
    cam = (621, lerp(1300, 1180, smooth(ramp(f, 0, ge))), lerp(1.3, 1.7, smooth(ramp(f, 0, ge))) * rz(f) + .05 * kick(f, el, .6), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = estacao_girassol_bg('tarde').copy()
    gi = wt(2, 'girassois') - 3; fi = wt(2, 'ficar') - 3
    x2 = lerp(780, 860, ramp(f, fi, fi + 10)) if f >= fi else 780
    pessoa(c, 440, f, JONAS_J, seed=4, expr='sorriso' if f < fi else 'preocupado', look=.6)
    pessoa(c, x2, f, ELIAS_J, seed=6, expr='sorriso', look=-.4 if f < fi else .5)
    if f >= gi: flor(c, x2 + 150, 2000, 420, back(ramp(f, gi, gi + 8)))
    cam = (lerp(600, 650, ramp(f, 0, gi)), 1400, lerp(1.0, 1.15, smooth(ramp(f, 0, gi))) * rz(f), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    c = vagao_bg('tarde', 'tunel', 0).copy()
    re = wt(3, 'regra') - 3; br = wt(3, 'bravo') - 3
    pessoa(c, 621, f, JONAS_J, seed=4, expr='desconfiado' if f < re else 'preocupado', look=-.5)
    cam = (621, 1350, lerp(1.2, 1.5, smooth(ramp(f, 0, re))) * rz(f) + .06 * kick(f, br, .6) + .06 * kick(f, re, .6), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = estacao_girassol_bg('dia').copy()
    gi = wt(4, 'girassol') - 3; ir = wt(4, 'irmao') - 3
    eu(c, 360, f, expr='curioso' if f < ir else 'sorriso', look=.8)
    pessoa(c, 880, f, ELIAS, expr='sorriso', look=-.6)
    t = smooth(ramp(f, gi, gi + 16))
    if f >= gi: flor(c, lerp(760, 500, t), lerp(1700, 1720, t), 380, back(ramp(f, gi, gi + 6)))
    cam = (lerp(640, 600, t), 1400, lerp(1.1, 1.2, smooth(ramp(f, 0, ir))) * rz(f) + .05 * kick(f, gi, .6), 0); CAM[4] = cam
    return c, cam, 'vivo'


def s5(f):
    ca = wt(5, 'calado') - 3; fl = wt(5, 'flor') - 3
    c = rua_banca('tarde').copy()
    if f >= ca:   # CLOSE do seu Jonas
        c = put_close(c, f, expr='preocupado', look=0, seed=5, **JONAS)
        flor(c, 621, 2208, 520, 1)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, ca, ca + 10))) * rz(f - ca), 0); CAM[5] = cam
        return c, cam, 'tarde'
    eu(c, 480, f, expr='sorriso', look=.7)
    pessoa(c, 820, f, JONAS, expr='neutro' if f < fl else 'curioso', look=-.6)
    flor(c, lerp(600, 680, ramp(f, fl, fl + 12)), 1900, 320)
    cam = (680, 1420, lerp(1.15, 1.35, smooth(ramp(f, 0, ca))) * rz(f) + .05 * kick(f, fl, .6), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    pa = wt(6, 'parou') - 3; jo = wt(6, 'jonas') - 3
    fim = jo + 14
    if f >= fim:
        c = estacao_girassol_bg('dia').copy()
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, fim, fim + 10))) * rz(f - fim), 0); CAM[6] = cam
        return c, cam, 'vivo'
    ab = pa + 8
    c = vagao_bg('tarde', 'girassol' if f >= pa else 'tunel', round(easeOut(ramp(f, ab, ab + 12)) * 8) / 8 if f >= ab else 0).copy()
    if f < jo:
        pessoa(c, 621, f, JONAS, feet=1990, h=940, expr='neutro', look=0, flip=True)
    else:   # desce: vai encolhendo pra dentro da estação
        t = easeOut(ramp(f, jo, jo + 12))
        pessoa(c, 621, f, JONAS, feet=lerp(1990, 1555, t), h=lerp(940, 760, t), expr='sorriso', look=0, walk=1)
    eu(c, 260, f, expr='curioso' if f < jo else 'sorriso', look=.7)
    sh = 6 * math.sin(f * 2.1) * (1 - ramp(f, pa, pa + 10)) if f >= pa else 0
    cam = (540 + sh, 1300, lerp(1.1, 1.2, smooth(ramp(f, 0, jo))) * rz(f) + .07 * kick(f, pa, .7), 0); CAM[6] = cam
    return c, cam, 'tarde' if f < jo else 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['EU DESCI NA', 'ESTAÇÃO PROIBIDA'], 170, 1, 100)
        else:
            if 45 <= f < 90: stamp(im, 'PARTE 2', 880, 110, back(ramp(f, 45, 52)), 46)
            fi = wt(0, 'finalmente') - 3
            if f >= fi: burst(im, 'FINALMENTE!', 540, 330, back(ramp(f, fi, fi + 8)), 60, cor=(240, 190, 60))
    elif si == 1:
        jo = wt(1, 'jonas') - 3; el = wt(1, 'elias') - 3; ge = wt(1, 'gemeo') - 3
        if f < el: interrog(im, 540, 260, f, ramp(f, jo, jo + 8))
        elif f < ge: card(im, 'Elias', 'não é o Jonas', 540, 250, ramp(f, el, el + 10))
        else: stamp(im, 'IRMÃO GÊMEO', 540, 250, back(ramp(f, ge, ge + 8)), 90, big=True)
    elif si == 2:
        qu = wt(2, 'quarenta') - 3; fi = wt(2, 'ficar') - 3
        if f < fi: painel(im, 'LEMBRANÇA: HÁ', '40 ANOS', 540, 260, ramp(f, qu, qu + 10), w=440)
        else: card(im, 'Elias ficou', 'cuidando dos girassóis', 540, 260, ramp(f, fi, fi + 10))
    elif si == 3:
        br = wt(3, 'bravo') - 3; re = wt(3, 'regra') - 3
        if f < re: burst(im, 'HUNF!', 540, 280, back(ramp(f, br, br + 6)), 80) if f >= br else None
        else:
            stamp(im, 'A REGRA', 540, 230, back(ramp(f, re, re + 8)), 100, big=True)
            card(im, 'Foi o Jonas', 'que inventou', 540, 450, ramp(f, re + 4, re + 14))
    elif si == 4:
        ir = wt(4, 'irmao') - 3; ci = wt(4, 'cinco') - 3
        if f < ci: card(im, '"Leva pro', 'meu irmão"', 540, 250, ramp(f, ir, ir + 10))
        else: painel(im, 'EU ESPERO O TREM DAS', '17:00', 540, 270, ramp(f, ci, ci + 10), w=480)
    elif si == 5:
        fl = wt(5, 'flor') - 3; ca = wt(5, 'calado') - 3
        if f < ca: stamp(im, 'LÁ EM CIMA', 540, 230, back(ramp(f, 4, 12)), 76)
        else: burst(im, '...', 540, 280, back(ramp(f, ca, ca + 6)), 90, cor=(150, 160, 175))
    elif si == 6:
        pa = wt(6, 'parou') - 3; jo = wt(6, 'jonas') - 3; fim = jo + 14
        if f < jo: painel(im, 'HOJE', '17:00', 540, 260, ramp(f, 4, 14), w=360)
        elif f < fim: stamp(im, 'ELE DESCEU', 540, 260, back(ramp(f, jo, jo + 8)), 90, big=True)
        else: stamp(im, 'ENFIM JUNTOS', 540, 250, back(ramp(f, fim + 2, fim + 10)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
