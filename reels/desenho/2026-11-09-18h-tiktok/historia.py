"""Um Café com o Mundo — TIKTOK LONGO "O QUE IMPORTA HOJE" (segunda 09/11/2026, 18h).
Notícia 1: ataques russos à rede elétrica da Ucrânia, ~850 mil sem luz, usina de Zaporíjia só com geradores a diesel,
negociações em Abu Dhabi (fatos e fontes em reels/desenho/2026-11-09-18h/historia.py: Al Jazeera 08/11, Euromaidan Press 08/11,
10 Things 09/11).
Notícia 2: China prorroga a trégua tarifária com os EUA e o elo com a soja do Brasil (fatos e fontes em
reels/desenho/2026-11-09-10h/historia.py: Bloomberg/Yahoo Finance 08-09/11, The Tribune/ANI 09/11).
Nenhum fato novo: só o que já foi conferido nas duas pastas. Cenas reaproveitadas das duas pastas."""
import os, importlib.util
from kit import *
import kit

_here = os.path.dirname(os.path.abspath(__file__))


def _load(nome, sub):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(_here, '..', sub, 'historia.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


A = _load('hist_ucrania', '2026-11-09-18h')
B = _load('hist_tarifas', '2026-11-09-10h')
politico = B.politico; cargueiro = B.cargueiro

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O QUE IMPORTA HOJE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "A Ucrânia ficou no escuro, e a soja do Brasil entrou na briga entre Estados Unidos e China. Duas notícias que importam hoje.",
    A.LINES[1], A.LINES[2], A.LINES[4], A.LINES[6],
    "E tem mais: a guerra das tarifas entre Estados Unidos e China foi adiada, e isso mexe com a soja do Brasil.",
    B.LINES[1], B.LINES[2], B.LINES[4], B.LINES[5],
]
CAPTXT = [
    "A Ucrânia ficou no escuro, e a soja do Brasil|entrou na briga entre EUA e China.|Duas notícias que importam hoje.",
    A.CAPTXT[1], A.CAPTXT[2], A.CAPTXT[4], A.CAPTXT[6],
    "E tem mais: a guerra das tarifas entre EUA e China|foi adiada, e isso mexe|com a soja do Brasil.",
    B.CAPTXT[1], B.CAPTXT[2], B.CAPTXT[4], B.CAPTXT[5],
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]

MAPA_A = {1: 1, 2: 2, 4: 3, 6: 4}
MAPA_B = {0: 5, 1: 6, 2: 7, 4: 8, 5: 9}
A.wt = lambda si, w, nth=0: kit.wt(MAPA_A[si], w, nth)
B.wt = lambda si, w, nth=0: kit.wt(MAPA_B[si], w, nth)

CHECK = [(0, 'Ucrania', 4), (0, 'soja', 4), (0, 'Duas', 4), (1, 'cento', 6), (2, 'seiscentas', 6), (3, 'usina', 4),
         (3, 'diesel', 4), (4, 'Abu', 4), (5, 'adiada', 4), (6, 'vinte', 6), (7, 'janeiro', 4), (8, 'concorrencia', 4),
         (9, 'encontrar', 4)]


def s_hook(f):
    c = CEN('cidade', 'dusk').copy(); A.noite(c)
    u0 = wt(0, 'Ucrania') - 3
    e0 = wt(0, 'escuro') - 3
    s0_ = wt(0, 'soja') - 3
    d0 = wt(0, 'Duas') - 3
    lit = 1 - smooth(ramp(f, e0, e0 + 14)) * .93
    A.predio(c, 220, 1530, 260, 760, lit, 1)
    A.predio(c, 420, 1530, 220, 600, lit, 2)
    if f >= u0:
        paste_c(c, A.bandeira(), 340, 760, back(ramp(f, u0, u0 + 8)) * .5)
    A.num(c, 'UCRÂNIA', 360, 600, f, u0, 72, -3)
    if f >= s0_:
        B.put_saco(c, 880, 1330, 280, back(ramp(f, s0_, s0_ + 8)))
        B.put_band(c, B.bandeira_us(), 760, 820, 200, f, back(ramp(f, s0_ + 6, s0_ + 14)))
        B.put_band(c, B.bandeira_cn(), 1000, 820, 200, f + 7, back(ramp(f, s0_ + 9, s0_ + 17)))
        A.num(c, 'SOJA DO BRASIL', 860, 640, f, s0_, 56, 3)
    A.num(c, '2 NOTÍCIAS', 640, 430, f, d0, 120, -4)
    z = lerp(1.3, 1.03, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, d0)
    return c, (640 + 20 * math.sin(f * .03), 1080 + k * 8, z, k), 'dusk'


SCENES = [s_hook, A.s1, A.s2, A.s4, A.s6, B.s0, B.s1, B.s2, B.s4, B.s5]


def SFX(s):
    s.thunk(s.W(0, 'escuro') - 3, 140, .7)
    s.ting(s.W(0, 'soja') - 3, .3)
    s.thunk(s.W(0, 'Duas') - 3, 140, .8)
    s.engine(s.W(1, 'cento') - 6, s.W(1, 'cento') + 50, .08)
    s.thunk(s.W(2, 'seiscentas') - 3, 140, .6)
    s.thunk(s.W(3, 'ultima') + 3, 160, .8)
    s.ting(s.W(4, 'Abu') - 3, .3)
    s.thunk(s.W(5, 'adiada') - 3, 140, .8)
    s.ting(s.W(6, 'vinte') - 3, .3)
    s.ting(s.W(7, 'janeiro') - 3, .3)
    s.ting(s.W(8, 'Brasil') - 3, .3)
    s.thunk(s.W(8, 'concorrencia') - 3, 140, .7)
    s.ting(s.W(9, 'encontrar') - 3, .3)
