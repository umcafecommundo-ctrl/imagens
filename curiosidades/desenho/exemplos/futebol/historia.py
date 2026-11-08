"""anima.futebol — 08/11/2026 10h — Copa do Brasil: Grêmio é o 1º finalista; hoje Vasco x Palmeiras decide o outro.
Fontes (conferidas em 08/11/2026): Gazeta Esportiva, site oficial do Atlético-MG, Terra/OneFootball, Diário de Goiás,
Revista Fórum, Esporte News Mundo (Atlético-MG 1x1 Grêmio, sáb 07/11, Belo Horizonte; Renan Lodi golaço 25' 1ºT;
Carlos Vinícius de cabeça 37' 1ºT; Grêmio venceu a ida por 2 x 0, agregado 3 x 1; 10ª final do Grêmio, busca o 6º título);
Bahia Notícias, Tribuna de Jundiaí, Folha do Leste, A Crítica (Palmeiras 1x0 Vasco na ida em 01/11; volta hoje 08/11, 17h,
São Januário; Palmeiras avança com empate; Vasco precisa vencer por 2 gols, ou por 1 para levar aos pênaltis;
final em jogo único em 06/12, Mané Garrincha, Brasília — primeira final em jogo único da história da Copa do Brasil).
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'COPA DO BRASIL  ·  SEMIFINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O primeiro finalista da Copa do Brasil já saiu, e hoje a gente descobre o outro.",
    "Ontem à noite, em Belo Horizonte, o Atlético Mineiro até abriu o placar com um golaço de Renan Lodi.",
    "Mas Carlos Vinícius empatou de cabeça, e o Grêmio, que tinha vencido a ida por dois a zero, garantiu a vaga.",
    "É a décima final do Grêmio, que agora sonha com o sexto título.",
    "Hoje, às cinco da tarde, Vasco e Palmeiras se enfrentam em São Januário.",
    "O Palmeiras venceu a ida por um a zero e joga pelo empate.",
    "O Vasco precisa ganhar por dois gols, ou por um para levar aos pênaltis.",
    "E a grande final vai ser em jogo único, no dia seis de dezembro, em Brasília.",
]
CAPTXT = [
    "O primeiro finalista da Copa do Brasil já saiu,|e hoje a gente descobre o outro.",
    "Ontem à noite, em Belo Horizonte, o Atlético Mineiro|até abriu o placar com um golaço de Renan Lodi.",
    "Mas Carlos Vinícius empatou de cabeça, e o Grêmio,|que tinha vencido a ida por 2 a 0, garantiu a vaga.",
    "É a 10ª final do Grêmio,|que agora sonha com o 6º título.",
    "Hoje, às 17h, Vasco e Palmeiras|se enfrentam em São Januário.",
    "O Palmeiras venceu a ida por 1 a 0|e joga pelo empate.",
    "O Vasco precisa ganhar por 2 gols,|ou por 1 para levar aos pênaltis.",
    "E a grande final vai ser em jogo único,|no dia 6 de dezembro, em Brasília.",
]
FALA_TIKTOK = "Quem enfrenta o Grêmio na final, Vasco ou Palmeiras? Comenta aqui, e segue o Anima Futebol!"
CTA_TEXTO = "QUEM PASSA?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'saiu', 4), (0, 'outro', 4), (1, 'golaco', 6), (2, 'cabeca', 6), (2, 'vaga', 4), (3, 'sexto', 4),
         (4, 'Palmeiras', 4), (5, 'empate', 4), (6, 'penaltis', 4), (7, 'Brasilia', 4)]

GRE, GRE_F = time_('GRÊMIO')
CAM, CAM_F = time_('ATLÉTICO-MG')
VAS, VAS_F = time_('VASCO')
PAL, PAL_F = time_('PALMEIRAS')
CINZA, _ = time_('GENÉRICO')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    sa = wt(0, 'saiu') - 3; ou = wt(0, 'outro') - 3
    put_trofeu(c, 640, 1050, 520, f, 0)
    num(c, 'FINAL', 640, 640, f, wt(0, 'finalista') - 3, 170, -4)
    put_jog(c, 330, 2010, 860, f, 1, cores=GRE, faixa=GRE_F, arms='up' if f >= sa else 'cintura', expr='grin' if f >= sa else 'proud', skin=1)
    put_placa(c, 'GRÊMIO', GRE, 330, 1150, f, sa, 66, -4)
    if f >= ou - 6:
        put_jog(c, 960, 2010, 860, f, 2, cores=CINZA, faixa=None, arms='shrug', expr='neutral', skin=2, hair='#3a3d46')
        num(c, '?', 960, 1150, f, ou, 220, 6)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, sa, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    ab = wt(1, 'abriu') - 3; go = wt(1, 'golaco') - 4
    if f < go: num(c, 'BELO HORIZONTE', 640, 740, f, wt(1, 'Belo') - 3, 90, -3)
    put_goleiro(c, f, GRE, GRE_F, arms='shrug', expr='shock' if f >= go else 'nervous', skin=0)
    put_jog(c, 470, 1990, 860, f, 3, cores=CAM, faixa=CAM_F, arms='up' if f >= go + 8 else 'run', kick=pulse(f, go - 5, 5),
            expr='grin' if f >= go else 'stern', skin=3, hair='#111111')
    put_placa(c, 'ATLÉTICO-MG', CAM, 470, 1080, f, wt(1, 'Atletico') - 3, 58, -3)
    put_placa(c, 'RENAN LODI', CAM, 520, 1230, f, wt(1, 'Renan') - 3, 46, 3)
    rb = raio_bola(860)  # bola proporcional ao jogador
    if f < go - 5: bx, by, r = 640, 1990 - rb, rb
    else: t = ramp(f, go - 5, go + 3); bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, 'GOLAÇO!', 660, 760, f, go, 170, -5)
    num(c, '1 x 0', 640, 930, f, go + 6, 140, 4)
    k = kick(f, go)
    return c, (lerp(600, 690, smooth(ramp(f, ab - 10, go))), 1480 + k * 10, 1.12 * (1 + .0007 * f), k), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    ca = wt(2, 'cabeca') - 4; va = wt(2, 'vaga') - 3
    pulo = pulse(f, ca - 8, 10)
    put_goleiro(c, f, CAM, CAM_F, arms='cheek' if f >= ca else 'hang', expr='pained' if f >= ca else 'nervous', skin=3, hair='#111111')
    put_jog(c, 560, 1990 - 160 * pulo, 860, f, 4, cores=GRE, faixa=GRE_F, arms='up' if f >= ca + 6 else 'run', expr='grin' if f >= ca else 'stern', skin=1)
    if f < va: put_placa(c, 'CARLOS VINÍCIUS', GRE, 560, 1170, f, wt(2, 'Carlos') - 3, 46, -3)
    rb = raio_bola(860)
    if f < ca - 14: bx, by, r = lerp(-60, 560, ramp(f, 0, ca - 14)), 1300, rb
    elif f < ca: bx, by, r = 560, lerp(1300, 1170 - 160 * pulo, ramp(f, ca - 14, ca)), rb
    else: t = ramp(f, ca, ca + 8); bx, by, r = lerp(560, gx + 90, t), lerp(1170, gy, t), lerp(rb, raio_bola(300), t)
    if f < va: put_bola(c, bx, by, r, f)
    num(c, '1 x 1', 640, 720, f, ca + 2, 150, -4)
    num(c, 'IDA: 2 x 0', 640, 880, f, wt(2, 'dois') - 3, 100, 3)
    num(c, 'VAGA NA FINAL!', 640, 1040, f, va, 100, -3)
    k = kick(f, ca, .9)
    return c, (640 + 25 * math.sin(f * .03), 1460 + k * 10, 1.1 * (1 + .0008 * f), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    put_trofeu(c, 900, 1250, 560, f, wt(3, 'sexto') - 3)
    put_jog(c, 450, 2020, 920, f, 1, cores=GRE, faixa=GRE_F, arms='up', expr='grin', skin=1)
    put_placa(c, 'GRÊMIO', GRE, 450, 1100, f, wt(3, 'Gremio') - 3, 66, -3)
    num(c, '10ª FINAL', 640, 620, f, wt(3, 'decima') - 3, 140, -4)
    num(c, 'RUMO AO 6º TÍTULO', 640, 800, f, wt(3, 'sexto') - 3, 90, 3)
    return c, (640, 1400, lerp(1.08, 1.16, smooth(f / 120)), 0), 'dusk'


def s4(f):
    c = estadio('day').copy()
    va = wt(4, 'Vasco') - 3; pa = wt(4, 'Palmeiras') - 3
    vx = lerp(-260, 340, easeOut(ramp(f, va - 10, va + 8)))
    px = lerp(1500, 920, easeOut(ramp(f, pa - 10, pa + 8)))
    put_jog(c, vx, 2010, 880, f, 5, cores=VAS, faixa=VAS_F, arms='cintura', expr='stern', skin=2, hair='#151515', look=1)
    put_jog(c, px, 2010, 880, f, 6, cores=PAL, faixa=PAL_F, arms='cintura', expr='smug', skin=0, look=-1)
    put_placa(c, 'VASCO', VAS, 340, 1120, f, va + 4, 66, -4)
    put_placa(c, 'PALMEIRAS', PAL, 920, 1120, f, pa + 4, 60, 4)
    num(c, 'HOJE 17H', 640, 680, f, wt(4, 'Hoje') - 3, 150, -4)
    num(c, 'SÃO JANUÁRIO', 640, 850, f, wt(4, 'Sao') - 3, 100, 3)
    num(c, 'X', 640, 1500, f, pa + 6, 160)
    z = lerp(1.25, 1.06, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    return c, (640, 1400, z, 0), 'golden'


def s5(f):
    c = estadio('day').copy()
    put_jog(c, 640, 2030, 940, f, 6, cores=PAL, faixa=PAL_F, arms='joinha' if f >= wt(5, 'empate') - 3 else 'cintura', expr='smug', skin=0)
    put_placa(c, 'PALMEIRAS', PAL, 640, 1120, f, wt(5, 'Palmeiras') - 3, 64)
    num(c, 'IDA: 1 x 0', 640, 700, f, wt(5, 'ida') - 3, 140, -4)
    num(c, 'EMPATE = VAGA', 640, 870, f, wt(5, 'empate') - 3, 110, 3)
    return c, (640 + 20 * math.sin(f * .04), 1420, lerp(1.06, 1.16, smooth(f / 100)), 0), 'golden'


def s6(f):
    c = estadio('day').copy()
    pe = wt(6, 'penaltis') - 3
    put_jog(c, 640, 2030, 940, f, 5, cores=VAS, faixa=VAS_F, arms='point', expr='stern', skin=2, hair='#151515', look=1)
    put_placa(c, 'VASCO', VAS, 640, 1120, f, wt(6, 'Vasco') - 3, 70)
    num(c, 'VENCER POR 2 = VAGA', 640, 720, f, wt(6, 'dois') - 3, 76, -3)
    num(c, 'POR 1 = PÊNALTIS', 640, 870, f, pe, 76, 3)
    if f >= pe: put_bola(c, 860, 2030 - raio_bola(940), raio_bola(940), 0)
    k = kick(f, pe, .7)
    return c, (640, 1420 + k * 10, lerp(1.06, 1.18, smooth(f / 110)), k), 'golden'


def s7(f):
    c = estadio('dusk').copy()
    put_trofeu(c, 640, 1180, 600, f, 0)
    num(c, 'JOGO ÚNICO', 640, 640, f, wt(7, 'unico') - 3, 130, -3)
    d0 = wt(7, 'seis') - 3
    if f >= d0: paste_c(c, calendario('06', 'DEZ'), 1010, 820, .8 * back(ramp(f, d0, d0 + 8)))
    num(c, 'BRASÍLIA', 640, 1500, f, wt(7, 'Brasilia') - 3, 110, 3)
    put_jog(c, 250, 2040, 760, f, 1, cores=GRE, faixa=GRE_F, arms='up', expr='grin', skin=1)
    put_jog(c, 1030, 2050, 720, f, 2, cores=CINZA, faixa=None, arms='shrug', expr='neutral', skin=2, hair='#3a3d46')
    num(c, '?', 1030, 1200, f, 0, 160, 6)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1360, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'saiu') - 3, 140, 1.0)
    s.ting(s.W(0, 'outro') - 3, .3)
    s.thunk(s.W(1, 'golaco') - 4, 120, 1.0)
    s.thunk(s.W(2, 'cabeca') - 4, 160, .9)
    s.ting(s.W(2, 'vaga') - 3, .35)
    s.thunk(s.W(3, 'decima') - 3, 200, .6)
    s.thunk(s.W(4, 'Hoje') - 3, 140, .8)
    s.thunk(s.W(5, 'empate') - 3, 220, .5)
    s.thunk(s.W(6, 'penaltis') - 3, 160, .7)
    s.ting(s.W(7, 'Brasilia') - 3, .3)
