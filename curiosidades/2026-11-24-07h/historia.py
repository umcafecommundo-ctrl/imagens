"""Formato MISTÉRIO: "A estátua de mão aberta", PARTE 1 (24/11/2026, 07h). História inventada.
Narrador: menino de cabelo curto preto, pele morena, camiseta coral e calça azul (mesmas cores na parte 2).
Premissa: no museu da cidade há uma estátua de pedra de uma menina com a mão aberta; toda manhã aparece um objeto novo
na mão dela (pena, bolinha de gude, chave); o museu fecha às seis com alarme e ninguém sabe quem coloca; regra: ninguém
tira nada da mão dela; o avô do narrador foi guarda 30 anos e jurava que ela nunca repetiu objeto; ontem o narrador
visitou o museu e voltou com o chaveiro no bolso (conferiu); hoje cedo o chaveiro com o nome dele está na mão da estátua.
Cenários/cores: s0 CAPA close (museu de dia) -> museu de dia, estátua (vivo) | s1 a mão de perto, objetos (vivo) |
s2 museu de noite, alarme (sombrio_noite) | s3 museu de dia, a regra (vivo) | s4 lembrança: avô guarda (tarde) |
s5 quarto de tarde, chaveiro na mão + CLOSE (tarde) | s6 museu de manhã fria, chaveiro na mão da estátua + CLOSE final (frio)."""
from kit import *
import kit
from sombrio import *
from museu_estatua import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#2b1d14', pele='#8a5a3a', roupa='#e8655a', calca='#2f4a6a')
AVO = dict(penteado='careca', cabelo='#d8d8d8', pele='#8a5a3a', roupa='#3d5a80', calca='#2d2f32', velho=True, barba=True)
GUARDA = dict(penteado='coque', cabelo='#3a2a22', pele='#e6c8ad', roupa='#3d5a80', calca='#2d2f32')
EX, EP = 630, 1120   # estátua: centro do corpo e pés (em cima do pedestal)
EH = 640
MX, MY = mao_estatua(EX, EP, EH)

LINES = [
    "No museu da minha cidade, tem uma estátua de pedra de uma menina com a mão aberta.",
    "Toda manhã, aparece uma coisa nova na mão dela. Uma pena. Uma bolinha de gude. Uma chave.",
    "O museu fecha às seis, com o alarme ligado. E ninguém sabe quem coloca.",
    "A regra do museu é uma só: ninguém tira nada da mão dela.",
    "Meu avô foi guarda lá por trinta anos. Ele jurava: ela nunca repetiu um objeto.",
    "Ontem eu visitei o museu e voltei pra casa com o meu chaveiro no bolso. Eu conferi.",
    "Hoje cedo, na mão da estátua... tinha um chaveiro com o meu nome.",
]
FALA_TIKTOK = "Comenta QUERO pra parte dois."
CTA_TEXTO = "COMENTA QUERO"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'estatua', 6), (0, 'aberta', 6), (1, 'pena', 4), (1, 'bolinha', 4), (1, 'chave', 6), (2, 'seis', 6),
         (2, 'ninguem', 6), (3, 'regra', 4), (3, 'tira', 6), (4, 'trinta', 6), (4, 'repetiu', 6), (5, 'chaveiro', 6),
         (5, 'conferi', 8), (6, 'estatua', 6), (6, 'nome', 10)]
CAM = {}
CAPA = 36


