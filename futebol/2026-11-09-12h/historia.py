"""anima.futebol — 09/11/2026 12h — Série B: Novorizontino garante acesso inédito à Série A.
Fontes (conferidas em 09/11/2026): VAVEL Brasil (07/11 e 08/11), Gazeta do Paraná, Bahia Notícias, Correio (24horas),
Diário de Goiás, Antenados no Futebol: Novorizontino 2x1 Fortaleza, sábado 07/11, Estádio Jorge Ismael de Biasi (Jorjão),
37ª rodada; Nicolas Careca (Novorizontino) expulso aos 7'; Paulo Baya abre o placar para o Fortaleza logo depois;
Lucas Emanoel (Fortaleza) expulso por volta dos 20'; Matheus Bianqui empata no 1º tempo (27'/28');
Luís Oyama vira no 2º tempo; Novorizontino 70 pts, líder, 2 à frente do Juventude (68); acesso inédito com 1 rodada
de antecedência; clube fundado em 2010 (16 anos); última rodada: Criciúma x Novorizontino, sábado 14/11, fora de casa.
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'SÉRIE B  ·  37ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Novorizontino vai jogar a Série A pela primeira vez na história.",
    "Foi no sábado, no Jorjão, no interior de São Paulo, contra o Fortaleza.",
    "Logo aos sete minutos, o Novorizontino teve um expulso, e o Fortaleza abriu o placar com Paulo Baya.",
    "Mas o Fortaleza também perdeu um jogador, e Matheus Bianqui empatou ainda no primeiro tempo.",
    "No segundo tempo, Luís Oyama virou o jogo: dois a um.",
    "Com setenta pontos, o Tigre do Vale lidera a Série B e subiu com uma rodada de antecedência.",
    "E é um clube jovem: foi fundado em dois mil e dez, só dezesseis anos atrás.",
    "Agora, no sábado, contra o Criciúma, o Novorizontino joga pelo título da Série B.",
]
CAPTXT = [
    "O Novorizontino vai jogar a Série A|pela primeira vez na história.",
    "Foi no sábado, no Jorjão, no interior|de São Paulo, contra o Fortaleza.",
    "Logo aos 7 minutos, o Novorizontino teve um expulso,|e o Fortaleza abriu o placar com Paulo Baya.",
    "Mas o Fortaleza também perdeu um jogador, e Matheus|Bianqui empatou ainda no primeiro tempo.",
    "No segundo tempo, Luís Oyama|virou o jogo: 2 a 1.",
    "Com 70 pontos, o Tigre do Vale lidera a Série B|e subiu com uma rodada de antecedência.",
    "E é um clube jovem: foi fundado em 2010,|só 16 anos atrás.",
    "Agora, no sábado, contra o Criciúma, o Novorizontino|joga pelo título da Série B.",
]
FALA_TIKTOK = "O Novorizontino vai se dar bem na Série A? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = [4]
CHECK = [(0, 'primeira', 4), (1, 'Jorjao', 4), (1, 'Fortaleza', 4), (2, 'expulso', 4), (2, 'Baya', 6), (3, 'Bianqui', 6),
         (4, 'virou', 6), (5, 'setenta', 4), (5, 'subiu', 4), (6, 'dezesseis', 4), (7, 'Criciuma', 4), (7, 'titulo', 4)]

NOV, NOV_F = time_('NOVORIZONTINO')
FOR, FOR_F = time_('FORTALEZA')
JUV, _ = time_('JUVENTUDE')
CRI, CRI_F = time_('CRICIÚMA')


@lru_cache(maxsize=2)
def cartao():
    im = Image.new('RGBA', (170, 240), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, 164, 234], 18, fill=(214, 30, 40, 255), outline=INK + (255,), width=8)
    d.rectangle([24, 22, 60, 120], fill=(240, 80, 80, 255))
    return im


def put_cartao(c, x, y, f, f0, rot=-10):
    if f < f0: return
    im = cartao().rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y - 40 * (1 - back(ramp(f, f0, f0 + 8))), back(ramp(f, f0, f0 + 8)))


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def chute(c, f, go, x0, feet, h, gx, gy):
    rb = raio_bola(h)
    if f < go - 5: bx, by, r = x0, feet - rb, rb
    else:
        t = ramp(f, go - 5, go + 3)
        bx, by, r = lerp(x0, gx + 90, t), lerp(feet - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('day').copy()
    pr = wt(0, 'primeira') - 3
    put_trofeu(c, 950, 1180, 440, f, wt(0, 'Serie') - 3)
    num(c, 'SÉRIE A!', 640, 720, f, wt(0, 'Serie') - 3, 180, -4)
    num(c, '1ª VEZ NA HISTÓRIA', 640, 900, f, pr, 80, 3)
    put_jog(c, 420, 2010, 880, f, 1, cores=NOV, faixa=NOV_F, arms='up', expr='grin', skin=1)
    put_placa(c, 'NOVORIZONTINO', NOV, 470, 1080, f, 0, 54, -4)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, pr, .8)
    return c, (640, 1420 + k * 10, z, k), 'golden'


def s1(f):
    c = estadio('day').copy()
    jo = wt(1, 'Jorjao') - 3; fo = wt(1, 'Fortaleza') - 3
    d0 = wt(1, 'sabado') - 3
    if f >= d0: paste_c(c, calendario('07', 'NOV'), 640, 760, .62 * back(ramp(f, d0, d0 + 8)))
    num(c, 'JORJÃO', 640, 960, f, jo, 110, -3)
    nx = lerp(-260, 330, easeOut(ramp(f, 0, 18)))
    fx = lerp(1500, 930, easeOut(ramp(f, fo - 10, fo + 8)))
    put_jog(c, nx, 2010, 860, f, 1, cores=NOV, faixa=NOV_F, arms='cintura', expr='stern', skin=1, look=1)
    put_jog(c, fx, 2010, 860, f, 2, cores=FOR, faixa=FOR_F, arms='cintura', expr='stern', skin=3, hair='#111111', look=-1)
    put_placa(c, 'FORTALEZA', FOR, 900, 1090, f, fo + 4, 50, 4)
    put_placa(c, 'NOVORIZONTINO', NOV, 360, 1090, f, 4, 46, -4)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90)))
    return c, (640 + 20 * math.sin(f * .03), 1380, z, 0), 'golden'


def s2(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    ex = wt(2, 'expulso') - 3; go = wt(2, 'Baya') - 4
    put_goleiro(c, f, NOV, NOV_F, arms='shrug', expr='shock' if f >= go else 'nervous', skin=0)
    if f < go - 12:
        put_jog(c, 380, 2010, 860, f, 1, cores=NOV, faixa=NOV_F, arms='cheek' if f >= ex else 'hang', expr='shock' if f >= ex else 'neutral', skin=1)
        put_cartao(c, 640, 1050, f, ex, -10)
        num(c, '7 MIN', 640, 760, f, wt(2, 'sete') - 3, 150, -4)
        num(c, 'EXPULSO!', 900, 1260, f, ex, 110, 5)
    else:
        put_jog(c, 470, 1990, 860, f, 2, cores=FOR, faixa=FOR_F, arms='up' if f >= go + 8 else 'run', kick=pulse(f, go - 5, 5),
                expr='grin' if f >= go else 'stern', skin=3, hair='#111111')
        put_placa(c, 'PAULO BAYA', FOR, 470, 1110, f, go - 10, 52, -3)
        chute(c, f, go, 640, 1990, 860, gx, gy)
        num(c, '0 x 1', 640, 760, f, go + 2, 160, 4)
    k = kick(f, go) + kick(f, ex, .6)
    return c, (640, 1470 + k * 10, 1.1 * (1 + .0008 * f), k), 'golden'


def s3(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    pe = wt(3, 'perdeu') - 3; go = wt(3, 'Bianqui') - 4
    put_goleiro(c, f, FOR, FOR_F, arms='shrug', expr='shock' if f >= go else 'nervous', skin=3, hair='#111111')
    put_cartao(c, 250, 820, f, pe, 10)
    num(c, '10 x 10', 640, 760, f, pe + 4, 120, -3)
    put_jog(c, 500, 1990, 860, f, 3, cores=NOV, faixa=NOV_F, arms='up' if f >= go + 8 else 'run', kick=pulse(f, go - 5, 5),
            expr='grin' if f >= go else 'stern', skin=2, hair='#3a2416')
    put_placa(c, 'MATHEUS BIANQUI', NOV, 500, 1110, f, wt(3, 'Matheus') - 3, 46, -3)
    chute(c, f, go, 680, 1990, 860, gx, gy)
    num(c, '1 x 1', 900, 940, f, go + 2, 150, 4)
    k = kick(f, go)
    return c, (lerp(600, 680, smooth(ramp(f, 0, go))), 1470 + k * 10, 1.1 * (1 + .0008 * f), k), 'golden'


def s4(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    go = wt(4, 'virou') - 4
    put_goleiro(c, f, FOR, FOR_F, arms='cheek' if f >= go else 'hang', expr='pained' if f >= go else 'nervous', skin=3, hair='#111111')
    num(c, '2º TEMPO', 640, 760, f, wt(4, 'segundo') - 3, 120, -3)
    put_jog(c, 480, 1990, 860, f, 4, cores=NOV, faixa=NOV_F, arms='up' if f >= go + 8 else 'run', kick=pulse(f, go - 5, 5),
            expr='grin' if f >= go else 'stern', skin=1, hair='#111111')
    put_placa(c, 'LUÍS OYAMA', NOV, 480, 1110, f, wt(4, 'Luis') - 3, 52, -3)
    chute(c, f, go, 660, 1990, 860, gx, gy)
    num(c, 'VIRADA!', 640, 760 if f >= go else 99999, f, go, 170, -5)
    num(c, '2 x 1', 900, 940, f, wt(4, 'dois') - 3, 160, 4)
    k = kick(f, go)
    return c, (640 + 20 * math.sin(f * .04), 1470 + k * 10, 1.1 * (1 + .0008 * f), k), 'golden'


def s5(f):
    c = estadio('dusk').copy()
    num(c, 'SÉRIE B', 640, 720, f, 0, 130, -3)
    tabela(c, [('1º', 'NOVORIZONTINO', NOV, '70', True), ('2º', 'JUVENTUDE', JUV, '68', False)], 640, 960, f, wt(5, 'setenta') - 3)
    num(c, 'ACESSO!', 640, 1440, f, wt(5, 'subiu') - 3, 170, -4)
    num(c, 'FALTA 1 RODADA', 640, 1640, f, wt(5, 'rodada') - 3, 96, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    return c, (640, 1250, z, 0), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    num(c, 'FUNDADO EM 2010', 640, 740, f, wt(6, 'fundado') - 3, 84, -3)
    num(c, '16 ANOS', 640, 940, f, wt(6, 'dezesseis') - 3, 190, 4)
    put_jog(c, 640, 2030, 900, f, 5, cores=NOV, faixa=NOV_F, arms='joinha', expr='proud', skin=0)
    put_placa(c, 'NOVORIZONTINO', NOV, 640, 1160, f, wt(6, 'clube') - 3, 60, 3)
    return c, (640 + 20 * math.sin(f * .04), 1400, lerp(1.06, 1.16, smooth(f / 100)), 0), 'dusk'


def s7(f):
    c = estadio('dusk').copy()
    d0 = wt(7, 'sabado') - 3
    if f >= d0: paste_c(c, calendario('14', 'NOV'), 640, 820, .6 * back(ramp(f, d0, d0 + 8)))
    put_trofeu(c, 640, 1290, 380, f, wt(7, 'titulo') - 3)
    put_jog(c, 340, 1920, 700, f, 1, cores=NOV, faixa=NOV_F, arms='cintura', expr='stern', skin=1, look=1)
    put_jog(c, 940, 1920, 700, f, 2, cores=CRI, faixa=CRI_F, arms='cintura', expr='stern', skin=2, hair='#3a3d46', look=-1)
    put_placa(c, 'CRICIÚMA', CRI, 940, 1160, f, wt(7, 'Criciuma') - 3, 46, 4)
    put_placa(c, 'NOVORIZONTINO', NOV, 360, 1160, f, wt(7, 'Novorizontino') - 3, 40, -4)
    z = lerp(1.04, 1.12, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1330, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'primeira') - 3, 140, 1.0)
    s.ting(s.W(1, 'Jorjao') - 3, .3)
    s.thunk(s.W(2, 'expulso') - 3, 160, .8)
    s.thunk(s.W(2, 'Baya') - 4, 120, 1.0)
    s.thunk(s.W(3, 'Bianqui') - 4, 120, 1.0)
    s.thunk(s.W(4, 'virou') - 4, 120, 1.0)
    s.ting(s.W(5, 'subiu') - 3, .35)
    s.thunk(s.W(6, 'dezesseis') - 3, 200, .6)
    s.ting(s.W(7, 'titulo') - 3, .3)
