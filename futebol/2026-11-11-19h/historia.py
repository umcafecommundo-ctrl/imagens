"""anima.futebol — 11/11/2026 19h — Seleções: 1ª Data Fifa sem Messi, Cristiano Ronaldo e Neymar em mais de 15 anos.
Fontes (conferidas em 11/11/2026): Récord (MX, 10/11: Data Fifa de 9 a 17/11 sem os três, todos aposentados das seleções;
Messi 208 jogos/126 gols; CR7 234 jogos/146 gols; Neymar 130 jogos/80 gols); Metrópoles (05/11: CR7 anunciou o adeus em vídeo
em 05/11 após 23 anos; Messi anunciou em 31/08, 208 jogos e 126 gols; Neymar encerrou o ciclo após a Copa de 2026);
A Crítica (CR7 234 jogos, 146 gols, 3 títulos); Diário de Pernambuco (Neymar 130 jogos, 80 gols, maior artilheiro da Seleção).
Fontes divergem sobre o ano exato (2004/2009/2010): usamos "mais de quinze anos".
Sem escudos/logos nem rostos reais: bonecos genéricos com camisa nas cores e plaquinha do nome."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SELEÇÕES  ·  DATA FIFA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Pela primeira vez em mais de quinze anos, uma Data Fifa começa sem Messi, sem Cristiano Ronaldo e sem Neymar.",
    "Os três se despediram das seleções em dois mil e vinte e seis, o ano da Copa.",
    "O último foi Cristiano Ronaldo, que deu adeus a Portugal na semana passada, depois de vinte e três anos.",
    "Ele sai com duzentos e trinta e quatro jogos e cento e quarenta e seis gols, o maior artilheiro de seleções da história.",
    "Messi fechou a conta com duzentos e oito jogos e cento e vinte e seis gols, e uma Copa do Mundo no currículo.",
    "E Neymar parou nos oitenta gols, o maior artilheiro da história da Seleção Brasileira.",
    "Somando os três, são trezentos e cinquenta e dois gols com a camisa das seleções.",
    "Agora fica a pergunta: quem vai herdar esse trono?",
]
CAPTXT = [
    "Pela 1ª vez em mais de 15 anos, uma Data Fifa começa|sem Messi, sem Cristiano Ronaldo e sem Neymar.",
    "Os 3 se despediram das seleções|em 2026, o ano da Copa.",
    "O último foi Cristiano Ronaldo, que deu adeus a Portugal|na semana passada, depois de 23 anos.",
    "Ele sai com 234 jogos e 146 gols,|o maior artilheiro de seleções da história.",
    "Messi fechou a conta com 208 jogos e 126 gols,|e uma Copa do Mundo no currículo.",
    "E Neymar parou nos 80 gols,|o maior artilheiro da história da Seleção Brasileira.",
    "Somando os 3, são 352 gols|com a camisa das seleções.",
    "Agora fica a pergunta:|quem vai herdar esse trono?",
]
FALA_TIKTOK = "Quem vai ser o novo dono desse trono? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM HERDA?"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'Messi', 4), (0, 'Neymar', 4), (1, 'Copa', 4), (2, 'Portugal', 4), (3, 'quarenta', 6), (4, 'Copa', 4),
         (5, 'oitenta', 4), (6, 'dois', 6), (7, 'trono', 4)]

ARG, ARG_F = time_('ARGENTINA')
POR, POR_F = time_('PORTUGAL')
BRA, BRA_F = time_('BRASIL')
CINZA, _ = time_('GENÉRICO')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def tres(c, f, y=2010, h=720, arms='hang', expr='neutral', k0=(0, 0, 0)):
    put_jog(c, 270, y, h, f, 1, cores=ARG, faixa=ARG_F, arms=arms, expr=expr, skin=0, hair='#3a2414')
    put_jog(c, 640, y + 15, h, f, 2, cores=POR, faixa=POR_F, arms=arms, expr=expr, skin=1, hair='#1a1410')
    put_jog(c, 1010, y, h, f, 3, cores=BRA, faixa=BRA_F, arms=arms, expr=expr, skin=2, hair='#151515')


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    me = wt(0, 'Messi') - 3; cr = wt(0, 'Cristiano') - 3; ne = wt(0, 'Neymar') - 3
    num(c, 'DATA FIFA', 640, 700, f, wt(0, 'Data') - 3, 150, -4)
    num(c, 'SEM ELES!', 640, 880, f, wt(0, 'sem') - 3, 120, 3)
    tres(c, f, arms='up', expr='proud')
    put_placa(c, 'MESSI', ARG, 280, 1180, f, me, 46, -4)
    put_placa(c, 'CRISTIANO', POR, 640, 1230, f, cr, 46, 3)
    put_placa(c, 'NEYMAR', BRA, 990, 1180, f, ne, 46, -3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, ne, .7)
    return c, (640, 1430 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    put_trofeu(c, 640, 1180, 460, f, wt(1, 'Copa') - 3)
    num(c, '2026', 640, 720, f, wt(1, 'dois') - 3, 190, -4)
    tres(c, f, h=700, arms='cheek' if f >= wt(1, 'despediram') - 3 else 'hang', expr='pained' if f >= wt(1, 'despediram') - 3 else 'neutral')
    num(c, 'ADEUS!', 640, 890, f, wt(1, 'despediram') - 3, 100, 4)
    return c, (640 + 20 * math.sin(f * .03), 1420, lerp(1.04, 1.14, smooth(f / 110)), 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    po = wt(2, 'Portugal') - 3
    put_jog(c, 640, 2030, 920, f, 2, cores=POR, faixa=POR_F, arms='up' if f >= po else 'hang', expr='proud', skin=1, hair='#1a1410', num_='7')
    put_placa(c, 'CRISTIANO RONALDO', POR, 640, 1100, f, wt(2, 'Cristiano') - 3, 60, -3)
    num(c, 'ADEUS, PORTUGAL', 640, 700, f, po, 80, -3)
    num(c, '23 ANOS', 640, 870, f, wt(2, 'vinte') - 3, 140, 4)
    z = lerp(1.2, 1.06, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    return c, (640, lerp(1440, 1400, smooth(f / 120)), z, 0), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    go = wt(3, 'quarenta') - 4
    put_goleiro(c, f, CINZA, None, arms='shrug', expr='shock' if f >= go else 'nervous', skin=0, hair='#3a3d46')
    put_jog(c, 470, 1990, 860, f, 2, cores=POR, faixa=POR_F, arms='up' if f >= go + 8 else 'run', kick=pulse(f, go - 5, 5),
            expr='grin' if f >= go else 'stern', skin=1, hair='#1a1410', num_='7')
    rb = raio_bola(860)
    if f < go - 5: bx, by, r = 640, 1990 - rb, rb
    else: t = ramp(f, go - 5, go + 3); bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, '234 JOGOS', 640, 700, f, wt(3, 'duzentos') - 3, 130, -4)
    num(c, '146 GOLS', 640, 860, f, go, 150, 3)
    num(c, 'RECORDE!', 420, 1040, f, wt(3, 'artilheiro') - 3, 100, -5)
    k = kick(f, go)
    return c, (lerp(600, 680, smooth(f / 120)), 1470 + k * 10, 1.1 * (1 + .0007 * f), k), 'dusk'


def s4(f):
    c = estadio('day').copy()
    cp = wt(4, 'Copa') - 3
    put_trofeu(c, 930, 1300, 480, f, cp)
    put_jog(c, 430, 2030, 900, f, 1, cores=ARG, faixa=ARG_F, arms='up' if f >= cp else 'cintura', expr='grin' if f >= cp else 'proud',
            skin=0, hair='#3a2414', num_='10')
    put_placa(c, 'MESSI', ARG, 430, 1110, f, wt(4, 'Messi') - 3, 64, -3)
    num(c, '208 JOGOS', 640, 700, f, wt(4, 'duzentos') - 3, 130, -4)
    num(c, '126 GOLS', 640, 860, f, wt(4, 'vinte') - 3, 150, 3)
    z = lerp(1.18, 1.05, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    return c, (640 + 20 * math.sin(f * .04), 1420, z, 0), 'golden'


def s5(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    ca = wt(5, 'oitenta') - 4
    pulo = pulse(f, ca - 8, 10)
    put_goleiro(c, f, CINZA, None, arms='cheek' if f >= ca else 'hang', expr='pained' if f >= ca else 'nervous', skin=3, hair='#111111')
    put_jog(c, 560, 1990 - 160 * pulo, 860, f, 3, cores=BRA, faixa=BRA_F, arms='up' if f >= ca + 6 else 'run',
            expr='grin' if f >= ca else 'stern', skin=2, hair='#151515', num_='10')
    put_placa(c, 'NEYMAR', BRA, 560, 1130 - 160 * pulo, f, wt(5, 'Neymar') - 3, 56, -3)
    rb = raio_bola(860)
    if f < ca - 14: bx, by, r = lerp(-60, 560, ramp(f, 0, ca - 14)), 1300, rb
    elif f < ca: bx, by, r = 560, lerp(1300, 1170 - 160 * pulo, ramp(f, ca - 14, ca)), rb
    else: t = ramp(f, ca, ca + 8); bx, by, r = lerp(560, gx + 90, t), lerp(1170, gy, t), lerp(rb, raio_bola(300), t)
    if f < ca + 9: put_bola(c, bx, by, r, f)
    num(c, '80 GOLS', 640, 720, f, ca + 2, 160, -4)
    num(c, 'MAIOR DA SELEÇÃO', 640, 890, f, wt(5, 'maior') - 3, 76, 3)
    k = kick(f, ca, .9)
    return c, (640 + 15 * math.sin(f * .03), 1460 + k * 10, 1.1 * (1 + .0008 * f), k), 'golden'


def s6(f):
    c = estadio('dusk').copy()
    so = wt(6, 'dois') - 3
    tres(c, f, h=760, arms='up' if f >= so else 'cintura', expr='grin' if f >= so else 'proud')
    num(c, '126', 290, 1150, f, 0, 90, -4)
    num(c, '146', 640, 1170, f, 3, 90, 3)
    num(c, '80', 990, 1150, f, 6, 90, -3)
    num(c, '352 GOLS', 640, 760, f, so, 180, -4)
    k = kick(f, so)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s7(f):
    c = estadio('dusk').copy()
    tr = wt(7, 'trono') - 3
    put_trofeu(c, 640, 1150, 480, f, 0)
    put_jog(c, 300, 2040, 760, f, 4, cores=ARG, faixa=ARG_F, arms='shrug', expr='neutral', skin=3, hair='#2b1d14')
    put_jog(c, 980, 2040, 760, f, 5, cores=BRA, faixa=BRA_F, arms='shrug', expr='neutral', skin=1, hair='#2b1d14')
    num(c, '?', 300, 1160, f, wt(7, 'quem') - 3, 160, -6)
    num(c, '?', 980, 1160, f, wt(7, 'quem') + 1, 160, 6)
    num(c, 'QUEM HERDA?', 640, 720, f, tr, 105, -3)
    z = lerp(1.0, 1.12, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'Messi') - 3, 160, .8)
    s.thunk(s.W(0, 'Cristiano') - 3, 140, .8)
    s.thunk(s.W(0, 'Neymar') - 3, 120, 1.0)
    s.ting(s.W(1, 'Copa') - 3, .3)
    s.thunk(s.W(2, 'Portugal') - 3, 160, .7)
    s.thunk(s.W(3, 'quarenta') - 4, 120, 1.0)
    s.ting(s.W(4, 'Copa') - 3, .35)
    s.thunk(s.W(5, 'oitenta') - 4, 140, 1.0)
    s.thunk(s.W(6, 'dois') - 3, 180, .9)
    s.ting(s.W(7, 'trono') - 3, .3)
