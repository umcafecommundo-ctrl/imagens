"""Formato MISTÉRIO: "A árvore dos bolinhos", PARTE 2 (25/11/2026, 21h). História inventada.
Narrador: o mesmo da parte 1 (menino de cabelo curto preto, pele morena, camiseta amarela e calça azul).
Resolução: ele bate três vezes e a portinha abre pela primeira vez; dentro não há ninguém, só um fogãozinho aceso e um
caderno com o nome de todo mundo da cidade; na primeira página: plantada há cem anos, no dia em que a cidade nasceu; virada:
o bolinho de vela cem era o aniversário da própria árvore, que ninguém nunca lembrou; ele leva a cidade toda pra cantar
parabéns; as folhas balançam sem vento; no dia seguinte a árvore dá flor pela primeira vez e deixa um bolinho escrito obrigada.
Cenários/cores: s0 CAPA close (floresta de tarde) -> portinha de manhã, abre com luz (frio) | s1 dentro da árvore, fogãozinho
(tarde) | s2 o caderno de perto (tarde) | s3 CLOSE: entendi, floresta de tarde (tarde) | s4 a cidade cantando parabéns
(tarde) | s5 folhas balançando sem vento (tarde) | s6 árvore florida de dia + bolinho obrigada + CLOSE final sorriso (vivo)."""
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
VIZ3 = dict(penteado='coque', cabelo='#d8d8d8', pele='#c98f65', roupa='#8a5ab8', calca='#2d2f32', velho=True)
VIZ4 = dict(penteado='curto', cabelo='#5a3420', pele='#d9a77c', roupa='#3f9e6e', calca='#3d5a80')
PX, PB = 621, 1830

