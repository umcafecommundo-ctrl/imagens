"""EXEMPLO do estilo SOMBRIO (pedido do Luis em 20/11/2026, a partir de um vídeo de referência):
mistério em 1ª pessoa ("Na minha cidade..."), cores frias e lavadas, neblina, cartões de informação (HUD),
carimbos de título, placar digital, onomatopeias, legenda de 1 palavra, voz grave e mais calma, sem música.
História inventada: o relógio da praça que anda pra trás a cada mentira."""
from kit import *
import kit
from sombrio import *

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'

LINES = [
    "Na minha cidade, o relógio da praça anda pra trás toda vez que alguém mente.",
    "Ninguém sabe quem construiu. Ele já estava lá quando a cidade nasceu.",
    "Mas todo morador conhece a regra: ao meio-dia, ele tem que bater doze badaladas certinhas.",
    "Se estiver atrasado, a prefeitura tranca as portas, e a cidade fica em silêncio até alguém confessar.",
    "Ontem, ele estava sete minutos atrasado. Sete mentiras numa manhã só.",
    "Hoje cedo, eu passei pela praça, e o ponteiro estava parado.",
    "Só que o relógio não para quando ninguém mente. Ele para quando alguém mente sem parar.",
    "E a única pessoa na praça... era eu.",
]
FALA_TIKTOK = "Quer saber o que eu fiz? Comenta parte dois, e segue pra não perder!"
CTA_TEXTO = "PARTE 2?"
TWIST = 6
FLASH = []
CHECK = [(0, 'relogio', 4), (0, 'mente', 6), (1, 'nasceu', 6), (2, 'regra', 4), (2, 'badaladas', 6), (3, 'tranca', 4),
         (3, 'silencio', 6), (4, 'sete', 4), (4, 'mentiras', 6), (5, 'parado', 6), (6, 'parar', 6), (7, 'eu', 10)]

CAM = {}


