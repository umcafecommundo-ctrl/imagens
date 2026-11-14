"""Formato DESENHO: por que os dias em português terminam em "feira" (Curiosidades da IA, 14/11/2026, 12h).
Categoria: HISTÓRIA.
Fatos: Xataka Brasil (linguista Marco Neves, Univ. NOVA de Lisboa) e Correio Braziliense: os romanos davam aos dias
nomes de astros/deuses (Lua, Marte, Mercúrio, Júpiter, Vênus, Saturno, Sol), que o espanhol e o italiano mantêm
(lunes, martes / lunedì, martedì); por volta de 536 d.C. um bispo de Braga (hoje Portugal) quis acabar com os nomes
pagãos e espalhou o costume da liturgia de contar os dias em latim como "feria secunda", "feria tertia"; virou
segunda-feira. "Feria" em latim = dia de festa/descanso, origem da palavra "feriado". O português é uma das únicas
línguas latinas assim.
Cenários: s0 escola (aula de espanhol, lunes = Lua) | s1 antiga (Roma, astros dos dias) | s2 mapa (Espanha e Itália) |
s3 antiga ao dourado (o bispo há ~1.500 anos) | s4 antiga ao entardecer (bispo com pergaminho FERIA SECUNDA) |
s5 cidade (calendário moderno) | s6 quarto ao entardecer (segunda de manhã = feriado?)."""
from kit import *
import kit, os, importlib.util
from art import face

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h0810', '2026-11-08-10h')
pessoa = _m.pessoa

