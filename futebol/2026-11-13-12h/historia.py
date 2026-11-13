"""anima.futebol — 13/11/2026 12h — Premier League: Manchester United anuncia Pochettino um dia após demitir Carrick.
Fontes (conferidas em 13/11/2026): Gazeta Esportiva 13/11 (anúncio na sexta 13/11; Carrick demitido na quinta; assume em
18/11 depois dos compromissos com a seleção dos EUA nesta Data Fifa; acordo com a federação americana; 18º com 8 pontos e
1 vitória após 10 rodadas, zona de rebaixamento; Tottenham final da Champions 2019; EUA nas oitavas da Copa); Metrópoles 13/11
(anúncio 13/11; Carrick demitido quinta 12/11; 18º com 8 pontos, zona de rebaixamento; EUA nas oitavas da Copa 2026;
Tottenham 2014-2019 com final da Champions); TV Sim Brasil 13/11 (um dia após demitir Carrick; 18º, 8 pontos; assume 18/11).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD)
SELO = 'PREMIER LEAGUE  ·  TÉCNICO NOVO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Manchester United tem técnico novo: Mauricio Pochettino foi anunciado nesta sexta-feira.",
    "A troca foi relâmpago: Michael Carrick tinha sido demitido um dia antes, na quinta.",
    "O motivo é a crise: depois de dez rodadas, o United é só o décimo oitavo colocado da Premier League.",
    "São apenas oito pontos e uma vitória, e o gigante inglês está na zona de rebaixamento.",
    "Pochettino conhece bem a Inglaterra: levou o Tottenham à final da Champions em dois mil e dezenove.",
    "E hoje ele ainda comanda os Estados Unidos, que chegaram às oitavas da Copa do Mundo.",
    "O argentino só assume o United no dia dezoito de novembro, depois desta Data Fifa.",
]
CAPTXT = [
    "O Manchester United tem técnico novo: Mauricio|Pochettino foi anunciado nesta sexta-feira.",
    "A troca foi relâmpago: Michael Carrick tinha|sido demitido um dia antes, na quinta.",
    "O motivo é a crise: depois de 10 rodadas, o United|é só o 18º colocado da Premier League.",
    "São apenas 8 pontos e 1 vitória, e o gigante|inglês está na zona de rebaixamento.",
    "Pochettino conhece bem a Inglaterra: levou o|Tottenham à final da Champions em 2019.",
    "E hoje ele ainda comanda os Estados Unidos,|que chegaram às oitavas da Copa do Mundo.",
    "O argentino só assume o United no dia 18|de novembro, depois desta Data Fifa.",
]
FALA_TIKTOK = "Pochettino tira o United da zona? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = [1]
CHECK = [(0, 'Manchester', 4), (0, 'Pochettino', 4), (1, 'Carrick', 4), (1, 'demitido', 4), (2, 'dez', 4),
         (2, 'oitavo', 4), (3, 'oito', 4), (3, 'rebaixamento', 4), (4, 'Tottenham', 4), (4, 'dezenove', 4),
         (5, 'Estados', 4), (5, 'oitavas', 4), (6, 'dezoito', 4), (6, 'Fifa', 4)]

MU, MU_F = time_('MANCHESTER UNITED')
USA, USA_F = time_('ESTADOS UNIDOS')
TOT, TOT_F = time_('TOTTENHAM')
TEC = ('#23283a', '#23283a', '#23283a')
TEC2 = ('#2c3e66', '#2c3e66', '#2c3e66')


def put_cal(c, dia, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, 'NOV'), x, y, s * back(ramp(f, f0, f0 + 8)))


def poch(c, x, y, h, f, **kw):
    kw.setdefault('arms', 'cintura'); kw.setdefault('expr', 'proud')
    put_jog(c, x, y, h, f, 9, cores=TEC, faixa=None, skin=0, hair='#cfcfcf', **kw)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    mu = wt(0, 'Manchester') - 3; nv = wt(0, 'novo') - 3; po = wt(0, 'Pochettino') - 3; an = wt(0, 'anunciado') - 3
    put_placa(c, 'MANCHESTER UNITED', MU, 640, 1120, f, mu, 62, -3)
    for x, sd, sk in ((180, 11, 1), (1090, 12, 2)):
        yy = lerp(2500, 1960, easeOut(ramp(f, mu - 4, mu + 6)))
        put_jog(c, x, yy, 620, f, sd, cores=MU, faixa=MU_F, arms='up' if f >= an else 'hang', expr='grin', skin=sk,
                hair='#111111', flip=x > 640)
    num(c, 'TÉCNICO NOVO', 640, 760, f, nv, 120, -4)
    y = lerp(2700, 2030, easeOut(ramp(f, po - 8, po + 6)))
    poch(c, 640, y, 880, f, arms='joinha' if f >= an else 'cintura')
    put_placa(c, 'POCHETTINO', TEC, 640, 930, f, po, 56, 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, an, .7)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = CEN('cidade', 'dusk').copy()
    ca = wt(1, 'Carrick') - 3; de = wt(1, 'demitido') - 3; di = wt(1, 'dia') - 3; qu = wt(1, 'quinta') - 3
    if f < de: num(c, 'RELÂMPAGO!', 640, 740, f, 2, 120, -4)
    # Carrick sai andando para a esquerda depois de "demitido"
    xx = 520 if f < de + 4 else lerp(520, 380, ramp(f, de + 4, de + 40))
    put_jog(c, xx, 2020, 860, f, 5, cores=TEC2, faixa=None, arms='hang', expr='pained' if f >= de else 'neutral',
            skin=0, hair='#6b4a2a', walk=(f * .06) % 1 if de + 4 <= f < de + 40 else 0, flip=True)
    put_placa(c, 'CARRICK', TEC2, xx, 1230, f, ca, 50, -3)
    num(c, 'DEMITIDO', 640, 760, f, de, 130, 4)
    put_cal(c, '12', 1010, 1330, .45, f, qu)
    num(c, '1 DIA ANTES', 640, 1110, f, di, 80, -3)
    return c, (lerp(600, 680, smooth(f / 120)), 1420, 1.06 * (1 + .0008 * f), 0), 'dusk'


def s2(f):
    c = estadio('day').copy()
    cr = wt(2, 'crise') - 3; dz = wt(2, 'dez') - 3; oi = wt(2, 'oitavo') - 3
    num(c, 'CRISE', 640, 740, f, cr, 150, -4)
    num(c, '10 RODADAS', 640, 900, f, dz, 96, 3)
    tabela(c, [('18º', 'MAN. UNITED', MU, '8 PTS', True)], 640, 1120, f, oi)
    put_jog(c, 330, 2030, 820, f, 3, cores=MU, faixa=MU_F, arms='cheek' if f >= oi else 'hang', expr='shock' if f >= oi else 'nervous',
            skin=1, hair='#111111')
    put_jog(c, 950, 2010, 760, f, 4, cores=MU, faixa=MU_F, arms='shrug', expr='pained', skin=3, hair='#111111', flip=True)
    z = lerp(1.0, 1.08, smooth(f / 100))
    k = kick(f, oi, .7)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 10, z, k), 'golden'


def s3(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c, x=760)
    op = wt(3, 'oito') - 3; vi = wt(3, 'vitoria') - 3; re = wt(3, 'rebaixamento') - 3
    put_goleiro(c, f, ('#1f7a4a', '#1f7a4a', '#ffffff'), None, gx=780, arms='up', expr='grin', skin=2, hair='#111111')
    sh = vi + 4
    put_jog(c, 520, 2030, 860, f, 3, cores=MU, faixa=MU_F, arms='run' if f < sh + 10 else 'cheek',
            expr='grin' if f < sh + 10 else 'shock', skin=1, hair='#111111', kick=pulse(f, sh - 4, 5))
    rb = raio_bola(860)
    if f < sh: bx, by, r = 640, 2030 - rb, rb
    else:  # chute pra fora, por cima do travessão
        t = ramp(f, sh, sh + 10)
        bx, by, r = lerp(640, gx + 330, t), lerp(2030 - rb, gy - 260, t) - 160 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, '8 PONTOS', 640, 740, f, op, 110, -4)
    num(c, '1 VITÓRIA', 640, 880, f, vi, 100, 4)
    num(c, 'ZONA DE REBAIXAMENTO', 640, 1020, f, re, 72, -2)
    k = kick(f, re, .9)
    return c, (640 + 30 * math.sin(f * .03), 1420 + k * 10, lerp(1.0, 1.06, smooth(f / 110)), k * 1.5), 'golden'


def s4(f):
    c = estadio('dusk').copy()
    po = wt(4, 'Pochettino') - 3; to = wt(4, 'Tottenham') - 3; fi = wt(4, 'final') - 3; an = wt(4, 'dezenove') - 3
    num(c, 'INGLATERRA', 640, 740, f, wt(4, 'Inglaterra') - 3, 110, -4)
    poch(c, 380, 2030, 860, f, arms='point' if f >= fi else 'cintura')
    put_placa(c, 'POCHETTINO', TEC, 380, 1100, f, po, 44, -3)
    if f >= to - 6:
        xx = lerp(1550, 960, easeOut(ramp(f, to - 6, to + 6)))
        put_jog(c, xx, 1990, 760, f, 6, cores=TOT, faixa=TOT_F, arms='up' if f >= fi else 'run', expr='grin', skin=0,
                hair='#6b4a2a', flip=True)
        put_placa(c, 'TOTTENHAM', TOT, xx, 1170, f, to, 50, 3)
    num(c, 'FINAL DA CHAMPIONS', 640, 880, f, fi, 76, 3)
    num(c, '2019', 640, 1010, f, an, 110, -4)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0012 * f)
    return c, (640 + 25 * math.sin(f * .05), lerp(1380, 1440, smooth(f / 120)), z, .8 * math.sin(f * .04)), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    es = wt(5, 'Estados') - 3; oi = wt(5, 'oitavas') - 3; co = wt(5, 'Copa') - 3
    poch(c, 640, 2030, 880, f, arms='joinha' if f >= oi else 'cintura', expr='grin')
    for x, sd, sk in ((200, 13, 0), (1080, 14, 3)):
        yy = lerp(2500, 1960, easeOut(ramp(f, es - 4, es + 6)))
        put_jog(c, x, yy, 640, f, sd, cores=USA, faixa=USA_F, arms='up' if f >= oi else 'hang', expr='grin', skin=sk,
                hair='#2b1d14', flip=x > 640)
    put_placa(c, 'ESTADOS UNIDOS', USA, 640, 1080, f, es, 58, -3)
    num(c, 'OITAVAS', 640, 760, f, oi, 140, -4)
    num(c, 'DA COPA', 640, 910, f, co, 96, 3)
    k = kick(f, oi, .6)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 8, lerp(1.04, 1.1, smooth(f / 100)), k), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    un = wt(6, 'United') - 3; dz = wt(6, 'dezoito') - 3; ff = wt(6, 'Fifa') - 3
    bx = lerp(-300, 360, easeOut(ramp(f, 0, 14)))
    poch(c, bx, 2010, 860, f, arms='point' if f >= dz else 'cintura', look=1)
    if f >= un - 6:
        ax = lerp(1550, 930, easeOut(ramp(f, un - 6, un + 6)))
        put_jog(c, ax, 2010, 820, f, 6, cores=MU, faixa=MU_F, arms='joinha', expr='grin', skin=2, hair='#111111', look=-1, flip=True)
        put_placa(c, 'MANCHESTER UNITED', MU, 930, 1180, f, un, 40, 4)
    put_placa(c, 'POCHETTINO', TEC, 360, 1180, f, 4, 40, -4)
    put_cal(c, '18', 640, 820, .5, f, dz)
    num(c, 'DEPOIS DA DATA FIFA', 640, 1050, f, ff, 72, -3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, dz, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'Pochettino') - 3, 140, .8)
    s.thunk(s.W(1, 'demitido') - 3, 180, .9)
    s.ting(s.W(2, 'oitavo') - 3, .3)
    s.thunk(s.W(3, 'rebaixamento') - 3, 140, .8)
    s.ting(s.W(4, 'final') - 3, .25)
    s.ting(s.W(5, 'oitavas') - 3, .3)
    s.ting(s.W(6, 'dezoito') - 3, .3)
