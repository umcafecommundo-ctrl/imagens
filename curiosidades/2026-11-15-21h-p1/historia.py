"""Formato DESENHO — FICÇÃO em 2 partes (pedido do Luis em 15/11/2026): "O relógio que volta 1 minuto", PARTE 1.
História inventada (não é fato), narrada pelo Professor Bigode. Parte 2 em 2026-11-16-07h.
Cenários: s0 quarto (Professor apresenta a Bia e o relógio) | s1 escola (prova) e rua (tropeço) | s2 cidade ao entardecer
(ganhando tudo) | s3 cidade à noite (alguém some) | s4 cidade à noite (padeiro, professora, vizinho somem) |
s5 quarto à noite (guarda o relógio na gaveta) | s6 quarto à noite (relógio volta sozinho; Professor faz mistério)."""
from kit import *
import kit, os, importlib.util
from art import face

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1108', '2026-11-08-10h')
pessoa = _m.pessoa
def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)

LINES = [
    "Essa é a Bia. Um dia, ela achou um relógio que volta o tempo um minuto.",
    "Errou a prova? Volta um minuto. Tropeçou na rua? Volta um minuto.",
    "E ela começou a ganhar tudo: jogo, sorteio, até discussão.",
    "Mas um dia ela reparou numa coisa estranha: cada vez que voltava o tempo, alguém da cidade sumia.",
    "Primeiro o padeiro. Depois a professora. Depois o vizinho.",
    "Ela jurou nunca mais girar aquele relógio.",
    "Até que, de madrugada, ele começou a voltar sozinho... e o que aconteceu depois fica pra parte dois.",
]
CAPTXT = [
    "Essa é a Bia. Um dia, ela achou um relógio|que volta o tempo um minuto.",
    "Errou a prova? Volta um minuto.|Tropeçou na rua? Volta um minuto.",
    "E ela começou a ganhar tudo:|jogo, sorteio, até discussão.",
    "Mas um dia ela reparou numa coisa estranha:|cada vez que voltava o tempo, alguém da cidade sumia.",
    "Primeiro o padeiro. Depois a professora.|Depois o vizinho.",
    "Ela jurou nunca mais girar aquele relógio.",
    "Até que, de madrugada, ele começou a voltar sozinho...|e o que aconteceu depois fica pra parte dois.",
]
FALA_TIKTOK = "Quer a parte dois? Comenta sim, e segue pra não perder!"
CTA_TEXTO = "COMENTA: SIM!"
TWIST = 3
FLASH = [5]
CHECK = [(0, 'relogio', 4), (1, 'prova', 4), (1, 'tropecou', 4), (2, 'tudo', 4), (3, 'sumia', 6),
         (4, 'padeiro', 4), (4, 'professora', 4), (4, 'vizinho', 4), (5, 'nunca', 4), (6, 'sozinho', 6), (6, 'dois', 8)]

BIA = dict(skin=2, hair='#2b1d14', shirt='#7b5cd6', pants='#2f3f66', bun=True, pocket=False)


@lru_cache(maxsize=128)
def relogio(size, ang, glow=0):
    im = _m.relogio_bolso(size, ang)
    if glow:
        g = Image.new('RGBA', (size + 160, size + 160), (0, 0, 0, 0))
        d = ImageDraw.Draw(g)
        for r in range(80, 0, -8):
            d.ellipse((80 - r, 80 - r, size + 80 + r, size + 80 + r), fill=(140, 200, 255, int(70 * (1 - r / 80))))
        g.alpha_composite(im, (80, 80))
        return g
    return im


def rel(c, x, y, size, ang=0.0, glow=0, s=1.0):
    size = int(size * s)
    if size < 10: return
    paste_c(c, relogio(size, round(ang * 8) / 8, glow), x, y)


def fantasma(c, fn, a):
    """desenha fn(camada) e aplica opacidade a (0..1)."""
    if a <= .02: return
    L = Image.new('RGBA', c.size, (0, 0, 0, 0))
    fn(L)
    if a < .98:
        al = L.split()[3].point(lambda v: int(v * a))
        L.putalpha(al)
    c.alpha_composite(L)


def volta(c, x, y, f, f0, r=170):
    """seta circular anti-horária girando (efeito de voltar o tempo)."""
    if f < f0 or f > f0 + 18: return
    t = (f - f0) / 18
    d = ImageDraw.Draw(c)
    a0 = -t * 360
    d.arc((x - r, y - r, x + r, y + r), a0, a0 + 270, fill=(120, 190, 255, int(255 * (1 - t))), width=16)


