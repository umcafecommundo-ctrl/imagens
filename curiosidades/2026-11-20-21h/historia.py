"""Formato DESENHO: por que a pimenta arde (Curiosidades da IA, 20/11/2026, 21h).
Categoria: CIÊNCIA DO DIA A DIA.
Fatos: The Conversation (2024), "Why doesn't water help with spicy food? What about milk or beer?": a capsaicina da
pimenta se liga ao receptor TRPV1 da boca, o sensor que normalmente detecta calor que queima; o cérebro recebe o sinal de
queimadura sem calor de verdade; a capsaicina não se dissolve em água (é oleosa), então a água quase não ajuda e ainda
espalha; o leite ajuda mais (a caseína e a gordura 'pegam' a capsaicina). Britannica, "The science behind spicy foods" e
Psychology Today, "Why does drinking milk ease the pain of eating spicy food?" (mesmo mecanismo).
Cenários: s0 cozinha (Professor come a pimenta) | s1 dentro do corpo: a língua com sensores | s2 dentro do corpo:
gotinhas da pimenta acendem os sensores, termômetro normal | s3 cozinha (água não resolve, leite sim) |
s4 cozinha ao entardecer (Professor com o leite: incêndio que nunca existiu)."""
from kit import *
import kit, os, importlib.util
from functools import lru_cache

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1007p', '2026-11-10-07h')
termo = _m.termo

LINES = [
    "A pimenta não é quente. Ela engana o seu cérebro.",
    "Na língua, tem sensores que avisam quando algo está queimando.",
    "A substância da pimenta liga esses sensores, sem calor nenhum.",
    "Você vê, a água quase não ajuda, porque essa substância não se mistura com água. O leite ajuda bem mais.",
    "Ou seja: o leite apaga um incêndio que nunca existiu.",
]
CAPTXT = [
    "A pimenta não é quente. Ela engana o seu cérebro.",
    "Na língua, tem sensores que avisam|quando algo está queimando.",
    "A substância da pimenta liga esses sensores,|sem calor nenhum.",
    "Você vê, a água quase não ajuda, porque essa substância|não se mistura com água. O leite ajuda bem mais.",
    "Ou seja: o leite apaga um incêndio que nunca existiu.",
]
FALA_TIKTOK = "Você aguenta pimenta? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'quente', 4), (0, 'cerebro', 6), (1, 'sensores', 6), (1, 'queimando', 6), (2, 'liga', 6),
         (2, 'nenhum', 6), (3, 'agua', 4), (3, 'leite', 6), (4, 'existiu', 8)]

PIM = hexc('#e2362f'); PIMD = hexc('#a8231e'); TALO = hexc('#3f9a3a'); TALOD = hexc('#2b6e27')
TONG = (240, 120, 130, 255); TONGD = (200, 85, 100, 255); INKA = INK + (255,)


def SFX(s):
    s.thunk(s.W(0, 'pimenta') - 2, 300, .5)
    s.whoosh(s.W(0, 'quente') - 4, .5, .5); s.ting(s.W(0, 'cerebro'), .3)
    for i in range(4): s.ting(s.W(1, 'sensores') + i * 4, .15)
    s.thunk(s.W(1, 'queimando') - 2, 150, .7)
    s.patter(s.W(2, 'liga'), s.W(2, 'liga') + 30, 12, .12)
    s.ting(s.W(2, 'nenhum'), .3)
    s.splash(s.W(3, 'agua') - 3, .4)
    s.thunk(s.W(3, 'leite') - 2, 260, .5)
    s.trill(s.W(4, 'existiu'), 1.0, .3)


@lru_cache(maxsize=8)
def pimenta_img(h, expr='calm'):
    p = Pen(300, 700)
    body = [(150, 160)] + [(150 + 70 * math.sin(math.pi * t) * (1 - .6 * t) + 30 * t, 160 + 500 * t) for t in np.linspace(0, 1, 20)] + \
           [(150 - 70 * math.sin(math.pi * t) * (1 - .6 * t) + 30 * t, 160 + 500 * t) for t in np.linspace(1, 0, 20)]
    p.shape(body, PIM, PIMD, 6, 14)
    p.shape([(110, 170), (190, 170), (170, 120), (130, 120)], TALO, TALOD, 5, 4)
    p.line([(150, 125), (160, 70), (190, 40)], TALOD, 12, 4)
    # carinha
    for dx in (-28, 28):
        p.dot(150 + dx, 300, 20, (255, 255, 255), 4); p.dot(154 + dx, 302, 8, INK)
    if expr == 'smug':
        p.stroke([(110, 285), (190, 285)], 6)
    p.arc(150, 345, 26, 14, 20, 160, 5)
    return p.img.resize((max(4, int(h * 300 / 700)), max(4, h)), Image.LANCZOS)


