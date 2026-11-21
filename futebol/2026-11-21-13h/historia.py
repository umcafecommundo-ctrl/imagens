"""anima.futebol — 21/11/2026 13h — QUEM CAI? · EP. 2 — a conta do rebaixamento antes da 36ª rodada.
Fontes (conferidas em 21/11/2026, ver fatos.txt): Lance! (simulador de cenários após a 35ª, 20/11), Lance! (UFMG atualiza risco,
20/11), Bolavip (chances de rebaixamento após a 35ª, 20/11), Piranot (tabela após a 35ª), CNN Brasil/A Crítica/bahia.ba (post de
20/11 07h). Grêmio 38 e Inter 38 no Z4, Corinthians 40, Vitória 41; Inter x Vitória 23/11 19h30 Beira-Rio; Corinthians x Grêmio na
37ª; UFMG: Grêmio 70,6%, Inter 61,5%, Corinthians 26,6%. Sem escudos/logos: times por plaquinhas e cores."""
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
    "O Grêmio vai cair? Olha a conta, faltando três rodadas.",
    "Grêmio e Inter estão no Z4, com trinta e oito pontos.",
    "Logo acima, o Corinthians tem quarenta... e o Vitória, quarenta e um.",
    "Segunda tem confronto direto: Inter e Vitória, no Beira-Rio.",
    "E na penúltima rodada, Corinthians e Grêmio, frente a frente.",
    "Pela UFMG, o risco de queda do Grêmio passa de... setenta por cento.",
]
CAPTXT = [
    "O Grêmio vai cair? Olha a conta,|faltando 3 rodadas.",
    "Grêmio e Inter estão no Z4,|com 38 pontos.",
    "Logo acima, o Corinthians tem 40...|e o Vitória, 41.",
    "Segunda tem confronto direto:|Inter e Vitória, no Beira-Rio.",
    "E na penúltima rodada,|Corinthians e Grêmio, frente a frente.",
    "Pela UFMG, o risco de queda do Grêmio|passa de... 70%.",
]
FALA_TIKTOK = "O Grêmio vai cair? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "GRÊMIO CAI?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Gremio', 4), (0, 'cair', 4), (0, 'tres', 4), (1, 'trinta', 4), (2, 'quarenta', 4), (2, 'Vitoria', 4),
         (3, 'Segunda', 4), (3, 'Beira-Rio', 4), (4, 'penultima', 4), (4, 'frente', 4), (5, 'UFMG', 4), (5, 'setenta', 4)]

GRE, GRE_F = time_('GRÊMIO')
INT, INT_F = time_('INTERNACIONAL')
COR, COR_F = time_('CORINTHIANS')
VIT_, VIT_F = time_('VITÓRIA')


def gre(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=GRE, faixa=GRE_F, **kw)


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'raspado'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def cor(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=COR, faixa=COR_F, **kw)


def vit(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 4); kw.setdefault('hs', 'raspado'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=VIT_, faixa=VIT_F, **kw)


