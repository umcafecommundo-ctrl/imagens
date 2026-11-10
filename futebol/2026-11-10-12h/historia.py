"""anima.futebol — 10/11/2026 12h — Brasileirão: Grêmio, finalista da Copa do Brasil, está na zona de rebaixamento.
Fontes (conferidas em 10/11/2026): Portal do Gremista 10/11 (Grêmio 18º, 37 pts, Inter 1 ponto à frente e 1º fora da zona;
faltam Bahia (18/11, Arena), Santos, Corinthians e Mirassol; final da Copa do Brasil x Palmeiras 06/12 em Brasília);
Revista Oeste/Chance de Gol 06/11 (após 34 jogos: Grêmio 18º 37 pts, Corinthians 37 à frente pelo saldo, Inter 38;
risco de queda do Grêmio 47,5%); ValorFinal 10/11 (após a 34ª rodada: Chapecoense 21 pts rebaixada, Remo 29 pts;
Grêmio maior risco, 55,4%); Hoop78 (tabela: 18/11 Grêmio x Bahia, 21/11 Santos x Grêmio, 28/11 Corinthians x Grêmio,
02/12 Grêmio x Mirassol). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  RETA FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Grêmio está na final da Copa do Brasil, e ao mesmo tempo na zona de rebaixamento do Brasileirão.",
    "Na pausa da Data Fifa, o time gaúcho é o décimo oitavo colocado, com trinta e sete pontos.",
    "O Corinthians tem os mesmos trinta e sete, e o Internacional, primeiro fora da zona, só um a mais.",
    "Os simuladores dão ao Grêmio perto de cinquenta por cento de chance de cair.",
    "Faltam quatro jogos: Bahia, Santos, Corinthians, num confronto direto, e Mirassol.",
    "O primeiro é contra o Bahia, no dia dezoito, na Arena.",
    "E só quatro dias depois da última rodada, vem a final contra o Palmeiras, em Brasília.",
]
CAPTXT = [
    "O Grêmio está na final da Copa do Brasil, e ao mesmo|tempo na zona de rebaixamento do Brasileirão.",
    "Na pausa da Data Fifa, o time gaúcho|é o 18º colocado, com 37 pontos.",
    "O Corinthians tem os mesmos 37, e o Internacional,|primeiro fora da zona, só 1 a mais.",
    "Os simuladores dão ao Grêmio|perto de 50% de chance de cair.",
    "Faltam 4 jogos: Bahia, Santos,|Corinthians, num confronto direto, e Mirassol.",
    "O primeiro é contra o Bahia,|no dia 18, na Arena.",
    "E só 4 dias depois da última rodada,|vem a final contra o Palmeiras, em Brasília.",
]
FALA_TIKTOK = "O Grêmio escapa da queda? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'final', 4), (0, 'rebaixamento', 4), (1, 'oitavo', 4), (2, 'Corinthians', 4), (2, 'mais', 4),
         (3, 'cinquenta', 4), (4, 'Bahia', 4), (4, 'Mirassol', 4), (5, 'Arena', 4), (6, 'Palmeiras', 4)]

GRE, GRE_F = time_('GRÊMIO')
COR, COR_F = time_('CORINTHIANS')
INT, INT_F = time_('INTERNACIONAL')
BAH, BAH_F = time_('BAHIA')
PAL, PAL_F = time_('PALMEIRAS')
SAN, _ = time_('SANTOS')
MIR, _ = time_('MIRASSOL')
REM, _ = time_('REMO')
CHA, _ = time_('CHAPECOENSE')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    fi = wt(0, 'final') - 3; rb = wt(0, 'rebaixamento') - 3
    put_trofeu(c, 380, 1180, 440, f, fi)
    num(c, 'FINAL!', 400, 780, f, fi, 120, -5)
    num(c, 'Z4', 900, 960, f, rb, 220, 6)
    put_jog(c, 640, 2020, 900, f, 1, cores=GRE, faixa=GRE_F, arms='up' if f < rb else 'cheek',
            expr='grin' if f < rb else 'shock', skin=1)
    put_placa(c, 'GRÊMIO', GRE, 640, 1110, f, 2, 70, -3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, rb, .9)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    t0 = wt(1, 'Data') - 6
    linhas = [('16º', 'INTERNACIONAL', INT, '38', False), ('17º', 'CORINTHIANS', COR, '37', False),
              ('18º', 'GRÊMIO', GRE, '37', True), ('19º', 'REMO', REM, '29', False), ('20º', 'CHAPECOENSE', CHA, '21', False)]
    tabela(c, linhas, 640, 880, f, t0)
    zt = wt(1, 'oitavo') - 3
    if f >= zt:
        a = back(ramp(f, zt, zt + 8))
        num(c, 'ZONA DE QUEDA', 640, 730, f, zt, 90, -3)
    cy = lerp(1250, 1300, smooth(ramp(f, 0, 90)))
    return c, (640 + 14 * math.sin(f * .05), cy, lerp(1.0, 1.1, smooth(ramp(f, zt - 10, zt + 30))) * (1 + .0012 * f), 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    co = wt(2, 'Corinthians') - 3; it = wt(2, 'Internacional') - 3; ma = wt(2, 'mais') - 3
    put_jog(c, 320, 2020, 800, f, 7, cores=COR, faixa=COR_F, arms='cintura', expr='nervous', skin=2, hair='#111111', look=1)
    put_jog(c, 640, 2030, 840, f, 1, cores=GRE, faixa=GRE_F, arms='shrug', expr='nervous', skin=1)
    put_jog(c, 960, 2020, 800, f, 8, cores=INT, faixa=INT_F, arms='cintura', expr='stern', skin=0, look=-1)
    put_placa(c, 'CORINTHIANS', COR, 320, 1150, f, co, 40, -4)
    put_placa(c, 'GRÊMIO', GRE, 640, 1140, f, 0, 46, 2)
    put_placa(c, 'INTER', INT, 960, 1150, f, it, 50, 4)
    num(c, '37', 330, 960, f, wt(2, 'trinta') - 3, 150, -4)
    num(c, '37', 640, 960, f, wt(2, 'trinta') - 1, 150, 3)
    num(c, '38', 950, 960, f, ma, 150, -3)
    num(c, 'SÓ 1 PONTO!', 640, 730, f, ma + 4, 110, 3)
    x = lerp(600, 680, smooth(ramp(f, co - 6, ma + 6))) + 18 * math.sin(f * .05)
    k = kick(f, ma, .6)
    return c, (x, 1450 + k * 8 + 10 * math.sin(f * .04), 1.04 * (1 + .0015 * f), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    ci = wt(3, 'cinquenta') - 3; ca = wt(3, 'cair') - 3
    num(c, '50%', 640, 800, f, ci, 300, -4)
    num(c, 'DE CHANCE DE CAIR', 640, 1030, f, ca, 90, 3)
    put_jog(c, 640, 2030, 860, f, 1, cores=GRE, faixa=GRE_F, arms='cheek' if f >= ci else 'hang',
            expr='pained' if f >= ci else 'nervous', skin=1)
    k = kick(f, ci, 1.0)
    z = lerp(1.0, 1.18, smooth(ramp(f, 0, 90)))
    return c, (640, 1380 + k * 10, z, lerp(0, 3, smooth(ramp(f, ci, ci + 30))) + k), 'dusk'


def s4(f):
    c = estadio('day').copy()
    num(c, 'FALTAM 4', 640, 720, f, wt(4, 'Faltam') - 3, 150, -4)
    times = [('BAHIA', BAH, 'Bahia'), ('SANTOS', SAN, 'Santos'), ('CORINTHIANS', COR, 'Corinthians'), ('MIRASSOL', MIR, 'Mirassol')]
    for i, (n, cr, w) in enumerate(times):
        put_placa(c, n, cr, 560, 900 + i * 180, f, wt(4, w) - 3, 66, -3 if i % 2 else 3)
    cd = wt(4, 'confronto') - 3
    if f >= cd: num(c, 'DIRETO!', 1000, 1250, f, cd, 52, 8)
    put_jog(c, 300, 2040, 760, f, 1, cores=GRE, faixa=GRE_F, arms='point', expr='stern', skin=1, look=1)
    cy = lerp(1150, 1420, smooth(ramp(f, 0, wt(4, 'Mirassol') + 6)))
    return c, (640, cy, 1.08 * (1 + .0006 * f), 0), 'golden'


def s5(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    ba = wt(5, 'Bahia') - 3; ar = wt(5, 'Arena') - 4
    put_goleiro(c, f, BAH, BAH_F, arms='shrug' if f >= ar else 'hang', expr='shock' if f >= ar else 'nervous', skin=2, hair='#111111')
    d0 = wt(5, 'dezoito') - 3
    if f >= d0: paste_c(c, calendario('18', 'NOV'), 300, 900, .75 * back(ramp(f, d0, d0 + 8)))
    put_placa(c, 'BAHIA', BAH, 980, 760, f, ba, 66, 4)
    num(c, 'NA ARENA', 700, 1010, f, ar + 2, 90, -3)
    h = 860
    put_jog(c, 470, 1990, h, f, 1, cores=GRE, faixa=GRE_F, arms='up' if f >= ar + 8 else 'run', kick=pulse(f, ar - 5, 5),
            expr='grin' if f >= ar + 8 else 'stern', skin=1)
    rb = raio_bola(h)
    if f < ar - 5: bx, by, r = 620, 1990 - rb, rb
    else:
        t = ramp(f, ar - 5, ar + 3)
        bx, by, r = lerp(620, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    k = kick(f, ar)
    return c, (lerp(580, 700, smooth(ramp(f, 0, ar))), 1460 + k * 10, 1.1 * (1 + .0007 * f), k), 'golden'


def s6(f):
    c = estadio('dusk').copy()
    put_trofeu(c, 640, 1180, 560, f, 0)
    num(c, '4 DIAS DEPOIS', 640, 700, f, wt(6, 'quatro') - 3, 110, -3)
    d0 = wt(6, 'final') - 3
    if f >= d0: paste_c(c, calendario('06', 'DEZ'), 1030, 940, .7 * back(ramp(f, d0, d0 + 8)))
    pa = wt(6, 'Palmeiras') - 3
    put_jog(c, 300, 2040, 780, f, 1, cores=GRE, faixa=GRE_F, arms='cintura', expr='stern', skin=1, look=1)
    put_jog(c, 980, 2040, 780, f, 6, cores=PAL, faixa=PAL_F, arms='cintura', expr='smug', skin=0, look=-1)
    put_placa(c, 'GRÊMIO', GRE, 300, 1180, f, 0, 50, -3)
    put_placa(c, 'PALMEIRAS', PAL, 980, 1180, f, pa, 46, 3)
    num(c, 'BRASÍLIA', 640, 1560, f, wt(6, 'Brasilia') - 3, 110, 3)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1360, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.ting(s.W(0, 'final') - 3, .3)
    s.thunk(s.W(0, 'rebaixamento') - 3, 140, 1.0)
    s.thunk(s.W(1, 'oitavo') - 3, 160, .8)
    s.thunk(s.W(2, 'mais') - 3, 200, .6)
    s.thunk(s.W(3, 'cinquenta') - 3, 120, 1.0)
    s.thunk(s.W(4, 'confronto') - 3, 180, .7)
    s.thunk(s.W(5, 'Arena') - 4, 120, .9)
    s.ting(s.W(6, 'Brasilia') - 3, .3)
