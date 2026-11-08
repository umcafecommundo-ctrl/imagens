"""anima.futebol — 08/11/2026 18h — Premier League: Manchester United 4 x 4 Aston Villa em Old Trafford.
Fontes (conferidas em 08/11/2026): site oficial do Aston Villa (relatório), Lance!, ESPN (placar final 4-4),
Goal Brasil, Sofascore, premierleaguenewsnow, Grêmio.net/Trivela (Alysson, ex-Grêmio, vendido ao Aston Villa).
Alysson 1' e Jackson ~3' (0x2); Bruno Fernandes pênalti (1x2); empate no fim do 1º tempo (2x2); McGinn pênalti e
Goretzka no início do 2º tempo (2x4); Zirkzee nos acréscimos (3x4); Dorgu de cabeça, após escanteio, no último lance (4x4).
United com 8 pontos em 10 jogos, na zona de rebaixamento; pausa para as seleções; técnico Michael Carrick pressionado;
próximo jogo: Liverpool x United em Anfield. Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'PREMIER LEAGUE  ·  10ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Oito gols, e o empate saiu no último lance!",
    "Neste domingo, em Old Trafford, o Aston Villa abriu o placar no primeiro minuto, com o brasileiro Alysson, ex-Grêmio.",
    "Logo depois já era dois a zero, mas o Manchester United buscou o empate antes do intervalo.",
    "Na volta, o Villa fez mais dois, e abriu quatro a dois.",
    "Aí veio a loucura: Zirkzee diminuiu nos acréscimos, e Dorgu, de cabeça, deixou tudo quatro a quatro.",
    "Mesmo assim, o United segue na zona de rebaixamento, com só oito pontos em dez jogos.",
    "Agora o campeonato para por causa das seleções, e a pressão no técnico Michael Carrick só aumenta.",
    "E na volta tem clássico contra o Liverpool, em Anfield.",
]
CAPTXT = [
    "8 gols, e o empate saiu|no último lance!",
    "Neste domingo, em Old Trafford, o Aston Villa abriu o placar|no 1º minuto, com o brasileiro Alysson, ex-Grêmio.",
    "Logo depois já era 2 a 0, mas o Manchester United|buscou o empate antes do intervalo.",
    "Na volta, o Villa fez mais dois,|e abriu 4 a 2.",
    "Aí veio a loucura: Zirkzee diminuiu nos acréscimos,|e Dorgu, de cabeça, deixou tudo 4 a 4.",
    "Mesmo assim, o United segue na zona de rebaixamento,|com só 8 pontos em 10 jogos.",
    "Agora o campeonato para por causa das seleções,|e a pressão no técnico Michael Carrick só aumenta.",
    "E na volta tem clássico|contra o Liverpool, em Anfield.",
]
FALA_TIKTOK = "O Carrick fica no United? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "CARRICK FICA?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'gols', 4), (0, 'lance', 4), (1, 'primeiro', 6), (1, 'Alysson', 6), (2, 'zero', 4), (2, 'empate', 4),
         (3, 'dois', 4), (4, 'Zirkzee', 6), (4, 'cabeca', 6), (5, 'rebaixamento', 4), (6, 'Carrick', 4), (7, 'Anfield', 4)]

MU, MU_F = time_('MANCHESTER UNITED')
AV, AV_F = time_('ASTON VILLA')
LIV, LIV_F = time_('LIVERPOOL')
CINZA, _ = time_('GENÉRICO')


def chute(c, f, t0, xj, h, mira, ini_y=None):
    """bola sai do pé (xj, chão) e vai até o gol no fundo; r proporcional."""
    rb = raio_bola(h)
    if f < t0: bx, by, r = xj + 170, 2000 - rb, rb
    else:
        t = ramp(f, t0, t0 + 8)
        bx = lerp(xj + 170, mira[0] + 90, t); by = lerp(2000 - rb, mira[1], t) - 140 * math.sin(t * math.pi)
        r = lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    go = wt(0, 'gols') - 3; la = wt(0, 'lance') - 3
    num(c, '8 GOLS!', 640, 720, f, go, 190, -4)
    put_jog(c, 330, 2010, 860, f, 1, cores=MU, faixa=MU_F, arms='up' if f >= la else 'cintura', expr='grin' if f >= la else 'stern', skin=1)
    put_jog(c, 950, 2010, 860, f, 2, cores=AV, faixa=AV_F, arms='cheek' if f >= la else 'cintura', expr='shock' if f >= la else 'smug', skin=2, hair='#151515', look=-1)
    put_placa(c, 'UNITED', MU, 330, 1130, f, go + 6, 64, -4)
    put_placa(c, 'ASTON VILLA', AV, 950, 1130, f, go + 10, 56, 4)
    num(c, '4 x 4', 640, 920, f, la, 160, 4)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, la, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    go = wt(1, 'primeiro') - 4
    num(c, 'OLD TRAFFORD', 640, 720, f, wt(1, 'Old') - 3, 100, -3)
    put_goleiro(c, f, MU, MU_F, arms='shrug' if f >= go + 4 else 'hang', expr='shock' if f >= go else 'nervous', skin=0)
    put_jog(c, 460, 1990, 860, f, 3, cores=AV, faixa=AV_F, arms='up' if f >= go + 10 else 'run', kick=pulse(f, go - 5, 5),
            expr='grin' if f >= go else 'stern', skin=3, hair='#111111')
    chute(c, f, go - 2, 460, 860, (gx, gy))
    num(c, '1º MINUTO', 640, 880, f, go + 2, 120, 4)
    put_placa(c, 'ALYSSON', AV, 460, 1090, f, wt(1, 'Alysson') - 3, 62, -3)
    num(c, 'EX-GRÊMIO', 900, 930, f, wt(1, 'ex-Gremio') - 3, 80, 3)
    k = kick(f, go)
    return c, (lerp(600, 680, smooth(ramp(f, 0, go))), 1480 + k * 10, 1.12 * (1 + .0007 * f), k), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    ze = wt(2, 'zero') - 3; em = wt(2, 'empate') - 3
    if f < em:
        put_jog(c, 640, 2020, 900, f, 4, cores=MU, faixa=MU_F, arms='cheek', expr='pained', skin=1)
        num(c, '0 x 2', 640, 760, f, ze, 170, -4)
    else:
        put_jog(c, 380, 2020, 880, f, 4, cores=MU, faixa=MU_F, arms='up', expr='grin', skin=1)
        put_jog(c, 900, 2020, 880, f, 5, cores=MU, faixa=MU_F, arms='up', expr='grin', skin=3, hair='#111111', flip=True)
        num(c, '2 x 2', 640, 760, f, em, 170, 4)
        num(c, 'ANTES DO INTERVALO', 640, 930, f, em + 6, 80, -3)
    put_placa(c, 'UNITED', MU, 640, 1110, f, wt(2, 'Manchester') - 3, 66, 3)
    k = kick(f, em, .9)
    return c, (640 + 25 * math.sin(f * .03), 1440 + k * 10, 1.1 * (1 + .0008 * f), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    t1 = wt(3, 'mais') - 4; t2 = wt(3, 'quatro') - 6
    put_goleiro(c, f, MU, MU_F, arms='cheek' if f >= t1 else 'hang', expr='pained' if f >= t1 else 'nervous', skin=0)
    put_jog(c, 520, 1990, 860, f, 6, cores=AV, faixa=AV_F, arms='up' if f >= t2 + 8 else 'run', kick=pulse(f, t1 - 5, 5) + pulse(f, t2 - 5, 5),
            expr='grin', skin=2, hair='#151515')
    if f < t2 - 2: chute(c, f, t1 - 2, 520, 860, (gx, gy))
    else: chute(c, f, t2 - 2, 520, 860, (gx, gy))
    num(c, '+2', 640, 720, f, t1, 150, -4)
    num(c, '2 x 4', 640, 900, f, t2, 170, 4)
    k = kick(f, t2)
    return c, (640, 1470 + k * 10, lerp(1.08, 1.16, smooth(f / 100)), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    zi = wt(4, 'diminuiu') - 4; ca = wt(4, 'cabeca') - 4; qq = wt(4, 'quatro') - 3
    pulo = pulse(f, ca - 8, 10)
    put_goleiro(c, f, AV, AV_F, arms='cheek' if f >= ca else 'hang', expr='pained' if f >= ca else 'nervous', skin=2, hair='#151515')
    if f < ca - 16:
        put_jog(c, 460, 1990, 860, f, 7, cores=MU, faixa=MU_F, arms='up' if f >= zi + 6 else 'run', kick=pulse(f, zi - 5, 5), expr='grin', skin=0)
        put_placa(c, 'ZIRKZEE', MU, 460, 1090, f, wt(4, 'Zirkzee') - 3, 60, -3)
        chute(c, f, zi - 2, 460, 860, (gx, gy))
        num(c, '3 x 4', 640, 740, f, zi, 160, -4)
        num(c, 'ACRÉSCIMOS', 640, 900, f, wt(4, 'acrescimos') - 3, 100, 3)
    else:
        put_jog(c, 560, 1990 - 160 * pulo, 860, f, 8, cores=MU, faixa=MU_F, arms='up' if f >= ca + 6 else 'run', expr='grin' if f >= ca else 'stern', skin=1)
        put_placa(c, 'DORGU', MU, 560, 1110, f, wt(4, 'Dorgu') - 3, 60, 3)
        rb = raio_bola(860)
        if f < ca: bx, by, r = lerp(1300, 560, ramp(f, ca - 16, ca)), 1180 - 160 * pulo, rb
        else: t = ramp(f, ca, ca + 8); bx, by, r = lerp(560, gx + 90, t), lerp(1180, gy, t), lerp(rb, raio_bola(300), t)
        put_bola(c, bx, by, r, f)
        num(c, '4 x 4!', 640, 760, f, qq, 190, -4)
        num(c, 'ÚLTIMO LANCE', 640, 940, f, qq + 6, 100, 3)
    k = kick(f, ca, 1.0) + kick(f, zi, .6)
    return c, (640 + 20 * math.sin(f * .05), 1460 + k * 10, 1.1 * (1 + .001 * f), k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    put_jog(c, 640, 2030, 940, f, 4, cores=MU, faixa=MU_F, arms='cheek', expr='nervous', skin=1)
    put_placa(c, 'UNITED', MU, 640, 1110, f, wt(5, 'United') - 3, 64)
    num(c, 'ZONA DE', 640, 690, f, wt(5, 'zona') - 3, 120, -3)
    num(c, 'REBAIXAMENTO', 640, 830, f, wt(5, 'rebaixamento') - 3, 110, 3)
    num(c, '8 PONTOS EM 10 JOGOS', 640, 1500, f, wt(5, 'oito') - 3, 76, -2)
    return c, (640 + 20 * math.sin(f * .04), 1420, lerp(1.06, 1.16, smooth(f / 100)), lerp(0, 2, smooth(f / 100))), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    ca = wt(6, 'Carrick') - 3
    num(c, 'PAUSA', 640, 690, f, wt(6, 'para') - 3, 120, -3)
    num(c, 'SELEÇÕES', 640, 830, f, wt(6, 'selecoes') - 3, 110, 3)
    put_jog(c, 640, 2030, 940, f, 9, cores=CINZA, faixa=None, arms='cintura' if f < ca else 'cheek', expr='stern' if f < ca else 'nervous', skin=0, hair='#6b4a2e')
    put_placa(c, 'TÉCNICO: CARRICK', MU, 640, 1130, f, ca, 54, 3)
    num(c, 'PRESSÃO!', 640, 980, f, wt(6, 'pressao') - 3, 130, 4)
    k = kick(f, wt(6, 'pressao') - 3, .7)
    return c, (640, 1420 + k * 10, lerp(1.06, 1.2, smooth(f / 110)), k), 'dusk'


def s7(f):
    c = estadio('day').copy()
    li = wt(7, 'Liverpool') - 3
    vx = lerp(-260, 340, easeOut(ramp(f, li - 14, li + 4)))
    put_jog(c, 940, 2010, 880, f, 4, cores=MU, faixa=MU_F, arms='cintura', expr='stern', skin=1, look=-1)
    put_jog(c, vx, 2010, 880, f, 10, cores=LIV, faixa=LIV_F, arms='cintura', expr='smug', skin=3, hair='#111111', look=1)
    put_placa(c, 'UNITED', MU, 940, 1120, f, 4, 64, 4)
    put_placa(c, 'LIVERPOOL', LIV, 340, 1120, f, li + 4, 60, -4)
    num(c, 'CLÁSSICO', 640, 700, f, wt(7, 'classico') - 3, 150, -4)
    num(c, 'EM ANFIELD', 640, 870, f, wt(7, 'Anfield') - 3, 110, 3)
    num(c, 'X', 640, 1500, f, li + 6, 160)
    z = lerp(1.25, 1.06, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    return c, (640, 1400, z, 0), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'gols') - 3, 140, 1.0)
    s.ting(s.W(0, 'lance') - 3, .3)
    s.thunk(s.W(1, 'primeiro') - 4, 120, 1.0)
    s.thunk(s.W(2, 'empate') - 3, 160, .8)
    s.thunk(s.W(3, 'quatro') - 6, 140, .9)
    s.thunk(s.W(4, 'diminuiu') - 4, 140, .8)
    s.thunk(s.W(4, 'cabeca') - 4, 120, 1.0)
    s.ting(s.W(4, 'quatro') - 3, .35)
    s.thunk(s.W(5, 'rebaixamento') - 3, 220, .6)
    s.thunk(s.W(6, 'pressao') - 3, 160, .7)
    s.ting(s.W(7, 'Anfield') - 3, .3)
