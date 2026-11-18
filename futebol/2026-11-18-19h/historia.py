"""anima.futebol — 18/11/2026 19h — Brasileirão 35ª rodada: Coritiba x Santos hoje, com a volta de Neymar.
Fontes (conferidas em 18/11/2026): Gazeta Esportiva (Coritiba x Santos quarta 18/11 19h30 Couto Pereira; Santos 9º com 47 pts,
3 jogos sem vencer; Coritiba 13º com 42, 5 acima da zona; Neymar volta de suspensão; provável Santos com Arthur, Cebolinha,
Neymar, Coutinho e Gabigol; Coritiba venceu 3x0 no 1º turno; Santos x Grêmio 23/11 21h Morumbis);
Revista Oeste (18/11: 19h30 Couto Pereira, Neymar volta após suspensão e reassume a titularidade, Cuca com quinteto ofensivo
Arthur, Coutinho, Cebolinha, Gabigol e Neymar, Santos 9º 47 pts, Coritiba 13º 42, jejum de 3 rodadas, Santos x Grêmio 23/11 21h).
Sem escudos/logos/taças reais: times por plaquinhas e cores; jogadores genéricos com placa do nome."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Neymar está de volta ao Santos, depois de cumprir suspensão.",
    "O jogo é contra o Coritiba, hoje, às sete e meia da noite, no Couto Pereira.",
    "E o Cuca deve escalar um ataque pesado: Neymar, Coutinho, Everton Cebolinha e Gabigol juntos.",
    "O Santos precisa reagir: são três jogos sem vencer no Brasileirão.",
    "E tem revanche: no primeiro turno, deu Coritiba, três a zero.",
    "Na tabela, o Santos é nono, com quarenta e sete pontos, de olho na Libertadores.",
    "O Coritiba é décimo terceiro, com quarenta e dois, cinco acima da zona de rebaixamento.",
    "Depois, na segunda, o Santos recebe o Grêmio no Morumbis.",
]
CAPTXT = [
    "Neymar está de volta ao Santos,|depois de cumprir suspensão.",
    "O jogo é contra o Coritiba, hoje,|às 19h30, no Couto Pereira.",
    "E o Cuca deve escalar um ataque pesado: Neymar,|Coutinho, Everton Cebolinha e Gabigol juntos.",
    "O Santos precisa reagir:|são 3 jogos sem vencer no Brasileirão.",
    "E tem revanche: no 1º turno,|deu Coritiba, 3 a 0.",
    "Na tabela, o Santos é 9º, com 47 pontos,|de olho na Libertadores.",
    "O Coritiba é 13º, com 42,|5 acima da zona de rebaixamento.",
    "Depois, na segunda,|o Santos recebe o Grêmio no Morumbis.",
]
FALA_TIKTOK = "Neymar faz gol hoje? Comenta sim ou não, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Neymar', 4), (0, 'suspensao', 4), (1, 'Coritiba', 4), (1, 'sete', 4), (1, 'Pereira', 4), (2, 'Cuca', 4),
         (2, 'Coutinho', 4), (2, 'Cebolinha', 4), (2, 'Gabigol', 4), (3, 'tres', 4), (4, 'revanche', 4), (4, 'zero', 4),
         (5, 'nono', 4), (5, 'quarenta', 4), (6, 'decimo', 4), (6, 'cinco', 4), (7, 'Gremio', 4), (7, 'Morumbis', 4)]

SAN, SAN_F = time_('SANTOS')
CFC, CFC_F = time_('CORITIBA')
GRE, GRE_F = time_('GRÊMIO')
GK = ('#6b3fa0', '#111111', '#111111')


def san(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=SAN, faixa=SAN_F, **kw)


def cfc(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=CFC, faixa=CFC_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    ne = wt(0, 'Neymar') - 3; vo = wt(0, 'volta') - 3; su = wt(0, 'suspensao') - 3
    x = lerp(-250, 640, easeOut(ramp(f, 0, vo + 4)))
    if f < vo: linhas_vel(c, x, 2030, 880, f)
    san(c, x, 2030, 880, f, 7, hs='topete', arms='run' if f < vo + 4 else 'up', run=(f * .09) % 1 if f < vo + 4 else None,
        expr='grin', num_='10')
    put_placa(c, 'NEYMAR', SAN, 640, 1040, f, ne, 70, -3)
    explosao(c, 640, 780, f, vo, 220)
    num(c, 'DE VOLTA!', 640, 780, f, vo, 140, -4)
    if f >= vo: foco(c, 640, 1650, 470, .5 * ramp(f, vo, vo + 6))
    num(c, 'FIM DA SUSPENSÃO', 640, 1250, f, su, 70, 3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, vo, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    co = wt(1, 'Coritiba') - 3; se = wt(1, 'sete') - 3; cp = wt(1, 'Couto') - 3
    paste_c(c, calendario('18', 'NOV'), 640, 1180, .6 * back(ramp(f, 2, 10)))
    num(c, '19H30', 640, 740, f, se, 130, -3)
    cfc(c, 290, 2060, 640, f, 13, arms='cintura', expr='stern', look=1)
    put_placa(c, 'CORITIBA', CFC, 290, 1340, f, co, 46, -3)
    san(c, 990, 2060, 640, f, 12, arms='cintura', expr='stern', look=-1, flip=True)
    put_placa(c, 'SANTOS', SAN, 990, 1340, f, 2, 46, 3)
    num(c, 'COUTO PEREIRA', 640, 900, f, cp, 84, 2)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1380, z, 0), 'dusk'


def s2(f):
    c = estadio2('golden').copy()
    cu = wt(2, 'Cuca') - 3; at = wt(2, 'ataque') - 3
    nomes = [('NEYMAR', 'Neymar', '10', 2, 'topete'), ('COUTINHO', 'Coutinho', '11', 1, 'curto'),
             ('CEBOLINHA', 'Cebolinha', '7', 3, 'curto'), ('GABIGOL', 'Gabigol', '9', 2, 'raspado')]
    num(c, 'ATAQUE PESADO', 640, 720, f, at, 110, -3)
    put_placa(c, 'TÉCNICO: CUCA', SAN, 640, 880, f, cu, 44, 2)
    for i, (nome, w_, n_, sk, hs) in enumerate(nomes):
        k0 = wt(2, w_) - 3
        x = 200 + 280 * i
        if f >= k0 - 4:
            san(c, x, 2060, 600, f, 3 + i, num_=n_, hs=hs, arms='hang' if f < k0 + 6 else 'punho', expr='grin', skin=sk, look=0)
            put_placa(c, nome, SAN, x, 1380 - 100 * (i % 2), f, k0, 34, -3 + 3 * (i % 2))
    z = lerp(1.04, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .00015 * f)
    return c, (lerp(630, 650, smooth(f / 160)), 1420, z, 0), 'golden'


def s3(f):
    c = estadio2('dusk').copy()
    tr = wt(3, 'tres') - 3; re = wt(3, 'reagir') - 3
    san(c, 640, 2040, 840, f, 5, num_='10', hs='topete', arms='shrug' if f >= tr else 'cintura', expr='nervous' if f >= tr else 'stern')
    num(c, 'PRECISA REAGIR', 640, 720, f, re, 110, -3)
    num(c, '3 JOGOS SEM VENCER', 640, 880, f, tr, 76, 3)
    z = lerp(1.0, 1.1, easeOut(ramp(f, tr - 6, tr + 20))) * (1 + .0004 * f)
    k = kick(f, tr, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    re = wt(4, 'revanche') - 3; ze = wt(4, 'zero') - 3; kf = max(14, wt(4, 'Coritiba') - 6)
    gx, gy = put_gol2(c, x=760, estufa=pulse(f, kf + 9, 6))
    put_goleiro(c, f, GK, None, gx=780 + (60 if f > kf + 6 else 0), arms='up', expr='shock', skin=1)
    x = lerp(-200, 330, easeOut(ramp(f, 0, kf - 3)))
    if f < kf - 4: linhas_vel(c, x, 2030, 840, f)
    cfc(c, x, 2030, 840, f, 4, arms='run' if f < kf + 6 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
        kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='9')
    rb = raio_bola(840)
    bola_voo(c, f, kf, x + 840 * .13, 2030 - rb, gx + 90, gy, rb, raio_bola(300))
    if f < kf + 9: num(c, 'REVANCHE', 640, 720, f, re, 120, -3)
    else:
        explosao(c, 640, 740, f, kf + 9, 200)
        num(c, '1º TURNO', 640, 740, f, kf + 11, 110, -3)
    if f >= ze - 2:
        put_placa(c, 'CORITIBA 3 x 0 SANTOS', CFC, 640, 930, f, ze - 2, 50, 2)
    k = kick(f, kf + 9, .8) + kick(f, ze, .5)
    return c, (lerp(600, 680, smooth(f / 140)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    no = wt(5, 'nono') - 3; qu = wt(5, 'quarenta') - 3; li = wt(5, 'Libertadores') - 3
    tabela(c, [('6º', 'BAHIA', time_('BAHIA')[0], '53', False), ('9º', 'SANTOS', SAN, '47', True)], 640, 880, f, no)
    num(c, '47 PONTOS', 640, 720, f, qu, 120, -3)
    san(c, 640, 2040, 640, f, 5, num_='10', hs='topete', arms='point' if f >= li else 'cintura', expr='stern', look=0)
    num(c, 'ZONA DA LIBERTADORES', 640, 1250, f, li, 66, 2)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, qu, .5)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    de = wt(6, 'decimo') - 3; ci = wt(6, 'cinco') - 3; zo = wt(6, 'rebaixamento') - 3
    tabela(c, [('13º', 'CORITIBA', CFC, '42', True)], 640, 900, f, de)
    num(c, '13º LUGAR', 640, 720, f, de, 120, -3)
    cfc(c, 640, 2040, 640, f, 9, arms='cintura' if f < ci else 'shrug', expr='stern' if f < ci else 'nervous', look=0)
    num(c, '+5 DA ZONA', 640, 1150, f, ci, 100, 3)
    if f >= zo: foco(c, 640, 1650, 380, .4 * ramp(f, zo, zo + 6))
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0005 * f)
    k = kick(f, ci, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


def s7(f):
    c = estadio2('day').copy()
    se = wt(7, 'segunda') - 3; gr = wt(7, 'Gremio') - 3; mo = wt(7, 'Morumbis') - 3
    san(c, 320, 2040, 760, f, 3, arms='cintura', expr='stern', look=1, num_='10', hs='topete')
    put_placa(c, 'SANTOS', SAN, 320, 1220, f, 0, 40, -3)
    if f >= gr - 4:
        put_atleta(c, 960, 2040, 760, f, 7, cores=GRE, faixa=GRE_F, skin=1, hs='curto', hair='#3a2a1e', arms='cintura',
                   expr='stern', look=-1, flip=True, num_='9')
        put_placa(c, 'GRÊMIO', GRE, 960, 1220, f, gr, 40, 3)
    if f >= se: paste_c(c, calendario('23', 'NOV'), 640, 1000, .45 * back(ramp(f, se, se + 8)))
    num(c, 'SEGUNDA 21H', 640, 720, f, se, 110, -3)
    num(c, 'MORUMBIS', 640, 1500, f, mo, 80, 2)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    k = kick(f, gr, .6)
    return c, (640, 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('NEYMAR DE VOLTA', 'CUMPRIU SUSPENSÃO', wt(0, 'suspensao') + 6),
         1: ('CORITIBA x SANTOS', 'HOJE, 19H30, COUTO PEREIRA', wt(1, 'Pereira') + 4),
         2: ('O ATAQUE DO CUCA', 'NEYMAR, COUTINHO, CEBOLINHA E GABIGOL', wt(2, 'Gabigol') + 6),
         3: ('SANTOS EM JEJUM', '3 JOGOS SEM VENCER', wt(3, 'Brasileirao') + 2),
         4: ('1º TURNO: CORITIBA 3 x 0', 'SANTOS QUER REVANCHE', wt(4, 'zero') + 8),
         5: ('SANTOS 9º, 47 PONTOS', 'DE OLHO NA LIBERTADORES', wt(5, 'Libertadores') + 4),
         6: ('CORITIBA 13º, 42 PONTOS', '5 ACIMA DA ZONA', wt(6, 'rebaixamento') + 4)}
    if si == 7: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'Neymar') - 3, 150, .8)
    s.ting(s.W(0, 'volta') - 3, .35)
    s.thunk(s.W(1, 'Coritiba') - 3, 160, .6)
    s.ting(s.W(1, 'sete') - 3, .3)
    for w in ('Neymar', 'Coutinho', 'Cebolinha', 'Gabigol'):
        s.thunk(s.W(2, w) - 3, 180, .45)
    s.thunk(s.W(3, 'tres') - 3, 120, .9)
    s.whoosh(s.W(4, 'revanche') - 4, .5)
    s.thunk(s.W(4, 'zero') - 3, 140, .8)
    s.thunk(s.W(5, 'nono') - 3, 150, .6)
    s.thunk(s.W(6, 'decimo') - 3, 150, .6)
    s.thunk(s.W(7, 'Gremio') - 3, 140, .6)
    s.ting(s.W(7, 'Morumbis') - 3, .35)
