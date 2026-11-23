"""Formato MISTÉRIO: "As batidas das três", PARTE 2 (23/11/2026, 21h). História inventada.
Narrador: o mesmo da parte 1 (menino ruivo, cabelo curto, pele clara, macacão azul).
Resolução: depois que ele bate de volta, uma luz azul acende do outro lado do vidro: é um robozinho laranja grudado no casco,
com a antena torta; no caderno da avó (que construiu a estação) está o desenho dele: Pipo; toda noite às três ele batia três
vezes para dizer "tudo bem aqui fora"; quatro batidas = socorro; virada: a placa era da avó, para ninguém responder no lugar
dela; mas ela voltou pra Terra e ninguém mais respondia; fim: a engenheira conserta a antena e toda noite, às três, ele bate
três vezes de volta.
Cenários/cores: s0 CAPA close (cabine à noite) -> cabine à noite (sombrio_noite) | s1 janelinha, luz azul (sombrio_noite) |
s2 lado de fora, robô no casco (frio) | s3 cabine de dia, caderno da avó (vivo) | s4 lembrança, robô bate 3x (tarde) |
s5 robô com antena torta, 4 batidas + CLOSE (frio) | s6 corredor de dia, placa e a Terra na janela (vivo) |
s7 antena consertada, ele bate de volta + CLOSE final (vivo -> sombrio_noite)."""
from kit import *
import kit
from sombrio import *
from estacao3 import *
from farol import caderno
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#b5532a', pele='#f0c8a8', roupa='#4a78c8', calca='#2e4a80')
AZUL = (140, 230, 255)

