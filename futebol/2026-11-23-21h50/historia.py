"""anima.futebol — 23/11/2026 21h50 — QUEM CAI? · EP. 5 — Internacional 2x5 Vitória no Beira-Rio (36ª rodada).
Fontes (conferidas em 23/11/2026, ver fatos.txt): Gazeta Esportiva (21:32), A Tarde (21:31), Bahia Notícias (21h30),
Lance!, brasileirao.com.br, VAVEL, ESPN. Vitória 5x2, gol com segundos de jogo, Vitória 44; Inter segue com 38 na zona,
Corinthians 40; faltam 2 rodadas. Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  36ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Inter vai cair? Olha a conta.",
    "No Beira-Rio, o Vitória marcou com segundos de jogo.",
    "E o placar final... cinco a dois para o Vitória.",
    "O Vitória chega a quarenta e quatro pontos.",
    "O Inter fica com trinta e oito, na zona... e o Corinthians tem quarenta.",
    "Faltam duas rodadas. O Inter ainda escapa?",
]
CAPTXT = [
    "O Inter vai cair?|Olha a conta.",
    "No Beira-Rio, o Vitória marcou|com segundos de jogo.",
    "E o placar final...|5 a 2 para o Vitória.",
    "O Vitória chega|a 44 pontos.",
    "O Inter fica com 38, na zona...|e o Corinthians tem 40.",
    "Faltam 2 rodadas.|O Inter ainda escapa?",
]
FALA_TIKTOK = "O Inter escapa? Comenta sim ou não."
CTA_TEXTO = "INTER ESCAPA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [2]
CHECK = [(0, 'Inter', 4), (0, 'conta', 4), (1, 'Beira-Rio', 4), (1, 'segundos', 4), (2, 'final', 4), (2, 'cinco', 4),
         (3, 'quarenta', 4), (3, 'quatro', 4), (4, 'oito', 4), (4, 'Corinthians', 4), (4, 'quarenta', 4),
         (5, 'duas', 4), (5, 'escapa', 4)]

INT, INT_F = time_('INTERNACIONAL')
VTR, VTR_F = time_('VITÓRIA')
COR_, COR_F = time_('CORINTHIANS')


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def vit(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=VTR, faixa=VTR_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 38


def s0(f):
    """quadro 0 = capa: close do torcedor do Inter (vermelho) + série + pergunta; depois o jogador do Inter."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, roupa='#c8102e', pele='#e0a87e', cabelo='#3a2414')
        num(c, 'QUEM CAI?', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 5', 621, 440, f, 0, 100, 2)
        num(c, 'O INTER', 621, 1350, f, 0, 150, -2)
        num(c, 'VAI CAIR?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    co = wt(0, 'conta') - 3
    inter(c, 640, 2080, 860, f, 6, arms='cheek' if f >= co else 'hang', expr='pained' if f >= co else 'nervous', look=0, num_='10')
    if f < co - 2:
        put_placa(c, 'INTERNACIONAL', INT, 640, 880, f, CLOSE_F, 80, -3)
    else:
        num(c, 'A CONTA', 640, 880, f, co, 150, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio à noite: gol do Vitória com segundos de jogo."""
    c = estadio2('dusk').copy()
    be = wt(1, 'Beira-Rio') - 3; sg = wt(1, 'segundos') - 3
    ks = sg - 14
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, INT, INT_F, arms='shrug' if f >= ks + 8 else 'hang', expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    inter(c, 900, 1960, 700, f, 4, num_='5', arms='run', run=(f * .08) % 1 if f < ks else None, expr='shock' if f >= ks + 8 else 'stern', flip=True)
    sx = lerp(260, 430, easeOut(ramp(f, 0, ks - 4))); H = 860
    if f < ks - 4: linhas_vel(c, sx, 2010, H, f, dir=-1)
    vit(c, sx, 2010, H, f, 9, num_='7', arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 4 else None,
        kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 120, 10)
    if f < be - 2:
        put_placa(c, 'VITÓRIA', VTR, 640, 860, f, 0, 90, -2)
    elif f < sg - 2:
        num(c, 'BEIRA-RIO', 640, 860, f, be, 120, -2)
    else:
        explosao(c, 640, 860, f, sg, 200)
        num(c, 'SEGUNDOS!', 640, 860, f, sg, 130, 3)
    k = kick(f, ks, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s2(f):
    """telão: placar final 5 x 2 para o Vitória."""
    c = telao('dusk').copy()
    fi = wt(2, 'final') - 3; ci = wt(2, 'cinco') - 3
    vit(c, 330, 2080, 680, f, 3, arms='up' if f >= ci else 'cintura', expr='grin', look=1, num_='9')
    inter(c, 950, 2080, 680, f, 5, arms='cheek' if f >= ci else 'hang', expr='pained' if f >= ci else 'stern', look=-1, flip=True, num_='8')
    if f < ci - 2:
        telao_txt(c, [('FINAL', 200)], f, fi, y=700)
    else:
        telao_txt(c, [('INTER 2', 150), ('VITÓRIA 5', 150)], f, ci, y=650)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, ci if f >= ci else fi, .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s3(f):
    """vestiário do Vitória: 44 pontos."""
    c = vestiario(VTR, VTR_F).copy()
    qu = wt(3, 'quarenta') - 3
    vit(c, 640, 2110, 860, f, 6, arms='up' if f >= qu else 'cintura', expr='grin', look=0, num_='10')
    if f >= qu:
        numero_gigante(c, '44 PTS', 640, 1000, f, qu, 200, -3)
    else:
        put_placa(c, 'VITÓRIA', VTR, 640, 1000, f, 0, 90, -2)
    confete(c, 640, 600, f, qu, 50, 500)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, qu, .7)
    return c, (640, 1400 + k * 10, z, k), 'golden'


def s4(f):
    """a conta: Inter 38, na zona; Corinthians 40."""
    c = conta_bg().copy()
    oi = wt(4, 'oito') - 3; co = wt(4, 'Corinthians') - 3; qa = wt(4, 'quarenta') - 3
    if f < oi - 2:
        put_placa(c, 'INTERNACIONAL', INT, 640, 1000, f, 0, 80, -2)
    elif f < co - 2:
        numero_gigante(c, '38', 640, 1000, f, oi, 300, 3)
    elif f < qa - 2:
        put_placa(c, 'CORINTHIANS', COR_, 640, 1000, f, co, 84, -2)
    else:
        numero_gigante(c, '40', 640, 1000, f, qa, 300, -3)
    if f >= co:
        put_atleta(c, 640, 2090, 760, f, 7, cores=COR_, faixa=COR_F, skin=2, hs='curto', hair='#151010',
                   arms='cintura', expr='stern', look=0, num_='9')
    else:
        inter(c, 640, 2090, 760, f, 6, arms='cheek' if f >= oi else 'hang', expr='nervous', look=0, num_='10')
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, qa if f >= qa else (co if f >= co else oi), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """vestiário do Inter: faltam 2 rodadas, escapa?"""
    c = vestiario(INT, INT_F).copy()
    du = wt(5, 'duas') - 3; es = wt(5, 'escapa') - 8
    inter(c, 640, 2110, 860, f, 6, arms='hang' if f < es else 'cheek', expr='nervous' if f < es else 'pained', look=0, num_='10')
    if f < es - 2:
        if f >= du: numero_gigante(c, '2 RODADAS', 640, 1000, f, du, 150, -3)
    else:
        num(c, 'ESCAPA?', 640, 1000, f, es, 170, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, es if f >= es else du, .6)
    return c, (640, 1400 + k * 8, z, k), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'conta') - 3, 130, .7)
    s.apito(s.W(1, 'Beira-Rio') - 6)
    ks = s.W(1, 'segundos') - 17
    s.chute(ks); s.rede(ks + 10); s.rugido(ks + 11, 2.0, .7)
    s.thunk(s.W(1, 'segundos') - 3, 150, .9)
    s.apito(s.W(2, 'final') - 4, longo=True)
    s.thunk(s.W(2, 'cinco') - 3, 160, 1.0)
    s.thunk(s.W(3, 'quarenta') - 3, 150, .9)
    s.thunk(s.W(4, 'oito') - 3, 150, .9)
    s.thunk(s.W(4, 'Corinthians') - 3, 120, .7)
    s.thunk(s.W(4, 'quarenta') - 3, 150, .9)
    s.thunk(s.W(5, 'duas') - 3, 130, .8)
    s.ting(s.W(5, 'escapa') - 8, .35)
    s.thunk(s.W(5, 'escapa') - 8, 160, 1.0)
