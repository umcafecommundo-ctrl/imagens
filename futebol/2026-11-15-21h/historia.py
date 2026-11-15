"""anima.futebol — 15/11/2026 21h — Nations League: Espanha 2x3 Inglaterra no Metropolitano, fim da invencibilidade de 44 jogos.
Fontes (conferidas em 15/11/2026): Metrópoles (3x2 em Madri; Kane pênalti nos acréscimos do 1º tempo, Konsa de cabeça aos 8 do 2º,
Ben White ~4 min depois; Anderson expulso por falta em Lamine Yamal que gerou o pênalti de Oyarzabal; Nico Williams com passe de Yamal;
empate em pontos, Inglaterra 1ª pelo saldo; Espanha perde após 44 jogos invicta; quartas em março de 2027);
SportBuzz (Kane 45' pên., Konsa 53', White 57', Anderson vermelho 63', Oyarzabal 65' pên., Nico Williams 75'; 15 pontos cada;
as duas já classificadas); Itatiaia (mesmos gols; vermelho aos 18 do 2º tempo; série de 44 jogos encerrada; 15 pontos, Inglaterra na frente pelo saldo);
A Bola (Metropolitano, Madri, 6ª rodada do Grupo A3; Espanha venceu a ida 3x2 em Wembley).
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
    "A Espanha, campeã do mundo, perdeu depois de quarenta e quatro jogos: a Inglaterra venceu por três a dois, em Madri.",
    "Foi na última rodada da Nations League, no Metropolitano, valendo o primeiro lugar do grupo.",
    "Harry Kane abriu o placar de pênalti, no fim do primeiro tempo.",
    "Na volta do intervalo, Konsa, de cabeça, e Ben White fizeram mais dois em quatro minutos.",
    "Aí Elliot Anderson foi expulso por falta em Lamine Yamal, e Oyarzabal descontou de pênalti.",
    "Nico Williams ainda fez o segundo, mas a Inglaterra, com dez, segurou a vitória.",
    "As duas terminaram com quinze pontos, e os ingleses ficaram em primeiro pelo saldo de gols.",
    "Espanha e Inglaterra já estavam nas quartas, que só começam em março.",
]
CAPTXT = [
    "A Espanha, campeã do mundo, perdeu depois de 44 jogos:|a Inglaterra venceu por 3 a 2, em Madri.",
    "Foi na última rodada da Nations League, no Metropolitano,|valendo o 1º lugar do grupo.",
    "Harry Kane abriu o placar de pênalti,|no fim do primeiro tempo.",
    "Na volta do intervalo, Konsa, de cabeça, e Ben White|fizeram mais dois em 4 minutos.",
    "Aí Elliot Anderson foi expulso por falta em Lamine Yamal,|e Oyarzabal descontou de pênalti.",
    "Nico Williams ainda fez o segundo, mas a Inglaterra,|com 10, segurou a vitória.",
    "As duas terminaram com 15 pontos, e os ingleses|ficaram em 1º pelo saldo de gols.",
    "Espanha e Inglaterra já estavam nas quartas,|que só começam em março.",
]
FALA_TIKTOK = "Quem é mais forte hoje, Espanha ou Inglaterra? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM É MELHOR?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'quarenta', 6), (1, 'primeiro', 4), (2, 'penalti', 6), (3, 'cabeca', 6), (4, 'expulso', 6), (5, 'Williams', 4),
         (6, 'quinze', 4), (7, 'marco', 4)]

ING, ING_F = time_('INGLATERRA')
ESP, ESP_F = time_('ESPANHA')
GKI = ('#f2c94c', '#111111', '#111111')
GKE = ('#2fa35a', '#111111', '#111111')


def en(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 0); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=ING, faixa=ING_F, hair='#6a4a2a', sock='#ffffff', **kw)


def es(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=ESP, faixa=ESP_F, hair='#2a1a10', sock='#1a2a5c', **kw)


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


@lru_cache(maxsize=2)
def cartao():
    im = Image.new('RGBA', (170, 240), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, 164, 234], 18, fill=(214, 30, 40, 255), outline=INK + (255,), width=8)
    d.rectangle([24, 22, 60, 120], fill=(240, 80, 80, 255))
    return im


def put_cartao(c, x, y, f, f0, rot=-10):
    if f < f0: return
    im = cartao().rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y - 40 * (1 - back(ramp(f, f0, f0 + 8))), back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    qu = wt(0, 'quarenta') - 3; tr = wt(0, 'tres') - 3
    es(c, 300, 1700, 520, f, 11, arms='cheek', expr='pained')
    es(c, 990, 1690, 500, f, 12, arms='cheek', expr='pained', skin=2, hs='cacheado', flip=True)
    x = lerp(1250, 620, easeOut(ramp(f, 0, 22)))
    if f < 24: linhas_vel(c, x, 2050, 900, f, dir=1)
    en(c, x, 2050, 900, f, 6, arms='aviao', expr='grin', run=(f * .08) % 1 if f < 22 else -1, num_='9', flip=True)
    num(c, '44 JOGOS', 640, 800, f, qu, 130, -3)
    num(c, 'SEM PERDER', 640, 960, f, qu + 6, 90, 3)
    if f >= tr:
        confete(c, 640, 900, f, tr, 90, 900)
        explosao(c, 640, 1130, f, tr, 200)
        num(c, '3 x 2', 640, 1130, f, tr + 2, 140, -3)
    z = lerp(1.22, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, tr, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    me = wt(1, 'Metropolitano') - 3; pr = wt(1, 'primeiro') - 3
    xe = lerp(-250, 340, easeOut(ramp(f, 0, 18)))
    xs = lerp(1500, 920, easeOut(ramp(f, 0, 18)))
    en(c, xe, 2000, 840, f, 21, arms='cintura', expr='stern', look=1, run=(f * .09) % 1 if f < 18 else None, num_='10')
    es(c, xs, 2000, 840, f, 22, arms='cintura', expr='stern', look=-1, flip=True, run=(f * .09) % 1 if f < 18 else None, num_='19', skin=2)
    put_placa(c, 'INGLATERRA', ING, 340, 1080, f, 6, 64, -3)
    put_placa(c, 'ESPANHA', ESP, 920, 1080, f, 8, 64, 3)
    if f < pr: num(c, 'MADRI', 640, 760, f, me, 110, -2)
    if f >= pr:
        explosao(c, 640, 900, f, pr, 200)
        num(c, '1º LUGAR', 640, 900, f, pr + 2, 110, 3)
    z = lerp(1.0, 1.1, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .04), 1420, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    ka = wt(2, 'Kane') - 3; pe = wt(2, 'penalti') - 3
    kf = pe + 2
    gx, gy = put_gol2(c, x=700, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKE, None, gx=720 - 70 * clamp((f - kf) / 7), arms='up', expr='shock' if f >= kf + 5 else 'nervous', skin=1)
    x = 330
    en(c, x, 2030, 880, f, 8, arms='run' if f < kf + 10 else 'punho', kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0,
       expr='stern' if f < kf else 'grin', num_='9', hs='curto')
    foco(c, x, 1640, 380, .85 * pulse(f, ka, 30))
    put_placa(c, 'HARRY KANE', ING, 900, 1150, f, ka, 60, -3)
    chute_gol(c, f, kf, x, 880, gx, gy, alvo=(110, -10), arco=60)
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, 'PÊNALTI!')
    k = kick(f, kf + 9)
    return c, (lerp(600, 660, smooth(f / 80)), 1430 + k * 10, lerp(1.04, 1.1, smooth(f / 80)), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    ko = wt(3, 'Konsa') - 3; ca = wt(3, 'cabeca') - 3; bw = wt(3, 'White') - 3; qm = wt(3, 'quatro') - 3
    k1 = ca; k2 = max(k1 + 26, bw + 4)
    est = max(pulse(f, k1 + 9, 6) * (f < k1 + 20), pulse(f, k2 + 9, 6))
    gx, gy = put_gol2(c, x=740, estufa=est)
    put_goleiro(c, f, GKE, None, gx=760 + (60 if f > k1 + 6 else 0) * (f < k1 + 20) + (-60 if f > k2 + 6 else 0),
                arms='up', expr='shock', skin=1)
    if f < k1 + 20:
        x = 360
        hop = -90 * pulse(f, k1 - 6, 10)
        en(c, x, 2030 + hop, 880, f, 14, arms='up', expr='stern' if f < k1 else 'grin', num_='4', hs='raspado', skin=4)
        hy = 2030 + hop - 880 * .9
        if f < k1:
            t = ramp(f, max(0, k1 - 18), k1)
            put_bola(c, lerp(-60, x + 20, t), lerp(1500, hy, t) - 160 * math.sin(t * math.pi), raio_bola(880), f)
        else:
            bola_voo(c, f, k1, x + 20, hy, gx + 80, gy, raio_bola(880), raio_bola(300), 40, 9)
        put_placa(c, 'KONSA', ING, 940, 1150, f, ko, 60, -3)
        if f >= k1 + 9: gol_txt(c, f, k1 + 9, 640, 860, 'DE CABEÇA!')
    else:
        x = lerp(1450, 880, easeOut(ramp(f, k1 + 20, k2 - 3)))
        if f < k2 - 4: linhas_vel(c, x, 2030, 860, f, dir=1)
        en(c, x, 2030, 860, f, 5, arms='run' if f < k2 + 6 else 'aviao', run=(f * .09) % 1 if f < k2 - 4 else None,
           kick=pulse(f, k2 - 4, 5) if f >= k2 - 4 else 0, expr='grin', num_='2', hs='topete', flip=True, skin=1)
        rb = raio_bola(860)
        bola_voo(c, f, k2, x - 110, 2030 - rb, gx + 40, gy - 10, rb, raio_bola(300), 140)
        put_placa(c, 'BEN WHITE', ING, 420, 1150, f, k1 + 20, 60, 3)
        if f >= k2 + 9: gol_txt(c, f, k2 + 9, 640, 860, '3 x 0')
    k = kick(f, k1 + 9, .8) + kick(f, k2 + 9, .8)
    return c, (lerp(600, 680, smooth(f / 120)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    an = wt(4, 'Anderson') - 3; ex = wt(4, 'expulso') - 3; oy = wt(4, 'Oyarzabal') - 3; pe = wt(4, 'penalti') - 3
    if f < oy - 4:
        en(c, 380, 2020, 860, f, 16, arms='cheek' if f >= ex else 'hang', expr='pained' if f >= ex else 'nervous', num_='8', skin=0, hs='topete')
        es(c, 900, 2020, 820, f, 17, arms='cintura', expr='stern', look=-1, flip=True, num_='10', skin=3, hs='cacheado')
        put_placa(c, 'ANDERSON', ING, 380, 1080, f, an, 60, -3)
        put_placa(c, 'LAMINE YAMAL', ESP, 900, 1080, f, wt(4, 'Yamal') - 4, 56, 3)
        put_cartao(c, 640, 820, f, ex, -10)
        if f >= ex: num(c, 'EXPULSO!', 640, 1220, f, ex + 2, 100, -3)
        k = kick(f, ex, .8)
        return c, (640, 1430 + k * 8, lerp(1.08, 1.0, smooth(f / 50)), k), 'dusk'
    kf = max(oy, pe) + 2
    gx, gy = put_gol2(c, x=700, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKI, None, gx=720 + 70 * clamp((f - kf) / 7), arms='up', expr='shock' if f >= kf + 5 else 'nervous', skin=0)
    x = 330
    es(c, x, 2030, 880, f, 18, arms='run' if f < kf + 10 else 'punho', kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0,
       expr='stern' if f < kf else 'grin', num_='21', hs='curto')
    put_placa(c, 'OYARZABAL', ESP, 900, 1150, f, oy - 4, 60, -3)
    chute_gol(c, f, kf, x, 880, gx, gy, alvo=(60, -10), arco=60)
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, '3 x 1', (230, 60, 70))
    k = kick(f, kf + 9)
    return c, (lerp(620, 660, smooth((f - oy) / 60)), 1430 + k * 10, 1.06, k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    ni = wt(5, 'Nico') - 3; de = wt(5, 'dez') - 3; vi = wt(5, 'vitoria') - 3
    if f < de - 6:
        kf = max(10, ni + 4)
        gx, gy = put_gol2(c, x=760, estufa=pulse(f, kf + 9, 10))
        put_goleiro(c, f, GKI, None, gx=780 - 60 * clamp((f - kf) / 7), arms='up', expr='shock', skin=0)
        x = lerp(-200, 340, easeOut(ramp(f, 0, kf - 3)))
        if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
        es(c, x, 2030, 860, f, 19, arms='run' if f < kf + 6 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
           kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='17', skin=4, hs='raspado')
        chute_gol(c, f, kf, x, 860, gx, gy)
        put_placa(c, 'NICO WILLIAMS', ESP, 900, 1150, f, ni, 58, 3)
        if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, '3 x 2', (230, 60, 70))
        k = kick(f, kf + 9)
        return c, (lerp(600, 660, smooth(f / 60)), 1430 + k * 10, 1.05, k), 'dusk'
    for i, (x, s) in enumerate(((260, 'topete'), (640, 'curto'), (1020, 'raspado'))):
        en(c, x, 1990 + (40 if i == 1 else 0), 780 + (60 if i == 1 else 0), f, 40 + i, num_=('5', '9', '6')[i],
           arms='up' if f >= vi else 'cintura', expr='grin' if f >= vi else 'stern', skin=(0, 0, 4)[i], hs=s)
    num(c, 'COM 10', 640, 780, f, de, 120, -3)
    if f >= vi:
        confete(c, 640, 800, f, vi, 70, 900)
        num(c, 'VITÓRIA!', 640, 950, f, vi + 2, 110, 3)
    z = lerp(1.1, 1.0, smooth((f - de) / 40))
    return c, (640 + 20 * math.sin(f * .05), 1420, z, 0), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    qz = wt(6, 'quinze') - 3; sa = wt(6, 'saldo') - 3
    tabela(c, [('1º', 'INGLATERRA', ING, '15', True), ('2º', 'ESPANHA', ESP, '15', False)], 640, 820, f, qz)
    if f >= sa: num(c, 'PELO SALDO', 640, 1180, f, sa, 100, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    return c, (640, lerp(1300, 1360, smooth(f / 150)), z, 0), 'dusk'


def s7(f):
    c = estadio2('dusk').copy()
    qa = wt(7, 'quartas') - 3; ma = wt(7, 'marco') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, 0, 16)))
    en(c, bx, 2010, 860, f, 3, arms='cintura', expr='stern', look=1, run=(f * .09) % 1 if f < 16 else None, num_='9')
    sx = lerp(1550, 940, easeOut(ramp(f, 0, 16)))
    es(c, sx, 2010, 860, f, 7, arms='cintura', expr='proud', look=-1, flip=True, run=(f * .09) % 1 if f < 16 else None, num_='10', skin=3, hs='cacheado')
    if f >= qa: num(c, 'QUARTAS', 640, 780, f, qa, 120, -3)
    if f >= ma: num(c, 'MARÇO 2027', 640, 950, f, ma, 100, 3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, qa, .6) + kick(f, ma, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def _k3():
    k1 = wt(3, 'cabeca') - 3; k2 = max(k1 + 26, wt(3, 'White') - 3 + 4)
    return k1 + 9, k2 + 9


def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'ESP', 'ING', 2, 3, ESP, ING, 'FIM', lf)
    elif si == 2:
        k = wt(2, 'penalti') + 8
        im = placar_tv(im, 'ESP', 'ING', 0, int(lf >= k), ESP, ING, '1º T', lf + 99, pulse_b=k)
    elif si == 3:
        k1, k2 = _k3()
        im = placar_tv(im, 'ESP', 'ING', 0, 1 + (lf >= k1) + (lf >= k2), ESP, ING, '2º T', lf + 99, pulse_b=k1 if lf < k2 else k2)
    elif si == 4:
        k = max(wt(4, 'Oyarzabal'), wt(4, 'penalti')) - 1 + 9
        im = placar_tv(im, 'ESP', 'ING', int(lf >= k), 3, ESP, ING, '2º T', lf + 99, pulse_a=k)
    elif si == 5:
        k = max(10, wt(5, 'Nico') + 1) + 9
        im = placar_tv(im, 'ESP', 'ING', 1 + (lf >= k), 3, ESP, ING, '2º T' if lf < wt(5, 'vitoria') - 3 else 'FIM', lf + 99, pulse_a=k)
    D = {0: ('ESPANHA 2 x 3 INGLATERRA', 'FIM DE 44 JOGOS SEM PERDER', 4),
         1: ('ÚLTIMA RODADA DO GRUPO', 'NO METROPOLITANO, EM MADRI', wt(1, 'Metropolitano') - 3),
         2: ('KANE DE PÊNALTI', 'FIM DO PRIMEIRO TEMPO', wt(2, 'penalti') + 12),
         3: ('KONSA E BEN WHITE', '2 GOLS EM 4 MINUTOS', wt(3, 'quatro') + 6),
         4: ('ANDERSON EXPULSO', 'OYARZABAL DESCONTA DE PÊNALTI', wt(4, 'expulso') + 2),
         5: ('NICO WILLIAMS FAZ 3 x 2', 'INGLATERRA SEGURA COM 10', wt(5, 'dez') - 3),
         6: ('INGLATERRA EM 1º', 'EMPATE EM PONTOS, SALDO DECIDE', wt(6, 'quinze') - 3),
         7: ('AS DUAS NAS QUARTAS', 'MATA-MATA EM MARÇO DE 2027', wt(7, 'quartas') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (230, 60, 70) if si in (0, 4) else (255, 216, 74), y=1250 if si == 6 else 1330)


def SFX(s):
    s.thunk(s.W(0, 'tres') - 3, 150, .8)
    s.ting(s.W(1, 'primeiro') - 3, .35)
    s.thunk(s.W(2, 'penalti') + 8, 160, .8)
    k1 = s.W(3, 'cabeca') - 3; k2 = max(k1 + 26, s.W(3, 'White') + 1)
    s.thunk(k1 + 9, 140, .7)
    s.thunk(k2 + 9, 140, .7)
    s.thunk(s.W(4, 'expulso') - 3, 150, .8)
    s.thunk(max(s.W(4, 'Oyarzabal'), s.W(4, 'penalti')) - 1 + 9, 140, .7)
    s.thunk(max(10, s.W(5, 'Nico') + 1) + 9, 140, .7)
    s.ting(s.W(5, 'vitoria') - 3, .3)
    s.ting(s.W(6, 'quinze') - 3, .3)
    s.ting(s.W(7, 'quartas') - 3, .3)
