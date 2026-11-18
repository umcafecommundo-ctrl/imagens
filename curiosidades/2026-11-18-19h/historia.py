"""Formato DESENHO: por que a batata amolece quando cozinha — PARTE 2 (Curiosidades da IA, 18/11/2026, 19h).
Categoria: CIÊNCIA DO DIA A DIA. Dupla com 2026-11-18-12h (parte 1: por que o ovo endurece).
Fatos: IFT (Institute of Food Technologists, "Method Matters When Cooking Vegetables"): o que segura as células dos
vegetais umas nas outras é a pectina, e o calor quebra a pectina, soltando as células. America's Test Kitchen ("Why sous
vide is perfect for cooking vegetables"): a parede das células tem celulose, hemicelulose e pectina; a pectina e a
hemicelulose começam a se dissolver entre 88 °C e 92 °C, as células se separam e o vegetal amolece.
Scientific American (parte 1): no ovo, o calor faz as proteínas se ligarem numa rede.
Cenários: s0 cozinha (PARTE 2, Professor com o ovo cozido e a batata na panela) | s1 cozinha + lupa dentro da batata
(células como tijolinhos) | s2 cozinha + lupa (a cola pectina brilha) | s3 cozinha, fogo forte e termômetro + lupa (cola se
desfaz) | s4 cozinha ao entardecer + lupa (células se soltam, garfo entra) | s5 cozinha ao entardecer (Professor, ovo e batata)."""
from kit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '2026-11-18-12h'))
import cozinha_lib as L

