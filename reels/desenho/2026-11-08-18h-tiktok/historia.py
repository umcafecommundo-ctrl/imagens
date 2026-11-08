"""Um Café com o Mundo — TIKTOK LONGO "O QUE IMPORTA HOJE" (domingo 08/11/2026, 18h).
Notícia 1: França, 4º fim de semana de protestos contra o custo de vida (fatos e fontes em reels/desenho/2026-11-08-18h/historia.py:
Al Jazeera 07/11, CNBC 08/11, Wikipedia 2026 French student protests).
Notícia 2: petróleo Brent com a maior queda semanal desde 2020 e o efeito no Brasil (fatos e fontes em
reels/desenho/2026-11-08-15h/historia.py: FinanceFeeds/CNBC/Reuters 07/11, Agência Estado 08/11).
Nenhum fato novo: só o que já foi conferido nas duas pastas. Cenas reaproveitadas das duas pastas."""
import os, importlib.util
from kit import *
import kit

_here = os.path.dirname(os.path.abspath(__file__))


def _load(nome, sub):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(_here, '..', sub, 'historia.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


A = _load('hist_franca', '2026-11-08-18h')
B = _load('hist_petroleo', '2026-11-08-15h')
# nomes que o kit procura em sys.modules['historia']
pessoa = A.pessoa; politico = B.politico; cargueiro = B.cargueiro

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O QUE IMPORTA HOJE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "O petróleo despencou, mas a França foi às ruas contra o preço dos combustíveis. Duas notícias que mexem com o seu bolso.",
    A.LINES[0], A.LINES[1], A.LINES[2], A.LINES[4], A.LINES[5],
    "E tem mais: o petróleo despencou dezesseis por cento em uma semana, a maior queda desde dois mil e vinte.",
    B.LINES[2], B.LINES[4], B.LINES[5], B.LINES[6],
]
CAPTXT = [
    "O petróleo despencou, mas a França foi às ruas|contra o preço dos combustíveis. Duas notícias|que mexem com o seu bolso.",
    A.CAPTXT[0], A.CAPTXT[1], A.CAPTXT[2], A.CAPTXT[4], A.CAPTXT[5],
    "E tem mais: o petróleo despencou 16%|em uma semana, a maior queda|desde 2020.",
    B.CAPTXT[2], B.CAPTXT[4], B.CAPTXT[5], B.CAPTXT[6],
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 6
FLASH = [6]

MAPA_A = {0: 1, 1: 2, 2: 3, 4: 4, 5: 5}
MAPA_B = {0: 6, 2: 7, 4: 8, 5: 9, 6: 10}
A.wt = lambda si, w, nth=0: kit.wt(MAPA_A[si], w, nth)
B.wt = lambda si, w, nth=0: kit.wt(MAPA_B[si], w, nth)

CHECK = [(0, 'petroleo', 4), (0, 'Franca', 4), (0, 'bolso', 4), (1, 'cento', 8), (2, 'professores', 4), (3, 'combustiveis', 4),
         (4, 'lacrimogeneo', 4), (5, 'abril', 4), (6, 'dezesseis', 6), (7, 'acordo', 4), (8, 'subsidio', 4), (9, 'dobro', 6), (10, 'Opep', 4)]


def s_hook(f):
    c = CEN('cidade', 'golden').copy()
    p0 = wt(0, 'petroleo') - 3
    fr0 = wt(0, 'Franca') - 3
    d0 = wt(0, 'duas') - 3
    # esquerda: barril que cai; direita: multidão com cartazes
    yb = lerp(600, 1180, easeOut(ramp(f, p0 - 6, p0 + 8)))
    paste_c(c, B.barril().resize((300, 390)), 330, yb, 1)
    B.seta(c, 330, 820, 200, up=False, col=hexc('#d8443c'), s=back(ramp(f, p0 + 4, p0 + 12)))
    if f >= fr0:
        A.multidao(c, f, 1640, 420, 3, 760, 1140, 2, march=ramp(f, fr0, fr0 + 120), expr='stern', rows=1)
        A.put_band(c, 960, 860, 200, f, back(ramp(f, fr0, fr0 + 8)))
    A.num(c, 'PETRÓLEO', 390, 560, f, p0, 80, -3)
    A.num(c, 'FRANÇA', 950, 560, f, fr0, 80, 3)
    A.num(c, '2 NOTÍCIAS', 640, 400, f, d0, 120, -4)
    A.num(c, 'NO SEU BOLSO', 640, 1000, f, wt(0, 'bolso') - 3, 70, 2)
    z = lerp(1.3, 1.03, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, d0)
    return c, (640 + 20 * math.sin(f * .03), 1060 + k * 8, z, k), 'golden'


SCENES = [s_hook, A.s0, A.s1, A.s2, A.s4, A.s5, B.s0, B.s2, B.s4, B.s5, B.s6]


def SFX(s):
    s.thunk(s.W(0, 'petroleo') - 3, 140, .8)
    s.ting(s.W(0, 'duas') - 3, .3)
    s.thunk(s.W(1, 'cento') - 3, 140, .9)
    s.thunk(s.W(2, 'escolas') - 3, 200, .5)
    s.thunk(s.W(3, 'combustiveis') - 3, 160, .6)
    s.thunk(s.W(4, 'Setenta') - 3, 120, .6)
    s.ting(s.W(5, 'abril') - 3, .3)
    s.thunk(s.W(6, 'dezesseis') - 3, 140, 1.0)
    s.whoosh(s.W(7, 'acordo') - 3, .3, .5)
    s.ting(s.W(8, 'Brasil') - 3, .3)
    s.thunk(s.W(9, 'dobro') - 3, 140, .9)
    s.ting(s.W(10, 'Opep') - 3, .3)
