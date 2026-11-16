"""anima.futebol — 16/11/2026 21h — Nations League: Alemanha 5x0 Holanda no Estádio Olímpico de Berlim.
Fontes (conferidas em 16/11/2026): CNN Brasil (5x0 no Olímpico de Berlim, última rodada do Grupo A2, Klopp técnico,
Scherhant no fim do 1º tempo, Schlotterbeck, Gruda e Wirtz 2; Alemanha líder e classificada; mata-mata a partir de março, por sorteio);
AP/WSLS (5-0 em Berlim, Klopp; Scherhant antes do intervalo, Wirtz 60' e 71', Schlotterbeck ~65', Gruda 77'; Alemanha nas quartas);
ESPN (Germany 5-0 Netherlands, 16/11/2026); Sportbuzz e Metrópoles (goleada, Alemanha avança como líder).
"""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'NATIONS LEAGUE  ·  6ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "A Alemanha de Jürgen Klopp atropelou a Holanda: cinco a zero, em Berlim.",
    "Foi na última rodada da Nations League, no Estádio Olímpico, valendo o primeiro lugar do grupo.",
    "Scherhant abriu o placar no fim do primeiro tempo.",
    "No segundo tempo, Florian Wirtz apareceu e fez dois gols.",
    "O zagueiro Schlotterbeck, de cabeça, e Brajan Gruda completaram a goleada.",
    "Com a vitória, a Alemanha terminou em primeiro no grupo e está nas quartas.",
    "Os confrontos saem por sorteio, e o mata-mata só começa em março.",
]
CAPTXT = [
    "A Alemanha de Jürgen Klopp atropelou a Holanda:|5 a 0, em Berlim.",
    "Foi na última rodada da Nations League, no Estádio Olímpico,|valendo o 1º lugar do grupo.",
    "Scherhant abriu o placar|no fim do primeiro tempo.",
    "No segundo tempo, Florian Wirtz|apareceu e fez 2 gols.",
    "O zagueiro Schlotterbeck, de cabeça,|e Brajan Gruda completaram a goleada.",
    "Com a vitória, a Alemanha terminou em 1º no grupo|e está nas quartas.",
    "Os confrontos saem por sorteio,|e o mata-mata só começa em março.",
]
FALA_TIKTOK = "A Alemanha do Klopp é favorita? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'cinco', 6), (1, 'primeiro', 4), (2, 'Scherhant', 6), (3, 'dois', 6), (4, 'cabeca', 6), (5, 'quartas', 4),
         (6, 'marco', 4)]

ALE, ALE_F = time_('ALEMANHA')
HOL, HOL_F = time_('HOLANDA')
GKA = ('#2fa35a', '#111111', '#111111')
GKH = ('#f2c94c', '#111111', '#111111')


def al(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 0); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=ALE, faixa=ALE_F, hair='#6a4a2a', sock='#ffffff', **kw)


def ho(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=HOL, faixa=HOL_F, hair='#2a1a10', sock='#f36c21', **kw)


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


