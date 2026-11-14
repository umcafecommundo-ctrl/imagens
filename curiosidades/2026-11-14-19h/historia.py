"""Formato DESENHO: por que tem gente que espirra quando olha pro sol (Curiosidades da IA, 14/11/2026, 19h).
Categoria: CORPO HUMANO.
Fatos: PBS NewsHour ("Does the sun make you sneeze?") e Popular Science: o reflexo fótico do espirro atinge cerca de
10% a 35% das pessoas; pesquisadores o chamam de síndrome ACHOO (Autosomal Dominant Compelling Helio-Ophthalmic
Outburst); é herdado de forma dominante (basta um dos pais); a teoria mais aceita é que sinais "cruzam" entre o nervo
óptico (que responde à luz) e o nervo trigêmeo (que sente o rosto e o nariz), e o cérebro reage com um espirro.
Cenários: s0 praia (olha pro sol e espirra) | s1 cidade (rua com 3 pessoas, 1 espirra) | s2 lab (cientista, ACHOO) |
s3 sala (pai e filho espirram na janela ensolarada) | s4 corpo ao entardecer (nervo do olho e do nariz vizinhos) |
s5 corpo ao entardecer (cérebro: NARIZ?!) | s6 praia ao entardecer (luz entra pelo olho, sai pelo nariz)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h0810', '2026-11-08-10h')
pessoa = _m.pessoa
cerebro = _load('h0812', '2026-11-08-12h').cerebro

LINES = [
    "Tem gente que espirra só de olhar pro sol.",
    "Não é alergia: é um reflexo, e acontece com até uma em cada três pessoas.",
    "Os cientistas chamam de síndrome ACHOO, que em inglês soa igual a atchim.",
    "E passa de pai pra filho: basta um dos pais ter.",
    "Você vê, a ideia mais aceita é que o nervo do olho e o nervo que sente o nariz ficam vizinhos.",
    "A luz forte manda um sinal tão grande que ele escorrega pro nervo errado, e o cérebro entende: tem coisa no nariz!",
    "Ou seja: a luz entra pelo olho... e sai pelo nariz.",
]
CAPTXT = [
    "Tem gente que espirra só de olhar pro sol.",
    "Não é alergia: é um reflexo,|e acontece com até 1 em cada 3 pessoas.",
    "Os cientistas chamam de síndrome ACHOO,|que em inglês soa igual a atchim.",
    "E passa de pai pra filho: basta um dos pais ter.",
    "Você vê, a ideia mais aceita é que o nervo do olho|e o nervo que sente o nariz ficam vizinhos.",
    "A luz forte manda um sinal tão grande que ele escorrega pro nervo errado,|e o cérebro entende: tem coisa no nariz!",
    "Ou seja: a luz entra pelo olho...|e sai pelo nariz.",
]
FALA_TIKTOK = "Você espirra no sol? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = []
CHECK = [(0, 'sol', 4), (1, 'tres', 6), (2, 'achoo', 4), (2, 'atchim', 6), (3, 'filho', 6), (4, 'olho', 4),
         (4, 'nariz', 4), (5, 'errado', 6), (5, 'nariz', 6), (6, 'nariz', 8)]

AZ = '#2f7fd1'


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def atchim(c, x, y, f, f0, s=1.0, rot=8, flip=False):
    """espirro: palavra + gotinhas saindo para o lado."""
    a = f - f0
    if a < 0 or a > 40: return
    paste_c(c, txt('ATCHIM!', int(110 * s), rot), x, y, back(ramp(f, f0, f0 + 7)))
    d = ImageDraw.Draw(c)
    sg = -1 if flip else 1
    for i in range(9):
        t = min(1, a / 14)
        ang = (i - 4) * .12
        r = (60 + i * 22) * t * s
        px = x - sg * 60 * s + sg * r * math.cos(ang)
        py = y + 260 * s + r * math.sin(ang)
        rr = (10 - i % 3 * 2) * s
        if a < 30:
            d.ellipse((px - rr, py - rr, px + rr, py + rr), fill=(200, 232, 255, 255), outline=INK + (255,), width=3)


def sol_brilho(c, x, y, r, f):
    paste_c(c, sun_icon(int(r * 2), 1.0).rotate(f * .6, Image.BICUBIC), x, y)


@lru_cache(maxsize=4)
def olho_img(w):
    p = Pen(300, 200)
    p.shape(ell_pts(150, 100, 130, 80), hexc('#ffffff'), hexc('#dfe3e8'), 6, 6)
    p.shape(ell_pts(150, 100, 55, 55), hexc('#5aa06a'), hexc('#3f7f50'), 5, 4)
    p.dot(150, 100, 26, INK)
    p.dot(138, 88, 9, (255, 255, 255))
    return p.img.resize((w, int(w * 2 / 3)), Image.LANCZOS)


@lru_cache(maxsize=4)
def nariz_img(w):
    p = Pen(300, 300)
    sk = hexc('#f5c9a0')
    p.shape([(150, 20), (200, 200), (250, 250), (190, 280), (110, 280), (50, 250), (100, 200)], sk, mul(sk, .85), 6, 12)
    p.shape(ell_pts(115, 255, 22, 12), hexc('#7a4a3a'), None, 3, 0)
    p.shape(ell_pts(185, 255, 22, 12), hexc('#7a4a3a'), None, 3, 0)
    return p.img.resize((w, w), Image.LANCZOS)


def nervos(c, f, f_spark=None, slip=0.0):
    """dois nervos: do olho (amarelo) e do nariz (azul) correndo lado a lado até o alto."""
    d = ImageDraw.Draw(c)
    A = [(440, 900), (520, 760), (560, 600), (600, 420)]
    B = [(760, 1290), (720, 1000), (690, 760), (680, 420)]
    for pts, col in ((A, (255, 214, 90)), (B, (120, 190, 255))):
        d.line(pts, fill=INK + (255,), width=34, joint='curve')
        d.line(pts, fill=col + (255,), width=22, joint='curve')
    if f_spark is not None and 0 <= f - f_spark < 95:
        t = clamp((f - f_spark) / 80)
        path = A[:3] + ([B[2], B[1], B[0]] if slip > .5 else [A[3]])
        k = t * (len(path) - 1); i = min(len(path) - 2, int(k)); u = k - i
        q = (lerp(path[i][0], path[i + 1][0], u), lerp(path[i][1], path[i + 1][1], u))
        r = 34 + 6 * math.sin(f * .8)
        d.ellipse((q[0] - r, q[1] - r, q[0] + r, q[1] + r), fill=(255, 255, 255, 255), outline=(255, 214, 90, 255), width=8)


def SFX(s):
    s.ting(s.W(0, 'sol'), .3)
    s.thunk(s.W(0, 'espirra') + 18, 160, .7)
    s.thunk(s.W(1, 'reflexo') - 2, 220, .5)
    for i in range(3): s.thunk(s.W(1, 'tres') - 2 + i * 4, 260, .4)
    s.thunk(s.W(2, 'achoo') - 2, 180, .7)
    s.thunk(s.W(2, 'atchim') - 2, 140, .8)
    s.thunk(s.W(3, 'filho') - 2, 160, .6); s.thunk(s.W(3, 'filho') + 4, 220, .5)
    s.ting(s.W(4, 'olho'), .3); s.ting(s.W(4, 'nariz'), .3)
    s.whoosh(s.W(5, 'escorrega') - 6, .5, .5)
    s.thunk(s.W(5, 'nariz') - 2, 200, .7)
    s.thunk(s.W(6, 'nariz') - 2, 140, .9); s.trill(s.W(6, 'nariz') + 6, 1.0, .3)


def s0(f):
    c = CEN('praia', 'day').copy()
    k = wt(0, 'sol') - 3
    e = k + 22
    look_up = f >= k
    expr = 'neutral' if not look_up else ('pained' if f < e else 'shock')
    put_p(c, 520, 1780, 900, f, 3, shirt='#ff8a5c', arms='hang' if f < e else 'cheek', expr=expr, look=1, tilt=-6 if look_up else 0)
    atchim(c, 640, 860, f, e)
    z = lerp(1.3, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (680, 1250 + kick(f, e, .7) * 12, z, 0), 'day'


def s1(f):
    c = CEN('cidade', 'day').copy()
    k = wt(1, 'tres') - 3
    for i, (x, sh) in enumerate(((260, '#3fae6a'), (620, '#ff8a5c'), (980, '#e8a33c'))):
        sneeze = i == 1 and f >= k
        put_p(c, x, 1760, 760, f, 10 + i, shirt=sh, arms='cheek' if sneeze else 'hang', expr='shock' if sneeze else 'grin', look=0)
    if f >= k:
        atchim(c, 640, 860, f, k, .8)
        paste_c(c, txt('1 EM CADA 3', 90, -4), 621, 640, back(ramp(f, k, k + 8)))
    al = wt(1, 'alergia') - 3
    if al <= f < k: paste_c(c, txt('ALERGIA? NÃO!', 84, 5), 621, 640, back(ramp(f, al, al + 8)))
    z = lerp(1.02, 1.12, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1240 + kick(f, k, .6) * 10, z, 0), 'day'


def s2(f):
    c = CEN('lab', 'day').copy()
    a = wt(2, 'achoo') - 3
    t = wt(2, 'atchim') - 3
    put_sci(c, 360, 1760, 860, f, 2, arms='point' if f >= a else 'clip', bun=True, expr='grin', look=1)
    if f >= a: paste_c(c, txt('ACHOO', 140, -5), 780, 840, back(ramp(f, a, a + 8)))
    if f >= t: paste_c(c, txt('= ATCHIM!', 96, 5), 800, 1040, back(ramp(f, t, t + 8)))
    z = lerp(1.2, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1240 + kick(f, t, .6) * 10, z, 0), 'day'


def s3(f):
    c = CEN('sala', 'day').copy()
    k = wt(3, 'filho') - 3
    pa = wt(3, 'pai') - 3
    put_p(c, 380, 1780, 900, f, 4, shirt=AZ, mous=True, arms='cheek' if f >= pa else 'hang',
          expr='shock' if f >= pa else 'neutral', look=1)
    put_p(c, 820, 1780, 600, f, 5, shirt=AZ, arms='cheek' if f >= k else 'hang', expr='shock' if f >= k else 'grin', look=-1)
    atchim(c, 420, 900, f, pa, .75, 6)
    atchim(c, 860, 1080, f, k, .65, -6, True)
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (630, 1280 + kick(f, k, .6) * 10, z, 0), 'day'


def s4(f):
    c = CEN('corpo', 'dusk').copy()
    o = wt(4, 'olho') - 3
    n = wt(4, 'nariz') - 3
    v = wt(4, 'vizinhos') - 3
    if f >= v: nervos(c, f)
    po = 1 + .25 * pulse(f, o, 14)
    pn = 1 + .25 * pulse(f, n, 14)
    paste_c(c, olho_img(300), 400, 960, back(ramp(f, 0, 8)) * po)
    paste_c(c, nariz_img(320), 780, 1350, back(ramp(f, 5, 13)) * pn)
    if f < v: paste_c(c, txt('OLHO E NARIZ', 90, -4), 621, 560, back(ramp(f, 4, 12)))
    if f >= v: paste_c(c, txt('VIZINHOS!', 100, -4), 621, 560, back(ramp(f, v, v + 8)))
    t = smooth(ramp(f, 0, 120))
    z = lerp(1.15, 1.02, t) * (1 + .0009 * f)
    return c, (620, lerp(1150, 1080, t), z, lerp(0, 2, t)), 'dusk'


def s5(f):
    c = CEN('corpo', 'dusk').copy()
    fo = wt(5, 'forte') - 3
    sn = wt(5, 'sinal') - 3
    er = wt(5, 'errado') - 3
    nz = wt(5, 'nariz') - 3
    nervos(c, f, sn, 1.0)
    paste_c(c, olho_img(300), 400, 960)
    paste_c(c, nariz_img(320), 780, 1350)
    paste_c(c, cerebro(380), 640, 330)
    if fo <= f < fo + 26: paste_c(c, txt('LUZ!', 110, 6), 300, 720, back(ramp(f, fo, fo + 6)))
    if f >= er and f < nz: paste_c(c, txt('OPA!', 110, -6), 900, 720, back(ramp(f, er, er + 6)))
    if f >= nz: paste_c(c, txt('NARIZ?!', 120, -6), 640, 640, back(ramp(f, nz, nz + 8)))
    z = lerp(1.02, 1.1, smooth(ramp(f, 0, 150))) * (1 + .0009 * f)
    return c, (630, 1000 + kick(f, nz, .7) * 10, z, 0), 'dusk'


def s6(f):
    c = CEN('praia', 'dusk').copy()
    o = wt(6, 'olho') - 3
    n = wt(6, 'nariz') - 3
    put_p(c, 520, 1780, 900, f, 3, shirt='#ff8a5c', arms='cheek' if f >= n else 'hang',
          expr='shock' if f >= n else ('pained' if f >= o else 'neutral'), look=1, tilt=-6)
    if o <= f < n: paste_c(c, txt('ENTRA...', 90, 5), 820, 860, back(ramp(f, o, o + 8)))
    atchim(c, 640, 860, f, n)
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.22, t) * (1 + .0009 * f)
    return c, (660, lerp(1250, 1180, t) + kick(f, n, .7) * 12, z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
