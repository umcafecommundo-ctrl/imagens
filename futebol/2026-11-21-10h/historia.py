"""anima.futebol — 21/11/2026 10h — RAIO-X · EP. 2 — Palmeiras x Flamengo hoje 16h30 no Nubank Parque (36ª rodada).
Fontes (conferidas em 21/11/2026, ver fatos.txt): CNN Brasil (20/11: desfalques do Palmeiras Barboza suspenso, Murilo, Piquerez e
Paulinho; Flamengo sem Léo Pereira e Pulgar suspensos e De la Cruz vetado pelo gramado sintético; prováveis escalações), ESPN
(20/11: prováveis escalações, Barboza/Léo Pereira/Pulgar pelo 3º amarelo, Murilo e Piquerez fora, Abel "Este título está entregue"),
Lance! (20/11: prováveis escalações, técnicos Abel Ferreira e Leonardo Jardim), TMC (20/11: quatro desfalques do Palmeiras),
Soccerway/Flashscore/A Bola (Abel: "o título está entregue"). Escalações = PROVÁVEIS (3 zagueiros Fuchs, Gómez e Benedetti nas
3 fontes; ataque do Fla Carrascal, Pedro e Samuel Lino nas 3 fontes). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  36ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "Com quatro desfalques, o Palmeiras segura o Flamengo hoje?",
    "Sem Barboza, suspenso, e sem Murilo, Piquerez e Paulinho, lesionados.",
    "Por isso, Abel deve ir com três zagueiros: Fuchs, Gómez e Benedetti.",
    "O Flamengo não tem Léo Pereira e Pulgar, suspensos... nem De la Cruz.",
    "Na frente, Jardim deve ir com o trio Carrascal, Pedro e Samuel Lino.",
    "E Abel já disse: o título está entregue. Será?",
]
CAPTXT = [
    "Com 4 desfalques, o Palmeiras|segura o Flamengo hoje?",
    "Sem Barboza, suspenso, e sem Murilo,|Piquerez e Paulinho, lesionados.",
    "Por isso, Abel deve ir com 3 zagueiros:|Fuchs, Gómez e Benedetti.",
    "O Flamengo não tem Léo Pereira e Pulgar,|suspensos... nem De la Cruz.",
    "Na frente, Jardim deve ir com o trio|Carrascal, Pedro e Samuel Lino.",
    "E Abel já disse: o título está entregue.|Será?",
]
FALA_TIKTOK = "O Palmeiras segura o Flamengo? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SEGURA O FLA?"
TWIST = 5
FLASH = [3]
CHECK = [(0, 'desfalques', 4), (0, 'segura', 4), (1, 'Barboza', 4), (1, 'Murilo', 4), (2, 'zagueiros', 4),
         (3, 'Pulgar', 4), (3, 'Cruz', 4), (4, 'trio', 4), (4, 'Lino', 4), (5, 'entregue', 4), (5, 'Sera', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')
AGAS = ('#22303f', '#ffffff', '#22303f')   # agasalho genérico do técnico


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def s0(f):
    """conta_bg: marca da série grande e depois a pergunta polêmica."""
    c = conta_bg().copy()
    de = wt(0, 'desfalques') - 3; sg = wt(0, 'segura') - 3
    q = max(45, de)
    pal(c, 330, 2060, 760, f, 6, arms='cintura', expr='stern' if f < de else 'nervous', look=1, num_='9')
    fla(c, 950, 2060, 760, f, 3, arms='cintura' if f < sg else 'punho', expr='stern' if f < sg else 'smug', look=-1, flip=True, num_='10')
    if f < sg - 2:
        num(c, 'RAIO-X', 640, 860, f, 0, 170, -3)
        num(c, 'EP. 2', 640, 1060, f, 4, 130, 3)
    else:
        num(c, 'SEGURA', 640, 860, f, sg, 160, -3)
        num(c, 'O FLA?', 640, 1060, f, sg + 3, 160, 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, sg, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """vestiário do Palmeiras: os quatro desfalques."""
    c = vestiario(PAL, PAL_F).copy()
    ba = wt(1, 'Barboza') - 3; mu = wt(1, 'Murilo') - 3
    pal(c, 640, 2110, 820, f, 6, arms='cintura' if f < mu else 'shrug', expr='stern' if f < mu else 'nervous', look=0, num_='9')
    if f < mu - 2:
        if f >= ba: num(c, 'BARBOZA SUSPENSO', 640, 1110, f, ba, 96, -3)
    else:
        num(c, '+3 LESIONADOS', 640, 1110, f, mu, 110, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, mu, .6)
    return c, (640 + 18 * math.sin(f * .04), 1400 + k * 10, z, k), 'day'


# posições na prancheta (Palmeiras embaixo, atacando para cima)
ZAG = [(380, 1420), (621, 1460), (862, 1420)]


def s2(f):
    """prancheta: Palmeiras com linha de três zagueiros."""
    c = prancheta().copy()
    tr = wt(2, 'tres') - 3; za = wt(2, 'zagueiros') - 3
    for i, x in enumerate((300, 520, 722, 942)):
        pino(c, x, 1130 + 12 * math.sin(f * .2 + i), PAL, f, 4 + i * 2, '', 58)
    for i, (x, y) in enumerate(ZAG):
        pino(c, x, y + (0 if f >= za else 60) + 12 * math.sin(f * .2 + i * 1.7), PAL, f, tr + i * 3, 'FGB'[i], 90)
    if f >= za:
        seta(c, (290, 1560), (952, 1560), f, za + 2, 14, (255, 216, 74), 12)
    if f < tr - 2:
        num(c, 'PALMEIRAS', 640, 800, f, 2, 120, -3)
    else:
        num(c, '3 ZAGUEIROS', 640, 800, f, tr, 112, 3)
    z = lerp(1.18, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, tr, .6)
    return c, (640 + 40 * math.sin(f * .06), 1320 + k * 8 + 20 * math.sin(f * .045), z * (1 + .0012 * f), lerp(0, -2, smooth(ramp(f, 0, 60))) + .8 * math.sin(f * .05)), 'day'


def s3(f):
    """estádio de dia: o Flamengo e as ausências."""
    c = estadio2('day').copy()
    pu = wt(3, 'suspensos') - 3; cr = wt(3, 'nem') - 3
    put_gol2(c)
    fla(c, 430, 2010, 860, f, 5, arms='cintura' if f < cr else 'shrug', expr='stern' if f < cr else 'nervous', look=1, num_='5')
    fla(c, 900, 2040, 780, f, 8, arms='hang', expr='nervous', look=-1, flip=True, skin=1, hs='raspado', num_='8')
    if f < pu - 2:
        put_placa(c, 'FLAMENGO', FLA, 640, 820, f, 2, 90)
    elif f < cr - 2:
        num(c, '2 SUSPENSOS', 640, 840, f, pu, 110, -3)
    else:
        num(c, 'DE LA CRUZ FORA', 640, 840, f, cr, 100, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, cr, .6)
    return c, (640, 1400 + k * 8, z, lerp(0, 2, smooth(ramp(f, 0, 60)))), 'day'


def s4(f):
    """prancheta: o trio de ataque do Flamengo (de cima para baixo)."""
    c = prancheta().copy()
    tr = wt(4, 'trio') - 3; ca = wt(4, 'Carrascal') - 3; pe = wt(4, 'Pedro') - 3; li = wt(4, 'Lino') - 3
    for i, x in enumerate((360, 621, 882)):
        pino(c, x, 1000 + 12 * math.sin(f * .2 + i), FLA, f, 2 + i * 2, '', 58)
    alvo = [(380, 1420, ca, 'C'), (621, 1480, pe, 'P'), (862, 1420, li, 'L')]
    for (x, y, t0, r) in alvo:
        if f >= t0: seta(c, (x, 1060), (x, y - 100), f, t0, 10, (255, 255, 255), 10)
        pino(c, x, y + 12 * math.sin(f * .2 + x), FLA, f, t0, r, 90)
    if f < tr - 2:
        num(c, 'FLAMENGO', 640, 760, f, 2, 112, -3)
    else:
        num(c, 'TRIO NA FRENTE', 640, 760, f, tr, 96, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, li, .6)
    return c, (640 - 40 * math.sin(f * .06), 1300 + k * 8 + 20 * math.sin(f * .045), z * (1 + .0012 * f), lerp(0, 2, smooth(ramp(f, 0, 60))) + .8 * math.sin(f * .05)), 'day'


def s5(f):
    """coletiva: técnico genérico + placa; a frase; e a pergunta."""
    c = coletiva(PAL).copy()
    di = wt(5, 'disse') - 3; en = wt(5, 'entregue') - 3; se = wt(5, 'Sera') - 3
    put_atleta(c, 640, 2000, 980, f, 4, cores=AGAS, faixa=None, skin=1, hs='careca', hair='#2a2a2a',
               arms='shrug' if f >= en else 'hang', expr='pained' if f >= en else 'stern', look=0)
    mesa_coletiva(c)
    if f < di - 2:
        put_placa(c, 'ABEL', PAL, 640, 760, f, 2, 96)
    elif f >= se:
        num(c, 'SERÁ?', 640, 780, f, se, 200, 3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, se, .8)
    return c, (640, 1350 + k * 10, z * (1 + .0015 * max(0, f - se)), k), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    if si == 5:
        di = wt(5, 'disse') - 3; se = wt(5, 'Sera') - 3
        if di <= lf < se - 2:
            im = destaque(im, '"O TÍTULO ESTÁ ENTREGUE"', lf, di, sub='ABEL FERREIRA', y=760)
    return im


def SFX(s):
    s.thunk(s.W(0, 'desfalques') - 3, 150, .8)
    s.thunk(s.W(0, 'segura') - 3, 120, .9)
    s.thunk(s.W(1, 'Barboza') - 3, 150, .8)
    s.thunk(s.W(1, 'Murilo') - 3, 120, .9)
    s.thunk(s.W(2, 'tres') - 3, 140, .9)
    s.apito(s.W(2, 'zagueiros') - 3)
    s.thunk(s.W(3, 'suspensos') - 3, 150, .8)
    s.thunk(s.W(3, 'nem') - 3, 120, .9)
    s.thunk(s.W(4, 'trio') - 3, 150, .8)
    s.thunk(s.W(4, 'Carrascal') - 3, 170, .5)
    s.thunk(s.W(4, 'Pedro') - 3, 170, .5)
    s.thunk(s.W(4, 'Lino') - 3, 170, .6)
    s.thunk(s.W(5, 'entregue') - 3, 130, .8)
    s.ting(s.W(5, 'Sera') - 3, .35)
