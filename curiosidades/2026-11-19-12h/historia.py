"""Formato DESENHO: por que as estrelas piscam (Curiosidades da IA, 19/11/2026, 12h).
Categoria: ESPAÇO.
Fatos: Britannica, "Why Do Stars Twinkle?" (ao atravessar as camadas da atmosfera da Terra, a turbulência entorta a luz
da estrela; os planetas em geral não piscam porque estão mais perto e aparecem como pequenos discos, que anulam a distorção);
Texas A&M Physics, "Why don't planets twinkle?" (o ar turbulento espalha a luz da estrela; planetas são fontes maiores
e a tremida se compensa); Space.com, "Why do stars twinkle?" ("no espaço, acima da atmosfera, as estrelas não piscam";
por isso o telescópio Hubble foi para a órbita).
Cenários: s0 montanha à noite (Professor olha o céu, estrela piscando) | s1 espaço (raio de luz reto viajando) |
s2 montanha à noite com faixas de ar quente/frio no céu (raio entortando) | s3 montanha à noite (estrela treme e muda de brilho) |
s4 montanha à noite (planeta-bolinha firme x estrela-pontinho piscando) | s5 estação espacial (Professor na janela, estrelas paradas) |
s6 montanha à noite (Professor: quem pisca é o céu da Terra)."""
from kit import *
from functools import lru_cache

LINES = [
    "As estrelas não piscam. Quem faz elas piscarem é o ar.",
    "A luz de uma estrela atravessa o espaço por anos, sem nenhum tremido.",
    "Mas no finalzinho da viagem, ela entra no ar da Terra, cheio de camadas quentes e frias se mexendo.",
    "Cada camada entorta a luz um pouquinho, e a estrela parece tremer e mudar de brilho.",
    "Você vê, os planetas quase não piscam: estão tão perto que parecem uma bolinha, e não um pontinho.",
    "E lá em cima, fora do ar, as estrelas não piscam nada.",
    "Ou seja: quem pisca não é a estrela... é o céu da Terra.",
]
CAPTXT = [
    "As estrelas não piscam.|Quem faz elas piscarem é o ar.",
    "A luz de uma estrela atravessa o espaço por anos,|sem nenhum tremido.",
    "Mas no finalzinho da viagem, ela entra no ar da Terra,|cheio de camadas quentes e frias se mexendo.",
    "Cada camada entorta a luz um pouquinho,|e a estrela parece tremer e mudar de brilho.",
    "Você vê, os planetas quase não piscam: estão tão perto|que parecem uma bolinha, e não um pontinho.",
    "E lá em cima, fora do ar, as estrelas não piscam nada.",
    "Ou seja: quem pisca não é a estrela... é o céu da Terra.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 4
FLASH = [5]
CHECK = [(0, 'piscam', 4), (0, 'ar', 6), (1, 'tremido', 6), (2, 'camadas', 6), (3, 'entorta', 4), (3, 'brilho', 6),
         (4, 'bolinha', 4), (4, 'pontinho', 4), (5, 'nada', 6), (6, 'terra', 8)]

STAR = (255, 236, 140)


def SFX(s):
    s.ting(s.W(0, 'piscam'), .3); s.whoosh(s.W(0, 'ar') - 6, .5, .4)
    s.whoosh(s.W(1, 'luz') - 4, .6, .5); s.ting(s.W(1, 'tremido'), .25)
    s.whoosh(s.W(2, 'terra') - 4, .5, .5); s.patter(s.W(2, 'camadas'), s.W(2, 'camadas') + 40, 10, .1)
    for i in range(5): s.ting(s.W(3, 'tremer') + i * 5, .12)
    s.thunk(s.W(4, 'bolinha') - 2, 220, .6); s.ting(s.W(4, 'pontinho'), .3)
    s.thunk(s.W(5, 'nada') - 2, 180, .5)
    s.trill(s.W(6, 'terra'), 1.0, .3)


@lru_cache(maxsize=4)
def noite_bg(seed=4):
    c = CEN('montanha', 'dusk').copy()
    ov = Image.new('RGBA', c.size, (10, 16, 60, 150)); c.alpha_composite(ov)
    d = ImageDraw.Draw(c); rnd = random.Random(seed)
    for _ in range(140):
        x, y, r = rnd.randint(0, 1242), rnd.randint(0, 1000), rnd.choice((2, 2, 3, 4))
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 230, 255))
    return c


