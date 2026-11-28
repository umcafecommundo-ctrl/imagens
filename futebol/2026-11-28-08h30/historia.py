"""anima.futebol — 28/11/2026 08h30 — BASTIDORES · EP. 5 — Último treino: Murilo e Piquerez de volta. Piquerez joga a final?
Fontes (conferidas em 28/11/2026, ver fatos.txt): Gazeta Esportiva (27/11 19h01, Palmeiras encerra preparação com dois
reforços: Murilo e Piquerez treinaram com o elenco na tarde de sexta no CT do Albion, lesões na coxa, Murilo com mais chance),
Nosso Palestra (27/11 19h03, Murilo e Piquerez participaram do treino de sexta, provável Murilo, Gómez e Barboza, final sábado
17h no Centenário).
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
    "Piquerez joga a final? O Palmeiras ganhou dois reforços.",
    "No último treino, nesta sexta, Murilo e Piquerez treinaram com o elenco.",
    "Os dois estavam fora por lesão muscular... na coxa.",
    "Murilo tem mais chance de começar, com Gómez e Barboza.",
    "Na ala esquerda, a dúvida segue: Piquerez ou... Arthur.",
    "Hoje, às cinco da tarde, no Centenário... é a final.",
]
CAPTXT = [
    "Piquerez joga a final?|O Palmeiras ganhou dois reforços.",
    "No último treino, nesta sexta, Murilo|e Piquerez treinaram com o elenco.",
    "Os dois estavam fora|por lesão muscular... na coxa.",
    "Murilo tem mais chance de começar,|com Gómez e Barboza.",
    "Na ala esquerda, a dúvida segue:|Piquerez ou... Arthur.",
    "Hoje, às 17h, no Centenário...|é a final.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "PIQUEREZ JOGA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 1
FLASH = [1]
CHECK = [(0, 'Piquerez', 4), (0, 'final', 4), (0, 'reforcos', 4), (1, 'treino', 4), (1, 'sexta', 4), (1, 'Murilo', 4),
         (1, 'Piquerez', 4), (1, 'elenco', 4), (2, 'lesao', 4), (2, 'coxa', 4), (3, 'Murilo', 4), (3, 'Gomez', 4),
         (3, 'Barboza', 4), (4, 'esquerda', 4), (4, 'Piquerez', 4), (4, 'Arthur', 4), (5, 'Hoje', 4), (5, 'cinco', 4),
         (5, 'Centenario', 4), (5, 'final', 4)]

PAL, PAL_F = time_('PALMEIRAS')
VERDE = '#1b6b3a'
TORC = dict(roupa=VERDE, pele='#e0ac85', cabelo='#2a1a10')


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor em choque + série + pergunta; depois telão com 2 REFORÇOS."""
    if f < CLOSE_F:
        c = vestiario(PAL, PAL_F).copy()
        c = put_close(c, f, expr='choque', s=.9, look=0, **TORC)
        num(c, 'BASTIDORES', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 5', 621, 430, f, 0, 100, 2)
        num(c, 'PIQUEREZ', 621, 1350, f, 0, 160, -2)
        num(c, 'JOGA?', 621, 1530, f, 0, 170, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'golden'
    c = telao('dusk').copy()
    re = wt(0, 'reforcos') - 3
    pal(c, 420, 2080, 860, f, 4, num_='26', skin=3, hair='#151010', arms='point' if f < re else 'up',
        expr='neutral' if f < re else 'grin', look=1)
    pal(c, 920, 2020, 700, f, 6, num_='22', arms='cintura' if f < re else 'punho',
        expr='neutral' if f < re else 'grin', flip=True, look=-1)
    if f < re - 2:
        telao_txt(c, [('PALMEIRAS', 160)], f, CLOSE_F, y=760)
    else:
        telao_txt(c, [('2 REFORÇOS', 118)], f, re, y=760)
    z = lerp(1.16, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, re, 10))
    k = kick(f, re if f >= re else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


def s1(f):
    """campo de treino de dia: os dois correm no treino; ÚLTIMO TREINO, MURILO, PIQUEREZ."""
    c = estadio2('day').copy()
    tr = wt(1, 'treino') - 3; mu = wt(1, 'Murilo') - 3; pq = wt(1, 'Piquerez') - 3; el = wt(1, 'elenco') - 3
    H = 840
    x1 = lerp(260, 470, easeOut(ramp(f, 0, el)))
    corre = f < el
    if corre: linhas_vel(c, x1, 2060, H, f, dir=-1)
    pal(c, x1, 2060, H, f, 2, num_='26', skin=3, hair='#151010', run=(f * .1) % 1 if corre else None,
        arms='run' if corre else 'joinha', expr='stern' if f < mu else 'grin', look=1 if f < el else 0)
    rb = raio_bola(H)
    put_bola(c, x1 + H * .18 + 20, 2060 - rb, rb, f)
    pal(c, x1 + 470, 2000, 720, f, 8, num_='22', skin=1, hair='#3a2a1e', run=((f * .1) + .5) % 1 if corre else None,
        arms='run' if corre else 'up', expr='neutral' if f < pq else 'grin', look=-1)
    if f < mu - 2:
        if f >= tr: num(c, 'ÚLTIMO TREINO', 640, 900, f, tr, 104, -3)
    elif f < pq - 2:
        put_placa(c, 'MURILO', PAL, 640, 900, f, mu, 110, -3)
    else:
        put_placa(c, 'PIQUEREZ', PAL, 640, 900, f, pq, 110, 3)
    z = lerp(1.14, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, mu, 10)) * (1 + .1 * pulse(f, pq, 10))
    k = kick(f, pq if f >= pq else (mu if f >= mu else max(tr, 0)), .6)
    return c, (lerp(600, 660, smooth(f / 120)), 1440 + k * 8, z, k), 'day'


def s2(f):
    """vestiário: jogador com a mão na cintura, preocupado -> LESÃO -> NA COXA."""
    c = vestiario(PAL, PAL_F).copy()
    le = wt(2, 'lesao') - 3; cx = wt(2, 'coxa') - 3
    pal(c, 640, 2100, 1050, f, 7, num_='22', skin=1, hair='#3a2a1e', arms='hang' if f < le else 'cintura',
        expr='neutral' if f < le else ('nervous' if f < cx else 'pained'), look=-1 if f < cx else 1)
    if f < cx - 2:
        if f >= le: num(c, 'LESÃO', 640, 860, f, le, 170, -2)
    else:
        num(c, 'NA COXA', 640, 860, f, cx, 160, 3)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, cx, 10))
    k = kick(f, cx if f >= cx else max(le, 0), .7)
    return c, (640 - 20 * math.sin(f * .04), 1420 + k * 8, z, k), 'day'


