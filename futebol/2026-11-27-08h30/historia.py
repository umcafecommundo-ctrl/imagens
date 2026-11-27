"""anima.futebol — 27/11/2026 08h30 — BASTIDORES · EP. 4 — Palmeiras treina em Montevidéu: Vitor Roque começa a final?
Fontes (conferidas em 27/11/2026, ver fatos.txt): Portal do Palestra (26/11 08h04, treino quinta 16h no CT do Albion, três
zagueiros, Piquerez ou Arthur), Palmeiras Todo Dia (26/11 19h01, 1º treino em Montevidéu na tarde de quinta no CT do Albion,
opções de escalação), ESPN (26/11 13h35 e 22h36, três zagueiros, trio Flaco López, Arias e Vitor Roque, Piquerez/Arthur,
final sábado 17h no Centenário).
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
    "Vitor Roque começa a final? O Palmeiras já treinou em Montevidéu.",
    "O primeiro treino no Uruguai foi nesta quinta, no CT do Albion.",
    "Abel deve manter três zagueiros... Murilo, Gómez e Barboza.",
    "No ataque, Vitor Roque deve se juntar a Arias e Flaco López.",
    "A dúvida segue na ala esquerda: Piquerez ou... Arthur.",
    "Sábado, às cinco da tarde, no Centenário... é a final.",
]
CAPTXT = [
    "Vitor Roque começa a final?|O Palmeiras já treinou em Montevidéu.",
    "O primeiro treino no Uruguai foi|nesta quinta, no CT do Albion.",
    "Abel deve manter três zagueiros...|Murilo, Gómez e Barboza.",
    "No ataque, Vitor Roque deve se juntar|a Arias e Flaco López.",
    "A dúvida segue na ala esquerda:|Piquerez ou... Arthur.",
    "Sábado, às 17h, no Centenário...|é a final.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "ROQUE TITULAR?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 3
FLASH = [3]
CHECK = [(0, 'Roque', 4), (0, 'final', 4), (0, 'Montevideu', 4), (1, 'treino', 4), (1, 'Uruguai', 4), (1, 'quinta', 4),
         (1, 'Albion', 4), (2, 'tres', 4), (2, 'Murilo', 4), (2, 'Gomez', 4), (2, 'Barboza', 4), (3, 'Roque', 4),
         (3, 'Arias', 4), (3, 'Flaco', 4), (4, 'esquerda', 4), (4, 'Piquerez', 4), (4, 'Arthur', 4), (5, 'Sabado', 4),
         (5, 'cinco', 4), (5, 'Centenario', 4), (5, 'final', 4)]

PAL, PAL_F = time_('PALMEIRAS')
EST, EST_F = time_('ESTUDIANTES')
VERDE = '#1b6b3a'
TORC = dict(roupa=VERDE, pele='#e0ac85', cabelo='#2a1a10')


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor em choque + série + pergunta; depois telão com MONTEVIDÉU."""
    if f < CLOSE_F:
        c = vestiario(PAL, PAL_F).copy()
        c = put_close(c, f, expr='choque', s=.9, look=0, **TORC)
        num(c, 'BASTIDORES', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 4', 621, 430, f, 0, 100, 2)
        num(c, 'ROQUE', 621, 1350, f, 0, 170, -2)
        num(c, 'TITULAR?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'golden'
    c = telao('dusk').copy()
    mo = wt(0, 'Montevideu') - 3
    pal(c, 420, 2080, 860, f, 4, num_='9', skin=3, hair='#151010', arms='point' if f < mo else 'up',
        expr='stern' if f < mo else 'grin', look=1)
    pal(c, 920, 2020, 700, f, 6, num_='7', arms='cintura' if f < mo else 'punho',
        expr='neutral' if f < mo else 'grin', flip=True, look=-1)
    if f < mo - 2:
        telao_txt(c, [('PALMEIRAS', 160)], f, CLOSE_F, y=760)
    else:
        telao_txt(c, [('MONTEVIDÉU', 150)], f, mo, y=760)
    z = lerp(1.16, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, mo, 10))
    k = kick(f, mo if f >= mo else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


def s1(f):
    """campo de treino de dia: dois jogadores correndo no treino; QUINTA e depois CT DO ALBION."""
    c = estadio2('day').copy()
    qu = wt(1, 'quinta') - 3; al = wt(1, 'Albion') - 3
    H = 840
    x1 = lerp(260, 470, easeOut(ramp(f, 0, al)))
    corre = f < al
    if corre: linhas_vel(c, x1, 2060, H, f, dir=-1)
    pal(c, x1, 2060, H, f, 2, num_='10', run=(f * .1) % 1 if corre else None, arms='run' if corre else 'joinha',
        expr='stern' if f < qu else 'grin', look=1 if f < al else 0)
    rb = raio_bola(H)
    put_bola(c, x1 + H * .18 + 20, 2060 - rb, rb, f)
    pal(c, x1 + 470, 2000, 700, f, 8, num_='5', skin=4, hair='#151010', run=((f * .1) + .5) % 1 if corre else None,
        arms='run' if corre else 'cintura', expr='neutral' if f < al else 'proud', look=-1)
    if f < al - 2:
        if f >= qu: num(c, 'QUINTA', 640, 900, f, qu, 170, -3)
    else:
        num(c, 'CT DO ALBION', 640, 900, f, al, 92, 2)
    z = lerp(1.14, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, al, 10))
    k = kick(f, al if f >= al else max(qu, 0), .6)
    return c, (lerp(600, 660, smooth(f / 120)), 1440 + k * 8, z, k), 'day'


def s2(f):
    """prancheta: três pinos da zaga entram um a um (M, G, B) e o texto 3 ZAGUEIROS."""
    c = prancheta().copy()
    tr = wt(2, 'tres') - 3
    mu = wt(2, 'Murilo') - 3; go = wt(2, 'Gomez') - 3; ba = wt(2, 'Barboza') - 3
    pino(c, 300, 1280, PAL, f, 0, '', 60)
    pino(c, 980, 1280, PAL, f, 0, '', 60)
    for x, y, k0, r in [(420, 1440, mu, 'M'), (640, 1490, go, 'G'), (860, 1440, ba, 'B')]:
        if f >= k0: pino(c, x, y, PAL, f, k0, r, 95)
    if f >= tr - 2:
        num(c, '3 ZAGUEIROS', 640, 900, f, max(tr, 0), 104, -2)
    z = lerp(1.06, .96, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .08 * pulse(f, mu, 10)) * (1 + .08 * pulse(f, ba, 10))
    k = kick(f, ba if f >= ba else (go if f >= go else (mu if f >= mu else 0)), .7)
    return c, (lerp(600, 680, f / 125) + 12 * math.sin(f * .07), 1320 + k * 8 - 1.2 * f, z * (1 + .0015 * f), lerp(-2, 2, f / 125) + k), 'day'


def s3(f):
    """estádio à noite: Vitor Roque em velocidade com a bola, placa e depois o trio."""
    c = estadio2('dusk').copy()
    ro = wt(3, 'Roque') - 3; ar = wt(3, 'Arias') - 3; fl = wt(3, 'Flaco') - 3
    H = 860
    x = lerp(280, 600, easeOut(ramp(f, 0, ar)))
    corre = f < ar
    if corre: linhas_vel(c, x, 2040, H, f, dir=-1)
    pal(c, x, 2040, H, f, 9, num_='9', skin=3, hair='#151010', run=(f * .12) % 1 if corre else None,
        arms='run' if corre else 'up', expr='stern' if corre else 'grin', look=1 if corre else 0)
    rb = raio_bola(H)
    if corre: put_bola(c, x + H * .18 + 20, 2040 - rb, rb, f)
    if f >= ar:
        pal(c, 250, 1960, 640, f, 3, num_='11', skin=2, arms='punho', expr='grin', look=1)
        pal(c, 1000, 1960, 640, f, 5, num_='42', skin=1, hair='#3a2a1e', arms='up', expr='grin', flip=True, look=-1)
    if f < ar - 2:
        put_placa(c, 'VITOR ROQUE', PAL, 640, 900, f, max(ro, 0), 96, -3)
    else:
        num(c, 'TRIO', 640, 900, f, ar, 190, 3)
    z = lerp(1.28, 1.08, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ar, 10)) * (1 + .06 * pulse(f, fl, 10))
    k = kick(f, ar if f >= ar else max(ro, 0), .7)
    return c, (lerp(560, 660, smooth(f / 110)), 1440 + k * 8, z, k), 'dusk'