def gol_txt(c, f, f0, x=640, y=880, s='GOL!', cor=(255, 216, 74)):
    explosao(c, x, y, f, f0, 260, cor)
    num(c, s, x, y, f, f0 + 2, 150, -4)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    kl = wt(0, 'Klopp') - 3; ci = wt(0, 'cinco') - 3; be = wt(0, 'Berlim') - 3
    ho(c, 300, 1700, 520, f, 11, arms='cheek', expr='pained')
    ho(c, 990, 1690, 500, f, 12, arms='cheek', expr='pained', skin=2, hs='cacheado', flip=True)
    x = lerp(1250, 620, easeOut(ramp(f, 0, 22)))
    if f < 24: linhas_vel(c, x, 2050, 900, f, dir=1)
    al(c, x, 2050, 900, f, 6, arms='aviao', expr='grin', run=(f * .08) % 1 if f < 22 else -1, num_='10', flip=True)
    if f < ci: put_placa(c, 'KLOPP', ALE, 640, 820, f, kl, 80, -3)
    if f >= ci:
        confete(c, 640, 900, f, ci, 90, 900)
        explosao(c, 640, 860, f, ci, 220)
        num(c, '5 x 0', 640, 860, f, ci + 2, 160, -3)
    if f >= be: num(c, 'BERLIM', 640, 1060, f, be, 90, 3)
    z = lerp(1.22, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ci, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    ol = wt(1, 'Olimpico') - 3; pr = wt(1, 'primeiro') - 3
    xe = lerp(-250, 340, easeOut(ramp(f, 0, 18)))
    xs = lerp(1500, 920, easeOut(ramp(f, 0, 18)))
    al(c, xe, 2000, 840, f, 21, arms='cintura', expr='stern', look=1, run=(f * .09) % 1 if f < 18 else None, num_='17')
    ho(c, xs, 2000, 840, f, 22, arms='cintura', expr='stern', look=-1, flip=True, run=(f * .09) % 1 if f < 18 else None, num_='4', skin=2)
    put_placa(c, 'ALEMANHA', ALE, 340, 1080, f, 6, 64, -3)
    put_placa(c, 'HOLANDA', HOL, 920, 1080, f, 8, 64, 3)
    if f < pr: num(c, 'OLÍMPICO', 640, 760, f, ol, 110, -2)
    if f >= pr:
        explosao(c, 640, 900, f, pr, 200)
        num(c, '1º LUGAR', 640, 900, f, pr + 2, 110, 3)
    z = lerp(1.0, 1.1, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .04), 1420, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    sc = wt(2, 'Scherhant') - 3
    kf = max(14, wt(2, 'placar') - 2)
    gx, gy = put_gol2(c, x=740, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKH, None, gx=760 - 60 * clamp((f - kf) / 7), arms='up', expr='shock' if f >= kf + 5 else 'nervous', skin=0)
    x = lerp(-200, 340, easeOut(ramp(f, 0, kf - 3)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
    al(c, x, 2030, 860, f, 8, arms='run' if f < kf + 6 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
       kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='11', hs='topete')
    chute_gol(c, f, kf, x, 860, gx, gy)
    put_placa(c, 'SCHERHANT', ALE, 920, 1150, f, sc, 60, 3)
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, '1 x 0')
    k = kick(f, kf + 9)
    return c, (lerp(600, 660, smooth(f / 60)), 1430 + k * 10, 1.05, k), 'dusk'


def _k3():
    k1 = max(16, wt(3, 'Wirtz') + 2); k2 = max(k1 + 24, wt(3, 'dois') - 2)
    return k1, k2


def s3(f):
    c = estadio2('dusk').copy()
    wi = wt(3, 'Florian') - 3
    k1, k2 = _k3()
    est = max(pulse(f, k1 + 9, 6) * (f < k1 + 18), pulse(f, k2 + 9, 6))
    gx, gy = put_gol2(c, x=720, estufa=est)
    put_goleiro(c, f, GKH, None, gx=740 + (60 if k1 + 6 < f < k1 + 18 else 0) + (-60 if f > k2 + 6 else 0),
                arms='up', expr='shock', skin=0)
    if f < k1 + 18:
        x = lerp(-200, 330, easeOut(ramp(f, 0, k1 - 3)))
        if f < k1 - 4: linhas_vel(c, x, 2030, 860, f)
        al(c, x, 2030, 860, f, 9, arms='run' if f < k1 + 6 else 'punho', run=(f * .09) % 1 if f < k1 - 4 else None,
           kick=pulse(f, k1 - 4, 5) if f >= k1 - 4 else 0, expr='grin', num_='10', hs='curto')
        chute_gol(c, f, k1, x, 860, gx, gy, alvo=(120, -10))
        if f >= k1 + 9: gol_txt(c, f, k1 + 9, 640, 860, 'GOL!')
    else:
        x = lerp(1450, 900, easeOut(ramp(f, k1 + 18, k2 - 3)))
        if f < k2 - 4: linhas_vel(c, x, 2030, 860, f, dir=1)
        al(c, x, 2030, 860, f, 9, arms='run' if f < k2 + 6 else 'aviao', run=(f * .09) % 1 if f < k2 - 4 else None,
           kick=pulse(f, k2 - 4, 5) if f >= k2 - 4 else 0, expr='grin', num_='10', hs='curto', flip=True)
        rb = raio_bola(860)
        bola_voo(c, f, k2, x - 110, 2030 - rb, gx + 40, gy - 10, rb, raio_bola(300), 140)
        if f >= k2 + 9: gol_txt(c, f, k2 + 9, 640, 860, 'DOIS DELE!')
    put_placa(c, 'WIRTZ', ALE, 640, 1150, f, wi, 64, -3)
    k = kick(f, k1 + 9, .8) + kick(f, k2 + 9, .8)
    return c, (lerp(600, 680, smooth(f / 120)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'dusk'


def _k4():
    k1 = wt(4, 'cabeca') - 3; k2 = max(k1 + 26, wt(4, 'Gruda') + 1)
    return k1, k2


def s4(f):
    c = estadio2('dusk').copy()
    sc = wt(4, 'Schlotterbeck') - 3; gr = wt(4, 'Brajan') - 3
    k1, k2 = _k4()
    est = max(pulse(f, k1 + 9, 6) * (f < k1 + 20), pulse(f, k2 + 9, 6))
    gx, gy = put_gol2(c, x=740, estufa=est)
    put_goleiro(c, f, GKH, None, gx=760 + (60 if f > k1 + 6 else 0) * (f < k1 + 20) + (-60 if f > k2 + 6 else 0),
                arms='up', expr='shock', skin=0)
    if f < k1 + 20:
        x = 360
        hop = -90 * pulse(f, k1 - 6, 10)
        al(c, x, 2030 + hop, 880, f, 14, arms='up', expr='stern' if f < k1 else 'grin', num_='15', hs='raspado', skin=0)
        hy = 2030 + hop - 880 * .9
        if f < k1:
            t = ramp(f, max(0, k1 - 18), k1)
            put_bola(c, lerp(-60, x + 20, t), lerp(1500, hy, t) - 160 * math.sin(t * math.pi), raio_bola(880), f)
        else:
            bola_voo(c, f, k1, x + 20, hy, gx + 80, gy, raio_bola(880), raio_bola(300), 40, 9)
        put_placa(c, 'SCHLOTTERBECK', ALE, 900, 1150, f, sc, 52, -3)
        if f >= k1 + 9: gol_txt(c, f, k1 + 9, 640, 860, 'DE CABEÇA!')
    else:
        x = lerp(1180, 880, easeOut(ramp(f, k1 + 20, k2 - 3)))
        if f < k2 - 4: linhas_vel(c, x, 2030, 860, f, dir=1)
        al(c, x, 2030, 860, f, 5, arms='run' if f < k2 + 6 else 'aviao', run=(f * .09) % 1 if f < k2 - 4 else None,
           kick=pulse(f, k2 - 4, 5) if f >= k2 - 4 else 0, expr='grin', num_='19', hs='topete', flip=True, skin=2)
        rb = raio_bola(860)
        bola_voo(c, f, k2, x - 110, 2030 - rb, gx + 40, gy - 10, rb, raio_bola(300), 140)
        put_placa(c, 'GRUDA', ALE, 420, 1150, f, max(gr, k1 + 20), 60, 3)
        if f >= k2 + 9: gol_txt(c, f, k2 + 9, 640, 860, 'GOLEADA!')
    k = kick(f, k1 + 9, .8) + kick(f, k2 + 9, .8)
    return c, (lerp(600, 680, smooth(f / 120)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    pr = wt(5, 'primeiro') - 3; qa = wt(5, 'quartas') - 3
    for i, (x, s) in enumerate(((260, 'topete'), (640, 'curto'), (1020, 'raspado'))):
        al(c, x, 1990 + (40 if i == 1 else 0), 780 + (60 if i == 1 else 0), f, 40 + i, num_=('7', '10', '15')[i],
           arms='up' if f >= pr else 'cintura', expr='grin' if f >= pr else 'stern', skin=(0, 0, 2)[i], hs=s)
    if f >= pr:
        confete(c, 640, 800, f, pr, 70, 900)
        num(c, 'LÍDER', 640, 780, f, pr, 130, -3)
    if f >= qa: num(c, 'NAS QUARTAS', 640, 960, f, qa, 100, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, pr, .6) + kick(f, qa, .6)
    return c, (640 + 20 * math.sin(f * .05), 1420 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    so = wt(6, 'sorteio') - 3; ma = wt(6, 'marco') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, 0, 16)))
    al(c, bx, 2010, 860, f, 3, arms='cintura', expr='proud', look=1, run=(f * .09) % 1 if f < 16 else None, num_='10')
    sx = lerp(1550, 940, easeOut(ramp(f, 0, 16)))
    ho(c, sx, 2010, 860, f, 7, arms='cintura', expr='stern', look=-1, flip=True, run=(f * .09) % 1 if f < 16 else None, num_='4', skin=3, hs='cacheado')
    if f >= so: num(c, 'SORTEIO', 640, 780, f, so, 120, -3)
    if f >= ma: num(c, 'MARÇO 2027', 640, 950, f, ma, 100, 3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, so, .6) + kick(f, ma, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'ALE', 'HOL', 5, 0, ALE, HOL, 'FIM', lf)
    elif si == 2:
        k = max(14, wt(2, 'placar') - 2) + 9
        im = placar_tv(im, 'ALE', 'HOL', int(lf >= k), 0, ALE, HOL, '1º T', lf + 99, pulse_a=k)
    D = {0: ('ALEMANHA 5 x 0 HOLANDA', 'GOLEADA NO OLÍMPICO DE BERLIM', 4),
         1: ('ÚLTIMA RODADA DO GRUPO', 'VALENDO O PRIMEIRO LUGAR', wt(1, 'Olimpico') - 3),
         2: ('SCHERHANT ABRE O PLACAR', 'NO FIM DO PRIMEIRO TEMPO', max(14, wt(2, 'placar') - 2) + 12),
         3: ('FLORIAN WIRTZ', '2 GOLS NO SEGUNDO TEMPO', wt(3, 'dois') + 4),
         4: ('SCHLOTTERBECK E GRUDA', 'COMPLETAM A GOLEADA', wt(4, 'goleada') - 3),
         5: ('ALEMANHA EM 1º', 'CLASSIFICADA PARA AS QUARTAS', wt(5, 'quartas') - 3),
         6: ('MATA-MATA POR SORTEIO', 'JOGOS SÓ EM MARÇO DE 2027', wt(6, 'sorteio') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'cinco') - 3, 150, .8)
    s.ting(s.W(1, 'primeiro') - 3, .35)
    s.thunk(max(14, s.W(2, 'placar') - 2) + 9, 160, .8)
    k1 = max(16, s.W(3, 'Wirtz') + 2); k2 = max(k1 + 24, s.W(3, 'dois') - 2)
    s.thunk(k1 + 9, 140, .7)
    s.thunk(k2 + 9, 140, .7)
    k1 = s.W(4, 'cabeca') - 3; k2 = max(k1 + 26, s.W(4, 'Gruda') + 1)
    s.thunk(k1 + 9, 140, .7)
    s.thunk(k2 + 9, 140, .7)
    s.ting(s.W(5, 'primeiro') - 3, .3)
    s.ting(s.W(5, 'quartas') - 3, .3)
    s.ting(s.W(6, 'marco') - 3, .3)
