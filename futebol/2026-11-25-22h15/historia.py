"""anima.futebol — 25/11/2026 22h15 — QUEM CAI? · EP. 7 — Atlético-MG 1x1 Corinthians na Arena MRV (36ª rodada).
Fontes (conferidas em 25/11/2026 ~22h15, ver fatos.txt): Gazeta Esportiva, CNN Brasil, Jovem Pan, Brasileirão.com.br, VAVEL.
Thiago Borbas (Galo) expulso no 2º tempo após revisão do VAR; Kaio César de cabeça após cruzamento de Angileri;
Cuello empata nos acréscimos com chute cruzado; Corinthians 41, 15º, fora do Z4, mesma pontuação do Mirassol (1º do Z4). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  36ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Corinthians saiu do zê quatro? Olha esse empate em BH.",
    "No segundo tempo, Borbas, do Galo, foi expulso... depois do VAR.",
    "Pouco depois, Kaio César subiu... e fez de cabeça.",
    "Mas nos acréscimos, Cuello bateu cruzado... um a um.",
    "Com quarenta e um, o Timão sai do zê quatro... por pouco.",
    "O Mirassol, no zê quatro, também tem quarenta e um. O Timão se salva?",
]
CAPTXT = [
    "O Corinthians saiu do Z4?|Olha esse empate em BH.",
    "No segundo tempo, Borbas, do Galo,|foi expulso... depois do VAR.",
    "Pouco depois, Kaio César subiu...|e fez de cabeça.",
    "Mas nos acréscimos, Cuello|bateu cruzado... 1 a 1.",
    "Com 41, o Timão sai do Z4...|por pouco.",
    "O Mirassol, no Z4, também tem 41.|O Timão se salva?",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "TIMÃO SE SALVA?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [2]
CHECK = [(0, 'Corinthians', 4), (0, 'BH', 4), (1, 'Borbas', 4), (1, 'expulso', 4), (1, 'VAR', 4),
         (2, 'Kaio', 4), (2, 'cabeca', 4), (3, 'acrescimos', 4), (3, 'Cuello', 4), (3, 'um', 4),
         (4, 'um', 4), (4, 'quatro', 4), (4, 'pouco', 4), (5, 'Mirassol', 4), (5, 'um', 4), (5, 'salva', 4)]

COR, COR_F = time_('CORINTHIANS')
CAM, CAM_F = time_('ATLÉTICO-MG')
MIR, MIR_F = time_('MIRASSOL')
TORC = dict(roupa='#f2f2f2', pele='#c98e64', cabelo='#1a120c')
CLOSE_F = 36


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def cor(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=COR, faixa=COR_F, **kw)


def cam(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=CAM, faixa=CAM_F, **kw)


def s0(f):
    """quadro 0 = capa: close do torcedor corinthiano + série + pergunta; depois o vestiário do Timão."""
    c = vestiario(COR, COR_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, **TORC)
        num(c, 'QUEM CAI?', 621, 300, f, 0, 110, -2)
        num(c, 'EP. 7', 621, 440, f, 0, 100, 2)
        num(c, 'CORINTHIANS', 621, 1350, f, 0, 130, -2)
        num(c, 'SAIU DO Z4?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    bh = wt(0, 'BH') - 3
    cor(c, 640, 2090, 880, f, 5, arms='cintura' if f < bh else 'point', expr='stern' if f < bh else 'neutral',
        look=0 if f < bh else 1, num_='7')
    if f < bh - 2:
        put_placa(c, 'CORINTHIANS', COR, 640, 1000, f, CLOSE_F, 100, -3)
    else:
        num(c, 'BH', 640, 1000, f, bh, 190, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0012 * f)
    k = kick(f, bh if f >= bh else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s1(f):
    """telão: o VAR chama e Borbas, do Galo, é expulso."""
    c = telao('dusk').copy()
    bo = wt(1, 'Borbas') - 3; ex = wt(1, 'expulso') - 3; va = wt(1, 'VAR') - 3
    cam(c, 640, 2110, 980, f, 3, num_='9', skin=1,
        arms='hang' if f < ex else ('cheek' if f < va else 'shrug'),
        expr='neutral' if f < bo else ('nervous' if f < ex else 'pained'), look=-1 if f < ex else 1)
    if f < ex - 2:
        telao_txt(c, [('BORBAS', 180)], f, max(0, bo), y=700)
    elif f < va - 2:
        telao_txt(c, [('EXPULSO', 150)], f, ex, y=700, cor=(255, 80, 80))
    else:
        telao_txt(c, [('VAR', 260)], f, va, y=640)
    if ex <= f:
        # cartão vermelho subindo
        k = back(ramp(f, ex, ex + 8))
        if k > .05:
            cv = Image.new('RGBA', (160, 230), (0, 0, 0, 0)); d = ImageDraw.Draw(cv)
            d.rounded_rectangle([8, 8, 152, 222], 14, fill=(220, 30, 40, 255), outline=INK + (255,), width=8)
            paste_c(c, cv.rotate(-12, Image.BICUBIC, expand=True), 980, 1480, k)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ex, 10))
    k = kick(f, va if f >= va else (ex if f >= ex else 0), .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s2(f):
    """prancheta: cruzamento e a cabeçada de Kaio César, 1 x 0."""
    c = prancheta().copy()
    ka = wt(2, 'Kaio') - 3; ca = wt(2, 'cabeca') - 3
    for i, (x, y) in enumerate(((500, 820), (690, 780), (840, 860))):
        pino(c, x, y + 10 * math.sin(f * .2 + i), CAM, f, 2 + i * 2, '', 70)
    pino(c, 621, 610, ('#2d2d2d',), f, 0, '', 60)
    pino(c, 1060, 980, COR, f, 2, '', 62)
    pino(c, 600, 900 + 8 * math.sin(f * .2), COR, f, ka, 'K', 90)
    seta(c, (1040, 960), (620, 880), f, 4, 14, (255, 255, 255), 10)
    seta(c, (600, 880), (600, 600), f, ca, 8, (255, 216, 74), 16)
    if f < ca - 2:
        put_placa(c, 'KAIO CÉSAR', COR, 640, 1350, f, ka, 96, -2)
    else:
        explosao(c, 640, 1350, f, ca, 180)
        num(c, '0 x 1', 640, 1350, f, ca, 170, 3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ca, 10))
    k = kick(f, ca if f >= ca else 0, .8)
    return c, (640 + 12 * math.sin(f * .06), 1150 + k * 8, z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s3(f):
    """estádio ao entardecer: nos acréscimos Cuello bate cruzado e empata, 1 x 1."""
    c = estadio2('golden').copy()
    ac = wt(3, 'acrescimos') - 3; cu = wt(3, 'Cuello') - 3; um = wt(3, 'um') - 6
    ks = cu + 6
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, ('#2d2d2d', '#2d2d2d', '#2d2d2d'), None, arms='up' if f >= ks + 2 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    H = 860
    sx = lerp(820, 600, easeOut(ramp(f, 0, ks - 2)))
    if f < ks - 2: linhas_vel(c, sx, 2010, H, f, dir=1)
    cam(c, sx, 2010, H, f, 7, num_='10', skin=1, hair='#3a2a1e', flip=True,
        arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 2 else None,
        kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx - H * .13 - 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx - H * .13 - 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 40, 9)
    if f >= ks + 12: confete(c, 600, 700, f, ks + 12, 40, 400)
    if f < cu - 2:
        num(c, 'ACRÉSCIMOS', 640, 860, f, max(0, ac), 130, -2)
    elif f < ks + 8:
        put_placa(c, 'CUELLO', CAM, 640, 860, f, cu, 110, 2)
    else:
        explosao(c, 640, 860, f, ks + 8, 200)
        num(c, '1 x 1', 640, 860, f, ks + 8, 180, -3)
    z = lerp(1.15, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, ks + 8, 10))
    k = kick(f, ks + 8 if f >= ks + 8 else 0, .9)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 10, z, k), 'golden'


def s4(f):
    """a conta: 41 pontos, fora do Z4... por pouco."""
    c = conta_bg().copy()
    qu = wt(4, 'um') - 6; zq = wt(4, 'quatro') - 3; po = wt(4, 'pouco') - 3
    cor(c, 640, 2100, 920, f, 5, arms='hang' if f < zq else ('punho' if f < po else 'cheek'),
        expr='neutral' if f < zq else ('grin' if f < po else 'nervous'), look=0 if f < po else 1, num_='7')
    if f < zq - 2:
        numero_gigante(c, '41', 640, 1000, f, max(0, qu), 300, 3)
    elif f < po - 2:
        num(c, 'FORA DO Z4', 640, 1000, f, zq, 125, -3)
    else:
        num(c, 'POR POUCO', 640, 1000, f, po, 135, 3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, qu, 10))
    k = kick(f, po if f >= po else (zq if f >= zq else (qu if f >= qu else 0)), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


def s5(f):
    """estádio à noite: Mirassol também com 41 no Z4; close final na pergunta."""
    c = estadio2('dusk').copy()
    mi = wt(5, 'Mirassol') - 3; um = wt(5, 'um') - 6; sa = wt(5, 'salva') - 10
    cor(c, 400, 2030, 820, f, 6, arms='cintura', expr='stern' if f < um else 'nervous', look=1, num_='10')
    put_atleta(c, 900, 2030, 820, f, 4, cores=MIR, faixa=MIR_F, skin=3, hs='curto', hair='#151010',
               arms='cintura', expr='stern', look=-1, flip=True, num_='9')
    if f < um - 2:
        put_placa(c, 'MIRASSOL', MIR, 640, 900, f, max(0, mi), 100, 3)
    else:
        num(c, '41 x 41', 640, 900, f, um, 170, -3)
    if f >= sa:
        c = put_close(c, f, expr='preocupado', look=-1 if f < sa + 12 else 0, s=.9, **TORC)
        num(c, 'SE SALVA?', 621, 1450, f, sa, 160, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - sa)), 0), 'dusk'
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0012 * f) * (1 + .1 * pulse(f, um, 10))
    k = kick(f, um, .7) if f >= um else 0
    return c, (640, 1400 + k * 8, z, lerp(0, 2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'BH') - 3, 130, .7)
    s.apito(s.W(1, 'Borbas') - 4)
    s.thunk(s.W(1, 'expulso') - 3, 160, 1.0)
    s.thunk(s.W(1, 'VAR') - 3, 140, .8)
    s.thunk(s.W(2, 'Kaio') - 3, 130, .8)
    s.rede(s.W(2, 'cabeca') - 2)
    s.thunk(s.W(2, 'cabeca') - 3, 170, 1.0)
    s.rugido(s.W(2, 'cabeca') - 1, 1.5, .55)
    k3 = s.W(3, 'Cuello') + 3
    s.thunk(s.W(3, 'acrescimos') - 3, 130, .8)
    s.chute(k3); s.rede(k3 + 9); s.rugido(k3 + 10, 1.5, .5)
    s.thunk(k3 + 8, 170, 1.0)
    s.apito(s.W(3, 'um') + 8, longo=True)
    s.thunk(s.W(4, 'um') - 6, 170, 1.0)
    s.thunk(s.W(4, 'quatro') - 3, 140, .8)
    s.thunk(s.W(4, 'pouco') - 3, 140, .8)
    s.thunk(s.W(5, 'Mirassol') - 3, 130, .8)
    s.thunk(s.W(5, 'um') - 6, 160, 1.0)
    s.ting(s.W(5, 'salva') - 10, .35)
