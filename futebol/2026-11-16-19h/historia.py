"""anima.futebol — 16/11/2026 19h — Morre Dino Sani, campeão do mundo com a Seleção em 1958, aos 94 anos.
Fontes (conferidas em 16/11/2026): Gazeta Esportiva (morreu domingo 15/11 aos 94; São Paulo 324 jogos e 113 gols;
Milan campeão italiano 1962 e europeu 1963; técnico: Gaúcho com o Inter 1971, 72, 73 e 83, uruguaio com o Peñarol 1978 e 79;
homenagens de São Paulo, CBF, Corinthians e Internacional); VAVEL Brasil (titular nos 2 primeiros jogos da Copa de 1958:
3x0 Áustria e 0x0 Inglaterra; lesão muscular, Zito entrou; estava no grupo da final 5x2 Suécia; Milan Taça dos Campeões 1962/63;
campeão mundial brasileiro mais velho vivo desde a morte de Zagallo); TNH1 (CBF confirmou e lamentou; volante; 324 jogos e 113 gols
pelo São Paulo; mais velho campeão mundial brasileiro vivo); CNN Brasil (manchete 15/11 23h08).
Tom sério de homenagem, sem humor. Sem escudos/logos nem rosto real: boneco genérico com placa do nome."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SELEÇÃO BRASILEIRA  ·  HOMENAGEM'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Morreu Dino Sani, campeão do mundo com a Seleção em mil novecentos e cinquenta e oito, aos noventa e quatro anos.",
    "Ele morreu neste domingo, e era o campeão mundial brasileiro mais velho ainda vivo.",
    "Na Copa da Suécia, foi titular nos dois primeiros jogos: três a zero na Áustria e zero a zero com a Inglaterra.",
    "Uma lesão tirou Dino do resto do torneio, mas ele estava no grupo que venceu a final por cinco a dois.",
    "No São Paulo, virou ídolo: foram trezentos e vinte e quatro jogos e cento e treze gols.",
    "Depois, na Itália, foi campeão europeu com o Milan, em mil novecentos e sessenta e três.",
    "Como técnico, ganhou quatro Gauchões pelo Internacional e dois títulos uruguaios pelo Peñarol.",
    "Clubes e CBF homenagearam Dino Sani, um dos campeões da primeira estrela do Brasil.",
]
CAPTXT = [
    "Morreu Dino Sani, campeão do mundo|com a Seleção em 1958, aos 94 anos.",
    "Ele morreu neste domingo, e era o campeão|mundial brasileiro mais velho ainda vivo.",
    "Na Copa da Suécia, foi titular nos 2 primeiros|jogos: 3 a 0 na Áustria e 0 a 0 com a Inglaterra.",
    "Uma lesão tirou Dino do resto do torneio, mas ele|estava no grupo que venceu a final por 5 a 2.",
    "No São Paulo, virou ídolo:|foram 324 jogos e 113 gols.",
    "Depois, na Itália, foi campeão europeu|com o Milan, em 1963.",
    "Como técnico, ganhou 4 Gauchões pelo Internacional|e 2 títulos uruguaios pelo Peñarol.",
    "Clubes e CBF homenagearam Dino Sani,|um dos campeões da primeira estrela do Brasil.",
]
FALA_TIKTOK = "Deixa sua homenagem ao Dino Sani nos comentários, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "ETERNO DINO"
TWIST = 3
FLASH = []
CHECK = [(0, 'Dino', 4), (0, 'noventa', 6), (1, 'domingo', 4), (1, 'velho', 4), (2, 'tres', 4), (2, 'Inglaterra', 4),
         (3, 'lesao', 6), (3, 'cinco', 4), (4, 'trezentos', 6), (4, 'cento', 6), (5, 'Milan', 4), (5, 'sessenta', 4),
         (6, 'Internacional', 4), (6, 'Penarol', 4), (7, 'estrela', 4)]

BRA, BRA_F = time_('BRASIL')
AUT, AUT_F = time_('ÁUSTRIA')
ING, ING_F = time_('INGLATERRA')
SUE, SUE_F = time_('SUÉCIA')
SPA, SPA_F = time_('SÃO PAULO')
MIL, MIL_F = time_('MILAN')
INT, INT_F = time_('INTERNACIONAL')
PEN, PEN_F = time_('PEÑAROL')
TEC = ('#2b2f3a', '#3b4152', '#2b2f3a')


def dino(c, x, y, h, f, cores=BRA, faixa=BRA_F, sock=None, **kw):
    """Dino Sani: boneco genérico (sem tentar parecer com ele), volante."""
    kw.setdefault('expr', 'neutral'); kw.setdefault('skin', 1); kw.setdefault('hs', 'curto')
    put_atleta(c, x, y, h, f, 5, cores=cores, faixa=faixa, hair='#2a1a10', sock=sock, **kw)


def companheiro(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', seed % 5); kw.setdefault('hs', ('curto', 'raspado', 'topete')[seed % 3])
    put_atleta(c, x, y, h, f, seed, cores=BRA, faixa=BRA_F, hair='#1b1410', **kw)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 10)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    di = wt(0, 'Dino') - 3; mi = wt(0, 'mil') - 3; no = wt(0, 'noventa') - 3
    dino(c, 640, 2040, 900, f, arms='hang', expr='neutral')
    foco(c, 640, 1600, 430, .75 * ramp(f, 0, 14))
    put_placa(c, 'DINO SANI', BRA, 640, 1010, f, di, 70, -2)
    if f < no: num(c, 'CAMPEÃO EM 1958', 640, 760, f, mi, 92, -3)
    else: num(c, '94 ANOS', 640, 760, f, no, 150, -3)
    z = lerp(1.22, 1.04, easeOut(ramp(f, 0, 50))) * (1 + .0005 * f)
    return c, (640, 1430, z, 0), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    do = wt(1, 'domingo') - 3; ve = wt(1, 'velho') - 3
    dino(c, 880, 2030, 860, f, arms='hang', expr='neutral', look=-.5)
    if f >= do: paste_c(c, calendario('15', 'NOV'), 360, 1050, .72 * back(ramp(f, do, do + 9)))
    num(c, 'DOMINGO', 360, 1330, f, do + 4, 80, -3)
    num(c, 'O CAMPEÃO MAIS VELHO', 640, 740, f, ve, 62, -2)
    foco(c, 640, 1350, 620, .45)
    return c, (640, 1420, lerp(1.04, 1.12, smooth(f / 120)), 0), 'dusk'


def _k2():
    tr = wt(2, 'tres') - 9
    return tr, wt(2, 'Inglaterra') - 3


def s2(f):
    c = estadio2('day').copy()
    tr, ig = _k2(); ti = wt(2, 'titular') - 3
    eng = f >= ig - 6
    gx, gy = put_gol2(c, x=780, estufa=0 if eng else pulse(f, tr + 9, 10))
    if eng: put_goleiro(c, f, ING, ING_F, gx=800, arms='cintura', expr='stern', skin=0)
    else: put_goleiro(c, f, AUT, AUT_F, gx=800 - 50 * clamp((f - tr) / 7), arms='up', expr='shock' if f >= tr + 5 else 'nervous', skin=0)
    x = lerp(-200, 380, easeOut(ramp(f, 0, 22)))
    if f < 20: linhas_vel(c, x, 2030, 860, f)
    dino(c, x, 2030, 860, f, arms='run' if f < tr + 10 else ('punho' if not eng else 'cintura'),
         run=(f * .08) % 1 if f < 20 else None, kick=pulse(f, tr - 4, 5) if tr - 4 <= f < ig - 6 else 0,
         expr='stern' if f < tr else 'grin', num_='5')
    rb = raio_bola(860)
    if eng: put_bola(c, x + 120, 2030 - rb, rb, 0)
    else: bola_voo(c, f, tr, x + 120, 2030 - rb, gx + 60, gy - 10, rb, raio_bola(300), 150)
    if f < ti: num(c, 'SUÉCIA 1958', 640, 740, f, wt(2, 'Suecia') - 3, 110, -3)
    else: num(c, 'TITULAR', 640, 740, f, ti, 120, -3)
    if eng: put_placa(c, 'INGLATERRA', ING, 640, 980, f, ig, 60, 3)
    else: put_placa(c, 'ÁUSTRIA', AUT, 640, 980, f, wt(2, 'Austria') - 3, 64, 3)
    k = kick(f, tr + 9, .7)
    return c, (lerp(600, 670, smooth(f / 140)), 1430 + k * 10, 1.05 * (1 + .0005 * f), k), 'golden'


def s3(f):
    c = estadio2('dusk').copy()
    le = wt(3, 'lesao') - 3; ma = wt(3, 'mas') - 3; fi = wt(3, 'final') - 3; ci = wt(3, 'cinco') - 3
    if f < ma:
        dino(c, 640, 2040, 880, f, arms='cheek', expr='pained')
        num(c, 'LESÃO', 640, 760, f, le, 130, -3)
        foco(c, 640, 1580, 440, .6)
        return c, (640, 1440, lerp(1.04, 1.14, smooth(f / 60)), 0), 'dusk'
    put_trofeu(c, 640, 1150, 560, f, fi)
    for i, (x, sd) in enumerate(((260, 31), (1020, 33))):
        companheiro(c, x, 2000, 780, f, sd, arms='up' if f >= ci else 'hang', expr='grin' if f >= ci else 'neutral')
    dino(c, 640, 2040, 860, f, arms='up' if f >= ci else 'hang', expr='grin' if f >= ci else 'neutral', num_='5')
    num(c, 'FINAL: 5 x 2', 640, 740, f, ci, 110, -3)
    return c, (640, 1420, lerp(1.12, 1.02, smooth((f - ma) / 50)), 0), 'dusk'


def s4(f):
    c = estadio2('day').copy()
    sp = wt(4, 'Sao') - 3; tr = wt(4, 'trezentos') - 3; ce = wt(4, 'cento') - 3
    x = lerp(1450, 640, easeOut(ramp(f, 0, 20)))
    if f < 18: linhas_vel(c, x, 2040, 880, f, dir=1)
    dino(c, x, 2040, 880, f, cores=SPA, faixa=SPA_F, sock='#ffffff', arms='run' if f < 20 else ('joinha' if f >= ce else 'cintura'),
         run=(f * .08) % 1 if f < 20 else None, expr='grin', num_='5', flip=f < 20)
    put_placa(c, 'SÃO PAULO', SPA, 640, 1190, f, sp, 64, -3)
    num(c, '324 JOGOS', 640, 720, f, tr, 120, -3)
    num(c, '113 GOLS', 640, 940, f, ce, 120, 3)
    return c, (640 + 25 * math.sin(f * .04), 1430, lerp(1.1, 1.03, smooth(f / 60)) * (1 + .0005 * f), 0), 'golden'


def s5(f):
    c = estadio2('dusk').copy()
    it = wt(5, 'Italia') - 3; eu = wt(5, 'europeu') - 3; mi = wt(5, 'Milan') - 3; se = wt(5, 'sessenta') - 3
    put_trofeu(c, 930, 1250, 520, f, eu)
    dino(c, 400, 2040, 880, f, cores=MIL, faixa=MIL_F, sock='#111111', arms='up' if f >= eu else 'cintura',
         expr='grin' if f >= eu else 'neutral', num_='5')
    num(c, 'ITÁLIA', 640, 740, f, it, 120, -3)
    put_placa(c, 'MILAN', MIL, 400, 1080, f, mi, 66, -3)
    num(c, '1963', 930, 1580, f, se, 120, 4)
    return c, (lerp(600, 690, smooth(f / 120)), 1430, lerp(1.0, 1.1, smooth(f / 120)), 0), 'dusk'


def s6(f):
    c = estadio2('day').copy()
    te = wt(6, 'tecnico') - 3; inn = wt(6, 'Internacional') - 3; pe = wt(6, 'Penarol') - 3
    put_atleta(c, 640, 2050, 820, f, 5, cores=TEC, faixa=None, hair='#5a5048', hs='curto', skin=1,
               arms='point' if f >= inn else 'cintura', expr='proud', sock='#2b2f3a', flip=f >= pe)
    num(c, 'TÉCNICO', 640, 720, f, te, 120, -3)
    put_placa(c, 'INTERNACIONAL', INT, 370, 900, f, inn, 40, -2)
    num(c, '4 GAUCHÕES', 370, 1040, f, inn + 6, 64, -2)
    put_placa(c, 'PEÑAROL', PEN, 900, 900, f, pe, 54, 3)
    num(c, '2 URUGUAIOS', 900, 1040, f, pe + 6, 60, 2)
    return c, (640, 1430, lerp(1.08, 1.02, smooth(f / 100)) * (1 + .0004 * f), 0), 'golden'


def s7(f):
    c = estadio2('dusk').copy()
    di = wt(7, 'Dino') - 3; es = wt(7, 'estrela') - 3
    dino(c, 640, 2050, 880, f, arms='hang', expr='neutral')
    foco(c, 640, 1400, 520, .7 * ramp(f, 0, 20))
    put_placa(c, 'DINO SANI', BRA, 640, 730, f, di, 66, 0)
    if f >= es:
        explosao(c, 640, 960, f, es, 130, (255, 216, 74))
        num(c, '1958', 640, 960, f, es + 2, 70, 0)
    z = lerp(1.0, 1.12, smooth(f / 130))
    return c, (640, 1400, z, 0), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    if si == 2:
        tr, ig = _k2()
        if lf < ig - 6: im = placar_tv(im, 'BRA', 'AUT', int(lf >= tr + 9) * 3, 0, BRA, AUT, '1958', lf, pulse_a=tr + 9)
        else: im = placar_tv(im, 'BRA', 'ING', 0, 0, BRA, ING, '1958', lf - ig + 6)
    elif si == 3 and lf >= wt(3, 'cinco') - 3:
        im = placar_tv(im, 'BRA', 'SUE', 5, 2, BRA, SUE, 'FINAL', lf - wt(3, 'cinco') + 3)
    D = {0: ('MORRE DINO SANI', 'CAMPEÃO DO MUNDO EM 1958, AOS 94 ANOS', wt(0, 'noventa') + 4),
         1: ('O CAMPEÃO MAIS VELHO', 'MORREU NESTE DOMINGO, 15/11', wt(1, 'velho') + 6),
         2: ('COPA DE 1958, NA SUÉCIA', 'TITULAR NOS 2 PRIMEIROS JOGOS', wt(2, 'Inglaterra') + 6),
         3: ('CAMPEÃO DO MUNDO', 'BRASIL 5 x 2 SUÉCIA NA FINAL', wt(3, 'cinco') + 6),
         4: ('ÍDOLO DO SÃO PAULO', '324 JOGOS E 113 GOLS', wt(4, 'cento') + 6),
         5: ('CAMPEÃO EUROPEU', 'COM O MILAN, EM 1963', wt(5, 'sessenta') + 4),
         6: ('TÉCNICO VENCEDOR', '4 GAUCHÕES NO INTER, 2 URUGUAIOS NO PEÑAROL', wt(6, 'Penarol') + 6),
         7: ('ETERNO DINO SANI', 'UM DOS HERÓIS DA 1ª ESTRELA', wt(7, 'estrela') + 4)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub, (255, 216, 74))


def SFX(s):
    s.thunk(s.W(0, 'Dino') - 3, 160, .6)
    s.ting(s.W(0, 'noventa') - 3, .25)
    s.thunk(s.W(1, 'domingo') - 3, 180, .5)
    s.thunk(s.W(2, 'tres') - 9 + 9, 140, .7)
    s.thunk(s.W(2, 'Inglaterra') - 3, 180, .5)
    s.thunk(s.W(3, 'lesao') - 3, 220, .5)
    s.ting(s.W(3, 'cinco') - 3, .3)
    s.thunk(s.W(4, 'trezentos') - 3, 160, .6)
    s.thunk(s.W(4, 'cento') - 3, 160, .6)
    s.ting(s.W(5, 'europeu') - 3, .3)
    s.thunk(s.W(6, 'Internacional') - 3, 160, .5)
    s.thunk(s.W(6, 'Penarol') - 3, 160, .5)
    s.ting(s.W(7, 'estrela') - 3, .3)
