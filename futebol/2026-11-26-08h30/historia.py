"""anima.futebol — 26/11/2026 08h30 — BASTIDORES · EP. 3 — Palmeiras já em Montevidéu: Piquerez joga a final?
Fontes (conferidas em 26/11/2026, ver fatos.txt): Portal do Palestra (25/11 21h29, chegada a Montevidéu na noite de quarta,
Paulinho relacionado), palmeiras.com.br (25/11, Piquerez em parte do treino integrado, final sábado 17h no Centenário),
Lance (25/11, Piquerez será reavaliado, Arthur substituto, Paulinho tendência de não ter condições), worldofsports (25/11, idem).
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'LIBERTADORES  ·  FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "Piquerez joga a final? O Palmeiras já está em Montevidéu.",
    "A delegação chegou ao Uruguai na noite desta quarta.",
    "Piquerez fez parte do treino com o grupo... mas será reavaliado.",
    "Paulinho foi relacionado, mas a tendência... é não jogar.",
    "Se Piquerez não puder, quem entra é... Arthur.",
    "Sábado, às cinco da tarde... a final contra o Estudiantes.",
]
CAPTXT = [
    "Piquerez joga a final? O Palmeiras|já está em Montevidéu.",
    "A delegação chegou ao Uruguai|na noite desta quarta.",
    "Piquerez fez parte do treino com o grupo...|mas será reavaliado.",
    "Paulinho foi relacionado,|mas a tendência... é não jogar.",
    "Se Piquerez não puder,|quem entra é... Arthur.",
    "Sábado, às 17h...|a final contra o Estudiantes.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "PIQUEREZ JOGA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Piquerez', 4), (0, 'final', 4), (0, 'Montevideu', 4), (1, 'chegou', 4), (1, 'Uruguai', 4), (1, 'noite', 4),
         (1, 'quarta', 4), (2, 'Piquerez', 4), (2, 'treino', 4), (2, 'reavaliado', 4), (3, 'Paulinho', 4), (3, 'relacionado', 4),
         (3, 'jogar', 4), (4, 'Piquerez', 4), (4, 'Arthur', 4), (5, 'Sabado', 4), (5, 'cinco', 4), (5, 'final', 4),
         (5, 'Estudiantes', 4)]

PAL, PAL_F = time_('PALMEIRAS')
EST, EST_F = time_('ESTUDIANTES')
VERDE = '#1b6b3a'
TORC = dict(roupa=VERDE, pele='#e0ac85', cabelo='#2a1a10')


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def est(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=EST, faixa=EST_F, **kw)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor preocupado + série + pergunta; depois telão com MONTEVIDÉU."""
    if f < CLOSE_F:
        c = vestiario(PAL, PAL_F).copy()
        c = put_close(c, f, expr='preocupado', s=.9, look=0, **TORC)
        num(c, 'BASTIDORES', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 3', 621, 430, f, 0, 100, 2)
        num(c, 'PIQUEREZ', 621, 1350, f, 0, 150, -2)
        num(c, 'JOGA?', 621, 1530, f, 0, 170, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'golden'
    c = telao('dusk').copy()
    mo = wt(0, 'Montevideu') - 3
    pal(c, 420, 2080, 860, f, 4, num_='6', arms='point' if f < mo else 'up', expr='stern' if f < mo else 'grin', look=1)
    pal(c, 920, 2020, 700, f, 6, num_='9', skin=3, hair='#151010', arms='cintura' if f < mo else 'punho',
        expr='neutral' if f < mo else 'grin', flip=True, look=-1)
    if f < mo - 2:
        telao_txt(c, [('PALMEIRAS', 160)], f, CLOSE_F, y=760)
    else:
        telao_txt(c, [('MONTEVIDÉU', 150)], f, mo, y=760)
    z = lerp(1.16, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, mo, 10))
    k = kick(f, mo if f >= mo else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio à noite: dois jogadores chegando (andando), URUGUAI e depois QUARTA À NOITE."""
    c = estadio2('dusk').copy()
    ur = wt(1, 'Uruguai') - 3; no = wt(1, 'noite') - 3
    andando = f < ur + 20
    ph = (f * .06) % 1 if andando else None
    x1 = lerp(250, 420, easeOut(ramp(f, 0, ur + 20)))
    pal(c, x1, 2060, 840, f, 2, num_='10', run=ph, arms='hang' if andando else 'joinha',
        expr='neutral' if f < ur else 'grin', look=1 if f < no else 0)
    pal(c, x1 + 480, 2000, 700, f, 8, num_='5', skin=4, hair='#151010', run=((f * .06) + .5) % 1 if andando else None,
        arms='hang' if andando else 'cintura', expr='neutral' if f < no else 'proud', look=-1)
    if f < no - 2:
        if f >= ur: num(c, 'URUGUAI', 640, 860, f, ur, 170, -3)
    else:
        num(c, 'QUARTA À NOITE', 640, 860, f, no, 96, 3)
    z = lerp(1.14, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, no, 10))
    k = kick(f, no if f >= no else max(ur, 0), .6)
    return c, (lerp(580, 700, smooth(f / 120)), 1420 + k * 8, z, k), 'dusk'


def s2(f):
    """estádio de dia (treino): Piquerez conduz a bola; na palavra reavaliado ele para preocupado."""
    c = estadio2('day').copy()
    pq = wt(2, 'Piquerez') - 3; re = wt(2, 'reavaliado') - 3
    corre = f < re
    H = 860
    x = lerp(300, 640, easeOut(ramp(f, 0, re)))
    if corre: linhas_vel(c, x, 2040, H, f, dir=-1)
    pal(c, x, 2040, H, f, 3, num_='22', skin=1, hair='#3a2a1e', run=(f * .1) % 1 if corre else None,
        arms='run' if corre else 'cintura', expr='stern' if corre else 'nervous', look=1 if corre else 0)
    rb = raio_bola(H)
    put_bola(c, x + H * .18 + 20, 2040 - rb, rb, f)
    if f < re - 2:
        put_placa(c, 'PIQUEREZ', PAL, 640, 1000, f, max(pq, 0), 100, -3)
    else:
        num(c, 'REAVALIADO', 640, 1000, f, re, 108, 3)
    z = lerp(1.3, 1.18, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, re, 10))
    k = kick(f, re if f >= re else 0, .7)
    return c, (lerp(560, 680, smooth(f / 120)), 1480 + k * 8, z, k), 'day'


def s3(f):
    """vestiário: Paulinho com a mão na cintura, triste; placa e depois FORA?."""
    c = vestiario(PAL, PAL_F).copy()
    pa = wt(3, 'Paulinho') - 3; jo = wt(3, 'jogar') - 3; te = wt(3, 'tendencia') - 3
    pal(c, 640, 2090, 880, f, 7, num_='10', skin=2, hair='#151010', arms='hang' if f < te else 'cintura',
        expr='neutral' if f < te else ('nervous' if f < jo else 'pained'), look=-1 if f < te else 0)
    if f < jo - 2:
        put_placa(c, 'PAULINHO', PAL, 640, 860, f, max(pa, 0), 100, -2)
    else:
        num(c, 'FORA?', 640, 860, f, jo, 190, 3)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, jo, 10))
    k = kick(f, jo if f >= jo else 0, .7)
    return c, (640 - 20 * math.sin(f * .04), 1380 + k * 8, z, k), 'day'


def s4(f):
    """prancheta: ímã do Piquerez na lateral esquerda sai, entra o ímã do Arthur (seta)."""
    c = prancheta().copy()
    pq = wt(4, 'Piquerez') - 3; ar = wt(4, 'Arthur') - 3
    # zaga e meio para dar contexto
    for i, (x, y) in enumerate([(470, 1600), (640, 1640), (810, 1600), (520, 1330), (760, 1330)]):
        pino(c, x, y, PAL, f, 2 + i * 2, '', 60)
    if f < ar:
        pu = wt(4, 'puder') - 3
        tre = 10 * math.sin(f * .9) * ramp(f, pu, pu + 4)
        pino(c, 300 + tre, 1450, PAL, f, max(pq, 0), '6', 80 + int(14 * pulse(f, pu, 10)))
    else:
        seta(c, (220, 1800), (290, 1500), f, ar - 6, 10)
        pino(c, 300, 1450, ('#ffd84a', '#ffffff', '#ffffff'), f, ar, 'A', 90)
    if f < ar - 2:
        num(c, 'PIQUEREZ?', 640, 860, f, max(pq, 0), 130, -3)
    else:
        num(c, 'ARTHUR', 640, 860, f, ar, 180, 3)
    en = wt(4, 'entra') - 3
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .003 * f) * (1 + .12 * pulse(f, ar, 10)) * (1 + .1 * pulse(f, en, 12))
    k = kick(f, ar if f >= ar else (en if f >= en else 0), .8)
    return c, (lerp(560, 700, smooth(f / 95)), 1300 + k * 8 + lerp(60, -40, smooth(f / 95)), z,
               lerp(-2, 2, smooth(f / 95)) + k), 'day'


def s5(f):
    """close do torcedor: curioso com a data, sorriso na final contra o Estudiantes."""
    c = conta_bg().copy()
    paste_c(c, trofeu(), 640, 1380, .9)
    sa = wt(5, 'Sabado') - 3; ci = wt(5, 'cinco') - 3; fi = wt(5, 'final') - 3; es = wt(5, 'Estudiantes') - 3
    c = put_close(c, f, expr='curioso' if f < fi else 'sorriso', s=.95, look=(1 if f < ci else -1) if f < fi else 0, **TORC)
    if f < ci - 2:
        num(c, 'SÁBADO', 621, 720, f, max(sa, 0), 150, -2)
    elif f < fi - 2:
        num(c, '17H', 621, 720, f, ci, 170, 2)
    elif f < es - 2:
        num(c, 'FINAL', 621, 720, f, fi, 170, -2)
    else:
        put_placa(c, 'ESTUDIANTES', EST, 621, 720, f, es, 100, 2)
    z = (1.04 + .002 * f) * (1 + .08 * pulse(f, fi, 10))
    return c, (621, 1104, z, kick(f, fi, .5)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'Montevideu') - 3, 150, .9)
    s.thunk(s.W(1, 'Uruguai') - 3, 140, .8)
    s.thunk(s.W(1, 'noite') - 3, 150, .9)
    s.thunk(s.W(2, 'Piquerez') - 3, 130, .8)
    s.chute(s.W(2, 'treino') - 3)
    s.thunk(s.W(2, 'reavaliado') - 3, 150, .9)
    s.thunk(s.W(3, 'Paulinho') - 3, 140, .8)
    s.thunk(s.W(3, 'jogar') - 3, 150, .9)
    s.thunk(s.W(4, 'Piquerez') - 3, 130, .8)
    s.ting(s.W(4, 'Arthur') - 3, .35)
    s.thunk(s.W(4, 'Arthur') - 3, 160, 1.0)
    s.thunk(s.W(5, 'Sabado') - 3, 140, .8)
    s.thunk(s.W(5, 'cinco') - 3, 150, .9)
    s.apito(s.W(5, 'final') - 4)
    s.thunk(s.W(5, 'Estudiantes') - 3, 150, .9)
