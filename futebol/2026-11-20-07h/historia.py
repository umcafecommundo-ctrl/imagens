"""anima.futebol — 20/11/2026 07h — Brasileirão 35ª rodada: Inter perde para o Vasco e termina a rodada no Z4; Vitória vence e respira.
Fontes (conferidas em 20/11/2026): CNN Brasil e A Crítica (Vasco 2x1 Internacional em São Januário, 19/11 19h30: Thiago Mendes no
1º tempo, Juninho de cabeça no início do 2º, Colidio no 2º tempo; Vasco 47 pts, Inter 38 pts 17º no Z4, Grêmio 38 18º,
Corinthians 40 16º, Remo e Chapecoense também no Z4; faltam 3 rodadas); CNN Brasil e bahia.ba (Vitória 2x1 Bragantino no Barradão:
Brítez 3' e Renê 23'/24' no 1º tempo, Gean contra no 2º; estreia de Rafael Lacerda no lugar de Jair Ventura; fim de jejum de 5 jogos;
Vitória 41 pts 14º); Internacional x Vitória segunda 23/11 19h30 no Beira-Rio (CNN, A Crítica, bahia.ba).
Permanência "matemática" do Vasco só em 1 fonte -> não usada. Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Internacional perdeu e terminou a rodada dentro da zona de rebaixamento.",
    "Ontem à noite, a briga contra a queda teve dois jogos no mesmo horário.",
    "Em São Januário, Thiago Mendes abriu o placar para o Vasco, e Juninho empatou de cabeça para o Inter.",
    "Mas no segundo tempo, Colidio fez o gol da vitória do Vasco: dois a um.",
    "Em Salvador, o Vitória estreou o técnico Rafael Lacerda e fez dois gols no primeiro tempo, com Brítez e Renê.",
    "O Bragantino ainda diminuiu, mas o Vitória venceu e acabou com um jejum de cinco jogos.",
    "Agora o Corinthians, com quarenta, está fora. Inter e Grêmio, com trinta e oito, estão no Z4.",
    "E na segunda-feira tem Inter e Vitória, no Beira-Rio. Quem escapa?",
]
CAPTXT = [
    "O Internacional perdeu e terminou a rodada|dentro da zona de rebaixamento.",
    "Ontem à noite, a briga contra a queda|teve 2 jogos no mesmo horário.",
    "Em São Januário, Thiago Mendes abriu o placar para o Vasco,|e Juninho empatou de cabeça para o Inter.",
    "Mas no 2º tempo, Colidio fez|o gol da vitória do Vasco: 2 a 1.",
    "Em Salvador, o Vitória estreou o técnico Rafael Lacerda|e fez 2 gols no 1º tempo, com Brítez e Renê.",
    "O Bragantino ainda diminuiu, mas o Vitória venceu|e acabou com um jejum de 5 jogos.",
    "Agora o Corinthians, com 40, está fora.|Inter e Grêmio, com 38, estão no Z4.",
    "E na segunda-feira tem Inter e Vitória,|no Beira-Rio. Quem escapa?",
]
FALA_TIKTOK = "Quem escapa da queda, Inter ou Vitória? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM ESCAPA?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'Internacional', 4), (0, 'rebaixamento', 4), (1, 'noite', 4), (1, 'dois', 4), (2, 'Mendes', 4), (2, 'Juninho', 4),
         (3, 'Colidio', 4), (3, 'dois', 4), (4, 'Lacerda', 4), (4, 'Britez', 4), (4, 'Rene', 4), (5, 'Bragantino', 4),
         (5, 'jejum', 4), (6, 'quarenta', 4), (6, 'trinta', 4), (7, 'segunda-feira', 4), (7, 'escapa', 4)]

VAS, VAS_F = time_('VASCO')
INT, INT_F = time_('INTERNACIONAL')
VIT_, VIT_F = time_('VITÓRIA')
RBB, RBB_F = time_('BRAGANTINO')
COR, COR_F = time_('CORINTHIANS')
GRE, GRE_F = time_('GRÊMIO')


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def vit(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'raspado'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=VIT_, faixa=VIT_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def gol_cena(c, f, kf, kcores, kfaixa, gcores, gfaixa, kseed, kskin=1, khair='#2a1a10', run_in=True, num_='10', hs='curto'):
    """chute: atacante na frente, gol no fundo, bola diminuindo."""
    gx, gy = put_gol2(c, estufa=ramp(f, kf + 8, kf + 14))
    put_goleiro(c, f, gcores, gfaixa, arms='shrug' if f >= kf + 8 else 'hang', expr='shock' if f >= kf + 8 else 'nervous', skin=2)
    sx = lerp(260, 470, easeOut(ramp(f, 0, kf - 4))) if run_in else 470
    if run_in and f < kf - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    put_atleta(c, sx, 2010, 860, f, kseed, cores=kcores, faixa=kfaixa, skin=kskin, hair=khair, hs=hs, num_=num_,
               arms='up' if f >= kf + 10 else 'run', run=(f * .1) % 1 if (run_in and f < kf - 4) else None,
               kick=pulse(f, kf - 3, 5), expr='grin' if f >= kf + 6 else 'stern')
    rb = raio_bola(860)
    if f < kf + 40: bola_voo(c, f, kf, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 140)
    return gx, gy


def s0(f):
    c = estadio2('dusk').copy()
    it = wt(0, 'Internacional') - 3; pe = wt(0, 'perdeu') - 3; rb = wt(0, 'rebaixamento') - 3
    inter(c, 640, 2030, 900, f, 3, arms='cheek' if f >= pe else 'hang', expr='pained' if f >= pe else 'nervous', look=0, num_='10')
    put_placa(c, 'INTERNACIONAL', INT, 640, 1060, f, it, 64, -3)
    if f >= rb: explosao(c, 640, 780, f, rb, 220, cor=(230, 60, 60))
    num(c, 'NO Z4!', 640, 780, f, rb + 2, 150, -4)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, rb, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    no = wt(1, 'noite') - 3; do = wt(1, 'dois') - 3
    if f >= no: paste_c(c, calendario('19', 'NOV'), 640, 1080, .6 * back(ramp(f, no, no + 8)))
    num(c, 'ONTEM, 19H30', 640, 720, f, no, 110, -3)
    put_placa(c, 'VASCO x INTER', VAS, 640, 1430, f, do, 60, -3)
    put_placa(c, 'VITÓRIA x BRAGANTINO', VIT_, 640, 1580, f, do + 4, 56, 3)
    inter(c, 230, 2120, 540, f, 4, arms='hang', expr='nervous', look=1)
    vit(c, 1040, 2120, 540, f, 8, arms='hang', expr='nervous', look=-1, flip=True)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1360, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    tm = wt(2, 'Mendes') - 3; ju = wt(2, 'Juninho') - 3; ca = wt(2, 'cabeca') - 3
    gol_cena(c, f, tm, VAS, VAS_F, INT, INT_F, 5, kskin=2, khair='#151010', num_='8')
    num(c, 'SÃO JANUÁRIO', 640, 700, f, wt(2, 'Januario') - 3, 86, -3)
    put_placa(c, 'THIAGO MENDES', VAS, 470, 860, f, tm + 6, 56, -3)
    put_placa(c, 'JUNINHO (INTER)', INT, 470, 990, f, ju, 56, 2)
    num(c, 'VAS 1 x 1 INT', 820, 1160, f, ca, 80, 2)
    k = kick(f, tm, .9)
    return c, (lerp(600, 680, smooth(f / 150)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    co = wt(3, 'Colidio') - 3; do = wt(3, 'dois') - 3
    gol_cena(c, f, co, VAS, VAS_F, INT, INT_F, 9, kskin=1, khair='#2a1a10', num_='9')
    put_placa(c, 'COLIDIO', VAS, 400, 880, f, co + 6, 56, -4)
    if f >= do: explosao(c, 640, 1080, f, do, 170)
    num(c, 'VAS 2 x 1 INT', 640, 1080, f, do, 96, 3)
    k = kick(f, co, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    la = wt(4, 'Lacerda') - 3; br = wt(4, 'Britez') - 3; re = wt(4, 'Rene') - 3
    gol_cena(c, f, br, VIT_, VIT_F, RBB, RBB_F, 13, kskin=3, khair='#151010', num_='4', hs='raspado')
    num(c, 'BARRADÃO', 640, 700, f, wt(4, 'Salvador') - 3, 90, -3)
    put_placa(c, 'TÉCNICO: RAFAEL LACERDA', VIT_, 640, 850, f, la, 50, 2)
    put_placa(c, 'BRÍTEZ', VIT_, 420, 990, f, br + 2, 58, -3)
    put_placa(c, 'RENÊ', VIT_, 420, 1110, f, re, 58, 2)
    num(c, 'VIT 2 x 0 RBB', 820, 1230, f, re + 2, 76, 3)
    k = kick(f, br, .9)
    return c, (640, 1440 + k * 10, lerp(1.1, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f), k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    bg = wt(5, 'Bragantino') - 3; ve = wt(5, 'venceu') - 3; je = wt(5, 'jejum') - 3
    put_atleta(c, 1000, 2060, 640, f, 11, cores=RBB, faixa=RBB_F, skin=1, hs='curto', hair='#3a2a1e', arms='hang',
               expr='pained' if f >= ve else 'stern', flip=True)
    vit(c, 380, 2040, 860, f, 3, arms='up' if f >= ve else 'cintura', expr='grin' if f >= ve else 'stern', look=1, num_='4')
    num(c, 'VIT 2 x 1 RBB', 640, 760, f, bg, 100, -3)
    num(c, 'FIM DO JEJUM!', 640, 960, f, je, 96, 3)
    if f >= je: confete(c, 380, 1200, f, je, 50, 500)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, ve, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    qu = wt(6, 'quarenta') - 3; tr = wt(6, 'trinta') - 3
    tabela(c, [('16º', 'CORINTHIANS', COR, '40', False)], 640, 1000, f, qu)
    tabela(c, [('17º', 'INTER', INT, '38', True), ('18º', 'GRÊMIO', GRE, '38', True)], 640, 1260, f, tr)
    num(c, 'FORA DO Z4', 640, 760, f, qu + 4, 100, -3)
    num(c, 'NO Z4', 640, 1690, f, tr + 6, 110, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, tr, .5)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s7(f):
    c = estadio2('day').copy()
    se = wt(7, 'segunda-feira') - 3; be = wt(7, 'Beira-Rio') - 3; es = wt(7, 'escapa') - 3
    fx = lerp(-260, 330, easeOut(ramp(f, se - 6, se + 10)))
    px = lerp(1500, 930, easeOut(ramp(f, se - 6, se + 10)))
    if f < se + 10:
        linhas_vel(c, fx, 2010, 840, f, dir=-1); linhas_vel(c, px, 2010, 840, f, dir=1)
    inter(c, fx, 2010, 840, f, 3, arms='cintura', expr='stern', look=1, num_='10', run=(f * .1) % 1 if f < se + 10 else None)
    vit(c, px, 2010, 840, f, 7, arms='punho' if f >= es else 'cintura', expr='stern', look=-1, flip=True, num_='9',
        run=(f * .1) % 1 if f < se + 10 else None)
    put_placa(c, 'INTER', INT, 330, 1190, f, se + 10, 54, -3)
    put_placa(c, 'VITÓRIA', VIT_, 930, 1190, f, se + 10, 54, 3)
    if f >= se: paste_c(c, calendario('23', 'NOV'), 640, 860, .45 * back(ramp(f, se, se + 8)))
    num(c, 'BEIRA-RIO', 640, 1040, f, be, 76, -2)
    num(c, 'QUEM ESCAPA?', 640, 1300, f, es, 100, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    return c, (640, 1400, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('INTER NO Z4', 'FALTAM 3 RODADAS', wt(0, 'rebaixamento') + 6),
         1: ('QUINTA, 19/11, 19H30', 'BRIGA CONTRA A QUEDA', wt(1, 'horario') + 4),
         2: ('VASCO 1 x 1 INTER', 'SÃO JANUÁRIO', wt(2, 'Inter') + 4),
         3: ('VASCO 2 x 1 INTER', 'COLIDIO NO 2º TEMPO', wt(3, 'um') + 4),
         4: ('VITÓRIA 2 x 0 BRAGANTINO', 'ESTREIA DE RAFAEL LACERDA', wt(4, 'Rene') + 8),
         5: ('VITÓRIA 2 x 1 BRAGANTINO', 'FIM DE 5 JOGOS SEM VENCER', wt(5, 'jogos') + 2),
         6: ('', '', 4), 7: ('', '', 4)}
    if si in (6, 7): return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'perdeu') - 3, 150, .9)
    s.thunk(s.W(0, 'rebaixamento') - 3, 110, .9)
    s.thunk(s.W(1, 'noite') - 3, 160, .6)
    s.thunk(s.W(2, 'Mendes') - 3, 120, .9)
    s.thunk(s.W(2, 'Juninho') - 3, 180, .6)
    s.thunk(s.W(3, 'Colidio') - 3, 120, 1.0)
    s.ting(s.W(3, 'dois') - 3, .3)
    s.thunk(s.W(4, 'Britez') - 3, 120, .9)
    s.thunk(s.W(4, 'Rene') - 3, 140, .7)
    s.ting(s.W(5, 'jejum') - 3, .3)
    s.thunk(s.W(6, 'quarenta') - 3, 150, .7)
    s.thunk(s.W(6, 'trinta') - 3, 120, .8)
    s.ting(s.W(7, 'escapa') - 3, .3)
