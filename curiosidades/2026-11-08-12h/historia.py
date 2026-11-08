"""Formato DESENHO: por que o pica-pau não machuca a cabeça (Curiosidades da IA, 08/11/2026, 12h). Categoria: ANIMAIS.
Fatos: Van Wassenbergh et al. 2022, Current Biology, via Phys.org (14/07/2022) "Woodpeckers' heads act more like stiff hammers
than safety helmets", ScienceDaily (14/07/2022) e NPR (14/07/2022): a cabeça era vista como um capacete que absorve o
impacto; a equipe analisou vídeos em alta velocidade de três espécies de pica-pau (mais de 100 bicadas); a cabeça
funciona como um martelo duro e não amortece; amortecer atrapalharia a bicada; a desaceleração passa do limite de
concussão de humanos e macacos, mas o cérebro pequeno do pica-pau aguenta (a carga no cérebro dele fica abaixo da que
causa concussão em humanos). PBS Nature: o pica-pau bate o bico na árvore até 20 vezes por segundo."""
from kit import *
import kit

LINES = [
    "O pica-pau bate a cabeça na árvore até vinte vezes por segundo... e o cérebro dele não se machuca.",
    "Por muito tempo, cientistas acharam que a cabeça dele era um capacete que amortece a pancada.",
    "Até que, em dois mil e vinte e dois, uma equipe filmou pica-paus em câmera superlenta.",
    "E viu o contrário: a cabeça dele não amortece nada. Ela é dura, igual a um martelo.",
    "Se amortecesse, a bicada perdia a força e ele nem furava a madeira.",
    "Você vê, o segredo é o tamanho: o cérebro dele é tão pequeno que aguenta pancadas que fariam mal ao nosso.",
    "Ou seja: o pica-pau não tem capacete nenhum... só tem a cabeça dura e o cérebro pequeno.",
]
CAPTXT = [
    "O pica-pau bate a cabeça na árvore até 20 vezes por segundo...|e o cérebro dele não se machuca.",
    "Por muito tempo, cientistas acharam que a cabeça dele|era um capacete que amortece a pancada.",
    "Até que, em 2022, uma equipe|filmou pica-paus em câmera superlenta.",
    "E viu o contrário: a cabeça dele não amortece nada.|Ela é dura, igual a um martelo.",
    "Se amortecesse, a bicada perdia a força|e ele nem furava a madeira.",
    "Você vê, o segredo é o tamanho: o cérebro dele é tão pequeno|que aguenta pancadas que fariam mal ao nosso.",
    "Ou seja: o pica-pau não tem capacete nenhum...|só tem a cabeça dura e o cérebro pequeno.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [2]
CHECK = [(0, 'vinte', 4), (0, 'machuca', 6), (1, 'capacete', 4), (1, 'pancada', 6), (2, 'filmou', 4), (2, 'superlenta', 6),
         (3, 'nada', 4), (3, 'martelo', 6), (4, 'forca', 4), (4, 'madeira', 6), (5, 'pequeno', 4), (5, 'nosso', 6),
         (6, 'capacete', 4), (6, 'pequeno', 8)]

PRETO, PRETOD = hexc('#2e2a33'), hexc('#1c1a20')
BRANCO = hexc('#f6f4ee')
VERM, VERMD = hexc('#d8342c'), hexc('#a32019')
BICO, BICOD = hexc('#8a8f99'), hexc('#5f6470')
CEREBRO, CEREBROD = hexc('#f4a6b8'), hexc('#d47a92')


# ------------------------------------------------------------------ personagens e objetos novos
def picapau(peck=0.0, blink=0, expr='calm', look=0.4, xray=0, soft=0.0, helmet=0, dizzy=0):
    """pica-pau agarrado num tronco à direita (640x800). O tronco começa em x≈600 do desenho.
    peck 0..1 = cabeça vai para a frente (bico encosta no tronco em peck=1); xray mostra o cérebro;
    soft 0..1 = cabeça mole/achatada; helmet = capacete amarelo."""
    p = Pen(640, 800)
    # cauda dura apoiada no tronco
    p.shape([(390, 600), (470, 610), (520, 790), (470, 770), (430, 790)], PRETO, PRETOD, 5, 8)
    # corpo
    p.shape(ell_pts(410, 470, 115, 190, 56, -.12), BRANCO, hexc('#d6d2c6'), 5, 14)
    # asa preta com bolinhas brancas
    p.shape(ell_pts(370, 480, 95, 170, 48, -.18), PRETO, PRETOD, 5, 10)
    for i, (x, y) in enumerate(((340, 420), (380, 450), (330, 500), (370, 540), (320, 580), (360, 610))):
        p.dot(x, y, 10, BRANCO)
    # pés agarrados no tronco
    for y in (520, 600):
        p.line([(470, y - 20), (540, y), (600, y - 10)], hexc('#6f6a62'), 10, 3)
        p.line([(540, y), (600, y + 18)], hexc('#6f6a62'), 9, 3)
    # cabeça
    hx, hy = 380 + peck * 62, 220 + peck * 6
    rx, ry = 92 * (1 + soft * .25), 90 * (1 - soft * .3)
    if soft: hx += soft * 10
    p.shape(ell_pts(hx, hy, rx, ry, 56), PRETO, PRETOD, 5, 12)
    p.shape(ell_pts(hx + 10, hy + 30 * (1 - soft * .3), rx * .8, ry * .55, 48), BRANCO, hexc('#d6d2c6'), 0, 8)
    p.stroke([(hx - 70, hy + 30), (hx + 60, hy + 28)], 14, PRETO)
    # boné vermelho na nuca
    p.shape(ell_pts(hx - 50, hy - 50 * (1 - soft * .3), 48, 34, 32, -.5), VERM, VERMD, 4, 6)
    # bico reto e comprido
    bx = hx + rx - 6
    p.shape([(bx, hy - 18), (bx + 98, hy + 2), (bx, hy + 22)], BICO, BICOD, 5, 6)
    p.stroke([(bx + 4, hy + 2), (bx + 80, hy + 2)], 3)
    # olho
    ex, ey = hx + 22, hy - 8
    if xray:
        p.shape(ell_pts(hx - 14, hy - 6, 34, 26, 32), CEREBRO, CEREBROD, 4, 6)
        p.arc(hx - 20, hy - 10, 14, 8, 200, 340, 3); p.arc(hx - 6, hy - 2, 14, 8, 20, 160, 3)
    if blink:
        p.stroke([(ex - 18, ey), (ex + 18, ey)], 6)
    elif dizzy:
        p.dot(ex, ey, 26, (255, 255, 255), 5)
        p.arc(ex, ey, 12, 12, 0, 300, 4)
    else:
        r = 30 if expr == 'shock' else 25
        p.dot(ex, ey, r, (255, 255, 255), 5)
        p.dot(ex + look * 9, ey + 2, 11, INK); p.dot(ex + look * 9 - 3, ey - 2, 3.5, (255, 255, 255))
        if expr in ('smug', 'side'):
            p.poly([(ex - r - 4, ey - r - 4), (ex + r + 4, ey - r - 4), (ex + r + 4, ey - 4), (ex - r - 4, ey - 4)], PRETO); p.stroke([(ex - r, ey - 4), (ex + r, ey - 4)], 6)
    if helmet:
        hp = [(x, min(y, hy - 30)) for x, y in ell_pts(hx - 6, hy - 30, rx + 14, ry + 10, 48)]
        p.shape(hp, hexc('#f2c230'), hexc('#c9971c'), 5, 10)
        p.shape(ell_pts(hx - 6, hy - 32, rx + 34, 14, 40), hexc('#f2c230'), hexc('#c9971c'), 5, 4)
    return p.img


def put_pp(c, x, feet, h, f, seed=1, **kw):
    """x = centro do desenho; feet = base. O bico encosta no tronco em x + (600-320)*h/800."""
    kw['blink'] = 1 if (blinkAt(f, seed) > .6 and not kw.get('dizzy')) else 0
    for k, n in (('peck', 4), ('soft', 4)):
        if k in kw: kw[k] = round(kw[k] * n) / n
    put_sprite(c, 'picapau', x, feet, h, 640 / 800, False, None, **kw)


def head_y(feet, h):
    return feet - h + 226 * h / 800


def tronco_x(x, h):
    """x do começo do tronco para um pica-pau desenhado em x com altura h."""
    return x + (600 - 320) * h / 800


def tronco(c, x0, furos=0, f=0, top=0, bot=BH):
    """tronco grande começando em x0 e indo até a direita, com casca."""
    c.alpha_composite(_tronco_img(int(x0), int(top), int(bot)), (int(x0), int(top)))


@lru_cache(maxsize=16)
def _tronco_img(x0, top, bot):
    w = BW - x0 + 40
    p = Pen(int(w), int(bot - top))
    p.shape([(0, -20), (w, -20), (w, bot - top + 20), (0, bot - top + 20)], hexc('#8a5f35'), hexc('#65452a'), 7, 30)
    rnd = random.Random(int(x0))
    for i in range(14):
        y = rnd.randint(0, int(bot - top)); xx = rnd.randint(30, int(w) - 60)
        p.stroke([(xx, y), (xx + rnd.randint(-10, 10), y + rnd.randint(80, 200))], 5, hexc('#5a3d24'))
    return p.img.resize((int(w), int(bot - top)), Image.LANCZOS)


def furo(c, x, y, r):
    if r < 2: return
    paste_c(c, _furo_img(int(r)), x, y)


@lru_cache(maxsize=64)
def _furo_img(r):
    p = Pen(200, 200)
    p.shape(ell_pts(100, 100, 80, 90, 32), hexc('#3a2614'), None, 5)
    p.dot(100, 112, 50, hexc('#1f140a'))
    return p.img.resize((int(2 * r), int(2 * r)), Image.LANCZOS)


def lascas(c, x, y, age, life=12):
    if age < 0 or age >= life: return
    t = age / life
    for k in range(5):
        a = -1.2 + k * .5
        px, py = x - 30 - 160 * t * math.cos(a) * (.6 + k * .1), y + 160 * t * math.sin(a) + 300 * t * t
        p = Pen(60, 30); p.shape([(5, 10), (55, 5), (50, 22), (8, 25)], hexc('#e7c08a'), hexc('#c99a62'), 3, 3)
        paste_c(c, p.img.rotate(k * 40 + age * 25, expand=True), px, py)


@lru_cache(maxsize=8)
def cerebro(size=300):
    p = Pen(300, 240)
    p.shape(ell_pts(150, 120, 135, 100, 48), CEREBRO, CEREBROD, 6, 14)
    for (x, y, a0, a1) in ((90, 90, 200, 340), (150, 70, 20, 160), (210, 100, 200, 340), (110, 150, 20, 160), (190, 160, 200, 340)):
        p.arc(x, y, 40, 22, a0, a1, 6)
    p.stroke([(150, 30), (150, 210)], 6)
    return p.img.resize((size, int(size * .8)), Image.LANCZOS)


def filmadora(c, x, feet, s=1.0, rec=True):
    """câmera de filmar em tripé (feet = base)."""
    if s <= .02: return
    p = Pen(360, 600)
    for dx in (-90, 0, 90): p.line([(180, 260), (180 + dx, 590)], hexc('#3b3f4a'), 12, 4)
    p.shape([(60, 120), (270, 120), (270, 260), (60, 260)], hexc('#3b3f4a'), hexc('#262830'), 6, 10)
    p.shape([(270, 150), (350, 125), (350, 255), (270, 230)], hexc('#5b5f6b'), None, 5)
    p.dot(310, 190, 30, hexc('#8fc7ff'), 4)
    if rec: p.dot(95, 150, 16, hexc('#ff3b30'), 3)
    im = p.img.resize((int(360 * s), int(600 * s)), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(feet - im.size[1])))


