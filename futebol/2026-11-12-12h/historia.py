"""anima.futebol — 12/11/2026 12h — Seleção Brasileira: Ancelotti testa quatro atacantes e Bruno Guimarães volta.
Fontes (conferidas em 12/11/2026): Sportbuzz (treino de quinta, 12/11, estádio Jalan Besar, Singapura, 1º com todos os
convocados; quarteto Raphinha, Estêvão, Vini Jr e Rayan; meio Andrey Santos e Bruno Guimarães; defesa Wesley, Jair,
Gabriel Magalhães e Douglas Santos; Pedro Morisco, do Coritiba, favorito no gol, Bento segue na disputa; Japão 14/11 7h15,
Estádio Nacional de Singapura); Lance! (mesma data; 4-2-4 com Morisco favorito, Wesley, Jair Cunha, Gabriel Magalhães,
Douglas Santos; Andrey Santos e Bruno Guimarães; Estêvão, Rayan, Raphinha e Vini Jr; Bruno de volta ao treino completo;
Raphinha capitão; sábado 14/11 7h15); IstoÉ (quarteto ofensivo com Vini Jr e Rayan).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD)
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Quatro atacantes: Ancelotti testou um Brasil ofensivo para pegar o Japão.",
    "Nesta quinta, em Singapura, a Seleção treinou pela primeira vez com todos os convocados.",
    "Na frente, Raphinha, Estêvão, Vini Júnior e Rayan, num quatro, dois, quatro.",
    "E a novidade no meio: Bruno Guimarães voltou ao treino e fez dupla com Andrey Santos.",
    "No gol, Pedro Morisco, do Coritiba, aparece como favorito, mas Bento segue na briga.",
    "A defesa continua a mesma: Wesley, Jair, Gabriel Magalhães e Douglas Santos.",
    "Brasil e Japão jogam no sábado, às sete e quinze da manhã de Brasília, em Singapura.",
]
CAPTXT = [
    "Quatro atacantes: Ancelotti testou|um Brasil ofensivo para pegar o Japão.",
    "Nesta quinta, em Singapura, a Seleção treinou|pela 1ª vez com todos os convocados.",
    "Na frente, Raphinha, Estêvão, Vini Júnior|e Rayan, num 4-2-4.",
    "E a novidade no meio: Bruno Guimarães voltou|ao treino e fez dupla com Andrey Santos.",
    "No gol, Pedro Morisco, do Coritiba, aparece|como favorito, mas Bento segue na briga.",
    "A defesa continua a mesma: Wesley, Jair,|Gabriel Magalhães e Douglas Santos.",
    "Brasil e Japão jogam no sábado, às 7h15|de Brasília, em Singapura.",
]
FALA_TIKTOK = "Quatro atacantes contra o Japão: aprova ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "APROVA?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'Quatro', 4), (0, 'Japao', 4), (1, 'Singapura', 4), (1, 'convocados', 4), (2, 'Rayan', 4), (2, 'quatro', 4),
         (3, 'Bruno', 4), (3, 'Andrey', 4), (4, 'Morisco', 4), (4, 'Bento', 4), (5, 'Wesley', 4), (5, 'Douglas', 4),
         (6, 'quinze', 4), (6, 'Singapura', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
TEC = ('#23283a', '#23283a', '#23283a')
COX = ('#2a9d8f', '#ffffff', '#ffffff')


def put_cal(c, dia, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, 'NOV'), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    qu = wt(0, 'Quatro') - 3; an = wt(0, 'Ancelotti') - 3; of = wt(0, 'ofensivo') - 3; ja = wt(0, 'Japao') - 3
    num(c, '4 ATACANTES', 640, 720, f, qu, 120, -4)
    num(c, 'CONTRA O JAPÃO', 640, 880, f, ja, 90, 3)
    for i, (x, nome, sd, sk, hair) in enumerate(((280, 'VINI JR.', 2, 3, '#111111'), (510, 'RAPHINHA', 3, 1, '#2b1d14'),
                                                 (740, 'RAYAN', 4, 2, '#111111'), (970, 'ESTÊVÃO', 5, 2, '#111111'))):
        f0 = qu + i * 4
        if f < f0 - 4: continue
        y = lerp(2500, 2010, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, y, 700, f, sd, cores=BRA, faixa=BRA_F, arms='up' if f >= of else 'cintura', expr='grin', skin=sk, hair=hair)
        put_placa(c, nome, BRA, x, 1220 + (70 if i % 2 else 0), f, f0, 38, -3 if i % 2 else 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ja, .7)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = CEN('cidade', 'dusk').copy()
    si = wt(1, 'Singapura') - 3; pr = wt(1, 'primeira') - 3; co = wt(1, 'convocados') - 3
    for i, (x, sd, sk) in enumerate(((260, 2, 1), (640, 3, 3), (1000, 4, 0))):
        xx = x + lerp(-600, 0, easeOut(ramp(f, i * 4, i * 4 + 22)))
        if i == 1:
            put_jog(c, xx, 2000, 820, f, 9, cores=TEC, faixa=None, arms='point' if f >= co else 'cintura', expr='proud', skin=0, hair='#9a9a9a')
        else:
            put_jog(c, xx, 1960, 760, f, sd, cores=BRA, faixa=BRA_F, walk=(f * .05) % 1 if f < 30 else 0,
                    arms='run' if f < 30 else 'joinha', expr='grin', skin=sk)
    put_placa(c, 'ANCELOTTI', TEC, 640, 1120, f, wt(1, 'Selecao') - 3, 60, -3)
    num(c, 'SINGAPURA', 640, 720, f, si, 110, -4)
    num(c, '1º TREINO COM TODOS', 640, 870, f, pr, 62, 3)
    return c, (lerp(600, 680, smooth(f / 120)), 1420, 1.06 * (1 + .0008 * f), 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=700)
    qa = wt(2, 'quatro') - 3
    put_goleiro(c, f, ('#ff8c1a', '#111111', '#111111'), None, gx=720, arms='shrug', expr='shock' if f >= qa + 6 else 'nervous', skin=0)
    ws = (('Raphinha', 'RAPHINHA', 520, 2020, 860, 3, 1, '#2b1d14'), ('Estevao', 'ESTÊVÃO', 1000, 1990, 740, 4, 2, '#111111'),
          ('Vini', 'VINI JR.', 240, 1990, 740, 2, 3, '#111111'), ('Rayan', 'RAYAN', 800, 1960, 680, 5, 2, '#111111'))
    for w, nome, x, y, h, sd, sk, hair in ws:
        f0 = wt(2, w) - 3
        if f < f0 - 4: continue
        yy = lerp(2500, y, easeOut(ramp(f, f0 - 4, f0 + 6)))
        if w == 'Raphinha':
            put_jog(c, x, yy, h, f, sd, cores=BRA, faixa=BRA_F, arms='up' if f >= qa + 8 else 'run', kick=pulse(f, qa - 5, 5),
                    expr='grin', skin=sk, hair=hair)
        else:
            put_jog(c, x, yy, h, f, sd, cores=BRA, faixa=BRA_F, arms='up' if f >= qa + 8 else 'run', expr='grin', skin=sk, hair=hair,
                    flip=x > 700)
        py = {'RAPHINHA': 990, 'ESTÊVÃO': 1060, 'VINI JR.': 1060, 'RAYAN': 1130}[nome]
        put_placa(c, nome, BRA, x, py, f, f0, 36, -3 if x < 640 else 3)
    rb = raio_bola(860)
    if f < qa - 3: bx, by, r = 620, 2020 - rb, rb
    else:
        t = ramp(f, qa - 3, qa + 6)
        bx, by, r = lerp(620, gx + 90, t), lerp(2020 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, '4-2-4', 640, 800, f, qa, 170, -3)
    k = kick(f, qa + 4)
    return c, (640 + 30 * math.sin(f * .03), 1420 + k * 10, lerp(1.0, 1.05, smooth(f / 110)), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    no = wt(3, 'novidade') - 3; br = wt(3, 'Bruno') - 3; vo = wt(3, 'voltou') - 3; an = wt(3, 'Andrey') - 3
    num(c, 'NOVIDADE NO MEIO', 640, 720, f, no, 96, -4)
    bxp = lerp(-300, 450, easeOut(ramp(f, br - 8, br + 6)))
    put_jog(c, bxp, 2030, 860, f, 6, cores=BRA, faixa=BRA_F, arms='joinha' if f >= vo else 'run', expr='grin', skin=1,
            walk=(f * .06) % 1 if f < br + 6 else 0)
    put_placa(c, 'BRUNO GUIMARÃES', BRA, 470, 1100, f, br, 36, -3)
    if f >= an - 6:
        axp = lerp(1550, 820, easeOut(ramp(f, an - 6, an + 6)))
        put_jog(c, axp, 2030, 860, f, 7, cores=BRA, faixa=BRA_F, arms='joinha' if f >= an + 6 else 'run', expr='grin', skin=2,
                hair='#111111', flip=True)
        put_placa(c, 'ANDREY SANTOS', BRA, 800, 1170, f, an, 36, 3)
    num(c, 'VOLTOU!', 640, 880, f, vo, 110, 3)
    k = kick(f, vo, .7)
    return c, (640, 1420 + k * 8, lerp(1.04, 1.1, smooth(f / 100)), k), 'dusk'


def s4(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c, x=640)
    mo = wt(4, 'Morisco') - 3; fa = wt(4, 'favorito') - 3; be = wt(4, 'Bento') - 3
    num(c, 'NO GOL', 640, 720, f, wt(4, 'gol') - 3, 100, -3)
    put_jog(c, 470, 2020, 840, f, 12, cores=COX, faixa=None, arms='up' if f >= fa else 'hang', expr='proud' if f >= fa else 'neutral', skin=1)
    put_placa(c, 'PEDRO MORISCO', COX, 470, 1110, f, mo, 40, -3)
    num(c, 'FAVORITO', 470, 880, f, fa, 90, 3)
    if f >= be - 6:
        xx = lerp(1500, 900, easeOut(ramp(f, be - 6, be + 6)))
        put_jog(c, xx, 2000, 780, f, 13, cores=('#ff8c1a', '#111111', '#111111'), faixa=None, arms='cintura', expr='stern', skin=2,
                hair='#111111', flip=True)
        put_placa(c, 'BENTO', ('#ff8c1a', '#111111', '#111111'), 900, 1180, f, be, 46, 3)
        num(c, 'NA BRIGA', 900, 1000, f, wt(4, 'briga') - 3, 76, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0012 * f)
    return c, (640 + 25 * math.sin(f * .05), lerp(1380, 1440, smooth(f / 120)), z, .8 * math.sin(f * .04)), 'golden'


def s5(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=640)
    num(c, 'A MESMA DEFESA', 640, 760, f, wt(5, 'defesa') - 3, 100, -3)
    for i, (x, nome, w, sk, hair) in enumerate(((300, 'WESLEY', 'Wesley', 3, '#111111'), (530, 'JAIR', 'Jair', 2, '#111111'),
                                                (760, 'G. MAGALHÃES', 'Gabriel', 1, '#2b1d14'), (990, 'DOUGLAS SANTOS', 'Douglas', 2, '#111111'))):
        f0 = wt(5, w) - 3
        if f < f0 - 4: continue
        y = lerp(2500, 2010, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, y, 640, f, 10 + i, cores=BRA, faixa=BRA_F, arms='cintura', expr='stern', skin=sk, hair=hair)
        put_placa(c, nome, BRA, x, 1250 if i % 2 == 0 else 1320, f, f0, 32, -3 if i % 2 else 3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0012 * f)
    return c, (640 + 25 * math.sin(f * .05), lerp(1380, 1460, smooth(f / 120)), z, .8 * math.sin(f * .04)), 'dusk'


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
    num(c, 'SINGAPURA', 640, 960, f, wt(6, 'Singapura') - 3, 90, 3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ja, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'Quatro') - 3, 140, .8)
    s.ting(s.W(1, 'convocados') - 3, .3)
    s.thunk(s.W(2, 'Rayan') - 3, 140, .8)
    s.thunk(s.W(2, 'quatro') - 3, 180, .9)
    s.ting(s.W(3, 'voltou') - 3, .3)
    s.ting(s.W(4, 'favorito') - 3, .25)
    s.thunk(s.W(5, 'Douglas') - 3, 140, .7)
    s.ting(s.W(6, 'quinze') - 3, .3)
