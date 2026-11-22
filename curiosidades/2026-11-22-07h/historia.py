"""Formato MISTÉRIO: "O cavalo treze", PARTE 1 (22/11/2026, 07h). História inventada.
Narradora: Nina, menina de cabelo longo castanho-escuro, pele morena, blusa rosa e calça azul (mesmas cores na parte 2).
Seu Dito: senhor da bilheteria (cabelo branco, óculos, barba, camisa verde).
Premissa: no parque de diversões da cidade, o carrossel tem doze cavalos de madeira; em toda noite de lua cheia quem passa conta
treze; o 13º é branco de crina dourada e gira sozinho, sem música; regra: ninguém sobe no cavalo treze; ninguém sabe de onde ele
vem, de manhã só há doze; o moço da bilheteria jura que antigamente o carrossel tinha treze; hoje é lua cheia e ele deu a Nina uma
ficha com o número treze.
Cenários/cores: s0 CAPA close (noite) -> parque de dia (vivo) | s1 parque à noite, lua cheia + CLOSE no susto (sombrio_noite) |
s2 carrossel à noite, cavalo branco (sombrio_noite) | s3 parque fim de tarde (tarde) | s4 parque com neblina -> manhã fria (sombrio/frio) |
s5 bilheteria fim de tarde, lembrança (tarde) | s6 bilheteria à noite (sombrio_noite) | s7 ficha 13 + CLOSE final (sombrio_noite)."""
from kit import *
import kit
from sombrio import *
from carrossel import *

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='longo', cabelo='#3a2418', pele='#a8714a', roupa='#e86a8a', calca='#3b5a8a')
DITO = dict(penteado='curto', cabelo='#e4e4e0', pele='#e8c4a4', roupa='#5a9a6a', calca='#4a4036', oculos=True, barba=True, velho=True)

LINES = [
    "No parque da minha cidade, tem um carrossel com doze cavalos de madeira.",
    "Mas toda noite de lua cheia, quem passa na frente conta treze.",
    "O cavalo a mais é branco, de crina dourada. E gira sozinho, sem música.",
    "A regra do parque é uma só: ninguém sobe no cavalo treze.",
    "Ninguém sabe de onde ele vem. De manhã, sobram só os doze.",
    "O moço da bilheteria jura que, antigamente, o carrossel tinha treze cavalos.",
    "Hoje é noite de lua cheia. E ele me deu uma ficha diferente.",
    "Com o número treze.",
]
FALA_TIKTOK = "Comenta QUERO pra parte dois."
CTA_TEXTO = "COMENTA QUERO"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'carrossel', 6), (1, 'lua', 4), (1, 'treze', 6), (2, 'branco', 4), (2, 'sozinho', 4), (3, 'regra', 4),
         (3, 'treze', 6), (4, 'manha', 6), (5, 'bilheteria', 6), (6, 'ficha', 8), (7, 'treze', 10)]
CAM = {}
CAPA = 38   # quadros da capa (close + gancho) no início da cena 0


