"""anima.futebol — MODELO TESTE do visual novo (futebol2.py), com a mesma história de 14/11/2026 12h:
Japão 3x2 Brasil em Singapura. Fontes: ver futebol/2026-11-14-12h/historia.py. Não publicado."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Japão venceu o Brasil por três a dois, com um gol nos acréscimos, em Singapura.",
    "Logo no começo, Kubo e Nakamura marcaram, e o Japão abriu dois a zero em menos de vinte minutos.",
    "Vini Júnior diminuiu com um chutaço de fora da área, ainda no primeiro tempo.",
    "No segundo tempo, Vini marcou de novo e empatou: dois a dois.",
    "Mas, nos acréscimos, Sakamoto fez o gol da vitória japonesa.",
    "O Brasil reclamou de falta no lance, e Ancelotti e Raphinha acabaram expulsos.",
    "É só a segunda vitória do Japão sobre o Brasil na história, e as duas por três a dois.",
    "Na terça, às sete da manhã, o Brasil fecha o ano contra Singapura.",
]
CAPTXT = [
    "O Japão venceu o Brasil por 3 a 2, com um gol|nos acréscimos, em Singapura.",
    "Logo no começo, Kubo e Nakamura marcaram, e o Japão|abriu 2 a 0 em menos de 20 minutos.",
    "Vini Júnior diminuiu com um chutaço de fora da área,|ainda no primeiro tempo.",
    "No segundo tempo, Vini marcou de novo|e empatou: 2 a 2.",
    "Mas, nos acréscimos, Sakamoto fez|o gol da vitória japonesa.",
    "O Brasil reclamou de falta no lance, e Ancelotti|e Raphinha acabaram expulsos.",
    "É só a 2ª vitória do Japão sobre o Brasil na história,|e as duas por 3 a 2.",
    "Na terça, às 7h da manhã, o Brasil fecha|o ano contra Singapura.",
]
FALA_TIKTOK = "Teve falta no gol do Japão: sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "FOI FALTA?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'tres', 6), (1, 'Kubo', 2), (1, 'marcaram', 8), (2, 'chutaco', 8), (3, 'empatou', 4), (4, 'Sakamoto', 8),
         (5, 'expulsos', 4), (6, 'duas', 4), (7, 'Singapura', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
SIN, SIN_F = time_('SINGAPURA')
TEC = ('#2a2f45', '#2a2f45', '#2a2f45')
GKB = ('#2fa35a', '#111111', '#111111')
GKJ = ('#f2994a', '#111111', '#111111')
JUIZ = ('#f2e600', '#111111', '#111111')


def jp(c, x, y, h, f, seed, **kw):
    kw.setdefault('hs', 'curto'); put_atleta(c, x, y, h, f, seed, cores=JAP, faixa=JAP_F, skin=1, hair='#151010', **kw)


def br(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); put_atleta(c, x, y, h, f, seed, cores=BRA, faixa=BRA_F, hair='#151010', **kw)


def vini(c, x, y, h, f, **kw):
    br(c, x, y, h, f, 2, skin=4, hs='raspado', num_='7', **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    """bola sai de (x0,y0) no quadro k0 e chega em (x1,y1); antes fica no pé; deixa rastro."""
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
    ac = wt(0, 'acrescimos') - 3; tr = wt(0, 'tres') - 3
    br(c, 330, 1700, 520, f, 11, arms='cheek', expr='pained', skin=2)
    br(c, 980, 1690, 500, f, 12, arms='cheek', expr='pained', skin=4, hs='cacheado', flip=True)
    x = lerp(1250, 620, easeOut(ramp(f, 0, 22)))
    jp(c, x, 2050, 900, f, 6, arms='aviao', expr='grin', run=(f * .08) % 1 if f < 22 else -1, num_='8', flip=True)
    if f < 24: linhas_vel(c, x, 2050, 900, f, dir=1)
    confete(c, 640, 900, f, tr, 90, 900)
    explosao(c, 640, 820, f, tr, 250)
    num(c, '3 x 2', 640, 820, f, tr + 2, 170, -3)
    z = lerp(1.22, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, tr, .8) + kick(f, ac, .5)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    ku0 = wt(1, 'Kubo'); ma = wt(1, 'marcaram')
    k1 = max(14, ku0 - 9); ku = k1 - 3
    na = ku0 + 10; k2 = max(na + 8, ma - 4)
    est = max(pulse(f, k1 + 9, 6) * (f < na), pulse(f, k2 + 9, 6))
    gx, gy = put_gol2(c, x=760, estufa=est)
    put_goleiro(c, f, GKB, None, gx=780 + (60 if f > k1 + 6 else 0) * (f < na) + (-60 if f > k2 + 6 else 0), arms='up', expr='shock', skin=1)
    if f < na - 4:
        x = lerp(-200, 330, easeOut(ramp(f, 0, ku)))
        jp(c, x, 2030, 840, f, 4, arms='run' if f < k1 + 6 else 'punho', run=(f * .09) % 1 if f < k1 - 4 else None,
           kick=pulse(f, k1 - 4, 5) if f >= k1 - 4 else 0, expr='grin', num_='20')
        foco(c, x, 1650, 360, .9 * pulse(f, ku - 6, 40))
        chute_gol(c, f, k1, x, 840, gx, gy)
        if f >= k1 + 9: gol_txt(c, f, k1 + 9, 640, 860)
        if f < k1 - 4: linhas_vel(c, x, 2030, 840, f)
    else:
        x = lerp(1450, 880, easeOut(ramp(f, na - 4, na + 2)))
        jp(c, x, 2030, 840, f, 8, arms='run' if f < k2 + 6 else 'aviao', run=(f * .09) % 1 if f < k2 - 4 else None,
           kick=pulse(f, k2 - 4, 5) if f >= k2 - 4 else 0, expr='grin', num_='10', flip=True, hs='topete')
        foco(c, x, 1650, 360, .9 * pulse(f, na - 4, 40))
        rb = raio_bola(840)
        bola_voo(c, f, k2, x - 110, 2030 - rb, gx + 40, gy - 10, rb, raio_bola(300), 140)
        if f >= k2 + 9: gol_txt(c, f, k2 + 9, 640, 860)
    k = kick(f, k1 + 9, .8) + kick(f, k2 + 9, .8)
    return c, (lerp(600, 680, smooth(f / 140)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    vi = wt(2, 'Vini') - 3; ch = wt(2, 'chutaco') - 3
    kf = ch + 1
    gx, gy = put_gol2(c, x=860, s=.6, estufa=pulse(f, kf + 11, 8))
    put_goleiro(c, f, GKJ, None, gx=880 - 40 * clamp((f - kf) / 8), arms='up', expr='shock' if f >= kf + 6 else 'nervous', skin=0, hair='#111111')
    x = lerp(120, 360, easeOut(ramp(f, 0, kf - 4)))
    foco(c, x, 1640, 380, .85 * pulse(f, vi, 30))
    vini(c, x, 2030, 880, f, arms='run' if f < kf + 10 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
         kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='stern' if f < kf else 'grin')
    rb = raio_bola(880)
    bola_voo(c, f, kf, x + 115, 2030 - rb, gx + 160, gy - 70, rb, raio_bola(260), 320, 12)
    if f >= kf + 12: gol_txt(c, f, kf + 12, 600, 860, 'CHUTAÇO!')
    k = kick(f, kf + 12)
    return c, (lerp(560, 700, smooth(f / 100)), 1430 + k * 10, lerp(1.08, 1.0, smooth(f / 60)), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    mn = wt(3, 'novo') - 3; dd = wt(3, 'dois') - 3
    for i, (xx, sd, sk, hs) in enumerate(((260, 21, 2, 'cacheado'), (1000, 22, 1, 'curto'))):
        xr = lerp(xx + (-500 if i == 0 else 500), xx, easeOut(ramp(f, mn - 6, mn + 14)))
        br(c, xr, 1800, 600, f, sd, skin=sk, hs=hs, arms='up', expr='grin', run=(f * .09) % 1 if f < mn + 14 else None, flip=i == 1)
    x = lerp(900, 640, easeOut(ramp(f, 0, 30)))
    vini(c, x, 2050, 920, f, arms='aviao' if f >= mn else 'run', expr='grin', run=(f * .08) % 1 if f < 30 else None, flip=True)
    confete(c, 640, 900, f, mn, 80, 800)
    explosao(c, 640, 830, f, dd, 240)
    num(c, '2 x 2', 640, 830, f, dd + 2, 170, -3)
    k = kick(f, dd, .8)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .001 * f)
    return c, (640 + 25 * math.sin(f * .05), 1430 + k * 10, z, k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    sa = wt(4, 'Sakamoto') - 3; kf = sa + 4
    gx, gy = put_gol2(c, x=700, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKB, None, gx=720 + 70 * clamp((f - kf) / 7), arms='up', expr='shock', skin=1)
    x = lerp(-150, 560, easeOut(ramp(f, 0, kf - 4)))
    br(c, x - 380 + 40 * math.sin(f * .2), 2000, 760, f, 31, run=(f * .1) % 1, arms='run', expr='pained', skin=2)
    jp(c, x, 2030, 880, f, 9, arms='run' if f < kf + 10 else 'punho', run=(f * .1) % 1 if f < kf - 4 else None,
       kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='14')
    if f < kf - 4: linhas_vel(c, x, 2030, 880, f)
    foco(c, x, 1640, 380, .85 * pulse(f, sa, 26))
    chute_gol(c, f, kf, x, 880, gx, gy)
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, 'GOL!', (230, 60, 70))
    k = kick(f, kf + 9)
    return c, (lerp(560, 660, smooth(f / 60)), 1420 + k * 12, lerp(1.0, 1.08, smooth(f / 70)), k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    an = wt(5, 'Ancelotti') - 3; ra = wt(5, 'Raphinha') - 3; ex = wt(5, 'expulsos') - 3
    put_atleta(c, 260, 2010, 820, f, 9, cores=TEC, faixa=None, arms='shrug' if f < ex else 'cheek', expr='stern',
               skin=1, hair='#a7a7a7', hs='curto', sock='#1a1a1a', look=1)
    put_placa(c, 'ANCELOTTI', TEC, 260, 1080, f, an, 52, -3)
    br(c, 1000, 2010, 820, f, 3, skin=2, num_='11', arms='shrug' if f < ex else 'cheek', expr='pained', look=-1, flip=True)
    put_placa(c, 'RAPHINHA', BRA, 1000, 1080, f, ra, 52, 3)
    put_atleta(c, 630, 1960, 760, f, 40, cores=JUIZ, faixa=None, arms='punho' if f >= ex - 4 else 'point', expr='stern',
               skin=0, hs='raspado', hair='#3a2a1a', sock='#111111')
    if f >= ex - 4:
        hx, hy = 630 + (470 - 300) * .76, 1960 - (975 - 120) * .76
        foco(c, hx, hy + 60, 260, .8 * ramp(f, ex - 4, ex + 4))
        paste_c(c, cartao(), hx, hy - 50, .75 * back(ramp(f, ex - 4, ex + 4)))
    num(c, 'FALTA?', 640, 760, f, wt(5, 'falta') - 3, 120, -4) if f < ex - 4 else None
    k = kick(f, ex, .8)
    return c, (640, 1430 + k * 10, lerp(1.0, 1.06, smooth(f / 90)), k), 'dusk'


@lru_cache(maxsize=2)
def cartao():
    im = Image.new('RGBA', (200, 280), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([6, 6, 194, 274], 22, fill=(214, 36, 40, 255), outline=INK + (255,), width=9)
    ImageDraw.Draw(im).line([(40, 40), (60, 200)], fill=(240, 110, 110, 255), width=12)
    return im


def s6(f):
    c = estadio2('golden').copy()
    se = wt(6, 'segunda') - 3; du = wt(6, 'duas') - 3
    jp(c, 640, 2040, 900, f, 6, arms='joinha' if f < du else 'up', expr='proud', num_='8')
    explosao(c, 640, 820, f, se, 250)
    num(c, '2ª VEZ', 640, 820, f, se + 2, 150, -4)
    num(c, '2025:  3 x 2', 640, 1010, f, du, 84, -2)
    num(c, '2026:  3 x 2', 640, 1130, f, du + 6, 84, 2)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0008 * f)
    return c, (640 + 20 * math.sin(f * .04), 1430, z, 0), 'golden'


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


# ------------------------------------------------------------------ em tela: placar de TV + manchete do assunto
def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'JAP', 'BRA', 3, 2, JAP, BRA, 'FIM', lf)
    elif si == 1:
        ku0 = wt(1, 'Kubo'); k1 = max(14, ku0 - 9) + 9; k2 = max(ku0 + 18, wt(1, 'marcaram') - 4) + 9
        im = placar_tv(im, 'JAP', 'BRA', (lf >= k1) + (lf >= k2), 0, JAP, BRA, '1º T', lf + 99, pulse_a=k1 if lf < k2 else k2)
    elif si == 2:
        k = wt(2, 'chutaco') + 10
        im = placar_tv(im, 'JAP', 'BRA', 2, int(lf >= k), JAP, BRA, '1º T', lf + 99, pulse_b=k)
    elif si == 3:
        k = wt(3, 'empatou') - 3
        im = placar_tv(im, 'JAP', 'BRA', 2, 1 + (lf >= k), JAP, BRA, '2º T', lf + 99, pulse_b=k)
    elif si == 4:
        k = wt(4, 'Sakamoto') + 10
        im = placar_tv(im, 'JAP', 'BRA', 2 + (lf >= k), 2, JAP, BRA, 'ACR.', lf + 99, pulse_a=k)
    elif si == 5: im = placar_tv(im, 'JAP', 'BRA', 3, 2, JAP, BRA, 'FIM', lf + 99)
    D = {0: ('JAPÃO 3 x 2 BRASIL', 'GOL DA VITÓRIA NOS ACRÉSCIMOS', 4),
         1: ('KUBO E NAKAMURA', '2 GOLS EM MENOS DE 20 MINUTOS', wt(1, 'zero')),
         2: ('VINI JR. DIMINUI', 'CHUTE DE FORA DA ÁREA', wt(2, 'chutaco') + 12),
         3: ('VINI JR. DE NOVO', '2 GOLS NO JOGO', wt(3, 'Vini') - 3),
         4: ('SAKAMOTO DECIDE', 'NOS ACRÉSCIMOS', wt(4, 'Sakamoto') + 12),
         5: ('2 EXPULSOS', 'ANCELOTTI E RAPHINHA', wt(5, 'expulsos') - 3),
         6: ('2ª VITÓRIA DO JAPÃO', 'SOBRE O BRASIL NA HISTÓRIA', wt(6, 'segunda') - 3),
         7: ('BRASIL x SINGAPURA', 'TERÇA, 17/11, ÀS 7H', wt(7, 'terca') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (230, 60, 70) if si in (4, 5) else (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'tres') - 3, 150, .8)
    s.thunk(max(14, s.W(1, 'Kubo') - 9) + 9, 140, .7)
    s.thunk(max(s.W(1, 'Kubo') + 18, s.W(1, 'marcaram') - 4) + 9, 140, .7)
    s.thunk(s.W(2, 'chutaco') + 10, 160, .8)
    s.ting(s.W(3, 'empatou') - 3, .35)
    s.thunk(s.W(4, 'Sakamoto') + 10, 170, .9)
    s.thunk(s.W(5, 'expulsos') - 3, 150, .7)
    s.ting(s.W(6, 'segunda') - 3, .3)
    s.ting(s.W(7, 'terca') - 3, .3)
