"""anima.futebol — 17/11/2026 21h — Nations League: País de Gales 2x3 Portugal em Cardiff, gol do novo camisa 7 Carlos Forbs.
Fontes (conferidas em 17/11/2026): Observador (Cardiff City Stadium; Bruno Fernandes 11', Brooks 13', Sorba Thomas 41',
Pedro Neto 43', Forbs 70' após entrar aos 60' no lugar de Trincão; Neto expulso aos 74' por 2º amarelo; Portugal 1º do grupo;
técnicos Jorge Jesus e Craig Bellamy); RTP (3x2, Bruno de fora da área, Brooks, Sorba Thomas, Neto, Forbs saído do banco;
Neto expulso aos 73'; Portugal 1º com 15 pontos; quartas no fim de março; adversário no sorteio); Notícias de Coimbra
(Bruno 11', Neto 43' e expulso 74', Forbs 70'; 1º lugar do grupo); Sport TV (Forbs, do Brugge, 'orgulhoso' do número 7 de
Cristiano Ronaldo; 1º gol pela seleção principal); oGol ('com gol do novo camisa 7, Portugal vence Gales e avança em primeiro').
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'NATIONS LEAGUE  ·  6ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O novo camisa sete de Portugal, o primeiro depois de Cristiano Ronaldo, fez o gol da vitória por três a dois sobre o País de Gales.",
    "Foi em Cardiff, na última rodada da Nations League, depois de levar quatro a um da Dinamarca.",
    "Bruno Fernandes abriu o placar de fora da área, mas Brooks e Sorba Thomas viraram para os galeses.",
    "Pedro Neto empatou pouco antes do intervalo.",
    "Aos vinte e cinco do segundo tempo, Carlos Forbs, que tinha acabado de entrar, fez o primeiro gol dele pela seleção.",
    "Quatro minutos depois, Neto levou o segundo amarelo e foi expulso, mas Portugal segurou.",
    "Com quinze pontos, Portugal termina em primeiro do grupo e está nas quartas.",
    "O adversário sai no sorteio, e o mata-mata só começa em março.",
]
CAPTXT = [
    "O novo camisa 7 de Portugal, o 1º depois de Cristiano Ronaldo,|fez o gol da vitória por 3 a 2 sobre o País de Gales.",
    "Foi em Cardiff, na última rodada da Nations League,|depois de levar 4 a 1 da Dinamarca.",
    "Bruno Fernandes abriu o placar de fora da área,|mas Brooks e Sorba Thomas viraram para os galeses.",
    "Pedro Neto empatou|pouco antes do intervalo.",
    "Aos 25 do 2º tempo, Carlos Forbs, que tinha acabado de entrar,|fez o 1º gol dele pela seleção.",
    "4 minutos depois, Neto levou o 2º amarelo e foi expulso,|mas Portugal segurou.",
    "Com 15 pontos, Portugal termina em 1º do grupo|e está nas quartas.",
    "O adversário sai no sorteio,|e o mata-mata só começa em março.",
]
FALA_TIKTOK = "O novo camisa sete aguenta o peso da camisa? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Cristiano', 6), (0, 'dois', 4), (1, 'Cardiff', 4), (2, 'Bruno', 4), (2, 'viraram', 6), (3, 'empatou', 6),
         (4, 'Forbs', 6), (5, 'expulso', 6), (6, 'quinze', 4), (7, 'marco', 4)]

POR, POR_F = time_('PORTUGAL')
GAL = ('#c8102e', '#ffffff', '#c8102e'); GAL_F = None
GKP = ('#2fa35a', '#111111', '#111111')
GKG = ('#f2c94c', '#111111', '#111111')


def pt(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=POR, faixa=POR_F, hair='#2a1a10', sock='#c8102e', **kw)


def wa(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 0); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=GAL, faixa=GAL_F, hair='#6a4a2a', sock='#ffffff', **kw)


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


@lru_cache(maxsize=4)
def cartao(cor=(214, 30, 40)):
    im = Image.new('RGBA', (170, 240), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, 164, 234], 18, fill=cor + (255,), outline=INK + (255,), width=8)
    d.rectangle([24, 22, 60, 120], fill=tuple(min(255, v + 60) for v in cor) + (255,))
    return im


def put_cartao(c, x, y, f, f0, rot=-10, cor=(214, 30, 40)):
    if f < f0: return
    im = cartao(cor).rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y - 40 * (1 - back(ramp(f, f0, f0 + 8))), back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    cr = wt(0, 'Cristiano') - 3; tr = wt(0, 'tres') - 3
    wa(c, 300, 1700, 520, f, 11, arms='cheek', expr='pained')
    wa(c, 990, 1690, 500, f, 12, arms='cheek', expr='pained', skin=2, hs='cacheado', flip=True)
    x = lerp(1250, 640, easeOut(ramp(f, 0, 22)))
    if f < 24: linhas_vel(c, x, 2050, 900, f, dir=1)
    pt(c, x, 2050, 900, f, 6, arms='aviao' if f >= tr else 'run', expr='grin', run=(f * .08) % 1 if f < 22 else -1,
       num_='7', skin=4, hs='raspado', flip=True)
    num(c, 'NOVO 7', 640, 760, f, 6, 150, -3)
    if f < tr: num(c, 'DEPOIS DE CR7', 640, 930, f, cr, 90, 3)
    if f >= tr:
        confete(c, 640, 900, f, tr, 90, 900)
        explosao(c, 640, 1000, f, tr, 200)
        num(c, '3 x 2', 640, 1000, f, tr + 2, 140, -3)
    z = lerp(1.22, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, tr, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    ca = wt(1, 'Cardiff') - 3; go = wt(1, 'quatro') - 3
    xe = lerp(-250, 340, easeOut(ramp(f, 0, 18)))
    xs = lerp(1500, 920, easeOut(ramp(f, 0, 18)))
    pt(c, xe, 2000, 840, f, 21, arms='cintura' if f < go else 'cheek', expr='stern' if f < go else 'pained', look=1,
       run=(f * .09) % 1 if f < 18 else None, num_='8')
    wa(c, xs, 2000, 840, f, 22, arms='cintura', expr='stern', look=-1, flip=True, run=(f * .09) % 1 if f < 18 else None, num_='11')
    put_placa(c, 'PORTUGAL', POR, 340, 1080, f, 6, 64, -3)
    put_placa(c, 'PAÍS DE GALES', GAL, 920, 1080, f, 8, 56, 3)
    num(c, 'CARDIFF', 640, 740, f, ca, 110, -2)
    if f >= go: num(c, 'ANTES: 1 x 4 DINAMARCA', 640, 900, f, go, 70, 3)
    z = lerp(1.0, 1.1, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .04), 1420, z, 0), 'dusk'


def _k2():
    k0 = max(8, wt(2, 'fora') - 3)
    k1 = max(k0 + 28, wt(2, 'Brooks') - 3)
    k2 = max(k1 + 22, wt(2, 'Thomas') - 3)
    return k0, k1, k2


def s2(f):
    c = estadio2('dusk').copy()
    k0, k1, k2 = _k2()
    if f < k1 - 4:
        gx, gy = put_gol2(c, x=760, estufa=pulse(f, k0 + 9, 10))
        put_goleiro(c, f, GKG, None, gx=780 - 60 * clamp((f - k0) / 7), arms='up', expr='shock', skin=0)
        x = 360
        pt(c, x, 2030, 880, f, 8, arms='run' if f < k0 + 10 else 'punho', kick=pulse(f, k0 - 4, 5) if f >= k0 - 4 else 0,
           expr='stern' if f < k0 else 'grin', num_='8', hs='curto', skin=1)
        foco(c, x, 1640, 380, .85 * pulse(f, wt(2, 'Bruno') - 3, 30))
        put_placa(c, 'BRUNO FERNANDES', POR, 880, 1150, f, wt(2, 'Bruno') - 3, 52, -3)
        chute_gol(c, f, k0, x, 880, gx, gy, alvo=(120, -20), arco=220)
        if f >= k0 + 9: gol_txt(c, f, k0 + 9, 640, 860, 'DE FORA!')
        k = kick(f, k0 + 9)
        return c, (lerp(600, 660, smooth(f / 60)), 1430 + k * 10, 1.05, k), 'dusk'
    kf = k1 if f < k2 - 4 else k2
    gx, gy = put_gol2(c, x=740, estufa=pulse(f, kf + 9, 8))
    put_goleiro(c, f, GKP, None, gx=760 + (60 if kf == k1 else -60) * clamp((f - kf) / 7), arms='up', expr='shock', skin=1)
    if kf == k1:
        x = lerp(-200, 360, easeOut(ramp(f, k1 - 4, k1 - 1)))
        wa(c, x, 2030, 870, f, 14, arms='run' if f < k1 + 8 else 'punho', kick=pulse(f, k1 - 4, 5) if f >= k1 - 4 else 0,
           expr='grin', num_='20', hs='topete', skin=0)
        put_placa(c, 'BROOKS', GAL, 900, 1150, f, k1 - 4, 60, -3)
        chute_gol(c, f, k1, x, 870, gx, gy)
        if f >= k1 + 9: gol_txt(c, f, k1 + 9, 640, 860, '1 x 1', (230, 60, 70))
    else:
        x = lerp(1450, 880, easeOut(ramp(f, k2 - 4, k2 - 1)))
        wa(c, x, 2030, 860, f, 15, arms='run' if f < k2 + 8 else 'aviao', kick=pulse(f, k2 - 4, 5) if f >= k2 - 4 else 0,
           expr='grin', num_='14', hs='raspado', skin=4, flip=True)
        rb = raio_bola(860)
        bola_voo(c, f, k2, x - 110, 2030 - rb, gx + 40, gy - 10, rb, raio_bola(300), 140)
        put_placa(c, 'SORBA THOMAS', GAL, 420, 1150, f, k2 - 4, 56, 3)
        if f >= k2 + 9: gol_txt(c, f, k2 + 9, 640, 860, 'VIRADA!', (230, 60, 70))
    k = kick(f, k1 + 9, .8) + kick(f, k2 + 9, .8)
    return c, (lerp(620, 680, smooth(f / 120)), 1430 + k * 10, 1.05 * (1 + .0006 * f), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    kf = max(8, wt(3, 'empatou') - 3)
    gx, gy = put_gol2(c, x=700, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKG, None, gx=720 - 70 * clamp((f - kf) / 7), arms='up', expr='shock' if f >= kf + 5 else 'nervous', skin=0)
    x = lerp(-200, 340, easeOut(ramp(f, 0, kf - 3)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
    pt(c, x, 2030, 860, f, 9, arms='run' if f < kf + 8 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
       kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='stern' if f < kf else 'grin', num_='17', hs='cacheado', skin=2)
    put_placa(c, 'PEDRO NETO', POR, 900, 1150, f, max(0, wt(3, 'Pedro') - 3), 60, -3)
    chute_gol(c, f, kf, x, 860, gx, gy)
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, '2 x 2')
    k = kick(f, kf + 9)
    return c, (lerp(600, 660, smooth(f / 60)), 1430 + k * 10, lerp(1.0, 1.08, smooth(f / 70)), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    vi = wt(4, 'vinte') - 3; fo = wt(4, 'Forbs') - 3; en = wt(4, 'entrar') - 3; pr = wt(4, 'primeiro') - 3
    kf = max(en + 6, fo + 14)
    gx, gy = put_gol2(c, x=740, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKG, None, gx=760 + 70 * clamp((f - kf) / 7), arms='up', expr='shock' if f >= kf + 5 else 'nervous', skin=0)
    x = lerp(1450, 860, easeOut(ramp(f, fo - 6, kf - 3)))
    if fo - 6 <= f < kf - 4: linhas_vel(c, x, 2030, 880, f, dir=1)
    if f >= fo - 6:
        pt(c, x, 2030, 880, f, 6, arms='run' if f < kf + 8 else 'aviao', run=(f * .09) % 1 if f < kf - 4 else None,
           kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='stern' if f < kf else 'grin', num_='7', hs='raspado', skin=4, flip=True)
        foco(c, x, 1640, 380, .85 * pulse(f, fo, 30))
    rb = raio_bola(880)
    if f >= fo - 6: bola_voo(c, f, kf, x - 115, 2030 - rb, gx + 50, gy - 10, rb, raio_bola(300), 150)
    if f < fo: num(c, "70'", 640, 900, f, vi, 160, -3)
    put_placa(c, 'CARLOS FORBS', POR, 420, 1150, f, fo, 58, 3)
    if f >= kf + 9:
        confete(c, 640, 860, f, kf + 9, 80, 900)
        gol_txt(c, f, kf + 9, 640, 860, '3 x 2')
    if f >= pr: num(c, '1º GOL NA SELEÇÃO', 640, 1020, f, pr, 76, 3)
    k = kick(f, kf + 9)
    return c, (lerp(680, 620, smooth(f / 90)), 1430 + k * 10, 1.05 * (1 + .0007 * f), k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    am = wt(5, 'amarelo') - 3; ex = wt(5, 'expulso') - 3; se = wt(5, 'segurou') - 3
    if f < se - 4:
        pt(c, 640, 2030, 900, f, 9, arms='cheek' if f >= ex else 'hang', expr='pained' if f >= ex else 'nervous',
           num_='17', hs='cacheado', skin=2)
        put_placa(c, 'PEDRO NETO', POR, 640, 1080, f, 4, 62, -3)
        put_cartao(c, 470, 820, f, am, -12, (245, 200, 40))
        put_cartao(c, 810, 820, f, ex, 10)
        if f >= ex: num(c, 'EXPULSO!', 640, 1230, f, ex + 2, 100, -3)
        num(c, "74'", 640, 680, f, 2, 90, 3)
        k = kick(f, ex, .8)
        return c, (640, 1430 + k * 8, lerp(1.08, 1.0, smooth(f / 50)), k), 'dusk'
    for i, (x, s) in enumerate(((260, 'topete'), (640, 'raspado'), (1020, 'curto'))):
        pt(c, x, 1990 + (40 if i == 1 else 0), 780 + (60 if i == 1 else 0), f, 40 + i, num_=('8', '7', '4')[i],
           arms='up', expr='grin', skin=(1, 4, 0)[i], hs=s)
    confete(c, 640, 800, f, se, 70, 900)
    num(c, 'COM 10', 640, 780, f, se, 110, -3)
    num(c, 'VITÓRIA!', 640, 950, f, se + 4, 110, 3)
    z = lerp(1.1, 1.0, smooth((f - se) / 40))
    return c, (640 + 20 * math.sin(f * .05), 1420, z, 0), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    qz = wt(6, 'quinze') - 3; qa = wt(6, 'quartas') - 3
    tabela(c, [('1º', 'PORTUGAL', POR, '15', True)], 640, 820, f, qz)
    if f >= qa: num(c, 'NAS QUARTAS!', 640, 1130, f, qa, 110, -3)
    pt(c, 640, 1720, 520, f, 6, arms='up' if f >= qa else 'cintura', expr='grin', num_='7', hs='raspado', skin=4)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    return c, (640, lerp(1300, 1360, smooth(f / 150)), z, 0), 'dusk'


def s7(f):
    c = estadio2('dusk').copy()
    so = wt(7, 'sorteio') - 3; ma = wt(7, 'marco') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, 0, 16)))
    pt(c, bx, 2010, 860, f, 3, arms='cintura', expr='proud', look=1, run=(f * .09) % 1 if f < 16 else None, num_='7', hs='raspado', skin=4)
    sx = lerp(1550, 940, easeOut(ramp(f, 0, 16)))
    put_atleta(c, sx, 2010, 860, f, 7, cores=('#555a66', '#555a66', '#555a66'), faixa=None, hair='#3a3d46', sock='#555a66',
               arms='shrug', expr='neutral', look=-1, flip=True, run=(f * .09) % 1 if f < 16 else None, skin=2, hs='curto')
    num(c, '?', 940, 1050, f, so, 200, 6)
    if f >= so: num(c, 'SORTEIO', 640, 780, f, so, 120, -3)
    if f >= ma: num(c, 'MARÇO', 640, 940, f, ma, 110, 3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, so, .6) + kick(f, ma, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def _k4():
    return max(wt(4, 'entrar') + 3, wt(4, 'Forbs') + 11) + 9


def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'GAL', 'POR', 2, 3, GAL, POR, 'FIM', lf)
    elif si == 2:
        k0, k1, k2 = _k2()
        im = placar_tv(im, 'GAL', 'POR', (lf >= k1 + 9) + (lf >= k2 + 9), int(lf >= k0 + 9), GAL, POR, '1º T', lf + 99,
                       pulse_b=k0 + 9, pulse_a=k1 + 9 if lf < k2 + 9 else k2 + 9)
    elif si == 3:
        k = max(8, wt(3, 'empatou') - 3) + 9
        im = placar_tv(im, 'GAL', 'POR', 2, 1 + (lf >= k), GAL, POR, '1º T', lf + 99, pulse_b=k)
    elif si == 4:
        k = _k4()
        im = placar_tv(im, 'GAL', 'POR', 2, 2 + (lf >= k), GAL, POR, '2º T', lf + 99, pulse_b=k)
    elif si == 5:
        im = placar_tv(im, 'GAL', 'POR', 2, 3, GAL, POR, '2º T' if lf < wt(5, 'segurou') - 3 else 'FIM', lf + 99)
    k0, k1, k2 = _k2()
    D = {0: ('GALES 2 x 3 PORTUGAL', 'GOL DO NOVO CAMISA 7', 4),
         1: ('ÚLTIMA RODADA DO GRUPO', 'EM CARDIFF, NO PAÍS DE GALES', wt(1, 'Cardiff') - 3),
         2: ('BRUNO ABRE, GALES VIRA', 'BROOKS E SORBA THOMAS', k2 + 12),
         3: ('PEDRO NETO EMPATA', 'POUCO ANTES DO INTERVALO', max(8, wt(3, 'empatou') - 3) + 12),
         4: ('CARLOS FORBS DECIDE', 'ENTROU E FEZ O 1º GOL NA SELEÇÃO', _k4() + 4),
         5: ('NETO EXPULSO AOS 74', 'PORTUGAL SEGURA COM 10', wt(5, 'expulso') + 2),
         6: ('PORTUGAL EM 1º', '15 PONTOS NO GRUPO', wt(6, 'quinze') - 3),
         7: ('QUARTAS DE FINAL', 'ADVERSÁRIO SAI NO SORTEIO', wt(7, 'sorteio') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (230, 60, 70) if si in (2, 5) else (255, 216, 74), y=1250)


def SFX(s):
    s.thunk(s.W(0, 'tres') - 3, 150, .8)
    s.ting(s.W(1, 'Cardiff') - 3, .3)
    k0 = max(8, s.W(2, 'fora') - 3); k1 = max(k0 + 28, s.W(2, 'Brooks') - 3); k2 = max(k1 + 22, s.W(2, 'Thomas') - 3)
    for k in (k0, k1, k2): s.thunk(k + 9, 140, .7)
    s.thunk(max(8, s.W(3, 'empatou') - 3) + 9, 140, .7)
    s.thunk(max(s.W(4, 'entrar') + 3, s.W(4, 'Forbs') + 11) + 9, 140, .8)
    s.thunk(s.W(5, 'expulso') - 3, 150, .8)
    s.ting(s.W(5, 'segurou') - 3, .3)
    s.ting(s.W(6, 'quinze') - 3, .3)
    s.ting(s.W(7, 'sorteio') - 3, .3)
