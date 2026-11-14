"""Formato DESENHO: por que a panela de pressão cozinha mais rápido (Curiosidades da IA, 14/11/2026, 07h).
Categoria: CIÊNCIA DO DIA A DIA.
Fatos: Wikipedia "Pressure cooking" e Physics Van (Univ. de Illinois, "Pressure Cooker"): numa panela aberta a água
fervendo fica em ~100 °C ao nível do mar, e mais fogo só faz ferver mais forte; a panela de pressão prende o vapor,
a pressão interna sobe (~1 atm a mais) e a água só ferve por volta de 120 °C; mais quente, a comida cozinha bem
mais rápido (feijão em uma fração do tempo).
Cenários: s0 cozinha (panela comum, termômetro 100) | s1 cozinha (mais fogo, termômetro parado) |
s2 cozinha (panela de pressão, tampa trava, vapor) | s3 cozinha ao entardecer (vapor apertando, termômetro 120) |
s4 cozinha (feijão pronto, relógio rápido) | s5 cozinha ao entardecer (panela com carinha convencida chiando)."""
from kit import *
import kit, os, importlib.util
from art import face

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1007', '2026-11-10-07h')
put_pessoa = _m.put_pessoa
pessoa = _m.pessoa
panela, fogo, termo, seta_img = _m.panela, _m.fogo, _m.termo, _m.seta_img

LINES = [
    "Na panela comum, a água nunca passa de cem graus.",
    "Pode aumentar o fogo: ela só borbulha mais forte.",
    "A panela de pressão trava a tampa e prende o vapor.",
    "Você vê, com o vapor apertando, a água só ferve lá pelos cento e vinte graus.",
    "E mais quente, o feijão fica pronto bem mais rápido.",
    "Ou seja: o chiado é a panela se gabando.",
]
CAPTXT = [
    "Na panela comum, a água nunca passa de 100 graus.",
    "Pode aumentar o fogo: ela só borbulha mais forte.",
    "A panela de pressão trava a tampa e prende o vapor.",
    "Você vê, com o vapor apertando,|a água só ferve lá pelos 120 graus.",
    "E mais quente, o feijão fica pronto bem mais rápido.",
    "Ou seja: o chiado é a panela se gabando.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'cem', 6), (1, 'fogo', 4), (1, 'forte', 6), (2, 'trava', 4), (2, 'vapor', 6), (3, 'vinte', 6),
         (4, 'feijao', 4), (4, 'rapido', 6), (5, 'chiado', 4), (5, 'gabando', 8)]

PANELA = '#c9d0d8'; PANELA_D = '#99a3ae'; CABO = '#2d2f35'


@lru_cache(maxsize=64)
def pressao_img(w, lock=1.0, ph=0, steam=0, eyes='', blink=0):
    p = Pen(600, 640)
    # corpo
    p.shape([(110, 300), (490, 300), (475, 600), (125, 600)], hexc(PANELA), hexc(PANELA_D), 6, 22)
    # cabo de baixo (fixo, direita)
    p.shape([(480, 330), (590, 320), (590, 360), (480, 368)], hexc(CABO), None, 5, 0)
    # tampa em domo
    dome = sorted([pt for pt in ell_pts(300, 300, 205, 95, n=64) if pt[1] <= 300], key=lambda q: q[0])
    p.shape(dome, hexc('#dfe4ea'), hexc('#b3bcc6'), 6, 8)
    p.shape([(95, 292), (505, 292), (505, 318), (95, 318)], hexc('#aeb7c2'), None, 5, 0)
    # cabo da tampa: gira até travar por cima do cabo de baixo
    a = -(1 - lock) * 0.55
    ca, sa = math.cos(a), math.sin(a)
    px, py = 300, 300
    pts = [(0, -20), (290, -20), (290, 16), (0, 16)]
    p.shape([(px + x * ca - y * sa, py + x * sa + y * ca) for x, y in pts], hexc(CABO), None, 5, 0)
    # válvula (pino) que balança
    sw = 8 * math.sin(ph * 1.7) if steam else 0
    p.shape([(285, 170), (315, 170), (318, 236), (282, 236)], hexc('#6f7783'), None, 5, 0)
    p.shape(ell_pts(300 + sw, 160, 34, 26), hexc('#40444c'), None, 5, 0)
    if steam:
        for i in range(3):
            x = 300 + sw + (i - 1) * 40 + 10 * math.sin(ph + i * 2)
            p.stroke([(x, 130), (x + 25, 90), (x - 10, 50), (x + 20, 8)], 14, (255, 255, 255))
    if eyes:
        face(p, 300, 440, eyes, blink, 0.3, u=5.6)
    return p.img.resize((w, int(w * 640 / 600)), Image.LANCZOS)


