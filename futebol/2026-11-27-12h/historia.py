"""anima.futebol — 27/11/2026 12h — QUEM CAI? · EP. 8 — O Inter pode cair já no domingo?
Fontes (conferidas em 27/11/2026, ver fatos.txt): Gazeta Esportiva (26/11, tabela e risco UFMG após a 36ª), Portal SMO/GZH
(27/11, cenários da 37ª), Terra/Gávea News (26/11), Terra/Jogada10 (24/11), Gazeta Esportiva/Corinthians (26/11).
Inter 18º com 38; Corinthians, Grêmio e Mirassol com 41; domingo 18h30 Inter x Bragantino no Beira-Rio e Corinthians x Grêmio;
se o Inter perder e Corinthians x Grêmio empatar, o Inter cai; risco de queda acima de 90% (UFMG).
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  37ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Inter pode cair já no domingo? Olha a conta.",
    "O Colorado é o décimo oitavo, com... trinta e oito pontos.",
    "Corinthians, Grêmio e Mirassol estão na frente, com... quarenta e um.",
    "Domingo, às seis e meia, o Inter recebe o Bragantino no Beira-Rio.",
    "Se perder, e Corinthians e Grêmio empatarem... o Inter cai.",
    "O risco de queda, pela UFMG, já passa de... noventa por cento.",
]
CAPTXT = [
    "O Inter pode cair já no domingo?|Olha a conta.",
    "O Colorado é o 18º,|com... 38 pontos.",
    "Corinthians, Grêmio e Mirassol|estão na frente, com... 41.",
    "Domingo, às 18h30, o Inter recebe|o Bragantino no Beira-Rio.",
    "Se perder, e Corinthians e Grêmio|empatarem... o Inter cai.",
    "O risco de queda, pela UFMG,|já passa de... 90%.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "INTER ESCAPA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Inter', 4), (0, 'domingo', 4), (0, 'conta', 4), (1, 'oitavo', 4), (1, 'oito', 4),
         (2, 'Corinthians', 4), (2, 'Gremio', 4), (2, 'Mirassol', 4), (2, 'um', 4),
         (3, 'Domingo', 4), (3, 'meia', 4), (3, 'Bragantino', 4), (3, 'Beira-Rio', 4),
         (4, 'perder', 4), (4, 'empatarem', 4), (4, 'cai', 4), (5, 'UFMG', 4), (5, 'cento', 4)]

INT, INT_F = time_('INTERNACIONAL')
COR, COR_F = time_('CORINTHIANS')
GRE, GRE_F = time_('GRÊMIO')
MIR, MIR_F = time_('MIRASSOL')
BRA, BRA_F = time_('BRAGANTINO')
TORC = dict(roupa='#c8102e', pele='#e0ac85', cabelo='#3a2a1e')
CLOSE_F = 36


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def s0(f):
    """quadro 0 = capa: close do torcedor colorado em choque + série + pergunta; depois vestiário do Inter."""
    c = vestiario(INT, INT_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, look=0, **TORC)
        num(c, 'QUEM CAI?', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 8', 621, 440, f, 0, 100, 2)
        num(c, 'INTER CAI', 621, 1350, f, 0, 150, -2)
        num(c, 'DOMINGO?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    do = wt(0, 'domingo') - 3; co = wt(0, 'conta') - 3
    inter(c, 640, 2090, 900, f, 5, num_='10', arms='cheek' if f < co else 'point',
          expr='nervous' if f < co else 'stern', look=-1 if f < co else 1)
    if f < co - 2:
        put_placa(c, 'INTERNACIONAL', INT, 640, 1000, f, CLOSE_F, 96, -3)
    else:
        num(c, 'A CONTA', 640, 1000, f, co, 170, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, co, 10))
    k = kick(f, co if f >= co else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s1(f):
    """telão da tabela: 18º e depois 38 pontos; jogador do Inter lamenta."""
    c = telao('dusk').copy()
    oi = wt(1, 'oitavo') - 3; to = wt(1, 'oito') - 3
    inter(c, 640, 2110, 980, f, 3, num_='9', skin=3, hair='#151010',
          arms='hang' if f < oi else ('cintura' if f < to else 'cheek'),
          expr='neutral' if f < oi else ('nervous' if f < to else 'pained'), look=1 if f < to else -1)
    if f < to - 2:
        telao_txt(c, [('18º', 260)], f, max(0, oi), y=680, cor=(255, 80, 80))
    else:
        telao_txt(c, [('38', 280)], f, to, y=660)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, to, 10))
    k = kick(f, to if f >= to else max(oi, 0), .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """estádio de dia: Corinthians, Grêmio e Mirassol entram um a um; depois 41."""
    c = estadio2('day').copy()
    co = wt(2, 'Corinthians') - 3; gr = wt(2, 'Gremio') - 3; mi = wt(2, 'Mirassol') - 3; um = wt(2, 'um') - 6
    if f >= co:
        put_atleta(c, 300, 2020, 760, f, 2, cores=COR, faixa=COR_F, skin=2, hs='curto', hair='#2a1a10',
                   arms='punho' if f >= um else 'cintura', expr='grin' if f >= um else 'stern', look=1, num_='7')
    if f >= gr:
        put_atleta(c, 640, 2060, 820, f, 4, cores=GRE, faixa=GRE_F, skin=1, hs='curto', hair='#3a2a1e',
                   arms='punho' if f >= um else 'cintura', expr='grin' if f >= um else 'stern', look=0, num_='10')
    if f >= mi:
        put_atleta(c, 980, 2020, 760, f, 6, cores=MIR, faixa=MIR_F, skin=3, hs='curto', hair='#151010', flip=True,
                   arms='punho' if f >= um else 'cintura', expr='grin' if f >= um else 'stern', look=-1, num_='9')
    if f < gr - 2:
        if f >= co: put_placa(c, 'CORINTHIANS', COR, 640, 900, f, co, 96, -3)
    elif f < mi - 2:
        put_placa(c, 'GRÊMIO', GRE, 640, 900, f, gr, 110, 3)
    elif f < um - 2:
        put_placa(c, 'MIRASSOL', MIR, 640, 900, f, mi, 104, -3)
    else:
        explosao(c, 640, 900, f, um, 200)
        numero_gigante(c, '41', 640, 900, f, um, 280, 3)
    z = lerp(1.16, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, um, 10))
    k = kick(f, um if f >= um else max(0, mi if f >= mi else (gr if f >= gr else co)), .6)
    return c, (lerp(600, 680, smooth(f / 120)), 1440 + k * 8, z, k), 'day'


def s3(f):
    """estádio ao entardecer: Inter x Bragantino frente a frente; DOMINGO, 18H30, BRAGANTINO, BEIRA-RIO."""
    c = estadio2('golden').copy()
    do = wt(3, 'Domingo') - 3; me = wt(3, 'meia') - 3; br = wt(3, 'Bragantino') - 3; be = wt(3, 'Beira-Rio') - 3
    inter(c, 380, 2040, 860, f, 7, num_='5', arms='cintura' if f < br else 'point', expr='stern', look=1)
    put_atleta(c, 900, 2040, 860, f, 9, cores=BRA, faixa=BRA_F, skin=2, hs='curto', hair='#151010', flip=True,
               arms='cintura' if f < br else 'punho', expr='neutral' if f < br else 'grin', look=-1, num_='8')
    if f < me - 2:
        num(c, 'DOMINGO', 640, 880, f, max(0, do), 160, -3)
    elif f < br - 2:
        num(c, '18H30', 640, 880, f, me, 190, 3)
    elif f < be - 2:
        put_placa(c, 'BRAGANTINO', BRA, 640, 880, f, br, 100, -2)
    else:
        num(c, 'BEIRA-RIO', 640, 880, f, be, 140, 3)
    z = lerp(1.2, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .08 * pulse(f, me, 10)) * (1 + .08 * pulse(f, be, 10))
    k = kick(f, be if f >= be else (br if f >= br else (me if f >= me else 0)), .7)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 10, z, k), 'golden'


def s4(f):
    """prancheta: Inter perde (X), Corinthians e Grêmio empatam (=) ... CAI."""
    c = prancheta().copy()
    pe = wt(4, 'perder') - 3; em = wt(4, 'empatarem') - 3; ca = wt(4, 'cai') - 3
    pino(c, 360, 1300, INT, f, 0, 'I', 100)
    pino(c, 760, 1260, COR, f, 0, 'C', 90)
    pino(c, 980, 1260, GRE, f, 0, 'G', 90)
    if f >= pe:
        k = back(ramp(f, pe, pe + 8))
        if k > .05:
            xm = Image.new('RGBA', (220, 220), (0, 0, 0, 0)); d = ImageDraw.Draw(xm)
            d.line([30, 30, 190, 190], fill=(220, 30, 40, 255), width=34); d.line([190, 30, 30, 190], fill=(220, 30, 40, 255), width=34)
            paste_c(c, xm, 360, 1300, k)
    if f >= em:
        seta(c, (790, 1420), (950, 1420), f, em, 8, (255, 255, 255), 12)
        seta(c, (950, 1420), (790, 1420), f, em, 8, (255, 255, 255), 12)
    if f < em - 2:
        if f >= pe: num(c, 'SE PERDER', 640, 860, f, pe, 140, -3)
    elif f < ca - 2:
        num(c, 'EMPATE', 640, 860, f, em, 170, 3)
    else:
        explosao(c, 640, 860, f, ca, 220, (230, 50, 50))
        num(c, 'CAI', 640, 860, f, ca, 240, -3)
    z = lerp(1.08, .98, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ca, 10)) * (1 + .06 * pulse(f, em, 10))
    k = kick(f, ca if f >= ca else (em if f >= em else 0), .9)
    return c, (640 + 35 * math.sin(f * .07), 1180 + k * 8 - 1.5 * f, z * (1 + .003 * f), lerp(0, -2, smooth(ramp(f, 0, 60))) + k + 1.2 * math.sin(f * .05)), 'day'


def s5(f):
    """conta: close do torcedor colorado preocupado -> medo; MAIS DE 90%."""
    c = conta_bg().copy()
    uf = wt(5, 'UFMG') - 3; ce = wt(5, 'cento') - 8
    c = put_close(c, f, expr='curioso' if f < uf else ('preocupado' if f < ce else 'medo'), s=.95,
                  look=(1 if f < uf else -1) if f < ce else 0, **TORC)
    if f < ce - 2:
        num(c, 'RISCO', 621, 720, f, max(0, uf), 170, -2)
    else:
        num(c, '+90%', 621, 720, f, ce, 200, 3)
    z = (1.05 + .004 * f) * (1 + .1 * pulse(f, ce, 10)) * (1 + .08 * pulse(f, uf, 10))
    return c, (621 + 30 * math.sin(f * .08), 1104 + 20 * math.cos(f * .06), z, (kick(f, ce, .6) if f >= ce else 0) + 1.5 * math.sin(f * .05)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'conta') - 3, 140, .8)
    s.thunk(s.W(1, 'oitavo') - 3, 150, .9)
    s.thunk(s.W(1, 'oito') - 3, 160, 1.0)
    s.thunk(s.W(2, 'Corinthians') - 3, 120, .7)
    s.thunk(s.W(2, 'Gremio') - 3, 120, .7)
    s.thunk(s.W(2, 'Mirassol') - 3, 120, .7)
    s.thunk(s.W(2, 'um') - 6, 170, 1.0)
    s.apito(s.W(3, 'Domingo') - 4)
    s.thunk(s.W(3, 'meia') - 3, 150, .9)
    s.thunk(s.W(3, 'Bragantino') - 3, 130, .8)
    s.thunk(s.W(3, 'Beira-Rio') - 3, 140, .8)
    s.thunk(s.W(4, 'perder') - 3, 150, .9)
    s.thunk(s.W(4, 'empatarem') - 3, 150, .9)
    s.apito(s.W(4, 'cai') - 4, longo=True)
    s.thunk(s.W(4, 'cai') - 3, 180, 1.0)
    s.ting(s.W(4, 'cai') - 2, .35)
    s.thunk(s.W(5, 'UFMG') - 3, 130, .8)
    s.thunk(s.W(5, 'cento') - 8, 170, 1.0)
