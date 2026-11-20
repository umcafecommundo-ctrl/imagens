"""Formato DESENHO: por que o ouvido entope no avião (Curiosidades da IA, 20/11/2026, 12h).
Categoria: CORPO HUMANO.
Fatos: Mayo Clinic, "Airplane ear" (atrás do tímpano fica o ouvido médio, um espaço com ar; a tuba auditiva liga o
ouvido médio ao fundo da garganta/nariz; na subida e na descida a pressão do ar da cabine muda rápido e a tuba não
equilibra a tempo; o tímpano é empurrado/esticado e a audição fica abafada; engolir e bocejar abrem a tuba e equilibram a
pressão, com o 'pop'). Popular Science, TIME e Mental Floss ("Why do our ears pop when we ride airplanes"): a tuba fica
normalmente fechada e se abre ao engolir ou bocejar; o estalo é o ar passando e igualando a pressão.
Cenários: s0 cabine do avião (Professor com o ouvido entupido) | s1 avião subindo sobre a cidade | s2-s4 dentro do corpo:
ouvido em corte (canal, tímpano, ouvido médio com ar, tuba até a garganta) | s5 cabine (Professor boceja: PLÓC) |
s6 cabine ao entardecer (Professor: manutenção)."""
from kit import *
import kit, os, importlib.util
from functools import lru_cache

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_cab = _load('h1121', '2026-11-11-21h')
cabine = _cab.cabine

LINES = [
    "O ouvido entope no avião por causa de uma salinha de ar escondida atrás do tímpano.",
    "Quando o avião sobe ou desce, a pressão do ar da cabine muda.",
    "Mas o ar preso dentro do ouvido continua igual, e o tímpano é empurrado.",
    "Ele fica esticado, e tudo parece abafado.",
    "Você vê, existe um canudinho que liga o ouvido à garganta, e ele vive fechado.",
    "Quando você engole ou boceja, ele abre, o ar passa... e faz plóc.",
    "Ou seja: no avião, bocejar não é falta de educação. É manutenção.",
]
CAPTXT = [
    "O ouvido entope no avião por causa de uma salinha|de ar escondida atrás do tímpano.",
    "Quando o avião sobe ou desce,|a pressão do ar da cabine muda.",
    "Mas o ar preso dentro do ouvido continua igual,|e o tímpano é empurrado.",
    "Ele fica esticado, e tudo parece abafado.",
    "Você vê, existe um canudinho que liga o ouvido|à garganta, e ele vive fechado.",
    "Quando você engole ou boceja, ele abre,|o ar passa... e faz plóc.",
    "Ou seja: no avião, bocejar não é falta de educação.|É manutenção.",
]
FALA_TIKTOK = "Seu ouvido já entupiu no avião? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 4
FLASH = []
CHECK = [(0, 'entope', 4), (0, 'timpano', 6), (1, 'pressao', 6), (2, 'empurrado', 6), (3, 'abafado', 6),
         (4, 'canudinho', 6), (4, 'fechado', 6), (5, 'boceja', 6), (5, 'ploc', 4), (6, 'manutencao', 8)]

SKIN = (245, 201, 160, 255); SKIND = (217, 167, 124, 255); INKA = INK + (255,)
PINK = (255, 150, 140, 255); AIR = (190, 228, 255, 255)


def SFX(s):
    s.thunk(s.W(0, 'entope') - 2, 220, .5); s.ting(s.W(0, 'timpano'), .3)
    s.whoosh(s.W(1, 'sobe') - 6, .8, .5); s.whoosh(s.W(1, 'desce') - 4, .6, .4)
    s.thunk(s.W(1, 'pressao') - 2, 150, .7)
    s.thunk(s.W(2, 'empurrado') - 2, 180, .8)
    s.thunk(s.W(3, 'esticado') - 2, 260, .5)
    s.thunk(s.W(4, 'canudinho') - 2, 300, .4); s.thunk(s.W(4, 'fechado') - 2, 140, .6)
    s.whoosh(s.W(5, 'boceja') - 6, .6, .4)
    s.thunk(s.W(5, 'ploc') - 1, 420, 1.0); s.ting(s.W(5, 'ploc') + 3, .3)
    s.trill(s.W(6, 'manutencao'), 1.0, .3)


