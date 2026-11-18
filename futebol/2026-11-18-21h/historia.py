"""anima.futebol — 18/11/2026 21h — Brasileirão 35ª rodada: Corinthians x Botafogo hoje, Corinthians no Z4.
Fontes (conferidas em 18/11/2026): Revista Oeste (21h30 Neo Química Arena; Corinthians 17º com 37 pts no Z4, Seedorf;
Botafogo 42 pts, Tite ex-Corinthians, vem de 1x0 no Atlético-MG; suspensos Yuri Alberto e André Ramalho; Garro lesionado;
vitória pode tirar do Z4; Grêmio x Bahia quarta 21h30); CartaCapital/Terra (21h30 Neo Química Arena, Corinthians 17º,
Seedorf, Botafogo 42 pts e 1x0 no Atlético-MG, Ramalho, Yuri Alberto suspensos, Garro lesão no joelho);
VAVEL (37 pts na zona, precisa vencer para ter chance de deixar o Z4, Tite x Seedorf, mesmos desfalques);
Bolavip (Grêmio x Bahia 21h30).
Sem escudos/logos/taças reais: times por plaquinhas e cores; jogadores genéricos com placa do nome."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Corinthians entra em campo hoje dentro da zona de rebaixamento.",
    "O jogo é contra o Botafogo, às nove e meia da noite, na Neo Química Arena.",
    "E tem reencontro: o Tite, ex-técnico do Corinthians, agora comanda o Botafogo contra o Seedorf.",
    "O Seedorf não terá Yuri Alberto nem André Ramalho, suspensos, e perdeu o Garro, lesionado.",
    "Na tabela, o Corinthians é décimo sétimo, com trinta e sete pontos.",
    "O Botafogo tem quarenta e dois e vem de vitória por um a zero sobre o Atlético Mineiro.",
    "Se vencer, o Corinthians pode sair da zona ainda nesta rodada, e o Grêmio joga no mesmo horário.",
]
CAPTXT = [
    "O Corinthians entra em campo hoje|dentro da zona de rebaixamento.",
    "O jogo é contra o Botafogo, às 21h30,|na Neo Química Arena.",
    "E tem reencontro: o Tite, ex-técnico do Corinthians,|agora comanda o Botafogo contra o Seedorf.",
    "O Seedorf não terá Yuri Alberto nem André Ramalho,|suspensos, e perdeu o Garro, lesionado.",
    "Na tabela, o Corinthians é 17º,|com 37 pontos.",
    "O Botafogo tem 42 e vem de vitória|por 1 a 0 sobre o Atlético-MG.",
    "Se vencer, o Corinthians pode sair da zona ainda nesta rodada,|e o Grêmio joga no mesmo horário.",
]
FALA_TIKTOK = "O Corinthians sai do Z4 hoje? Comenta sim ou não, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'Corinthians', 4), (0, 'rebaixamento', 4), (1, 'Botafogo', 4), (1, 'nove', 4), (1, 'Arena', 4),
         (2, 'Tite', 4), (2, 'Seedorf', 4), (3, 'Yuri', 4), (3, 'Ramalho', 4), (3, 'Garro', 4),
         (4, 'setimo', 4), (4, 'trinta', 4), (5, 'quarenta', 4), (5, 'zero', 4), (5, 'Mineiro', 4),
         (6, 'vencer', 4), (6, 'zona', 4), (6, 'Gremio', 4), (6, 'horario', 4)]

COR, COR_F = time_('CORINTHIANS')
BOT, BOT_F = time_('BOTAFOGO')
GRE, GRE_F = time_('GRÊMIO')
GK = ('#ffd84a', '#111111', '#111111')
TEC_C = ('#2b2b33', '#2b2b33', '#111111')


def cor(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=COR, faixa=COR_F, **kw)


def bot(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=BOT, faixa=BOT_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def s0(f):
    c = estadio2('dusk').copy()
    co = wt(0, 'Corinthians') - 3; zo = wt(0, 'zona') - 3; re = wt(0, 'rebaixamento') - 3
    x = lerp(-250, 640, easeOut(ramp(f, 0, co + 10)))
    if f < co + 8: linhas_vel(c, x, 2030, 880, f)
    cor(c, x, 2030, 880, f, 7, arms='run' if f < co + 10 else 'shrug', run=(f * .09) % 1 if f < co + 10 else None,
        expr='nervous' if f >= zo else 'stern', num_='10')
    put_placa(c, 'CORINTHIANS', COR, 640, 1040, f, co, 60, -3)
    explosao(c, 640, 780, f, zo, 220, cor=(230, 60, 50))
    num(c, 'NO Z4', 640, 780, f, zo, 150, -4)
    if f >= zo: foco(c, 640, 1650, 470, .5 * ramp(f, zo, zo + 6))
    num(c, 'ZONA DE REBAIXAMENTO', 640, 1250, f, re, 66, 3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, zo, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    bo = wt(1, 'Botafogo') - 3; no = wt(1, 'nove') - 3; ar = wt(1, 'Neo') - 3
    paste_c(c, calendario('18', 'NOV'), 640, 1180, .6 * back(ramp(f, 2, 10)))
    num(c, '21H30', 640, 740, f, no, 130, -3)
    cor(c, 290, 2060, 640, f, 13, arms='cintura', expr='stern', look=1, num_='10')
    put_placa(c, 'CORINTHIANS', COR, 290, 1340, f, 2, 40, -3)
    bot(c, 990, 2060, 640, f, 12, arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    put_placa(c, 'BOTAFOGO', BOT, 990, 1340, f, bo, 44, 3)
    num(c, 'NEO QUÍMICA ARENA', 640, 900, f, ar, 76, 2)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1380, z, 0), 'dusk'


def s2(f):
    c = estadio2('golden').copy()
    re = wt(2, 'reencontro') - 3; ti = wt(2, 'Tite') - 3; ex = wt(2, 'Corinthians') - 3; se = wt(2, 'Seedorf') - 3
    num(c, 'REENCONTRO', 640, 720, f, re, 120, -3)
    if f >= ti - 4:
        put_atleta(c, 330, 2050, 760, f, 21, cores=TEC_C, faixa=None, skin=1, hs='curto', hair='#d8d8d8',
                   arms='point' if f >= se else 'cintura', expr='smug', look=1)
        put_placa(c, 'TITE', BOT, 330, 1250, f, ti, 60, -3)
        num(c, 'EX-CORINTHIANS', 330, 1110, f, ex, 52, 2)
    if f >= se - 4:
        put_atleta(c, 950, 2050, 760, f, 22, cores=TEC_C, faixa=None, skin=4, hs='raspado', hair='#151010',
                   arms='cintura', expr='stern', look=-1, flip=True)
        put_placa(c, 'SEEDORF', COR, 950, 1250, f, se, 56, 3)
    if f >= se: num(c, 'x', 640, 1000, f, se, 140, 0)
    z = lerp(1.04, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0003 * f)
    k = kick(f, se, .6)
    return c, (lerp(620, 660, smooth(f / 160)), 1420 + k * 8, z, k), 'golden'


def s3(f):
    c = estadio2('dusk').copy()
    num(c, 'DESFALQUES', 640, 720, f, max(0, wt(3, 'Yuri') - 8), 120, -3)
    ps = [('YURI ALBERTO', 'Yuri', 'SUSPENSO', 'suspensos', '9', 2, 'curto'),
          ('ANDRÉ RAMALHO', 'Ramalho', 'SUSPENSO', 'suspensos', '5', 1, 'raspado'),
          ('GARRO', 'Garro', 'LESIONADO', 'lesionado', '8', 0, 'curto')]
    for i, (nome, w_, mot, wm, n_, sk, hs) in enumerate(ps):
        k0 = wt(3, w_) - 3; km = wt(3, wm) - 3
        x = 230 + 390 * i
        if f >= k0 - 4:
            cor(c, x, 2050, 620, f, 30 + i, num_=n_, hs=hs, skin=sk, arms='shrug' if f >= km else 'hang', expr='nervous', look=0)
            put_placa(c, nome, COR, x, 1180 - 110 * (i % 2), f, k0, 40, -3 + 3 * (i % 2))
            num(c, mot, x, 1480, f, km, 46, 2 - 2 * i)
    z = lerp(1.0, 1.06, easeOut(ramp(f, 0, 60))) * (1 + .0003 * f)
    k = kick(f, wt(3, 'Garro') - 3, .6)
    return c, (640, 1420 + k * 8, z, k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    se = wt(4, 'setimo') - 3; tr = wt(4, 'trinta') - 3
    tabela(c, [('17º', 'CORINTHIANS', COR, '37', True)], 640, 900, f, se)
    num(c, '17º LUGAR', 640, 720, f, se, 120, -3)
    cor(c, 640, 2040, 640, f, 9, num_='10', arms='cintura' if f < tr else 'shrug', expr='stern' if f < tr else 'nervous', look=0)
    num(c, '37 PONTOS', 640, 1150, f, tr, 100, 3)
    if f >= tr: foco(c, 640, 1650, 380, .4 * ramp(f, tr, tr + 6))
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, tr, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


def s5(f):
    c = estadio2('day').copy()
    qu = wt(5, 'quarenta') - 3; ze = wt(5, 'zero') - 3; kf = max(14, wt(5, 'vitoria') - 6)
    gx, gy = put_gol2(c, x=760, estufa=pulse(f, kf + 9, 6))
    put_goleiro(c, f, GK, None, gx=780 + (60 if f > kf + 6 else 0), arms='up', expr='shock', skin=1)
    x = lerp(-200, 330, easeOut(ramp(f, 0, kf - 3)))
    if f < kf - 4: linhas_vel(c, x, 2030, 840, f)
    bot(c, x, 2030, 840, f, 4, arms='run' if f < kf + 6 else 'punho', run=(f * .09) % 1 if f < kf - 4 else None,
        kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='9')
    rb = raio_bola(840)
    bola_voo(c, f, kf, x + 840 * .13, 2030 - rb, gx + 90, gy, rb, raio_bola(300))
    if f < kf + 9: num(c, '42 PONTOS', 640, 720, f, qu, 120, -3)
    else:
        explosao(c, 640, 740, f, kf + 9, 200)
        num(c, 'VITÓRIA', 640, 740, f, kf + 11, 120, -3)
    if f >= ze - 2:
        put_placa(c, 'BOTAFOGO 1 x 0 ATLÉTICO-MG', BOT, 640, 930, f, ze - 2, 44, 2)
    k = kick(f, kf + 9, .8) + kick(f, ze, .5)
    return c, (lerp(600, 680, smooth(f / 140)), 1430 + k * 10, 1.05 * (1 + .0008 * f), k), 'golden'


def s6(f):
    c = estadio2('dusk').copy()
    ve = wt(6, 'vencer') - 3; zo = wt(6, 'zona') - 3; gr = wt(6, 'Gremio') - 3; ho = wt(6, 'horario') - 3
    cor(c, 330, 2040, 760, f, 3, num_='10', arms='punho' if f >= ve else 'cintura', expr='grin' if f >= ve else 'stern', look=1)
    put_placa(c, 'CORINTHIANS', COR, 330, 1220, f, 0, 50, -3)
    num(c, 'SE VENCER...', 640, 720, f, ve, 110, -3)
    num(c, 'PODE SAIR DO Z4', 640, 880, f, zo, 90, 2)
    if f >= gr - 4:
        put_atleta(c, 960, 2040, 760, f, 7, cores=GRE, faixa=GRE_F, skin=1, hs='curto', hair='#3a2a1e', arms='cintura',
                   expr='nervous', look=-1, flip=True, num_='9')
        put_placa(c, 'GRÊMIO x BAHIA', GRE, 930, 1220, f, gr, 46, 3)
    num(c, 'TAMBÉM ÀS 21H30', 640, 1050, f, ho, 76, -2)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    k = kick(f, zo, .6)
    return c, (640, 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def OVERLAY(im, si, lf):
    D = {0: ('CORINTHIANS NO Z4', 'JOGA HOJE PRA SAIR', wt(0, 'rebaixamento') + 6),
         1: ('CORINTHIANS x BOTAFOGO', 'HOJE, 21H30, NEO QUÍMICA ARENA', wt(1, 'Arena') + 4),
         2: ('TITE x SEEDORF', 'EX-TÉCNICO DO TIMÃO NO OUTRO BANCO', wt(2, 'Seedorf') + 6),
         3: ('3 DESFALQUES', 'YURI ALBERTO, ANDRÉ RAMALHO E GARRO', wt(3, 'lesionado') + 4),
         4: ('CORINTHIANS 17º', '37 PONTOS', wt(4, 'pontos') + 4),
         5: ('BOTAFOGO: 42 PONTOS', 'VEM DE 1 x 0 NO ATLÉTICO-MG', wt(5, 'Mineiro') + 4)}
    if si in (3, 6): return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'Corinthians') - 3, 150, .8)
    s.thunk(s.W(0, 'zona') - 3, 110, .9)
    s.thunk(s.W(1, 'Botafogo') - 3, 160, .6)
    s.ting(s.W(1, 'nove') - 3, .3)
    s.whoosh(s.W(2, 'reencontro') - 4, .5)
    s.thunk(s.W(2, 'Tite') - 3, 170, .5)
    s.thunk(s.W(2, 'Seedorf') - 3, 170, .5)
    for w in ('Yuri', 'Ramalho', 'Garro'):
        s.thunk(s.W(3, w) - 3, 130, .5)
    s.thunk(s.W(4, 'setimo') - 3, 150, .6)
    s.thunk(s.W(5, 'quarenta') - 3, 150, .6)
    s.thunk(s.W(5, 'zero') - 3, 140, .7)
    s.ting(s.W(6, 'zona') - 3, .35)
    s.thunk(s.W(6, 'Gremio') - 3, 140, .6)
