"""anima.futebol — 27/11/2026 22h15 — CONTA DA VAGA · EP. 3 — Fluminense 0x1 Cruzeiro no Maracanã (Brasileirão, 37ª rodada).
Fontes (conferidas em 27/11/2026, ver fatos.txt): CNN Brasil, Revista Placar, Jovem Pan, Gazeta Esportiva (título).
Kaio Jorge bate cruzado logo no começo; Jonathan Jesus é expulso no 2º tempo; o Flu pressiona e Otávio faz seis defesas;
Cruzeiro 69 garante o 3º lugar; Fluminense segue 4º com 63.
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
    "O Cruzeiro garantiu o terceiro lugar? Olha o fim do jogo.",
    "Logo no começo, Kaio Jorge bateu cruzado... um a zero.",
    "No segundo tempo, Jonathan Jesus foi expulso. O Cruzeiro ficou com dez.",
    "O Flu pressionou, mas o goleiro Otávio fez... seis defesas.",
    "Cruzeiro com sessenta e nove... terceiro lugar garantido.",
    "O Flu segue quarto, com sessenta e três. Foi justo?",
]
CAPTXT = [
    "O Cruzeiro garantiu o 3º lugar?|Olha o fim do jogo.",
    "Logo no começo, Kaio Jorge|bateu cruzado... 1 a 0.",
    "No 2º tempo, Jonathan Jesus foi|expulso. O Cruzeiro ficou com 10.",
    "O Flu pressionou, mas o goleiro|Otávio fez... 6 defesas.",
    "Cruzeiro com 69...|3º lugar garantido.",
    "O Flu segue 4º, com 63.|Foi justo?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "FOI JUSTO?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [4]
CHECK = [(0, 'garantiu', 4), (0, 'fim', 4), (1, 'Kaio', 4), (1, 'cruzado', 4), (1, 'zero', 4), (2, 'Jonathan', 4),
         (2, 'expulso', 4), (2, 'dez', 4), (3, 'pressionou', 4), (3, 'Otavio', 4), (3, 'seis', 4),
         (4, 'sessenta', 4), (4, 'garantido', 4), (5, 'quarto', 4), (5, 'tres', 4), (5, 'justo', 4)]

FLUC, FLU_F = time_('FLUMINENSE')
CRUC, CRU_F = time_('CRUZEIRO')
TORC = dict(roupa='#1d4fa8', pele='#e0b08a', cabelo='#3a2414')
TORC_FLU = dict(roupa='#7a1f3d', pele='#c98e64', cabelo='#1a120c')


def flu(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=FLUC, faixa=FLU_F, **kw)


def cru(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=CRUC, faixa=CRU_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor celeste + série + pergunta; depois o vestiário do Cruzeiro."""
    c = vestiario(CRUC, CRU_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, **TORC)
        num(c, 'CONTA DA VAGA', 621, 300, f, 0, 96, -2)
        num(c, 'EP. 3', 621, 430, f, 0, 100, 2)
        num(c, 'GARANTIU', 621, 1350, f, 0, 130, -2)
        num(c, 'O 3º?', 621, 1530, f, 0, 170, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    fi = wt(0, 'fim') - 3
    cru(c, 640, 2100, 860, f, 6, arms='cintura' if f < fi else 'point', expr='nervous' if f < fi else 'stern',
        look=1 if f < fi else 0, num_='19')
    if f < fi - 2:
        num(c, 'MARACANÃ', 640, 1000, f, CLOSE_F, 120, -3)
    else:
        put_placa(c, 'CRUZEIRO', CRUC, 640, 1000, f, fi, 110, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0008 * f) * (1 + .08 * pulse(f, fi, 10))
    k = kick(f, fi if f >= fi else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s1(f):
    """estádio à noite: Kaio Jorge bate cruzado, 1 x 0."""
    c = estadio2('dusk').copy()
    ka = wt(1, 'Kaio') - 3; cz = wt(1, 'cruzado') - 3; ze = wt(1, 'zero') - 3
    ks = cz - 4
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, FLUC, FLU_F, arms='up' if f >= ks + 2 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    H = 860
    sx = lerp(900, 600, easeOut(ramp(f, 0, ks - 2)))
    if f < ks - 2: linhas_vel(c, sx, 2010, H, f, dir=1)
    cru(c, sx, 2010, H, f, 9, num_='19', flip=True,
        arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 2 else None,
        kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx - H * .13 - 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx - H * .13 - 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 60, 9)
    if f >= ks + 12: confete(c, 640, 700, f, ks + 12, 40, 400)
    if f < ze - 2:
        put_placa(c, 'KAIO JORGE', CRUC, 640, 860, f, ka, 100, -2)
    else:
        explosao(c, 640, 860, f, ze, 200)
        num(c, '1 x 0', 640, 860, f, ze, 170, 3)
    k = kick(f, ks + 8 if f >= ks + 8 else ka, .9)
    return c, (lerp(600, 670, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0012 * f) * (1 + .08 * pulse(f, ka, 10)), k), 'dusk'


def s2(f):
    """prancheta: Jonathan Jesus expulso, o Cruzeiro com dez."""
    c = prancheta().copy()
    jo = wt(2, 'Jonathan') - 3; ex = wt(2, 'expulso') - 3; dz = wt(2, 'dez') - 3
    pos = [(420, 1500), (640, 1520), (860, 1500), (380, 1260), (560, 1240), (720, 1240), (900, 1260),
           (500, 1000), (780, 1000), (640, 820)]
    for i, (x, y) in enumerate(pos):
        pino(c, x, y + 8 * math.sin(f * .2 + i), CRUC, f, 2 + i * 2, '', 66)
    # o pino expulso sai da prancheta
    if f < ex + 10:
        yo = 1760 + 500 * ramp(f, ex + 2, ex + 10) ** 2
        pino(c, 640, yo, CRUC, f, jo, 'J', 80)
    if ex - 1 <= f < ex + 24:
        rr = Image.new('RGBA', (120, 170), (0, 0, 0, 0)); d = ImageDraw.Draw(rr)
        d.rounded_rectangle((6, 6, 114, 164), 14, fill=(214, 30, 40), outline=(36, 20, 30), width=8)
        rr = rr.rotate(-12 + 6 * math.sin(f * .5), expand=True, resample=Image.BICUBIC)
        c.alpha_composite(rr, (820, 1640))
    if f < ex - 2:
        put_placa(c, 'JONATHAN JESUS', CRUC, 640, 760, f, jo, 84, -2)
    elif f < dz - 2:
        num(c, 'EXPULSO', 640, 760, f, ex, 140, 2)
    else:
        explosao(c, 640, 760, f, dz, 180)
        num(c, 'COM DEZ', 640, 760, f, dz, 150, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ex, 10))
    k = kick(f, dz if f >= dz else (ex if f >= ex else jo), .7)
    return c, (640 + 12 * math.sin(f * .06), 1250 + k * 8, z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s3(f):
    """estádio golden: o Flu chuta, Otávio defende; seis defesas."""
    c = estadio2('golden').copy()
    pr = wt(3, 'pressionou') - 3; ot = wt(3, 'Otavio') - 3; se = wt(3, 'seis') - 3
    gx, gy = put_gol2(c)
    ks = ot - 6
    defende = f >= ks + 7
    put_goleiro(c, f, CRUC, CRU_F, arms='up' if f >= ks + 2 else 'hang',
                expr='grin' if f >= se else ('stern' if defende else 'nervous'), skin=3)
    H = 860
    sx = lerp(300, 520, easeOut(ramp(f, 0, ks - 2)))
    if f < ks - 2: linhas_vel(c, sx, 2010, H, f, dir=-1)
    flu(c, sx, 2010, H, f, 4, num_='10',
        arms='run' if f < ks + 8 else 'cheek', run=(f * .1) % 1 if f < ks - 2 else None,
        kick=pulse(f, ks - 3, 5), expr='stern' if f < ks + 8 else 'pained')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 7:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 40, gy - 40, rb, raio_bola(300), 60, 7)
    elif f < ks + 20:
        t = ramp(f, ks + 7, ks + 20)
        put_bola(c, lerp(gx + 40, gx - 260, t), lerp(gy - 40, gy - 200, t) + 300 * t * t, raio_bola(320), f)
    if f < ot - 2:
        num(c, 'PRESSÃO', 640, 860, f, pr, 140, -2)
    elif f < se - 2:
        put_placa(c, 'OTÁVIO', CRUC, 640, 860, f, ot, 110, 2)
    else:
        explosao(c, 640, 860, f, se, 200)
        num(c, '6 DEFESAS', 640, 860, f, se, 140, -3)
    z = lerp(1.14, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ks + 7, 10))
    k = kick(f, ks + 7 if f >= ks + 7 else pr, .9)
    return c, (640 + 20 * math.sin(f * .04), 1440 + k * 10, z, k), 'golden'


