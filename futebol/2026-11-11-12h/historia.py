"""anima.futebol — 11/11/2026 12h — Seleção Brasileira: Ancelotti esboça o time para pegar o Japão.
Fontes (conferidas em 11/11/2026): CNN Brasil/Itatiaia (treino de 11/11 em Singapura; coletivo com Bento; Wesley, Jair,
Gabriel Magalhães e Douglas Santos; Marlon Gomes e Gabriel Bontempo; Rayan, Estêvão, Raphinha e Vinicius Júnior; depois
Andrey Santos e João Gomes testados com Bontempo no 4-3-3; André Luiz também; Bruno Guimarães poupado; Japão 14/11 7h15 e
Singapura 17/11 7h, Estádio Nacional de Singapura); Diário de Goiás (mesma defesa; Estêvão pela direita, Vini pela
esquerda, Raphinha centralizado; meio-campo indefinido; Bruno Guimarães fora da parte mais intensa pelo 3º dia, controle
de carga; mesmas datas/local); Metrópoles e A Tarde (grupo completo a partir de 11/11; jogo 14/11 7h15 Estádio Nacional).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD)
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Vini Júnior, Raphinha e Estêvão: esse é o ataque que Ancelotti testou para pegar o Japão.",
    "Com o grupo completo em Singapura, a Seleção fez o primeiro treino com cara de time titular.",
    "No gol, Bento. Na defesa, Wesley, Jair, Gabriel Magalhães e Douglas Santos.",
    "Na frente, Estêvão pela direita, Vini pela esquerda e Raphinha mais centralizado.",
    "Mas a dúvida é o meio-campo: Ancelotti testou Bontempo, Marlon Gomes, Andrey Santos e João Gomes.",
    "E Bruno Guimarães foi poupado de novo, por controle de carga.",
    "Brasil e Japão jogam no sábado, às sete e quinze da manhã de Brasília, no Estádio Nacional de Singapura.",
]
CAPTXT = [
    "Vini Júnior, Raphinha e Estêvão:|esse é o ataque que Ancelotti testou para pegar o Japão.",
    "Com o grupo completo em Singapura, a Seleção|fez o primeiro treino com cara de time titular.",
    "No gol, Bento. Na defesa, Wesley, Jair,|Gabriel Magalhães e Douglas Santos.",
    "Na frente, Estêvão pela direita, Vini pela esquerda|e Raphinha mais centralizado.",
    "Mas a dúvida é o meio-campo: Ancelotti testou Bontempo,|Marlon Gomes, Andrey Santos e João Gomes.",
    "E Bruno Guimarães foi poupado de novo,|por controle de carga.",
    "Brasil e Japão jogam no sábado, às 7h15 de Brasília,|no Estádio Nacional de Singapura.",
]
FALA_TIKTOK = "Quem você bota no meio-campo? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM NO MEIO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Estevao', 4), (0, 'Japao', 4), (1, 'titular', 4), (2, 'Bento', 4), (2, 'Douglas', 4),
         (3, 'centralizado', 4), (4, 'duvida', 4), (4, 'Joao', 4), (5, 'poupado', 4), (6, 'quinze', 4), (6, 'Nacional', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
TEC = ('#23283a', '#23283a', '#23283a')


def put_cal(c, dia, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, 'NOV'), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    vi = wt(0, 'Vini') - 3; ra = wt(0, 'Raphinha') - 3; es = wt(0, 'Estevao') - 3; ja = wt(0, 'Japao') - 3
    for x, f0, nome, sd, sk, hair in ((330, vi, 'VINI JR.', 2, 3, '#111111'), (640, ra, 'RAPHINHA', 3, 1, '#2b1d14'),
                                      (950, es, 'ESTÊVÃO', 4, 2, '#111111')):
        if f < f0 - 4: continue
        y = lerp(2500, 2010, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, y, 800, f, sd, cores=BRA, faixa=BRA_F, arms='up' if f >= ja else 'cintura', expr='grin', skin=sk, hair=hair)
        put_placa(c, nome, BRA, x, 1150 + (60 if x == 640 else 0), f, f0, 50, -3 if x < 640 else 3)
    num(c, 'O ATAQUE', 640, 720, f, wt(0, 'ataque') - 3, 120, -4)
    num(c, 'CONTRA O JAPÃO', 640, 880, f, ja, 90, 3)
    z = lerp(1.25, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ja, .7)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = CEN('cidade', 'dusk').copy()
    co = wt(1, 'completo') - 3; si = wt(1, 'Singapura') - 3; ti = wt(1, 'titular') - 3
    for i, (x, sd, sk) in enumerate(((260, 2, 1), (640, 3, 3), (1000, 4, 0))):
        xx = x + lerp(-600, 0, easeOut(ramp(f, i * 4, i * 4 + 22)))
        if i == 1:
            put_jog(c, xx, 2000, 820, f, 9, cores=TEC, faixa=None, arms='point' if f >= ti else 'cintura', expr='proud', skin=0, hair='#9a9a9a')
        else:
            put_jog(c, xx, 1960, 760, f, sd, cores=BRA, faixa=BRA_F, walk=(f * .05) % 1 if f < 30 else 0,
                    arms='run' if f < 30 else 'joinha', expr='grin', skin=sk)
    put_placa(c, 'ANCELOTTI', TEC, 640, 1120, f, wt(1, 'Selecao') - 3, 60, -3)
    num(c, 'GRUPO COMPLETO', 640, 720, f, co, 100, -4)
    num(c, 'SINGAPURA', 640, 870, f, si, 110, 3)
    num(c, 'CARA DE TITULAR', 640, 1360, f, ti, 84, -3)
    return c, (lerp(600, 680, smooth(f / 120)), 1420, 1.06 * (1 + .0008 * f), 0), 'dusk'


def s2(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c, x=640)
    be = wt(2, 'Bento') - 3
    put_goleiro(c, f, ('#2a9d8f', '#111111', '#111111'), None, gx=660, arms='up' if f >= be else 'hang', expr='grin', skin=1)
    put_placa(c, 'BENTO', ('#2a9d8f', '#ffffff', '#ffffff'), 640, 1150, f, be, 46, -3)
    num(c, 'NO GOL', 640, 720, f, wt(2, 'gol') - 3, 100, -3)
    num(c, 'DEFESA', 640, 860, f, wt(2, 'defesa') - 3, 100, 3)
    for i, (x, nome, w, sk, hair) in enumerate(((300, 'WESLEY', 'Wesley', 3, '#111111'), (530, 'JAIR', 'Jair', 2, '#111111'),
                                                (760, 'G. MAGALHÃES', 'Gabriel', 1, '#2b1d14'), (990, 'DOUGLAS SANTOS', 'Douglas', 2, '#111111'))):
        f0 = wt(2, w) - 3
        if f < f0 - 4: continue
        y = lerp(2500, 2010, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, y, 640, f, 10 + i, cores=BRA, faixa=BRA_F, arms='cintura', expr='stern', skin=sk, hair=hair)
        put_placa(c, nome, BRA, x, 1250 if i % 2 == 0 else 1320, f, f0, 32, -3 if i % 2 else 3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0012 * f)
    return c, (640 + 25 * math.sin(f * .05), lerp(1380, 1460, smooth(f / 120)), z, .8 * math.sin(f * .04)), 'golden'


def s3(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=700)
    ce = wt(3, 'centralizado') - 3
    put_goleiro(c, f, ('#ff8c1a', '#111111', '#111111'), None, gx=720, arms='shrug', expr='shock' if f >= ce + 6 else 'nervous', skin=0)
    es = wt(3, 'Estevao') - 3; vi = wt(3, 'Vini') - 3; ra = wt(3, 'Raphinha') - 3
    put_jog(c, 1000, 2000, 760, f, 4, cores=BRA, faixa=BRA_F, arms='run', expr='grin', skin=2, hair='#111111', flip=True)
    put_placa(c, 'ESTÊVÃO', BRA, 1000, 1180, f, es, 40, 3)
    put_jog(c, 260, 2000, 760, f, 2, cores=BRA, faixa=BRA_F, arms='run', expr='grin', skin=3, hair='#111111')
    put_placa(c, 'VINI JR.', BRA, 260, 1180, f, vi, 40, -3)
    put_jog(c, 560, 2020, 860, f, 3, cores=BRA, faixa=BRA_F, arms='up' if f >= ce + 8 else 'run', kick=pulse(f, ce - 5, 5),
            expr='grin', skin=1)
    put_placa(c, 'RAPHINHA', BRA, 560, 1080, f, ra, 50, -3)
    rb = raio_bola(860)
    if f < ce - 3: bx, by, r = 660, 2020 - rb, rb
    else:
        t = ramp(f, ce - 3, ce + 6)
        bx, by, r = lerp(660, gx + 90, t), lerp(2020 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, 'DIREITA', 930, 720, f, wt(3, 'direita') - 3, 72, 4)
    num(c, 'ESQUERDA', 350, 720, f, wt(3, 'esquerda') - 3, 72, -4)
    num(c, 'CENTRALIZADO', 640, 880, f, ce, 96, -3)
    k = kick(f, ce + 4)
    return c, (640 + 30 * math.sin(f * .03), 1420 + k * 10, lerp(1.0, 1.06, smooth(f / 110)), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    du = wt(4, 'duvida') - 3
    num(c, 'MEIO-CAMPO?', 640, 720, f, du, 120, -4)
    for i, (x, nome, w, sk, hair) in enumerate(((300, 'BONTEMPO', 'Bontempo', 1, '#2b1d14'), (530, 'MARLON GOMES', 'Marlon', 3, '#111111'),
                                                (760, 'ANDREY SANTOS', 'Andrey', 2, '#111111'), (990, 'JOÃO GOMES', 'Joao', 3, '#111111'))):
        f0 = wt(4, w) - 3
        if f < f0 - 4: continue
        y = lerp(2500, 2010, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, y, 640, f, 14 + i, cores=BRA, faixa=BRA_F, arms='shrug' if f < f0 + 10 else 'cintura', expr='nervous', skin=sk, hair=hair)
        put_placa(c, nome, BRA, x, 1250 if i % 2 == 0 else 1320, f, f0, 32, -3 if i % 2 else 3)
    if f >= du: num(c, '?', 640, 1000, f, du + 4, int(200 + 10 * math.sin(f * .3)), 0)
    k = kick(f, du, .8)
    return c, (640, 1420 + k * 10, lerp(1.0, 1.05, smooth(f / 120)), lerp(0, 2, smooth(f / 120)) + k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    po = wt(5, 'poupado') - 3; ca = wt(5, 'carga') - 3
    put_jog(c, 640, 2030, 900, f, 6, cores=BRA, faixa=BRA_F, arms='joinha' if f >= ca else 'hang', expr='smug' if f >= ca else 'neutral', skin=1)
    put_placa(c, 'BRUNO GUIMARÃES', BRA, 640, 1080, f, wt(5, 'Bruno') - 3, 54, -3)
    num(c, 'POUPADO', 640, 720, f, po, 140, -4)
    num(c, 'CONTROLE DE CARGA', 640, 880, f, ca, 80, 3)
    k = kick(f, po, .7)
    return c, (640, 1420 + k * 8, lerp(1.04, 1.14, smooth(f / 90)), k), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    br = wt(6, 'Brasil') - 3; ja = wt(6, 'Japao') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, br - 8, br + 8)))
    ax = lerp(1550, 930, easeOut(ramp(f, ja - 8, ja + 8)))
    put_jog(c, bx, 2010, 860, f, 5, cores=BRA, faixa=BRA_F, arms='cintura', expr='stern', skin=2, look=1)
    put_jog(c, ax, 2010, 860, f, 6, cores=JAP, faixa=JAP_F, arms='cintura', expr='smug', skin=0, hair='#111111', look=-1)
    put_placa(c, 'BRASIL', BRA, 330, 1180, f, br + 2, 64, -4)
    put_placa(c, 'JAPÃO', JAP, 930, 1180, f, ja + 2, 64, 4)
    num(c, 'X', 640, 1520, f, ja + 4, 160)
    put_cal(c, '14', 300, 780, .6, f, wt(6, 'sabado') - 3)
    num(c, '7H15', 840, 780, f, wt(6, 'quinze') - 3, 140, -4)
    num(c, 'ESTÁDIO NACIONAL', 640, 960, f, wt(6, 'Nacional') - 3, 80, 3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ja, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'Vini') - 3, 140, .8)
    s.thunk(s.W(0, 'Raphinha') - 3, 140, .8)
    s.thunk(s.W(0, 'Estevao') - 3, 140, .8)
    s.ting(s.W(1, 'titular') - 3, .3)
    s.ting(s.W(2, 'Bento') - 3, .25)
    s.thunk(s.W(3, 'centralizado') - 3, 180, .9)
    s.ting(s.W(4, 'Joao') - 3, .25)
    s.thunk(s.W(5, 'poupado') - 3, 160, .8)
    s.ting(s.W(6, 'quinze') - 3, .3)
