"""anima.futebol — 10/11/2026 19h — Santos: Neymar pai, novo CEO, quer renovar com o filho.
Fontes (conferidas em 10/11/2026): CNN Brasil 06/11 (Santos anuncia Neymar pai como CEO na sexta 06/11; contrato
até dezembro de 2026, continuidade depende da eleição); Terra 07/11 (nomeação 06/11; eleição do Santos em 12/12;
continuidade se Marcelo Teixeira for reeleito); VAVEL Brasil 10/11 ("Primeiro, eu preciso deixar o Neymar feliz aqui.
Ele ficando feliz aqui, eu consigo mantê-lo aqui"; Neymar já recebeu várias propostas; contrato até 31/12/2026, sem
renovação confirmada); Goal Brasil 10/11 ("preciso manter Neymar feliz"; contrato termina em dezembro; faltam 4 rodadas).
Sem escudos/logos nem rostos reais: bonecos genéricos com plaquinhas."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SANTOS  ·  BASTIDORES'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O pai do Neymar agora manda no Santos, e a missão número um dele é segurar o próprio filho.",
    "Desde o dia seis de novembro, Neymar pai é o novo CEO do clube da Vila Belmiro.",
    "E ele foi direto: primeiro, eu preciso deixar o Neymar feliz aqui.",
    "Segundo o pai, o craque já recebeu várias propostas para sair.",
    "O problema: o contrato de Neymar termina em trinta e um de dezembro, e a renovação ainda não saiu.",
    "E no dia doze de dezembro tem eleição no Santos, e o cargo do pai depende de quem vencer.",
    "Até lá, o Santos ainda tem quatro rodadas pelo Brasileirão.",
]
CAPTXT = [
    "O pai do Neymar agora manda no Santos, e a missão|número 1 dele é segurar o próprio filho.",
    "Desde o dia 6 de novembro, Neymar pai é|o novo CEO do clube da Vila Belmiro.",
    "E ele foi direto: primeiro, eu preciso|deixar o Neymar feliz aqui.",
    "Segundo o pai, o craque já recebeu|várias propostas para sair.",
    "O problema: o contrato de Neymar termina em 31 de|dezembro, e a renovação ainda não saiu.",
    "E no dia 12 de dezembro tem eleição no Santos,|e o cargo do pai depende de quem vencer.",
    "Até lá, o Santos ainda tem|4 rodadas pelo Brasileirão.",
]
FALA_TIKTOK = "O Neymar fica no Santos em dois mil e vinte e sete? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "FICA OU SAI?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'manda', 4), (0, 'filho', 4), (1, 'CEO', 4), (2, 'feliz', 4), (3, 'propostas', 4),
         (4, 'trinta', 4), (4, 'renovacao', 4), (5, 'eleicao', 4), (5, 'vencer', 4), (6, 'quatro', 4)]

SAN, SAN_F = time_('SANTOS')
TERNO = ('#2b2f3a', '#2b2f3a', '#2b2f3a')
GEN, GEN_F = time_('GENÉRICO')


def pai(c, x, feet, h, f, **kw):
    """dirigente genérico de 'terno' escuro (não é retrato de ninguém)."""
    kw.setdefault('skin', 1); kw.setdefault('hair', '#3a3a3a')
    put_jog(c, x, feet, h, f, 3, cores=TERNO, faixa=None, **kw)


def craque(c, x, feet, h, f, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hair', '#2b1d14')
    put_jog(c, x, feet, h, f, 1, cores=SAN, faixa=SAN_F, **kw)


def put_cal(c, dia, mes, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, mes), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    ma = wt(0, 'manda') - 3; fi = wt(0, 'filho') - 3
    pai(c, 360, 2020, 860, f, arms='cintura' if f < fi else 'point', expr='proud' if f < fi else 'stern', look=1)
    craque(c, 900, 2030, 880, f, arms='hang' if f < fi else 'shrug', expr='neutral' if f < fi else 'grin', look=-1)
    put_placa(c, 'NEYMAR PAI', TERNO, 360, 1110, f, 2, 56, -3)
    put_placa(c, 'NEYMAR', SAN, 900, 1110, f, fi - 4, 60, 3)
    num(c, 'O CHEFE!', 640, 720, f, ma, 110, -4)
    num(c, 'SEGURAR O FILHO', 640, 900, f, fi, 80, 3)
    z = lerp(1.3, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, fi, .8)
    return c, (640 + 12 * math.sin(f * .05), 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    d0 = wt(1, 'seis') - 3; ce = wt(1, 'CEO') - 3; vb = wt(1, 'Vila') - 3
    put_cal(c, '06', 'NOV', 330, 930, .8, f, d0)
    num(c, 'NOVO CEO', 780, 820, f, ce, 104, 4)
    put_placa(c, 'SANTOS', SAN, 820, 1040, f, vb, 70, -3)
    pai(c, 760, 2030, 880, f, arms='up' if f >= ce else 'cintura', expr='grin' if f >= ce else 'proud', look=-1)
    put_placa(c, 'NEYMAR PAI', TERNO, 760, 1260, f, 0, 50, 2)
    cy = lerp(1300, 1420, smooth(ramp(f, 0, 90)))
    k = kick(f, ce, .7)
    return c, (640 + 14 * math.sin(f * .05), cy + k * 8, 1.05 * (1 + .0012 * f), k), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    pr = wt(2, 'primeiro') - 3; fe = wt(2, 'feliz') - 3
    num(c, '"PRIMEIRO..."', 640, 740, f, pr, 110, -3)
    num(c, 'NEYMAR FELIZ', 640, 900, f, fe, 100, 3)
    pai(c, 380, 2030, 860, f, arms='point', expr='stern', look=1)
    craque(c, 900, 2020, 840, f, arms='joinha' if f >= fe else 'hang', expr='grin' if f >= fe else 'neutral', look=-1)
    put_placa(c, 'NEYMAR PAI', TERNO, 380, 1150, f, 0, 50, -3)
    put_placa(c, 'NEYMAR', SAN, 900, 1160, f, 0, 56, 3)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, fe + 10))) * (1 + .0006 * f)
    k = kick(f, fe, .6)
    return c, (640 + 16 * math.sin(f * .04), 1430 + k * 8, z, k), 'dusk'


def s3(f):
    c = estadio('day').copy()
    pp = wt(3, 'propostas') - 3; sa = wt(3, 'sair') - 3
    craque(c, 640, 2030, 880, f, arms='shrug' if f >= pp else 'hang', expr='smug' if f >= pp else 'neutral')
    put_placa(c, 'NEYMAR', SAN, 640, 1160, f, 0, 56, 0)
    for i, (x, y, r) in enumerate(((320, 780, -8), (930, 860, 7), (360, 1010, 5), (900, 1080, -6))):
        num(c, 'PROPOSTA!', x, y, f, pp + i * 5, 78, r)
    num(c, 'PARA SAIR?', 640, 1290, f, sa, 90, -3)
    z = lerp(1.15, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0008 * f)
    k = kick(f, pp, .6)
    return c, (640, lerp(1380, 1440, smooth(ramp(f, 0, 90))) + k * 8, z, k), 'golden'


def s4(f):
    c = estadio('dusk').copy()
    co = wt(4, 'contrato') - 3; tr = wt(4, 'trinta') - 3; rn = wt(4, 'renovacao') - 3
    num(c, 'FIM DO CONTRATO', 640, 710, f, co, 88, -3)
    put_cal(c, '31', 'DEZ', 300, 930, .65, f, tr)
    num(c, 'SEM RENOVAÇÃO', 640, 1170, f, rn, 86, 3)
    craque(c, 900, 2030, 860, f, arms='cheek' if f >= rn else 'cintura', expr='nervous' if f >= rn else 'neutral', look=-1)
    k = kick(f, rn, 1.0)
    z = lerp(1.0, 1.14, smooth(ramp(f, 0, 100)))
    return c, (640, 1400 + k * 10, z, lerp(0, 3, smooth(ramp(f, rn, rn + 30))) + k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    dz = wt(5, 'doze') - 3; el = wt(5, 'eleicao') - 3; ve = wt(5, 'vencer') - 3
    put_cal(c, '12', 'DEZ', 300, 880, .7, f, dz)
    num(c, 'ELEIÇÃO!', 830, 760, f, el, 110, 4)
    put_placa(c, 'SANTOS', SAN, 830, 930, f, el + 3, 56, -3)
    num(c, 'CARGO EM JOGO', 640, 1110, f, ve, 86, -3)
    pai(c, 820, 2030, 860, f, arms='cintura' if f < ve else 'shrug', expr='stern' if f < ve else 'nervous', look=-1)
    put_placa(c, 'NEYMAR PAI', TERNO, 820, 1240, f, 0, 44, 2)
    x = lerp(620, 670, smooth(ramp(f, 0, ve + 6))) + 10 * math.sin(f * .05)
    k = kick(f, el, .7)
    return c, (x, 1430 + k * 8, 1.06 * (1 + .0012 * f), k), 'dusk'


def s6(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    qa = wt(6, 'quatro') - 3; br = wt(6, 'Brasileirao') - 4
    put_goleiro(c, f, GEN, GEN_F, arms='shrug' if f >= br else 'hang', expr='shock' if f >= br else 'nervous', skin=2, hair='#111111')
    num(c, 'FALTAM 4', 600, 760, f, qa, 120, -4)
    num(c, 'RODADAS', 600, 920, f, qa + 4, 90, 3)
    h = 860
    craque(c, 470, 1990, h, f, arms='up' if f >= br + 8 else 'run', kick=pulse(f, br - 5, 5),
           expr='grin' if f >= br + 8 else 'stern')
    rb = raio_bola(h)
    if f < br - 5: bx, by, r = 620, 1990 - rb, rb
    else:
        t = ramp(f, br - 5, br + 3)
        bx, by, r = lerp(620, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    k = kick(f, br)
    return c, (lerp(600, 660, smooth(ramp(f, 0, br))), 1460 + k * 10, 1.1 * (1 + .0007 * f), k), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.ting(s.W(0, 'manda') - 3, .3)
    s.thunk(s.W(0, 'filho') - 3, 160, .8)
    s.ting(s.W(1, 'CEO') - 3, .3)
    s.thunk(s.W(2, 'feliz') - 3, 200, .6)
    s.thunk(s.W(3, 'propostas') - 3, 180, .7)
    s.thunk(s.W(4, 'renovacao') - 3, 120, 1.0)
    s.thunk(s.W(5, 'eleicao') - 3, 160, .8)
    s.thunk(s.W(6, 'Brasileirao') - 4, 120, .9)
