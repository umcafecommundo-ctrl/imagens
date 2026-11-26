"""Formato MISTÉRIO: "A lousa da sala quatro", PARTE 2 (26/11/2026, 12h). História inventada.
Narrador: Caio (cabelo curto castanho escuro, blusa amarela, calça azul, as mesmas cores da parte 1). Pai: barba, blusa azul.
Premissa: depois da aula ele cola o rosto no vidro da sala 4 e o giz levanta sozinho; desenha uma forca e quatro risquinhos:
"você é o próximo" era a vez dele de jogar a forca; ele passa a letra A por baixo da porta e o giz escreve duas; a palavra é
TATÁ, o apelido do pai dele quando criança; em casa o pai fica quieto e busca uma caixa velha; dentro, o caderno da escola de
30 anos atrás, cheio de jogos da forca e o nome CAIO em todos; virada: o pai estudou na sala 4 e quem jogava com ele do outro
lado da lousa era o Caio; o pai sempre jogou com um tal de Caio, por isso deu esse nome ao filho.
Cenários/cores: s0 CAPA close (corredor de tarde) -> corredor de tarde, rosto no vidro -> lousa com o giz voando (tarde) |
s1 lousa com a forca e os risquinhos + CLOSE curioso (tarde) | s2 pé da porta com o papel -> lousa com _A_A (tarde) |
s3 lousa TATA (tarde) | s4 sala de casa no fim de tarde, pai e caixa (tarde) | s5 caderno velho em close (tarde) |
s6 lembrança: sala de aula antiga com o pai menino na lousa (tarde) | s7 sala de casa, pai e filho + CLOSE final sorriso (vivo)."""
from kit import *
import kit
from sombrio import *
from sala4 import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'; PITCH = '-4Hz'
EU = dict(penteado='curto', cabelo='#3a2416', pele='#e0b48c', roupa='#e8b730', calca='#2e4a7a')
PAI = dict(penteado='curto', cabelo='#3a2416', pele='#e0b48c', roupa='#4a7a9a', calca='#3a3a40', barba=True)
PAI_MENINO = dict(penteado='curto', cabelo='#3a2416', pele='#e0b48c', roupa='#f2f2ee', calca='#2e4a7a')

LINES = [
    "Depois da aula, eu colei o rosto no vidro da sala quatro. E o giz levantou sozinho.",
    "Ele desenhou uma forca e quatro risquinhos. Você é o próximo... era a minha vez de jogar.",
    "Eu passei a letra A num papel, por baixo da porta. E o giz escreveu duas.",
    "Letra por letra, apareceu a palavra: Tatá. O apelido do meu pai, quando ele era criança.",
    "Em casa, eu mostrei pro meu pai. Ele ficou quieto e buscou uma caixa velha.",
    "Dentro, um caderno da escola, de trinta anos atrás. Cheio de jogos da forca... e o meu nome em todos.",
    "O meu pai estudou na sala quatro. E quem jogava com ele, do outro lado da lousa... era eu.",
    "Ele sempre jogou com um tal de Caio. Por isso ele me deu esse nome.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "VOCÊ JOGARIA?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'vidro', 6), (0, 'giz', 6), (0, 'sozinho', 6), (1, 'forca', 6), (1, 'risquinhos', 6), (1, 'jogar', 8),
         (2, 'porta', 6), (2, 'duas', 6), (3, 'tata', 8), (3, 'pai', 6), (4, 'casa', 6), (4, 'caixa', 6),
         (5, 'caderno', 6), (5, 'nome', 8), (6, 'sala', 6), (6, 'eu', 10), (7, 'caio', 6), (7, 'nome', 10)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    s.ting(s.W(0, 'giz'), .3); s.whoosh(s.W(0, 'levantou') - 2, .5, .25)
    s.thunk(s.W(1, 'forca') - 2, 70, .5); s.ting(s.W(1, 'vez'), .3)
    s.whoosh(s.W(2, 'porta') - 4, .5, .25); s.ting(s.W(2, 'duas'), .35)
    s.thunk(s.W(3, 'tata') - 2, 90, .7)
    s.thunk(s.W(4, 'caixa'), 60, .5)
    s.ting(s.W(5, 'caderno'), .3); s.thunk(s.W(5, 'nome') + 2, 70, .7)
    s.whoosh(s.W(6, 'sala') - 3, .6, .2); s.thunk(s.W(6, 'eu') + 2, 60, .9)
    s.ting(s.W(7, 'nome'), .4)


