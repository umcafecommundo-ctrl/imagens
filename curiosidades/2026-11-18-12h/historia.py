"""Formato DESENHO: por que o ovo endurece quando cozinha — PARTE 1 (Curiosidades da IA, 18/11/2026, 12h).
Categoria: CIÊNCIA DO DIA A DIA. Dupla com 2026-11-18-19h (parte 2: por que a batata amolece).
Fatos: Scientific American ("Shape-Shifting Science: Molding Hard-Boiled Eggs"): a clara é ~85% água e ~10% proteína;
as proteínas começam enroladas "como novelos de lã"; o calor quebra as ligações fracas e elas se desenrolam; as proteínas
desenroladas se ligam umas às outras (coagulação), formam uma rede que prende a água, e a clara vira gel e depois sólido;
depois de frio, fica permanentemente assim.
Cenários: s0 cozinha (Professor, ovo entra na panela e sai duro) | s1 cozinha + lupa dentro da clara (novelos) |
s2 cozinha, fogo + lupa (novelos se abrem) | s3 cozinha + lupa (fios se agarram, rede) | s4 cozinha ao entardecer + lupa
(rede prende a água, clara fica branca) | s5 cozinha ao entardecer (Professor com cara de mistério e a batata na panela)."""
from kit import *
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cozinha_lib as L

