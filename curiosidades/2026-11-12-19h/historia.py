"""Formato DESENHO: o ketchup já foi vendido como remédio (Curiosidades da IA, 12/11/2026, 19h). Categoria: INVENÇÕES E OBJETOS.
Fatos: Popular Science, "Ketchup was once a diarrhea cure": o ketchup original vem de um molho de peixe fermentado da
Ásia, sem tomate; nos anos 1830 um médico de Ohio (EUA) dizia que o tomate tratava diarreia e indigestão; em 1835 surgiram
as 'pílulas de tomate', vendidas como extrato de tomate em farmácias e mercearias; investigações acharam pílulas sem
tomate nenhum; em 1869 médicos da associação médica americana contestaram o valor medicinal. Tasting Table, "The Fascinating
Medicinal Origins Of Ketchup": em 1834 o médico vendia ketchup como cura de diarreia e indigestão, depois em pílula;
outras empresas copiaram; por volta de 1850 algumas vendiam laxante com rótulo de pílula de tomate."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10d', '2026-11-08-10h')
pessoa = _h10.pessoa

LINES = [
    "O ketchup já foi vendido como remédio.",
    "E o primeiro ketchup nem tinha tomate: era um molho de peixe que veio da Ásia.",
    "Nos anos mil oitocentos e trinta, nos Estados Unidos, um médico começou a dizer que o tomate curava diarreia e má digestão.",
    "Logo, as farmácias estavam vendendo pílula de extrato de tomate.",
    "Você vê, virou moda. E apareceu tanta pílula copiada que algumas nem tinham tomate: eram só laxante.",
    "Com o tempo, os médicos derrubaram a ideia, e o ketchup voltou pra cozinha.",
    "Ou seja: o ketchup não curava nada... mas pelo menos combina com batata frita.",
]
CAPTXT = [
    "O ketchup já foi vendido como remédio.",
    "E o primeiro ketchup nem tinha tomate:|era um molho de peixe que veio da Ásia.",
    "Nos anos 1830, nos Estados Unidos, um médico começou a dizer|que o tomate curava diarreia e má digestão.",
    "Logo, as farmácias estavam vendendo|pílula de extrato de tomate.",
    "Você vê, virou moda. E apareceu tanta pílula copiada|que algumas nem tinham tomate: eram só laxante.",
    "Com o tempo, os médicos derrubaram a ideia,|e o ketchup voltou pra cozinha.",
    "Ou seja: o ketchup não curava nada...|mas pelo menos combina com batata frita.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [2, 5]
CHECK = [(0, 'ketchup', 4), (0, 'remedio', 6), (1, 'tomate', 4), (1, 'peixe', 4), (1, 'asia', 6), (2, 'medico', 4), (2, 'tomate', 4),
         (2, 'digestao', 6), (3, 'farmacias', 4), (3, 'pilula', 4), (4, 'moda', 4), (4, 'copiada', 4), (4, 'laxante', 6),
         (5, 'derrubaram', 4), (5, 'cozinha', 6), (6, 'nada', 4), (6, 'batata', 6)]

VERM, VERM_D = hexc('#e3262b'), hexc('#a8191d')


# ------------------------------------------------------------------ objetos novos
def tomate(expr='calm', blink=0, look=0.0):
    """tomate com carinha (400x400)."""
    p = Pen(400, 400)
    p.shape(ell_pts(200, 220, 170, 150, 56, 0, .06), VERM, VERM_D, 6, 20)
    for a in range(5):
        an = a * 2 * math.pi / 5 - math.pi / 2
        p.shape([(200, 80), (200 + 70 * math.cos(an - .3), 80 + 40 * math.sin(an - .3) + 20), (200 + 95 * math.cos(an), 80 + 50 * math.sin(an) + 18),
                 (200 + 70 * math.cos(an + .3), 80 + 40 * math.sin(an + .3) + 20)], hexc('#4caf50'), hexc('#2e7d32'), 4, 2)
    p.line([(200, 80), (205, 30)], hexc('#2e7d32'), 12, 4)
    for s in (-1, 1):
        x, y = 200 + s * 55, 210
        if blink > .6: p.stroke([(x - 16, y), (x + 16, y)], 6)
        elif expr == 'shock': p.dot(x, y, 26, (255, 255, 255), 4); p.dot(x + look * 6, y, 9, INK)
        elif expr == 'smug': p.dot(x, y, 22, (255, 255, 255), 4); p.dot(x + 6, y + 3, 9, INK); p.stroke([(x - 22, y - 8), (x + 22, y - 8)], 6)
        else: p.dot(x, y, 22, (255, 255, 255), 4); p.dot(x + look * 6, y, 9, INK)
    if expr == 'shock': p.dot(200, 290, 22, hexc('#7a2e2e'), 4)
    elif expr in ('proud', 'smug'): p.arc(205, 275, 40, 22, 20, 160, 7)
    else: p.arc(200, 278, 30, 16, 20, 160, 6)
    return p.img


def put_tomate(c, x, y, h, f, seed=1, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    paste_c(c, sprite('tomate', tuple(sorted(kw.items())), int(h), 1.0, False), x, y + 4 * math.sin((f + seed * 9) * .12))


@lru_cache(maxsize=4)
def frasco(w=260, tom=True, rot='TOMATE'):
    """caixinha/frasco de pílulas (rótulo)."""
    p = Pen(300, 400)
    p.shape([(60, 90), (240, 90), (250, 380), (50, 380)], hexc('#8a5a2b'), hexc('#5e3c1c'), 6, 12)
    p.shape([(70, 40), (230, 40), (232, 95), (68, 95)], hexc('#f2efe6'), hexc('#cfc9b8'), 5, 4)
    p.shape([(62, 170), (238, 170), (242, 320), (58, 320)], hexc('#f7ecd0'), hexc('#d9c6a2'), 4, 4)
    if tom: p.shape(ell_pts(150, 245, 46, 42, 32), VERM, VERM_D, 4, 6)
    else: p.stroke([(110, 205), (190, 285)], 10, VERM); p.stroke([(190, 205), (110, 285)], 10, VERM)
    im = p.img.resize((300, 400), Image.LANCZOS)
    return im.resize((w, int(w * 4 / 3)), Image.LANCZOS)


@lru_cache(maxsize=8)
def pilula(r=36):
    p = Pen(4 * r, 2 * r + 10)
    p.shape(ell_pts(2 * r, r + 5, 2 * r - 6, r - 4, 32), VERM, VERM_D, 4, 4)
    p.poly([(2 * r, 6), (4 * r - 8, 6), (4 * r - 8, 2 * r + 4), (2 * r, 2 * r + 4)], hexc('#f2efe6'), 0)
    p.stroke([(2 * r, 6), (2 * r, 2 * r + 4)], 4)
    return p.img.resize((4 * r, 2 * r + 10), Image.LANCZOS)


def peixe(expr='calm', blink=0, look=0.0):
    """peixe de lado, olhando p/ direita (500x300)."""
    p = Pen(500, 300)
    p.shape([(40, 60), (130, 150), (40, 240)], hexc('#4fa3e0'), hexc('#2f78b0'), 5, 4)
    p.shape(ell_pts(280, 150, 180, 105, 48), hexc('#7cc4f2'), hexc('#4fa3e0'), 6, 16)
    p.arc(250, 150, 50, 70, -60, 60, 5)
    x, y = 380, 125
    if blink > .6: p.stroke([(x - 16, y), (x + 16, y)], 6)
    else:
        p.dot(x, y, 30 if expr == 'shock' else 26, (255, 255, 255), 4); p.dot(x + 6 + look * 4, y, 10, INK)
    p.arc(440, 175, 18, 10, 120, 240, 6) if expr != 'shock' else p.dot(448, 178, 12, hexc('#7a2e2e'), 3)
    return p.img


@lru_cache(maxsize=2)
def garrafa_peixe(h=420):
    p = Pen(260, 520)
    p.shape([(100, 20), (160, 20), (165, 140), (215, 200), (220, 500), (40, 500), (45, 200), (95, 140)], hexc('#b87a2e'), hexc('#8a5a1e'), 6, 12)
    p.shape([(45, 290), (215, 290), (217, 420), (43, 420)], hexc('#f7ecd0'), hexc('#d9c6a2'), 4, 4)
    p.shape([(80, 330), (150, 355), (80, 380)], hexc('#4fa3e0'), None, 3)
    p.shape(ell_pts(160, 355, 40, 24, 24), hexc('#4fa3e0'), None, 3)
    im = p.img.resize((260, 520), Image.LANCZOS)
    return im.resize((int(h / 2), h), Image.LANCZOS)


@lru_cache(maxsize=2)
def ketchup_img(h=500):
    p = Pen(260, 560)
    p.shape([(105, 20), (155, 20), (160, 120), (220, 210), (225, 540), (35, 540), (40, 210), (100, 120)], VERM, VERM_D, 6, 14)
    p.shape([(95, 10), (165, 10), (165, 60), (95, 60)], hexc('#f2efe6'), hexc('#cfc9b8'), 4, 4)
    p.shape([(40, 300), (220, 300), (222, 440), (38, 440)], hexc('#f7ecd0'), hexc('#d9c6a2'), 4, 4)
    p.shape(ell_pts(130, 370, 40, 36, 28), VERM, VERM_D, 3, 4)
    im = p.img.resize((260, 560), Image.LANCZOS)
    return im.resize((int(h * 26 / 56), h), Image.LANCZOS)


@lru_cache(maxsize=2)
def batata_img(h=420):
    p = Pen(340, 440)
    for i in range(7):
        x = 70 + i * 32
        p.shape([(x, 60 + (i % 3) * 30), (x + 26, 60 + (i % 3) * 30), (x + 30, 260), (x - 2, 260)], hexc('#ffd54a'), hexc('#e0a800'), 4, 4)
    p.shape([(40, 200), (300, 200), (260, 430), (80, 430)], VERM, VERM_D, 6, 10)
    p.shape(ell_pts(170, 315, 50, 50, 28), hexc('#ffffff'), None, 4)
    im = p.img.resize((340, 440), Image.LANCZOS)
    return im.resize((int(h * 34 / 44), h), Image.LANCZOS)


@lru_cache(maxsize=4)
def farmacia(luz='day'):
    """farmácia antiga do século 19: prateleiras de madeira com frascos e balcão."""
    W, H = BW, BH
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc('#e9dcc0'))
    for x in range(0, W, 90): p.stroke([(x, 0), (x, 1520)], 3, hexc('#ddcba8'))
    p.shape([(60, 200), (1182, 200), (1182, 1300), (60, 1300)], hexc('#8a5f35'), hexc('#6b4a2a'), 6, 14)
    cores = ['#4fa3e0', '#7cc46f', '#e8b34a', '#c56fd0', '#e3262b', '#f2efe6']
    rnd = random.Random(2)
    for row, y in enumerate((460, 760, 1060)):
        p.shape([(80, y), (1162, y), (1162, y + 30), (80, y + 30)], hexc('#b07a45'), hexc('#8a5f35'), 4, 4)
        x = 120
        while x < 1120:
            w = rnd.randint(50, 80); hh = rnd.randint(110, 190)
            col = hexc(cores[rnd.randrange(len(cores))])
            p.shape([(x, y - hh), (x + w, y - hh), (x + w, y), (x, y)], col, mul(col, .78), 4, 6)
            p.shape([(x + 10, y - hh - 24), (x + w - 10, y - hh - 24), (x + w - 10, y - hh), (x + 10, y - hh)], hexc('#5e3c1c'), None, 3)
            p.shape([(x + 6, y - hh * .6), (x + w - 6, y - hh * .6), (x + w - 6, y - hh * .3), (x + 6, y - hh * .3)], hexc('#f7ecd0'), None, 2)
            x += w + rnd.randint(18, 40)
    p.shape([(0, 1520), (W, 1520), (W, H), (0, H)], hexc('#b48a5a'), hexc('#9a7347'), 0, 0)
    for y in range(1560, H, 90): p.stroke([(0, y), (W, y)], 3, hexc('#9a7347'))
    im = p.img.resize((W, H), Image.LANCZOS)
    return im


def balcao(c, y=1640):
    d = ImageDraw.Draw(c)
    d.rectangle((0, y, BW, y + 70), fill=hexc('#6b4a2a') + (255,), outline=INK + (255,), width=6)
    d.rectangle((20, y + 70, BW - 20, y + 600), fill=hexc('#8a5f35') + (255,), outline=INK + (255,), width=6)


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


MED = dict(shirt='#f2efe6', vest='#3b3b5a', pants='#2b2b3a', mous=True, hair='#6b5a4a')


def SFX(s):
    s.ting(s.W(0, 'ketchup'), .3); s.thunk(s.W(0, 'remedio') - 2, 160, .8)
    s.thunk(s.W(1, 'tomate') - 2, 220, .5); s.splash(s.W(1, 'peixe') - 3, .4)
    s.whoosh(s.W(2, 'medico') - 6, .4, .4); s.ting(s.W(2, 'tomate'), .3)
    s.thunk(s.W(3, 'farmacias') - 2, 200, .5)
    for i in range(4): s.thunk(s.W(3, 'pilula') - 2 + i * 4, 320, .3)
    s.ting(s.W(4, 'moda'), .3)
    for i in range(5): s.thunk(s.W(4, 'copiada') - 2 + i * 3, 280, .3)
    s.thunk(s.W(4, 'laxante') - 2, 120, .9)
    s.thunk(s.W(5, 'derrubaram') - 2, 140, .8); s.whoosh(s.W(5, 'cozinha') - 6, .5, .4)
    s.trill(s.W(6, 'batata'), .9, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    """farmácia antiga: frasco de ketchup no balcão com placa de REMÉDIO."""
    c = farmacia('day').copy()
    balcao(c)
    k0 = wt(0, 'ketchup') - 3
    r0 = wt(0, 'remedio') - 3
    put_pessoa(c, 330, 1700, 1100, f, 1, expr='proud' if f >= r0 else 'grin', arms='point', look=1, **MED)
    paste_c(c, ketchup_img(480), 800, 1400, back(ramp(f, k0, k0 + 8)))
    if f >= r0: paste_c(c, txt('REMÉDIO!', 110, -6), 820, 1020, back(ramp(f, r0, r0 + 8)))
    kk = kick(f, r0 + 2)
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.35, 1.1, t) * (1 + .0009 * f)
    return c, (620, 1250 + kk * 10, z, kk), 'day'


def s1(f):
    """mapa: o molho de peixe vindo da Ásia."""
    c = CEN('mapa', 'day').copy()
    t0 = wt(1, 'tomate') - 3
    p0 = wt(1, 'peixe') - 3
    a0 = wt(1, 'asia') - 3
    if f >= t0:
        paste_c(c, frasco(220, tom=False), 330, 900, back(ramp(f, t0, t0 + 8)))
        paste_c(c, txt('SEM TOMATE!', 90, -6), 640, 560, back(ramp(f, t0, t0 + 8)))
    if f >= p0:
        paste_c(c, garrafa_peixe(460), 820, 1100, back(ramp(f, p0, p0 + 8)))
        sw = 20 * math.sin(f * .3)
        im = sprite('peixe', (('blink', 1 if blinkAt(f, 3) > .6 else 0), ('expr', 'calm')), 220, 500 / 300, False)
        paste_c(c, im, 560 + sw, 1300, back(ramp(f, p0, p0 + 8)))
    if f >= a0: paste_c(c, txt('ÁSIA', 100, 6), 900, 1500, back(ramp(f, a0, a0 + 8)))
    z = lerp(1.1, 1.22, smooth(f / 120)) * (1 + .0009 * f)
    return c, (640, 1100, z, 0), 'day'


def s2(f):
    """farmácia (anos 1830): o médico apresenta o tomate."""
    c = farmacia('day').copy()
    m0 = wt(2, 'medico') - 3
    t0 = wt(2, 'tomate') - 3
    d0 = wt(2, 'digestao') - 3
    put_pessoa(c, 430, 2080, 1450, f, 2, expr='proud' if f >= t0 else 'neutral', arms='up' if f >= t0 else 'hang', look=1, **MED)
    paste_c(c, txt('1830', 110, -6), 380, 580, back(ramp(f, 4, 12)))
    if f >= t0: put_tomate(c, 880, 1000, 360 * back(ramp(f, t0, t0 + 8)), f, 2, expr='proud')
    if f >= d0: paste_c(c, txt('CURA!', 100, 6), 840, 640, back(ramp(f, d0, d0 + 8)))
    z = lerp(1.12, 1.25, smooth(f / 150)) * (1 + .0009 * f)
    return c, (640, 1150, z, 0), 'day'


def s3(f):
    """farmácia: balcão cheio de frascos de pílula de tomate."""
    c = farmacia('day').copy()
    balcao(c)
    f0 = wt(3, 'farmacias') - 3
    p0 = wt(3, 'pilula') - 3
    put_pessoa(c, 950, 1700, 1050, f, 3, expr='grin', arms='point' if f >= p0 else 'hang', look=-1, dress='#5fa8d8', bun=True, shirt='#5fa8d8', hair='#3b2a1e')
    for i, x in enumerate((180, 380, 580)):
        paste_c(c, frasco(220), x, 1500, back(ramp(f, f0 + i * 4, f0 + i * 4 + 8)))
    if f >= p0:
        for i in range(5):
            a = clamp((f - p0 - i * 4) / 14)
            if a > 0: paste_c(c, pilula(46), 240 + i * 120, lerp(1300, 1180 - (i % 2) * 60, easeOut(a)))
        paste_c(c, txt('PÍLULA DE TOMATE', 74, -4), 600, 640, back(ramp(f, p0, p0 + 8)))
    z = lerp(1.2, 1.08, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (620, 1250, z, 0), 'day'


def s4(f):
    """farmácia (dusk): pílulas copiadas, uma sem tomate: laxante."""
    c = farmacia('dusk').copy()
    balcao(c)
    m0 = wt(4, 'moda') - 3
    c0 = wt(4, 'copiada') - 3
    l0 = wt(4, 'laxante') - 3
    put_pessoa(c, 330, 1700, 1100, f, 4, expr='shock' if f >= l0 else 'nervous', arms='cheek' if f >= l0 else 'hang', look=1, **MED)
    if f >= m0: paste_c(c, txt('MODA!', 100, -6), 420, 580, back(ramp(f, m0, m0 + 8)))
    for i in range(6):
        x = 560 + (i % 3) * 200; y = 1480 - (i // 3) * 300
        s = back(ramp(f, c0 + i * 3, c0 + i * 3 + 8))
        if s > .05: paste_c(c, frasco(150, tom=not (i == 4 and f >= l0)), x, y, s)
    if f >= l0: paste_c(c, txt('SÓ LAXANTE!', 86, 6), 720, 780, back(ramp(f, l0, l0 + 8)))
    kk = kick(f, l0 + 2)
    z = lerp(1.05, 1.18, smooth(f / 150)) * (1 + .0009 * f)
    return c, (640, 1200 + kk * 10, z, kk), 'dusk'


def s5(f):
    """cozinha (golden): o ketchup volta pra cozinha."""
    c = CEN('cozinha', 'golden').copy()
    d0 = wt(5, 'derrubaram') - 3
    k0 = wt(5, 'cozinha') - 3
    if f < k0:
        paste_c(c, frasco(300), 640, 1250)
        if f >= d0: paste_c(c, txt('NÃO CURA!', 100, -6), 640, 800, back(ramp(f, d0, d0 + 8)))
    else:
        a = back(ramp(f, k0, k0 + 10))
        paste_c(c, ketchup_img(520), lerp(1300, 640, clamp(a)), 1300)
        paste_c(c, txt('DE VOLTA!', 100, 6), 640, 800, a)
    z = lerp(1.08, 1.2, smooth(f / 120)) * (1 + .0009 * f)
    return c, (640, 1150, z, 0), 'golden'


def s6(f):
    """cozinha (dusk): batata frita com ketchup."""
    c = CEN('cozinha', 'dusk').copy()
    n0 = wt(6, 'nada') - 3
    b0 = wt(6, 'batata') - 3
    put_pessoa(c, 400, 2080, 1450, f, 5, expr='smug' if f >= b0 else 'neutral', arms='shrug' if f < b0 else 'point', look=1)
    paste_c(c, ketchup_img(420), 960, 1450)
    if f >= n0 and f < b0: paste_c(c, txt('NADA...', 90, -6), 700, 660, back(ramp(f, n0, n0 + 8)))
    if f >= b0:
        paste_c(c, batata_img(380), 820, 1150, back(ramp(f, b0, b0 + 8)))
        paste_c(c, txt('HUMM!', 100, 6), 700, 660, back(ramp(f, b0, b0 + 8)))
    z = lerp(1.05, 1.28, easeOut(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (640, 1200, z, lerp(0, -3, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
