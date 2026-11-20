"""anima.futebol — 20/11/2026 19h — RAIO-X · EP. 1 — Final da Sul-Americana: Atlético-MG x Boca Juniors, sábado 21/11 19h30.
Fontes (conferidas em 20/11/2026, ver fatos.txt): CNN Brasil, Terra, Lance!, Metrópoles, Tribuna Popular (Conmebol/Opta):
19h30 de Brasília no Metropolitano Roberto Meléndez, Barranquilla (jogo único); Galo 7 jogos sem vencer; Boca campeão em 2004 e 2005;
Galo nunca ganhou, vice em 2025 (Lanús, pênaltis); Alan Franco suspenso; retrospecto em 8 jogos: Boca 3 vitórias, Galo 1, 4 empates.
Só em 1 fonte -> não usado: prêmio, artilheiros, técnico do Boca, árbitro. Sem escudos/logos/rostos reais: plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'SUL-AMERICANA  ·  FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Galo está há sete jogos sem vencer. Dá pra bater o Boca?",
    "A final é amanhã, às dezenove e trinta, em Barranquilla, na Colômbia.",
    "O Boca já ganhou a Sul-Americana... duas vezes.",
    "O Galo nunca ganhou. No ano passado, perdeu a final... nos pênaltis.",
    "E o Galo não terá Alan Franco, suspenso.",
    "No retrospecto, o Boca venceu três jogos... o Galo, só um. Quem leva?",
]
CAPTXT = [
    "O Galo está há 7 jogos sem vencer.|Dá pra bater o Boca?",
    "A final é amanhã, às 19h30,|em Barranquilla, na Colômbia.",
    "O Boca já ganhou a Sul-Americana...|2 vezes.",
    "O Galo nunca ganhou. No ano passado,|perdeu a final... nos pênaltis.",
    "E o Galo não terá|Alan Franco, suspenso.",
    "No retrospecto, o Boca venceu 3 jogos...|o Galo, só 1. Quem leva?",
]
FALA_TIKTOK = "Quem leva a Sul-Americana, Galo ou Boca? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'sete', 4), (0, 'Boca', 4), (1, 'amanha', 4), (1, 'dezenove', 4), (1, 'Barranquilla', 4), (2, 'duas', 4),
         (3, 'nunca', 4), (3, 'penaltis', 4), (4, 'Alan', 4), (4, 'suspenso', 4), (5, 'tres', 4), (5, 'um', 4), (5, 'leva', 4)]

CAM, CAM_F = time_('ATLÉTICO-MG')
BOC, BOC_F = time_('BOCA JUNIORS')


def galo(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=CAM, faixa=CAM_F, **kw)


def boca(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=BOC, faixa=BOC_F, **kw)


def s0(f):
    """conta_bg: marca da série e depois a pergunta polêmica."""
    c = conta_bg().copy()
    se = wt(0, 'sete') - 3; bo = wt(0, 'Boca') - 3
    q = max(42, se - 2)
    galo(c, 300, 2060, 760, f, 3, arms='cintura', expr='stern' if f < se else 'nervous', look=1, num_='10')
    boca(c, 960, 2060, 760, f, 6, arms='cintura' if f < bo else 'punho', expr='stern', look=-1, flip=True, num_='9')
    if f < q - 2:
        num(c, 'RAIO-X', 640, 860, f, 0, 150, -3)
        num(c, 'EP. 1', 640, 1060, f, 4, 130, 3)
    elif f < bo - 2:
        num(c, '7 SEM VENCER', 640, 940, f, q, 120, -3)
    else:
        num(c, 'BATE O BOCA?', 640, 940, f, bo, 130, 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, bo, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio à noite: frente a frente, data, hora e local."""
    c = estadio2('dusk').copy()
    am = wt(1, 'amanha') - 3; de = wt(1, 'dezenove') - 3; ba = wt(1, 'Barranquilla') - 3
    gx = lerp(-260, 360, easeOut(ramp(f, 0, 16)))
    bx = lerp(1500, 900, easeOut(ramp(f, 0, 16)))
    if f < 16:
        linhas_vel(c, gx, 2010, 840, f, dir=-1); linhas_vel(c, bx, 2010, 840, f, dir=1)
    galo(c, gx, 2010, 840, f, 3, arms='cintura', expr='stern', look=1, num_='10', run=(f * .1) % 1 if f < 16 else None)
    boca(c, bx, 2010, 840, f, 7, arms='cintura', expr='stern', look=-1, flip=True, num_='9', run=(f * .1) % 1 if f < 16 else None)
    if f < de - 2:
        if f >= am: paste_c(c, calendario('21', 'NOV'), 640, 960, .55 * back(ramp(f, am, am + 8)))
    elif f < ba - 2:
        num(c, '19H30', 640, 920, f, de, 170, 3)
    else:
        num(c, 'BARRANQUILLA', 640, 920, f, ba, 94, -2)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, de, .6)
    return c, (640, 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


def s2(f):
    """estádio dourado com a taça genérica: Boca bicampeão."""
    c = estadio2('golden').copy()
    bo = wt(2, 'Boca') - 3; du = wt(2, 'duas') - 3
    paste_c(c, trofeu(), 900, 1500, .75 + .02 * math.sin(f * .1))
    boca(c, 420, 2030, 880, f, 5, arms='up' if f >= du else 'cintura', expr='grin' if f >= du else 'stern', look=1, num_='9')
    if f < du - 2:
        put_placa(c, 'BOCA JUNIORS', BOC, 640, 800, f, bo, 80, -2)
    else:
        num(c, '2 TÍTULOS', 640, 820, f, du, 160, 3)
        if f >= du: confete(c, 640, 900, f, du, 50, 600)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, du, .8)
    return c, (640, 1420 + k * 10, z, k), 'golden'


