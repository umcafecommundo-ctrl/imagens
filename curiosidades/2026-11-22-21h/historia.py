"""Formato MISTÉRIO: "O farol sem faroleiro", PARTE 2 (22/11/2026, 21h). História inventada. Mesmo Caio da parte 1.
Virada: o cadeado abre; Caio sobe cento e vinte degraus; lá em cima não há ninguém, só uma máquina de engrenagens girando a luz;
o caderno da última faroleira conta que ela construiu a máquina pra durar quarenta anos; a luz verde avisa tempestade, mas três
piscadas eram a corda acabando; o pacote ela deixou no correio há quarenta anos, pra quem morasse na casa azul; Caio gira a
manivela e às seis da tarde a luz acende; na última página: daqui a quarenta anos, mande a chave pra próxima.
Cenários/cores: s0 CAPA close (sombrio) -> ilha fim de tarde, chave na mão (tarde) | s1 porta do farol -> escada (sombrio) |
s2 sala da lanterna, máquina (frio) | s3 caderno, lembrança (tarde) | s4 lanterna piscando verde + CLOSE (sombrio_noite) |
s5 ilha há quarenta anos, faroleira com o pacote (tarde) | s6 manivela, luz acende (vivo) | s7 caderno à noite + CLOSE final (sombrio_noite)."""
from kit import *
import kit
from sombrio import *
from farol import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#1e1612', pele='#7a4a2a', roupa='#e8803a', calca='#3a3f46')
VELHA = dict(penteado='coque', cabelo='#d8d8d4', pele='#c8956b', roupa='#2f4a6a', calca='#3a3f46', oculos=True, velho=True)
VERDE = (120, 240, 150); AMARELO = (255, 236, 150)

LINES = [
    "Na parte um, o farol piscou verde sem tempestade. E a chave dele apareceu na minha porta.",
    "O cadeado abriu na primeira volta. Subi cento e vinte degraus.",
    "Lá em cima, não tinha ninguém. Só uma máquina cheia de engrenagens, girando a luz.",
    "Do lado, o caderno da última faroleira. Ela construiu a máquina pra durar quarenta anos.",
    "A luz verde avisa a tempestade. Mas três piscadas... era a corda da máquina acabando.",
    "E o pacote, ela deixou no correio, há quarenta anos. Pra quem morasse na casa azul.",
    "Eu girei a manivela até o braço doer. Às seis da tarde, a luz acendeu.",
    "Na última página, ela escreveu: daqui a quarenta anos, mande a chave pra próxima.",
]
FALA_TIKTOK = "Você subiria no farol sozinho? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 4
FLASH = []
CHECK = [(0, 'chave', 6), (1, 'abriu', 4), (1, 'degraus', 6), (2, 'ninguem', 4), (2, 'engrenagens', 6), (3, 'caderno', 6),
         (3, 'quarenta', 6), (4, 'piscadas', 6), (4, 'acabando', 6), (5, 'correio', 6), (5, 'azul', 6), (6, 'manivela', 6),
         (6, 'acendeu', 6), (7, 'proxima', 10)]
CAM = {}
CAPA = 38


