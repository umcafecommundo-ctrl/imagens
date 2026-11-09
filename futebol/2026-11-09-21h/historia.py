"""anima.futebol — 09/11/2026 21h — Brasileirão: Data Fifa pausa a briga pelo título entre Flamengo e Palmeiras.
Fontes (conferidas em 09/11/2026): Gazeta Esportiva (classificação após 34 rodadas: Flamengo 76, Palmeiras 73,
Cruzeiro 60, Fluminense 57), Wikipedia/valorfinal (mesma tabela; 34ª rodada terminou em 06/11), CNN Brasil e Correio
Braziliense (35ª rodada em 18/11 às 20h30: Flamengo x Athletico-PR no Maracanã e Cruzeiro x Palmeiras no Mineirão;
36ª rodada: Palmeiras x Flamengo em 21/11 às 16h30, em São Paulo), DGABC (Seleção joga 14 e 17/11 em Singapura).
Cruzeiro: 60 + 4 x 3 = 72 < 76, não alcança mais o Flamengo. Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'BRASILEIRÃO  ·  RETA FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Só dois times ainda podem ser campeões brasileiros: Flamengo e Palmeiras!",
    "O Flamengo lidera com setenta e seis pontos, três a mais que o Palmeiras.",
    "O Cruzeiro, terceiro, tem sessenta, e mesmo vencendo tudo não alcança mais o líder.",
    "Faltam quatro rodadas, e agora o campeonato para por causa da data Fifa.",
    "Na volta, dia dezoito, o Flamengo recebe o Athletico no Maracanã, e o Palmeiras visita o Cruzeiro no Mineirão.",
    "E três dias depois, no dia vinte e um, tem Palmeiras contra Flamengo, em São Paulo.",
    "Pode ser a final antecipada do Brasileirão.",
]
CAPTXT = [
    "Só 2 times ainda podem ser campeões brasileiros:|Flamengo e Palmeiras!",
    "O Flamengo lidera com 76 pontos,|3 a mais que o Palmeiras.",
    "O Cruzeiro, 3º, tem 60, e mesmo vencendo tudo|não alcança mais o líder.",
    "Faltam 4 rodadas, e agora o campeonato|para por causa da Data Fifa.",
    "Na volta, dia 18, o Flamengo recebe o Athletico no Maracanã,|e o Palmeiras visita o Cruzeiro no Mineirão.",
    "E 3 dias depois, no dia 21,|tem Palmeiras contra Flamengo, em São Paulo.",
    "Pode ser a final antecipada|do Brasileirão.",
]
FALA_TIKTOK = "Quem leva o Brasileirão, Flamengo ou Palmeiras? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'dois', 4), (0, 'Palmeiras', 4), (1, 'setenta', 4), (2, 'sessenta', 4), (2, 'alcanca', 4), (3, 'quatro', 4),
         (3, 'Fifa', 4), (4, 'Maracana', 4), (4, 'Mineirao', 4), (5, 'vinte', 4), (5, 'Flamengo', 6), (6, 'final', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')
CRU, CRU_F = time_('CRUZEIRO')
CAP, CAP_F = time_('ATHLETICO-PR')
GOLEIRO = ('#2a5fb0', '#1b3f80', '#1b3f80')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def put_cal(c, dia, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, 'NOV'), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    d2 = wt(0, 'dois') - 3; fl = wt(0, 'Flamengo') - 3; pa = wt(0, 'Palmeiras') - 3
    put_trofeu(c, 640, 1130, 520, f, 0)
    num(c, 'SÓ 2 PODEM!', 640, 740, f, d2, 110, -4)
    px = lerp(-300, 330, easeOut(ramp(f, fl - 10, fl + 8)))
    qx = lerp(1550, 950, easeOut(ramp(f, pa - 10, pa + 8)))
    put_jog(c, px, 2010, 860, f, 1, cores=FLA, faixa=FLA_F, arms='cintura', expr='proud', skin=2, hair='#151515', look=1)
    put_jog(c, qx, 2010, 860, f, 6, cores=PAL, faixa=PAL_F, arms='cintura', expr='stern', skin=0, look=-1)
    put_placa(c, 'FLAMENGO', FLA, 330, 1080, f, fl + 4, 58, -4)
    put_placa(c, 'PALMEIRAS', PAL, 950, 1080, f, pa + 4, 58, 4)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, d2, .8)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    t0 = wt(1, 'lidera') - 6
    tabela(c, [('1º', 'FLAMENGO', FLA, '76', True), ('2º', 'PALMEIRAS', PAL, '73', False)], 640, 940, f, t0)
    num(c, '76 PONTOS', 640, 740, f, wt(1, 'setenta') - 3, 110, -3)
    num(c, '+3', 1000, 1330, f, wt(1, 'tres') - 3, 150, 6)
    put_jog(c, 380, 2030, 640, f, 2, cores=FLA, faixa=FLA_F, arms='up' if f >= wt(1, 'setenta') else 'joinha', expr='grin', skin=2, hair='#151515')
    put_jog(c, 880, 2030, 640, f, 7, cores=PAL, faixa=PAL_F, arms='cintura', expr='nervous', skin=1, look=-1)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 80)))
    return c, (640, lerp(1250, 1320, smooth(f / 90)), z, 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    t0 = 0
    tabela(c, [('1º', 'FLAMENGO', FLA, '76', False), ('2º', 'PALMEIRAS', PAL, '73', False),
               ('3º', 'CRUZEIRO', CRU, '60', True)], 640, 940, f, t0)
    al = wt(2, 'alcanca') - 3
    num(c, '60 + 12 = 72', 640, 760, f, wt(2, 'vencendo') - 3, 96, -3)
    num(c, 'NÃO DÁ!', 900, 1560, f, al, 120, 6)
    put_jog(c, 420, 2040, 600, f, 4, cores=CRU, faixa=CRU_F, arms='shrug' if f >= al else 'hang',
            expr='pained' if f >= al else 'neutral', skin=1)
    k = kick(f, al, .8)
    z = lerp(1.06, 1.0, smooth(ramp(f, 0, 70)))
    return c, (lerp(620, 660, smooth(f / 90)), 1300 + k * 10, z, k), 'dusk'


def s3(f):
    c = estadio('day').copy()
    q = wt(3, 'quatro') - 3; fi = wt(3, 'Fifa') - 3
    num(c, 'FALTAM 4 RODADAS', 640, 760, f, q, 84, -3)
    num(c, 'PAUSA: DATA FIFA', 640, 920, f, fi, 84, 3)
    # jogadores param, bola parada no meio
    put_jog(c, 360, 2010, 840, f, 1, cores=FLA, faixa=FLA_F, arms='cintura' if f >= fi else 'run', walk=0 if f >= fi else (f / 16) % 1,
            expr='neutral', skin=2, hair='#151515', look=1)
    put_jog(c, 920, 2010, 840, f, 6, cores=PAL, faixa=PAL_F, arms='cintura' if f >= fi else 'run', walk=0 if f >= fi else (f / 16 + .5) % 1,
            expr='neutral', skin=0, look=-1)
    rb = raio_bola(840)
    put_bola(c, 640, 2010 - rb, rb, 0 if f >= fi else f)
    z = lerp(1.1, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0007 * f)
    k = kick(f, fi, .7)
    return c, (640, 1420 + k * 10, z, k), 'golden'


def s4(f):
    c = estadio('dusk').copy()
    d = wt(4, 'dezoito') - 3; pa = wt(4, 'Palmeiras') - 3
    put_cal(c, '18', 640, 800, .5, f, d)
    if f < pa - 6:
        num(c, 'MARACANÃ', 640, 960, f, wt(4, 'Maracana') - 3, 96, -3)
        put_jog(c, 350, 2010, 840, f, 1, cores=FLA, faixa=FLA_F, arms='cintura', expr='proud', skin=2, hair='#151515', look=1)
        put_jog(c, 930, 2010, 840, f, 3, cores=CAP, faixa=CAP_F, arms='cintura', expr='stern', skin=0, look=-1)
        put_placa(c, 'FLAMENGO', FLA, 350, 1090, f, wt(4, 'Flamengo') - 3, 54, -4)
        put_placa(c, 'ATHLETICO-PR', CAP, 930, 1090, f, wt(4, 'Athletico') - 3, 50, 4)
    else:
        num(c, 'MINEIRÃO', 640, 960, f, wt(4, 'Mineirao') - 3, 96, -3)
        put_jog(c, 350, 2010, 840, f, 4, cores=CRU, faixa=CRU_F, arms='cintura', expr='stern', skin=1, look=1)
        put_jog(c, 930, 2010, 840, f, 6, cores=PAL, faixa=PAL_F, arms='cintura', expr='proud', skin=0, look=-1)
        put_placa(c, 'CRUZEIRO', CRU, 350, 1090, f, pa, 54, -4)
        put_placa(c, 'PALMEIRAS', PAL, 930, 1090, f, pa + 3, 54, 4)
    k = kick(f, pa, .7)
    return c, (lerp(600, 680, smooth(f / 150)), 1400 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s5(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    v = wt(5, 'vinte') - 3; pa = wt(5, 'Palmeiras') - 3; fl = wt(5, 'Flamengo') - 3
    put_cal(c, '21', 300, 860, .55, f, v)
    num(c, '16H30', 300, 1110, f, v + 6, 80, -3)
    put_goleiro(c, f, GOLEIRO, None, arms='hang', expr='nervous', skin=1)
    px = lerp(-260, 400, easeOut(ramp(f, pa - 10, pa + 8)))
    qx = lerp(1550, 860, easeOut(ramp(f, fl - 10, fl + 8)))
    put_jog(c, px, 2010, 860, f, 6, cores=PAL, faixa=PAL_F, arms='cintura', expr='stern', skin=0, look=1)
    put_jog(c, qx, 2010, 860, f, 1, cores=FLA, faixa=FLA_F, arms='cintura', expr='stern', skin=2, hair='#151515', look=-1)
    put_placa(c, 'PALMEIRAS', PAL, 400, 1090, f, pa + 4, 54, -4)
    put_placa(c, 'FLAMENGO', FLA, 860, 1090, f, fl + 4, 54, 4)
    num(c, 'X', 630, 1750, f, fl + 6, 140)
    rb = raio_bola(860)
    put_bola(c, 630, 2010 - rb, rb, f)
    num(c, 'EM SÃO PAULO', 700, 740, f, wt(5, 'Sao') - 3, 92, -3)
    z = lerp(1.25, 1.04, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, fl, .9)
    return c, (640, 1400 + k * 10, z, k + lerp(0, -2, smooth(f / 90))), 'golden'


def s6(f):
    c = estadio('dusk').copy()
    put_trofeu(c, 640, 1150, 600, f, 0)
    num(c, 'FINAL ANTECIPADA?', 640, 730, f, wt(6, 'final') - 3, 96, -3)
    put_jog(c, 250, 2040, 760, f, 1, cores=FLA, faixa=FLA_F, arms='point', expr='smug', skin=2, hair='#151515')
    put_jog(c, 1030, 2050, 740, f, 6, cores=PAL, faixa=PAL_F, arms='point', expr='smug', skin=0, flip=True)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1360, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'dois') - 3, 140, 1.0)
    s.ting(s.W(1, 'setenta') - 3, .3)
    s.thunk(s.W(2, 'alcanca') - 3, 160, .8)
    s.ting(s.W(3, 'quatro') - 3, .3)
    s.thunk(s.W(3, 'Fifa') - 3, 200, .7)
    s.ting(s.W(4, 'dezoito') - 3, .3)
    s.thunk(s.W(5, 'Flamengo') - 3, 160, 1.0)
    s.ting(s.W(6, 'final') - 3, .35)
