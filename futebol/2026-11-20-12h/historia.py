"""anima.futebol — 20/11/2026 12h — CONTA DO TÍTULO · EP. 1 — Palmeiras x Flamengo amanhã (21/11) 16h30 no Nubank Parque.
Fontes (conferidas em 20/11/2026): Lance (18/11: Fla 79 x Pal 73; vitória = 82 pts e título; empate = 80 e não pode mais ser
ultrapassado; vitória do Palmeiras faz a diferença cair para 3), Boca Notícias (79 pts em 35 jogos, 3 rodadas, sábado 16h30,
empate garante o título, desempate por vitórias favorece o Fla, Palmeiras precisa da vitória), Super Rádio Tupi (19/11: 36ª rodada,
sábado (21) 16h30 no Nubank Parque, basta um empate, se o Palmeiras vencer a festa fica para as rodadas finais).
Só em 1 fonte -> não usado: número de vitórias (24 x 21), título de 1999, desfalques. Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  36ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Flamengo pode ser campeão amanhã, na casa do Palmeiras?",
    "Faltam três rodadas. O Flamengo tem setenta e nove pontos, o Palmeiras... setenta e três.",
    "Amanhã tem confronto direto no Nubank Parque, às dezesseis e trinta.",
    "Se o Flamengo vencer ou empatar... é campeão.",
    "O Palmeiras precisa ganhar. Aí a diferença cai para... três pontos.",
    "E sobram só duas rodadas. Quem leva?",
]
CAPTXT = [
    "O Flamengo pode ser campeão amanhã,|na casa do Palmeiras?",
    "Faltam 3 rodadas. O Flamengo tem 79 pontos,|o Palmeiras... 73.",
    "Amanhã tem confronto direto|no Nubank Parque, às 16h30.",
    "Se o Flamengo vencer ou empatar...|é campeão.",
    "O Palmeiras precisa ganhar.|Aí a diferença cai para... 3 pontos.",
    "E sobram só 2 rodadas.|Quem leva?",
]
FALA_TIKTOK = "Quem leva o título, Flamengo ou Palmeiras? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'Flamengo', 4), (0, 'Palmeiras', 4), (1, 'tres', 4), (1, 'setenta', 4), (2, 'Nubank', 4), (2, 'dezesseis', 4),
         (3, 'empatar', 4), (3, 'campeao', 4), (4, 'ganhar', 4), (4, 'tres', 4), (5, 'duas', 4), (5, 'leva', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def s0(f):
    """conta_bg: marca da série grande e depois a pergunta polêmica."""
    c = conta_bg().copy()
    pa = wt(0, 'Palmeiras') - 3; ca = wt(0, 'campeao') - 3
    q = max(42, ca - 4)
    fla(c, 300, 2060, 760, f, 3, arms='punho' if f >= ca else 'cintura', expr='grin' if f >= ca else 'stern', look=1, num_='10')
    pal(c, 960, 2060, 760, f, 6, arms='cintura', expr='stern' if f < pa else 'nervous', look=-1, flip=True, num_='9')
    if f < q - 2:
        num(c, 'CONTA DO TÍTULO', 640, 860, f, 0, 92, -3)
        num(c, 'EP. 1', 640, 1040, f, 4, 130, 3)
    else:
        num(c, 'CAMPEÃO', 640, 860, f, q, 140, -3)
        num(c, 'AMANHÃ?', 640, 1040, f, q + 3, 150, 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, q, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """telão: a tabela dos dois de cima."""
    c = telao('dusk').copy()
    tr = wt(1, 'tres') - 3; se = wt(1, 'setenta') - 3
    if f < se - 2:
        num(c, '3 RODADAS', 640, 950, f, tr, 140, -3)
    else:
        tabela(c, [('1º', 'FLAMENGO', FLA, '79', True), ('2º', 'PALMEIRAS', PAL, '73', False)], 640, 830, f, se)
    fla(c, 260, 2080, 620, f, 4, arms='cintura', expr='stern', look=1)
    pal(c, 1000, 2080, 620, f, 8, arms='hang', expr='nervous', look=-1, flip=True)
    z = lerp(1.0, 1.08, smooth(f / 120))
    k = kick(f, se, .5)
    return c, (640 + 20 * math.sin(f * .03), 1300 + k * 8, z, k), 'dusk'


def s2(f):
    """estádio de dia: frente a frente, data, local e hora."""
    c = estadio2('day').copy()
    am = wt(2, 'Amanha') - 3; nu = wt(2, 'Nubank') - 3; de = wt(2, 'dezesseis') - 3
    fx = lerp(-260, 360, easeOut(ramp(f, 0, 16)))
    px = lerp(1500, 900, easeOut(ramp(f, 0, 16)))
    if f < 16:
        linhas_vel(c, fx, 2010, 840, f, dir=-1); linhas_vel(c, px, 2010, 840, f, dir=1)
    fla(c, fx, 2010, 840, f, 3, arms='cintura', expr='stern', look=1, num_='10', run=(f * .1) % 1 if f < 16 else None)
    pal(c, px, 2010, 840, f, 7, arms='punho', expr='stern', look=-1, flip=True, num_='9', run=(f * .1) % 1 if f < 16 else None)
    if f < nu - 2:
        if f >= am: paste_c(c, calendario('21', 'NOV'), 640, 900, .55 * back(ramp(f, am, am + 8)))
    elif f < de - 2:
        num(c, 'NUBANK PARQUE', 640, 900, f, nu, 92, -3)
    else:
        num(c, '16H30', 640, 900, f, de, 170, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, de, .6)
    return c, (640, 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'day'


def s3(f):
    """estádio dourado com a taça genérica: vence ou empata = campeão."""
    c = estadio2('golden').copy()
    ve = wt(3, 'vencer') - 3; ca = wt(3, 'campeao') - 3
    paste_c(c, trofeu(), 900, 1500, .75 + .02 * math.sin(f * .1))
    fla(c, 420, 2030, 880, f, 5, arms='up' if f >= ca else 'cintura', expr='grin' if f >= ca else 'stern', look=1, num_='10')
    if f < ca - 2:
        num(c, 'VENCE OU EMPATA', 640, 800, f, ve, 92, -3)
    else:
        if f >= ca: explosao(c, 640, 820, f, ca, 200)
        num(c, 'CAMPEÃO!', 640, 820, f, ca, 170, 3)
        if f >= ca: confete(c, 640, 900, f, ca, 60, 600)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, ca, .8)
    return c, (640, 1420 + k * 10, z, k), 'golden'


def s4(f):
    """vestiário do Palmeiras: precisa vencer, diferença cai para 3."""
    c = vestiario(PAL, PAL_F).copy()
    ga = wt(4, 'ganhar') - 3; tr = wt(4, 'tres') - 3
    pal(c, 640, 2110, 820, f, 6, arms='punho' if f >= ga else 'hang', expr='stern', look=0, num_='9')
    if f < tr - 2:
        num(c, 'PRECISA VENCER', 640, 1110, f, ga, 94, -3)
    else:
        num(c, '3 PONTOS', 640, 1110, f, tr, 160, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, tr, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s5(f):
    """prancheta: as 2 rodadas finais e a pergunta."""
    c = prancheta().copy()
    du = wt(5, 'duas') - 3; le = wt(5, 'leva') - 3
    pino(c, 420, 1500 + 14 * math.sin(f * .18), FLA, f, 2, 'F', 90)
    pino(c, 820, 1500 + 14 * math.sin(f * .18 + 1.6), PAL, f, 6, 'P', 90)
    seta(c, (420, 1400), (560, 1260), f, du + 4)
    seta(c, (820, 1400), (680, 1260), f, du + 6)
    if f < le - 2:
        num(c, '2 RODADAS', 640, 900, f, du, 150, -3)
    else:
        num(c, 'QUEM LEVA?', 640, 900, f, le, 124, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, le, .6)
    return c, (640 + 26 * math.sin(f * .05), 1300 + k * 8, z * (1 + .002 * f), lerp(0, 2, smooth(ramp(f, 0, 60)))), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    # s.torcida(s.cut(1), s.cut(4), 1.0)              # telão + estádio de dia + estádio dourado
    # s.torcida(s.cut(4), s.cut(5), .4)               # vestiário: torcida de longe
    s.thunk(s.W(0, 'Flamengo') - 3, 150, .8)
    s.thunk(s.W(0, 'campeao') - 3, 120, .9)
    s.thunk(s.W(1, 'tres') - 3, 150, .8)
    s.thunk(s.W(1, 'setenta') - 3, 120, .9)
    s.apito(s.W(2, 'Amanha') - 3)
    s.thunk(s.W(2, 'Nubank') - 3, 150, .7)
    s.thunk(s.W(2, 'dezesseis') - 3, 120, .9)
    s.thunk(s.W(3, 'vencer') - 3, 150, .8)
    s.ting(s.W(3, 'campeao') - 3, .35)
    s.rugido(s.W(3, 'campeao') - 1, 2.2, .7)
    s.thunk(s.W(4, 'ganhar') - 3, 150, .8)
    s.thunk(s.W(4, 'tres') - 3, 120, 1.0)
    s.thunk(s.W(5, 'duas') - 3, 140, .8)
    s.ting(s.W(5, 'leva') - 3, .3)
