"""anima.futebol — 23/11/2026 08h30 — QUEM CAI? · EP. 4 — Athletico-PR 4x2 Remo na Arena da Baixada (36ª rodada): Remo rebaixado.
Fontes (conferidas em 23/11/2026, ver fatos.txt): Paraná Portal, VAVEL Brasil (22/11 23:53), GazetaWeb/Metrópoles (22/11 18:22),
Metrópoles (resultados de domingo), A Tarde/Flashscore (Chapecoense 1º rebaixado). 2x0 no 1º tempo, Remo desconta, 4x2 final;
Remo 19º com 32, 2º rebaixado; Corinthians (1º fora do Z4) com 40. Sem escudos/logos: times por plaquinhas e cores."""
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
    "O Remo caiu de vez? Olha a conta.",
    "Na Arena da Baixada, o Athletico fez dois a zero no primeiro tempo.",
    "O Remo descontou, o Athletico fez mais dois, e o placar final... quatro a dois.",
    "O Remo fica com trinta e dois pontos, em décimo nono.",
    "Mesmo ganhando os dois últimos jogos, chega a trinta e oito... e o Corinthians tem quarenta.",
    "Rebaixado. É o segundo, depois da Chapecoense. Quem cai junto?",
]
CAPTXT = [
    "O Remo caiu de vez?|Olha a conta.",
    "Na Arena da Baixada, o Athletico|fez 2 a 0 no primeiro tempo.",
    "O Remo descontou, o Athletico fez mais dois,|e o placar final... 4 a 2.",
    "O Remo fica com 32 pontos,|em 19º.",
    "Mesmo ganhando os 2 últimos jogos, chega a 38...|e o Corinthians tem 40.",
    "Rebaixado. É o segundo,|depois da Chapecoense. Quem cai junto?",
]
FALA_TIKTOK = "Quem cai junto com o Remo? Comenta o time."
CTA_TEXTO = "QUEM CAI JUNTO?"
CTA_PALAVRA = 'O TIME'
TWIST = 5
FLASH = [2]
CHECK = [(0, 'Remo', 4), (0, 'conta', 4), (1, 'Arena', 4), (1, 'zero', 4), (1, 'primeiro', 4), (2, 'descontou', 4),
         (2, 'dois', 4), (2, 'quatro', 4), (3, 'trinta', 4), (3, 'decimo', 4), (4, 'oito', 4), (4, 'Corinthians', 4),
         (4, 'quarenta', 4), (5, 'Rebaixado', 4), (5, 'Chapecoense', 4), (5, 'junto', 4)]

CAP, CAP_F = time_('ATHLETICO-PR')
REM, REM_F = time_('REMO')
COR_, COR_F = time_('CORINTHIANS')
CHA, CHA_F = time_('CHAPECOENSE')


def cap(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=CAP, faixa=CAP_F, **kw)


def rem(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=REM, faixa=REM_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 38


def s0(f):
    """quadro 0 = capa: close do torcedor do Remo (azul-marinho) + série + pergunta; depois o jogador do Remo."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, roupa='#0d2a5c', pele='#8a5a3c', cabelo='#151010')
        num(c, 'QUEM CAI?', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 4', 621, 440, f, 0, 100, 2)
        num(c, 'O REMO', 621, 1350, f, 0, 150, -2)
        num(c, 'CAIU?', 621, 1530, f, 0, 170, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    co = wt(0, 'conta') - 3
    rem(c, 640, 2080, 860, f, 6, arms='cheek' if f >= co else 'hang', expr='pained' if f >= co else 'nervous', look=0, num_='10')
    if f < co - 2:
        put_placa(c, 'REMO', REM, 640, 880, f, CLOSE_F, 90, -3)
    else:
        num(c, 'A CONTA', 640, 880, f, co, 150, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio de dia: gol do Athletico, 2 x 0 no 1º tempo."""
    c = estadio2('day').copy()
    ar = wt(1, 'Arena') - 3; ze = wt(1, 'zero') - 3; pr = wt(1, 'primeiro') - 3
    ks = ze - 14
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, REM, REM_F, arms='shrug' if f >= ks + 8 else 'hang', expr='shock' if f >= ks + 8 else 'nervous', skin=3)
    rem(c, 900, 1960, 700, f, 4, num_='4', arms='run', run=(f * .08) % 1 if f < ks else None, expr='shock' if f >= ks + 8 else 'stern', flip=True)
    sx = lerp(260, 430, easeOut(ramp(f, 0, ks - 4))); H = 860
    if f < ks - 4: linhas_vel(c, sx, 2010, H, f, dir=-1)
    cap(c, sx, 2010, H, f, 9, num_='9', arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 4 else None,
        kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern', skin=1)
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 120, 10)
    if f < ar - 2:
        put_placa(c, 'ATHLETICO', CAP, 640, 860, f, 0, 80, -2)
    elif f < ze - 2:
        num(c, 'ARENA DA BAIXADA', 640, 860, f, ar, 82, -2)
    elif f < pr - 2:
        explosao(c, 640, 860, f, ze, 200)
        num(c, '2 x 0', 640, 860, f, ze, 170, 3)
    else:
        num(c, '1º TEMPO', 640, 860, f, pr, 130, 3)
    k = kick(f, ks, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'day'


def s2(f):
    """telão: 2x1, mais dois, 4 x 2 final (um texto por vez)."""
    c = telao('day').copy()
    de = wt(2, 'descontou') - 3; do = wt(2, 'dois') - 3; qu = wt(2, 'quatro') - 3
    cap(c, 330, 2080, 680, f, 3, arms='up' if f >= do else 'cintura', expr='grin', look=1, num_='11')
    rem(c, 950, 2080, 680, f, 5, arms='cheek' if f >= qu else 'hang', expr='pained' if f >= qu else 'stern', look=-1, flip=True, num_='8')
    if f < do - 2:
        telao_txt(c, [('2 x 1', 200)], f, de, y=700)
    elif f < qu - 2:
        telao_txt(c, [('+2', 220)], f, do, y=700)
    else:
        telao_txt(c, [('4 x 2', 230)], f, qu, y=690)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, qu if f >= qu else (do if f >= do else de), .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'day'


def s3(f):
    """vestiário do Remo: 32 pontos, 19º."""
    c = vestiario(REM, REM_F).copy()
    tr = wt(3, 'trinta') - 3; de = wt(3, 'decimo') - 3
    rem(c, 640, 2110, 860, f, 6, arms='hang' if f < tr else 'cheek', expr='nervous' if f < tr else 'pained', look=0, num_='10')
    if f < de - 2:
        if f >= tr: numero_gigante(c, '32 PTS', 640, 1000, f, tr, 200, -3)
    else:
        tabela(c, [('19º', 'REMO', REM, '32', True)], 640, 1000, f, de)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, de if f >= de else tr, .7)
    return c, (640, 1400 + k * 10, z, k), 'golden'


