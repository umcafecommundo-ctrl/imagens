"""Formato MISTÉRIO: "O cavalo treze", PARTE 2 (22/11/2026, 12h). História inventada. Mesma Nina e mesmo Seu Dito da parte 1.
Virada: à meia-noite o cavalo branco para na frente da Nina e abaixa a cabeça; ela sobe; o carrossel gira sozinho cada vez mais
rápido; o cavalo desce e trota até o depósito do parque; debaixo de uma lona velha há um cavalo de madeira quebrado, branco, de
crina dourada: era ele, tirado pra conserto há cinquenta anos e esquecido; ele só queria voltar pro lugar dele; Nina e Seu Dito
consertam o cavalo e o carrossel passa a ter treze; mas na lua cheia seguinte quem passa conta catorze.
Cenários/cores: s0 CAPA close (noite) -> parque à noite (sombrio_noite) | s1 carrossel parado, cavalo branco (sombrio_noite) |
s2 montada no cavalo + CLOSE no giro (sombrio_noite) | s3 caminho até o depósito, madrugada (frio) | s4 depósito, lona (sombrio) |
s5 depósito + CLOSE na descoberta (tarde/lembrança) | s6 carrossel com o lugar vazio, fim de tarde (tarde) |
s7 parque de dia, treze cavalos (vivo) | s8 lua cheia, catorze + CLOSE final (sombrio_noite)."""
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
    "Na parte um, o carrossel ganhou um cavalo na lua cheia. E a minha ficha era a treze.",
    "À meia-noite, o cavalo branco parou bem na minha frente. E abaixou a cabeça.",
    "Eu subi. E o carrossel girou sozinho, cada vez mais rápido.",
    "Quando parou, ele desceu e trotou até o depósito do parque.",
    "Lá dentro, debaixo de uma lona, tinha um cavalo de madeira quebrado. Branco.",
    "Era ele. Tirado pra conserto há cinquenta anos, e esquecido ali.",
    "Ele não queria assustar ninguém. Só queria voltar pro lugar dele.",
    "No dia seguinte, eu e o Seu Dito consertamos o cavalo. Agora são treze.",
    "Mas ontem foi lua cheia de novo. E quem passou na frente contou catorze.",
]
FALA_TIKTOK = "Você subiria no cavalo catorze? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 5
FLASH = []
CHECK = [(0, 'treze', 6), (1, 'parou', 4), (1, 'cabeca', 6), (2, 'subi', 4), (2, 'rapido', 6), (3, 'deposito', 6),
         (4, 'lona', 4), (4, 'quebrado', 6), (5, 'ele', 6), (5, 'cinquenta', 6), (6, 'lugar', 6), (7, 'treze', 6), (8, 'catorze', 10)]
CAM = {}
CAPA = 38


def SFX(s):
    s.thunk(2, 120, .8)
    s.ting(s.W(0, 'treze'), .3)
    s.thunk(s.W(1, 'parou') - 2, 90, .7); s.whoosh(s.W(1, 'cabeca') - 6, .4, .2)
    s.whoosh(s.W(2, 'girou') - 6, .7, .4); s.whoosh(s.W(2, 'rapido') - 6, .9, .5)
    for i in range(6): s.thunk(s.W(3, 'trotou') + i * 7, 300, .25)
    s.whoosh(s.W(4, 'lona') - 6, .6, .3); s.thunk(s.W(4, 'quebrado') - 2, 90, .7)
    s.thunk(s.W(5, 'ele') - 2, 70, .9)
    s.trill(s.W(6, 'lugar'), .6, .12)
    s.ting(s.W(7, 'treze'), .3)
    s.thunk(s.W(8, 'catorze') - 2, 60, 1.0)


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


def branco(c, x, y_top, h, rot=0, flip=False, brilho=True):
    im = cavalo_img('#f4f2ec', '#e8b83a', int(h / 8) * 8, flip, brilho=brilho)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y_top)))


def montada(c, x, y_top, h, f, **kw):
    """Nina montada no cavalo branco: corpo dela atrás, cavalo na frente."""
    nina(c, x - h * .17, f, feet=y_top + h * .82, h=h * 1.05, **kw)
    branco(c, x, y_top, h)


