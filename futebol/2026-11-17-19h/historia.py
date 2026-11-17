"""anima.futebol — 17/11/2026 19h — Brasileirão: Palmeiras volta com 5 desfalques contra o Cruzeiro.
Fontes (conferidas em 17/11/2026): Lance! (17/11, 13h: Gustavo Gómez e Maurício jogaram pela seleção na manhã de 17/11 e estão fora;
Piquerez voltou lesionado da seleção uruguaia; Murilo, Paulinho e Jefté com problemas físicos, fora; Giay, Flaco López e Arias em voo
fretado, chegam na madrugada de quarta e tendem a começar no banco; Abel pode abandonar a linha de 3 zagueiros; Palmeiras 73 x 76 Flamengo);
Diário Celeste (17/11: 5 desfalques Murilo, Paulinho, Piquerez, Gustavo Gómez, Maurício; Giay/Flaco/Arias dúvidas; Cruzeiro x Palmeiras
quarta 18/11 20h30 Mineirão, 35ª rodada); Coluna do Fla / O Presente (Flamengo x Athletico-PR quarta 20h30 Maracanã).
Conta: Fla 76 + 3 = 79; Palmeiras perde = 73 -> 6 pontos antes de Palmeiras x Flamengo (21/11).
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
    "O Palmeiras volta ao Brasileirão amanhã com cinco desfalques.",
    "O jogo é contra o Cruzeiro, quarta, às oito e meia da noite, no Mineirão.",
    "Gustavo Gómez e Maurício jogaram hoje pela seleção e não voltam a tempo.",
    "Piquerez voltou machucado do Uruguai, e Murilo e Paulinho seguem no departamento médico.",
    "Giay, Flaco López e Arias chegam de madrugada, em voo fretado, e devem começar no banco.",
    "Com a zaga desfalcada, o Abel pode até deixar de lado o esquema com três zagueiros.",
    "E tudo isso a três pontos do líder Flamengo, que recebe o Athletico no mesmo horário.",
    "Se o Flamengo vencer e o Palmeiras perder, a diferença vai a seis pontos antes do confronto de sábado.",
]
CAPTXT = [
    "O Palmeiras volta ao Brasileirão amanhã|com 5 desfalques.",
    "O jogo é contra o Cruzeiro, quarta,|às 20h30, no Mineirão.",
    "Gustavo Gómez e Maurício jogaram hoje pela seleção|e não voltam a tempo.",
    "Piquerez voltou machucado do Uruguai, e Murilo|e Paulinho seguem no departamento médico.",
    "Giay, Flaco López e Arias chegam de madrugada,|em voo fretado, e devem começar no banco.",
    "Com a zaga desfalcada, o Abel pode até deixar|de lado o esquema com 3 zagueiros.",
    "E tudo isso a 3 pontos do líder Flamengo,|que recebe o Athletico no mesmo horário.",
    "Se o Flamengo vencer e o Palmeiras perder, a diferença|vai a 6 pontos antes do confronto de sábado.",
]
FALA_TIKTOK = "O Palmeiras segura o Cruzeiro mesmo desfalcado? Comenta sim ou não, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 7
FLASH = [7]
CHECK = [(0, 'cinco', 4), (0, 'desfalques', 4), (1, 'Cruzeiro', 4), (1, 'Mineirao', 4), (2, 'Gomez', 4), (2, 'Mauricio', 4),
         (3, 'Piquerez', 4), (3, 'Murilo', 4), (3, 'Paulinho', 4), (4, 'Giay', 4), (4, 'Arias', 4), (4, 'banco', 4),
         (5, 'tres', 4), (6, 'Flamengo', 4), (6, 'Athletico', 4), (7, 'seis', 4), (7, 'sabado', 4)]

FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')
CAP, CAP_F = time_('ATHLETICO-PR')
CRU, CRU_F = time_('CRUZEIRO')


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def pal(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=PAL, faixa=PAL_F, **kw)


def cru(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'raspado'); kw.setdefault('hair', '#111111')
    put_atleta(c, x, y, h, f, seed, cores=CRU, faixa=CRU_F, **kw)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    ci = wt(0, 'cinco') - 3; de = wt(0, 'desfalques') - 3
    pal(c, 640, 2030, 900, f, 7, num_='9', arms='shrug' if f >= de else 'cintura', expr='nervous' if f >= de else 'stern')
    put_placa(c, 'PALMEIRAS', PAL, 640, 1080, f, wt(0, 'Palmeiras') - 3, 64, -3)
    explosao(c, 640, 800, f, ci, 200, cor=(230, 70, 60))
    num(c, '5 DESFALQUES', 640, 800, f, ci, 110, -4)
    if f >= de: foco(c, 640, 1650, 460, .55 * ramp(f, de, de + 6))
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ci, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    cr = wt(1, 'Cruzeiro') - 3; qu = wt(1, 'quarta') - 3; oi = wt(1, 'oito') - 3; mi = wt(1, 'Mineirao') - 3
    if f >= qu: paste_c(c, calendario('18', 'NOV'), 640, 1200, .6 * back(ramp(f, qu, qu + 8)))
    num(c, '20H30', 640, 740, f, oi, 130, -3)
    cru(c, 290, 2060, 640, f, 13, arms='cintura', expr='stern', look=1)
    put_placa(c, 'CRUZEIRO', CRU, 290, 1340, f, cr, 44, -3)
    pal(c, 990, 2060, 640, f, 9, arms='cintura', expr='stern', look=-1, flip=True)
    put_placa(c, 'PALMEIRAS', PAL, 990, 1340, f, wt(1, 'jogo') - 3, 44, 3)
    num(c, 'MINEIRÃO', 640, 900, f, mi, 90, 2)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1380, z, 0), 'dusk'


def s2(f):
    c = estadio2('golden').copy()
    go = wt(2, 'Gomez') - 3; ma = wt(2, 'Mauricio') - 3; se = wt(2, 'selecao') - 3; te = wt(2, 'tempo') - 3
    pal(c, 360, 2040, 760, f, 4, num_='15', arms='cintura', expr='stern', look=1)
    put_placa(c, 'GUSTAVO GÓMEZ', PAL, 420, 1180, f, go, 46, -3)
    if f >= ma - 4:
        pal(c, 920, 2040, 760, f, 11, num_='18', arms='cintura', expr='neutral', look=-1, flip=True, skin=2)
        put_placa(c, 'MAURÍCIO', PAL, 900, 1180, f, ma, 46, 3)
    num(c, 'NA SELEÇÃO', 640, 720, f, se, 110, -3)
    num(c, 'NÃO VOLTAM A TEMPO', 640, 880, f, te, 76, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, te, .5)
    return c, (lerp(620, 660, smooth(f / 120)), 1400 + k * 8, z, k), 'golden'


def s3(f):
    c = estadio2('dusk').copy()
    pi = wt(3, 'Piquerez') - 3; mu = wt(3, 'Murilo') - 3; pa = wt(3, 'Paulinho') - 3; dm = wt(3, 'medico') - 3
    pal(c, 240, 2060, 620, f, 5, num_='22', arms='cheek' if f >= pi + 6 else 'hang', expr='pained', look=1, skin=0, hair='#c8a060')
    put_placa(c, 'PIQUEREZ', PAL, 240, 1380, f, pi, 48, -3)
    if f >= mu - 4:
        pal(c, 640, 2060, 620, f, 6, num_='26', arms='hang', expr='pained', skin=2)
        put_placa(c, 'MURILO', PAL, 640, 1380, f, mu, 48, 2)
    if f >= pa - 4:
        pal(c, 1020, 2060, 620, f, 8, num_='10', arms='hang', expr='pained', look=-1, flip=True, skin=4)
        put_placa(c, 'PAULINHO', PAL, 1020, 1380, f, pa, 48, -2)
    num(c, 'LESIONADOS', 640, 760, f, pi + 8, 120, -3)
    num(c, 'DEPARTAMENTO MÉDICO', 640, 930, f, dm, 70, 3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0005 * f)
    return c, (lerp(600, 680, smooth(f / 150)), 1420, z, 0), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    gi = wt(4, 'Giay') - 3; fl = wt(4, 'Flaco') - 3; ar = wt(4, 'Arias') - 3
    md = wt(4, 'madrugada') - 3; vo = wt(4, 'voo') - 3; ba = wt(4, 'banco') - 3
    xs = []
    for i, (k0, nome, seed, sk) in enumerate([(gi, 'GIAY', 3, 1), (fl, 'FLACO LÓPEZ', 10, 1), (ar, 'ARIAS', 12, 4)]):
        x = lerp(1500, 240 + 380 * i, easeOut(ramp(f, k0 - 10, k0 + 6)))
        running = f < k0 + 6
        if f >= k0 - 10:
            if running: linhas_vel(c, x, 2060, 600, f, dir=1)
            pal(c, x, 2060, 600, f, seed, arms='run' if running else ('shrug' if f >= ba else 'hang'),
                run=(f * .1) % 1 if running else -1, expr='neutral' if f < ba else 'nervous', look=-1, flip=True, skin=sk)
            put_placa(c, nome, PAL, 240 + 380 * i, 1400 - 70 * (i % 2), f, k0 + 4, 46, -3 + 3 * i)
    num(c, 'DE MADRUGADA', 640, 720, f, md, 100, -3)
    num(c, 'VOO FRETADO', 640, 880, f, vo, 100, 3)
    num(c, 'NO BANCO?', 640, 1060, f, ba, 110, -2)
    z = lerp(1.0, 1.06, smooth(f / 150))
    k = kick(f, ba, .5)
    return c, (lerp(680, 620, smooth(f / 150)), 1420 + k * 8, z, k), 'dusk'


def s5(f):
    c = estadio2('day').copy()
    za = wt(5, 'zaga') - 3; ab = wt(5, 'Abel') - 3; de = wt(5, 'deixar') - 3; tr = wt(5, 'tres') - 3
    out = ramp(f, de, de + 14)
    # 3 zagueiros -> 2 (o do meio sai)
    pal(c, lerp(380, 420, out), 2000, 640, f, 4, num_='4', arms='cintura', expr='stern', look=1)
    pal(c, lerp(900, 860, out), 2000, 640, f, 6, num_='3', arms='cintura', expr='stern', look=-1, flip=True, skin=2)
    if out < 1:
        xm = lerp(640, 1500, (out * out))
        if out > 0: linhas_vel(c, xm, 1900, 600, f, dir=-1)
        pal(c, xm, 1900, 600, f, 9, num_='?', arms='run' if out > 0 else 'cintura', run=(f * .1) % 1 if out > 0 else -1, expr='neutral')
    put_placa(c, 'ZAGA', PAL, 640, 1200, f, za, 50, -3)
    num(c, '3 ZAGUEIROS?', 640, 760, f, tr, 110, -3)
    if f >= de + 14: num(c, 'OU 2?', 640, 930, f, de + 14, 110, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    return c, (lerp(660, 620, smooth(f / 90)), 1420, z, 0), 'golden'


def s6(f):
    c = estadio2('dusk').copy()
    tr = wt(6, 'tres') - 3; fl = wt(6, 'Flamengo') - 3; at = wt(6, 'Athletico') - 3; ho = wt(6, 'horario') - 3
    tabela(c, [('1º', 'FLAMENGO', FLA, '76', True), ('2º', 'PALMEIRAS', PAL, '73', False)], 640, 1000, f, tr)
    num(c, '3 PONTOS', 640, 720, f, tr, 120, -3)
    fla(c, 300, 2060, 560, f, 5, arms='cintura', expr='stern', look=1)
    if f >= at - 4:
        put_atleta(c, 980, 2060, 560, f, 12, cores=CAP, faixa=CAP_F, skin=1, hair='#2a1a10', arms='cintura', expr='stern', look=-1, flip=True)
        put_placa(c, 'ATHLETICO-PR', CAP, 980, 1480, f, at, 44, 3)
    put_placa(c, 'FLAMENGO', FLA, 300, 1480, f, fl, 44, -3)
    num(c, 'MESMO HORÁRIO', 640, 1380, f, ho, 70, 2)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, tr, .5)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s7(f):
    c = estadio2('dusk').copy()
    ve = wt(7, 'vencer') - 3; pe = wt(7, 'perder') - 3; se = wt(7, 'seis') - 3; sa = wt(7, 'sabado') - 3
    fla(c, 300, 2040, 760, f, 3, arms='up' if f >= ve else 'cintura', expr='grin' if f >= ve else 'stern', look=1, num_='10')
    pal(c, 980, 2040, 760, f, 7, arms='shrug' if f >= pe else 'cintura', expr='pained' if f >= pe else 'stern', look=-1, flip=True, num_='9')
    put_placa(c, 'FLAMENGO', FLA, 300, 1220, f, 0, 38, -3)
    put_placa(c, 'PALMEIRAS', PAL, 980, 1220, f, 0, 38, 3)
    explosao(c, 640, 820, f, se, 200)
    num(c, '6 PONTOS', 640, 820, f, se, 130, -4)
    if f >= sa: paste_c(c, calendario('21', 'NOV'), 640, 1300, .45 * back(ramp(f, sa, sa + 8)))
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    k = kick(f, se, .7)
    return c, (640, 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('PALMEIRAS DESFALCADO', '5 FORA CONTRA O CRUZEIRO', wt(0, 'desfalques') + 4),
         1: ('CRUZEIRO x PALMEIRAS', 'QUARTA, 18/11, 20H30', wt(1, 'Mineirao') + 4),
         2: ('GÓMEZ E MAURÍCIO FORA', 'NA SELEÇÃO ATÉ HOJE', wt(2, 'tempo') + 4),
         3: ('PIQUEREZ, MURILO, PAULINHO', 'FORA POR LESÃO', wt(3, 'medico') + 4),
         4: ('GIAY, FLACO E ARIAS', 'CHEGAM DE MADRUGADA', wt(4, 'banco') + 4),
         5: ('ABEL MUDA A ZAGA?', 'SAI O ESQUEMA COM 3', wt(5, 'zagueiros') + 4),
         6: ('FLAMENGO 76 x 73 PALMEIRAS', 'FLA x ATHLETICO NO MESMO HORÁRIO', wt(6, 'horario') + 4)}
    if si == 7: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'cinco') - 3, 150, .9)
    s.ting(s.W(0, 'desfalques') - 3, .3)
    s.thunk(s.W(1, 'Cruzeiro') - 3, 160, .6)
    s.ting(s.W(1, 'Mineirao') - 3, .3)
    s.thunk(s.W(2, 'Gomez') - 3, 180, .5)
    s.thunk(s.W(2, 'Mauricio') - 3, 180, .5)
    s.thunk(s.W(3, 'Piquerez') - 3, 160, .5)
    s.thunk(s.W(3, 'Murilo') - 3, 170, .5)
    s.thunk(s.W(3, 'Paulinho') - 3, 180, .5)
    s.whoosh(s.W(4, 'Giay') - 10, .4)
    s.whoosh(s.W(4, 'Flaco') - 10, .4)
    s.whoosh(s.W(4, 'Arias') - 10, .4)
    s.ting(s.W(4, 'banco') - 3, .3)
    s.whoosh(s.W(5, 'deixar') - 2, .4)
    s.thunk(s.W(6, 'tres') - 3, 150, .7)
    s.thunk(s.W(7, 'seis') - 3, 120, 1.0)
    s.ting(s.W(7, 'sabado') - 3, .35)
