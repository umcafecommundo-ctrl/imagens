"""Formato DESENHO: como surgiu o papelzinho de recado que gruda (post-it) (Curiosidades da IA, 06/11/2026, post extra).
Categoria: INVENÇÕES E OBJETOS.
Fatos: MinnPost/MNopedia "How a failed glue experiment and a church choir singer's frustration led to the invention
of Post-it" (1968: cientista da 3M tentava fazer cola forte e obteve uma leve, fácil de soltar; ~5 anos procurando uso
entre colegas; colega com marcadores caindo do livro de hinos do coral; amostras grátis em Boise: ~90% disseram que
comprariam; à venda nos EUA em 1980); History.com (Post-it notes debut, 1980)."""
from kit import *
import kit
from PIL import ImageDraw

LINES = [
    "O papelzinho de recado que gruda nasceu de uma cola que deu errado.",
    "Em mil novecentos e sessenta e oito, um cientista tentava criar uma cola superforte.",
    "Só que saiu o contrário: uma cola fraquinha, que grudava e soltava fácil.",
    "Por uns cinco anos, ele mostrou a cola pros colegas. E ninguém sabia pra que servia.",
    "Até que um colega, que cantava no coral, teve um problema: os marcadores viviam caindo do livro de hinos.",
    "Você vê, ele precisava de um papel que grudasse na página, mas soltasse sem rasgar.",
    "Nos testes com amostras grátis, nove em cada dez pessoas queriam comprar. Em mil novecentos e oitenta, chegou às lojas.",
    "Ou seja: a cola que não servia pra nada... hoje gruda em tudo.",
]
CAPTXT = [
    "O papelzinho de recado que gruda nasceu de uma cola que deu errado.",
    "Em 1968, um cientista tentava criar uma cola superforte.",
    "Só que saiu o contrário: uma cola fraquinha,|que grudava e soltava fácil.",
    "Por uns 5 anos, ele mostrou a cola pros colegas.|E ninguém sabia pra que servia.",
    "Até que um colega, que cantava no coral, teve um problema:|os marcadores viviam caindo do livro de hinos.",
    "Você vê, ele precisava de um papel que grudasse na página,|mas soltasse sem rasgar.",
    "Nos testes com amostras grátis, 9 em cada 10 pessoas queriam comprar.|Em 1980, chegou às lojas.",
    "Ou seja: a cola que não servia pra nada... hoje gruda em tudo.",
]
FALA_TIKTOK = "Você usa esses papeizinhos? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [3, 6]
CHECK = [(0, 'errado', 4), (1, 'superforte', 4), (2, 'soltava', 4), (3, 'ninguem', 6), (4, 'caindo', 4), (5, 'soltasse', 4), (6, 'nove', 6), (6, 'oitenta', 4), (7, 'tudo', 6)]

YEL, YELD = hexc('#ffd84a'), hexc('#e0b52a')


# ------------------------------------------------------------------ objetos novos
@lru_cache(maxsize=64)
def note_img(size=160, rot=0, curl=0.0):
    """papelzinho amarelo quadrado com sombra e cantinho levantado."""
    p = Pen(220, 220)
    s = 160
    x0, y0 = 30, 30
    pts = [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s - 30 * curl), (x0 + s - 30 * curl, y0 + s), (x0, y0 + s)]
    p.shape(pts, YEL, YELD, 5, 10)
    if curl > .05: p.poly([(x0 + s, y0 + s - 30 * curl), (x0 + s - 34 * curl, y0 + s - 34 * curl), (x0 + s - 30 * curl, y0 + s)], YELD, 4)
    for i in range(3): p.stroke([(x0 + 24, y0 + 44 + i * 34), (x0 + s - 30 - (i % 2) * 30, y0 + 44 + i * 34)], 5, hexc('#9b7d2a'))
    im = p.img.resize((size, size), Image.LANCZOS)
    return im.rotate(rot, Image.BICUBIC, expand=True) if rot else im


def note(c, x, y, size=160, rot=0, s=1.0, curl=0.0):
    paste_c(c, note_img(int(size), int(round(rot)), round(curl * 4) / 4), x, y, s)