def SFX(s):
    s.thunk(2, 120, .8)
    s.ting(s.W(0, 'chave'), .3)
    s.thunk(s.W(1, 'abriu') - 2, 160, .7)
    for i in range(8): s.thunk(s.W(1, 'subi') + i * 6, 320, .2)
    s.whoosh(s.W(2, 'ninguem') - 6, .4, .2)
    for i in range(5): s.ting(s.W(2, 'engrenagens') + i * 10, .08)
    s.whoosh(s.W(3, 'caderno') - 6, .4, .2)
    for i in range(3): s.ting(s.W(4, 'piscadas') + i * 9, .2)
    s.thunk(s.W(4, 'acabando') - 2, 60, 1.0)
    s.ting(s.W(5, 'azul'), .25)
    for i in range(6): s.thunk(s.W(6, 'manivela') + i * 8, 260, .25)
    s.trill(s.W(6, 'acendeu'), .7, .14)
    s.thunk(s.W(7, 'proxima') - 2, 70, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def caio(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def maquina(c, f, vel=1.0, luz_cor=AMARELO, brilho=.6):
    lente(c, 621, 820, 190, luz_cor, brilho)
    a = f * 3 * vel
    engrenagem(c, 300, 1380, 170, a)
    engrenagem(c, 520, 1500, 110, -a * 1.55, '#a8a8a0')
    engrenagem(c, 900, 1420, 140, -a * 1.2)
    p = Pen(60, 60)


@lru_cache(maxsize=2)
def porta_bg():
    p = Pen(W_, H_)
    for k in range(8):
        col = hexc('#c9524a') if k % 2 == 0 else hexc('#e8e4da')
        p.poly([(0, k * 300), (W_, k * 300), (W_, k * 300 + 300), (0, k * 300 + 300)], mul(col, .8))
    p.poly([(0, 1700), (W_, 1700), (W_, H_), (0, H_)], hexc('#7a7f82'))
    p.stroke([(0, 1700), (W_, 1700)], 7)
    p.shape([(370, 600), (870, 600), (870, 1700), (370, 1700)], hexc('#6a4a32'), hexc('#53392a'), 8, 16)
    for x in (470, 620, 770): p.stroke([(x, 620), (x, 1690)], 5, hexc('#53392a'))
    p.shape([(370, 900), (870, 900), (870, 940), (370, 940)], hexc('#4a4e50'), None, 5, 0)
    p.shape([(370, 1360), (870, 1360), (870, 1400), (370, 1400)], hexc('#4a4e50'), None, 5, 0)
    return p.img.resize((W_, H_), Image.LANCZOS)


def cadeado(c, x, y, aberto=0.0):
    p = Pen(300, 360)
    p.arc(150, 130 - 50 * aberto, 50, 60, 180, 360, 18, hexc('#7a7f82'))
    p.shape([(85, 130), (215, 130), (215, 250), (85, 250)], hexc('#b0703a'), hexc('#8a5228'), 6, 10)
    p.dot(150, 180, 12, (36, 30, 32))
    for xx, yy in ((105, 150), (190, 220), (130, 235)): p.dot(xx, yy, 9, hexc('#7a4a2a'))
    c.alpha_composite(p.img.resize((300, 360), Image.LANCZOS), (int(x - 150), int(y - 180)))


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close + PARTE 2 + gancho
        c = porta_bg().copy(); cadeado(c, 780, 1180, 1)
        c = put_close(c, f, expr='medo', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'sombrio'
    g = f - CAPA
    c = ilha_bg('tarde').copy()
    v = wt(0, 'verde') - 3
    if v <= f < v + 30 and (f - v) % 10 < 6: facho(c, 190, VERDE)
    caio(c, 420, f, expr='preocupado', look=.75)
    hx, hy = mao_dir(420, 1900, 900)
    ch = wt(0, 'chave') - 3
    chave(c, hx + 40, hy - 20, .55 * back(ramp(f, ch, ch + 8)), rot=20)
    t = smooth(ramp(g, 0, 140))
    cam = (lerp(560, 520, t), lerp(1100, 1350, t), lerp(1.0, 1.2, t) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'tarde'


def s1(f):
    su = wt(1, 'subi') - 3
    if f < su:
        c = porta_bg().copy()
        ab = wt(1, 'abriu') - 3
        u = easeOut(ramp(f, 0, ab))
        cadeado(c, 780, 1180, back(ramp(f, ab, ab + 8)))
        chave(c, lerp(1150, 860, u), 1190, .9, rot=0)
        cam = (760, 1180, 1.5 * (1 + .0009 * f) + .06 * kick(f, ab, .8), 0); CAM[1] = cam
        return c, cam, 'sombrio'
    g = f - su
    c = escada_bg('sombrio').copy()
    k = min(12, g / 6)   # degrau atual
    ki = int(k); fr = k - ki
    lado = ki % 2
    xa = 330 if lado == 0 else 900
    xb = 900 if lado == 0 else 330
    x = lerp(xa, xb, fr) if ki < 12 else xa
    feet = 2150 - 150 * k
    caio(c, x, f, feet=feet, h=760, walk=1, expr='neutro', look=.5)
    cam = (621, feet - 420, 1.15 * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'sombrio'


def s2(f):
    c = sala_lanterna_bg('dia').copy()
    maquina(c, f, 1.0, AMARELO, .5)
    ni = wt(2, 'ninguem') - 3
    caio(c, 980, f, feet=1980, h=860, expr='choque' if f >= ni else 'neutro', look=-.75, flip=True)
    t = smooth(ramp(f, 0, 150))
    cam = (lerp(800, 621, t), lerp(1350, 1150, t), lerp(1.2, 1.0, t) * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'frio'


def s3(f):
    c = sala_lanterna_bg('tarde').copy().filter(ImageFilter.GaussianBlur(10)).convert('RGBA')
    ca = wt(3, 'caderno') - 3; co = wt(3, 'construiu') - 3
    caderno(c, 621, 1050, .95 * back(ramp(f, ca - 4, ca + 6)), ['Farol da ilha,', 'outono.', 'Máquina de corda.', 'Dura 40 anos.'], ramp(f, co - 10, co + 40))
    cam = (621, 1080, lerp(1.0, 1.1, smooth(ramp(f, 0, 150))) * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = sala_lanterna_bg('noite').copy()
    pi = wt(4, 'piscadas') - 3; ac = wt(4, 'acabando') - 3
    pisc = any(pi + i * 9 <= f < pi + i * 9 + 5 for i in range(3))
    verde_ = wt(4, 'verde') - 3 <= f < wt(4, 'mas') - 3
    vel = 1 - .85 * ramp(f, pi, ac)
    maquina(c, f, vel, VERDE if (pisc or verde_) else AMARELO, 1.0 if (pisc or verde_) else .25)
    if f >= ac:   # CLOSE na descoberta
        c = put_close(c, f, expr='choque', look=.5, shake=.3, escurece=.2, **EU)
        cam = (621, 1104 + kick(f, ac, .8) * 12, lerp(1.25, 1.05, easeOut(ramp(f, ac, ac + 10))) * (1 + .0009 * f), 0); CAM[4] = cam
        return c, cam, 'sombrio_noite'
    caio(c, 1060, f, feet=1980, h=860, expr='preocupado', look=-.75, flip=True)
    cam = (680, 1150, 1.05 * (1 + .0009 * f), 0); CAM[4] = cam
    return c, cam, 'sombrio_noite'


def s5(f):
    c = ilha_bg('tarde').copy()
    put_menino(c, 560, 1900, 920, f, seed=9, expr='sorriso', look=-.75, flip=True, **VELHA)
    hx, hy = 560 - .13 * 920, 1900 - .26 * 920
    pacote(c, hx - 20, hy - 30, .6)
    t = smooth(ramp(f, 0, 140))
    cam = (lerp(520, 400, t), lerp(1300, 1250, t), lerp(1.05, 1.15, t) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    ac = wt(6, 'acendeu') - 3; ma = wt(6, 'manivela') - 3
    c = sala_lanterna_bg('tarde' if f < ac else 'dia').copy()
    vel = .2 + 2.2 * ramp(f, ma, ma + 30)
    lente(c, 621, 820, 190, AMARELO, 1.0 if f >= ac else .2)
    a = sum(.2 + 2.2 * ramp(k, ma, ma + 30) for k in range(0, f, 2)) * 6
    engrenagem(c, 300, 1380, 170, a)
    engrenagem(c, 520, 1500, 110, -a * 1.55, '#a8a8a0')
    # manivela na engrenagem grande
    p = Pen(W_, 600); r = math.radians(a)
    ex, ey = 300 + 130 * math.cos(r), 300 + 130 * math.sin(r)
    p.line([(300, 300), (ex, ey)], hexc('#5a5f62'), 22, 5); p.dot(ex, ey, 26, hexc('#c0453a'), 5)
    c.alpha_composite(p.img.resize((W_, 600), Image.LANCZOS), (0, 1080))
    caio(c, 640, f, feet=1980, h=860, expr='sorriso' if f >= ac else 'preocupado', look=-.75, flip=True)
    cam = (621, 1150, 1.05 * (1 + .0009 * f) + .06 * kick(f, ac, .7), 0); CAM[6] = cam
    return c, cam, 'vivo' if f >= ac else 'tarde'


def s7(f):
    c = ilha_bg('noite').copy(); facho(c, 190 - 25 * math.sin(f * .05), AMARELO)
    c = c.filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
    da = wt(7, 'daqui') - 3; pr = wt(7, 'proxima')
    caderno(c, 621, 1050, .95 * back(ramp(f, 0, 8)), ['Daqui a', '40 anos,', 'mande a chave', 'pra próxima.'], ramp(f, da, pr + 6))
    fim = pr + 12
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='preocupado', look=0, escurece=.35, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[7] = cam
        return c, cam, 'sombrio_noite'
    cam = (621, 1060, 1.05 * (1 + .002 * f), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 2', 540, 100, 1, 64, big=True)
            gancho(im, ['EU ABRI O', 'FAROL PROIBIDO'], 180, 1, 110)
        else:
            stamp(im, 'NA PARTE 1', 300, 520, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
    elif si == 1:
        su = wt(1, 'subi') - 3; ab = wt(1, 'abriu') - 3
        if f < su: burst(im, 'CLIC!', 300, 420, back(ramp(f, ab, ab + 8)), 70)
        else: painel(im, 'DEGRAUS', str(min(120, int((f - su) / 72 * 120))), 540, 230, ramp(f, su, su + 8))
    elif si == 2:
        ni = wt(2, 'ninguem') - 3; en = wt(2, 'engrenagens') - 3
        stamp(im, 'NINGUÉM', 540, 200, back(ramp(f, ni, ni + 8)), 80)
        card(im, 'A máquina', 'engrenagens girando a luz', 330, 1240, ramp(f, en, en + 10))
    elif si == 3:
        qu = wt(3, 'quarenta') - 3
        stamp(im, 'O CADERNO DA FAROLEIRA', 540, 200, back(ramp(f, 0, 8)), 60)
        painel(im, 'DURAÇÃO', '40 ANOS', 540, 1240, ramp(f, qu, qu + 10), w=560)
    elif si == 4:
        pi = wt(4, 'piscadas') - 3; ac = wt(4, 'acabando') - 3
        if f < ac: painel(im, 'PISCADAS', str(sum(1 for i in range(3) if f >= pi + i * 9)), 540, 230, ramp(f, pi - 6, pi + 4))
        else: stamp(im, 'A CORDA ACABANDO', 540, 250, back(ramp(f, ac + 2, ac + 10)), 70)
    elif si == 5:
        co = wt(5, 'correio') - 3; az = wt(5, 'azul') - 3
        stamp(im, 'HÁ 40 ANOS', 540, 170, back(ramp(f, co - 6, co + 2)), 80, big=True)
        ax, ay = to_out(5, 175, 1300)
        card(im, 'Para:', 'quem morar na casa azul', 600, 520, ramp(f, az - 8, az + 2), alvo=(ax, ay))
    elif si == 6:
        se = wt(6, 'seis') - 3
        painel(im, 'HORA', '18:00', 540, 230, ramp(f, se, se + 10))
    elif si == 7:
        pr = wt(7, 'proxima'); fim = pr + 12
        if f < fim: stamp(im, 'ÚLTIMA PÁGINA', 540, 200, back(ramp(f, 0, 8)), 70)
        else: stamp(im, 'DAQUI A 40 ANOS...', 540, 250, back(ramp(f, fim + 4, fim + 12)), 70, rot=3)
    return grao(im.convert('RGB'), lf)
