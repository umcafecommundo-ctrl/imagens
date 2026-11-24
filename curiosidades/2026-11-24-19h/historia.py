"""Formato MISTÉRIO: "O boneco de neve que anda", PARTE 1 (24/11/2026, 19h). História inventada.
Narradora: menina de cabelo ruivo comprido, pele clara, casaco azul e calça escura (mesmas cores na parte 2).
Premissa: na vila da serra só neva uma noite por ano e na manhã seguinte sempre há um boneco de neve na praça (cachecol
vermelho, nariz de cenoura); ninguém vê quem faz; regra: ninguém derruba o boneco, ele derrete sozinho em sete dias;
toda noite ele amanhece alguns passos mais perto de uma casa; onde ele para, alguém acha um presente de lã na porta
(ano passado, na padaria); este ano ela marcou na neve onde ele estava e ele vinha pra rua dela; hoje cedo ele está
parado no portão dela, de costas, olhando pro alto do morro.
Cenários/cores: s0 CAPA close (vila de dia) -> praça de dia com neve caindo (vivo) | s1 o boneco de perto, manhã (frio) |
s2 a regra, vila de dia (vivo) | s3 noite, o boneco andando com pegadas (sombrio_noite) | s4 lembrança: presente na
padaria (tarde) | s5 marcação na neve + CLOSE (frio) | s6 portão de manhã, de costas pro morro + CLOSE final (frio)."""
from kit import *
import kit
from sombrio import *
from neve_vila import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='longo', cabelo='#c0622f', pele='#e6c8ad', roupa='#3a7bd5', calca='#2d2f32')
VIZ = dict(penteado='careca', cabelo='#3a2a22', pele='#8a5a3a', roupa='#5a9a6a', calca='#2d2f32', barba=True)

LINES = [
    "Na minha vila, na serra, só neva uma noite por ano. E na manhã seguinte, tem um boneco de neve na praça.",
    "Ninguém vê quem faz. Ele tem um cachecol vermelho e um nariz de cenoura.",
    "A regra da vila é uma só: ninguém derruba o boneco. Ele derrete sozinho em sete dias.",
    "Mas toda noite, ele amanhece alguns passos mais perto de uma casa.",
    "Onde ele para, alguém acha um presente de lã na porta. Ano passado, foi na padaria.",
    "Este ano, eu marquei na neve onde ele estava. E ele vinha na direção da minha rua.",
    "Hoje cedo, ele estava parado no meu portão. Mas de costas... olhando pro alto do morro.",
]
FALA_TIKTOK = "Comenta QUERO pra parte dois."
CTA_TEXTO = "COMENTA QUERO"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'neva', 6), (0, 'boneco', 6), (1, 'ninguem', 6), (1, 'cachecol', 6), (2, 'regra', 4), (2, 'sete', 6),
         (3, 'passos', 6), (4, 'presente', 6), (4, 'padaria', 6), (5, 'marquei', 6), (5, 'rua', 8), (6, 'portao', 6),
         (6, 'costas', 6), (6, 'morro', 10)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    s.ting(s.W(0, 'neva'), .25); s.thunk(s.W(0, 'boneco') - 2, 80, .5)
    s.ting(s.W(1, 'cachecol'), .3)
    s.thunk(s.W(2, 'regra') - 2, 90, .7); s.ting(s.W(2, 'sete'), .25)
    for k in range(4): s.thunk(s.W(3, 'passos') + k * 9, 40, .35)
    s.ting(s.W(4, 'presente'), .35)
    s.whoosh(s.W(5, 'marquei') - 3, .6, .2); s.ting(s.W(5, 'rua'), .3)
    s.thunk(s.W(6, 'portao') - 2, 90, .6); s.thunk(s.W(6, 'morro') + 6, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def presente(c, x, base, s=1.0):
    if s <= .03: return
    p = Pen(300, 300)
    p.shape([(30, 290), (30, 120), (270, 120), (270, 290)], hexc('#f4d35e'), hexc('#c9a73a'), 6, 0)
    p.shape([(130, 120), (170, 120), (170, 290), (130, 290)], hexc('#d8423a'), None, 4, 0)
    p.shape(ell_pts(115, 95, 50, 30, 24), hexc('#d8423a'), None, 4, 0); p.shape(ell_pts(185, 95, 50, 30, 24), hexc('#d8423a'), None, 4, 0)
    im = p.img.resize((max(4, int(300 * s)), max(4, int(300 * s))), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height)))