def ouvido(c, f, bulge=0.0, tube=0.0, hl_tube=0.0, flow=None):
    """ouvido em corte. bulge: -1..1 tímpano curvado (+ = para fora/esquerda); tube 0 fechado..1 aberto."""
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0))
    _ouvido(lay, f, bulge, tube, hl_tube, flow)
    im = lay.crop((0, 620, 1200, 1600))
    im = im.resize((int(1200 * .64), int(980 * .64)), Image.LANCZOS)
    c.alpha_composite(im, (621 - im.width // 2, 1060 - im.height // 2))


OX = lambda x: 621 - 384 + x * .64
OY = lambda y: 1060 - 314 + (y - 620) * .64


def _ouvido(c, f, bulge=0.0, tube=0.0, hl_tube=0.0, flow=None):
    d = ImageDraw.Draw(c)
    # canal do ouvido (da orelha até o tímpano)
    d.rounded_rectangle((40, 800, 560, 1000), 40, fill=SKIND, outline=INKA, width=7)
    d.rectangle((60, 830, 560, 970), fill=(250, 225, 200, 255))
    # orelha na ponta
    d.ellipse((-60, 640, 120, 1160), fill=SKIN, outline=INKA, width=7)
    d.ellipse((10, 830, 90, 970), fill=(200, 140, 110, 255))
    # tuba auditiva (canudinho) até a garganta
    w = 10 + 34 * tube
    pts = [(760, 1030), (820, 1200), (900, 1380)]
    col = (255, 210, 80, 255) if hl_tube > .5 else SKIND
    d.line(pts, fill=INKA, width=int(w + 18), joint='curve')
    d.line(pts, fill=col, width=int(w + 4), joint='curve')
    if tube > .3: d.line(pts, fill=AIR, width=int(w - 6), joint='curve')
    # garganta
    d.rounded_rectangle((820, 1360, 1180, 1560), 70, fill=PINK, outline=INKA, width=7)
    # ouvido médio (a salinha de ar)
    d.ellipse((560, 760, 900, 1050), fill=AIR, outline=INKA, width=7)
    # tímpano (membrana curvada)
    bx = 560 - 130 * bulge
    tp = [(560, 800), (bx, 900), (560, 1000)]
    n = 24
    curve = [((1 - t) ** 2 * tp[0][0] + 2 * (1 - t) * t * tp[1][0] + t * t * tp[2][0],
              (1 - t) ** 2 * tp[0][1] + 2 * (1 - t) * t * tp[1][1] + t * t * tp[2][1]) for t in [i / n for i in range(n + 1)]]
    d.line(curve, fill=INKA, width=22, joint='curve'); d.line(curve, fill=(255, 120, 120, 255), width=12, joint='curve')
    # bolinhas de ar passando pelo canudinho
    if flow is not None:
        for i in range(5):
            t = ((flow * .05 + i * .2) % 1)
            x = lerp(900, 760, t) if t < 1 else 760; y = lerp(1380, 1030, t)
            d.ellipse((x - 14, y - 14, x + 14, y + 14), fill=(255, 255, 255, 255), outline=INKA, width=4)


def aviao_img(w):
    return _aviao(int(w // 8 * 8))


@lru_cache(maxsize=4)
def _aviao(w):
    p = Pen(900, 400)
    p.shape([(60, 120), (140, 30), (210, 30), (230, 170)], hexc('#2f6fb3'), hexc('#24568c'), 6, 8)  # cauda
    p.shape(ell_pts(440, 210, 390, 85, 50), (250, 250, 252), hexc('#d6dbe2'), 7, 16)
    p.shape([(380, 230), (520, 230), (420, 380), (330, 380)], hexc('#c9d2dc'), hexc('#9aa6b4'), 6, 8)  # asa
    for x in range(260, 720, 55):
        p.dot(x, 185, 13, hexc('#5aa0e6'), 4)
    p.shape([(760, 160), (830, 200), (760, 210)], hexc('#5aa0e6'), None, 4)
    return p.img.resize((w, int(w * 400 / 900)), Image.LANCZOS)


def s0(f):
    c = cabine('day').copy()
    e_ = wt(0, 'entope') - 3
    t_ = wt(0, 'timpano') - 3
    put_prof(c, 621, 1900, 1050, f, expr='pained' if f >= e_ else 'neutral', arms='chin' if f >= e_ else 'hang', look=-1)
    if e_ <= f < t_: paste_c(c, txt('ENTUPIU!', 110, -6), 640, 560, back(ramp(f, e_, e_ + 8)))
    if f >= t_:
        r = 60 * back(ramp(f, t_, t_ + 8))
        d = ImageDraw.Draw(c)
        if r > 2: d.ellipse((530 - r, 1000 - r, 530 + r, 1000 + r), outline=(255, 210, 60, 255), width=10)
        paste_c(c, txt('TÍMPANO', 100, 5), 640, 560, back(ramp(f, t_, t_ + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1200 + kick(f, e_, .8) * 12, z, 0), 'day'


def s1(f):
    c = CEN('cidade', 'day').copy()
    s_ = wt(1, 'sobe') - 3
    de = wt(1, 'desce') - 3
    p_ = wt(1, 'pressao') - 3
    t = ramp(f, 0, 200)
    x = lerp(150, 1050, t)
    up = smooth(ramp(f, s_ - 10, de))
    dn = smooth(ramp(f, de, de + 40))
    y = 1150 - 500 * up + 300 * dn
    ang = 12 * (ramp(f, s_ - 10, s_) - ramp(f, de - 4, de + 4)) - 8 * ramp(f, de, de + 10)
    im = aviao_img(520).rotate(ang, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)
    if f >= p_: paste_c(c, txt('PRESSÃO MUDA!', 100, -4), 640, 520, back(ramp(f, p_, p_ + 8)))
    z = 1.05 * (1 + .0009 * f)
    return c, (lerp(560, 700, t), 1050, z, 0), 'day'


def s2(f):
    c = CEN('corpo', 'day').copy()
    a_ = wt(2, 'ar') - 3
    e_ = wt(2, 'empurrado') - 3
    b = .9 * back(ramp(f, e_, e_ + 10))
    ouvido(c, f, bulge=b)
    if f >= a_: paste_c(c, txt('AR', 100, 0), OX(730), OY(905), back(ramp(f, a_, a_ + 8)))
    if f >= e_: paste_c(c, txt('EMPURRA!', 96, -5), 560, 600, back(ramp(f, e_, e_ + 8)))
    z = lerp(1.0, 1.25, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (lerp(621, 600, smooth(ramp(f, 0, 80))), 1080 + kick(f, e_, .8) * 10, z, 0), 'day'


def s3(f):
    c = CEN('corpo', 'day').copy()
    es = wt(3, 'esticado') - 3
    ab = wt(3, 'abafado') - 3
    wob = .06 * math.sin(f * .6)
    ouvido(c, f, bulge=.9 + wob)
    if es <= f < ab: paste_c(c, txt('ESTICADO!', 104, 5), 560, 600, back(ramp(f, es, es + 8)))
    if f >= ab:
        im = txt('BLÁ blá blá...', 80, -3)
        paste_c(c, im, 600, 600, .9 * back(ramp(f, ab, ab + 8)))
        ImageDraw.Draw(c)
    z = lerp(1.25, 1.12, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (600, 1060, z, 2 * math.sin(f * .05)), 'day'


def s4(f):
    c = CEN('corpo', 'dusk').copy()
    k = wt(4, 'canudinho') - 3
    fe = wt(4, 'fechado') - 3
    hl = 1 if f >= k else 0
    ouvido(c, f, bulge=.6, tube=0, hl_tube=hl)
    if k <= f < fe: paste_c(c, txt('CANUDINHO', 100, -4), 640, 600, back(ramp(f, k, k + 8)))
    if f >= fe: paste_c(c, txt('FECHADO!', 110, 5), 640, 600, back(ramp(f, fe, fe + 8)))
    g = wt(4, 'garganta') - 3
    if f >= g: paste_c(c, txt('GARGANTA', 56, 0), OX(1000), OY(1460), back(ramp(f, g, g + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (lerp(621, 660, t), lerp(1060, 1120, t), z, 0), 'dusk'


def s5(f):
    c = cabine('day').copy()
    en = wt(5, 'engole') - 3
    bo = wt(5, 'boceja') - 3
    pl = wt(5, 'ploc') - 2
    yawn = bo <= f < pl
    put_prof(c, 621, 1900, 1050, f, expr='shock' if yawn else ('grin' if f >= pl else 'neutral'),
             arms='up' if yawn else ('shrug' if f >= pl else 'chin'), look=-1 if f < pl else 1)
    if en <= f < bo: paste_c(c, txt('GLUP', 96, -5), 900, 760, back(ramp(f, en, en + 8)))
    if yawn: paste_c(c, txt('AAAHHH...', 96, 5), 640, 560, back(ramp(f, bo, bo + 8)))
    if f >= pl: paste_c(c, txt('PLÓC!', 150, -6), 640, 560, back(ramp(f, pl, pl + 6)))
    rings(c, 530, 1000, f, pl, 24, .9)
    z = lerp(1.05, 1.2, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (621, 1200 + kick(f, pl, 1.0) * 14, z, 0), 'day'


def s6(f):
    c = cabine('dusk').copy()
    ed = wt(6, 'educacao') - 3
    mn = wt(6, 'manutencao') - 3
    yawn = f < ed
    put_prof(c, 621, 1900, 1050, f, expr='shock' if yawn else ('smug' if f < mn else 'grin'),
             arms='up' if yawn else ('wave' if f < mn else 'shrug'), look=1)
    if f >= mn: paste_c(c, txt('MANUTENÇÃO!', 90, -4), 630, 660, back(ramp(f, mn, mn + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (621, 1200 + kick(f, mn, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