@lru_cache(maxsize=8)
def book_img(w=420, mark=1.0):
    """livro aberto (livro de hinos) visto de frente; mark = marcador amarelo/branco no meio."""
    p = Pen(520, 360)
    p.shape([(40, 60), (255, 90), (255, 330), (40, 300)], hexc('#f7f1e1'), hexc('#ddd2b8'), 5, 8)
    p.shape([(265, 90), (480, 60), (480, 300), (265, 330)], hexc('#f7f1e1'), hexc('#ddd2b8'), 5, 8)
    p.shape([(30, 300), (260, 340), (490, 300), (490, 320), (260, 352), (30, 320)], hexc('#7a2f3a'), hexc('#561e28'), 5, 4)
    for i in range(5):
        p.stroke([(70, 120 + i * 34), (230, 140 + i * 34)], 4, hexc('#8f8a80'))
        p.stroke([(290, 140 + i * 34), (450, 120 + i * 34)], 4, hexc('#8f8a80'))
    if mark > 0:
        p.shape([(250, 20 + (1 - mark) * 200), (272, 20 + (1 - mark) * 200), (272, 120), (250, 120)], (255, 255, 255), hexc('#dddddd'), 4, 2)
    return p.img.resize((w, int(w * 360 / 520)), Image.LANCZOS)


@lru_cache(maxsize=4)
def flask_img(size=240, fill=0.6):
    p = Pen(300, 360)
    neck = [(120, 30), (180, 30), (180, 130), (270, 320), (30, 320), (120, 130)]
    p.shape(neck, hexc('#e8f4fa'), hexc('#c4dbe6'), 5, 6)
    lv = 320 - 160 * fill
    xl = 120 - (lv - 130) * (90 / 190); xr = 180 + (lv - 130) * (90 / 190)
    p.poly([(xl, lv), (xr, lv), (268, 318), (32, 318)], hexc('#8fd16a'), 0)
    p.stroke(neck + [neck[0]], 5)
    for bx, by, r in ((140, 280, 12), (180, 250, 8), (110, 300, 7)): p.dot(bx, by, r, hexc('#c6f0a8'), 3)
    return p.img.resize((size, int(size * 1.2)), Image.LANCZOS)


@lru_cache(maxsize=4)
def shelf_img():
    p = Pen(1100, 900)
    for k, y in enumerate((260, 560, 860)):
        p.shape([(20, y - 20), (1080, y - 20), (1080, y + 10), (20, y + 10)], hexc('#b98b59'), hexc('#8e6438'), 5, 6)
        for i in range(6):
            x = 70 + i * 170
            for j in range(3):
                yy = y - 30 - j * 40
                p.shape([(x, yy - 34), (x + 130, yy - 34), (x + 130, yy), (x, yy)], YEL if (i + k) % 3 else hexc('#ff9fb2') if (i + k) % 2 else hexc('#8fd6ff'), YELD, 4, 3)
    return p.img


def SFX(s):
    s.thunk(s.W(0, 'errado') - 2, 150, .8)
    s.ting(s.W(1, 'sessenta'), .3)
    s.thunk(s.W(1, 'superforte') - 2, 120, .9)
    s.whoosh(s.W(2, 'soltava') - 4, .35, .45)
    for i in range(3): s.thunk(s.W(3, 'ninguem') + i * 6, 260, .35)
    s.whoosh(s.W(4, 'caindo') - 4, .5, .45); s.thunk(s.W(4, 'caindo') + 8, 300, .5)
    s.ting(s.W(5, 'grudasse'), .3)
    s.ting(s.W(6, 'nove'), .35); s.thunk(s.W(6, 'oitenta') - 2, 160, .8)
    for i in range(6): s.thunk(s.W(7, 'tudo') - 4 + i * 3, 300, .35)
    s.trill(s.W(7, 'tudo') + 6, .8, .25)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    rnd = random.Random(3)
    spots = [(rnd.randint(140, 1100), rnd.randint(330, 1350), rnd.randint(-14, 14)) for _ in range(16)]
    for i, (x, y, r) in enumerate(spots):
        t0 = 2 + i * 2
        if f >= t0: note(c, x, y, 170, r, back(ramp(f, t0, t0 + 7)), curl=.5 * (i % 3 == 0))
    k = wt(0, 'errado') - 3
    put_sci(c, 640, 2080, 1150, f, 2, arms='cheek' if f >= k else 'hang', expr='shock' if f >= k else 'grin', look=0)
    if f >= k: paste_c(c, txt('DEU ERRADO?!', 100, -6), 640, 700, back(ramp(f, k, k + 8)))
    kk = kick(f, k + 2)
    z = lerp(1.35, 1.08, easeOut(ramp(f, 0, 40)))
    return c, (640, 1250 + kk * 10, z, kk), 'day'


