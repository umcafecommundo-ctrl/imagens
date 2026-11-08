"""anima.futebol — 08/11/2026 21h — Copa do Brasil: Palmeiras elimina o Vasco nos pênaltis e enfrenta o Grêmio na final.
Fontes (conferidas em 08/11/2026): Sportbuzz, Tribuna do Planalto, Rede 98, ND Mais (tweet oficial do Palmeiras
"Vasco (4) 2x1 (5) Palmeiras"), brasileirao.com.br: Vasco 2x1 Palmeiras em São Januário (Colidio e Puma Rodríguez;
Piquerez no 1º tempo), agregado 2x2 (ida 1x0 Palmeiras), pênaltis 5x4 Palmeiras; Carlos Miguel defendeu Lescano e
Andrés Gómez (última); final em jogo único em 06/12 no Mané Garrincha, Brasília. Final de 2020: Palmeiras campeão sobre o Grêmio.
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'COPA DO BRASIL  ·  SEMIFINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O Palmeiras está na final da Copa do Brasil, e foi nos pênaltis!",
    "Em São Januário, o Vasco precisava vencer, e Colidio abriu o placar no primeiro tempo.",
    "Piquerez empatou ainda no primeiro tempo, mas Puma Rodríguez fez dois a um na etapa final.",
    "Com o agregado em dois a dois, a vaga foi decidida nos pênaltis.",
    "Aí brilhou o goleiro Carlos Miguel: defendeu duas cobranças, e o Palmeiras venceu por cinco a quatro.",
    "Agora é Palmeiras contra Grêmio, repetindo a final de dois mil e vinte.",
    "A decisão é em jogo único, no dia seis de dezembro, em Brasília.",
]
CAPTXT = [
    "O Palmeiras está na final da Copa do Brasil,|e foi nos pênaltis!",
    "Em São Januário, o Vasco precisava vencer,|e Colidio abriu o placar no 1º tempo.",
    "Piquerez empatou ainda no 1º tempo,|mas Puma Rodríguez fez 2 a 1 na etapa final.",
    "Com o agregado em 2 a 2,|a vaga foi decidida nos pênaltis.",
    "Aí brilhou o goleiro Carlos Miguel: defendeu 2 cobranças,|e o Palmeiras venceu por 5 a 4.",
    "Agora é Palmeiras contra Grêmio,|repetindo a final de 2020.",
    "A decisão é em jogo único,|no dia 6 de dezembro, em Brasília.",
]
FALA_TIKTOK = "Quem leva a Copa do Brasil, Palmeiras ou Grêmio? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'final', 4), (0, 'penaltis', 4), (1, 'Colidio', 6), (2, 'Piquerez', 4), (2, 'Puma', 6), (3, 'agregado', 4),
         (4, 'Carlos', 4), (4, 'cinco', 4), (5, 'Gremio', 4), (6, 'Brasilia', 4)]

GRE, GRE_F = time_('GRÊMIO')
VAS, VAS_F = time_('VASCO')
PAL, PAL_F = time_('PALMEIRAS')
GOLEIRO_PAL = ('#2a5fb0', '#1b3f80', '#1b3f80')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('day').copy()
    fi = wt(0, 'final') - 3; pe = wt(0, 'penaltis') - 3
    put_trofeu(c, 900, 1150, 520, f, fi)
    num(c, 'FINAL!', 640, 700, f, fi, 170, -4)
    num(c, 'NOS PÊNALTIS', 640, 880, f, pe, 110, 3)
    put_jog(c, 400, 2010, 880, f, 1, cores=PAL, faixa=PAL_F, arms='up' if f >= fi else 'cintura',
            expr='grin' if f >= fi else 'proud', skin=0)
    put_placa(c, 'PALMEIRAS', PAL, 400, 1120, f, wt(0, 'Palmeiras') - 3, 64, -4)
    z = lerp(1.35, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, pe, .8)
    return c, (640, 1420 + k * 10, z, k), 'golden'


def s1(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    go = wt(1, 'abriu') - 4
    if f < go: num(c, 'SÃO JANUÁRIO', 640, 740, f, wt(1, 'Sao') - 3, 100, -3)
    put_goleiro(c, f, GOLEIRO_PAL, None, arms='shrug' if f >= go else 'hang', expr='shock' if f >= go else 'nervous', skin=1)
    put_jog(c, 470, 1990, 860, f, 3, cores=VAS, faixa=VAS_F, arms='up' if f >= go + 8 else 'run', kick=pulse(f, go - 5, 5),
            expr='grin' if f >= go else 'stern', skin=0, hair='#3a2618')
    put_placa(c, 'VASCO', VAS, 470, 1080, f, wt(1, 'Vasco') - 3, 62, -3)
    put_placa(c, 'COLIDIO', VAS, 520, 1230, f, wt(1, 'Colidio') - 3, 50, 3)
    rb = raio_bola(860)
    if f < go - 5: bx, by, r = 640, 1990 - rb, rb
    else:
        t = ramp(f, go - 5, go + 3)
        bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, 'GOL!', 660, 760, f, go, 170, -5)
    num(c, 'VASCO 1 x 0', 640, 930, f, go + 6, 110, 4)
    k = kick(f, go)
    return c, (lerp(600, 690, smooth(ramp(f, 0, go))), 1480 + k * 10, 1.12 * (1 + .0007 * f), k), 'golden'


def s2(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    pq = wt(2, 'empatou') - 3; pu = wt(2, 'dois') - 4
    if f < pu - 16:
        # Piquerez comemora o empate
        put_jog(c, 640, 2010, 880, f, 6, cores=PAL, faixa=PAL_F, arms='up' if f >= pq else 'cintura', expr='grin', skin=0)
        put_placa(c, 'PIQUEREZ', PAL, 640, 1120, f, wt(2, 'Piquerez') - 3, 60, -3)
        num(c, '1 x 1', 640, 760, f, pq, 160, -4)
    else:
        put_goleiro(c, f, GOLEIRO_PAL, None, arms='shrug' if f >= pu else 'hang', expr='shock' if f >= pu else 'nervous', skin=1)
        put_jog(c, 470, 1990, 860, f, 4, cores=VAS, faixa=VAS_F, arms='up' if f >= pu + 8 else 'run', kick=pulse(f, pu - 5, 5),
                expr='grin' if f >= pu else 'stern', skin=2, hair='#151515')
        put_placa(c, 'PUMA RODRÍGUEZ', VAS, 500, 1100, f, pu - 14, 46, 3)
        rb = raio_bola(860)
        if f < pu - 5: bx, by, r = 640, 1990 - rb, rb
        else:
            t = ramp(f, pu - 5, pu + 3)
            bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
        put_bola(c, bx, by, r, f)
        num(c, 'VASCO 2 x 1', 640, 760, f, pu, 120, -4)
    k = kick(f, pu, .9) + kick(f, pq, .5)
    return c, (640 + 25 * math.sin(f * .03), 1460 + k * 10, 1.1 * (1 + .0008 * f), k), 'golden'


def s3(f):
    c = estadio('dusk').copy()
    ag = wt(3, 'agregado') - 3; pe = wt(3, 'penaltis') - 3
    put_jog(c, 330, 2010, 860, f, 5, cores=VAS, faixa=VAS_F, arms='cintura', expr='stern', skin=2, hair='#151515', look=1)
    put_jog(c, 950, 2010, 860, f, 6, cores=PAL, faixa=PAL_F, arms='cintura', expr='stern', skin=0, look=-1)
    put_placa(c, 'VASCO', VAS, 330, 1120, f, 0, 62, -4)
    put_placa(c, 'PALMEIRAS', PAL, 950, 1120, f, 0, 58, 4)
    num(c, 'AGREGADO 2 x 2', 640, 700, f, ag, 110, -3)
    num(c, 'PÊNALTIS!', 640, 880, f, pe, 150, 3)
    if f >= pe: put_bola(c, 640, 2010 - raio_bola(860), raio_bola(860), 0)
    z = lerp(1.25, 1.06, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, pe, .7)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    de = wt(4, 'defendeu') - 4; ci = wt(4, 'cinco') - 3
    # cobrador do Vasco chuta, goleiro defende e a bola volta
    t = ramp(f, de - 8, de)
    pulo = pulse(f, de - 4, 12)
    put_jog(c, gx - 40 - 90 * pulo, GOL_BASE + 10 - 40 * pulo, 300, f, 21, cores=GOLEIRO_PAL, faixa=None,
            arms='up' if f >= de - 4 else 'hang', expr='grin' if f >= de else 'stern', skin=1)
    put_placa(c, 'CARLOS MIGUEL', PAL, 790, 1200, f, wt(4, 'Carlos') - 3, 44, -3)
    put_jog(c, 420, 1990, 860, f, 7, cores=VAS, faixa=VAS_F, arms='cheek' if f >= de + 2 else 'run', kick=pulse(f, de - 12, 5),
            expr='pained' if f >= de + 2 else 'stern', skin=3, hair='#111111')
    rb = raio_bola(860)
    if f < de - 8: bx, by, r = 560, 1990 - rb, rb
    elif f < de: bx, by, r = lerp(560, gx - 60, t), lerp(1990 - rb, gy, t), lerp(rb, raio_bola(300), t)
    else:
        u = ramp(f, de, de + 14)
        bx, by, r = lerp(gx - 60, 1250, u), lerp(gy, 1700, u) - 140 * math.sin(u * math.pi), lerp(raio_bola(300), raio_bola(500), u)
    if f < de + 14: put_bola(c, bx, by, r, f)
    num(c, 'DEFENDEU 2!', 640, 720, f, wt(4, 'duas') - 3, 104, -3)
    num(c, 'PALMEIRAS 5 x 4', 640, 880, f, ci, 84, 2)
    k = kick(f, de)
    return c, (lerp(630, 660, smooth(f / 90)), 1440 + k * 10, lerp(1.06, 1.14, smooth(f / 120)), k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    pa = wt(5, 'Palmeiras') - 3; gr = wt(5, 'Gremio') - 3
    px = lerp(-260, 340, easeOut(ramp(f, pa - 10, pa + 8)))
    gx_ = lerp(1500, 920, easeOut(ramp(f, gr - 10, gr + 8)))
    put_jog(c, px, 2010, 880, f, 6, cores=PAL, faixa=PAL_F, arms='cintura', expr='smug', skin=0, look=1)
    put_jog(c, gx_, 2010, 880, f, 1, cores=GRE, faixa=GRE_F, arms='cintura', expr='stern', skin=1, look=-1)
    put_placa(c, 'PALMEIRAS', PAL, 340, 1120, f, pa + 4, 58, -4)
    put_placa(c, 'GRÊMIO', GRE, 920, 1120, f, gr + 4, 64, 4)
    num(c, 'X', 640, 1500, f, gr + 6, 160)
    num(c, 'REPETECO DE 2020', 640, 760, f, wt(5, 'repetindo') - 3, 96, -3)
    z = lerp(1.25, 1.06, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    return c, (640, 1400, z, 0), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    put_trofeu(c, 640, 1180, 600, f, 0)
    num(c, 'JOGO ÚNICO', 560, 700, f, wt(6, 'unico') - 3, 110, -3)
    d0 = wt(6, 'seis') - 3
    if f >= d0: paste_c(c, calendario('06', 'DEZ'), 1010, 1000, .8 * back(ramp(f, d0, d0 + 8)))
    num(c, 'BRASÍLIA', 640, 1560, f, wt(6, 'Brasilia') - 3, 110, 3)
    put_jog(c, 250, 2040, 760, f, 6, cores=PAL, faixa=PAL_F, arms='up', expr='grin', skin=0)
    put_jog(c, 1030, 2050, 740, f, 1, cores=GRE, faixa=GRE_F, arms='up', expr='grin', skin=1)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1360, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'final') - 3, 140, 1.0)
    s.ting(s.W(0, 'penaltis') - 3, .3)
    s.thunk(s.W(1, 'abriu') - 4, 120, 1.0)
    s.ting(s.W(2, 'empatou') - 3, .3)
    s.thunk(s.W(2, 'dois') - 4, 160, .9)
    s.thunk(s.W(3, 'penaltis') - 3, 200, .7)
    s.thunk(s.W(4, 'defendeu') - 4, 140, 1.0)
    s.ting(s.W(4, 'cinco') - 3, .35)
    s.thunk(s.W(5, 'Gremio') - 3, 200, .6)
    s.ting(s.W(6, 'Brasilia') - 3, .3)
