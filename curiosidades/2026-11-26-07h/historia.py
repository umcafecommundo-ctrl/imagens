"""Formato MISTÉRIO: "A lousa da sala quatro", PARTE 1 (26/11/2026, 07h). História inventada.
Narrador: Caio, menino de cabelo curto castanho escuro, pele clara morena, blusa amarela e calça azul (mesmas cores na parte 2).
Premissa: na escola dele, a sala 4 está fechada há 30 anos, mas toda manhã a lousa amanhece escrita com giz, letra torta de
criança; regra da escola: ninguém apaga a lousa da sala 4; a diretora jura que a chave sumiu; às vezes aparece uma conta,
os alunos passam a resposta num papel por baixo da porta e no outro dia aparece uma estrela e "certo"; hoje cedo a lousa
tinha o nome dele e embaixo "você é o próximo" (com uma forca pequena desenhada no canto: a pista da parte 2).
Cenários/cores: s0 CAPA close (corredor de dia) -> corredor de dia com a porta da SALA 4 (vivo) | s1 lousa em close de dia
(vivo) | s2 corredor de dia com a diretora (vivo) | s3 lousa com a conta -> pé da porta com o papel (tarde) | s4 lousa com
estrela e CERTO (tarde) | s5 corredor de manhã fria, andando + CLOSE curioso (frio) | s6 lousa com o nome + CLOSE final (frio)."""
from kit import *
import kit
from sombrio import *
from sala4 import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'; PITCH = '-4Hz'
EU = dict(penteado='curto', cabelo='#3a2416', pele='#e0b48c', roupa='#e8b730', calca='#2e4a7a')
DIRETORA = dict(penteado='coque', cabelo='#9a9a9a', pele='#c98f65', roupa='#7b4a8c', calca='#2d2f32', oculos=True, velho=True)

