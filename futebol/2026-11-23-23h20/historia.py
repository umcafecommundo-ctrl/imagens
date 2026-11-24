"""anima.futebol — 23/11/2026 23h20 — QUEM CAI? · EP. 6 — Santos 0x2 Grêmio no Morumbis (36ª rodada).
Fontes (conferidas em 23/11/2026, ver fatos.txt): Gazeta Esportiva (23:05), Leouve (23:05), FogãoNET (23:07), Lance!, ESPN.
Amuzu no 1º tempo, Braithwaite de pênalti no 2º; Grêmio 41 sai da zona; Corinthians 40 volta ao Z4;
domingo (29/11) Corinthians x Grêmio. Sem escudos/logos: times por plaquinhas e cores."""
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
    "O Grêmio escapou? Olha a conta.",
    "No Morumbis, Amuzu abriu o placar no primeiro tempo.",
    "No segundo tempo, Braithwaite de pênalti... dois a zero.",
    "O Grêmio chega a quarenta e um pontos e sai da zona.",
    "E o Corinthians, com quarenta, volta para a zona.",
    "Domingo tem Corinthians e Grêmio. O Grêmio escapa?",
]
CAPTXT = [
    "O Grêmio escapou?|Olha a conta.",
    "No Morumbis, Amuzu abriu|o placar no 1º tempo.",
    "No 2º tempo, Braithwaite|de pênalti... 2 a 0.",
    "O Grêmio chega a 41 pontos|e sai da zona.",
    "E o Corinthians, com 40,|volta para a zona.",
    "Domingo tem Corinthians e Grêmio.|O Grêmio escapa?",
]
FALA_TIKTOK = "O Grêmio escapa? Comenta sim ou não."
CTA_TEXTO = "GRÊMIO ESCAPA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [2]
CHECK = [(0, 'Grêmio', 4), (0, 'conta', 4), (1, 'Morumbis', 4), (1, 'Amuzu', 4), (1, 'placar', 4), (2, 'Braithwaite', 4),
         (2, 'pênalti', 4), (2, 'zero', 4), (3, 'quarenta', 4), (3, 'zona', 4), (4, 'Corinthians', 4), (4, 'quarenta', 4),
         (4, 'zona', 4), (5, 'Domingo', 4), (5, 'escapa', 4)]

GRE, GRE_F = time_('GRÊMIO')
SAN, SAN_F = time_('SANTOS')
COR_, COR_F = time_('CORINTHIANS')


def gre(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=GRE, faixa=GRE_F, **kw)


def san(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=SAN, faixa=SAN_F, **kw)


