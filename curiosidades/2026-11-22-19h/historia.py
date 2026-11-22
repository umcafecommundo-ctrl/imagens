"""Formato MISTÉRIO: "O farol sem faroleiro", PARTE 1 (22/11/2026, 19h). História inventada.
Narrador: Caio, menino de cabelo preto curto, pele marrom, camiseta laranja e calça cinza-escura (mesmas cores na parte 2).
Premissa: na ilha do Caio o farol não tem faroleiro há quarenta anos e mesmo assim acende sozinho todo dia às seis da tarde;
quando a luz fica verde nenhum barco sai e no outro dia vem tempestade; regra: ninguém sobe no farol; a porta tem um cadeado
enferrujado e a chave sumiu com a última faroleira; ontem o farol piscou verde três vezes e o céu continuou limpo; hoje cedo
havia um pacote na porta do Caio com uma chave enferrujada e um bilhete: agora é a sua vez.
Cenários/cores: s0 CAPA close (noite, luz verde) -> ilha de dia (vivo) | s1 ilha fim de tarde, farol acende (tarde) |
s2 ilha à noite, luz verde -> tempestade com neblina (sombrio_noite/sombrio) | s3 ilha de dia, a regra (vivo) |
s4 porta do farol com cadeado, neblina (sombrio) | s5 noite limpa, 3 piscadas verdes + CLOSE (sombrio_noite) |
s6 casa azul de manhã cedo, pacote (frio) | s7 chave + bilhete + CLOSE final (frio)."""
from kit import *
import kit
from sombrio import *
from farol import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#1e1612', pele='#7a4a2a', roupa='#e8803a', calca='#3a3f46')
VERDE = (120, 240, 150); AMARELO = (255, 236, 150)

LINES = [
    "Na minha ilha, o farol não tem faroleiro há quarenta anos.",
    "Mesmo assim, ele acende sozinho, todo dia, às seis da tarde.",
    "Quando a luz fica verde, nenhum barco sai. No outro dia, sempre vem tempestade.",
    "A regra da ilha é uma só: ninguém sobe no farol.",
    "A porta tem um cadeado enferrujado. A chave sumiu com a última faroleira.",
    "Mas ontem, o farol piscou verde três vezes. E o céu continuou limpo.",
    "Hoje cedo, tinha um pacote na minha porta.",
    "Dentro, uma chave enferrujada. E um bilhete: agora é a sua vez.",
]
FALA_TIKTOK = "Comenta QUERO pra parte dois."
CTA_TEXTO = "COMENTA QUERO"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 5
FLASH = []
CHECK = [(0, 'farol', 6), (1, 'seis', 6), (2, 'verde', 4), (2, 'tempestade', 6), (3, 'regra', 4), (3, 'farol', 6),
         (4, 'cadeado', 6), (4, 'faroleira', 6), (5, 'tres', 6), (5, 'limpo', 6), (6, 'pacote', 6), (7, 'chave', 6), (7, 'vez', 10)]
CAM = {}
CAPA = 38


