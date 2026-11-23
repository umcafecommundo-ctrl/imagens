"""Formato MISTÉRIO: "As batidas das três", PARTE 1 (23/11/2026, 19h). História inventada.
Narrador: menino ruivo de cabelo curto, pele clara, macacão azul (mesmas cores na parte 2).
Premissa: na estação espacial onde ele mora, alguém bate na janela grande toda noite às três da manhã: sempre três batidas,
do lado de fora, onde não tem ar nem ninguém; regra (placa na parede): nunca bata de volta; ninguém sabe quem escreveu a placa;
ontem as batidas vieram na janelinha do quarto dele, e foram quatro; gancho: e ele bateu de volta.
Cenários/cores: s0 CAPA close (corredor à noite) -> corredor à noite (sombrio_noite) | s1 janela grande de perto, TOC (sombrio_noite) |
s2 lado de fora, espaço e casco (frio) | s3 corredor de dia, placa da regra (vivo) | s4 corredor de dia, a placa (tarde) |
s5 corredor à noite, silêncio + CLOSE (sombrio_noite) | s6 cabine à noite, 4 batidas (sombrio_noite) | s7 bate de volta + CLOSE final (sombrio_noite)."""
from kit import *
import kit
from sombrio import *
from estacao3 import *
from carrossel import gancho

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#b5532a', pele='#f0c8a8', roupa='#4a78c8', calca='#2e4a80')

LINES = [
    "Na estação espacial onde eu moro, alguém bate na janela toda noite, às três da manhã.",
    "São sempre três batidas. Toc. Toc. Toc. Do lado de fora.",
    "Só que lá fora não tem ar, não tem chão. Não tem ninguém.",
    "A regra da estação é uma só: nunca bata de volta.",
    "Ninguém sabe quem escreveu essa placa. Ela já estava lá quando eu nasci.",
    "Mas ontem, às três, as batidas não vieram na janela grande.",
    "Vieram na janelinha do meu quarto. E não eram três. Eram quatro.",
    "E, sem pensar... eu bati de volta.",
]
FALA_TIKTOK = "Comenta QUERO pra parte dois."
CTA_TEXTO = "COMENTA QUERO"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 6
FLASH = []
CHECK = [(0, 'janela', 6), (0, 'tres', 6), (1, 'toc', 4), (1, 'fora', 6), (2, 'ar', 6), (2, 'ninguem', 6),
         (3, 'regra', 4), (3, 'volta', 6), (4, 'placa', 6), (4, 'nasci', 6), (5, 'tres', 6), (5, 'grande', 10),
         (6, 'janelinha', 6), (6, 'quatro', 6), (7, 'bati', 4), (7, 'volta', 12)]
CAM = {}
CAPA = 36


