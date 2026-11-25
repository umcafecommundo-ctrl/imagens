"""Formato MISTÉRIO: "A padaria das três", PARTE 2 (25/11/2026, 12h). História inventada.
Narradora: a mesma da parte 1 (menina de coque castanho, pele morena clara, blusa verde e calça azul).
Resolução: às 3h ela bate na porta e a porta abre sozinha; no forno está o seu Bento, que jurava nunca estar lá; ele diz que
o pão com o rosto dela não é aviso, é convite; há 50 anos apareceu um pão com o rosto dele e desde então é ele quem assa o
pão a mais; a massa escolhe a forma sozinha; ele dá o avental pra ela e vai descansar: a padaria das três agora é dela;
fim: o pão de hoje saiu do forno com formato de guarda-chuva.
Cenários/cores: s0 CAPA close (rua de madrugada) -> porta da padaria às 3h, porta abre com luz (sombrio_noite) |
s1 dentro, forno aceso, seu Bento + CLOSE choque (sombrio_noite) | s2 balcão, pão com o rosto, convite (tarde: luz do forno) |
s3 lembrança de 50 anos atrás, Bento jovem (tarde) | s4 massa mudando de forma no balcão (sombrio_noite) | s5 avental + CLOSE
sorriso (tarde) | s6 manhã clara, pão guarda-chuva + CLOSE final (vivo)."""
from kit import *
import kit
from sombrio import *
from padaria import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'; PITCH = '-4Hz'
EU = dict(penteado='coque', cabelo='#5a3420', pele='#d9a77c', roupa='#3f9e6e', calca='#3d5a80')
BENTO = dict(penteado='careca', velho=True, barba=True, roupa='#f6f2ea', pele='#c98f65', cabelo='#d8d8d8', calca='#2d2f32')
BENTO_JOVEM = dict(penteado='curto', roupa='#f6f2ea', pele='#c98f65', cabelo='#2b1d14', calca='#2d2f32')

LINES = [
    "Às três da manhã, eu bati na porta da padaria. E ela abriu sozinha.",
    "Quem estava no forno era o seu Bento. O mesmo que jurava nunca estar ali de madrugada.",
    "Ele olhou o pão com o meu rosto e sorriu. Isso não é um aviso. É um convite.",
    "Cinquenta anos atrás, apareceu um pão com o rosto dele. Desde então, é ele quem assa o pão a mais.",
    "A massa escolhe a forma sozinha. A gente só põe no forno... e descobre o que o dia vai trazer.",
    "Ele me deu o avental dele. Agora ele vai descansar. E a padaria das três... é minha.",
    "O primeiro pão que eu assei já saiu do forno. E ele tem o formato... de um guarda-chuva.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "VOCÊ ACEITARIA?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 3
FLASH = []
CHECK = [(0, 'bati', 6), (0, 'sozinha', 6), (1, 'bento', 6), (1, 'jurava', 8), (2, 'rosto', 6), (2, 'convite', 8),
         (3, 'cinquenta', 6), (3, 'dele', 6), (4, 'massa', 6), (4, 'forno', 6), (5, 'avental', 6), (5, 'minha', 10),
         (6, 'forno', 6), (6, 'guarda-chuva', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    for k in range(3): s.thunk(s.W(0, 'bati') + k * 7, 60, .45)
    s.whoosh(s.W(0, 'abriu') - 3, .7, .25)
    s.thunk(s.W(1, 'bento') - 2, 80, .5); s.ting(s.W(1, 'jurava'), .3)
    s.ting(s.W(2, 'convite'), .4)
    s.whoosh(s.W(3, 'cinquenta') - 3, .6, .2); s.ting(s.W(3, 'dele'), .3)
    for k in range(4): s.ting(s.W(4, 'massa') + k * 8, .18)
    s.thunk(s.W(4, 'forno') - 2, 70, .5)
    s.ting(s.W(5, 'avental'), .3); s.thunk(s.W(5, 'minha') - 2, 80, .6)
    s.ting(s.W(6, 'forno'), .3); s.patter(s.W(6, 'guarda-chuva') + 6, 1.8, .3)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1960, h=900, avental=False, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))
    if avental:
        a = avental_img().resize((int(230 * h / 900), int(276 * h / 900)), Image.LANCZOS)
        c.alpha_composite(a, (int(x - a.width / 2), int(feet - h * .5)))


def porta_aberta(c, s):
    if s <= 0: return
    d = ImageDraw.Draw(c)
    x0, y0, x1, y1 = 191 + 580, 645 + 420, 191 + 790, 645 + 890
    xm = lerp(x1, x0 + 30, s)
    d.rectangle((x0, y0, xm, y1), fill=(255, 205, 110, 255))
    d.polygon([(xm, y0), (xm + 40, y0 - 20), (xm + 40, y1 + 20), (xm, y1)], fill=(120, 80, 50, 255))
    gl = Image.new('RGBA', c.size, (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
    dg.polygon([(x0, y1), (xm, y1), (xm + 300 * s, 1900), (x0 - 200 * s, 1900)], fill=(255, 200, 100, int(120 * s)))
    c.alpha_composite(gl.filter(ImageFilter.GaussianBlur(20)))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = rua_padaria('noite', True).copy()
        c = put_close(c, f, expr='medo', look=.4, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0012 * f), 0); CAM[0] = cam
        return c, cam, 'tarde'
    g = f - CAPA
    c = rua_padaria('noite', True).copy()
    ab = wt(0, 'abriu') - 3; ba = wt(0, 'bati') - 3
    porta_aberta(c, smooth(ramp(f, ab, ab + 14)))
    eu(c, 560, f, expr='curioso' if f < ab else 'choque', look=.9)
    t = smooth(ramp(g, 0, 60))
    cam = (lerp(660, 720, t), 1400, lerp(1.25, 1.12, easeOut(ramp(g, 0, 18))) * (1 + .0012 * f) + .04 * kick(f, ba, .5) + .06 * kick(f, ab, .6), 0); CAM[0] = cam
    return c, cam, 'tarde'


def s1(f):
    c = interior('noite', True).copy()
    ju = wt(1, 'jurava') - 3; be = wt(1, 'bento') - 3
    if f >= ju:   # CLOSE choque
        c = put_close(c, f, expr='choque', look=.6, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, ju, ju + 10))) * (1 + .0012 * f), 0); CAM[1] = cam
        return c, cam, 'tarde'
    put_menino(c, 870, 2000, 960, f, expr='neutro' if f < be else 'sorriso', look=-.7, flip=True, seed=5, **BENTO)
    eu(c, 300, f, feet=2040, expr='curioso', look=.8)
    t = smooth(ramp(f, 0, ju))
    cam = (lerp(800, 620, t), 1300, lerp(1.3, 1.05, t) * (1 + .0012 * f) + .05 * kick(f, be, .6), 0); CAM[1] = cam
    return c, cam, 'tarde'