@lru_cache(maxsize=4)
def deposito_bg(luz='sombrio'):
    tarde = luz == 'tarde'
    p = Pen(W_, H_)
    madeira = hexc('#8a6440') if tarde else hexc('#4e4034')
    p.poly([(0, 0), (W_, 0), (W_, 1560), (0, 1560)], madeira)
    for x in range(0, W_, 150): p.stroke([(x, 0), (x, 1560)], 5, mul(madeira, .75))
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], mul(madeira, .7))
    for y in range(1620, H_, 110): p.stroke([(0, y), (W_, y)], 3, mul(madeira, .55))
    p.stroke([(0, 1560), (W_, 1560)], 7)
    # janelinha com lua
    p.shape([(880, 300), (1120, 300), (1120, 560), (880, 560)], hexc('#f0d9a0') if tarde else hexc('#2c3a4a'), None, 7, 0)
    p.stroke([(1000, 300), (1000, 560)], 8, mul(madeira, 1.2)); p.stroke([(880, 430), (1120, 430)], 8, mul(madeira, 1.2))
    # caixas e prateleira
    for bx, by, bw in ((60, 1300, 260), (110, 1080, 200), (1000, 1350, 220)):
        p.shape([(bx, by), (bx + bw, by), (bx + bw, by + 260), (bx, by + 260)], hexc('#b58a5a') if tarde else hexc('#6f5a44'), None, 6, 0)
        p.stroke([(bx, by), (bx + bw, by + 260)], 4, mul(hexc('#6f5a44'), .7))
    p.shape([(60, 760), (420, 760), (420, 790), (60, 790)], mul(madeira, .6), None, 5, 0)
    p.dot(140, 720, 40, hexc('#d9634f'), 5); p.dot(260, 720, 36, hexc('#5aa6d8'), 5)
    im = p.img.resize((W_, H_), Image.LANCZOS)
    if not tarde:   # luz da lanterna
        g = Image.new('RGBA', (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
        d.ellipse((240, 1100, 1000, 1900), fill=(255, 240, 190, 60)); g = g.filter(ImageFilter.GaussianBlur(60))
        im.alpha_composite(g)
    return im


def quebrado(c, x, y, h):
    """cavalo de madeira quebrado deitado no chão + a perna solta."""
    im = cavalo_img('#e6e2d6', '#d9a83a', int(h / 8) * 8, False, brilho=False).rotate(78, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height * .62)))
    p = Pen(300, 120)
    p.line([(30, 70), (220, 50)], hexc('#e6e2d6'), 26, 5)
    c.alpha_composite(p.img.resize((300, 120), Image.LANCZOS), (int(x + h * .35), int(y - 40)))


