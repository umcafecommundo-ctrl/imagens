"""Formato MISTÉRIO: "A padaria das três", PARTE 1 (25/11/2026, 07h). História inventada.
Narradora: menina de coque castanho, pele morena clara, blusa verde e calça azul (mesmas cores na parte 2).
Premissa: a padaria da rua fecha às 19h, mas toda madrugada às 3h a luz acende e sai cheiro de pão; regra da rua: ninguém
bate na porta às três; de manhã o seu Bento (padeiro) jura que não estava lá, mas sempre há um pão a mais no balcão; o pão
a mais tem formato de algo que vai acontecer (guarda-chuva = chuva à tarde; peixe = rio encheu; estrela = faltou luz);
hoje cedo o pão a mais tinha o formato do rosto da narradora.
Cenários/cores: s0 CAPA close (rua de dia) -> padaria de dia (vivo) e de madrugada acesa (sombrio_noite) | s1 rua à noite,
padaria acesa, vapor (sombrio_noite) | s2 dentro da padaria de manhã, seu Bento (vivo) | s3 balcão, pão guarda-chuva ->
rua de tarde com chuva + CLOSE curioso (tarde) | s4 balcão à tarde: peixe, estrela, apagão (tarde) | s5 rua de manhã fria,
andando (frio) | s6 balcão de manhã, pão com o rosto + CLOSE final (frio)."""
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

