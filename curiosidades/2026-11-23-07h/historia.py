"""Formato MISTÉRIO: "A nuvem da casa 27", PARTE 1 (23/11/2026, 07h). História inventada.
Narradora: menina de coque castanho, pele morena, blusa amarela e calça azul (mesmas cores na parte 2).
Premissa: na rua dela, toda terça às quatro da tarde chove só em cima da casa 27 (uma nuvem pequena, dez minutos);
no resto da rua o céu fica azul; regra: ninguém abre guarda-chuva ali (Dona Zica dizia que a chuva era visita);
Dona Zica se mudou há um ano, a casa ficou vazia e a nuvem continuou vindo; ontem (terça) a nuvem não veio;
hoje de manhã tem uma nuvem pequena parada em cima da casa da narradora.
Cenários/cores: s0 CAPA close (rua de dia com a nuvem) -> rua de dia, nuvem na 27 (vivo) | s1 casa 27 de perto, chuva (vivo) |
s2 rua toda, céu azul, vizinho olhando (vivo) | s3 lembrança: Dona Zica na chuva (tarde) | s4 casa vazia na neblina (sombrio) |
s5 terça 16h sem nuvem + CLOSE (vivo) | s6 manhã fria, nuvem em cima da casa dela + CLOSE final (frio)."""
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
VIZ = dict(penteado='careca', cabelo='#3a2a22', pele='#8a5a3a', roupa='#5a9a6a', calca='#2d2f32', barba=True)
RUA = (('#e8b4b8', '', False), ('#f4d35e', '27', False), ('#a8d0e6', '', False))
MINHA = (('#e8b4b8', '', False), ('#7fb3d5', '12', True), ('#c9e2b3', '', False))

