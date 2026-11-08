"""anima.futebol — 08/11/2026 12h — LaLiga: Atlético de Madrid x Barcelona hoje, 1º contra 2º, valendo a liderança.
Fontes (conferidas em 08/11/2026): Lance! (jogos de hoje: Atlético de Madrid x Barcelona 17h), Al Jazeera (prévia 07/11) e
Sports Illustrated (prévia 08/11): 12ª rodada, Riyadh Air Metropolitano, Madri, 21h na Espanha (17h de Brasília);
Barcelona 1º com 30 pontos, Atlético 2º com 28; Barça venceu o Aston Villa por 3 x 0 (03/11, Champions);
Atlético perdeu para o Bayern por 0 x 2 (03/11, Champions). Raphinha renovou até 2030 (Al Jazeera, Soccernews,
Tribuna de Jundiaí); capitão do Barça (Soccernews: Flick, "o melhor capitão que o Barcelona poderia ter").
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'LALIGA  ·  12ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Primeiro contra segundo: hoje tem Atlético de Madrid e Barcelona, valendo a liderança do Espanhol.",
    "A bola rola às cinco da tarde, horário de Brasília, no estádio Metropolitano, em Madri.",
    "O Barcelona lidera com trinta pontos, e o Atlético vem logo atrás, com vinte e oito.",
    "Se o Atlético vencer, passa o Barça e assume a ponta. Se empatar, o Barça segue na frente.",
    "E tem brasileiro no centro de tudo: Raphinha, capitão do Barça, que renovou até dois mil e trinta.",
    "O Barça chega embalado, depois de vencer o Aston Villa na Champions.",
    "Já o Atlético vem de derrota para o Bayern, também na Champions.",
    "É a décima segunda rodada, e o Espanhol pode ter líder novo ainda hoje.",
]
CAPTXT = [
    "Primeiro contra segundo: hoje tem Atlético de Madrid|e Barcelona, valendo a liderança do Espanhol.",
    "A bola rola às 17h, horário de Brasília,|no estádio Metropolitano, em Madri.",
    "O Barcelona lidera com 30 pontos,|e o Atlético vem logo atrás, com 28.",
    "Se o Atlético vencer, passa o Barça e assume a ponta.|Se empatar, o Barça segue na frente.",
    "E tem brasileiro no centro de tudo: Raphinha,|capitão do Barça, que renovou até 2030.",
    "O Barça chega embalado, depois de vencer|o Aston Villa na Champions.",
    "Já o Atlético vem de derrota para o Bayern,|também na Champions.",
    "É a 12ª rodada, e o Espanhol|pode ter líder novo ainda hoje.",
]
FALA_TIKTOK = "Quem vence, Atlético ou Barcelona? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM VENCE?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'segundo', 4), (0, 'lideranca', 4), (1, 'cinco', 4), (1, 'Madri', 4), (2, 'trinta', 4), (2, 'oito', 4),
         (3, 'vencer', 6), (3, 'empatar', 4), (4, 'Raphinha', 4), (4, 'trinta', 4), (5, 'Villa', 4), (6, 'Bayern', 4),
         (7, 'novo', 4)]

ATM, ATM_F = time_('ATLÉTICO DE MADRID')
BAR, BAR_F = time_('BARCELONA')


def duelo(c, f, xa, xb, pe=2010, h=860, ea='stern', eb='stern', aa='cintura', ab='cintura'):
    put_jog(c, xa, pe, h, f, 5, cores=ATM, faixa=ATM_F, arms=aa, expr=ea, skin=0, look=1)
    put_jog(c, xb, pe, h, f, 6, cores=BAR, faixa=BAR_F, arms=ab, expr=eb, skin=2, hair='#151515', look=-1)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    at = wt(0, 'Atletico') - 3; ba = wt(0, 'Barcelona') - 3
    num(c, '1º x 2º', 640, 720, f, 0, 190, -4)
    xa = lerp(-300, 330, easeOut(ramp(f, at - 10, at + 8)))
    xb = lerp(1550, 930, easeOut(ramp(f, ba - 10, ba + 8)))
    duelo(c, f, xa, xb)
    put_placa(c, 'ATLÉTICO', ATM, 330, 1120, f, at + 4, 60, -4)
    put_placa(c, 'BARCELONA', BAR, 930, 1120, f, ba + 4, 60, 4)
    num(c, 'X', 640, 1500, f, ba + 6, 160)
    num(c, 'VALE A LIDERANÇA', 640, 900, f, wt(0, 'lideranca') - 3, 92, 3)
    z = lerp(1.32, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, ba, .7)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    num(c, 'HOJE 17H', 640, 720, f, wt(1, 'cinco') - 3, 170, -4)
    d0 = wt(1, 'rola') - 3
    if f >= d0: paste_c(c, calendario('08', 'NOV'), 640, 1180, .9 * back(ramp(f, d0, d0 + 8)))
    num(c, 'METROPOLITANO', 640, 1560, f, wt(1, 'Metropolitano') - 3, 84, 3)
    num(c, 'MADRI', 640, 1720, f, wt(1, 'Madri') - 3, 120, -3)
    rb = raio_bola(860)
    put_bola(c, lerp(-80, 260, easeOut(ramp(f, 0, 30))), 2010 - rb, rb, f)
    z = lerp(1.0, 1.12, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .03), 1300, z, 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    num(c, 'TABELA', 640, 720, f, 0, 140, -3)
    tabela(c, [('1º', 'BARCELONA', BAR, '30', True)], 640, 950, f, wt(2, 'Barcelona') - 3)
    tabela(c, [('2º', 'ATLÉTICO', ATM, '28', False)], 640, 1140, f, wt(2, 'Atletico') - 3)
    num(c, 'PONTOS', 640, 1380, f, wt(2, 'trinta') - 3, 100, 3)
    num(c, '- 2', 1000, 1560, f, wt(2, 'oito') - 3, 130, 6)
    z = lerp(1.18, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    return c, (640, 1250, z, 0), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    ve = wt(3, 'vencer') - 4; po = wt(3, 'ponta') - 3; em = wt(3, 'empatar') - 3
    put_goleiro(c, f, BAR, BAR_F, arms='shrug' if f >= ve and f < em else 'hang', expr='shock' if ve <= f < em else 'nervous', skin=2, hair='#151515')
    put_jog(c, 470, 1990, 860, f, 3, cores=ATM, faixa=ATM_F, arms='up' if ve + 8 <= f < em else 'run',
            kick=pulse(f, ve - 5, 5), expr='grin' if ve <= f < em else 'stern', skin=0)
    put_placa(c, 'ATLÉTICO', ATM, 470, 1080, f, wt(3, 'Atletico') - 3, 58, -3)
    rb = raio_bola(860)
    if f < ve - 5 or f >= em: bx, by, r = 640, 1990 - rb, rb
    else: t = ramp(f, ve - 5, ve + 3); bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    if f < em:
        num(c, 'VITÓRIA DO ATLÉTICO', 640, 720, f, ve, 70, -3)
        num(c, 'NOVO LÍDER!', 640, 880, f, po, 120, 3)
    else:
        num(c, 'EMPATE', 640, 720, f, em, 130, -3)
        num(c, 'BARÇA SEGUE 1º', 640, 880, f, em + 6, 100, 3)
    k = kick(f, ve) + kick(f, em, .6)
    return c, (lerp(620, 660, smooth(ramp(f, 0, ve))), 1480 + k * 10, 1.06 * (1 + .0007 * f), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    ra = wt(4, 'Raphinha') - 3
    put_jog(c, 640, 2030, 940, f, 6, cores=BAR, faixa=BAR_F, arms='joinha' if f >= wt(4, 'renovou') - 3 else 'cintura',
            expr='proud', skin=1, hair='#2b1d14')
    put_placa(c, 'RAPHINHA', BAR, 640, 1100, f, ra, 70, -3)
    num(c, 'BRASILEIRO', 640, 700, f, wt(4, 'brasileiro') - 3, 120, -4)
    num(c, 'CAPITÃO', 360, 880, f, wt(4, 'capitao') - 3, 84, -5)
    num(c, 'ATÉ 2030', 910, 880, f, wt(4, 'trinta') - 3, 84, 5)
    z = lerp(1.25, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0007 * f)
    k = kick(f, ra, .7)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    vi = wt(5, 'vencer') - 3
    put_jog(c, 640, 2030, 920, f, 6, cores=BAR, faixa=BAR_F, arms='up' if f >= vi else 'run', expr='grin', skin=2, hair='#151515')
    put_placa(c, 'BARCELONA', BAR, 640, 1100, f, wt(5, 'Barca') - 3, 64)
    num(c, 'EMBALADO', 640, 700, f, wt(5, 'embalado') - 3, 140, -4)
    num(c, 'VENCEU O ASTON VILLA', 640, 870, f, wt(5, 'Villa') - 3, 72, 3)
    return c, (640 + 20 * math.sin(f * .04), 1420, lerp(1.06, 1.16, smooth(f / 100)), 0), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    de = wt(6, 'derrota') - 3
    put_jog(c, 640, 2030, 920, f, 5, cores=ATM, faixa=ATM_F, arms='cheek' if f >= de else 'hang',
            expr='pained' if f >= de else 'neutral', skin=0)
    put_placa(c, 'ATLÉTICO', ATM, 640, 1100, f, wt(6, 'Atletico') - 3, 64)
    num(c, 'DERROTA', 640, 700, f, de, 150, -4)
    num(c, 'PARA O BAYERN', 640, 880, f, wt(6, 'Bayern') - 3, 100, 3)
    k = kick(f, de, .6)
    return c, (640, 1420 + k * 10, lerp(1.16, 1.06, smooth(f / 100)), lerp(0, 2, smooth(ramp(f, de, de + 20)))), 'dusk'


def s7(f):
    c = estadio('dusk').copy()
    duelo(c, f, 330, 930, pe=2030, h=820, ea='stern', eb='smug')
    put_placa(c, 'ATLÉTICO', ATM, 330, 1170, f, 0, 56, -4)
    put_placa(c, 'BARCELONA', BAR, 930, 1170, f, 0, 56, 4)
    num(c, '12ª RODADA', 640, 700, f, wt(7, 'decima') - 3, 120, -3)
    num(c, 'LÍDER NOVO?', 640, 880, f, wt(7, 'novo') - 3, 130, 3)
    rb = raio_bola(820)
    put_bola(c, 640, 2030 - rb, rb, f)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'Barcelona') - 3, 140, 1.0)
    s.ting(s.W(0, 'lideranca') - 3, .3)
    s.thunk(s.W(1, 'cinco') - 3, 160, .7)
    s.thunk(s.W(2, 'trinta') - 3, 200, .6)
    s.thunk(s.W(3, 'vencer') - 4, 120, 1.0)
    s.ting(s.W(3, 'empatar') - 3, .3)
    s.thunk(s.W(4, 'Raphinha') - 3, 140, .8)
    s.ting(s.W(5, 'Villa') - 3, .3)
    s.thunk(s.W(6, 'derrota') - 3, 220, .6)
    s.ting(s.W(7, 'novo') - 3, .3)
