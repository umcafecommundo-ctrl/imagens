"""Formato DESENHO — FICÇÃO em 2 partes (pedido do Luis em 15/11/2026): "O relógio que volta 1 minuto", PARTE 2.
História inventada (não é fato), narrada pelo Professor Bigode. Parte 1 em 2026-11-15-21h-p1.
Cenários: s0 quarto à noite (Professor + PARTE 2, resumo) | s1 cidade à noite (Bia corre pra praça) |
s2 cidade à noite (padeiro, professora e vizinho repetindo o mesmo minuto) | s3 cidade (relógios iguais) |
s4 cidade (Professor explica: quem volta demais fica preso) | s5 cidade (relógio da Bia brilha: ela é a próxima) |
s6 cidade ao amanhecer (larga o relógio, o ponteiro anda pra frente) | s7 cidade de dia (todos voltam; Professor reage)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_p1 = _load('h1115p1', '2026-11-15-21h-p1')
pessoa = _p1.pessoa
put_pessoa, rel, volta, BIA, relogio = _p1.put_pessoa, _p1.rel, _p1.volta, _p1.BIA, _p1.relogio

LINES = [
    "Na parte um, a Bia voltava o tempo um minuto, e a cada volta alguém da cidade sumia.",
    "Quando o relógio começou a voltar sozinho, ela correu pra praça.",
    "E lá estavam o padeiro, a professora e o vizinho, repetindo o mesmo minuto sem parar.",
    "Cada um segurava um relógio igual ao dela.",
    "Você vê, ninguém tinha sumido: quem volta o tempo demais fica preso naquele minuto.",
    "E o relógio dela voltava sozinho porque a próxima a ficar presa era ela.",
    "Então a Bia fez o que ninguém tinha feito: largou o relógio e deixou o minuto passar.",
    "E todo mundo voltou. Ou seja: pra salvar a cidade, ela só precisou... esperar um minuto.",
]
CAPTXT = [
    "Na parte um, a Bia voltava o tempo um minuto,|e a cada volta alguém da cidade sumia.",
    "Quando o relógio começou a voltar sozinho,|ela correu pra praça.",
    "E lá estavam o padeiro, a professora e o vizinho,|repetindo o mesmo minuto sem parar.",
    "Cada um segurava um relógio igual ao dela.",
    "Você vê, ninguém tinha sumido:|quem volta o tempo demais fica preso naquele minuto.",
    "E o relógio dela voltava sozinho|porque a próxima a ficar presa era ela.",
    "Então a Bia fez o que ninguém tinha feito:|largou o relógio e deixou o minuto passar.",
    "E todo mundo voltou. Ou seja: pra salvar a cidade,|ela só precisou... esperar um minuto.",
]
FALA_TIKTOK = "Você faria igual a Bia? Comenta sim ou não, e segue pra mais histórias!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [6]
CHECK = [(0, 'sumia', 4), (1, 'praca', 4), (2, 'padeiro', 4), (2, 'parar', 4), (3, 'relogio', 4), (4, 'preso', 4),
         (5, 'ela', 6), (6, 'largou', 4), (6, 'passar', 4), (7, 'voltou', 4), (7, 'minuto', 8)]

PEOPLE = [(300, dict(shirt='#ffffff', pants='#ffffff', hair='#3b2a1e', skin=3), 'PADEIRO'),
          (621, dict(shirt='#e2574c', dress='#e2574c', hair='#9a9a9a', skin=1, bun=True), 'PROFESSORA'),
          (940, dict(shirt='#4caf7a', hair='#2b1d14', skin=2, mous=True), 'VIZINHO')]


def loop_people(c, f, feet=1760, h=700, watches=0.0, frozen=False, ang_mul=1.0):
    for i, (x, kw, lab) in enumerate(PEOPLE):
        ph = (f + i * 7) % 30
        arms = 'up' if (ph < 15 and not frozen) else 'hang'
        put_pessoa(c, x, feet, h, f, 10 + i, expr='nervous' if not frozen else 'grin', arms=arms, look=0, **kw)
        if watches > 0: rel(c, x, feet - h * 1.12, 110, -f * .2 * ang_mul, 1, watches)


def SFX(s):
    s.whoosh(s.W(0, 'sumia') - 4, .5, .4)
    s.patter(s.W(1, 'sozinho'), s.W(1, 'praca'), 10, .14)
    for w in ('padeiro', 'professora', 'vizinho'): s.thunk(s.W(2, w) - 2, 240, .4)
    s.ting(s.W(3, 'relogio'), .35)
    s.thunk(s.W(4, 'preso') - 2, 160, .8)
    s.thunk(s.W(5, 'ela') - 2, 140, .9)
    s.thunk(s.W(6, 'largou') - 2, 260, .7); s.ting(s.W(6, 'passar'), .35)
    s.trill(s.W(7, 'minuto'), 1.0, .3)


def s0(f):
    c = CEN('quarto', 'dusk').copy()
    k = wt(0, 'sumia') - 3
    put_prof(c, 330, 1780, 920, f, expr='grin' if f < k else 'nervous', arms='point', look=1)
    put_pessoa(c, 880, 1780, 800, f, 2, expr='grin' if f < k else 'shock', arms='hang', look=-1, **BIA)
    rel(c, 880, 900, 180, -f * .1, 1)
    volta(c, 880, 900, f, (f // 24) * 24)
    if f < 50: paste_c(c, txt('PARTE 2', 120, -4), 621, 560, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)))
    if f >= k: paste_c(c, txt('SUMIA!', 110, 5), 621, 600, back(ramp(f, k, k + 8)))
    z = lerp(1.25, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, k, .6) * 10, z, 0), 'dusk'


def s1(f):
    c = CEN('cidade', 'dusk').copy()
    p = wt(1, 'praca') - 3
    x = lerp(150, 900, smooth(ramp(f, 10, p + 10)))
    put_pessoa(c, x, 1800, 820, f, 3, expr='shock', arms='up' if (f // 6) % 2 else 'hang', look=1, **BIA)
    rel(c, x + 140, 1200, 120, -f * .3, 1)
    if f >= p: paste_c(c, txt('PRAÇA!', 110, -5), 621, 640, back(ramp(f, p, p + 8)))
    z = 1.1 * (1 + .0009 * f)
    return c, (lerp(450, 800, smooth(ramp(f, 10, p + 10))), 1300, z, 0), 'dusk'


def s2(f):
    c = CEN('cidade', 'dusk').copy()
    ks = [wt(2, w) - 3 for w in ('padeiro', 'professora', 'vizinho')]
    r = wt(2, 'repetindo') - 3
    for i, ((x, kw, lab), k) in enumerate(zip(PEOPLE, ks)):
        if f >= k:
            ph = (f + i * 7) % 30
            put_pessoa(c, x, 1760, 700 * back(ramp(f, k, k + 8)), f, 10 + i, expr='nervous', arms='up' if (f >= r and ph < 15) else 'hang', look=0, **kw)
            nxt = ks[i + 1] if i < 2 else r
            if f < nxt: paste_c(c, txt(lab, 80, (-5, 4, -3)[i]), min(max(x, 360), 880), 700, back(ramp(f, k, k + 6)))
    if f >= r:
        paste_c(c, txt('DE NOVO... DE NOVO...', 76, -4), 621, 700, back(ramp(f, r, r + 8)))
        for x, _, _ in PEOPLE: volta(c, x, 1180, f, r + ((f - r) // 20) * 20, 120)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1280, z, 0), 'dusk'


def s3(f):
    c = CEN('cidade', 'dusk').copy()
    k = wt(3, 'relogio') - 3
    loop_people(c, f, watches=back(ramp(f, k, k + 9)) if f >= k else 0)
    if f >= k: paste_c(c, txt('IGUAL AO DELA!', 86, 5), 621, 620, back(ramp(f, k, k + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, k, .6) * 8, z, 0), 'dusk'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    s_ = wt(4, 'sumido') - 3
    p = wt(4, 'preso') - 3
    for i, (x, kw, lab) in enumerate(PEOPLE[1:]):
        xx = 700 + i * 300
        put_pessoa(c, xx, 1760, 640, f, 11 + i, expr='nervous', arms='up' if (f + i * 7) % 30 < 15 else 'hang', look=-1, **kw)
        volta(c, xx, 1200, f, (f // 20) * 20, 110)
    put_prof(c, 300, 1790, 900, f, expr='stern' if f >= p else 'neutral', arms='point' if f >= s_ else 'chin', look=1)
    if s_ <= f < p: paste_c(c, txt('NINGUÉM SUMIU', 90, -4), 640, 640, back(ramp(f, s_, s_ + 8)))
    if f >= p: paste_c(c, txt('PRESOS NO MINUTO!', 84, 4), 640, 640, back(ramp(f, p, p + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.05, 1.15, t) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, p, .7) * 10, z, lerp(0, 2, t)), 'dusk'


def s5(f):
    c = CEN('cidade', 'dusk').copy()
    e = wt(5, 'ela') - 3
    put_pessoa(c, 621, 1800, 900, f, 4, expr='shock' if f >= e else 'nervous', arms='hang', look=0, **BIA)
    rel(c, 621, 820, 260, -f * .35, 1)
    volta(c, 621, 820, f, (f // 16) * 16, 200)
    if f >= e: paste_c(c, txt('A PRÓXIMA É ELA!', 78, -5), 621, 600, back(ramp(f, e, e + 8)))
    t = easeOut(ramp(f, 0, 80))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (621, lerp(1300, 1200, t) + kick(f, e, .8) * 12, z, lerp(0, -3, t)), 'dusk'


def s6(f):
    c = CEN('cidade', 'golden').copy()
    l = wt(6, 'largou') - 3
    ps = wt(6, 'passar') - 3
    put_pessoa(c, 500, 1800, 880, f, 5, expr='stern' if f < ps else 'proud', arms='point' if f < l else 'hang', look=1, **BIA)
    if f < l:
        rel(c, 700, 1100, 180, -f * .3, 1)
    else:
        t = easeOut(ramp(f, l, l + 14))
        rel(c, lerp(700, 860, t), lerp(1100, 1700, t), 180, 0)
    # relógio grande da praça: ponteiro anda pra FRENTE
    if f >= l:
        fw = ramp(f, l + 6, ps + 10)
        paste_c(c, clock_img(round(fw * 6 * 4) / 4 + 3.0, round(fw * 12 * 4) / 4, 240), 900, 760, back(ramp(f, l, l + 8)))
    if f >= ps: paste_c(c, txt('+1 MINUTO', 100, 5), 500, 620, back(ramp(f, ps, ps + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, l + 14, .6) * 10, z, 0), 'golden'


def s7(f):
    c = CEN('cidade', 'day').copy()
    v = wt(7, 'voltou') - 3
    m = wt(7, 'minuto') - 3
    for i, (x, kw, lab) in enumerate(PEOPLE):
        xx = (600, 800, 1000)[i]
        put_pessoa(c, xx, 1760, 620 * back(ramp(f, v + i * 3, v + i * 3 + 8)), f, 10 + i, expr='grin', arms='up', look=-1, **kw)
        put_dust(c, xx, 1750, 50, f - v - i * 3)
    put_prof(c, 320, 1800, 900, f, expr='smug' if f < m else 'grin', arms='chin' if f < m else 'shrug', look=1)
    if v <= f < m: paste_c(c, txt('VOLTARAM!', 110, -5), 700, 620, back(ramp(f, v, v + 8)))
    if f >= m: paste_c(c, txt('SÓ ESPERAR!', 110, 5), 640, 640, back(ramp(f, m, m + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.03, 1.12, t) * (1 + .0006 * f)
    return c, (640, lerp(1300, 1260, t), z, 0), 'day'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