def SFX(s):
    s.ting(s.W(0, 'relogio'), .35)
    for w in ('prova', 'tropecou'):
        s.thunk(s.W(1, w) - 2, 200, .6)
    for i in range(2): s.whoosh(s.W(1, 'volta', i) - 4, .5, .4)
    for w in ('jogo', 'sorteio', 'discussao'): s.ting(s.W(2, w), .25)
    s.whoosh(s.W(3, 'sumia') - 4, .6, .5)
    for w in ('padeiro', 'professora', 'vizinho'): s.whoosh(s.W(4, w) - 4, .4, .4)
    s.thunk(s.W(5, 'nunca') - 2, 160, .7)
    s.patter(s.W(6, 'madrugada'), s.W(6, 'sozinho') + 20, 6, .14)
    s.trill(s.W(6, 'dois'), 1.0, .3)


def s0(f):
    c = CEN('quarto', 'day').copy()
    r = wt(0, 'relogio') - 3
    put_pessoa(c, 860, 1780, 820, f, 2, expr='shock' if f >= r else 'grin', arms='up' if f >= r else 'hang', look=-1, **BIA)
    put_prof(c, 330, 1780, 900, f, expr='grin', arms='point', look=1)
    if f >= r: rel(c, 860, 820, 230, -(f - r) * .12, 1, back(ramp(f, r, r + 9)))
    if f < 50: paste_c(c, txt('PARTE 1', 120, -4), 621, 560, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)))
    z = lerp(1.25, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, r, .6) * 10, z, 0), 'day'


