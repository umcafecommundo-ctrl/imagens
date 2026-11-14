"""anima.futebol — 14/11/2026 07h — Seleção Brasileira: a surpresa de Ancelotti para o Japão, Rayan no meio-campo.
Fontes (conferidas em 14/11/2026): ISTOÉ 13/11 10h50 (último treino; provável Pedro Morisco; Wesley, Jair, Gabriel
Magalhães e Carlos Augusto; Andrey Santos, Bruno Guimarães e Rayan; Estêvão, Raphinha e Vinicius Júnior; Rayan como
meio-campista pela esquerda; Raphinha centroavante; Bruno participou do treino e está disponível; sábado 14/11 7h15 de
Brasília, Estádio Nacional de Singapura; escalação não confirmada oficialmente); Sportbuzz 13/11 (mesma provável, Rayan no
meio pelo lado esquerdo, 7h15, Estádio Nacional de Singapura); Gazeta Esportiva 13/11 (mesma provável, Rayan novidade no
meio, info do ge; terça 17/11 7h Brasil x Singapura, 1º confronto da história).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD)
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "A surpresa de Ancelotti para o Japão: o atacante Rayan deve jogar no meio de campo.",
    "No último treino em Singapura, Rayan foi para o meio, pela esquerda, ao lado de Bruno Guimarães e Andrey Santos.",
    "E Bruno Guimarães, que era dúvida na semana, treinou e está liberado.",
    "No gol, a tendência é Pedro Morisco.",
    "Na frente, Raphinha de centroavante, com Estêvão pela direita e Vini Júnior pela esquerda.",
    "A provável defesa tem Wesley, Jair, Gabriel Magalhães e Carlos Augusto.",
    "A bola rola hoje, às sete e quinze, no Estádio Nacional de Singapura, e na terça o Brasil pega a seleção da casa.",
]
CAPTXT = [
    "A surpresa de Ancelotti para o Japão: o atacante|Rayan deve jogar no meio de campo.",
    "No último treino em Singapura, Rayan foi para o meio, pela esquerda,|ao lado de Bruno Guimarães e Andrey Santos.",
    "E Bruno Guimarães, que era dúvida na semana,|treinou e está liberado.",
    "No gol, a tendência é Pedro Morisco.",
    "Na frente, Raphinha de centroavante, com Estêvão|pela direita e Vini Júnior pela esquerda.",
    "A provável defesa tem Wesley, Jair,|Gabriel Magalhães e Carlos Augusto.",
    "A bola rola hoje, às 7h15, no Estádio Nacional de Singapura,|e na terça o Brasil pega a seleção da casa.",
]
FALA_TIKTOK = "Rayan no meio de campo: aprova ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "APROVA?"
TWIST = 4
FLASH = [2]
CHECK = [(0, 'Rayan', 4), (0, 'campo', 4), (1, 'treino', 4), (1, 'Andrey', 4), (2, 'liberado', 4), (3, 'Morisco', 4),
         (4, 'Raphinha', 4), (4, 'Vini', 4), (5, 'Jair', 4), (5, 'Augusto', 4), (6, 'quinze', 4), (6, 'terca', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
SIN, SIN_F = time_('SINGAPURA')
TEC = ('#23283a', '#23283a', '#23283a')
GK = ('#2fa35a', '#111111', '#111111')   # camisa de goleiro genérica


def put_cal(c, dia, x, y, s, f, f0, mes='NOV'):
    if f >= f0: paste_c(c, calendario(dia, mes), x, y, s * back(ramp(f, f0, f0 + 8)))


def rayan(c, x, y, h, f, **kw):
    put_jog(c, x, y, h, f, 5, cores=BRA, faixa=BRA_F, skin=2, hair='#111111', **kw)


def bruno(c, x, y, h, f, **kw):
    put_jog(c, x, y, h, f, 6, cores=BRA, faixa=BRA_F, skin=1, hair='#2b1d14', **kw)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    su = wt(0, 'surpresa') - 3; an = wt(0, 'Ancelotti') - 3; ra = wt(0, 'Rayan') - 3; me = wt(0, 'meio') - 3
    num(c, 'SURPRESA!', 640, 740, f, su, 150, -4)
    if f >= an - 6:
        xx = lerp(-400, 300, easeOut(ramp(f, an - 6, an + 6)))
        put_jog(c, xx, 2000, 700, f, 9, cores=TEC, faixa=None, arms='point', expr='smug', skin=0, hair='#9a9a9a')
        put_placa(c, 'ANCELOTTI', TEC, 300, 1220, f, an, 52, -3)
    if f >= ra - 6:
        y = lerp(2600, 2030, easeOut(ramp(f, ra - 6, ra + 6)))
        rayan(c, 860, y, 880, f, arms='up' if f >= me else 'cintura', expr='shock' if f < me else 'grin', flip=True)
        put_placa(c, 'RAYAN', BRA, 860, 1080, f, ra, 60, 3)
    num(c, 'NO MEIO-CAMPO', 640, 900, f, me, 96, 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, me, .7)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('day').copy()
    tr = wt(1, 'treino') - 3; si = wt(1, 'Singapura') - 3; es = wt(1, 'esquerda') - 3
    br = wt(1, 'Bruno') - 3; ad = wt(1, 'Andrey') - 3
    num(c, 'ÚLTIMO TREINO', 640, 720, f, tr, 110, -3)
    num(c, 'SINGAPURA', 640, 870, f, si, 90, 3)
    rx = lerp(640, 250, easeOut(ramp(f, es - 6, es + 6)))
    rayan(c, rx, 2030, 760, f, arms='run' if f < es + 6 else 'joinha', expr='grin')
    put_placa(c, 'RAYAN', BRA, rx, 1160, f, 0, 56, -3)
    if f >= br - 6:
        bruno(c, lerp(1550, 680, easeOut(ramp(f, br - 6, br + 6))), 1990, 700, f, arms='cintura', expr='proud', flip=True)
        put_placa(c, 'BRUNO G.', BRA, 680, 1200, f, br, 52, 3)
    if f >= ad - 6:
        put_jog(c, lerp(1600, 1060, easeOut(ramp(f, ad - 6, ad + 6))), 1960, 660, f, 8, cores=BRA, faixa=BRA_F,
                arms='cintura', expr='grin', skin=3, hair='#111111', flip=True)
        put_placa(c, 'ANDREY', BRA, 1040, 1240, f, ad, 52, -3)
    return c, (lerp(600, 680, smooth(f / 140)), 1430, 1.04 * (1 + .0008 * f), 0), 'golden'


def s2(f):
    c = estadio('day').copy()
    du = wt(2, 'duvida') - 3; tr = wt(2, 'treinou') - 3; li = wt(2, 'liberado') - 3
    num(c, 'DÚVIDA?', 640, 740, f, du, 140, -4)
    bruno(c, 600, 2030, 880, f, arms='shrug' if f < tr else ('joinha' if f < li else 'up'), expr='nervous' if f < tr else 'grin',
          walk=(f * .06) % 1 if tr <= f < li else 0)
    put_placa(c, 'BRUNO GUIMARÃES', BRA, 600, 1080, f, wt(2, 'Bruno') - 3, 56, -3)
    num(c, 'LIBERADO!', 640, 910, f, li, 130, 4)
    k = kick(f, li, .8)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 40))) * (1 + .0012 * f)
    return c, (640 + 25 * math.sin(f * .05), 1430 + k * 10, z, k), 'golden'


def s3(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=640)
    mo = wt(3, 'Morisco') - 3
    put_jog(c, 640, 2030, 860, f, 4, cores=GK, faixa=None, arms='up' if f >= mo else 'shrug', expr='proud', skin=0, hair='#6b4a2b')
    put_placa(c, 'PEDRO MORISCO', GK, 640, 1080, f, mo, 48, -3)
    num(c, 'NO GOL', 640, 760, f, wt(3, 'gol') - 3, 140, -4)
    num(c, 'TENDÊNCIA', 640, 920, f, wt(3, 'tendencia') - 3, 90, 3)
    k = kick(f, mo, .7)
    return c, (640, 1440 + k * 8, lerp(1.0, 1.1, smooth(f / 60)), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=700)
    ce = wt(4, 'centroavante') - 3; es = wt(4, 'Estevao') - 3; vi = wt(4, 'Vini') - 3; la = wt(4, 'esquerda') - 3
    put_goleiro(c, f, JAP, JAP_F, gx=720, arms='shrug', expr='shock' if f >= la else 'nervous', skin=0, hair='#111111')
    put_jog(c, 600, 2030, 860, f, 3, cores=BRA, faixa=BRA_F, skin=1, hair='#2b1d14', num_='9', arms='run', expr='grin',
            kick=pulse(f, la - 5, 5))
    put_placa(c, 'RAPHINHA', BRA, 600, 1050, f, wt(4, 'Raphinha') - 3, 54, -3)
    num(c, 'CENTROAVANTE', 640, 760, f, ce, 100, -3)
    for nome, x, sd, sk, f0 in (('ESTÊVÃO', 1040, 4, 2, es), ('VINI JR.', 200, 2, 3, vi)):
        if f < f0 - 4: continue
        yy = lerp(2500, 1990, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, yy, 720, f, sd, cores=BRA, faixa=BRA_F, arms='up' if f >= la + 8 else 'run', expr='grin', skin=sk,
                hair='#111111', flip=x > 640)
        put_placa(c, nome, BRA, min(max(x, 260), 1000), 1200, f, f0, 46, -3 if x < 640 else 3)
    rb = raio_bola(860)
    if f < la - 3: bx, by, r = 700, 2030 - rb, rb
    else:
        t = ramp(f, la - 3, la + 6)
        bx, by, r = lerp(700, gx + 90, t), lerp(2030 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    k = kick(f, la + 4)
    return c, (640 + 30 * math.sin(f * .03), 1420 + k * 10, lerp(1.0, 1.05, smooth(f / 110)), k), 'dusk'


def s5(f):
    c = estadio('day').copy()
    num(c, 'DEFESA', 640, 720, f, wt(5, 'defesa') - 3, 140, -3)
    for i, (w, nome, sk) in enumerate((('Wesley', 'WESLEY', 3), ('Jair', 'JAIR', 2), ('Gabriel', 'GABRIEL M.', 1), ('Carlos', 'C. AUGUSTO', 0))):
        f0 = wt(5, w) - 3
        if f < f0 - 4: continue
        x = 175 + i * 297
        yy = lerp(2500, 2000, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, yy, 700, f, 11 + i, cores=BRA, faixa=BRA_F, arms='cintura', expr='stern', skin=sk, hair='#111111', flip=x > 640)
        put_placa(c, nome, BRA, min(max(x, 230), 1030), 1120 + (i % 2) * 100, f, f0, 40, -3 if i % 2 else 3)
    return c, (640 + 20 * math.sin(f * .04), 1440, lerp(1.0, 1.06, smooth(f / 100)), 0), 'golden'


def s6(f):
    c = estadio('dusk').copy()
    ho = wt(6, 'hoje') - 3; te = wt(6, 'terca') - 3
    if f < te:
        bx = lerp(-300, 330, easeOut(ramp(f, 0, 14)))
        ax = lerp(1550, 930, easeOut(ramp(f, 4, 18)))
        put_jog(c, bx, 2010, 860, f, 3, cores=BRA, faixa=BRA_F, skin=1, num_='9', arms='cintura', expr='stern', look=1)
        put_jog(c, ax, 2010, 860, f, 6, cores=JAP, faixa=JAP_F, arms='cintura', expr='smug', skin=0, hair='#111111', look=-1)
        put_placa(c, 'BRASIL', BRA, 330, 1180, f, 6, 64, -4)
        put_placa(c, 'JAPÃO', JAP, 930, 1180, f, 10, 64, 4)
        num(c, 'X', 640, 1520, f, 12, 160)
        num(c, 'HOJE 7H15', 640, 740, f, ho, 140, -4)
        num(c, 'ESTÁDIO NACIONAL', 640, 900, f, wt(6, 'Estadio') - 3, 80, 3)
    else:
        put_jog(c, 330, 2010, 860, f, 3, cores=BRA, faixa=BRA_F, skin=1, num_='9', arms='point', expr='grin', look=1)
        sx = lerp(1550, 930, easeOut(ramp(f, te, te + 12)))
        put_jog(c, sx, 2010, 860, f, 7, cores=SIN, faixa=SIN_F, arms='cintura', expr='proud', skin=0, hair='#111111', look=-1)
        put_placa(c, 'SINGAPURA', SIN, 930, 1180, f, te + 4, 54, 4)
        put_cal(c, '17', 640, 820, .6, f, te)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ho, .6) + kick(f, te, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'surpresa') - 3, 140, .8)
    s.thunk(s.W(0, 'meio') - 3, 160, .8)
    s.ting(s.W(1, 'esquerda') - 3, .3)
    s.ting(s.W(2, 'liberado') - 3, .35)
    s.thunk(s.W(3, 'Morisco') - 3, 150, .8)
    s.thunk(s.W(4, 'esquerda') - 3, 140, .8)
    s.thunk(s.W(5, 'defesa') - 3, 200, .6)
    s.ting(s.W(6, 'quinze') - 3, .3)
    s.ting(s.W(6, 'terca') - 3, .3)