def porta_padaria(c, x, base):
    p = Pen(460, 760)
    p.shape([(20, 740), (20, 60), (440, 60), (440, 740)], hexc('#e9b48a'), hexc('#c9946a'), 6, 0)
    p.shape([(140, 740), (140, 320), (320, 320), (320, 740)], hexc('#8a5a38'), None, 6, 0)
    p.shape([(40, 90), (420, 90), (420, 230), (40, 230)], hexc('#f6efd9'), None, 5, 0)
    im = p.img.resize((460, 760), Image.LANCZOS)
    d = ImageDraw.Draw(im); fnt = font(F_STAMP, 70); tw = d.textlength('PADARIA', font=fnt)
    d.text((230 - tw / 2, 118), 'PADARIA', font=fnt, fill=(150, 70, 50))
    c.alpha_composite(im, (int(x - 230), int(base - 760)))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = vila_bg('dia').copy(); put_boneco(c, 780, 1700, 700); flocos(c, f)
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    c = vila_bg('dia').copy()
    b = wt(0, 'boneco') - 3
    put_boneco(c, 800, 1700, 700, s=back(ramp(f, b, b + 8)) if f >= b else 0)
    eu(c, 280, f, expr='neutro' if f < b else 'preocupado', look=.75)
    flocos(c, f, 160, 4)
    t = smooth(ramp(g, 0, 120))
    cam = (lerp(560, 640, t), lerp(1250, 1130, t), lerp(1.3, 1.02, easeOut(ramp(g, 0, 18))) * (1 + .0009 * f) + .05 * kick(f, b, .6), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = vila_bg('frio').copy()
    put_boneco(c, 621, 1750, 760, look=math.sin(f * .05))
    flocos(c, f, 80, 3)
    ca = wt(1, 'cachecol') - 3
    t = smooth(ramp(f, 0, ca + 8))
    cam = (621, lerp(1300, 1250, t), lerp(1.05, 1.6, t) * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'frio'


def s2(f):
    c = vila_bg('dia').copy()
    put_boneco(c, 640, 1700, 700)
    eu(c, 260, f, expr='neutro', look=.75)
    put_menino(c, 990, 1900, 900, f, expr='preocupado' if f >= wt(2, 'derruba') - 3 else 'neutro', look=-.75, flip=True, seed=5, **VIZ)
    r = wt(2, 'regra') - 3
    cam = (621, 1150, lerp(1.0, 1.1, smooth(ramp(f, 0, 120))) * (1 + .0009 * f) + .05 * kick(f, r, .6), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = vila_bg('noite').copy()
    t = smooth(ramp(f, 10, 110))
    x = lerp(300, 900, t)
    pegadas(c, [(xx, 1800 + 14 * ((i % 2) * 2 - 1)) for i, xx in enumerate(range(250, int(x) - 120, 70))])
    put_boneco(c, x, 1800, 700, look=1)
    flocos(c, f, 100, 3)
    cam = (lerp(450, 800, t), 1250, 1.15 * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'sombrio_noite'


def s4(f):
    c = vila_bg('tarde').copy()
    porta_padaria(c, 760, 1700)
    put_boneco(c, 330, 1760, 680, look=1)
    pr = wt(4, 'presente') - 3
    presente(c, 760, 1760, back(ramp(f, pr, pr + 8)) * .9 if f >= pr else 0)
    t = smooth(ramp(f, 0, 160))
    cam = (lerp(560, 640, t), lerp(1200, 1300, t), lerp(1.02, 1.15, t) * (1 + .0009 * f) + .04 * kick(f, pr, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = vila_bg('frio').copy()
    ru = wt(5, 'rua') - 3
    if f >= ru + 4:   # CLOSE preocupado
        c = put_close(c, f, expr='preocupado', look=.5, **EU)
        cam = (621, 1104, lerp(1.2, 1.05, easeOut(ramp(f, ru + 4, ru + 12))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'frio'
    put_boneco(c, 960, 1700, 560)
    ma = wt(5, 'marquei') - 3
    k = ramp(f, ma, ma + 20)
    if k > 0:
        d = ImageDraw.Draw(c)
        d.line((440, 1850, lerp(440, 860, k), lerp(1850, 1730, k)), fill=(120, 132, 150, 255), width=12)
        if k >= 1: d.polygon([(890, 1722), (840, 1712), (855, 1765)], fill=(120, 132, 150, 255))
    eu(c, 300, f, expr='neutro', look=.75)
    t = smooth(ramp(f, 0, ru))
    cam = (lerp(560, 680, t), lerp(1250, 1350, t), lerp(1.0, 1.15, t) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'frio'


def s6(f):
    c = vila_bg('frio', True).copy()
    po = wt(6, 'portao') - 3; co = wt(6, 'costas') - 3
    portao(c, 621, 1900, 1.3)
    put_boneco(c, 621, 1840, 760, costas=f >= co)
    fim = wt(6, 'morro') + 6
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.3, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[6] = cam
        return c, cam, 'frio'
    al = wt(6, 'alto') - 3
    t = smooth(ramp(f, 0, po + 6)); t2 = smooth(ramp(f, al - 6, al + 14))
    cam = (lerp(621, 900, t2), lerp(lerp(1150, 1400, t), 800, t2), lerp(lerp(1.0, 1.15, t), 1.5, t2) * (1 + .0009 * f) + .05 * kick(f, co, .6),
           2 * math.sin(f * .05) * ramp(f, co, co + 10)); CAM[6] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 1', 540, 100, 1, 64, big=True)
            gancho(im, ['O BONECO DE NEVE', 'ANDA SOZINHO'], 180, 1, 100)
        else:
            stamp(im, 'NA MINHA VILA', 540, 210, back(ramp(f, CAPA + 2, CAPA + 10)), 72)
            n = wt(0, 'neva') - 3
            painel(im, 'NEVE POR ANO', '1 NOITE', 540, 450, ramp(f, n, n + 10), w=460)
    elif si == 1:
        n = wt(1, 'ninguem') - 3; ca = wt(1, 'cachecol') - 3
        if f < ca: interrog(im, 540, 260, f, ramp(f, n, n + 8))
        else: card(im, 'Cachecol vermelho', 'nariz de cenoura', 540, 260, ramp(f, ca, ca + 10))
    elif si == 2:
        r = wt(2, 'regra') - 3; de = wt(2, 'derruba') - 3; se = wt(2, 'sete') - 3
        stamp(im, 'A REGRA', 540, 200, back(ramp(f, r, r + 8)), 100, big=True)
        if f < se: card(im, 'Proibido', 'derrubar o boneco', 540, 420, ramp(f, de, de + 10))
        else: painel(im, 'DERRETE EM', '7 DIAS', 540, 430, ramp(f, se, se + 10), w=400)
    elif si == 3:
        to = wt(3, 'toda') - 3; pa = wt(3, 'passos') - 3
        stamp(im, 'TODA NOITE', 540, 220, back(ramp(f, to, to + 8)), 80)
        burst(im, 'TUM TUM', 800, 430, back(ramp(f, pa, pa + 8)) if f >= pa else 0, 54)
    elif si == 4:
        pr = wt(4, 'presente') - 3; pd = wt(4, 'padaria') - 3
        card(im, 'Presente de lã', 'na porta de alguém', 540, 260, ramp(f, pr, pr + 10))
        stamp(im, 'ANO PASSADO', 540, 470, back(ramp(f, pd - 6, pd + 2)) if f >= pd - 6 else 0, 64)
    elif si == 5:
        ma = wt(5, 'marquei') - 3; ru = wt(5, 'rua') - 3
        if f < ru + 4: card(im, 'Marquei na neve', 'pra onde ele vai', 540, 300, ramp(f, ma, ma + 10))
        else: stamp(im, 'PRA MINHA RUA', 540, 250, back(ramp(f, ru + 6, ru + 14)), 76)
    elif si == 6:
        h_ = wt(6, 'hoje') - 3; fim = wt(6, 'morro') + 6; co = wt(6, 'costas') - 3
        if f < co: stamp(im, 'NO MEU PORTÃO', 540, 200, back(ramp(f, h_, h_ + 8)), 70)
        elif f < fim: burst(im, 'DE COSTAS', 300, 330, back(ramp(f, co, co + 8)), 56)
        else: stamp(im, 'O QUE TEM LÁ?', 540, 250, back(ramp(f, fim + 4, fim + 12)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