def s4(f):
    """vestiário: lateral com a mão na cintura (dúvida); PIQUEREZ? e depois ARTHUR."""
    c = vestiario(PAL, PAL_F).copy()
    es = wt(4, 'esquerda') - 3; pq = wt(4, 'Piquerez') - 3; ar = wt(4, 'Arthur') - 3
    if f < ar:
        pal(c, 640, 2100, 1050, f, 7, num_='22', skin=1, hair='#3a2a1e', arms='hang' if f < pq else 'cintura',
            expr='neutral' if f < pq else 'nervous', look=-1 if f < pq else 1)
    else:
        pal(c, 640, 2100, 1050, f, 11, num_='6', skin=2, hair='#151010', arms='joinha', expr='grin', look=0)
    if f < pq - 2:
        if f >= es: num(c, 'ALA ESQUERDA', 640, 860, f, es, 110, -2)
    elif f < ar - 2:
        num(c, 'PIQUEREZ?', 640, 860, f, pq, 140, 3)
    else:
        num(c, 'ARTHUR?', 640, 860, f, ar, 170, -3)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ar, 10))
    k = kick(f, ar if f >= ar else max(pq, 0), .7)
    return c, (640 - 20 * math.sin(f * .04), 1420 + k * 8, z, k), 'day'


def s5(f):
    """close do torcedor: curioso com a data, sorriso na final."""
    c = conta_bg().copy()
    paste_c(c, trofeu(), 640, 1380, .9)
    sa = wt(5, 'Sabado') - 3; ci = wt(5, 'cinco') - 3; ce = wt(5, 'Centenario') - 3; fi = wt(5, 'final') - 3
    c = put_close(c, f, expr='curioso' if f < fi else 'sorriso', s=.95, look=(1 if f < ci else -1) if f < fi else 0, **TORC)
    if f < ci - 2:
        num(c, 'SÁBADO', 621, 720, f, max(sa, 0), 150, -2)
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
    s.thunk(s.W(0, 'Montevideu') - 3, 150, .9)
    s.apito(s.W(1, 'treino') - 3)
    s.thunk(s.W(1, 'quinta') - 3, 140, .8)
    s.thunk(s.W(1, 'Albion') - 3, 150, .9)
    s.thunk(s.W(2, 'tres') - 3, 140, .8)
    s.thunk(s.W(2, 'Murilo') - 3, 130, .8)
    s.thunk(s.W(2, 'Gomez') - 3, 130, .8)
    s.thunk(s.W(2, 'Barboza') - 3, 150, .9)
    s.thunk(s.W(3, 'Roque') - 3, 140, .8)
    s.chute(s.W(3, 'Arias') - 5)
    s.ting(s.W(3, 'Arias') - 3, .35)
    s.thunk(s.W(3, 'Flaco') - 3, 150, .9)
    s.thunk(s.W(4, 'esquerda') - 3, 130, .8)
    s.thunk(s.W(4, 'Piquerez') - 3, 140, .8)
    s.thunk(s.W(4, 'Arthur') - 3, 160, 1.0)
    s.thunk(s.W(5, 'Sabado') - 3, 140, .8)
    s.thunk(s.W(5, 'cinco') - 3, 150, .9)
    s.thunk(s.W(5, 'Centenario') - 3, 140, .8)
    s.apito(s.W(5, 'final') - 4)