@lru_cache(maxsize=64)
def estrela_img(size, rays=5):
    p = Pen(300, 300)
    pts = []
    for i in range(rays * 2):
        a = -math.pi / 2 + i * math.pi / rays
        r = 130 if i % 2 == 0 else 56
        pts.append((150 + r * math.cos(a), 155 + r * math.sin(a)))
    p.shape(pts, STAR, hexc('#e8b93a'), 6, 12)
    p.dot(125, 150, 9, INK); p.dot(175, 150, 9, INK)
    p.arc(150, 172, 16, 10, 20, 160, 4)
    s = max(4, int(size))
    return p.img.resize((s, s), Image.LANCZOS)


def brilho(c, x, y, r, a):
    if a <= 0 or r < 2: return
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(4):
        rr = r * (1 + k * .5)
        d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(255, 240, 170, int(110 * a / (k + 1))))
    c.alpha_composite(lay)


def star(c, x, y, size, f, twinkle=0.0, rot=0.0):
    tw = 1 + twinkle * (.35 * math.sin(f * 1.7) + .2 * math.sin(f * 3.1 + 1))
    sz = size * tw
    if sz < 8: return
    brilho(c, x, y, sz * .5, min(1, .5 + .5 * tw))
    im = estrela_img(int(round(sz / 8) * 8))
    if rot: im = im.rotate(rot, Image.BICUBIC)
    paste_c(c, im, x + twinkle * 10 * math.sin(f * 2.3), y + twinkle * 8 * math.cos(f * 1.9))


def raio(c, pts, w=16, col=(255, 240, 170)):
    d = ImageDraw.Draw(c)
    d.line(pts, fill=INK + (255,), width=w + 10, joint='curve')
    d.line(pts, fill=col + (255,), width=w, joint='curve')


def faixas(c, f, a=1.0, y0=520, n=5):
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(n):
        y = y0 + k * 110
        col = (255, 140, 90) if k % 2 == 0 else (110, 180, 255)
        pts = [(x, y + 22 * math.sin(x / 140 + f * .12 + k)) for x in range(-20, 1270, 30)]
        d.line(pts, fill=col + (int(150 * a),), width=46, joint='curve')
    c.alpha_composite(lay)


def planeta_img(size):
    p = Pen(300, 300)
    p.shape(ell_pts(150, 150, 120, 120, 40), hexc('#e8a25c'), hexc('#b8733a'), 6, 18)
    for y in (110, 170): p.arc(150, y, 110, 14, 10, 170, 6, hexc('#c98448'))
    return p.img.resize((int(size), int(size)), Image.LANCZOS)