def eu(c, x, f, feet=1960, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def rz(f):
    return 1 + .0012 * f


def giz_voa(c, f, f0, x0=850, y0=1450, x1=560, y1=900):
    t = smooth(ramp(f, f0, f0 + 18))
    x = lerp(x0, x1, t) + 20 * math.sin(f * .3); y = lerp(y0, y1, t) + 15 * math.sin(f * .21)
    put_giz(c, x, y, 25 + 15 * math.sin(f * .17))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = corredor_bg('tarde').copy()
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * rz(f), 0); CAM[0] = cam
        return c, cam, 'tarde'
    gz = wt(0, 'giz') - 3
    if f < gz:
        c = corredor_bg('tarde').copy()
        eu(c, 760, f, expr='curioso', look=.3, feet=1990, h=1000)
        t = easeOut(ramp(f, CAPA, CAPA + 14))
        cam = (lerp(700, 800, t), lerp(1250, 1150, t), lerp(1.2, 1.6, smooth(ramp(f, CAPA, gz))) * rz(f), 0); CAM[0] = cam
        return c, cam, 'tarde'
    c = lousa_bg((), 'tarde').copy()
    lv = wt(0, 'levantou') - 3
    if f < lv: put_giz(c, 400, 1640, 0)
    else: giz_voa(c, f, lv, 400, 1640, 640, 1000)
    cam = (621, 1150, lerp(1.35, 1.15, easeOut(ramp(f, gz, gz + 10))) * rz(f) + .06 * kick(f, lv, .6), 0); CAM[0] = cam
    return c, cam, 'tarde'


def s1(f):
    fo = wt(1, 'forca') - 3; ri = wt(1, 'risquinhos') - 3; ve = wt(1, 'vez') - 3
    if f >= ve:
        c = lousa_bg((), 'tarde', 2).copy(); put_risquinhos(c, 4)
        c = put_close(c, f, expr='curioso', look=.4, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, ve, ve + 10))) * rz(f - ve), 0); CAM[1] = cam
        return c, cam, 'tarde'
    c = lousa_bg((), 'tarde', 2 if f >= fo else 0).copy()
    if f >= ri: put_risquinhos(c, 4, s=ramp(f, ri, ri + 6))
    if f < fo: giz_voa(c, f, 0, 640, 1000, 320, 760)
    elif f < ri: put_giz(c, 430 + 10 * math.sin(f * .3), 820, 30)
    else: put_giz(c, 960, 1380 + 10 * math.sin(f * .3), 30)
    cam = (621, lerp(1000, 1200, smooth(ramp(f, 0, ve))), 1.12 * rz(f) + .06 * kick(f, fo, .6) + .05 * kick(f, ri, .6), 0); CAM[1] = cam
    return c, cam, 'tarde'


