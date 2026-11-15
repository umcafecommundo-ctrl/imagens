"""anima.futebol — 15/11/2026 07h — Nations League: Portugal 1x4 Dinamarca em Braga, 1º jogo sem Cristiano Ronaldo.
Fontes (conferidas em 15/11/2026): DN (gols: Højbjerg pênalti 43', Højlund 50' e 57', Andersen de cabeça 75', Bernardo Silva 90+3';
classificação Portugal 12, Dinamarca 9, Noruega 6, Gales 3; última rodada 17/11 em Gales; Portugal já nas quartas; 1 ponto garante o 1º);
VAVEL Brasil (mesmos gols e minutos; camisas 7 e aplausos aos 7 minutos; Portugal 12 x Dinamarca 9; terça 17/11 em Cardiff);
CNN Portugal (1x4 em Braga, homenagem no minuto 7); Observador e Sol (1ª derrota de Jorge Jesus na seleção; 1º jogo pós-Ronaldo);
Notícias ao Minuto (vitória ou empate em Gales garante o 1º; Dinamarca leva o confronto direto); O Jogo (gol de honra de Bernardo Silva).
"""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'NATIONS LEAGUE  ·  5ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "A Dinamarca goleou Portugal por quatro a um, em Braga, no primeiro jogo dos portugueses sem Cristiano Ronaldo.",
    "Antes da bola rolar, teve homenagem: todo mundo com a camisa sete, e aplausos no minuto sete.",
    "Mas em campo deu Dinamarca: Hoibierg abriu o placar de pênalti, no fim do primeiro tempo.",
    "Na volta do intervalo, Hoilund marcou duas vezes em sete minutos.",
    "Andersen ainda fez o quarto, de cabeça, e Bernardo Silva só descontou nos acréscimos.",
    "Foi a primeira derrota de Jorge Jesus no comando de Portugal.",
    "Mesmo assim, Portugal segue líder, com doze pontos, três a mais que a Dinamarca, e já está nas quartas.",
    "Na terça, contra o País de Gales, um empate garante o primeiro lugar.",
]
CAPTXT = [
    "A Dinamarca goleou Portugal por 4 a 1, em Braga, no 1º jogo|dos portugueses sem Cristiano Ronaldo.",
    "Antes da bola rolar, teve homenagem: todo mundo|com a camisa 7, e aplausos no minuto 7.",
    "Mas em campo deu Dinamarca: Højbjerg abriu o placar|de pênalti, no fim do primeiro tempo.",
    "Na volta do intervalo, Højlund marcou|duas vezes em 7 minutos.",
    "Andersen ainda fez o quarto, de cabeça, e Bernardo Silva|só descontou nos acréscimos.",
    "Foi a 1ª derrota de Jorge Jesus|no comando de Portugal.",
    "Mesmo assim, Portugal segue líder, com 12 pontos, 3 a mais|que a Dinamarca, e já está nas quartas.",
    "Na terça, contra o País de Gales, um empate|garante o 1º lugar.",
]
FALA_TIKTOK = "Portugal sentiu falta do Cristiano: sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SENTIU FALTA?"
TWIST = 2
FLASH = [2]
CHECK = [(0, 'quatro', 6), (1, 'sete', 4), (2, 'penalti', 6), (3, 'duas', 6), (4, 'cabeca', 6), (5, 'derrota', 4),
         (6, 'doze', 4), (7, 'empate', 4)]

POR, POR_F = time_('PORTUGAL')
DIN, DIN_F = time_('DINAMARCA')
GAL, GAL_F = time_('PAÍS DE GALES')
NOR, NOR_F = time_('NORUEGA')
TEC = ('#2a2f45', '#2a2f45', '#2a2f45')
GKP = ('#f2c94c', '#111111', '#111111')
GKD = ('#2fa35a', '#111111', '#111111')


def pt(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=POR, faixa=POR_F, hair='#2a1a10', **kw)


