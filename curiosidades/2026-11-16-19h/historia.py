"""Formato DESENHO: por que a nossa voz parece estranha na gravação (Curiosidades da IA, 16/11/2026, 19h).
Categoria: CORPO HUMANO.
Fatos: Popular Science ("Why Does My Voice Sound Different When I Hear It On A Recording?", com Ben Hornsby, audiologia,
Vanderbilt): quando falamos, as pregas vocais vibram e a vibração chega ao ouvido por dois caminhos: pelo ar e por dentro,
pelos ossos e tecidos da cabeça (condução óssea); a parte que vem pelos ossos tem frequência mais baixa (som mais grave);
o gravador/alto-falante só capta o som que vai pelo ar, por isso a gravação soa mais fina para nós; Wonderopolis e
Irish Examiner: a gravação é mais parecida com a voz que os outros escutam.
Cenários: s0 sala (Professor fala: não é a sua voz) | s1 sala (garganta vibra, 2 caminhos até o ouvido) |
s2 corpo (crânio: caminho pelo ar e pelos ossos) | s3 sala (voz grave e bonita na cabeça) |
s4 escritorio (celular grava, só o ar) | s5 escritorio ao entardecer (gravação = voz que todos escutam) |
s6 sala ao entardecer (Professor: quem nunca ouviu a própria voz é você)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h0810v', '2026-11-08-10h')
pessoa = _h10.pessoa
_h18 = _load('h0818v', '2026-11-08-18h')
celular = _h18.celular

LINES = [
    "A voz que você escuta quando fala não é a voz que os outros escutam.",
    "Quando você fala, a garganta vibra, e o som chega no seu ouvido por dois caminhos.",
    "Um vai pelo ar, por fora. O outro vai por dentro, pelos ossos da cabeça.",
    "E o caminho dos ossos deixa a voz mais grave, mais grossa, mais bonita.",
    "Mas o celular só grava o som que vai pelo ar.",
    "Você vê, aquela voz estranha da gravação é justamente a voz que todo mundo conhece.",
    "Ou seja: a única pessoa que nunca ouviu a sua voz de verdade... é você.",
]
CAPTXT = [
    "A voz que você escuta quando fala|não é a voz que os outros escutam.",
    "Quando você fala, a garganta vibra,|e o som chega no seu ouvido por dois caminhos.",
    "Um vai pelo ar, por fora.|O outro vai por dentro, pelos ossos da cabeça.",
    "E o caminho dos ossos deixa a voz|mais grave, mais grossa, mais bonita.",
    "Mas o celular só grava o som que vai pelo ar.",
    "Você vê, aquela voz estranha da gravação|é justamente a voz que todo mundo conhece.",
    "Ou seja: a única pessoa que nunca ouviu|a sua voz de verdade... é você.",
]
FALA_TIKTOK = "Você estranha a sua voz gravada? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 5
FLASH = []
CHECK = [(0, 'outros', 6), (1, 'vibra', 4), (1, 'caminhos', 6), (2, 'ar', 4), (2, 'ossos', 4), (3, 'grave', 4),
         (3, 'bonita', 6), (4, 'grava', 4), (4, 'ar', 6), (5, 'conhece', 6), (6, 'voce', 8)]

AZ = (90, 170, 255); LA = (255, 150, 60)


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def prof_pts(x, feet, h):
    """pontos do rosto do Professor no palco: boca, garganta, orelha direita."""
    s = h / 1000; top = feet + .025 * h - h
    P_ = lambda cx, cy: (x + (cx - 300) * s, top + cy * s)
    return P_(300, 330), P_(300, 405), P_(414, 272)


def onda(c, x0, y, w, amp, wl, f, cor, larg=10, fase=.25):
    d = ImageDraw.Draw(c)
    pts = [(x0 + i, y + amp * math.sin((i / wl - f * fase / 6) * 2 * math.pi)) for i in range(0, int(w), 6)]
    if len(pts) > 1:
        d.line(pts, fill=INK + (255,), width=larg + 8, joint='curve')
        d.line(pts, fill=tuple(cor) + (255,), width=larg, joint='curve')


def caminho(c, pts, f, f0, cor, t=1.0, dash=False):
    """linha que se desenha até a fração t, com bolinha andando."""
    if f < f0: return
    d = ImageDraw.Draw(c)
    k = clamp((f - f0) / 14) * t
    n = max(2, int(len(pts) * k))
    seg = pts[:n]
    if dash:
        for i in range(0, len(seg) - 1, 2):
            d.line(seg[i:i + 2], fill=INK + (255,), width=22)
            d.line(seg[i:i + 2], fill=cor + (255,), width=12)
    else:
        d.line(seg, fill=INK + (255,), width=26, joint='curve')
        d.line(seg, fill=cor + (255,), width=16, joint='curve')
    q = pts[int((f - f0) * 1.2) % len(pts)] if k >= 1 else seg[-1]
    r = 20
    d.ellipse((q[0] - r, q[1] - r, q[0] + r, q[1] + r), fill=(255, 255, 255, 255), outline=cor + (255,), width=7)


def bez(a, b, cc, n=40):
    return [((1 - t) ** 2 * a[0] + 2 * (1 - t) * t * cc[0] + t * t * b[0],
             (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * cc[1] + t * t * b[1]) for t in [i / (n - 1) for i in range(n)]]


@lru_cache(maxsize=2)
def cranio_img(w):
    """crânio de lado (olhando para a direita), card 600x700."""
    p = Pen(600, 700)
    bone = hexc('#f4ecd8'); boned = hexc('#d9ccb0')
    p.shape(ell_pts(270, 260, 220, 200), bone, boned, 6, 18)
    p.shape([(380, 300), (480, 330), (500, 420), (470, 470), (420, 480), (330, 470)], bone, boned, 6, 10)
    p.shape([(250, 420), (470, 470), (480, 540), (420, 580), (300, 560), (240, 470)], bone, boned, 6, 12)
    for x in range(330, 470, 26):
        p.stroke([(x, 470), (x + 4, 500)], 4)
    p.shape(ell_pts(400, 290, 50, 44), hexc('#4a3a4a'), None, 5, 0)
    p.shape([(470, 360), (500, 400), (470, 410)], hexc('#4a3a4a'), None, 4, 0)
    p.shape(ell_pts(190, 330, 36, 50), hexc('#f2a0a0'), hexc('#d07a7a'), 6, 6)   # orelha
    p.dot(190, 330, 12, hexc('#7a4a4a'))
    p.shape([(230, 560), (330, 560), (320, 690), (240, 690)], hexc('#f5c9a0'), hexc('#d9a77c'), 6, 8)  # pescoço
    p.shape(ell_pts(280, 610, 34, 22), hexc('#ff8a7a'), hexc('#d9665a'), 5, 4)  # garganta
    return p.img.resize((w, int(w * 700 / 600)), Image.LANCZOS)


@lru_cache(maxsize=4)
def rec_img(on=True, play=False):
    im = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if play:
        d.polygon([(100, 70), (100, 230), (230, 150)], fill=(60, 180, 90, 255), outline=INK + (255,))
    elif on:
        d.ellipse((90, 60, 210, 180), fill=(230, 50, 50, 255), outline=INK + (255,), width=6)
    t = txt('PLAY' if play else 'REC', 70)
    im.alpha_composite(t, (150 - t.size[0] // 2, 215 - t.size[1] // 2))
    return im


@lru_cache(maxsize=2)
def mesa_img(w):
    p = Pen(800, 300)
    p.shape([(0, 0), (800, 0), (800, 50), (0, 50)], hexc('#b07a4a'), hexc('#8a5a34'), 6, 8)
    p.shape([(40, 50), (90, 50), (90, 300), (40, 300)], hexc('#8a5a34'), None, 5, 0)
    p.shape([(710, 50), (760, 50), (760, 300), (710, 300)], hexc('#8a5a34'), None, 5, 0)
    return p.img.resize((w, int(w * 300 / 800)), Image.LANCZOS)


def SFX(s):
    s.ting(s.W(0, 'outros'), .3)
    s.thunk(s.W(1, 'vibra') - 2, 160, .6)
    s.thunk(s.W(1, 'caminhos') - 2, 220, .5); s.thunk(s.W(1, 'caminhos') + 4, 260, .5)
    s.whoosh(s.W(2, 'ar') - 6, .5, .4)
    s.thunk(s.W(2, 'ossos') - 2, 120, .8)
    s.thunk(s.W(3, 'grave') - 2, 90, .9); s.ting(s.W(3, 'bonita'), .3)
    s.ting(s.W(4, 'grava') - 2, .25)
    s.whoosh(s.W(5, 'estranha') - 6, .4, .4)
    s.thunk(s.W(5, 'conhece') - 2, 200, .6)
    s.thunk(s.W(6, 'voce') - 2, 140, .9); s.trill(s.W(6, 'voce') + 6, 1.0, .3)


def s0(f):
    c = CEN('sala', 'day').copy()
    k = wt(0, 'outros') - 3
    put_prof(c, 430, 1780, 950, f, expr='grin' if f < k else 'smug', arms='wave' if f < k else 'point', look=1)
    m, _, _ = prof_pts(430, 1780, 950)
    rings(c, m[0] + 60, m[1], f % 40, 0, 30, .8)
    if f >= k: paste_c(c, txt('NÃO É A MESMA!', 100, -5), 640, 620, back(ramp(f, k, k + 8)))
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('sala', 'day').copy()
    v = wt(1, 'vibra') - 3
    k = wt(1, 'caminhos') - 3
    X, FT, H = 520, 1800, 1000
    tremor = 4 * math.sin(f * 2.3) if v <= f < v + 30 else 0
    put_prof(c, X + tremor, FT, H, f, expr='grin', arms='hang', look=0)
    m, g, e = prof_pts(X, FT, H)
    if f >= v:
        rings(c, g[0], g[1], f, v, 40, .6)
    if f >= k:
        caminho(c, bez(m, e, (m[0] + 480, m[1] - 60)), f, k, AZ, dash=True)
        caminho(c, bez(g, e, (g[0] + 90, g[1] - 60)), f, k + 4, LA)
        paste_c(c, txt('2 CAMINHOS', 100, -4), 640, 600, back(ramp(f, k, k + 8)))
    t = smooth(ramp(f, 0, 80))
    z = lerp(1.1, 1.35, t) * (1 + .0009 * f)
    return c, (lerp(621, 640, t), lerp(1250, 1150, t), z, 0), 'day'


def s2(f):
    c = CEN('corpo', 'day').copy()
    a = wt(2, 'ar') - 3
    o = wt(2, 'ossos') - 3
    W_ = 760
    cx, cy = 560, 1150
    paste_c(c, cranio_img(W_), cx, cy, back(ramp(f, 0, 8)))
    sc = W_ / 600; ox, oy = cx - 300 * sc, cy - 350 * sc
    Q = lambda x, y: (ox + x * sc, oy + y * sc)
    boca, gar, ore = Q(490, 450), Q(280, 610), Q(190, 330)
    if f >= a:
        caminho(c, bez(boca, Q(620, 200), Q(660, 430), 14) + bez(Q(620, 200), Q(270, 0), Q(580, -10), 14) + bez(Q(270, 0), Q(40, 300), Q(40, 20), 14) + bez(Q(40, 300), ore, Q(90, 340), 8), f, a, AZ, dash=True)
        paste_c(c, txt('AR', 110, 6), 960, 600, back(ramp(f, a, a + 8)))
    if f >= o:
        caminho(c, bez(gar, ore, Q(300, 420)), f, o, LA)
        paste_c(c, txt('OSSOS', 110, -6), 450, 560, back(ramp(f, o, o + 8)))
    t = smooth(ramp(f, 0, 120))
    z = lerp(1.0, 1.12, t) * (1 + .0009 * f)
    return c, (621, 1120 + kick(f, o, .6) * 10, z, 0), 'day'


def s3(f):
    c = CEN('sala', 'day').copy()
    g = wt(3, 'grave') - 3
    gr = wt(3, 'grossa') - 3
    b = wt(3, 'bonita') - 3
    put_prof(c, 360, 1780, 920, f, expr='proud' if f >= b else 'grin', arms='up' if f >= b else 'chin', look=1)
    m, _, _ = prof_pts(360, 1780, 920)
    if f >= g:
        onda(c, m[0] + 70, m[1], 560, 70 if f >= gr else 45, 260, f, LA, 18 if f >= gr else 12)
    lab = 'GRAVE' if f < gr else ('GROSSA' if f < b else 'BONITA!')
    t0 = g if f < gr else (gr if f < b else b)
    if f >= g: paste_c(c, txt(lab, 120, -5), 760, 640, back(ramp(f, t0, t0 + 7)))
    z = lerp(1.25, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1250 + kick(f, b, .5) * 10, z, 0), 'day'


def s4(f):
    c = CEN('escritorio', 'day').copy()
    gv = wt(4, 'grava') - 3
    ar = wt(4, 'ar') - 3
    paste_c(c, mesa_img(620), 860, 1690)
    celular(c, 860, 1440, 400, f, rec_img(f >= gv and (f // 10) % 2 == 0 or f < gv), back(ramp(f, 0, 8)))
    put_prof(c, 330, 1800, 940, f, expr='grin', arms='point', look=1)
    m, _, _ = prof_pts(330, 1800, 940)
    if f >= gv:
        onda(c, m[0] + 60, m[1] + 10, 380, 22, 70, f, AZ, 8, .5)
    if f >= ar: paste_c(c, txt('SÓ O AR', 110, 5), 760, 700, back(ramp(f, ar, ar + 8)))
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (640, 1250 + kick(f, gv, .5) * 8, z, 0), 'day'


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    es = wt(5, 'estranha') - 3
    co = wt(5, 'conhece') - 3
    paste_c(c, mesa_img(620), 640, 1690)
    celular(c, 640, 1440, 380, f, rec_img(False, True))
    onda(c, 720, 1260, 160, 18, 50, f, AZ, 7, .5)
    put_prof(c, 300, 1800, 900, f, expr='pained' if f >= es else 'neutral', arms='chin' if f >= es else 'hang', look=1)
    put_p(c, 1000, 1800, 820, f, 7, shirt='#3fae6a', arms='point' if f >= co else 'hang', expr='grin', look=-1)
    if es <= f < co: paste_c(c, txt('ECA!', 120, -6), 330, 700, back(ramp(f, es, es + 7)))
    if f >= co: paste_c(c, txt('É ESSA MESMO!', 96, 5), 680, 700, back(ramp(f, co, co + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.15, 1.02, t) * (1 + .0009 * f)
    return c, (640, 1250 + kick(f, co, .6) * 10, z, lerp(0, 2, t)), 'dusk'


def s6(f):
    c = CEN('sala', 'dusk').copy()
    n = wt(6, 'nunca') - 3
    v = wt(6, 'voce') - 3
    put_prof(c, 560, 1780, 980, f, expr='shock' if f >= v else ('nervous' if f >= n else 'neutral'),
             arms='up' if f >= v else 'chin', look=0)
    if n <= f < v: paste_c(c, txt('NUNCA?', 100, 5), 700, 660, back(ramp(f, n, n + 8)))
    if f >= v: paste_c(c, txt('EU?!', 150, -6), 640, 640, back(ramp(f, v, v + 7)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.22, t) * (1 + .0009 * f)
    return c, (600, lerp(1250, 1180, t) + kick(f, v, .7) * 12, z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
