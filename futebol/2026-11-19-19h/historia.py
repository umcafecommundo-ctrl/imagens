"""anima.futebol — 19/11/2026 19h — Brasileirão 35ª rodada: noite decisiva contra o rebaixamento (Vasco x Inter e Vitória x Bragantino).
Fontes (conferidas em 19/11/2026): CNN Brasil (Vasco x Internacional quinta 19/11 19h30 em São Januário; Vasco 11º com 44 pts,
duas vitórias seguidas; Inter 38 pts; técnicos Pedro Emanuel e Eduardo Baptista); Tribuna Popular/Notícias ao Minuto (Inter 38,
Vitória 38 e Grêmio 38; Corinthians 40 após 4x0 no Botafogo; vitória leva o Inter a 41 e passa Grêmio e Corinthians;
Vitória x Bragantino no mesmo horário no Barradão; Alan Patrick volta; Inter sem vitória fora com Eduardo Baptista);
Sou Timão (se Inter e Vitória vencerem, Corinthians volta ao Z4). Posição exata do Inter diverge (16º x 17º) -> não citada.
Sem escudos/logos/taças reais: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Hoje à noite, dois jogos podem jogar o Corinthians de volta para a zona de rebaixamento.",
    "Às sete e meia, o Vasco recebe o Internacional em São Januário, e o Vitória enfrenta o Bragantino no Barradão.",
    "Internacional, Vitória e Grêmio têm trinta e oito pontos, e o Corinthians tem quarenta.",
    "Se o Inter vencer, chega a quarenta e um e passa Grêmio e Corinthians de uma vez.",
    "Eduardo Baptista ganha a volta de Alan Patrick, mas ainda não venceu fora de casa no comando do Inter.",
    "E o Vasco, décimo primeiro com quarenta e quatro pontos, vem de duas vitórias seguidas.",
    "Se Inter e Vitória vencerem, o Corinthians cai de novo para a zona.",
    "Quem se salva nessa noite de decisão?",
]
CAPTXT = [
    "Hoje à noite, 2 jogos podem jogar o Corinthians|de volta para a zona de rebaixamento.",
    "Às 19h30, o Vasco recebe o Internacional em São Januário,|e o Vitória enfrenta o Bragantino no Barradão.",
    "Internacional, Vitória e Grêmio têm 38 pontos,|e o Corinthians tem 40.",
    "Se o Inter vencer, chega a 41|e passa Grêmio e Corinthians de uma vez.",
    "Eduardo Baptista ganha a volta de Alan Patrick, mas ainda|não venceu fora de casa no comando do Inter.",
    "E o Vasco, 11º com 44 pontos,|vem de 2 vitórias seguidas.",
    "Se Inter e Vitória vencerem,|o Corinthians cai de novo para a zona.",
    "Quem se salva|nessa noite de decisão?",
]
FALA_TIKTOK = "Quem se salva hoje? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM SE SALVA?"
TWIST = 6
FLASH = [3]
CHECK = [(0, 'dois', 4), (0, 'Corinthians', 4), (0, 'rebaixamento', 4), (1, 'Vasco', 4), (1, 'Internacional', 4),
         (1, 'Vitoria', 4), (1, 'Bragantino', 4), (2, 'trinta', 4), (2, 'quarenta', 4), (3, 'quarenta', 4), (3, 'Corinthians', 4),
         (4, 'Alan', 4), (4, 'fora', 4), (5, 'Vasco', 4), (5, 'duas', 4), (6, 'zona', 4), (7, 'salva', 4)]

COR, COR_F = time_('CORINTHIANS')
VAS, VAS_F = time_('VASCO')
GRE, GRE_F = time_('GRÊMIO')
INT, INT_F = time_('INTERNACIONAL')
VIT_, VIT_F = time_('VITÓRIA')
BRA, BRA_F = time_('BRAGANTINO')


def jog(c, x, y, h, f, seed, cores, faixa, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=cores, faixa=faixa, **kw)


def s0(f):
    c = estadio2('dusk').copy()
    ho = wt(0, 'Hoje') - 3; do = wt(0, 'dois') - 3; co = wt(0, 'Corinthians') - 3; re = wt(0, 'rebaixamento') - 3
    if f >= ho: paste_c(c, calendario('19', 'NOV'), 940, 1000, .5 * back(ramp(f, ho, ho + 8)))
    jog(c, 380, 2030, 860, f, 3, COR, COR_F, skin=4, hair='#151010', arms='cintura' if f < re else 'shrug',
        expr='stern' if f < re else 'nervous', look=1, num_='10')
    put_placa(c, 'CORINTHIANS', COR, 380, 1080, f, co, 46, -3)
    num(c, '2 JOGOS', 640, 740, f, do, 130, -4)
    if f >= re: explosao(c, 870, 1420, f, re, 150, cor=(214, 40, 44))
    num(c, 'VOLTA AO Z4?', 870, 1420, f, re, 76, 3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, re, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    se = wt(1, 'sete') - 3; va = wt(1, 'Vasco') - 3; it = wt(1, 'Internacional') - 3; sj = wt(1, 'Januario') - 3
    vi = wt(1, 'Vitoria') - 3; br = wt(1, 'Bragantino') - 3; ba = wt(1, 'Barradao') - 3
    num(c, '19H30', 640, 730, f, se, 120, -3)
    for (x, cores, faixa, nome, k0, fl, sd, sk) in [(250, VAS, VAS_F, 'VASCO', va, False, 4, 3), (500, INT, INT_F, 'INTER', it, True, 6, 1),
                                                    (760, VIT_, VIT_F, 'VITÓRIA', vi, False, 8, 4), (1010, BRA, BRA_F, 'BRAGANTINO', br, True, 10, 2)]:
        if f >= k0 - 6:
            yy = 1990 + 60 * (1 - easeOut(ramp(f, k0 - 6, k0 + 4)))
            jog(c, x, yy, 520, f, sd, cores, faixa, skin=sk, arms='cintura', expr='stern', look=-1 if fl else 1, flip=fl)
            put_placa(c, nome, cores, x, 1400, f, k0, 28, -3 if fl else 3)
    num(c, 'SÃO JANUÁRIO', 380, 960, f, sj, 64, -3)
    num(c, 'BARRADÃO', 890, 1120, f, ba, 64, 3)
    z = lerp(1.0, 1.08, smooth(f / 150))
    return c, (640 + 20 * math.sin(f * .03), 1380, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    tr = wt(2, 'trinta') - 3; qu = wt(2, 'quarenta') - 3
    tabela(c, [('', 'CORINTHIANS', COR, '40', False)], 640, 880, f, qu)
    tabela(c, [('', 'INTERNACIONAL', INT, '38', True)], 640, 1040, f, wt(2, 'Internacional') - 3)
    tabela(c, [('', 'VITÓRIA', VIT_, '38', False)], 640, 1200, f, wt(2, 'Vitoria') - 3)
    tabela(c, [('Z4', 'GRÊMIO', GRE, '38', False)], 640, 1360, f, wt(2, 'Gremio') - 3)
    num(c, '38 PONTOS', 640, 720, f, tr, 100, -3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, qu, .5)
    return c, (640, 1300 + k * 8, z, k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    ve = wt(3, 'vencer') - 3; qu = wt(3, 'quarenta') - 3; co = wt(3, 'Corinthians') - 3
    jog(c, 560, 2030, 820, f, 6, INT, INT_F, skin=1, arms='up' if f >= qu else 'cintura', expr='grin' if f >= qu else 'stern', look=0, num_='10')
    put_placa(c, 'INTERNACIONAL', INT, 980, 1500, f, 0, 34, 3)
    if f >= qu: explosao(c, 640, 760, f, qu, 190)
    num(c, '41 PONTOS', 640, 760, f, qu + 2, 120, -4)
    num(c, 'PASSA GRÊMIO', 640, 930, f, wt(3, 'Gremio') - 3, 64, -2)
    num(c, 'E CORINTHIANS', 640, 1040, f, co, 64, 2)
    z = lerp(1.25, 1.04, easeOut(ramp(f, 0, 35))) * (1 + .0006 * f)
    k = kick(f, qu, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    ed = wt(4, 'Eduardo') - 3; al = wt(4, 'Alan') - 3; fo = wt(4, 'fora') - 3
    ex = lerp(-200, 330, easeOut(ramp(f, ed - 10, ed + 4)))
    ax = lerp(1500, 930, easeOut(ramp(f, al - 10, al + 4)))
    jog(c, ex, 2040, 760, f, 11, INT, INT_F, skin=1, hair='#3a2a1e', arms='cintura', expr='stern' if f < fo else 'nervous', look=1)
    jog(c, ax, 2040, 760, f, 13, INT, INT_F, skin=2, hair='#151010', arms='joinha' if f >= al + 4 else 'run',
        run=(f * .1) % 1 if f < al + 4 else None, expr='grin', look=-1, flip=True, num_='10')
    put_placa(c, 'EDUARDO BAPTISTA', INT, 330, 1180, f, ed, 34, -3)
    put_placa(c, 'ALAN PATRICK', INT, 930, 1180, f, al, 38, 3)
    num(c, 'ESTÁ DE VOLTA', 930, 900, f, al + 6, 60, 3)
    num(c, 'SEM VENCER FORA', 640, 720, f, fo, 84, -3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, fo, .5)
    return c, (640 + 15 * math.sin(f * .04), 1400 + k * 8, z, k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    va = wt(5, 'Vasco') - 3; de = wt(5, 'decimo') - 3; du = wt(5, 'duas') - 3
    jog(c, 380, 2030, 820, f, 4, VAS, VAS_F, skin=3, arms='up' if f >= du else 'cintura', expr='grin' if f >= du else 'proud', look=1, num_='9')
    put_placa(c, 'VASCO', VAS, 380, 1100, f, va, 50, -3)
    tabela(c, [('11º', 'VASCO', VAS, '44', True)], 640, 760, f, de)
    if f >= du: explosao(c, 880, 1300, f, du, 150)
    num(c, '2 VITÓRIAS', 880, 1260, f, du, 80, 3)
    num(c, 'SEGUIDAS', 880, 1380, f, du + 3, 70, -2)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, du, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('golden').copy()
    it = wt(6, 'Inter') - 3; vi = wt(6, 'Vitoria') - 3; co = wt(6, 'Corinthians') - 3; zo = wt(6, 'zona') - 3
    ix = lerp(-220, 260, easeOut(ramp(f, it - 10, it + 4)))
    vx = lerp(1500, 1000, easeOut(ramp(f, vi - 10, vi + 4)))
    jog(c, ix, 2030, 640, f, 12, INT, INT_F, skin=2, arms='up' if f >= co else 'cintura', expr='grin', look=1)
    jog(c, vx, 2030, 640, f, 14, VIT_, VIT_F, skin=4, hair='#111111', arms='up' if f >= co else 'cintura', expr='grin', look=-1, flip=True)
    jog(c, 640, 2060, 760, f, 3, COR, COR_F, skin=4, hair='#151010', arms='shrug' if f >= zo else 'cintura', expr='nervous' if f >= co else 'stern', look=0)
    put_placa(c, 'INTER', INT, 260, 1290, f, it, 34, -3)
    put_placa(c, 'VITÓRIA', VIT_, 1000, 1290, f, vi, 34, 3)
    put_placa(c, 'CORINTHIANS', COR, 640, 1200, f, co, 40, -2)
    if f >= zo: explosao(c, 640, 800, f, zo, 170, cor=(214, 40, 44))
    num(c, 'DE VOLTA AO Z4', 640, 800, f, zo, 84, -3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, zo, .7)
    return c, (640, 1420 + k * 8, z, k), 'golden'


def s7(f):
    c = estadio2('dusk').copy()
    sa = wt(7, 'salva') - 3; de = wt(7, 'decisao') - 3
    jog(c, 260, 2030, 640, f, 12, INT, INT_F, skin=2, arms='cintura', expr='nervous', look=1)
    jog(c, 640, 2050, 700, f, 3, COR, COR_F, skin=4, hair='#151010', arms='cintura', expr='nervous', look=0)
    jog(c, 1010, 2030, 640, f, 14, VIT_, VIT_F, skin=4, hair='#111111', arms='cintura', expr='nervous', look=-1, flip=True)
    put_placa(c, 'INTER', INT, 260, 1310, f, 0, 32, -3)
    put_placa(c, 'CORINTHIANS', COR, 640, 1260, f, 0, 36, 2)
    put_placa(c, 'VITÓRIA', VIT_, 1010, 1310, f, 0, 32, 3)
    num(c, 'QUEM SE SALVA?', 640, 760, f, sa, 96, -4)
    num(c, 'NOITE DE DECISÃO', 640, 960, f, de, 66, 3)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('NOITE DECISIVA NO Z4', 'QUINTA, 19/11', wt(0, 'rebaixamento') + 4),
         1: ('VASCO x INTER  ·  VITÓRIA x BRAGANTINO', 'HOJE, 19H30', wt(1, 'Barradao') + 4),
         2: ('BRIGA CONTRA O Z4', 'TRÊS TIMES COM 38', wt(2, 'quarenta') + 4),
         3: ('SE O INTER VENCER', 'PASSA DOIS RIVAIS', wt(3, 'Corinthians') + 4),
         4: ('INTER COM ALAN PATRICK', 'SEM VITÓRIA FORA COM EDUARDO BAPTISTA', wt(4, 'Inter') + 2),
         5: ('VASCO 11º, 44 PONTOS', 'DUAS VITÓRIAS SEGUIDAS', wt(5, 'seguidas') + 2),
         6: ('INTER E VITÓRIA VENCENDO', 'CORINTHIANS VOLTA AO Z4', wt(6, 'zona') + 4)}
    if si == 7: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'dois') - 3, 150, .9)
    s.ting(s.W(0, 'rebaixamento') - 3, .3)
    s.thunk(s.W(1, 'sete') - 3, 160, .6)
    s.thunk(s.W(1, 'Vasco') - 3, 150, .5)
    s.thunk(s.W(1, 'Vitoria') - 3, 150, .5)
    s.thunk(s.W(2, 'trinta') - 3, 150, .7)
    s.thunk(s.W(3, 'quarenta') - 3, 120, .9)
    s.thunk(s.W(4, 'Alan') - 3, 160, .6)
    s.ting(s.W(5, 'duas') - 3, .3)
    s.thunk(s.W(6, 'zona') - 3, 140, .9)
    s.ting(s.W(7, 'salva') - 3, .3)