LINES = [
    "Na minha rua, a padaria fecha às sete da noite. Mas toda madrugada, às três, a luz acende sozinha.",
    "Sai cheiro de pão quente. E a regra da rua é uma só: ninguém bate na porta às três.",
    "De manhã, o seu Bento, o padeiro, jura que não estava lá. Mas sempre tem um pão a mais no balcão.",
    "E o pão a mais tem formato de alguma coisa. Quando é um guarda-chuva... chove à tarde.",
    "Já veio um peixe, e o rio encheu. Veio uma estrela, e faltou luz na rua toda.",
    "Eu nunca acreditei. Até hoje cedo, quando eu fui comprar pão.",
    "O pão a mais estava lá, ainda quente. E ele tinha o formato... do meu rosto.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "EU BATO NA PORTA?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'sete', 4), (0, 'tres', 6), (1, 'regra', 4), (1, 'porta', 6), (2, 'bento', 6), (2, 'balcao', 6),
         (3, 'guarda-chuva', 6), (3, 'chove', 8), (4, 'peixe', 6), (4, 'estrela', 6), (4, 'luz', 8), (5, 'cedo', 6),
         (6, 'quente', 6), (6, 'rosto', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.whoosh(2, .5, .15)
    s.ting(s.W(0, 'tres'), .3); s.thunk(s.W(0, 'acende') - 2, 80, .5)
    s.thunk(s.W(1, 'regra') - 2, 90, .7)
    for k in range(3): s.thunk(s.W(1, 'porta') + k * 7, 50, .35)
    s.ting(s.W(2, 'balcao'), .35)
    s.ting(s.W(3, 'guarda-chuva'), .3); s.patter(s.W(3, 'chove') - 2, 2.2, .35)
    s.ting(s.W(4, 'peixe'), .3); s.splash(s.W(4, 'rio'), .35); s.ting(s.W(4, 'estrela'), .3); s.thunk(s.W(4, 'luz') - 2, 70, .6)
    s.whoosh(s.W(5, 'cedo') - 3, .6, .2)
    s.ting(s.W(6, 'quente'), .3); s.thunk(s.W(6, 'rosto') + 4, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1960, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def chuva(c, f, dens=1.0):
    d = ImageDraw.Draw(c); rnd = random.Random(11)
    for i in range(int(140 * dens)):
        x = rnd.randint(-100, W_ + 100); y0 = rnd.randint(0, H_)
        y = (y0 + f * 60) % (H_ + 200) - 100; x2 = x - ((f * 18) % 1)
        d.line((x2, y, x2 - 18, y + 70), fill=(200, 215, 235, 190), width=5)


def escuro(c, a):
    if a <= 0: return c
    c.alpha_composite(Image.new('RGBA', c.size, (6, 8, 16, int(200 * a)))); return c


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = rua_padaria('dia').copy()
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0012 * f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    md = wt(0, 'madrugada') - 3
    if f < md:
        c = rua_padaria('dia').copy()
        eu(c, 230, f, expr='neutro', look=.75)
        t = smooth(ramp(g, 0, md - CAPA))
        cam = (lerp(560, 660, t), lerp(1280, 1180, t), lerp(1.25, 1.02, easeOut(ramp(g, 0, 18))) * (1 + .0012 * f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    ac = wt(0, 'acende') - 3
    c = rua_padaria('noite', f >= ac).copy()
    t = smooth(ramp(f, md, md + 60))
    cam = (lerp(640, 690, t), lerp(1150, 1150, t), lerp(1.0, 1.15, t) * (1 + .0012 * f) + .06 * kick(f, ac, .6), 0); CAM[0] = cam
    return c, cam, 'sombrio_noite'


def s1(f):
    c = rua_padaria('noite', True).copy()
    vapor(c, 700, 640, f, 1.0)
    vapor(c, 380, 640, f + 40, .8)
    po = wt(1, 'porta') - 3
    t = smooth(ramp(f, 0, po))
    cam = (lerp(560, 900, t), lerp(1100, 1330, t), lerp(1.0, 1.5, t) * (1 + .0012 * f) + .05 * kick(f, po, .6),
           2 * math.sin(f * .07) * ramp(f, po, po + 10)); CAM[1] = cam
    return c, cam, 'sombrio_noite'


def s2(f):
    c = interior('dia').copy()
    ba = wt(2, 'balcao') - 3; ma = wt(2, 'mais') - 3
    put_pao(c, 'comum', 760, 1320, 300, back(ramp(f, ma, ma + 8)) if f >= ma else 0)
    ju = wt(2, 'jura') - 3
    put_menino(c, 330, 2000, 960, f, expr='sorriso' if f < ju else 'desconfiado', look=.6, seed=5, **BENTO)
    t = smooth(ramp(f, 0, ma))
    cam = (lerp(420, 560, t), lerp(1250, 1250, t), lerp(1.25, 1.12, t) * (1 + .0012 * f) + .05 * kick(f, ba, .6), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    ch = wt(3, 'chove') - 3
    if f < ch:
        c = interior('dia').copy()
        gu = wt(3, 'guarda-chuva') - 3
        put_pao(c, 'comum' if f < gu else 'guarda', 621, 1320, 380, 1.0 if f < gu else back(ramp(f, gu, gu + 8)))
        cam = (621, 1220, lerp(1.6, 1.9, smooth(ramp(f, 0, ch))) * (1 + .0012 * f) + .06 * kick(f, gu, .6), 0); CAM[3] = cam
        return c, cam, 'vivo'
    c = rua(f, 300 + f * 2, luz='tarde', neb=0)
    eu(c, 621, f, expr='curioso', look=-.5)
    chuva(c, f)
    if f >= ch + 18:   # CLOSE curioso
        c = put_close(c, f, expr='curioso', look=-.5, **EU)
        chuva(c, f, .6)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, ch + 18, ch + 26))) * (1 + .0012 * f), 0); CAM[3] = cam
        return c, cam, 'tarde'
    cam = (621, 1300, lerp(1.3, 1.1, easeOut(ramp(f, ch, ch + 12))) * (1 + .0012 * f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = interior('tarde').copy()
    pe = wt(4, 'peixe') - 3; es = wt(4, 'estrela') - 3; lu = wt(4, 'luz') - 3
    if f < es:
        put_pao(c, 'peixe', 621, 1320, 380, back(ramp(f, pe, pe + 8)) if f >= pe else 0)
        put_pao(c, 'comum', 300, 1320, 260); put_pao(c, 'comum', 950, 1320, 260)
    else:
        put_pao(c, 'estrela', 621, 1320, 400, back(ramp(f, es, es + 8)))
        put_pao(c, 'comum', 300, 1320, 260); put_pao(c, 'comum', 950, 1320, 260)
    if f >= lu: c = escuro(c, .75 * ramp(f, lu, lu + 3))
    cam = (621, 1200, (1.45 if f < es else 1.6) * (1 + .0012 * f) + .06 * kick(f, pe, .6) + .06 * kick(f, es, .6) + .05 * kick(f, lu, .6), 0); CAM[4] = cam
    return c, cam, 'tarde' if f < lu else 'sombrio_noite'


def s5(f):
    ce = wt(5, 'cedo') - 3
    if f < ce:
        c = quarto_bg('dia').copy() if False else rua(f, f * 9, luz='dia', neb=0)
        eu(c, 621, f, walk=1, expr='neutro', look=.4)
        cam = (621, 1300, 1.12 * (1 + .0012 * f), 0); CAM[5] = cam
        return c, cam, 'frio'
    c = rua_padaria('dia').copy()
    eu(c, 400, f, walk=0, expr='neutro', look=.8)
    co = wt(5, 'comprar') - 3
    if f >= co:   # CLOSE curioso olhando a padaria
        c = put_close(c, f, expr='curioso', look=.8, **EU)
        cam = (621, 1104, lerp(1.2, 1.05, easeOut(ramp(f, co, co + 10))) * (1 + .0012 * f), 0); CAM[5] = cam
        return c, cam, 'frio'
    cam = (lerp(520, 700, smooth(ramp(f, ce, co))), 1250, 1.05 * (1 + .0012 * f) + .05 * kick(f, ce, .6), 0); CAM[5] = cam
    return c, cam, 'frio'


def s6(f):
    c = interior('frio').copy()
    ro = wt(6, 'rosto') - 3; fo = wt(6, 'formato') - 3
    fim = ro + 16
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.3, suor=1, shake=.3, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[6] = cam
        return c, cam, 'frio'
    vapor(c, 621, 1180, f, 1.0)
    if f < ro:
        put_pao(c, 'comum', 621, 1320, 340)
        put_pao(c, 'comum', 300, 1320, 240); put_pao(c, 'comum', 950, 1320, 240)
        t = smooth(ramp(f, 0, ro))
        cam = (621, lerp(1150, 1220, t), lerp(1.2, 1.7, t) * (1 + .0012 * f), 2 * math.sin(f * .05) * ramp(f, fo, fo + 10)); CAM[6] = cam
    else:
        put_pao(c, 'rosto', 621, 1330, 430, back(ramp(f, ro, ro + 8)))
        cam = (621, 1180, 1.75 * (1 + .0012 * f) + .08 * kick(f, ro, .8), 3 * math.sin(f * .4) * (1 - ramp(f, ro, ro + 12))); CAM[6] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            gancho(im, ['O PÃO TINHA', 'O MEU ROSTO'], 170, 1, 104)
            stamp(im, 'PARTE 1', 880, 1240, 1, 46)
        else:
            md = wt(0, 'madrugada') - 3; tr = wt(0, 'tres') - 3
            if f < md:
                stamp(im, 'NA MINHA RUA', 540, 200, back(ramp(f, CAPA + 2, CAPA + 10)), 72)
                se = wt(0, 'sete') - 3
                painel(im, 'FECHA ÀS', '19:00', 800, 1180, ramp(f, se, se + 10), w=340)
            else:
                painel(im, 'LUZ ACESA', '03:00', 540, 300, ramp(f, tr, tr + 10), glitch=.3, w=420)
    elif si == 1:
        ch = wt(1, 'cheiro') - 3; r = wt(1, 'regra') - 3; po = wt(1, 'porta') - 3
        if f < r: burst(im, 'HMMM', 760, 300, back(ramp(f, ch, ch + 8)) if f >= ch else 0, 60, cor=(230, 170, 90))
        else:
            stamp(im, 'A REGRA', 540, 480, back(ramp(f, r, r + 8)), 100, big=True)
            card(im, 'Ninguém bate', 'na porta às 3h', 540, 700, ramp(f, po - 8, po + 2))
    elif si == 2:
        b = wt(2, 'bento') - 3; ju = wt(2, 'jura') - 3; ma = wt(2, 'mais') - 3
        if f < ma:
            card(im, 'Seu Bento', 'o padeiro', 540, 230, ramp(f, b, b + 10))
            if f >= ju: burst(im, 'NÃO FUI EU', 760, 440, back(ramp(f, ju, ju + 8)), 50)
        else:
            stamp(im, '1 PÃO A MAIS', 540, 230, back(ramp(f, ma, ma + 8)), 80)
    elif si == 3:
        fo = wt(3, 'formato') - 3; gu = wt(3, 'guarda-chuva') - 3; ch = wt(3, 'chove') - 3
        if f < gu: interrog(im, 540, 260, f, ramp(f, fo, fo + 8))
        elif f < ch: card(im, 'Guarda-chuva', 'de pão', 540, 260, ramp(f, gu, gu + 10))
        elif f < ch + 18: burst(im, 'PLIC PLOC', 540, 300, back(ramp(f, ch, ch + 8)), 60, cor=(110, 150, 210))
        else: stamp(im, 'CHOVEU', 540, 260, back(ramp(f, ch + 18, ch + 26)), 84)
    elif si == 4:
        pe = wt(4, 'peixe') - 3; es = wt(4, 'estrela') - 3; ri = wt(4, 'rio') - 3; lu = wt(4, 'luz') - 3
        if f < es:
            card(im, 'Pão de peixe', 'o rio encheu' if f >= ri else '...', 540, 260, ramp(f, pe, pe + 10))
        elif f < lu:
            card(im, 'Pão de estrela', '...', 540, 260, ramp(f, es, es + 10))
        else:
            stamp(im, 'APAGÃO', 540, 280, back(ramp(f, lu, lu + 8)), 96, big=True)
    elif si == 5:
        nu = wt(5, 'nunca') - 3; ce = wt(5, 'cedo') - 3
        if f < ce: card(im, 'Eu nunca', 'acreditei', 540, 250, ramp(f, nu, nu + 10))
        else: painel(im, 'HOJE', '06:40', 800, 1180, ramp(f, ce, ce + 10), w=360)
    elif si == 6:
        q = wt(6, 'quente') - 3; ro = wt(6, 'rosto') - 3; fim = ro + 16
        if f < ro: card(im, 'O pão a mais', 'ainda quente', 540, 250, ramp(f, q, q + 10))
        elif f < fim: burst(im, '?!', 540, 300, back(ramp(f, ro, ro + 6)), 110)
        else: stamp(im, 'É O MEU ROSTO', 540, 250, back(ramp(f, fim + 2, fim + 10)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