LINES = [
    "Eu bati três vezes na portinha da árvore. E, pela primeira vez, ela abriu.",
    "Lá dentro, não tinha ninguém. Só um fogãozinho aceso e um caderno com o nome de todo mundo da cidade.",
    "Na primeira página, estava escrito: plantada há cem anos, no dia em que a cidade nasceu.",
    "Aí eu entendi. O bolinho com a vela de cem... era o aniversário dela. E ninguém nunca lembrou.",
    "Naquela tarde, eu levei a cidade inteira pra floresta. E todo mundo cantou parabéns pra árvore.",
    "Quando a gente terminou, as folhas balançaram... sem vento nenhum.",
    "No dia seguinte, a árvore deu flor pela primeira vez. E na portinha tinha um bolinho escrito: obrigada.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "VOCÊ CANTARIA?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 3
FLASH = []
CHECK = [(0, 'bati', 6), (0, 'abriu', 6), (1, 'fogaozinho', 6), (1, 'caderno', 6), (2, 'plantada', 6), (2, 'nasceu', 6),
         (3, 'entendi', 6), (3, 'aniversario', 6), (3, 'lembrou', 8), (4, 'cidade', 6), (4, 'parabens', 6),
         (5, 'balancaram', 6), (5, 'vento', 8), (6, 'flor', 6), (6, 'obrigada', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    for k in range(3): s.thunk(s.W(0, 'bati') + k * 7, 60, .45)
    s.whoosh(s.W(0, 'abriu') - 3, .7, .25)
    s.ting(s.W(1, 'fogaozinho'), .25); s.ting(s.W(1, 'caderno'), .3)
    s.ting(s.W(2, 'plantada'), .3); s.thunk(s.W(2, 'nasceu') - 2, 70, .5)
    s.thunk(s.W(3, 'entendi') - 2, 90, .7)
    s.trill(s.W(4, 'parabens'), .3)
    s.whoosh(s.W(5, 'balancaram') - 3, 1.2, .3)
    s.ting(s.W(6, 'flor'), .35); s.ting(s.W(6, 'obrigada'), .4)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=2040, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def brilho(c, x, y, a, r=200):
    if a <= 0: return
    gl = Image.new('RGBA', c.size, (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
    dg.ellipse((x - r, y - r, x + r, y + r), fill=(255, 210, 120, int(150 * a)))
    c.alpha_composite(gl.filter(ImageFilter.GaussianBlur(50)))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = floresta_arvore('tarde', False, True).copy(); brilho(c, PX, PB - 120, 1)
        c = put_close(c, f, expr='choque', look=.4, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0012 * f), 0); CAM[0] = cam
        return c, cam, 'tarde'
    g = f - CAPA
    ab = wt(0, 'abriu') - 3; ba = wt(0, 'bati') - 3
    c = floresta_arvore('frio', False, f >= ab).copy()
    if f >= ab: brilho(c, PX, PB - 120, ramp(f, ab, ab + 10))
    eu(c, 330, f, expr='curioso' if f < ab else 'choque', look=.9)
    t = smooth(ramp(g, 0, 60))
    cam = (lerp(470, 520, t), 1520, lerp(1.4, 1.3, easeOut(ramp(g, 0, 18))) * (1 + .0012 * f) + .04 * kick(f, ba, .5) + .06 * kick(f, ab, .6), 0); CAM[0] = cam
    return c, cam, 'frio'


def s1(f):
    c = dentro_arvore('tarde').copy()
    cd = wt(1, 'caderno') - 3; fo = wt(1, 'fogaozinho') - 3
    c.alpha_composite(caderno_img().resize((300, 368), Image.LANCZOS), (240, 1020))
    eu(c, 690, f, feet=2100, expr='curioso', look=-.6 if f < fo else .8)
    t = smooth(ramp(f, 0, cd))
    cam = (lerp(621, 800, smooth(ramp(f, fo - 10, fo + 10))) if f < cd else lerp(800, 400, smooth(ramp(f, cd, cd + 14))),
           lerp(1300, 1250, t), lerp(1.05, 1.2, t) * (1 + .0012 * f) + .05 * kick(f, cd, .6), 0); CAM[1] = cam
    return c, cam, 'tarde'


def s2(f):
    c = dentro_arvore('tarde').copy()
    c.alpha_composite(caderno_img().resize((700, 860), Image.LANCZOS), (271, 700))
    pl = wt(2, 'plantada') - 3
    t = smooth(ramp(f, 0, 160))
    cam = (621, lerp(1150, 1100, t), lerp(1.3, 1.45, t) * (1 + .0012 * f) + .05 * kick(f, pl, .6), 1.5 * math.sin(f * .05)); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    c = floresta_arvore('tarde').copy()
    put_bolinho(c, PX, PB + 10, 260, vela='100', cor='#f0e2c8')
    an = wt(3, 'aniversario') - 3; le = wt(3, 'lembrou') - 3
    ex = 'curioso' if f < an else ('choque' if f < le else 'preocupado')
    c = put_close(c, f, expr=ex, look=.3 if f < an else 0, **EU)
    en = wt(3, 'entendi') - 3
    cam = (621, 1104, lerp(1.2, 1.05, easeOut(ramp(f, 0, 12))) * (1 + .0012 * f) + .06 * kick(f, an, .6), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = floresta_arvore('tarde').copy()
    ci = wt(4, 'cidade') - 3; pa = wt(4, 'parabens') - 3
    gente = [(170, VIZ3, 7), (380, EU, 2), (900, VIZ, 5), (1090, VIZ2, 8)]
    for i, (x, kw, sd) in enumerate(gente):
        if kw is not EU and f < ci + i * 4: continue
        put_menino(c, x, 2060 + (i % 2) * 30, 860, f, expr='sorriso' if f >= pa else 'curioso', look=(.8 if x < PX else -.8), flip=x > PX, seed=sd, **kw)
    put_menino(c, 640, 2160, 820, f, expr='sorriso' if f >= pa else 'curioso', look=0, seed=9, **VIZ4) if f >= ci + 10 else None
    t = smooth(ramp(f, 0, 150))
    cam = (621, lerp(1350, 1300, t), lerp(1.0, 1.08, t) * (1 + .0012 * f) + .05 * kick(f, pa, .6), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = floresta_arvore('tarde').copy()
    ba = wt(5, 'balancaram') - 3
    k = ramp(f, ba, ba + 6)
    if k > 0:
        tr = arvore_img(False, False, False)
        sway = 3.2 * math.sin(f * .45) * k
        top = tr.crop((0, 0, 1100, 760)).rotate(sway, Image.BICUBIC, center=(550, 760))
        c.alpha_composite(top, (621 - 550, 1830 - 1600))
        rnd = random.Random(f // 3)
        d = ImageDraw.Draw(c)
        for i in range(14):
            x = rnd.randint(100, 1150); y = rnd.randint(300, 1700)
            d.ellipse((x - 16, y - 9, x + 16, y + 9), fill=(80, 150, 70, 255), outline=(36, 30, 38, 255), width=3)
    cam = (621, lerp(900, 1000, smooth(ramp(f, 0, 100))), 1.15 * (1 + .0012 * f) + .04 * kick(f, ba, .6), 1.5 * math.sin(f * .3) * k); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    fl = wt(6, 'flor') - 3; ob = wt(6, 'obrigada') - 3
    fim = ob + 30
    c = floresta_arvore('dia', f >= fl).copy()
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[6] = cam
        return c, cam, 'vivo'
    po = wt(6, 'portinha') - 3
    if f < po:
        eu(c, 300, f, expr='curioso' if f < fl else 'sorriso', look=.9)
        cam = (621, lerp(800, 1100, smooth(ramp(f, 0, po))), lerp(1.0, 1.05, smooth(ramp(f, 0, po))) * (1 + .0012 * f) + .06 * kick(f, fl, .6), 0); CAM[6] = cam
    else:
        put_bolinho(c, PX, PB + 10, 240, back(ramp(f, po, po + 8)), nome='OBRIGADA' if f >= ob else None, cor='#f6a6c1')
        cam = (PX, 1690, 2.2 * (1 + .0012 * f) + .06 * kick(f, ob, .6), 0); CAM[6] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['O QUE TINHA', 'DENTRO DA ÁRVORE'], 170, 1, 100)
        else:
            ba = wt(0, 'bati') - 3; ab = wt(0, 'abriu') - 3
            if 45 <= f < 90: stamp(im, 'PARTE 2', 880, 110, back(ramp(f, 45, 52)), 46)
            if f < ab: burst(im, 'TOC TOC TOC', 540, 330, back(ramp(f, ba, ba + 8)) if f >= ba else 0, 58)
            else: stamp(im, 'ABRIU', 540, 330, back(ramp(f, ab, ab + 8)), 96, big=True)
    elif si == 1:
        ni = wt(1, 'ninguem') - 3; cd = wt(1, 'caderno') - 3
        if f < cd: interrog(im, 540, 260, f, ramp(f, ni, ni + 8))
        else: card(im, 'Um caderno', 'com o nome de todo mundo', 540, 250, ramp(f, cd, cd + 10))
    elif si == 2:
        pl = wt(2, 'plantada') - 3; na = wt(2, 'nasceu') - 3
        card(im, 'Plantada há 100 anos', 'no dia em que a cidade nasceu' if f >= na else '...', 540, 240, ramp(f, pl, pl + 10))
    elif si == 3:
        an = wt(3, 'aniversario') - 3; le = wt(3, 'lembrou') - 3
        if f < le: stamp(im, 'O ANIVERSÁRIO DELA', 540, 250, back(ramp(f, an, an + 8)), 66)
        else: painel(im, 'LEMBRARAM', '0 VEZES', 540, 260, ramp(f, le, le + 10), w=420)
    elif si == 4:
        ci = wt(4, 'cidade') - 3; pa = wt(4, 'parabens') - 3
        if f < pa: stamp(im, 'A CIDADE INTEIRA', 540, 230, back(ramp(f, ci, ci + 8)), 70)
        else: burst(im, 'PARABÉNS!', 540, 300, back(ramp(f, pa, pa + 8)), 70, cor=(240, 170, 90))
    elif si == 5:
        ba = wt(5, 'balancaram') - 3; ve = wt(5, 'vento') - 3
        if f < ve: burst(im, 'FSSSH', 760, 1150, back(ramp(f, ba, ba + 8)) if f >= ba else 0, 60, cor=(120, 190, 120))
        else: card(im, 'Sem vento', 'nenhum', 540, 1150, ramp(f, ve, ve + 10))
    elif si == 6:
        fl = wt(6, 'flor') - 3; ob = wt(6, 'obrigada') - 3; fim = ob + 30; po = wt(6, 'portinha') - 3
        if f < po: stamp(im, 'PRIMEIRA FLOR', 540, 1250, back(ramp(f, fl, fl + 8)), 72)
        elif f < fim: card(im, 'Na portinha', 'um bolinho', 540, 250, ramp(f, po, po + 10))
        else: stamp(im, 'OBRIGADA', 540, 250, back(ramp(f, fim + 2, fim + 10)), 90, rot=3)
    return grao(im.convert('RGB'), lf)