def s3(f):
    """telão à noite: Murilo de braço erguido; MURILO e depois o trio no telão."""
    c = telao('day').copy()
    mu = wt(3, 'Murilo') - 3; go = wt(3, 'Gomez') - 3; ba = wt(3, 'Barboza') - 3
    pal(c, 640, 2100, 900, f, 9, num_='26', skin=3, hair='#151010', arms='hang' if f < go else 'up',
        expr='stern' if f < go else 'grin', look=0)
    if f >= go:
        pal(c, 240, 2000, 640, f, 3, num_='15', skin=2, arms='punho', expr='grin', look=1)
    if f >= ba:
        pal(c, 1040, 2000, 640, f, 5, num_='3', skin=4, hair='#151010', arms='punho', expr='grin', flip=True, look=-1)
    if f < go - 2:
        telao_txt(c, [('MURILO', 170)], f, max(mu, 0), y=760)
    else:
        telao_txt(c, [('3 ZAGUEIROS', 110)], f, go, y=760)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .08 * pulse(f, go, 10)) * (1 + .08 * pulse(f, ba, 10))
    k = kick(f, ba if f >= ba else (go if f >= go else max(mu, 0)), .7)
    return c, (lerp(600, 680, f / 110), 1420 + k * 8, z, k), 'day'


