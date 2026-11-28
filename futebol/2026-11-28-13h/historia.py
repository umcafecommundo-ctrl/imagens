"""anima.futebol — 28/11/2026 13h — RAIO-X · EP. 8 — Final da Libertadores hoje 17h no Centenário: Palmeiras x Estudiantes.
Fontes (conferidas em 28/11/2026, ver fatos.txt): Gazeta Esportiva (27/11 20h), Portal do Palestra (27/11 16h15),
CNN Brasil (28/11 05h), Revista Fórum (28/11 08h40). Palmeiras busca o 4º (1999, 2020, 2021), Estudiantes o 5º e venceu
o Palmeiras na final de 1968; três zagueiros (Murilo, Gómez, Barboza), ataque Arias, Vitor Roque e Flaco López; Paulinho
fora do time provável, Jefté suspenso; Estudiantes sem Baltasar Rodríguez; empate = prorrogação e pênaltis.
Sem escudos/logos/taça real: times por plaquinhas e cores, taça genérica."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'LIBERTADORES  ·  FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Palmeiras é tetra hoje? Olha a prancheta.",
    "Cinco da tarde, no Centenário. O Palmeiras busca o quarto título.",
    "Abel vai de três zagueiros... e Arias, Vitor Roque e Flaco na frente.",
    "Paulinho não deve começar. E Jefté está suspenso.",
    "O Estudiantes busca o quinto... e bateu o Palmeiras na final de sessenta e oito.",
    "Empatou? Prorrogação... e pênaltis. O Verdão é tetra?",
]
CAPTXT = [
    "O Palmeiras é tetra hoje?|Olha a prancheta.",
    "17h, no Centenário. O Palmeiras|busca o 4º título.",
    "Abel vai de 3 zagueiros... e Arias,|Vitor Roque e Flaco na frente.",
    "Paulinho não deve começar.|E Jefté está suspenso.",
    "O Estudiantes busca o 5º... e bateu|o Palmeiras na final de 68.",
    "Empatou? Prorrogação...|e pênaltis. O Verdão é tetra?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "É TETRA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [1]
CHECK = [(0, 'tetra', 4), (0, 'prancheta', 4), (1, 'Cinco', 4), (1, 'Centenario', 4), (1, 'quarto', 4), (1, 'titulo', 4),
         (2, 'zagueiros', 4), (2, 'Arias', 4), (2, 'Flaco', 4), (3, 'Paulinho', 4), (3, 'Jefte', 4), (3, 'suspenso', 4),
         (4, 'quinto', 4), (4, 'bateu', 4), (4, 'oito', 4), (5, 'Empatou', 4), (5, 'Prorrogacao', 4), (5, 'penaltis', 4),
         (5, 'tetra', 4)]

PAL, PAL_F = time_('PALMEIRAS')
EST, EST_F = time_('ESTUDIANTES')
VERDE = '#1b6b3a'
TORC = dict(roupa=VERDE, pele='#e0ac85', cabelo='#2a1a10')


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def est(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 0); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2414')
    put_atleta(c, x, y, h, f, seed, cores=EST, faixa=EST_F, **kw)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor alviverde + série + pergunta; depois a prancheta com as duas placas."""
    c = prancheta().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, look=0, **TORC)
        num(c, 'RAIO-X', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 8', 621, 440, f, 0, 100, 2)
        num(c, 'PALMEIRAS', 621, 1350, f, 0, 150, -2)
        num(c, 'É TETRA?', 621, 1530, f, 0, 170, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    pr = wt(0, 'prancheta') - 3
    for i, (x, y) in enumerate([(380, 1150), (862, 1150), (621, 1380), (380, 1600), (862, 1600)]):
        pino(c, x, y + 12 * math.sin(f * .2 + i), PAL if i % 2 == 0 else EST, f, CLOSE_F + i * 3, '?', 80)
    if f < pr - 2:
        put_placa(c, 'PALMEIRAS', PAL, 640, 820, f, CLOSE_F, 100, -3)
    else:
        put_placa(c, 'x ESTUDIANTES', EST, 640, 820, f, pr, 96, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f)
    k = kick(f, pr if f >= pr else CLOSE_F, .7)
    return c, (640, 1320 + k * 10, z, k), 'day'


def s1(f):
    """telão do estádio: 17h no Centenário, depois 4º título com a taça genérica."""
    c = telao('dusk').copy()
    qu = wt(1, 'quarto') - 3
    pal(c, 640, 2100, 920, f, 3, arms='cintura' if f < qu else 'up', expr='neutral' if f < qu else 'grin',
        look=-1 if f < qu else 0, num_='10')
    if f < qu - 2:
        telao_txt(c, [('CENTENÁRIO', 104), ('17H', 190)], f, 0, y=640)
    else:
        telao_txt(c, [('4º TÍTULO', 124)], f, qu, y=700)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, qu, 10))
    k = kick(f, qu if f >= qu else 0, .6)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """prancheta: três zagueiros e o trio de ataque."""
    c = prancheta().copy()
    zg = wt(2, 'zagueiros') - 4; ar = wt(2, 'Arias') - 3
    for i, (x, r) in enumerate([(360, '1'), (621, '2'), (882, '3')]):
        pino(c, x, 1700 + 8 * math.sin(f * .2 + i), PAL, f, zg + i * 3, r, 90)
    for i, (x, r) in enumerate([(360, 'A'), (621, 'V'), (882, 'F')]):
        pino(c, x, 1000 + 8 * math.sin(f * .2 + i), PAL, f, ar + i * 6, r, 90)
    if f >= ar + 14:
        seta(c, (621, 1110), (621, 700), f, ar + 14, 10)
    if f < zg - 2:
        put_placa(c, 'ABEL', PAL, 640, 1300, f, 0, 110, -3)
    elif f < ar - 2:
        num(c, '3 ZAGUEIROS', 640, 1330, f, zg, 120, 3)
    else:
        put_placa(c, 'ARIAS · ROQUE · FLACO', PAL, 640, 1330, f, ar, 72, -2)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .09 * pulse(f, zg, 10))
    k = kick(f, ar if f >= ar else (zg if f >= zg else 0), .7)
    return c, (640 + 20 * math.sin(f * .05), 1330 + k * 8, z, k), 'day'


