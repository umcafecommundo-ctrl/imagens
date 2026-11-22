"""anima.futebol — 22/11/2026 18h50 — QUEM CAI? · EP. 3 — tabela do rebaixamento antes do fim da 36ª rodada (pedido do Luis).
Fontes (conferidas em 22/11/2026, ver fatos.txt): Futmetrica (tabela e risco, atualizado 22/11 06:46, 10 mil simulações),
ValorFinal (tabela e risco, 21/11 20:30), UFMG via Lance/Itatiaia (após a 35ª). Inter 38 e Grêmio 38 no Z4, Corinthians 40,
Vitória e Mirassol 41, Botafogo 42. Risco (Futmetrica): Grêmio 71,8%, Inter 65,1%, Corinthians 17,4%.
Amanhã: Inter x Vitória 19h30 e Santos x Grêmio 21h. Sem escudos/logos: times por plaquinhas e cores."""
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
    "Quem cai: Inter ou Grêmio? Olha a tabela, antes do fim da rodada.",
    "No Z4, Inter e Grêmio estão com... trinta e oito pontos.",
    "Logo acima, Corinthians tem quarenta... Vitória e Mirassol, quarenta e um.",
    "Na Futmétrica, o risco de queda do Grêmio é de... quase setenta e dois por cento.",
    "O do Inter, sessenta e cinco... e o do Corinthians, dezessete.",
    "Amanhã tem Inter e Vitória, e Santos e Grêmio. Quem cai?",
]
CAPTXT = [
    "Quem cai: Inter ou Grêmio?|Olha a tabela, antes do fim da rodada.",
    "No Z4, Inter e Grêmio estão com...|38 pontos.",
    "Logo acima, Corinthians tem 40...|Vitória e Mirassol, 41.",
    "Na Futmétrica, o risco de queda do Grêmio|é de... quase 72%.",
    "O do Inter, 65%...|e o do Corinthians, 17%.",
    "Amanhã tem Inter e Vitória,|e Santos e Grêmio. Quem cai?",
]
FALA_TIKTOK = "Quem cai? Comenta Inter ou Grêmio."
CTA_TEXTO = "QUEM CAI?"
CTA_PALAVRA = 'INTER ou GRÊMIO'
TWIST = 3
FLASH = [3]
CHECK = [(0, 'Inter', 4), (0, 'Gremio', 4), (0, 'tabela', 4), (1, 'Z4', 4), (1, 'trinta', 4), (2, 'quarenta', 4),
         (2, 'Mirassol', 4), (3, 'Futmetrica', 4), (3, 'setenta', 4), (4, 'sessenta', 4), (4, 'dezessete', 4),
         (5, 'Amanha', 4), (5, 'Santos', 4), (5, 'cai', 4)]

GRE, GRE_F = time_('GRÊMIO')
INT, INT_F = time_('INTERNACIONAL')
COR, COR_F = time_('CORINTHIANS')
VIT_, VIT_F = time_('VITÓRIA')
MIR, MIR_F = time_('MIRASSOL')
SAN, SAN_F = time_('SANTOS')


def gre(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=GRE, faixa=GRE_F, **kw)


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'raspado'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def cor(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=COR, faixa=COR_F, **kw)


CLOSE_F = 38   # ~1,3 s de close de abertura