def s4(f):
    """estádio à noite: lateral em velocidade pela esquerda; PIQUEREZ? e depois ARTHUR?"""
    c = estadio2('dusk').copy()
    es = wt(4, 'esquerda') - 3; pq = wt(4, 'Piquerez') - 3; ar = wt(4, 'Arthur') - 3
    H = 860
    x = lerp(280, 600, easeOut(ramp(f, 0, ar)))
    corre = f < ar
    if corre: linhas_vel(c, x, 2040, H, f, dir=-1)
    if f < ar:
        pal(c, x, 2040, H, f, 11, num_='22', skin=1, hair='#3a2a1e', run=(f * .12) % 1 if corre else None,
            arms='run', expr='stern', look=1)
    else:
        pal(c, x, 2040, H, f, 12, num_='6', skin=2, hair='#151010', arms='joinha', expr='grin', look=0)
    rb = raio_bola(H)
    if corre: put_bola(c, x + H * .18 + 20, 2040 - rb, rb, f)
    if f < pq - 2:
        if f >= es: num(c, 'ALA ESQUERDA', 640, 900, f, es, 110, -2)
    elif f < ar - 2:
        num(c, 'PIQUEREZ?', 640, 900, f, pq, 140, 3)
    else:
        num(c, 'ARTHUR?', 640, 900, f, ar, 170, -3)
    z = lerp(1.28, 1.08, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ar, 10)) * (1 + .06 * pulse(f, pq, 10))
    k = kick(f, ar if f >= ar else max(pq, 0), .7)
    return c, (lerp(560, 660, smooth(f / 110)), 1440 + k * 8, z, k), 'dusk'


def s5(f):
    """close do torcedor: curioso com a hora, sorriso na final."""
    c = conta_bg().copy()
    paste_c(c, trofeu(), 640, 1380, .9)
    ho = wt(5, 'Hoje') - 3; ci = wt(5, 'cinco') - 3; ce = wt(5, 'Centenario') - 3; fi = wt(5, 'final') - 3
    c = put_close(c, f, expr='curioso' if f < fi else 'sorriso', s=.95, look=(1 if f < ci else -1) if f < fi else 0, **TORC)
    if f < ci - 2:
        num(c, 'HOJE', 621, 720, f, max(ho, 0), 170, -2)
    elif f < ce - 2:
        num(c, '17H', 621, 720, f, ci, 170, 2)
    elif f < fi - 2:
        num(c, 'CENTENÁRIO', 621, 720, f, ce, 120, -2)
    else:
        num(c, 'FINAL', 621, 720, f, fi, 180, 2)
    z = (1.04 + .002 * f) * (1 + .08 * pulse(f, fi, 10)) * (1 + .06 * pulse(f, ce, 10))
    return c, (621, 1104, z, kick(f, fi, .5)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'reforcos') - 3, 150, .9)
    s.apito(s.W(1, 'treino') - 3)
    s.thunk(s.W(1, 'Murilo') - 3, 140, .8)
    s.thunk(s.W(1, 'Piquerez') - 3, 150, .9)
    s.ting(s.W(1, 'elenco') - 3, .35)
    s.thunk(s.W(2, 'lesao') - 3, 130, .8)
    s.thunk(s.W(2, 'coxa') - 3, 150, .9)
    s.thunk(s.W(3, 'Murilo') - 3, 140, .8)
    s.thunk(s.W(3, 'Gomez') - 3, 130, .8)
    s.thunk(s.W(3, 'Barboza') - 3, 150, .9)
    s.thunk(s.W(4, 'esquerda') - 3, 130, .8)
    s.chute(s.W(4, 'Piquerez') - 5)
    s.thunk(s.W(4, 'Piquerez') - 3, 140, .8)
    s.thunk(s.W(4, 'Arthur') - 3, 160, 1.0)
    s.thunk(s.W(5, 'Hoje') - 3, 140, .8)
    s.thunk(s.W(5, 'cinco') - 3, 150, .9)
    s.thunk(s.W(5, 'Centenario') - 3, 140, .8)
    s.apito(s.W(5, 'final') - 4)
