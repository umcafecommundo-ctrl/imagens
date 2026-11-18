"""anima.futebol — 18/11/2026 07h — Amistoso: Argentina 7x0 Costa Rica, 1ª vitória depois da despedida de Messi.
Fontes (conferidas em 18/11/2026): Tribuna do Sertão / agência (Argentina 7x0 Costa Rica em Córdoba na terça 17/11,
gols de Nico Paz 2, Julián Álvarez 2, Mastantuono 2 e Mac Allister; técnico Scaloni; após a derrota em casa para o
Uruguai na sexta); SANA (Estádio Mario Alberto Kempes, Córdoba; Nico Paz 8' e 38', Julián Álvarez 35' e 43',
Mastantuono 48' e 88', Mac Allister 78'); Terra/VAVEL/Mixvale (Uruguai venceu na Bombonera no 1º jogo sem Messi, 13-14/11);
temas.txt 11/11 (Messi deixou a seleção com 208 jogos e 126 gols); CBF (próxima Data Fifa em março).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'AMISTOSO  ·  SELEÇÕES'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "A Argentina goleou a Costa Rica por sete a zero, a primeira vitória depois da despedida de Messi.",
    "Foi ontem, no Estádio Kempes, em Córdoba, quatro dias depois de perder para o Uruguai na Bombonera.",
    "Nico Paz abriu, Julián Álvarez ampliou, e os dois repetiram a dose antes do intervalo.",
    "No segundo tempo, Mastantuono fez mais dois, e Mac Allister também deixou o dele.",
    "Foram quatro jogadores diferentes balançando a rede, num time que perdeu o dono de cento e vinte e seis gols.",
    "Agora, a Argentina de Scaloni só volta a campo na próxima Data Fifa, em março.",
]
CAPTXT = [
    "A Argentina goleou a Costa Rica por 7 a 0, a primeira|vitória depois da despedida de Messi.",
    "Foi ontem, no Estádio Kempes, em Córdoba, 4 dias|depois de perder para o Uruguai na Bombonera.",
    "Nico Paz abriu, Julián Álvarez ampliou, e os dois|repetiram a dose antes do intervalo.",
    "No segundo tempo, Mastantuono fez mais 2,|e Mac Allister também deixou o dele.",
    "Foram 4 jogadores diferentes balançando a rede, num time|que perdeu o dono de 126 gols.",
    "Agora, a Argentina de Scaloni só volta a campo|na próxima Data Fifa, em março.",
]
FALA_TIKTOK = "Quem vai ser o novo camisa dez da Argentina? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "NOVO CAMISA 10?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'sete', 6), (1, 'Uruguai', 4), (2, 'abriu', 4), (2, 'dose', 4), (3, 'Allister', 6), (4, 'seis', 4),
         (5, 'marco', 4)]

ARG, ARG_F = time_('ARGENTINA')
CRC, CRC_F = time_('COSTA RICA')
URU, URU_F = time_('URUGUAI')
GKC = ('#f5c518', '#111111', '#111111')   # goleiro da Costa Rica (genérico)


def ar(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    kw.setdefault('hair', '#3a2414')
    put_atleta(c, x, y, h, f, seed, cores=ARG, faixa=ARG_F, sock='#ffffff', **kw)


def cr(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=CRC, faixa=CRC_F, hair='#111111', sock='#d4282c', **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f) if t < 1 else None
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def gol_txt(c, f, f0, x=640, y=880, s='GOL!', cor=(255, 216, 74), size=150):
    explosao(c, x, y, f, f0, 260, cor)
    num(c, s, x, y, f, f0 + 2, size, -4)


def put_cal(c, dia, x, y, s, f, f0, mes='NOV'):
    if f >= f0: paste_c(c, calendario(dia, mes), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    se = wt(0, 'sete') - 3; me = wt(0, 'Messi') - 3
    cr(c, 300, 1700, 520, f, 11, arms='cheek', expr='pained')
    cr(c, 990, 1690, 500, f, 12, arms='cheek', expr='pained', skin=1, flip=True)
    x = lerp(1250, 620, easeOut(ramp(f, 0, 22)))
    if f < 24: linhas_vel(c, x, 2050, 900, f, dir=1)
    ar(c, x, 2050, 900, f, 6, arms='aviao', expr='grin', run=(f * .08) % 1 if f < 22 else -1, num_='9', flip=True)
    if f < se: put_placa(c, 'ARGENTINA', ARG, 640, 820, f, 4, 76, -3)
    if f >= se:
        confete(c, 640, 900, f, se, 90, 900)
        explosao(c, 640, 860, f, se, 220)
        num(c, '7 x 0', 640, 860, f, se + 2, 170, -3)
    if f >= me: num(c, '1ª VITÓRIA PÓS-MESSI', 640, 1060, f, me, 80, 3)
    z = lerp(1.22, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, se, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    on = wt(1, 'ontem') - 3; ke = wt(1, 'Kempes') - 3; ur = wt(1, 'Uruguai') - 3
    xe = lerp(-250, 340, easeOut(ramp(f, 0, 18)))
    xs = lerp(1500, 920, easeOut(ramp(f, 0, 18)))
    ar(c, xe, 2000, 840, f, 21, arms='cintura', expr='stern', look=1, run=(f * .09) % 1 if f < 18 else None, num_='5')
    cr(c, xs, 2000, 840, f, 22, arms='cintura', expr='stern', look=-1, flip=True, run=(f * .09) % 1 if f < 18 else None, num_='4')
    put_placa(c, 'ARGENTINA', ARG, 340, 1080, f, 6, 56, -3)
    put_placa(c, 'COSTA RICA', CRC, 920, 1080, f, 8, 56, 3)
    if f < ur:
        put_cal(c, '17', 640, 760, .45, f, on)
        num(c, 'CÓRDOBA', 640, 940, f, ke, 90, 3)
    else:
        explosao(c, 640, 800, f, ur, 200, (255, 120, 120))
        num(c, '4 DIAS APÓS PERDER', 640, 790, f, ur + 2, 80, -3)
        put_placa(c, 'URUGUAI', URU, 640, 940, f, ur + 4, 56, 3)
    z = lerp(1.0, 1.1, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .04), 1420, z, 0), 'dusk'


def _k2():
    # (jogador 0 = Nico Paz à esquerda, 1 = Julián à direita, quadro do chute)
    return [(0, wt(2, 'abriu') + 2), (1, wt(2, 'ampliou') + 2), (0, wt(2, 'repetiram') + 2), (1, wt(2, 'dose') + 2)]


def _k3():
    return [(0, wt(3, 'Mastantuono') + 2), (0, wt(3, 'dois') + 2), (1, wt(3, 'Allister') + 2)]


def _cena_gols(c, f, ks, P, placar0):
    est = max(pulse(f, k + 9, 6) for _, k in ks)
    gx, gy = put_gol2(c, x=640, estufa=est)
    put_goleiro(c, f, GKC, None, gx=660, arms='up', expr='shock', skin=2)
    for j, (x, nome, n, hs, sk, hair) in enumerate(P):
        mine = [k for jj, k in ks if jj == j]
        kk = max([k for k in mine if f >= k - 4] or [-99])
        festa = any(k + 6 <= f < k + 30 for k in mine)
        ar(c, x, 2030, 780, f, 30 + j, arms='punho' if festa else 'run', expr='grin', num_=n, hs=hs, skin=sk, hair=hair,
           kick=pulse(f, kk - 4, 5) if f >= kk - 4 and kk > 0 else 0, flip=x > 700)
        put_placa(c, nome, ARG, (360, 880)[j], 1170 + 40 * j, f, mine[0] - 10, 50, (-3, 3)[j])
        for k in mine:
            if k - 2 <= f < k + 12:
                rb = raio_bola(780)
                bola_voo(c, f, k, x + (60 if x < 700 else -60), 2030 - rb, gx + 40, gy, rb, raio_bola(300), 120)
    for i, (_, k) in enumerate(ks):
        nxt = ks[i + 1][1] + 9 if i + 1 < len(ks) else 10 ** 6
        if k + 9 <= f < nxt:
            gol_txt(c, f, k + 9, 640, 800, '%d x 0' % (placar0 + i + 1), size=160)
    return sum(kick(f, k + 9, .7) for _, k in ks)


def s2(f):
    c = estadio2('dusk').copy()
    P = ((280, 'NICO PAZ', '8', 'topete', 1, '#3a2414'), (1000, 'JULIÁN ÁLVAREZ', '9', 'curto', 1, '#2b1d14'))
    kk = _cena_gols(c, f, _k2(), P, 0)
    iv = wt(2, 'intervalo') - 3
    if f >= iv: num(c, 'NO INTERVALO', 640, 960, f, iv, 90, 3)
    return c, (640 + 20 * math.sin(f * .05), 1430 + kk * 10, lerp(1.05, 1.0, smooth(f / 80)), kk), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    se = wt(3, 'segundo') - 3
    ks = _k3()
    P = ((280, 'MASTANTUONO', '30', 'cacheado', 0, '#2b1d14'), (1000, 'MAC ALLISTER', '20', 'curto', 0, '#a0522d'))
    kk = _cena_gols(c, f, ks, P, 4)
    if f < ks[0][1] + 9: num(c, '2º TEMPO', 640, 760, f, se, 120, -3)
    if f >= ks[2][1] + 9: confete(c, 640, 800, f, ks[2][1] + 9, 80, 900)
    return c, (640 + 20 * math.sin(f * .05), 1430 + kk * 10, lerp(1.05, 1.0, smooth(f / 80)), kk), 'dusk'


def s4(f):
    c = estadio2('golden').copy()
    qu = wt(4, 'quatro') - 3; pe = wt(4, 'perdeu') - 3; cs = wt(4, 'cento') - 3
    if f < pe:
        nomes = ('NICO PAZ', 'JULIÁN', 'MASTANTUONO', 'MAC ALLISTER')
        for i, nm in enumerate(nomes):
            put_placa(c, nm, ARG, 330 if i % 2 == 0 else 930, 1120 + (i // 2) * 150, f, qu + i * 4, 42, (-3, 3)[i % 2])
        ar(c, 640, 2010, 820, f, 3, arms='joinha' if f >= qu else 'cintura', expr='proud', num_='7', hs='curto')
        num(c, '4 GOLEADORES', 640, 800, f, qu, 120, -3)
    else:
        x = lerp(1500, 640, easeOut(ramp(f, pe - 6, pe + 8)))
        ar(c, x, 2010, 840, f, 4, arms='wave' if False else 'up', expr='proud', num_='10', hs='curto', hair='#4a3020', flip=True)
        put_placa(c, 'MESSI', ARG, 640, 1120, f, pe, 64, 3)
        if f >= cs:
            explosao(c, 640, 820, f, cs, 220)
            num(c, '126 GOLS', 640, 820, f, cs + 2, 160, -3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0008 * f)
    k = kick(f, cs, .7)
    return c, (640 + 20 * math.sin(f * .04), 1430 + k * 8, z, k), 'golden'


def s5(f):
    c = estadio2('dusk').copy()
    sc = wt(5, 'Scaloni') - 3; ma = wt(5, 'marco') - 3
    bx = lerp(-300, 400, easeOut(ramp(f, 0, 16)))
    ar(c, bx, 2010, 860, f, 3, arms='cintura' if f < ma else 'joinha', expr='proud', look=1,
       run=(f * .09) % 1 if f < 16 else None, num_='9')
    put_placa(c, 'ARGENTINA', ARG, 400, 1120, f, 6, 60, -3)
    if f >= sc: put_placa(c, 'SCALONI', ARG, 900, 1300, f, sc, 52, 3)
    put_cal(c, 'MAR', 900, 1000, .55, f, ma - 10, '2027')
    if f >= ma: num(c, 'SÓ EM MARÇO', 640, 760, f, ma, 120, -3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ma, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def _placar(im, ks, base, minuto, lf):
    g = sum(lf >= k + 9 for _, k in ks)
    return placar_tv(im, 'ARG', 'CRC', base + g, 0, ARG, CRC, minuto, lf + 99,
                     pulse_a=max([k + 9 for _, k in ks if lf >= k + 9] or [-1]))


def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'ARG', 'CRC', 7, 0, ARG, CRC, 'FIM', lf)
    elif si == 2: im = _placar(im, _k2(), 0, '1º T', lf)
    elif si == 3: im = _placar(im, _k3(), 4, '2º T', lf)
    D = {0: ('ARGENTINA 7 x 0 COSTA RICA', '1ª VITÓRIA PÓS-MESSI', 4),
         1: ('ESTÁDIO KEMPES, CÓRDOBA', 'DEPOIS DA DERROTA PARA O URUGUAI', wt(1, 'Kempes') - 3),
         2: ('NICO PAZ E JULIÁN: 2 CADA', '4 x 0 NO INTERVALO', _k2()[3][1] + 14),
         3: ('MASTANTUONO FAZ 2', 'MAC ALLISTER FECHA O 7 x 0', _k3()[2][1] + 14),
         4: ('4 GOLEADORES DIFERENTES', None, wt(4, 'quatro') - 3),
         5: ('PRÓXIMA DATA FIFA', 'SÓ EM MARÇO DE 2027', wt(5, 'marco') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'sete') - 3, 150, .8)
    s.ting(s.W(1, 'Uruguai') - 3, .3)
    for w in ('abriu', 'ampliou', 'repetiram', 'dose'): s.thunk(s.W(2, w) + 11, 140, .7)
    for w in ('Mastantuono', 'dois', 'Allister'): s.thunk(s.W(3, w) + 11, 140, .7)
    s.ting(s.W(4, 'cento') - 3, .35)
    s.ting(s.W(5, 'marco') - 3, .3)