LINES = [
    "Na parte um, alguém bateu quatro vezes na janelinha do meu quarto, no espaço. E eu bati de volta.",
    "Do outro lado do vidro, uma luz azul se acendeu.",
    "Era um robozinho laranja, grudado no casco da estação. Com a antena torta.",
    "No caderno da minha avó, que construiu a estação, achei o desenho dele: Pipo.",
    "Toda noite, às três, ele batia três vezes. Era o jeito dele dizer: tudo bem aqui fora.",
    "Quatro batidas queriam dizer outra coisa: socorro.",
    "A placa era da minha avó, pra ninguém responder no lugar dela. Mas ela voltou pra Terra.",
    "Hoje, a engenheira consertou a antena do Pipo. E toda noite, às três, eu bato três vezes de volta.",
]
FALA_TIKTOK = "Você responderia as batidas? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'quatro', 6), (0, 'volta', 6), (1, 'azul', 6), (2, 'robozinho', 6), (2, 'torta', 6), (3, 'caderno', 6),
         (3, 'pipo', 8), (4, 'tres', 6), (4, 'fora', 6), (5, 'quatro', 6), (5, 'socorro', 10), (6, 'placa', 6),
         (6, 'terra', 6), (7, 'antena', 6), (7, 'bato', 6), (7, 'volta', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.thunk(2, 120, .6)
    s.thunk(s.W(0, 'bati') - 1, 180, .8)
    s.ting(s.W(1, 'azul'), .3)
    s.whoosh(s.W(2, 'era') - 4, .8, .3); s.trill(s.W(2, 'torta'), .4, .1)
    s.thunk(s.W(3, 'caderno') - 2, 140, .5); s.ting(s.W(3, 'pipo'), .3)
    for k in range(3): s.thunk(s.W(4, 'tres', 1) + 4 + k * 8, 180, .7)
    for k in range(4): s.thunk(s.W(5, 'quatro') + k * 6, 180, .8)
    s.thunk(s.W(5, 'socorro') - 2, 60, 1.0)
    s.thunk(s.W(6, 'placa') - 2, 90, .6)
    s.ting(s.W(7, 'antena'), .35)
    for k in range(3): s.thunk(s.W(7, 'bato') + k * 7, 180, .8)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def tremor(f, f0, amp=6):
    return amp * math.sin(f * 2.1) * (1 - ramp(f, f0, f0 + 8)) if f >= f0 else 0


def brilho(c, x, y, r, s, cor=AZUL):
    if s <= .03: return
    g = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    d.ellipse((x - r, y - r, x + r, y + r), fill=cor + (int(200 * s),))
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(r * .4)))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = cabine_bg('noite').copy()
        c = put_close(c, f, expr='choque', look=0, shake=.3, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'frio'
    g = f - CAPA
    c = cabine_bg('noite').copy()
    eu(c, 640, f, expr='preocupado', look=.75)
    t = smooth(ramp(g, 0, 120))
    cam = (lerp(640, 760, t), lerp(1300, 1100, t), lerp(1.25, 1.05, easeOut(ramp(g, 0, 16))) * (1 + .0009 * f) + .04 * kick(f, wt(0, 'bati') - 2, .6), 0); CAM[0] = cam
    return c, cam, 'sombrio_noite'


def s1(f):
    c = cabine_bg('noite').copy()
    az = wt(1, 'azul') - 3
    brilho(c, JANI[0], JANI[1], 90, ramp(f, az, az + 6) * (.85 + .15 * math.sin(f * .3)))
    eu(c, 640, f, expr='choque' if f >= az else 'neutro', look=.75)
    cam = (lerp(760, JANI[0], smooth(ramp(f, 0, az))), lerp(1100, 950, smooth(ramp(f, 0, az))), lerp(1.05, 1.5, smooth(ramp(f, 0, az + 6))) * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'sombrio_noite'


def s2(f):
    c = casco_bg().copy()
    tt = wt(2, 'torta') - 3
    sonda(c, 860, 1100, .9, f, antena=.3, olho=(-.6, .2), luz_olho=1.0)
    t = smooth(ramp(f, 0, tt))
    cam = (lerp(700, 860, t), lerp(1250, 1050, t), lerp(1.1, 1.55, t) * (1 + .0009 * f), 0)
    if f > tt: cam = (860, 1000, 1.55 * (1 + .0009 * f) + .05 * kick(f, tt, .6), 0)
    CAM[2] = cam
    return c, cam, 'frio'


def s3(f):
    c = cabine_bg('dia').copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
    ca = wt(3, 'caderno') - 3; pi = wt(3, 'pipo') - 3
    s_ = back(ramp(f, ca, ca + 10)) * 1.0
    caderno(c, 621, 1000, s_, linhas=('PIPO', 'bate 3x = ok'), t=ramp(f, pi - 20, pi + 6))
    if s_ > .1: sonda(c, 621 + 230 * s_, 1000, .42 * s_ * back(ramp(f, pi, pi + 8)), f, antena=1.0)
    cam = (621, 1050, lerp(1.0, 1.06, smooth(ramp(f, 0, 150))) * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'vivo'


def s4(f):
    c = casco_bg().copy()
    t0 = wt(4, 'tres', 1) + 4
    rr = sum(-8 * (1 - ramp(f, t0 + k * 8, t0 + k * 8 + 5)) * (f >= t0 + k * 8) for k in range(3))
    sonda(c, 860, 1100, .9, f, antena=1.0, olho=(-.6, 0), rot=rr)
    brilho(c, 860, 1080, 50, .5 + .3 * math.sin(f * .2))
    cam = (lerp(780, 860, smooth(ramp(f, 0, 150))), 1100, lerp(1.25, 1.4, smooth(ramp(f, 0, 150))) * (1 + .0009 * f), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = casco_bg().copy()
    so = wt(5, 'socorro') - 3
    if f >= so + 4:   # CLOSE descoberta
        c = cabine_bg('noite').copy()
        c = put_close(c, f, expr='choque', look=.25, shake=.4, **EU)
        cam = (621, 1104, lerp(1.2, 1.04, easeOut(ramp(f, so + 4, so + 14))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'sombrio_noite'
    q = wt(5, 'quatro')
    rr = sum(-8 * (1 - ramp(f, q + k * 6, q + k * 6 + 4)) * (f >= q + k * 6) for k in range(4))
    pisca = 1.0 if (f // 5) % 2 else .2
    sonda(c, 860, 1100, .9, f, antena=.3, olho=(-.6, .2), luz_olho=pisca, rot=rr)
    cam = (860, 1050, lerp(1.3, 1.6, smooth(ramp(f, 0, so))) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'frio'


def s6(f):
    c = corredor_bg('dia').copy()
    placa(c, 360, 700, .9)
    te = wt(6, 'mas') - 3
    t = smooth(ramp(f, te, te + 24))
    cam = (lerp(450, JAN[0], t), lerp(900, 1050, t), lerp(1.35, 1.5, t) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'vivo'


def s7(f):
    an = wt(7, 'antena') - 3; e_ = wt(7, 'e') - 3
    fim = wt(7, 'volta') - 2
    if f < e_:   # antena consertada
        c = casco_bg().copy()
        a = .3 + .7 * back(ramp(f, an, an + 8))
        sonda(c, 860, 1100, .9, f, antena=a, olho=(-.6, 0))
        brilho(c, 860, 1080, 60, ramp(f, an, an + 8) * .7)
        cam = (860, 1080, lerp(1.2, 1.4, smooth(ramp(f, 0, e_))) * (1 + .0009 * f), 0); CAM[7] = cam
        return c, cam, 'vivo'
    c = cabine_bg('noite').copy()
    brilho(c, JANI[0], JANI[1], 90, .8)
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.2, 1.06, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[7] = cam
        return c, cam, 'sombrio_noite'
    ba = wt(7, 'bato') - 3
    eu(c, 760, f, expr='sorriso', look=.75)
    sh = sum(tremor(f, ba + 3 + k * 7, 6) for k in range(3))
    cam = (800 + sh, 1060, lerp(1.1, 1.3, smooth(ramp(f, e_, fim))) * (1 + .0009 * f), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 2', 540, 100, 1, 64, big=True)
            gancho(im, ['QUEM BATIA', 'NA JANELA?'], 180, 1, 110)
        else:
            stamp(im, 'PARTE 2', 290, 230, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
            b = wt(0, 'bati') - 3
            burst(im, 'TOC', 780, 420, back(ramp(f, b, b + 6)), 60)
    elif si == 1:
        az = wt(1, 'azul') - 3
        stamp(im, 'LUZ AZUL', 540, 260, back(ramp(f, az, az + 8)), 84)
    elif si == 2:
        ro = wt(2, 'robozinho') - 3; tt = wt(2, 'torta') - 3
        ax, ay = to_out(2, 940, 900)
        card(im, 'Robozinho', 'grudado no casco', 300, 280, ramp(f, ro, ro + 10))
        if f >= tt: stamp(im, 'ANTENA TORTA', 540, 520, back(ramp(f, tt, tt + 8)), 70)
    elif si == 3:
        ca = wt(3, 'caderno') - 3; pi = wt(3, 'pipo') - 3
        card(im, 'Caderno da vó', 'ela construiu a estação', 330, 250, ramp(f, ca, ca + 10))
        stamp(im, 'PIPO', 760, 1250, back(ramp(f, pi, pi + 8)), 100, big=True)
    elif si == 4:
        t0 = wt(4, 'tres', 1) + 4; tb = wt(4, 'tudo') - 3
        n = sum(1 for k in range(3) if f >= t0 + k * 8)
        painel(im, 'BATIDAS', str(n), 300, 280, ramp(f, t0 - 8, t0), w=340)
        card(im, '3 batidas', 'tudo bem aqui fora', 700, 1250, ramp(f, tb, tb + 10))
    elif si == 5:
        q = wt(5, 'quatro'); so = wt(5, 'socorro') - 3
        n = sum(1 for k in range(4) if f >= q + k * 6)
        if f < so + 4: painel(im, 'BATIDAS', str(n), 300, 280, ramp(f, q - 8, q), glitch=.6 if n == 4 else 0, w=340)
        else: stamp(im, 'SOCORRO', 540, 250, back(ramp(f, so + 4, so + 12)), 96, big=True)
    elif si == 6:
        pl = wt(6, 'placa') - 3; te = wt(6, 'terra') - 3
        stamp(im, 'A VERDADE', 300, 230, back(ramp(f, pl, pl + 8)), 90, big=True)
        if f >= te: card(im, 'A vó', 'voltou pra Terra', 330, 1250, ramp(f, te, te + 10))
    elif si == 7:
        an = wt(7, 'antena') - 3; e_ = wt(7, 'e') - 3; ba = wt(7, 'bato') - 3; fim = wt(7, 'volta') - 2
        if f < e_: stamp(im, 'CONSERTADO', 540, 250, back(ramp(f, an, an + 8)), 84)
        elif f < fim:
            for k in range(3):
                a = ba + 3 + k * 7
                if f >= a: burst(im, 'TOC', [300, 780, 540][k], [330, 380, 600][k], back(ramp(f, a, a + 6)), 56, rot=[-8, 8, -4][k])
        else: painel(im, 'TODA NOITE', '03:00', 540, 260, ramp(f, fim + 2, fim + 10), w=420)
    return grao(im.convert('RGB'), lf)