@lru_cache(maxsize=4)
def mata(luz='day'):
    return CEN('floresta', luz)


def SFX(s):
    for i in range(6): s.thunk(s.W(0, 'arvore') - 2 + i * 3, 520, .45)
    s.ting(s.W(0, 'machuca'), .3)
    s.ting(s.W(1, 'capacete'), .3)
    s.thunk(s.W(1, 'pancada') - 2, 260, .6)
    s.whoosh(s.W(2, 'filmou') - 6, .4, .4)
    s.thunk(s.W(3, 'martelo') - 2, 140, .9)
    s.thunk(s.W(4, 'forca') - 2, 330, .4)
    s.ting(s.W(5, 'pequeno'), .3)
    s.trill(s.W(6, 'pequeno'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 floresta (pica-pau batendo no tronco) | s1 laboratório (cientista imagina capacete) | s2 floresta (equipe filma em câmera lenta)
# s3 floresta (cabeça dura = martelo) | s4 floresta (cabeça mole quica e não fura) | s5 floresta ao entardecer (raio-x: cérebro pequeno x nosso)
# s6 floresta golden (sem capacete, cabeça dura)
H_PP = 1100
X_PP = 520


def bater(f, f0, f1, per=6):
    """0..1 batendo rápido entre f0 e f1."""
    if f < f0 or f >= f1: return 0.0
    ph = (f - f0) % per
    return 1.0 if ph < per / 2 else 0.0


def s0(f):
    c = mata('day').copy()
    tx = tronco_x(X_PP, H_PP)
    tronco(c, tx)
    v0 = wt(0, 'vinte') - 3
    m0 = wt(0, 'machuca') - 3
    pk = bater(f, 2, m0 - 6, 4)
    n = len([k for k in range(2, min(f, m0 - 6), 4)])
    furo(c, tx + 40, head_y(1500, H_PP), min(70, 8 + n * 2.5))
    put_pp(c, X_PP, 1500, H_PP, f, 1, peck=pk, expr='calm' if f < m0 else 'smug', look=1)
    if pk: lascas(c, tx + 10, head_y(1500, H_PP), (f - 2) % 12)
    if f >= v0 and f < m0: paste_c(c, txt('20 POR SEGUNDO!', 66, -5), 600, 380, back(ramp(f, v0, v0 + 8)))
    if f >= m0: paste_c(c, txt('TUDO BEM!', 90, 5), 600, 380, back(ramp(f, m0, m0 + 8)))
    t = easeOut(ramp(f, 0, 40))
    kk = .4 * kick(f, 2 + ((f - 2) // 4) * 4) if pk else 0
    return c, (lerp(680, 640, t), 1000 + kk * 8, lerp(1.45, 1.2, t), kk), 'day'


def s1(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    k0 = wt(1, 'capacete') - 3
    p0 = wt(1, 'pancada') - 3
    put_sci(c, 420, 1560, 900, f, 1, arms='cheek' if f >= k0 else 'clip', expr='grin' if f >= k0 else 'neutral', look=1, hair='#9a9a9a', skin=1)
    if f >= k0 - 4:
        cont = Image.new('RGBA', (440, 380), (0, 0, 0, 0))
        im = sprite('picapau', tuple(sorted(dict(helmet=1, blink=0, look=.4, peck=1.0 if (f >= p0 and (f - p0) % 8 < 4) else 0.0).items())), 340, 640 / 800, False)
        cont.alpha_composite(im, (60, 20))
        thought(c, 840, 700, 260, back(ramp(f, k0 - 4, k0 + 6)), cont)
        paste_c(c, txt('CAPACETE?', 84, -5), 820, 390, back(ramp(f, k0, k0 + 8)))
    if f >= p0: paste_c(c, txt('AMORTECE!', 72, 5), 820, 1060, back(ramp(f, p0, p0 + 8)))
    t = smooth(ramp(f, 0, 110))
    return c, (lerp(600, 680, t), 1050, lerp(1.2, 1.25, t), 0), 'day'


def s2(f):
    c = mata('day').copy()
    tx = tronco_x(820, 760)
    tronco(c, tx)
    f0 = wt(2, 'filmou') - 3
    sl = wt(2, 'superlenta') - 3
    per = 4 if f < sl else 24
    pk = bater(f, 0, 10 ** 6, per)
    furo(c, tx + 30, head_y(1600, 760), 40)
    put_pp(c, 820, 1600, 760, f, 2, peck=pk, look=1)
    filmadora(c, 470, 1980, back(ramp(f, f0 - 6, f0 + 4)) * 1.1, rec=(f // 10) % 2 == 0)
    put_sci(c, 230, 2000, 900 * back(ramp(f, f0 - 2, f0 + 7)), f, 2, arms='point', bun=True, expr='grin', look=1)
    if f >= sl: paste_c(c, txt('CÂMERA LENTA', 76, -5), 600, 520, back(ramp(f, sl, sl + 8)))
    t = smooth(ramp(f, 0, 100))
    return c, (lerp(560, 600, t), lerp(1300, 1260, t), lerp(1.1, 1.18, t), 0), 'day'


def s3(f):
    c = mata('day').copy()
    tx = tronco_x(X_PP, H_PP)
    tronco(c, tx)
    n0 = wt(3, 'nada') - 3
    m0 = wt(3, 'martelo') - 3
    hit = f >= m0 and (f - m0) % 14 < 4
    furo(c, tx + 40, head_y(1500, H_PP), 60)
    put_pp(c, X_PP, 1500, H_PP, f, 3, peck=1.0 if hit else 0.0, expr='smug', look=1)
    if f >= n0 and f < m0: paste_c(c, txt('AMORTECE? NADA!', 62, -5), 640, 420, back(ramp(f, n0, n0 + 8)))
    if f >= m0:
        paste_c(c, txt('DURA COMO MARTELO!', 56, 5), 660, 420, back(ramp(f, m0, m0 + 8)))
        # martelinho fantasma junto da cabeça
        p = Pen(300, 200)
        p.line([(40, 160), (200, 60)], hexc('#9b6b3d'), 18, 4)
        p.shape([(170, 20), (270, 60), (250, 110), (150, 70)], hexc('#8d939e'), hexc('#5f6470'), 5, 6)
        paste_c(c, p.img.resize((240, 160), Image.LANCZOS), 380, 560, back(ramp(f, m0, m0 + 8)))
    if hit: lascas(c, tx + 10, head_y(1500, H_PP), (f - m0) % 14)
    kk = kick(f, m0 + ((f - m0) // 14) * 14) if f >= m0 else 0
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(640, 680, t), 1000 + kk * 10, lerp(1.2, 1.32, t), kk), 'day'


def s4(f):
    c = mata('golden').copy()
    tx = tronco_x(X_PP, H_PP)
    tronco(c, tx)
    fo = wt(4, 'forca') - 3
    md = wt(4, 'madeira') - 3
    ph = f % 16
    soft = 1.0 if ph < 6 else 0.0
    pk = 1.0 if ph < 6 else 0.0
    put_pp(c, X_PP, 1500, H_PP, f, 4, peck=pk, soft=soft, expr='shock' if f >= md else 'calm', dizzy=1 if f >= md + 10 else 0, look=1)
    if soft: paste_c(c, txt('BOING!', 80, -8), tx - 40, 760, 1.0)
    if f >= fo and f < md: paste_c(c, txt('SEM FORÇA', 80, 5), 600, 420, back(ramp(f, fo, fo + 8)))
    if f >= md: paste_c(c, txt('NEM UM FURO!', 72, 5), 600, 420, back(ramp(f, md, md + 8)))
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(640, 620, t), 1000, lerp(1.2, 1.3, t), lerp(0, -2, t)), 'golden'


def s5(f):
    c = mata('dusk').copy()
    tx = tronco_x(420, 900)
    tronco(c, tx)
    p0 = wt(5, 'pequeno') - 3
    n0 = wt(5, 'nosso') - 3
    put_pp(c, 420, 1500, 900, f, 5, xray=1 if f >= p0 - 6 else 0, look=1, expr='calm')
    if f >= p0: paste_c(c, txt('PEQUENINO', 70, -5), 480, 520, back(ramp(f, p0, p0 + 8)))
    if f >= n0:
        s = back(ramp(f, n0, n0 + 9))
        paste_c(c, cerebro(330), 870, 760, s)
        paste_c(c, txt('O NOSSO', 72, 5), 870, 990, s)
    t = smooth(ramp(f, 0, 60)); t2 = smooth(ramp(f, n0 - 10, n0 + 10))
    return c, (lerp(lerp(560, 540, t), 680, t2), lerp(1000, 960, t2), lerp(lerp(1.3, 1.4, t), 1.18, t2), 0), 'dusk'


def s6(f):
    c = mata('golden').copy()
    tx = tronco_x(X_PP, H_PP)
    tronco(c, tx)
    k0 = wt(6, 'capacete') - 3
    d0 = wt(6, 'dura') - 3
    p0 = wt(6, 'pequeno', 0) - 3
    furo(c, tx + 40, head_y(1500, H_PP), 60)
    pk = bater(f, d0, 10 ** 6, 4)
    put_pp(c, X_PP, 1500, H_PP, f, 6, peck=pk, xray=1 if f >= p0 else 0, expr='smug', look=1)
    if pk: lascas(c, tx + 10, head_y(1500, H_PP), (f - d0) % 12)
    if f >= k0 and f < d0: paste_c(c, txt('SEM CAPACETE', 70, -5), 620, 420, back(ramp(f, k0, k0 + 8)))
    if f >= d0 and f < p0: paste_c(c, txt('CABEÇA DURA', 76, 5), 620, 420, back(ramp(f, d0, d0 + 8)))
    if f >= p0: paste_c(c, txt('CÉREBRO PEQUENO', 60, -4), 620, 420, back(ramp(f, p0, p0 + 8)))
    t = easeOut(ramp(f, 0, 80))
    return c, (lerp(640, 620, t), lerp(1050, 1000, t), lerp(1.15, 1.3, t), lerp(0, 2.5, t)), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
