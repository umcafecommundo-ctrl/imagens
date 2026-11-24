"""anima.futebol — 24/11/2026 20h45 — FIM DE JOGO · EP. 4 — Chapecoense 3x0 Palmeiras na Arena Condá (Brasileirão, 37ª).
Fontes (conferidas em 24/11/2026, ver fatos.txt): PTD/verdao.net (pós-jogo 3x0), VAVEL (3-0), Diário 24 Horas (3x0), ESPN Brasil e Lance! (Camilo e Max no 1º tempo),
TV Sim Brasil (reservas, Palmeiras 2º com 74, final x Estudiantes sábado em Montevidéu), Diário 24 Horas.
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  37ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "Poupar foi erro? A lanterna bateu o Palmeiras.",
    "Na Arena Condá, Camilo abriu o placar logo no começo.",
    "Max ampliou, e no fim veio o terceiro... três a zero.",
    "Abel poupou os titulares e escalou três garotos do sub-20.",
    "Sábado tem a final da Libertadores... contra o Estudiantes.",
    "Com a final chegando... poupar foi certo?",
]
CAPTXT = [
    "Poupar foi erro?|A lanterna bateu o Palmeiras.",
    "Na Arena Condá, Camilo abriu|o placar logo no começo.",
    "Max ampliou, e no fim veio|o terceiro... 3 a 0.",
    "Abel poupou os titulares e|escalou 3 garotos do sub-20.",
    "Sábado tem a final da Libertadores...|contra o Estudiantes.",
    "Com a final chegando... poupar foi certo?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "POUPAR CERTO?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [2]
CHECK = [(0, 'Poupar', 4), (0, 'lanterna', 4), (0, 'Palmeiras', 4), (1, 'Conda', 4), (1, 'Camilo', 4), (1, 'comeco', 4),
         (2, 'Max', 4), (2, 'ampliou', 4), (2, 'terceiro', 4), (2, 'tres', 4), (3, 'Abel', 4), (3, 'titulares', 4), (3, 'sub-20', 4),
         (4, 'Sabado', 4), (4, 'Libertadores', 4), (4, 'Estudiantes', 4), (5, 'certo', 4)]

PAL, PAL_F = time_('PALMEIRAS')
CHA, CHA_F = time_('CHAPECOENSE')
EST, EST_F = time_('ESTUDIANTES')
VERDE = '#1b6b3a'


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def cha(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=CHA, faixa=CHA_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor do Palmeiras (camisa verde) + série + pergunta; depois a Chape comemora no estádio."""
    if f < CLOSE_F:
        c = vestiario(PAL, PAL_F).copy()
        c = put_close(c, f, expr='preocupado', s=.9, roupa=VERDE, pele='#e0ac85', cabelo='#2a1a10', look=0)
        num(c, 'FIM DE JOGO', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 4', 621, 430, f, 0, 100, 2)
        num(c, 'POUPAR', 621, 1350, f, 0, 150, -2)
        num(c, 'FOI ERRO?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    c = estadio2('day').copy()
    la = wt(0, 'lanterna') - 3; pa = wt(0, 'Palmeiras') - 3
    cha(c, 470, 2060, 860, f, 6, num_='10', arms='up' if f >= la else 'punho', expr='grin', look=0)
    pal(c, 940, 1990, 640, f, 3, num_='5', arms='hang' if f < pa else 'cintura', expr='stern' if f < pa else 'shock',
        flip=True)
    if f >= la: confete(c, 470, 700, f, la, 50, 500)
    if f < la - 2:
        put_placa(c, 'CHAPECOENSE', CHA, 640, 900, f, CLOSE_F, 90, -3)
    else:
        num(c, 'LANTERNA', 640, 900, f, la, 150, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, la, 10))
    k = kick(f, la if f >= la else CLOSE_F, .7)
    return c, (640, 1420 + k * 10, z, k), 'day'


def s1(f):
    """estádio à noite: Camilo em velocidade, chute, gol: 1 x 0."""
    c = estadio2('dusk').copy()
    ar = wt(1, 'Conda') - 3; ca = wt(1, 'Camilo') - 3; ab = wt(1, 'abriu') - 3; ci = wt(1, 'comeco') - 3
    ks = ab + 2
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, ('#2d2d2d', '#2d2d2d', '#2d2d2d'), None, arms='up' if f >= ks + 2 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    H = 860
    sx = lerp(260, 500, easeOut(ramp(f, 0, ks - 2)))
    if f < ks - 3: linhas_vel(c, sx, 2010, H, f, dir=-1)
    cha(c, sx, 2010, H, f, 8, num_='27', skin=1, hair='#3a2414', arms='up' if f >= ks + 10 else 'run',
        run=(f * .1) % 1 if f < ks - 3 else None, kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 40, 9)
    if f < ca - 2:
        num(c, 'ARENA CONDÁ', 640, 860, f, ar, 110, -2)
    elif f < ks + 8:
        put_placa(c, 'CAMILO', CHA, 640, 860, f, ca, 100, -2)
    else:
        explosao(c, 640, 860, f, ks + 8, 200)
        num(c, '1 x 0', 640, 860, f, ks + 8, 170, 3)
    k = kick(f, ks, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0012 * f) * (1 + .1 * pulse(f, ci, 10)), k), 'dusk'


