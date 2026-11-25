"""anima.futebol — 25/11/2026 08h30 — BASTIDORES · EP. 2 — Palmeiras embarca para a final da Libertadores em Montevidéu.
Fontes (conferidas em 25/11/2026, ver fatos.txt): Sportbuzz (24/11, embarque na quarta, final de 2025 perdida para o Flamengo),
Portal do Palestra (24/11, embarque quarta, final sábado 17h no Centenário, Paulinho e Piquerez em tratamento, busca a 4ª),
Terra (23/11, final 28/11 17h, Paulinho sem previsão, Piquerez cronograma individual, quarto título).
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
    "O Palmeiras vai ser tetra? A viagem para a final começa hoje.",
    "O elenco embarca nesta quarta para Montevidéu, no Uruguai.",
    "Sábado, às cinco da tarde, a final... contra o Estudiantes.",
    "Mas Paulinho e Piquerez ainda estão em tratamento.",
    "O Palmeiras tem três Libertadores... e busca a quarta.",
    "Ano passado perdeu a final. Agora vem o tetra?",
]
CAPTXT = [
    "O Palmeiras vai ser tetra?|A viagem para a final começa hoje.",
    "O elenco embarca nesta quarta|para Montevidéu, no Uruguai.",
    "Sábado, às 17h, a final...|contra o Estudiantes.",
    "Mas Paulinho e Piquerez ainda|estão em tratamento.",
    "O Palmeiras tem 3 Libertadores...|e busca a quarta.",
    "Ano passado perdeu a final.|Agora vem o tetra?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "VAI SER TETRA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [2]
CHECK = [(0, 'tetra', 4), (0, 'hoje', 4), (1, 'embarca', 4), (1, 'Montevideu', 4), (1, 'Uruguai', 4),
         (2, 'Sabado', 4), (2, 'cinco', 4), (2, 'final', 4), (2, 'Estudiantes', 4), (3, 'Paulinho', 4), (3, 'Piquerez', 4),
         (3, 'tratamento', 4), (4, 'tres', 4), (4, 'quarta', 4), (5, 'perdeu', 4), (5, 'tetra', 4)]

PAL, PAL_F = time_('PALMEIRAS')
EST, EST_F = time_('ESTUDIANTES')
VERDE = '#1b6b3a'


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def est(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=EST, faixa=EST_F, **kw)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor do Palmeiras + série + pergunta; depois vestiário com o elenco animado."""
    if f < CLOSE_F:
        c = estadio2('golden').copy()
        c = put_close(c, f, expr='sorriso', s=.9, roupa=VERDE, pele='#e0ac85', cabelo='#2a1a10', look=0)
        num(c, 'BASTIDORES', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 2', 621, 430, f, 0, 100, 2)
        num(c, 'VAI SER', 621, 1350, f, 0, 150, -2)
        num(c, 'TETRA?', 621, 1530, f, 0, 170, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'golden'
    c = vestiario(PAL, PAL_F).copy()
    ho = wt(0, 'hoje') - 3
    pal(c, 400, 2070, 840, f, 4, num_='9', arms='point' if f < ho else 'up', expr='stern' if f < ho else 'grin', look=1)
    pal(c, 900, 2000, 660, f, 6, num_='15', skin=3, hair='#151010', arms='cintura' if f < ho else 'punho',
        expr='neutral' if f < ho else 'grin', flip=True)
    if f < ho - 2:
        put_placa(c, 'PALMEIRAS', PAL, 640, 880, f, CLOSE_F, 100, -3)
    else:
        num(c, 'HOJE', 640, 880, f, ho, 190, 3)
    z = lerp(1.18, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ho, 10))
    k = kick(f, ho if f >= ho else CLOSE_F, .7)
    return c, (640, 1420 + k * 10, z, k), 'day'


def s1(f):
    """prancheta como mapa: pino de São Paulo, seta até o pino de Montevidéu."""
    c = prancheta().copy()
    em = wt(1, 'embarca') - 3; mo = wt(1, 'Montevideu') - 3; ur = wt(1, 'Uruguai') - 3
    a = (330, 1050); b = (880, 1520)
    pino(c, a[0], a[1], PAL, f, 0, 'SP', 90)
    seta(c, (a[0] + 50, a[1] + 50), (b[0] - 60, b[1] - 60), f, em, 16)
    pino(c, b[0], b[1], ('#3a8fd6', '#ffffff', '#ffffff'), f, mo, 'MVD', 90)
    if f < mo - 2:
        num(c, 'EMBARQUE', 640, 800, f, em, 140, -3)
    elif f < ur - 2:
        num(c, 'MONTEVIDÉU', 640, 800, f, mo, 120, 3)
    else:
        num(c, 'URUGUAI', 640, 800, f, ur, 150, -2)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, mo, 10))
    k = kick(f, mo if f >= mo else em, .7)
    return c, (640 + 14 * math.sin(f * .06), 1330 + k * 8, z, lerp(0, 1.5, smooth(ramp(f, 0, 60)))), 'day'