LINES = [
    "Na minha rua, toda terça, às quatro da tarde, chove. Mas só em cima de uma casa.",
    "A casa vinte e sete. Uma nuvem pequena aparece, chove dez minutos, e vai embora.",
    "No resto da rua, o céu fica azul. Ninguém sabe de onde a nuvem vem.",
    "A regra da rua é uma só: ninguém abre guarda-chuva ali. Dona Zica dizia que a chuva era visita.",
    "Mas faz um ano que Dona Zica se mudou. A casa ficou vazia. E a nuvem continuou vindo.",
    "Ontem foi terça. Às quatro, o céu ficou azul. E a nuvem não veio.",
    "Hoje, quando eu acordei, tinha uma nuvem pequena... parada em cima da minha casa.",
]
FALA_TIKTOK = "Comenta QUERO pra parte dois."
CTA_TEXTO = "COMENTA QUERO"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 5
FLASH = []
CHECK = [(0, 'chove', 6), (0, 'casa', 6), (1, 'vinte', 6), (1, 'embora', 8), (2, 'azul', 6), (2, 'ninguem', 6),
         (3, 'regra', 4), (3, 'visita', 6), (4, 'vazia', 6), (4, 'continuou', 6), (5, 'quatro', 6), (5, 'veio', 10),
         (6, 'nuvem', 6), (6, 'casa', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.patter(2, 60, 4, .05)
    s.patter(s.W(0, 'chove') - 2, s.W(1, 'embora'), 4, .06)
    s.ting(s.W(0, 'quatro'), .25)
    s.ting(s.W(1, 'vinte'), .25); s.whoosh(s.W(1, 'embora') - 4, .7, .25)
    s.patter(s.W(2, 'no'), s.W(2, 'ninguem') + 30, 4, .03)
    s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.patter(s.W(3, 'dona'), s.W(3, 'visita') + 20, 4, .04)
    s.thunk(s.W(4, 'vazia') - 2, 120, .6)
    s.patter(s.W(4, 'continuou') - 2, s.W(4, 'vindo') + 20, 4, .05)
    s.ting(s.W(5, 'quatro'), .3); s.trill(s.W(5, 'veio'), .5, .12)
    s.thunk(s.W(6, 'nuvem') - 2, 120, .6)
    s.patter(s.W(6, 'parada'), s.W(6, 'casa') + 30, 4, .04)
    s.thunk(s.W(6, 'casa') + 6, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close assustado + PARTE 1 + gancho
        c = rua27_bg('dia').copy(); nuvem(c, 621, 640, 1, f)
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    c = rua27_bg('dia').copy()
    ch = wt(0, 'chove') - 3
    nuvem(c, 621, 640, back(ramp(f, ch, ch + 10)), f, chove=ramp(f, ch + 4, ch + 12))
    eu(c, 260, f, expr='preocupado' if f >= wt(0, 'casa') - 3 else 'neutro', look=.75)
    t = smooth(ramp(g, 0, 120))
    cam = (lerp(520, 621, t), lerp(1350, 1150, t), lerp(1.25, 1.02, easeOut(ramp(g, 0, 16))) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = rua27_bg('dia').copy()
    em = wt(1, 'embora') - 3
    t = smooth(ramp(f, em, em + 24))
    nuvem(c, 621 + 900 * t, 640 - 150 * t, 1 - .5 * t, f, chove=1 - t)
    vi = wt(1, 'vinte') - 3
    z = lerp(1.05, 1.45, smooth(ramp(f, 0, vi + 10))) + .05 * kick(f, vi, .6)
    cy = lerp(1100, 1050, smooth(ramp(f, 0, vi + 10)))
    if f > em: z = lerp(z, 1.1, smooth(ramp(f, em, em + 24))); cy = lerp(cy, 900, smooth(ramp(f, em, em + 24)))
    cam = (621, cy, z * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = rua27_bg('dia').copy()
    nuvem(c, 621, 640, 1, f)
    az = wt(2, 'azul') - 3
    eu(c, 230, f, expr='neutro', look=.5)
    put_menino(c, 1020, 1900, 880, f, expr='preocupado' if f >= az else 'neutro', look=-.5, flip=True, seed=5, **VIZ)
    cam = (621, lerp(1000, 1150, smooth(ramp(f, 0, 140))), lerp(1.0, 1.08, smooth(ramp(f, 0, 140))) * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = rua27_bg('tarde').copy()
    nuvem(c, 621, 640, 1, f, cor=(226, 214, 206))
    put_menino(c, 640, 1880, 860, f, expr='sorriso', look=-.5, seed=4, **ZICA)
    eu(c, 230, f, expr='neutro', look=.75)
    gc = wt(3, 'abre') - 3
    guarda_chuva(c, 360, 1880, back(ramp(f, gc, gc + 8)) * .9)
    r = wt(3, 'regra') - 3
    cam = (621, 1150, lerp(1.0, 1.12, smooth(ramp(f, 0, 150))) * (1 + .0009 * f) + .05 * kick(f, r, .6), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = rua27_bg('neblina').copy()
    co = wt(4, 'continuou') - 3
    nuvem(c, 621, 640, back(ramp(f, co, co + 10)), f, chove=ramp(f, co + 4, co + 12), cor=(200, 206, 210))
    nb = neblina_img(1.0); o2 = int(f * 2) % W_
    c.alpha_composite(nb.crop((o2, 0, o2 + W_, 420)), (0, 1350))
    va = wt(4, 'vazia') - 3
    t = smooth(ramp(f, 0, va + 6))
    cam = (621, lerp(1000, 1180, t), lerp(1.0, 1.5, t) * (1 + .0009 * f), 0)
    if f > co - 6: cam = (621, lerp(1180, 950, smooth(ramp(f, co - 6, co + 14))), lerp(1.5, 1.08, smooth(ramp(f, co - 6, co + 14))) * (1 + .0009 * f), 0)
    CAM[4] = cam
    return c, cam, 'sombrio'


def s5(f):
    c = rua27_bg('dia').copy()
    ve = wt(5, 'veio') - 3
    if f >= ve + 6:   # CLOSE desconfiado
        c = put_close(c, f, expr='desconfiado', look=.5, **EU)
        cam = (621, 1104, lerp(1.15, 1.04, easeOut(ramp(f, ve + 6, ve + 14))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'vivo'
    eu(c, 300, f, expr='preocupado' if f >= wt(5, 'azul') - 3 else 'neutro', look=.75)
    cam = (lerp(560, 621, smooth(ramp(f, 0, ve))), 1100, lerp(1.1, 1.0, smooth(ramp(f, 0, ve))) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'vivo'


def s6(f):
    c = rua27_bg('frio', MINHA).copy()
    nu = wt(6, 'nuvem') - 3
    nuvem(c, 621, 640, back(ramp(f, nu, nu + 10)), f, chove=0, cor=(206, 214, 224))
    ca = wt(6, 'casa')
    fim = ca + 6
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.3, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[6] = cam
        return c, cam, 'frio'
    pa = wt(6, 'parada') - 3
    eu(c, 260, f, expr='choque' if f >= pa else 'neutro', look=.75)
    t = smooth(ramp(f, 0, pa))
    cam = (621, lerp(1150, 1000, t), lerp(1.05, 1.0, t) * (1 + .0009 * f), 2 * math.sin(f * .05) * ramp(f, pa, pa + 10)); CAM[6] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 1', 540, 100, 1, 64, big=True)
            gancho(im, ['SÓ CHOVE EM', 'UMA CASA DA RUA'], 180, 1, 104)
        else:
            stamp(im, 'NA MINHA RUA', 290, 230, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
            q = wt(0, 'quatro') - 3
            painel(im, 'TERÇA', '16:00', 800, 250, ramp(f, q, q + 10), w=380)
    elif si == 1:
        v = wt(1, 'vinte') - 3; d_ = wt(1, 'dez') - 3
        stamp(im, 'CASA 27', 540, 200, back(ramp(f, v, v + 8)), 80)
        ax, ay = to_out(1, 621, 1350)
        card(im, 'Chuva', 'só 10 minutos', 300, 1240, ramp(f, d_, d_ + 10) * (1 - ramp(f, wt(1, 'embora') + 10, wt(1, 'embora') + 18)))
    elif si == 2:
        az = wt(2, 'azul') - 3; n = wt(2, 'ninguem') - 3
        card(im, 'Resto da rua', 'céu azul, nenhuma gota', 300, 230, ramp(f, az, az + 10))
        interrog(im, 760, 300, f, ramp(f, n, n + 8))
    elif si == 3:
        r = wt(3, 'regra') - 3; gc = wt(3, 'abre') - 3; z = wt(3, 'zica') - 3
        if f < z: stamp(im, 'A REGRA', 540, 220, back(ramp(f, r, r + 8)), 100, big=True)
        if f < z: card(im, 'Proibido', 'abrir guarda-chuva ali', 300, 420, ramp(f, gc, gc + 10))
        else: card(im, 'Dona Zica', 'a chuva é visita', 330, 260, ramp(f, z, z + 10))
    elif si == 4:
        a = wt(4, 'ano') - 3; va = wt(4, 'vazia') - 3
        painel(im, 'CASA VAZIA HÁ', '1 ANO', 540, 230, ramp(f, a, a + 10), w=460)
        if f >= wt(4, 'continuou') - 3: burst(im, 'PLIC PLIC', 780, 520, back(ramp(f, wt(4, 'continuou'), wt(4, 'continuou') + 8)), 50)
    elif si == 5:
        q = wt(5, 'quatro') - 3; ve = wt(5, 'veio') - 3
        if f < ve + 6: painel(im, 'TERÇA', '16:00', 780, 300, ramp(f, q, q + 10), w=380)
        else: stamp(im, 'NENHUMA NUVEM', 540, 250, back(ramp(f, ve + 8, ve + 16)), 72)
    elif si == 6:
        h_ = wt(6, 'hoje') - 3; fim = wt(6, 'casa') + 6
        if f < fim: stamp(im, 'HOJE CEDO', 540, 160, back(ramp(f, h_, h_ + 8)), 70)
        else: stamp(im, 'A MINHA CASA?', 540, 250, back(ramp(f, fim + 4, fim + 12)), 72, rot=3)
    return grao(im.convert('RGB'), lf)