def cor(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=COR_, faixa=COR_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 38


def s0(f):
    """quadro 0 = capa: close do torcedor do Grêmio (azul) + série + pergunta; depois o jogador do Grêmio."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='sorriso', s=.9, roupa='#1e6fbf', pele='#e0a87e', cabelo='#3a2414')
        num(c, 'QUEM CAI?', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 6', 621, 440, f, 0, 100, 2)
        num(c, 'O GRÊMIO', 621, 1350, f, 0, 150, -2)
        num(c, 'ESCAPOU?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    co = wt(0, 'conta') - 3
    gre(c, 640, 2080, 860, f, 6, arms='up' if f >= co else 'hang', expr='grin' if f >= co else 'nervous', look=0, num_='10')
    if f < co - 2:
        put_placa(c, 'GRÊMIO', GRE, 640, 880, f, CLOSE_F, 90, -3)
    else:
        num(c, 'A CONTA', 640, 880, f, co, 150, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio à noite: Amuzu abre o placar."""
    c = estadio2('dusk').copy()
    mo = wt(1, 'Morumbis') - 3; am = wt(1, 'Amuzu') - 3; pl = wt(1, 'placar') - 3
    ks = pl - 12
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, SAN, SAN_F, arms='shrug' if f >= ks + 8 else 'hang', expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    san(c, 900, 1960, 700, f, 4, num_='4', arms='run', run=(f * .08) % 1 if f < ks else None,
        expr='shock' if f >= ks + 8 else 'stern', flip=True)
    sx = lerp(260, 430, easeOut(ramp(f, 0, ks - 4))); H = 860
    if f < ks - 4: linhas_vel(c, sx, 2010, H, f, dir=-1)
    gre(c, sx, 2010, H, f, 9, num_='7', arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 4 else None,
        kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 60, 10)
    if f < am - 2:
        num(c, 'MORUMBIS', 640, 860, f, mo, 120, -2)
    elif f < ks + 8:
        put_placa(c, 'AMUZU', GRE, 640, 860, f, am, 100, -2)
    else:
        explosao(c, 640, 860, f, ks + 8, 200)
        num(c, '1 x 0', 640, 860, f, ks + 8, 160, 3)
    k = kick(f, ks, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s2(f):
    """estádio de dia/golden: pênalti de Braithwaite no meio do gol, 2 x 0."""
    c = estadio2('golden').copy()
    br = wt(2, 'Braithwaite') - 3; pe = wt(2, 'pênalti') - 3; ze = wt(2, 'zero') - 3
    ks = pe + 4
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, SAN, SAN_F, arms='up' if f >= ks + 2 else 'hang', expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    H = 860; sx = 520
    gre(c, sx, 2010, H, f, 3, num_='9', skin=0, hs='careca' if False else 'curto', hair='#c9a06a',
        arms='up' if f >= ks + 10 else 'hang', kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 40, 9)
    if f < pe - 2:
        put_placa(c, 'BRAITHWAITE', GRE, 640, 860, f, br, 80, -2)
    elif f < ze - 2:
        num(c, 'PÊNALTI', 640, 860, f, pe, 140, 3)
    else:
        explosao(c, 640, 860, f, ze, 200)
        num(c, '2 x 0', 640, 860, f, ze, 170, -3)
    z = lerp(1.12, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, ks, .9)
    return c, (640 + 20 * math.sin(f * .04), 1440 + k * 10, z, k), 'golden'


def s3(f):
    """vestiário do Grêmio: 41 pontos, fora da zona."""
    c = vestiario(GRE, GRE_F).copy()
    qu = wt(3, 'quarenta') - 3; zo = wt(3, 'zona') - 3
    gre(c, 640, 2110, 860, f, 6, arms='up' if f >= qu else 'cintura', expr='grin', look=0, num_='10')
    if f < qu - 2:
        put_placa(c, 'GRÊMIO', GRE, 640, 1000, f, 0, 90, -2)
    elif f < zo - 2:
        numero_gigante(c, '41 PTS', 640, 1000, f, qu, 200, -3)
    else:
        num(c, 'FORA DO Z4', 640, 1000, f, zo, 120, 3)
    confete(c, 640, 600, f, zo, 50, 500)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, zo if f >= zo else qu, .7)
    return c, (640, 1400 + k * 10, z, k), 'golden'


def s4(f):
    """a conta: Corinthians 40, volta ao Z4."""
    c = conta_bg().copy()
    co = wt(4, 'Corinthians') - 3; qa = wt(4, 'quarenta') - 3; zo = wt(4, 'zona') - 3
    if f < qa - 2:
        num(c, 'CORINTHIANS', 640, 1000, f, co, 120, -2)
    elif f < zo - 2:
        numero_gigante(c, '40', 640, 1000, f, qa, 300, -3)
    else:
        numero_gigante(c, 'Z4', 640, 1000, f, zo, 300, 3)
    cor(c, 640, 2090, 760, f, 7, arms='cheek' if f >= zo else 'cintura', expr='pained' if f >= zo else 'stern', look=0, num_='9')
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, zo if f >= zo else (qa if f >= qa else co), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """prancheta: domingo Corinthians x Grêmio — o Grêmio escapa?"""
    c = prancheta().copy()
    do = wt(5, 'Domingo') - 3; es = wt(5, 'escapa') - 8
    cor(c, 330, 2090, 760, f, 7, arms='cintura', expr='stern', look=1, num_='9')
    gre(c, 950, 2090, 760, f, 6, arms='hang' if f < es else 'cheek', expr='nervous', look=-1, flip=True, num_='10')
    if f < es - 2:
        if f >= do: paste_c(c, calendario('29', 'NOV'), 640, 1050, 1.1 * back(ramp(f, do, do + 8)))
    else:
        num(c, 'ESCAPA?', 640, 1000, f, es, 170, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, es if f >= es else do, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'conta') - 3, 130, .7)
    s.apito(s.W(1, 'Morumbis') - 6)
    ks = s.W(1, 'placar') - 15
    s.chute(ks); s.rede(ks + 10); s.rugido(ks + 11, 2.0, .7)
    s.thunk(ks + 8, 150, .9)
    s.apito(s.W(2, 'pênalti') - 6)
    k2 = s.W(2, 'pênalti') + 1
    s.chute(k2); s.rede(k2 + 9); s.rugido(k2 + 10, 2.0, .7)
    s.thunk(s.W(2, 'zero') - 3, 160, 1.0)
    s.thunk(s.W(3, 'quarenta') - 3, 150, .9)
    s.thunk(s.W(3, 'zona') - 3, 150, .9)
    s.thunk(s.W(4, 'quarenta') - 3, 150, .9)
    s.thunk(s.W(4, 'zona') - 3, 150, .9)
    s.thunk(s.W(5, 'Domingo') - 3, 130, .8)
    s.ting(s.W(5, 'escapa') - 8, .35)
    s.thunk(s.W(5, 'escapa') - 8, 160, 1.0)
