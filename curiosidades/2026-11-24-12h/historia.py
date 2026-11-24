"""Formato MISTÉRIO: "A estátua de mão aberta", PARTE 2 (24/11/2026, 12h). História inventada.
Narrador: o mesmo da parte 1 (menino de cabelo curto preto, pele morena, camiseta coral e calça azul).
Resolução: naquela noite o guarda deixa o narrador ficar no museu; à meia-noite a estátua abre os olhos e desce do pedestal;
ela sai pela janela e volta com um guarda-chuva perdido; virada: ela não pega nada, toda noite sai pra achar o que a cidade
perdeu; o bolso do narrador tinha um furo, o chaveiro caiu na rua e ela achou; fim: agora, quando alguém perde algo na
cidade, ele sabe onde procurar.
Cenários/cores: s0 CAPA close (museu à noite) -> museu de manhã fria com o chaveiro (frio) | s1 museu à noite, lanterna (sombrio_noite) |
s2 meia-noite, olhos abertos + CLOSE choque, estátua no chão (sombrio_noite) | s3 rua à noite, a estátua andando (sombrio_noite) |
s4 museu à noite, achados (sombrio_noite) | s5 museu, o furo no bolso + CLOSE (sombrio_noite) | s6 museu de dia + CLOSE final sorrindo (vivo)."""
from kit import *
import kit
from sombrio import *
from museu_estatua import *
from chuva27 import guarda_chuva
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#2b1d14', pele='#8a5a3a', roupa='#e8655a', calca='#2f4a6a')
GUARDA = dict(penteado='coque', cabelo='#3a2a22', pele='#e6c8ad', roupa='#3d5a80', calca='#2d2f32')
EX, EP = 630, 1120
EH = 640
MX, MY = mao_estatua(EX, EP, EH)

LINES = [
    "Na parte um, a estátua do museu amanheceu com o meu chaveiro na mão. E ninguém tinha entrado lá.",
    "Naquela noite, o guarda deixou eu ficar no museu com ele, de lanterna na mão.",
    "À meia-noite em ponto, a estátua abriu os olhos. E desceu do pedestal.",
    "Ela pulou a janela, foi pra rua... e voltou com um guarda-chuva perdido.",
    "Aí eu entendi. Ela não pega nada. Toda noite, ela sai pra achar o que a cidade perdeu.",
    "Eu olhei o meu bolso. Tinha um furo. O meu chaveiro caiu na rua, e ela achou.",
    "Agora, quando alguém perde alguma coisa na minha cidade, eu já sei onde procurar.",
]
FALA_TIKTOK = "Você ficaria no museu à noite? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 4
FLASH = []
CHECK = [(0, 'chaveiro', 6), (1, 'lanterna', 6), (2, 'olhos', 6), (2, 'desceu', 6), (3, 'rua', 6), (3, 'perdido', 6),
         (4, 'entendi', 6), (4, 'perdeu', 8), (5, 'furo', 6), (5, 'achou', 8), (6, 'procurar', 10)]
CAM = {}
CAPA = 36
STONE = dict(PEDRA)


def SFX(s):
    s.thunk(2, 60, .6)
    s.ting(s.W(0, 'chaveiro'), .3)
    s.thunk(s.W(1, 'lanterna') - 2, 50, .4)
    s.ting(s.W(2, 'meia-noite'), .3); s.thunk(s.W(2, 'olhos') - 2, 120, .9); s.thunk(s.W(2, 'desceu'), 60, .7)
    s.whoosh(s.W(3, 'pulou') - 3, .7, .3); s.thunk(s.W(3, 'perdido'), 60, .5)
    s.ting(s.W(4, 'perdeu'), .35)
    s.thunk(s.W(5, 'furo') - 2, 80, .6); s.ting(s.W(5, 'achou'), .35)
    s.ting(s.W(6, 'procurar'), .3)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def pedra_viva(c, x, feet, h, f, **kw):
    put_menino(c, x, feet, h, f, seed=7, **dict(STONE, **kw))


