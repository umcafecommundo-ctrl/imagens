"""anima.futebol — 22/11/2026 20h50 — CONTA DA VAGA · EP. 1 — Fluminense 1x0 Mirassol no Maracanã (36ª rodada).
Fontes (conferidas em 22/11/2026, ver fatos.txt): Metrópoles (22/11 20:32), Revista Placar (22/11 20:31), La Nación (22/11 20:29),
FogãoNET (22/11 20:31); pré-jogo Lance/O Tempo e Tupi (G4 = vaga direta). Gol de Riquelme nos acréscimos, no rebote de uma
cabeçada na trave; Fluminense 4º com 63 pontos; Mirassol 15º com 41; sexta (27/11) Fluminense x Cruzeiro.
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
    "O Fluminense fica no G4? Olha a conta.",
    "No Maracanã, contra o Mirassol, o zero a zero durou até os acréscimos.",
    "Aí a cabeçada bateu na trave, e Riquelme pegou o rebote... um a zero.",
    "Com a vitória, o Fluminense chega a sessenta e três pontos, em quarto.",
    "O Mirassol fica com quarenta e um, em décimo quinto.",
    "Sexta tem Fluminense e Cruzeiro. O Flu fica no G4?",
]
CAPTXT = [
    "O Fluminense fica no G4?|Olha a conta.",
    "No Maracanã, contra o Mirassol,|o 0 a 0 durou até os acréscimos.",
    "Aí a cabeçada bateu na trave,|e Riquelme pegou o rebote... 1 a 0.",
    "Com a vitória, o Fluminense chega|a 63 pontos, em 4º.",
    "O Mirassol fica com 41,|em 15º.",
    "Sexta tem Fluminense e Cruzeiro.|O Flu fica no G4?",
]
FALA_TIKTOK = "O Flu fica no G4? Comenta sim ou não."
CTA_TEXTO = "FICA NO G4?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 2
FLASH = [2]
CHECK = [(0, 'Fluminense', 4), (0, 'G4', 4), (0, 'conta', 4), (1, 'Maracana', 4), (1, 'Mirassol', 4), (1, 'zero', 4),
         (1, 'acrescimos', 4), (2, 'trave', 4), (2, 'Riquelme', 4), (2, 'um', 4), (3, 'sessenta', 4), (3, 'quarto', 4),
         (4, 'quarenta', 4), (4, 'decimo', 4), (5, 'Sexta', 4), (5, 'Cruzeiro', 4), (5, 'G4', 4)]

FLU_, FLU_F = time_('FLUMINENSE')
MIR, MIR_F = time_('MIRASSOL')
CRU_, CRU_F = time_('CRUZEIRO')


def flu(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=FLU_, faixa=FLU_F, **kw)


def mir(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=MIR, faixa=MIR_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10, rastro_=True):
    """bola de (x0,y0) a (x1,y1) entre k0 e k0+dur; devolve True quando chegou."""
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if rastro_ and 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)
    return t >= 1


CLOSE_F = 38   # ~1,3 s de close de abertura


def s0(f):
    """quadro 0 = capa: close do torcedor do Fluminense (grená) + série + pergunta; depois o jogador do Flu."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='preocupado', s=.9, roupa='#7a1f3d', pele='#b07a55', cabelo='#151010')
        num(c, 'CONTA DA VAGA', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 1', 621, 430, f, 0, 100, 2)
        num(c, 'O FLU FICA', 621, 1350, f, 0, 135, -2)
        num(c, 'NO G4?', 621, 1520, f, 0, 160, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    co = wt(0, 'conta') - 3
    flu(c, 640, 2080, 860, f, 6, arms='cintura', expr='stern' if f < co else 'grin', look=0, num_='10')
    if f < co - 2:
        num(c, 'FLU x MIRASSOL', 640, 880, f, CLOSE_F, 92, -3)
    else:
        num(c, 'A CONTA', 640, 880, f, co, 150, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """telão à noite: 0 x 0 até os acréscimos (um texto por vez)."""
    c = telao('dusk').copy()
    ze = wt(1, 'zero') - 3; ac = wt(1, 'acrescimos') - 3; mi = wt(1, 'Mirassol') - 3
    flu(c, 330, 2080, 680, f, 3, arms='cheek' if f >= ac else 'hang', expr='nervous', look=1, num_='9')
    mir(c, 950, 2080, 680, f, 5, arms='cintura', expr='stern', look=-1, flip=True, num_='8')
    if f < mi - 2:
        num(c, 'MARACANÃ', 640, 880, f, 0, 130, -2)
    elif f < ze - 2:
        put_placa(c, 'MIRASSOL', MIR, 640, 860, f, mi, 80, 2)
    elif f < ac - 2:
        numero_gigante(c, '0 x 0', 640, 900, f, ze, 220, -3)
    else:
        num(c, 'ACRÉSCIMOS', 640, 900, f, ac, 130, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, ze if f < ac else ac, .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """estádio à noite: cabeçada na trave, Riquelme no rebote, gol no fundo."""
    c = estadio2('dusk').copy()
    tr = wt(2, 'trave') - 3; ri = wt(2, 'Riquelme') - 3; um = wt(2, 'um') - 3
    kh = tr - 8           # cabeçada
    ks = ri + 6           # chute do Riquelme
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, MIR, MIR_F, arms='shrug' if f >= ks + 8 else 'hang', expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    # quem cabeceia (camisa 9), atrás, à direita
    H2 = 700; hx = 900
    pulo = 60 * pulse(f, kh - 6, 12)
    flu(c, hx, 1960 - pulo, H2, f, 4, num_='9', arms='up' if f < kh + 30 else 'cheek', expr='stern', flip=True, skin=4)
    # Riquelme, na frente
    sx = lerp(260, 430, easeOut(ramp(f, 0, ks - 4))); H = 860
    if f < ks - 4: linhas_vel(c, sx, 2010, H, f, dir=-1)
    flu(c, sx, 2010, H, f, 9, num_='37', arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 4 else None,
        kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern', skin=3)
    rb = raio_bola(H); rh = raio_bola(H2)
    tx, ty = gx - 170, gy - 20     # trave esquerda
    hy = 1960 - pulo - H2 * .92
    if f < kh:
        voo(c, f, kh - 14, 1400, 1300, hx - 10, hy, rh * .9, rh, 60, 14)
    elif f < tr + 2:
        voo(c, f, kh, hx - 10, hy, tx, ty, rh, raio_bola(300), 30, 10)
    elif f < ks:
        voo(c, f, tr + 2, tx, ty, sx + H * .13, 2010 - rb, raio_bola(300), rb, 140, max(4, ks - tr - 2))
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 120, 10)
    if f >= um:
        explosao(c, 640, 860, f, um, 200)
        num(c, '1 x 0', 640, 860, f, um, 170, 3)
    elif f >= ri:
        put_placa(c, 'RIQUELME', FLU_, 640, 800, f, ri, 76, -3)
    elif f >= tr:
        num(c, 'NA TRAVE!', 640, 820, f, tr, 120, -3)
    k = kick(f, ks, .9) + .6 * kick(f, tr, .5)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s3(f):
    """telão de dia: Fluminense 4º com 63."""
    c = telao('day').copy()
    se = wt(3, 'sessenta') - 3; qu = wt(3, 'quarto') - 3
    flu(c, 640, 2090, 820, f, 6, arms='up' if f >= se else 'cintura', expr='grin' if f >= se else 'stern', look=0, num_='10')
    if f < se - 2:
        num(c, 'VITÓRIA', 640, 900, f, 0, 140, -3)
    else:
        tabela(c, [('4º', 'FLUMINENSE', FLU_, '63', True)], 640, 900, f, se)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, qu if f >= qu else se, .6)
    return c, (640 + 30 * math.sin(f * .05), 1380 + k * 8, z, k), 'day'


def s4(f):
    """vestiário do Mirassol: 41 pontos, 15º."""
    c = vestiario(MIR, MIR_F).copy()
    qu = wt(4, 'quarenta') - 3; de = wt(4, 'decimo') - 3
    mir(c, 640, 2110, 860, f, 6, arms='hang' if f < qu else 'cheek', expr='nervous' if f < qu else 'pained', look=0, num_='10')
    if f < de - 2:
        if f >= qu: numero_gigante(c, '41 PTS', 640, 1000, f, qu, 200, -3)
    else:
        tabela(c, [('15º', 'MIRASSOL', MIR, '41', False)], 640, 1000, f, de)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, de if f >= de else qu, .7)
    return c, (640, 1400 + k * 10, z, k), 'golden'


def s5(f):
    """estádio de dia: sexta Fluminense x Cruzeiro e a pergunta."""
    c = estadio2('day').copy()
    sx = wt(5, 'Sexta') - 3; cr = wt(5, 'Cruzeiro') - 3; g4 = wt(5, 'G4') - 8
    flu(c, 340, 2010, 820, f, 3, arms='cintura', expr='stern', look=1, num_='10')
    put_atleta(c, 940, 2010, 820, f, 7, cores=CRU_, faixa=CRU_F, skin=1, hs='curto', hair='#3a2a1e',
               arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    if f < cr - 2:
        paste_c(c, calendario('27', 'NOV'), 640, 960, .95 * back(ramp(f, sx, sx + 8)))
    elif f < g4 - 2:
        num(c, 'FLU x CRUZEIRO', 640, 880, f, cr, 100, -3)
    else:
        num(c, 'FICA NO G4?', 640, 880, f, g4, 140, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, cr if f < g4 else g4, .6)
    return c, (640, 1400 + k * 8, z, k), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'conta') - 3, 130, .7)
    s.apito(s.W(1, 'Maracana') - 4)
    s.thunk(s.W(1, 'Mirassol') - 3, 120, .6)
    s.thunk(s.W(1, 'zero') - 3, 150, .8)
    s.thunk(s.W(1, 'acrescimos') - 3, 130, .8)
    s.chute(s.W(2, 'trave') - 11)
    s.thunk(s.W(2, 'trave') - 3, 160, 1.0)
    s.chute(s.W(2, 'Riquelme') + 3); s.rede(s.W(2, 'Riquelme') + 14); s.rugido(s.W(2, 'Riquelme') + 15, 2.2, .7)
    s.thunk(s.W(2, 'um') - 3, 120, 1.0)
    s.ting(s.W(2, 'um') - 3, .35)
    s.apito(s.W(3, 'vitoria') - 4, longo=True)
    s.thunk(s.W(3, 'sessenta') - 3, 150, .9)
    s.thunk(s.W(3, 'quarto') - 3, 120, .7)
    s.thunk(s.W(4, 'quarenta') - 3, 150, .8)
    s.thunk(s.W(4, 'decimo') - 3, 120, .8)
    s.thunk(s.W(5, 'Sexta') - 3, 130, .7)
    s.thunk(s.W(5, 'Cruzeiro') - 3, 130, .7)
    s.thunk(s.W(5, 'G4') - 8, 110, .9)