def put_pim(c, x, y, h, rot=0, expr='calm'):
    if h < 8: return
    im = pimenta_img(int(h // 4 * 4), expr)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def chamas(c, x, y, f, s=1.0):
    """labaredas saindo da boca para a direita (sem cobrir o rosto)."""
    if s <= .05: return
    d = ImageDraw.Draw(c)
    x0 = x + 55
    for i in range(3):
        a = math.radians(-25 + i * 22)
        L = (190 + 40 * math.sin(f * .7 + i * 2)) * s
        w = 30 * s
        tx, ty = x0 + L * math.cos(a), y + L * math.sin(a)
        nx, ny = -math.sin(a), math.cos(a)
        d.polygon([(x0 + nx * w, y + ny * w), (tx, ty), (x0 - nx * w, y - ny * w)], fill=(255, 140, 40, 235), outline=INKA)
        d.polygon([(x0 + nx * w * .45, y + ny * w * .45), (lerp(x0, tx, .7), lerp(y, ty, .7)), (x0 - nx * w * .45, y - ny * w * .45)], fill=(255, 220, 80, 255))


def lingua(c, f, lit=0.0, gotas=None, hot=0.0):
    """língua grande vista de cima (dentro do corpo) com sensores."""
    p = Pen(1000, 900)
    pts = [(500 + 380 * math.sin(a) * (0.75 + .25 * math.cos(a)), 120 + 700 * (1 - math.cos(a)) / 2) for a in np.linspace(-math.pi, math.pi, 50)]
    pts = [(500 + 390 * math.sin(t * math.pi) if True else 0, 0) for t in []] or \
          [(500 - 380 * math.sin(math.pi * t), 120 + 720 * t) for t in np.linspace(0, 1, 25)] + \
          [(500 + 380 * math.sin(math.pi * t), 120 + 720 * t) for t in np.linspace(1, 0, 25)]
    p.shape(pts, hexc('#f07882'), hexc('#c85564'), 7, 20)
    p.stroke([(500, 160), (500, 700)], 6, hexc('#c85564'))
    im = p.img.resize((1000, 900), Image.LANCZOS)
    c.alpha_composite(im, (121, 760))
    d = ImageDraw.Draw(c)
    rnd = random.Random(4)
    for i in range(14):
        x = rnd.randint(330, 910); y = rnd.randint(960, 1500)
        on = lit > 0 and (i / 14) <= lit
        r = 26
        if on:
            g = 50 + 10 * math.sin(f * .6 + i)
            d.ellipse((x - g, y - g, x + g, y + g), fill=(255, 210, 60, 110))
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 90, 60, 255) if on else (255, 200, 205, 255), outline=INKA, width=5)
    if gotas is not None:
        for i in range(10):
            t = clamp(gotas - i * .05)
            if t <= 0: continue
            x = 380 + (i * 61) % 520; y = lerp(700, 1000 + (i * 97) % 480, easeOut(t))
            d.ellipse((x - 18, y - 22, x + 18, y + 22), fill=(255, 180, 40, 255), outline=INKA, width=4)


@lru_cache(maxsize=4)
def copo_img(h, leite=False):
    p = Pen(300, 400)
    p.shape([(40, 30), (260, 30), (230, 390), (70, 390)], hexc('#e8f4ff'), hexc('#c4dcef'), 6, 6)
    col = hexc('#fbfbf6') if leite else hexc('#8cc8f5')
    p.shape([(52, 120), (248, 120), (228, 380), (72, 380)], col, mul(col, .9), 0, 8)
    return p.img.resize((int(h * 300 / 400), h), Image.LANCZOS)


