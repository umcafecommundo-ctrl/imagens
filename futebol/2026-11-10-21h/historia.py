"""anima.futebol — 10/11/2026 21h — Brasileirão: Vitória contrata Rafael Lacerda, técnico da Chapecoense (já rebaixada).
Fontes (conferidas em 10/11/2026): A Crítica (Campo Grande) 10/11 (anúncio na terça 10/11, substitui Jair Ventura,
vinha da Chapecoense já rebaixada, contrato até dez/2027, Vitória 15º com 38 pts, 1 acima do Corinthians, 1º do Z4,
faltam 4 rodadas, venceu Corinthians, São Paulo e Fluminense com elenco mais fraco, estreia 19/11 x Bragantino no Barradão);
Tribuna do Sertão/Agência Estado 10/11 (mesmos fatos; estreia 19/11 x Bragantino no Barradão; 15º, 38 pts);
Interior da Bahia 10/11 (contrato até dez/2027; próximos jogos Bragantino, Internacional, Santos e Vasco).
Sem escudos/logos: times por plaquinhas e cores; técnicos como bonecos genéricos com placa do nome."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  RETA FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "A quatro rodadas do fim, o Vitória foi buscar o técnico do lanterna do Brasileirão.",
    "Nesta terça, o clube baiano anunciou Rafael Lacerda, que comandava a Chapecoense, já rebaixada.",
    "Ele chega no lugar de Jair Ventura.",
    "O motivo, segundo o presidente: mesmo com um elenco mais fraco, ele venceu Corinthians, São Paulo e Fluminense.",
    "E o contrato vai até o fim de dois mil e vinte e sete.",
    "O Vitória é o décimo quinto, com trinta e oito pontos, só um acima da zona de rebaixamento.",
    "A estreia é no dia dezenove, contra o Bragantino, no Barradão.",
    "Depois, ainda tem Internacional, Santos e Vasco pela frente.",
]
CAPTXT = [
    "A 4 rodadas do fim, o Vitória foi buscar|o técnico do lanterna do Brasileirão.",
    "Nesta terça, o clube baiano anunciou Rafael Lacerda,|que comandava a Chapecoense, já rebaixada.",
    "Ele chega no lugar|de Jair Ventura.",
    "O motivo, segundo o presidente: mesmo com um elenco mais fraco,|ele venceu Corinthians, São Paulo e Fluminense.",
    "E o contrato vai|até o fim de 2027.",
    "O Vitória é o 15º, com 38 pontos,|só 1 acima da zona de rebaixamento.",
    "A estreia é no dia 19, contra|o Bragantino, no Barradão.",
    "Depois, ainda tem Internacional,|Santos e Vasco pela frente.",
]
FALA_TIKTOK = "O Vitória escapa da queda? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'lanterna', 4), (1, 'Lacerda', 4), (1, 'rebaixada', 4), (2, 'Ventura', 4), (3, 'Corinthians', 4),
         (3, 'Fluminense', 4), (4, 'sete', 4), (5, 'quinto', 4), (5, 'rebaixamento', 4), (6, 'Bragantino', 4),
         (6, 'Barradao', 4), (7, 'Vasco', 4)]

VI, VI_F = time_('VITÓRIA')
CH, CH_F = time_('CHAPECOENSE')
COR, COR_F = time_('CORINTHIANS')
INT, INT_F = time_('INTERNACIONAL')
GRE, GRE_F = time_('GRÊMIO')
BRA, BRA_F = time_('BRAGANTINO')
SAN, _ = time_('SANTOS')
VAS, _ = time_('VASCO')
SPA, _ = time_('SÃO PAULO')
FLUc, _ = time_('FLUMINENSE')
TEC = dict(skin=1, hair='#3a2a1c')   # técnico genérico (boneco), nome só na placa


def s0(f):
    c = estadio('dusk').copy()
    vi = wt(0, 'Vitoria') - 3; la = wt(0, 'lanterna') - 3
    num(c, 'FALTAM 4', 640, 720, f, wt(0, 'quatro') - 3, 130, -4)
    put_jog(c, 330, 2020, 820, f, 3, cores=VI, faixa=VI_F, arms='point', expr='stern', skin=2, hair='#111111', look=1)
    put_placa(c, 'VITÓRIA', VI, 330, 1110, f, vi, 60, -3)
    put_jog(c, 930, 2030, 840, f, 1, cores=CH, faixa=CH_F, arms='hang', expr='shock' if f >= la else 'neutral', **TEC)
    num(c, 'LANTERNA', 930, 960, f, la, 100, 5)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, la, .8)
    return c, (lerp(560, 700, smooth(ramp(f, 0, la + 10))), 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('day').copy()
    t0 = wt(1, 'terca') - 3; la = wt(1, 'Lacerda') - 3; ch = wt(1, 'Chapecoense') - 3; rb = wt(1, 'rebaixada') - 3
    if f >= t0: paste_c(c, calendario('10', 'NOV'), 960, 960, .62 * back(ramp(f, t0, t0 + 8)))
    put_jog(c, 520, 2030, 860, f, 1, cores=CH, faixa=CH_F, arms='cintura', expr='neutral', **TEC)
    put_placa(c, 'RAFAEL LACERDA', CH, 600, 760, f, la, 62, -3)
    put_placa(c, 'CHAPECOENSE', CH, 520, 1130, f, ch, 54, 3)
    num(c, 'REBAIXADA', 880, 1250, f, rb, 70, 5)
    cy = lerp(1300, 1420, smooth(ramp(f, 0, 90)))
    return c, (640 + 14 * math.sin(f * .05), cy, 1.06 * (1 + .001 * f), 0), 'golden'


def s2(f):
    c = estadio('day').copy()
    ve = wt(2, 'Ventura') - 3; lu = wt(2, 'lugar') - 3
    xo = lerp(330, -200, smooth(ramp(f, ve + 4, ve + 40)))
    put_jog(c, xo, 2010, 800, f, 5, flip=True, cores=VI, faixa=VI_F, arms='hang', expr='nervous', skin=0, hair='#5a4a3a',
            walk=(f * .06) % 1 if f > ve + 4 else 0)
    put_placa(c, 'JAIR VENTURA', VI, max(xo, 390), 1110, f, ve, 44, -3)
    xi = lerp(1300, 860, smooth(ramp(f, lu - 6, lu + 18)))
    put_jog(c, xi, 2030, 840, f, 1, flip=True, cores=VI, faixa=VI_F, arms='joinha' if f > lu + 18 else 'run',
            walk=0 if f > lu + 18 else (f * .07) % 1, expr='grin', **TEC)
    put_placa(c, 'LACERDA', VI, xi, 1130, f, lu + 12, 56, 3)
    num(c, 'SAI', 380, 780, f, ve + 2, 110, -5)
    num(c, 'ENTRA', 880, 780, f, lu, 110, 4)
    return c, (640 + 12 * math.sin(f * .06), 1430, 1.04 * (1 + .0015 * f), 0), 'day'


def s3(f):
    c = estadio('dusk').copy()
    fr = wt(3, 'fraco') - 3
    num(c, 'ELENCO MAIS FRACO', 640, 720, f, fr, 82, -3)
    for i, (n, cr, w) in enumerate((('CORINTHIANS', COR, 'Corinthians'), ('SÃO PAULO', SPA, 'Sao'), ('FLUMINENSE', FLUc, 'Fluminense'))):
        put_placa(c, n, cr, 860, 900 + i * 170, f, wt(3, w) - 3, 56, 3 if i % 2 else -3)
    vc = wt(3, 'venceu') - 3
    put_jog(c, 330, 2030, 860, f, 1, cores=CH, faixa=CH_F, arms='up' if f >= vc else 'cintura',
            expr='grin' if f >= vc else 'stern', **TEC)
    num(c, 'VENCEU!', 400, 1060, f, vc, 80, -5)
    k = kick(f, vc, .7)
    cy = lerp(1250, 1420, smooth(ramp(f, 0, wt(3, 'Fluminense') + 6)))
    return c, (640, cy + k * 8, 1.06 * (1 + .0008 * f), k), 'dusk'


def s4(f):
    c = estadio('day').copy()
    co = wt(4, 'contrato') - 3; se = wt(4, 'sete') - 3
    num(c, 'CONTRATO', 640, 740, f, co, 100, -3)
    num(c, 'ATÉ 2027', 640, 930, f, se, 140, 3)
    put_jog(c, 640, 2030, 880, f, 1, cores=VI, faixa=VI_F, arms='joinha', expr='proud', **TEC)
    put_placa(c, 'LACERDA', VI, 640, 1190, f, 0, 52, -2)
    z = lerp(1.0, 1.16, smooth(ramp(f, 0, 70)))
    k = kick(f, se, .7)
    return c, (640, 1400 + k * 8, z, k), 'golden'


def s5(f):
    c = estadio('dusk').copy()
    t0 = wt(5, 'Vitoria') - 4
    linhas = [('15º', 'VITÓRIA', VI, '38', True), ('16º', 'INTERNACIONAL', INT, '38', False),
              ('17º', 'CORINTHIANS', COR, '37', False), ('18º', 'GRÊMIO', GRE, '37', False)]
    tabela(c, linhas, 640, 900, f, t0)
    zt = wt(5, 'rebaixamento') - 3
    num(c, 'ZONA DE QUEDA', 640, 1640, f, zt, 90, -3)
    num(c, 'SÓ 1 PONTO!', 640, 740, f, wt(5, 'um') - 3, 100, 3)
    cy = lerp(1180, 1330, smooth(ramp(f, 0, zt + 10)))
    return c, (640 + 14 * math.sin(f * .05), cy, lerp(1.0, 1.08, smooth(ramp(f, zt - 10, zt + 30))) * (1 + .001 * f),
               lerp(0, 2, smooth(ramp(f, zt, zt + 30)))), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    br = wt(6, 'Bragantino') - 3; ba = wt(6, 'Barradao') - 4
    put_goleiro(c, f, BRA, BRA_F, arms='shrug' if f >= ba else 'hang', expr='shock' if f >= ba else 'nervous', skin=0)
    d0 = wt(6, 'dezenove') - 3
    if f >= d0: paste_c(c, calendario('19', 'NOV'), 280, 960, .72 * back(ramp(f, d0, d0 + 8)))
    put_placa(c, 'BRAGANTINO', BRA, 880, 940, f, br, 54, 4)
    num(c, 'BARRADÃO', 640, 750, f, ba + 2, 96, -3)
    h = 860
    put_jog(c, 470, 1990, h, f, 3, cores=VI, faixa=VI_F, arms='up' if f >= ba + 8 else 'run', kick=pulse(f, ba - 5, 5),
            expr='grin' if f >= ba + 8 else 'stern', skin=2, hair='#111111')
    rb = raio_bola(h)
    if f < ba - 5: bx, by, r = 620, 1990 - rb, rb
    else:
        t = ramp(f, ba - 5, ba + 3)
        bx, by, r = lerp(620, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    k = kick(f, ba)
    return c, (lerp(580, 700, smooth(ramp(f, 0, ba))), 1460 + k * 10, 1.1 * (1 + .0007 * f), k), 'dusk'


def s7(f):
    c = estadio('dusk').copy()
    for i, (n, cr, w) in enumerate((('INTERNACIONAL', INT, 'Internacional'), ('SANTOS', SAN, 'Santos'), ('VASCO', VAS, 'Vasco'))):
        put_placa(c, n, cr, 640, 820 + i * 180, f, wt(7, w) - 3, 70, 3 if i % 2 else -3)
    put_jog(c, 300, 2040, 760, f, 1, cores=VI, faixa=VI_F, arms='cintura', expr='stern', look=1, **TEC)
    put_jog(c, 980, 2040, 760, f, 3, cores=VI, faixa=VI_F, arms='cintura', expr='stern', skin=2, hair='#111111', look=-1)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, lerp(1200, 1380, smooth(ramp(f, 0, 70))), z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'lanterna') - 3, 140, 1.0)
    s.ting(s.W(1, 'Lacerda') - 3, .3)
    s.thunk(s.W(1, 'rebaixada') - 3, 160, .7)
    s.thunk(s.W(3, 'venceu') - 3, 200, .6)
    s.ting(s.W(4, 'sete') - 3, .3)
    s.thunk(s.W(5, 'rebaixamento') - 3, 120, 1.0)
    s.thunk(s.W(6, 'Barradao') - 4, 120, .9)
