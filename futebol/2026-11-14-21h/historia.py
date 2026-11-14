"""anima.futebol — 14/11/2026 21h — Série B: última rodada define Juventude na Série A e os playoffs.
Fontes (conferidas em 14/11/2026): Lance! (resultados da 38ª rodada: Juventude 2x0 Botafogo-SP, Criciúma 0x1 Novorizontino,
Fortaleza 1x0 Vila Nova, Atlético-GO 1x0 Cuiabá; Novorizontino campeão, Juventude acesso direto; playoffs Vila Nova, Fortaleza,
Criciúma e Atlético-GO; rebaixados Avaí, Londrina, América-MG e Ponte Preta); A Rede (mesmos resultados; Juventude 2x0 no
Alfredo Jaconi, Caxias do Sul; 3º x 6º e 4º x 5º em ida e volta, vencedores sobem); O Povo (Fortaleza 1x0, Maílton no fim do
1º tempo, 4º com 65 pts, decide em casa); O Liberal (Maílton aos 44' de fora da área, 10º gol na Série B; Vila Nova 66, Fortaleza 65,
Criciúma 62, Atlético-GO 61; Fortaleza x Criciúma e Vila Nova x Atlético-GO).
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SÉRIE B  ·  38ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Juventude garantiu o acesso e vai jogar a Série A no ano que vem!",
    "Neste sábado, na última rodada, o time gaúcho bateu o Botafogo de Ribeirão Preto por dois a zero, em Caxias.",
    "O campeão foi o Novorizontino, que fechou a campanha vencendo o Criciúma fora de casa, por um a zero.",
    "Em Fortaleza, Maílton marcou de fora da área no fim do primeiro tempo, e o Leão venceu o Vila Nova.",
    "Agora, mais duas vagas vão ser decididas nos playoffs, em ida e volta.",
    "O Fortaleza enfrenta o Criciúma, e o Vila Nova encara o Atlético Goianiense, num clássico goiano.",
    "Na outra ponta, Avaí, Londrina, América Mineiro e Ponte Preta caíram para a Série C.",
    "E quem vencer os playoffs completa os quatro times que sobem para a Série A.",
]
CAPTXT = [
    "O Juventude garantiu o acesso e vai jogar|a Série A no ano que vem!",
    "Neste sábado, na última rodada, o time gaúcho|bateu o Botafogo-SP por 2 a 0, em Caxias.",
    "O campeão foi o Novorizontino, que fechou a campanha|vencendo o Criciúma fora de casa, por 1 a 0.",
    "Em Fortaleza, Maílton marcou de fora da área no fim|do 1º tempo, e o Leão venceu o Vila Nova.",
    "Agora, mais 2 vagas vão ser decididas|nos playoffs, em ida e volta.",
    "O Fortaleza enfrenta o Criciúma, e o Vila Nova encara|o Atlético Goianiense, num clássico goiano.",
    "Na outra ponta, Avaí, Londrina, América Mineiro|e Ponte Preta caíram para a Série C.",
    "E quem vencer os playoffs completa os 4 times|que sobem para a Série A.",
]
FALA_TIKTOK = "Quem sobe, Fortaleza ou Criciúma? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM SOBE?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Juventude', 4), (0, 'Serie', 4), (1, 'dois', 4), (2, 'Novorizontino', 4), (3, 'Mailton', 4),
         (4, 'playoffs', 4), (5, 'Criciuma', 4), (6, 'Avai', 4), (7, 'quatro', 4)]

JUV, JUV_F = time_('JUVENTUDE')
BFS, BFS_F = time_('BOTAFOGO-SP')
NOV, NOV_F = time_('NOVORIZONTINO')
CRI, CRI_F = time_('CRICIÚMA')
FOR, FOR_F = time_('FORTALEZA')
VIL, VIL_F = time_('VILA NOVA')
ACG, ACG_F = time_('ATLÉTICO-GO')
CINZA, _ = time_('GENÉRICO')
GK = ('#2a2f45', '#2a2f45', '#2a2f45')


def jog(c, x, y, h, f, seed, t, **kw):
    cores, fx = time_(t)
    kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=cores, faixa=fx, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f) if t < 1 else None
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def gol_txt(c, f, f0, x=640, y=880, s='GOL!', cor=(255, 216, 74)):
    explosao(c, x, y, f, f0, 240, cor)
    num(c, s, x, y, f, f0 + 2, 140, -4)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    ju = wt(0, 'Juventude') - 3; se = wt(0, 'Serie') - 3
    x = lerp(-250, 640, easeOut(ramp(f, 0, 20)))
    if f < 20: linhas_vel(c, x, 2030, 900, f)
    jog(c, x, 2030, 900, f, 1, 'JUVENTUDE', arms='up' if f >= se else 'run', run=(f * .09) % 1 if f < 20 else None,
        expr='grin', skin=2, num_='10')
    put_placa(c, 'JUVENTUDE', JUV, 640, 1060, f, ju, 66, -3)
    explosao(c, 640, 780, f, se, 230)
    num(c, 'SÉRIE A!', 640, 780, f, se + 2, 150, -4)
    confete(c, 640, 900, f, se, 90, 900)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, se, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('golden').copy()
    ca = wt(1, 'Caxias') - 3; d0 = wt(1, 'dois'); kf = max(30, d0 - 12)
    gx, gy = put_gol2(c, x=780, estufa=pulse(f, kf + 9, 8))
    put_goleiro(c, f, GK, None, gx=800 + 50 * clamp((f - kf) / 8), arms='up', expr='shock' if f >= kf + 6 else 'nervous', skin=1)
    x = lerp(60, 360, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
    jog(c, x, 2030, 860, f, 4, 'JUVENTUDE', arms='run' if f < kf + 6 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
        kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', skin=3, num_='9')
    jog(c, 1040, 1990, 760, f, 5, 'BOTAFOGO-SP', arms='cheek' if f >= kf + 8 else 'run', expr='pained' if f >= kf + 8 else 'stern',
        skin=1, flip=True, num_='4')
    put_placa(c, 'BOTAFOGO-SP', BFS, 1040, 1160, f, wt(1, 'Botafogo') - 3, 46, 3)
    rb = raio_bola(860)
    bola_voo(c, f, kf, x + 860 * .13, 2030 - rb, gx + 70, gy, rb, raio_bola(300), 150)
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 820)
    num(c, 'CAXIAS DO SUL', 640, 1010, f, ca, 84, 3)
    k = kick(f, kf + 9, .8)
    return c, (lerp(600, 680, smooth(f / 140)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'golden'


def s2(f):
    c = estadio2('dusk').copy()
    ca = wt(2, 'campeao') - 3; no = wt(2, 'Novorizontino') - 3; cr = wt(2, 'Criciuma') - 3
    put_trofeu(c, 820, 1000, 420, f, ca)
    jog(c, 380, 2020, 860, f, 2, 'NOVORIZONTINO', arms='up' if f >= no else 'cintura', expr='grin', skin=2, num_='7')
    put_placa(c, 'NOVORIZONTINO', NOV, 420, 1140, f, no, 44, -3)
    if f >= cr - 8:
        xx = lerp(1450, 990, easeOut(ramp(f, cr - 8, cr + 6)))
        jog(c, xx, 2020, 800, f, 3, 'CRICIÚMA', arms='cheek' if f >= cr + 6 else 'run', run=(f * .09) % 1 if f < cr + 6 else None,
            expr='pained', skin=1, flip=True)
        put_placa(c, 'CRICIÚMA', CRI, 990, 1240, f, cr + 4, 50, 3)
    num(c, 'CAMPEÃO!', 640, 700, f, ca, 140, -4)
    num(c, '1 x 0 FORA', 640, 1480, f, wt(2, 'zero') - 3, 100, 3)
    confete(c, 640, 800, f, no, 70, 800)
    z = lerp(1.18, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ca, .7)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 10, z, k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    ma = wt(3, 'Mailton') - 3; fo = wt(3, 'fora'); kf = max(24, fo - 4)
    gx, gy = put_gol2(c, x=860, s=.6, estufa=pulse(f, kf + 11, 8))
    put_goleiro(c, f, GK, None, gx=880 - 40 * clamp((f - kf) / 8), arms='up', expr='shock' if f >= kf + 6 else 'nervous', skin=0, hair='#111111')
    x = lerp(120, 330, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
    foco(c, x, 1640, 380, .85 * pulse(f, ma, 30))
    jog(c, x, 2030, 860, f, 6, 'FORTALEZA', arms='run' if f < kf + 8 else 'aviao', run=(f * .09) % 1 if f < kf - 4 else None,
        kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', skin=4, num_='2')
    put_placa(c, 'MAÍLTON', FOR, 330, 1080, f, ma, 54, -3)
    rb = raio_bola(860)
    bola_voo(c, f, kf, x + 860 * .13, 2030 - rb, gx + 50, gy - 40, rb, raio_bola(260), 220, 12)
    if f >= kf + 12: gol_txt(c, f, kf + 12, 640, 820, 'GOLAÇO!')
    num(c, "44' DO 1º TEMPO", 640, 1000, f, wt(3, 'primeiro') - 3, 76, 3)
    k = kick(f, kf + 12, .9)
    return c, (lerp(620, 690, smooth(f / 120)), 1430 + k * 10, 1.04 * (1 + .0008 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    pl = wt(4, 'playoffs') - 3
    num(c, 'PLAYOFFS', 640, 700, f, pl, 130, -4)
    tabela(c, [('3º', 'VILA NOVA', VIL, '66', False), ('4º', 'FORTALEZA', FOR, '65', True),
               ('5º', 'CRICIÚMA', CRI, '62', True), ('6º', 'ATLÉTICO-GO', ACG, '61', False)], 640, 890, f, wt(4, 'vagas') - 3)
    num(c, '+2 VAGAS', 640, 1640, f, wt(4, 'duas') - 3, 90, 3)
    z = lerp(1.14, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, pl, .6)
    return c, (640 + 25 * math.sin(f * .06), 1260 + 30 * smooth(f / 130) + k * 8, z, k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    fo = wt(5, 'Fortaleza') - 3; cr = wt(5, 'Criciuma') - 3; vi = wt(5, 'Vila Nova encara o') - 3; at = wt(5, 'Atletico') - 3
    cam = clamp((f - vi + 10) / 14)
    # duelo 1 (esquerda do palco) e duelo 2 (direita): a câmera passa de um para o outro
    jog(c, 200, 1800, 540, f, 1, 'FORTALEZA', arms='cintura', expr='stern', skin=3, look=1) if f >= fo - 4 else None
    put_placa(c, 'FORTALEZA', FOR, 265, 1180, f, fo, 44, -3)
    jog(c, 500, 1800, 540, f, 2, 'CRICIÚMA', arms='cintura', expr='stern', skin=1, look=-1, flip=True) if f >= cr - 4 else None
    put_placa(c, 'CRICIÚMA', CRI, 500, 1240, f, cr, 46, 3)
    num(c, 'X', 350, 1500, f, cr, 120)
    jog(c, 760, 1800, 540, f, 3, 'VILA NOVA', arms='cintura', expr='stern', skin=2, look=1) if f >= vi - 4 else None
    put_placa(c, 'VILA NOVA', VIL, 770, 1180, f, vi, 46, -3)
    jog(c, 1060, 1800, 540, f, 4, 'ATLÉTICO-GO', arms='cintura', expr='stern', skin=4, look=-1, flip=True) if f >= at - 4 else None
    put_placa(c, 'ATLÉTICO-GO', ACG, 990, 1240, f, at, 40, 3)
    num(c, 'X', 910, 1500, f, at, 120)
    num(c, 'CLÁSSICO GOIANO', 640, 1050, f, wt(5, 'classico') - 3, 70, -3)
    num(c, 'IDA E VOLTA', 640, 900, f, fo + 6, 80, 3)
    x = lerp(600, 680, smooth(cam)) + 25 * math.sin(f * .05)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0005 * f)
    return c, (x, 1420, z, 0), 'dusk'


def s6(f):
    c = estadio2('golden').copy()
    sc = wt(6, 'cairam') - 3
    nomes = [('AVAÍ', 'Avai', 330, 1080), ('LONDRINA', 'Londrina', 930, 1080), ('AMÉRICA-MG', 'America', 330, 1300),
             ('PONTE PRETA', 'Ponte', 930, 1300)]
    for i, (n, w, x, y) in enumerate(nomes):
        f0 = wt(6, w) - 3
        cores, _ = time_(n)
        dy = 0 if f < sc else 600 * (ramp(f, sc + i * 2, sc + i * 2 + 14) ** 2)
        if dy < 900: put_placa(c, n, cores, x, y + dy, f, f0, 54, (-4, 4, 3, -3)[i])
    jog(c, 640, 2040, 760, f, 7, 'GENÉRICO', arms='cheek' if f >= sc else 'hang', expr='pained', skin=2)
    num(c, 'SÉRIE C', 640, 760, f, sc, 150, -4)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, sc, .8)
    return c, (640, 1420 + k * 10, z, lerp(0, -2, smooth(ramp(f, sc, sc + 20)))), 'golden'


def s7(f):
    c = estadio2('dusk').copy()
    qu = wt(7, 'quatro') - 3
    put_trofeu(c, 640, 980, 420, f, 0)
    num(c, '4 VAGAS NA SÉRIE A', 640, 700, f, qu, 80, -3)
    xs = (230, 500, 770, 1040)
    for i, x in enumerate(xs):
        if i == 0: jog(c, x, 2010, 640, f, 1, 'NOVORIZONTINO', arms='up', expr='grin', skin=2)
        elif i == 1: jog(c, x, 2010, 640, f, 2, 'JUVENTUDE', arms='up', expr='grin', skin=3)
        else:
            put_atleta(c, x, 2010, 640, f, 3 + i, cores=CINZA, faixa=None, arms='shrug', expr='neutral', skin=i, hair='#3a3d46', hs='curto')
            num(c, '?', x, 1250, f, qu + 4 * i, 140, 6)
    put_placa(c, 'NOVORIZONTINO', NOV, 250, 1250, f, 2, 32, -3)
    put_placa(c, 'JUVENTUDE', JUV, 500, 1320, f, 4, 34, 3)
    z = lerp(.98, 1.02, easeOut(ramp(f, 0, 60))) * (1 + .0003 * f)
    return c, (640, 1380, z, 0), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    if si == 1: im = placar_tv(im, 'JUV', 'BOT', 2, 0, JUV, BFS, 'FIM', lf + 99)
    if si == 2: im = placar_tv(im, 'CRI', 'NOV', 0, 1, CRI, NOV, 'FIM', lf + 99)
    if si == 3: im = placar_tv(im, 'FOR', 'VIL', 1 if lf >= 0 else 0, 0, FOR, VIL, 'FIM', lf + 99)
    D = {0: ('JUVENTUDE NA SÉRIE A', 'ACESSO DIRETO EM 2º', 4),
         1: ('JUVENTUDE 2 x 0', 'BOTAFOGO-SP', wt(1, 'Caxias') - 3),
         2: ('NOVORIZONTINO CAMPEÃO', 'DA SÉRIE B 2026', wt(2, 'fechou') - 3),
         3: ('FORTALEZA 1 x 0 VILA NOVA', 'GOL DE MAÍLTON', wt(3, 'Leao') - 3),
         4: ('PLAYOFFS DE ACESSO', '2 VAGAS NA SÉRIE A', wt(4, 'ida') - 3),
         5: ('OS CONFRONTOS', 'IDA E VOLTA', wt(5, 'enfrenta') - 3),
         6: ('REBAIXADOS', 'PARA A SÉRIE C', wt(6, 'cairam') - 3),
         7: ('QUEM SOBE?', 'FALTAM 2 VAGAS', wt(7, 'playoffs') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (230, 60, 70) if si == 6 else (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'Serie') - 3, 150, .8)
    s.thunk(s.W(1, 'dois') - 3, 140, .7)
    s.ting(s.W(2, 'campeao') - 3, .35)
    s.thunk(s.W(3, 'fora') + 8, 150, .8)
    s.thunk(s.W(4, 'playoffs') - 3, 160, .7)
    s.ting(s.W(5, 'classico') - 3, .3)
    s.thunk(s.W(6, 'cairam') - 3, 200, .8)
    s.ting(s.W(7, 'quatro') - 3, .3)
