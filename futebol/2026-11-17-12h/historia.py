"""anima.futebol — 17/11/2026 12h — Seleção Brasileira: Brasil 7x0 Singapura, último jogo de 2026.
Fontes (conferidas em 17/11/2026): CBF (7x0, Vini Jr. 3 gols, Endrick, Estêvão, Rayan, Allan; maior goleada desde o
8x0 sobre a China em 10/09/2012; último jogo de 2026, próximo compromisso na Data Fifa de março); Metro 1 (Estádio Nacional
de Singapura, 4x0 no intervalo, Vini 8', 14', 20', Endrick 30', Estêvão 5' do 2º T, Rayan 19' do 2º T, Allan 28' do 2º T;
recuperação após o 3x2 do Japão); Bolavip (Vini 9', 15', 21', Endrick 31', 4x0 no intervalo); GC Mais (maior goleada desde
o 8x0 na China em 2012, segundo a CBF; gol de Allan).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Brasil goleou Singapura por sete a zero e fechou o ano com festa.",
    "Foi hoje de manhã, no Estádio Nacional de Singapura, três dias depois da derrota para o Japão.",
    "Vini Júnior fez três gols em vinte minutos, ainda no primeiro tempo.",
    "Endrick ampliou com um chute rasteiro, e o Brasil foi para o intervalo com quatro a zero.",
    "No segundo tempo, Estêvão, Rayan e Allan completaram a goleada.",
    "É a maior goleada da Seleção desde o oito a zero sobre a China, em dois mil e doze.",
    "Agora, a Seleção só volta a campo em março.",
]
CAPTXT = [
    "O Brasil goleou Singapura por 7 a 0|e fechou o ano com festa.",
    "Foi hoje de manhã, no Estádio Nacional de Singapura,|3 dias depois da derrota para o Japão.",
    "Vini Júnior fez 3 gols em 20 minutos,|ainda no primeiro tempo.",
    "Endrick ampliou com um chute rasteiro, e o Brasil|foi para o intervalo com 4 a 0.",
    "No segundo tempo, Estêvão, Rayan e Allan|completaram a goleada.",
    "É a maior goleada da Seleção desde o 8 a 0|sobre a China, em 2012.",
    "Agora, a Seleção só volta a campo em março.",
]
FALA_TIKTOK = "Que nota você dá pro Vini? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "NOTA PRO VINI?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'sete', 6), (1, 'Japao', 4), (2, 'tres', 6), (3, 'quatro', 6), (4, 'Allan', 6), (5, 'oito', 4),
         (6, 'marco', 4)]

BRA, BRA_F = time_('BRASIL')
SIN, SIN_F = time_('SINGAPURA')
CHI, CHI_F = time_('CHINA')
JAP, JAP_F = time_('JAPÃO')
GKS = ('#2fa35a', '#111111', '#111111')   # goleiro de Singapura (genérico)


def br(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=BRA, faixa=BRA_F, hair='#111111', sock='#ffffff', **kw)


def sg(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=SIN, faixa=SIN_F, hair='#111111', sock='#d4282c', **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f) if t < 1 else None
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def chute_gol(c, f, kf, sx, h, gx, gy, alvo=(90, 0), arco=160):
    rb = raio_bola(h)
    bola_voo(c, f, kf, sx + h * .13, 2030 - rb, gx + alvo[0], gy + alvo[1], rb, raio_bola(300), arco)


def gol_txt(c, f, f0, x=640, y=880, s='GOL!', cor=(255, 216, 74), size=150):
    explosao(c, x, y, f, f0, 260, cor)
    num(c, s, x, y, f, f0 + 2, size, -4)


def put_cal(c, dia, x, y, s, f, f0, mes='NOV'):
    if f >= f0: paste_c(c, calendario(dia, mes), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    se = wt(0, 'sete') - 3; fe = wt(0, 'festa') - 3
    sg(c, 300, 1700, 520, f, 11, arms='cheek', expr='pained')
    sg(c, 990, 1690, 500, f, 12, arms='cheek', expr='pained', skin=0, flip=True)
    x = lerp(1250, 620, easeOut(ramp(f, 0, 22)))
    if f < 24: linhas_vel(c, x, 2050, 900, f, dir=1)
    br(c, x, 2050, 900, f, 6, arms='aviao', expr='grin', run=(f * .08) % 1 if f < 22 else -1, num_='7', flip=True)
    if f < se: put_placa(c, 'BRASIL', BRA, 640, 820, f, 4, 80, -3)
    if f >= se:
        confete(c, 640, 900, f, se, 90, 900)
        explosao(c, 640, 860, f, se, 220)
        num(c, '7 x 0', 640, 860, f, se + 2, 170, -3)
    if f >= fe: num(c, 'FIM DE ANO COM FESTA', 640, 1060, f, fe, 80, 3)
    z = lerp(1.22, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, se, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('day').copy()
    ma = wt(1, 'manha') - 3; es = wt(1, 'Estadio') - 3; ja = wt(1, 'Japao') - 3
    xe = lerp(-250, 340, easeOut(ramp(f, 0, 18)))
    xs = lerp(1500, 920, easeOut(ramp(f, 0, 18)))
    br(c, xe, 2000, 840, f, 21, arms='cintura', expr='stern', look=1, run=(f * .09) % 1 if f < 18 else None, num_='10')
    sg(c, xs, 2000, 840, f, 22, arms='cintura', expr='stern', look=-1, flip=True, run=(f * .09) % 1 if f < 18 else None, num_='4')
    put_placa(c, 'BRASIL', BRA, 340, 1080, f, 6, 64, -3)
    put_placa(c, 'SINGAPURA', SIN, 920, 1080, f, 8, 56, 3)
    if f < ja:
        put_cal(c, '17', 640, 760, .45, f, ma)
        num(c, 'ESTÁDIO NACIONAL', 640, 935, f, es, 76, 3)
    else:
        explosao(c, 640, 800, f, ja, 200, (255, 120, 120))
        num(c, '3 DIAS APÓS O 3 x 2', 640, 800, f, ja + 2, 76, -3)
        put_placa(c, 'JAPÃO', JAP, 640, 940, f, ja + 4, 56, 3)
    z = lerp(1.0, 1.1, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .04), 1420, z, 0), 'golden'


def _k2():
    k1 = 12; k2 = k1 + 26; k3 = k2 + 26
    return k1, k2, k3


def s2(f):
    c = estadio2('dusk').copy()
    vi = wt(2, 'Vini') - 3
    ks = _k2()
    est = max(pulse(f, k + 9, 6) for k in ks)
    gx, gy = put_gol2(c, x=720, estufa=est)
    i = 0 if f < ks[1] - 10 else (1 if f < ks[2] - 10 else 2)
    k = ks[i]; k0 = ks[i - 1] + 16 if i else 0
    put_goleiro(c, f, GKS, None, gx=740 + (60 if f > k + 5 else 0) * (-1 if i == 1 else 1), arms='up', expr='shock', skin=1)
    if i == 1:
        x = lerp(1450, 900, easeOut(ramp(f, k0, k - 3)))
        if f < k - 4: linhas_vel(c, x, 2030, 860, f, dir=1)
        br(c, x, 2030, 860, f, 2, arms='run' if f < k + 6 else 'aviao', run=(f * .09) % 1 if f < k - 4 else None,
           kick=pulse(f, k - 4, 5) if f >= k - 4 else 0, expr='grin', num_='7', flip=True)
        rb = raio_bola(860)
        bola_voo(c, f, k, x - 110, 2030 - rb, gx + 40, gy - 10, rb, raio_bola(300), 140)
    else:
        x = lerp(-200, 340, easeOut(ramp(f, k0, k - 3)))
        if f < k - 4: linhas_vel(c, x, 2030, 860, f)
        br(c, x, 2030, 860, f, 2, arms='run' if f < k + 6 else 'punho', run=(f * .09) % 1 if f < k - 4 else None,
           kick=pulse(f, k - 4, 5) if f >= k - 4 else 0, expr='grin', num_='7')
        chute_gol(c, f, k, x, 860, gx, gy, alvo=(110, -10))
    put_placa(c, 'VINI JR.', BRA, 640, 1270, f, max(0, vi), 60, -3)
    for j, kk in enumerate(ks):
        if kk + 9 <= f < (ks[j + 1] - 10 if j < 2 else 10 ** 6):
            gol_txt(c, f, kk + 9, 640, 860, ('GOL!', 'DE NOVO!', '3 EM 20 MIN!')[j], size=(150, 140, 120)[j])
    kk = sum(kick(f, x_ + 9, .8) for x_ in ks)
    return c, (lerp(600, 680, smooth(f / 120)), 1430 + kk * 10, 1.05 * (1 + .0008 * f), kk), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    en = wt(3, 'Endrick') - 3; iv = wt(3, 'intervalo') - 3
    kf = max(16, wt(3, 'rasteiro') - 2)
    gx, gy = put_gol2(c, x=740, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKS, None, gx=760 - 60 * clamp((f - kf) / 7), arms='up', expr='shock' if f >= kf + 5 else 'nervous', skin=1)
    x = lerp(-200, 340, easeOut(ramp(f, 0, kf - 3)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
    br(c, x, 2030, 860, f, 8, arms='run' if f < kf + 6 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
       kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='9', hs='topete', skin=2)
    chute_gol(c, f, kf, x, 860, gx, gy, alvo=(100, 30), arco=30)
    if f < iv: put_placa(c, 'ENDRICK', BRA, 960, 1240, f, en, 56, 3)
    if kf + 9 <= f < iv: gol_txt(c, f, kf + 9, 640, 800, 'GOL!')
    if f >= iv: gol_txt(c, f, iv, 640, 780, '4 x 0', size=160); num(c, 'NO INTERVALO', 640, 960, f, iv + 3, 90, 3)
    k = kick(f, kf + 9) + kick(f, iv, .6)
    return c, (lerp(600, 660, smooth(f / 60)), 1430 + k * 10, 1.05, k), 'dusk'


def _k4():
    return wt(4, 'Estevao') + 4, wt(4, 'Rayan') + 4, wt(4, 'Allan') + 4


def s4(f):
    c = estadio2('dusk').copy()
    se = wt(4, 'segundo') - 3
    ks = _k4()
    est = max(pulse(f, k + 9, 6) for k in ks)
    gx, gy = put_gol2(c, x=640, estufa=est)
    put_goleiro(c, f, GKS, None, gx=660, arms='up', expr='shock', skin=1)
    P = ((250, 'ESTÊVÃO', '41', 'curto', 1), (640, 'RAYAN', '20', 'cacheado', 3), (1030, 'ALLAN', '8', 'raspado', 2))
    for j, (x, nome, n, hs, sk) in enumerate(P):
        k = ks[j]
        br(c, x, 2030, 780, f, 30 + j, arms='punho' if f >= k + 6 else 'run', expr='grin', num_=n, hs=hs, skin=sk,
           kick=pulse(f, k - 4, 5) if f >= k - 4 else 0, flip=x > 700)
        put_placa(c, nome, BRA, x, 1170 + (60 if j == 1 else 0), f, k - 6, 50, (-3, 2, 3)[j])
        if k - 2 <= f < k + 12:
            rb = raio_bola(780)
            bola_voo(c, f, k, x + (60 if x < 700 else -60), 2030 - rb, gx + 40, gy, rb, raio_bola(300), 120)
    if f < ks[0] + 9: num(c, '2º TEMPO', 640, 760, f, se, 120, -3)
    for j, k in enumerate(ks):
        if k + 9 <= f < (ks[j + 1] + 9 if j < 2 else 10 ** 6):
            gol_txt(c, f, k + 9, 640, 800, '%d x 0' % (5 + j), size=160)
    if f >= ks[2] + 9: confete(c, 640, 800, f, ks[2] + 9, 80, 900)
    kk = sum(kick(f, k + 9, .7) for k in ks)
    return c, (640 + 20 * math.sin(f * .05), 1430 + kk * 10, lerp(1.05, 1.0, smooth(f / 80)), kk), 'dusk'


def s5(f):
    c = estadio2('golden').copy()
    mg = wt(5, 'maior') - 3; oi = wt(5, 'oito') - 3; ch = wt(5, 'China') - 3; an = wt(5, 'doze') - 3
    br(c, 330, 2010, 840, f, 3, arms='joinha' if f >= mg else 'cintura', expr='proud', look=1, num_='10')
    if f >= ch - 8:
        sx = lerp(1550, 940, easeOut(ramp(f, ch - 8, ch + 4)))
        put_atleta(c, sx, 2010, 840, f, 7, cores=CHI, faixa=CHI_F, hair='#111111', sock='#d4282c', skin=0,
                   arms='cheek', expr='pained', look=-1, flip=True)
        put_placa(c, 'CHINA', CHI, 940, 1150, f, ch, 60, 3)
    put_placa(c, 'BRASIL', BRA, 330, 1150, f, oi - 4, 60, -3)
    if f < oi: num(c, 'MAIOR GOLEADA', 640, 780, f, mg, 120, -3)
    else:
        explosao(c, 640, 800, f, oi, 220)
        num(c, '8 x 0', 640, 800, f, oi + 2, 170, -3)
    num(c, 'EM 2012', 640, 990, f, an, 110, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0008 * f)
    k = kick(f, oi, .7)
    return c, (640 + 20 * math.sin(f * .04), 1430 + k * 8, z, k), 'golden'


def s6(f):
    c = estadio2('dusk').copy()
    vo = wt(6, 'volta') - 3; ma = wt(6, 'marco') - 3
    bx = lerp(-300, 400, easeOut(ramp(f, 0, 16)))
    br(c, bx, 2010, 860, f, 3, arms='cintura' if f < ma else 'joinha', expr='proud', look=1,
       run=(f * .09) % 1 if f < 16 else None, num_='7')
    put_placa(c, 'BRASIL', BRA, 400, 1120, f, 6, 64, -3)
    put_cal(c, 'MAR', 900, 1000, .55, f, vo, '2027')
    if f >= ma: num(c, 'SÓ EM MARÇO', 640, 760, f, ma, 120, -3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ma, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'BRA', 'SIN', 7, 0, BRA, SIN, 'FIM', lf)
    elif si == 2:
        ks = _k2(); g = sum(lf >= k + 9 for k in ks)
        im = placar_tv(im, 'BRA', 'SIN', g, 0, BRA, SIN, '1º T', lf + 99, pulse_a=max([k + 9 for k in ks if lf >= k + 9] or [-1]))
    elif si == 3:
        kf = max(16, wt(3, 'rasteiro') - 2) + 9
        im = placar_tv(im, 'BRA', 'SIN', 3 + int(lf >= kf), 0, BRA, SIN, '1º T', lf + 99, pulse_a=kf)
    elif si == 4:
        ks = _k4(); g = sum(lf >= k + 9 for k in ks)
        im = placar_tv(im, 'BRA', 'SIN', 4 + g, 0, BRA, SIN, '2º T', lf + 99, pulse_a=max([k + 9 for k in ks if lf >= k + 9] or [-1]))
    D = {0: ('BRASIL 7 x 0 SINGAPURA', 'ÚLTIMO JOGO DE 2026', 4),
         1: ('ESTÁDIO NACIONAL', 'HOJE DE MANHÃ, EM SINGAPURA', wt(1, 'Estadio') - 3),
         2: ('VINI JR. FAZ 3', 'TUDO NOS PRIMEIROS 20 MINUTOS', _k2()[2] + 14),
         3: ('ENDRICK AMPLIA', '4 x 0 NO INTERVALO', wt(3, 'intervalo') - 3),
         4: ('ESTÊVÃO, RAYAN E ALLAN', 'COMPLETAM A GOLEADA', _k4()[2] + 14),
         5: ('MAIOR GOLEADA DESDE 2012', 'NO 8 x 0 SOBRE A CHINA', wt(5, 'China') - 3),
         6: ('PRÓXIMA DATA FIFA', 'SÓ EM MARÇO DE 2027', wt(6, 'marco') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'sete') - 3, 150, .8)
    s.ting(s.W(1, 'Japao') - 3, .3)
    for k in _k2(): s.thunk(k + 9, 140, .7)
    s.thunk(max(16, s.W(3, 'rasteiro') - 2) + 9, 150, .8)
    for k in (s.W(4, 'Estevao') + 4, s.W(4, 'Rayan') + 4, s.W(4, 'Allan') + 4): s.thunk(k + 9, 140, .7)
    s.ting(s.W(5, 'oito') - 3, .35)
    s.ting(s.W(6, 'marco') - 3, .3)