def s2(f):
    """telão: Max amplia, 2 x 0, Chape comemora na frente."""
    c = telao('dusk').copy()
    mx = wt(2, 'Max') - 3; am = wt(2, 'ampliou') - 3; te = wt(2, 'terceiro') - 3; do = wt(2, 'tres') - 3
    cha(c, 640, 2090, 820, f, 7, num_='22', skin=3, hair='#151010',
        arms='run' if f < am else ('punho' if f < te else 'up'), run=(f * .1) % 1 if f < am else None,
        expr='stern' if f < am else 'grin', look=0)
    if f < am + 6:
        telao_txt(c, [('MAX', 200)], f, mx, y=720)
    elif f < do - 2:
        telao_txt(c, [('2 x 0', 200)], f, am + 6, y=720)
    else:
        telao_txt(c, [('3 x 0', 230)], f, do, y=700)
    if f >= do: confete(c, 640, 500, f, do, 70, 600)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, do, 10))
    k = kick(f, do if f >= do else mx, .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s3(f):
    """prancheta: titulares saem, garotos do sub-20 entram."""
    c = prancheta().copy()
    ab = wt(3, 'Abel') - 3; ti = wt(3, 'titulares') - 3; ga = wt(3, 'garotos') - 3; sb = wt(3, 'sub-20') - 3
    xs = (330, 620, 910)
    for i, x in enumerate(xs):
        if f < ti + 6:
            y = 1250 + 10 * math.sin(f * .2 + i) + (0 if f < ti else 900 * (ramp(f, ti, ti + 6) ** 2))
            pino(c, x, y, PAL, f, 2 + i * 2, '', 80)
    for i, x in enumerate(xs):
        if f >= ga - 4 + i * 3:
            pino(c, x, 1450 + 10 * math.sin(f * .2 + i), PAL, f, ga - 4 + i * 3, '', 80)
    if f < ti - 2:
        put_placa(c, 'ABEL', PAL, 640, 820, f, ab, 100, -2)
    elif f < sb - 2:
        num(c, 'POUPOU', 640, 820, f, ti, 150, 3)
    else:
        num(c, 'SUB-20', 640, 820, f, sb, 170, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, sb, 10))
    k = kick(f, sb if f >= sb else ti, .7)
    return c, (640 + 12 * math.sin(f * .06), 1330 + k * 8, z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s4(f):
    """vestiário do Palmeiras: taça genérica, calendário de sábado, placa do Estudiantes."""
    c = vestiario(PAL, PAL_F).copy()
    sa = wt(4, 'Sabado') - 3; li = wt(4, 'Libertadores') - 3; es = wt(4, 'Estudiantes') - 3
    tk = back(ramp(f, li, li + 8))
    if tk > .03: paste_c(c, trofeu(), 330, 1500, .7 * tk)
    pal(c, 760, 2080, 820, f, 9, num_='7', skin=1, hair='#2a1a10',
        arms='cintura' if f < li else ('point' if f < es else 'up'),
        expr='stern' if f < li else ('grin' if f < es else 'stern'), look=0 if f < es else 1)
    if f < li - 2:
        if f >= sa: paste_c(c, calendario('28', 'NOV'), 640, 900, .55 * back(ramp(f, sa, sa + 8)))
    elif f < es - 2:
        num(c, 'FINAL', 640, 880, f, li, 160, 3)
    else:
        put_placa(c, 'ESTUDIANTES', EST, 640, 880, f, es, 90, -2)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .08 * pulse(f, li, 10))
    k = kick(f, li if f >= li else sa, .7)
    return c, (640 + 25 * math.sin(f * .05), 1400 + k * 8, z, k), 'dusk'


def s5(f):
    """close do torcedor de novo, agora desconfiado: poupar foi certo?"""
    c = estadio2('golden').copy()
    ce = wt(5, 'certo') - 3
    c = put_close(c, f, expr='curioso' if f < ce else 'desconfiado', s=.9, roupa=VERDE, pele='#e0ac85',
                  cabelo='#2a1a10', look=-1 if f < ce else 0)
    z = (1.04 + .002 * f) * (1 + .08 * pulse(f, ce, 10))
    return c, (621, 1104, z, kick(f, ce, .5)), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'lanterna') - 3, 140, .9)
    s.rugido(s.W(0, 'lanterna') - 2, 1.2, .5)
    s.apito(s.W(1, 'Conda') - 6)
    k1 = s.W(1, 'abriu') - 1
    s.chute(k1); s.rede(k1 + 9); s.rugido(k1 + 10, 1.5, .6)
    s.thunk(k1 + 8, 150, .9)
    s.thunk(s.W(2, 'Max') - 3, 140, .8)
    s.thunk(s.W(2, 'ampliou') + 3, 150, .9)
    s.thunk(s.W(2, 'terceiro') - 3, 150, .9)
    s.rugido(s.W(2, 'terceiro') - 2, 1.2, .5)
    s.thunk(s.W(2, 'tres') - 3, 170, 1.0)
    s.apito(s.W(2, 'tres') + 6, longo=True)
    s.thunk(s.W(3, 'titulares') - 3, 140, .8)
    s.thunk(s.W(3, 'sub-20') - 3, 160, 1.0)
    s.thunk(s.W(4, 'Sabado') - 3, 140, .8)
    s.thunk(s.W(4, 'Libertadores') - 3, 160, .9)
    s.thunk(s.W(4, 'Estudiantes') - 3, 150, .9)
    s.ting(s.W(5, 'certo') - 3, .35)