def s0(f):
    """conta_bg: marca da série e depois a pergunta polêmica."""
    c = conta_bg().copy()
    ca = wt(0, 'cair') - 3; tr = wt(0, 'tres') - 3
    gre(c, 640, 2080, 860, f, 6, arms='cintura' if f < ca else 'cheek', expr='stern' if f < ca else 'nervous', look=0, num_='10')
    if f < ca - 2:
        num(c, 'QUEM CAI?', 640, 820, f, 0, 170, -3)
        num(c, 'EP. 2', 640, 1030, f, 4, 130, 3)
    elif f < tr - 2:
        num(c, 'O GRÊMIO', 640, 820, f, ca, 150, -3)
        num(c, 'VAI CAIR?', 640, 1010, f, ca + 3, 150, 3)
    else:
        num(c, '3 RODADAS', 640, 900, f, tr, 140, -3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ca, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """telão com a tabelinha do Z4."""
    c = telao('dusk').copy()
    z4 = wt(1, 'Z4') - 3; tr = wt(1, 'trinta') - 3
    tabela(c, [('Z4', 'GRÊMIO', GRE, '38', True), ('Z4', 'INTER', INT, '38', True)], 640, 840, f, z4)
    gre(c, 330, 2080, 640, f, 3, arms='hang', expr='nervous', look=1, num_='9')
    inter(c, 950, 2080, 640, f, 5, arms='cheek' if f >= tr else 'hang', expr='pained' if f >= tr else 'nervous', look=-1, flip=True, num_='7')
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, tr, .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """estádio dourado: quem está logo acima (um número por vez)."""
    c = estadio2('golden').copy()
    qu = wt(2, 'quarenta') - 3; vi = wt(2, 'Vitoria') - 3
    cor(c, 360, 2040, 820, f, 4, arms='cintura', expr='stern' if f < vi else 'nervous', look=1, num_='9')
    vit(c, 920, 2060, 780, f, 8, arms='cintura' if f < vi else 'punho', expr='stern', look=-1, flip=True, num_='10')
    if f < vi - 2:
        if f >= qu: num(c, 'CORINTHIANS 40', 640, 820, f, qu, 94, -2)
    else:
        num(c, 'VITÓRIA 41', 640, 820, f, vi, 120, 3)
    z = lerp(1.18, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, max(qu, vi), .5)
    return c, (lerp(600, 680, smooth(f / 120)), 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'golden'


def s3(f):
    """estádio de dia: Inter x Vitória segunda (calendário, depois o confronto)."""
    c = estadio2('day').copy()
    se = wt(3, 'Segunda') - 3; it = wt(3, 'Inter') - 3; be = wt(3, 'Beira-Rio') - 3
    fx = lerp(-260, 330, easeOut(ramp(f, it - 6, it + 10)))
    px = lerp(1500, 930, easeOut(ramp(f, it - 6, it + 10)))
    if f < it + 10:
        linhas_vel(c, fx, 2010, 840, f, dir=-1); linhas_vel(c, px, 2010, 840, f, dir=1)
    inter(c, fx, 2010, 840, f, 3, arms='cintura', expr='stern', look=1, num_='10', run=(f * .1) % 1 if f < it + 10 else None)
    vit(c, px, 2010, 840, f, 7, arms='punho' if f >= be else 'cintura', expr='stern', look=-1, flip=True, num_='9',
        run=(f * .1) % 1 if f < it + 10 else None)
    if f < it - 2:
        if f >= se: paste_c(c, calendario('23', 'NOV'), 640, 960, .7 * back(ramp(f, se, se + 8)))
    else:
        num(c, 'INTER x VITÓRIA', 640, 860, f, it, 104, -3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, it, .6)
    return c, (640, 1400 + k * 8, z, k), 'day'


def s4(f):
    """prancheta: Corinthians x Grêmio na 37ª rodada."""
    c = prancheta().copy()
    pe = wt(4, 'penultima') - 3; co = wt(4, 'Corinthians') - 3; fr = wt(4, 'frente') - 3
    for i, x in enumerate((330, 621, 912)):
        pino(c, x, 1000 + 12 * math.sin(f * .2 + i), COR, f, co + i * 2, '', 80)
        pino(c, x, 1460 + 12 * math.sin(f * .2 + i * 1.7), GRE, f, co + 6 + i * 2, '', 80)
    if f >= fr:
        seta(c, (621, 1080), (621, 1200), f, fr, 8, (255, 255, 255), 12)
        seta(c, (621, 1380), (621, 1260), f, fr, 8, (255, 216, 74), 12)
    if f < co - 2:
        num(c, '37ª RODADA', 640, 760, f, pe, 120, -3)
    else:
        num(c, 'COR x GRÊMIO', 640, 760, f, co, 116, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, fr, .6)
    return c, (640 + 40 * math.sin(f * .06), 1300 + k * 8 + 20 * math.sin(f * .045), z * (1 + .0012 * f),
               lerp(0, 2, smooth(ramp(f, 0, 60))) + .8 * math.sin(f * .05)), 'day'


def s5(f):
    """vestiário do Grêmio: a resposta, o número gigante."""
    c = vestiario(GRE, GRE_F).copy()
    uf = wt(5, 'UFMG') - 3; se = wt(5, 'setenta') - 3
    gre(c, 640, 2110, 860, f, 6, arms='hang' if f < se else 'cheek', expr='nervous' if f < se else 'pained', look=0, num_='10')
    if f < se - 2:
        if f >= uf: num(c, 'RISCO DE QUEDA', 640, 1080, f, uf, 110, -3)
    else:
        if f >= se: explosao(c, 640, 1080, f, se, 260, cor=(230, 60, 60))
        numero_gigante(c, '70,6%', 640, 1080, f, se, 240, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, se, .8)
    return c, (640, 1400 + k * 10, z * (1 + .0015 * max(0, f - se)), k), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(s.W(0, 'cair') - 3, 150, .9)
    s.thunk(s.W(0, 'tres') - 3, 120, .8)
    s.thunk(s.W(1, 'Z4') - 3, 150, .8)
    s.thunk(s.W(1, 'trinta') - 3, 120, .9)
    s.thunk(s.W(2, 'quarenta') - 3, 150, .7)
    s.thunk(s.W(2, 'Vitoria') - 3, 120, .8)
    s.thunk(s.W(3, 'Segunda') - 3, 160, .6)
    s.apito(s.W(3, 'Inter') - 4)
    s.thunk(s.W(3, 'Beira-Rio') - 3, 130, .7)
    s.thunk(s.W(4, 'penultima') - 3, 150, .7)
    s.thunk(s.W(4, 'frente') - 3, 120, .9)
    s.thunk(s.W(5, 'UFMG') - 3, 150, .7)
    s.thunk(s.W(5, 'setenta') - 3, 110, 1.0)
    s.ting(s.W(5, 'setenta') - 3, .35)