def dk(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 0); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, seed, cores=DIN, faixa=DIN_F, hair='#c9a25a', sock='#c8102e', **kw)


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
    qu = wt(0, 'quatro') - 3; cr = wt(0, 'Cristiano') - 3
    pt(c, 300, 1700, 520, f, 11, arms='cheek', expr='pained')
    pt(c, 990, 1690, 500, f, 12, arms='cheek', expr='pained', skin=3, hs='cacheado', flip=True)
    x = lerp(1250, 620, easeOut(ramp(f, 0, 22)))
    if f < 24: linhas_vel(c, x, 2050, 900, f, dir=1)
    dk(c, x, 2050, 900, f, 6, arms='aviao', expr='grin', run=(f * .08) % 1 if f < 22 else -1, num_='9', flip=True)
    confete(c, 640, 900, f, qu, 90, 900)
    explosao(c, 640, 820, f, qu, 250)
    num(c, '1 x 4', 640, 820, f, qu + 2, 170, -3)
    num(c, 'SEM CR7', 640, 1010, f, cr, 90, 3)
    z = lerp(1.22, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, qu, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    s7 = wt(1, 'sete') - 3; ap = wt(1, 'aplausos') - 3
    xs = (250, 640, 1030)
    for i, x in enumerate(xs):
        xr = lerp(x, x, 1)
        pt(c, xr, 1960 + (40 if i == 1 else 0), 760 + (60 if i == 1 else 0), f, 30 + i, num_='7',
           arms='up' if f >= ap else 'hang', expr='proud' if f < ap else 'grin', skin=(1, 3, 2)[i],
           hs=('curto', 'raspado', 'topete')[i])
    if f >= s7: num(c, 'CAMISA 7', 640, 760, f, s7, 120, -3)
    if f >= ap:
        confete(c, 640, 760, f, ap, 60, 900)
        num(c, "MINUTO 7'", 640, 930, f, ap, 100, 3)
    z = lerp(1.0, 1.1, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .04), 1420, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    ho = wt(2, 'Hoibierg') - 3; pe = wt(2, 'penalti') - 3
    kf = pe + 2
    gx, gy = put_gol2(c, x=700, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKP, None, gx=720 - 70 * clamp((f - kf) / 7), arms='up', expr='shock' if f >= kf + 5 else 'nervous', skin=1)
    x = 330
    dk(c, x, 2030, 880, f, 8, arms='run' if f < kf + 10 else 'punho', kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0,
       expr='stern' if f < kf else 'grin', num_='23', hs='raspado')
    foco(c, x, 1640, 380, .85 * pulse(f, ho, 30))
    put_placa(c, 'HØJBJERG', DIN, 900, 1150, f, ho, 60, -3)
    chute_gol(c, f, kf, x, 880, gx, gy, alvo=(110, -10), arco=60)
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860, 'PÊNALTI!')
    k = kick(f, kf + 9)
    return c, (lerp(600, 660, smooth(f / 80)), 1430 + k * 10, lerp(1.04, 1.1, smooth(f / 80)), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    hl = wt(3, 'Hoilund'); du = wt(3, 'duas')
    k1 = max(12, hl - 4); k2 = max(k1 + 26, du - 2)
    est = max(pulse(f, k1 + 9, 6) * (f < k1 + 20), pulse(f, k2 + 9, 6))
    gx, gy = put_gol2(c, x=760, estufa=est)
    put_goleiro(c, f, GKP, None, gx=780 + (60 if f > k1 + 6 else 0) * (f < k1 + 20) + (-60 if f > k2 + 6 else 0),
                arms='up', expr='shock', skin=1)
    if f < k1 + 20:
        x = lerp(-200, 340, easeOut(ramp(f, 0, k1 - 3)))
        if f < k1 - 4: linhas_vel(c, x, 2030, 860, f)
        dk(c, x, 2030, 860, f, 4, arms='run' if f < k1 + 6 else 'punho', run=(f * .09) % 1 if f < k1 - 4 else None,
           kick=pulse(f, k1 - 4, 5) if f >= k1 - 4 else 0, expr='grin', num_='9', hs='topete')
        chute_gol(c, f, k1, x, 860, gx, gy)
        if f >= k1 + 9: gol_txt(c, f, k1 + 9, 640, 860)
    else:
        x = lerp(1450, 880, easeOut(ramp(f, k1 + 20, k2 - 3)))
        dk(c, x, 2030, 860, f, 4, arms='run' if f < k2 + 6 else 'aviao', run=(f * .09) % 1 if f < k2 - 4 else None,
           kick=pulse(f, k2 - 4, 5) if f >= k2 - 4 else 0, expr='grin', num_='9', hs='topete', flip=True)
        rb = raio_bola(860)
        bola_voo(c, f, k2, x - 110, 2030 - rb, gx + 40, gy - 10, rb, raio_bola(300), 140)
        if f >= k2 + 9: gol_txt(c, f, k2 + 9, 640, 860, '2 GOLS!')
    put_placa(c, 'HØJLUND', DIN, 940 if f < k1 + 20 else 330, 1150, f, max(0, hl - 6), 60, 3)
    k = kick(f, k1 + 9, .8) + kick(f, k2 + 9, .8)
    return c, (lerp(600, 680, smooth(f / 120)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    an = wt(4, 'Andersen') - 3; ca = wt(4, 'cabeca') - 3; be = wt(4, 'Bernardo') - 3
    if f < be - 4:
        kf = ca
        gx, gy = put_gol2(c, x=700, estufa=pulse(f, kf + 9, 10))
        put_goleiro(c, f, GKP, None, gx=720 + 60 * clamp((f - kf) / 7), arms='up', expr='shock', skin=1)
        x = 360
        hop = -90 * pulse(f, kf - 6, 10)
        dk(c, x, 2030 + hop, 880, f, 14, arms='up', expr='stern' if f < kf else 'grin', num_='6', hs='curto')
        hy = 2030 + hop - 880 * .9
        if f < kf:
            t = ramp(f, max(0, kf - 18), kf)
            put_bola(c, lerp(-60, x + 20, t), lerp(1500, hy, t) - 160 * math.sin(t * math.pi), raio_bola(880), f)
        else:
            bola_voo(c, f, kf, x + 20, hy, gx + 80, gy, raio_bola(880), raio_bola(300), 40, 9)
        put_placa(c, 'ANDERSEN', DIN, 920, 1100, f, an, 60, -3)
        if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 820, 'DE CABEÇA!')
        k = kick(f, kf + 9)
        return c, (lerp(600, 660, smooth(f / 60)), 1430 + k * 10, 1.05, k), 'dusk'
    x = 640
    pt(c, x, 2040, 880, f, 20, arms='joinha', expr='neutral', num_='10', hs='cacheado', skin=1)
    put_placa(c, 'BERNARDO SILVA', POR, 640, 1080, f, be - 4, 64, -2)
    num(c, '1 x 4', 640, 840, f, be, 150, 3)
    z = lerp(1.08, 1.0, smooth((f - be) / 40))
    return c, (640, 1430, z, 0), 'dusk'


def s5(f):
    c = estadio2('golden').copy()
    jj = wt(5, 'Jorge') - 3; de = wt(5, 'derrota') - 3
    put_atleta(c, 640, 2030, 900, f, 9, cores=TEC, faixa=None, arms='cheek' if f >= de else 'cintura', expr='pained' if f >= de else 'stern',
               skin=1, hair='#d8d8d8', hs='topete', sock='#1a1a1a')
    put_placa(c, 'JORGE JESUS', POR, 640, 1090, f, jj, 66, -2)
    explosao(c, 640, 760, f, de, 230, (230, 60, 70))
    num(c, '1ª DERROTA', 640, 760, f, de + 2, 120, -3)
    z = lerp(1.15, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0008 * f)
    return c, (640 + 20 * math.sin(f * .04), 1430, z, 0), 'golden'


def s6(f):
    c = estadio2('dusk').copy()
    li = wt(6, 'lider') - 3; qa = wt(6, 'quartas') - 3
    tabela(c, [('1º', 'PORTUGAL', POR, '12', True), ('2º', 'DINAMARCA', DIN, '9', False),
               ('3º', 'NORUEGA', NOR, '6', False), ('4º', 'PAÍS DE GALES', GAL, '3', False)], 640, 820, f, li)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    return c, (640, lerp(1300, 1360, smooth(f / 150)), z, 0), 'dusk'


def s7(f):
    c = estadio2('dusk').copy()
    te = wt(7, 'terca') - 3; ga = wt(7, 'Gales') - 3; em = wt(7, 'empate') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, 0, 16)))
    pt(c, bx, 2010, 860, f, 3, arms='cintura', expr='stern', look=1, run=(f * .09) % 1 if f < 16 else None, num_='8')
    paste_c(c, calendario('17', 'NOV'), 640, 820, .5 * back(ramp(f, te, te + 8))) if f >= te else None
    if f >= ga - 8:
        sx = lerp(1550, 940, easeOut(ramp(f, ga - 8, ga + 6)))
        put_atleta(c, sx, 2010, 860, f, 7, cores=GAL, faixa=GAL_F, arms='cintura', expr='proud', skin=0, hair='#3a2a1a',
                   look=-1, flip=True, run=(f * .09) % 1 if f < ga + 6 else None, num_='11')
    if f >= em: num(c, 'EMPATE BASTA', 640, 1130, f, em, 96, -2)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, te, .6) + kick(f, em, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    if si == 0: im = placar_tv(im, 'POR', 'DIN', 1, 4, POR, DIN, 'FIM', lf)
    elif si == 2:
        k = wt(2, 'penalti') + 8
        im = placar_tv(im, 'POR', 'DIN', 0, int(lf >= k), POR, DIN, '1º T', lf + 99, pulse_b=k)
    elif si == 3:
        hl = wt(3, 'Hoilund'); k1 = max(12, hl - 4) + 9; k2 = max(k1 + 26, wt(3, 'duas') - 2 + 9)
        im = placar_tv(im, 'POR', 'DIN', 0, 1 + (lf >= k1) + (lf >= k2), POR, DIN, '2º T', lf + 99, pulse_b=k1 if lf < k2 else k2)
    elif si == 4:
        k = wt(4, 'cabeca') + 6; kb = wt(4, 'Bernardo') - 3
        im = placar_tv(im, 'POR', 'DIN', int(lf >= kb), 3 + (lf >= k), POR, DIN, 'ACR.' if lf >= kb else '2º T', lf + 99,
                       pulse_b=k if lf < kb else -1, pulse_a=kb)
    elif si == 5: im = placar_tv(im, 'POR', 'DIN', 1, 4, POR, DIN, 'FIM', lf + 99)
    D = {0: ('PORTUGAL 1 x 4 DINAMARCA', '1º JOGO SEM CRISTIANO RONALDO', 4),
         1: ('HOMENAGEM AO CAPITÃO', 'CAMISA 7 E APLAUSOS NO MINUTO 7', wt(1, 'homenagem') - 3),
         2: ('HØJBJERG DE PÊNALTI', 'FIM DO PRIMEIRO TEMPO', wt(2, 'penalti') + 12),
         3: ('HØJLUND 2 VEZES', 'EM 7 MINUTOS', wt(3, 'duas') + 12),
         4: ('BERNARDO SILVA DESCONTA', 'NOS ACRÉSCIMOS', wt(4, 'Bernardo') + 4),
         5: ('JORGE JESUS NA SELEÇÃO', '1ª DERROTA COMO TÉCNICO', wt(5, 'derrota')),
         6: ('PORTUGAL SEGUE LÍDER', 'JÁ CLASSIFICADO ÀS QUARTAS', wt(6, 'lider') - 3),
         7: ('PAÍS DE GALES x PORTUGAL', 'TERÇA, 17/11 · EMPATE GARANTE O 1º', wt(7, 'terca') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (230, 60, 70) if si in (0, 5) else (255, 216, 74), y=1250 if si == 6 else 1330)


def SFX(s):
    s.thunk(s.W(0, 'quatro') - 3, 150, .8)
    s.ting(s.W(1, 'aplausos') - 3, .35)
    s.thunk(s.W(2, 'penalti') + 11, 160, .8)
    s.thunk(max(12, s.W(3, 'Hoilund') - 4) + 9, 140, .7)
    s.thunk(max(max(12, s.W(3, 'Hoilund') - 4) + 26, s.W(3, 'duas') - 2) + 9, 140, .7)
    s.thunk(s.W(4, 'cabeca') + 6, 150, .8)
    s.thunk(s.W(5, 'derrota') - 3, 140, .7)
    s.ting(s.W(6, 'lider') - 3, .3)
    s.ting(s.W(7, 'terca') - 3, .3)
