"""anima.futebol — 16/11/2026 07h — Ronaldinho Gaúcho volta a jogar aos 46 anos: Ravenna 2x0 Forlì (Série C da Itália).
Fontes (conferidas em 16/11/2026): Terra (Ravenna 2x0 Forlì pela Série C italiana, estádio Bruno Benelli; Ronaldinho, 46 anos,
titular, jogou o 1º tempo e saiu no intervalo; participou da jogada do 1º gol, com finalização de fora da área envolvendo Lonardi e Donati);
Itatiaia (2x0 no Bruno Benelli; Donati fez o 1º gol perto do fim do 1º tempo; Ronaldinho, 46 anos, 11 anos sem jogar, titular,
jogou o 1º tempo; passe dele originou a jogada do gol de Donati); Yahoo Sports/CNN Brasil/Terra (titular no domingo 15/11, 1º jogo
oficial em mais de 11 anos); Lance! (Ronaldinho estreou pelo Ravenna com vitória por 2 a 0 sobre o Forlì).
Sem escudos/logos nem rosto real: times por plaquinhas e cores; Ronaldinho é um boneco genérico com placa do nome."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SÉRIE C DA ITÁLIA  ·  A VOLTA DO BRUXO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Aos quarenta e seis anos, Ronaldinho Gaúcho voltou a jogar futebol profissional, e ainda saiu vencedor.",
    "Foi ontem, na terceira divisão da Itália: Ravenna contra o Forlì, no estádio Bruno Benelli.",
    "Ele não jogava uma partida oficial havia onze anos, e mesmo assim começou como titular.",
    "No fim do primeiro tempo, um passe dele começou a jogada do primeiro gol, marcado por Donati.",
    "Ronaldinho jogou só o primeiro tempo e saiu no intervalo.",
    "Sem ele em campo, o Ravenna fez mais um e venceu por dois a zero.",
    "Agora, a dúvida é quantos jogos o Bruxo ainda vai fazer nessa volta.",
]
CAPTXT = [
    "Aos 46 anos, Ronaldinho Gaúcho voltou a jogar|futebol profissional, e ainda saiu vencedor.",
    "Foi ontem, na terceira divisão da Itália: Ravenna|contra o Forlì, no estádio Bruno Benelli.",
    "Ele não jogava uma partida oficial havia 11 anos,|e mesmo assim começou como titular.",
    "No fim do primeiro tempo, um passe dele começou|a jogada do primeiro gol, marcado por Donati.",
    "Ronaldinho jogou só o primeiro tempo|e saiu no intervalo.",
    "Sem ele em campo, o Ravenna fez mais um|e venceu por 2 a 0.",
    "Agora, a dúvida é quantos jogos o Bruxo|ainda vai fazer nessa volta.",
]
FALA_TIKTOK = "Você queria ver o Ronaldinho jogando de novo? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'quarenta', 6), (0, 'vencedor', 4), (1, 'Italia', 4), (1, 'Benelli', 4), (2, 'onze', 6), (2, 'titular', 4),
         (3, 'passe', 6), (3, 'Donati', 6), (4, 'intervalo', 4), (5, 'dois', 4), (6, 'Bruxo', 4)]

RAV, RAV_F = time_('RAVENNA')
FOR, FOR_F = time_('FORLÌ')
GKF = ('#2fa35a', '#111111', '#111111')


def rav(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=RAV, faixa=RAV_F, hair='#2a1a10', sock='#c8102e', **kw)


def r10(c, x, y, h, f, **kw):
    """Ronaldinho: boneco genérico de camisa 10 do Ravenna (sem tentar parecer com ele)."""
    kw.setdefault('expr', 'grin')
    rav(c, x, y, h, f, 10, skin=3, hs='cacheado', num_='10', **kw)


def frl(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 0); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=FOR, faixa=FOR_F, hair='#4a3020', sock='#ffffff', **kw)


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


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    qu = wt(0, 'quarenta') - 3; ro = wt(0, 'Ronaldinho') - 3; ve = wt(0, 'vencedor') - 3
    x = lerp(-250, 640, easeOut(ramp(f, 0, 20)))
    if f < 20: linhas_vel(c, x, 2030, 900, f)
    r10(c, x, 2030, 900, f, arms='up' if f >= ve else ('run' if f < 20 else 'joinha'), run=(f * .08) % 1 if f < 20 else None)
    num(c, '46 ANOS', 640, 760, f, qu, 160, -4)
    put_placa(c, 'RONALDINHO', RAV, 640, 1060, f, ro, 66, 3)
    if f >= ve:
        confete(c, 640, 900, f, ve, 90, 900)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, qu, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    it = wt(1, 'Italia') - 3; ra = wt(1, 'Ravenna') - 3; fo = wt(1, 'Forli') - 3; be = wt(1, 'Bruno') - 3
    xr = lerp(-250, 340, easeOut(ramp(f, ra - 12, ra + 6)))
    xf = lerp(1500, 920, easeOut(ramp(f, fo - 12, fo + 6)))
    rav(c, xr, 2010, 840, f, 21, arms='cintura', expr='stern', look=1, num_='5', run=(f * .09) % 1 if f < ra + 6 else None)
    frl(c, xf, 2010, 840, f, 22, arms='cintura', expr='stern', look=-1, flip=True, num_='8', run=(f * .09) % 1 if f < fo + 6 else None)
    put_placa(c, 'RAVENNA', RAV, 340, 1080, f, ra + 2, 62, -3)
    put_placa(c, 'FORLÌ', FOR, 920, 1080, f, fo + 2, 62, 3)
    num(c, 'ITÁLIA', 640, 720, f, it, 130, -3)
    num(c, '3ª DIVISÃO', 640, 870, f, it + 6, 90, 3)
    num(c, 'X', 640, 1500, f, fo + 6, 150)
    z = lerp(1.0, 1.1, smooth(f / 130))
    return c, (640 + 30 * math.sin(f * .04), 1420, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    on = wt(2, 'onze') - 3; ti = wt(2, 'titular') - 3
    if f >= on:
        paste_c(c, calendario('11', 'ANOS'), 640, 800, .75 * back(ramp(f, on, on + 8)))
    if f < ti - 2: num(c, 'SEM JOGO OFICIAL', 640, 1120, f, on + 8, 80, -3)
    x = lerp(1450, 640, easeOut(ramp(f, ti - 16, ti)))
    if f >= ti - 16:
        if f < ti: linhas_vel(c, x, 2030, 880, f, dir=1)
        r10(c, x, 2030, 880, f, arms='run' if f < ti else 'punho', run=(f * .08) % 1 if f < ti else None, flip=True)
    if f >= ti:
        explosao(c, 640, 1120, f, ti, 190)
        num(c, 'TITULAR!', 640, 1120, f, ti + 2, 110, 3)
    z = lerp(1.12, 1.02, smooth(f / 90))
    k = kick(f, ti, .7)
    return c, (640, lerp(1380, 1430, smooth(f / 120)) + k * 8, z, k), 'dusk'


def _k3():
    pa = wt(3, 'passe') - 3
    kd = max(pa + 22, wt(3, 'Donati') - 6)
    return pa, kd


def s3(f):
    c = estadio2('dusk').copy()
    pa, kd = _k3()
    gx, gy = put_gol2(c, x=760, estufa=pulse(f, kd + 9, 10))
    put_goleiro(c, f, GKF, None, gx=780 - 60 * clamp((f - kd) / 7), arms='up', expr='shock' if f >= kd + 5 else 'nervous', skin=0)
    # Ronaldinho à esquerda passa para Donati à direita
    rx, dx = 300, 900
    r10(c, rx, 2030, 860, f, arms='point' if f >= pa + 8 else 'run', kick=pulse(f, pa - 4, 5) if f >= pa - 4 else 0,
        expr='grin' if f >= pa else 'stern')
    rav(c, dx, 2010, 840, f, 4, arms='run' if f < kd + 10 else 'aviao', kick=pulse(f, kd - 4, 5) if f >= kd - 4 else 0,
        expr='stern' if f < kd else 'grin', num_='2', skin=0, hs='topete', flip=True)
    rb = raio_bola(860)
    if f < pa + 10:
        bola_voo(c, f, pa, rx + 110, 2030 - rb, dx - 90, 2010 - rb, rb, rb, 30, 10)
    else:
        bola_voo(c, f, kd, dx - 90, 2010 - rb, gx + 70, gy - 10, rb, raio_bola(300), 150, 10)
    put_placa(c, 'RONALDINHO', RAV, rx + 90, 1110, f, wt(3, 'dele') - 3, 52, -3)
    put_placa(c, 'DONATI', RAV, dx, 1110, f, wt(3, 'Donati') - 4, 58, 3)
    if f < pa: num(c, 'FIM DO 1º TEMPO', 640, 760, f, wt(3, 'fim') - 3, 84, -2)
    if f >= kd + 9: gol_txt(c, f, kd + 9, 640, 860, 'GOL!')
    k = kick(f, kd + 9)
    return c, (lerp(600, 680, smooth(f / 110)), 1430 + k * 10, 1.04 * (1 + .0007 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    pr = wt(4, 'primeiro') - 3; iv = wt(4, 'intervalo') - 3
    x = lerp(640, 1350, smooth(ramp(f, iv, iv + 40)))
    r10(c, x, 2020, 880, f, arms='joinha' if f < iv else 'hang', expr='grin', run=(f * .05) % 1 if f >= iv else None)
    num(c, '45 MINUTOS', 640, 720, f, pr, 130, -3)
    if f >= iv:
        explosao(c, 640, 1000, f, iv, 180, (230, 60, 70))
        num(c, 'INTERVALO', 640, 1000, f, iv + 2, 100, 3)
    z = lerp(1.1, 1.0, smooth(f / 60))
    return c, (lerp(640, 720, smooth(ramp(f, iv, iv + 40))), 1420, z, 0), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    ma = wt(5, 'mais') - 3; ve = wt(5, 'venceu') - 3
    if f < ve - 2:
        kf = max(8, ma)
        gx, gy = put_gol2(c, x=760, estufa=pulse(f, kf + 9, 10))
        put_goleiro(c, f, GKF, None, gx=780 + 60 * clamp((f - kf) / 7), arms='up', expr='shock', skin=0)
        x = lerp(-200, 360, easeOut(ramp(f, 0, kf - 3)))
        if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
        rav(c, x, 2030, 860, f, 19, arms='run' if f < kf + 6 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
            kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='9', skin=4, hs='raspado')
        rb = raio_bola(860)
        bola_voo(c, f, kf, x + 110, 2030 - rb, gx + 60, gy - 10, rb, raio_bola(300), 150)
        if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, '2 x 0')
        k = kick(f, kf + 9)
        return c, (lerp(600, 660, smooth(f / 60)), 1430 + k * 10, 1.05, k), 'dusk'
    for i, (x, s, sk) in enumerate(((260, 'topete', 0), (640, 'raspado', 4), (1020, 'curto', 1))):
        rav(c, x, 1990 + (40 if i == 1 else 0), 780 + (60 if i == 1 else 0), f, 40 + i, num_=('2', '9', '7')[i],
            arms='up', expr='grin', skin=sk, hs=s)
    confete(c, 640, 800, f, ve, 70, 900)
    num(c, 'VITÓRIA!', 640, 820, f, ve + 2, 120, -3)
    put_placa(c, 'RAVENNA', RAV, 640, 1000, f, ve + 4, 60, 3)
    z = lerp(1.1, 1.0, smooth((f - ve) / 40))
    return c, (640 + 20 * math.sin(f * .05), 1420, z, 0), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    qj = wt(6, 'quantos') - 3; br = wt(6, 'Bruxo') - 3; vo = wt(6, 'volta') - 3
    r10(c, 640, 2030, 920, f, arms='shrug' if f >= qj else 'cintura', expr='smug' if f >= br else 'grin')
    foco(c, 640, 1600, 420, .8 * ramp(f, br - 4, br + 10))
    num(c, 'QUANTOS JOGOS?', 640, 760, f, qj, 100, -3)
    put_placa(c, 'O BRUXO', RAV, 640, 1060, f, br, 66, 3)
    if f >= vo: num(c, '?', 960, 1200, f, vo, 200, 8)
    z = lerp(1.0, 1.14, smooth(f / 110))
    return c, (640, 1420, z, lerp(0, -2, smooth(f / 110))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'RAV', 'FOR', 2, 0, RAV, FOR, 'FIM', lf)
    elif si == 3:
        pa, kd = _k3(); k = kd + 9
        im = placar_tv(im, 'RAV', 'FOR', int(lf >= k), 0, RAV, FOR, '1º T', lf + 99, pulse_a=k)
    elif si == 5:
        k = max(8, wt(5, 'mais') - 3) + 9
        im = placar_tv(im, 'RAV', 'FOR', 1 + (lf >= k), 0, RAV, FOR, '2º T' if lf < wt(5, 'venceu') - 3 else 'FIM', lf + 99, pulse_a=k)
    pa, kd = _k3()
    D = {0: ('RONALDINHO VOLTOU', 'AOS 46 ANOS, COM VITÓRIA', 4),
         1: ('RAVENNA x FORLÌ, NA ITÁLIA', 'NO ESTÁDIO BRUNO BENELLI', wt(1, 'Bruno') - 3),
         2: ('11 ANOS DEPOIS', 'E DIRETO COMO TITULAR', wt(2, 'titular') + 6),
         3: ('PASSE DO BRUXO', 'COMEÇA A JOGADA DO GOL DE DONATI', kd + 14),
         4: ('SÓ O PRIMEIRO TEMPO', 'SAIU NO INTERVALO', wt(4, 'intervalo') + 4),
         5: ('RAVENNA 2 x 0 FORLÌ', 'VITÓRIA NA REESTREIA', wt(5, 'venceu') - 1),
         6: ('E AGORA, BRUXO?', 'QUANTOS JOGOS MAIS?', wt(6, 'Bruxo') + 4)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'quarenta') - 3, 150, .8)
    s.ting(s.W(0, 'vencedor') - 3, .35)
    s.thunk(s.W(1, 'Italia') - 3, 160, .6)
    s.thunk(s.W(2, 'onze') - 3, 150, .7)
    s.ting(s.W(2, 'titular') - 3, .35)
    pa = s.W(3, 'passe') - 3; kd = max(pa + 22, s.W(3, 'Donati') - 6)
    s.thunk(pa, 200, .5)
    s.thunk(kd + 9, 140, .8)
    s.ting(s.W(4, 'intervalo') - 3, .3)
    s.thunk(max(8, s.W(5, 'mais') - 3) + 9, 140, .7)
    s.ting(s.W(5, 'venceu') - 3, .3)
    s.ting(s.W(6, 'Bruxo') - 3, .3)
