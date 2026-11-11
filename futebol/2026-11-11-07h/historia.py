"""anima.futebol — 11/11/2026 07h — Finais continentais: Brasil x Argentina na Sul-Americana e na Libertadores.
Fontes (conferidas em 11/11/2026): DGABC/Estadão e O Liberal (30/10: final da Sul-Americana Atlético-MG x Boca Juniors,
sáb 21/11, 20h de Brasília, Metropolitano Roberto Meléndez, Barranquilla; Galo vice em 2025 busca o 1º título; Boca
campeão em 2004 e 2005; Boca eliminou São Paulo nas quartas e Vasco na semi); Tribuna de Jundiaí (23/10: as duas finais,
jogos únicos); A Crítica (31/10) e Gazeta Esportiva (06/11: final da Libertadores Palmeiras x Estudiantes, sáb 28/11,
17h, Estádio Centenário, Montevidéu; Palmeiras 3 títulos (1999, 2020, 2021) busca o 4º, vice em 2025; Estudiantes
4 títulos (1968, 69, 70 e 2009) busca o 5º; os dois passaram nos pênaltis na semi: Palmeiras x Fluminense,
Estudiantes x Flamengo).
Sem escudos/logos/taças reais: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'LIBERTADORES E SULA  ·  FINAIS'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Brasil contra Argentina em duas finais, e a primeira é daqui a dez dias.",
    "No dia vinte e um, em Barranquilla, na Colômbia, o Atlético Mineiro encara o Boca Juniors na final da Sul-Americana.",
    "O Galo, vice no ano passado, busca o primeiro título, e o Boca, que eliminou São Paulo e Vasco, quer o terceiro.",
    "Uma semana depois, no dia vinte e oito, vem a final da Libertadores, no Centenário, em Montevidéu.",
    "O Palmeiras passou pelo Fluminense nos pênaltis, e o Estudiantes eliminou o Flamengo, também nos pênaltis.",
    "O Verdão quer o quarto título, e o Estudiantes quer o quinto, dezessete anos depois do último.",
    "Dois jogos únicos que vão dizer se novembro é do Brasil, ou da Argentina.",
]
CAPTXT = [
    "Brasil contra Argentina em duas finais,|e a primeira é daqui a 10 dias.",
    "No dia 21, em Barranquilla, na Colômbia, o Atlético-MG|encara o Boca Juniors na final da Sul-Americana.",
    "O Galo, vice no ano passado, busca o 1º título, e o Boca,|que eliminou São Paulo e Vasco, quer o 3º.",
    "Uma semana depois, no dia 28, vem a final|da Libertadores, no Centenário, em Montevidéu.",
    "O Palmeiras passou pelo Fluminense nos pênaltis, e o|Estudiantes eliminou o Flamengo, também nos pênaltis.",
    "O Verdão quer o 4º título, e o Estudiantes|quer o 5º, 17 anos depois do último.",
    "Dois jogos únicos que vão dizer|se novembro é do Brasil, ou da Argentina.",
]
FALA_TIKTOK = "Quem leva as duas taças, Brasil ou Argentina? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 6
FLASH = [3]
CHECK = [(0, 'Argentina', 4), (0, 'dez', 4), (1, 'Barranquilla', 4), (1, 'Boca', 6), (2, 'primeiro', 4), (2, 'terceiro', 4),
         (3, 'Centenario', 4), (4, 'Flamengo', 6), (5, 'dezessete', 4), (6, 'Argentina', 4)]

GAL, GAL_F = time_('ATLÉTICO-MG')
BOC, BOC_F = time_('BOCA JUNIORS')
PAL, PAL_F = time_('PALMEIRAS')
EST, EST_F = time_('ESTUDIANTES')
BRA, BRA_F = time_('BRASIL')
ARG, ARG_F = time_('ARGENTINA')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def put_cal(c, dia, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, 'NOV'), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    ar = wt(0, 'Argentina') - 3; du = wt(0, 'duas') - 3; dz = wt(0, 'dez') - 3
    put_trofeu(c, 470, 1180, 300, f, du)
    put_trofeu(c, 790, 1180, 300, f, du + 3)
    bx = lerp(-260, 290, easeOut(ramp(f, 0, 14)))
    axx = lerp(1500, 960, easeOut(ramp(f, ar - 10, ar + 6)))
    put_jog(c, bx, 2020, 860, f, 1, cores=BRA, faixa=BRA_F, arms='cintura', expr='stern', skin=2, look=1)
    put_jog(c, axx, 2020, 860, f, 2, cores=ARG, faixa=ARG_F, arms='cintura', expr='stern', skin=0, look=-1, hair='#5a3b22')
    num(c, 'BRASIL x ARGENTINA', 640, 700, f, wt(0, 'Brasil') - 3, 78, -3)
    num(c, '2 FINAIS', 640, 830, f, du, 110, 3)
    num(c, 'EM 10 DIAS!', 640, 970, f, dz, 110, -4)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, dz, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    ga = wt(1, 'Atletico') - 3; bo = wt(1, 'Boca') - 3
    put_cal(c, '21', 640, 1070, .5, f, wt(1, 'vinte') - 3)
    gx = lerp(-260, 310, easeOut(ramp(f, ga - 10, ga + 6)))
    bx = lerp(1500, 940, easeOut(ramp(f, bo - 10, bo + 6)))
    put_jog(c, gx, 2020, 860, f, 3, cores=GAL, faixa=GAL_F, arms='cintura', expr='stern', skin=3, hair='#111111', look=1)
    put_jog(c, bx, 2020, 860, f, 4, cores=BOC, faixa=BOC_F, arms='cintura', expr='smug', skin=1, look=-1)
    put_placa(c, 'ATLÉTICO-MG', GAL, 370, 1240, f, ga + 4, 44, -4)
    put_placa(c, 'BOCA JUNIORS', BOC, 880, 1240, f, bo + 4, 44, 4)
    num(c, 'BARRANQUILLA', 640, 700, f, wt(1, 'Barranquilla') - 3, 96, -3)
    num(c, 'FINAL DA SUL-AMERICANA', 640, 840, f, wt(1, 'final') - 3, 66, 3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0006 * f)
    return c, (640 + 20 * math.sin(f * .03), 1420, z, 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    pr = wt(2, 'primeiro') - 3; te = wt(2, 'terceiro') - 3; el = wt(2, 'eliminou') - 3
    put_jog(c, 330, 2020, 880, f, 3, cores=GAL, faixa=GAL_F, arms='up' if f >= pr else 'cintura',
            expr='grin' if f >= pr else 'stern', skin=3, hair='#111111', look=1)
    put_jog(c, 930, 2020, 880, f, 4, cores=BOC, faixa=BOC_F, arms='joinha' if f >= te else 'cintura', expr='smug', skin=1, look=-1)
    num(c, 'VICE EM 2025', 640, 700, f, wt(2, 'vice') - 3, 100, -3)
    num(c, '1º TÍTULO?', 390, 880, f, pr, 64, -4)
    if el <= f < te: num(c, 'TIROU SÃO PAULO E VASCO', 640, 1020, f, el, 56, 3)
    num(c, '3º TÍTULO?', 870, 880, f, te, 64, 4)
    z = lerp(1.06, 1.15, smooth(f / 120))
    k = kick(f, pr, .6)
    return c, (lerp(560, 720, smooth(ramp(f, pr - 10, te))), 1420 + k * 8, z, k), 'dusk'


def s3(f):
    c = estadio('day').copy()
    vo = wt(3, 'vinte') - 3; fi = wt(3, 'Libertadores') - 3
    if f < fi: num(c, 'UMA SEMANA DEPOIS', 640, 700, f, 0, 80, -3)
    num(c, 'FINAL DA LIBERTADORES', 640, 700, f, fi, 70, -3)
    put_cal(c, '28', 330, 1080, .72, f, vo)
    put_trofeu(c, 900, 1120, 520, f, fi)
    num(c, 'CENTENÁRIO', 640, 1440, f, wt(3, 'Centenario') - 3, 90, 3)
    num(c, 'MONTEVIDÉU', 640, 1580, f, wt(3, 'Montevideu') - 3, 90, -3)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, lerp(1250, 1400, smooth(ramp(f, 0, 90))), z, 0), 'golden'


def s4(f):
    c = estadio('day').copy()
    pa = wt(4, 'Palmeiras') - 3; es = wt(4, 'Estudiantes') - 3; pe = wt(4, 'penaltis') - 3
    px = lerp(-260, 310, easeOut(ramp(f, pa - 10, pa + 6)))
    ex = lerp(1500, 940, easeOut(ramp(f, es - 10, es + 6)))
    put_jog(c, px, 2020, 860, f, 5, cores=PAL, faixa=PAL_F, arms='cintura', expr='smug', skin=0, look=1)
    put_jog(c, ex, 2020, 860, f, 6, cores=EST, faixa=EST_F, arms='cintura', expr='stern', skin=1, look=-1, hair='#1a1a1a')
    put_placa(c, 'PALMEIRAS', PAL, 370, 1240, f, pa + 4, 44, -4)
    put_placa(c, 'ESTUDIANTES', EST, 880, 1240, f, es + 4, 44, 4)
    num(c, 'NOS PÊNALTIS', 640, 700, f, pe, 110, -3)
    num(c, 'TIROU O FLU', 400, 880, f, wt(4, 'Fluminense') - 3, 58, -4)
    num(c, 'TIROU O FLA', 860, 880, f, wt(4, 'Flamengo') - 3, 58, 4)
    if f >= pe: put_bola(c, 640, 2020 - raio_bola(860), raio_bola(860), f)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0006 * f)
    k = kick(f, pe, .6)
    return c, (640, 1420 + k * 8, z, k), 'golden'


def s5(f):
    c = estadio('dusk').copy()
    qu = wt(5, 'quarto') - 3; qi = wt(5, 'quinto') - 3; dz = wt(5, 'dezessete') - 3
    put_trofeu(c, 640, 1150, 440, f, 0)
    put_jog(c, 300, 2020, 860, f, 5, cores=PAL, faixa=PAL_F, arms='up' if f >= qu else 'cintura', expr='grin' if f >= qu else 'proud', skin=0, look=1)
    put_jog(c, 960, 2020, 860, f, 6, cores=EST, faixa=EST_F, arms='up' if f >= qi else 'cintura', expr='grin' if f >= qi else 'stern', skin=1, look=-1, hair='#1a1a1a')
    num(c, '4º TÍTULO?', 400, 870, f, qu, 62, -4)
    num(c, '5º TÍTULO?', 860, 870, f, qi, 62, 4)
    num(c, 'ÚLTIMO: 2009', 640, 700, f, dz, 96, -3)
    z = lerp(1.05, 1.15, smooth(f / 110))
    k = kick(f, qu, .5)
    return c, (640 + 22 * math.sin(f * .035), 1420 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    br = wt(6, 'Brasil') - 3; ar = wt(6, 'Argentina') - 3
    put_trofeu(c, 470, 1120, 360, f, 0)
    put_trofeu(c, 790, 1120, 360, f, 0)
    num(c, '2 JOGOS ÚNICOS', 640, 700, f, wt(6, 'jogos') - 3, 100, -3)
    put_jog(c, 280, 2030, 820, f, 1, cores=BRA, faixa=BRA_F, arms='up' if f >= br else 'cintura', expr='grin' if f >= br else 'stern', skin=2, look=1)
    put_jog(c, 980, 2030, 820, f, 2, cores=ARG, faixa=ARG_F, arms='up' if f >= ar else 'cintura', expr='grin' if f >= ar else 'stern', skin=0, look=-1, hair='#5a3b22')
    num(c, 'NOVEMBRO', 640, 860, f, wt(6, 'novembro') - 3, 100, 3)
    num(c, '?', 640, 1520, f, ar + 6, 200, 6)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'duas') - 3, 140, 1.0)
    s.ting(s.W(0, 'dez') - 3, .3)
    s.thunk(s.W(1, 'Boca') - 3, 160, .8)
    s.ting(s.W(2, 'primeiro') - 3, .3)
    s.ting(s.W(2, 'terceiro') - 3, .3)
    s.thunk(s.W(3, 'Libertadores') - 3, 140, .9)
    s.thunk(s.W(4, 'penaltis') - 3, 160, .8)
    s.ting(s.W(5, 'dezessete') - 3, .3)
    s.thunk(s.W(6, 'Argentina') - 3, 200, .7)