def s3(f):
    """vestiário do Palmeiras: Paulinho fora do time, Jefté suspenso."""
    c = vestiario(PAL, PAL_F).copy()
    pa = wt(3, 'Paulinho') - 3; je = wt(3, 'Jefte') - 3; su = wt(3, 'suspenso') - 4
    if f < je:
        pal(c, 640, 2090, 900, f, 4, arms='cheek', expr='nervous', look=-1 if f < pa + 20 else 1, num_='10', skin=3,
            hair='#151010')
        if f >= pa:
            put_placa(c, 'PAULINHO', PAL, 640, 960, f, pa, 110, -3)
        z = 1.12 * (1 + .0015 * f)
        return c, (640, 1420, z, kick(f, pa, .7) if f >= pa else 0), 'day'
    pal(c, 640, 2070, 880, f, 7, arms='hang', expr='stern' if f < su else 'pained', look=1 if f < su else 0, num_='6')
    if f < su - 2:
        put_placa(c, 'JEFTÉ', PAL, 640, 960, f, je, 110, 3)
    else:
        num(c, 'SUSPENSO', 640, 960, f, su, 140, -3)
    z = 1.02 * (1 + .0015 * (f - je))
    k = kick(f, su if f >= su else je, .8)
    return c, (640, 1440 + k * 8, z, k), 'day'


def s4(f):
    """estádio ao entardecer: o Estudiantes busca o 5º; taça genérica; final de 68."""
    c = estadio2('golden').copy()
    qi = wt(4, 'quinto') - 3; ba = wt(4, 'bateu') - 3; oi = wt(4, 'oito') - 6
    est(c, 400, 2040, 860, f, 5, arms='up' if f >= qi else 'cintura', expr='grin' if f >= qi else 'neutral', look=1,
        num_='9', run=(f * .25) % 1 if f < qi else -1)
    est(c, 880, 2040, 860, f, 8, arms='punho' if f >= ba else 'cintura', expr='smug' if f >= ba else 'neutral',
        look=-1, flip=True, num_='5', skin=2, hair='#151010')
    if f < ba - 2:
        put_trofeu(c, 640, 1150, 520, f, qi)
        if f >= qi:
            num(c, '5º', 640, 760, f, qi, 170, -3)
    elif f < oi - 2:
        put_placa(c, 'FINAL', EST, 640, 1000, f, ba, 120, 3)
    else:
        numero_gigante(c, '1968', 640, 1000, f, oi, 260, -3)
    z = lerp(1.18, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, oi, 10))
    k = kick(f, oi if f >= oi else (ba if f >= ba else (qi if f >= qi else 0)), .7)
    return c, (640 + 25 * math.sin(f * .05), 1400 + k * 8, z, k), 'golden'


def s5(f):
    """conta: empatou -> prorrogação -> pênaltis; close final na pergunta."""
    c = conta_bg().copy()
    em = wt(5, 'Empatou') - 3; pr = wt(5, 'Prorrogacao') - 3; pe = wt(5, 'penaltis') - 4; te = wt(5, 'tetra') - 12
    if f >= te:
        c = estadio2('dusk').copy()
        c = put_close(c, f, expr='curioso', look=0, s=.9, **TORC)
        num(c, 'É TETRA?', 621, 1450, f, te, 170, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - te)), 0), 'dusk'
    pal(c, 420, 2080, 860, f, 6, arms='cintura' if f < pe else 'cheek', expr='nervous', look=1, num_='10')
    est(c, 880, 2080, 860, f, 4, arms='cintura', expr='stern', look=-1, flip=True, num_='10')
    if f < pr - 2:
        num(c, 'EMPATE?', 640, 1000, f, em, 170, -3)
    elif f < pe - 2:
        num(c, '+30 MIN', 640, 1000, f, pr, 170, 3)
    else:
        num(c, 'PÊNALTIS', 640, 1000, f, pe, 150, -3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .09 * pulse(f, pe, 10))
    k = kick(f, pe if f >= pe else (pr if f >= pr else em), .7)
    return c, (640 + 20 * math.sin(f * .05), 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'prancheta') - 3, 130, .7)
    s.apito(s.W(1, 'Centenario') - 4)
    s.thunk(s.W(1, 'quarto') - 3, 160, .9)
    s.thunk(s.W(2, 'zagueiros') - 4, 150, .8)
    s.thunk(s.W(2, 'Arias') - 3, 140, .8)
    s.thunk(s.W(3, 'Paulinho') - 3, 140, .8)
    s.thunk(s.W(3, 'Jefte') - 3, 140, .8)
    s.thunk(s.W(3, 'suspenso') - 4, 150, .9)
    s.thunk(s.W(4, 'quinto') - 3, 150, .8)
    s.thunk(s.W(4, 'bateu') - 3, 140, .8)
    s.thunk(s.W(4, 'oito') - 6, 170, 1.0)
    s.thunk(s.W(5, 'Empatou') - 3, 140, .8)
    s.thunk(s.W(5, 'Prorrogacao') - 3, 150, .8)
    s.ting(s.W(5, 'penaltis') - 4, .3)
    s.thunk(s.W(5, 'tetra') - 12, 140, .8)