def pressao(c, x, base, w, f=0, lock=1.0, steam=0, eyes='', blink=0):
    if w < 8: return
    im = pressao_img(int(w), round(lock * 10) / 10, (f // 2) % 8 if steam else 0, steam, eyes, 1 if blink > .6 else 0)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(base - im.size[1] * 600 / 640)))


@lru_cache(maxsize=4)
def prato_img(w):
    p = Pen(500, 260)
    p.shape(ell_pts(250, 150, 230, 80), hexc('#ffffff'), hexc('#d8dde3'), 6, 10)
    p.shape(ell_pts(250, 130, 160, 50), hexc('#7a3e22'), hexc('#5a2c18'), 5, 6)
    rnd = random.Random(3)
    for i in range(22):
        x = 250 + rnd.uniform(-130, 130); y = 128 + rnd.uniform(-30, 30)
        if ((x - 250) / 150) ** 2 + ((y - 130) / 46) ** 2 < 1:
            p.shape(ell_pts(x, y, 14, 9), hexc('#4a2414'), None, 3, 0)
    return p.img.resize((w, int(w * 260 / 500)), Image.LANCZOS)


def SFX(s):
    s.patter(0, 50, 10, .12)
    s.thunk(s.W(0, 'cem') - 2, 200, .6)
    s.whoosh(s.W(1, 'fogo') - 6, .4, .4)
    s.patter(s.W(1, 'borbulha'), s.W(1, 'forte') + 20, 14, .16)
    s.thunk(s.W(2, 'trava') - 2, 260, .9)
    s.whoosh(s.W(2, 'vapor') - 4, .5, .4)
    s.thunk(s.W(3, 'vinte') - 2, 160, .7); s.ting(s.W(3, 'vinte') + 2, .3)
    s.ting(s.W(4, 'pronto'), .35)
    s.whoosh(s.W(5, 'chiado') - 4, .6, .5)
    s.trill(s.W(5, 'gabando'), 1.0, .3)


def s0(f):
    c = CEN('cozinha', 'day').copy()
    fogo(c, 560, 1760, 460, f)
    panela(c, 560, 1640, 500, 1, f)
    k = wt(0, 'cem') - 3
    v = .2 + .6 * easeOut(ramp(f, 4, k))
    termo(c, 970, 1720, 720 * back(ramp(f, 0, 10)), v)
    put_pessoa(c, 270, 1760, 820, f, 3, shirt='#ff8a5c', arms='point' if f >= k else 'hang', expr='grin', look=1)
    if f >= k: paste_c(c, txt('100 GRAUS', 100, -5), 720, 880, back(ramp(f, k, k + 8)))
    z = lerp(1.35, 1.1, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1300 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('cozinha', 'day').copy()
    k = wt(1, 'fogo') - 3
    b = wt(1, 'forte') - 3
    fw = 460 + 220 * easeOut(ramp(f, k, k + 10))
    fogo(c, 560, 1760, fw, f)
    panela(c, 560, 1640, 500, 1, f // 1 if f < k else f * 2)
    termo(c, 980, 1720, 720, .8 + .01 * math.sin(f * .8))
    put_pessoa(c, 270, 1760, 820, f, 3, shirt='#ff8a5c', arms='point' if f >= k else 'hang',
               expr='grin' if f < b else 'shock', look=1)
    if k <= f < b: paste_c(c, txt('MAIS FOGO!', 100, 6), 600, 880, back(ramp(f, k, k + 8)))
    if f >= b: paste_c(c, txt('AINDA 100...', 96, -5), 640, 880, back(ramp(f, b, b + 8)))
    z = lerp(1.08, 1.22, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (640, 1320 + kick(f, k, .6) * 10, z, 0), 'day'


def s2(f):
    c = CEN('cozinha', 'day').copy()
    t = wt(2, 'trava') - 3
    v = wt(2, 'vapor') - 3
    fogo(c, 600, 1760, 460, f)
    pressao(c, 600, 1650, 560, f, lock=easeOut(ramp(f, t - 8, t)), steam=1 if f >= v else 0)
    put_pessoa(c, 220, 1760, 800, f, 3, shirt='#ff8a5c', arms='up' if f >= t else 'hang', expr='grin', look=1)
    if t <= f < v: paste_c(c, txt('TRAVOU!', 110, -6), 640, 820, back(ramp(f, t, t + 8)))
    if f >= v: paste_c(c, txt('VAPOR PRESO', 90, 5), 640, 820, back(ramp(f, v, v + 8)))
    z = lerp(1.3, 1.12, easeOut(ramp(f, 0, 30))) * (1 + .0009 * f)
    return c, (640, 1300 + kick(f, t, .8) * 12, z, 0), 'day'


def s3(f):
    c = CEN('cozinha', 'dusk').copy()
    a = wt(3, 'apertando') - 3
    k = wt(3, 'vinte') - 3
    fogo(c, 520, 1760, 480, f)
    pressao(c, 520, 1650, 580, f, steam=1)
    for i, x in enumerate((340, 520, 700)):
        s = back(ramp(f, a + i * 4, a + i * 4 + 8))
        if s > .05: paste_c(c, seta_img(200), x, 1080 + 20 * math.sin(f * .2 + i), s)
    v = .8 + .2 * easeOut(ramp(f, k - 12, k + 4))
    termo(c, 1000, 1720, 760, v)
    if f >= k: paste_c(c, txt('120 GRAUS', 110, -5), 640, 760, back(ramp(f, k, k + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.08, 1.22, t) * (1 + .0009 * f)
    return c, (640, lerp(1300, 1250, t) + kick(f, k, .7) * 10, z, lerp(0, 2, t)), 'dusk'


def s4(f):
    c = CEN('cozinha', 'day').copy()
    fj = wt(4, 'feijao') - 3
    r = wt(4, 'rapido') - 3
    fogo(c, 330, 1760, 380, f)
    pressao(c, 330, 1650, 440, f, steam=1)
    spin = ramp(f, 0, 80) * 5
    paste_c(c, clock_img(spin * 2 * math.pi / 12 * 0 + spin, spin * 12, 260), 330, 560)
    put_pessoa(c, 900, 1760, 860, f, 3, shirt='#ff8a5c', arms='up' if f >= r else 'hang',
               expr='grin', look=-1)
    if f >= fj: paste_c(c, prato_img(340), 700, 1440, back(ramp(f, fj, fj + 8)))
    if f >= r: paste_c(c, txt('PRONTO!', 120, 6), 640, 900, back(ramp(f, r, r + 8)))
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (640, 1300 + kick(f, r, .6) * 10, z, 0), 'day'


def s5(f):
    c = CEN('cozinha', 'dusk').copy()
    ch = wt(5, 'chiado') - 3
    g = wt(5, 'gabando') - 3
    fogo(c, 621, 1760, 520, f)
    pressao(c, 621, 1650, 760, f, steam=1 if f >= ch else 0, eyes='smug' if f >= g else 'neutral', blink=blinkAt(f, 4))
    if f >= ch: paste_c(c, txt('TSSSSS!', 110, -6), 621, 780, back(ramp(f, ch, ch + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.35, t) * (1 + .0012 * f)
    return c, (621, lerp(1300, 1220, t), z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
