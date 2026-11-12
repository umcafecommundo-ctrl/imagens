"""anima.futebol — 12/11/2026 19h — Brasileirão: guerra de bastidores entre Flamengo e Palmeiras pela arbitragem.
Fontes (conferidas em 12/11/2026): Lance! (11/11: Daronco em Cruzeiro x Palmeiras, Rafael Klein em Flamengo x Athletico-PR,
35ª rodada; origem: possível pênalti de Barboza não marcado para o Vasco na semifinal da Copa do Brasil);
Terra/Esporte News Mundo/ESPN (12/11: Flamengo critica a escala de Daronco; Palmeiras questiona Klein no jogo do Flamengo;
Fla 76 x Palmeiras 73, faltam 4 rodadas); Correio Braziliense (11/11: CBF não pretende alterar as designações);
Diário do Centro do Mundo (12/11: Cruzeiro x Palmeiras dia 18, Palmeiras x Flamengo dia 21); Revista Oeste (calendário).
Sem escudos/logos: times por plaquinhas e cores; árbitros como bonecos genéricos com placa do nome."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "A briga pelo título do Brasileirão saiu do gramado e foi parar na arbitragem.",
    "A CBF escalou Anderson Daronco para apitar Cruzeiro e Palmeiras, no dia dezoito, em Belo Horizonte.",
    "E o Flamengo reclamou, porque foi Daronco quem não marcou um possível pênalti para o Vasco contra o Palmeiras, na Copa do Brasil.",
    "Do outro lado, o Palmeiras questionou Rafael Klein, escalado para Flamengo e Athletico, na mesma rodada.",
    "Mas a CBF não recuou e manteve os dois árbitros.",
    "Tudo porque o Flamengo lidera com setenta e seis pontos, só três à frente do Palmeiras, faltando quatro rodadas.",
    "E no dia vinte e um, os dois se enfrentam, num jogo que pode decidir o título.",
]
CAPTXT = [
    "A briga pelo título do Brasileirão saiu do gramado|e foi parar na arbitragem.",
    "A CBF escalou Anderson Daronco para apitar|Cruzeiro e Palmeiras, dia 18, em Belo Horizonte.",
    "E o Flamengo reclamou, porque foi Daronco quem não marcou|um possível pênalti para o Vasco contra o Palmeiras, na Copa do Brasil.",
    "Do outro lado, o Palmeiras questionou Rafael Klein,|escalado para Flamengo e Athletico, na mesma rodada.",
    "Mas a CBF não recuou|e manteve os dois árbitros.",
    "Tudo porque o Flamengo lidera com 76 pontos,|só 3 à frente do Palmeiras, faltando 4 rodadas.",
    "E no dia 21, os dois se enfrentam,|num jogo que pode decidir o título.",
]
FALA_TIKTOK = "Quem leva o título, Flamengo ou Palmeiras? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'arbitragem', 4), (1, 'Daronco', 4), (1, 'Palmeiras', 4), (2, 'reclamou', 4), (2, 'penalti', 4),
         (3, 'Klein', 4), (4, 'manteve', 4), (5, 'setenta', 4), (6, 'titulo', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')
CRU_, CRU_F = time_('CRUZEIRO')
VAS, VAS_F = time_('VASCO')
CAP, CAP_F = time_('ATHLETICO-PR')
ARB = ('#f5c518', '#111111', '#111111')   # uniforme genérico de árbitro
PLACA_ARB = ('#2b2b2b', '#f5c518', '#111111')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def cartao(cor):
    p = Pen(120, 170)
    p.shape([(10, 10), (110, 10), (110, 160), (10, 160)], hexc(cor), mul(hexc(cor), .8), 5, 8)
    return p.img


def put_arb(c, x, feet, h, f, seed, **kw):
    put_jog(c, x, feet, h, f, seed, cores=ARB, faixa=None, hair='#1a1a1a', **kw)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    ar = wt(0, 'arbitragem') - 3
    put_jog(c, 280, 2030, 820, f, 1, cores=FLA, faixa=FLA_F, arms='cintura', expr='stern', skin=1, look=1)
    put_jog(c, 970, 2030, 820, f, 2, cores=PAL, faixa=PAL_F, arms='cintura', expr='stern', skin=0, look=-1, flip=True)
    put_placa(c, 'FLAMENGO', FLA, 320, 1150, f, wt(0, 'titulo') - 3, 48, -4)
    put_placa(c, 'PALMEIRAS', PAL, 940, 1150, f, wt(0, 'titulo') + 2, 48, 4)
    if f >= ar - 8:
        y = lerp(2600, 2050, easeOut(ramp(f, ar - 8, ar + 4)))
        put_arb(c, 620, y, 900, f, 3, arms='up' if f >= ar else 'hang', expr='nervous')
    num(c, 'BRIGA PELO TÍTULO', 640, 720, f, wt(0, 'briga') - 3, 76, -3)
    num(c, 'ARBITRAGEM!', 640, 880, f, ar, 130, 4)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, ar, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    da = wt(1, 'Daronco') - 3; cr = wt(1, 'Cruzeiro') - 3; pa = wt(1, 'Palmeiras') - 3
    put_arb(c, 640, 2040, 900, f, 3, arms='point', expr='neutral')
    put_placa(c, 'DARONCO', PLACA_ARB, 640, 1160, f, da, 64)
    cx_ = lerp(-200, 250, easeOut(ramp(f, cr - 8, cr + 6)))
    px_ = lerp(1450, 1000, easeOut(ramp(f, pa - 8, pa + 6)))
    if f >= cr - 8: put_jog(c, cx_, 1880, 600, f, 4, cores=CRU_, faixa=CRU_F, arms='cintura', expr='stern', skin=2)
    if f >= pa - 8: put_jog(c, px_, 1880, 600, f, 5, cores=PAL, faixa=PAL_F, arms='cintura', expr='stern', skin=0, flip=True)
    put_placa(c, 'CRUZEIRO', CRU_, 300, 1330, f, cr + 4, 44, -4)
    put_placa(c, 'PALMEIRAS', PAL, 960, 1330, f, pa + 4, 44, 4)
    d0 = wt(1, 'dezoito') - 3
    if f >= d0: paste_c(c, calendario('18', 'NOV'), 330, 800, .62 * back(ramp(f, d0, d0 + 8)))
    num(c, 'BELO HORIZONTE', 790, 820, f, wt(1, 'Belo') - 3, 58, 3)
    z = lerp(1.04, 1.14, smooth(f / 130))
    return c, (640 + 20 * math.sin(f * .03), 1420, z, 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    re = wt(2, 'reclamou') - 3; pe = wt(2, 'penalti') - 4
    put_goleiro(c, f, PAL, PAL_F, arms='hang', expr='nervous', skin=0)
    if f < pe - 2:
        put_jog(c, 380, 2030, 860, f, 1, cores=FLA, faixa=FLA_F, arms='point' if f >= re else 'cintura', expr='stern', skin=1)
        put_placa(c, 'FLAMENGO', FLA, 400, 1140, f, 0, 50, -4)
        put_arb(c, 900, 2010, 820, f, 3, arms='shrug' if f >= re else 'hang', expr='nervous', flip=True)
        num(c, 'RECLAMOU!', 640, 760, f, re, 130, -4)
    else:
        caiu = ramp(f, pe, pe + 8)
        put_jog(c, 470, 2030 - 0 * caiu, 860, f, 6, cores=VAS, faixa=VAS_F, arms='up' if f >= pe else 'run', expr='shock', skin=2, hair='#151515', tilt=-14 * caiu)
        put_placa(c, 'VASCO', VAS, 470, 1150, f, pe, 56, -4)
        rb = raio_bola(860)
        put_bola(c, 700, 2030 - rb, rb, f)
        put_arb(c, 930, 2010, 760, f, 3, arms='hang', expr='neutral', flip=True)
        num(c, 'PÊNALTI?', 640, 740, f, pe, 150, -4)
        num(c, 'SEMI DA COPA', 640, 900, f, wt(2, 'Copa') - 3, 90, 3)
    k = kick(f, pe, .8)
    return c, (640, 1450 + k * 10, 1.1 * (1 + .0008 * f), k), 'dusk'


def s3(f):
    c = estadio('day').copy()
    kl = wt(3, 'Klein') - 3; fl = wt(3, 'Flamengo') - 3; at = wt(3, 'Athletico') - 3
    put_jog(c, 300, 2030, 860, f, 2, cores=PAL, faixa=PAL_F, arms='point' if f >= kl else 'cintura', expr='stern', skin=0)
    put_placa(c, 'PALMEIRAS', PAL, 360, 1130, f, wt(3, 'Palmeiras') - 3, 52, -4)
    put_arb(c, 920, 2010, 820, f, 7, arms='shrug', expr='nervous', flip=True)
    put_placa(c, 'RAFAEL KLEIN', PLACA_ARB, 920, 1160, f, kl, 50, 3)
    put_placa(c, 'FLAMENGO', FLA, 370, 720, f, fl, 46, -3)
    num(c, 'x', 640, 730, f, at, 90, 0)
    put_placa(c, 'ATHLETICO-PR', CAP, 900, 720, f, at, 42, 3)
    z = lerp(1.25, 1.06, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    return c, (640, 1420, z, 0), 'golden'


def s4(f):
    c = estadio('dusk').copy()
    ma = wt(4, 'manteve') - 3
    put_arb(c, 380, 2030, 860, f, 3, arms='joinha' if f >= ma else 'hang', expr='proud' if f >= ma else 'neutral')
    put_arb(c, 880, 2030, 860, f, 7, arms='joinha' if f >= ma else 'hang', expr='proud' if f >= ma else 'neutral', flip=True)
    put_placa(c, 'DARONCO', PLACA_ARB, 380, 1140, f, ma, 48, -3)
    put_placa(c, 'KLEIN', PLACA_ARB, 880, 1140, f, ma + 3, 48, 3)
    num(c, 'CBF NÃO RECUOU', 640, 730, f, wt(4, 'recuou') - 3, 100, -3)
    num(c, 'ESCALA MANTIDA', 640, 910, f, ma, 100, 3)
    k = kick(f, ma)
    return c, (640, 1420 + k * 10, lerp(1.04, 1.16, smooth(f / 80)), k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    tabela(c, [('1º', 'FLAMENGO', FLA, '76', True), ('2º', 'PALMEIRAS', PAL, '73', False)], 640, 1150, f, 2)
    num(c, '3 PONTOS', 640, 740, f, wt(5, 'tres') - 3, 120, -3)
    num(c, 'FALTAM 4 RODADAS', 640, 1620, f, wt(5, 'faltando') - 3, 96, 3)
    return c, (640 + 15 * math.sin(f * .04), 1300, lerp(1.0, 1.08, smooth(f / 120)), 0), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    pa_ = wt(6, 'enfrentam') - 3; ti = wt(6, 'titulo') - 3
    fx = lerp(-260, 300, easeOut(ramp(f, pa_ - 12, pa_ + 6)))
    px = lerp(1500, 960, easeOut(ramp(f, pa_ - 12, pa_ + 6)))
    put_trofeu(c, 640, 1250, 520, f, ti)
    put_jog(c, fx, 2030, 860, f, 1, cores=FLA, faixa=FLA_F, arms='cintura', expr='stern', skin=1, look=1)
    put_jog(c, px, 2030, 860, f, 2, cores=PAL, faixa=PAL_F, arms='cintura', expr='stern', skin=0, look=-1, flip=True)
    put_placa(c, 'PALMEIRAS', PAL, 930, 1160, f, pa_ + 4, 46, 4)
    put_placa(c, 'FLAMENGO', FLA, 340, 1160, f, pa_ + 4, 46, -4)
    d0 = wt(6, 'vinte') - 3
    if f >= d0: paste_c(c, calendario('21', 'NOV'), 640, 780, .6 * back(ramp(f, d0, d0 + 8)))
    num(c, 'VALE O TÍTULO?', 640, 1600, f, ti, 100, -3)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'arbitragem') - 3, 140, 1.0)
    s.ting(s.W(1, 'Daronco') - 3, .3)
    s.thunk(s.W(2, 'reclamou') - 3, 160, .8)
    s.thunk(s.W(2, 'penalti') - 4, 120, .9)
    s.ting(s.W(3, 'Klein') - 3, .3)
    s.thunk(s.W(4, 'manteve') - 3, 200, .9)
    s.ting(s.W(5, 'lidera') - 3, .3)
    s.thunk(s.W(6, 'titulo') - 3, 140, .9)