def lanterna(c, x0, y0, x1, y1, w=170, a=70):
    g = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    ang = math.atan2(y1 - y0, x1 - x0); nx, ny = -math.sin(ang), math.cos(ang)
    d.polygon([(x0, y0), (x1 + nx * w, y1 + ny * w), (x1 - nx * w, y1 - ny * w)], fill=(255, 236, 160, a))
    d.ellipse((x1 - w, y1 - w, x1 + w, y1 + w), fill=(255, 236, 160, a))
    c.alpha_composite(g)


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA
        c = museu_bg('frio').copy(); put_estatua(c, EX, EP, EH, f, None, olho=True)
        c = put_close(c, f, expr='medo', look=0, shake=.25, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'frio'
    g = f - CAPA
    c = museu_bg('frio').copy()
    put_estatua(c, EX, EP, EH, f, 'chaveiro')
    t = smooth(ramp(g, 0, 120))
    ch = wt(0, 'chaveiro') - 3
    cam = (lerp(621, MX - 120, t), lerp(1150, 1000, t), lerp(1.25, 1.35, t) * (1 + .0009 * f) + .05 * kick(f, ch, .6), 0); CAM[0] = cam
    return c, cam, 'frio'


def s1(f):
    c = museu_bg('noite').copy()
    put_estatua(c, EX, EP, EH, f, None)
    eu(c, 230, f, expr='preocupado', look=.75)
    put_menino(c, 1010, 1900, 900, f, expr='neutro', look=-.75, flip=True, seed=5, **GUARDA)
    la = wt(1, 'lanterna') - 3
    if f >= la:
        sw = math.sin(f * .05) * 60
        lanterna(c, 900, 1530, EX + sw, 820, 150, int(70 * ramp(f, la, la + 6)))
    t = smooth(ramp(f, 0, 150))
    cam = (621, lerp(1200, 1120, t), lerp(1.15, 1.02, t) * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'sombrio_noite'


def s2(f):
    c = museu_bg('noite').copy()
    ol = wt(2, 'olhos') - 3; de = wt(2, 'desceu') - 3
    if f < de:
        put_estatua(c, EX, EP, EH, f, None, olho=f >= ol)
        lanterna(c, 900, 1530, EX, 820, 150, 60)
        if ol + 4 <= f < de - 2:   # CLOSE choque
            c = put_close(c, f, expr='choque', look=-.25, shake=.4, escurece=.25, **EU)
            cam = (621, 1104, lerp(1.25, 1.06, easeOut(ramp(f, ol + 4, ol + 12))) * (1 + .0009 * f), 0); CAM[2] = cam
            return c, cam, 'sombrio_noite'
        t = smooth(ramp(f, 0, ol))
        cam = (621, lerp(1100, 800, t), lerp(1.0, 1.9, t) * (1 + .0009 * f) + .08 * kick(f, ol, .6), 0); CAM[2] = cam
        return c, cam, 'sombrio_noite'
    # estátua no chão, pedestal vazio
    pedra_viva(c, 820, 1900, 760, f, expr='neutro', look=-.5, flip=True)
    eu(c, 230, f, expr='choque', look=.75)
    cam = (621, 1150, lerp(1.1, 1.0, easeOut(ramp(f, de, de + 12))) * (1 + .0009 * f) + .06 * kick(f, de, .6), 0); CAM[2] = cam
    return c, cam, 'sombrio_noite'


def s3(f):
    ru = wt(3, 'rua') - 3; pe = wt(3, 'perdido') - 3
    c = rua(f, scroll=f * 9, luz='noite', neb=.4)
    pedra_viva(c, 620, 1900, 820, f, walk=1, expr='neutro', look=.5)
    if f >= pe - 8:
        guarda_chuva(c, 860, 1900, back(ramp(f, pe - 8, pe)) * 1.4)
    cam = (621, lerp(1180, 1120, smooth(ramp(f, 0, 140))), lerp(1.12, 1.02, smooth(ramp(f, 0, 140))) * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'sombrio_noite'


def s4(f):
    c = museu_bg('noite').copy()
    pedra_viva(c, 860, 1900, 760, f, expr='sorriso' if f >= wt(4, 'perdeu') - 3 else 'neutro', look=-.75, flip=True)
    guarda_chuva(c, 1100, 1900, 1.2)
    eu(c, 260, f, expr='preocupado' if f < wt(4, 'entendi') - 3 else 'neutro', look=.75)
    lanterna(c, 900, 1530, 860, 1200, 120, 40)
    en = wt(4, 'entendi') - 3
    t = smooth(ramp(f, 0, 170))
    cam = (lerp(560, 640, t), 1150, lerp(1.05, 1.15, t) * (1 + .0009 * f) + .04 * kick(f, en, .6), 0); CAM[4] = cam
    return c, cam, 'sombrio_noite'


def s5(f):
    c = museu_bg('noite').copy()
    ac = wt(5, 'achou') - 3
    if f >= ac:   # CLOSE choque/alívio
        c = put_close(c, f, expr='choque', look=.5, **EU)
        cam = (621, 1104, lerp(1.2, 1.05, easeOut(ramp(f, ac, ac + 10))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'sombrio_noite'
    eu(c, 560, f, expr='preocupado' if f >= wt(5, 'furo') - 3 else 'neutro', look=.25)
    fu = wt(5, 'furo') - 3
    t = smooth(ramp(f, 0, fu + 6))
    hx, hy = mao_dir(560, 1900, 900)
    cam = (lerp(621, hx, t), lerp(1150, hy - 40, t), lerp(1.0, 1.9, t) * (1 + .0009 * f) + .06 * kick(f, fu, .6), 0); CAM[5] = cam
    return c, cam, 'sombrio_noite'


def s6(f):
    c = museu_bg('dia').copy()
    put_estatua(c, EX, EP, EH, f, 'flor')
    pr = wt(6, 'procurar') - 3
    if f >= pr:   # CLOSE final sorrindo
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.25, 1.06, easeOut(ramp(f, pr, pr + 10))) * (1 + .0012 * (f - pr)), 0); CAM[6] = cam
        return c, cam, 'vivo'
    eu(c, 250, f, expr='sorriso', look=.75)
    o = objeto_img('chaveiro', 200)
    hx, hy = mao_dir(250, 1900, 900)
    c.alpha_composite(o, (int(hx + 20 - o.width / 2), int(hy - 40 - o.height / 2)))
    t = smooth(ramp(f, 0, pr))
    cam = (lerp(560, 621, t), lerp(1250, 1120, t), lerp(1.2, 1.02, t) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 2', 540, 100, 1, 64, big=True)
            gancho(im, ['A ESTÁTUA', 'ABRIU OS OLHOS'], 180, 1, 104)
        else:
            stamp(im, 'NA PARTE 1', 540, 210, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
            ch = wt(0, 'chaveiro') - 3
            card(im, 'Meu chaveiro', 'na mão da estátua', 330, 420, ramp(f, ch, ch + 10))
    elif si == 1:
        k = wt(1, 'noite') - 3
        stamp(im, 'NAQUELA NOITE', 540, 200, back(ramp(f, k, k + 8)), 80)
    elif si == 2:
        m = wt(2, 'meia-noite') - 3; ol = wt(2, 'olhos') - 3; de = wt(2, 'desceu') - 3
        if f < ol + 4: painel(im, 'MUSEU', '00:00', 540, 230, ramp(f, m, m + 10), w=380)
        elif f < de - 2: stamp(im, 'ABRIU OS OLHOS', 540, 250, back(ramp(f, ol + 6, ol + 14)), 72, rot=3)
        else: burst(im, 'TUM!', 820, 420, back(ramp(f, de, de + 8)), 70)
    elif si == 3:
        pe = wt(3, 'perdido') - 3
        stamp(im, 'PRA RUA', 540, 210, back(ramp(f, wt(3, 'rua') - 3, wt(3, 'rua') + 5)), 80)
        card(im, 'Guarda-chuva', 'perdido na calçada', 760, 470, ramp(f, pe, pe + 10))
    elif si == 4:
        to = wt(4, 'toda') - 3; pe = wt(4, 'perdeu') - 3
        stamp(im, 'ACHADOS E PERDIDOS', 540, 220, back(ramp(f, to, to + 8)), 72)
        card(im, 'Toda noite', 'ela acha o que a cidade perdeu', 540, 430, ramp(f, pe, pe + 10))
    elif si == 5:
        fu = wt(5, 'furo') - 3; ac = wt(5, 'achou') - 3
        if f < ac: burst(im, 'UM FURO!', 540, 1260, back(ramp(f, fu, fu + 8)), 70)
        else: stamp(im, 'ELA ACHOU', 540, 250, back(ramp(f, ac + 2, ac + 10)), 80)
    elif si == 6:
        pr = wt(6, 'procurar') - 3; pe = wt(6, 'perde') - 3
        if f < pr: card(im, 'Perdeu algo?', 'olha na mão dela', 740, 430, ramp(f, pe, pe + 10), to_out(6, MX, MY))
        else: stamp(im, 'EU SEI ONDE PROCURAR', 540, 250, back(ramp(f, pr + 4, pr + 12)), 66, rot=3)
    return grao(im.convert('RGB'), lf)
