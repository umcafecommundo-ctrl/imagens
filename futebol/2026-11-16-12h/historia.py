"""anima.futebol — 16/11/2026 12h — Seleção Brasileira: provável time com 7 mudanças para Brasil x Singapura.
Fontes (conferidas em 16/11/2026): Metrópoles (provável Lucas Perri; Vanderson, Jonathan Jesus, Gabriel Magalhães, Douglas Santos;
João Gomes, Bruno Guimarães, Rayan; Estêvão, Endrick, Vini Jr; 7 mudanças, só Gabriel, Bruno, Estêvão e Vini mantidos; Endrick no
lugar de Raphinha suspenso; Rayan testado pela esquerda do meio; terça 17/11 7h, Estádio Nacional; último jogo de 2026);
ABCD Jornal (mesmo time, 7 peças trocadas, auxiliar Francesco Mauri à beira do campo com Ancelotti suspenso, 7h, Estádio Nacional);
NC News (Mauri no banco, Endrick no lugar de Raphinha, Rayan no meio pela esquerda, Japão 3x2, último jogo de 2026, próxima Data Fifa
em março de 2027). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "A Seleção Brasileira deve ter sete mudanças no time para enfrentar Singapura.",
    "O jogo é amanhã, às sete da manhã, e é o último do Brasil em dois mil e vinte e seis.",
    "Com Raphinha suspenso, quem deve ganhar a vaga no ataque é Endrick.",
    "Ele forma o trio com Estêvão e Vini Júnior, que fez os dois gols contra o Japão.",
    "No meio, Rayan, que é atacante, deve ser testado pelo lado esquerdo.",
    "Do time que perdeu, só quatro continuam: Gabriel Magalhães, Bruno Guimarães, Estêvão e Vini.",
    "E sem Ancelotti, também suspenso, quem comanda o Brasil na beira do campo é o auxiliar Francesco Mauri.",
    "Depois dos três a dois para o Japão, o Brasil quer uma resposta, porque a próxima Data Fifa só vem em março.",
]
CAPTXT = [
    "A Seleção Brasileira deve ter 7 mudanças|no time para enfrentar Singapura.",
    "O jogo é amanhã, às 7h,|e é o último do Brasil em 2026.",
    "Com Raphinha suspenso, quem deve ganhar|a vaga no ataque é Endrick.",
    "Ele forma o trio com Estêvão e Vini Júnior,|que fez os 2 gols contra o Japão.",
    "No meio, Rayan, que é atacante,|deve ser testado pelo lado esquerdo.",
    "Do time que perdeu, só 4 continuam: Gabriel|Magalhães, Bruno Guimarães, Estêvão e Vini.",
    "E sem Ancelotti, também suspenso, quem comanda o Brasil|na beira do campo é o auxiliar Francesco Mauri.",
    "Depois dos 3 a 2 para o Japão, o Brasil quer uma resposta,|porque a próxima Data Fifa só vem em março.",
]
FALA_TIKTOK = "Endrick no lugar de Raphinha: aprova, sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "APROVA?"
TWIST = 2
FLASH = [2]
CHECK = [(0, 'sete', 4), (0, 'Singapura', 4), (1, 'sete', 4), (1, 'ultimo', 4), (2, 'Raphinha', 4), (2, 'Endrick', 4),
         (3, 'Estevao', 4), (3, 'Japao', 4), (4, 'Rayan', 4), (4, 'esquerdo', 4), (5, 'quatro', 4), (5, 'Vini', 4),
         (6, 'Ancelotti', 4), (6, 'Mauri', 4), (7, 'marco', 4)]

BRA, BRA_F = time_('BRASIL')
SIN, SIN_F = time_('SINGAPURA')
TEC = ('#2a2f45', '#2a2f45', '#2a2f45')


def br(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=BRA, faixa=BRA_F, **kw)


def sin(c, x, y, h, f, seed, **kw):
    kw.setdefault('hair', '#111111')
    put_atleta(c, x, y, h, f, seed, cores=SIN, faixa=SIN_F, skin=1, **kw)


def tec(c, x, y, h, f, seed=9, hair='#a7a7a7', **kw):
    kw.setdefault('arms', 'hang'); kw.setdefault('expr', 'stern')
    put_atleta(c, x, y, h, f, seed, cores=TEC, faixa=None, skin=1, hair=hair, hs='curto', sock='#1a1a1a', **kw)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    se = wt(0, 'sete') - 3; si = wt(0, 'Singapura') - 3
    br(c, 330, 2010, 860, f, 3, arms='cintura', expr='stern', look=1, num_='10')
    put_placa(c, 'BRASIL', BRA, 330, 1110, f, wt(0, 'Selecao') - 3, 60, -3)
    explosao(c, 640, 800, f, se, 240)
    num(c, '7 MUDANÇAS', 640, 800, f, se + 2, 120, -4)
    if f >= si - 10:
        sx = lerp(1550, 950, easeOut(ramp(f, si - 10, si + 4)))
        if f < si + 4: linhas_vel(c, sx, 2010, 860, f, dir=1)
        sin(c, sx, 2010, 860, f, 7, arms='cintura', expr='proud', look=-1, flip=True, run=(f * .09) % 1 if f < si + 4 else None, num_='9')
        put_placa(c, 'SINGAPURA', SIN, 950, 1110, f, si + 4, 54, 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, se, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('golden').copy()
    am = wt(1, 'amanha') - 3; se = wt(1, 'sete') - 3; ul = wt(1, 'ultimo') - 3
    if f >= am: paste_c(c, calendario('17', 'NOV'), 380, 1130, .62 * back(ramp(f, am, am + 8)))
    num(c, '7H', 900, 1130, f, se, 180, 4)
    num(c, 'AMANHÃ', 640, 700, f, am, 110, -3)
    num(c, 'ÚLTIMO JOGO DE 2026', 640, 860, f, ul, 76, 3)
    br(c, 250, 2040, 700, f, 4, arms='hang', expr='neutral', look=1, skin=2)
    sin(c, 1030, 2040, 700, f, 8, arms='hang', expr='neutral', look=-1, flip=True)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1360, z, 0), 'golden'


def s2(f):
    c = estadio2('dusk').copy()
    gx, gy = put_gol2(c, estufa=ramp(f, wt(2, 'Endrick') + 6, wt(2, 'Endrick') + 12))
    ra = wt(2, 'Raphinha') - 3; su = wt(2, 'suspenso') - 3; en = wt(2, 'Endrick') - 4
    put_goleiro(c, f, SIN, SIN_F, arms='shrug' if f >= en + 4 else 'hang', expr='shock' if f >= en + 4 else 'nervous', skin=1)
    # Raphinha sai pela esquerda
    rx = 330 if f < su else lerp(330, -400, (ramp(f, su, su + 16) ** 2))
    if f < su + 16:
        br(c, rx, 2010, 820, f, 3, skin=2, num_='11', arms='hang' if f < su else 'run', run=(f * .1) % 1 if f >= su else None,
           expr='pained', look=-1, flip=f >= su)
        put_placa(c, 'RAPHINHA', BRA, rx, 1080, f, ra, 50, -3)
        num(c, 'SUSPENSO', 640, 760, f, su, 120, -4)
    # Endrick entra e chuta
    if f >= su + 4:
        ex = lerp(1500, 600, easeOut(ramp(f, su + 4, en - 4)))
        if f < en - 4: linhas_vel(c, ex, 2010, 860, f, dir=1)
        br(c, ex, 2010, 860, f, 5, skin=3, num_='9', arms='up' if f >= en + 8 else 'run', run=(f * .1) % 1 if f < en - 4 else None,
           kick=pulse(f, en - 3, 5), expr='grin' if f >= en else 'stern', flip=True)
        if f >= en - 2: foco(c, ex, 1650, 420, .6 * ramp(f, en - 2, en + 4))
        put_placa(c, 'ENDRICK', BRA, ex, 1110, f, en, 60, 3)
        rb = raio_bola(860)
        if f < en: bx, by, r = ex - 110, 2010 - rb, rb
        else:
            t = ramp(f, en, en + 9); bx, by = lerp(490, gx + 90, t), lerp(2010 - rb, gy, t) - 120 * math.sin(t * math.pi)
            r = lerp(rb, raio_bola(300), t)
        if f < en + 30: put_bola(c, bx, by, r, f)
    k = kick(f, en, .9)
    return c, (lerp(600, 680, smooth(f / 90)), 1440 + k * 10, 1.06 * (1 + .0007 * f), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    es = wt(3, 'Estevao') - 3; vi = wt(3, 'Vini') - 3; ja = wt(3, 'Japao') - 3
    br(c, 640, 2030, 860, f, 5, num_='9', arms='cintura', expr='grin')
    put_placa(c, 'ENDRICK', BRA, 640, 1110, f, 0, 52)
    if f >= es - 8:
        x = lerp(-300, 280, easeOut(ramp(f, es - 8, es + 6)))
        br(c, x, 2050, 760, f, 6, skin=2, num_='7', arms='up', expr='grin', look=1, run=(f * .1) % 1 if f < es + 6 else None)
        put_placa(c, 'ESTÊVÃO', BRA, 280, 1220, f, es, 46, -3)
    if f >= vi - 8:
        x = lerp(1550, 1000, easeOut(ramp(f, vi - 8, vi + 6)))
        br(c, x, 2050, 760, f, 7, skin=4, num_='10', arms='up', expr='grin', look=-1, flip=True, run=(f * .1) % 1 if f < vi + 6 else None)
        put_placa(c, 'VINI JR', BRA, 1000, 1220, f, vi, 46, 3)
    num(c, 'TRIO DE ATAQUE', 640, 720, f, wt(3, 'trio') - 3, 96, -3)
    num(c, '2 GOLS NO JAPÃO', 640, 870, f, ja, 70, 3)
    if f >= ja: confete(c, 1000, 1300, f, ja, 40, 300)
    z = lerp(1.15, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    return c, (640, 1420, z, 0), 'dusk'


def s4(f):
    c = estadio2('day').copy()
    ra = wt(4, 'Rayan') - 3; at = wt(4, 'atacante') - 3; eq = wt(4, 'esquerdo') - 3
    x = 640 if f < eq else lerp(640, 330, easeOut(ramp(f, eq, eq + 14)))
    if eq <= f < eq + 14: linhas_vel(c, x, 2020, 880, f, dir=1)
    br(c, x, 2020, 880, f, 8, skin=3, num_='20', arms='point' if f < eq else 'run', run=(f * .1) % 1 if eq <= f < eq + 14 else None,
       expr='proud', flip=f >= eq)
    put_placa(c, 'RAYAN', BRA, x, 1120, f, ra, 60, -3)
    num(c, 'ATACANTE NO MEIO', 640, 740, f, at, 90, -3)
    if f >= eq: num(c, 'PELA ESQUERDA', 640, 900, f, eq, 76, 2)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    return c, (lerp(680, 600, smooth(f / 90)), 1420, z, 0), 'golden'


def s5(f):
    c = estadio2('dusk').copy()
    qu = wt(5, 'quatro') - 3
    nomes = [('GABRIEL', 'Gabriel', 230, 2, 'raspado'), ('BRUNO', 'Bruno', 490, 1, 'curto'),
             ('ESTÊVÃO', 'Estevao', 750, 2, 'curto'), ('VINI', 'Vini', 1010, 4, 'curto')]
    for i, (n, w, x, sk, hs) in enumerate(nomes):
        t0 = wt(5, w) - 4
        if f >= t0 - 6:
            y = lerp(2600, 2010, back(ramp(f, t0 - 6, t0 + 4)))
            br(c, x, y, 660, f, 20 + i, skin=sk, hs=hs, arms='joinha', expr='proud', num_=str(4 + i * 2), flip=i >= 2)
            put_placa(c, n, BRA, x, 1260, f, t0, 40, -3 if i % 2 else 3)
    num(c, 'SÓ 4 CONTINUAM', 640, 760, f, qu, 110, -3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0005 * f)
    return c, (640 + 15 * math.sin(f * .04), 1420, z, 0), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    an = wt(6, 'Ancelotti') - 3; su = wt(6, 'suspenso') - 3; ma = wt(6, 'Mauri') - 4
    # Ancelotti ao fundo, fora do campo
    tec(c, 940, 1720, 470, f, 9, arms='cheek' if f >= su else 'hang', look=-1, flip=True)
    put_placa(c, 'ANCELOTTI', TEC, 940, 1180, f, an, 40, 3)
    num(c, 'SUSPENSO', 940, 1050, f, su, 60, -3)
    tec(c, 470, 2030, 880, f, 31, hair='#4a3a2e', arms='point' if f >= ma else 'cintura', expr='stern', look=1)
    put_placa(c, 'FRANCESCO MAURI', TEC, 470, 1090, f, ma, 44, -3)
    if f >= ma: foco(c, 470, 1650, 430, .6 * ramp(f, ma, ma + 6))
    num(c, 'AUXILIAR NO COMANDO', 640, 740, f, wt(6, 'auxiliar') - 3, 70, -3)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, ma, .5)
    return c, (lerp(600, 660, smooth(f / 90)), 1430 + k * 8, z, k), 'dusk'


def s7(f):
    c = estadio2('dusk').copy()
    re = wt(7, 'resposta') - 3; ma = wt(7, 'marco') - 3
    br(c, 330, 2010, 860, f, 3, arms='punho' if f >= re else 'cintura', expr='stern', look=1, num_='10')
    sin(c, 950, 2010, 860, f, 7, arms='cintura', expr='proud', look=-1, flip=True, num_='9')
    num(c, 'X', 640, 1520, f, 0, 160)
    num(c, 'HORA DA RESPOSTA', 640, 740, f, re, 82, -3)
    num(c, 'PRÓXIMA DATA FIFA: MARÇO', 640, 900, f, ma, 54, 3)
    z = lerp(1.0, 1.05, easeOut(ramp(f, 0, 70))) * (1 + .0003 * f)
    k = kick(f, re, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('7 MUDANÇAS', 'CONTRA SINGAPURA', wt(0, 'sete') - 3),
         1: ('TERÇA, 17/11, ÀS 7H', 'ÚLTIMO JOGO DE 2026', wt(1, 'ultimo') - 3),
         2: ('ENDRICK NO ATAQUE', 'NO LUGAR DE RAPHINHA', wt(2, 'Endrick') + 14),
         3: ('O TRIO DE ATAQUE', 'ENDRICK, ESTÊVÃO E VINI JR', wt(3, 'Vini') + 6),
         4: ('RAYAN NO MEIO', 'TESTE PELA ESQUERDA', wt(4, 'esquerdo') + 4),
         5: ('SÓ 4 MANTIDOS', 'DO TIME QUE PERDEU PARA O JAPÃO', wt(5, 'Vini') + 2),
         6: ('FRANCESCO MAURI', 'AUXILIAR COMANDA O BRASIL', wt(6, 'Mauri') + 4),
         7: ('BRASIL x SINGAPURA', 'AMANHÃ, ÀS 7H', wt(7, 'resposta') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'sete') - 3, 150, .8)
    s.ting(s.W(1, 'ultimo') - 3, .3)
    s.thunk(s.W(2, 'suspenso') - 3, 140, .6)
    s.thunk(s.W(2, 'Endrick') - 4, 120, 1.0)
    s.ting(s.W(3, 'Vini') - 3, .3)
    s.thunk(s.W(4, 'esquerdo') - 3, 200, .5)
    s.thunk(s.W(5, 'quatro') - 3, 160, .6)
    s.ting(s.W(6, 'Mauri') - 3, .3)
    s.thunk(s.W(7, 'resposta') - 3, 150, .7)
