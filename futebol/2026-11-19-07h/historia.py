"""anima.futebol — 19/11/2026 07h — Brasileirão 35ª rodada: Flamengo abre 6 pontos e fica a uma vitória do título.
Fontes (conferidas em 19/11/2026): CNN Brasil e Metrópoles (Flamengo 2x1 Athletico-PR no Maracanã, 18/11: Vargas 10' de longe,
Carrascal 16', Jorginho de pênalti no 1º tempo (23'/26' divergem -> "ainda no primeiro tempo"); Fla 79 pts, 24 vitórias);
Gazeta Esportiva, 10frames e Metrópoles (Cruzeiro 2x1 Palmeiras no Mineirão: Sosa aos 17s do 2º tempo, Matheus Pereira de falta,
Khellven contra, minutos 28-29/31-32 divergem -> sem minuto; Palmeiras 73 pts); Palmeiras x Flamengo sábado 21/11 16h30 Nubank Parque.
Conta: Fla vence sábado -> 82 pts; Palmeiras no máximo 79 -> título. (empate não usado: depende de critério).
Sem escudos/logos/taças reais: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Flamengo abriu seis pontos e está a uma vitória do título brasileiro.",
    "Ontem à noite, os dois primeiros colocados jogaram no mesmo horário.",
    "No Maracanã, o Athletico saiu na frente com Vargas, mas Carrascal empatou, e Jorginho virou de pênalti.",
    "No Mineirão, o Palmeiras abriu o placar com Sosa, com só dezessete segundos do segundo tempo.",
    "Mas Matheus Pereira empatou numa cobrança de falta, e Khellven, contra, virou para o Cruzeiro.",
    "Agora o Flamengo tem setenta e nove pontos, contra setenta e três do Palmeiras, e faltam só três rodadas.",
    "E no sábado, às quatro e meia da tarde, os dois se enfrentam. Se o Flamengo vencer, é campeão.",
    "Festa no sábado, ou o Palmeiras ainda reage?",
]
CAPTXT = [
    "O Flamengo abriu 6 pontos|e está a 1 vitória do título brasileiro.",
    "Ontem à noite, os 2 primeiros colocados|jogaram no mesmo horário.",
    "No Maracanã, o Athletico saiu na frente com Vargas,|mas Carrascal empatou, e Jorginho virou de pênalti.",
    "No Mineirão, o Palmeiras abriu o placar com Sosa,|com só 17 segundos do 2º tempo.",
    "Mas Matheus Pereira empatou numa cobrança de falta,|e Khellven, contra, virou para o Cruzeiro.",
    "Agora o Flamengo tem 79 pontos, contra 73 do Palmeiras,|e faltam só 3 rodadas.",
    "E no sábado, às 16h30, os dois se enfrentam.|Se o Flamengo vencer, é campeão.",
    "Festa no sábado,|ou o Palmeiras ainda reage?",
]
FALA_TIKTOK = "O Flamengo fecha o título no sábado? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "FECHA SÁBADO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'seis', 4), (0, 'titulo', 4), (1, 'noite', 4), (2, 'Vargas', 4), (2, 'Carrascal', 4), (2, 'Jorginho', 4),
         (3, 'Sosa', 4), (3, 'dezessete', 4), (4, 'falta', 4), (4, 'Khellven', 4), (5, 'setenta', 4), (5, 'tres', 4),
         (6, 'quatro', 4), (6, 'campeao', 4), (7, 'Festa', 4), (7, 'reage', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')
CAP, CAP_F = time_('ATHLETICO-PR')
CRU, CRU_F = time_('CRUZEIRO')


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)



def gol_cena(c, f, kf, kcores, kfaixa, gcores, gfaixa, kseed, kskin=1, khair='#2a1a10', run_in=True, num_='10'):
    """chute de longe: atacante na frente, gol no fundo, bola diminuindo."""
    gx, gy = put_gol2(c, estufa=ramp(f, kf + 8, kf + 14))
    put_goleiro(c, f, gcores, gfaixa, arms='shrug' if f >= kf + 8 else 'hang', expr='shock' if f >= kf + 8 else 'nervous', skin=2)
    sx = lerp(260, 470, easeOut(ramp(f, 0, kf - 4))) if run_in else 470
    if run_in and f < kf - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    put_atleta(c, sx, 2010, 860, f, kseed, cores=kcores, faixa=kfaixa, skin=kskin, hair=khair, hs='curto', num_=num_,
               arms='up' if f >= kf + 10 else 'run', run=(f * .1) % 1 if (run_in and f < kf - 4) else None,
               kick=pulse(f, kf - 3, 5), expr='grin' if f >= kf + 6 else 'stern')
    rb = raio_bola(860)
    if f < kf + 40: bola_voo(c, f, kf, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 140)
    return gx, gy


def s0(f):
    c = estadio2('dusk').copy()
    se = wt(0, 'seis') - 3; ti = wt(0, 'titulo') - 3
    put_trofeu(c, 900, 1250, 520, f, ti)
    fla(c, 400, 2020, 880, f, 3, arms='up' if f >= se else 'cintura', expr='grin' if f >= se else 'stern', look=1, num_='10')
    put_placa(c, 'FLAMENGO', FLA, 400, 1100, f, wt(0, 'Flamengo') - 3, 60, -3)
    explosao(c, 640, 760, f, se, 220)
    num(c, '+6 PONTOS', 640, 760, f, se + 2, 130, -4)
    num(c, 'A 1 VITÓRIA', 640, 930, f, wt(0, 'vitoria') - 3, 80, 3)
    if f >= ti: confete(c, 640, 900, f, ti, 50, 500)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, se, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    no = wt(1, 'noite') - 3; ho = wt(1, 'horario') - 3
    if f >= no: paste_c(c, calendario('18', 'NOV'), 640, 1150, .7 * back(ramp(f, no, no + 8)))
    num(c, 'ONTEM, 20H30', 640, 720, f, no, 110, -3)
    num(c, 'MESMO HORÁRIO', 640, 1500, f, ho, 80, 3)
    fla(c, 230, 2120, 560, f, 4, arms='hang', expr='neutral', look=1)
    pal(c, 1040, 2120, 560, f, 8, arms='hang', expr='neutral', look=-1, flip=True)
    put_placa(c, 'FLAMENGO', FLA, 230, 1640, f, 0, 34, -3)
    put_placa(c, 'PALMEIRAS', PAL, 1040, 1640, f, 0, 34, 3)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1360, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    va = wt(2, 'Vargas') - 3; ca = wt(2, 'Carrascal') - 3; jo = wt(2, 'Jorginho') - 3; vi = wt(2, 'virou') - 3
    gol_cena(c, f, vi, FLA, FLA_F, CAP, CAP_F, 5, kskin=3, khair='#151010', num_='8')
    num(c, 'MARACANÃ', 640, 700, f, wt(2, 'Maracana') - 3, 90, -3)
    put_placa(c, 'VARGAS', CAP, 300, 840, f, va, 40, -3)
    put_placa(c, 'CARRASCAL', FLA, 300, 935, f, ca, 40, 2)
    put_placa(c, 'JORGINHO', FLA, 300, 1030, f, jo, 40, -2)
    if f >= vi + 8: explosao(c, 820, 1060, f, vi + 8, 150)
    num(c, 'FLA 2 x 1 CAP', 820, 1060, f, vi + 8, 80, 2)
    k = kick(f, vi, .9)
    return c, (lerp(600, 680, smooth(f / 150)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    so = wt(3, 'Sosa') - 3; de = wt(3, 'dezessete') - 3
    gol_cena(c, f, so, PAL, PAL_F, CRU, CRU_F, 9, kskin=1, khair='#3a2a1e', num_='7')
    num(c, 'MINEIRÃO', 640, 700, f, wt(3, 'Mineirao') - 3, 90, -3)
    put_placa(c, 'SOSA', PAL, 400, 900, f, so + 6, 56, -4)
    num(c, '17 SEGUNDOS!', 640, 1040, f, de, 86, 3)
    num(c, 'CRU 0 x 1 PAL', 640, 1290, f, de + 14, 70, -2)
    k = kick(f, so, .8)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    mp = wt(4, 'Matheus') - 3; fa = wt(4, 'falta') - 3; kh = wt(4, 'Khellven') - 3; vi = wt(4, 'virou') - 3
    gol_cena(c, f, fa, CRU, CRU_F, PAL, PAL_F, 13, kskin=1, khair='#111111', run_in=False, num_='10')
    put_placa(c, 'MATHEUS PEREIRA', CRU, 640, 720, f, mp, 44, -3)
    num(c, 'DE FALTA!', 640, 900, f, fa + 8, 100, 3)
    put_placa(c, 'KHELLVEN (CONTRA)', PAL, 640, 1080, f, kh, 40, -2)
    if f >= vi: explosao(c, 640, 1240, f, vi, 170)
    num(c, 'CRU 2 x 1 PAL', 640, 1240, f, vi, 100, 3)
    k = kick(f, vi, .9)
    return c, (640, 1440 + k * 10, lerp(1.1, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f), k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    se = wt(5, 'setenta') - 3; se2 = wt(5, 'setenta', 1) - 3; tr = wt(5, 'tres') - 3
    tabela(c, [('1º', 'FLAMENGO', FLA, '79', True), ('2º', 'PALMEIRAS', PAL, '73', False)], 640, 1060, f, se)
    num(c, '+6 PONTOS', 640, 720, f, se2, 120, -3)
    num(c, 'FALTAM 3 RODADAS', 640, 1560, f, tr, 76, 3)
    fla(c, 300, 2100, 520, f, 5, arms='joinha' if f >= se else 'cintura', expr='proud', look=1)
    pal(c, 980, 2100, 520, f, 9, arms='cintura', expr='stern', look=-1, flip=True)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, se, .5)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('day').copy()
    sa = wt(6, 'sabado') - 3; qu = wt(6, 'quatro') - 3; en = wt(6, 'enfrentam') - 3; ca = wt(6, 'campeao') - 3
    fx = lerp(-260, 360, easeOut(ramp(f, en - 12, en + 4)))
    px = lerp(1500, 900, easeOut(ramp(f, en - 12, en + 4)))
    if f < en + 4:
        linhas_vel(c, fx, 2010, 860, f, dir=-1); linhas_vel(c, px, 2010, 860, f, dir=1)
    fla(c, fx, 2010, 860, f, 3, arms='up' if f >= ca else 'cintura', expr='grin' if f >= ca else 'stern', look=1, num_='10',
        run=(f * .1) % 1 if f < en + 4 else None)
    pal(c, px, 2010, 860, f, 7, arms='cintura', expr='stern', look=-1, flip=True, num_='9', run=(f * .1) % 1 if f < en + 4 else None)
    put_placa(c, 'FLAMENGO', FLA, 360, 1110, f, en + 4, 54, -3)
    put_placa(c, 'PALMEIRAS', PAL, 900, 1110, f, en + 4, 54, 3)
    if f >= sa: paste_c(c, calendario('21', 'NOV'), 380, 840, .5 * back(ramp(f, sa, sa + 8)))
    num(c, '16H30', 900, 820, f, qu, 140, 4)
    num(c, 'VENCEU = CAMPEÃO', 640, 965, f, ca, 76, -2)
    if f >= ca: confete(c, 360, 1300, f, ca, 40, 400)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ca, .7)
    return c, (640, 1400 + k * 8, z, k), 'golden'


def s7(f):
    c = estadio2('dusk').copy()
    fe = wt(7, 'Festa') - 3; re = wt(7, 'reage') - 3
    put_trofeu(c, 640, 1250, 520, f, 0)
    fla(c, 290, 2040, 740, f, 3, arms='up' if f >= fe else 'cintura', expr='grin' if f >= fe else 'stern', look=1, num_='10')
    pal(c, 990, 2040, 740, f, 7, arms='punho' if f >= re else 'cintura', expr='stern', look=-1, flip=True, num_='9')
    put_placa(c, 'FLAMENGO', FLA, 300, 1220, f, 0, 38, -3)
    put_placa(c, 'PALMEIRAS', PAL, 960, 1220, f, 0, 38, 3)
    num(c, 'FESTA?', 420, 720, f, fe, 110, -4)
    num(c, 'REAÇÃO?', 820, 860, f, re, 110, 4)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('FLAMENGO 6 PONTOS NA FRENTE', 'A 1 VITÓRIA DO TÍTULO', wt(0, 'titulo') + 2),
         1: ('QUARTA, 18/11, 20H30', '35ª RODADA DO BRASILEIRÃO', wt(1, 'horario') + 4),
         2: ('FLAMENGO 2 x 1 ATHLETICO', 'VIRADA NO 1º TEMPO', wt(2, 'penalti') + 4),
         3: ('CRUZEIRO 0 x 1 PALMEIRAS', 'GOL AOS 17 SEGUNDOS DO 2º TEMPO', wt(3, 'segundo') + 2),
         4: ('CRUZEIRO 2 x 1 PALMEIRAS', 'VIRADA NO MINEIRÃO', wt(4, 'Cruzeiro') + 2),
         5: ('FLAMENGO 79 x 73 PALMEIRAS', 'FALTAM 3 RODADAS', wt(5, 'rodadas') + 2),
         6: ('PALMEIRAS x FLAMENGO', 'SÁBADO, 21/11, ÀS 16H30', wt(6, 'enfrentam') + 4),
         7: ('', '', 4)}
    if si == 7: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'seis') - 3, 150, .9)
    s.ting(s.W(0, 'titulo') - 3, .3)
    s.thunk(s.W(1, 'noite') - 3, 160, .6)
    s.thunk(s.W(2, 'Vargas') - 3, 200, .5)
    s.thunk(s.W(2, 'virou') - 3, 120, 1.0)
    s.thunk(s.W(3, 'Sosa') - 3, 120, .9)
    s.ting(s.W(3, 'dezessete') - 3, .3)
    s.thunk(s.W(4, 'falta') - 3, 120, .9)
    s.thunk(s.W(4, 'virou') - 3, 140, .8)
    s.thunk(s.W(5, 'setenta') - 3, 150, .7)
    s.thunk(s.W(6, 'enfrentam') - 3, 140, .9)
    s.ting(s.W(6, 'campeao') - 3, .35)
    s.ting(s.W(7, 'reage') - 3, .3)
