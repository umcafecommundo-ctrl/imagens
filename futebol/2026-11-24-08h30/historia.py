"""anima.futebol — 24/11/2026 08h30 — BASTIDORES · EP. 1 — o presidente do Inter depois de Internacional 2x5 Vitória.
Fontes (conferidas em 24/11/2026, ver fatos.txt): Terra (24/11 00h40), TV Sim Brasil (24/11 01h22), Zona Mista (23/11 23h03),
Antenados no Futebol (24/11 02h05), SBT Sports, A Tarde, Gazeta Esportiva.
Alessandro Barcellos pediu desculpas, "é inadmissível", o resultado "nos envergonha"; Inter 38 pontos na zona;
faltam Bragantino (Beira-Rio, 29/11) e Cruzeiro (fora, 2/12). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  BASTIDORES'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Inter ainda escapa? Ouve o presidente.",
    "No Beira-Rio, o Vitória goleou... cinco a dois.",
    "Depois do jogo, o presidente Alessandro Barcellos pediu desculpas ao torcedor.",
    "Disse que foi inadmissível... e que o resultado envergonha.",
    "O Inter segue na zona, com trinta e oito pontos.",
    "Faltam Bragantino, em casa, e Cruzeiro, fora. O Inter escapa?",
]
CAPTXT = [
    "O Inter ainda escapa?|Ouve o presidente.",
    "No Beira-Rio, o Vitória|goleou... 5 a 2.",
    "Depois do jogo, o presidente|Alessandro Barcellos pediu|desculpas ao torcedor.",
    "Disse que foi inadmissível...|e que o resultado envergonha.",
    "O Inter segue na zona,|com 38 pontos.",
    "Faltam Bragantino, em casa,|e Cruzeiro, fora. O Inter escapa?",
]
FALA_TIKTOK = "O Inter escapa? Comenta sim ou não."
CTA_TEXTO = "INTER ESCAPA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [1]
CHECK = [(0, 'Inter', 4), (0, 'escapa', 4), (0, 'presidente', 4), (1, 'Vitória', 4), (1, 'goleou', 4), (1, 'cinco', 4),
         (2, 'presidente', 4), (2, 'Barcellos', 4), (2, 'desculpas', 4), (3, 'inadmissível', 4), (3, 'envergonha', 4),
         (4, 'zona', 4), (4, 'trinta', 4), (5, 'Bragantino', 4), (5, 'Cruzeiro', 4), (5, 'escapa', 4)]

INT, INT_F = time_('INTERNACIONAL')
VIT_, VIT_F = time_('VITÓRIA')
BRA, BRA_F = time_('BRAGANTINO')
CRU_, CRU_F = time_('CRUZEIRO')
TERNO = ('#23262e', '#ffffff', '#23262e')   # terno escuro genérico do presidente


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def vit(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=VIT_, faixa=VIT_F, **kw)


def pres(c, f, **kw):
    put_atleta(c, 640, 2000, 980, f, 4, cores=TERNO, faixa=None, skin=0, hs='curto', hair='#5a4a3a', **kw)


CLOSE_F = 38


def s0(f):
    """quadro 0 = capa: close do torcedor do Inter (vermelho) + série + pergunta; depois o jogador do Inter no vestiário."""
    c = vestiario(INT, INT_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='preocupado', s=.9, roupa='#c8102e', pele='#e0a87e', cabelo='#3a2414')
        num(c, 'BASTIDORES', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 1', 621, 440, f, 0, 100, 2)
        num(c, 'O INTER', 621, 1350, f, 0, 150, -2)
        num(c, 'ESCAPA?', 621, 1530, f, 0, 160, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    pr = wt(0, 'presidente') - 3
    inter(c, 640, 2110, 860, f, 6, arms='cheek', expr='pained', look=0, num_='10')
    if f < pr - 2:
        put_placa(c, 'INTER', INT, 640, 1180, f, CLOSE_F, 110, -3)
    else:
        num(c, 'O PRESIDENTE', 640, 1180, f, pr, 120, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


def s1(f):
    """telão do estádio: Internacional 2 x 5 Vitória."""
    c = telao('dusk').copy()
    vi = wt(1, 'Vitória') - 3; ci = wt(1, 'cinco') - 3
    if f < vi - 2:
        telao_txt(c, [('BEIRA-RIO', 150)], f, 0, y=800)
    elif f < ci - 2:
        telao_txt(c, [('VITÓRIA', 160)], f, vi, y=800)
    else:
        telao_txt(c, [('INTER 2 x 5', 140), ('VITÓRIA', 140)], f, ci, y=680, gap=170)
    vit(c, 900, 2060, 820, f, 3, num_='7', flip=True, arms='up' if f >= vi else 'hang', expr='grin', look=-1)
    inter(c, 360, 2080, 840, f, 5, num_='9', arms='cheek' if f >= ci else 'hang', expr='pained', look=1)
    z = lerp(1.1, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, ci if f >= ci else vi, .8)
    return c, (lerp(660, 620, smooth(f / 120)), 1300 + k * 10, z, k), 'dusk'


def s2(f):
    """coletiva: o presidente (boneco genérico de terno) + placa; pediu desculpas."""
    c = coletiva(INT).copy()
    ba = wt(2, 'Barcellos') - 3; de = wt(2, 'desculpas') - 3
    pres(c, f, arms='hang', expr='pained' if f >= de else 'stern', look=0)
    mesa_coletiva(c)
    if f < ba - 2:
        num(c, 'PRESIDENTE', 640, 760, f, 2, 120, -3)
    elif f < de - 2:
        put_placa(c, 'BARCELLOS', INT, 640, 780, f, ba, 96, -2)
    else:
        num(c, 'DESCULPAS', 640, 780, f, de, 140, 3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, de if f >= de else ba, .7)
    return c, (640 + 20 * math.sin(f * .04), 1350 + k * 10, z, k), 'day'


def s3(f):
    """coletiva mais perto: "inadmissível" (manchete no OVERLAY) e VERGONHA."""
    c = coletiva(INT).copy()
    en = wt(3, 'envergonha') - 3
    pres(c, f, arms='shrug' if f < en else 'hang', expr='stern' if f < en else 'pained', look=0)
    mesa_coletiva(c)
    if f >= en:
        num(c, 'VERGONHA', 640, 780, f, en, 150, -3)
    z = lerp(1.15, 1.06, easeOut(ramp(f, 0, 30))) * (1 + .0010 * f)
    k = kick(f, en if f >= en else 0, .8)
    return c, (640, 1250 + k * 10, z, k + .8 * math.sin(f * .05)), 'day'


def s4(f):
    """a conta: Inter na zona, 38 pontos."""
    c = conta_bg().copy()
    zo = wt(4, 'zona') - 3; tr = wt(4, 'trinta') - 3
    if f < zo - 2:
        put_placa(c, 'INTER', INT, 640, 1000, f, 0, 110, -2)
    elif f < tr - 2:
        numero_gigante(c, 'Z4', 640, 1000, f, zo, 300, 3)
    else:
        numero_gigante(c, '38 PTS', 640, 1000, f, tr, 220, -3)
    inter(c, 640, 2090, 760, f, 7, arms='cheek' if f >= zo else 'cintura', expr='pained', look=0, num_='9')
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, tr if f >= tr else (zo if f >= zo else 0), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """prancheta: faltam Bragantino (em casa) e Cruzeiro (fora) — o Inter escapa?"""
    c = prancheta().copy()
    br = wt(5, 'Bragantino') - 3; cr = wt(5, 'Cruzeiro') - 3; es = wt(5, 'escapa') - 8
    inter(c, 640, 2090, 780, f, 6, arms='hang' if f < es else 'cheek', expr='nervous', look=0, num_='10')
    if f < cr - 2:
        if f >= br: put_placa(c, 'BRAGANTINO', BRA, 640, 900, f, br, 96, -2)
        if f >= br + 6: num(c, 'EM CASA', 640, 1100, f, br + 6, 100, 2)
    elif f < es - 2:
        put_placa(c, 'CRUZEIRO', CRU_, 640, 900, f, cr, 96, 2)
        if f >= cr + 6: num(c, 'FORA', 640, 1100, f, cr + 6, 110, -2)
    else:
        num(c, 'ESCAPA?', 640, 1000, f, es, 170, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, es if f >= es else (cr if f >= cr else br), .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    if si == 3:
        en = wt(3, 'envergonha') - 3
        if lf < en - 2:
            im = destaque(im, '"É INADMISSÍVEL"', lf, 2, sub='PRESIDENTE DO INTER', y=470)
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.ting(s.W(0, 'presidente') - 3, .35)
    s.thunk(s.W(0, 'presidente') - 3, 130, .7)
    s.thunk(s.W(1, 'Vitória') - 3, 130, .8)
    s.apito(s.W(1, 'cinco') - 8, longo=True)
    s.thunk(s.W(1, 'cinco') - 3, 160, 1.0)
    s.thunk(s.W(2, 'Barcellos') - 3, 130, .8)
    s.thunk(s.W(2, 'desculpas') - 3, 150, .9)
    s.thunk(s.W(3, 'inadmissível') - 3, 150, .9)
    s.thunk(s.W(3, 'envergonha') - 3, 160, 1.0)
    s.thunk(s.W(4, 'zona') - 3, 150, .9)
    s.thunk(s.W(4, 'trinta') - 3, 160, 1.0)
    s.thunk(s.W(5, 'Bragantino') - 3, 130, .8)
    s.thunk(s.W(5, 'Cruzeiro') - 3, 130, .8)
    s.ting(s.W(5, 'escapa') - 8, .35)
    s.thunk(s.W(5, 'escapa') - 8, 160, 1.0)
