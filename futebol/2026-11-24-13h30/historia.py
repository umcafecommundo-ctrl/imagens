"""anima.futebol — 24/11/2026 13h30 — RAIO-X · EP. 4 — Chapecoense x Palmeiras hoje 18h na Arena Condá (37ª rodada).
Fontes (conferidas em 24/11/2026, ver fatos.txt): ESPN (23/11), Bolavip (24/11), brasileirao.com.br (24/11),
Campo Grande News (24/11), Gazeta Esportiva (23/11), Portal do Palestra (23/11). Abel poupa os titulares e leva 19 jogadores;
Koné, Heittor e Fabiano do sub-20; Chape lanterna 21 e rebaixada; Palmeiras vice com 74; final x Estudiantes sáb 28/11.
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  37ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Palmeiras vai de reserva hoje? Olha a prancheta.",
    "Abel levou só dezenove jogadores a Chapecó... e deixou os titulares em casa.",
    "Três garotos do sub-vinte vão junto: Koné, Heittor e Fabiano.",
    "Do outro lado, a Chape, já rebaixada, tem vinte e um pontos.",
    "O Palmeiras, com o vice garantido, tem setenta e quatro.",
    "O motivo é sábado: a final contra o Estudiantes. Poupar foi certo?",
]
CAPTXT = [
    "O Palmeiras vai de reserva hoje?|Olha a prancheta.",
    "Abel levou só 19 jogadores a Chapecó...|e deixou os titulares em casa.",
    "Três garotos do sub-20 vão junto:|Koné, Heittor e Fabiano.",
    "Do outro lado, a Chape,|já rebaixada, tem 21 pontos.",
    "O Palmeiras, com o vice garantido,|tem 74.",
    "O motivo é sábado: a final contra|o Estudiantes. Poupar foi certo?",
]
FALA_TIKTOK = "Poupar foi certo? Comenta sim ou não."
CTA_TEXTO = "POUPAR CERTO?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [1]
CHECK = [(0, 'Palmeiras', 4), (0, 'prancheta', 4), (1, 'dezenove', 4), (1, 'titulares', 4), (2, 'Kone', 4), (2, 'Heittor', 4),
         (2, 'Fabiano', 4), (3, 'rebaixada', 4), (3, 'um', 4), (4, 'vice', 4), (4, 'quatro', 4), (5, 'sabado', 4),
         (5, 'Estudiantes', 4), (5, 'certo', 4)]

PAL, PAL_F = time_('PALMEIRAS')
CHA, CHA_F = time_('CHAPECOENSE')
EST, EST_F = time_('ESTUDIANTES')


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor palmeirense + série + pergunta; depois a prancheta."""
    c = prancheta().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, roupa='#1b6b3a', pele='#e0ac85', cabelo='#3a2a1e')
        num(c, 'RAIO-X', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 4', 621, 440, f, 0, 100, 2)
        num(c, 'PALMEIRAS', 621, 1350, f, 0, 140, -2)
        num(c, 'DE RESERVA?', 621, 1530, f, 0, 140, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    pr = wt(0, 'prancheta') - 3
    for i, (x, y) in enumerate([(380, 1150), (862, 1150), (621, 1380), (380, 1600), (862, 1600)]):
        pino(c, x, y + 12 * math.sin(f * .2 + i), PAL, f, CLOSE_F + i * 3, '?', 80)
    if f < pr - 2:
        put_placa(c, 'PALMEIRAS', PAL, 640, 820, f, CLOSE_F, 100, -3)
    else:
        num(c, 'RESERVAS?', 640, 820, f, pr, 120, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, pr if f >= pr else CLOSE_F, .7)
    return c, (640, 1320 + k * 10, z, k), 'day'


def s1(f):
    """vestiário: 19 relacionados, titulares ficam."""
    c = vestiario(PAL, PAL_F).copy()
    dz = wt(1, 'dezenove') - 3; ti = wt(1, 'titulares') - 3
    pal(c, 640, 2100, 820, f, 6, arms='cintura' if f < ti else 'cheek', expr='stern' if f < ti else 'nervous', look=0, num_='19')
    if f < ti - 2:
        if f >= dz: numero_gigante(c, '19', 640, 1180, f, dz, 280, -3)
        else: put_placa(c, 'ABEL', PAL, 640, 1180, f, 0, 100)
    else:
        num(c, 'SEM TITULARES', 640, 1180, f, ti, 110, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, ti if f >= ti else dz, .6)
    return c, (640 + 20 * math.sin(f * .04), 1380 + k * 8, z, k), 'day'


def s2(f):
    """prancheta: os três do sub-20 (K, H, F) entram no desenho."""
    c = prancheta().copy()
    ko = wt(2, 'Kone') - 3; he = wt(2, 'Heittor') - 3; fa = wt(2, 'Fabiano') - 3
    for i, x in enumerate((300, 520, 722, 942)):
        pino(c, x, 1050 + 12 * math.sin(f * .2 + i), PAL, f, 2 + i * 2, '', 58)
    alvo = [(380, 1460, ko, 'K'), (621, 1520, he, 'H'), (862, 1460, fa, 'F')]
    for (x, y, t0, r) in alvo:
        if f >= t0: seta(c, (x, 1900), (x, y + 110), f, t0, 10, (255, 216, 74), 12)
        pino(c, x, y + 12 * math.sin(f * .2 + x), PAL, f, t0, r, 90)
    num(c, 'SUB-20', 640, 800, f, 0, 130, -3)
    z = lerp(1.06, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0004 * f)
    k = kick(f, fa if f >= fa else (he if f >= he else ko), .6)
    return c, (640 + 12 * math.sin(f * .06), 1330 + k * 8 + 20 * math.sin(f * .045), z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s3(f):
    """telão: a Chape, rebaixada, 21 pontos."""
    c = telao('dusk').copy()
    rb = wt(3, 'rebaixada') - 3; um = wt(3, 'um') - 3
    put_atleta(c, 640, 2080, 740, f, 3, cores=CHA, faixa=CHA_F, skin=3, hs='curto', hair='#151010',
               arms='hang' if f < rb else 'cheek', expr='stern' if f < rb else 'pained', look=0, num_='9', flip=True)
    if f < um - 2:
        telao_txt(c, [('CHAPE', 150)], f, 0, y=700)
    else:
        telao_txt(c, [('CHAPE', 110), ('21', 200)], f, um, y=640)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, um if f >= um else rb, .6)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s4(f):
    """a conta: Palmeiras vice com 74."""
    c = conta_bg().copy()
    vi = wt(4, 'vice') - 3; qu = wt(4, 'quatro') - 6
    pal(c, 640, 2090, 760, f, 5, arms='punho' if f < qu else 'up', expr='stern' if f < qu else 'grin', look=0, num_='10')
    if f < qu - 2:
        put_placa(c, 'VICE GARANTIDO', PAL, 640, 1000, f, vi, 80, -2)
    else:
        numero_gigante(c, '74', 640, 1000, f, qu, 300, 3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, qu if f >= qu else vi, .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """estádio ao entardecer: sábado 28, a final contra o Estudiantes, e a pergunta."""
    c = estadio2('golden').copy()
    sa = wt(5, 'sabado') - 3; es = wt(5, 'Estudiantes') - 3; ce = wt(5, 'certo') - 8
    pal(c, 400, 2030, 820, f, 6, arms='cintura', expr='stern', look=1, num_='10')
    put_atleta(c, 900, 2030, 820, f, 4, cores=EST, faixa=EST_F, skin=1, hs='curto', hair='#2a1a10',
               arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    if f < es - 2:
        if f >= sa: paste_c(c, calendario('28', 'NOV'), 640, 1000, .95 * back(ramp(f, sa, sa + 8)))
    elif f < ce - 2:
        put_placa(c, 'x ESTUDIANTES', EST, 640, 900, f, es, 90, 3)
    else:
        num(c, 'CERTO?', 640, 900, f, ce, 190, -3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ce if f >= ce else (es if f >= es else sa), .7)
    return c, (640, 1400 + k * 8, z * (1 + .0015 * max(0, f - ce)), lerp(0, 2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'prancheta') - 3, 130, .7)
    s.thunk(s.W(1, 'dezenove') - 3, 150, .9)
    s.thunk(s.W(1, 'titulares') - 3, 130, .8)
    s.thunk(s.W(2, 'Kone') - 3, 170, .5)
    s.thunk(s.W(2, 'Heittor') - 3, 170, .5)
    s.thunk(s.W(2, 'Fabiano') - 3, 170, .6)
    s.thunk(s.W(3, 'um') - 3, 150, .9)
    s.thunk(s.W(4, 'quatro') - 6, 160, 1.0)
    s.apito(s.W(5, 'sabado') - 4)
    s.thunk(s.W(5, 'Estudiantes') - 3, 130, .8)
    s.ting(s.W(5, 'certo') - 8, .35)
