"""Formato DESENHO: a Islândia não tinha mosquito (Curiosidades da IA, 08/11/2026, 16h). Categoria: LUGARES E GEOGRAFIA.
Fatos: AP via KAXE (22/10/2025) "Iceland reports the presence of mosquitoes for the first time as climate warms": um entusiasta
de insetos viu uma 'mosca estranha' numa fita com vinho tinto (usada para atrair mariposas) numa fazenda em Kjós, ao norte
de Reykjavík, em 16 de outubro de 2025; pegou mais dois; o Instituto de Ciências Naturais da Islândia confirmou: três
Culiseta annulata (2 fêmeas e 1 macho), espécie que aguenta o frio; devem ter chegado em cargas; a Antártida é o único lugar
que se acredita não ter mosquitos; o Ártico esquenta mais de duas vezes mais rápido que a média.
Earth.com (30/10/2025): verão curto e fresco; poças congelam e descongelam e isso mata as larvas (uma das explicações).
Britannica: a Islândia fica logo ao sul do Círculo Polar Ártico."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10b', '2026-11-08-10h')
pessoa = _h10.pessoa

LINES = [
    "A Islândia era um dos poucos lugares do mundo onde não existia mosquito.",
    "O país fica lá no norte, quase no Círculo Polar Ártico, e o verão de lá é curto e fresquinho.",
    "Uma das explicações: o frio vai e volta, congela as poças, e as larvas do mosquito não conseguem crescer.",
    "Até que, em outubro de dois mil e vinte e cinco, um fã de insetos viu uma mosca esquisita numa fita com vinho, numa fazenda.",
    "Era um mosquito! Depois ele pegou mais dois, e os cientistas confirmaram.",
    "Você vê, eles devem ter chegado de carona em alguma carga, e o clima mais quente ajuda eles a aguentar por lá.",
    "Ou seja: agora, pelo que se sabe, o único lugar do mundo sem mosquito... é a Antártida.",
]
CAPTXT = [
    "A Islândia era um dos poucos lugares do mundo|onde não existia mosquito.",
    "O país fica lá no norte, quase no Círculo Polar Ártico,|e o verão de lá é curto e fresquinho.",
    "Uma das explicações: o frio vai e volta, congela as poças,|e as larvas do mosquito não conseguem crescer.",
    "Até que, em outubro de 2025, um fã de insetos viu uma mosca esquisita|numa fita com vinho, numa fazenda.",
    "Era um mosquito! Depois ele pegou mais dois,|e os cientistas confirmaram.",
    "Você vê, eles devem ter chegado de carona em alguma carga,|e o clima mais quente ajuda eles a aguentar por lá.",
    "Ou seja: agora, pelo que se sabe,|o único lugar do mundo sem mosquito... é a Antártida.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [3]
CHECK = [(0, 'islandia', 4), (0, 'mosquito', 6), (1, 'artico', 4), (1, 'fresquinho', 6), (2, 'pocas', 4), (2, 'crescer', 6),
         (3, 'mosca', 4), (3, 'vinho', 6), (4, 'mosquito', 4), (4, 'dois', 6), (5, 'carga', 4), (5, 'quente', 6),
         (6, 'mosquito', 4), (6, 'antartida', 8)]

MOSQ, MOSQD = hexc('#7a6a5c'), hexc('#54483e')


# ------------------------------------------------------------------ personagens e objetos novos
def mosquito(expr='calm', blink=0, look=0.4, wing=0.0):
    """mosquito de lado olhando para a direita (600x500). wing 0..1 bate as asas."""
    p = Pen(600, 500)
    # pernas compridas
    for i, x in enumerate((230, 290, 350)):
        p.stroke([(x, 300), (x - 60 + i * 20, 380), (x - 90 + i * 40, 490)], 6)
    # asas
    a = -0.5 + wing * 0.9
    for k, dx in ((0, 0), (1, 40)):
        pts = ell_pts(260 + dx + 110 * math.cos(a - 1.2), 220 - 110 * math.sin(a + .3) * .6, 130, 50, 40, a - .3)
        p.shape(pts, hexc('#e3f2fb'), None, 4)
    # abdômen listrado
    p.shape(ell_pts(170, 290, 130, 50, 48, .25), MOSQ, MOSQD, 5, 10)
    for x in (110, 160, 210): p.stroke([(x, 255 + (x - 110) * .2), (x - 14, 330 + (x - 110) * .2)], 6, hexc('#e8e0d2'))
    # tórax
    p.shape(ell_pts(320, 270, 70, 60, 40), MOSQ, MOSQD, 5, 10)
    # cabeça
    p.shape(ell_pts(420, 250, 62, 58, 40), MOSQ, MOSQD, 5, 10)
    # ferrão / probóscide
    p.stroke([(470, 270), (590, 320)], 7)
    # antenas
    p.stroke([(430, 200), (470, 120), (500, 100)], 5); p.stroke([(410, 200), (420, 110), (440, 90)], 5)
    ex, ey = 425, 240
    if blink: p.stroke([(ex - 22, ey), (ex + 22, ey)], 6)
    else:
        r = 34 if expr == 'shock' else 28
        p.dot(ex, ey, r, (255, 255, 255), 5)
        p.dot(ex + look * 10, ey + 2, 12, INK); p.dot(ex + look * 10 - 4, ey - 3, 4, (255, 255, 255))
        if expr in ('smug', 'side'):
            p.poly([(ex - r - 4, ey - r - 4), (ex + r + 4, ey - r - 4), (ex + r + 4, ey - 4), (ex - r - 4, ey - 4)], MOSQ); p.stroke([(ex - r, ey - 4), (ex + r, ey - 4)], 6)
    return p.img


def put_mosq(c, x, y, h, f, seed=1, flip=False, **kw):
    """y = centro. Bate as asas sozinho."""
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    kw['wing'] = (f + seed) % 3 / 2
    im = sprite('mosquito', tuple(sorted(kw.items())), int(h), 600 / 500, flip)
    paste_c(c, im, x + 6 * math.sin((f + seed * 5) * .2), y + 10 * math.sin((f + seed * 3) * .17))


def larva(expr='calm', blink=0, cold=0):
    """larvinha de mosquito com carinha (300x300)."""
    p = Pen(300, 300)
    col = hexc('#c9b79a') if not cold else hexc('#a9c8e0')
    pts = [(60 + i * 30, 200 + 25 * math.sin(i * .9)) for i in range(7)]
    for i, (x, y) in enumerate(pts):
        p.shape(ell_pts(x, y, 34 - i * 2, 30 - i * 2, 28), col, mul(col, .8), 4, 6)
    hx, hy = 60, 190
    p.shape(ell_pts(hx, hy - 10, 48, 44, 32), col, mul(col, .8), 5, 8)
    for dx in (-16, 16):
        if blink: p.stroke([(hx + dx - 9, hy - 14), (hx + dx + 9, hy - 14)], 5)
        else: p.dot(hx + dx, hy - 14, 12, (255, 255, 255), 4); p.dot(hx + dx, hy - 12, 5, INK)
    if expr == 'sad' or cold: p.arc(hx, hy + 16, 14, 7, 200, 340, 5)
    else: p.arc(hx, hy + 6, 14, 7, 20, 160, 5)
    if cold:
        for i in range(3): p.stroke([(hx - 50 - i * 8, hy - 50 + i * 20), (hx - 64 - i * 8, hy - 40 + i * 20)], 4, hexc('#7fb4e0'))
    return p.img


def put_larva(c, x, y, h, f, seed=1, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('larva', tuple(sorted(kw.items())), int(h), 1.0, False)
    shake = 4 * math.sin(f * 1.7 + seed) if kw.get('cold') else 0
    paste_c(c, im, x + shake, y + 8 * math.sin((f + seed * 7) * .12))


def pinguim(blink=0, look=0.3, expr='calm', wave=0):
    """pinguim genérico de frente (400x560)."""
    p = Pen(400, 560)
    for s in (-1, 1): p.shape(ell_pts(200 + s * 50, 540, 50, 18, 24), hexc('#f2a23a'), hexc('#c97d1e'), 4, 4)
    p.shape(ell_pts(200, 330, 140, 210, 56, 0, .1), hexc('#2b2d3a'), hexc('#1b1c26'), 6, 16)
    p.shape(ell_pts(200, 370, 100, 160, 48), BRANCO if False else hexc('#f6f4ee'), hexc('#d9d6cc'), 0, 10)
    p.shape([(70, 260), (20, 380 if not wave else 180), (80, 400)], hexc('#2b2d3a'), None, 5)
    p.shape([(330, 260), (380, 380), (320, 400)], hexc('#2b2d3a'), None, 5)
    for dx in (-36, 36):
        if blink: p.stroke([(200 + dx - 14, 200), (200 + dx + 14, 200)], 5)
        else: p.dot(200 + dx, 200, 22, (255, 255, 255), 4); p.dot(200 + dx + look * 8, 202, 9, INK)
    p.shape([(170, 235), (230, 235), (200, 275)], hexc('#f2a23a'), hexc('#c97d1e'), 4, 4)
    if expr == 'smug': p.arc(200, 290, 20, 10, 20, 160, 5)
    return p.img


def put_ping(c, x, feet, h, f, seed=1, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('pinguim', tuple(sorted(kw.items())), int(h), 400 / 560, False)
    put(c, im, x, feet + 4 * math.sin((f + seed * 5) * .15))


@lru_cache(maxsize=4)
def navio_img(w=520):
    p = Pen(600, 340)
    p.shape([(20, 200), (580, 200), (520, 320), (80, 320)], hexc('#c0392b'), hexc('#8e2a20'), 6, 10)
    for i, col in enumerate(('#2f7fd1', '#f2a23a', '#3aa76d', '#2f7fd1', '#f2a23a')):
        x = 90 + i * 80
        p.shape([(x, 120), (x + 74, 120), (x + 74, 200), (x, 200)], hexc(col), mul(hexc(col), .78), 4, 6)
    p.shape([(460, 60), (540, 60), (540, 200), (460, 200)], (255, 255, 255), hexc('#d8d8d8'), 5, 6)
    p.dot(480, 100, 10, hexc('#9fd3ff'), 3); p.dot(520, 100, 10, hexc('#9fd3ff'), 3)
    return p.img.resize((w, int(w * 340 / 600)), Image.LANCZOS)


def termometro(c, x, y, h, nivel):
    if h < 8: return
    p = Pen(120, 420)
    p.shape([(40, 20), (80, 20), (80, 330), (40, 330)], (255, 255, 255), hexc('#dfe8f0'), 5, 4)
    p.dot(60, 360, 44, hexc('#e3463b'), 5)
    top = 330 - 290 * nivel
    p.poly([(48, top), (72, top), (72, 340), (48, 340)], hexc('#e3463b'))
    paste_c(c, p.img.resize((int(h * 120 / 420), int(h)), Image.LANCZOS), x, y)


def placa(c, x, y, texto, s=1.0, size=70):
    paste_c(c, txt(texto, size, 0), x, y, s)


@lru_cache(maxsize=4)
def ilha(luz='day'):
    """mapa: mar com uma ilha no norte (a Islândia), sem o continente do mapa padrão."""
    base = Image.new('RGBA', (BW, BH), hexc('#5fa8d8') + (255,)); p = Pen(BW, BH); rnd = random.Random(9)
    for i in range(34):
        x, y = rnd.randint(0, BW), rnd.randint(0, BH)
        p.stroke([(x, y), (x + 40, y - 6), (x + 80, y)], 4, hexc('#7cbde6'))
    pts = [(250, 760), (330, 640), (420, 700), (520, 600), (700, 620), (860, 560), (1010, 640), (1060, 780), (980, 960),
           (800, 1060), (600, 1100), (420, 1060), (330, 960), (240, 940), (190, 860)]
    sm = []
    for i in range(len(pts)):
        a, b, c = pts[i - 1], pts[i], pts[(i + 1) % len(pts)]
        sm += curve(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), b, ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2), 8)
    p.shape(sm, hexc('#9ccf6a'), hexc('#79a94c'), 7, 22)
    for cx, cy in ((560, 800), (760, 760), (700, 900)):
        p.shape([(cx - 70, cy + 40), (cx, cy - 60), (cx + 70, cy + 40)], (255, 255, 255), hexc('#dfe8f0'), 4, 6)
    # linha do Círculo Polar Ártico (tracejada) logo acima da ilha
    for x in range(0, BW, 60): p.stroke([(x, 470), (x + 34, 470)], 6, (255, 255, 255))
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


@lru_cache(maxsize=4)
def fazenda(luz='dusk'):
    """fazenda islandesa: vale com montanhas, cerca e a fita com vinho para atrair mariposas."""
    c = CEN('montanha', luz).copy()
    p = Pen(BW, BH)
    for x in range(0, BW + 1, 200):
        p.line([(x, 1540), (x, 1700)], hexc('#8a5f35'), 18, 4)
    p.line([(0, 1580), (BW, 1580)], hexc('#8a5f35'), 12, 4); p.line([(0, 1640), (BW, 1640)], hexc('#8a5f35'), 12, 4)
    p.shape([(900, 1250), (1180, 1250), (1180, 1480), (900, 1480)], hexc('#c0392b'), hexc('#8e2a20'), 6, 10)
    p.shape([(870, 1260), (1040, 1130), (1210, 1260)], hexc('#5a3d24'), None, 6)
    p.shape([(1010, 1360), (1070, 1360), (1070, 1480), (1010, 1480)], hexc('#5a3d24'), None, 4)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


def fita(c, x0, x1, y, f):
    """corda com fita vermelho-vinho pendurada."""
    p = Pen(int(x1 - x0) + 40, 220)
    pts = [(20 + i * (x1 - x0) / 10, 30 + 30 * math.sin(i / 10 * math.pi)) for i in range(11)]
    p.stroke(pts, 6, hexc('#d8c9a3'))
    for i in (3, 5, 7):
        x, y_ = pts[i]
        sw = 8 * math.sin(f * .12 + i)
        p.shape([(x - 14, y_), (x + 14, y_), (x + 18 + sw, y_ + 150), (x - 10 + sw, y_ + 150)], hexc('#7a1f3d'), hexc('#561229'), 4, 6)
    c.alpha_composite(p.img, (int(x0) - 20, int(y)))


def SFX(s):
    s.thunk(s.W(0, 'mosquito') - 2, 300, .6)
    s.ting(s.W(1, 'artico'), .3)
    s.whoosh(s.W(1, 'fresquinho') - 6, .4, .4)
    s.thunk(s.W(2, 'pocas') - 2, 420, .5)
    s.ting(s.W(3, 'mosca'), .3)
    s.thunk(s.W(4, 'mosquito') - 2, 140, .9)
    for i in range(2): s.thunk(s.W(4, 'dois') - 2 + i * 6, 360, .4)
    s.whoosh(s.W(5, 'carga') - 6, .5, .4)
    s.trill(s.W(6, 'antartida'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 mapa (ilha da Islândia, mosquito barrado) | s1 neve (montanhas geladas do norte, sol fraco, termômetro)
# s2 neve (poça congelando, larvas com frio) | s3 fazenda em Kjós ao entardecer (fã de insetos, fita com vinho, mosca)
# s4 fazenda (é mosquito! mais dois) | s5 mapa (navio de carga chega à ilha, termômetro sobe) | s6 neve ao entardecer (Antártida, pinguim)


def s0(f):
    c = ilha('day').copy()
    i0 = wt(0, 'islandia') - 3
    m0 = wt(0, 'mosquito') - 3
    if f >= i0: placa(c, 620, 1240, 'ISLÂNDIA', back(ramp(f, i0, i0 + 8)), 90)
    if f >= m0:
        s = back(ramp(f, m0, m0 + 8))
        put_mosq(c, 640, 440, 260 * s, f, 1, expr='shock')
        p = Pen(300, 300); p.stroke([(40, 40), (260, 260)], 26, hexc('#e3463b')); p.stroke([(260, 40), (40, 260)], 26, hexc('#e3463b'))
        paste_c(c, p.img.resize((260, 260), Image.LANCZOS), 640, 440, s)
        placa(c, 640, 600, 'SEM MOSQUITO', s, 76)
    t = easeOut(ramp(f, 0, 60))
    return c, (620, lerp(900, 820, t), lerp(1.45, 1.15, t), 0), 'day'


def s1(f):
    c = CEN('neve', 'day').copy()
    a0 = wt(1, 'artico') - 3
    q0 = wt(1, 'fresquinho') - 3
    put_pessoa(c, 620, 1980, 1050, f, 1, shirt='#2f7fd1', pants='#3b3f4a', pocket=False, skin=0, hair='#d8b25a',
               expr='pained' if f >= q0 else 'neutral', arms='cheek' if f >= q0 else 'hang')
    if f >= a0: placa(c, 620, 560, 'QUASE NO ÁRTICO', back(ramp(f, a0, a0 + 8)), 70)
    if f >= q0:
        termometro(c, 960, 860, 380 * back(ramp(f, q0, q0 + 8)), .25)
        placa(c, 620, 690, 'VERÃO CURTO', back(ramp(f, q0 + 2, q0 + 10)), 72)
    t = smooth(ramp(f, 0, 130))
    return c, (lerp(600, 640, t), lerp(1200, 1150, t), lerp(1.12, 1.22, t), 0), 'day'


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def poca(c, x, y, w, ice):
    p = Pen(600, 200)
    p.shape(ell_pts(300, 100, 280, 80, 48), hexc('#5fa8d8') if ice < .5 else hexc('#cfe9f7'), hexc('#3f88b8') if ice < .5 else hexc('#a9d0e6'), 5, 10)
    if ice >= .5:
        for a, b in (((160, 80), (260, 120)), ((300, 60), (380, 130)), ((400, 90), (470, 70))): p.stroke([a, b], 4, (255, 255, 255))
    c.alpha_composite(p.img.resize((w, int(w / 3)), Image.LANCZOS), (int(x - w / 2), int(y - w / 6)))


def s2(f):
    c = CEN('neve', 'dusk').copy()
    p0 = wt(2, 'pocas') - 3
    l0 = wt(2, 'larvas') - 3
    k0 = wt(2, 'crescer') - 3
    cyc = (f // 20) % 2
    ice = 1 if f >= p0 and (f < l0 or True) else cyc
    poca(c, 620, 1560, 900, ice)
    for i, x in enumerate((420, 620, 820)):
        put_larva(c, x, 1530 - (i % 2) * 30, 200 * back(ramp(f, l0 + i * 3, l0 + i * 3 + 8)), f, i, cold=1 if f >= p0 else 0)
    if f < p0: placa(c, 620, 800, 'GELA... DEGELA...', 1.0, 70)
    if f >= p0 and f < k0: placa(c, 620, 800, 'CONGELOU!', back(ramp(f, p0, p0 + 8)), 96)
    if f >= k0: placa(c, 620, 800, 'NÃO CRESCEM', back(ramp(f, k0, k0 + 8)), 84)
    t = smooth(ramp(f, 0, 120))
    return c, (620, lerp(1300, 1350, t), lerp(1.2, 1.4, t), 0), 'dusk'


def s3(f):
    c = fazenda('dusk').copy()
    m0 = wt(3, 'mosca') - 3
    v0 = wt(3, 'vinho') - 3
    fz = wt(3, 'fazenda') - 3
    fita(c, 160, 760, 1060, f)
    put_pessoa(c, 900, 2040, 1050, f, 2, shirt='#3aa76d', pants='#3b3f4a', pocket=False, skin=1, hair='#6b3a1e',
               expr='shock' if f >= m0 else 'neutral', arms='point' if f >= m0 else 'hang', look=-1, tilt=0)
    if f >= m0: put_mosq(c, 470, 1150, 170, f, 3, flip=True, expr='calm')
    if f >= m0 and f < v0: placa(c, 560, 640, 'MOSCA ESQUISITA?', back(ramp(f, m0, m0 + 8)), 66)
    if f >= v0: placa(c, 560, 640, 'FITA COM VINHO', back(ramp(f, v0, v0 + 8)), 70)
    if f < m0: placa(c, 620, 460, 'OUTUBRO DE 2025', back(ramp(f, 0, 8)), 72)
    t = smooth(ramp(f, 0, 160))
    return c, (lerp(560, 640, t), 1250, lerp(1.25, 1.15, t), 0), 'dusk'


def s4(f):
    c = fazenda('dusk').copy()
    m0 = wt(4, 'mosquito') - 3
    d0 = wt(4, 'dois') - 3
    k0 = wt(4, 'confirmaram') - 3
    fita(c, 160, 760, 1060, f)
    put_pessoa(c, 900, 2040, 1050, f, 2, shirt='#3aa76d', pants='#3b3f4a', pocket=False, skin=1, hair='#6b3a1e',
               expr='shock' if f < d0 else 'grin', arms='up' if f < d0 else 'point', look=-1)
    put_mosq(c, 470, 1150, 260, f, 3, flip=True, expr='smug')
    for i, (x, y) in enumerate(((300, 900), (560, 860))):
        if f >= d0 + i * 4: put_mosq(c, x, y, 200 * back(ramp(f, d0 + i * 4, d0 + i * 4 + 8)), f, 4 + i, flip=True)
    if f >= m0 and f < k0: placa(c, 600, 560, 'MOSQUITO!', back(ramp(f, m0, m0 + 8)), 110)
    if f >= k0: placa(c, 600, 560, 'CONFIRMADO!', back(ramp(f, k0, k0 + 8)), 96)
    kk = kick(f, m0)
    t = smooth(ramp(f, 0, 100))
    return c, (lerp(640, 600, t), 1200 + kk * 10, lerp(1.15, 1.25, t), kk), 'dusk'


def s5(f):
    c = ilha('dusk').copy()
    k0 = wt(5, 'carga') - 3
    q0 = wt(5, 'quente') - 3
    placa(c, 760, 1170, 'ISLÂNDIA', 1.0, 80)
    t = ramp(f, 0, k0 + 20)
    x, y = lerp(-200, 420, easeOut(t)), lerp(1900, 1420, easeOut(t))
    paste_c(c, navio_img(460), x, y + 6 * math.sin(f * .15))
    if f >= k0:
        put_mosq(c, x - 40 + 30 * math.sin(f * .2), y - 200, 150, f, 6, expr='smug')
        placa(c, x + 140, y - 360, 'DE CARONA', back(ramp(f, k0, k0 + 8)), 76)
    if f >= q0:
        termometro(c, 1040, 900, 380 * back(ramp(f, q0, q0 + 8)), lerp(.25, .8, easeOut(ramp(f, q0, q0 + 30))))
        placa(c, 820, 560, 'MAIS QUENTE', back(ramp(f, q0 + 2, q0 + 10)), 72)
    tt = smooth(ramp(f, 0, 150))
    return c, (lerp(560, 680, tt), lerp(1200, 1050, tt), lerp(1.15, 1.2, tt), 0), 'dusk'


def s6(f):
    c = CEN('neve', 'golden').copy()
    m0 = wt(6, 'mosquito') - 3
    a0 = wt(6, 'antartida') - 3
    for i, x in enumerate((420, 820)):
        put_ping(c, x, 1720 - i * 30, 540, f, 7 + i, look=.5 - i, expr='smug' if f >= a0 else 'calm')
    if f >= m0 and f < a0: placa(c, 620, 800, 'SEM MOSQUITO...', back(ramp(f, m0, m0 + 8)), 76)
    if f >= a0: placa(c, 620, 800, 'SÓ A ANTÁRTIDA!', back(ramp(f, a0, a0 + 8)), 76)
    t = easeOut(ramp(f, 0, 90))
    return c, (lerp(620, 640, t), lerp(1250, 1200, t), lerp(1.1, 1.3, t), lerp(0, 2, t)), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