def s0(f):
    c = noite_bg().copy()
    pi_ = wt(0, 'piscam') - 3
    a_ = wt(0, 'ar') - 3
    star(c, 920, 720, 220, f, 1.0 if f >= pi_ else .3)
    if f >= a_: faixas(c, f, .6 * ramp(f, a_, a_ + 10), 700, 3)
    put_prof(c, 380, 1880, 980, f, expr='shock' if f >= a_ else 'grin', arms='point' if f < a_ else 'up', look=1)
    if pi_ <= f < a_: paste_c(c, txt('PISCA?', 110, -5), 640, 450, back(ramp(f, pi_, pi_ + 8)))
    if f >= a_: paste_c(c, txt('É O AR!', 120, 5), 640, 450, back(ramp(f, a_, a_ + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1200 + kick(f, a_, .8) * 12, z, 0), 'day'


def s1(f):
    c = CEN('espaco', 'dusk').copy()
    t_ = wt(1, 'tremido') - 3
    star(c, 230, 420, 260, f, .0)
    L = ramp(f, 2, 60)
    if L > 0:
        raio(c, [(300, 500), (lerp(300, 1150, L), lerp(500, 1450, L))])
        paste_c(c, estrela_img(40), lerp(300, 1150, L), lerp(500, 1450, L))
    if f >= t_: paste_c(c, txt('RETINHA!', 110, -5), 760, 520, back(ramp(f, t_, t_ + 8)))
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (lerp(500, 700, smooth(ramp(f, 0, 70))), 1100, z, 0), 'dusk'


def s2(f):
    c = noite_bg().copy()
    k = wt(2, 'camadas') - 3
    e_ = wt(2, 'terra') - 6
    faixas(c, f, ramp(f, e_ - 4, e_ + 10), 520, 5)
    L = ramp(f, 0, e_)
    yA = lerp(-40, 480, L)
    pts = [(700, -40), (700, yA)]
    if f >= e_:
        L2 = ramp(f, e_, e_ + 40)
        n = int(1 + L2 * 5)
        for i in range(1, n + 1):
            pts.append((700 + (40 if i % 2 else -40) * math.sin(f * .4 + i), 480 + i * 110))
    raio(c, pts)
    if f >= k:
        paste_c(c, txt('QUENTE', 80, -4), 300, 560 + 0, back(ramp(f, k, k + 8)))
        paste_c(c, txt('FRIO', 80, 4), 1000, 670, back(ramp(f, k + 4, k + 12)))
    put_prof(c, 390, 1880, 720, f, expr='shock' if f >= k else 'neutral', arms='chin', look=1)
    z = lerp(1.1, 1.0, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (660, 1150, z, 0), 'day'


def s3(f):
    c = noite_bg().copy()
    en = wt(3, 'entorta') - 3
    tr = wt(3, 'tremer') - 3
    faixas(c, f, .7, 780, 3)
    tw = ramp(f, tr - 4, tr + 6)
    star(c, 760, 700, 260, f, tw * 1.2)
    if f >= en:
        pts = [(760, 820)] + [(760 + 40 * math.sin(f * .5 + i), 820 + i * 100) for i in range(1, 5)]
        raio(c, pts, 12)
    if en <= f < tr: paste_c(c, txt('ENTORTA!', 100, -5), 700, 460, back(ramp(f, en, en + 8)))
    if f >= tr: paste_c(c, txt('TREME!', 120, 5), 700, 460, back(ramp(f, tr, tr + 8)))
    put_prof(c, 330, 1880, 760, f, expr='grin' if f >= tr else 'neutral', arms='point', look=1)
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (660, 1050, z, 2 * math.sin(f * .05)), 'dusk'


def s4(f):
    c = noite_bg().copy()
    b_ = wt(4, 'bolinha') - 3
    p_ = wt(4, 'pontinho') - 3
    faixas(c, f, .5, 820, 3)
    if f >= b_ - 4:
        s = back(ramp(f, b_ - 4, b_ + 6))
        if s > .05: paste_c(c, planeta_img(max(8, int(300 * s))), 360, 560)
        if f >= b_: paste_c(c, txt('FIRME', 90, -5), 360, 400, back(ramp(f, b_, b_ + 8)))
    star(c, 900, 560, 170, f, 1.2 if f >= p_ else .6)
    if f >= p_: paste_c(c, txt('PISCA!', 90, 5), 900, 400, back(ramp(f, p_, p_ + 8)))
    put_prof(c, 620, 1880, 820, f, expr='proud' if f >= b_ else 'neutral', arms='point' if f < p_ else 'shrug', look=-1 if f < p_ else 1)
    z = lerp(1.15, 1.05, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (640, 1100, z, 0), 'dusk'


@lru_cache(maxsize=1)
def janela_bg():
    c = CEN('estacao', 'dusk').copy()
    d = ImageDraw.Draw(c)
    cx, cy, R = 640, 760, 420
    d.ellipse((cx - R - 40, cy - R - 40, cx + R + 40, cy + R + 40), fill=(150, 156, 168, 255), outline=INK + (255,), width=12)
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=(12, 16, 48, 255), outline=INK + (255,), width=10)
    rnd = random.Random(2)
    for _ in range(70):
        a = rnd.random() * 6.283; r = rnd.random() ** .5 * (R - 30)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a); rr = rnd.choice((2, 3, 4))
        d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(255, 255, 230, 255))
    return c


def s5(f):
    c = janela_bg().copy()
    n_ = wt(5, 'nada') - 3
    for x, y, s in ((520, 640, 120), (780, 820, 90), (640, 980, 70)):
        star(c, x, y, s, f, 0)
    put_prof(c, 400, 1950, 900, f, expr='proud' if f >= n_ else 'shock', arms='point', look=1)
    if f >= n_: paste_c(c, txt('NADA!', 120, -5), 900, 1350, back(ramp(f, n_, n_ + 8)))
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 50))) * (1 + .0009 * f)
    return c, (640, 1150, z, 0), 'dusk'


def s6(f):
    c = noite_bg().copy()
    q = wt(6, 'quem') - 3
    t_ = wt(6, 'terra') - 3
    faixas(c, f, .6, 760, 3)
    star(c, 900, 760, 220, f, 1.0)
    put_prof(c, 380, 1880, 980, f, expr='smug' if f < t_ else 'grin', arms='chin' if f < t_ else 'shrug', look=1)
    if f >= t_: paste_c(c, txt('CULPA DO AR!', 100, 5), 660, 580, back(ramp(f, t_, t_ + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (640, lerp(1220, 1180, t) + kick(f, t_, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
