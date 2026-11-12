"""Um Café com o Mundo — TIKTOK LONGO "O QUE IMPORTA HOJE" (quinta 12/11/2026, 18h).
Notícia 1: ebola no Congo passa de 11 mil casos, 2º maior surto da história (fatos e fontes em
reels/desenho/2026-11-12-18h/historia.py: AP 11/11/2026, Reuters via CNBC Africa 11/11/2026).
Notícia 2: Jensen Huang renuncia ao comando da Nvidia, ações despencam (fatos e fontes em
reels/desenho/2026-11-12-15h/historia.py: Yahoo Finance, Suno, CBS News, 12/11/2026).
Nenhum fato novo: só o que já foi conferido nas duas pastas. Cenas reaproveitadas das duas pastas."""
import os, importlib.util
from kit import *
import kit

_here = os.path.dirname(os.path.abspath(__file__))


def _load(nome, sub):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(_here, '..', sub, 'historia.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


A = _load('hist_ebola', '2026-11-12-18h')
B = _load('hist_nvidia', '2026-11-12-15h')
politico = B.politico

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O QUE IMPORTA HOJE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Duas notícias de hoje que você precisa saber. Primeiro: o ebola já infectou mais de onze mil pessoas no Congo, e matou mais de cinco mil.",
    A.LINES[1], A.LINES[3], A.LINES[4], A.LINES[5],
    "E tem mais: " + B.LINES[0][0].lower() + B.LINES[0][1:],
    B.LINES[1], B.LINES[3], B.LINES[4], B.LINES[5],
]
CAPTXT = [
    "Duas notícias de hoje que você precisa saber.|Primeiro: o ebola já infectou mais de 11 mil pessoas|no Congo, e matou mais de 5 mil.",
    A.CAPTXT[1], A.CAPTXT[3], A.CAPTXT[4], A.CAPTXT[5],
    "E tem mais: " + B.CAPTXT[0][0].lower() + B.CAPTXT[0][1:],
    B.CAPTXT[1], B.CAPTXT[3], B.CAPTXT[4], B.CAPTXT[5],
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 8
FLASH = [8]
MAPA_A = {0: 0, 1: 1, 3: 2, 4: 3, 5: 4}
MAPA_B = {0: 5, 1: 6, 3: 7, 4: 8, 5: 9}
A.wt = lambda si, w, nth=0: kit.wt(MAPA_A[si], w, nth)
B.wt = lambda si, w, nth=0: kit.wt(MAPA_B[si], w, nth)
CHECK = [(0, 'Duas', 4), (0, 'onze', 4), (0, 'cinco', 4), (1, 'segundo', 4), (2, 'Bundibugyo', 4), (2, 'vacina', 4),
         (3, 'oito', 4), (3, 'Uganda', 4), (4, 'quatro', 4), (4, 'mil', 4), (5, 'mais', 4)]


def h0(f):
    c, cam, luz = A.s0(f)
    d0 = wt(0, 'Duas') - 3
    if f < wt(0, 'ebola') - 3:
        A.num(c, '2 NOTÍCIAS DE HOJE', 640, 520, f, d0, 62, -3)
    return c, cam, luz


SCENES = [h0, A.s1, A.s3, A.s4, A.s5, B.s0, B.s1, B.s3, B.s4, B.s5]


def SFX(s):
    s.ting(s.W(0, 'Duas') - 3, .3)
    s.thunk(s.W(0, 'onze') - 3, 150, .8)
    s.thunk(s.W(0, 'cinco') - 3, 120, .6)
    s.thunk(s.W(1, 'segundo') - 3, 160, .6)
    s.ting(s.W(2, 'Bundibugyo') - 3, .2)
    s.thunk(s.W(2, 'vacina') - 3, 130, .5)
    s.ting(s.W(3, 'oito') - 3, .25)
    s.thunk(s.W(4, 'quatro') - 3, 120, .5)
    s.ting(s.W(5, 'tem') - 3, .3)
    s.thunk(s.W(5, 'chips') - 3, 160, .7)
    s.thunk(s.W(5, 'despencaram') - 3, 120, 1.0)
    s.ting(s.W(6, 'mil') - 3, .3)
    s.thunk(s.W(6, 'trinta') - 3, 150, .8)
    s.thunk(s.W(7, 'catorze') - 3, 130, 1.0)
    s.whoosh(s.W(7, 'diretora') - 3, .3, .5)
    s.thunk(s.W(8, 'bolsas') - 3, 150, .8)
    s.thunk(s.W(9, 'oito') - 3, 140, .9)
