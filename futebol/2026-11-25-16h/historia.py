"""anima.futebol — 25/11/2026 16h — RAIO-X · EP. 5 — Atlético-MG x Corinthians hoje 20h na Arena MRV (36ª rodada).
Fontes (conferidas em 25/11/2026, ver fatos.txt): Gazeta Esportiva (24/11), Terra (24/11), O Folha de Minas (25/11),
Central do Timão (24/11). Corinthians 17º com 40 no Z4, sem Yuri Alberto e Carrillo (suspensos), Garro volta;
Galo 7º com 51 e 8 jogos sem vencer; vitória leva o Timão a 43 e fora do Z4; domingo Corinthians x Grêmio.
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  36ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Corinthians sai do zê quatro hoje? Olha a prancheta.",
    "Hoje, vinte horas, Arena MRV. O Timão é décimo sétimo... com quarenta.",
    "Sem Yuri Alberto e Carrillo, suspensos. Mas Garro volta.",
    "O Galo está há oito jogos sem vencer... e tem cinquenta e um.",
    "Se o Timão vencer, vai a... quarenta e três, e sai do zê quatro.",
    "Domingo ainda tem Corinthians e Grêmio. O Timão escapa?",
]
CAPTXT = [
    "O Corinthians sai do Z4 hoje?|Olha a prancheta.",
    "Hoje, 20h, Arena MRV. O Timão|é 17º... com 40.",
    "Sem Yuri Alberto e Carrillo,|suspensos. Mas Garro volta.",
    "O Galo está há 8 jogos sem vencer...|e tem 51.",
    "Se o Timão vencer, vai a... 43,|e sai do Z4.",
    "Domingo ainda tem Corinthians|e Grêmio. O Timão escapa?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "TIMÃO ESCAPA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [1]
CHECK = [(0, 'Corinthians', 4), (0, 'prancheta', 4), (1, 'vinte', 4), (1, 'setimo', 4), (1, 'quarenta', 4),
         (2, 'Yuri', 4), (2, 'suspensos', 4), (2, 'Garro', 4), (3, 'oito', 4), (3, 'um', 4),
         (4, 'vencer', 4), (4, 'tres', 4), (5, 'Gremio', 4), (5, 'escapa', 4)]

COR, COR_F = time_('CORINTHIANS')
CAM, CAM_F = time_('ATLÉTICO-MG')
GRE, GRE_F = time_('GRÊMIO')


def cor(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=COR, faixa=COR_F, **kw)


CLOSE_F = 36
TORC = dict(roupa='#f2f2f2', pele='#c98e64', cabelo='#1a120c')


def s0(f):
    """quadro 0 = capa: close do torcedor corinthiano + série + pergunta; depois a prancheta."""
    c = prancheta().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, **TORC)
        num(c, 'RAIO-X', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 5', 621, 440, f, 0, 100, 2)
        num(c, 'CORINTHIANS', 621, 1350, f, 0, 130, -2)
        num(c, 'SAI DO Z4?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    pr = wt(0, 'prancheta') - 3
    for i, (x, y) in enumerate([(380, 1150), (862, 1150), (621, 1380), (380, 1600), (862, 1600)]):
        pino(c, x, y + 12 * math.sin(f * .2 + i), COR, f, CLOSE_F + i * 3, '?', 80)
    if f < pr - 2:
        put_placa(c, 'CORINTHIANS', COR, 640, 820, f, CLOSE_F, 100, -3)
    else:
        num(c, 'Z4?', 640, 820, f, pr, 150, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f)
    k = kick(f, pr if f >= pr else CLOSE_F, .7)
    return c, (640, 1320 + k * 10, z, k), 'day'


def s1(f):
    """telão do estádio: 20h na Arena MRV, depois 17º com 40."""
    c = telao('dusk').copy()
    st = wt(1, 'setimo') - 3; qu = wt(1, 'quarenta') - 4
    cor(c, 640, 2100, 920, f, 3, arms='hang' if f < st else 'cheek', expr='nervous' if f < qu else 'pained',
        look=-1 if f < st else 0, num_='7')
    if f < st - 2:
        telao_txt(c, [('ARENA MRV', 100), ('20H', 190)], f, 0, y=640)
    elif f < qu - 2:
        telao_txt(c, [('17º', 200)], f, st, y=680)
    else:
        telao_txt(c, [('17º', 110), ('40 PTS', 190)], f, qu, y=640)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, qu if f >= qu else (st if f >= st else 0), .6)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """vestiário: os dois suspensos, depois a volta do Garro."""
    c = vestiario(COR, COR_F).copy()
    su = wt(2, 'suspensos') - 3; ga = wt(2, 'Garro') - 3
    if f < ga:
        cor(c, 400, 2090, 860, f, 5, arms='cintura', expr='stern' if f < su else 'nervous', look=1, num_='9')
        cor(c, 880, 2090, 860, f, 6, arms='hang', expr='nervous', look=-1, num_='11', flip=True, skin=3, hair='#151010')
        if f < su - 2:
            put_placa(c, 'YURI E CARRILLO', COR, 640, 1020, f, 2, 80, -2)
        else:
            num(c, 'SUSPENSOS', 640, 1020, f, su, 120, 3)
        z = lerp(1.1, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
        return c, (640 + 15 * math.sin(f * .05), 1400, z, kick(f, su, .6) if f >= su else 0), 'day'
    cor(c, 640, 2090, 880, f, 4, arms='up', expr='grin', look=0, num_='10')
    num(c, 'GARRO VOLTA', 640, 1000, f, ga, 120, -3)
    z = 1.12 * (1 + .0015 * (f - ga))
    k = kick(f, ga, .8)
    return c, (640, 1420 + k * 10, z, k), 'day'


def s3(f):
    """estádio de dia: o Galo, 8 jogos sem vencer, 51 pontos."""
    c = estadio2('day').copy()
    oi = wt(3, 'oito') - 3; um = wt(3, 'um') - 5
    put_atleta(c, 640, 2040, 840, f, 2, cores=CAM, faixa=CAM_F, skin=4, hs='curto', hair='#151010',
               arms='cintura' if f < oi else ('cheek' if f < um else 'point'), expr='stern' if f < oi else ('pained' if f < um else 'neutral'),
               look=0 if f < oi else 1, num_='10')
    if f < oi - 2:
        put_placa(c, 'ATLÉTICO-MG', CAM, 640, 900, f, 0, 100, -3)
    elif f < um - 2:
        num(c, '8 SEM VENCER', 640, 900, f, oi, 115, 3)
    else:
        numero_gigante(c, '51', 640, 960, f, um, 300, -3)
    z = lerp(1.18, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, um if f >= um else (oi if f >= oi else 0), .7)
    return c, (640 + 25 * math.sin(f * .05), 1400 + k * 8, z, k), 'day'


def s4(f):
    """a conta: vitória = 43 e fora do Z4."""
    c = conta_bg().copy()
    ve = wt(4, 'vencer') - 3; tr = wt(4, 'tres') - 6; zq = wt(4, 'quatro') - 3
    cor(c, 640, 2100, 920, f, 5, arms='punho' if f < tr else 'up', expr='neutral' if f < tr else 'grin', look=0, num_='7')
    if f < tr - 2:
        num(c, 'SE VENCER...', 640, 1000, f, ve, 115, -2)
    elif f < zq - 2:
        numero_gigante(c, '43', 640, 1000, f, tr, 300, 3)
    else:
        num(c, 'FORA DO Z4', 640, 1000, f, zq, 125, -3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, zq if f >= zq else (tr if f >= tr else ve), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """estádio ao entardecer: domingo Corinthians x Grêmio; close final na pergunta."""
    c = estadio2('golden').copy()
    gr = wt(5, 'Gremio') - 3; es = wt(5, 'escapa') - 10
    cor(c, 400, 2030, 820, f, 6, arms='cintura', expr='stern', look=1, num_='10')
    put_atleta(c, 900, 2030, 820, f, 4, cores=GRE, faixa=GRE_F, skin=1, hs='curto', hair='#2a1a10',
               arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    if f < gr - 2:
        paste_c(c, calendario('29', 'NOV'), 640, 1000, .95 * back(ramp(f, 0, 8)))
    else:
        put_placa(c, 'x GRÊMIO', GRE, 640, 900, f, gr, 100, 3)
    if f >= es:
        c = put_close(c, f, expr='preocupado', look=0, s=.9, **TORC)
        num(c, 'ESCAPA?', 621, 1450, f, es, 170, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - es)), 0), 'golden'
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0012 * f)
    k = kick(f, gr, .7) if f >= gr else 0
    return c, (640, 1400 + k * 8, z, lerp(0, 2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'prancheta') - 3, 130, .7)
    s.thunk(s.W(1, 'setimo') - 3, 150, .8)
    s.thunk(s.W(1, 'quarenta') - 4, 160, .9)
    s.thunk(s.W(2, 'suspensos') - 3, 140, .8)
    s.ting(s.W(2, 'Garro') - 3, .3)
    s.thunk(s.W(3, 'oito') - 3, 150, .8)
    s.thunk(s.W(3, 'um') - 5, 160, .9)
    s.thunk(s.W(4, 'tres') - 6, 170, 1.0)
    s.ting(s.W(4, 'quatro') - 3, .35)
    s.apito(s.W(5, 'Gremio') - 4)
    s.thunk(s.W(5, 'escapa') - 10, 140, .8)