LINES = [
    "O ovo entra mole na panela e sai duro, só com água quente.",
    "Dentro da clara, tem proteínas enroladinhas, como novelos de lã, boiando na água.",
    "O calor desmancha esses novelos, e os fios se abrem.",
    "Aí os fios se agarram uns nos outros e formam uma rede.",
    "Você vê, essa rede prende a água lá dentro, e a clara mole vira um sólido branco.",
    "Mas, na mesma panela, a batata faz o contrário: amolece. E isso fica pra parte dois.",
]
CAPTXT = [
    "O ovo entra mole na panela e sai duro,|só com água quente.",
    "Dentro da clara, tem proteínas enroladinhas,|como novelos de lã, boiando na água.",
    "O calor desmancha esses novelos,|e os fios se abrem.",
    "Aí os fios se agarram uns nos outros|e formam uma rede.",
    "Você vê, essa rede prende a água lá dentro,|e a clara mole vira um sólido branco.",
    "Mas, na mesma panela, a batata faz o contrário: amolece.|E isso fica pra parte dois.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 4
FLASH = []
CHECK = [(0, 'duro', 4), (1, 'novelos', 6), (2, 'desmancha', 4), (2, 'abrem', 6), (3, 'agarram', 6), (3, 'rede', 6),
         (4, 'prende', 6), (4, 'branco', 6), (5, 'batata', 4), (5, 'dois', 8)]


def SFX(s):
    s.splash(8)
    s.patter(10, 70, 10, .08)
    s.thunk(s.W(0, 'duro') - 2, 220, .8); s.ting(s.W(0, 'quente'), .25)
    s.ting(s.W(1, 'novelos'), .3)
    s.patter(s.W(1, 'boiando'), s.W(1, 'boiando') + 40, 8, .08)
    s.whoosh(s.W(2, 'calor') - 4, .4, .4)
    s.whoosh(s.W(2, 'abrem') - 4, .5, .4)
    for i in range(4): s.thunk(s.W(3, 'agarram') - 2 + i * 4, 300, .4)
    s.ting(s.W(3, 'rede'), .3)
    s.thunk(s.W(4, 'prende') - 2, 180, .6); s.ting(s.W(4, 'branco'), .35)
    s.thunk(s.W(5, 'amolece') - 2, 120, .7); s.trill(s.W(5, 'dois'), 1.0, .3)


def cena_base(luz, f, fogo_w=420, boil=1):
    c = CEN('cozinha', luz).copy()
    L.fogo(c, 820, 1760, fogo_w, f)
    L.panela(c, 820, 1640, 460, boil, f)
    return c


def s0(f):
    c = cena_base('day', f)
    du = wt(0, 'duro') - 3
    # ovo cai na panela (0-10), some na água, pula cozido no 'duro'
    if f < 12:
        y = lerp(700, 1440, ramp(f, 0, 12) ** 2)
        paste_c(c, L.ovo_img(170), 820, y)
    elif f >= du:
        t = back(ramp(f, du, du + 10))
        paste_c(c, L.ovo_img(220, 1), 820, lerp(1440, 980, t))
    put_prof(c, 330, 1880, 960, f, expr='grin' if f < du else 'shock', arms='point', look=1)
    if f < 46: paste_c(c, txt('PARTE 1', 120, -4), 640, 520, back(ramp(f, 0, 8)) * (1 - ramp(f, 40, 46)))
    if f >= du: paste_c(c, txt('DURO!', 120, 6), 860, 640, back(ramp(f, du, du + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1240 + kick(f, du, .6) * 10, z, 0), 'day'


def s1(f):
    c = cena_base('day', f)
    paste_c(c, L.ovo_img(200, 1), 820, 1420)
    n = wt(1, 'novelos') - 3
    L.clara(c, 690, 880, 380 * back(ramp(f, 0, 10)) if f < 10 else 400, f, 0)
    put_prof(c, 330, 1830, 700, f, expr='neutral' if f < n else 'grin', arms='chin' if f < n else 'point', look=1)
    if f >= n: paste_c(c, txt('NOVELOS', 100, -5), 690, 420, back(ramp(f, n, n + 8)))
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (640, 1150, z, 0), 'day'


def s2(f):
    k = wt(2, 'calor') - 3
    a = wt(2, 'abrem') - 3
    c = cena_base('day', f, 420 + 160 * easeOut(ramp(f, k, k + 10)))
    u = smooth(ramp(f, wt(2, 'desmancha') - 3, a + 6))
    L.clara(c, 690, 880, 380, f, u)
    put_prof(c, 330, 1830, 700, f, expr='shock' if f >= a else 'neutral', arms='up' if f >= a else 'point', look=1)
    if k <= f < a: paste_c(c, txt('CALOR!', 100, 6), 900, 1380, back(ramp(f, k, k + 8)))
    if f >= a: paste_c(c, txt('ABRIU!', 110, -5), 690, 420, back(ramp(f, a, a + 8)))
    z = lerp(1.18, 1.1, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (640, 1150 + kick(f, a, .5) * 8, z, math.sin(f * .05) * 1.2), 'day'


def s3(f):
    c = cena_base('day', f, 560)
    g = wt(3, 'agarram') - 3
    r = wt(3, 'rede') - 3
    L.clara(c, 690, 880, 380, f, 1, smooth(ramp(f, g, r + 4)))
    put_prof(c, 330, 1830, 700, f, expr='grin', arms='point' if f >= g else 'chin', look=1)
    if f >= r: paste_c(c, txt('REDE!', 120, 5), 640, 420, back(ramp(f, r, r + 8)))
    z = lerp(1.1, 1.22, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (660, lerp(1150, 1080, smooth(ramp(f, 0, 80))), z, 0), 'day'


def s4(f):
    c = cena_base('dusk', f, 560)
    p = wt(4, 'prende') - 3
    b = wt(4, 'branco') - 3
    L.clara(c, 690, 880, 380, f, 1, 1, smooth(ramp(f, b - 10, b + 6)), smooth(ramp(f, p, p + 20)))
    put_prof(c, 330, 1830, 700, f, expr='proud' if f >= b else 'neutral', arms='up' if f >= b else 'point', look=1)
    if p <= f < b - 10: paste_c(c, txt('PRESA!', 100, -5), 640, 420, back(ramp(f, p, p + 8)))
    if f >= b: paste_c(c, txt('SÓLIDO!', 120, 5), 640, 420, back(ramp(f, b, b + 8)))
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.22, 1.1, t) * (1 + .0009 * f)
    return c, (660, 1100, z, lerp(2, 0, t)), 'dusk'


def s5(f):
    c = cena_base('dusk', f)
    bt = wt(5, 'batata') - 3
    am = wt(5, 'amolece') - 3
    pd = wt(5, 'parte') - 3
    paste_c(c, L.ovo_img(170, 1), 1080, 1640)
    if f >= bt:
        paste_c(c, L.batata_img(300, 1, 1 if f >= am else 0), 820, lerp(1440, 1250, back(ramp(f, bt, bt + 10))))
    put_prof(c, 330, 1880, 980, f, expr='smug' if f >= pd else ('shock' if f >= am else 'neutral'),
             arms='chin' if f >= pd else 'point', look=1)
    if am <= f < pd: paste_c(c, txt('AMOLECE?!', 100, -5), 760, 780, back(ramp(f, am, am + 8)))
    if f >= pd:
        paste_c(c, txt('CONTINUA...', 100, -5), 680, 700, back(ramp(f, pd, pd + 8)))
        paste_c(c, txt('PARTE 2: 19H', 84, -5), 700, 830, back(ramp(f, pd + 4, pd + 12)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (640, lerp(1250, 1200, t) + kick(f, am, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
