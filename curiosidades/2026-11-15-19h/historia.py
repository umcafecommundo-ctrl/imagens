"""Formato DESENHO: a ilha que muda de país a cada seis meses (Curiosidades da IA, 15/11/2026, 19h).
Categoria: LUGARES E GEOGRAFIA.
Fatos: The Connexion (França, "The tiny Basque island that is both French and Spanish"), Wikipedia "Pheasant Island",
idealista e Islands.com: Ilha dos Faisões, no rio Bidasoa, na fronteira entre França e Espanha; ~210 m de comprimento
e ~40 m de largura; Tratado dos Pireneus assinado ali em 1659 (paz entre os dois países, ilha "das conferências");
condomínio dos dois países: Espanha de 1º de fevereiro a 31 de julho, França de 1º de agosto a 31 de janeiro;
ninguém mora lá e a visita é fechada ao público.
Cenários: s0 beira do rio com a ilha (Professor) | s1 mapa da fronteira | s2 rio no passado (mesa do acordo de 1659) |
s3 rio (duas bandeiras) | s4 rio (calendário troca a bandeira) | s5 rio ao entardecer (Professor e calendário
dividido) | s6 rio ao entardecer (ilha vazia, só passarinhos; Professor reage)."""
from kit import *
import cenarios

LINES = [
    "Existe uma ilha que muda de país a cada seis meses.",
    "É a Ilha dos Faisões, num rio entre a França e a Espanha, com uns duzentos metros de comprimento.",
    "Em mil seiscentos e cinquenta e nove, os dois países assinaram um acordo de paz bem ali.",
    "E desde então, a ilha é dos dois.",
    "De fevereiro a julho, ela é da Espanha. De agosto a janeiro, da França.",
    "Você vê, em vez de brigar pela ilha, eles dividiram... o calendário.",
    "E ninguém mora lá. Ou seja: ela troca de país duas vezes por ano... e ninguém precisa fazer mudança.",
]
CAPTXT = [
    "Existe uma ilha que muda de país a cada seis meses.",
    "É a Ilha dos Faisões, num rio entre a França e a Espanha,|com uns 200 metros de comprimento.",
    "Em 1659, os dois países assinaram|um acordo de paz bem ali.",
    "E desde então, a ilha é dos dois.",
    "De fevereiro a julho, ela é da Espanha.|De agosto a janeiro, da França.",
    "Você vê, em vez de brigar pela ilha,|eles dividiram... o calendário.",
    "E ninguém mora lá. Ou seja: ela troca de país duas vezes por ano...|e ninguém precisa fazer mudança.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [2]
CHECK = [(0, 'seis', 6), (1, 'faisoes', 4), (1, 'duzentos', 4), (2, 'paz', 4), (3, 'dois', 4),
         (4, 'espanha', 4), (4, 'franca', 4), (5, 'calendario', 6), (6, 'mudanca', 8)]

W_, H_ = 1242, 2208


@lru_cache(maxsize=4)
def rio_bg(luz='day'):
    base = cenarios._ceu(luz, 980).copy()
    p = Pen(W_, H_)
    rnd = random.Random(7)
    # montanhas ao fundo (Pireneus)
    p.shape([(-20, 980), (160, 760), (330, 900), (520, 700), (720, 880), (900, 720), (1100, 860), (1262, 780), (1262, 980)],
            hexc('#8fa7c4'), hexc('#7189a8'), 5, 10)
    # margem de lá (Espanha)
    p.shape([(-20, 960), (1262, 960), (1262, 1080), (-20, 1080)], hexc('#6fb04c'), hexc('#548a38'), 5, 6)
    for i in range(9):
        x = 60 + i * 140 + rnd.randint(-20, 20)
        p.shape(ell_pts(x, 960, 70, 60), hexc('#3e8a3a'), hexc('#2f6b2c'), 5, 6)
    # rio
    p.poly([(0, 1080), (W_, 1080), (W_, 1440), (0, 1440)], hexc('#4f9fd6'))
    for i in range(26):
        x, y = rnd.randint(0, W_), rnd.randint(1100, 1420)
        p.stroke([(x, y), (x + 40, y - 6), (x + 80, y)], 4, hexc('#8ccaf0'))
    # ilha comprida no meio do rio
    p.shape(ell_pts(621, 1270, 470, 90), hexc('#8ccf5e'), hexc('#6aa844'), 6, 14)
    for i, x in enumerate((260, 380, 520, 760, 900, 1000)):
        p.line([(x, 1270), (x, 1190)], hexc('#7a4e2c'), 14, 4)
        p.shape(ell_pts(x, 1150, 60 + (i % 2) * 14, 64), hexc('#4b9a3f'), hexc('#367a2e'), 5, 8)
    # margem de cá (França)
    p.shape([(-20, 1440), (W_ + 20, 1440), (W_ + 20, H_ + 20), (-20, H_ + 20)], hexc('#79bd56'), hexc('#5d9c40'), 6, 10)
    for i in range(40):
        x, y = rnd.randint(0, W_), rnd.randint(1500, 2180)
        p.stroke([(x, y), (x + 6, y - 22)], 3, hexc('#5a9a3c'))
    p.stroke([(0, 1440), (W_, 1440)], 7)
    base.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    return base


@lru_cache(maxsize=4)
def fronteira_map():
    base = Image.new('RGBA', (W_, H_), hexc('#5fa8d8') + (255,))
    p = Pen(W_, H_)
    # França em cima, Espanha embaixo, rio fazendo a fronteira na diagonal
    p.shape([(300, -20), (1262, -20), (1262, 1060), (700, 1000), (420, 1110), (300, 1060)], hexc('#9ccf6a'), hexc('#79a94c'), 7, 16)
    p.shape([(300, 1130), (420, 1170), (700, 1060), (1262, 1120), (1262, 2228), (300, 2228)], hexc('#e8c66a'), hexc('#c9a64a'), 7, 16)
    p.line([(300, 1095), (420, 1140), (700, 1030), (1262, 1090)], hexc('#3f8fd0'), 26, 5)
    base.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    return base


@lru_cache(maxsize=32)
def bandeira_img(w, pais, ph=0):
    p = Pen(400, 600)
    p.line([(40, 590), (40, 20)], hexc('#7a5a3a'), 16, 4)
    p.dot(40, 20, 16, hexc('#ffd84a'), 4)
    wv = [8 * math.sin(ph * .8 + i * .9) for i in range(4)]
    x0, x1, y0, y1 = 48, 380, 50, 280
    def q(xa, xb, ya, yb, col):
        ia = (xa - x0) / (x1 - x0) * 3; ib = (xb - x0) / (x1 - x0) * 3
        da = wv[int(ia)] if ia < 3 else wv[3]; db = wv[int(ib)] if ib < 3 else wv[3]
        p.poly([(xa, ya + da), (xb, ya + db), (xb, yb + db), (xa, yb + da)], hexc(col))
    if pais == 'fr':
        for i, col in enumerate(('#2c4fb5', '#ffffff', '#e23b3b')):
            q(x0 + i * 110.7, x0 + (i + 1) * 110.7, y0, y1, col)
    else:
        q(x0, x1, y0, y0 + 58, '#d0272d'); q(x0, x1, y0 + 58, y1 - 58, '#ffcc29'); q(x0, x1, y1 - 58, y1, '#d0272d')
    p.stroke([(x0, y0 + wv[0]), (x1, y0 + wv[3]), (x1, y1 + wv[3]), (x0, y1 + wv[0]), (x0, y0 + wv[0])], 5)
    return p.img.resize((w, int(w * 1.5)), Image.LANCZOS)


def bandeira(c, x, base, w, pais, f, s=1.0):
    w = int(w * s)
    if w < 8: return
    im = bandeira_img(w, pais, (f // 2) % 8)
    c.alpha_composite(im, (int(x - im.size[0] * 40 / 400), int(base - im.size[1] * 590 / 600)))


@lru_cache(maxsize=4)
def mesa_img(w):
    p = Pen(500, 300)
    p.shape([(20, 60), (480, 60), (480, 110), (20, 110)], hexc('#9a6a40'), hexc('#6f4a2a'), 6, 6)
    for x in (60, 440): p.line([(x, 110), (x, 290)], hexc('#6f4a2a'), 22, 5)
    p.shape([(150, 20), (350, 20), (350, 62), (150, 62)], hexc('#f4e6c4'), hexc('#d8c69c'), 5, 4)
    for x in (180, 230, 280): p.stroke([(x, 40), (x + 40, 40)], 3)
    p.line([(330, 30), (390, -20)], hexc('#ffffff'), 8, 3)
    return p.img.resize((w, int(w * 300 / 500)), Image.LANCZOS)


@lru_cache(maxsize=8)
def calendario_img(w, rasgo=0):
    p = Pen(500, 560)
    if rasgo == 0:
        p.shape([(20, 40), (480, 40), (480, 540), (20, 540)], hexc('#ffffff'), hexc('#d9dde3'), 6, 10)
        p.shape([(20, 40), (480, 40), (480, 150), (20, 150)], hexc('#e23b3b'), None, 6, 0)
    else:
        for s, dx in ((-1, -30), (1, 30)):
            xa, xb = (20, 250) if s < 0 else (250, 480)
            pts = [(xa + dx, 40), (xb + dx, 40), (xb + dx, 540), (xa + dx, 540)]
            p.shape(pts, hexc('#ffffff'), hexc('#d9dde3'), 6, 10)
            p.shape([(xa + dx, 40), (xb + dx, 40), (xb + dx, 150), (xa + dx, 150)], hexc('#e23b3b'), None, 6, 0)
    for r in range(4):
        for col in range(5):
            x = 70 + col * 90 + (0 if not rasgo else (-30 if col < 2.5 else 30))
            p.dot(x, 210 + r * 90, 16, hexc('#c4ccd6'))
    for x in (120, 380): p.line([(x, 10), (x, 70)], hexc('#5a5f6b'), 14, 4)
    return p.img.resize((w, int(w * 560 / 500)), Image.LANCZOS)


@lru_cache(maxsize=8)
def passaro_img(w, ph=0):
    p = Pen(200, 120)
    a = 40 if ph else -10
    p.stroke([(20, 60 + a * .3), (100, 70), (180, 60 + a * .3)], 10)
    return p.img.resize((w, int(w * .6)), Image.LANCZOS)


def flag_now(f, k1, k2):
    """troca de bandeira a cada 14 quadros."""
    return 'fr' if (f // 14) % 2 == 0 else 'es'


def SFX(s):
    s.whoosh(s.W(0, 'pais') - 4, .4, .4); s.ting(s.W(0, 'seis'), .3)
    s.thunk(s.W(1, 'faisoes') - 2, 200, .6); s.thunk(s.W(1, 'duzentos') - 2, 240, .5)
    s.thunk(s.W(2, 'paz') - 2, 160, .7); s.ting(s.W(2, 'paz') + 2, .3)
    s.ting(s.W(3, 'dois'), .3)
    s.whoosh(s.W(4, 'espanha') - 4, .4, .4); s.whoosh(s.W(4, 'franca') - 4, .4, .4)
    s.thunk(s.W(5, 'calendario') - 2, 260, .8)
    s.trill(s.W(6, 'mudanca'), 1.0, .3)


def s0(f):
    c = rio_bg('day').copy()
    k = wt(0, 'pais') - 3
    sx = wt(0, 'seis') - 3
    pais = 'fr' if f < k else flag_now(f - k, 0, 0)
    bandeira(c, 640, 1260, 230, pais, f, back(ramp(f, 2, 10)))
    put_prof(c, 340, 1960, 960, f, expr='shock' if f >= k else 'grin', arms='point' if f >= 6 else 'wave', look=1)
    if f >= sx: paste_c(c, txt('A CADA 6 MESES', 96, -5), 640, 660, back(ramp(f, sx, sx + 8)))
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1300 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = fronteira_map().copy()
    fa = wt(1, 'faisoes') - 3
    fr = wt(1, 'franca') - 3
    es = wt(1, 'espanha') - 3
    du = wt(1, 'duzentos') - 3
    if f >= fr: paste_c(c, txt('FRANÇA', 120, -4), 820, 600, back(ramp(f, fr, fr + 8)))
    if f >= es: paste_c(c, txt('ESPANHA', 120, 4), 820, 1500, back(ramp(f, es, es + 8)))
    pul = 1 + .15 * math.sin(f * .3)
    if f >= fa:
        s = back(ramp(f, fa, fa + 8))
        paste_c(c, Image.new('RGBA', (1, 1)), 0, 0)
        pp = Pen(160, 160); pp.shape(ell_pts(80, 80, 60, 26), hexc('#4b9a3f'), hexc('#367a2e'), 5, 4)
        paste_c(c, pp.img.resize((int(150 * s * pul) or 1, int(150 * s * pul) or 1)), 560, 1062)
        paste_c(c, txt('ILHA DOS FAISÕES', 72, -8), 560, 900, s)
    if f >= du: paste_c(c, txt('200 m', 100, 5), 620, 1250, back(ramp(f, du, du + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.0, 1.12, t) * (1 + .0009 * f)
    return c, (lerp(700, 640, t), 1100, z, 0), 'day'


def s2(f):
    c = rio_bg('golden').copy()
    a = wt(2, 'acordo') - 3
    pz = wt(2, 'paz') - 3
    paste_c(c, mesa_img(380), 621, 1180, back(ramp(f, 4, 14)))
    bandeira(c, 330, 1270, 170, 'fr', f, back(ramp(f, a - 6, a + 2)))
    bandeira(c, 850, 1270, 170, 'es', f, back(ramp(f, a - 2, a + 6)))
    paste_c(c, txt('1659', 140, -5), 621, 640, back(ramp(f, 2, 10)))
    if f >= pz: paste_c(c, txt('PAZ!', 130, 6), 621, 820, back(ramp(f, pz, pz + 8)))
    t = smooth(ramp(f, 0, 80))
    z = lerp(1.05, 1.3, t) * (1 + .0009 * f)
    return c, (621, lerp(1250, 1150, t) + kick(f, pz, .6) * 10, z, 0), 'golden'


def s3(f):
    c = rio_bg('day').copy()
    d = wt(3, 'dois') - 3
    bandeira(c, 470, 1260, 190, 'fr', f)
    bandeira(c, 780, 1260, 190, 'es', f + 5)
    put_prof(c, 330, 1960, 900, f, expr='grin' if f >= d else 'neutral', arms='shrug' if f >= d else 'hang', look=1)
    if f >= d: paste_c(c, txt('DOS DOIS!', 120, -5), 640, 660, back(ramp(f, d, d + 8)))
    z = lerp(1.08, 1.18, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1320 + kick(f, d, .6) * 10, z, 0), 'day'


def s4(f):
    c = rio_bg('day').copy()
    es = wt(4, 'espanha') - 3
    fr = wt(4, 'franca') - 3
    ag = wt(4, 'agosto') - 3
    pais = 'es' if f < ag else 'fr'
    bandeira(c, 640, 1260, 230, pais, f)
    paste_c(c, calendario_img(330), 330, 1640)
    if f < ag:
        paste_c(c, txt('FEV A JUL', 72, 0), 330, 1500, back(ramp(f, 4, 12)))
    else:
        paste_c(c, txt('AGO A JAN', 72, 0), 330, 1500, back(ramp(f, ag, ag + 8)))
    if es <= f < ag: paste_c(c, txt('ESPANHA', 110, -5), 760, 660, back(ramp(f, es, es + 8)))
    if f >= fr: paste_c(c, txt('FRANÇA', 110, 5), 760, 660, back(ramp(f, fr, fr + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1300 + kick(f, ag, .6) * 10, z, 0), 'day'


def s5(f):
    c = rio_bg('dusk').copy()
    b = wt(5, 'brigar') - 3
    k = wt(5, 'calendario') - 3
    bandeira(c, 640, 1260, 200, flag_now(f, 0, 0), f)
    put_prof(c, 330, 1960, 900, f, expr='stern' if f < k else 'proud', arms='chin' if f < k else 'point', look=1)
    paste_c(c, calendario_img(380, 1 if f >= k else 0), 880, 1660, back(ramp(f, 6, 14)))
    if b <= f < k: paste_c(c, txt('BRIGA?', 110, -5), 640, 660, back(ramp(f, b, b + 8)))
    if f >= k: paste_c(c, txt('METADE CADA!', 100, 5), 640, 660, back(ramp(f, k, k + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (621, 1350 + kick(f, k, .7) * 10, z, lerp(0, 2, t)), 'dusk'


def s6(f):
    c = rio_bg('dusk').copy()
    n = wt(6, 'ninguem') - 3
    m = wt(6, 'mudanca') - 3
    bandeira(c, 640, 1260, 200, flag_now(f, 0, 0), f)
    for i in range(4):
        x = (200 + i * 260 + f * 4) % 1300 - 30
        paste_c(c, passaro_img(80, (f // 6 + i) % 2), x, 820 + 40 * math.sin(f * .08 + i))
    if f >= n and f < m: paste_c(c, txt('NINGUÉM MORA', 90, -4), 640, 640, back(ramp(f, n, n + 8)))
    put_prof(c, 360, 1960, 920, f, expr='smug' if f < m else 'grin', arms='chin' if f < m else 'shrug', look=1)
    if f >= m: paste_c(c, txt('SEM MUDANÇA!', 88, -6), 621, 720, back(ramp(f, m, m + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.03, 1.15, t) * (1 + .0006 * f)
    return c, (621, lerp(1350, 1300, t), z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