def SFX(s):
    s.thunk(2, 120, .6)
    s.ting(s.W(0, 'tres'), .25)
    for k in range(3): s.thunk(s.W(1, 'toc', k) - 1, 180, .9)
    s.whoosh(s.W(2, 'so') - 4, .8, .3)
    s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.thunk(s.W(4, 'placa') - 2, 140, .5)
    s.ting(s.W(5, 'tres'), .3); s.trill(s.W(5, 'grande'), .5, .12)
    q = s.W(6, 'quatro')
    for k in range(4): s.thunk(s.W(6, 'janelinha') + 6 + k * 7, 180, .8)
    s.thunk(q - 2, 60, .8)
    s.thunk(s.W(7, 'bati') - 1, 180, 1.0)
    s.thunk(s.W(7, 'volta') + 8, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def eu(c, x, f, feet=1950, h=900, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def tremor(f, f0, amp=6):
    return amp * math.sin(f * 2.1) * (1 - ramp(f, f0, f0 + 8)) if f >= f0 else 0


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = corredor_bg('noite').copy()
        c = put_close(c, f, expr='medo', look=0, shake=.3, **EU)
        cam = (621, 1104, 1.0 * (1 + .0009 * f), 0); CAM[0] = cam
        return c, cam, 'frio'
    g = f - CAPA
    c = corredor_bg('noite').copy()
    eu(c, 330, f, expr='preocupado' if f >= wt(0, 'bate') - 3 else 'neutro', look=.75)
    t = smooth(ramp(g, 0, 120))
    cam = (lerp(500, 700, t), lerp(1350, 1150, t), lerp(1.25, 1.02, easeOut(ramp(g, 0, 16))) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'sombrio_noite'


def s1(f):
    c = corredor_bg('noite').copy()
    sh = sum(tremor(f, wt(1, 'toc', k) - 2, 10) for k in range(3))
    cam = (JAN[0] + sh, JAN[1] + 40, lerp(1.7, 2.0, smooth(ramp(f, 0, 90))) * (1 + .0009 * f) + sum(.05 * kick(f, wt(1, 'toc', k) - 2, .6) for k in range(3)), 0)
    fo = wt(1, 'fora') - 3
    if f > fo: cam = (lerp(JAN[0], 621, smooth(ramp(f, fo, fo + 20))), lerp(JAN[1] + 40, 1150, smooth(ramp(f, fo, fo + 20))), lerp(2.0, 1.05, smooth(ramp(f, fo, fo + 20))) * (1 + .0009 * f), 0)
    if f > fo: eu(c, 330, f, expr='choque', look=.75)
    CAM[1] = cam
    return c, cam, 'sombrio_noite'


def s2(f):
    c = casco_bg().copy()
    t = smooth(ramp(f, 0, 150))
    cam = (lerp(800, 500, t), lerp(700, 1000, t), lerp(1.2, 1.05, t) * (1 + .0009 * f), lerp(-3, 2, t)); CAM[2] = cam
    return c, cam, 'frio'


def s3(f):
    c = corredor_bg('dia').copy()
    nu = wt(3, 'nunca') - 3
    placa(c, 360, 700, .9 * back(ramp(f, nu, nu + 8)))
    eu(c, 330, f, expr='preocupado', look=.75)
    r = wt(3, 'regra') - 3
    cam = (621, 1100, lerp(1.0, 1.1, smooth(ramp(f, 0, 120))) * (1 + .0009 * f) + .05 * kick(f, r, .6), 0); CAM[3] = cam
    return c, cam, 'vivo'


def s4(f):
    c = corredor_bg('dia').copy()
    placa(c, 360, 700, .9)
    if f > wt(4, 'ja') + 4: eu(c, 900, f, expr='neutro', look=-.75, flip=True)
    t = smooth(ramp(f, 0, wt(4, 'placa') + 6))
    cam = (lerp(621, 420, t), lerp(1100, 800, t), lerp(1.0, 1.6, t) * (1 + .0009 * f), 0)
    na = wt(4, 'ja') - 3
    if f > na: cam = (lerp(420, 621, smooth(ramp(f, na, na + 24))), lerp(800, 1100, smooth(ramp(f, na, na + 24))), lerp(1.6, 1.05, smooth(ramp(f, na, na + 24))) * (1 + .0009 * f), 0)
    CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = corredor_bg('noite').copy()
    gr = wt(5, 'grande') - 3
    if f >= gr + 4:   # CLOSE desconfiado
        c = put_close(c, f, expr='desconfiado', look=.5, **EU)
        cam = (621, 1104, lerp(1.15, 1.04, easeOut(ramp(f, gr + 4, gr + 12))) * (1 + .0009 * f), 0); CAM[5] = cam
        return c, cam, 'sombrio_noite'
    eu(c, 330, f, expr='neutro', look=.75)
    cam = (lerp(700, 760, smooth(ramp(f, 0, gr))), 1150, lerp(1.05, 1.15, smooth(ramp(f, 0, gr))) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'sombrio_noite'


def s6(f):
    c = cabine_bg('noite').copy()
    k0 = wt(6, 'janelinha') + 6
    sh = sum(tremor(f, k0 + k * 7 - 1, 8) for k in range(4))
    eu(c, 640, f, feet=1900, expr='choque' if f >= k0 else 'preocupado', look=.75)
    t = smooth(ramp(f, 0, k0))
    cam = (lerp(621, 800, t) + sh, lerp(1150, 1060, t), lerp(1.0, 1.3, t) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'sombrio_noite'


def s7(f):
    c = cabine_bg('noite').copy()
    ba = wt(7, 'bati') - 3
    fim = wt(7, 'volta') + 8
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.35, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[7] = cam
        return c, cam, 'sombrio_noite'
    x = lerp(520, 760, smooth(ramp(f, 0, ba)))
    eu(c, x, f, feet=1900, walk=1 if f < ba else 0, expr='preocupado', look=.75)
    cam = (lerp(700, 800, smooth(ramp(f, 0, ba))) + tremor(f, ba + 2, 8), 1050, lerp(1.1, 1.3, smooth(ramp(f, 0, ba))) * (1 + .0009 * f) + .05 * kick(f, ba + 2, .6), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'PARTE 1', 540, 100, 1, 64, big=True)
            gancho(im, ['ALGUÉM BATE', 'NA JANELA DO ESPAÇO'], 180, 1, 100)
        else:
            stamp(im, 'NA MINHA ESTAÇÃO', 330, 230, back(ramp(f, CAPA + 2, CAPA + 10)), 64)
            q = wt(0, 'tres') - 3
            painel(im, 'TODA NOITE', '03:00', 800, 460, ramp(f, q, q + 10), w=380)
    elif si == 1:
        for k in range(3):
            a = wt(1, 'toc', k) - 2
            if f >= a: burst(im, 'TOC', [300, 780, 540][k], [330, 380, 1240][k], back(ramp(f, a, a + 6)), 60, rot=[-8, 8, -4][k])
    elif si == 2:
        a = wt(2, 'ar') - 3; n = wt(2, 'ninguem') - 3
        card(im, 'Lá fora', 'sem ar, sem chão', 300, 300, ramp(f, a, a + 10))
        stamp(im, 'NINGUÉM', 700, 560, back(ramp(f, n, n + 8)), 90)
    elif si == 3:
        r = wt(3, 'regra') - 3
        stamp(im, 'A REGRA', 720, 230, back(ramp(f, r, r + 8)), 100, big=True)
    elif si == 4:
        n = wt(4, 'ninguem') - 3; na = wt(4, 'nasci') - 3
        interrog(im, 540, 260, f, ramp(f, n, n + 8))
        card(im, 'A placa', 'estava lá antes de mim', 330, 1250, ramp(f, na, na + 10))
    elif si == 5:
        q = wt(5, 'tres') - 3; gr = wt(5, 'grande') - 3
        if f < gr + 4: painel(im, 'ONTEM', '03:00', 780, 300, ramp(f, q, q + 10), w=380)
        else: stamp(im, 'SILÊNCIO', 540, 250, back(ramp(f, gr + 6, gr + 14)), 80)
    elif si == 6:
        k0 = wt(6, 'janelinha') + 6
        n = sum(1 for k in range(4) if f >= k0 + k * 7 - 1)
        painel(im, 'BATIDAS', str(n), 300, 280, ramp(f, k0 - 8, k0), glitch=.6 if f >= wt(6, 'quatro') - 3 else 0, w=360)
        if f >= wt(6, 'quatro') - 3: stamp(im, 'QUATRO?!', 760, 520, back(ramp(f, wt(6, 'quatro') - 3, wt(6, 'quatro') + 5)), 80)
    elif si == 7:
        ba = wt(7, 'bati') - 3; fim = wt(7, 'volta') + 8
        if f < fim: burst(im, 'TOC', 760, 360, back(ramp(f, ba + 2, ba + 8)), 64)
        else: stamp(im, 'E AGORA?', 540, 250, back(ramp(f, fim + 4, fim + 12)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
