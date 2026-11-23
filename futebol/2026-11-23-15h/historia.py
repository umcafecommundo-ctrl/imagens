"""anima.futebol — 23/11/2026 15h — RAIO-X · EP. 3 — Internacional x Vitória hoje 19h30 no Beira-Rio (36ª rodada).
Fontes (conferidas em 23/11/2026, ver fatos.txt): ESPN (20/11), Gazeta Esportiva (22/11), Olhar Digital (23/11), A Tarde (22/11),
Portal Salvador FM (23/11), Folha do Estado (23/11). Inter 17º 38 x Vitória 14º 41; Alan Patrick e Mateus Silva suspensos;
Inter provável com 3 zagueiros (Mercado e Juninho em todas); ataque do Vitória Erick, Tarzia e Renê. Escalações PROVÁVEIS.
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  36ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Inter sai do Z4 hoje? Olha a prancheta.",
    "No Beira-Rio, o Inter tem trinta e oito... e o Vitória, quarenta e um.",
    "Sem Alan Patrick, suspenso, o Inter deve ir com três zagueiros.",
    "O Vitória perde Mateus Silva, suspenso, mas tem Erick, Tarzia e Renê.",
    "Se vencer, o Inter chega a quarenta e um... e passa o Corinthians.",
    "Se perder, o Vitória abre seis pontos. O Inter escapa?",
]
CAPTXT = [
    "O Inter sai do Z4 hoje?|Olha a prancheta.",
    "No Beira-Rio, o Inter tem 38...|e o Vitória, 41.",
    "Sem Alan Patrick, suspenso,|o Inter deve ir com 3 zagueiros.",
    "O Vitória perde Mateus Silva, suspenso,|mas tem Erick, Tarzia e Renê.",
    "Se vencer, o Inter chega a 41...|e passa o Corinthians.",
    "Se perder, o Vitória abre 6 pontos.|O Inter escapa?",
]
FALA_TIKTOK = "O Inter vence hoje? Comenta sim ou não."
CTA_TEXTO = "INTER VENCE?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [4]
CHECK = [(0, 'Inter', 4), (0, 'prancheta', 4), (1, 'Beira-Rio', 4), (1, 'oito', 4), (1, 'Vitoria', 4), (1, 'um', 4),
         (2, 'Patrick', 4), (2, 'tres', 4), (2, 'zagueiros', 4), (3, 'Mateus', 4), (3, 'Erick', 4), (3, 'Tarzia', 4),
         (3, 'Rene', 4), (4, 'vencer', 4), (4, 'quarenta', 4), (4, 'Corinthians', 4), (5, 'seis', 4), (5, 'escapa', 4)]

INT, INT_F = time_('INTERNACIONAL')
VIT_, VIT_F = time_('VITÓRIA')
COR_, COR_F = time_('CORINTHIANS')


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def vit(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=VIT_, faixa=VIT_F, **kw)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor colorado + série + pergunta; depois os dois times frente a frente."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='preocupado', s=.9, roupa='#c8102e', pele='#e0ac85', cabelo='#3a2a1e')
        num(c, 'RAIO-X', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 3', 621, 440, f, 0, 100, 2)
        num(c, 'O INTER SAI', 621, 1350, f, 0, 140, -2)
        num(c, 'DO Z4?', 621, 1530, f, 0, 170, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    pr = wt(0, 'prancheta') - 3
    inter(c, 330, 2070, 780, f, 6, arms='cintura', expr='nervous', look=1, num_='10')
    vit(c, 950, 2070, 780, f, 3, arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    if f < pr - 2:
        put_placa(c, 'INTER', INT, 640, 860, f, CLOSE_F, 100, -3)
    else:
        put_placa(c, 'x VITÓRIA', VIT_, 640, 860, f, pr, 96, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """telão no fim de tarde: Beira-Rio, 38 x 41."""
    c = telao('dusk').copy()
    be = wt(1, 'Beira-Rio') - 3; oi = wt(1, 'oito') - 3; um = wt(1, 'um') - 3
    inter(c, 330, 2080, 700, f, 5, arms='hang' if f < oi else 'cheek', expr='nervous', look=1, num_='5')
    vit(c, 950, 2080, 700, f, 8, arms='cintura', expr='stern' if f < um else 'grin', look=-1, flip=True, num_='8')
    if f < oi - 2:
        telao_txt(c, [('BEIRA-RIO', 150)], f, be, y=700)
    elif f < um - 2:
        telao_txt(c, [('INTER', 110), ('38', 200)], f, oi, y=640)
    else:
        telao_txt(c, [('VITÓRIA', 110), ('41', 200)], f, um, y=640)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, um if f >= um else (oi if f >= oi else be), .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


ZAG = [(380, 1440), (621, 1480), (862, 1440)]


def s2(f):
    """prancheta: Inter sem Alan Patrick, linha de três zagueiros (M = Mercado, J = Juninho)."""
    c = prancheta().copy()
    pa = wt(2, 'Patrick') - 3; tr = wt(2, 'tres') - 3; za = wt(2, 'zagueiros') - 3
    for i, x in enumerate((300, 520, 722, 942)):
        pino(c, x, 1150 + 12 * math.sin(f * .2 + i), INT, f, 4 + i * 2, '', 58)
    for i, (x, y) in enumerate(ZAG):
        pino(c, x, y + (0 if f >= za else 60) + 12 * math.sin(f * .2 + i * 1.7), INT, f, tr + i * 3, ['M', '', 'J'][i], 90)
    if f >= za:
        seta(c, (290, 1580), (952, 1580), f, za + 2, 14, (255, 216, 74), 12)
    if f < tr - 2:
        if f >= pa - 6: num(c, 'SEM ALAN PATRICK', 640, 820, f, pa - 6, 90, -3)
        else: put_placa(c, 'INTER', INT, 640, 820, f, 0, 96)
    else:
        num(c, '3 ZAGUEIROS', 640, 820, f, tr, 112, 3)
    z = lerp(1.06, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0004 * f)
    k = kick(f, tr, .6)
    return c, (640 + 12 * math.sin(f * .06), 1320 + k * 8 + 20 * math.sin(f * .045), z, lerp(0, -1, smooth(ramp(f, 0, 60))) + .8 * math.sin(f * .05)), 'day'


def s3(f):
    """prancheta: Vitória sem Mateus Silva; trio Erick, Tarzia, Renê (E, T, R)."""
    c = prancheta().copy()
    ma = wt(3, 'Mateus') - 3; er = wt(3, 'Erick') - 3; ta = wt(3, 'Tarzia') - 3; re = wt(3, 'Rene') - 3
    for i, x in enumerate((360, 621, 882)):
        pino(c, x, 1020 + 12 * math.sin(f * .2 + i), VIT_, f, 2 + i * 2, '', 58)
    alvo = [(380, 1440, er, 'E'), (621, 1500, ta, 'T'), (862, 1440, re, 'R')]
    for (x, y, t0, r) in alvo:
        if f >= t0: seta(c, (x, 1080), (x, y - 100), f, t0, 10, (255, 255, 255), 10)
        pino(c, x, y + 12 * math.sin(f * .2 + x), VIT_, f, t0, r, 90)
    if f < er - 2:
        if f >= ma: num(c, 'SEM MATEUS SILVA', 640, 780, f, ma, 90, -3)
        else: put_placa(c, 'VITÓRIA', VIT_, 640, 780, f, 0, 96)
    else:
        num(c, 'TRIO NA FRENTE', 640, 780, f, er, 96, 3)
    z = lerp(1.06, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0004 * f)
    k = kick(f, re, .6)
    return c, (640 - 12 * math.sin(f * .06), 1300 + k * 8 + 20 * math.sin(f * .045), z, lerp(0, 1, smooth(ramp(f, 0, 60))) + .8 * math.sin(f * .05)), 'day'


def s4(f):
    """a conta: 38 + 3 = 41 e passa o Corinthians (40)."""
    c = conta_bg().copy()
    ve = wt(4, 'vencer') - 3; qa = wt(4, 'quarenta') - 3; co = wt(4, 'Corinthians') - 3
    if f < qa - 2:
        numero_gigante(c, '38 + 3', 640, 1000, f, ve, 230, -3)
    elif f < co - 2:
        numero_gigante(c, '41', 640, 1000, f, qa, 300, 3)
    else:
        put_placa(c, 'CORINTHIANS 40', COR_, 640, 1000, f, co, 80, -2)
    if f >= co:
        put_atleta(c, 640, 2090, 760, f, 7, cores=COR_, faixa=COR_F, skin=2, hs='curto', hair='#151010',
                   arms='cheek', expr='nervous', look=0, num_='9')
    else:
        inter(c, 640, 2090, 760, f, 6, arms='up' if f >= qa else 'punho', expr='grin' if f >= qa else 'stern', look=0, num_='10')
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, co if f >= co else (qa if f >= qa else ve), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """estádio à noite: +6 do Vitória e a pergunta."""
    c = estadio2('dusk').copy()
    se = wt(5, 'seis') - 3; es = wt(5, 'escapa') - 6
    put_gol2(c)
    vit(c, 900, 2040, 780, f, 8, arms='up' if f >= se else 'cintura', expr='grin' if f >= se else 'stern', look=-1, flip=True, num_='11')
    inter(c, 400, 2010, 860, f, 5, arms='hang' if f < se else 'cheek', expr='nervous' if f < se else 'pained', look=1, num_='10')
    if f < es - 2:
        if f >= se: numero_gigante(c, '+6', 640, 900, f, se, 260, -3)
        else: put_placa(c, 'SE PERDER...', INT, 640, 880, f, 0, 90)
    else:
        num(c, 'ESCAPA?', 640, 880, f, es, 190, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, es if f >= es else se, .7)
    return c, (640, 1400 + k * 8, z * (1 + .0015 * max(0, f - es)), lerp(0, 2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'prancheta') - 3, 130, .7)
    s.apito(s.W(1, 'Beira-Rio') - 4)
    s.thunk(s.W(1, 'oito') - 3, 150, .9)
    s.thunk(s.W(1, 'um') - 3, 150, .9)
    s.thunk(s.W(2, 'Patrick') - 9, 130, .8)
    s.thunk(s.W(2, 'tres') - 3, 150, .9)
    s.thunk(s.W(3, 'Mateus') - 3, 130, .8)
    s.thunk(s.W(3, 'Erick') - 3, 170, .5)
    s.thunk(s.W(3, 'Tarzia') - 3, 170, .5)
    s.thunk(s.W(3, 'Rene') - 3, 170, .6)
    s.thunk(s.W(4, 'quarenta') - 3, 160, 1.0)
    s.thunk(s.W(4, 'Corinthians') - 3, 120, .8)
    s.thunk(s.W(5, 'seis') - 3, 150, .9)
    s.ting(s.W(5, 'escapa') - 6, .35)
