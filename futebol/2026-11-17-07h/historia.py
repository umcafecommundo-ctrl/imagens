"""anima.futebol — 17/11/2026 07h — Brasileirão: Flamengo pode ser campeão já no sábado.
Fontes (conferidas em 17/11/2026): O Presente (15/11: Brasileirão volta quarta 18/11; Flamengo 76 pts, 23V 7E 4D; Palmeiras 73 pts,
21V 10E 3D; 4 rodadas; Flamengo x Athletico-PR 20h30 Maracanã e Cruzeiro x Palmeiras 20h30 Mineirão na quarta; confronto direto
sábado 21/11); aRede (08/11: 76 x 73 após 34 jogos; Palmeiras x Flamengo sábado 21/11 16h30 na casa do Palmeiras; 1º critério de
desempate = vitórias); Flashscore (tabela CBF rodadas 35 e 36: Palmeiras x Flamengo 21/11 16h30 Nubank Parque).
Conta: se o Fla vence quarta e sábado chega a 82 pts e 25 vitórias; o Palmeiras chega no máximo a 82 pts e 24 vitórias -> título no sábado.
Se o Palmeiras vence os dois, chega a 79 e encosta (passa se o Fla não vencer na quarta).
Sem escudos/logos/taças reais: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª E 36ª RODADAS'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Flamengo pode ser campeão brasileiro já neste sábado.",
    "O Brasileirão volta amanhã, depois da Data Fifa, e faltam só quatro rodadas.",
    "O Flamengo lidera com setenta e seis pontos, três a mais que o Palmeiras.",
    "Amanhã à noite, o Flamengo recebe o Athletico no Maracanã, e o Palmeiras visita o Cruzeiro no Mineirão.",
    "E no sábado, às quatro e meia da tarde, os dois se enfrentam na casa do Palmeiras.",
    "Se o Flamengo vencer os dois jogos, é campeão no sábado, porque o Palmeiras não alcança mais nem no número de vitórias.",
    "Mas se o Palmeiras vencer os dois, encosta ou até passa na frente, e a briga segue aberta.",
    "Sábado pode ser o dia da festa, ou o dia da virada.",
]
CAPTXT = [
    "O Flamengo pode ser campeão brasileiro|já neste sábado.",
    "O Brasileirão volta amanhã, depois da Data Fifa,|e faltam só 4 rodadas.",
    "O Flamengo lidera com 76 pontos,|3 a mais que o Palmeiras.",
    "Amanhã à noite, o Flamengo recebe o Athletico no Maracanã,|e o Palmeiras visita o Cruzeiro no Mineirão.",
    "E no sábado, às 16h30,|os dois se enfrentam na casa do Palmeiras.",
    "Se o Flamengo vencer os 2 jogos, é campeão no sábado,|porque o Palmeiras não alcança mais nem no número de vitórias.",
    "Mas se o Palmeiras vencer os 2, encosta|ou até passa na frente, e a briga segue aberta.",
    "Sábado pode ser o dia da festa,|ou o dia da virada.",
]
FALA_TIKTOK = "Quem leva o Brasileirão, Flamengo ou Palmeiras? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'campeao', 4), (0, 'sabado', 4), (1, 'amanha', 4), (1, 'quatro', 4), (2, 'setenta', 4), (2, 'Palmeiras', 4),
         (3, 'Athletico', 4), (3, 'Cruzeiro', 4), (4, 'quatro', 4), (4, 'Palmeiras', 4), (5, 'campeao', 4), (5, 'vitorias', 4),
         (6, 'Palmeiras', 4), (6, 'aberta', 4), (7, 'festa', 4), (7, 'virada', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')
CAP, CAP_F = time_('ATHLETICO-PR')
CRU, CRU_F = time_('CRUZEIRO')


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    ca = wt(0, 'campeao') - 3; sa = wt(0, 'sabado') - 3
    put_trofeu(c, 900, 1250, 520, f, ca)
    fla(c, 400, 2020, 880, f, 3, arms='up' if f >= ca else 'cintura', expr='grin' if f >= ca else 'stern', look=1, num_='10')
    put_placa(c, 'FLAMENGO', FLA, 400, 1100, f, wt(0, 'Flamengo') - 3, 60, -3)
    explosao(c, 640, 760, f, ca, 220)
    num(c, 'CAMPEÃO?', 640, 760, f, ca + 2, 130, -4)
    if f >= sa: paste_c(c, calendario('21', 'NOV'), 960, 1680 - 260, .5 * back(ramp(f, sa, sa + 8)))
    if f >= ca: confete(c, 640, 900, f, ca, 50, 500)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ca, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('golden').copy()
    am = wt(1, 'amanha') - 3; qu = wt(1, 'quatro') - 3
    if f >= am: paste_c(c, calendario('18', 'NOV'), 640, 1150, .7 * back(ramp(f, am, am + 8)))
    num(c, 'VOLTA AMANHÃ', 640, 720, f, am, 110, -3)
    num(c, 'FALTAM 4 RODADAS', 640, 1500, f, qu, 80, 3)
    fla(c, 230, 2120, 560, f, 4, arms='hang', expr='neutral', look=1)
    pal(c, 1040, 2120, 560, f, 8, arms='hang', expr='neutral', look=-1, flip=True)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1360, z, 0), 'golden'


def s2(f):
    c = estadio2('dusk').copy()
    se = wt(2, 'setenta') - 3; tr = wt(2, 'tres') - 3
    tabela(c, [('1º', 'FLAMENGO', FLA, '76', True), ('2º', 'PALMEIRAS', PAL, '73', False)], 640, 1060, f, se)
    num(c, '+3 PONTOS', 640, 720, f, tr, 120, -3)
    fla(c, 300, 2060, 560, f, 5, arms='joinha' if f >= se else 'cintura', expr='proud', look=1)
    pal(c, 980, 2060, 560, f, 9, arms='cintura', expr='stern', look=-1, flip=True)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, se, .5)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    fl = wt(3, 'Flamengo') - 3; at = wt(3, 'Athletico') - 3; pa = wt(3, 'Palmeiras') - 3; cr = wt(3, 'Cruzeiro') - 3
    num(c, 'QUARTA, 20H30', 640, 700, f, wt(3, 'noite') - 3, 100, -3)
    # esquerda: Flamengo x Athletico
    fla(c, 190, 1700, 520, f, 6, arms='cintura', expr='stern', look=1)
    put_placa(c, 'FLAMENGO', FLA, 210, 1060, f, fl, 34, -3)
    if f >= at - 6:
        put_atleta(c, 450, 1700, 520, f, 12, cores=CAP, faixa=CAP_F, skin=1, hair='#2a1a10', arms='cintura', expr='stern', look=-1, flip=True)
        put_placa(c, 'ATHLETICO-PR', CAP, 450, 1200, f, at, 32, 3)
    num(c, 'MARACANÃ', 330, 880, f, wt(3, 'Maracana') - 3, 60, 2)
    # direita: Cruzeiro x Palmeiras
    if f >= pa - 6:
        pal(c, 1000, 2040, 560, f, 9, arms='cintura', expr='stern', look=-1, flip=True)
        put_placa(c, 'PALMEIRAS', PAL, 990, 1440, f, pa, 32, 3)
    if f >= cr - 6:
        put_atleta(c, 760, 2040, 560, f, 13, cores=CRU, faixa=CRU_F, skin=3, hair='#111111', arms='cintura', expr='stern', look=1)
        put_placa(c, 'CRUZEIRO', CRU, 760, 1560, f, cr, 32, -3)
    num(c, 'MINEIRÃO', 880, 1300, f, wt(3, 'Mineirao') - 3, 60, -2)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0005 * f)
    return c, (lerp(620, 660, smooth(f / 150)), 1400, z, 0), 'dusk'


def s4(f):
    c = estadio2('day').copy()
    sa = wt(4, 'sabado') - 3; qu = wt(4, 'quatro') - 3; en = wt(4, 'enfrentam') - 3
    fx = lerp(-260, 360, easeOut(ramp(f, en - 12, en + 4)))
    px = lerp(1500, 900, easeOut(ramp(f, en - 12, en + 4)))
    if f < en + 4:
        linhas_vel(c, fx, 2010, 860, f, dir=-1); linhas_vel(c, px, 2010, 860, f, dir=1)
    fla(c, fx, 2010, 860, f, 3, arms='cintura', expr='stern', look=1, num_='10', run=(f * .1) % 1 if f < en + 4 else None)
    pal(c, px, 2010, 860, f, 7, arms='cintura', expr='stern', look=-1, flip=True, num_='9', run=(f * .1) % 1 if f < en + 4 else None)
    put_placa(c, 'FLAMENGO', FLA, 360, 1110, f, en + 4, 54, -3)
    put_placa(c, 'PALMEIRAS', PAL, 900, 1110, f, en + 4, 54, 3)
    if f >= sa: paste_c(c, calendario('21', 'NOV'), 380, 780 + 60, .5 * back(ramp(f, sa, sa + 8)))
    num(c, '16H30', 900, 820, f, qu, 140, 4)
    num(c, 'X', 640, 1500, f, en + 4, 160)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, en + 4, .7)
    return c, (640, 1400 + k * 8, z, k), 'golden'


def s5(f):
    c = estadio2('dusk').copy()
    ve = wt(5, 'vencer') - 3; ca = wt(5, 'campeao') - 3; vi = wt(5, 'vitorias') - 3
    gx, gy = put_gol2(c, estufa=ramp(f, ca + 6, ca + 12))
    put_goleiro(c, f, PAL, PAL_F, arms='shrug' if f >= ca + 6 else 'hang', expr='shock' if f >= ca + 6 else 'nervous', skin=1)
    sx = lerp(260, 470, easeOut(ramp(f, 0, ca - 4)))
    if f < ca - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    fla(c, sx, 2010, 860, f, 5, num_='10', arms='up' if f >= ca + 8 else 'run', run=(f * .1) % 1 if f < ca - 4 else None,
        kick=pulse(f, ca - 3, 5), expr='grin' if f >= ca else 'stern')
    rb = raio_bola(860)
    if f < ca + 40: bola_voo(c, f, ca, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 140)
    if f >= ca + 6: explosao(c, 640, 900, f, ca + 6, 160)
    num(c, 'VENCEU 2 =', 640, 690, f, ve, 100, -3)
    num(c, 'CAMPEÃO!', 640, 900, f, ca + 8, 120, 3)
    num(c, 'MAIS VITÓRIAS', 640, 1080, f, vi, 76, -2)
    if f >= ca + 8: confete(c, 500, 1300, f, ca + 8, 50, 400)
    k = kick(f, ca, .9)
    return c, (lerp(600, 680, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0007 * f), k), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    pa = wt(6, 'Palmeiras') - 3; en = wt(6, 'encosta') - 3; ab = wt(6, 'aberta') - 3
    pal(c, 640, 2030, 920, f, 7, num_='9', arms='punho' if f >= en else 'cintura', expr='grin' if f >= en else 'stern')
    put_placa(c, 'PALMEIRAS', PAL, 640, 1100, f, pa, 64, -3)
    if f >= en: foco(c, 640, 1650, 440, .6 * ramp(f, en, en + 6))
    num(c, 'VENCEU 2 = ENCOSTA', 640, 720, f, en, 70, -3)
    num(c, 'BRIGA ABERTA', 640, 880, f, ab, 110, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, en, .6)
    return c, (lerp(660, 620, smooth(f / 90)), 1420 + k * 8, z, k), 'dusk'


def s7(f):
    c = estadio2('dusk').copy()
    fe = wt(7, 'festa') - 3; vi = wt(7, 'virada') - 3
    put_trofeu(c, 640, 1250, 520, f, 0)
    fla(c, 290, 2040, 740, f, 3, arms='up' if f >= fe else 'cintura', expr='grin' if f >= fe else 'stern', look=1, num_='10')
    pal(c, 990, 2040, 740, f, 7, arms='punho' if f >= vi else 'cintura', expr='stern', look=-1, flip=True, num_='9')
    put_placa(c, 'FLAMENGO', FLA, 300, 1220, f, 0, 38, -3)
    put_placa(c, 'PALMEIRAS', PAL, 960, 1220, f, 0, 38, 3)
    num(c, 'FESTA?', 420, 720, f, fe, 110, -4)
    num(c, 'VIRADA?', 820, 860, f, vi, 110, 4)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('FLAMENGO CAMPEÃO?', 'PODE SER JÁ NO SÁBADO', wt(0, 'campeao') + 2),
         1: ('O BRASILEIRÃO VOLTA', 'FALTAM 4 RODADAS', wt(1, 'quatro') + 6),
         2: ('FLAMENGO 76 x 73 PALMEIRAS', 'DIFERENÇA DE 3 PONTOS', wt(2, 'Palmeiras') + 4),
         3: ('QUARTA, 18/11, 20H30', 'FLA x ATHLETICO  ·  CRUZEIRO x PALMEIRAS', wt(3, 'Mineirao') + 4),
         4: ('PALMEIRAS x FLAMENGO', 'SÁBADO, 21/11, ÀS 16H30', wt(4, 'Palmeiras') + 4),
         5: ('2 VITÓRIAS = TÍTULO', 'FLAMENGO TEM MAIS VITÓRIAS', wt(5, 'vitorias') + 4),
         6: ('PALMEIRAS VENCE 2?', 'ENCOSTA OU PASSA NA FRENTE', wt(6, 'encosta') - 2),
         7: ('SÁBADO DECISIVO', 'FESTA OU VIRADA?', 4)}
    if si == 7: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'campeao') - 3, 150, .9)
    s.ting(s.W(0, 'sabado') - 3, .3)
    s.thunk(s.W(1, 'amanha') - 3, 160, .6)
    s.ting(s.W(1, 'quatro') - 3, .3)
    s.thunk(s.W(2, 'setenta') - 3, 150, .7)
    s.thunk(s.W(3, 'Athletico') - 3, 200, .5)
    s.thunk(s.W(3, 'Cruzeiro') - 3, 200, .5)
    s.thunk(s.W(4, 'enfrentam') - 3, 140, .9)
    s.thunk(s.W(5, 'campeao') - 3, 120, 1.0)
    s.ting(s.W(5, 'vitorias') - 3, .35)
    s.thunk(s.W(6, 'encosta') - 3, 150, .7)
    s.ting(s.W(7, 'virada') - 3, .3)
