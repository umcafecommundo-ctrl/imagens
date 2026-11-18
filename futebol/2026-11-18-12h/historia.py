"""anima.futebol — 18/11/2026 12h — Brasileirão: Flamengo x Athletico hoje com 8 pendurados antes da decisão contra o Palmeiras.
Fontes (conferidas em 18/11/2026): VAVEL Brasil (18/11: Flamengo x Athletico-PR quarta 18/11 20h30 Maracanã; Fla líder 76 pts,
3 à frente do Palmeiras; no limite de cartões e podem desfalcar contra o Palmeiras: Arrascaeta, Pedro, Pulgar, Léo Pereira,
Alex Sandro, Bruno Henrique, Luiz Araújo e Vitão); Diário do Rio (8 pendurados com 2 amarelos: titulares Léo Pereira, Alex Sandro,
Pulgar, Arrascaeta e Pedro; reservas Vitão, Bruno Henrique e Luiz Araújo; 3º amarelo contra o Athletico = fora de Palmeiras x Flamengo
sábado 21/11 16h30 em São Paulo); Gazeta Esportiva (18/11: 20h30 Maracanã, Fla 76 x Palmeiras 73, faltam 4 rodadas).
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
    "Oito jogadores do Flamengo entram em campo hoje pendurados.",
    "O jogo é contra o Athletico, às oito e meia da noite, no Maracanã.",
    "Entre eles, cinco titulares: Léo Pereira, Alex Sandro, Pulgar, Arrascaeta e Pedro.",
    "No banco, também estão pendurados Vitão, Bruno Henrique e Luiz Araújo.",
    "Quem levar o terceiro amarelo hoje fica fora do jogo contra o Palmeiras.",
    "O Flamengo lidera com setenta e seis pontos, três a mais que o Palmeiras, que visita o Cruzeiro no mesmo horário.",
    "E sábado, às quatro e meia da tarde, os dois se enfrentam num jogo que pode encaminhar o título.",
]
CAPTXT = [
    "8 jogadores do Flamengo|entram em campo hoje pendurados.",
    "O jogo é contra o Athletico,|às 20h30, no Maracanã.",
    "Entre eles, 5 titulares: Léo Pereira, Alex Sandro,|Pulgar, Arrascaeta e Pedro.",
    "No banco, também estão pendurados|Vitão, Bruno Henrique e Luiz Araújo.",
    "Quem levar o 3º amarelo hoje|fica fora do jogo contra o Palmeiras.",
    "O Flamengo lidera com 76 pontos, 3 a mais que o Palmeiras,|que visita o Cruzeiro no mesmo horário.",
    "E sábado, às 16h30, os dois se enfrentam|num jogo que pode encaminhar o título.",
]
FALA_TIKTOK = "Algum pendurado leva amarelo hoje? Comenta sim ou não, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Oito', 4), (0, 'pendurados', 4), (1, 'Athletico', 4), (1, 'Maracana', 4), (2, 'cinco', 4), (2, 'Pereira', 4),
         (2, 'Sandro', 4), (2, 'Pulgar', 4), (2, 'Arrascaeta', 4), (2, 'Pedro', 4), (3, 'Vitao', 4), (3, 'Henrique', 4),
         (3, 'Araujo', 4), (4, 'terceiro', 4), (4, 'Palmeiras', 4), (5, 'setenta', 4), (5, 'Cruzeiro', 4), (6, 'sabado', 4), (6, 'titulo', 4)]

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


@lru_cache(maxsize=4)
def cartao(h=300):
    """cartão amarelo desenhado (só um retângulo amarelo)."""
    w = int(h * .7); S = 2
    im = Image.new('RGBA', (w * S + 40, h * S + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([20, 20, 20 + w * S, 20 + h * S], 26, fill=(255, 214, 40, 255), outline=INK + (255,), width=12)
    d.rectangle([44, 44, 70, 20 + h * S - 30], fill=(255, 240, 150, 255))
    return im.resize((w + 20, h + 20), Image.LANCZOS)


def put_cartao(c, x, y, f, f0, h=300, rot=0, n=1):
    if f < f0: return
    s = back(ramp(f, f0, f0 + 8))
    for i in range(n):
        im = cartao(h)
        r = rot + (i - (n - 1) / 2) * 12 + 2 * math.sin(f * .1 + i)
        im = im.rotate(r, Image.BICUBIC, expand=True)
        paste_c(c, im, x + (i - (n - 1) / 2) * h * .35, y, s)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    oi = wt(0, 'Oito') - 3; pe = wt(0, 'pendurados') - 3
    fla(c, 640, 2030, 900, f, 7, num_='10', arms='shrug' if f >= pe else 'cintura', expr='nervous' if f >= pe else 'stern')
    put_placa(c, 'FLAMENGO', FLA, 640, 1080, f, wt(0, 'Flamengo') - 3, 64, -3)
    explosao(c, 640, 780, f, oi, 200, cor=(255, 214, 40))
    num(c, '8 PENDURADOS', 640, 780, f, oi, 110, -4)
    put_cartao(c, 1010, 1300, f, pe, 220, 12, 2)
    if f >= pe: foco(c, 640, 1650, 460, .5 * ramp(f, pe, pe + 6))
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, oi, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    at = wt(1, 'Athletico') - 3; oi = wt(1, 'oito') - 3; ma = wt(1, 'Maracana') - 3
    paste_c(c, calendario('18', 'NOV'), 640, 1200, .6 * back(ramp(f, 2, 10)))
    num(c, '20H30', 640, 740, f, oi, 130, -3)
    fla(c, 290, 2060, 640, f, 13, arms='cintura', expr='stern', look=1)
    put_placa(c, 'FLAMENGO', FLA, 290, 1340, f, 2, 44, -3)
    put_atleta(c, 990, 2060, 640, f, 12, cores=CAP, faixa=CAP_F, skin=1, hair='#2a1a10', arms='cintura', expr='stern', look=-1, flip=True)
    put_placa(c, 'ATHLETICO-PR', CAP, 990, 1340, f, at, 40, 3)
    num(c, 'MARACANÃ', 640, 900, f, ma, 90, 2)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1380, z, 0), 'dusk'


def s2(f):
    c = estadio2('golden').copy()
    ci = wt(2, 'cinco') - 3
    nomes = [('LÉO PEREIRA', 'Pereira', '4', 0), ('ALEX SANDRO', 'Sandro', '26', 3), ('PULGAR', 'Pulgar', '5', 1),
             ('ARRASCAETA', 'Arrascaeta', '10', 0), ('PEDRO', 'Pedro', '9', 4)]
    num(c, '5 TITULARES', 640, 720, f, ci, 120, -3)
    for i, (nome, w_, n_, sk) in enumerate(nomes):
        k0 = wt(2, w_) - 3
        x = 195 + 213 * i
        if f >= k0 - 4:
            fla(c, x, 2060, 540, f, 3 + i, num_=n_, arms='hang' if f < k0 + 6 else 'cintura', expr='nervous', skin=sk, look=0)
            put_placa(c, nome, FLA, x, 1400 - 110 * (i % 2), f, k0, 27, -3 + 3 * (i % 2))
            put_cartao(c, x + 85, 1820, f, k0 + 2, 80, 8, 2)
    z = lerp(1.04, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .00015 * f)
    return c, (lerp(630, 650, smooth(f / 160)), 1420, z, 0), 'golden'


def s3(f):
    c = estadio2('dusk').copy()
    ba = wt(3, 'banco') - 3
    nomes = [('VITÃO', 'Vitao', 2), ('BRUNO HENRIQUE', 'Henrique', 4), ('LUIZ ARAÚJO', 'Araujo', 1)]
    num(c, 'NO BANCO', 640, 720, f, ba, 120, -3)
    for i, (nome, w_, sk) in enumerate(nomes):
        k0 = wt(3, w_) - 3
        if w_ == 'Henrique': k0 = wt(3, 'Bruno') - 3
        x = 250 + 370 * i
        if f >= k0 - 4:
            fla(c, x, 2060, 600, f, 8 + i, arms='cintura', expr='nervous', skin=sk, look=1 - i)
            put_placa(c, nome, FLA, x, 1380 - 90 * (i % 2), f, k0, 40, -3 + 3 * i)
            put_cartao(c, x + 110, 1800, f, k0 + 2, 90, 8, 2)
    z = lerp(1.06, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0005 * f)
    return c, (lerp(680, 600, smooth(f / 150)), 1420, z, 0), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    te = wt(4, 'terceiro') - 3; fo = wt(4, 'fora') - 3; pa = wt(4, 'Palmeiras') - 3
    fla(c, 420, 2040, 820, f, 5, num_='10', arms='cheek' if f >= fo else 'shrug', expr='shock' if f >= fo else 'nervous', look=1)
    sub = back(ramp(f, te, te + 10))
    put_cartao(c, 930, lerp(1700, 1250, sub), f, te, 360, -8)
    num(c, '3º AMARELO', 640, 720, f, te, 120, -3)
    num(c, 'FORA!', 640, 900, f, fo, 150, 4)
    if f >= pa - 4:
        put_placa(c, 'x PALMEIRAS', PAL, 900, 1580, f, pa, 46, 3)
    z = lerp(1.0, 1.12, easeOut(ramp(f, te - 6, te + 20))) * (1 + .0004 * f)
    k = kick(f, fo, .9)
    return c, (640, 1420 + k * 10, z, k * 1.5), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    se = wt(5, 'setenta') - 3; tr = wt(5, 'tres') - 3; cr = wt(5, 'Cruzeiro') - 3; ho = wt(5, 'horario') - 3
    tabela(c, [('1º', 'FLAMENGO', FLA, '76', True), ('2º', 'PALMEIRAS', PAL, '73', False)], 640, 880, f, se)
    num(c, '3 PONTOS', 640, 720, f, tr, 120, -3)
    pal(c, 300, 1960, 520, f, 5, arms='cintura', expr='stern', look=1)
    put_placa(c, 'PALMEIRAS', PAL, 300, 1400, f, wt(5, 'Palmeiras') - 3, 40, -3)
    if f >= cr - 4:
        put_atleta(c, 980, 1960, 520, f, 12, cores=CRU, faixa=CRU_F, skin=3, hs='raspado', hair='#111111', arms='cintura', expr='stern', look=-1, flip=True)
        put_placa(c, 'CRUZEIRO', CRU, 980, 1400, f, cr, 40, 3)
    num(c, 'MESMO HORÁRIO', 640, 1300, f, ho, 70, 2)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, tr, .5)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s6(f):
    c = estadio2('day').copy()
    sa = wt(6, 'sabado') - 3; qu = wt(6, 'quatro') - 3; ti = wt(6, 'titulo') - 3
    fla(c, 320, 2040, 760, f, 3, arms='cintura', expr='stern', look=1, num_='10')
    pal(c, 960, 2040, 760, f, 7, arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    put_placa(c, 'FLAMENGO', FLA, 320, 1220, f, 0, 38, -3)
    put_placa(c, 'PALMEIRAS', PAL, 960, 1220, f, 0, 38, 3)
    if f >= sa: paste_c(c, calendario('21', 'NOV'), 640, 1000, .45 * back(ramp(f, sa, sa + 8)))
    num(c, 'SÁBADO 16H30', 640, 720, f, qu, 110, -3)
    if f >= ti:
        put_t = trofeu(); paste_c(c, put_t, 640, 1500, .45 * back(ramp(f, ti, ti + 8)))
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 60))) * (1 + .0004 * f)
    k = kick(f, ti, .7)
    return c, (640, 1400 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def OVERLAY(im, si, lf):
    D = {0: ('FLAMENGO PENDURADO', '8 JOGADORES COM 2 AMARELOS', wt(0, 'pendurados') + 4),
         1: ('FLAMENGO x ATHLETICO', 'HOJE, 20H30, MARACANÃ', wt(1, 'Maracana') + 4),
         2: ('5 TITULARES PENDURADOS', 'UM AMARELO E ESTÁ FORA', wt(2, 'Pedro') + 6),
         3: ('VITÃO, BRUNO HENRIQUE E LUIZ ARAÚJO', 'TAMBÉM PENDURADOS', wt(3, 'Araujo') + 4),
         4: ('3º AMARELO = SUSPENSÃO', 'FORA DE PALMEIRAS x FLAMENGO', wt(4, 'Palmeiras') + 4),
         5: ('FLAMENGO 76 x 73 PALMEIRAS', 'CRUZEIRO x PALMEIRAS NO MESMO HORÁRIO', wt(5, 'horario') + 4)}
    if si == 6: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'Oito') - 3, 150, .9)
    s.ting(s.W(0, 'pendurados') - 3, .3)
    s.thunk(s.W(1, 'Athletico') - 3, 160, .6)
    s.ting(s.W(1, 'Maracana') - 3, .3)
    for w in ('Pereira', 'Sandro', 'Pulgar', 'Arrascaeta', 'Pedro'):
        s.thunk(s.W(2, w) - 3, 180, .45)
    for w in ('Vitao', 'Bruno', 'Araujo'):
        s.thunk(s.W(3, w) - 3, 170, .45)
    s.whoosh(s.W(4, 'terceiro') - 4, .5)
    s.thunk(s.W(4, 'fora') - 3, 120, 1.0)
    s.thunk(s.W(5, 'setenta') - 3, 150, .7)
    s.thunk(s.W(6, 'sabado') - 3, 140, .7)
    s.ting(s.W(6, 'titulo') - 3, .35)
