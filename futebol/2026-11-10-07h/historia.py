"""anima.futebol — 10/11/2026 07h — Seleção Brasileira: última Data Fifa de 2026 em Singapura.
Fontes (conferidas em 10/11/2026): Metrópoles (Ancelotti; jogos no Estádio Nacional de Singapura; Japão 14/11 7h15 e
Singapura 17/11 7h de Brasília; Jonathan Jesus/Cruzeiro e André Luiz/Corinthians na lista; Danilo Santos/Botafogo cortado
por dores); Imirante (mesmas datas/horários; CBF deixou Flamengo e Palmeiras de fora pela reta final do Brasileirão,
que volta em 18/11); Rádio Clube do Pará (grupo se reunindo em Singapura desde 08/11, 1º treino 09/11; André Luiz e
Jonathan Jesus apresentados); Campo Grande News (nenhum jogador de Fla/Palmeiras na seleção brasileira; Jonathan Jesus
e André na lista); IstoÉ (primeira vez na história contra Singapura).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD)
SELO = 'SELEÇÃO BRASILEIRA  ·  DATA FIFA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Sem nenhum jogador do Flamengo e do Palmeiras, a Seleção Brasileira fecha o ano do outro lado do mundo.",
    "O grupo de Ancelotti já treina em Singapura, para os dois últimos jogos do ano.",
    "No sábado, às sete e quinze da manhã de Brasília, o Brasil encara o Japão.",
    "E na terça seguinte, às sete, enfrenta Singapura pela primeira vez na história.",
    "A CBF poupou Flamengo e Palmeiras, que brigam pelo título do Brasileirão.",
    "Na lista, caras novas, como o zagueiro Jonathan Jesus, do Cruzeiro, e o volante André Luiz, do Corinthians.",
    "Mas já teve baixa: o volante Danilo Santos, do Botafogo, foi cortado.",
    "Depois dos amistosos, o Brasileirão volta no dia dezoito, com a reta final pelo título.",
]
CAPTXT = [
    "Sem nenhum jogador do Flamengo e do Palmeiras,|a Seleção Brasileira fecha o ano do outro lado do mundo.",
    "O grupo de Ancelotti já treina em Singapura,|para os 2 últimos jogos do ano.",
    "No sábado, às 7h15 de Brasília,|o Brasil encara o Japão.",
    "E na terça seguinte, às 7h, enfrenta Singapura|pela primeira vez na história.",
    "A CBF poupou Flamengo e Palmeiras,|que brigam pelo título do Brasileirão.",
    "Na lista, caras novas, como o zagueiro Jonathan Jesus, do Cruzeiro,|e o volante André Luiz, do Corinthians.",
    "Mas já teve baixa: o volante Danilo Santos,|do Botafogo, foi cortado.",
    "Depois dos amistosos, o Brasileirão volta no dia 18,|com a reta final pelo título.",
]
FALA_TIKTOK = "O Brasil ganha do Japão? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Flamengo', 4), (0, 'Palmeiras', 4), (0, 'mundo', 4), (1, 'Singapura', 4), (2, 'Japao', 4),
         (3, 'primeira', 4), (4, 'poupou', 4), (5, 'Jonathan', 4), (5, 'Andre', 4), (6, 'cortado', 4), (7, 'dezoito', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
SIN, SIN_F = time_('SINGAPURA')
FLA, FLA_F = time_('FLAMENGO')
PAL, PAL_F = time_('PALMEIRAS')
CRU_, _ = time_('CRUZEIRO')
COR, _ = time_('CORINTHIANS')
BOT, _ = time_('BOTAFOGO')
TEC = ('#23283a', '#23283a', '#23283a')   # técnico de agasalho escuro (genérico)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def put_cal(c, dia, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, 'NOV'), x, y, s * back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    fl = wt(0, 'Flamengo') - 3; pa = wt(0, 'Palmeiras') - 3; se = wt(0, 'Selecao') - 3; mu = wt(0, 'mundo') - 3
    sai = ramp(f, se, se + 10) ** 2
    put_placa(c, 'FLAMENGO', FLA, 420 - 800 * sai, 840, f, fl, 52, -5)
    put_placa(c, 'PALMEIRAS', PAL, 860 + 800 * sai, 840, f, pa, 52, 5)
    if f < se + 4: num(c, 'FORA', 640, 1010, f, pa + 6, 150, -6)
    if f >= se - 4:
        y = lerp(1400, 2020, easeOut(ramp(f, se - 4, se + 6)))
        put_jog(c, 640, y, 880, f, 1, cores=BRA, faixa=BRA_F, arms='up' if f >= mu else 'cintura', expr='grin', skin=2, num_='10')
        put_placa(c, 'BRASIL', BRA, 640, 1130, f, se + 2, 70, -3)
    num(c, 'OUTRO LADO', 640, 720, f, mu, 100, -3); num(c, 'DO MUNDO', 640, 860, f, mu + 3, 100, 3)
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, se + 4, .8)
    return c, (640, 1430 + k * 10, z, k), 'dusk'


def s1(f):
    c = CEN('cidade', 'dusk').copy()
    an = wt(1, 'Ancelotti') - 3; si = wt(1, 'Singapura') - 3; do = wt(1, 'dois') - 3
    for i, (x, sd, sk) in enumerate(((300, 2, 1), (640, 3, 3), (980, 4, 0))):
        xx = x + lerp(-500, 0, easeOut(ramp(f, i * 4, i * 4 + 22)))
        if i == 1:
            put_jog(c, xx, 2000, 820, f, 9, cores=TEC, faixa=None, arms='point' if f >= do else 'cintura', expr='proud', skin=0, hair='#9a9a9a')
        else:
            put_jog(c, xx, 1960, 760, f, sd, cores=BRA, faixa=BRA_F, walk=(f * .05) % 1 if f < 30 else 0, arms='run' if f < 30 else 'joinha', expr='grin', skin=sk)
    put_placa(c, 'ANCELOTTI', TEC, 640, 1120, f, an, 60, -3)
    num(c, 'SINGAPURA', 640, 720, f, si, 130, -4)
    num(c, '2 JOGOS', 640, 890, f, do, 110, 3)
    return c, (lerp(600, 680, smooth(f / 120)), 1420, 1.08 * (1 + .0008 * f), 0), 'dusk'


def duelo(f, li, adv, adv_cores, adv_f, dia, hora_txt, hw, ex=None, exw=None):
    c = estadio('dusk').copy()
    br = wt(li, 'Brasil') - 3 if li == 2 else 0
    ad = wt(li, hw) - 3
    bx = lerp(-300, 330, easeOut(ramp(f, br - 10, br + 8)))
    ax = lerp(1550, 930, easeOut(ramp(f, ad - 10, ad + 8)))
    put_jog(c, bx, 2010, 860, f, 5, cores=BRA, faixa=BRA_F, arms='cintura', expr='stern', skin=2, look=1)
    put_jog(c, ax, 2010, 860, f, 6, cores=adv_cores, faixa=adv_f, arms='cintura', expr='smug', skin=0, hair='#111111', look=-1)
    put_placa(c, 'BRASIL', BRA, 330, 1120, f, br + 4, 64, -4)
    put_placa(c, adv, adv_cores, 930, 1120, f, ad + 4, 60, 4)
    num(c, 'X', 640, 1520, f, ad + 6, 160)
    d0 = wt(li, dia[1]) - 3
    put_cal(c, dia[0], 300, 760, .62, f, d0)
    num(c, hora_txt, 820, 760, f, wt(li, dia[2]) - 3, 140, -4)
    if ex: num(c, ex, 640, 960, f, wt(li, exw) - 3, 88, 3)
    z = lerp(1.22, 1.06, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ad, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


def s2(f):
    return duelo(f, 2, 'JAPÃO', JAP, JAP_F, ('14', 'sabado', 'sete'), '7H15', 'Japao')


def s3(f):
    return duelo(f, 3, 'SINGAPURA', SIN, SIN_F, ('17', 'terca', 'sete'), '7H', 'Singapura', '1ª VEZ NA HISTÓRIA', 'primeira')


def s4(f):
    c = estadio('dusk').copy()
    po = wt(4, 'poupou') - 3; ti = wt(4, 'titulo') - 3
    put_trofeu(c, 640, 1250, 520, f, ti)
    put_jog(c, 340, 2020, 840, f, 7, cores=FLA, faixa=FLA_F, arms='joinha' if f >= po else 'cintura', expr='grin', skin=2, look=1)
    put_jog(c, 940, 2020, 840, f, 8, cores=PAL, faixa=PAL_F, arms='joinha' if f >= po else 'cintura', expr='grin', skin=0, look=-1)
    put_placa(c, 'FLAMENGO', FLA, 360, 1110, f, wt(4, 'Flamengo') - 3, 52, -4)
    put_placa(c, 'PALMEIRAS', PAL, 920, 1110, f, wt(4, 'Palmeiras') - 3, 52, 4)
    num(c, 'POUPADOS', 640, 700, f, po, 150, -4)
    num(c, 'BRIGA PELO TÍTULO', 640, 870, f, ti, 90, 3)
    k = kick(f, po, .7)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 8, lerp(1.06, 1.15, smooth(f / 100)), k), 'dusk'


def s5(f):
    c = estadio('day').copy()
    jo = wt(5, 'Jonathan') - 3; an = wt(5, 'Andre') - 3; ca = wt(5, 'caras') - 3
    put_jog(c, 400, 2010, 860, f, 3, cores=BRA, faixa=BRA_F, arms='up' if f >= jo else 'hang', expr='grin' if f >= jo else 'neutral', skin=3, hair='#111111')
    put_jog(c, 880, 2010, 860, f, 4, cores=BRA, faixa=BRA_F, arms='up' if f >= an else 'hang', expr='grin' if f >= an else 'neutral', skin=1)
    put_placa(c, 'JONATHAN JESUS', CRU_, 420, 1080, f, jo, 40, -3)
    put_placa(c, 'ANDRÉ LUIZ', COR, 870, 1180, f, an, 44, 3)
    num(c, 'CARAS NOVAS', 640, 740, f, ca, 100, -4)
    cx = lerp(610, 670, smooth(ramp(f, jo, an + 10)))
    return c, (cx, 1420, 1.1 * (1 + .0008 * f), 0), 'golden'


def s6(f):
    c = estadio('dusk').copy()
    co = wt(6, 'cortado') - 3; ba = wt(6, 'baixa') - 3
    put_jog(c, 640, 2030, 920, f, 6, cores=BRA, faixa=BRA_F, arms='cheek' if f >= co else 'hang', expr='pained' if f >= co else 'nervous', skin=2)
    put_placa(c, 'DANILO SANTOS', BOT, 640, 1110, f, wt(6, 'Danilo') - 3, 54, -3)
    num(c, 'BAIXA', 640, 700, f, ba, 150, -4)
    num(c, 'CORTADO', 640, 880, f, co, 130, 4)
    k = kick(f, co, .9)
    return c, (640, 1420 + k * 10, lerp(1.06, 1.18, smooth(f / 90)), k), 'dusk'


def s7(f):
    c = estadio('dusk').copy()
    br = wt(7, 'Brasileirao') - 3; de = wt(7, 'dezoito') - 3
    put_trofeu(c, 640, 1500, 380, f, wt(7, 'titulo') - 3)
    num(c, 'BRASILEIRÃO', 640, 700, f, br, 100, -3); num(c, 'VOLTA', 640, 840, f, br + 3, 90, 3)
    put_cal(c, '18', 640, 1050, .55, f, de)
    put_jog(c, 330, 2040, 780, f, 7, cores=FLA, faixa=FLA_F, arms='cintura', expr='stern', skin=2, look=1)
    put_jog(c, 950, 2040, 780, f, 8, cores=PAL, faixa=PAL_F, arms='cintura', expr='stern', skin=0, look=-1)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'Selecao') - 3, 140, 1.0)
    s.ting(s.W(0, 'mundo') - 3, .3)
    s.ting(s.W(1, 'Singapura') - 3, .3)
    s.thunk(s.W(2, 'Japao') - 3, 140, .8)
    s.ting(s.W(3, 'primeira') - 3, .35)
    s.thunk(s.W(4, 'poupou') - 3, 160, .8)
    s.ting(s.W(5, 'Jonathan') - 3, .25)
    s.ting(s.W(5, 'Andre') - 3, .25)
    s.thunk(s.W(6, 'cortado') - 3, 200, .8)
    s.ting(s.W(7, 'dezoito') - 3, .3)