def s3(f):
    """vestiário do Galo: nunca ganhou, vice nos pênaltis."""
    c = vestiario(CAM, CAM_F).copy()
    nu = wt(3, 'nunca') - 3; pe = wt(3, 'penaltis') - 3
    galo(c, 640, 2110, 820, f, 6, arms='hang', expr='stern' if f < pe else 'nervous', look=0, num_='10')
    if f < pe - 2:
        num(c, 'NUNCA GANHOU', 640, 1110, f, nu, 110, -3)
    else:
        num(c, 'NOS PÊNALTIS', 640, 1110, f, pe, 120, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, pe, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s4(f):
    """prancheta: a defesa do Galo com o desfalque."""
    c = prancheta().copy()
    al = wt(4, 'Alan') - 3; su = wt(4, 'suspenso') - 3
    ys = [1440, 1420, 1420, 1440]
    for i, x in enumerate((260, 500, 740, 980)):
        if i == 2 and f >= su:
            continue
        pino(c, x, ys[i] + 10 * math.sin(f * .16 + i), ('#ffffff',), f, 2 + i * 2, str(i + 2), 80)
    if f >= su:   # o lugar vazio do zagueiro
        d = ImageDraw.Draw(c); k = back(ramp(f, su, su + 8)); r = 70 * k
        d.line([(740 - r, 1420 - r), (740 + r, 1420 + r)], fill=(230, 40, 40, 255), width=22)
        d.line([(740 - r, 1420 + r), (740 + r, 1420 - r)], fill=(230, 40, 40, 255), width=22)
    if f < su - 2:
        put_placa(c, 'ALAN FRANCO', CAM, 640, 900, f, al, 84, -2)
    else:
        num(c, 'SUSPENSO', 640, 900, f, su, 150, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, su, .6)
    return c, (640 + 26 * math.sin(f * .05), 1300 + k * 8, z, lerp(0, 2, smooth(ramp(f, 0, 60)))), 'day'


def s5(f):
    """telão: retrospecto e a pergunta."""
    c = telao('dusk').copy()
    tr = wt(5, 'tres') - 3; um = wt(5, 'um') - 3; le = wt(5, 'leva') - 3
    if f < le - 2:
        linhas = [('BOCA  3', 150)]
        if f >= um: linhas.append(('GALO  1', 150))
        if f >= tr: telao_txt(c, linhas, f, tr, y=700)
    else:
        telao_txt(c, [('QUEM LEVA?', 150)], f, le, y=840)
    galo(c, 260, 2080, 640, f, 4, arms='cintura' if f < le else 'punho', expr='stern', look=1)
    boca(c, 1000, 2080, 640, f, 8, arms='cintura', expr='stern', look=-1, flip=True)
    z = lerp(1.0, 1.08, smooth(f / 120))
    k = kick(f, le, .5)
    return c, (640 + 20 * math.sin(f * .03), 1300 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(s.W(0, 'sete') - 3, 150, .8)
    s.thunk(s.W(0, 'Boca') - 3, 120, .9)
    s.apito(s.W(1, 'amanha') - 3)
    s.thunk(s.W(1, 'dezenove') - 3, 150, .8)
    s.thunk(s.W(1, 'Barranquilla') - 3, 120, .7)
    s.thunk(s.W(2, 'duas') - 3, 120, .9)
    s.rugido(s.W(2, 'duas') - 1, 1.8, .6)
    s.thunk(s.W(3, 'nunca') - 3, 150, .8)
    s.apito(s.W(3, 'penaltis') - 3, longo=True)
    s.thunk(s.W(4, 'Alan') - 3, 150, .7)
    s.thunk(s.W(4, 'suspenso') - 3, 120, 1.0)
    s.thunk(s.W(5, 'tres') - 3, 150, .8)
    s.thunk(s.W(5, 'um') - 3, 120, .9)
    s.ting(s.W(5, 'leva') - 3, .3)