def s4(f):
    """telão: 69 pontos, terceiro lugar garantido."""
    c = telao('dusk').copy()
    se = wt(4, 'sessenta') - 3; ga = wt(4, 'garantido') - 3
    cru(c, 640, 2090, 820, f, 7, num_='19',
        arms='punho' if f < ga else 'up', expr='stern' if f < se else 'grin', look=0)
    if f < se - 2:
        telao_txt(c, [('FIM DE JOGO', 150)], f, 0, y=720)
    elif f < ga - 2:
        telao_txt(c, [('69 PTS', 230)], f, se, y=700)
    else:
        telao_txt(c, [('3º GARANTIDO', 108)], f, ga, y=720)
    if f >= ga: confete(c, 640, 500, f, ga, 70, 600)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ga, 10))
    k = kick(f, ga if f >= ga else se, .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s5(f):
    """a conta do Flu: 4º com 63; fecha no close do torcedor tricolor."""
    c = vestiario(FLUC, FLU_F).copy()
    q = wt(5, 'quarto') - 3; tr = wt(5, 'tres') - 3; ju = wt(5, 'justo') - 6
    flu(c, 640, 2100, 840, f, 5, num_='10', arms='hang' if f < tr else 'cheek',
        expr='nervous' if f < tr else 'pained', look=-1 if f < q else 1)
    if f < tr - 2:
        put_placa(c, 'FLUMINENSE', FLUC, 640, 1000, f, q, 100, -2)
    else:
        num(c, '4º · 63', 640, 1000, f, tr, 160, 3)
    if f >= ju:
        c = put_close(c, f, expr='curioso' if f < ju + 14 else 'choque', look=-1 if f < ju + 10 else 0, s=.9, **TORC_FLU)
        num(c, 'FOI JUSTO?', 621, 1450, f, ju, 150, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - ju)), 0), 'dusk'
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, tr, 10))
    k = kick(f, tr if f >= tr else 0, .7)
    return c, (640 + 25 * math.sin(f * .05), 1400 + k * 8, z, k), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'fim') - 3, 140, .9)
    s.apito(s.W(1, 'Kaio') - 6)
    s.thunk(s.W(1, 'Kaio') - 3, 140, .8)
    k1 = s.W(1, 'cruzado') - 4
    s.chute(k1); s.rede(k1 + 9); s.rugido(k1 + 10, 1.4, .5)
    s.thunk(s.W(1, 'zero') - 3, 160, 1.0)
    s.thunk(s.W(2, 'Jonathan') - 3, 140, .8)
    s.apito(s.W(2, 'expulso') - 4)
    s.thunk(s.W(2, 'expulso') - 3, 150, .9)
    s.thunk(s.W(2, 'dez') - 3, 160, 1.0)
    k2 = s.W(3, 'Otavio') - 6
    s.chute(k2)
    s.thunk(k2 + 7, 150, .9)
    s.thunk(s.W(3, 'seis') - 3, 170, 1.0)
    s.apito(s.W(4, 'sessenta') - 8, longo=True)
    s.thunk(s.W(4, 'sessenta') - 3, 160, 1.0)
    s.thunk(s.W(4, 'garantido') - 3, 170, 1.0)
    s.rugido(s.W(4, 'garantido') - 2, 1.4, .5)
    s.ting(s.W(4, 'garantido') + 6, .35)
    s.thunk(s.W(5, 'quarto') - 3, 140, .8)
    s.thunk(s.W(5, 'tres') - 3, 150, .9)