def s0(f):
    """quadro 0 = capa: close do torcedor (camisa vermelha, Inter) + série + pergunta; depois Inter e Grêmio lado a lado."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='medo', s=.9, roupa='#c8102e', pele='#c89070', cabelo='#3a2a1e')
        num(c, 'QUEM CAI?', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 3', 621, 430, f, 0, 100, 2)
        num(c, 'QUEM CAI:', 621, 1350, f, 0, 130, -2)
        num(c, 'INTER OU GRÊMIO?', 621, 1520, f, 0, 100, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    ta = wt(0, 'tabela') - 3
    inter(c, 360, 2080, 820, f, 5, arms='cheek', expr='nervous', look=1, num_='7')
    gre(c, 920, 2080, 820, f, 6, arms='cheek', expr='nervous', look=-1, flip=True, num_='10')
    if f < ta - 2:
        num(c, 'INTER x GRÊMIO', 640, 860, f, CLOSE_F, 110, -3)
    else:
        num(c, 'A TABELA', 640, 860, f, ta, 140, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """telão: o Z4 (2 linhas)."""
    c = telao('dusk').copy()
    z4 = wt(1, 'Z4') - 3; tr = wt(1, 'trinta') - 3
    tabela(c, [('17º', 'INTER', INT, '38', True), ('18º', 'GRÊMIO', GRE, '38', True)], 640, 840, f, z4)
    inter(c, 330, 2080, 640, f, 3, arms='hang', expr='nervous', look=1, num_='9')
    gre(c, 950, 2080, 640, f, 5, arms='cheek' if f >= tr else 'hang', expr='pained' if f >= tr else 'nervous', look=-1, flip=True, num_='7')
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, tr, .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """estádio dourado: quem está logo acima (3 linhas)."""
    c = estadio2('golden').copy()
    qu = wt(2, 'quarenta') - 3
    tabela(c, [('14º', 'VITÓRIA', VIT_, '41', False), ('15º', 'MIRASSOL', MIR, '41', False),
               ('16º', 'CORINTHIANS', COR, '40', True)], 640, 760, f, qu)
    cor(c, 640, 2080, 760, f, 4, arms='cintura', expr='stern', look=0, num_='9')
    z = lerp(1.18, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, qu, .5)
    return c, (lerp(600, 680, smooth(f / 120)), 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'golden'


def s3(f):
    """vestiário do Grêmio: a porcentagem gigante."""
    c = vestiario(GRE, GRE_F).copy()
    fm = wt(3, 'Futmetrica') - 3; se = wt(3, 'setenta') - 3
    gre(c, 640, 2110, 860, f, 6, arms='hang' if f < se else 'cheek', expr='nervous' if f < se else 'pained', look=0, num_='10')
    if f < se - 2:
        if f >= fm: num(c, 'RISCO DE QUEDA', 640, 1000, f, fm, 110, -3)
    else:
        explosao(c, 640, 1080, f, se, 260, cor=(230, 60, 60))
        numero_gigante(c, '71,8%', 640, 1080, f, se, 240, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, se, .8)
    return c, (640, 1400 + k * 10, z * (1 + .0015 * max(0, f - se)), k), 'day'


def s4(f):
    """telão: Inter, depois Corinthians (uma porcentagem por vez)."""
    c = telao('day').copy()
    it = wt(4, 'sessenta') - 3; co = wt(4, 'Corinthians') - 3; de = wt(4, 'dezessete') - 3
    if f < co - 2:
        inter(c, 640, 2090, 820, f, 3, arms='cheek', expr='pained', look=0, num_='10')
        if f >= it:
            numero_gigante(c, '65,1%', 640, 980, f, it, 220, -3)
        else:
            num(c, 'INTER', 640, 980, f, 0, 140, -3)
    else:
        cor(c, 640, 2090, 820, f, 4, arms='cintura', expr='stern', look=0, num_='9')
        if f >= de:
            numero_gigante(c, '17,4%', 640, 980, f, de, 220, 3)
        else:
            num(c, 'CORINTHIANS', 640, 980, f, co, 120, 3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, max(it, de if f >= de else it), .6)
    return c, (640 + 30 * math.sin(f * .05), 1380 + k * 8, z, k), 'day'


def s5(f):
    """estádio de dia: os jogos de amanhã (um por vez) e a pergunta."""
    c = estadio2('day').copy()
    am = wt(5, 'Amanha') - 3; sa = wt(5, 'Santos') - 3; qc = wt(5, 'cai') - 6
    if f < sa - 2:
        inter(c, 340, 2010, 820, f, 3, arms='cintura', expr='stern', look=1, num_='10')
        put_atleta(c, 940, 2010, 820, f, 7, cores=VIT_, faixa=VIT_F, skin=4, hs='raspado', hair='#151010',
                   arms='cintura', expr='stern', look=-1, flip=True, num_='9')
        if f < am + 10:
            paste_c(c, calendario('23', 'NOV'), 640, 960, .7 * back(ramp(f, am, am + 8)))
        else:
            num(c, 'INTER x VITÓRIA', 640, 820, f, am + 10, 90, -3)
            num(c, '19H30', 640, 990, f, am + 12, 130, 3)
    else:
        put_atleta(c, 340, 2010, 820, f, 2, cores=SAN, faixa=SAN_F, skin=2, hs='curto', hair='#151010',
                   arms='cintura', expr='stern', look=1, num_='10')
        gre(c, 940, 2010, 820, f, 6, arms='cheek' if f >= qc else 'cintura', expr='nervous', look=-1, flip=True, num_='9')
        if f < qc - 2:
            num(c, 'SANTOS x GRÊMIO', 640, 820, f, sa, 90, 3)
            num(c, '21H', 640, 990, f, sa + 2, 130, -3)
        else:
            num(c, 'QUEM CAI?', 640, 880, f, qc, 160, -3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, sa, .6)
    return c, (640, 1400 + k * 8, z, k), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(CLOSE_F, 150, .8)
    s.thunk(s.W(0, 'tabela') - 3, 130, .7)
    s.thunk(s.W(1, 'Z4') - 3, 150, .8)
    s.thunk(s.W(1, 'trinta') - 3, 120, .9)
    s.thunk(s.W(2, 'quarenta') - 3, 150, .8)
    s.thunk(s.W(2, 'Mirassol') - 3, 120, .7)
    s.thunk(s.W(3, 'Futmetrica') - 3, 150, .7)
    s.thunk(s.W(3, 'setenta') - 3, 110, 1.0)
    s.ting(s.W(3, 'setenta') - 3, .35)
    s.thunk(s.W(4, 'sessenta') - 3, 120, .9)
    s.thunk(s.W(4, 'dezessete') - 3, 120, .9)
    s.apito(s.W(5, 'Amanha') - 4)
    s.thunk(s.W(5, 'Santos') - 3, 130, .7)
    s.thunk(s.W(5, 'cai') - 6, 110, .9)
