"""Formato DESENHO: batidinha na lata chacoalhada não adianta (Curiosidades da IA, 12/11/2026, 12h). Categoria: CIÊNCIA DO DIA A DIA.
Fatos: The Conversation, "Does tapping a can of fizzy drink really stop it foaming over?" (2016): o gás carbônico fica
dissolvido sob pressão; chacoalhar solta bolhas das paredes e põe mais bolhas no líquido; ao abrir, a pressão cai, as bolhas
crescem, sobem e empurram o líquido para fora. The Register, 13/12/2019 (estudo da Universidade do Sul da Dinamarca):
1.000 latas de 330 ml, metade chacoalhada por 2 minutos, com e sem 3 batidinhas na lateral; pesadas antes e depois de abrir:
diferença sem significância estatística (0,159 g); o único jeito aparente de não perder líquido é esperar as bolhas assentarem.
Live Science, "Does tapping on a soda can really stop it from exploding?"."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10c', '2026-11-08-10h')
pessoa = _h10.pessoa

LINES = [
    "Dar batidinha na lata chacoalhada não adianta nada.",
    "Dentro da latinha fechada, o gás fica espremido, misturado na bebida.",
    "Quando você chacoalha, aparece um monte de bolinhas de gás no meio do líquido.",
    "Aí você abre: a pressão cai, as bolinhas incham de uma vez e empurram a bebida pra fora.",
    "Na Dinamarca, cientistas chacoalharam latinhas e deram batidinhas em metade delas. Foram mil latas!",
    "Você vê, a bebida que espirrou foi praticamente a mesma. A batidinha não muda nada.",
    "O único truque que funciona é esperar as bolinhas se acalmarem.",
    "Ou seja: a batidinha só serve pra te distrair... enquanto você espera.",
]
CAPTXT = [
    "Dar batidinha na lata chacoalhada não adianta nada.",
    "Dentro da latinha fechada, o gás fica espremido,|misturado na bebida.",
    "Quando você chacoalha, aparece um monte|de bolinhas de gás no meio do líquido.",
    "Aí você abre: a pressão cai, as bolinhas incham de uma vez|e empurram a bebida pra fora.",
    "Na Dinamarca, cientistas chacoalharam latinhas|e deram batidinhas em metade delas. Foram 1.000 latas!",
    "Você vê, a bebida que espirrou foi praticamente a mesma.|A batidinha não muda nada.",
    "O único truque que funciona|é esperar as bolinhas se acalmarem.",
    "Ou seja: a batidinha só serve pra te distrair...|enquanto você espera.",
]
FALA_TIKTOK = "Você dá batidinha na lata? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [4]
CHECK = [(0, 'batidinha', 4), (0, 'nada', 6), (1, 'gas', 4), (1, 'espremido', 6), (2, 'chacoalha', 4), (2, 'bolinhas', 6),
         (3, 'abre', 4), (3, 'incham', 4), (3, 'fora', 6), (4, 'cientistas', 4), (4, 'metade', 4), (4, 'mil', 6),
         (5, 'mesma', 4), (5, 'nada', 6), (6, 'esperar', 6), (7, 'distrair', 4), (7, 'espera', 8)]

LATA, LATA_D = hexc('#e8463c'), hexc('#b32e27')
BEB, BEB_D = hexc('#7a3b1e'), hexc('#5a2a14')
ESP, ESP_D = hexc('#f3e7cf'), hexc('#d9c6a2')


# ------------------------------------------------------------------ objetos novos
def lata(expr='calm', blink=0, look=0.0, aberta=0, inch=0.0):
    """latinha de bebida com carinha (300x500). aberta=1 anel puxado; inch 0..1 = lata estufada."""
    p = Pen(300, 500)
    w = 105 + 14 * inch
    p.shape([(150 - w, 70), (150 + w, 70), (150 + w + 4, 430), (150 - w - 4, 430)], LATA, LATA_D, 6, 16)
    p.shape(ell_pts(150, 70, w, 26, 40), hexc('#c9ced6'), hexc('#9aa1ad'), 5, 4)
    p.shape(ell_pts(150, 432, w + 4, 22, 40, 0, 0, 2.0), hexc('#c9ced6'), hexc('#9aa1ad'), 5, 4)
    p.poly([(150 - w + 6, 300), (150 + w - 6, 300), (150 + w - 4, 340), (150 - w + 4, 340)], hexc('#ffffff'), 0)
    if aberta:
        p.shape(ell_pts(170, 64, 26, 10, 20), hexc('#3a2a2a'), None, 3)
        p.shape(ell_pts(120, 40, 26, 14, 20, -.6), hexc('#9aa1ad'), hexc('#6f7683'), 3, 2)
    else:
        p.shape(ell_pts(150, 66, 34, 12, 20), hexc('#9aa1ad'), hexc('#6f7683'), 3, 2)
    for s in (-1, 1):
        x, y = 150 + s * 40, 190
        if blink > .6: p.stroke([(x - 14, y), (x + 14, y)], 6)
        elif expr == 'shock': p.dot(x, y, 24, (255, 255, 255), 4); p.dot(x + look * 6, y, 8, INK)
        elif expr == 'side': p.dot(x, y, 20, (255, 255, 255), 4); p.dot(x + look * 6, y + 2, 8, INK); p.stroke([(x - 20, y - 6), (x + 20, y - 6)], 6)
        else: p.dot(x, y, 20, (255, 255, 255), 4); p.dot(x + look * 6, y, 8, INK)
    if expr == 'shock': p.dot(150, 250, 18, hexc('#7a2e2e'), 4)
    elif expr == 'dizzy':
        pts = [(118 + i * 8, 248 + (5 if i % 2 else -5)) for i in range(9)]; p.stroke(pts, 5)
    elif expr == 'smug': p.arc(156, 238, 26, 14, 20, 160, 6)
    else: p.arc(150, 236, 26, 16, 20, 160, 6)
    return p.img


def put_lata(c, x, y, h, f, seed=1, rot=0, **kw):
    """lata centrada em (x, y)."""
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'inch' in kw: kw['inch'] = round(kw['inch'] * 8) / 8
    im = sprite('lata', tuple(sorted(kw.items())), int(h), .6, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


@lru_cache(maxsize=2)
def corte_bg():
    """lata gigante cortada: dá pra ver a bebida dentro (palco inteiro, transparente fora)."""
    p = Pen(BW, BH)
    p.shape([(171, 360), (1071, 360), (1091, 2000), (151, 2000)], LATA, LATA_D, 8, 24)
    p.shape([(231, 430), (1011, 430), (1026, 1930), (216, 1930)], BEB, BEB_D, 6, 20)
    p.shape(ell_pts(621, 360, 450, 70, 48), hexc('#c9ced6'), hexc('#9aa1ad'), 6, 8)
    p.stroke([(171, 520), (1071, 520)], 5)
    return p.img.resize((BW, BH), Image.LANCZOS)


@lru_cache(maxsize=32)
def bolha(r):
    p = Pen(2 * r + 20, 2 * r + 20)
    p.shape(ell_pts(r + 10, r + 10, r, r, 28), hexc('#f6d9b8'), hexc('#d9b48a'), 3, 3)
    p.dot(r + 10 - r * .35, r + 10 - r * .35, max(2, r * .22), (255, 255, 255))
    return p.img.resize((2 * r + 20, 2 * r + 20), Image.LANCZOS)


@lru_cache(maxsize=4)
def espirro(s=1.0):
    """jato de espuma saindo da lata (400x700, base embaixo no centro)."""
    p = Pen(400, 700)
    rnd = random.Random(3)
    pts = [(200 - 40, 700), (200 - 150, 380), (200 - 120, 150), (200, 40), (200 + 120, 150), (200 + 150, 380), (200 + 40, 700)]
    p.shape(pts, ESP, ESP_D, 5, 10)
    for i in range(8):
        p.dot(rnd.randint(80, 320), rnd.randint(80, 600), rnd.randint(14, 30), ESP, 4)
    return p.img.resize((400, 700), Image.LANCZOS)


@lru_cache(maxsize=2)
def balanca_img():
    p = Pen(900, 500)
    p.shape([(400, 120), (500, 120), (520, 460), (380, 460)], hexc('#9aa1ad'), hexc('#6f7683'), 5, 8)
    p.shape([(250, 440), (650, 440), (670, 490), (230, 490)], hexc('#6f7683'), hexc('#4f5560'), 5, 6)
    p.line([(70, 120), (830, 120)], hexc('#c9ced6'), 26, 5)
    for x in (130, 770):
        p.line([(x, 120), (x - 70, 260)], INK, 4, 0); p.line([(x, 120), (x + 70, 260)], INK, 4, 0)
        p.shape(ell_pts(x, 270, 120, 26, 32), hexc('#c9ced6'), hexc('#9aa1ad'), 5, 4)
    p.dot(450, 120, 22, hexc('#ffd84a'), 5)
    return p.img.resize((900, 500), Image.LANCZOS)


def SFX(s):
    for i in range(3): s.thunk(s.W(0, 'batidinha') - 2 + i * 5, 320, .4)
    s.thunk(s.W(0, 'nada') - 2, 140, .8)
    s.thunk(s.W(1, 'espremido') - 2, 200, .5)
    s.patter(s.W(2, 'chacoalha') - 2, s.W(2, 'chacoalha') + 24, 10, .2)
    s.ting(s.W(2, 'bolinhas'), .3)
    s.thunk(s.W(3, 'abre') - 2, 300, .6); s.splash(s.W(3, 'fora') - 6, .6)
    s.thunk(s.W(4, 'cientistas') - 2, 220, .5)
    for i in range(3): s.thunk(s.W(4, 'metade') - 2 + i * 5, 320, .35)
    s.ting(s.W(4, 'mil'), .35)
    s.thunk(s.W(5, 'mesma') - 2, 150, .7)
    s.ting(s.W(6, 'esperar'), .3)
    for i in range(3): s.thunk(s.W(7, 'distrair') - 2 + i * 6, 320, .35)
    s.trill(s.W(7, 'espera'), .9, .3)


def maos(x, feet, h):
    """posição da lata nas mãos da pessoa com arms='ask' (mãos juntas na frente da barriga)."""
    s = h / 1000
    return x, feet - (975 - 540) * s


# ---------------------------------------------------------------- cenas
def s0(f):
    """cozinha: pessoa dando batidinhas na lata; NADA!"""
    c = CEN('cozinha', 'day').copy()
    b0 = wt(0, 'batidinha') - 3
    n0 = wt(0, 'nada') - 3
    x, feet, h = 560, 2080, 1500
    put_pessoa(c, x, feet, h, f, 1, expr='grin' if f < n0 else 'shock', arms='ask', look=1)
    lx, ly = maos(x, feet, h)
    put_lata(c, lx, ly + 70, 260, f, 1, expr='side' if f < n0 else 'shock', look=-1)
    if b0 <= f < n0:
        tap = (f - b0) % 10 < 4
        paste_c(c, txt('TOC TOC', 80, -6), lx + 330, ly + 40 - (10 if tap else 0))
    if f >= n0: paste_c(c, txt('NÃO ADIANTA!', 96, 6), 640, 560, back(ramp(f, n0, n0 + 8)))
    kk = kick(f, n0 + 2)
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.35, 1.1, t) * (1 + .0009 * f)
    return c, (600, 1250 + kk * 10, z, kk), 'day'


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def bolhas_dentro(c, f, n, r0, r1, seed, inch=0.0, sobe=0.0):
    rnd = random.Random(seed)
    for i in range(n):
        x = rnd.randint(290, 950); y = rnd.randint(650, 1850)
        y -= sobe * (y - 450) * (.4 + .6 * rnd.random())
        r = int(lerp(r0, r1, rnd.random()) * (1 + 1.6 * inch))
        paste_c(c, bolha(max(6, r)), x + 6 * math.sin(f * .2 + i), y)


def s1(f):
    """dentro da lata (corte): gás espremido misturado na bebida."""
    c = CEN('cozinha', 'day').copy()
    c.alpha_composite(corte_bg())
    g0 = wt(1, 'gas') - 3
    e0 = wt(1, 'espremido') - 3
    if f >= g0: bolhas_dentro(c, f, 26, 16, 26, 4)
    if f >= g0: paste_c(c, txt('GÁS', 110, -6), 621, 700, back(ramp(f, g0, g0 + 8)))
    if f >= e0: paste_c(c, txt('ESPREMIDO!', 90, 6), 621, 1150, back(ramp(f, e0, e0 + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.0, 1.12, t) * (1 + .0009 * f)
    return c, (621, lerp(1000, 1150, t), z, 0), 'day'


def s2(f):
    """cozinha: pessoa chacoalhando a lata; no corte aparecem bolinhas."""
    c = CEN('cozinha', 'day').copy()
    ch = wt(2, 'chacoalha') - 3
    bo = wt(2, 'bolinhas') - 3
    x, feet, h = 430, 2080, 1400
    sh = f >= ch
    put_pessoa(c, x, feet, h, f, 2, expr='grin' if sh else 'neutral', arms='up' if sh else 'ask', look=1)
    s = h / 1000
    if sh:
        lx, ly = x + 20 * math.sin(f * 1.3), feet - 975 * s + 60 * s + 30 * math.sin(f * 1.3 + 1)
        put_lata(c, lx, ly, 220, f, 2, rot=18 * math.sin(f * 1.3), expr='dizzy')
        paste_c(c, txt('CHACOALHA!', 80, -6), 600, 450, back(ramp(f, ch, ch + 8)))
    else:
        lx, ly = maos(x, feet, h); put_lata(c, lx, ly + 70, 250, f, 2)
    # lupa: o que acontece lá dentro
    if f >= bo:
        a = back(ramp(f, bo, bo + 10))
        r = int(250 * a)
        if r > 10:
            lu = Image.new('RGBA', (2 * r + 20, 2 * r + 20), (0, 0, 0, 0))
            d = ImageDraw.Draw(lu)
            d.ellipse((10, 10, 10 + 2 * r, 10 + 2 * r), fill=BEB + (255,), outline=INK + (255,), width=10)
            rnd = random.Random(8)
            for i in range(22):
                bx, by = rnd.randint(40, 2 * r - 20), rnd.randint(40, 2 * r - 20)
                if (bx - r - 10) ** 2 + (by - r - 10) ** 2 < (r - 30) ** 2:
                    bb = bolha(max(6, int(rnd.randint(20, 38) * a)))
                    lu.alpha_composite(bb, (int(bx - bb.size[0] / 2), int(by - bb.size[1] / 2)))
            c.alpha_composite(lu, (int(900 - r - 10), int(1050 - r - 10)))
            paste_c(c, txt('BOLINHAS!', 80, 6), 900, 1380, a)
    z = lerp(1.08, 1.2, smooth(f / 120)) * (1 + .0009 * f)
    return c, (640, 1200, z, 1.5 * math.sin(f * .3) * (1 if ch <= f < bo + 20 else 0)), 'day'


def s3(f):
    """cozinha: abre a lata, as bolinhas incham e a bebida espirra."""
    c = CEN('cozinha', 'day').copy()
    a0 = wt(3, 'abre') - 3
    i0 = wt(3, 'incham') - 3
    fo = wt(3, 'fora') - 3
    x, feet, h = 440, 2080, 1400
    aberto = f >= a0
    put_pessoa(c, x, feet, h, f, 3, expr='shock' if f >= fo else ('grin' if not aberto else 'nervous'), arms='point', look=1)
    s_ = h / 1000
    lx, ly = x + 260 * s_, feet - 975 * s_ + 380 * s_ + 120
    inch = smooth(ramp(f, i0, i0 + 10))
    if f >= fo:
        g = back(ramp(f, fo, fo + 8))
        if g > .05:
            im = espirro()
            im = im.resize((max(1, int(400 * g)), max(1, int(700 * g))))
            c.alpha_composite(im, (int(lx - im.size[0] / 2), int(ly - 120 - im.size[1])))
    put_lata(c, lx, ly, 260, f, 3, expr='shock' if f >= i0 else 'side', aberta=1 if aberto else 0, inch=inch)
    if aberto: paste_c(c, txt('PSSST!', 90, -6), 400, 520, back(ramp(f, a0, a0 + 8)))
    if f >= fo: paste_c(c, txt('SPLASH!', 100, 6), 700, 380, back(ramp(f, fo, fo + 8)))
    kk = kick(f, fo + 2)
    z = lerp(1.15, 1.05, easeOut(ramp(f, fo - 6, fo + 12))) * (1 + .0009 * f)
    return c, (640, 1150 + kk * 12, z, kk * 2), 'day'


def s4(f):
    """laboratório: cientistas com muitas latas, batidinhas em metade."""
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    c0 = wt(4, 'cientistas') - 3
    m0 = wt(4, 'metade') - 3
    k0 = wt(4, 'mil') - 3
    for i, (x, sd, kw) in enumerate(((330, 1, dict(arms='clip', hair='#9a9a9a', skin=3, expr='stern')),
                                     (930, 2, dict(arms='point' if f >= m0 else 'clip', bun=True, expr='neutral', look=-1)))):
        s = back(ramp(f, c0 + i * 5, c0 + i * 5 + 9))
        put_sci(c, x, 1500, 760 * s, f, sd, **kw)
    # bancada com latas
    ImageDraw.Draw(c).rectangle((40, 1500, 1200, 1560), fill=hexc('#8a5f35') + (255,), outline=INK + (255,), width=6)
    n = 12
    for i in range(n):
        x = 120 + i * 92
        ap = back(ramp(f, 6 + i * 2, 14 + i * 2))
        tap = i >= n // 2 and f >= m0 and (f - m0 + i * 3) % 10 < 4
        put_lata(c, x, 1440 - (8 if tap else 0), 140 * ap, f, 10 + i, expr='side' if tap else 'calm')
    if f >= m0: paste_c(c, txt('METADE: TOC TOC', 64, -4), 621, 1700, back(ramp(f, m0, m0 + 8)))
    if f >= k0: paste_c(c, txt('1.000 LATAS!', 110, 6), 621, 620, back(ramp(f, k0, k0 + 8)))
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.25, 1.05, t) * (1 + .0009 * f)
    return c, (621, 1250, z, 0), 'day'


def s5(f):
    """laboratório (dusk): balança empatada entre latas com e sem batidinha."""
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(.5))
    m0 = wt(5, 'mesma') - 3
    n0 = wt(5, 'nada') - 3
    bal = balanca_img()
    wob = 4 * math.sin(f * .15) * (1 - smooth(ramp(f, m0 - 10, m0 + 4)))
    paste_c(c, bal.rotate(wob, Image.BICUBIC), 621, 1250)
    for k, (x, ex) in enumerate(((621 - 320, 'calm'), (621 + 320, 'side'))):
        yy = 1250 - 250 + 270 - 60 + (wob * 6 if k == 0 else -wob * 6)
        put_lata(c, x, yy - 110, 220, f, 20 + k, expr=ex, aberta=1)
    paste_c(c, txt('SEM TOC', 60, 0), 621 - 320, 1500)
    paste_c(c, txt('COM TOC', 60, 0), 621 + 320, 1500)
    if f >= m0: paste_c(c, txt('EMPATE!', 120, -6), 621, 640, back(ramp(f, m0, m0 + 8)))
    if f >= n0: paste_c(c, txt('NÃO MUDA NADA', 76, 5), 621, 820, back(ramp(f, n0, n0 + 8)))
    z = lerp(1.05, 1.2, smooth(f / 150)) * (1 + .0009 * f)
    return c, (621, 1150, z, 0), 'dusk'


def s6(f):
    """cozinha (golden, tempo passando): esperar as bolinhas se acalmarem."""
    c = CEN('cozinha', 'golden').copy()
    e0 = wt(6, 'esperar') - 3
    x, feet, h = 430, 2080, 1400
    put_pessoa(c, x, feet, h, f, 4, expr='neutral', arms='ask', look=1)
    lx, ly = maos(x, feet, h)
    put_lata(c, lx, ly + 70, 250, f, 4, expr='calm' if f >= e0 + 30 else 'side')
    spin = ramp(f, e0, e0 + 60)
    paste_c(c, clock_img(round((1 + spin * 3) * 8) / 8, round(spin * 36 * 4) / 4, 260), 940, 700, back(ramp(f, e0 - 4, e0 + 6)))
    if f >= e0: paste_c(c, txt('ESPERA...', 90, 6), 900, 1000, back(ramp(f, e0, e0 + 8)))
    z = lerp(1.08, 1.2, smooth(f / 150)) * (1 + .0009 * f)
    return c, (640, 1200, z, 0), 'golden'


def s7(f):
    """cozinha (dusk): a pessoa dá batidinhas só pra passar o tempo, olhando o relógio."""
    c = CEN('cozinha', 'dusk').copy()
    d0 = wt(7, 'distrair') - 3
    e0 = wt(7, 'espera') - 3
    x, feet, h = 560, 2080, 1450
    put_pessoa(c, x, feet, h, f, 5, expr='smug' if f >= e0 else 'neutral', arms='ask', look=1)
    lx, ly = maos(x, feet, h)
    tap = f >= d0 and (f - d0) % 12 < 4
    put_lata(c, lx, ly + 70 - (8 if tap else 0), 260, f, 5, expr='side', look=-1)
    if f >= d0: paste_c(c, txt('TOC TOC', 70, -6), lx + 240, ly - 60, back(ramp(f, d0, d0 + 8)))
    paste_c(c, clock_img(round(f / 60 * 8) / 8, round(f / 5 * 4) / 4, 220), 950, 620)
    z = lerp(1.05, 1.3, easeOut(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (640, 1200, z, lerp(0, -3, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
