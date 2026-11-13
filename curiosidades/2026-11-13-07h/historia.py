"""Formato DESENHO: a pegada na Lua dura milhões de anos (Curiosidades da IA, 13/11/2026, 07h). Categoria: ESPAÇO.
Fatos: Space.com, "Eugene Cernan's Legacy: Apollo 17 Commander's Footprints Still on the Moon" (2017): as pegadas e os
equipamentos das missões Apollo (1969-1972) devem durar "muitos milhões de anos"; na Lua não há erosão por vento nem por
água (não há água líquida e quase não há atmosfera); partículas do Sol desgastam a superfície muito devagar; o maior risco
é um meteorito cair em cima. Dawn / ScienceBlog: sem vento e sem chuva, as pegadas devem continuar nítidas por milhões de anos."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h12 = _load('h0612', '2026-11-06-12h')
_h10 = _load('h0810', '2026-11-08-10h')
astronaut = _h12.astronaut
put_astro = _h12.put_astro
pessoa = _h10.pessoa

LINES = [
    "Na Lua tem pegada de astronauta com mais de cinquenta anos.",
    "Aqui na Terra, pegada na areia some rapidinho: o vento e a chuva apagam.",
    "Na Lua não tem vento, nem chuva, nem água nenhuma.",
    "Você vê, sem nada pra mexer na poeira, a pegada pode durar milhões de anos.",
    "Ou seja: o astronauta já foi embora faz tempo. A pegada, ainda não.",
]
CAPTXT = [
    "Na Lua tem pegada de astronauta|com mais de 50 anos.",
    "Aqui na Terra, pegada na areia some rapidinho:|o vento e a chuva apagam.",
    "Na Lua não tem vento, nem chuva,|nem água nenhuma.",
    "Você vê, sem nada pra mexer na poeira,|a pegada pode durar milhões de anos.",
    "Ou seja: o astronauta já foi embora faz tempo.|A pegada, ainda não.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'pegada', 4), (0, 'cinquenta', 6), (1, 'areia', 4), (1, 'vento', 4), (1, 'chuva', 4), (2, 'vento', 4),
         (2, 'chuva', 4), (2, 'agua', 4), (3, 'poeira', 4), (3, 'milhoes', 6), (4, 'embora', 6), (4, 'ainda', 8)]

POE, POE_D = hexc('#b9bcc4'), hexc('#8c9099')


# ------------------------------------------------------------------ cenário e objetos novos
@lru_cache(maxsize=4)
def lua_bg(luz='day'):
    """superfície da Lua: céu preto com estrelas, a Terra no alto, chão cinza com crateras (chão a partir de y≈1250)."""
    W, H = BW, BH
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc('#07091a') if luz != 'dusk' else hexc('#0c0f28'))
    rnd = random.Random(3)
    for i in range(150):
        p.dot(rnd.randint(0, W), rnd.randint(0, 1250), rnd.choice((2, 2, 3, 4)), (255, 255, 230))
    p.shape(ell_pts(930, 380, 150, 150, 64), hexc('#3a86e0'), hexc('#2458a8'), 6, 20)
    p.shape(ell_pts(890, 340, 60, 40, 32, .4, .2), hexc('#5cc46f'), hexc('#3c9a50'), 4, 8)
    p.shape(ell_pts(990, 440, 40, 26, 32, .2, .2), hexc('#5cc46f'), hexc('#3c9a50'), 4, 6)
    hills = [(0, 1260), (200, 1200), (420, 1240), (640, 1180), (880, 1230), (1100, 1190), (W, 1220), (W, H), (0, H)]
    p.shape(hills, hexc('#a7aab3'), hexc('#878a93'), 6, 24)
    for (x, y, r) in ((180, 1420, 90), (1000, 1360, 70), (620, 1900, 120), (1080, 2060, 80), (140, 2100, 60), (400, 1300, 40)):
        p.shape(ell_pts(x, y, r, r * .35, 40), hexc('#8f939c'), hexc('#767a83'), 4, 8)
        p.arc(x - r, y - r * .35, 2 * r, r * .7, 180, 360, 5, hexc('#c9ccd3'))
    return p.img.resize((W, H), Image.LANCZOS)


@lru_cache(maxsize=8)
def bota(w=260, apaga=0.0, face_=''):
    """marca de bota (vista de cima), com sulcos. apaga 0..1 = some; face_ = '' | 'smug' (carinha)."""
    p = Pen(300, 560)
    a = int(255 * (1 - apaga))
    sole = ell_pts(150, 280, 110, 250, 48)
    p.shape(sole, hexc('#6f737c'), hexc('#5b5f68'), 4, 10)
    for k in range(9):
        y = 90 + k * 46
        p.stroke([(70, y), (230, y)], 10, hexc('#8a8e97'))
    if face_:
        face(p, 150, 250, face_, 0, .3, u=3.0)
    im = p.img
    if apaga > 0:
        al = im.split()[3].point(lambda v: v * a // 255)
        im.putalpha(al)
    return im.resize((w, int(w * 560 / 300)), Image.LANCZOS)


def put_bota(c, x, y, w, apaga=0.0, rot=0, face_=''):
    if w < 8: return
    im = bota(int(w), round(apaga * 10) / 10, face_)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


@lru_cache(maxsize=2)
def nuvem_chuva():
    p = Pen(600, 300)
    for (x, y, r) in ((180, 170, 110), (320, 130, 130), (450, 180, 100)):
        p.shape(ell_pts(x, y, r, r * .8, 40), hexc('#8b95a8'), hexc('#6f7a8f'), 5, 10)
    return p.img


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def SFX(s):
    s.ting(s.W(0, 'pegada'), .3)
    s.thunk(s.W(0, 'cinquenta') - 2, 180, .7)
    s.whoosh(s.W(1, 'vento') - 4, .8, .5)
    s.patter(s.W(1, 'chuva'), s.W(1, 'chuva') + 40, 14, .12)
    for i, w in enumerate(('vento', 'chuva', 'agua')): s.thunk(s.W(2, w) - 2, 200 + i * 40, .6)
    s.ting(s.W(3, 'poeira'), .3)
    s.thunk(s.W(3, 'milhoes') - 2, 140, .9)
    s.whoosh(s.W(4, 'embora') - 6, .6, .4)
    s.trill(s.W(4, 'ainda'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 Lua (pegada + astronauta) | s1 praia (Terra: pegada na areia some) | s2 Lua (sem vento/chuva/água)
# s3 Lua ao entardecer (explicação: milhões de anos) | s4 Lua (astronauta vai embora, a pegada fica)
def s0(f):
    c = lua_bg('day').copy()
    k = wt(0, 'pegada') - 3
    put_bota(c, 420, 1720, 300 * back(ramp(f, k, k + 8)), rot=12)
    put_bota(c, 680, 1560, 260 * back(ramp(f, k + 3, k + 11)), rot=6)
    put_astro(c, 950, 1500, 820, f, 1, arms='wave', expr='grin', look=-.6)
    n = wt(0, 'cinquenta') - 2
    if f >= n: paste_c(c, txt('+50 ANOS', 120, -6), 540, 640, back(ramp(f, n, n + 8)))
    t = easeOut(ramp(f, 0, 50))
    z = lerp(1.6, 1.08, t) * (1 + .0009 * f)
    return c, (lerp(520, 660, t), lerp(1650, 1300, t), z, 0), 'day'


def s1(f):
    c = CEN('praia', 'day').copy()
    v = wt(1, 'vento') - 3
    ch = wt(1, 'chuva') - 3
    ap = max(.0, min(.95, .5 * ramp(f, v, v + 20) + .5 * ramp(f, ch, ch + 25)))
    for i, (x, y) in enumerate(((260, 1900), (440, 1760), (600, 1880), (780, 1740))):
        put_bota(c, x, y, 140, apaga=ap, rot=-60 + (i % 2) * 14)
    put_pessoa(c, 760, 1600, 760, f, 2, expr='shock' if f >= v else 'grin', arms='shrug' if f >= ch else 'hang', look=-.8,
               shirt='#ff8a5c')
    if f >= v:
        for i in range(5):
            x0 = ((f - v) * 40 + i * 260) % 1500 - 200
            ImageDraw.Draw(c).line([(x0, 1500 + i * 90), (x0 + 180, 1500 + i * 90)], fill=(255, 255, 255, 200), width=10)
        if f < ch + 10: paste_c(c, txt('VUUUSH!', 100, -6), 520, 1180, back(ramp(f, v, v + 8)))
    if f >= ch:
        paste_c(c, nuvem_chuva(), 470, 800 + 0 * f, back(ramp(f, ch, ch + 8)))
        d = ImageDraw.Draw(c)
        for i in range(24):
            x = 220 + (i * 37) % 520
            y = 900 + ((f - ch) * 38 + i * 53) % 1000
            d.line([(x, y), (x - 8, y + 40)], fill=(120, 170, 230, 230), width=8)
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(560, 680, t), lerp(1500, 1350, t), lerp(1.25, 1.1, t) * (1 + .0009 * f), 0), 'day'


def s2(f):
    c = lua_bg('day').copy()
    put_bota(c, 360, 1820, 260, rot=10)
    put_astro(c, 960, 1560, 860, f, 3, arms='hang' if f < wt(2, 'agua') else 'cheek', expr='neutral' if f < wt(2, 'vento') else 'grin', look=-.4)
    for i, (w, lab) in enumerate((('vento', 'SEM VENTO'), ('chuva', 'SEM CHUVA'), ('agua', 'SEM ÁGUA'))):
        k = wt(2, w) - 3
        if f >= k: paste_c(c, txt(lab, 84, -5 + i * 4), 500, 600 + i * 140, back(ramp(f, k, k + 8)))
    z = (1.12 + .0009 * f)
    return c, (630, 1250 + kick(f, wt(2, 'agua') - 2) * 8, z, 0), 'day'


def s3(f):
    c = lua_bg('dusk').copy()
    p0 = wt(3, 'poeira') - 3
    m = wt(3, 'milhoes') - 3
    put_bota(c, 621, 1480, 420, rot=8)
    if f >= p0:
        for i in range(10):
            a = i * .63
            r = 300 + 20 * math.sin(f * .2 + i)
            c.alpha_composite(Image.new('RGBA', (1, 1)), (0, 0))
            ImageDraw.Draw(c).ellipse([621 + r * math.cos(a) - 10, 1480 + .5 * r * math.sin(a) - 10,
                                       621 + r * math.cos(a) + 10, 1480 + .5 * r * math.sin(a) + 10], fill=(200, 203, 210, 255))
    if f >= m:
        paste_c(c, txt('MILHÕES', 140, -6), 621, 900, back(ramp(f, m, m + 8)))
        paste_c(c, txt('DE ANOS!', 120, 4), 621, 1060, back(ramp(f, m + 3, m + 11)))
    t = smooth(ramp(f, 0, 120))
    return c, (621, lerp(1500, 1250, t), lerp(1.5, 1.15, t) * (1 + .0009 * f), lerp(0, 2, t)), 'dusk'


def s4(f):
    c = lua_bg('dusk').copy()
    e = wt(4, 'embora') - 4
    a = wt(4, 'ainda') - 3
    go = smooth(ramp(f, e, e + 22))
    put_bota(c, 420, 1760, 300, rot=12, face_='smug' if f >= a else '')
    put_bota(c, 680, 1600, 260, rot=6, face_='smug' if f >= a else '')
    put_astro(c, lerp(950, 1600, go), 1500 - 300 * go, 820 * (1 - .3 * go), f, 4, arms='wave' if f >= e else 'hang', expr='grin', look=.6)
    if f >= a: paste_c(c, txt('AINDA AQUI!', 110, -5), 560, 1080, back(ramp(f, a, a + 8)))
    t = smooth(ramp(f, 0, 140))
    return c, (lerp(700, 580, t), lerp(1350, 1450, t), lerp(1.08, 1.3, t) * (1 + .0009 * f), lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