def SFX(s):
    s.thunk(2, 60, .6)
    s.ting(s.W(0, 'estatua'), .2); s.ting(s.W(0, 'aberta'), .25)
    s.ting(s.W(1, 'pena'), .3); s.ting(s.W(1, 'bolinha'), .3); s.ting(s.W(1, 'chave'), .35)
    s.thunk(s.W(2, 'seis') - 2, 90, .6); s.trill(s.W(2, 'alarme'), .4, .1)
    s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.ting(s.W(4, 'trinta'), .25)
    s.ting(s.W(5, 'chaveiro'), .3); s.thunk(s.W(5, 'conferi') + 4, 60, .6)
    s.ting(s.W(6, 'chaveiro'), .35)
    s.thunk(s.W(6, 'nome') + 6, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def objeto_do_dia(si, f):
    """objeto na mão da estátua na cena 1 (troca na palavra)."""
    o, s = None, 0
    for w_, nome in (('pena', 'pena'), ('bolinha', 'bolinha'), ('chave', 'chave')):
        k = wt(1, w_) - 3
        if f >= k: o, s = nome, back(ramp(f, k, k + 6))
    return o, s


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close assustado + PARTE 1 + gancho
        c = museu_bg('dia').copy(); put_estatua(c, EX, EP, EH, f, 'chaveiro')
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    c = museu_bg('dia').copy()
    put_estatua(c, EX, EP, EH, f)
    eu(c, 250, f, expr='neutro', look=.75)
    t = smooth(ramp(g, 0, 110))
    ab = wt(0, 'aberta') - 3
    z = lerp(1.3, 1.02, easeOut(ramp(g, 0, 18))) + .04 * kick(f, ab, .6)
    cam = (lerp(560, 621, t), lerp(1250, 1120, t), z * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = museu_bg('dia').copy()
    o, so = objeto_do_dia(1, f)
    put_estatua(c, EX, EP, EH, f, o, so)
    pe = wt(1, 'pena') - 3
    t = smooth(ramp(f, 0, pe))
    z = lerp(1.05, 1.9, t)
    for w_ in ('pena', 'bolinha', 'chave'): z += .06 * kick(f, wt(1, w_) - 2, .6)
    cam = (lerp(621, MX - 60, t), lerp(1150, MY + 60, t), z * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = museu_bg('noite').copy()
    put_estatua(c, EX, EP, EH, f, None)
    al = wt(2, 'alarme') - 3
    if f >= al and (f // 8) % 2 == 0:   # luz vermelha do alarme piscando
        g = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
        d.ellipse((1060, 220, 1160, 320), fill=(230, 60, 60, 255)); d.ellipse((960, 120, 1260, 420), fill=(230, 60, 60, 60))
        c.alpha_composite(g)
    t = smooth(ramp(f, 0, 150))
    cam = (621, lerp(950, 1000, t), lerp(1.12, 1.0, t) * (1 + .0009 * f), 1.5 * math.sin(f * .04)); CAM[2] = cam
    return c, cam, 'sombrio_noite'


def s3(f):
    c = museu_bg('dia').copy()
    put_estatua(c, EX, EP, EH, f, 'chave')
    eu(c, 230, f, expr='preocupado' if f >= wt(3, 'tira') - 3 else 'neutro', look=.75)
    put_menino(c, 1010, 1900, 900, f, expr='neutro', look=-.75, flip=True, seed=5, **GUARDA)
    r = wt(3, 'regra') - 3
    cam = (621, 1120, lerp(1.0, 1.1, smooth(ramp(f, 0, 120))) * (1 + .0009 * f) + .05 * kick(f, r, .6), 0); CAM[3] = cam
    return c, cam, 'vivo'


def s4(f):
    c = museu_bg('tarde').copy()
    put_estatua(c, EX, EP, EH, f, 'bolinha')
    put_menino(c, 1030, 1900, 920, f, expr='sorriso', look=-.75, flip=True, seed=4, **AVO)
    eu(c, 260, f, feet=1900, h=700, expr='sorriso', look=.75)   # o narrador pequeno, na lembrança
    tr = wt(4, 'trinta') - 3
    t = smooth(ramp(f, 0, 150))
    cam = (lerp(700, 621, t), lerp(1150, 1100, t), lerp(1.15, 1.02, t) * (1 + .0009 * f) + .04 * kick(f, tr, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = quarto_bg('tarde').copy()
    co = wt(5, 'conferi') - 3
    if f >= co:   # CLOSE desconfiado
        c = put_close(c, f, expr='desconfiado', look=.5, **EU)
        cam = (621, 1104, lerp(1.2, 1.05, easeOut(ramp(f, co, co + 10))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'tarde'
    eu(c, 560, f, expr='neutro', look=.5)
    ch = wt(5, 'chaveiro') - 3
    s_ = back(ramp(f, ch, ch + 8))
    if s_ > .02:
        o = objeto_img('chaveiro', max(8, int(240 * s_)))
        hx, hy = mao_dir(560, 1900, 900)
        c.alpha_composite(o, (int(hx + 30 - o.width / 2), int(hy - 60 - o.height / 2)))
    t = smooth(ramp(f, 0, co))
    cam = (lerp(621, 680, t), lerp(1150, 1250, t), lerp(1.0, 1.3, t) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = museu_bg('frio').copy()
    ch = wt(6, 'chaveiro') - 3
    put_estatua(c, EX, EP, EH, f, 'chaveiro', back(ramp(f, ch, ch + 6)) if f >= ch else 0)
    fim = wt(6, 'nome') + 6
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.3, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[6] = cam
        return c, cam, 'frio'
    t = smooth(ramp(f, 0, ch + 4))
    cam = (lerp(621, MX - 60, t), lerp(1100, MY + 80, t), lerp(1.0, 1.9, t) * (1 + .0009 * f) + .06 * kick(f, ch + 2, .6),
           2 * math.sin(f * .05) * ramp(f, ch, ch + 10)); CAM[6] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 1', 540, 100, 1, 64, big=True)
            gancho(im, ['A ESTÁTUA ACHOU', 'O MEU CHAVEIRO'], 180, 1, 100)
        else:
            stamp(im, 'NO MUSEU DA MINHA CIDADE', 540, 210, back(ramp(f, CAPA + 2, CAPA + 10)), 60)
            ab = wt(0, 'aberta') - 3
            card(im, 'Estátua de pedra', 'a mão sempre aberta', 330, 420, ramp(f, ab, ab + 10), to_out(0, MX, MY))
    elif si == 1:
        k = wt(1, 'toda') - 3
        stamp(im, 'TODA MANHÃ', 540, 200, back(ramp(f, k, k + 8)), 80)
        cur = None
        for w_, t_ in (('pena', 'UMA PENA'), ('bolinha', 'BOLINHA DE GUDE'), ('chave', 'UMA CHAVE')):
            q = wt(1, w_) - 3
            if f >= q: cur = (t_, q)
        if cur: burst(im, cur[0], 540, 1250, back(ramp(f, cur[1], cur[1] + 8)), 54, rot=-6)
    elif si == 2:
        s6_ = wt(2, 'seis') - 3; n = wt(2, 'ninguem') - 3
        painel(im, 'FECHA ÀS', '18:00', 540, 230, ramp(f, s6_, s6_ + 10), w=400)
        interrog(im, 830, 700, f, ramp(f, n, n + 8))
    elif si == 3:
        r = wt(3, 'regra') - 3; ti = wt(3, 'tira') - 3
        stamp(im, 'A REGRA', 540, 220, back(ramp(f, r, r + 8)), 100, big=True)
        card(im, 'Proibido', 'tirar nada da mão dela', 540, 430, ramp(f, ti, ti + 10))
    elif si == 4:
        tr = wt(4, 'trinta') - 3; rp = wt(4, 'repetiu') - 3
        painel(im, 'MEU AVÔ, GUARDA', '30 ANOS', 540, 230, ramp(f, tr, tr + 10), w=480)
        card(im, 'Nunca repetiu', 'nenhum objeto', 330, 470, ramp(f, rp, rp + 10))
    elif si == 5:
        ch = wt(5, 'chaveiro') - 3; co = wt(5, 'conferi') - 3
        if f < co: card(im, 'Meu chaveiro', 'no meu bolso', 330, 300, ramp(f, ch, ch + 10))
        else: stamp(im, 'NO BOLSO. CERTEZA.', 540, 260, back(ramp(f, co + 2, co + 10)), 70)
    elif si == 6:
        h_ = wt(6, 'hoje') - 3; fim = wt(6, 'nome') + 6; ch = wt(6, 'chaveiro') - 3
        if f < fim:
            stamp(im, 'HOJE CEDO', 540, 180, back(ramp(f, h_, h_ + 8)), 70)
            card(im, 'Na mão dela', 'um chaveiro com o meu nome', 540, 400, ramp(f, ch + 6, ch + 16))
        else: stamp(im, 'O MEU NOME?', 540, 250, back(ramp(f, fim + 4, fim + 12)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
