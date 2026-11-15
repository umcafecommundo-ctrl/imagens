"""anima.futebol — 15/11/2026 19h — Copa do Brasil Feminina: Internacional campeão inédito, 1 x 0 no Flamengo no Beira-Rio.
Fontes (conferidas em 15/11/2026): Gazeta Esportiva (Internacional 1 x 0 Flamengo, final de volta, Beira-Rio, domingo 15/11, 16h;
gol do Inter no 2º tempo; gol de Sole Jaimes no 1º tempo anulado pelo VAR por posição irregular; agregado 4 x 1; título inédito);
Metrópoles (Inter 1 x 0, gol de Pati Llanos no 2º tempo; gol de Sole Jaimes anulado pelo VAR por impedimento; ida 3 x 1 no
Luso-Brasileiro em 11/11; agregado 4 x 1). Prêmio de R$ 1,1 milhão ao campeão e 1ª final do Inter: Flashscore Brasil (post 12h).
Minuto do gol diverge (13'/14' do 2º tempo): usado só "segundo tempo". Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'COPA DO BRASIL FEMININA  ·  FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Internacional é campeão da Copa do Brasil feminina pela primeira vez na história.",
    "Neste domingo, no Beira-Rio, o Inter venceu o Flamengo por um a zero.",
    "No primeiro tempo, Sole Jaimes até balançou a rede, mas o VAR anulou por impedimento.",
    "No segundo tempo, Pati Llanos apareceu na área e marcou o gol do título.",
    "Como o Inter já tinha vencido a ida por três a um, o placar somado ficou quatro a um.",
    "Na primeira final da sua história, o Inter leva a taça e um milhão e cem mil reais de prêmio.",
    "E o Flamengo, que também sonhava com o título inédito, fica com o vice.",
]
CAPTXT = [
    "O Internacional é campeão da Copa do Brasil|feminina pela primeira vez na história.",
    "Neste domingo, no Beira-Rio,|o Inter venceu o Flamengo por 1 a 0.",
    "No primeiro tempo, Sole Jaimes até balançou|a rede, mas o VAR anulou por impedimento.",
    "No segundo tempo, Pati Llanos apareceu|na área e marcou o gol do título.",
    "Como o Inter já tinha vencido a ida por 3 a 1,|o placar somado ficou 4 a 1.",
    "Na primeira final da sua história, o Inter leva|a taça e R$ 1,1 milhão de prêmio.",
    "E o Flamengo, que também sonhava|com o título inédito, fica com o vice.",
]
FALA_TIKTOK = "O Inter mereceu o título? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "MERECEU?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'primeira', 4), (1, 'Beira-Rio', 4), (2, 'anulou', 6), (3, 'titulo', 4), (4, 'quatro', 6),
         (5, 'milhao', 4), (6, 'vice', 4)]

INT, INT_F = time_('INTERNACIONAL')
FLA, FLA_F = time_('FLAMENGO')
GKI = ('#2b2b2b', '#f2c94c', '#2b2b2b')
GKF = ('#2fa35a', '#111111', '#111111')


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'rabo'); kw.setdefault('hair', '#3a2414')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 4); kw.setdefault('hs', 'coque'); kw.setdefault('hair', '#111111')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def gol_txt(c, f, f0, x=640, y=880, s='GOL!', cor=(255, 216, 74)):
    explosao(c, x, y, f, f0, 260, cor)
    num(c, s, x, y, f, f0 + 2, 150, -4)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y + 12 * math.sin(f * .08), s)



# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    ca = wt(0, 'campeao') - 3; pr = wt(0, 'primeira') - 3
    put_trofeu(c, 640, 1080, 520, f, ca)
    num(c, 'CAMPEÃO INÉDITO', 640, 720, f, pr, 100, -3)
    for i, (x, sd) in enumerate(((260, 1), (640, 3), (1000, 5))):
        xx = lerp(x + (-500 if i == 0 else 500 if i == 2 else 0), x, easeOut(ramp(f, 0, 18)))
        inter(c, xx, 2040 + (30 if i == 1 else 0), 800 if i != 1 else 860, f, sd, arms='up' if f >= ca else 'run',
              expr='grin', look=1 if i == 0 else -1, flip=(i == 2), num_=['9', '10', '7'][i],
              run=(f * .08) % 1 if f < 18 else None)
    confete(c, 640, 900, f, ca, 90, 900)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ca, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('golden').copy()
    ii = wt(1, 'Inter') - 3; ff = wt(1, 'Flamengo') - 3; do = wt(1, 'domingo') - 3; be = wt(1, 'Beira-Rio') - 3
    um = wt(1, 'zero') - 6
    vx = lerp(-260, 340, easeOut(ramp(f, ii - 10, ii + 8)))
    px = lerp(1500, 940, easeOut(ramp(f, ff - 10, ff + 8)))
    inter(c, vx, 2030, 720, f, 3, arms='punho' if f >= um else 'cintura', expr='grin' if f >= um else 'stern', look=1, num_='9',
          run=(f * .08) % 1 if f < ii + 8 else None)
    fla(c, px, 2030, 720, f, 4, arms='cheek' if f >= um else 'cintura', expr='pained' if f >= um else 'stern', look=-1, flip=True,
        num_='10', run=(f * .08) % 1 if f < ff + 8 else None)
    put_placa(c, 'INTERNACIONAL', INT, 340, 1210, f, ii + 4, 44, -4)
    put_placa(c, 'FLAMENGO', FLA, 940, 1210, f, ff + 4, 50, 4)
    if f >= do: paste_c(c, calendario('15', 'NOV'), 640, 770, .42 * back(ramp(f, do, do + 8)))
    num(c, 'BEIRA-RIO', 640, 950, f, be, 84, 3)
    num(c, '1 x 0', 640, 1070, f, um, 120, -3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0005 * f)
    k = kick(f, um, .7) + kick(f, be, .4)
    return c, (640, 1420 + k * 8, z, k), 'golden'


def s2(f):
    c = estadio2('dusk').copy()
    ba = wt(2, 'balancou') - 3; an = wt(2, 'anulou') - 3; im_ = wt(2, 'impedimento') - 3
    kf = max(ba - 8, 16)
    gx, gy = put_gol2(c, x=760, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKF, None, gx=780 - 60 * clamp((f - kf) / 7), arms='up', expr='shock', skin=3)
    x = lerp(-150, 520, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
    inter(c, x, 2030, 860, f, 5, arms='run' if f < kf + 10 else ('cheek' if f >= an else 'punho'),
          run=(f * .1) % 1 if f < kf - 4 else None, kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0,
          expr='pained' if f >= an else 'grin', num_='9')
    if f < an: put_placa(c, 'SOLE JAIMES', INT, 520, 1130, f, wt(2, 'Sole') - 3, 50, -3)
    rb = raio_bola(860)
    bola_voo(c, f, kf, x + 112, 2030 - rb, gx + 90, gy, rb, raio_bola(300))
    if kf + 9 <= f < an: gol_txt(c, f, kf + 9, 640, 780)
    if f >= an:
        explosao(c, 640, 760, f, an, 230, (230, 60, 60))
        num(c, 'ANULADO', 640, 760, f, an, 130, -4)
        num(c, 'VAR: IMPEDIMENTO', 640, 1020, f, im_, 76, 3)
    k = kick(f, kf + 9) + kick(f, an, .9)
    return c, (lerp(580, 680, smooth(f / 80)), 1430 + k * 10, lerp(1.0, 1.08, smooth(f / 80)), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    pa = wt(3, 'Pati') - 3; ma = wt(3, 'marcou') - 3; ti = wt(3, 'titulo') - 3
    kf = max(ma - 6, 18)
    gx, gy = put_gol2(c, x=520, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKF, None, gx=540 + 90 * clamp((f - kf) / 7), arms='up', expr='shock', skin=3)
    x = lerp(1400, 760, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f, dir=1)
    inter(c, x, 2030, 860, f, 6, arms='run' if f < kf + 10 else 'up', run=(f * .1) % 1 if f < kf - 4 else None,
          kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='11', flip=True, look=-1)
    put_placa(c, 'PATI LLANOS', INT, 760, 1130, f, pa, 50, 3)
    rb = raio_bola(860)
    bola_voo(c, f, kf, x - 112, 2030 - rb, gx + 90, gy, rb, raio_bola(300))
    if f >= kf + 9:
        gol_txt(c, f, kf + 9, 640, 780)
        confete(c, 640, 900, f, kf + 9, 60, 700)
    k = kick(f, kf + 9)
    return c, (lerp(700, 600, smooth(f / 80)), 1430 + k * 10, lerp(1.0, 1.08, smooth(f / 80)), k), 'dusk'


def s4(f):
    c = estadio2('golden').copy()
    ida = wt(4, 'ida') - 3; so = wt(4, 'somado') - 3; qu = wt(4, 'quatro') - 3
    inter(c, 640, 2040, 860, f, 7, arms='joinha' if f >= qu else 'cintura', expr='proud' if f >= qu else 'smug', num_='10')
    foco(c, 640, 1620, 420, .7 * pulse(f, ida, 40))
    num(c, 'IDA: 3 x 1', 640, 720, f, ida, 84, -3)
    num(c, 'VOLTA: 1 x 0', 640, 840, f, ida + 10, 84, 2)
    num(c, 'TOTAL: 4 x 1', 640, 990, f, qu, 110, -3)
    k = kick(f, qu, .8)
    return c, (640 + 20 * math.sin(f * .04), 1430 + k * 8, lerp(1.0, 1.06, smooth(f / 110)), k), 'golden'


def s5(f):
    c = estadio2('dusk').copy()
    ta = wt(5, 'taca') - 3; mi = wt(5, 'milhao') - 3
    put_trofeu(c, 640, 1300, 480, f, 0)
    num(c, '1ª FINAL, 1º TÍTULO', 640, 700, f, wt(5, 'primeira') - 3, 80, -2)
    if f >= mi: explosao(c, 640, 880, f, mi, 150)
    num(c, 'R$ 1,1 MILHÃO', 640, 870, f, mi, 110, -3)
    inter(c, 250, 2040, 780, f, 1, arms='up' if f >= ta else 'cintura', expr='grin', look=1)
    inter(c, 1030, 2040, 780, f, 2, arms='up' if f >= ta else 'cintura', expr='grin', look=-1, flip=True, num_='5')
    if f >= ta: confete(c, 640, 900, f, ta, 70, 800)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, mi, .6)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    fl = wt(6, 'Flamengo') - 3; vi = wt(6, 'vice') - 3
    fla(c, 640, 2040, 880, f, 8, arms='cheek' if f >= vi else 'cintura', expr='pained' if f >= vi else 'stern', num_='9')
    put_placa(c, 'FLAMENGO', FLA, 640, 1060, f, fl, 66, 3)
    num(c, 'VICE-CAMPEÃO', 640, 760, f, vi, 100, -3)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, vi, .5)
    return c, (640, 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60))) + k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def OVERLAY(im, si, lf):
    if si in (1, 2, 3):
        if si == 1: im = placar_tv(im, 'INT', 'FLA', 1, 0, INT, FLA, 'FIM', lf)
        elif si == 2: im = placar_tv(im, 'INT', 'FLA', 0, 0, INT, FLA, '1º T', lf + 99)
        else:
            kf = max(wt(3, 'marcou') - 6, 18) + 9
            im = placar_tv(im, 'INT', 'FLA', 1 if lf >= kf else 0, 0, INT, FLA, '2º T', lf + 99, pulse_a=kf)
    D = {0: ('INTER CAMPEÃO', 'COPA DO BRASIL FEMININA', wt(0, 'primeira') + 6),
         1: ('INTER 1 x 0 FLAMENGO', 'FINAL DE VOLTA, NO BEIRA-RIO', wt(1, 'zero') + 4),
         2: ('GOL ANULADO PELO VAR', 'SOLE JAIMES, NO 1º TEMPO', wt(2, 'impedimento') + 6),
         3: ('PATI LLANOS DECIDE', 'GOL DO TÍTULO NO 2º TEMPO', max(wt(3, 'marcou') - 6, 18) + 24),
         4: ('AGREGADO: 4 x 1', 'IDA 3 x 1 + VOLTA 1 x 0', wt(4, 'quatro') + 4),
         5: ('TÍTULO INÉDITO', 'PRÊMIO DE R$ 1,1 MILHÃO', wt(5, 'premio') - 3),
         6: ('FLAMENGO É VICE', 'TAMBÉM BUSCAVA O 1º TÍTULO', wt(6, 'vice') + 4)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.ting(s.W(0, 'campeao') - 3, .35)
    s.thunk(s.W(1, 'zero') - 6, 150, .7)
    s.thunk(max(s.W(2, 'balancou') - 8, 16) + 9, 160, .8)
    s.thunk(s.W(2, 'anulou') - 3, 120, .8)
    s.thunk(max(s.W(3, 'marcou') - 6, 18) + 9, 160, .9)
    s.thunk(s.W(4, 'quatro') - 3, 200, .6)
    s.ting(s.W(5, 'milhao') - 3, .35)
