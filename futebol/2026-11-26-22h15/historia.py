"""anima.futebol — 26/11/2026 22h15 — CONTA DA VAGA · EP. 2 — São Paulo 3x1 Remo no Morumbis (Brasileirão, 37ª rodada).
Fontes (conferidas em 26/11/2026, ver fatos.txt): Gazeta Esportiva (pós-jogo), Diário 24 Horas, Terra (minuto a minuto), Lance, Band.
Calleri abre no 1º tempo; Poveda empata de cabeça; Ryan Francisco desempata na reta final; Calleri fecha no fim.
São Paulo sai de 5 jogos sem vencer e chega a 48; a vaga na Sul-Americana vai para a última rodada, x Athletico-PR em Curitiba.
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
    "O São Paulo voltou a vencer? Olha o fim do jogo.",
    "Calleri abriu o placar no primeiro tempo... um a zero.",
    "Mas Poveda, de cabeça, empatou para o Remo... um a um.",
    "Na reta final, Ryan Francisco desempatou... dois a um.",
    "E no fim, Calleri de novo... três a um.",
    "Acabou o jejum. Quarenta e oito pontos, e a vaga se decide em Curitiba.",
]
CAPTXT = [
    "O São Paulo voltou a vencer?|Olha o fim do jogo.",
    "Calleri abriu o placar no|primeiro tempo... 1 a 0.",
    "Mas Poveda, de cabeça, empatou|para o Remo... 1 a 1.",
    "Na reta final, Ryan Francisco|desempatou... 2 a 1.",
    "E no fim, Calleri|de novo... 3 a 1.",
    "Acabou o jejum. 48 pontos, e a|vaga se decide em Curitiba.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "A VAGA VEM?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 3
FLASH = [3]
CHECK = [(0, 'vencer', 4), (0, 'fim', 4), (1, 'Calleri', 4), (1, 'placar', 4), (1, 'zero', 4), (2, 'Poveda', 4),
         (2, 'cabeca', 4), (2, 'empatou', 4), (2, 'um', 4), (3, 'Ryan', 4), (3, 'desempatou', 4), (3, 'dois', 4),
         (4, 'Calleri', 4), (4, 'tres', 4), (5, 'jejum', 4), (5, 'Quarenta', 4), (5, 'Curitiba', 4)]

SAO, SAO_F = time_('SÃO PAULO')
REM, REM_F = time_('REMO')
TORC = dict(roupa='#f4f4f4', pele='#c98e64', cabelo='#1a120c')


def sp(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=SAO, faixa=SAO_F, **kw)


def rem(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 4); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=REM, faixa=REM_F, **kw)


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
    """quadro 0 = capa: close do torcedor tricolor + série + pergunta; depois o vestiário do São Paulo."""
    c = vestiario(SAO, SAO_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, **TORC)
        num(c, 'CONTA DA VAGA', 621, 300, f, 0, 96, -2)
        num(c, 'EP. 2', 621, 430, f, 0, 100, 2)
        num(c, 'VOLTOU A', 621, 1350, f, 0, 130, -2)
        num(c, 'VENCER?', 621, 1530, f, 0, 160, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    fi = wt(0, 'fim') - 3
    sp(c, 640, 2100, 860, f, 6, arms='cintura' if f < fi else 'point', expr='nervous' if f < fi else 'stern',
       look=1 if f < fi else 0, num_='9')
    if f < fi - 2:
        num(c, '5 SEM VENCER', 640, 1000, f, CLOSE_F, 110, -3)
    else:
        put_placa(c, 'SÃO PAULO', SAO, 640, 1000, f, fi, 110, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0008 * f) * (1 + .08 * pulse(f, fi, 10))
    k = kick(f, fi if f >= fi else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s1(f):
    """estádio à noite: Calleri abre, 1 x 0."""
    c = estadio2('dusk').copy()
    ca = wt(1, 'Calleri') - 3; pl = wt(1, 'placar') - 3; ze = wt(1, 'zero') - 3
    ks = pl - 6
    lance(c, f, ks, sp, ('#0d2a5c', '#0d2a5c', '#0d2a5c'), 4, '9', sx0=280, sx1=480)
    if f < ze - 2:
        put_placa(c, 'CALLERI', SAO, 640, 860, f, ca, 110, -2)
    else:
        explosao(c, 640, 860, f, ze, 200)
        num(c, '1 x 0', 640, 860, f, ze, 170, 3)
    k = kick(f, ks + 8 if f >= ks + 8 else ca, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0012 * f) * (1 + .08 * pulse(f, ca, 10)), k), 'dusk'


def s2(f):
    """prancheta: cruzamento e cabeçada de Poveda, 1 x 1."""
    c = prancheta().copy()
    po = wt(2, 'Poveda') - 3; cb = wt(2, 'cabeca') - 3; em = wt(2, 'empatou') - 3; um = wt(2, 'um') - 3
    for i, (x, y) in enumerate(((480, 720), (660, 690), (840, 740))):
        pino(c, x, y + 10 * math.sin(f * .2 + i), SAO, f, 2 + i * 2, '', 70)
    pino(c, 1040, 1000, REM, f, 0, '', 70)
    pino(c, 640, 800 + 8 * math.sin(f * .2), REM, f, po, 'P', 90)
    seta(c, (1030, 980), (660, 820), f, max(2, cb - 10), 12, (255, 255, 255), 10)
    seta(c, (640, 790), (620, 560), f, em, 8, (255, 216, 74), 16)
    if f < cb - 2:
        put_placa(c, 'POVEDA', REM, 640, 1320, f, po, 110, -2)
    elif f < um - 2:
        num(c, 'DE CABEÇA', 640, 1320, f, cb, 130, 2)
    else:
        explosao(c, 640, 1320, f, um, 180)
        num(c, '1 x 1', 640, 1320, f, um, 170, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, em, 10))
    k = kick(f, um if f >= um else (cb if f >= cb else po), .7)
    return c, (640 + 12 * math.sin(f * .06), 1150 + k * 8, z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s3(f):
    """estádio golden: Ryan Francisco desempata, 2 x 1."""
    c = estadio2('golden').copy()
    ry = wt(3, 'Ryan') - 3; de = wt(3, 'desempatou') - 3; do = wt(3, 'dois') - 3
    ks = de - 4
    lance(c, f, ks, sp, ('#0d2a5c', '#0d2a5c', '#0d2a5c'), 9, '11', sx0=900, sx1=560, skin=4, hair='#151010')
    if f < do - 2:
        put_placa(c, 'RYAN FRANCISCO', SAO, 640, 860, f, ry, 84, -2)
    else:
        explosao(c, 640, 860, f, do, 200)
        num(c, '2 x 1', 640, 860, f, do, 170, -3)
    z = lerp(1.14, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ks + 8, 10))
    k = kick(f, ks + 8 if f >= ks + 8 else ry, .9)
    return c, (640 + 20 * math.sin(f * .04), 1440 + k * 10, z, k), 'golden'


def s4(f):
    """telão: Calleri de novo, 3 x 1."""
    c = telao('dusk').copy()
    ca = wt(4, 'Calleri') - 3; tr = wt(4, 'tres') - 3
    sp(c, 640, 2090, 820, f, 7, num_='9', skin=2,
       arms='run' if f < ca else ('punho' if f < tr else 'up'), run=(f * .1) % 1 if f < ca else None,
       expr='stern' if f < ca else 'grin', look=0)
    if f < ca - 2:
        telao_txt(c, [('FIM DE JOGO', 150)], f, 0, y=720)
    elif f < tr - 2:
        telao_txt(c, [('CALLERI', 170)], f, ca, y=720)
    else:
        telao_txt(c, [('3 x 1', 230)], f, tr, y=700)
    if f >= tr: confete(c, 640, 500, f, tr, 70, 600)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, tr, 10))
    k = kick(f, tr if f >= tr else ca, .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s5(f):
    """a conta: 48 pontos; Curitiba; fecha no close sorrindo do torcedor."""
    c = conta_bg().copy()
    q = wt(5, 'Quarenta') - 3; cu = wt(5, 'Curitiba') - 3; fim = cu + 16
    sp(c, 640, 2090, 780, f, 6, num_='9', arms='up' if f >= q else 'punho', expr='grin', look=0)
    if f < q - 2:
        numero_gigante(c, 'FIM DO JEJUM', 640, 1000, f, 0, 118, 3)
    elif f < cu - 2:
        numero_gigante(c, '48 PTS', 640, 1000, f, q, 230, -3)
    else:
        numero_gigante(c, 'CURITIBA', 640, 1000, f, cu, 170, 3)
    if f >= fim:
        c = put_close(c, f, expr='sorriso', look=-1 if f < fim + 12 else 0, s=.9, **TORC)
        num(c, 'A VAGA VEM?', 621, 1450, f, fim, 150, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - fim)), 0), 'dusk'
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, q, 10))
    k = kick(f, q if f >= q else 0, .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'fim') - 3, 140, .9)
    s.apito(s.W(1, 'Calleri') - 6)
    s.thunk(s.W(1, 'Calleri') - 3, 140, .8)
    k1 = s.W(1, 'placar') - 6
    s.chute(k1); s.rede(k1 + 9); s.rugido(k1 + 10, 1.4, .5)
    s.thunk(s.W(1, 'zero') - 3, 160, 1.0)
    s.thunk(s.W(2, 'Poveda') - 3, 140, .8)
    s.thunk(s.W(2, 'cabeca') - 3, 150, .9)
    s.thunk(s.W(2, 'um') - 3, 160, 1.0)
    k2 = s.W(3, 'desempatou') - 4
    s.chute(k2); s.rede(k2 + 9); s.rugido(k2 + 10, 1.4, .5)
    s.thunk(s.W(3, 'dois') - 3, 170, 1.0)
    s.thunk(s.W(4, 'Calleri') - 3, 140, .8)
    s.thunk(s.W(4, 'tres') - 3, 170, 1.0)
    s.rugido(s.W(4, 'tres') - 2, 1.4, .5)
    s.apito(s.W(4, 'tres') + 8, longo=True)
    s.thunk(s.W(5, 'Quarenta') - 3, 160, 1.0)
    s.thunk(s.W(5, 'Curitiba') - 3, 150, .9)
    s.ting(s.W(5, 'Curitiba') + 12, .35)