def s2(f):
    du = wt(2, 'duas') - 3
    if f < du:
        c = corredor_bg('tarde').copy()
        eu(c, 470, f, expr='curioso', look=.8)
        po = wt(2, 'porta') - 3
        t = smooth(ramp(f, po - 6, po + 10))
        x = lerp(560, 780, t); pi = papel_img(200)
        if x < 690: c.alpha_composite(pi, (int(x - 100), 1530))
        else:
            w = max(1, int(pi.width - (x - 690))); c.alpha_composite(pi.crop((0, 0, w, pi.height)), (int(x - 100), 1530))
        cam = (lerp(560, 640, t), 1480, lerp(1.5, 1.8, smooth(ramp(f, 0, du))) * rz(f), 0); CAM[2] = cam
        return c, cam, 'tarde'
    c = lousa_bg((), 'tarde', 2).copy(); put_risquinhos(c, 4); put_letras(c, '_A_A', s=ramp(f, du, du + 5))
    put_giz(c, 960, 1300 + 10 * math.sin(f * .3), 30)
    cam = (621, 1250, 1.2 * rz(f) + .07 * kick(f, du, .7), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    ta = wt(3, 'tata') - 3; le = wt(3, 'letra') - 3
    c = lousa_bg((), 'tarde', 2).copy(); put_risquinhos(c, 4)
    k = int(ramp(f, 0, ta) * 2.99)
    estado = 'TATA' if f >= ta else ['_A_A', 'TA_A', 'TATA'][k]
    put_letras(c, estado)
    cam = (621, lerp(1250, 1200, ramp(f, 0, ta)), (1.2 if f < ta else 1.45) * rz(f) + .08 * kick(f, ta, .8), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = CEN('sala', 'golden').copy()
    qu = wt(4, 'quieto') - 3; cx = wt(4, 'caixa') - 3
    if f >= cx: c.alpha_composite(caixa_img(300), (470, int(lerp(2208, 1760, back(ramp(f, cx, cx + 8))))))
    eu(c, 300, f, expr='sorriso' if f < qu else 'curioso', look=.7)
    put_menino(c, 900, 2050, 1200, f, expr='curioso' if f < qu else 'preocupado', look=-.6, seed=4, **PAI)
    cam = (lerp(560, 640, smooth(ramp(f, 0, cx))), 1350, lerp(1.05, 1.18, smooth(ramp(f, 0, cx))) * rz(f) + .05 * kick(f, qu, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = caderno_bg('tarde').copy()
    no = wt(5, 'nome') - 3; fo = wt(5, 'forca') - 3
    if f < fo:
        cam = (621, 1150, lerp(1.0, 1.2, smooth(ramp(f, 0, fo))) * rz(f), 0)
    elif f < no:
        cam = (400, 900, 1.6 * rz(f) + .05 * kick(f, fo, .6), 0)
    else:
        cam = (lerp(400, 560, easeOut(ramp(f, no, no + 10))), 820, lerp(1.6, 2.3, easeOut(ramp(f, no, no + 10))) * rz(f) + .08 * kick(f, no, .8), 0)
    CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    e = wt(6, 'eu') - 3; lo = wt(6, 'lousa') - 3
    if f >= e:   # CLOSE choque: era eu
        c = CEN('escola', 'golden').copy()
        c = put_close(c, f, expr='choque', look=0, shake=.25, **EU)
        cam = (621, 1104, lerp(1.3, 1.06, easeOut(ramp(f, e, e + 10))) * rz(f - e), 0); CAM[6] = cam
        return c, cam, 'tarde'
    c = CEN('escola', 'golden').copy()
    put_menino(c, 620, 1980, 860, f, expr='sorriso' if f < lo else 'curioso', look=-.5, seed=7, **PAI_MENINO)
    put_giz(c, 500, 1560 + 10 * math.sin(f * .2), 20)
    cam = (lerp(560, 621, smooth(ramp(f, 0, e))), lerp(1350, 1550, smooth(ramp(f, 0, e))), lerp(1.3, 1.55, smooth(ramp(f, 0, e))) * rz(f) + .05 * kick(f, lo, .6), 0); CAM[6] = cam
    return c, cam, 'tarde'


def s7(f):
    no = wt(7, 'nome') - 3; ca = wt(7, 'caio') - 3
    c = CEN('sala', 'day').copy()
    if f >= no:   # CLOSE final sorriso
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, no, no + 10))) * rz(f - no), 0); CAM[7] = cam
        return c, cam, 'vivo'
    eu(c, 380, f, expr='curioso', look=.7)
    put_menino(c, 860, 2050, 1200, f, expr='sorriso', look=-.6, seed=4, **PAI)
    cam = (lerp(560, 700, smooth(ramp(f, 0, no))), 1350, 1.1 * rz(f) + .05 * kick(f, ca, .6), 0); CAM[7] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['O GIZ ESCREVEU', 'SOZINHO'], 170, 1, 104)
        else:
            if 45 <= f < 90: stamp(im, 'PARTE 2', 880, 110, back(ramp(f, 45, 52)), 46)
            so = wt(0, 'sozinho') - 3
            if f >= so: burst(im, 'TEC TEC', 540, 300, back(ramp(f, so, so + 8)), 64, cor=(230, 230, 220))
    elif si == 1:
        fo = wt(1, 'forca') - 3; ve = wt(1, 'vez') - 3
        if f < ve: stamp(im, 'JOGO DA FORCA', 540, 230, back(ramp(f, fo, fo + 8)), 76) if f >= fo else None
        else: stamp(im, 'MINHA VEZ', 540, 250, back(ramp(f, ve, ve + 8)), 84)
    elif si == 2:
        le = wt(2, 'letra') - 3; du = wt(2, 'duas') - 3
        if f < du: card(im, 'Letra A', 'por baixo da porta', 540, 260, ramp(f, le, le + 10))
        else: burst(im, 'DUAS!', 540, 280, back(ramp(f, du, du + 6)), 80, cor=(230, 190, 80))
    elif si == 3:
        ta = wt(3, 'tata') - 3; pa = wt(3, 'pai') - 3
        if f < pa: interrog(im, 540, 260, f, ramp(f, 4, 12)) if f < ta else stamp(im, 'TATÁ', 540, 250, back(ramp(f, ta, ta + 8)), 110, big=True)
        else: card(im, 'Tatá', 'o apelido do meu pai', 540, 250, ramp(f, pa, pa + 10))
    elif si == 4:
        qu = wt(4, 'quieto') - 3; cx = wt(4, 'caixa') - 3
        if f < cx: stamp(im, 'EM CASA', 540, 230, back(ramp(f, 4, 12)), 76)
        else: card(im, 'Uma caixa velha', '', 540, 240, ramp(f, cx, cx + 10))
    elif si == 5:
        tr = wt(5, 'trinta') - 3; no = wt(5, 'nome') - 3
        if f < no: painel(im, 'CADERNO DE', '1996', 540, 260, ramp(f, tr, tr + 10), w=420)
        else: burst(im, 'O MEU NOME?!', 540, 250, back(ramp(f, no, no + 6)), 64)
    elif si == 6:
        sa = wt(6, 'sala') - 3; e = wt(6, 'eu') - 3
        if f < e: card(im, 'Sala 4, 30 anos atrás', 'o meu pai, com 9 anos', 540, 240, ramp(f, sa, sa + 10))
        else: stamp(im, 'ERA EU', 540, 260, back(ramp(f, e, e + 8)), 96, big=True)
    elif si == 7:
        ca = wt(7, 'caio') - 3; no = wt(7, 'nome') - 3
        if f < no: card(im, 'Um tal de Caio', '', 540, 240, ramp(f, ca, ca + 10))
        else: stamp(im, 'POR ISSO EU SOU CAIO', 540, 260, back(ramp(f, no + 4, no + 12)), 64, rot=3)
    return grao(im.convert('RGB'), lf)