LINES = [
    "Em espanhol, a segunda é o dia da Lua. Em português, é só... segunda-feira.",
    "Na Roma antiga, cada dia tinha nome de astro ou de deus: Lua, Marte, Mercúrio, Júpiter, Vênus.",
    "O espanhol e o italiano guardaram esses nomes até hoje.",
    "Mas, há uns mil e quinhentos anos, um bispo de onde hoje é Portugal não queria dia com nome de deus pagão.",
    "Você vê, a Igreja já contava os dias em latim com a palavra féria: féria segunda, féria terça.",
    "O jeito pegou por aqui, e virou segunda-feira, terça-feira.",
    "Ou seja: o dia mais odiado da semana... tem nome de feriado.",
]
CAPTXT = [
    "Em espanhol, a segunda é o dia da Lua.|Em português, é só... segunda-feira.",
    "Na Roma antiga, cada dia tinha nome de astro ou de deus:|Lua, Marte, Mercúrio, Júpiter, Vênus.",
    "O espanhol e o italiano guardaram esses nomes até hoje.",
    "Mas, há uns 1.500 anos, um bispo de onde hoje é Portugal|não queria dia com nome de deus pagão.",
    "Você vê, a Igreja já contava os dias em latim com a palavra feria:|feria segunda, feria terça.",
    "O jeito pegou por aqui, e virou segunda-feira, terça-feira.",
    "Ou seja: o dia mais odiado da semana...|tem nome de feriado.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [3]
CHECK = [(0, 'lua', 4), (0, 'portugues', 6), (1, 'marte', 4), (1, 'venus', 4), (2, 'italiano', 4), (3, 'bispo', 4),
         (3, 'pagao', 6), (4, 'feria', 4), (4, 'terca', 6), (5, 'virou', 6), (6, 'feriado', 8)]

ROXO = '#7b3f8c'


def bispo(**kw):
    im = pessoa(dress=ROXO, shirt=ROXO, hair='#d9d9d9', **kw).copy()
    p = Pen(600, 1000)
    hc = (300, 262)
    gold = hexc('#e8c25a')
    p.shape([(hc[0] - 92, hc[1] - 70), (hc[0] - 78, hc[1] - 200), (hc[0], hc[1] - 290), (hc[0] + 78, hc[1] - 200),
             (hc[0] + 92, hc[1] - 70)], hexc('#f4efe2'), hexc('#d6cdb6'), 5, 10)
    p.line([(hc[0], hc[1] - 80), (hc[0], hc[1] - 270)], gold, 14, 3)
    p.line([(hc[0] - 50, hc[1] - 180), (hc[0] + 50, hc[1] - 180)], gold, 14, 3)
    p.shape([(hc[0] - 94, hc[1] - 96), (hc[0] + 94, hc[1] - 96), (hc[0] + 94, hc[1] - 66), (hc[0] - 94, hc[1] - 66)], gold, None, 4, 0)
    im.alpha_composite(p.img.resize(im.size, Image.LANCZOS))
    return im


def put_bispo(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'bispo', x, feet, h, f, seed, **kw)


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


ASTROS = {'lua': ('#e9e6dc', 0), 'marte': ('#d9573a', 0), 'mercurio': ('#9aa0a8', 0), 'jupiter': ('#e3a15a', 1),
          'venus': ('#f2d36b', 0), 'sol': ('#ffc93c', 2)}


@lru_cache(maxsize=16)
def astro_img(nome, r):
    col, kind = ASTROS[nome]
    p = Pen(300, 300)
    if kind == 2:
        for i in range(12):
            a = i * math.pi / 6
            p.line([(150 + 100 * math.cos(a), 150 + 100 * math.sin(a)), (150 + 140 * math.cos(a), 150 + 140 * math.sin(a))], hexc(col), 14, 4)
    p.shape(ell_pts(150, 150, 95, 95), hexc(col), mul(hexc(col), .8), 6, 16)
    if kind == 1:
        for y, w in ((115, 80), (150, 92), (185, 78)):
            p.line([(150 - w, y), (150 + w, y)], hexc('#b86a36'), 10, 0)
    if nome in ('lua', 'mercurio'):
        for (x, y, rr) in ((120, 120, 18), (180, 170, 14), (130, 190, 10)):
            p.shape(ell_pts(x, y, rr, rr), mul(hexc(col), .85), None, 3, 0)
    return p.img.resize((r * 2, r * 2), Image.LANCZOS)


@lru_cache(maxsize=16)
def folha_img(texto, w=420, icon=''):
    h = int(w * 1.15)
    p = Pen(420, 483)
    p.shape([(20, 40), (400, 40), (400, 470), (20, 470)], hexc('#ffffff'), hexc('#dfe3e8'), 6, 10)
    p.shape([(20, 40), (400, 40), (400, 130), (20, 130)], hexc('#e04a3c'), None, 6, 0)
    for x in (110, 310): p.shape(ell_pts(x, 40, 14, 24), hexc('#6f7783'), None, 4, 0)
    im = p.img.resize((420, 483), Image.LANCZOS)
    partes = texto.split('|')
    for j, parte in enumerate(partes):
        t = txt(parte, 70)
        if t.size[0] > 370: t = t.resize((370, int(t.size[1] * 370 / t.size[0])), Image.LANCZOS)
        yc = (400 if icon else 300) + (j - (len(partes) - 1) / 2) * 95
        im.alpha_composite(t, (210 - t.size[0] // 2, int(yc - t.size[1] // 2)))
    if icon:
        a = astro_img(icon, 90)
        im.alpha_composite(a, (210 - 90, 160))
    return im.resize((w, h), Image.LANCZOS)


@lru_cache(maxsize=4)
def pergaminho_img(w):
    p = Pen(600, 400)
    p.shape([(60, 60), (540, 60), (540, 340), (60, 340)], hexc('#f3e2b8'), hexc('#d9c08a'), 6, 10)
    for x in (60, 540): p.shape(ell_pts(x, 200, 36, 160), hexc('#e2c88f'), hexc('#bfa36a'), 6, 8)
    im = p.img.resize((600, 400), Image.LANCZOS)
    for i, tx in enumerate(('FERIA SECUNDA', 'FERIA TERTIA')):
        t = txt(tx, 54)
        if t.size[0] > 420: t = t.resize((420, int(t.size[1] * 420 / t.size[0])), Image.LANCZOS)
        im.alpha_composite(t, (300 - t.size[0] // 2, 140 + i * 110 - t.size[1] // 2))
    return im.resize((w, int(w * 400 / 600)), Image.LANCZOS)


def SFX(s):
    s.ting(s.W(0, 'lua'), .3)
    s.thunk(s.W(0, 'portugues') - 2, 200, .6)
    for i, w in enumerate(('lua', 'marte', 'mercurio', 'jupiter', 'venus')):
        s.thunk(s.W(1, w) - 2, 220 + i * 20, .5)
    s.thunk(s.W(2, 'espanhol') - 2, 240, .5); s.thunk(s.W(2, 'italiano') - 2, 260, .5)
    s.thunk(s.W(3, 'bispo') - 2, 160, .7)
    s.thunk(s.W(3, 'pagao') - 2, 120, .8)
    s.whoosh(s.W(4, 'feria') - 6, .4, .4); s.ting(s.W(4, 'segunda'), .3)
    for i in range(2): s.thunk(s.W(5, 'virou') + i * 8, 260, .5)
    s.trill(s.W(6, 'feriado'), 1.0, .3)


def s0(f):
    c = CEN('escola', 'day').copy()
    l = wt(0, 'lua') - 3
    pt = wt(0, 'portugues') - 3
    put_p(c, 330, 1760, 860, f, 4, shirt='#e8a33c', hair='#2a1a10', bun=True, arms='point' if f >= l else 'hang',
          expr='grin', look=1)
    paste_c(c, folha_img('LUNES', 360, 'lua'), 800, 1000, back(ramp(f, l - 4, l + 6)))
    if f >= pt:
        put_p(c, 980, 1780, 760, f, 5, shirt='#3fae6a', arms='shrug', expr='shock', look=-1)
        paste_c(c, txt('E A NOSSA?', 96, -5), 760, 620, back(ramp(f, pt, pt + 8)))
    z = lerp(1.3, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1260 + kick(f, pt, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('antiga', 'day').copy()
    put_p(c, 330, 1760, 820, f, 6, dress='#f4f1e8', shirt='#f4f1e8', hair='#3b2a1e', arms='up', expr='proud', look=1)
    for i, (nome, x, y) in enumerate((('lua', 620, 760), ('marte', 900, 760), ('mercurio', 1060, 980),
                                      ('jupiter', 700, 1040), ('venus', 900, 1220))):
        k = wt(1, nome) - 3
        if f >= k:
            paste_c(c, astro_img(nome, 125), x, y + 8 * math.sin(f * .1 + i), back(ramp(f, k, k + 8)))
    z = lerp(1.1, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (680, lerp(1200, 1250, smooth(ramp(f, 0, 90))), z, 0), 'day'


def s2(f):
    c = CEN('mapa', 'day').copy()
    e = wt(2, 'espanhol') - 3
    it = wt(2, 'italiano') - 3
    if f >= e: paste_c(c, folha_img('LUNES', 380, 'lua'), 420, 1000, back(ramp(f, e, e + 8)))
    if f >= it: paste_c(c, folha_img('LUNEDÌ', 380, 'lua'), 840, 1100, back(ramp(f, it, it + 8)))
    if f >= e: paste_c(c, txt('ESPANHOL', 70, -4), 420, 760, back(ramp(f, e, e + 8)))
    if f >= it: paste_c(c, txt('ITALIANO', 70, 4), 840, 860, back(ramp(f, it, it + 8)))
    z = lerp(1.25, 1.05, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (630, 1120, z, 0), 'day'


def s3(f):
    c = CEN('antiga', 'golden').copy()
    b = wt(3, 'bispo') - 3
    pg = wt(3, 'pagao') - 3
    if f < pg + 2:
        put_bispo(c, 620, 1780, 900 * back(ramp(f, b, b + 9)) if f >= b else 0, f, 2, arms='hang', expr='neutral', look=1)
    else:
        put_bispo(c, 620, 1780, 900, f, 2, arms='point', expr='stern', look=1)
    if f >= b: put_dust(c, 620, 1760, 100, f - b)
    if f < b: paste_c(c, txt('HÁ 1.500 ANOS', 90, -4), 621, 760, back(ramp(f, 2, 10)))
    if f >= pg:
        paste_c(c, astro_img('jupiter', 110), 900, 860)
        paste_c(c, txt('NÃO!', 130, 8), 880, 680, back(ramp(f, pg, pg + 8)))
    z = lerp(1.15, 1.25, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    return c, (680, 1180 + kick(f, pg, .7) * 10, z, 0), 'golden'


def s4(f):
    c = CEN('antiga', 'dusk').copy()
    k = wt(4, 'feria') - 3
    put_bispo(c, 400, 1780, 860, f, 2, arms='ask' if f >= k else 'hang', expr='proud' if f >= k else 'neutral', look=1)
    if f >= k:
        paste_c(c, pergaminho_img(520), 880, 860, back(ramp(f, k, k + 9)))
    t = smooth(ramp(f, 0, 100))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (lerp(620, 660, t), 1200, z, lerp(0, 2, t)), 'dusk'


def s5(f):
    c = CEN('cidade', 'day').copy()
    v = wt(5, 'virou') - 3
    tc = wt(5, 'terça-feira') - 3
    put_p(c, 280, 1780, 820, f, 7, shirt='#2f7fd1', arms='point' if f >= v else 'hang', expr='grin', look=1)
    if f >= v: paste_c(c, folha_img('SEGUNDA|-FEIRA', 400), 740, 900, back(ramp(f, v, v + 8)))
    if f >= tc: paste_c(c, folha_img('TERÇA|-FEIRA', 400), 920, 1160, back(ramp(f, tc, tc + 8)))
    z = lerp(1.2, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (660, 1250, z, 0), 'day'


def s6(f):
    c = CEN('quarto', 'dusk').copy()
    k = wt(6, 'feriado') - 3
    put_p(c, 400, 1780, 900, f, 7, shirt='#2f7fd1', arms='cheek' if f >= k else 'hang',
          expr='shock' if f >= k else 'pained', look=1)
    paste_c(c, folha_img('SEGUNDA', 340), 840, 960)
    if f >= k: paste_c(c, txt('FERIADO?!', 110, -6), 621, 760, back(ramp(f, k, k + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.02, 1.15, t) * (1 + .0009 * f)
    return c, (630, lerp(1250, 1170, t) + kick(f, k, .7) * 10, z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