def lona(c, x, y, w, t):
    """lona cinza por cima do cavalo; t 0..1 = puxada para a esquerda."""
    if t >= 1: return
    p = Pen(W_, 700)
    dx = -t * (w + 400)
    pts = [(x - w / 2 - 40 + dx, 650), (x - w / 2 + 60 + dx, 470), (x - 120 + dx, 380), (x + 60 + dx, 360), (x + 220 + dx, 420), (x + w / 2 + 40 + dx, 650)]
    p.shape(pts, hexc('#8a9496'), hexc('#6c7678'), 7, 18)
    p.stroke([(x - 100 + dx, 420), (x - 70 + dx, 640)], 4, hexc('#6c7678')); p.stroke([(x + 120 + dx, 420), (x + 160 + dx, 640)], 4, hexc('#6c7678'))
    c.alpha_composite(p.img.resize((W_, 700), Image.LANCZOS), (0, int(y - 650)))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close + PARTE 2 + gancho
        c = noite_bg(); carrossel(c, f, 'noite', 12, f * .02, extra=True)
        c = put_close(c, f, expr='medo', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'sombrio_noite'
    g = f - CAPA
    c = noite_bg()
    carrossel(c, f, 'noite', 12, f * .015, extra=True)
    nina(c, 330, f, feet=1900, h=900, expr='preocupado', look=.75)
    hx, hy = mao_dir(330, 1900, 900)
    tr = wt(0, 'treze') - 3
    ficha(c, hx + 20, hy - 30, 46 * ramp(f, tr - 8, tr), 13)
    t = smooth(ramp(g, 0, 140))
    cam = (lerp(621, 520, t), lerp(1100, 1250, t), lerp(1.0, 1.15, t) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'sombrio_noite'


def s1(f):
    c = noite_bg()
    carrossel(c, f, 'noite', 12, .4)
    pa = wt(1, 'parou') - 3; cb = wt(1, 'cabeca') - 3
    u = easeOut(ramp(f, 0, pa))
    branco(c, lerp(1100, 800, u), 1250 + 30 * math.sin(f * .3) * (1 - ramp(f, pa - 4, pa)), 560, rot=-14 * back(ramp(f, cb, cb + 10)))
    nina(c, 330, f, feet=1900, h=900, expr='choque' if f >= pa else 'neutro', look=.75)
    cam = (621, 1300, lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) * (1 + .0009 * f) + .05 * kick(f, pa, .6), 0); CAM[1] = cam
    return c, cam, 'sombrio_noite'


def s2(f):
    ra = wt(2, 'rapido') - 3
    c = noite_bg()
    vel = .02 + .12 * ramp(f, wt(2, 'girou') - 3, ra)
    fase = sum(.02 + .12 * ramp(k, wt(2, 'girou') - 3, ra) for k in range(f))
    carrossel(c, f, 'noite', 12, fase)
    if vel > .05:   # riscos de luz
        d = ImageDraw.Draw(c)
        for k in range(10):
            y = 900 + k * 60 + 20 * math.sin(f + k)
            d.line((0, y, W_, y + 10), fill=(250, 230, 160, int(60 * ramp(vel, .05, .14))), width=6)
    montada(c, 621, 1100, 640, f, expr='sorriso' if f < ra else 'choque', look=0)
    if f >= ra:   # CLOSE no giro
        c = c.filter(ImageFilter.BoxBlur(6)).convert('RGBA')
        c = put_close(c, f, expr='choque', look=0, shake=.6, fundo_blur=4, **EU)
        cam = (621, 1104 + kick(f, ra, .8) * 12, lerp(1.25, 1.05, easeOut(ramp(f, ra, ra + 10))) * (1 + .0009 * f), 2 * math.sin(f * .3)); CAM[2] = cam
        return c, cam, 'sombrio_noite'
    cam = (621, 1250, 1.15 * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'sombrio_noite'


def s3(f):
    c = parque_bg('noite').copy(); lua(c, 960, 300, 72)
    p = Pen(500, 500)   # depósito à direita
    p.shape([(40, 480), (40, 160), (460, 160), (460, 480)], hexc('#6a5442'), hexc('#54412f'), 7, 12)
    p.shape([(20, 170), (250, 30), (480, 170)], hexc('#4a3a2e'), None, 7, 0)
    p.shape([(180, 300), (320, 300), (320, 480), (180, 480)], hexc('#f2e2a0'), None, 6, 0)
    c.alpha_composite(p.img.resize((500, 500), Image.LANCZOS), (760, 1020))
    u = ramp(f, 0, wt(3, 'deposito') + 10)
    x = lerp(150, 820, u)
    montada(c, x, 1180 + 14 * abs(math.sin(f * .35)), 420, f, expr='preocupado', look=.75)
    cam = (lerp(450, 800, smooth(u)), 1250, 1.15 * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'frio'


def s4(f):
    c = deposito_bg('sombrio').copy()
    lo = wt(4, 'lona') - 3; qb = wt(4, 'quebrado') - 3
    quebrado(c, 640, 1700, 520)
    lona(c, 660, 1760, 640, easeOut(ramp(f, lo + 6, lo + 22)))
    nina(c, 330, f, feet=1980, h=900, expr='choque' if f >= qb else 'preocupado', look=.75)
    t = smooth(ramp(f, 0, 160))
    cam = (lerp(560, 640, t), lerp(1350, 1500, t), lerp(1.0, 1.25, t) * (1 + .0009 * f) + .05 * kick(f, qb, .6), 0); CAM[4] = cam
    CAM['q'] = (640, 1560)
    return c, cam, 'sombrio'


def s5(f):
    c = deposito_bg('tarde').copy()
    quebrado(c, 640, 1700, 520)
    el = wt(5, 'tirado') - 3
    if f < el + 4:   # CLOSE na descoberta
        nina(c, 230, f, feet=1980, h=900, expr='choque', look=.75)
        c = put_close(c, f, expr='choque', look=.5, shake=.3, **EU)
        cam = (621, 1104 + kick(f, 2, .8) * 12, lerp(1.25, 1.05, easeOut(ramp(f, 0, 10))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'tarde'
    nina(c, 230, f, feet=1980, h=900, expr='preocupado', look=.75)
    cam = (600, 1400, lerp(1.2, 1.05, smooth(ramp(f, el, el + 100))) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = parque_bg('tarde').copy()
    carrossel(c, f, 'tarde', 12, 0.25)
    lu = wt(6, 'lugar') - 3
    if f >= lu:   # contorno do lugar vazio
        d = ImageDraw.Draw(c); a = int(200 * ramp(f, lu, lu + 8))
        x0, y0 = 621 + 430 * math.sin(.25 + 2 * math.pi * 12 / 13) - 10, 1090
        for k in range(0, 360, 20):
            r = math.radians(k); d.arc((x0 - 150, y0 - 200, x0 + 150, y0 + 200), k, k + 10, fill=(255, 246, 210, a), width=8)
        CAM['vazio'] = (x0, y0)
    nina(c, 980, f, feet=1900, h=900, expr='preocupado', look=-.75, flip=True)
    cam = (621, 1150, lerp(1.0, 1.1, smooth(ramp(f, 0, 120))) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'tarde'


def s7(f):
    c = parque_bg('dia').copy()
    carrossel(c, f, 'dia', 12, f * .02, extra=True)
    nina(c, 250, f, feet=1940, h=900, expr='sorriso', look=.75)
    dito(c, 1000, f, feet=1940, h=940, expr='sorriso', look=-.75, flip=True)
    cam = (621, 1200, lerp(1.0, 1.08, smooth(ramp(f, 0, 140))) * (1 + .0009 * f), 0); CAM[7] = cam
    return c, cam, 'vivo'


def s8(f):
    c = noite_bg()
    ca = wt(8, 'catorze') - 3
    carrossel(c, f, 'noite', 13, f * .015, extra=f >= ca)
    fim = ca + 24
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.4, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[8] = cam
        return c, cam, 'sombrio_noite'
    nina(c, 330, f, feet=1900, h=900, expr='choque' if f >= ca else 'neutro', look=.75)
    cam = (621, lerp(1000, 1150, smooth(ramp(f, 0, ca))), 1.05 * (1 + .0009 * f) + .1 * kick(f, ca, .6), 0); CAM[8] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 2', 540, 100, 1, 64, big=True)
            gancho(im, ['EU SUBI NO', 'CAVALO TREZE'], 180, 1, 110)
        else:
            stamp(im, 'NA PARTE 1', 540, 200, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
            painel(im, 'CAVALOS', '13', 800, 470, ramp(f, CAPA + 14, CAPA + 24))
    elif si == 1:
        m = wt(1, 'meia-noite') - 3
        painel(im, 'HORA', '00:00', 540, 230, ramp(f, m, m + 10))
    elif si == 2:
        ra = wt(2, 'rapido') - 3; gi = wt(2, 'girou') - 3
        if f < ra: burst(im, 'VUUUSH', 760, 330, back(ramp(f, gi, gi + 8)), 60)
        else: burst(im, '?!', 860, 280, back(ramp(f, ra, ra + 8)), 70)
    elif si == 3:
        d = wt(3, 'deposito') - 3
        stamp(im, 'O DEPÓSITO', 540, 260, back(ramp(f, d, d + 8)), 80)
    elif si == 4:
        qb = wt(4, 'quebrado') - 3; br = wt(4, 'branco') - 3
        alvo = to_out(4, *CAM['q']) if 'q' in CAM else None
        card(im, 'Cavalo de madeira', 'quebrado, branco, de crina dourada', 330, 300, ramp(f, qb, qb + 10), alvo=alvo if f >= br else None)
    elif si == 5:
        ci = wt(5, 'cinquenta') - 3; el = wt(5, 'tirado') - 3
        if f < el + 4: stamp(im, 'ERA ELE', 540, 250, back(ramp(f, 2, 10)), 90, big=True)
        else: painel(im, 'ESQUECIDO HÁ', '50 ANOS', 540, 300, ramp(f, ci, ci + 10), w=560)
    elif si == 6:
        lu = wt(6, 'lugar') - 3
        alvo = to_out(6, *CAM['vazio']) if 'vazio' in CAM else None
        card(im, 'O lugar dele', 'vazio há cinquenta anos', 330, 300, ramp(f, lu, lu + 10), alvo=alvo)
    elif si == 7:
        tr = wt(7, 'treze') - 3; ds = wt(7, 'seguinte') - 3
        stamp(im, 'NO DIA SEGUINTE', 540, 180, back(ramp(f, ds, ds + 8)), 70)
        painel(im, 'CAVALOS', '13', 540, 420, ramp(f, tr, tr + 10))
    elif si == 8:
        ca = wt(8, 'catorze') - 3; fim = ca + 24; lu = wt(8, 'lua') - 3
        if f < fim:
            stamp(im, 'LUA CHEIA', 540, 120, back(ramp(f, lu, lu + 8)), 70)
            painel(im, 'CAVALOS', '14' if f >= ca else '13', 540, 340, ramp(f, 2, 12), glitch=1 if ca <= f < ca + 12 and f % 4 < 2 else 0)
        else: stamp(im, 'CAVALO 14?', 540, 250, back(ramp(f, fim + 4, fim + 12)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