def s0(f):
    c = CEN('cozinha', 'day').copy()
    q_ = wt(0, 'quente') - 3
    ce = wt(0, 'cerebro') - 3
    mx, my = 400, 1880 - 615
    t = ramp(f, 0, q_ - 6)
    if f < q_ - 4:
        put_pim(c, lerp(900, mx + 60, smooth(t)), lerp(900, my - 10, smooth(t)), 300, rot=lerp(0, 60, t))
    put_prof(c, 420, 1880, 1000, f, expr='pained' if f >= q_ else 'grin', arms='up' if f >= q_ else 'point', look=1)
    if f >= q_: chamas(c, mx, my - 10, f, back(ramp(f, q_, q_ + 8)))
    if q_ <= f < ce: paste_c(c, txt('ARDE!', 120, -6), 660, 700, back(ramp(f, q_, q_ + 8)))
    if f >= ce: paste_c(c, txt('ENGANADO!', 100, 5), 660, 700, back(ramp(f, ce, ce + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1200 + kick(f, q_, 1.0) * 14, z, 0), 'day'


def s1(f):
    c = CEN('corpo', 'day').copy()
    se = wt(1, 'sensores') - 3
    qu = wt(1, 'queimando') - 3
    lit = ramp(f, se, se + 12) * .0
    lingua(c, f, lit=lit)
    if f >= se:
        d = ImageDraw.Draw(c)
        rnd = random.Random(4)
        for i in range(14):
            x = rnd.randint(330, 910); y = rnd.randint(960, 1500)
            s = back(ramp(f, se + i, se + i + 6)); r = 36 * s
            if r > 2: d.ellipse((x - r, y - r, x + r, y + r), outline=(255, 210, 60, 255), width=7)
        paste_c(c, txt('SENSORES', 100, -4), 621, 660, back(ramp(f, se, se + 8)) if f < qu else 0)
    if f >= qu:
        paste_c(c, txt('ALARME DE FOGO', 88, 4), 621, 660, back(ramp(f, qu, qu + 8)))
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1150, z, 0), 'day'


def s2(f):
    c = CEN('corpo', 'dusk').copy()
    li = wt(2, 'liga') - 3
    ne = wt(2, 'nenhum') - 3
    lingua(c, f, lit=ramp(f, li, li + 15), gotas=ramp(f, 0, li + 2) * 1.5)
    if f >= li: paste_c(c, txt('ALARME!', 110, -5), 500, 640, back(ramp(f, li, li + 8)) * (1 if f < ne else 0))
    if f >= ne:
        termo(c, 960, 1180, 520 * back(ramp(f, ne, ne + 10)), .35)
        paste_c(c, txt('SEM CALOR', 100, 4), 560, 640, back(ramp(f, ne, ne + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (621, 1150 + kick(f, li, .6) * 10, z, 0), 'dusk'


def s3(f):
    c = CEN('cozinha', 'day').copy()
    ag = wt(3, 'agua') - 3
    mi = wt(3, 'mistura') - 3
    le = wt(3, 'leite') - 3
    mx, my = 400, 1880 - 615
    milk = f >= le
    paste_c(c, copo_img(260, milk), 690, 1420)
    burning = f < le + 10
    put_prof(c, 420, 1880, 1000, f, expr='pained' if burning else 'grin', arms='up' if f < le else 'shrug', look=1)
    if burning: chamas(c, mx, my - 10, f, 1.0 if f < le else 1 - ramp(f, le, le + 10))
    if ag <= f < mi: paste_c(c, txt('ÁGUA?', 110, -5), 660, 700, back(ramp(f, ag, ag + 8)))
    if mi <= f < le: paste_c(c, txt('NÃO MISTURA!', 90, 5), 660, 700, back(ramp(f, mi, mi + 8)))
    if f >= le: paste_c(c, txt('LEITE!', 120, -5), 660, 700, back(ramp(f, le, le + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    return c, (640, 1200, z, 0), 'day'


def s4(f):
    c = CEN('cozinha', 'dusk').copy()
    ap = wt(4, 'apaga') - 3
    ex = wt(4, 'existiu') - 3
    paste_c(c, copo_img(260, True), 690, 1420)
    put_pim(c, 960, 1300, 420, rot=-10, expr='smug' if f >= ex else 'calm')
    put_prof(c, 420, 1880, 1000, f, expr='grin' if f >= ex else 'smug', arms='shrug' if f >= ex else 'point', look=1)
    if ap <= f < ex: paste_c(c, txt('APAGOU?', 100, -5), 660, 620, back(ramp(f, ap, ap + 8)))
    if f >= ex: paste_c(c, txt('ALARME FALSO!', 86, 5), 650, 620, back(ramp(f, ex, ex + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (640, lerp(1250, 1200, t) + kick(f, ex, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