LINES = [
    "Na minha escola, a sala quatro está fechada há trinta anos. Mas toda manhã, a lousa dela amanhece escrita.",
    "Letra de giz, torta, de criança. E a regra da escola é uma só: ninguém apaga a lousa da sala quatro.",
    "A diretora jura que a chave sumiu faz tempo. Ninguém entra lá. Nem ela.",
    "Às vezes, na lousa, tem uma conta. E a gente passa a resposta num papel, por baixo da porta.",
    "No outro dia, do lado da conta, aparece uma estrela... e a palavra: certo.",
    "Hoje cedo, eu passei sozinho no corredor e olhei pelo vidro da porta.",
    "A lousa tinha o meu nome. E embaixo... você é o próximo.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "EU ENTRO NA SALA?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'quatro', 6), (0, 'trinta', 6), (0, 'lousa', 8), (1, 'giz', 6), (1, 'regra', 4), (2, 'diretora', 6),
         (2, 'chave', 6), (3, 'conta', 6), (3, 'papel', 8), (4, 'estrela', 6), (4, 'certo', 6), (5, 'corredor', 6),
         (5, 'vidro', 8), (6, 'nome', 8), (6, 'proximo', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    s.thunk(s.W(0, 'trinta') - 2, 80, .5); s.ting(s.W(0, 'lousa'), .3)
    s.thunk(s.W(1, 'regra') - 2, 90, .7)
    s.ting(s.W(2, 'chave'), .35)
    s.ting(s.W(3, 'conta'), .3); s.whoosh(s.W(3, 'porta') - 4, .5, .25)
    s.ting(s.W(4, 'estrela'), .4); s.ting(s.W(4, 'certo') + 2, .3)
    s.whoosh(s.W(5, 'cedo') - 3, .6, .2)
    s.ting(s.W(6, 'nome'), .3); s.thunk(s.W(6, 'proximo') + 4, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1960, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def ramp_z(f):
    return 1 + .0012 * f


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = corredor_bg('dia').copy()
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * ramp_z(f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    lo = wt(0, 'lousa') - 3
    c = corredor_bg('dia').copy()
    eu(c, 330, f, expr='neutro' if f < lo else 'curioso', look=.8)
    if f < lo:
        t = smooth(ramp(g, 0, lo - CAPA))
        cam = (lerp(560, 700, t), lerp(1250, 1200, t), lerp(1.25, 1.05, easeOut(ramp(g, 0, 18))) * ramp_z(f)
               + .05 * kick(f, wt(0, 'trinta') - 3, .6), 0)
    else:
        t = easeOut(ramp(f, lo, lo + 14))
        cam = (lerp(700, 850, t), lerp(1200, 1000, t), lerp(1.05, 2.3, t) * ramp_z(f - lo), 0)
    CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = lousa_bg((('BOM DIA', 170), ('TURMA', 140)), 'dia').copy()
    re = wt(1, 'regra') - 3
    t = smooth(ramp(f, 0, re))
    cam = (lerp(560, 621, t), lerp(1060, 1120, t), lerp(1.35, 1.15, t) * ramp_z(f) + .05 * kick(f, re, .6), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = corredor_bg('dia').copy()
    ch = wt(2, 'chave') - 3; ne = wt(2, 'nem') - 3
    eu(c, 300, f, expr='curioso', look=.7)
    put_menino(c, 930, 2000, 980, f, expr='desconfiado' if f < ne else 'preocupado', look=-.6 if f < ne else .3, seed=5, **DIRETORA)
    t = smooth(ramp(f, 0, ch))
    z = lerp(1.05, 1.15, t) if f < ne else 1.55
    cx = lerp(640, 680, t) if f < ne else 930
    cam = (cx, 1330, z * ramp_z(f) + .05 * kick(f, ch, .6) + .06 * kick(f, ne, .6), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    pa = wt(3, 'papel') - 3
    if f < pa:
        c = lousa_bg((('7 x 8 = ?', 150),), 'tarde').copy()
        co = wt(3, 'conta') - 3
        cam = (621, 1100, lerp(1.05, 1.2, smooth(ramp(f, 0, pa))) * ramp_z(f) + .06 * kick(f, co, .6), 0); CAM[3] = cam
        return c, cam, 'tarde'
    c = corredor_bg('tarde').copy()
    eu(c, 470, f, expr='curioso', look=.8)
    po = wt(3, 'porta') - 3
    t = smooth(ramp(f, po, po + 14))
    x = lerp(560, 780, t)
    pi = papel_img(200)
    if x < 690:
        c.alpha_composite(pi, (int(x - 100), 1530))
    else:   # passando por baixo da porta: corta na borda
        w = max(1, int(pi.width - (x - 690)))
        c.alpha_composite(pi.crop((0, 0, w, pi.height)), (int(x - 100), 1530))
    cam = (lerp(560, 640, t), 1500, lerp(1.6, 1.9, smooth(ramp(f, pa, po + 14))) * ramp_z(f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    es = wt(4, 'estrela') - 3; ce = wt(4, 'certo') - 3
    if f < es:
        c = lousa_bg((('7 x 8 = ?', 150),), 'tarde').copy()
    elif f < ce:
        c = lousa_bg((('7 x 8 = 56', 150),), 'tarde', 0, True).copy()
    else:
        c = lousa_bg((('7 x 8 = 56', 150), ('CERTO!', 150)), 'tarde', 0, True).copy()
    cam = (lerp(621, 680, smooth(ramp(f, 0, es))) if f < ce else 621, lerp(1100, 1250, smooth(ramp(f, 0, es))) if f < ce else 1160,
           (1.1 if f < es else 1.2 if f < ce else 1.1) * ramp_z(f) + .06 * kick(f, es, .6) + .06 * kick(f, ce, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    ol = wt(5, 'olhei') - 3
    c = corredor_bg('frio').copy()
    if f < ol:
        eu(c, lerp(220, 520, ramp(f, 0, ol)), f, walk=1, expr='neutro', look=.6)
        cam = (lerp(400, 620, ramp(f, 0, ol)), 1420, 1.4 * ramp_z(f), 0); CAM[5] = cam
        return c, cam, 'frio'
    eu(c, 520, f, expr='curioso', look=.8)
    c = put_close(c, f, expr='curioso', look=.75, **EU)
    cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, ol, ol + 10))) * ramp_z(f - ol), 0); CAM[5] = cam
    return c, cam, 'frio'


def s6(f):
    em = wt(6, 'embaixo') - 3; pr = wt(6, 'proximo') - 3
    fim = pr + 16
    if f >= fim:   # CLOSE final
        c = corredor_bg('frio').copy()
        c = put_close(c, f, expr='medo', look=0, escurece=.3, suor=1, shake=.3, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * ramp_z(f - fim), 0); CAM[6] = cam
        return c, cam, 'frio'
    if f < em:
        c = lousa_bg((('CAIO', 200),), 'frio', 1).copy()
        cam = (621, lerp(1000, 1060, ramp(f, 0, em)), lerp(1.25, 1.5, smooth(ramp(f, 0, em))) * ramp_z(f) + .07 * kick(f, wt(6, 'nome') - 3, .7), 0)
    else:
        c = lousa_bg((('CAIO', 200), ('VOCÊ É O PRÓXIMO', 76)), 'frio', 1).copy()
        cam = (621, 1120, lerp(1.45, 1.2, easeOut(ramp(f, em, em + 10))) * ramp_z(f) + .08 * kick(f, pr, .8),
               3 * math.sin(f * .4) * ramp(f, pr, pr + 4));
    CAM[6] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['A LOUSA TINHA', 'O MEU NOME'], 170, 1, 104)
            stamp(im, 'PARTE 1', 880, 1240, 1, 46)
        else:
            tr = wt(0, 'trinta') - 3; lo = wt(0, 'lousa') - 3
            if f < lo:
                stamp(im, 'NA MINHA ESCOLA', 540, 200, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
                painel(im, 'FECHADA HÁ', '30 ANOS', 790, 1130, ramp(f, tr, tr + 10), w=420)
            else:
                burst(im, '?!', 540, 260, back(ramp(f, lo + 6, lo + 14)), 90)
    elif si == 1:
        gi = wt(1, 'giz') - 3; r = wt(1, 'regra') - 3
        if f < r: card(im, 'Letra de giz', 'torta, de criança', 540, 230, ramp(f, gi, gi + 10))
        else:
            stamp(im, 'A REGRA', 540, 200, back(ramp(f, r, r + 8)), 100, big=True)
            ap = wt(1, 'apaga') - 3
            card(im, 'Ninguém apaga', 'a lousa da sala 4', 540, 1320, ramp(f, ap - 6, ap + 4))
    elif si == 2:
        d = wt(2, 'diretora') - 3; ch = wt(2, 'chave') - 3; ne = wt(2, 'nem') - 3
        if f < ch: card(im, 'A diretora', 'Dona Célia', 540, 230, ramp(f, d, d + 10))
        elif f < ne: burst(im, 'A CHAVE SUMIU', 540, 260, back(ramp(f, ch, ch + 8)), 56)
        else: stamp(im, 'NEM ELA', 540, 240, back(ramp(f, ne, ne + 8)), 84)
    elif si == 3:
        co = wt(3, 'conta') - 3; pa = wt(3, 'papel') - 3
        if f < pa: interrog(im, 540, 250, f, ramp(f, co, co + 8))
        else: card(im, 'A resposta', 'por baixo da porta', 540, 260, ramp(f, pa, pa + 10))
    elif si == 4:
        es = wt(4, 'estrela') - 3; ce = wt(4, 'certo') - 3
        if f < es: card(im, 'No outro dia...', '', 540, 240, ramp(f, 4, 14))
        elif f < ce: burst(im, 'PLIM', 540, 260, back(ramp(f, es, es + 6)), 70, cor=(230, 190, 80))
        else: stamp(im, 'RESPONDERAM', 540, 250, back(ramp(f, ce + 4, ce + 12)), 80)
    elif si == 5:
        ce = wt(5, 'cedo') - 3; ol = wt(5, 'olhei') - 3
        if f < ol: painel(im, 'HOJE', '06:50', 540, 260, ramp(f, ce, ce + 10), w=360)
        else: stamp(im, 'SOZINHO', 540, 250, back(ramp(f, ol, ol + 8)), 80)
    elif si == 6:
        no = wt(6, 'nome') - 3; pr = wt(6, 'proximo') - 3; fim = pr + 16
        if f < pr: burst(im, 'EU?!', 540, 250, back(ramp(f, no, no + 6)), 80) if f >= no else None
        elif f < fim: burst(im, '?!', 540, 260, back(ramp(f, pr, pr + 6)), 110)
        else: stamp(im, 'O PRÓXIMO SOU EU', 540, 250, back(ramp(f, fim + 2, fim + 10)), 76, rot=3)
    return grao(im.convert('RGB'), lf)
