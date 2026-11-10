"""Um Café com o Mundo — TIKTOK LONGO "O QUE IMPORTA HOJE" (terça 10/11/2026, 18h).
Notícia 1: Ucrânia, Rússia e EUA voltam a negociar em Abu Dhabi (fatos e fontes em reels/desenho/2026-11-10-18h/historia.py:
Al Jazeera 10/11, Euronews 10/11, Reuters via Just Security 10/11).
Notícia 2: França acusa a Guarda Revolucionária do Irã pelo ataque hacker às geladeiras de supermercados (fatos e fontes em
reels/desenho/2026-11-10-15h/historia.py: Al Jazeera 09/11, Reuters 10/11).
Nenhum fato novo: só o que já foi conferido nas duas pastas. Cenas reaproveitadas das duas pastas."""
import os, importlib.util
from kit import *
import kit

_here = os.path.dirname(os.path.abspath(__file__))


def _load(nome, sub):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(_here, '..', sub, 'historia.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


A = _load('hist_abudhabi', '2026-11-10-18h')
B = _load('hist_geladeiras', '2026-11-10-15h')
politico = A.politico; pessoa = B.pessoa

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'O QUE IMPORTA HOJE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "A guerra na Ucrânia voltou à mesa, e o Irã é acusado de esquentar geladeiras na França. Duas notícias de hoje.",
    A.LINES[0], A.LINES[1], A.LINES[3], A.LINES[4], A.LINES[6],
    "E tem mais: a França diz que hackers do Irã fizeram as geladeiras dos supermercados esquentarem até cinquenta graus.",
    B.LINES[1], B.LINES[2], B.LINES[3], B.LINES[6],
]
CAPTXT = [
    "A guerra na Ucrânia voltou à mesa,|e o Irã é acusado de esquentar geladeiras|na França. Duas notícias de hoje.",
    A.CAPTXT[0], A.CAPTXT[1], A.CAPTXT[3], A.CAPTXT[4], A.CAPTXT[6],
    "E tem mais: a França diz que hackers do Irã|fizeram as geladeiras dos supermercados|esquentarem até 50 graus.",
    B.CAPTXT[1], B.CAPTXT[2], B.CAPTXT[3], B.CAPTXT[6],
]
FALA_TIKTOK = "O que você acha disso? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
MAPA_A = {0: 1, 1: 2, 3: 3, 4: 4, 6: 5}
MAPA_B = {0: 6, 1: 7, 2: 8, 3: 9, 6: 10}
A.wt = lambda si, w, nth=0: kit.wt(MAPA_A[si], w, nth)
B.wt = lambda si, w, nth=0: kit.wt(MAPA_B[si], w, nth)
CHECK = [(0, 'Ucrania', 4), (0, 'Ira', 4), (0, 'Franca', 4), (0, 'Duas', 4), (1, 'fevereiro', 4), (2, 'Abu', 4),
         (3, 'vinte', 6), (4, 'flexibilidade', 4), (5, 'paz', 4), (6, 'Franca', 4), (6, 'cinquenta', 4),
         (7, 'outubro', 4), (8, 'fogo', 4), (9, 'culpado', 4), (10, 'sancoes', 4), (10, 'negar', 4)]


def s_hook(f):
    c = CEN('escritorio', 'dusk').copy()
    u0 = wt(0, 'Ucrania') - 3; i0 = wt(0, 'Ira') - 3; fr0 = wt(0, 'Franca') - 3; d0 = wt(0, 'Duas') - 3
    A.mesa(c, 330, 1330)
    if f >= u0:
        paste_c(c, A.bandeira(), 230, 1000, back(ramp(f, u0, u0 + 8)) * .4)
        paste_c(c, A.bandeira_ru(), 430, 1000, back(ramp(f, u0 + 4, u0 + 12)) * .4)
        A.num(c, 'UCRÂNIA', 330, 800, f, u0, 70, -3)
    if f >= i0:
        B.put_band(c, B.bandeira_ir(), 900, 760, 200, f, back(ramp(f, i0, i0 + 8)), pole=False)
    if f >= fr0:
        B.put_band(c, B.bandeira_fr(), 900, 960, 200, f + 5, back(ramp(f, fr0, fr0 + 8)), pole=False)
        B.put_termo(c, 1080, 1180, f, 8 * smooth(ramp(f, fr0, fr0 + 30)), .6)
        A.num(c, 'GELADEIRAS', 880, 1180, f, fr0, 60, 3)
    A.num(c, '2 NOTÍCIAS', 640, 470, f, d0, 120, -4)
    z = lerp(1.3, 1.03, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, d0)
    return c, (640 + 20 * math.sin(f * .03), 1080 + k * 8, z, k), 'dusk'


SCENES = [s_hook, A.s0, A.s1, A.s3, A.s4, A.s6, B.s0, B.s1, B.s2, B.s3, B.s6]


def SFX(s):
    s.ting(s.W(0, 'Ucrania') - 3, .3)
    s.ting(s.W(0, 'Franca') - 3, .3)
    s.thunk(s.W(0, 'Duas') - 3, 140, .8)
    s.ting(s.W(1, 'primeira') - 3, .3)
    s.ting(s.W(2, 'Abu') - 3, .25)
    s.thunk(s.W(3, 'vinte') - 3, 150, .6)
    s.ting(s.W(4, 'flexibilidade') - 3, .3)
    s.ting(s.W(5, 'paz') - 3, .3)
    s.thunk(s.W(6, 'cinquenta') - 3, 140, .7)
    s.thunk(s.W(8, 'fogo') - 3, 140, .6)
    s.thunk(s.W(9, 'culpado') - 3, 150, .7)
    s.ting(s.W(10, 'sancoes') - 3, .3)