def s1(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    a0 = wt(1, 'sessenta') - 3
    if f >= a0: paste_c(c, txt('1968', 140, -5), 680, 700, back(ramp(f, a0, a0 + 8)))
    k = wt(1, 'superforte') - 3
    put_sci(c, 520, 2060, 1120, f, 4, arms='up' if f >= k else 'clip', expr='grin' if f >= k else 'neutral', look=1, hair='#6b4a2f', glasses=True)
    sh = 6 * math.sin(f * .9) if f < k else 0
    paste_c(c, flask_img(260, .4 + .4 * ramp(f, 0, k)).rotate(sh, Image.BICUBIC, expand=True), 930, 1500)
    if f >= k:
        paste_c(c, txt('SUPERFORTE!', 100, 6), 680, 880, back(ramp(f, k, k + 8)))
    kk = kick(f, k + 2)
    z = lerp(1.08, 1.2, smooth(f / 120))
    return c, (680, 1260 + kk * 10, z, kk), 'day'


def s2(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    g0 = wt(2, 'grudava') - 2
    so = wt(2, 'soltava') - 3
    fr = wt(2, 'fraquinha') - 3
    put_sci(c, 420, 2060, 1120, f, 4, arms='point' if f >= g0 else 'hang', expr='shock' if f >= so else 'neutral', look=1, hair='#6b4a2f')
    # o papel gruda na parede e depois sai voando
    if f < so:
        s = back(ramp(f, g0, g0 + 7)) if f >= g0 else 0
        note(c, 920, 1050, 220, -4, s)
    else:
        t = f - so
        note(c, 920 + t * 9, 1050 - 120 * math.sin(min(t, 30) / 30 * math.pi) + max(0, t - 15) * 14, 220, -4 + t * 9, 1.0, curl=1)
    if f >= fr: paste_c(c, txt('FRAQUINHA...', 96, -6), 660, 700, back(ramp(f, fr, fr + 8)))
    z = lerp(1.1, 1.22, smooth(f / 100))
    return c, (660, 1250, z, 0), 'day'


def s3(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(.6))
    spin = ramp(f, 0, 70)
    paste_c(c, clock_img(round((1 + spin * 10) * 8) / 8, round(spin * 120 * 4) / 4, 240), 640, 430)
    a0 = wt(3, 'cinco') - 3
    if f >= a0: paste_c(c, txt('5 ANOS', 120, -6), 640, 700, back(ramp(f, a0, a0 + 8)))
    n0 = wt(3, 'ninguem') - 3
    put_sci(c, 260, 2000, 1000, f, 4, arms='point', expr='grin' if f < n0 else 'nervous', look=1, hair='#6b4a2f')
    note(c, 470, 1450, 150, 6)
    for i, (x, sd, kw) in enumerate(((760, 7, dict(hair='#2b2b2b', skin=2)), (1030, 8, dict(bun=True, hair='#a0522d', skin=1)))):
        put_sci(c, x, 2000 - i * 20, 960, f, sd, arms='hang', expr='neutral' if f < n0 else 'stern', look=-1, glasses=False, **kw)
        if f >= n0 + i * 4: paste_c(c, txt('?', 130, 8 - i * 14), x, 980, back(ramp(f, n0 + i * 4, n0 + i * 4 + 8)))
    z = lerp(1.05, 1.15, smooth(f / 140))
    return c, (640, 1250, z, 0), 'golden'


def s4(f):
    c = BG('golden').copy()
    sing = f < wt(4, 'problema') - 2
    put_sci(c, 560, 2080, 1150, f, 7, arms='clip', expr='grin' if sing else 'shock', look=.4, hair='#2b2b2b', skin=2, glasses=False)
    if sing:
        rings(c, 760, 1010, f % 30, 0, 30, .9)
        paste_c(c, txt('LÁ LÁ LÁ', 90, -8), 760, 800, back(ramp(f, 2, 10)))
    k = wt(4, 'caindo') - 4
    paste_c(c, book_img(440, 1.0 if f < k else 0), 600, 1500)
    if f >= k:
        t = f - k
        bx, by = 610 + t * 4, 1440 + t * t * 1.6
        if by < 2150:
            m = Pen(50, 160); m.shape([(10, 10), (40, 10), (40, 150), (10, 150)], (255, 255, 255), hexc('#dddddd'), 4, 2)
            paste_c(c, m.img.rotate(t * 7, Image.BICUBIC, expand=True), bx, by)
        paste_c(c, txt('CAIU!', 110, 6), 820, 1150, back(ramp(f, k + 4, k + 12)))
    m0 = wt(4, 'hinos') - 3
    if f >= m0 and f < k: pass
    z = lerp(1.08, 1.25, smooth(f / 150))
    kk = kick(f, k + 6)
    return c, (640, 1300 + kk * 10, z, kk), 'golden'


def s5(f):
    c = BG('dusk').copy()
    put_sci(c, 360, 2080, 1150, f, 7, arms='cheek', expr='grin', look=1, hair='#2b2b2b', skin=2, glasses=False)
    g0 = wt(5, 'grudasse') - 3
    so = wt(5, 'soltasse') - 3
    cont = Image.new('RGBA', (460, 380), (0, 0, 0, 0))
    cont.alpha_composite(book_img(420, 0), (20, 60))
    if f >= g0:
        lift = smooth(ramp(f, so, so + 12))
        n = note_img(130, -8, round(lift * 4) / 4)
        cont.alpha_composite(n, (250 + int(lift * 60), int(70 - lift * 80) if lift > 0 else 70))
    thought(c, 820, 700, 300, back(ramp(f, 2, 12)), cont)
    if f >= so: paste_c(c, txt('SEM RASGAR!', 90, 6), 720, 1150, back(ramp(f, so, so + 8)))
    z = lerp(1.05, 1.22, smooth(f / 120))
    return c, (700, 1200, z, lerp(0, -2, smooth(f / 120))), 'dusk'


def s6(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    sh = shelf_img()
    c.alpha_composite(sh.resize((1000, 818)), (120, 330))
    n0 = wt(6, 'nove') - 3
    o0 = wt(6, 'oitenta') - 3
    for i, x in enumerate((230, 450, 670, 890, 1080)):
        happy = f >= n0 + i * 2 and i < 4 or (i == 4 and f >= n0 + 10)
        put_sci(c, x, 2050, 800, f, 10 + i, arms='up' if (happy and i < 4) else 'hang', expr='grin' if (happy and i < 4) else 'neutral',
                look=0, glasses=i % 2 == 0, skin=i % 4, hair=('#2b2b2b', '#a0522d', '#6b4a2f', '#d8b25a', '#3b2a1e')[i], bun=i == 1)
        if f >= wt(6, 'amostras') - 3 + i * 2: note(c, x + 110, 1420, 110, 10 - i * 5, back(ramp(f, wt(6, 'amostras') - 3 + i * 2, wt(6, 'amostras') + 5 + i * 2)))
    if n0 <= f < o0: paste_c(c, txt('9 EM 10', 140, -6), 640, 700, back(ramp(f, n0, n0 + 8)))
    if f >= o0: paste_c(c, txt('1980: NAS LOJAS!', 84, 5), 640, 700, back(ramp(f, o0, o0 + 8)))
    kk = kick(f, o0 + 2)
    z = lerp(1.05, 1.18, smooth(f / 180))
    return c, (640, 1250 + kk * 10, z, kk), 'day'


def s7(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(.8))
    k = wt(7, 'tudo') - 4
    put_sci(c, 640, 2080, 1150, f, 4, arms='hang' if f < k else 'up', expr='smug' if f < k else 'grin', look=0, hair='#6b4a2f')
    rnd = random.Random(9)
    for i in range(22):
        x = rnd.randint(150, 1100); y = rnd.randint(320, 1900); t0 = k + i
        if f >= t0: note(c, x, y, 150, rnd.randint(-20, 20), back(ramp(f, t0, t0 + 6)))
    if f >= k + 6: paste_c(c, txt('GRUDA EM TUDO!', 88, -6), 640, 700, back(ramp(f, k + 6, k + 14)))
    z = lerp(1.25, 1.08, easeOut(ramp(f, 0, 50)))
    return c, (640, 1250, z, lerp(0, 2.5, smooth(ramp(f, 0, 70)))), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6, s7)]
