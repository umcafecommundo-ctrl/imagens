"""Formato DESENHO: por que a gente vê o raio antes de ouvir o trovão (Curiosidades da IA, 11/11/2026, 12h).
Categoria: CIÊNCIA DO DIA A DIA.
Fatos: Governo do Canadá (Environment and Climate Change Canada, "How thunder sounds"): o raio esquenta o ar a cerca de
30.000 °C em menos de um segundo, cinco vezes a temperatura da superfície do Sol; o ar se expande rápido e a onda de choque
é o trovão; o som anda ~0,3 km/s e a luz ~300.000 km/s; conte os segundos entre o clarão e o trovão e divida por 3 para ter
a distância em km (15 s = ~5 km). NOAA/NWS (weather.gov, "Understanding Lightning: Thunder"): o canal do raio chega a
~50.000 °F (~27.700 °C), cerca de cinco vezes a superfície do Sol; a luz chega quase na hora. Som no ar: ~340 m/s."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10c', '2026-11-08-10h')
pessoa = _h10.pessoa
kit.pessoa = pessoa
import art as _art; _art.pessoa = pessoa


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


LINES = [
    "O raio e o trovão acontecem ao mesmo tempo. Mas você vê um antes de ouvir o outro.",
    "O raio esquenta o ar em volta a uns trinta mil graus, numa fração de segundo.",
    "Isso é cinco vezes mais quente que a superfície do Sol.",
    "O ar se expande de repente, como uma explosão. Esse estrondo é o trovão.",
    "Só que a luz é tão rápida que o clarão chega na sua janela quase na hora.",
    "Já o som anda só uns trezentos e quarenta metros por segundo.",
    "Você vê, por isso dá pra fazer a conta: conte os segundos entre o clarão e o trovão e divida por três. É a distância em quilômetros.",
    "Ou seja: o trovão não chega atrasado... ele só vem a pé.",
]
CAPTXT = [
    "O raio e o trovão acontecem ao mesmo tempo.|Mas você vê um antes de ouvir o outro.",
    "O raio esquenta o ar em volta a uns 30 mil graus,|numa fração de segundo.",
    "Isso é cinco vezes mais quente que a superfície do Sol.",
    "O ar se expande de repente, como uma explosão.|Esse estrondo é o trovão.",
    "Só que a luz é tão rápida que o clarão chega|na sua janela quase na hora.",
    "Já o som anda só uns 340 metros por segundo.",
    "Você vê, por isso dá pra fazer a conta: conte os segundos|entre o clarão e o trovão e divida por três.|É a distância em quilômetros.",
    "Ou seja: o trovão não chega atrasado... ele só vem a pé.",
]
FALA_TIKTOK = "Você já fez essa conta? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 6
FLASH = [4]
CHECK = [(0, 'raio', 4), (0, 'trovao', 6), (1, 'trinta', 4), (2, 'sol', 4), (3, 'explosao', 4), (3, 'trovao', 6),
         (4, 'clarao', 4), (5, 'trezentos', 4), (6, 'segundos', 4), (6, 'tres', 6), (6, 'quilometros', 6), (7, 'pe', 8)]

# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 cidade em tempestade à noite (raio cai atrás dos prédios) | s1 cidade em tempestade (close no raio, ar em brasa)
# s2 cidade em tempestade (raio ao lado de um Sol para comparar) | s3 cidade em tempestade (ondas do estrondo saindo do raio)
# s4 sala com janela e tempestade lá fora (clarão entra na hora) | s5 sala (o "BRUUM" andando devagar da janela)
# s6 sala ao entardecer (pessoa contando 1, 2, 3 e a conta) | s7 sala ao entardecer (o BRUUM chega a pé)

RAIN = (190, 205, 235, 170)


@lru_cache(maxsize=2)
def tempestade():
    """cidade à noite com nuvens de chuva escuras."""
    im = CEN('cidade', 'dusk').copy()
    sky = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(sky)
    d.rectangle((0, 0, 1242, 1300), fill=(20, 22, 45, 120))
    p = Pen(1242, 2208)
    for cx, cy, r in ((180, 230, 170), (470, 180, 200), (800, 240, 190), (1100, 200, 180), (330, 380, 160), (950, 400, 170)):
        p.shape(ell_pts(cx, cy, r * 1.3, r * .7, 40), hexc('#4a4e6a'), hexc('#353850'), 5, 18)
    sky.alpha_composite(p.img)
    im.alpha_composite(sky)
    return im


@lru_cache(maxsize=4)
def bolt_img(h=900, seed=1):
    p = Pen(400, 1000)
    rnd = random.Random(seed)
    pts = [(200, 0)]
    y = 0
    while y < 1000:
        y += rnd.randint(90, 150)
        pts.append((200 + rnd.randint(-90, 90), min(1000, y)))
    left = [(x - 22, y) for x, y in pts]; right = [(x + 22, y) for x, y in reversed(pts)]
    p.shape(left + right, hexc('#fff59a'), hexc('#ffd84a'), 5, 6)
    return p.img.resize((int(h * .4), h), Image.LANCZOS)


def raio(c, x, y_top, h, a=1.0, glow=True):
    if a <= 0 or h < 8: return
    if glow:
        g = Image.new('RGBA', c.size, (0, 0, 0, 0))
        ImageDraw.Draw(g).rectangle((0, 0) + c.size, fill=(255, 255, 230, int(90 * a)))
        c.alpha_composite(g)
    im = bolt_img(int(h))
    if a < 1:
        im = im.copy(); im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
    c.alpha_composite(im, (int(x - im.width / 2), int(y_top)))


def chuva(c, f, n=40, seed=3, box=(0, 0, 1242, 2208)):
    d = ImageDraw.Draw(c)
    rnd = random.Random(seed)
    x0, y0, x1, y1 = box
    for i in range(n):
        x = rnd.uniform(x0, x1); sp = rnd.uniform(28, 40)
        y = y0 + (rnd.uniform(0, y1 - y0) + f * sp) % (y1 - y0)
        d.line((x, y, x - 8, y + 40), fill=RAIN, width=4)


def janela_tempestade(c, f, flash=0.0):
    """pinta a janela da sala (120..460 x 380..760) com céu de tempestade e chuva."""
    d = ImageDraw.Draw(c)
    col = (40, 44, 80) if flash <= 0 else tuple(int(40 + (255 - 40) * flash) for _ in range(3))
    for (a, b, cc, dd) in ((140, 400, 290, 560), (300, 400, 440, 560), (140, 580, 290, 740), (300, 580, 440, 740)):
        d.rectangle((a, b, cc, dd), fill=col + (255,))
    chuva(c, f, 14, 7, (140, 400, 440, 740))


def bruum(c, x, y, s, f, legs=True, walk=True):
    """o som do trovão com perninhas."""
    if s <= 0: return
    paste_c(c, txt('BRUUM', 110, 3 * math.sin(f * .3)), x, y, s)
    if legs:
        d = ImageDraw.Draw(c)
        ph = f * .35 if walk else 0
        for i, dx in enumerate((-60, 60)):
            sw = 30 * math.sin(ph + i * math.pi) * s
            d.line((x + dx * s, y + 50 * s, x + dx * s + sw, y + 150 * s), fill=(36, 23, 38, 255), width=int(12 * s) + 1)
            d.ellipse((x + dx * s + sw - 26 * s, y + 140 * s, x + dx * s + sw + 26 * s, y + 166 * s), fill=(36, 23, 38, 255))


def SFX(s):
    s.thunk(s.W(0, 'raio') - 2, 200, .6); s.thunk(s.W(0, 'trovao') - 1, 90, 1.0)
    s.patter(0, 120, 12, .1)
    s.ting(s.W(1, 'trinta'), .3); s.ting(s.W(2, 'sol'), .25)
    s.thunk(s.W(3, 'explosao') - 2, 80, 1.0); s.thunk(s.W(3, 'trovao') - 2, 100, .8)
    s.ting(s.W(4, 'clarao') - 1, .3)
    for i in range(4): s.thunk(s.W(5, 'anda') + i * 9, 260, .3)
    for w in ('conte', 'segundos', 'tres'): s.thunk(s.W(6, w) - 1, 300, .4)
    s.ting(s.W(6, 'quilometros'), .3)
    for i in range(4): s.thunk(s.W(7, 'vem') - 6 + i * 6, 260, .3)
    s.trill(s.W(7, 'pe'), 1.0, .3)


def s0(f):
    c = tempestade().copy()
    r = wt(0, 'raio') - 3
    t = wt(0, 'trovao') - 3
    if r <= f < r + 10: raio(c, 640, 0, 1200, 1 - (f - r) / 10 * .3)
    elif f >= r + 10 and (f - r) % 40 < 4: raio(c, 640, 0, 1200, .6, glow=False)
    if f >= t: paste_c(c, txt('BRUUUM!', 120, -6), 621, 760, back(ramp(f, t, t + 8)))
    v = wt(0, 've') - 3
    if f >= v: paste_c(c, txt('VÊ...', 100, 6), 400, 1050, back(ramp(f, v, v + 8)))
    o = wt(0, 'ouvir') - 3
    if f >= o: paste_c(c, txt('...OUVE', 100, -6), 850, 1200, back(ramp(f, o, o + 8)))
    chuva(c, f)
    k = kick(f, r, .8)
    z = lerp(1.0, 1.15, easeOut(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1150 + k * 10, z, k), 'dusk'


def s1(f):
    c = tempestade().copy()
    tr = wt(1, 'trinta') - 3
    heat = smooth(ramp(f, 4, 20))
    if heat > 0:
        g = Image.new('RGBA', c.size, (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse((640 - 260 * heat, 300, 640 + 260 * heat, 1400), fill=(255, 140, 40, int(110 * heat)))
        c.alpha_composite(g)
    raio(c, 640, 100, 1200, 1, glow=(f % 30) < 3)
    if f >= tr: paste_c(c, txt('30.000 °C', 120, -5), 640, 700, back(ramp(f, tr, tr + 8)))
    chuva(c, f, 30)
    z = lerp(1.3, 1.6, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (640, lerp(900, 850, smooth(ramp(f, 0, 90))), z, 0), 'dusk'


def s2(f):
    c = tempestade().copy()
    so = wt(2, 'sol') - 3
    ci = wt(2, 'cinco') - 3
    raio(c, 400, 200, 1100, 1, glow=False)
    if f >= so:
        sz = back(ramp(f, so, so + 10))
        d = ImageDraw.Draw(c)
        for i in range(12):
            a = i * math.pi / 6 + f * .02
            d.line((900 + 170 * sz * math.cos(a), 800 + 170 * sz * math.sin(a), 900 + 230 * sz * math.cos(a), 800 + 230 * sz * math.sin(a)), fill=(255, 200, 60, 255), width=int(16 * sz) + 1)
        d.ellipse((900 - 140 * sz, 800 - 140 * sz, 900 + 140 * sz, 800 + 140 * sz), fill=(255, 210, 70, 255), outline=(36, 23, 38, 255), width=6)
    if f >= ci: paste_c(c, txt('5x MAIS QUENTE', 78, -4), 700, 560, back(ramp(f, ci, ci + 8)))
    chuva(c, f, 30)
    z = 1.25 * (1 + .0012 * f)
    return c, (lerp(560, 680, smooth(ramp(f, 0, 70))), 950, z, 0), 'dusk'


def s3(f):
    c = tempestade().copy()
    e = wt(3, 'expande') - 3
    x = wt(3, 'explosao') - 3
    tv = wt(3, 'trovao') - 3
    raio(c, 640, 0, 1200, 1, glow=e <= f < e + 4)
    d = ImageDraw.Draw(c)
    for i in range(4):
        a = f - e - i * 7
        if a > 0:
            r = a * 22
            al = max(0, 255 - a * 6)
            d.ellipse((640 - r, 800 - r, 640 + r, 800 + r), outline=(255, 240, 180, al), width=10)
    if f >= x: paste_c(c, txt('BUUUM!', 140, -6), 621, 700, back(ramp(f, x, x + 8)))
    if f >= tv: paste_c(c, txt('= TROVÃO', 100, 5), 621, 1080, back(ramp(f, tv, tv + 8)))
    chuva(c, f)
    k = kick(f, x, 1.2)
    z = lerp(1.25, 1.05, easeOut(ramp(f, e - 4, e + 30))) * (1 + .0009 * f)
    return c, (621, 1000 + k * 12, z, k * 1.5), 'dusk'


def s4(f):
    c = CEN('sala', 'dusk').copy()
    cl = wt(4, 'clarao') - 3
    fl = 1 - ramp(f, cl, cl + 10) if f >= cl else 0
    janela_tempestade(c, f, fl)
    if fl > 0:
        g = Image.new('RGBA', c.size, (0, 0, 0, 0))
        ImageDraw.Draw(g).polygon([(140, 400), (440, 400), (1100, 1980), (300, 1980)], fill=(255, 255, 220, int(120 * fl)))
        c.alpha_composite(g)
    put_pessoa(c, 820, 1980, 1050, f, 1, shirt='#2f7fd1', pants='#3b3f4a', pocket=False, skin=2, hair='#2b2b2b',
               expr='shock' if f >= cl else 'neutral', arms='up' if f >= cl else 'hang', look=-1)
    if f >= cl: paste_c(c, txt('FLASH!', 110, -6), 520, 900, back(ramp(f, cl, cl + 8)))
    q = wt(4, 'quase') - 3
    if f >= q: paste_c(c, txt('NA HORA!', 90, 5), 820, 680, back(ramp(f, q, q + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (lerp(560, 680, smooth(ramp(f, 0, 90))), 1250, z, 0), 'dusk'


def s5(f):
    c = CEN('sala', 'dusk').copy()
    janela_tempestade(c, f)
    tz = wt(5, 'trezentos') - 3
    put_pessoa(c, 960, 1980, 1000, f, 1, shirt='#2f7fd1', pants='#3b3f4a', pocket=False, skin=2, hair='#2b2b2b',
               expr='nervous', arms='hang', look=-1)
    bx = lerp(300, 560, ramp(f, 0, 150))
    bruum(c, bx, 1150, 1.0, f)
    if f >= tz: paste_c(c, txt('340 m/s', 110, -5), 560, 700, back(ramp(f, tz, tz + 8)))
    z = 1.12 * (1 + .0009 * f)
    return c, (lerp(520, 640, smooth(ramp(f, 0, 120))), 1250, z, 0), 'dusk'


def s6(f):
    c = CEN('sala', 'dusk').copy()
    janela_tempestade(c, f)
    se = wt(6, 'segundos') - 3
    tr = wt(6, 'tres') - 3
    km = wt(6, 'quilometros') - 3
    put_pessoa(c, 820, 1980, 1050, f, 1, shirt='#2f7fd1', pants='#3b3f4a', pocket=False, skin=2, hair='#2b2b2b',
               expr='grin' if f >= km else 'neutral', arms='point' if f >= se else 'hang', look=-1)
    if se <= f < tr:
        n = 1 + min(2, (f - se) // 12)
        paste_c(c, txt('1... 2... 3...'[:int(n) * 5 - 1], 90, -4), 680, 760, 1)
    if f >= tr: paste_c(c, txt('SEGUNDOS ÷ 3', 72, -4), 680, 760, back(ramp(f, tr, tr + 8)))
    if f >= km: paste_c(c, txt('= km', 110, 5), 680, 920, back(ramp(f, km, km + 8)))
    k = kick(f, km, .6)
    z = lerp(1.1, 1.25, smooth(ramp(f, 0, 150))) * (1 + .0009 * f)
    return c, (lerp(620, 680, smooth(ramp(f, 0, 150))), 1250 + k * 8, z, k), 'dusk'


def s7(f):
    c = CEN('sala', 'dusk').copy()
    janela_tempestade(c, f)
    pe = wt(7, 'pe') - 3
    put_pessoa(c, 960, 1980, 1000, f, 1, shirt='#2f7fd1', pants='#3b3f4a', pocket=False, skin=2, hair='#2b2b2b',
               expr='smug' if f >= pe else 'neutral', arms='shrug' if f >= pe else 'hang', look=-1)
    bx = lerp(250, 620, ramp(f, 0, 90))
    bruum(c, bx, 1200, 1.0, f, walk=f < 90)
    if f >= pe: paste_c(c, txt('A PÉ!', 120, 6), 600, 880, back(ramp(f, pe, pe + 8)))
    z = lerp(1.05, 1.3, easeOut(ramp(f, 0, 80))) * (1 + .0012 * f)
    return c, (lerp(500, 700, smooth(ramp(f, 0, 80))), 1280, z, lerp(0, -3, smooth(ramp(f, 0, 80)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
