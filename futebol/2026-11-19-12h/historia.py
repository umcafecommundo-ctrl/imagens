"""anima.futebol — 19/11/2026 12h — Brasileirão 35ª rodada: Corinthians 4x0 Botafogo, hat-trick de Kaio César, Timão deixa o Z4.
Fontes (conferidas em 19/11/2026): Sou Timão, Brasil 247 (Corinthians 4x0 Botafogo, quarta 18/11, Neo Química Arena:
Kaio César 3 gols (1º no 1º tempo, 27'/28' divergem -> "no primeiro tempo"; outros 2 no 2º tempo), 2x0 no intervalo
(autor do 2º gol diverge: Depay x gol contra de Arthur Chaves -> não citado)); Placar (Corinthians 40 pts, sai do Z4,
Grêmio 38 pts no Z4, Seedorf técnico); Sou Timão (Corinthians depende de Vasco x Inter e Vitória x Bragantino nesta quinta:
se os dois vencerem volta ao Z4; próximo jogo Atlético-MG 25/11 na Arena MRV). Tite técnico do Botafogo (ex-Corinthians).
Sem escudos/logos/taças reais: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Kaio César fez três gols, o Corinthians goleou o Botafogo por quatro a zero e saiu da zona de rebaixamento.",
    "Foi ontem à noite, na Neo Química Arena, pela trigésima quinta rodada do Brasileirão.",
    "Kaio César abriu o placar no primeiro tempo, e o Corinthians foi para o intervalo vencendo por dois a zero.",
    "No segundo tempo, ele marcou mais dois gols e completou o hat-trick.",
    "E no banco, Seedorf venceu Tite, que já foi técnico do Timão.",
    "Com a vitória, o Corinthians chegou a quarenta pontos, e o Grêmio, com trinta e oito, ficou na zona.",
    "Mas o alívio pode durar pouco: se Internacional e Vitória vencerem hoje, o Timão volta para a zona.",
    "O Corinthians escapa, ou o sufoco vai até a última rodada?",
]
CAPTXT = [
    "Kaio César fez 3 gols, o Corinthians goleou o Botafogo|por 4 a 0 e saiu da zona de rebaixamento.",
    "Foi ontem à noite, na Neo Química Arena,|pela 35ª rodada do Brasileirão.",
    "Kaio César abriu o placar no 1º tempo, e o Corinthians|foi para o intervalo vencendo por 2 a 0.",
    "No 2º tempo, ele marcou mais 2 gols|e completou o hat-trick.",
    "E no banco, Seedorf venceu Tite,|que já foi técnico do Timão.",
    "Com a vitória, o Corinthians chegou a 40 pontos,|e o Grêmio, com 38, ficou na zona.",
    "Mas o alívio pode durar pouco: se Internacional e Vitória|vencerem hoje, o Timão volta para a zona.",
    "O Corinthians escapa,|ou o sufoco vai até a última rodada?",
]
FALA_TIKTOK = "O Corinthians escapa do rebaixamento? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "ESCAPA?"
TWIST = 6
FLASH = [3]
CHECK = [(0, 'tres', 4), (0, 'quatro', 4), (0, 'rebaixamento', 4), (1, 'noite', 4), (1, 'Arena', 4),
         (2, 'primeiro', 4), (2, 'dois', 4), (3, 'segundo', 4), (3, 'completou', 4), (4, 'Seedorf', 4), (4, 'Tite', 4),
         (5, 'quarenta', 4), (5, 'Gremio', 4), (6, 'Internacional', 4), (6, 'volta', 4), (7, 'escapa', 4), (7, 'rodada', 4)]

COR, COR_F = time_('CORINTHIANS')
BOT, BOT_F = time_('BOTAFOGO')
GRE, GRE_F = time_('GRÊMIO')
INT, INT_F = time_('INTERNACIONAL')
VIT_, VIT_F = time_('VITÓRIA')


def cor(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 4); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=COR, faixa=COR_F, **kw)


def bot(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=BOT, faixa=BOT_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def gol_cena(c, f, kf, kcores, kfaixa, gcores, gfaixa, kseed, kskin=4, khair='#151010', run_in=True, num_='11'):
    """chute de longe: atacante na frente, gol no fundo, bola diminuindo."""
    gx, gy = put_gol2(c, estufa=ramp(f, kf + 8, kf + 14))
    put_goleiro(c, f, gcores, gfaixa, arms='shrug' if f >= kf + 8 else 'hang', expr='shock' if f >= kf + 8 else 'nervous', skin=2)
    sx = lerp(260, 470, easeOut(ramp(f, 0, kf - 4))) if run_in else 470
    if run_in and f < kf - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    put_atleta(c, sx, 2010, 860, f, kseed, cores=kcores, faixa=kfaixa, skin=kskin, hair=khair, hs='curto', num_=num_,
               arms='up' if f >= kf + 10 else 'run', run=(f * .1) % 1 if (run_in and f < kf - 4) else None,
               kick=pulse(f, kf - 3, 5), expr='grin' if f >= kf + 6 else 'stern')
    rb = raio_bola(860)
    if f < kf + 40: bola_voo(c, f, kf, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 140)
    return gx, gy


def s0(f):
    c = estadio2('dusk').copy()
    tr = wt(0, 'tres') - 3; qu = wt(0, 'quatro') - 3; re = wt(0, 'rebaixamento') - 3
    cor(c, 330, 2020, 880, f, 3, arms='up' if f >= tr else 'cintura', expr='grin' if f >= tr else 'stern', look=1, num_='11')
    put_placa(c, 'KAIO CÉSAR', COR, 330, 1060, f, 2, 52, -3)
    explosao(c, 640, 760, f, tr, 200)
    num(c, '3 GOLS', 640, 760, f, tr + 2, 140, -4)
    num(c, 'COR 4 x 0 BOT', 870, 1180, f, qu, 70, 3)
    num(c, 'FORA DO Z4!', 870, 1340, f, re, 76, -3)
    if f >= re: confete(c, 640, 900, f, re, 50, 500)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, tr, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    no = wt(1, 'noite') - 3; ar = wt(1, 'Arena') - 3; ro = wt(1, 'rodada') - 3
    if f >= no: paste_c(c, calendario('18', 'NOV'), 640, 1150, .7 * back(ramp(f, no, no + 8)))
    num(c, 'NEO QUÍMICA ARENA', 640, 720, f, ar, 84, -3)
    num(c, '35ª RODADA', 640, 1500, f, ro, 90, 3)
    cor(c, 230, 1980, 520, f, 4, arms='hang', expr='neutral', look=1)
    bot(c, 1040, 1980, 520, f, 8, arms='hang', expr='neutral', look=-1, flip=True)
    put_placa(c, 'CORINTHIANS', COR, 250, 1530, f, 0, 32, -3)
    put_placa(c, 'BOTAFOGO', BOT, 1030, 1530, f, 0, 32, 3)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1360, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    ab = wt(2, 'abriu') - 3; pr = wt(2, 'primeiro') - 3; iv = wt(2, 'intervalo') - 3; do = wt(2, 'dois') - 3
    gol_cena(c, f, ab, COR, COR_F, BOT, BOT_F, 3)
    put_placa(c, 'KAIO CÉSAR', COR, 330, 860, f, wt(2, 'Kaio') - 3, 44, -3)
    if f >= ab + 8: explosao(c, 820, 1020, f, ab + 8, 140)
    num(c, 'GOL!', 820, 1020, f, ab + 8, 110, 3)
    num(c, '1º TEMPO', 330, 1000, f, pr, 70, 2)
    num(c, 'INTERVALO: 2 x 0', 640, 720, f, do, 80, -2)
    k = kick(f, ab, .9)
    return c, (lerp(600, 680, smooth(f / 150)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    ma = wt(3, 'marcou') - 3; co = wt(3, 'completou') - 3
    gol_cena(c, f, ma, COR, COR_F, BOT, BOT_F, 3, run_in=True)
    num(c, '2º TEMPO', 640, 720, f, wt(3, 'segundo') - 3, 90, -3)
    put_placa(c, 'KAIO CÉSAR', COR, 300, 980, f, ma, 40, -3)
    if f >= co: explosao(c, 830, 1040, f, co, 170)
    num(c, 'HAT-TRICK!', 830, 1040, f, co, 96, 3)
    num(c, 'COR 4 x 0 BOT', 640, 1250, f, co + 8, 72, -2)
    if f >= co: confete(c, 640, 900, f, co, 40, 450)
    k = kick(f, ma, .8)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    se = wt(4, 'Seedorf') - 3; ti = wt(4, 'Tite') - 3; ex = wt(4, 'Timao') - 3
    num(c, 'DUELO NO BANCO', 640, 720, f, wt(4, 'banco') - 3, 90, -3)
    sx = lerp(-200, 320, easeOut(ramp(f, se - 10, se + 4)))
    tx = lerp(1500, 940, easeOut(ramp(f, ti - 10, ti + 4)))
    cor(c, sx, 2040, 760, f, 6, arms='cintura', expr='proud', look=1, skin=3, hs='careca' if False else 'curto', hair='#151010')
    bot(c, tx, 2040, 760, f, 10, arms='cintura', expr='stern', look=-1, flip=True, skin=1, hair='#9a9a9a')
    put_placa(c, 'SEEDORF', COR, 320, 1180, f, se, 50, -3)
    put_placa(c, 'TITE', BOT, 940, 1180, f, ti, 56, 3)
    num(c, 'JÁ TREINOU O TIMÃO', 760, 920, f, ex, 64, 3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, ti, .5)
    return c, (640 + 15 * math.sin(f * .04), 1400 + k * 8, z, k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    qu = wt(5, 'quarenta') - 3; gr = wt(5, 'Gremio') - 3; zo = wt(5, 'zona') - 3
    tabela(c, [('', 'CORINTHIANS', COR, '40', True)], 640, 960, f, qu)
    tabela(c, [('Z4', 'GRÊMIO', GRE, '38', False)], 640, 1150, f, gr)
    num(c, '40 PONTOS', 640, 740, f, qu, 110, -3)
    num(c, 'NA ZONA', 640, 1420, f, zo, 80, 3)
    cor(c, 300, 1960, 480, f, 5, arms='joinha' if f >= qu else 'cintura', expr='proud', look=1)
    put_atleta(c, 980, 1960, 480, f, 9, cores=GRE, faixa=GRE_F, skin=1, hs='curto', hair='#3a2a1e', arms='cintura',
               expr='nervous', look=-1, flip=True)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, qu, .5)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('day').copy()
    hj = wt(6, 'hoje') - 3; it = wt(6, 'Internacional') - 3; vi = wt(6, 'Vitoria') - 3; vo = wt(6, 'volta') - 3
    num(c, 'ALÍVIO?', 640, 720, f, wt(6, 'alivio') - 3, 100, -3)
    if f >= hj: paste_c(c, calendario('19', 'NOV'), 640, 900, .45 * back(ramp(f, hj, hj + 8)))
    ix = lerp(-220, 300, easeOut(ramp(f, it - 10, it + 4)))
    vx = lerp(1500, 960, easeOut(ramp(f, vi - 10, vi + 4)))
    put_atleta(c, ix, 2030, 700, f, 12, cores=INT, faixa=INT_F, skin=2, hs='curto', hair='#2a1a10', arms='cintura', expr='stern', look=1)
    put_atleta(c, vx, 2030, 700, f, 14, cores=VIT_, faixa=VIT_F, skin=4, hs='curto', hair='#111111', arms='cintura', expr='stern', look=-1, flip=True)
    put_placa(c, 'INTERNACIONAL', INT, 300, 1060, f, it, 38, -3)
    put_placa(c, 'VITÓRIA', VIT_, 980, 1060, f, vi, 46, 3)
    if f >= vo: explosao(c, 640, 1200, f, vo, 150, cor=(214, 40, 44))
    num(c, 'TIMÃO VOLTA AO Z4', 640, 1200, f, vo, 74, -2)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, vo, .7)
    return c, (640, 1400 + k * 8, z, k), 'golden'


def s7(f):
    c = estadio2('dusk').copy()
    es = wt(7, 'escapa') - 3; ro = wt(7, 'rodada') - 3
    cor(c, 640, 2040, 820, f, 3, arms='up' if f >= es else 'cintura', expr='grin' if f < ro else 'nervous', look=0, num_='11')
    put_placa(c, 'CORINTHIANS', COR, 640, 1130, f, 0, 44, -2)
    num(c, 'ESCAPA?', 400, 740, f, es, 110, -4)
    num(c, 'SUFOCO ATÉ O FIM?', 760, 920, f, ro, 70, 4)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    if si in (2, 3):
        gols = 0 if lf < wt(2, 'abriu') + 6 else (1 if lf < wt(2, 'dois') else 2)
        if si == 3: gols = 2 if lf < wt(3, 'marcou') + 6 else 4
        im = placar_tv(im, 'COR', 'BOT', gols, 0, COR, BOT, '1º T' if si == 2 else '2º T', lf)
    D = {0: ('CORINTHIANS 4 x 0 BOTAFOGO', 'HAT-TRICK DE KAIO CÉSAR', wt(0, 'rebaixamento') + 4),
         1: ('QUARTA, 18/11, 21H30', 'NEO QUÍMICA ARENA', wt(1, 'Brasileirao') + 2),
         2: ('KAIO CÉSAR ABRE O PLACAR', '2 x 0 NO INTERVALO', wt(2, 'intervalo') + 4),
         3: ('3 GOLS DE KAIO CÉSAR', 'HAT-TRICK NO 2º TEMPO', wt(3, 'completou') + 14),
         4: ('SEEDORF x TITE', 'DUELO DE TÉCNICOS', wt(4, 'Timao') + 4),
         5: ('CORINTHIANS 40 PONTOS', 'FORA DO Z4 (POR ENQUANTO)', wt(5, 'zona') + 4),
         6: ('VASCO x INTER E VITÓRIA x BRAGANTINO', 'QUINTA, 19/11', wt(6, 'zona') + 2),
         7: ('', '', 4)}
    if si == 7: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'tres') - 3, 150, .9)
    s.ting(s.W(0, 'rebaixamento') - 3, .3)
    s.thunk(s.W(1, 'noite') - 3, 160, .6)
    s.thunk(s.W(2, 'abriu') - 3, 120, 1.0)
    s.thunk(s.W(3, 'marcou') - 3, 120, .9)
    s.ting(s.W(3, 'completou') - 3, .35)
    s.thunk(s.W(4, 'Seedorf') - 3, 160, .6)
    s.thunk(s.W(4, 'Tite') - 3, 160, .6)
    s.thunk(s.W(5, 'quarenta') - 3, 150, .7)
    s.thunk(s.W(6, 'volta') - 3, 140, .9)
    s.ting(s.W(7, 'escapa') - 3, .3)
