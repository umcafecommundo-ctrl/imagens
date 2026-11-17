"""Formato DESENHO: a lontra-marinha se amarra na alga antes de dormir (Curiosidades da IA, 17/11/2026, 07h).
Categoria: ANIMAIS.
Fatos: UC Davis Wildlife Health Center ("Sea Otter Facts"): boiam de costas; antes de cochilar podem se enrolar em kelp
ou outras algas para se ancorar; não têm camada de gordura (blubber). Georgia Aquarium (southern sea otter): acredita-se
que a lontra se enrola em kelp antes de dormir na superfície para não ser levada (drifting away). O kelp fica preso
ao fundo do mar pela base (rizoide/holdfast).
Cenários: s0 praia (Professor aponta a lontra no mar) | s1 mar aberto (lontra dorme boiando de barriga pra cima) |
s2 mar aberto (a correnteza leva a lontra) | s3 mar em corte, entardecer (alga presa no fundo vira corda) |
s4 praia ao entardecer (Professor: dorme de cinto de segurança)."""
from kit import *
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lontra_lib as L
from lontra_lib import lontra, put_lontra, mar_aberto, mar_corte, alga_corda

LINES = [
    "A lontra-marinha se amarra antes de dormir.",
    "Ela dorme boiando de barriga pra cima, no meio do mar.",
    "Só que, se dormir solta, a correnteza leva ela pra longe.",
    "Você vê, antes de cochilar, ela se enrola numa alga presa no fundo do mar, como uma corda.",
    "Ou seja: a lontra dorme... de cinto de segurança.",
]
CAPTXT = [
    "A lontra-marinha se amarra antes de dormir.",
    "Ela dorme boiando de barriga pra cima,|no meio do mar.",
    "Só que, se dormir solta,|a correnteza leva ela pra longe.",
    "Você vê, antes de cochilar, ela se enrola|numa alga presa no fundo do mar, como uma corda.",
    "Ou seja: a lontra dorme... de cinto de segurança.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'amarra', 4), (0, 'dormir', 6), (1, 'boiando', 4), (1, 'mar', 6), (2, 'correnteza', 4), (2, 'longe', 6),
         (3, 'enrola', 4), (3, 'fundo', 6), (3, 'corda', 6), (4, 'cinto', 8)]


def SFX(s):
    s.patter(0, 60, 8, .08)
    s.ting(s.W(0, 'amarra'), .3)
    s.splash(s.W(1, 'boiando') - 2)
    s.patter(s.W(1, 'mar'), s.W(1, 'mar') + 40, 10, .08)
    s.whoosh(s.W(2, 'correnteza') - 6, .5, .5)
    s.whoosh(s.W(2, 'longe') - 4, .4, .4)
    s.thunk(s.W(3, 'enrola') - 2, 200, .6)
    s.thunk(s.W(3, 'fundo') - 2, 120, .7)
    s.ting(s.W(3, 'corda'), .3)
    s.thunk(s.W(4, 'cinto') - 2, 260, .8); s.trill(s.W(4, 'cinto') + 6, 1.0, .3)


def zz(c, x, y, f):
    for i in range(3):
        a = (f + i * 14) % 42
        paste_c(c, txt('Z', 60 + i * 14), x + a * 3 + i * 36, y - a * 5 - i * 50, 1 - a / 42)