def s4(f):
    """a conta: 32 + 6 = 38, e o Corinthians tem 40."""
    c = conta_bg().copy()
    oi = wt(4, 'oito') - 3; co = wt(4, 'Corinthians') - 3; qa = wt(4, 'quarenta') - 3
    if f < oi - 2:
        numero_gigante(c, '32 + 6', 640, 1000, f, 0, 230, -3)
    elif f < co - 2:
        numero_gigante(c, '38', 640, 1000, f, oi, 300, 3)
    elif f < qa - 2:
        put_placa(c, 'CORINTHIANS', COR_, 640, 1000, f, co, 84, -2)
    else:
        numero_gigante(c, '40', 640, 1000, f, qa, 300, -3)
    if f >= co:
        put_atleta(c, 640, 2090, 760, f, 7, cores=COR_, faixa=COR_F, skin=2, hs='curto', hair='#151010',
                   arms='cintura', expr='stern', look=0, num_='9')
    else:
        rem(c, 640, 2090, 760, f, 6, arms='cheek' if f >= oi else 'hang', expr='nervous', look=0, num_='10')
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, qa if f >= qa else (co if f >= co else oi), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """telão à noite: rebaixados (Chapecoense, Remo) e a pergunta."""
    c = telao('dusk').copy()
    rb = wt(5, 'Rebaixado') - 3; ch = wt(5, 'Chapecoense') - 3; ju = wt(5, 'junto') - 8
    rem(c, 640, 2090, 820, f, 6, arms='hang', expr='pained', look=0, num_='10')
    if f < ch - 2:
        telao_txt(c, [('REBAIXADO', 150)], f, rb, y=720)
    elif f < ju - 2:
        tabela(c, [('1º', 'CHAPECOENSE', CHA, 'B', False), ('2º', 'REMO', REM, 'B', True)], 640, 860, f, ch)
    else:
        telao_txt(c, [('QUEM CAI', 140), ('JUNTO?', 160)], f, ju, y=640)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ju if f >= ju else (ch if f >= ch else rb), .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'conta') - 3, 130, .7)
    s.apito(s.W(1, 'Arena') - 6)
    ks = s.W(1, 'zero') - 17
    s.chute(ks); s.rede(ks + 10); s.rugido(ks + 11, 2.0, .7)
    s.thunk(s.W(1, 'zero') - 3, 150, .9)
    s.thunk(s.W(1, 'primeiro') - 3, 120, .6)
    s.thunk(s.W(2, 'descontou') - 3, 130, .8)
    s.thunk(s.W(2, 'dois') - 3, 130, .8)
    s.apito(s.W(2, 'final') - 4, longo=True)
    s.thunk(s.W(2, 'quatro') - 3, 160, 1.0)
    s.thunk(s.W(3, 'trinta') - 3, 150, .9)
    s.thunk(s.W(3, 'decimo') - 3, 120, .7)
    s.thunk(s.W(4, 'oito') - 3, 150, .9)
    s.thunk(s.W(4, 'Corinthians') - 3, 120, .7)
    s.thunk(s.W(4, 'quarenta') - 3, 150, .9)
    s.ting(s.W(5, 'Rebaixado') - 3, .35)
    s.thunk(s.W(5, 'Rebaixado') - 3, 160, 1.0)
    s.thunk(s.W(5, 'Chapecoense') - 3, 130, .8)
    s.thunk(s.W(5, 'junto') - 8, 110, .9)
