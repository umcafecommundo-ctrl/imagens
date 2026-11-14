"""anima.futebol — 14/11/2026 12h — Seleção Brasileira: Japão 3x2 Brasil em Singapura, gol nos acréscimos.
Fontes (conferidas em 14/11/2026): CNN Brasil (Japão 3x2; Kubo 14/15', Nakamura ~18/19', Vini Jr. de fora da área no
1º tempo, Vini Jr. aos 30' do 2º tempo, Sakamoto nos acréscimos; Ancelotti e Raphinha expulsos por reclamação; 2ª vitória
do Japão sobre o Brasil, a 1ª foi 3x2 em out/2025; terça 17/11 7h x Singapura); Tribuna de Jundiaí (3x2, Kubo 14',
Nakamura 18', Vini 32' de fora da área, Vini empata no 2º tempo, Sakamoto nos acréscimos após contra-ataque, Ancelotti e
Raphinha expulsos reclamando de falta); SBT News (Kubo 14', Vini 32', Sakamoto acréscimos, Ancelotti e Raphinha expulsos,
reclamação de falta, terça 17/11 x Singapura); Lance! (Kubo 15', Nakamura 19', Vini 33'); Metrópoles (2ª vitória na história).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD)
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Japão venceu o Brasil por três a dois, com um gol nos acréscimos, em Singapura.",
    "Logo no começo, Kubo e Nakamura marcaram, e o Japão abriu dois a zero em menos de vinte minutos.",
    "Vini Júnior diminuiu com um chutaço de fora da área, ainda no primeiro tempo.",
    "No segundo tempo, Vini marcou de novo e empatou: dois a dois.",
    "Mas, nos acréscimos, Sakamoto fez o gol da vitória japonesa.",
    "O Brasil reclamou de falta no lance, e Ancelotti e Raphinha acabaram expulsos.",
    "É só a segunda vitória do Japão sobre o Brasil na história, e as duas por três a dois.",
    "Na terça, às sete da manhã, o Brasil fecha o ano contra Singapura.",
]
CAPTXT = [
    "O Japão venceu o Brasil por 3 a 2, com um gol|nos acréscimos, em Singapura.",
    "Logo no começo, Kubo e Nakamura marcaram, e o Japão|abriu 2 a 0 em menos de 20 minutos.",
    "Vini Júnior diminuiu com um chutaço de fora da área,|ainda no primeiro tempo.",
    "No segundo tempo, Vini marcou de novo|e empatou: 2 a 2.",
    "Mas, nos acréscimos, Sakamoto fez|o gol da vitória japonesa.",
    "O Brasil reclamou de falta no lance, e Ancelotti|e Raphinha acabaram expulsos.",
    "É só a 2ª vitória do Japão sobre o Brasil na história,|e as duas por 3 a 2.",
    "Na terça, às 7h da manhã, o Brasil fecha|o ano contra Singapura.",
]
FALA_TIKTOK = "Teve falta no gol do Japão: sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "FOI FALTA?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'tres', 4), (0, 'acrescimos', 4), (1, 'Kubo', 4), (1, 'Nakamura', 4), (1, 'zero', 4), (2, 'chutaco', 4),
         (3, 'empatou', 4), (4, 'Sakamoto', 4), (5, 'expulsos', 4), (6, 'segunda', 4), (7, 'Singapura', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
SIN, SIN_F = time_('SINGAPURA')
TEC = ('#23283a', '#23283a', '#23283a')
GKB = ('#2fa35a', '#111111', '#111111')   # goleiro do Brasil (genérico)
GKJ = ('#f2994a', '#111111', '#111111')   # goleiro do Japão (genérico)


def put_cal(c, dia, x, y, s, f, f0, mes='NOV'):
    if f >= f0: paste_c(c, calendario(dia, mes), x, y, s * back(ramp(f, f0, f0 + 8)))


@lru_cache(maxsize=2)
def cartao():
    im = Image.new('RGBA', (200, 280), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([6, 6, 194, 274], 22, fill=(214, 36, 40, 255), outline=INK + (255,), width=9)
    ImageDraw.Draw(im).line([(40, 40), (60, 200)], fill=(240, 110, 110, 255), width=12)
    return im


def jap(c, x, y, h, f, seed, **kw):
    put_jog(c, x, y, h, f, seed, cores=JAP, faixa=JAP_F, skin=0, hair='#111111', **kw)


def vini(c, x, y, h, f, **kw):
    put_jog(c, x, y, h, f, 2, cores=BRA, faixa=BRA_F, skin=3, hair='#111111', **kw)


def chute(c, f, k0, sx, gx, gy, h):
    """bola sai do pé (sx, chão) no quadro k0 e entra no gol no fundo."""
    rb = raio_bola(h)
    if f < k0: bx, by, r = sx + 60, 2030 - rb, rb
    else:
        t = ramp(f, k0, k0 + 9)
        bx = lerp(sx + 60, gx + 90, t); by = lerp(2030 - rb, gy, t) - 160 * math.sin(t * math.pi)
        r = lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    tr = wt(0, 'tres') - 3; ac = wt(0, 'acrescimos') - 3; si = wt(0, 'Singapura') - 3
    jap(c, 360, 2020, 860, f, 6, arms='up', expr='grin')
    vini(c, 940, 2000, 820, f, arms='cheek' if f >= ac else 'shrug', expr='pained', flip=True)
    put_placa(c, 'JAPÃO', JAP, 340, 1150, f, 2, 64, -4)
    put_placa(c, 'BRASIL', BRA, 940, 1180, f, 6, 64, 4)
    num(c, '3 x 2', 640, 760, f, tr, 210, -3)
    num(c, 'NOS ACRÉSCIMOS', 640, 950, f, ac, 92, 3)
    num(c, 'SINGAPURA', 640, 1500, f, si, 80, -2)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, tr, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=760)
    ku = wt(1, 'Kubo') - 3; na = wt(1, 'Nakamura') - 3; ze = wt(1, 'zero') - 3; vi = wt(1, 'vinte') - 3
    put_goleiro(c, f, GKB, None, gx=780, arms='up' if f < na + 8 else 'shrug', expr='shock', skin=1)
    jap(c, 330, 2030, 840, f, 4, arms='run' if f < ku + 10 else 'up', expr='grin', kick=pulse(f, ku - 3, 6))
    put_placa(c, 'KUBO', JAP, 330, 1110, f, ku - 2, 56, -3)
    if f >= na - 6:
        nx = lerp(1500, 900, easeOut(ramp(f, na - 6, na + 2)))
        jap(c, nx, 2030, 840, f, 8, arms='run' if f < na + 12 else 'up', expr='grin', kick=pulse(f, na - 1, 6), flip=True)
        put_placa(c, 'NAKAMURA', JAP, 920, 1110, f, na - 2, 56, 3)
    if f < na: chute(c, f, ku + 2, 330, gx, gy, 840)
    else: chute(c, f, na + 3, 840, gx, gy, 840)
    if f < ze - 2: num(c, '1 x 0', 640, 760, f, ku + 10, 150, -4)
    num(c, '2 x 0', 640, 760, f, ze, 170, -4)
    num(c, 'MENOS DE 20 MIN', 640, 930, f, vi, 86, 3)
    k = kick(f, ku + 10, .6) + kick(f, na + 10, .6)
    return c, (lerp(600, 700, smooth(f / 120)), 1430 + k * 8, 1.04 * (1 + .0008 * f), k), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=820, s=.62)
    ch = wt(2, 'chutaco') - 3; fo = wt(2, 'fora') - 3; pr = wt(2, 'primeiro') - 3
    put_goleiro(c, f, GKJ, None, gx=840, arms='up', expr='shock' if f >= ch + 6 else 'nervous', skin=0, hair='#111111')
    vini(c, 380, 2030, 880, f, arms='run' if f < ch + 10 else 'up', expr='grin', kick=pulse(f, ch - 4, 6))
    put_placa(c, 'VINI JR.', BRA, 380, 1130, f, wt(2, 'Vini') - 3, 60, -3)
    chute(c, f, ch + 1, 380, gx, gy, 880)
    num(c, 'CHUTAÇO!', 640, 720, f, ch, 150, -4)
    num(c, 'DE FORA DA ÁREA', 640, 930, f, fo, 88, 3)
    num(c, '2 x 1', 900, 1260, f, pr, 140, 4)
    k = kick(f, ch + 6)
    return c, (lerp(560, 680, smooth(f / 100)), 1430 + k * 10, lerp(1.06, 1.0, smooth(f / 60)), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    se = wt(3, 'segundo') - 3; mn = wt(3, 'novo') - 3; em = wt(3, 'empatou') - 3; dd = wt(3, 'dois') - 3
    num(c, '2º TEMPO', 640, 720, f, se, 120, -3)
    vini(c, 640, 2030, 900, f, arms='up' if f >= mn else 'run', expr='proud' if f >= mn else 'grin',
         walk=(f * .07) % 1 if f < mn else 0)
    put_placa(c, 'VINI JR.', BRA, 640, 1110, f, wt(3, 'Vini') - 3, 64, 3)
    num(c, 'DE NOVO!', 640, 920, f, mn, 110, 3)
    num(c, '2 x 2', 640, 1500, f, dd, 200, -3)
    k = kick(f, em, .8)
    z = lerp(1.1, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .001 * f)
    return c, (640 + 25 * math.sin(f * .05), 1430 + k * 10, z, k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=700)
    ac = wt(4, 'acrescimos') - 3; sa = wt(4, 'Sakamoto') - 3; vi = wt(4, 'vitoria') - 3
    put_goleiro(c, f, GKB, None, gx=720, arms='up' if f < sa + 8 else 'shrug', expr='shock', skin=1)
    jap(c, 560, 2030, 880, f, 9, arms='run' if f < sa + 12 else 'up', expr='grin', kick=pulse(f, sa - 2, 6))
    put_placa(c, 'SAKAMOTO', JAP, 560, 1040, f, sa - 4, 58, -3)
    chute(c, f, sa + 3, 560, gx, gy, 880)
    num(c, 'ACRÉSCIMOS', 640, 720, f, ac, 120, -4)
    num(c, '3 x 2', 640, 960, f, vi, 140, 3)
    k = kick(f, sa + 8)
    return c, (640 + 20 * math.sin(f * .06), 1420 + k * 12, lerp(1.0, 1.08, smooth(f / 70)), k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    fa = wt(5, 'falta') - 3; an = wt(5, 'Ancelotti') - 3; ra = wt(5, 'Raphinha') - 3; ex = wt(5, 'expulsos') - 3
    num(c, 'FALTA?', 640, 740, f, fa, 150, -4)
    put_jog(c, 330, 2010, 840, f, 9, cores=TEC, faixa=None, arms='shrug' if f < ex else 'cheek', expr='stern',
            skin=0, hair='#9a9a9a', look=1)
    put_placa(c, 'ANCELOTTI', TEC, 330, 1120, f, an, 54, -3)
    put_jog(c, 930, 2010, 840, f, 3, cores=BRA, faixa=BRA_F, skin=1, num_='11', arms='shrug' if f < ex else 'cheek',
            expr='pained', look=-1)
    put_placa(c, 'RAPHINHA', BRA, 930, 1120, f, ra, 54, 3)
    if f >= ex - 2:
        paste_c(c, cartao(), 640, 1350, .9 * back(ramp(f, ex - 2, ex + 6)))
    num(c, 'EXPULSOS', 640, 940, f, ex, 120, 3)
    k = kick(f, ex, .8)
    return c, (640, 1420 + k * 10, lerp(1.0, 1.07, smooth(f / 90)), k), 'dusk'


def s6(f):
    c = estadio('day').copy()
    se = wt(6, 'segunda') - 3; hi = wt(6, 'historia') - 3; du = wt(6, 'duas') - 3
    jap(c, 640, 2030, 880, f, 6, arms='joinha' if f < du else 'up', expr='proud')
    put_placa(c, 'JAPÃO', JAP, 640, 1060, f, wt(6, 'Japao') - 3, 64, -3)
    num(c, '2ª VITÓRIA', 640, 740, f, se, 140, -4)
    num(c, 'NA HISTÓRIA', 640, 900, f, hi, 110, 3)
    num(c, '2025 E 2026: 3 x 2', 640, 1240, f, du, 76, -2)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0008 * f)
    return c, (640 + 20 * math.sin(f * .04), 1430, z, 0), 'golden'


def s7(f):
    c = estadio('dusk').copy()
    te = wt(7, 'terca') - 3; se = wt(7, 'sete') - 3; si = wt(7, 'Singapura') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, 0, 14)))
    put_jog(c, bx, 2010, 860, f, 3, cores=BRA, faixa=BRA_F, skin=1, arms='cintura', expr='stern', look=1)
    put_placa(c, 'BRASIL', BRA, 330, 1180, f, 6, 64, -4)
    put_cal(c, '17', 640, 800, .55, f, te)
    num(c, 'TERÇA 7H', 640, 1040, f, se, 110, 3)
    if f >= si - 8:
        sx = lerp(1550, 930, easeOut(ramp(f, si - 8, si + 4)))
        put_jog(c, sx, 2010, 860, f, 7, cores=SIN, faixa=SIN_F, arms='cintura', expr='proud', skin=0, hair='#111111', look=-1)
        put_placa(c, 'SINGAPURA', SIN, 930, 1180, f, si - 2, 54, 4)
        num(c, 'X', 640, 1520, f, si, 160)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, te, .6) + kick(f, si, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'tres') - 3, 150, .8)
    s.thunk(s.W(1, 'Kubo') + 2, 140, .7)
    s.thunk(s.W(1, 'Nakamura') + 2, 140, .7)
    s.thunk(s.W(2, 'chutaco') - 2, 160, .8)
    s.ting(s.W(3, 'empatou') - 3, .35)
    s.thunk(s.W(4, 'Sakamoto') + 3, 170, .9)
    s.thunk(s.W(5, 'expulsos') - 3, 150, .7)
    s.ting(s.W(6, 'segunda') - 3, .3)
    s.ting(s.W(7, 'terca') - 3, .3)