def SFX(s):
    for si in range(8): s.thunk(s.W(si, LINES[si].split()[0].strip(',.:')) - 4, 55, .18)
    s.thunk(s.W(0, 'tras') - 2, 300, .4); s.ting(s.W(0, 'mente'), .25)
    s.whoosh(s.W(1, 'nasceu') - 6, .8, .25)
    s.thunk(s.W(2, 'regra') - 2, 90, .7)
    for i in range(4): s.thunk(s.W(2, 'badaladas') - 2 + i * 12, 110, .6)
    s.thunk(s.W(3, 'tranca') - 2, 80, 1.0); s.thunk(s.W(3, 'tranca') + 4, 200, .5)
    for i in range(7): s.thunk(s.W(4, 'sete') - 2 + i * 4, 700, .2)
    s.thunk(s.W(5, 'parado') - 2, 120, .7)
    s.whoosh(s.W(6, 'parar') - 6, .9, .4)
    s.thunk(s.W(7, 'eu') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


@lru_cache(maxsize=2)
def prefeitura_img(fechada=0):
    p = Pen(1100, 1000)
    col = hexc('#a3aaa6')
    p.shape([(60, 1000), (60, 330), (1040, 330), (1040, 1000)], col, mul(col, .84), 7, 20)
    p.shape([(20, 330), (550, 90), (1080, 330)], mul(col, .78), None, 7, 0)
    for x in (160, 330, 770, 940):
        p.shape([(x - 34, 990), (x - 34, 420), (x + 34, 420), (x + 34, 990)], hexc('#d6dad6'), hexc('#b4b9b5'), 6, 8)
    p.shape([(420, 1000), (420, 560), (680, 560), (680, 1000)], hexc('#2b2f31'), None, 6, 0)
    return p.img.resize((1100, 1000), Image.LANCZOS)


def portas(c, x0, y0, a):
    """duas folhas de porta fechando (a 0 aberta .. 1 fechada) sobre o vão 420..680 / 560..1000 do prédio."""
    d = ImageDraw.Draw(c)
    w = 130 * a
    if w < 2: return
    for side in (0, 1):
        xa = x0 + 420 if side == 0 else x0 + 680 - w
        d.rectangle((xa, y0 + 560, xa + w, y0 + 1000), fill=(96, 74, 56, 255), outline=(36, 30, 32, 255), width=6)


# ---------------------------------------------------------------- cenas (mundo)
def s0(f):
    c = rua(f, 0)
    tr = wt(0, 'tras') - 3
    m = 53 - 2 * max(0, f - tr) * .5 if f >= tr else 53
    put_torre(c, 880, 1540, 1320, 11, m)
    me = wt(0, 'mente') - 3
    put_menino(c, 380, 1760, 980, f, expr='preocupado' if f >= me else 'neutro', look=.75)
    t = smooth(ramp(f, 4, wt(0, 'relogio') + 6))
    cam = (lerp(400, 640, t), lerp(1180, 1200, t), lerp(1.6, 1.05, t) * (1 + .0008 * f), 0)
    CAM[0] = cam
    return c, cam, 'sombrio'


def s1(f):
    c = rua(f, f * 9)
    put_menino(c, 430, 1760, 980, f, walk=1, expr='neutro', look=.25)
    cam = (621, 1180, 1.12 * (1 + .0006 * f), 0); CAM[1] = cam
    return c, cam, 'sombrio'


def s2(f):
    c = rua(f, 900 + f * 9)
    put_menino(c, 430, 1760, 980, f, walk=1, expr='neutro', look=.5)
    b = wt(2, 'badaladas') - 3
    sh = 6 * math.sin(f * 2.1) if b <= f < b + 40 else 0
    cam = (621 + sh, 1180, 1.12 * (1 + .0006 * f), sh * .2); CAM[2] = cam
    return c, cam, 'sombrio'


def s3(f):
    c = rua(f, 0)
    tr = wt(3, 'tranca') - 3
    im = prefeitura_img(); x0, y0 = 621 - 550, 1540 - 1000
    c.alpha_composite(im, (x0, y0))
    portas(c, x0, y0, easeOut(ramp(f, tr - 4, tr + 6)))
    put_menino(c, 300, 1800, 900, f, expr='preocupado' if f >= tr else 'neutro', look=.6)
    t = smooth(ramp(f, 0, 90))
    cam = (621, lerp(1180, 1250, t) + kick(f, tr + 2, .9) * 14, lerp(1.0, 1.12, t), 0); CAM[3] = cam
    return c, cam, 'sombrio'


def s4(f):
    c = rua(f, 0)
    st = wt(4, 'sete') - 3
    put_torre(c, 900, 1540, 1320, 11, 53)
    put_menino(c, 360, 1760, 980, f, expr='preocupado', look=.75)
    cam = (640, 1180, 1.08 * (1 + .0008 * f), 0); CAM[4] = cam
    return c, cam, 'sombrio'


def s5(f):
    c = rua(f, 0, neb=1.7)
    pa = wt(5, 'parado') - 3
    put_torre(c, 900, 1540, 1320, 11, 53)
    x = lerp(-150, 380, easeOut(ramp(f, 0, pa - 6)))
    walking = f < pa - 6
    put_menino(c, x, 1760, 980, f, walk=1 if walking else 0, expr='choque' if f >= pa else 'neutro', look=.75)
    cam = (640, 1180 + kick(f, pa, .7) * 10, 1.06 * (1 + .0008 * f), 0); CAM[5] = cam
    return c, cam, 'sombrio'


def s6(f):
    c = rua(f, 0, neb=1.4)
    pr = wt(6, 'parar') - 3
    tremor = .6 * math.sin(f * 1.7) if f >= pr else .15 * math.sin(f * .9)
    put_torre(c, 900, 1540, 1320, 11, 53 + tremor)
    t = smooth(ramp(f, 0, 100))
    sh = 5 * math.sin(f * 2.3) if f >= pr else 0
    cam = (900 + sh, lerp(900, 720, t), lerp(1.6, 2.4, t) * (1 + .0006 * f), sh * .3); CAM[6] = cam
    return c, cam, 'sombrio'


def s7(f):
    c = rua(f, 0, noite=True, neb=1.6)
    eu = wt(7, 'eu') - 3
    put_torre(c, 1020, 1540, 1320, 11, 53, noite=True)
    put_menino(c, 520, 1760, 980, f, expr='choque' if f >= eu else 'preocupado', look=0 if f >= eu else .6)
    t = smooth(ramp(f, 0, 120))
    cam = (lerp(640, 540, t), lerp(1200, 1060, t), lerp(1.05, 1.55, t) * (1 + .0006 * f), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD (tela)
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        stamp(im, 'NA MINHA CIDADE', 540, 150, back(ramp(f, 0, 8)) * (1 - ramp(f, 70, 78)), 72)
        r = wt(0, 'relogio') - 3
        cx, cy = to_out(0, 880, 1540 - 1320 * .62)
        card(im, 'Relógio da praça', 'anda pra trás a cada mentira', 300, 330, ramp(f, r, r + 12), alvo=(cx - 60, cy))
        me = wt(0, 'mente') - 3
        hx, hy = to_out(0, 380, 1760 - 980 * .78)
        burst(im, '?!', hx + 150, hy - 60, back(ramp(f, me, me + 8)), 64)
    elif si == 1:
        stamp(im, 'O RELÓGIO', 230, 150, back(ramp(f, 0, 8)), 60)
        s_ = wt(1, 'sabe') - 3; n = wt(1, 'nasceu') - 3
        interrog(im, 540, 470, f, back(ramp(f, s_, s_ + 8)) * (1 - ramp(f, n - 4, n)))
        card(im, 'Ninguém sabe', 'quem construiu', 560, 620, ramp(f, s_, s_ + 10) * (1 - ramp(f, n - 4, n)))
        card(im, 'Mais velho', 'que a própria cidade', 560, 620, ramp(f, n, n + 10))
    elif si == 2:
        rg = wt(2, 'regra') - 3
        a = ramp(f, rg + 18, rg + 30)
        stamp(im, 'A REGRA', lerp(540, 220, a), lerp(330, 170, a), back(ramp(f, rg, rg + 8)) * lerp(1.4, .7, a), 96, big=True)
        md = wt(2, 'meio-dia') - 3
        painel(im, 'MEIO-DIA', '12:00', 760, 420, ramp(f, md, md + 10))
        b = wt(2, 'badaladas') - 3
        for i in range(3):
            burst(im, 'DONG!', (820, 760, 560)[i], (720, 900, 330)[i], back(ramp(f, b + i * 12, b + i * 12 + 8)) * (1 - ramp(f, b + i * 12 + 22, b + i * 12 + 28)), 56, rot=(-8, 6, -3)[i])
        card(im, 'Regra da cidade', 'ao meio-dia, 12 badaladas certinhas', 560, 640, ramp(f, b + 40, b + 50))
    elif si == 3:
        tr = wt(3, 'tranca') - 3
        burst(im, 'TRANC!', 760, 520, back(ramp(f, tr, tr + 8)) * (1 - ramp(f, tr + 30, tr + 36)), 64)
        si_ = wt(3, 'silencio') - 3
        card(im, 'Silêncio', 'até alguém confessar', 560, 420, ramp(f, si_, si_ + 10))
    elif si == 4:
        stamp(im, 'ONTEM', 200, 150, back(ramp(f, 0, 8)), 64)
        st = wt(4, 'sete') - 3
        k = int(clamp((f - st) / 18) * 7)
        g = 1 - (f - st) % 6 / 6 if st <= f < st + 24 else 0
        painel(im, 'ATRASO (MIN)', f'-{k}' if k else '0', 560, 290, ramp(f, 2, 12), glitch=g)
        me = wt(4, 'mentiras') - 3
        card(im, '7 mentiras', 'numa manhã só', 330, 700, ramp(f, me, me + 10))
    elif si == 5:
        stamp(im, 'HOJE CEDO', 230, 150, back(ramp(f, 0, 8)), 64)
        pa = wt(5, 'parado') - 3
        cx, cy = to_out(5, 900, 1540 - 1320 * .62)
        burst(im, '?!', cx - 170, cy - 150, back(ramp(f, pa, pa + 8)), 60)
        card(im, 'Ponteiro', 'parado', 300, 470, ramp(f, pa + 4, pa + 14), alvo=(cx - 40, cy))
    elif si == 6:
        n = wt(6, 'ninguem') - 3; pr = wt(6, 'parar') - 3
        card(im, 'Ele não para', 'quando ninguém mente', 540, 300, ramp(f, n, n + 10) * (1 - ramp(f, pr - 6, pr - 2)))
        g = 1 if f >= pr and (f // 3) % 2 else 0
        painel(im, 'MENTIRAS', '???', 540, 330, ramp(f, pr, pr + 8), glitch=g)
    elif si == 7:
        u = wt(7, 'unica') - 3
        painel(im, 'NA PRAÇA', '1', 820, 360, ramp(f, u, u + 10))
    return grao(im.convert('RGB'), lf)