def SFX(s):
    s.thunk(2, 120, .8)
    s.patter(s.W(0, 'minha') - 4, s.W(0, 'minha') + 40, 4, .05)
    s.ting(s.W(1, 'seis'), .3)
    s.ting(s.W(2, 'verde'), .25); s.thunk(s.W(2, 'tempestade') - 2, 60, 1.0)
    s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.thunk(s.W(4, 'cadeado') - 2, 140, .6)
    for i in range(3): s.ting(s.W(5, 'verde') + i * 9, .2)
    s.trill(s.W(5, 'limpo'), .5, .12)
    s.thunk(s.W(6, 'pacote') - 2, 120, .6)
    s.ting(s.W(7, 'chave'), .3); s.thunk(s.W(7, 'vez') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def caio(c, x, f, feet=1900, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


@lru_cache(maxsize=2)
def porta_bg():
    p = Pen(W_, H_)
    for k in range(8):   # listras horizontais do farol de perto
        col = hexc('#c9524a') if k % 2 == 0 else hexc('#e8e4da')
        p.poly([(0, k * 300), (W_, k * 300), (W_, k * 300 + 300), (0, k * 300 + 300)], mul(col, .8))
    p.poly([(0, 1700), (W_, 1700), (W_, H_), (0, H_)], hexc('#7a7f82'))
    p.stroke([(0, 1700), (W_, 1700)], 7)
    p.shape([(370, 600), (870, 600), (870, 1700), (370, 1700)], hexc('#6a4a32'), hexc('#53392a'), 8, 16)
    for x in (470, 620, 770): p.stroke([(x, 620), (x, 1690)], 5, hexc('#53392a'))
    p.shape([(370, 900), (870, 900), (870, 940), (370, 940)], hexc('#4a4e50'), None, 5, 0)
    p.shape([(370, 1360), (870, 1360), (870, 1400), (370, 1400)], hexc('#4a4e50'), None, 5, 0)
    # cadeado enferrujado
    p.arc(780, 1130, 50, 60, 180, 360, 18, hexc('#7a7f82'))
    p.shape([(715, 1130), (845, 1130), (845, 1250), (715, 1250)], hexc('#b0703a'), hexc('#8a5228'), 6, 10)
    p.dot(780, 1180, 12, (36, 30, 32))
    for x, y in ((735, 1150), (820, 1220), (760, 1235)): p.dot(x, y, 9, hexc('#7a4a2a'))
    return p.img.resize((W_, H_), Image.LANCZOS)


def chuva(c, f, dens=1.0):
    d = ImageDraw.Draw(c); rnd = random.Random(f // 2)
    for i in range(int(90 * dens)):
        x = rnd.randint(0, W_); y = rnd.randint(0, H_)
        d.line((x, y, x - 30, y + 90), fill=(210, 220, 230, 130), width=4)


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close assustado + PARTE 1 + gancho
        c = ilha_bg('noite').copy(); facho(c, 160 + f * .3, VERDE)
        c = put_close(c, f, expr='choque', look=0, shake=.2, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'sombrio'
    g = f - CAPA
    c = ilha_bg('dia').copy()
    caio(c, 470, f, expr='neutro', look=.75)
    t = smooth(ramp(g, 0, 110))
    cam = (lerp(520, 640, t), lerp(1350, 1050, t), lerp(1.2, 1.02, easeOut(ramp(g, 0, 14))) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = ilha_bg('tarde').copy()
    se = wt(1, 'seis') - 3
    if f >= wt(1, 'acende') - 3: facho(c, 200 - 25 * math.sin(f * .04), AMARELO, ramp(f, wt(1, 'acende') - 3, wt(1, 'acende') + 8))
    caio(c, 380, f, expr='neutro', look=.75)
    cam = (621, lerp(1150, 950, smooth(ramp(f, 0, 120))), lerp(1.0, 1.1, smooth(ramp(f, 0, 120))) * (1 + .0009 * f) + .04 * kick(f, se, .6), 0); CAM[1] = cam
    return c, cam, 'tarde'


def s2(f):
    te = wt(2, 'outro') - 3
    if f < te:
        c = ilha_bg('noite').copy()
        v = wt(2, 'verde') - 3
        facho(c, 190 - 20 * math.sin(f * .05), VERDE if f >= v else AMARELO)
        caio(c, 380, f, expr='preocupado' if f >= v else 'neutro', look=.75)
        cam = (621, 1000, 1.05 * (1 + .0009 * f), 0); CAM[2] = cam
        return c, cam, 'sombrio_noite'
    c = ilha_bg('neblina').copy(); chuva(c, f)
    tp = wt(2, 'tempestade') - 3
    if tp <= f < tp + 4: c.alpha_composite(Image.new('RGBA', c.size, (255, 255, 255, 120)))
    cam = (621, 1050, lerp(1.2, 1.05, easeOut(ramp(f, te, te + 12))) * (1 + .0009 * f), 1.5 * math.sin(f * .2)); CAM[2] = cam
    return c, cam, 'sombrio'


def s3(f):
    c = ilha_bg('dia').copy()
    caio(c, 380, f, expr='preocupado', look=.75)
    r = wt(3, 'regra') - 3
    cam = (621, 1050, lerp(1.0, 1.12, smooth(ramp(f, 0, 120))) * (1 + .0009 * f) + .05 * kick(f, r, .6), 0); CAM[3] = cam
    return c, cam, 'vivo'


def s4(f):
    c = porta_bg().copy()
    nb = neblina_img(1.0); o2 = int(f * 2) % W_
    c.alpha_composite(nb.crop((o2, 0, o2 + W_, 420)), (0, 1500))
    ca = wt(4, 'cadeado') - 3
    t = smooth(ramp(f, 0, ca))
    cam = (lerp(621, 760, t), lerp(1150, 1180, t), lerp(1.0, 1.6, t) * (1 + .0009 * f), 0)
    if f > ca + 20: cam = (lerp(760, 621, smooth(ramp(f, ca + 20, ca + 60))), 1150, lerp(1.6, 1.15, smooth(ramp(f, ca + 20, ca + 60))) * (1 + .0009 * f), 0)
    CAM[4] = cam
    return c, cam, 'sombrio'


def s5(f):
    c = ilha_bg('noite').copy()
    d = ImageDraw.Draw(c)
    for k in range(40):   # céu limpo, estrelado
        rnd = random.Random(k); x, y = rnd.randint(0, W_), rnd.randint(60, 900)
        d.ellipse((x - 4, y - 4, x + 4, y + 4), fill=(240, 240, 220, 200))
    v = wt(5, 'verde') - 3
    for i in range(3):
        a = v + i * 9
        if a <= f < a + 6: facho(c, 185, VERDE, 1.0, abert=14)
    li = wt(5, 'limpo') - 3
    if f >= li + 4:   # CLOSE desconfiado
        c = put_close(c, f, expr='desconfiado', look=.5, **EU)
        cam = (621, 1104, lerp(1.25, 1.05, easeOut(ramp(f, li + 4, li + 14))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'sombrio_noite'
    caio(c, 380, f, expr='choque' if f >= v else 'neutro', look=.75)
    cam = (621, 1000, 1.05 * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'sombrio_noite'


def s6(f):
    c = ilha_bg('frio').copy()
    pa = wt(6, 'pacote') - 3
    pacote(c, 250, 1520, .75 * back(ramp(f, pa, pa + 8)))
    caio(c, 560, f, feet=1900, h=900, expr='choque' if f >= pa else 'neutro', look=-.75, flip=True)
    t = smooth(ramp(f, 0, pa))
    cam = (lerp(621, 380, t), lerp(1100, 1350, t), lerp(1.0, 1.35, t) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'frio'


def s7(f):
    c = ilha_bg('frio').copy().filter(ImageFilter.GaussianBlur(8)).convert('RGBA')
    ch = wt(7, 'chave') - 3; bi = wt(7, 'bilhete') - 3; vz = wt(7, 'vez')
    chave(c, 621, 900, 1.6 * back(ramp(f, ch, ch + 8)), rot=-10 + 4 * math.sin(f * .1))
    if f >= bi:
        b = bilhete_img('AGORA É|A SUA VEZ.', 560)
        s_ = back(ramp(f, bi, bi + 8))
        if s_ > .05:
            im = b.resize((max(4, int(b.width * s_ * 1.3)), max(4, int(b.height * s_ * 1.3))), Image.LANCZOS).rotate(4, Image.BICUBIC, expand=True)
            c.alpha_composite(im, (int(621 - im.width / 2), int(1300 - im.height / 2)))
    fim = vz + 10
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.35, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[7] = cam
        return c, cam, 'frio'
    cam = (621, 1100, 1.05 * (1 + .002 * f), 0); CAM[7] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 1', 540, 100, 1, 64, big=True)
            gancho(im, ['O FAROL ACENDE', 'SEM NINGUÉM LÁ'], 180, 1, 110)
        else:
            stamp(im, 'NA MINHA ILHA', 300, 640, back(ramp(f, CAPA + 2, CAPA + 10)), 70)
            q = wt(0, 'quarenta') - 3
            ax, ay = to_out(0, 700, 600)
            card(im, 'Farol', 'sem faroleiro há 40 anos', 300, 820, ramp(f, q, q + 10), alvo=(ax, ay))
    elif si == 1:
        se = wt(1, 'seis') - 3
        painel(im, 'HORA', '18:00', 260, 640, ramp(f, se, se + 10))
    elif si == 2:
        v = wt(2, 'verde') - 3; te = wt(2, 'outro') - 3
        if f < te: card(im, 'Luz verde', 'nenhum barco sai', 300, 760, ramp(f, v, v + 10))
        else: burst(im, 'TEMPESTADE', 330, 820, back(ramp(f, wt(2, 'tempestade') - 3, wt(2, 'tempestade') + 5)), 56)
    elif si == 3:
        r = wt(3, 'regra') - 3; n = wt(3, 'ninguem') - 3
        stamp(im, 'A REGRA', 300, 420, back(ramp(f, r, r + 8)), 110, big=True)
        card(im, 'Proibido', 'subir no farol', 290, 680, ramp(f, n, n + 10))
    elif si == 4:
        fa = wt(4, 'chave') - 3
        card(im, 'A chave', 'sumiu com a última faroleira', 540, 230, ramp(f, fa, fa + 10))
    elif si == 5:
        v = wt(5, 'verde') - 3; li = wt(5, 'limpo') - 3
        n = sum(1 for i in range(3) if f >= v + i * 9)
        if f < li + 4: painel(im, 'PISCADAS VERDES', str(n), 540, 240, ramp(f, v - 6, v + 4))
        else: stamp(im, 'SEM TEMPESTADE', 540, 250, back(ramp(f, li + 6, li + 14)), 70)
    elif si == 6:
        h_ = wt(6, 'hoje') - 3
        stamp(im, 'HOJE CEDO', 540, 160, back(ramp(f, h_, h_ + 8)), 70)
    elif si == 7:
        fim = wt(7, 'vez') + 10
        if f >= fim: stamp(im, 'A MINHA VEZ?', 540, 250, back(ramp(f, fim + 4, fim + 12)), 72, rot=3)
    return grao(im.convert('RGB'), lf)