LINES = [
    "Na parte um, a gente viu que o ovo endurece na água quente. Então por que a batata amolece?",
    "A batata é feita de células grudadas umas nas outras, como tijolinhos.",
    "E quem segura os tijolinhos é uma cola natural, chamada pectina.",
    "Na água fervendo, lá pelos noventa graus, essa cola começa a se desfazer.",
    "Você vê, sem a cola, as células se soltam, e o garfo entra fácil.",
    "Ou seja: o mesmo calor que gruda o ovo... é o que descola a batata.",
]
CAPTXT = [
    "Na parte 1, a gente viu que o ovo endurece na água quente.|Então por que a batata amolece?",
    "A batata é feita de células grudadas|umas nas outras, como tijolinhos.",
    "E quem segura os tijolinhos|é uma cola natural, chamada pectina.",
    "Na água fervendo, lá pelos 90 graus,|essa cola começa a se desfazer.",
    "Você vê, sem a cola, as células se soltam,|e o garfo entra fácil.",
    "Ou seja: o mesmo calor que gruda o ovo...|é o que descola a batata.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 4
FLASH = []
CHECK = [(0, 'ovo', 4), (0, 'batata', 6), (1, 'celulas', 4), (1, 'tijolinhos', 6), (2, 'pectina', 6),
         (3, 'noventa', 6), (3, 'desfazer', 6), (4, 'soltam', 4), (4, 'garfo', 6), (5, 'descola', 8)]


def SFX(s):
    s.patter(0, 70, 10, .08)
    s.ting(s.W(0, 'ovo'), .25); s.thunk(s.W(0, 'batata') - 2, 160, .7)
    for i in range(5): s.thunk(s.W(1, 'tijolinhos') - 4 + i * 3, 260, .4)
    s.ting(s.W(2, 'pectina'), .35)
    s.whoosh(s.W(3, 'fervendo') - 4, .4, .4); s.ting(s.W(3, 'noventa'), .3)
    s.patter(s.W(3, 'desfazer'), s.W(3, 'desfazer') + 40, 12, .1)
    s.whoosh(s.W(4, 'soltam') - 4, .5, .4); s.thunk(s.W(4, 'garfo') - 2, 300, .8)
    s.trill(s.W(5, 'descola'), 1.0, .3)


def cena_base(luz, f, fogo_w=420):
    c = CEN('cozinha', luz).copy()
    L.fogo(c, 820, 1760, fogo_w, f)
    L.panela(c, 820, 1640, 460, 1, f)
    return c


def s0(f):
    c = cena_base('day', f)
    o = wt(0, 'ovo') - 3
    b = wt(0, 'batata') - 3
    if f >= o:
        mv = smooth(ramp(f, b - 6, b + 6))
        paste_c(c, L.ovo_img(200, 1), lerp(820, 1000, mv), lerp(1000, 900, mv), back(ramp(f, o, o + 8)))
    if f >= b: paste_c(c, L.batata_img(300, 1), 820, lerp(1440, 1250, back(ramp(f, b, b + 10))))
    put_prof(c, 330, 1880, 960, f, expr='shock' if f >= b else 'grin', arms='point', look=1)
    if f < 46: paste_c(c, txt('PARTE 2', 120, -4), 640, 520, back(ramp(f, 0, 8)) * (1 - ramp(f, 40, 46)))
    if f >= b: paste_c(c, txt('AMOLECE?', 110, 5), 760, 700, back(ramp(f, b, b + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1240 + kick(f, b, .6) * 10, z, 0), 'day'


def s1(f):
    c = cena_base('day', f)
    paste_c(c, L.batata_img(280, 0), 820, 1440)
    t = wt(1, 'tijolinhos') - 3
    R = 380 * back(ramp(f, 0, 10)) if f < 10 else 380
    if R > 8: L.celulas(c, 690, 880, R, f)
    put_prof(c, 330, 1830, 700, f, expr='grin' if f >= t else 'neutral', arms='point' if f >= t else 'chin', look=1)
    if f >= t: paste_c(c, txt('TIJOLINHOS', 96, -5), 690, 420, back(ramp(f, t, t + 8)))
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (650, 1150, z, 0), 'day'


def s2(f):
    c = cena_base('day', f)
    p = wt(2, 'pectina') - 3
    g = wt(2, 'cola') - 3
    L.celulas(c, 690, 880, 380, f, 1, 0, pulse(f, g, 999) * (.6 + .4 * math.sin(f * .3)))
    put_prof(c, 330, 1830, 700, f, expr='proud' if f >= p else 'neutral', arms='up' if f >= p else 'point', look=1)
    if g <= f < p: paste_c(c, txt('COLA!', 110, 5), 690, 420, back(ramp(f, g, g + 8)))
    if f >= p: paste_c(c, txt('PECTINA', 110, -5), 690, 420, back(ramp(f, p, p + 8)))
    z = lerp(1.18, 1.25, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (660, 1100, z, 0), 'day'


def s3(f):
    fe = wt(3, 'fervendo') - 3
    n = wt(3, 'noventa') - 3
    d = wt(3, 'desfazer') - 3
    c = cena_base('golden', f, 420 + 180 * easeOut(ramp(f, fe, fe + 10)))
    L.termo(c, 1050, 1760, 560, .25 + .6 * smooth(ramp(f, fe, n)))
    L.celulas(c, 640, 860, 360, f, 1 - .7 * smooth(ramp(f, d, d + 40)), .15 * smooth(ramp(f, d, d + 40)))
    put_prof(c, 300, 1830, 680, f, expr='shock' if f >= d else 'neutral', arms='point', look=1)
    if f >= n: paste_c(c, txt('90 GRAUS', 100, -5), 640, 400, back(ramp(f, n, n + 8)))
    z = lerp(1.08, 1.16, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (660, 1130 + kick(f, n, .5) * 8, z, math.sin(f * .05) * 1.2), 'golden'


def s4(f):
    c = cena_base('dusk', f, 560)
    so = wt(4, 'soltam') - 3
    g = wt(4, 'garfo') - 3
    L.celulas(c, 690, 880, 380, f, .3 * (1 - ramp(f, 0, so)), .15 + .85 * smooth(ramp(f, so - 4, so + 16)))
    if f >= g:
        y = lerp(200, 760, easeOut(ramp(f, g, g + 12)))
        gi = L.garfo_img(620)
        c.alpha_composite(gi, (690 - gi.size[0] // 2, int(y - 620 + 200)))
    put_prof(c, 330, 1830, 700, f, expr='grin' if f >= g else 'neutral', arms='up' if f >= so else 'point', look=1)
    if f >= g: paste_c(c, txt('FÁCIL!', 110, 5), 900, 1300, back(ramp(f, g + 6, g + 14)))
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.22, 1.1, t) * (1 + .0009 * f)
    return c, (660, 1100 + kick(f, g + 8, .6) * 10, z, lerp(2, 0, t)), 'dusk'


def s5(f):
    c = cena_base('dusk', f)
    o = wt(5, 'ovo') - 3
    dc = wt(5, 'descola') - 3
    paste_c(c, L.ovo_img(200, 1, 1), 640, 1150 - (30 * back(ramp(f, o, o + 8)) if f >= o else 0))
    paste_c(c, L.batata_img(300, 1, 1), 900, 1260 + 8 * math.sin(f * .2))
    put_prof(c, 330, 1880, 980, f, expr='grin' if f >= dc else 'smug', arms='point' if f >= o else 'chin', look=1)
    if o <= f < dc: paste_c(c, txt('GRUDA', 100, -5), 680, 880, back(ramp(f, o + 4, o + 12)))
    if f >= dc: paste_c(c, txt('DESCOLA!', 120, -5), 700, 760, back(ramp(f, dc, dc + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (660, lerp(1250, 1200, t) + kick(f, dc, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