def s1(f):
    p = wt(1, 'prova') - 3
    t = wt(1, 'tropecou') - 3
    v1 = wt(1, 'volta', 0) - 3
    v2 = wt(1, 'volta', 1) - 3
    if f < t:
        c = CEN('escola', 'day').copy()
        put_pessoa(c, 621, 1800, 860, f, 3, expr='pained' if p <= f < v1 + 8 else 'grin', arms='point' if f >= v1 else 'hang', look=1, **BIA)
        if p <= f < v1 + 6: paste_c(c, txt('NOTA 2', 110, -6), 621, 640, back(ramp(f, p, p + 8)))
        if f >= v1 + 6: paste_c(c, txt('NOTA 10!', 110, 6), 621, 640, back(ramp(f, v1 + 6, v1 + 14)))
        volta(c, 621, 1100, f, v1)
        z = lerp(1.1, 1.18, smooth(ramp(f, 0, t))) * (1 + .0009 * f)
        return c, (621, 1280 + kick(f, p, .5) * 8, z, 0), 'day'
    c = CEN('cidade', 'day').copy()
    lf = f - t
    fall = t <= f < v2 + 4
    put_pessoa(c, 621, 1800, 860, f, 3, expr='shock' if fall else 'grin', arms='up' if fall else 'shrug', look=1,
               tilt=-14 * ramp(f, t, t + 8) if fall else 0, **BIA)
    if fall: paste_c(c, txt('OPA!', 110, -6), 621, 660, back(ramp(f, t, t + 8)))
    volta(c, 621, 1100, f, v2)
    z = lerp(1.15, 1.08, smooth(ramp(lf, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, t, .6) * 10, z, 0), 'day'


def s2(f):
    c = CEN('cidade', 'golden').copy()
    ws = [(wt(2, 'jogo') - 3, 'GANHOU!'), (wt(2, 'sorteio') - 3, 'SORTEIO!'), (wt(2, 'discussao') - 3, 'VENCEU!')]
    put_pessoa(c, 621, 1800, 880, f, 4, expr='proud', arms='up' if f >= ws[0][0] else 'hang', look=0, **BIA)
    for i, (k, w) in enumerate(ws):
        if f >= k: paste_c(c, txt(w, 90, (-6, 5, -3)[i]), (470, 820, 621)[i], (700, 820, 560)[i], back(ramp(f, k, k + 8)))
    rel(c, 860, 1250, 150, f * .1)
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (621, 1280, z, 0), 'golden'


def s3(f):
    c = CEN('cidade', 'dusk').copy()
    k = wt(3, 'sumia') - 3
    e = wt(3, 'estranha') - 3
    a = 1 - ramp(f, k, k + 14)
    fantasma(c, lambda L: put_pessoa(L, 960, 1760, 760, f, 5, expr='neutral', look=-1, shirt='#4caf7a', hair='#7a5230', skin=1), a)
    put_pessoa(c, 380, 1800, 860, f, 4, expr='shock' if f >= k else ('nervous' if f >= e else 'neutral'), arms='hang', look=1, **BIA)
    volta(c, 380, 1100, f, k - 10)
    if f >= k: paste_c(c, txt('SUMIU?!', 120, -5), 700, 640, back(ramp(f, k, k + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, k, .6) * 8, z, lerp(0, 2, t)), 'dusk'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    ks = [wt(4, w) - 3 for w in ('padeiro', 'professora', 'vizinho')]
    specs = [(300, dict(shirt='#ffffff', pants='#ffffff', hair='#3b2a1e', skin=3), 'PADEIRO'),
             (621, dict(shirt='#e2574c', dress='#e2574c', hair='#9a9a9a', skin=1, bun=True), 'PROFESSORA'),
             (940, dict(shirt='#4caf7a', hair='#2b1d14', skin=2, mous=True), 'VIZINHO')]
    for i, ((x, kw, lab), k) in enumerate(zip(specs, ks)):
        a = 1 - ramp(f, k + 2, k + 14)
        fantasma(c, lambda L, x=x, kw=kw, i=i: put_pessoa(L, x, 1760, 720, f, 6 + i, expr='shock' if f >= k - 6 else 'neutral', **kw), a)
        if k <= f < k + 22: paste_c(c, txt(lab, 70, (-5, 4, -3)[i]), min(max(x, 330), 900), 760 + i * 40, back(ramp(f, k, k + 6)))
        if k + 6 <= f < k + 26: put_dust(c, x, 1450, 80, f - k - 6, 14)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1280, z, 0), 'dusk'


def s5(f):
    c = CEN('quarto', 'dusk').copy()
    n = wt(5, 'nunca') - 3
    put_pessoa(c, 500, 1800, 880, f, 7, expr='stern' if f >= n else 'nervous', arms='point' if f >= n else 'hang', look=1, **BIA)
    gx = lerp(820, 940, easeOut(ramp(f, n, n + 14)))
    gy = lerp(1100, 1500, easeOut(ramp(f, n, n + 14)))
    # gaveta (cômoda)
    d = ImageDraw.Draw(c)
    d.rectangle((800, 1420, 1100, 1760), fill=(150, 104, 66, 255), outline=(36, 23, 38, 255), width=6)
    d.rectangle((830, 1460, 1070, 1580), fill=(170, 120, 78, 255), outline=(36, 23, 38, 255), width=5)
    if f < n + 14: rel(c, gx, gy, 170, 0)
    if f >= n: paste_c(c, txt('NUNCA MAIS!', 110, -5), 640, 640, back(ramp(f, n, n + 8)))
    z = lerp(1.1, 1.2, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1280 + kick(f, n + 14, .6) * 10, z, 0), 'dusk'


def s6(f):
    c = CEN('quarto', 'dusk').copy()
    m = wt(6, 'sozinho') - 3
    d2 = wt(6, 'dois') - 3
    d = ImageDraw.Draw(c)
    d.rectangle((800, 1420, 1100, 1760), fill=(150, 104, 66, 255), outline=(36, 23, 38, 255), width=6)
    d.rectangle((830, 1460, 1070, 1580), fill=(170, 120, 78, 255), outline=(36, 23, 38, 255), width=5)
    if f >= m - 10:
        sh = 6 * math.sin(f * 2.1)
        rel(c, 950 + sh, 1250, 220, -(f - m) * .25, 1, back(ramp(f, m - 10, m)))
        volta(c, 950, 1250, f, m + ((f - m) // 20) * 20 if f >= m else m)
        if f >= m: paste_c(c, txt('TIC... TAC...', 80, 5), 780, 900, back(ramp(f, m, m + 8)))
    put_prof(c, 380, 1800, 940, f, expr='nervous' if f < d2 else 'smug', arms='chin', look=1)
    if f >= d2: paste_c(c, txt('CONTINUA...', 110, -5), 621, 620, back(ramp(f, d2, d2 + 8)))
    t = easeOut(ramp(f, 0, 70))
    z = lerp(1.03, 1.16, t) * (1 + .0006 * f)
    return c, (640, lerp(1300, 1260, t), z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
