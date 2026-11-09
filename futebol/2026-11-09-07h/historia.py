"""anima.futebol — 09/11/2026 07h — LaLiga: Barcelona vira sobre o Atlético de Madrid (2 x 1) no Metropolitano.
Fontes (conferidas em 09/11/2026): Lance! ("Fermín decide com dois gols e Barcelona bate o Atlético", 08/11),
El Observador (Atlético 1-2 Barcelona: Giuliano Simeone 10', Fermín López 45' e 66' com passe de Lamine Yamal;
Barça segue 3 pontos à frente do Real Madrid), La Razón de México (mesmos gols e minutos; Barça 33 pontos, líder),
ClaroSports/VAVEL (antes do jogo: Barça 30, Atlético 28; 12ª rodada, domingo 08/11, 21h na Espanha).
Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'LALIGA  ·  12ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Virada no duelo de líderes: o Barcelona venceu o Atlético de Madrid por dois a um, fora de casa.",
    "Foi na noite de domingo, no estádio Metropolitano, em Madri, primeiro contra segundo do Espanhol.",
    "O Atlético saiu na frente logo no comecinho, com gol de Giuliano Simeone.",
    "Mas, no fim do primeiro tempo, Fermín López apareceu e empatou.",
    "No segundo tempo, Lamine Yamal deu o passe, e Fermín marcou de novo: virada do Barça.",
    "Agora o Barça tem trinta e três pontos: três a mais que o Real Madrid, e cinco a mais que o Atlético.",
    "O Atlético perdeu a chance de virar líder, e quem persegue o Barça agora é o Real Madrid.",
]
CAPTXT = [
    "Virada no duelo de líderes: o Barcelona venceu|o Atlético de Madrid por 2 a 1, fora de casa.",
    "Foi na noite de domingo, no estádio Metropolitano,|em Madri, 1º contra 2º do Espanhol.",
    "O Atlético saiu na frente logo no comecinho,|com gol de Giuliano Simeone.",
    "Mas, no fim do primeiro tempo,|Fermín López apareceu e empatou.",
    "No segundo tempo, Lamine Yamal deu o passe,|e Fermín marcou de novo: virada do Barça.",
    "Agora o Barça tem 33 pontos: 3 a mais que|o Real Madrid, e 5 a mais que o Atlético.",
    "O Atlético perdeu a chance de virar líder,|e quem persegue o Barça agora é o Real Madrid.",
]
FALA_TIKTOK = "O Barça vai ser campeão espanhol? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Virada', 4), (0, 'Barcelona', 4), (0, 'um', 4), (1, 'Metropolitano', 4), (1, 'Madri', 4),
         (2, 'frente', 4), (2, 'Simeone', 4), (3, 'Fermin', 4), (3, 'empatou', 4), (4, 'passe', 4), (4, 'novo', 4),
         (4, 'virada', 4), (5, 'tres', 4), (5, 'cinco', 4), (6, 'lider', 4), (6, 'Real', 4)]

ATM, ATM_F = time_('ATLÉTICO DE MADRID')
BAR, BAR_F = time_('BARCELONA')
RMA, RMA_F = time_('REAL MADRID')
RMA_P = ('#2d3a8c', '#f2c94c', '#ffffff')  # placa do Real: azul-marinho e dourado (texto branco legível)


def chute(c, f, k0, cores, faixa, gk_cores, gk_faixa, x=470, skin=0, hair='#2b1d14', seed=3, gk_skin=0):
    """jogador na frente chuta no quadro k0; bola vai ao gol lá no fundo. Devolve True depois do gol."""
    gx, gy = put_gol(c)
    gol_ = f >= k0 + 8
    put_goleiro(c, f, gk_cores, gk_faixa, arms='shrug' if gol_ else 'hang', expr='shock' if gol_ else 'nervous', skin=gk_skin)
    put_jog(c, x, 1990, 860, f, seed, cores=cores, faixa=faixa, arms='up' if f >= k0 + 12 else 'run',
            kick=pulse(f, k0 - 5, 6), expr='grin' if gol_ else 'stern', skin=skin, hair=hair)
    rb = raio_bola(860)
    if f < k0 - 3:
        bx, by, r = x + 170, 1990 - rb, rb
    else:
        t = ramp(f, k0 - 3, k0 + 8)
        bx, by, r = lerp(x + 170, gx + 90, t), lerp(1990 - rb, gy, t) - 140 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    return gol_


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    vi = wt(0, 'Virada') - 3; ba = wt(0, 'Barcelona') - 3; pl = wt(0, 'dois') - 3
    num(c, 'VIRADA!', 640, 720, f, vi, 190, -4)
    xb = lerp(1550, 900, easeOut(ramp(f, ba - 10, ba + 8)))
    put_jog(c, 340, 2010, 820, f, 5, cores=ATM, faixa=ATM_F, arms='cheek' if f >= pl else 'cintura',
            expr='pained' if f >= pl else 'stern', skin=0, look=1)
    put_jog(c, xb, 2010, 880, f, 6, cores=BAR, faixa=BAR_F, arms='up' if f >= pl else 'run', expr='grin', skin=2, hair='#151515', look=-1)
    put_placa(c, 'ATLÉTICO', ATM, 340, 1160, f, wt(0, 'Atletico') - 3, 58, -4)
    put_placa(c, 'BARCELONA', BAR, 900, 1120, f, ba + 4, 60, 4)
    num(c, '1 x 2', 640, 920, f, pl, 170, 3)
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, pl, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    d0 = wt(1, 'domingo') - 3
    if f >= d0: paste_c(c, calendario('08', 'NOV'), 640, 1150, .85 * back(ramp(f, d0, d0 + 8)))
    num(c, 'METROPOLITANO', 640, 720, f, wt(1, 'Metropolitano') - 3, 90, -3)
    num(c, 'MADRI', 640, 880, f, wt(1, 'Madri') - 3, 120, 3)
    num(c, '1º x 2º', 640, 1560, f, wt(1, 'primeiro') - 3, 150, -4)
    rb = raio_bola(860)
    put_bola(c, lerp(-80, 300, easeOut(ramp(f, 0, 30))), 2010 - rb, rb, f)
    z = lerp(1.0, 1.12, smooth(f / 120))
    return c, (640 + 30 * math.sin(f * .03), 1300, z, 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    k0 = wt(2, 'frente') - 2
    g = chute(c, f, k0, ATM, ATM_F, BAR, BAR_F, x=430, skin=0, seed=3, gk_skin=2)
    put_placa(c, 'G. SIMEONE', ATM, 430, 1080, f, wt(2, 'Simeone') - 3, 58, -3)
    num(c, 'ATLÉTICO 1 x 0', 640, 720, f, k0 + 8, 100, -3)
    num(c, 'NO COMECINHO', 640, 880, f, wt(2, 'comecinho') - 3, 84, 3)
    k = kick(f, k0 + 8)
    return c, (lerp(600, 660, smooth(ramp(f, 0, k0))), 1480 + k * 10, 1.06 * (1 + .0007 * f), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    k0 = wt(3, 'empatou') - 6
    chute(c, f, k0, BAR, BAR_F, ATM, ATM_F, x=430, skin=0, hair='#3a2a1c', seed=7, gk_skin=1)
    put_placa(c, 'FERMÍN LÓPEZ', BAR, 470, 1080, f, wt(3, 'Fermin') - 3, 58, -3)
    num(c, 'FIM DO 1º TEMPO', 640, 720, f, wt(3, 'fim') - 3, 90, -3)
    num(c, '1 x 1', 640, 880, f, k0 + 8, 140, 3)
    k = kick(f, k0 + 8)
    return c, (lerp(600, 660, smooth(ramp(f, 0, k0))), 1480 + k * 10, 1.06 * (1 + .0007 * f), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    pa = wt(4, 'passe') - 3; k0 = wt(4, 'novo') - 4
    gol_ = f >= k0 + 8
    put_goleiro(c, f, ATM, ATM_F, arms='shrug' if gol_ else 'hang', expr='shock' if gol_ else 'nervous', skin=1)
    # Yamal (esquerda, mais atrás) passa para Fermín (frente)
    put_jog(c, 280, 1960, 800, f, 9, cores=BAR, faixa=BAR_F, arms='point' if f >= pa + 6 else 'run',
            kick=pulse(f, pa - 4, 6), expr='grin', skin=2, hair='#151515')
    put_jog(c, 640, 2010, 860, f, 7, cores=BAR, faixa=BAR_F, arms='up' if f >= k0 + 12 else 'run',
            kick=pulse(f, k0 - 5, 6), expr='grin' if gol_ else 'stern', skin=0, hair='#3a2a1c')
    put_placa(c, 'LAMINE YAMAL', BAR, 330, 1050, f, wt(4, 'Lamine') - 3, 44, -4)
    put_placa(c, 'FERMÍN', BAR, 760, 1130, f, wt(4, 'Fermin') - 3, 58, 4)
    r1 = raio_bola(800); r2 = raio_bola(860)
    if f < pa:
        bx, by, r = 420, 1960 - r1, r1
    elif f < k0 - 3:
        t = ramp(f, pa, pa + 12)
        bx, by, r = lerp(420, 800, t), lerp(1960 - r1, 2010 - r2, t), lerp(r1, r2, t)
    else:
        t = ramp(f, k0 - 3, k0 + 8)
        bx, by, r = lerp(800, gx + 90, t), lerp(2010 - r2, gy, t) - 140 * math.sin(t * math.pi), lerp(r2, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, 'NO 2º TEMPO', 640, 720, f, wt(4, 'segundo') - 3, 100, -3)
    num(c, 'VIRADA! 2 x 1', 640, 880, f, wt(4, 'virada') - 3, 120, 3)
    k = kick(f, k0 + 8)
    return c, (lerp(600, 660, smooth(ramp(f, 0, k0))), 1480 + k * 10, 1.06 * (1 + .0007 * f), k * 1.5), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    num(c, 'TABELA', 640, 720, f, 0, 140, -3)
    tabela(c, [('1º', 'BARCELONA', BAR, '33', True)], 640, 960, f, wt(5, 'Barca') - 3)
    tabela(c, [('', 'REAL MADRID', RMA_P, '30', False)], 640, 1150, f, wt(5, 'Real') - 3)
    tabela(c, [('', 'ATLÉTICO', ATM, '28', False)], 640, 1340, f, wt(5, 'Atletico') - 3)
    num(c, '33 PONTOS', 640, 1580, f, wt(5, 'pontos') - 3, 100, 3)
    z = lerp(1.18, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    return c, (640, 1250, z, 0), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    re = wt(6, 'Real') - 3; ch = wt(6, 'chance') - 3
    put_jog(c, 330, 2030, 820, f, 5, cores=ATM, faixa=ATM_F, arms='cheek' if f >= ch else 'hang',
            expr='pained' if f >= ch else 'neutral', skin=0)
    put_placa(c, 'ATLÉTICO', ATM, 330, 1180, f, 0, 56, -4)
    xr = lerp(1550, 930, easeOut(ramp(f, re - 10, re + 8)))
    put_jog(c, xr, 2030, 840, f, 4, cores=RMA, faixa=RMA_F, arms='run' if f < re + 8 else 'cintura', expr='stern',
            walk=(f * .08) % 1 if f < re + 8 else 0, skin=1, look=-1)
    put_placa(c, 'REAL MADRID', RMA_P, 890, 1180, f, re + 4, 50, 4)
    num(c, 'NÃO VIROU LÍDER', 640, 720, f, wt(6, 'lider') - 3, 90, -3)
    num(c, 'PERSEGUIDOR', 640, 880, f, wt(6, 'persegue') - 3, 110, 3)
    rb = raio_bola(820)
    put_bola(c, 640, 2030 - rb, rb, f)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'Virada') - 3, 140, 1.0)
    s.ting(s.W(0, 'dois') - 3, .3)
    s.thunk(s.W(1, 'Metropolitano') - 3, 160, .7)
    s.thunk(s.W(2, 'frente') - 2, 120, 1.0)
    s.thunk(s.W(3, 'empatou') - 6, 120, 1.0)
    s.thunk(s.W(4, 'novo') - 4, 120, 1.0)
    s.ting(s.W(4, 'virada') - 3, .3)
    s.thunk(s.W(5, 'tres') - 3, 200, .6)
    s.ting(s.W(6, 'Real') - 3, .3)