def s2(f):
    c = interior('noite', True).copy()
    put_pao(c, 'rosto', 621, 1330, 330)
    vapor(c, 621, 1150, f, .8)
    so = wt(2, 'sorriu') - 3; co = wt(2, 'convite') - 3
    put_menino(c, 1000, 2040, 920, f, expr='neutro' if f < so else 'sorriso', look=-.8, flip=True, seed=5, **BENTO)
    eu(c, 270, f, feet=2060, expr='curioso' if f < co else 'preocupado', look=.8)
    t = smooth(ramp(f, 0, 150))
    cam = (621, lerp(1350, 1300, t), lerp(1.0, 1.1, t) * (1 + .0012 * f) + .05 * kick(f, co, .6), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    c = interior('tarde').copy()
    de = wt(3, 'dele') - 3; ass = wt(3, 'assa') - 3
    put_pao(c, 'rosto', 760, 1330, 320, back(ramp(f, de, de + 8)) if f >= de else 0)
    put_menino(c, 330, 2000, 960, f, expr='curioso' if f < de else 'choque', look=.8, seed=5, **BENTO_JOVEM)
    if f >= ass:
        a = avental_img().resize((260, 312), Image.LANCZOS); c.alpha_composite(a, (330 - 130, 2000 - 480))
    t = smooth(ramp(f, 0, 160))
    cam = (lerp(500, 600, t), 1300, lerp(1.15, 1.05, t) * (1 + .0012 * f) + .05 * kick(f, de, .6), 0); CAM[3] = cam
    return c, cam, 'tarde'


FORMAS = ['comum', 'peixe', 'estrela', 'guarda-chuva', 'rosto', 'comum']


def s4(f):
    c = interior('noite', True).copy()
    ma = wt(4, 'massa') - 3; fo = wt(4, 'forno') - 3
    k = 0 if f < ma else min(4, (f - ma) // 9)
    fm = ['comum', 'peixe', 'estrela', 'guarda', 'comum'][k]
    put_pao(c, fm, 621, 1330, 400, .85 + .15 * back(ramp(f, ma + k * 9, ma + k * 9 + 6)) if f >= ma else 1)
    if f >= fo:
        cam = (870, 1050, 1.5 * (1 + .0012 * f) + .06 * kick(f, fo, .6), 0); CAM[4] = cam
        return c, cam, 'tarde'
    cam = (621, 1230, lerp(1.4, 1.7, smooth(ramp(f, 0, fo))) * (1 + .0012 * f), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = interior('noite', True).copy()
    av = wt(5, 'avental') - 3; mi = wt(5, 'minha') - 3; de = wt(5, 'descansar') - 3
    if f >= mi:   # CLOSE sorriso
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, mi, mi + 10))) * (1 + .0012 * f), 0); CAM[5] = cam
        return c, cam, 'tarde'
    bx = lerp(900, 1300, smooth(ramp(f, de, de + 40))) if f >= de else 900
    put_menino(c, bx, 2000, 960, f, walk=1 if f >= de else 0, expr='sorriso', look=-.7 if f < de else .5, flip=f < de, seed=5, **BENTO)
    eu(c, 420, f, feet=2030, avental=f >= av, expr='curioso' if f < av else 'neutro', look=.8)
    cam = (lerp(620, 560, smooth(ramp(f, 0, mi))), 1320, 1.05 * (1 + .0012 * f) + .05 * kick(f, av, .6), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = interior('dia').copy()
    fo = wt(6, 'forno') - 3; gu = wt(6, 'guarda-chuva') - 3
    fim = gu + 30
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='curioso', look=-.6, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[6] = cam
        return c, cam, 'vivo'
    if f < gu:
        eu(c, 300, f, feet=2040, avental=True, expr='sorriso', look=.8)
        put_pao(c, 'comum', 760, 1330, 330, back(ramp(f, fo, fo + 8)) if f >= fo else 0)
        vapor(c, 760, 1170, f, 1.0 if f >= fo else 0)
        cam = (lerp(560, 650, smooth(ramp(f, 0, gu))), 1300, lerp(1.05, 1.2, smooth(ramp(f, 0, gu))) * (1 + .0012 * f), 0); CAM[6] = cam
    else:
        put_pao(c, 'guarda', 621, 1330, 430, back(ramp(f, gu, gu + 8)))
        vapor(c, 621, 1120, f, 1.0)
        cam = (621, 1180, 1.75 * (1 + .0012 * f) + .08 * kick(f, gu, .8), 0); CAM[6] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['A PORTA ABRIU', 'SOZINHA'], 170, 1, 104)
        else:
            ba = wt(0, 'bati') - 3; ab = wt(0, 'abriu') - 3
            if 45 <= f < 90: stamp(im, 'PARTE 2', 880, 110, back(ramp(f, 45, 52)), 46)
            painel(im, 'AGORA', '03:00', 830, 1250, ramp(f, CAPA + 2, CAPA + 12), w=340)
            if f >= ba and f < ab + 20: burst(im, 'TOC TOC', 250, 430, back(ramp(f, ba, ba + 8)), 60)
    elif si == 1:
        be = wt(1, 'bento') - 3; ju = wt(1, 'jurava') - 3
        if f < ju: card(im, 'Seu Bento', 'no forno, às 3h', 540, 250, ramp(f, be, be + 10))
        else: burst(im, 'ELE?!', 540, 260, back(ramp(f, ju, ju + 8)), 90)
    elif si == 2:
        ro = wt(2, 'rosto') - 3; av = wt(2, 'aviso') - 3; co = wt(2, 'convite') - 3
        if f < co: card(im, 'Não é um aviso', '...', 540, 250, ramp(f, av, av + 10))
        else: stamp(im, 'É UM CONVITE', 540, 250, back(ramp(f, co, co + 8)), 84)
    elif si == 3:
        ci = wt(3, 'cinquenta') - 3; ass = wt(3, 'assa') - 3
        if f < ass: painel(im, 'LEMBRANÇA', '50 ANOS', 540, 260, ramp(f, ci, ci + 10), w=420)
        else: card(im, 'Desde então', 'ele assa o pão a mais', 540, 260, ramp(f, ass, ass + 10))
    elif si == 4:
        ma = wt(4, 'massa') - 3; fo = wt(4, 'forno') - 3
        if f < fo: stamp(im, 'A MASSA ESCOLHE', 540, 230, back(ramp(f, ma, ma + 8)), 74)
        else: burst(im, 'FUUU', 300, 400, back(ramp(f, fo, fo + 8)), 64, cor=(230, 140, 70))
    elif si == 5:
        av = wt(5, 'avental') - 3; mi = wt(5, 'minha') - 3
        if f < mi: card(im, 'O avental', 'do seu Bento', 540, 250, ramp(f, av, av + 10))
        else: stamp(im, 'AGORA É MINHA', 540, 250, back(ramp(f, mi + 2, mi + 10)), 80)
    elif si == 6:
        pr = wt(6, 'primeiro') - 3; gu = wt(6, 'guarda-chuva') - 3; fim = gu + 30
        if f < gu: card(im, 'Meu primeiro', 'pão a mais', 540, 250, ramp(f, pr, pr + 10))
        elif f < fim: burst(im, '?!', 540, 300, back(ramp(f, gu, gu + 6)), 110)
        else: stamp(im, 'VAI CHOVER', 540, 250, back(ramp(f, fim + 2, fim + 10)), 84, rot=3)
    return grao(im.convert('RGB'), lf)