def s0(f):
    c = CEN('praia', 'day').copy()
    k = wt(0, 'amarra') - 3
    d = wt(0, 'dormir') - 3
    put_lontra(c, 700, 1230, 480, sleep=1 if f >= d else 0, look=-.5, bob=math.sin(f * .12),
               kelp=back(ramp(f, k, k + 8)) if f >= k else 0)
    if f >= d: zz(c, 800, 1060, f)
    put_prof(c, 330, 1880, 960, f, expr='grin' if f < k else 'shock', arms='point', look=1)
    if f >= k: paste_c(c, txt('SE AMARRA?!', 100, -5), 700, 660, back(ramp(f, k, k + 8)))
    z = lerp(1.3, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1240 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = mar_aberto('day').copy()
    b = wt(1, 'boiando') - 3
    put_lontra(c, 640, 1250, 900, sleep=1, bob=math.sin(f * .12), look=.3)
    L.agua_frente(c, 1320, f, alpha=120)
    zz(c, 900, 1000, f)
    if f >= b: paste_c(c, txt('BARRIGA PRA CIMA', 66, -4), 660, 640, back(ramp(f, b, b + 8)))
    t = smooth(ramp(f, 0, 80))
    z = lerp(1.35, 1.12, t) * (1 + .0009 * f)
    return c, (lerp(700, 640, t), lerp(1200, 1150, t), z, math.sin(f * .05) * 1.5), 'day'


def s2(f):
    c = mar_aberto('day').copy()
    k = wt(2, 'correnteza') - 3
    lo = wt(2, 'longe') - 3
    dx = 0 if f < k else (f - k) ** 1.25 * 3.2
    put_lontra(c, 420 + dx, 1250, 700, sleep=1 if f < lo else 0, expr='shock' if f >= lo else 'calm', bob=math.sin(f * .2), look=-1)
    L.agua_frente(c, 1300, f, alpha=110)
    if f >= k:
        d = ImageDraw.Draw(c)
        for i in range(4):
            y = 1380 + i * 70
            x0 = (f * 14 + i * 300) % 1500 - 300
            d.line([(x0, y), (x0 + 200, y)], fill=(220, 240, 255, 255), width=10)
            d.polygon([(x0 + 200, y - 20), (x0 + 240, y), (x0 + 200, y + 20)], fill=(220, 240, 255, 255))
        paste_c(c, txt('CORRENTEZA', 96, 5), 600, 620, back(ramp(f, k, k + 8)))
    if f >= lo: paste_c(c, txt('TCHAU!', 100, -6), 640, 840, back(ramp(f, lo, lo + 8)))
    t = smooth(ramp(f, k, k + 70))
    z = lerp(1.25, 1.05, t) * (1 + .0009 * f)
    return c, (lerp(560, 760, t), 1200, z, lerp(0, 3, t)), 'day'


def s3(f):
    c = mar_corte('dusk').copy()
    e = wt(3, 'enrola') - 3
    fu = wt(3, 'fundo') - 3
    co = wt(3, 'corda') - 3
    X = 640
    alga_corda(c, X - 40, 790, X + 20, 1945, ramp(f, e - 10, e + 14) if f >= e - 10 else 0, f)
    put_lontra(c, X, 790, 640, sleep=0 if f < co else 1, expr='smug', look=-1, bob=math.sin(f * .1) * .5,
               kelp=back(ramp(f, e, e + 10)) if f >= e else 0)
    if f >= e and f < fu: paste_c(c, txt('ENROLA!', 96, -5), 700, 400, back(ramp(f, e, e + 8)))
    if f >= co: paste_c(c, txt('= CORDA', 110, 5), 760, 1350, back(ramp(f, co, co + 8)))
    # câmera: na superfície, desce de grua até o fundo no 'fundo', volta para a lontra na 'corda'
    t1 = smooth(ramp(f, fu - 10, fu + 20)); t2 = smooth(ramp(f, co - 6, co + 24))
    cy = lerp(lerp(900, 1500, t1), 1150, t2)
    z = lerp(lerp(1.5, 1.25, t1), 1.05, t2) * (1 + .0009 * f)
    return c, (640, cy + kick(f, fu, .5) * 8, z, 0), 'dusk'


def s4(f):
    c = CEN('praia', 'dusk').copy()
    ci = wt(4, 'cinto') - 3
    put_lontra(c, 720, 1240, 480, sleep=0 if f >= ci else 1, expr='smug', look=-1, kelp=1, bob=math.sin(f * .12))
    if f < ci: zz(c, 820, 1080, f)
    put_prof(c, 360, 1880, 980, f, expr='grin' if f >= ci else 'smug', arms='point' if f >= ci else 'chin', look=1)
    if ci <= f < ci + 32:
        paste_c(c, txt('CINTO DE', 90, -5), 640, 600, back(ramp(f, ci, ci + 8)))
        paste_c(c, txt('SEGURANÇA!', 90, -5), 660, 720, back(ramp(f, ci + 3, ci + 11)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (620, lerp(1250, 1200, t) + kick(f, ci, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
