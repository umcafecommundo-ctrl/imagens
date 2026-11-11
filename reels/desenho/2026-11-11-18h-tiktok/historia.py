"""Um Café com o Mundo — TIKTOK LONGO "O QUE IMPORTA HOJE" (quarta 11/11/2026, 18h).
Notícia 1: fim das conversas de Abu Dhabi, Rússia e Ucrânia combinam grande troca de prisioneiros; enviados dos EUA vão a Putin
(fatos e fontes em reels/desenho/2026-11-11-18h/historia.py: Euronews 11/11, Kyiv Independent 11/11, Just Security 11/11).
Notícia 2: drones no céu dos países bálticos, alertas para se abrigar na Lituânia, Letônia e Estônia (fatos e fontes em
reels/desenho/2026-11-11-15h/historia.py: Reuters via Cyprus Mail 11/11, Just Security 11/11).
Nenhum fato novo: só o que já foi conferido nas duas pastas. Cenas reaproveitadas das duas pastas."""
import os, importlib.util
from kit import *
import kit

_here = os.path.dirname(os.path.abspath(__file__))


def _load(nome, sub):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(_here, '..', sub, 'historia.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


A = _load('hist_troca', '2026-11-11-18h')
B = _load('hist_drones', '2026-11-11-15h')
politico = A.politico; morador = B.morador

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O QUE IMPORTA HOJE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Duas notícias da guerra na Ucrânia hoje. Primeiro: Rússia e Ucrânia combinaram uma troca de prisioneiros que, segundo Moscou, vai ser a maior da guerra.",
    A.LINES[1], A.LINES[2], A.LINES[3], A.LINES[5],
    "E tem mais: nesta madrugada, três países da Otan mandaram a população se abrigar por causa de drones.",
    B.LINES[1], B.LINES[3], B.LINES[4], B.LINES[6],
]
CAPTXT = [
    "Duas notícias da guerra na Ucrânia hoje.|Primeiro: Rússia e Ucrânia combinaram uma troca|de prisioneiros que, segundo Moscou,|vai ser a maior da guerra.",
    A.CAPTXT[1], A.CAPTXT[2], A.CAPTXT[3], A.CAPTXT[5],
    "E tem mais: nesta madrugada, 3 países da Otan|mandaram a população se abrigar|por causa de drones.",
    B.CAPTXT[1], B.CAPTXT[3], B.CAPTXT[4], B.CAPTXT[6],
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
MAPA_A = {0: 0, 1: 1, 2: 2, 3: 3, 5: 4}
MAPA_B = {0: 5, 1: 6, 3: 7, 4: 8, 6: 9}
A.wt = lambda si, w, nth=0: kit.wt(MAPA_A[si], w, nth)
B.wt = lambda si, w, nth=0: kit.wt(MAPA_B[si], w, nth)
CHECK = [(0, 'Duas', 4), (0, 'troca', 4), (0, 'maior', 4), (1, 'Abu', 4), (2, 'mil', 4), (2, 'quinhentos', 4),
         (3, 'cessar-fogo', 4), (3, 'Donbas', 4), (4, 'Moscou', 4), (4, 'Putin', 4), (5, 'tres', 4), (5, 'abrigar', 4),
         (6, 'Lituania', 4), (6, 'Belarus', 4), (7, 'Quatro', 4), (7, 'cacas', 6), (8, 'restos', 4), (8, 'Ninguem', 4), (9, 'paz', 4)]

def h0(f):
    c, cam, luz = A.s0(f)
    d0 = wt(0, 'Duas') - 3
    A.num(c, '2 NOTÍCIAS DE HOJE', 640, 860, f, d0, 84, -3)
    return c, cam, luz


SCENES = [h0, A.s1, A.s2, A.s3, A.s5, B.s0, B.s1, B.s3, B.s4, B.s6]


def SFX(s):
    s.ting(s.W(0, 'troca') - 3, .3)
    s.thunk(s.W(0, 'maior') - 3, 140, .5)
    s.ting(s.W(1, 'Abu') - 3, .25)
    s.thunk(s.W(2, 'mil') - 3, 150, .5)
    s.thunk(s.W(3, 'cessar-fogo') - 3, 140, .5)
    s.thunk(s.W(4, 'Moscou') - 3, 140, .4)
    s.thunk(s.W(5, 'tres') - 3, 140, .5)
    s.ting(s.W(5, 'abrigar') - 3, .35)
    s.engine(s.W(5, 'drones') - 6, s.W(5, 'drones') + 50, .07)
    s.ting(s.W(6, 'Lituania') - 3, .2)
    s.ting(s.W(6, 'Estonia') - 3, .2)
    s.ting(s.W(7, 'Quatro') - 3, .3)
    s.engine(s.W(7, 'cacas') - 6, s.W(7, 'cacas') + 50, .09)
    s.thunk(s.W(8, 'restos') - 3, 150, .4)
    s.ting(s.W(8, 'Ninguem') - 3, .3)
    s.ting(s.W(9, 'paz') - 3, .3)
