"""anima.futebol — 27/11/2026 16h — RAIO-X · EP. 7 — Fluminense x Cruzeiro hoje 20h no Maracanã (37ª rodada).
Fontes (conferidas em 27/11/2026, ver fatos.txt): VAVEL (27/11), Diário Celeste (27/11), Central da Toca (27/11),
Gazeta Esportiva (26/11). Cruzeiro 3º com 66, Fluminense 4º com 63; empate garante o 3º ao Cruzeiro;
Gerson e Kaio Jorge voltam; Hulk pode começar no banco.
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  37ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Fluminense alcança o Cruzeiro hoje? Olha a prancheta.",
    "Vinte horas, Maracanã. O Cruzeiro é terceiro... com sessenta e seis.",
    "O Fluminense é quarto, com sessenta e três... e precisa vencer.",
    "Um empate já garante o terceiro lugar... para o Cruzeiro.",
    "Gerson e Kaio Jorge voltam. E Hulk pode começar no banco.",
    "Depois, falta só uma rodada. O Flu vence hoje?",
]
CAPTXT = [
    "O Fluminense alcança o Cruzeiro|hoje? Olha a prancheta.",
    "20h, Maracanã. O Cruzeiro|é 3º... com 66.",
    "O Fluminense é 4º, com 63...|e precisa vencer.",
    "Um empate já garante o 3º lugar...|para o Cruzeiro.",
    "Gerson e Kaio Jorge voltam. E Hulk|pode começar no banco.",
    "Depois, falta só uma rodada.|O Flu vence hoje?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "FLU VENCE?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 3
FLASH = [1]
CHECK = [(0, 'alcança', 4), (0, 'prancheta', 4), (1, 'Maracanã', 4), (1, 'terceiro', 4), (1, 'seis', 4),
         (2, 'quarto', 4), (2, 'três', 4), (2, 'vencer', 4), (3, 'empate', 4), (3, 'lugar', 4), (3, 'Cruzeiro', 4),
         (4, 'Gerson', 4), (4, 'Hulk', 4), (4, 'banco', 4), (5, 'rodada', 4), (5, 'vence', 4)]

FLUC, FLU_F = time_('FLUMINENSE')
CRUC, CRU_F = time_('CRUZEIRO')


def flu(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=FLUC, faixa=FLU_F, **kw)


def cru(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=CRUC, faixa=CRU_F, **kw)


CLOSE_F = 36
TORC = dict(roupa='#7a1f3d', pele='#e0b08a', cabelo='#3a2414')


def s0(f):
    """quadro 0 = capa: close do torcedor tricolor + série + pergunta; depois a prancheta."""
    c = prancheta().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='preocupado', s=.9, **TORC)
        num(c, 'RAIO-X', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 7', 621, 440, f, 0, 100, 2)
        num(c, 'O FLU ALCANÇA', 621, 1350, f, 0, 110, -2)
        num(c, 'O CRUZEIRO?', 621, 1530, f, 0, 110, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    pr = wt(0, 'prancheta') - 3
    for i, (x, y) in enumerate([(380, 1150), (862, 1150), (621, 1380), (380, 1600), (862, 1600)]):
        pino(c, x, y + 12 * math.sin(f * .2 + i), FLUC if i % 2 == 0 else CRUC, f, CLOSE_F + i * 3, '?', 80)
    if f < pr - 2:
        put_placa(c, 'FLUMINENSE', FLUC, 640, 820, f, CLOSE_F, 100, -3)
    else:
        put_placa(c, 'x CRUZEIRO', CRUC, 640, 820, f, pr, 100, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f)
    k = kick(f, pr if f >= pr else CLOSE_F, .7)
    return c, (640, 1320 + k * 10, z, k), 'day'


def s1(f):
    """telão do estádio: 20h no Maracanã, depois Cruzeiro 3º com 66."""
    c = telao('dusk').copy()
    te = wt(1, 'terceiro') - 3; se = wt(1, 'seis') - 6
    cru(c, 640, 2100, 920, f, 3, arms='cintura' if f < te else 'up', expr='neutral' if f < te else 'grin',
        look=-1 if f < te else (0 if f < se else 1), num_='10')
    if f < te - 2:
        telao_txt(c, [('MARACANÃ', 110), ('20H', 190)], f, 0, y=640)
    elif f < se - 2:
        telao_txt(c, [('CRUZEIRO', 100), ('3º', 200)], f, te, y=640)
    else:
        telao_txt(c, [('3º', 110), ('66 PTS', 190)], f, se, y=640)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, se if f >= se else (te if f >= te else 0), .6)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """a conta do Fluminense: 4º, 63, precisa vencer."""
    c = conta_bg().copy()
    qu = wt(2, 'quarto') - 3; tr = wt(2, 'três') - 6; ve = wt(2, 'vencer') - 4
    flu(c, 640, 2100, 920, f, 5, arms='cintura' if f < tr else 'punho', expr='nervous' if f < ve else 'stern',
        look=0 if f < tr else (1 if f < ve else -1), num_='7')
    if f < qu - 2:
        put_placa(c, 'FLUMINENSE', FLUC, 640, 1000, f, 0, 110, -2)
    elif f < tr - 2:
        num(c, '4º', 640, 1000, f, qu, 200, 3)
    elif f < ve - 2:
        numero_gigante(c, '63', 640, 1000, f, tr, 300, -3)
    else:
        num(c, 'PRECISA VENCER', 640, 1000, f, ve, 92, 2)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, ve if f >= ve else (tr if f >= tr else (qu if f >= qu else 0)), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s3(f):
    """vestiário do Cruzeiro: o empate garante o 3º lugar."""
    c = vestiario(CRUC, CRU_F).copy()
    em = wt(3, 'empate') - 3; lu = wt(3, 'lugar') - 5; cr = wt(3, 'Cruzeiro') - 3
    cru(c, 640, 2090, 900, f, 4, arms='hang' if f < lu else 'up', expr='neutral' if f < em else ('grin' if f >= lu else 'smug'),
        look=1 if f < lu else 0, num_='8')
    if f >= cr:
        cru(c, 300, 2060, 760, f, 7, arms='punho', expr='grin', look=1, num_='5', skin=1)
        cru(c, 980, 2060, 760, f, 8, arms='punho', expr='grin', look=-1, num_='9', flip=True, skin=4)
    if f < em - 2:
        pass
    elif f < lu - 2:
        num(c, 'EMPATE', 640, 1000, f, em, 140, -3)
    else:
        num(c, '3º LUGAR', 640, 1000, f, lu, 130, 3)
    z = (1.12 if f < cr else 1.0) * (1 + .0015 * f)
    k = kick(f, cr if f >= cr else (lu if f >= lu else (em if f >= em else 0)), .8)
    return c, (640, 1420 + k * 10, z, k), 'day'


def s4(f):
    """estádio de dia: Gerson e Kaio Jorge voltam; Hulk pode começar no banco."""
    c = estadio2('day').copy()
    ge = wt(4, 'Gerson') - 3; hu = wt(4, 'Hulk') - 3; ba = wt(4, 'banco') - 4
    if f < hu:
        cru(c, 400, 2040, 840, f, 6, arms='up', expr='grin', look=1, num_='8', run=(f * .25) % 1 if f < ge + 20 else -1)
        cru(c, 880, 2040, 840, f, 2, arms='up', expr='grin', look=-1, flip=True, num_='9', skin=1)
        if f >= ge:
            put_placa(c, 'GERSON E KAIO JORGE', CRUC, 640, 900, f, ge, 72, -3)
        z = lerp(1.15, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
        return c, (640 + 25 * math.sin(f * .05), 1400, z, kick(f, ge, .7) if f >= ge else 0), 'day'
    flu(c, 640, 2050, 880, f, 9, arms='cintura' if f < ba else 'cheek', expr='stern' if f < ba else 'nervous',
        look=-1 if f < ba else 1, num_='7', skin=3)
    if f < ba - 2:
        put_placa(c, 'HULK', FLUC, 640, 920, f, hu, 110, 3)
    else:
        num(c, 'NO BANCO?', 640, 940, f, ba, 120, -3)
    z = 1.1 * (1 + .0015 * (f - hu))
    k = kick(f, ba if f >= ba else hu, .8)
    return c, (640, 1420 + k * 8, z, k), 'day'


def s5(f):
    """estádio ao entardecer: falta uma rodada; close final na pergunta."""
    c = estadio2('golden').copy()
    ro = wt(5, 'rodada') - 3; ve = wt(5, 'vence') - 10
    flu(c, 400, 2030, 820, f, 6, arms='cintura', expr='stern', look=1, num_='10')
    cru(c, 900, 2030, 820, f, 4, arms='cintura', expr='stern', look=-1, flip=True, num_='10')
    if f >= ro and f < ve - 2:
        num(c, '1 RODADA', 640, 900, f, ro, 130, 3)
    if f >= ve:
        c = put_close(c, f, expr='curioso', look=0, s=.9, **TORC)
        num(c, 'VENCE?', 621, 1450, f, ve, 170, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - ve)), 0), 'golden'
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0012 * f)
    k = kick(f, ro, .7) if f >= ro else 0
    return c, (640, 1400 + k * 8, z, lerp(0, 2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'prancheta') - 3, 130, .7)
    s.apito(s.W(1, 'Maracanã') - 4)
    s.thunk(s.W(1, 'terceiro') - 3, 150, .8)
    s.thunk(s.W(1, 'seis') - 6, 160, .9)
    s.thunk(s.W(2, 'quarto') - 3, 150, .8)
    s.thunk(s.W(2, 'três') - 6, 170, 1.0)
    s.thunk(s.W(2, 'vencer') - 4, 140, .8)
    s.thunk(s.W(3, 'empate') - 3, 140, .8)
    s.ting(s.W(3, 'lugar') - 5, .3)
    s.thunk(s.W(3, 'Cruzeiro') - 3, 130, .7)
    s.thunk(s.W(4, 'Gerson') - 3, 140, .8)
    s.thunk(s.W(4, 'Hulk') - 3, 140, .8)
    s.thunk(s.W(4, 'banco') - 4, 150, .9)
    s.thunk(s.W(5, 'rodada') - 3, 140, .8)
    s.thunk(s.W(5, 'vence') - 10, 140, .8)