def SFX(s):
    for si in (0, 3): s.patter(s.W(si, LINES[si].split()[0].strip(',.:')) - 4, s.W(si, LINES[si].split()[0].strip(',.:')) + 40, 4, .05)
    s.thunk(2, 120, .8)
    s.whoosh(s.W(0, 'carrossel') - 6, .5, .2)
    s.trill(s.W(1, 'lua'), .5, .12)
    s.thunk(s.W(1, 'treze') - 2, 70, 1.0)
    s.ting(s.W(2, 'branco'), .25); s.whoosh(s.W(2, 'sozinho') - 6, .6, .3)
    s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.whoosh(s.W(4, 'manha') - 6, .5, .2)
    s.ting(s.W(5, 'treze'), .25)
    s.ting(s.W(6, 'ficha'), .35)
    s.thunk(s.W(7, 'treze') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def nina(c, x, f, feet=1760, h=960, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def dito(c, x, f, feet=1740, h=1000, **kw):
    put_menino(c, x, feet, h, f, seed=7, **dict(DITO, **kw))


def noite_bg():
    c = parque_bg('noite').copy(); lua(c, 960, 300, 72); return c


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close assustado + PARTE 1 + gancho (desde o quadro 0)
        c = noite_bg(); carrossel(c, f, 'noite', 12, f * .02, extra=True)
        c = put_close(c, f, expr='choque', look=0, shake=.2, escurece=0, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'sombrio_noite'
    g = f - CAPA
    c = parque_bg('dia').copy()
    carrossel(c, f, 'dia', 12, f * .02)
    nina(c, 250, f, feet=1900, h=900, expr='sorriso', look=.75)
    t = smooth(ramp(g, 0, 110))
    cam = (lerp(560, 621, t), lerp(1250, 1150, t), lerp(1.25, 1.02, easeOut(ramp(g, 0, 14))) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    tr = wt(1, 'treze') - 3
    c = noite_bg()
    carrossel(c, f, 'noite', 12, f * .015, extra=f >= tr)
    if f >= tr + 22:   # CLOSE no susto
        c = put_close(c, f, expr='choque', look=.5, shake=.3, **EU)
        cam = (621, 1104 + kick(f, tr + 22, .8) * 12, lerp(1.25, 1.05, easeOut(ramp(f, tr + 22, tr + 32))) * (1 + .0009 * f), 0); CAM[1] = cam
        return c, cam, 'sombrio_noite'
    nina(c, 330, f, feet=1900, h=900, expr='choque' if f >= tr else 'neutro', look=.75)
    t = smooth(ramp(f, 0, tr))
    cam = (621, lerp(900, 1150, t), lerp(1.15, 1.0, t) * (1 + .0009 * f) + .1 * kick(f, tr, .6), 0); CAM[1] = cam
    return c, cam, 'sombrio_noite'


def s2(f):
    c = noite_bg()
    p = carrossel(c, f, 'noite', 12, -5.75 + f * .004, extra=True)
    t = smooth(ramp(f, 0, 90))
    cam = (lerp(621, 640, t), lerp(1100, 1080, t), lerp(1.05, 1.45, t) * (1 + .0009 * f), lerp(0, 2, t)); CAM[2] = cam
    CAM['p13'] = p
    return c, cam, 'sombrio_noite'


def s3(f):
    c = parque_bg('tarde').copy()
    carrossel(c, f, 'tarde', 12, f * .02)
    nina(c, 980, f, feet=1900, h=900, expr='preocupado', look=-.75, flip=True)
    cam = (621, 1150, lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) * (1 + .0009 * f) + .05 * kick(f, wt(3, 'regra') - 3, .6), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    m = wt(4, 'manha') - 3
    if f < m:
        c = parque_bg('neblina').copy()
        carrossel(c, f, 'neblina', 12, 2 + f * .01)
        nb = neblina_img(1.0); o2 = int(f * 2) % W_
        c.alpha_composite(nb.crop((o2, 0, o2 + W_, 420)), (0, 1250))
        cam = (621, 1050, lerp(1.0, 1.15, smooth(ramp(f, 0, m))) * (1 + .0009 * f), 0); CAM[4] = cam
        return c, cam, 'sombrio'
    g = f - m
    c = parque_bg('frio').copy()
    carrossel(c, f, 'frio', 12, 0.4)
    cam = (621, 1100, lerp(1.2, 1.05, easeOut(ramp(g, 0, 14))) * (1 + .0009 * f), 0); CAM[4] = cam
    return c, cam, 'frio'


def s5(f):
    c = bilheteria_bg('tarde').copy()
    dito(c, 621, f, feet=1560, h=820, expr='neutro', look=-.5)
    d = ImageDraw.Draw(c); d.rectangle((330, 1100, 910, 1150), fill=(110, 74, 44, 255)); d.line((330, 1100, 910, 1100), fill=(36, 30, 32, 255), width=6)
    nina(c, 200, f, feet=1980, h=900, expr='neutro', look=.75)
    t = smooth(ramp(f, 0, 130))
    cam = (lerp(560, 621, t), lerp(1250, 1050, t), lerp(1.0, 1.2, t) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = bilheteria_bg('noite').copy(); lua(c, 960, 300, 72)
    dito(c, 621, f, feet=1560, h=820, expr='neutro', look=-.5)
    d = ImageDraw.Draw(c); d.rectangle((330, 1100, 910, 1150), fill=(70, 48, 30, 255)); d.line((330, 1100, 910, 1100), fill=(36, 30, 32, 255), width=6)
    fi = wt(6, 'ficha') - 3
    u = easeOut(ramp(f, fi - 8, fi + 8))
    ficha(c, lerp(621, 780, u), lerp(1040, 1060, u), 62 * ramp(f, fi - 10, fi - 4), '?')
    nina(c, 330, f, feet=1980, h=900, expr='preocupado' if f >= fi else 'neutro', look=.75)
    t = smooth(ramp(f, 0, fi))
    cam = (lerp(621, 580, t), lerp(1100, 1150, t), lerp(1.0, 1.15, t) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'sombrio_noite'


def s7(f):
    c = bilheteria_bg('noite').copy(); lua(c, 960, 300, 72)
    tr = wt(7, 'treze') - 3
    fim = tr + 22
    ficha(c, 621, 1000, 220 * easeOut(ramp(f, 0, 10)), 13, rot=6 * math.sin(f * .1))
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.45, shake=.15, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[7] = cam
        return c, cam, 'sombrio_noite'
    cam = (621, 1000, 1.2 * (1 + .002 * f) + .08 * kick(f, tr, .8), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 1', 540, 100, 1, 64, big=True)
            gancho(im, ['O CARROSSEL GANHA', 'UM CAVALO NA LUA CHEIA'], 180, 1, 96)
        else:
            stamp(im, 'NO PARQUE DA MINHA CIDADE', 540, 260, back(ramp(f, CAPA + 2, CAPA + 10)), 64)
            d = wt(0, 'doze') - 3
            painel(im, 'CAVALOS', '12', 800, 560, ramp(f, d, d + 10))
    elif si == 1:
        tr = wt(1, 'treze') - 3; lu = wt(1, 'lua') - 3
        if f < tr + 22: stamp(im, 'LUA CHEIA', 300, 470, back(ramp(f, lu, lu + 8)), 70)
        painel(im, 'CAVALOS', '13' if f >= tr else '12', 540, 230, ramp(f, 2, 12), glitch=1 if tr <= f < tr + 12 and f % 4 < 2 else 0)
    elif si == 2:
        b = wt(2, 'branco') - 3; m = wt(2, 'musica') - 3
        p = CAM.get('p13')
        alvo = to_out(2, *p) if p else None
        card(im, 'Cavalo 13', 'branco, de crina dourada', 330, 330, ramp(f, b, b + 10), alvo=alvo)
        burst(im, 'SEM MÚSICA', 760, 1250, back(ramp(f, m, m + 8)), 54)
    elif si == 3:
        r = wt(3, 'regra') - 3; n = wt(3, 'ninguem') - 3
        stamp(im, 'A REGRA', 540, 260, back(ramp(f, r, r + 8)), 110, big=True)
        card(im, 'Proibido', 'subir no cavalo treze', 540, 520, ramp(f, n, n + 10))
    elif si == 4:
        m = wt(4, 'manha') - 3
        if f < m: interrog(im, 540, 420, f, ramp(f, 2, 12))
        else:
            stamp(im, 'DE MANHÃ', 540, 200, back(ramp(f, m, m + 8)), 70)
            painel(im, 'CAVALOS', '12', 540, 440, ramp(f, m + 6, m + 16))
    elif si == 5:
        b = wt(5, 'bilheteria') - 3; a = wt(5, 'antigamente') - 3
        stamp(im, 'SEU DITO, DA BILHETERIA', 540, 170, back(ramp(f, b, b + 8)), 56)
        card(im, 'Antigamente', 'o carrossel tinha treze cavalos', 330, 330, ramp(f, a, a + 10))
    elif si == 6:
        h_ = wt(6, 'hoje') - 3; fi = wt(6, 'ficha') - 3
        stamp(im, 'HOJE: LUA CHEIA', 540, 110, back(ramp(f, h_, h_ + 8)), 70)
        burst(im, '?!', 850, 420, back(ramp(f, fi, fi + 8)), 70)
    elif si == 7:
        tr = wt(7, 'treze') - 3; fim = tr + 22
        if f < fim: card(im, 'Minha ficha', 'número treze', 540, 260, ramp(f, tr, tr + 8))
        else: stamp(im, 'NINGUÉM SOBE NO 13', 540, 250, back(ramp(f, fim + 4, fim + 12)), 64, rot=3)
    return grao(im.convert('RGB'), lf)
