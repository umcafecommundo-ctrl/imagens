"""anima.futebol — 26/11/2026 16h — RAIO-X · EP. 6 — São Paulo x Remo hoje 20h no Morumbis (37ª rodada).
Fontes (conferidas em 26/11/2026, ver fatos.txt): Itatiaia (26/11), Roma News (26/11), Metrópoles (26/11),
Gazeta Esportiva e Lance (1º turno). São Paulo 11º com 45, 5 jogos sem vencer, briga pela Sul-Americana;
Remo rebaixado com 32 e 3 suspensos; Wendell suspenso, Artur volta; 1º turno Remo 1x0.
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
    "O São Paulo volta a vencer hoje? Olha a prancheta.",
    "Vinte horas, Morumbis. O Tricolor é décimo primeiro... com quarenta e cinco.",
    "São cinco jogos sem vencer. E no turno, o Remo ganhou... um a zero.",
    "Wendell está suspenso. Mas Artur volta, com Lucas e Calleri.",
    "O Remo já caiu, tem trinta e dois... e três suspensos.",
    "Vale vaga na Sul-Americana. O São Paulo vence?",
]
CAPTXT = [
    "O São Paulo volta a vencer hoje?|Olha a prancheta.",
    "20h, Morumbis. O Tricolor|é 11º... com 45.",
    "São 5 jogos sem vencer. E no turno,|o Remo ganhou... 1 a 0.",
    "Wendell está suspenso. Mas Artur|volta, com Lucas e Calleri.",
    "O Remo já caiu, tem 32...|e 3 suspensos.",
    "Vale vaga na Sul-Americana.|O São Paulo vence?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "TRICOLOR VENCE?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 3
FLASH = [1]
CHECK = [(0, 'vencer', 4), (0, 'prancheta', 4), (1, 'Morumbis', 4), (1, 'primeiro', 4), (1, 'cinco', 4),
         (2, 'cinco', 4), (2, 'Remo', 4), (2, 'zero', 4), (3, 'suspenso', 4), (3, 'Artur', 4), (3, 'Calleri', 4),
         (4, 'caiu', 4), (4, 'dois', 4), (4, 'suspensos', 4), (5, 'Sul-Americana', 4), (5, 'vence', 4)]

SAO, SAO_F = time_('SÃO PAULO')
REM, REM_F = time_('REMO')


def sp(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=SAO, faixa=SAO_F, **kw)


def rem(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 4); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=REM, faixa=REM_F, **kw)


CLOSE_F = 36
TORC = dict(roupa='#f4f4f4', pele='#c98e64', cabelo='#1a120c')


def s0(f):
    """quadro 0 = capa: close do torcedor são-paulino + série + pergunta; depois a prancheta."""
    c = prancheta().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='preocupado', s=.9, **TORC)
        num(c, 'RAIO-X', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 6', 621, 440, f, 0, 100, 2)
        num(c, 'SÃO PAULO', 621, 1350, f, 0, 140, -2)
        num(c, 'VOLTA A VENCER?', 621, 1530, f, 0, 100, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    pr = wt(0, 'prancheta') - 3
    for i, (x, y) in enumerate([(380, 1150), (862, 1150), (621, 1380), (380, 1600), (862, 1600)]):
        pino(c, x, y + 12 * math.sin(f * .2 + i), SAO, f, CLOSE_F + i * 3, '?', 80)
    if f < pr - 2:
        put_placa(c, 'SÃO PAULO', SAO, 640, 820, f, CLOSE_F, 100, -3)
    else:
        put_placa(c, 'x REMO', REM, 640, 820, f, pr, 100, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f)
    k = kick(f, pr if f >= pr else CLOSE_F, .7)
    return c, (640, 1320 + k * 10, z, k), 'day'


def s1(f):
    """telão do estádio: 20h no Morumbis, depois 11º com 45."""
    c = telao('dusk').copy()
    pm = wt(1, 'primeiro') - 3; qc = wt(1, 'cinco') - 5
    sp(c, 640, 2100, 920, f, 3, arms='cintura' if f < pm else 'cheek', expr='neutral' if f < pm else 'nervous',
       look=-1 if f < pm else (0 if f < qc else 1), num_='7')
    if f < pm - 2:
        telao_txt(c, [('MORUMBIS', 110), ('20H', 190)], f, 0, y=640)
    elif f < qc - 2:
        telao_txt(c, [('11º', 200)], f, pm, y=680)
    else:
        telao_txt(c, [('11º', 110), ('45 PTS', 190)], f, qc, y=640)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, qc if f >= qc else (pm if f >= pm else 0), .6)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """estádio de dia: 5 jogos sem vencer; no 1º turno, Remo 1x0."""
    c = estadio2('day').copy()
    ci = wt(2, 'cinco') - 3; re = wt(2, 'Remo') - 3; ze = wt(2, 'zero') - 6
    if f < re:
        sp(c, 640, 2040, 860, f, 5, arms='cheek' if f >= ci else 'hang', expr='pained' if f >= ci else 'nervous',
           look=0, num_='10')
        if f >= ci:
            num(c, '5 SEM VENCER', 640, 920, f, ci, 120, 3)
        z = lerp(1.18, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
        return c, (640 + 25 * math.sin(f * .05), 1400, z, kick(f, ci, .7) if f >= ci else 0), 'day'
    sp(c, 380, 2030, 800, f, 6, arms='hang', expr='pained', look=1, num_='9')
    rem(c, 880, 2030, 840, f, 2, arms='up', expr='grin', look=-1, flip=True, num_='8')
    if f < ze - 2:
        put_placa(c, 'NO 1º TURNO', REM, 640, 900, f, re, 90, -3)
    else:
        num(c, 'REMO 1x0', 640, 940, f, ze, 150, -3)
    z = 1.08 * (1 + .0015 * (f - re))
    k = kick(f, ze if f >= ze else re, .8)
    return c, (640, 1420 + k * 8, z, k), 'day'


def s3(f):
    """vestiário: Wendell suspenso; Artur volta, com Lucas e Calleri."""
    c = vestiario(SAO, SAO_F).copy()
    su = wt(3, 'suspenso') - 3; ar = wt(3, 'Artur') - 3; lu = wt(3, 'Lucas') - 3
    if f < ar:
        sp(c, 640, 2090, 880, f, 5, arms='cintura', expr='stern' if f < su else 'nervous', look=1 if f < su else -1, num_='6')
        if f < su - 2:
            put_placa(c, 'WENDELL', SAO, 640, 1020, f, 2, 100, -2)
        else:
            num(c, 'SUSPENSO', 640, 1020, f, su, 130, 3)
        z = lerp(1.1, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
        return c, (640 + 15 * math.sin(f * .05), 1400, z, kick(f, su, .6) if f >= su else 0), 'day'
    sp(c, 640, 2090, 900, f, 4, arms='up', expr='grin', look=0, num_='11', skin=3)
    if f >= lu:
        sp(c, 300, 2060, 760, f, 7, arms='punho', expr='grin', look=1, num_='7', skin=1)
        sp(c, 980, 2060, 760, f, 8, arms='punho', expr='grin', look=-1, num_='9', flip=True, skin=1, hair='#6b4a2a')
    if f < lu - 2:
        num(c, 'ARTUR VOLTA', 640, 1000, f, ar, 120, -3)
    else:
        put_placa(c, 'LUCAS E CALLERI', SAO, 640, 1000, f, lu, 85, 3)
    z = (1.12 if f < lu else 1.0) * (1 + .0015 * (f - ar))
    k = kick(f, lu if f >= lu else ar, .8)
    return c, (640, 1420 + k * 10, z, k), 'day'


def s4(f):
    """a conta do Remo: rebaixado, 32 pontos, 3 suspensos."""
    c = conta_bg().copy()
    ca = wt(4, 'caiu') - 3; do = wt(4, 'dois') - 6; su = wt(4, 'suspensos') - 4
    rem(c, 640, 2100, 920, f, 2, arms='hang' if f < ca else 'cheek', expr='nervous' if f < ca else 'pained',
        look=0 if f < do else 1, num_='10')
    if f < ca - 2:
        put_placa(c, 'REMO', REM, 640, 1000, f, 0, 110, -2)
    elif f < do - 2:
        num(c, 'REBAIXADO', 640, 1000, f, ca, 125, 3)
    elif f < su - 2:
        numero_gigante(c, '32', 640, 1000, f, do, 300, -3)
    else:
        num(c, '3 SUSPENSOS', 640, 1000, f, su, 120, 2)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, su if f >= su else (do if f >= do else (ca if f >= ca else 0)), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """estádio ao entardecer: vale Sul-Americana; close final na pergunta."""
    c = estadio2('golden').copy()
    su = wt(5, 'Sul-Americana') - 3; ve = wt(5, 'vence') - 10
    sp(c, 400, 2030, 820, f, 6, arms='cintura', expr='stern', look=1, num_='10')
    rem(c, 900, 2030, 820, f, 4, arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    if f >= su:
        num(c, 'SUL-AMERICANA', 640, 900, f, su, 110, 3)
    if f >= ve:
        c = put_close(c, f, expr='curioso', look=0, s=.9, **TORC)
        num(c, 'VENCE?', 621, 1450, f, ve, 170, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - ve)), 0), 'golden'
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0012 * f)
    k = kick(f, su, .7) if f >= su else 0
    return c, (640, 1400 + k * 8, z, lerp(0, 2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'prancheta') - 3, 130, .7)
    s.thunk(s.W(1, 'primeiro') - 3, 150, .8)
    s.thunk(s.W(1, 'cinco') - 5, 160, .9)
    s.thunk(s.W(2, 'cinco') - 3, 150, .8)
    s.apito(s.W(2, 'Remo') - 4, longo=True)
    s.thunk(s.W(2, 'zero') - 6, 170, 1.0)
    s.thunk(s.W(3, 'suspenso') - 3, 140, .8)
    s.ting(s.W(3, 'Artur') - 3, .3)
    s.thunk(s.W(3, 'Lucas') - 3, 130, .7)
    s.thunk(s.W(4, 'caiu') - 3, 140, .8)
    s.thunk(s.W(4, 'dois') - 6, 170, 1.0)
    s.thunk(s.W(4, 'suspensos') - 4, 150, .8)
    s.thunk(s.W(5, 'Sul-Americana') - 3, 140, .8)
    s.thunk(s.W(5, 'vence') - 10, 140, .8)
