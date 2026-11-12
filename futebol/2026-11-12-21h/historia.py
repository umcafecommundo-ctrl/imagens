"""anima.futebol — 12/11/2026 21h — Liga das Nações: Harry Kane vira recordista de jogos da Inglaterra e decide contra a Croácia.
Fontes (conferidas em 12/11/2026): CNN Brasil, Lance!, Goal.com (Inglaterra 2x1 Croácia, quinta 12/11, Wembley,
Liga das Nações A, grupo 3, 5ª rodada; Morgan Rogers 24' 1ºT; Sucic 59'; Kane de pênalti 64' após revisão do VAR;
Kane chega a 126 jogos, recorde da seleção inglesa, passando Peter Shilton (125); 92 gols pela Inglaterra;
Inglaterra com 12 pontos, classificada às quartas; domingo 15/11 x Espanha (líder) no Metropolitano, em Madri,
valendo o 1º lugar do grupo). Homenagens: camisa 126 e mosaico em Wembley.
Sem escudos/logos: times por plaquinhas e cores; bonecos genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'LIGA DAS NAÇÕES  ·  5ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Harry Kane virou o jogador com mais jogos da história da seleção inglesa, e ainda fez o gol da vitória.",
    "Foi hoje, em Wembley, contra a Croácia, pela Liga das Nações.",
    "Morgan Rogers abriu o placar no primeiro tempo, mas a Croácia empatou com Sucic no segundo.",
    "Cinco minutos depois, pênalti, e Kane bateu para fazer dois a um.",
    "Foi o jogo de número cento e vinte e seis, um a mais que o goleiro Peter Shilton, o antigo recordista.",
    "E o gol foi o de número noventa e dois dele pela Inglaterra, que já está nas quartas de final.",
    "Agora vem a Espanha, no domingo, em Madri, valendo o primeiro lugar do grupo.",
]
CAPTXT = [
    "Harry Kane virou o jogador com mais jogos da história|da seleção inglesa, e ainda fez o gol da vitória.",
    "Foi hoje, em Wembley, contra a Croácia,|pela Liga das Nações.",
    "Morgan Rogers abriu o placar no 1º tempo,|mas a Croácia empatou com Sucic no 2º.",
    "5 minutos depois, pênalti,|e Kane bateu para fazer 2 a 1.",
    "Foi o jogo de número 126, 1 a mais que o goleiro|Peter Shilton, o antigo recordista.",
    "E o gol foi o de número 92 dele pela Inglaterra,|que já está nas quartas de final.",
    "Agora vem a Espanha, no domingo, em Madri,|valendo o 1º lugar do grupo.",
]
FALA_TIKTOK = "Kane chega aos cem gols pela Inglaterra? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Kane', 4), (0, 'vitoria', 4), (1, 'Wembley', 4), (1, 'Croacia', 4), (2, 'Rogers', 6), (2, 'empatou', 4),
         (3, 'penalti', 6), (3, 'dois', 4), (4, 'cento', 4), (4, 'Shilton', 4), (5, 'noventa', 4), (5, 'quartas', 4),
         (6, 'Espanha', 4), (6, 'Madri', 4)]

ING, ING_F = time_('INGLATERRA')
CRO, CRO_F = time_('CROÁCIA')
ESP, ESP_F = time_('ESPANHA')
KANE_H = '#a0703f'


def kane(c, x, feet, h, f, **kw):
    put_jog(c, x, feet, h, f, 9, cores=ING, faixa=ING_F, skin=0, hair=KANE_H, num_='9', **kw)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    ka = wt(0, 'Kane') - 3; jo = wt(0, 'jogos') - 3; vi = wt(0, 'vitoria') - 3
    kane(c, 640, 2020, 900, f, arms='up' if f >= vi else 'cintura', expr='grin' if f >= jo else 'proud')
    put_placa(c, 'HARRY KANE', ING, 640, 1060, f, ka, 70, -3)
    num(c, '126 JOGOS', 640, 700, f, jo, 150, -4)
    if f < vi: num(c, 'RECORDE!', 640, 880, f, wt(0, 'historia') - 3, 120, 4)
    else: num(c, '+ GOL DA VITÓRIA', 640, 880, f, vi, 86, -3)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, jo, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    we = wt(1, 'Wembley') - 3; cr = wt(1, 'Croacia') - 3
    ix = lerp(-260, 360, easeOut(ramp(f, 0, 14)))
    cx = lerp(1500, 900, easeOut(ramp(f, cr - 10, cr + 8)))
    put_jog(c, ix, 2010, 860, f, 5, cores=ING, faixa=ING_F, arms='cintura', expr='stern', skin=0, hair='#2b1d14', look=1)
    put_jog(c, cx, 2010, 860, f, 6, cores=CRO, faixa=CRO_F, arms='cintura', expr='smug', skin=0, hair='#111111', look=-1)
    put_placa(c, 'INGLATERRA', ING, 360, 1100, f, 4, 58, -4)
    put_placa(c, 'CROÁCIA', CRO, 900, 1100, f, cr + 4, 62, 4)
    num(c, 'WEMBLEY', 640, 700, f, we, 150, -4)
    num(c, 'LIGA DAS NAÇÕES', 640, 870, f, wt(1, 'Liga') - 3, 90, 3)
    num(c, 'X', 640, 1500, f, cr + 6, 160)
    if f >= wt(1, 'hoje') - 3 and f < we: paste_c(c, calendario('12', 'NOV'), 640, 780, .8 * back(ramp(f, wt(1, 'hoje') - 3, wt(1, 'hoje') + 5)))
    z = lerp(1.25, 1.06, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    return c, (640, 1400, z, 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    go = wt(2, 'abriu') - 4; em = wt(2, 'empatou') - 3
    if f < em:
        put_goleiro(c, f, CRO, CRO_F, arms='shrug', expr='shock' if f >= go else 'nervous', skin=0, hair='#111111')
        put_jog(c, 470, 1990, 860, f, 3, cores=ING, faixa=ING_F, arms='up' if f >= go + 8 else 'run', kick=pulse(f, go - 5, 5),
                expr='grin' if f >= go else 'stern', skin=1, hair='#2b1d14')
        put_placa(c, 'MORGAN ROGERS', ING, 560, 1080, f, wt(2, 'Morgan') - 3, 50, -3)
        rb = raio_bola(860)
        if f < go - 5: bx, by, r = 640, 1990 - rb, rb
        else: t = ramp(f, go - 5, go + 3); bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
        put_bola(c, bx, by, r, f)
        num(c, '1 x 0', 640, 760, f, go, 150, -4)
        num(c, '1º TEMPO', 640, 920, f, wt(2, 'primeiro') - 3, 90, 3)
    else:
        put_goleiro(c, f, ING, ING_F, arms='cheek', expr='pained', skin=0)
        put_jog(c, 560, 1990, 860, f, 4, cores=CRO, faixa=CRO_F, arms='up', expr='grin', skin=0, hair='#3a2a1a')
        put_placa(c, 'SUCIC', CRO, 560, 1090, f, wt(2, 'Sucic') - 3, 64, -3)
        num(c, '1 x 1', 640, 760, f, em, 150, -4)
        num(c, '2º TEMPO', 640, 920, f, wt(2, 'segundo') - 3, 90, 3)
    k = kick(f, go) + kick(f, em, .8)
    return c, (lerp(600, 690, smooth(ramp(f, 0, em))), 1480 + k * 10, 1.12 * (1 + .0007 * f), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    pe = wt(3, 'penalti') - 3; ba = wt(3, 'bateu') - 2; gl = wt(3, 'dois') - 3
    put_goleiro(c, f, CRO, CRO_F, arms='up' if f < ba else 'shrug', expr='nervous' if f < ba else 'shock', skin=0, hair='#111111')
    kane(c, 500, 1990, 860, f, arms='up' if f >= gl + 4 else 'run', kick=pulse(f, ba, 5), expr='grin' if f >= gl else 'stern')
    put_placa(c, 'KANE', ING, 500, 1080, f, wt(3, 'Kane') - 3, 66, -3)
    num(c, 'PÊNALTI', 640, 720, f, pe, 140, -4)
    rb = raio_bola(860)
    if f < ba + 2: bx, by, r = 660, 1990 - rb, rb
    else: t = ramp(f, ba + 2, ba + 9); bx, by, r = lerp(660, gx + 120, t), lerp(1990 - rb, gy - 20, t) - 60 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, '2 x 1', 640, 900, f, gl, 160, 4)
    k = kick(f, gl)
    return c, (640 + 20 * math.sin(f * .04), 1470 + k * 10, 1.12 * (1 + .0008 * f), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    ce = wt(4, 'cento') - 3; sh = wt(4, 'Shilton') - 3
    kane(c, 400, 2020, 900, f, arms='up' if f >= ce else 'cintura', expr='grin', look=1)
    put_placa(c, 'KANE', ING, 400, 1060, f, 2, 64, -3)
    num(c, '126', 400, 760, f, ce, 190, -4)
    if f >= sh - 10:
        sx = lerp(1500, 870, easeOut(ramp(f, sh - 10, sh + 6)))
        put_jog(c, sx, 2020, 820, f, 12, cores=('#3a8a3a', '#111111', '#111111'), faixa=None, arms='cintura', expr='smug', skin=0, hair='#d8d8d8', look=-1)
        put_placa(c, 'PETER SHILTON', ING, 860, 1140, f, sh + 2, 46, 3)
        num(c, '125', 870, 860, f, sh + 4, 150, 4)
    return c, (640, 1400, lerp(1.06, 1.16, smooth(f / 130)), lerp(0, 2, smooth(f / 130))), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    no = wt(5, 'noventa') - 3; qu = wt(5, 'quartas') - 3
    kane(c, 640, 2030, 940, f, arms='up' if f >= qu else 'joinha', expr='grin')
    put_placa(c, 'KANE', ING, 640, 1080, f, 2, 66)
    num(c, '92 GOLS', 640, 700, f, no, 160, -4)
    num(c, 'QUARTAS DE FINAL', 640, 880, f, qu, 90, 3)
    k = kick(f, qu, .7)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 10, lerp(1.06, 1.18, smooth(f / 110)), k), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    es = wt(6, 'Espanha') - 3; do = wt(6, 'domingo') - 3
    ex = lerp(1500, 920, easeOut(ramp(f, es - 10, es + 8)))
    kane(c, 340, 2010, 860, f, arms='cintura', expr='stern', look=1)
    put_jog(c, ex, 2010, 860, f, 7, cores=ESP, faixa=ESP_F, arms='cintura', expr='smug', skin=1, hair='#111111', look=-1)
    put_placa(c, 'INGLATERRA', ING, 340, 1100, f, 2, 56, -4)
    put_placa(c, 'ESPANHA', ESP, 920, 1100, f, es + 4, 62, 4)
    pr = wt(6, 'primeiro') - 3
    if do <= f < pr: paste_c(c, calendario('15', 'NOV'), 640, 820, .75 * back(ramp(f, do, do + 8)))
    num(c, 'MADRI', 640, 1500, f, wt(6, 'Madri') - 3, 110, 3)
    num(c, '1º LUGAR', 640, 800, f, pr, 120, -3)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1360, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'jogos') - 3, 140, 1.0)
    s.ting(s.W(0, 'vitoria') - 3, .3)
    s.thunk(s.W(1, 'Wembley') - 3, 160, .8)
    s.thunk(s.W(2, 'abriu') - 4, 120, 1.0)
    s.thunk(s.W(2, 'empatou') - 3, 160, .8)
    s.thunk(s.W(3, 'dois') - 3, 120, 1.0)
    s.ting(s.W(4, 'cento') - 3, .35)
    s.thunk(s.W(5, 'noventa') - 3, 200, .7)
    s.ting(s.W(6, 'Madri') - 3, .3)