def s2(f):
    """estádio ao entardecer: calendário de sábado, depois Palmeiras x Estudiantes frente a frente."""
    c = estadio2('dusk').copy()
    sa = wt(2, 'Sabado') - 3; ci = wt(2, 'cinco') - 3; fi = wt(2, 'final') - 3; es = wt(2, 'Estudiantes') - 3
    pal(c, 380, 2060, 840, f, 2, num_='10', arms='cintura' if f < fi else 'point', expr='stern', look=1)
    est(c, 900, 2020, 760, f, 5, num_='9', arms='hang' if f < es else 'cintura', expr='neutral' if f < es else 'stern',
        flip=True, look=-1)
    if f < ci - 2:
        if f >= sa: paste_c(c, calendario('28', 'NOV'), 640, 900, .6 * back(ramp(f, sa, sa + 8)))
    elif f < fi - 2:
        num(c, '17H', 640, 880, f, ci, 190, -3)
    elif f < es - 2:
        num(c, 'FINAL', 640, 880, f, fi, 170, 3)
    else:
        put_placa(c, 'ESTUDIANTES', EST, 640, 880, f, es, 100, -2)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, fi, 10))
    k = kick(f, fi if f >= fi else sa, .8)
    return c, (lerp(600, 680, smooth(f / 120)), 1440 + k * 10, z, k), 'dusk'


def s3(f):
    """telão: os dois nomes em tratamento; jogador preocupado na frente."""
    c = telao('day').copy()
    pa = wt(3, 'Paulinho') - 3; pi = wt(3, 'Piquerez') - 3; tr = wt(3, 'tratamento') - 3
    pal(c, 640, 2090, 820, f, 7, num_='7', skin=2, hair='#151010', arms='hang' if f < tr else 'cintura',
        expr='neutral' if f < pi else 'nervous', look=-1 if f < tr else 0)
    if f < pi - 2:
        telao_txt(c, [('PAULINHO', 170)], f, pa, y=760)
    elif f < tr - 2:
        telao_txt(c, [('PIQUEREZ', 170)], f, pi, y=760)
    else:
        telao_txt(c, [('TRATAMENTO', 150)], f, tr, y=760)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, tr, 10))
    k = kick(f, tr if f >= tr else pa, .7)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'day'


def s4(f):
    """fundo da conta: taça genérica e o número 3 que vira 4ª."""
    c = conta_bg().copy()
    tr = wt(4, 'tres') - 3; qu = wt(4, 'quarta') - 3
    tk = back(ramp(f, 2, 12))
    if tk > .03: paste_c(c, trofeu(), 640, 1380, .9 * tk)
    if f < qu - 2:
        if f >= tr: numero_gigante(c, '3 TÍTULOS', 640, 760, f, tr, 150, -3)
    else:
        explosao(c, 640, 760, f, qu, 260)
        numero_gigante(c, 'A 4ª?', 640, 760, f, qu, 230, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, qu, 10))
    k = kick(f, qu if f >= qu else tr, .8)
    return c, (640 + 18 * math.sin(f * .05), 1200 + k * 8, z, k), 'dusk'


def s5(f):
    """close do torcedor de novo: preocupado com a final perdida, depois curioso olhando pra câmera."""
    c = estadio2('dusk').copy()
    pe = wt(5, 'perdeu') - 3; te = wt(5, 'tetra') - 3
    c = put_close(c, f, expr='preocupado' if f < te else 'curioso', s=.95, roupa=VERDE, pele='#e0ac85',
                  cabelo='#2a1a10', look=-1 if f < pe + 10 else 0)
    if f < te - 2:
        num(c, '2025', 621, 720, f, pe, 140, -2)
    else:
        num(c, 'TETRA?', 621, 720, f, te, 160, 2)
    z = (1.04 + .002 * f) * (1 + .08 * pulse(f, te, 10))
    return c, (621, 1104, z, kick(f, te, .5)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'hoje') - 3, 150, .9)
    s.rugido(s.W(0, 'hoje') - 2, 1.0, .4)
    s.thunk(s.W(1, 'embarca') - 3, 130, .8)
    s.thunk(s.W(1, 'Montevideu') - 3, 150, .9)
    s.thunk(s.W(1, 'Uruguai') - 3, 140, .8)
    s.thunk(s.W(2, 'Sabado') - 3, 140, .8)
    s.thunk(s.W(2, 'cinco') - 3, 150, .9)
    s.apito(s.W(2, 'final') - 4)
    s.thunk(s.W(2, 'Estudiantes') - 3, 150, .9)
    s.thunk(s.W(3, 'Paulinho') - 3, 140, .8)
    s.thunk(s.W(3, 'Piquerez') - 3, 140, .8)
    s.thunk(s.W(3, 'tratamento') - 3, 150, .9)
    s.thunk(s.W(4, 'tres') - 3, 160, .9)
    s.thunk(s.W(4, 'quarta') - 3, 170, 1.0)
    s.rugido(s.W(4, 'quarta') - 2, 1.2, .5)
    s.thunk(s.W(5, 'perdeu') - 3, 140, .8)
    s.ting(s.W(5, 'tetra') - 3, .35)
