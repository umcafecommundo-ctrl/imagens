"""anima.futebol — 24/11/2026 19h15 — FIM DE JOGO · EP. 3 — Real Madrid 5x1 PSV no Bernabéu (Champions, fase de liga, 5ª rodada).
Fontes (conferidas em 24/11/2026, ver fatos.txt): ESPN (placar final), Foot Mercato, SDP Noticias, Bola na Rede, VAVEL, Diário 24 Horas.
Perisic de pênalti (PSV 1x0 no intervalo); Valverde empata, Bellingham vira, Mbappé faz dois, Vinícius Júnior fecha 5x1;
Real com 15 pontos, 5 vitórias em 5 jogos. Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'CHAMPIONS  ·  5ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Real é o favorito da Champions? Olha essa virada.",
    "No Bernabéu, o PSV saiu na frente com Perisic, de pênalti.",
    "No segundo tempo, Valverde empatou... e Bellingham virou.",
    "Depois, Mbappé fez dois.",
    "E Vinícius Júnior fechou a goleada... cinco a um.",
    "Cinco jogos, cinco vitórias... quinze pontos. É favorito?",
]
CAPTXT = [
    "O Real é o favorito da Champions?|Olha essa virada.",
    "No Bernabéu, o PSV saiu na frente|com Perisic, de pênalti.",
    "No 2º tempo, Valverde empatou...|e Bellingham virou.",
    "Depois, Mbappé fez dois.",
    "E Vinícius Júnior fechou|a goleada... 5 a 1.",
    "5 jogos, 5 vitórias... 15 pontos.|É favorito?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "REAL FAVORITO?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [2]
CHECK = [(0, 'Real', 4), (0, 'virada', 4), (1, 'Bernabeu', 4), (1, 'Perisic', 4), (1, 'penalti', 4), (2, 'Valverde', 4),
         (2, 'empatou', 4), (2, 'Bellingham', 4), (2, 'virou', 4), (3, 'Mbappe', 4), (3, 'dois', 4), (4, 'Vinicius', 4),
         (4, 'cinco', 4), (5, 'vitorias', 4), (5, 'quinze', 4), (5, 'favorito', 4)]

REA, REA_F = time_('REAL MADRID')
PSV, PSV_F = time_('PSV')


def rea(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=REA, faixa=REA_F, **kw)


def psv(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PSV, faixa=PSV_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor do Real (camisa branca) + série + pergunta; depois o vestiário do Real."""
    c = vestiario(REA, REA_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, roupa='#f4f4f4', pele='#e0ac85', cabelo='#3a2a1e')
        num(c, 'FIM DE JOGO', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 3', 621, 430, f, 0, 100, 2)
        num(c, 'REAL É', 621, 1350, f, 0, 150, -2)
        num(c, 'FAVORITO?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    vi = wt(0, 'virada') - 3
    rea(c, 640, 2100, 860, f, 6, arms='up' if f >= vi else 'point', expr='grin' if f >= vi else 'stern', look=0, num_='10')
    if f < vi - 2:
        put_placa(c, 'REAL MADRID', REA, 640, 1000, f, CLOSE_F, 90, -3)
    else:
        num(c, 'VIRADA', 640, 1000, f, vi, 170, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0008 * f)
    k = kick(f, vi if f >= vi else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s1(f):
    """estádio à noite: pênalti de Perisic, PSV 1 x 0."""
    c = estadio2('dusk').copy()
    be = wt(1, 'Bernabeu') - 3; pe_ = wt(1, 'Perisic') - 3; pn = wt(1, 'penalti') - 3
    ks = pn + 2
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, ('#2d2d2d', '#2d2d2d', '#2d2d2d'), None, arms='up' if f >= ks + 2 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    H = 860; sx = 520
    psv(c, sx, 2010, H, f, 4, num_='14', arms='up' if f >= ks + 10 else 'hang', kick=pulse(f, ks - 3, 5),
        expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 40, 9)
    if f < pe_ - 2:
        num(c, 'BERNABÉU', 640, 860, f, be, 120, -2)
    elif f < ks + 8:
        put_placa(c, 'PERISIC', PSV, 640, 860, f, pe_, 100, -2)
    else:
        explosao(c, 640, 860, f, ks + 8, 200)
        num(c, '0 x 1', 640, 860, f, ks + 8, 170, 3)
    k = kick(f, ks, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0008 * f), k), 'dusk'


def s2(f):
    """estádio golden: Valverde empata (gol), Bellingham comemora a virada 2 x 1."""
    c = estadio2('golden').copy()
    va = wt(2, 'Valverde') - 3; em = wt(2, 'empatou') - 3; bl = wt(2, 'Bellingham') - 3; vr = wt(2, 'virou') - 3
    ks = em - 8
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, ('#f5c518', '#f5c518', '#f5c518'), None, arms='shrug' if f >= ks + 8 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    psv(c, 920, 1960, 700, f, 5, num_='4', arms='run', run=(f * .08) % 1 if f < ks else None,
        expr='shock' if f >= ks + 8 else 'stern', flip=True)
    H = 860
    if f < bl:
        sx = lerp(260, 430, easeOut(ramp(f, 0, ks - 4)))
        if f < ks - 4: linhas_vel(c, sx, 2010, H, f, dir=-1)
        rea(c, sx, 2010, H, f, 9, num_='8', skin=1, hair='#3a2414', arms='up' if f >= ks + 10 else 'run',
            run=(f * .1) % 1 if f < ks - 4 else None, kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
        rb = raio_bola(H)
        if f < ks:
            put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
        elif f < ks + 40:
            voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 60, 10)
    else:
        rea(c, 470, 2010, H, f, 3, num_='5', skin=2, hair='#151010', arms='up' if f >= vr else 'punho',
            expr='grin', look=0)
        if f >= vr: confete(c, 640, 600, f, vr, 50, 500)
    if f < em - 2:
        put_placa(c, 'VALVERDE', REA, 640, 860, f, va, 90, -2)
    elif f < bl - 2:
        num(c, '1 x 1', 640, 860, f, em, 170, 3)
    elif f < vr - 2:
        put_placa(c, 'BELLINGHAM', REA, 640, 860, f, bl, 84, -2)
    else:
        explosao(c, 640, 860, f, vr, 200)
        num(c, '2 x 1', 640, 860, f, vr, 170, -3)
    z = lerp(1.12, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f) * (1 + .1 * pulse(f, vr, 10))
    k = kick(f, vr if f >= vr else ks, .9)
    return c, (640 + 20 * math.sin(f * .04), 1440 + k * 10, z, k), 'golden'


def s3(f):
    """prancheta: os dois gols de Mbappé desenhados com setas."""
    c = prancheta().copy()
    mb = wt(3, 'Mbappe') - 3; do = wt(3, 'dois') - 3
    for i, x in enumerate((330, 620, 910)):
        pino(c, x, 1150 + 12 * math.sin(f * .2 + i), PSV, f, 2 + i * 2, '', 70)
    pino(c, 400, 1700 + 10 * math.sin(f * .2), REA, f, mb, '10', 90)
    seta(c, (400, 1600), (560, 960), f, mb + 2, 10, (255, 216, 74), 14)
    if f >= do:
        pino(c, 860, 1700 + 10 * math.sin(f * .2 + 1), REA, f, do, '10', 90)
        seta(c, (860, 1600), (700, 960), f, do + 2, 10, (255, 216, 74), 14)
    if f < do - 2:
        put_placa(c, 'MBAPPÉ', REA, 640, 800, f, mb, 100, -2)
    else:
        num(c, '2 GOLS', 640, 800, f, do, 150, 3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, do if f >= do else mb, .7)
    return c, (640 + 12 * math.sin(f * .06), 1330 + k * 8, z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s4(f):
    """telão: Vinícius Júnior comemora, 5 x 1."""
    c = telao('dusk').copy()
    vn = wt(4, 'Vinicius') - 3; go = wt(4, 'goleada') - 3; ci = wt(4, 'cinco') - 3
    rea(c, 640, 2090, 820, f, 7, num_='7', skin=4, hs='curto', hair='#151010',
        arms='run' if f < go else ('punho' if f < ci else 'up'), run=(f * .1) % 1 if f < go else None,
        expr='stern' if f < vn + 10 else 'grin', look=0)
    if f < ci - 2:
        if f >= vn: telao_txt(c, [('VINI JR.', 170)], f, vn, y=720)
        else: telao_txt(c, [('4 x 1', 170)], f, 0, y=720)
    else:
        telao_txt(c, [('5 x 1', 230)], f, ci, y=700)
    if f >= ci: confete(c, 640, 500, f, ci, 70, 600)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ci, 10))
    k = kick(f, ci if f >= ci else vn, .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s5(f):
    """a conta: 5 em 5, 15 pontos — é favorito?"""
    c = conta_bg().copy()
    vt = wt(5, 'vitorias') - 3; qz = wt(5, 'quinze') - 3; fa = wt(5, 'favorito') - 8
    rea(c, 640, 2090, 780, f, 6, num_='10', arms='cintura' if f < qz else ('up' if f < fa else 'shrug'),
        expr='stern' if f < qz else ('grin' if f < fa else 'nervous'), look=0 if f < fa else 1)
    if f < qz - 2:
        if f >= vt - 10: numero_gigante(c, '5 EM 5', 640, 1000, f, vt - 10, 220, -3)
    elif f < fa - 2:
        numero_gigante(c, '15 PTS', 640, 1000, f, qz, 230, 3)
    else:
        num(c, 'FAVORITO?', 640, 1000, f, fa, 150, -3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f)
    k = kick(f, fa if f >= fa else (qz if f >= qz else 0), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'virada') - 3, 140, .9)
    s.apito(s.W(1, 'Bernabeu') - 6)
    k1 = s.W(1, 'penalti') + 2
    s.chute(k1); s.rede(k1 + 9); s.rugido(k1 + 10, 1.5, .5)
    s.thunk(k1 + 8, 150, .9)
    k2 = s.W(2, 'empatou') - 8
    s.chute(k2); s.rede(k2 + 10); s.rugido(k2 + 11, 1.8, .7)
    s.thunk(s.W(2, 'empatou') - 3, 150, .9)
    s.thunk(s.W(2, 'virou') - 3, 160, 1.0)
    s.rugido(s.W(2, 'virou') - 2, 1.5, .6)
    s.thunk(s.W(3, 'Mbappe') - 3, 140, .8)
    s.thunk(s.W(3, 'dois') - 3, 160, 1.0)
    s.thunk(s.W(4, 'Vinicius') - 3, 140, .8)
    s.thunk(s.W(4, 'cinco') - 3, 170, 1.0)
    s.apito(s.W(4, 'cinco') + 4, longo=True)
    s.thunk(s.W(5, 'vitorias') - 13, 150, .9)
    s.thunk(s.W(5, 'quinze') - 3, 160, 1.0)
    s.ting(s.W(5, 'favorito') - 8, .35)
