"""Formato DESENHO: por que o pão fica duro (Curiosidades da IA, 07/11/2026, 18h). Categoria: CIÊNCIA DO DIA A DIA.
Fatos: Don Mercer, "The Complexities of Bread Staling" (IUFoST): endurecer não é principalmente secar; ao assar, o amido
gelatiniza (começa por volta de 60-65 °C) e, quando o pão esfria, as moléculas de amido se realinham numa estrutura
cristalina ('retrogradação'); pão na geladeira endurece mais rápido que fora dela; esquentar/torrar dá energia que solta
os cristais e amacia o pão; congelar a -20 °C quase para o processo; guardar fechado só evita perder umidade.
Também: Eat Your Books (2023) e Milling & Grain, "Baking technology: staling" (geladeira acelera o envelhecimento)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10', '2026-11-06-10h')
cor = _h10.cor

LINES = [
    "O pão não fica duro porque seca.",
    "Mesmo guardado num saco bem fechado, no dia seguinte ele já está duro.",
    "O culpado é o amido: quando o pão assa, ele vira um gel macio.",
    "Mas quando o pão esfria, o amido volta a se arrumar em cristais duros, bem apertadinhos.",
    "E na geladeira isso acontece ainda mais rápido do que em cima da mesa.",
    "Você vê, é por isso que o pão de ontem fica macio de novo quando você esquenta: o calor desmancha os cristais.",
    "Ou seja: guardar o pão na geladeira... faz ele envelhecer mais rápido.",
]
CAPTXT = [
    "O pão não fica duro porque seca.",
    "Mesmo guardado num saco bem fechado,|no dia seguinte ele já está duro.",
    "O culpado é o amido:|quando o pão assa, ele vira um gel macio.",
    "Mas quando o pão esfria, o amido volta a se arrumar|em cristais duros, bem apertadinhos.",
    "E na geladeira isso acontece ainda mais rápido|do que em cima da mesa.",
    "Você vê, é por isso que o pão de ontem fica macio de novo quando você esquenta:|o calor desmancha os cristais.",
    "Ou seja: guardar o pão na geladeira...|faz ele envelhecer mais rápido.",
]
FALA_TIKTOK = "Você guarda pão na geladeira? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [1]
CHECK = [(0, 'duro', 4), (0, 'seca', 6), (1, 'fechado', 4), (1, 'duro', 6), (2, 'amido', 4), (2, 'macio', 6),
         (3, 'esfria', 4), (3, 'cristais', 6), (4, 'geladeira', 4), (4, 'mesa', 6), (5, 'esquenta', 4), (5, 'cristais', 6),
         (6, 'geladeira', 4), (6, 'rapido', 8)]

PAO, PAOD = hexc('#e9a650'), hexc('#c07c2c')
MIOLO = hexc('#fbe7c0')


def pao(expr='calm', blink=0, look=0.4, hard=0.0, warm=0.0):
    """pão francês de lado com carinha (700x420). hard 0..1 deixa cinza/rachado; warm dá brilho."""
    p = Pen(700, 420)
    col = tuple(int(lerp(a, b, hard)) for a, b in zip(PAO, hexc('#b99a72')))
    dk = tuple(int(lerp(a, b, hard)) for a, b in zip(PAOD, hexc('#8d7350')))
    p.shape(ell_pts(350, 230, 310, 150, 64, 0, 0, 2.4), col, dk, 7, 26)
    for k in range(4):  # cortes
        x = 190 + k * 105
        p.shape(ell_pts(x, 150, 52, 18, 24, -.5), hexc('#f6cf8c') if hard < .5 else hexc('#d8c4a0'), None, 4)
    if hard > .4:
        p.stroke([(520, 300), (560, 260), (590, 290)], 5)
        p.stroke([(140, 300), (170, 330), (200, 310)], 5)
    for dx in (-60, 60):
        ex, ey = 350 + dx, 240
        if blink > .6: p.stroke([(ex - 22, ey), (ex + 22, ey)], 7)
        else:
            r = 40 if expr == 'shock' else 32
            p.dot(ex, ey, r, (255, 255, 255), 5); p.dot(ex + look * 10, ey + 2, 13, INK); p.dot(ex + look * 10 - 4, ey - 3, 4, (255, 255, 255))
            if expr in ('stiff', 'smug'):
                p.poly([(ex - r - 3, ey - r - 5), (ex + r + 3, ey - r - 5), (ex + r + 3, ey - 6), (ex - r - 3, ey - 6)], col); p.stroke([(ex - r, ey - 6), (ex + r, ey - 6)], 6)
    if expr in ('grin', 'smug'): p.arc(350, 305, 36, 18, 20, 160, 7)
    elif expr == 'shock': p.dot(350, 318, 18, hexc('#7a2e2e'), 5)
    elif expr == 'stiff': p.stroke([(322, 312), (378, 312)], 7)
    else: p.arc(350, 308, 24, 12, 20, 160, 6)
    if warm > 0:
        for i, x in enumerate((230, 350, 470)):
            p.stroke([(x, 70), (x - 14, 45), (x + 6, 20), (x - 8, -0)], 6, hexc('#ffffff'))
    return p.img


def put_pao(c, x, feet, w, f, seed=1, rot=0, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'hard' in kw: kw['hard'] = round(kw['hard'] * 6) / 6
    im = sprite('pao', tuple(sorted(kw.items())), int(w * 420 / 700), 700 / 420, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    bob = 4 * math.sin((f + seed * 7) * .12)
    put(c, im, x, feet + bob)


def saco(c, x, feet, w, front=True):
    """saco plástico transparente com nó em cima."""
    h = int(w * .75)
    p = Pen(500, 380)
    p.shape([(30, 60), (470, 60), (490, 370), (10, 370)], (225, 240, 255), None, 5)
    p.stroke([(220, 60), (250, 10), (280, 60)], 7)
    im = p.img.resize((w, h), Image.LANCZOS)
    a = np.asarray(im).copy(); a[..., 3] = (a[..., 3] * .45).astype(np.uint8)
    c.alpha_composite(Image.fromarray(a), (int(x - w / 2), int(feet - h + 10)))


def put_amido(c, x, y, size, f, seed, expr='calm', look=0.0):
    put_sprite(c, 'cor', x, y + size / 2, size, 1.0, False, None, col=hexc('#fff3d6'), expr=expr,
               blink=1 if blinkAt(f, seed) > .6 else 0, look=round(look * 2) / 2)


def amido_grupo(c, cx, cy, f, crystal, size=150, n=9, seed=0, expr=None):
    """bolinhas de amido: soltas e dançando (gel) -> em grade apertada (cristal)."""
    rnd = random.Random(seed)
    for i in range(n):
        gx, gy = cx + ((i % 3) - 1) * size * .92, cy + ((i // 3) - 1) * size * .92
        fx = cx + rnd.uniform(-340, 340) + 40 * math.sin(f * .07 + i)
        fy = cy + rnd.uniform(-260, 260) + 40 * math.cos(f * .06 + i * 1.3)
        x, y = lerp(fx, gx, crystal), lerp(fy, gy, crystal)
        e = expr or ('stiff' if crystal > .8 else 'grin')
        put_amido(c, x, y - size / 2, size, f, seed + i, expr='calm' if e == 'stiff' else e, look=0)
        if crystal > .8:
            p = Pen(10, 10)
    if crystal > .8:
        p = Pen(int(size * 3), int(size * 3))
        for k in range(4):
            v = k * size * .92 + 4
            p.stroke([(v, 0), (v, size * 3)], 5, hexc('#9fd3ff')); p.stroke([(0, v), (size * 3, v)], 5, hexc('#9fd3ff'))
        im = p.img.resize((int(size * 3), int(size * 3)), Image.LANCZOS)
        a = np.asarray(im).copy(); a[..., 3] = (a[..., 3] * .6 * ramp(crystal, .8, 1)).astype(np.uint8)
        c.alpha_composite(Image.fromarray(a), (int(cx - size * 1.38 - 4), int(cy - size * 1.38 - size / 2 - 4)))


def lupa(c, x, y, r, fn, s=1.0):
    """círculo de lupa: desenha fn(canvas) num disco recortado."""
    if s <= .02: return
    R = int(r * s)
    sub = Image.new('RGBA', (BW, BH), hexc('#fbe7c0') + (255,))
    fn(sub)
    sub = sub.crop((int(x - R), int(y - R), int(x + R), int(y + R)))
    m = Image.new('L', sub.size, 0); ImageDraw.Draw(m).ellipse([0, 0, 2 * R - 1, 2 * R - 1], fill=255)
    p = Pen(2 * R + 60, 2 * R + 60)
    p.dot(R + 30, R + 30, R + 18, hexc('#5b5f6b'), 6)
    p.line([(R + 30 + R * .75, R + 30 + R * .75), (2 * R + 50, 2 * R + 50)], hexc('#5b5f6b'), 30, 6)
    ring = p.img.resize((2 * R + 60, 2 * R + 60), Image.LANCZOS)
    c.alpha_composite(ring, (int(x - R - 30), int(y - R - 30)))
    c.paste(sub, (int(x - R), int(y - R)), m)


@lru_cache(maxsize=4)
def coz(luz='day'):
    return CEN('cozinha', luz)


def balcao_pao(c, x, y, f, w=620, **kw):
    put_pao(c, x, y, w, f, **kw)


def SFX(s):
    s.thunk(s.W(0, 'duro') - 2, 180, .7)
    s.ting(s.W(0, 'seca'), .3)
    s.whoosh(s.W(1, 'fechado') - 6, .4, .4)
    s.thunk(s.W(1, 'duro') - 2, 260, .8)
    s.ting(s.W(2, 'amido'), .3)
    s.patter(s.W(2, 'macio'), s.W(2, 'macio') + 20, 10, .12)
    for i in range(6): s.thunk(s.W(3, 'cristais') - 2 + i * 3, 400, .3)
    s.thunk(s.W(4, 'geladeira') - 2, 120, .7)
    s.whoosh(s.W(5, 'esquenta') - 6, .5, .4)
    s.ting(s.W(5, 'cristais'), .3)
    s.trill(s.W(6, 'rapido'), .9, .3)


# ---------------------------------------------------------------- cenas: tudo na cozinha (onde o pão fica)
# s0 cozinha (pão no balcão) | s1 cozinha (pão no saco, dia seguinte) | s2 cozinha (lupa no miolo: gel macio, fogão quente)
# s3 cozinha (lupa: cristais) | s4 cozinha (geladeira x mesa) | s5 cozinha (pão esquentando no fogão) | s6 cozinha (geladeira)
TOP = 1300   # altura do balcão no cenário cozinha (y do tampo)


def geladeira_aberta(c, cold=1.0):
    """abre a porta de baixo da geladeira do cenário (x≈950-1190) e mostra a prateleira."""
    p = Pen(300, 620)
    p.shape([(10, 10), (250, 10), (250, 600), (10, 600)], hexc('#dff3ff'), hexc('#bfe0f2'), 5, 10)
    for y in (200, 400): p.stroke([(20, y), (240, y)], 8, hexc('#9fbfd2'))
    p.shape([(250, 0), (295, 30), (295, 590), (250, 610)], hexc('#e8ecef'), hexc('#c4cbd1'), 5, 6)
    c.alpha_composite(p.img.resize((300, 620), Image.LANCZOS), (945, 990))


def s0(f):
    c = coz('day').copy()
    d0 = wt(0, 'duro') - 3
    s0_ = wt(0, 'seca') - 3
    put_pao(c, 560, TOP + 20, 700, f, 1, hard=easeOut(ramp(f, d0, d0 + 8)), expr='stiff' if f >= d0 else 'grin', look=.4)
    if d0 <= f < s0_: paste_c(c, txt('DURO!', 120, -5), 560, 800, back(ramp(f, d0, d0 + 6)))
    if f >= s0_: paste_c(c, txt('SECOU? NÃO!', 100, 5), 580, 800, back(ramp(f, s0_, s0_ + 8)))
    kk = kick(f, d0 + 2)
    t = easeOut(ramp(f, 0, 40))
    return c, (lerp(560, 600, t), 1100 + kk * 10, lerp(1.6, 1.25, t), kk), 'day'


def s1(f):
    c = coz('golden').copy()
    fe = wt(1, 'fechado') - 3
    du = wt(1, 'duro') - 3
    put_pao(c, 560, TOP + 20, 620, f, 2, hard=easeOut(ramp(f, du, du + 10)), expr='stiff' if f >= du else 'calm', look=.3)
    saco(c, 560, TOP + 30, 720)
    if f >= fe and f < du: paste_c(c, txt('BEM FECHADO', 90, -5), 560, 800, back(ramp(f, fe, fe + 8)))
    if f >= du:
        paste_c(c, txt('NO OUTRO DIA:', 76, 5), 560, 760, back(ramp(f, du - 8, du)))
        paste_c(c, txt('DURO!', 110, -4), 560, 900, back(ramp(f, du, du + 8)))
    t = smooth(ramp(f, 0, 100))
    return c, (560, 1100, lerp(1.25, 1.4, t), 0), 'golden'


def s2(f):
    c = coz('day').copy()
    a0 = wt(2, 'amido') - 3
    m0 = wt(2, 'macio') - 3
    put_pao(c, 380, TOP + 20, 560, f, 3, expr='grin', warm=1, look=1)
    lupa(c, 780, 700, 260, lambda sub: amido_grupo(sub, 780, 760, f, 0.0, 105, 7, 1), back(ramp(f, a0 - 4, a0 + 6)))
    if f >= a0: paste_c(c, txt('AMIDO', 100, -5), 640, 330, back(ramp(f, a0, a0 + 8)))
    if f >= m0: paste_c(c, txt('GEL MACIO', 90, 5), 780, 1080, back(ramp(f, m0, m0 + 8)))
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(560, 640, t), 1000, lerp(1.25, 1.2, t), 0), 'day'


def s3(f):
    c = coz('golden').copy()
    e0 = wt(3, 'esfria') - 3
    k0 = wt(3, 'cristais') - 3
    put_pao(c, 380, TOP + 20, 560, f, 3, expr='stiff' if f >= k0 else 'calm', hard=easeOut(ramp(f, k0, k0 + 10)), look=1)
    cr = easeOut(ramp(f, e0, k0 + 4))
    lupa(c, 780, 700, 260, lambda sub: amido_grupo(sub, 780, 760, f, cr, 105, 9, 1, expr='calm' if cr < .8 else None), 1.0)
    if f >= e0 and f < k0: paste_c(c, txt('ESFRIOU...', 90, -5), 640, 330, back(ramp(f, e0, e0 + 8)))
    if f >= k0: paste_c(c, txt('CRISTAIS!', 110, 5), 640, 330, back(ramp(f, k0, k0 + 8)))
    t = smooth(ramp(f, 0, 100))
    return c, (640, 1000, lerp(1.2, 1.3, t), 0), 'golden'


def s4(f):
    c = coz('day').copy()
    g0 = wt(4, 'geladeira') - 3
    m0 = wt(4, 'mesa') - 3
    # geladeira do cenário fica à direita (x≈1000); um pão perto dela, outro no balcão
    put_pao(c, 360, TOP + 20, 440, f, 4, expr='calm' if f < m0 else 'grin', hard=.0, look=1)
    geladeira_aberta(c)
    put_pao(c, 1075, 1395, 230, f, 5, expr='shock' if f >= g0 else 'calm', hard=easeOut(ramp(f, g0, g0 + 30)), look=-1)
    if f >= g0:
        p = Pen(200, 200)
        for k in range(3):
            a = k * math.pi / 3
            p.stroke([(100 - 80 * math.cos(a), 100 - 80 * math.sin(a)), (100 + 80 * math.cos(a), 100 + 80 * math.sin(a))], 10, hexc('#9fd3ff'))
        for k in range(3):
            paste_c(c, p.img.resize((120, 120), Image.LANCZOS), 1000 + k * 80, 1060 - 20 * math.sin(f * .1 + k))
        paste_c(c, txt('MAIS RÁPIDO!', 84, -5), 700, 700, back(ramp(f, g0, g0 + 8)))
    if f >= m0: paste_c(c, txt('MESA', 90, 5), 420, 1000, back(ramp(f, m0, m0 + 8)))
    t = smooth(ramp(f, 0, 100))
    return c, (lerp(760, 660, t), 1150, lerp(1.35, 1.15, t), 0), 'day'


def s5(f):
    c = coz('dusk').copy()
    e0 = wt(5, 'esquenta') - 3
    k0 = wt(5, 'cristais') - 3
    hot = easeOut(ramp(f, e0, e0 + 20))
    put_pao(c, 660, TOP + 20, 480, f, 6, expr='grin' if f >= e0 else 'stiff', hard=1 - hot, warm=1 if f >= e0 else 0, look=1)
    cr = 1 - easeOut(ramp(f, k0 - 6, k0 + 14))
    lupa(c, 780, 700, 260, lambda sub: amido_grupo(sub, 780, 760, f, cr, 105, 9, 2, expr='grin' if cr < .8 else 'calm'), 1.0)
    if f >= e0 and f < k0: paste_c(c, txt('CALOR!', 110, -5), 640, 330, back(ramp(f, e0, e0 + 8)))
    if f >= k0: paste_c(c, txt('MACIO DE NOVO', 76, 5), 640, 330, back(ramp(f, k0, k0 + 8)))
    t = smooth(ramp(f, 0, 120))
    return c, (640, 1000, lerp(1.2, 1.3, t), lerp(0, -2, t)), 'dusk'


def s6(f):
    c = coz('golden').copy()
    g0 = wt(6, 'geladeira') - 3
    r0 = wt(6, 'rapido') - 3
    geladeira_aberta(c)
    put_pao(c, 1075, 1395, 230, f, 7, expr='smug' if f < r0 else 'shock', hard=easeOut(ramp(f, r0 - 10, r0 + 6)), look=-1)
    if f >= g0 and f < r0: paste_c(c, txt('GELADEIRA', 76, -5), 880, 800, back(ramp(f, g0, g0 + 8)))
    if f >= r0: paste_c(c, txt('ENVELHECEU!', 72, 5), 880, 800, back(ramp(f, r0, r0 + 8)))
    t = easeOut(ramp(f, 0, 80))
    return c, (lerp(900, 960, t), 1150, lerp(1.4, 1.7, t), lerp(0, 2.5, t)), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
