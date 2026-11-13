"""Formato DESENHO: a primeira webcam vigiava uma cafeteira (Curiosidades da IA, 13/11/2026, 12h). Categoria: TECNOLOGIA.
Fatos: Wikipedia, "Trojan Room coffee pot": em 1991, no laboratório de computação da Universidade de Cambridge (Inglaterra),
dois pesquisadores apontaram uma câmera para a cafeteira da 'Trojan Room' e ligaram ao computador, para quem trabalhava em
outras salas não ter a decepção de ir até lá e achar a jarra vazia; imagem de 128x128 pixels em tons de cinza; em novembro
de 1993 a imagem passou a ser vista pela web (HTTP) e ficou famosa no mundo todo; desligada em 22/08/2001.
The Register (2001) e Digital Camera World: a 'primeira webcam do mundo' foi montada para vigiar uma cafeteira."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h0810', '2026-11-08-10h')
_h18 = _load('h0618', '2026-11-06-18h')
_h12 = _load('h0812', '2026-11-08-12h')
pessoa = _h10.pessoa
crt = _h18.crt


def mesa(c, y, x0=60, x1=1180):
    w = x1 - x0 + 40
    p = Pen(w, 420)
    p.shape([(20, 20), (w - 20, 20), (w - 20, 70), (20, 70)], hexc('#9a6b3d'), hexc('#74502c'), 5, 8)
    for x in (60, w - 60): p.shape([(x - 20, 70), (x + 20, 70), (x + 20, 400), (x - 20, 400)], hexc('#8a5f35'), hexc('#65452a'), 5, 6)
    c.alpha_composite(p.img.resize((w, 420), Image.LANCZOS), (x0 - 20, int(y) - 20))
filmadora = _h12.filmadora

LINES = [
    "A primeira webcam do mundo foi feita pra vigiar uma cafeteira.",
    "Em mil novecentos e noventa e um, num laboratório de computação na Inglaterra, todo mundo dividia uma cafeteira só.",
    "Quem trabalhava em outra sala ia até lá... e achava a jarra vazia.",
    "Então dois pesquisadores apontaram uma câmera pra cafeteira e ligaram no computador.",
    "Você vê, a imagem era pequenininha e em preto e branco, mas dava pra ver de longe se tinha café.",
    "Dois anos depois, ela foi pra internet, e gente do mundo todo começou a assistir uma cafeteira.",
    "Ou seja: a internet aprendeu a enxergar... por causa de um cafezinho.",
]
CAPTXT = [
    "A primeira webcam do mundo|foi feita pra vigiar uma cafeteira.",
    "Em 1991, num laboratório de computação na Inglaterra,|todo mundo dividia uma cafeteira só.",
    "Quem trabalhava em outra sala ia até lá...|e achava a jarra vazia.",
    "Então dois pesquisadores apontaram uma câmera|pra cafeteira e ligaram no computador.",
    "Você vê, a imagem era pequenininha e em preto e branco,|mas dava pra ver de longe se tinha café.",
    "Dois anos depois, ela foi pra internet,|e gente do mundo todo começou a assistir uma cafeteira.",
    "Ou seja: a internet aprendeu a enxergar...|por causa de um cafezinho.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [5]
CHECK = [(0, 'webcam', 4), (0, 'cafeteira', 6), (1, 'laboratorio', 4), (1, 'so', 6), (2, 'vazia', 6), (3, 'camera', 4),
         (3, 'computador', 6), (4, 'preto', 4), (4, 'cafe', 6), (5, 'internet', 4), (5, 'mundo', 4), (6, 'cafezinho', 8)]

VID, VID_D = hexc('#e9f6ff'), hexc('#b9d8ec')
CAFE, CAFE_D = hexc('#6b3e22'), hexc('#4a2a16')


# ------------------------------------------------------------------ objetos novos
def cafeteira(nivel=1.0, expr='calm', blink=0, look=0.3, cinza=0):
    """cafeteira de filtro com jarra de vidro (500x600, base em y≈590). nivel 0..1 = café na jarra; carinha na jarra."""
    p = Pen(500, 600)
    pl, pld = (hexc('#3b3f4a'), hexc('#262830')) if not cinza else (hexc('#555555'), hexc('#333333'))
    p.shape([(40, 20), (300, 20), (300, 120), (40, 120)], pl, pld, 6, 10)       # topo (filtro)
    p.shape([(40, 100), (130, 100), (130, 560), (40, 560)], pl, pld, 6, 10)     # coluna de trás
    p.shape([(20, 540), (480, 540), (480, 590), (20, 590)], pl, pld, 6, 8)      # base/chapa
    jar = [(160, 200), (400, 200), (440, 300), (450, 470), (420, 535), (180, 535), (150, 470), (140, 300)]
    vc, vcd = (VID, VID_D) if not cinza else (hexc('#dddddd'), hexc('#bbbbbb'))
    p.shape(jar, vc, vcd, 6, 10)
    if nivel > .03:
        top = 525 - 222 * nivel
        cc, ccd = (CAFE, CAFE_D) if not cinza else (hexc('#444444'), hexc('#2a2a2a'))
        liq = [(x, max(y, top)) for (x, y) in jar if y >= top - 1] or []
        liq = [(143, top), (441, top), (448, 470), (420, 528), (180, 528), (152, 470)]
        p.shape(liq, cc, ccd, 0, 8)
    p.shape([(170, 170), (390, 170), (400, 210), (160, 210)], pl, pld, 5, 6)     # tampa da jarra
    p.line(curve((440, 260), (500, 330), (448, 440), 10), pl, 18, 5)             # alça
    p.dot(80, 80, 12, hexc('#ff3b30') if not cinza else hexc('#999999'), 3)
    face(p, 295, 330 if nivel < .55 else 330, expr, blink, look, u=2.2)
    return p.img


def put_cafe(c, x, base, h, f, seed=1, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'nivel' in kw: kw['nivel'] = round(kw['nivel'] * 10) / 10
    im = sprite('cafeteira', tuple(sorted(kw.items())), int(h), 500 / 600, False)
    bob = .006 * math.sin((f + seed * 11) * .11) * h
    put(c, im, x, base + bob)


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def put_crt(c, x, base, w, f, seed=1, **kw):
    if w < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('crt', tuple(sorted(kw.items())), int(w), 1.0, False)
    put(c, im, x, base)


@lru_cache(maxsize=4)
def bg_lab(luz='day', x0=200, x1=1100):
    c = CEN('lab', luz).copy()
    mesa(c, 1380, x0, x1)
    return c


@lru_cache(maxsize=4)
def bg_esc(luz='day'):
    return CEN('escritorio', luz)


def tela_cafe(w=300, nivel=1.0):
    """imagem pequena e em preto e branco da cafeteira (pixelada), para a tela do computador."""
    im = cafeteira(nivel=nivel, expr='calm', cinza=1).convert('RGBA')
    bgc = Image.new('RGBA', im.size, (200, 200, 200, 255)); bgc.alpha_composite(im)
    g = bgc.convert('L').resize((24, 28), Image.BILINEAR).resize((w, int(w * 28 / 24)), Image.NEAREST)
    return g.convert('RGBA')


def SFX(s):
    s.ting(s.W(0, 'webcam'), .3)
    s.thunk(s.W(0, 'cafeteira') - 2, 180, .7)
    s.thunk(s.W(1, 'laboratorio') - 2, 220, .5)
    s.patter(s.W(2, 'ia'), s.W(2, 'ia') + 30, 8, .12)
    s.thunk(s.W(2, 'vazia') - 2, 120, .9)
    s.ting(s.W(3, 'camera'), .3); s.thunk(s.W(3, 'computador') - 2, 240, .6)
    s.ting(s.W(4, 'cafe'), .35)
    s.whoosh(s.W(5, 'internet') - 6, .6, .4)
    for i in range(5): s.thunk(s.W(5, 'mundo') - 2 + i * 4, 260, .4)
    s.trill(s.W(6, 'cafezinho'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 laboratório (cafeteira + câmera) | s1 laboratório 1991 (todos dividem a cafeteira) | s2 laboratório (jarra vazia)
# s3 laboratório (câmera ligada no computador) | s4 escritório em outra sala (tela mostra o café) | s5 mapa (mundo todo assiste)
# s6 laboratório ao entardecer (cafeteira orgulhosa)
def s0(f):
    c = bg_lab('day').copy()
    put_cafe(c, 520, 1380, 560, f, 1, expr='calm' if f < wt(0, 'vigiar') else 'nervous', look=.8)
    k = wt(0, 'webcam') - 3
    filmadora(c, 950, 1380, 1.1 * back(ramp(f, k, k + 8)))
    if f >= k: paste_c(c, txt('WEBCAM Nº 1', 100, -5), 640, 620, back(ramp(f, k, k + 8)))
    t = easeOut(ramp(f, 0, 50))
    return c, (lerp(560, 660, t), lerp(1150, 1120, t), lerp(1.5, 1.1, t) * (1 + .0009 * f), 0), 'day'


def s1(f):
    c = bg_lab('day', 420, 860).copy()
    k = wt(1, 'laboratorio') - 3
    paste_c(c, txt('1991', 130, -4), 640, 560, back(ramp(f, 2, 10)))
    put_cafe(c, 640, 1380, 460, f, 2, expr='grin', look=0)
    for i, (x, sd, kw) in enumerate(((220, 3, dict(shirt='#5c8fd6')), (1060, 4, dict(shirt='#7bc47f', bun=True, hair='#6b4a2e')))):
        s = back(ramp(f, k + i * 5, k + i * 5 + 9))
        put_pessoa(c, x, 1640, 760 * s, f, sd, expr='grin', arms='ask', look=.8 if i == 0 else -.8, **kw)
    so = wt(1, 'so') - 3
    if f >= so: paste_c(c, txt('SÓ UMA!', 100, 5), 640, 760, back(ramp(f, so, so + 8)))
    z = 1.1 * (1 + .0009 * f)
    return c, (lerp(600, 680, smooth(ramp(f, 0, 150))), 1200, z, 0), 'day'


def s2(f):
    c = bg_lab('day', 620, 1100).copy()
    a = wt(2, 'ia') - 3
    v = wt(2, 'vazia') - 3
    walk = smooth(ramp(f, a, a + 26))
    put_cafe(c, 860, 1380, 460, f, 3, nivel=1 - .5 * ramp(f, 0, a) - .5 * ramp(f, a, v), expr='nervous' if f >= v else 'calm', look=-.8)
    put_pessoa(c, lerp(-200, 420, walk), 1640, 780, f, 5, expr='pained' if f >= v else 'grin', arms='ask' if f >= v else 'hang', look=.8,
               shirt='#ff8a5c')
    if f >= v: paste_c(c, txt('VAZIA!', 120, -6), 640, 720, back(ramp(f, v, v + 8)))
    t = smooth(ramp(f, 0, 60))
    return c, (lerp(500, 660, t), 1180 + kick(f, v) * 8, 1.12 * (1 + .0009 * f), 0), 'day'


def s3(f):
    c = bg_lab('day', 120, 1140).copy()
    k = wt(3, 'camera') - 3
    m = wt(3, 'computador') - 3
    put_cafe(c, 360, 1380, 440, f, 4, nivel=.8, expr='side' if f >= k else 'calm', look=.9)
    filmadora(c, 640, 1380, .85 * back(ramp(f, k, k + 8)))
    if f >= m:
        put_crt(c, 960, 1380, 380 * back(ramp(f, m, m + 8)), f, 6, expr='grin')
        ImageDraw.Draw(c).line([(700, 1300), (800, 1360), (860, 1350)], fill=(36, 23, 38, 255), width=10)
    for i, (x, sd, kw) in enumerate(((200, 7, dict(shirt='#5c8fd6', arms='point')), (1100, 8, dict(shirt='#c58be0', arms='thumb' if False else 'point')))):
        put_pessoa(c, x, 1960, 700, f, sd, expr='grin', look=.6 if i == 0 else -.6, **kw)
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(520, 680, t), lerp(1200, 1250, t), lerp(1.2, 1.05, t) * (1 + .0009 * f), 0), 'day'


def s4(f):
    c = bg_esc('dusk').copy()
    mesa(c, 1400, 160, 880)
    k = wt(4, 'pequenininha') - 3
    ca = wt(4, 'cafe') - 3
    # computador grande com a imagem da cafeteira na tela
    p = Pen(700, 700)
    p.shape([(60, 40), (640, 40), (660, 560), (40, 560)], hexc('#e8dcc0'), hexc('#c4b48e'), 6, 16)
    p.shape([(110, 90), (590, 90), (605, 500), (95, 500)], hexc('#1f2a2a'), None, 5)
    p.shape([(260, 560), (440, 560), (470, 640), (230, 640)], hexc('#e8dcc0'), hexc('#c4b48e'), 6, 6)
    mon = p.img.resize((700, 700), Image.LANCZOS)
    if f >= k: mon.alpha_composite(tela_cafe(300, 1.0), (200, 105))
    paste_c(c, mon, 520, 1400 - 320)
    put_pessoa(c, 1000, 1700, 820, f, 9, expr='grin' if f >= ca else 'neutral', arms='point' if f >= ca else 'hang', look=-.9, shirt='#ff8a5c')
    if f >= ca: paste_c(c, txt('TEM CAFÉ!', 110, -5), 620, 560, back(ramp(f, ca, ca + 8)))
    if k <= f < ca: paste_c(c, txt('128 x 128', 80, 4), 520, 640, back(ramp(f, k, k + 8)))
    t = smooth(ramp(f, 0, 120))
    return c, (lerp(560, 680, t), lerp(1150, 1200, t), lerp(1.4, 1.12, t) * (1 + .0009 * f), 0), 'dusk'


def s5(f):
    c = CEN('mapa', 'day').copy()
    k = wt(5, 'internet') - 3
    m = wt(5, 'mundo') - 3
    paste_c(c, txt('INTERNET 1993', 96, -4), 640, 520, back(ramp(f, k, k + 8)))
    pts = ((290, 820), (990, 800), (640, 760), (280, 1260), (1000, 1260))
    for i, (x, y) in enumerate(pts):
        s = back(ramp(f, m + i * 4, m + i * 4 + 8))
        if s > .02:
            fr = Image.new('RGBA', (230, 260), hexc('#241726') + (255,))
            fr.alpha_composite(tela_cafe(200, 1.0), (15, 10))
            fr = fr.resize((max(1, int(300 * s)), max(1, int(340 * s))))
            paste_c(c, fr, x, y)
    put_cafe(c, 640, 1520, 400, f, 10, expr='proud' if f >= m else 'shock', look=0)
    z = 1.05 * (1 + .0012 * f)
    return c, (640, 1200, z, 0), 'day'


def s6(f):
    c = bg_lab('dusk').copy()
    k = wt(6, 'cafezinho') - 3
    put_cafe(c, 520, 1380, 520, f, 11, expr='smug' if f >= wt(6, 'enxergar') - 3 else 'calm', look=.6)
    filmadora(c, 950, 1380, 1.0)
    if f >= k: paste_c(c, txt('CAFEZINHO!', 110, -5), 600, 700, back(ramp(f, k, k + 8)))
    t = easeOut(ramp(f, 0, 80))
    return c, (lerp(680, 600, t), 1150, lerp(1.08, 1.35, t) * (1 + .0009 * f), lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
