"""Formato DESENHO: a maior fronteira da França é com o Brasil (Curiosidades da IA, 13/11/2026, 19h). Categoria: LUGARES E GEOGRAFIA.
Fatos: Portal Amazônia (citando a Funag, fundação do governo federal): fronteira Brasil-França de 730 km (427 km por rios,
303 km por terra), entre o Amapá e a Guiana Francesa; é a maior fronteira da França. Xataka Brasil: a Guiana Francesa é um
departamento ultramarino da França; os moradores são cidadãos franceses, usam o euro e elegem deputados para o Parlamento
francês; a fronteira segue boa parte do rio Oiapoque; a ponte binacional sobre o Oiapoque liga Oiapoque (BR) e
Saint-Georges-de-l'Oyapock desde 2017; fronteiras da França com Espanha e Bélgica têm uns 620 km.
Britannica (French Guiana): colônia francesa, virou departamento ultramarino da França em 1946."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h0810', '2026-11-08-10h')
pessoa = _h10.pessoa

LINES = [
    "A maior fronteira da França não fica na Europa. Fica com o Brasil.",
    "Lá no norte do Amapá, do outro lado do rio Oiapoque, fica a Guiana Francesa.",
    "E ela não é um país vizinho: é um pedaço da França. Quem mora lá é francês, vota na França e paga em euro.",
    "São uns setecentos e trinta quilômetros de fronteira, mais do que com a Espanha.",
    "Você vê, a Guiana foi colônia francesa e, em mil novecentos e quarenta e seis, virou parte oficial do país.",
    "E desde dois mil e dezessete, uma ponte liga os dois lados do rio.",
    "Ou seja: dá pra ir do Brasil até a França... a pé.",
]
CAPTXT = [
    "A maior fronteira da França não fica na Europa.|Fica com o Brasil.",
    "Lá no norte do Amapá, do outro lado do rio Oiapoque,|fica a Guiana Francesa.",
    "E ela não é um país vizinho: é um pedaço da França.|Quem mora lá é francês, vota na França e paga em euro.",
    "São uns 730 quilômetros de fronteira,|mais do que com a Espanha.",
    "Você vê, a Guiana foi colônia francesa e, em 1946,|virou parte oficial do país.",
    "E desde 2017, uma ponte|liga os dois lados do rio.",
    "Ou seja: dá pra ir do Brasil até a França... a pé.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'europa', 4), (0, 'brasil', 6), (1, 'oiapoque', 4), (1, 'guiana', 6), (2, 'franca', 4), (2, 'euro', 6),
         (3, 'quilometros', 4), (3, 'espanha', 6), (4, 'colonia', 4), (4, 'oficial', 6), (5, 'ponte', 6), (6, 'pe', 8)]

RIO, RIO_D = hexc('#5fa8d8'), hexc('#3f88b8')


def placa(c, x, y, texto, s=1.0, size=70, rot=0):
    if s <= .02: return
    paste_c(c, txt(texto, size, rot), x, y, s)


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


# ------------------------------------------------------------------ cenários e objetos novos
@lru_cache(maxsize=8)
def rio_bg(luz='day', ponte=False):
    """floresta com um rio descendo no meio da tela: esquerda = Brasil, direita = Guiana Francesa."""
    c = CEN('floresta', luz).copy()
    p = Pen(BW, BH)
    p.shape([(560, 1380), (690, 1380), (900, 2208), (340, 2208)], RIO, RIO_D, 6, 14)
    rnd = random.Random(2)
    for i in range(14):
        y = rnd.randint(1450, 2150); x = lerp(600, 620, rnd.random()) + (y - 1400) * (rnd.random() - .5) * .5
        p.stroke([(x - 30, y), (x + 30, y)], 4, hexc('#a9d6f5'))
    if ponte:
        y = 1560
        p.shape([(300, y - 40), (960, y - 40), (960, y + 10), (300, y + 10)], hexc('#cfd4db'), hexc('#9aa1ad'), 6, 8)
        for x in (420, 520, 740, 840):
            p.shape([(x - 18, y + 10), (x + 18, y + 10), (x + 18, y + 170), (x - 18, y + 170)], hexc('#cfd4db'), hexc('#9aa1ad'), 5, 4)
        p.line(curve((360, y - 40), (630, y - 330), (900, y - 40), 24), hexc('#e3e7ec'), 18, 5)
        for k in range(1, 10):
            x = 360 + k * 54
            yy = y - 40 - 290 * math.sin(math.pi * k / 10) * .98
            p.stroke([(x, y - 40), (x, yy)], 5, hexc('#9aa1ad'))
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


@lru_cache(maxsize=4)
def mapa_bg(luz='day'):
    """mapa com o continente e a Guiana Francesa (amarela) no alto, separada por uma linha tracejada."""
    c = CEN('mapa', luz).copy()
    p = Pen(BW, BH)
    gui = [(600, 400), (760, 400), (900, 470), (880, 640), (760, 700), (640, 660), (590, 520)]
    p.shape(gui, hexc('#f0c24a'), hexc('#c99a2a'), 6, 10)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


def borda(c, f, f0, prog):
    """linha da fronteira desenhada aos poucos (prog 0..1)."""
    pts = [(590, 520), (640, 660), (760, 700), (880, 640)]
    d = ImageDraw.Draw(c)
    L = 3 * prog
    for i in range(3):
        if L <= i: break
        a, b = pts[i], pts[i + 1]
        t = min(1, L - i)
        e = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        d.line([a, e], fill=(227, 38, 43, 255), width=14)


@lru_cache(maxsize=2)
def moeda(r=90):
    p = Pen(200, 200)
    p.shape(ell_pts(100, 100, r, r, 48), hexc('#f2c94c'), hexc('#c9a227'), 5, 10)
    p.shape(ell_pts(100, 100, r * .72, r * .72, 48), hexc('#f7d76a'), None, 3)
    im = p.img.resize((200, 200), Image.LANCZOS)
    paste_c(im, txt('€', 110, 0), 100, 104)
    return im


def SFX(s):
    s.ting(s.W(0, 'europa'), .3)
    s.thunk(s.W(0, 'brasil') - 2, 160, .8)
    s.whoosh(s.W(1, 'oiapoque') - 6, .5, .4); s.ting(s.W(1, 'guiana'), .3)
    s.thunk(s.W(2, 'franca') - 2, 220, .6)
    for w in ('frances', 'vota', 'euro'): s.thunk(s.W(2, w) - 2, 260, .5)
    s.ting(s.W(2, 'euro'), .3)
    s.whoosh(s.W(3, 'quilometros') - 6, .6, .4); s.thunk(s.W(3, 'espanha') - 2, 180, .6)
    s.thunk(s.W(4, 'oficial') - 2, 150, .8)
    s.thunk(s.W(5, 'ponte') - 2, 140, .9)
    for i in range(4): s.thunk(s.W(6, 'ir') + i * 8, 300, .35)
    s.trill(s.W(6, 'pe'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 mapa (Guiana em amarelo, fronteira) | s1 rio na floresta (Brasil x Guiana) | s2 cidade (francês, vota, euro)
# s3 mapa (730 km > Espanha) | s4 cidade ao entardecer (colônia -> 1946) | s5 rio com a ponte | s6 rio com ponte, pessoa atravessa
def s0(f):
    c = mapa_bg('day').copy()
    e = wt(0, 'europa') - 3
    b = wt(0, 'brasil') - 3
    borda(c, f, b, ramp(f, b, b + 20))
    placa(c, 745, 540, 'FRANÇA', back(ramp(f, 2, 10)), 70)
    if f >= e: placa(c, 640, 250, 'NÃO É NA EUROPA!', back(ramp(f, e, e + 8)), 78, -4)
    if f >= b: placa(c, 640, 1000, 'BRASIL', back(ramp(f, b, b + 8)), 120)
    put_pessoa(c, 400, 1700, 640, f, 1, expr='shock' if f >= b else 'neutral', arms='shrug' if f >= b else 'hang', look=.8)
    t = easeOut(ramp(f, 0, 50))
    return c, (lerp(745, 640, t), lerp(560, 1000, t), lerp(2.0, 1.05, t) * (1 + .0009 * f), 0), 'day'


def s1(f):
    c = rio_bg('day').copy()
    o = wt(1, 'oiapoque') - 3
    g = wt(1, 'guiana') - 3
    placa(c, 300, 1250, 'BRASIL', back(ramp(f, 2, 10)), 80)
    if f >= o: placa(c, 625, 1700, 'RIO OIAPOQUE', back(ramp(f, o, o + 8)), 66, -4)
    if f >= g: placa(c, 950, 1180, 'GUIANA', back(ramp(f, g, g + 8)), 76); placa(c, 950, 1270, 'FRANCESA', back(ramp(f, g + 2, g + 10)), 70)
    put_pessoa(c, 260, 1900, 640, f, 2, expr='grin', arms='point' if f >= g else 'hang', look=.9, shirt='#7bc47f')
    t = smooth(ramp(f, 0, 110))
    return c, (lerp(480, 680, t), lerp(1500, 1450, t), lerp(1.25, 1.08, t) * (1 + .0009 * f), 0), 'day'


def s2(f):
    c = CEN('cidade', 'day').copy()
    pf = wt(2, 'franca') - 3
    fr = wt(2, 'frances') - 3
    vo = wt(2, 'vota') - 3
    eu = wt(2, 'euro') - 3
    put_pessoa(c, 640, 1700, 860, f, 3, expr='proud' if f >= fr else 'grin', arms='point' if f >= eu else 'hang', look=.6, shirt='#5c8fd6')
    if f >= pf: placa(c, 640, 480, 'PEDAÇO DA FRANÇA', back(ramp(f, pf, pf + 8)), 76, -3)
    if f >= fr: placa(c, 420, 660, 'FRANCÊS', back(ramp(f, fr, fr + 8)), 70, -5)
    if f >= vo: placa(c, 900, 660, 'VOTA', back(ramp(f, vo, vo + 8)), 76, 5)
    if f >= eu: paste_c(c, moeda(), 1000, 1150, back(ramp(f, eu, eu + 8)) * 1.3)
    t = smooth(ramp(f, 0, 170))
    return c, (lerp(600, 680, t), lerp(1200, 1150, t), lerp(1.1, 1.2, t) * (1 + .0009 * f), 0), 'day'


def s3(f):
    c = mapa_bg('day').copy()
    k = wt(3, 'quilometros') - 3
    es = wt(3, 'espanha') - 3
    borda(c, f, 0, 1)
    placa(c, 745, 540, 'FRANÇA', 1, 70)
    if f >= k: placa(c, 760, 820, '730 km', back(ramp(f, k, k + 8)), 120, -4)
    if f >= es: placa(c, 700, 1000, 'ESPANHA: ~620 km', back(ramp(f, es, es + 8)), 70, 3)
    put_pessoa(c, 980, 1640, 560, f, 4, expr='shock' if f >= es else 'grin', arms='up' if f >= es else 'point', look=-.8, shirt='#ff8a5c')
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(745, 720, t), lerp(700, 1050, t), lerp(1.7, 1.15, t) * (1 + .0009 * f), 0), 'day'


def s4(f):
    c = CEN('cidade', 'dusk').copy()
    co = wt(4, 'colonia') - 3
    an = wt(4, 'quarenta') - 4
    of = wt(4, 'oficial') - 3
    put_pessoa(c, 420, 1700, 820, f, 5, expr='proud' if f >= of else 'neutral', arms='hang', look=.6, shirt='#5c8fd6')
    if co <= f < an: placa(c, 820, 760, 'COLÔNIA', back(ramp(f, co, co + 8)), 90, -4)
    if f >= an: placa(c, 840, 760, '1946', back(ramp(f, an, an + 8)), 140, -4)
    if f >= of: placa(c, 840, 960, 'FRANÇA!', back(ramp(f, of, of + 8)), 100, 4)
    t = smooth(ramp(f, 0, 140))
    return c, (lerp(560, 660, t), 1150 + kick(f, of) * 8, lerp(1.25, 1.1, t) * (1 + .0009 * f), 0), 'dusk'


def s5(f):
    k = wt(5, 'ponte') - 3
    c = rio_bg('day', f >= k).copy()
    if f < k: placa(c, 640, 860, '2017', back(ramp(f, 2, 10)), 140, -4)
    else: placa(c, 640, 860, '2017', 1, 140, -4); placa(c, 630, 1040, 'PONTE!', back(ramp(f, k, k + 8)), 100, 4)
    placa(c, 340, 1250, 'BRASIL', 1, 66); placa(c, 920, 1250, 'GUIANA', 1, 66)
    z = (1.3 + .0009 * f) * (1 + .03 * kick(f, k))
    return c, (630, 1400, z, 0), 'day'


def s6(f):
    c = rio_bg('dusk', True).copy()
    p0 = 4
    pe = wt(6, 'pe') - 3
    walk = smooth(ramp(f, p0, pe + 6))
    x = lerp(340, 920, walk)
    put_pessoa(c, x, 1525, 380, f, 6, expr='smug' if f >= pe else 'grin', arms='hang', look=.8, shirt='#7bc47f', swing=math.sin(f * .5) * walk * (1 - walk) * 4)
    placa(c, 430, 1250, 'BRASIL', 1, 60); placa(c, 870, 1250, 'FRANÇA', 1, 60)
    if f >= pe: placa(c, 640, 1000, 'A PÉ!', back(ramp(f, pe, pe + 8)), 130, -5)
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(560, 700, walk), 1400, lerp(1.3, 1.45, t) * (1 + .0009 * f), lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
