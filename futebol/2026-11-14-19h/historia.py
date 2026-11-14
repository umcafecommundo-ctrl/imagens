"""anima.futebol — 14/11/2026 19h — Seleção Brasileira: Ancelotti e Raphinha fora de Brasil x Singapura após expulsões.
Fontes (conferidas em 14/11/2026): Metrópoles (Ancelotti e Raphinha expulsos e fora do amistoso contra Singapura; árbitro disse
que Ancelotti não controlou o banco; Minamino tomou a bola de João Gomes no início do contra-ataque; Raphinha já substituído
entrou com Ancelotti para reclamar; terça 17/11 7h); Terra (Ancelotti: árbitro 'não tem experiência para gerir esse jogo';
Ancelotti suspenso e Raphinha fora; auxiliar deve comandar); Liga da Notícia (vermelho para os dois após gol de Sakamoto nos
acréscimos, falta de Minamino em João Gomes, árbitro Jansen Foo Chuan Hui, fora contra Singapura); brasileirao.com.br
('não consegui controlar o banco de reservas'; árbitro sem experiência para o nível do jogo).
"""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Ancelotti e Raphinha estão fora do jogo do Brasil contra Singapura.",
    "Os dois foram expulsos nos acréscimos da derrota por três a dois para o Japão.",
    "No lance do gol japonês, Minamino tomou a bola de João Gomes, e o Brasil pediu falta.",
    "Raphinha, que já tinha sido substituído, invadiu o campo junto com Ancelotti para reclamar.",
    "E o árbitro mostrou o cartão vermelho para os dois.",
    "Segundo Ancelotti, o juiz disse que ele não conseguiu controlar o banco de reservas.",
    "O técnico ainda disse que o árbitro não tinha experiência para um jogo desse nível.",
    "Na terça, às sete da manhã, um auxiliar deve comandar o Brasil contra Singapura.",
]
CAPTXT = [
    "Ancelotti e Raphinha estão fora do jogo|do Brasil contra Singapura.",
    "Os dois foram expulsos nos acréscimos da derrota|por 3 a 2 para o Japão.",
    "No lance do gol japonês, Minamino tomou a bola|de João Gomes, e o Brasil pediu falta.",
    "Raphinha, que já tinha sido substituído, invadiu|o campo junto com Ancelotti para reclamar.",
    "E o árbitro mostrou o cartão vermelho|para os dois.",
    "Segundo Ancelotti, o juiz disse que ele não|conseguiu controlar o banco de reservas.",
    "O técnico ainda disse que o árbitro não tinha|experiência para um jogo desse nível.",
    "Na terça, às 7h da manhã, um auxiliar deve|comandar o Brasil contra Singapura.",
]
FALA_TIKTOK = "A expulsão foi justa: sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "FOI JUSTO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'fora', 4), (1, 'expulsos', 4), (2, 'Minamino', 4), (2, 'falta', 4), (3, 'Raphinha', 2), (4, 'vermelho', 4),
         (5, 'banco', 4), (6, 'experiencia', 4), (7, 'Singapura', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
SIN, SIN_F = time_('SINGAPURA')
TEC = ('#2a2f45', '#2a2f45', '#2a2f45')
JUIZ = ('#f2e600', '#111111', '#111111')


def jp(c, x, y, h, f, seed, **kw):
    kw.setdefault('hs', 'curto'); put_atleta(c, x, y, h, f, seed, cores=JAP, faixa=JAP_F, skin=1, hair='#151010', **kw)


def br(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); put_atleta(c, x, y, h, f, seed, cores=BRA, faixa=BRA_F, hair='#151010', **kw)


def anc(c, x, y, h, f, **kw):
    kw.setdefault('arms', 'shrug'); kw.setdefault('expr', 'stern')
    put_atleta(c, x, y, h, f, 9, cores=TEC, faixa=None, skin=1, hair='#a7a7a7', hs='curto', sock='#1a1a1a', **kw)


def rapha(c, x, y, h, f, **kw):
    br(c, x, y, h, f, 3, skin=2, num_='11', **kw)


def juiz(c, x, y, h, f, **kw):
    put_atleta(c, x, y, h, f, 40, cores=JUIZ, faixa=None, skin=1, hs='raspado', hair='#151010', sock='#111111', **kw)


@lru_cache(maxsize=2)
def cartao():
    im = Image.new('RGBA', (200, 280), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([6, 6, 194, 274], 22, fill=(214, 36, 40, 255), outline=INK + (255,), width=9)
    ImageDraw.Draw(im).line([(40, 40), (60, 200)], fill=(240, 110, 110, 255), width=12)
    return im


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    an = wt(0, 'Ancelotti') - 3; ra = wt(0, 'Raphinha') - 3; fo = wt(0, 'fora') - 3
    anc(c, 330, 2010, 820, f, arms='cheek' if f >= fo else 'hang', look=1)
    put_placa(c, 'ANCELOTTI', TEC, 330, 1080, f, an, 52, -3)
    rapha(c, 950, 2010, 820, f, arms='cheek' if f >= fo else 'hang', expr='pained', look=-1, flip=True)
    put_placa(c, 'RAPHINHA', BRA, 950, 1080, f, ra, 52, 3)
    explosao(c, 640, 800, f, fo, 240, (230, 60, 70))
    num(c, 'FORA!', 640, 800, f, fo + 2, 170, -4)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, fo, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    ex = wt(1, 'expulsos') - 3; tr = wt(1, 'tres') - 3
    br(c, 300, 1720, 520, f, 11, arms='cheek', expr='pained', skin=2)
    br(c, 990, 1710, 500, f, 12, arms='cheek', expr='pained', skin=4, hs='cacheado', flip=True)
    x = lerp(1250, 640, easeOut(ramp(f, 0, 22)))
    if f < 24: linhas_vel(c, x, 2050, 880, f, dir=1)
    jp(c, x, 2050, 880, f, 6, arms='aviao', expr='grin', run=(f * .08) % 1 if f < 22 else -1, num_='14', flip=True)
    if f >= ex - 4: paste_c(c, cartao(), 640, 820, .6 * back(ramp(f, ex - 4, ex + 4)), )
    num(c, '3 x 2', 640, 1000, f, tr, 130, 3)
    z = lerp(1.15, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ex, .7)
    return c, (640 + 20 * math.sin(f * .05), 1420 + k * 10, z, k), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    mi = wt(2, 'Minamino') - 3; jg = wt(2, 'Joao') - 3; fa = wt(2, 'falta') - 3
    tk = mi + 8                                     # roubada de bola
    gx = 520 - 120 * easeOut(ramp(f, tk, tk + 20))
    br(c, gx, 2020, 840, f, 5, skin=4, num_='8', arms='up' if f >= tk + 4 else 'run', expr='shock' if f >= tk + 2 else 'neutral',
       look=1, tilt=-.15 if f >= tk + 2 else 0)
    put_placa(c, 'JOÃO GOMES', BRA, gx, 1100, f, jg, 46, -3)
    mx = lerp(1300, 820, easeOut(ramp(f, 0, tk))) + (0 if f < tk + 6 else 260 * (ramp(f, tk + 6, tk + 30) ** 2))
    if f < tk: linhas_vel(c, mx, 2020, 840, f, dir=1)
    jp(c, mx, 2020, 840, f, 8, num_='8', arms='run', run=(f * .09) % 1, kick=pulse(f, tk - 2, 5), expr='grin', flip=f < tk + 6)
    put_placa(c, 'MINAMINO', JAP, min(mx, 1020), 1100, f, mi, 46, 3)
    rb = raio_bola(840)
    bx = lerp(gx + 120, mx - 100, ramp(f, tk - 2, tk + 3)) if f < tk + 6 else mx + 110
    put_bola(c, bx, 2020 - rb, rb, f)
    if f >= fa - 2: foco(c, gx, 1650, 380, .7 * ramp(f, fa - 2, fa + 4))
    num(c, 'FALTA?', 640, 800, f, fa, 140, -4)
    k = kick(f, tk, .6) + kick(f, fa, .5)
    return c, (lerp(600, 700, smooth(f / 90)), 1420 + k * 10, lerp(1.0, 1.08, smooth(f / 80)), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    ra = wt(3, 'Raphinha') - 3; inv = wt(3, 'invadiu') - 3; an = wt(3, 'Ancelotti') - 3
    juiz(c, 640, 1900, 680, f, arms='hang', expr='stern')
    rx = lerp(-250, 330, easeOut(ramp(f, inv - 6, inv + 14))) if f >= inv - 6 else -400
    if f < ra + 8 or rx < 0:
        rapha(c, 300, 2010, 820, f, arms='cintura', expr='stern', look=1) if f < inv - 6 else None
    if f >= inv - 6:
        if f < inv + 14: linhas_vel(c, rx, 2010, 820, f)
        rapha(c, rx, 2010, 820, f, arms='shrug' if f >= inv + 14 else 'run', run=(f * .1) % 1 if f < inv + 14 else None, expr='pained', look=1)
    put_placa(c, 'RAPHINHA', BRA, rx if f >= inv - 6 else 300, 1080, f, ra, 50, -3)
    ax = lerp(1500, 960, easeOut(ramp(f, an - 8, an + 12))) if f >= an - 8 else 1600
    if f >= an - 8:
        if f < an + 12: linhas_vel(c, ax, 2010, 820, f, dir=1)
        anc(c, ax, 2010, 820, f, arms='shrug' if f >= an + 12 else 'run', run=(f * .1) % 1 if f < an + 12 else None, look=-1, flip=True)
        put_placa(c, 'ANCELOTTI', TEC, ax, 1080, f, an, 50, 3)
    num(c, 'RECLAMAÇÃO!', 640, 760, f, wt(3, 'reclamar') - 3, 92, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    return c, (640 + 20 * math.sin(f * .04), 1430, z, 0), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    ve = wt(4, 'vermelho') - 3; do = wt(4, 'dois') - 3
    anc(c, 230, 2010, 780, f, arms='cheek' if f >= ve else 'shrug', look=1)
    rapha(c, 1050, 2010, 780, f, arms='cheek' if f >= ve else 'shrug', expr='pained', look=-1, flip=True)
    juiz(c, 640, 1990, 820, f, arms='punho' if f >= ve - 4 else 'point', expr='stern')
    if f >= ve - 4:
        hx, hy = 640 + (470 - 300) * .82, 1990 - (975 - 120) * .82
        foco(c, hx, hy + 60, 260, .8 * ramp(f, ve - 4, ve + 4))
        paste_c(c, cartao(), hx, hy - 50, .8 * back(ramp(f, ve - 4, ve + 4)))
    num(c, '2 VERMELHOS', 640, 760, f, do, 100, -3)
    k = kick(f, ve, 1.0)
    return c, (640, 1430 + k * 12, lerp(1.0, 1.08, smooth(f / 60)), k), 'dusk'


def s5(f):
    c = estadio2('golden').copy()
    ju = wt(5, 'juiz') - 3; ba = wt(5, 'banco') - 3
    # banco de reservas entrando no campo, ao fundo
    for i, (xx, sd, sk) in enumerate(((180, 21, 2), (420, 22, 4), (880, 23, 1), (1100, 24, 3))):
        xr = lerp(xx + (-300 if i < 2 else 300), xx, easeOut(ramp(f, ba - 10, ba + 10)))
        if f >= ba - 10:
            br(c, xr, 1720, 470, f, sd, skin=sk, arms='up', expr='stern', run=(f * .1) % 1 if f < ba + 10 else None, flip=i >= 2)
    anc(c, 640, 2010, 820, f, arms='shrug' if f < ba else 'cheek', look=0)
    juiz(c, 1050, 2000, 700, f, arms='point', expr='stern', flip=True) if f >= ju - 4 else None
    num(c, 'O BANCO!', 640, 820, f, ba, 130, -4)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ba, .6)
    return c, (640, 1420 + k * 10, z, k), 'golden'


def s6(f):
    c = estadio2('dusk').copy()
    ex = wt(6, 'experiencia') - 3; ni = wt(6, 'nivel') - 3
    anc(c, 380, 2030, 880, f, arms='point', expr='stern', look=1)
    juiz(c, 980, 2000, 760, f, arms='shrug' if f >= ex else 'hang', expr='nervous', flip=True, look=-1)
    num(c, 'SEM EXPERIÊNCIA?', 640, 790, f, ex, 82, -3)
    num(c, 'JOGO DE NÍVEL', 640, 940, f, ni, 76, 2)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    return c, (lerp(600, 680, smooth(f / 90)), 1430, z, 0), 'dusk'


def s7(f):
    c = estadio2('dusk').copy()
    te = wt(7, 'terca') - 3; si = wt(7, 'Singapura') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, 0, 16)))
    br(c, bx, 2010, 860, f, 3, skin=3, arms='cintura', expr='stern', look=1, run=(f * .09) % 1 if f < 16 else None, num_='10')
    paste_c(c, calendario('17', 'NOV'), 640, 860, .55 * back(ramp(f, te, te + 8))) if f >= te else None
    if f >= si - 10:
        sx = lerp(1550, 930, easeOut(ramp(f, si - 10, si + 4)))
        put_atleta(c, sx, 2010, 860, f, 7, cores=SIN, faixa=SIN_F, arms='cintura', expr='proud', skin=1, hair='#111111',
                   look=-1, flip=True, run=(f * .09) % 1 if f < si + 4 else None, num_='9')
        num(c, 'X', 640, 1520, f, si, 160)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, te, .6) + kick(f, si, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    if si in (1, 2, 3, 4): im = placar_tv(im, 'JAP', 'BRA', 3, 2, JAP, BRA, 'ACR.' if si > 1 else 'FIM', lf + (0 if si == 1 else 99))
    D = {0: ('FORA CONTRA SINGAPURA', 'ANCELOTTI E RAPHINHA', 4),
         1: ('EXPULSOS', 'NA DERROTA PARA O JAPÃO', wt(1, 'expulsos') - 3),
         2: ('A FALTA RECLAMADA', 'MINAMINO x JOÃO GOMES', wt(2, 'falta') - 3),
         3: ('INVASÃO DE CAMPO', 'RAPHINHA JÁ ESTAVA SUBSTITUÍDO', wt(3, 'substituido') - 3),
         4: ('CARTÃO VERMELHO', 'PARA OS DOIS', wt(4, 'arbitro')),
         5: ('A EXPLICAÇÃO', 'NÃO CONTROLOU O BANCO', wt(5, 'banco') - 3),
         6: ('ANCELOTTI CRITICA', 'O ÁRBITRO', wt(6, 'arbitro') - 3),
         7: ('BRASIL x SINGAPURA', 'TERÇA, 17/11, ÀS 7H', wt(7, 'terca') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (230, 60, 70) if si in (0, 1, 4) else (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'fora') - 3, 150, .8)
    s.thunk(s.W(1, 'expulsos') - 3, 140, .7)
    s.thunk(s.W(2, 'Minamino') + 5, 130, .6)
    s.ting(s.W(2, 'falta') - 3, .3)
    s.whoosh(s.W(3, 'invadiu') - 6, .4) if hasattr(s, 'whoosh') else None
    s.thunk(s.W(4, 'vermelho') - 3, 170, .9)
    s.ting(s.W(5, 'banco') - 3, .3)
    s.ting(s.W(7, 'terca') - 3, .3)
