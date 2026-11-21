"""anima.futebol — 21/11/2026 18h50 — CONTA DO TÍTULO · EP. 2 (episódio do campeão) — Palmeiras 1x1 Flamengo, Flamengo campeão.
Fontes (conferidas em 21/11/2026, ver fatos.txt): Bola na Rede (Flamengo vence o Brasileirão 2026, 80 x 74 pts, 10ª vez), aRede
(1 a 1 no Nubank Parque, Arias de cabeça no 1º tempo, Samuel Lino no 2º, título com 2 rodadas de antecedência), Lance! tempo real
(Arias de cabeça 11', Samuel Lino 75'), Lance! pré-jogo (décimo título), Soccerway (Fla 9 títulos até 2025), manchetes Coluna do Fla
e Mixvale. Sem escudos/logos/taça real: times por plaquinhas e cores, taça genérica."""
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
    "O Flamengo já é campeão brasileiro? Olha como foi.",
    "No Nubank Parque, o Palmeiras saiu na frente com Arias, de cabeça.",
    "No segundo tempo, Samuel Lino empatou... um a um.",
    "Com o empate, o Flamengo chega a oitenta pontos. O Palmeiras, setenta e quatro.",
    "Faltando duas rodadas, a conta fechou... o Flamengo é campeão!",
    "É o décimo título brasileiro do Flamengo.",
]
CAPTXT = [
    "O Flamengo já é campeão brasileiro?|Olha como foi.",
    "No Nubank Parque, o Palmeiras saiu na frente|com Arias, de cabeça.",
    "No 2º tempo, Samuel Lino empatou...|1 a 1.",
    "Com o empate, o Flamengo chega a 80 pontos.|O Palmeiras, 74.",
    "Faltando 2 rodadas, a conta fechou...|o Flamengo é campeão!",
    "É o 10º título brasileiro|do Flamengo.",
]
FALA_TIKTOK = "O Flamengo mereceu o título? Comenta sim ou não."
CTA_TEXTO = "MERECEU?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Flamengo', 4), (0, 'campeao', 4), (1, 'Palmeiras', 4), (1, 'Arias', 4), (1, 'cabeca', 4), (2, 'Lino', 4),
         (2, 'empatou', 4), (3, 'oitenta', 4), (3, 'setenta', 4), (4, 'duas', 4), (4, 'campeao', 4), (5, 'decimo', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 40   # quadros do close de abertura (~1,3 s)


def s0(f):
    """quadro 0 = capa: close do torcedor do Flamengo + série + pergunta; depois o jogador na conta."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, roupa='#c8102e', pele='#b07a55', cabelo='#151010')
        num(c, 'CONTA DO TÍTULO', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 2', 621, 430, f, 0, 100, 2)
        num(c, 'O FLAMENGO JÁ', 621, 1350, f, 0, 125, -2)
        num(c, 'É CAMPEÃO?', 621, 1520, f, 0, 145, 2)
        z = 1.0 + .0015 * f
        return c, (621, 1104, z, 0), 'dusk'
    ol = wt(0, 'Olha') - 3
    fla(c, 640, 2080, 880, f, 6, arms='cintura' if f < ol else 'punho', expr='stern' if f < ol else 'grin', look=0, num_='10')
    num(c, 'PAL x FLA', 640, 880, f, CLOSE_F, 150, -3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio à noite: cruzamento e Arias de cabeça, gol no fundo."""
    c = estadio2('dusk').copy()
    pa = wt(1, 'Palmeiras') - 3; ar = wt(1, 'Arias') - 3; ca = wt(1, 'cabeca') - 3
    kh = ar  # cabeçada
    gx, gy = put_gol2(c, estufa=ramp(f, kh + 8, kh + 14))
    put_goleiro(c, f, FLA, FLA_F, arms='shrug' if f >= kh + 8 else 'hang', expr='shock' if f >= kh + 8 else 'nervous', skin=2)
    sx = 470; H = 860
    pulo = 70 * pulse(f, kh - 6, 12)
    pal(c, sx, 2010 - pulo, H, f, 5, num_='11', arms='up' if f >= kh + 10 else 'run',
        expr='grin' if f >= kh + 6 else 'stern')
    hy = 2010 - pulo - H * .9
    rb = raio_bola(H)
    if f < kh:
        bola_voo(c, f, kh - 14, -120, 1250, sx + 10, hy, rb * .9, rb, 60, 14)
    elif f < kh + 40:
        bola_voo(c, f, kh, sx + 10, hy, gx + 90, gy, rb, raio_bola(300), 40, 10)
    if f < ar - 2:
        if f >= pa: put_placa(c, 'PALMEIRAS', PAL, 640, 760, f, pa, 70, -3)
    else:
        put_placa(c, 'ARIAS, DE CABEÇA', PAL, 640, 760, f, ar + 4, 68, 2)
    k = kick(f, kh, .9)
    return c, (lerp(600, 680, smooth(f / 150)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s2(f):
    """estádio dourado: Samuel Lino empata (1 a 1)."""
    c = estadio2('golden').copy()
    li = wt(2, 'Lino') - 3; em = wt(2, 'empatou') - 3; um = wt(2, 'um') - 3
    kf = em
    gx, gy = put_gol2(c, estufa=ramp(f, kf + 8, kf + 14))
    put_goleiro(c, f, PAL, PAL_F, arms='shrug' if f >= kf + 8 else 'hang', expr='shock' if f >= kf + 8 else 'nervous', skin=1)
    sx = lerp(260, 470, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    fla(c, sx, 2010, 860, f, 9, num_='16', arms='up' if f >= kf + 10 else 'run', run=(f * .1) % 1 if f < kf - 4 else None,
        kick=pulse(f, kf - 3, 5), expr='grin' if f >= kf + 6 else 'stern', skin=4)
    rb = raio_bola(860)
    if f < kf + 40: bola_voo(c, f, kf, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 140)
    if f >= um:
        explosao(c, 640, 860, f, um, 200)
        num(c, '1 x 1', 640, 860, f, um, 170, 3)
    elif f >= li:
        put_placa(c, 'SAMUEL LINO', FLA, 640, 800, f, li, 72, -3)
    k = kick(f, kf, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'golden'


def s3(f):
    """telão com a tabelinha 80 x 74."""
    c = telao('dusk').copy()
    oi = wt(3, 'oitenta') - 3; se = wt(3, 'setenta') - 3
    tabela(c, [('1º', 'FLAMENGO', FLA, '80', True)], 640, 860, f, oi)
    tabela(c, [('2º', 'PALMEIRAS', PAL, '74', False)], 640, 1050, f, se)
    fla(c, 330, 2080, 640, f, 3, arms='up' if f >= oi else 'hang', expr='grin' if f >= oi else 'stern', look=1, num_='9')
    pal(c, 950, 2080, 640, f, 5, arms='cheek' if f >= se else 'hang', expr='pained' if f >= se else 'nervous', look=-1, flip=True, num_='7')
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, max(oi, se) if f >= se else oi, .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s4(f):
    """a conta: 2 rodadas -> CAMPEÃO (resposta da pergunta)."""
    c = conta_bg().copy()
    du = wt(4, 'duas') - 3; ca = wt(4, 'campeao') - 3
    fla(c, 640, 2090, 860, f, 6, arms='up' if f >= ca else 'cintura', expr='grin' if f >= ca else 'stern', look=0, num_='10')
    if f < ca - 2:
        if f >= du: num(c, '2 RODADAS', 640, 900, f, du, 140, -3)
    else:
        explosao(c, 640, 960, f, ca, 280)
        numero_gigante(c, 'CAMPEÃO!', 640, 960, f, ca, 165, 3)
        confete(c, 640, 900, f, ca, 70, 650)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, ca, .8)
    return c, (640, 1400 + k * 10, z * (1 + .0015 * max(0, f - ca)), k), 'day'


def s5(f):
    """vestiário do Flamengo: taça genérica e o 10º título."""
    c = vestiario(FLA, FLA_F).copy()
    de = wt(5, 'decimo') - 3
    tk = back(ramp(f, 0, 10))
    if tk > .03: paste_c(c, trofeu(), 640, 1250, .9 * tk)
    fla(c, 300, 2110, 760, f, 3, arms='up', expr='grin', look=1, num_='9')
    fla(c, 980, 2110, 760, f, 8, arms='up', expr='grin', look=-1, flip=True, num_='11', skin=1, hair='#3a2a1e')
    if f >= de:
        numero_gigante(c, '10º TÍTULO', 640, 780, f, de, 125, -3)
        confete(c, 640, 700, f, de, 70, 650)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, de, .6)
    return c, (640, 1380 + k * 8, z, k), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(s.cut(0) + CLOSE_F, 120, .8)
    s.apito(s.W(1, 'Palmeiras') - 4)
    s.thunk(s.W(1, 'Palmeiras') - 3, 150, .6)
    s.chute(s.W(1, 'Arias') - 3); s.rede(s.W(1, 'Arias') + 6); s.rugido(s.W(1, 'Arias') + 7, 2.2, .7)
    s.thunk(s.W(1, 'cabeca') - 3, 130, .7)
    s.thunk(s.W(2, 'Lino') - 3, 150, .7)
    s.chute(s.W(2, 'empatou') - 3); s.rede(s.W(2, 'empatou') + 6); s.rugido(s.W(2, 'empatou') + 7)
    s.thunk(s.W(2, 'um') - 3, 120, 1.0)
    s.thunk(s.W(3, 'oitenta') - 3, 150, .8)
    s.thunk(s.W(3, 'setenta') - 3, 120, .8)
    s.thunk(s.W(4, 'duas') - 3, 150, .7)
    s.apito(s.W(4, 'campeao') - 8, longo=True)
    s.thunk(s.W(4, 'campeao') - 3, 110, 1.0)
    s.ting(s.W(4, 'campeao') - 3, .35)
    s.thunk(s.W(5, 'decimo') - 3, 130, .9)
