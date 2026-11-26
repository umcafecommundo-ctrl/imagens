"""anima.futebol — 26/11/2026 19h15 — FIM DE JOGO · EP. 6 — Olympiacos 2x4 Milan no Pireu (Liga Europa, fase de liga, 5ª rodada).
Fontes (conferidas em 26/11/2026, ver fatos.txt): acmilan.com (match report), pianetamilan.it (cronaca), Championat, A Bola, Goal.com IT.
Maignan contra (31') e Jota Silva (49') fazem 2x0; Hutchinson desconta (56'), Cisse empata (63'), Pulisic vira (71') e
Diego Moreira fecha nos acréscimos (95'). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'LIGA EUROPA  ·  5ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "Dá pra virar um dois a zero fora de casa? Olha o Milan.",
    "Maignan fez contra, e Jota Silva ampliou... dois a zero.",
    "Aí, no segundo tempo, Hutchinson descontou... dois a um.",
    "Cisse empatou, e Pulisic virou o jogo.",
    "Nos acréscimos, Moreira fechou... quatro a dois.",
    "Quatro gols em trinta e nove minutos.",
]
CAPTXT = [
    "Dá pra virar um 2 a 0 fora|de casa? Olha o Milan.",
    "Maignan fez contra, e Jota Silva|ampliou... 2 a 0.",
    "Aí, no segundo tempo, Hutchinson|descontou... 2 a 1.",
    "Cisse empatou, e Pulisic|virou o jogo.",
    "Nos acréscimos, Moreira|fechou... 4 a 2.",
    "4 gols em 39 minutos.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "MILAN VAI LONGE?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 3
FLASH = [3]
CHECK = [(0, 'virar', 4), (0, 'Milan', 4), (1, 'Maignan', 4), (1, 'contra', 4), (1, 'Jota', 4), (1, 'ampliou', 4),
         (1, 'dois', 4), (2, 'Hutchinson', 4), (2, 'descontou', 4), (2, 'um', 4), (3, 'Cisse', 4), (3, 'empatou', 4),
         (3, 'Pulisic', 4), (3, 'virou', 4), (4, 'acrescimos', 4), (4, 'Moreira', 4), (4, 'quatro', 4),
         (5, 'Quatro', 4), (5, 'trinta', 4)]

MIL, MIL_F = time_('MILAN')
OLY, OLY_F = time_('OLYMPIACOS')
TORC = dict(roupa='#c8102e', pele='#e0ac85', cabelo='#3a2a1e')


def mil(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=MIL, faixa=MIL_F, **kw)


def oly(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=OLY, faixa=OLY_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def lance(c, f, ks, time_chute, gk_cores, seed, num_, H=860, sx0=300, sx1=500, skin=1, hair='#2a1a10'):
    """chute de longe + gol: bola vai para (gx+90, gy)."""
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, gk_cores, None, arms='up' if f >= ks + 2 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    sx = lerp(sx0, sx1, easeOut(ramp(f, 0, ks - 2)))
    if f < ks - 2: linhas_vel(c, sx, 2010, H, f, dir=-1)
    time_chute(c, sx, 2010, H, f, seed, num_=num_, skin=skin, hair=hair,
               arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 2 else None,
               kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 60, 9)
    if f >= ks + 12: confete(c, 500, 700, f, ks + 12, 40, 400)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor do Milan (camisa vermelha) + série + pergunta; depois o vestiário do Milan."""
    c = vestiario(MIL, MIL_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, **TORC)
        num(c, 'FIM DE JOGO', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 6', 621, 430, f, 0, 100, 2)
        num(c, 'DÁ PRA VIRAR', 621, 1350, f, 0, 125, -2)
        num(c, 'UM 2 x 0?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    mi = wt(0, 'Milan') - 3
    mil(c, 640, 2100, 860, f, 6, arms='cintura' if f < mi else 'point', expr='nervous' if f < mi else 'stern',
        look=1 if f < mi else 0, num_='10')
    if f < mi - 2:
        num(c, 'FORA DE CASA', 640, 1000, f, CLOSE_F, 120, -3)
    else:
        put_placa(c, 'MILAN', MIL, 640, 1000, f, mi, 120, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0008 * f) * (1 + .08 * pulse(f, mi, 10))
    k = kick(f, mi if f >= mi else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s1(f):
    """estádio à noite: gol contra de Maignan, depois Jota Silva faz 2 x 0."""
    c = estadio2('dusk').copy()
    ma = wt(1, 'Maignan') - 3; ja = wt(1, 'Jota') - 3; am = wt(1, 'ampliou') - 3; do = wt(1, 'dois') - 3
    ks = am - 8
    lance(c, f, ks, oly, ('#2d2d2d', '#2d2d2d', '#2d2d2d'), 4, '7', sx0=280, sx1=480)
    if f < ja - 2:
        put_placa(c, 'MAIGNAN', MIL, 640, 860, f, ma, 110, -2)
    elif f < do - 2:
        put_placa(c, 'JOTA SILVA', OLY, 640, 860, f, ja, 100, 2)
    else:
        explosao(c, 640, 860, f, do, 200)
        num(c, '2 x 0', 640, 860, f, do, 170, 3)
    k = kick(f, ks + 8 if f >= ks + 8 else ma, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0012 * f) * (1 + .08 * pulse(f, ma, 10)), k), 'dusk'


def s2(f):
    """estádio golden: Hutchinson arranca e chuta, 2 x 1."""
    c = estadio2('golden').copy()
    hu = wt(2, 'Hutchinson') - 3; de = wt(2, 'descontou') - 3; um = wt(2, 'um') - 3
    ks = de - 4
    lance(c, f, ks, mil, ('#f5c518', '#f5c518', '#f5c518'), 9, '7', sx0=900, sx1=560, skin=4, hair='#151010')
    if f < um - 2:
        put_placa(c, 'HUTCHINSON', MIL, 640, 860, f, hu, 96, -2)
    else:
        explosao(c, 640, 860, f, um, 200)
        num(c, '2 x 1', 640, 860, f, um, 170, -3)
    z = lerp(1.14, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ks + 8, 10))
    k = kick(f, ks + 8 if f >= ks + 8 else hu, .9)
    return c, (640 + 20 * math.sin(f * .04), 1440 + k * 10, z, k), 'golden'


def s3(f):
    """prancheta: Cisse empata e Pulisic vira, 2 x 3."""
    c = prancheta().copy()
    ci = wt(3, 'Cisse') - 3; em = wt(3, 'empatou') - 3; pu = wt(3, 'Pulisic') - 3; vr = wt(3, 'virou') - 3
    for i, (x, y) in enumerate(((520, 820), (700, 780), (880, 860))):
        pino(c, x, y + 10 * math.sin(f * .2 + i), OLY, f, 2 + i * 2, '', 70)
    pino(c, 1040, 620, MIL, f, 0, '', 60)
    pino(c, 470, 700 + 8 * math.sin(f * .2), MIL, f, ci, 'C', 90)
    pino(c, 760, 1000 + 8 * math.sin(f * .2 + 1), MIL, f, pu, 'P', 90)
    seta(c, (1030, 640), (490, 690), f, 2, 14, (255, 255, 255), 10)
    seta(c, (470, 700), (560, 570), f, em, 8, (255, 216, 74), 16)
    seta(c, (760, 1000), (640, 570), f, vr, 8, (255, 216, 74), 16)
    if f < em - 2:
        put_placa(c, 'CISSE', MIL, 640, 1320, f, ci, 110, -2)
    elif f < pu - 2:
        explosao(c, 640, 1320, f, em, 180)
        num(c, '2 x 2', 640, 1320, f, em, 170, 3)
    elif f < vr - 2:
        put_placa(c, 'PULISIC', MIL, 640, 1320, f, pu, 110, 2)
    else:
        explosao(c, 640, 1320, f, vr, 200)
        num(c, '2 x 3', 640, 1320, f, vr, 180, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .08 * pulse(f, em, 10)) * (1 + .1 * pulse(f, vr, 10))
    k = kick(f, vr if f >= vr else (em if f >= em else ci), .7)
    return c, (640 + 12 * math.sin(f * .06), 1150 + k * 8, z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s4(f):
    """telão: acréscimos, Moreira fecha, 2 x 4."""
    c = telao('dusk').copy()
    ac = wt(4, 'acrescimos') - 3; mo = wt(4, 'Moreira') - 3; qu = wt(4, 'quatro') - 3
    mil(c, 640, 2090, 820, f, 7, num_='11', skin=3, hs='curto', hair='#151010',
        arms='run' if f < mo else ('punho' if f < qu else 'up'), run=(f * .1) % 1 if f < mo else None,
        expr='stern' if f < mo else 'grin', look=0)
    if f < mo - 2:
        telao_txt(c, [('90+5', 230)], f, max(0, ac), y=700)
    elif f < qu - 2:
        telao_txt(c, [('MOREIRA', 170)], f, mo, y=720)
    else:
        telao_txt(c, [('2 x 4', 230)], f, qu, y=700)
    if f >= qu: confete(c, 640, 500, f, qu, 70, 600)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, qu, 10))
    k = kick(f, qu if f >= qu else mo, .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s5(f):
    """a conta: 4 gols em 39 minutos; fecha no close sorrindo do torcedor."""
    c = conta_bg().copy()
    q = wt(5, 'Quatro') - 3; tr = wt(5, 'trinta') - 3; fim = tr + 18
    mil(c, 640, 2090, 780, f, 6, num_='10', arms='up' if f >= tr else 'punho', expr='grin', look=0)
    if f < tr - 2:
        numero_gigante(c, '4 GOLS', 640, 1000, f, max(0, q), 230, 3)
    else:
        numero_gigante(c, '39 MIN', 640, 1000, f, tr, 230, -3)
    if f >= fim:
        c = put_close(c, f, expr='sorriso', look=-1 if f < fim + 12 else 0, s=.9, **TORC)
        num(c, 'VAI LONGE?', 621, 1450, f, fim, 160, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - fim)), 0), 'dusk'
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, tr, 10))
    k = kick(f, tr if f >= tr else max(0, q), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'Milan') - 3, 140, .9)
    s.apito(s.W(1, 'Maignan') - 6)
    s.thunk(s.W(1, 'Maignan') - 3, 140, .8)
    k1 = s.W(1, 'ampliou') - 8
    s.chute(k1); s.rede(k1 + 9); s.rugido(k1 + 10, 1.4, .5)
    s.thunk(s.W(1, 'dois') - 3, 160, 1.0)
    k2 = s.W(2, 'descontou') - 4
    s.chute(k2); s.rede(k2 + 9); s.rugido(k2 + 10, 1.4, .5)
    s.thunk(s.W(2, 'um') - 3, 150, .9)
    s.thunk(s.W(3, 'empatou') - 3, 160, 1.0)
    s.rugido(s.W(3, 'empatou') - 2, 1.2, .5)
    s.thunk(s.W(3, 'virou') - 3, 170, 1.0)
    s.rugido(s.W(3, 'virou') - 2, 1.5, .6)
    s.thunk(s.W(4, 'Moreira') - 3, 140, .8)
    s.thunk(s.W(4, 'quatro') - 3, 170, 1.0)
    s.apito(s.W(4, 'quatro') + 8, longo=True)
    s.thunk(s.W(5, 'Quatro') - 3, 150, .9)
    s.thunk(s.W(5, 'trinta') - 3, 160, 1.0)
    s.ting(s.W(5, 'trinta') + 15, .35)
