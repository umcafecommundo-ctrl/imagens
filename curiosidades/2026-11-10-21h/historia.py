"""Formato DESENHO: por que não dá pra fazer cócegas em si mesmo (Curiosidades da IA, 10/11/2026, 21h). Categoria: CORPO HUMANO.
Fatos: Scientific American ("Why can't a person tickle himself?", Sarah-Jayne Blakemore, Institute of Cognitive Neuroscience,
University College London): o cerebelo, região no fundo do cérebro que monitora o movimento, prevê as sensações causadas pelos
nossos próprios movimentos e essa previsão diminui a resposta de outras áreas do cérebro, então o toque parece menos
cócegas; em experimentos com robô, um pequeno atraso entre o movimento e o toque deixa a sensação com mais cócegas, e quanto
maior o atraso, maior o efeito (Blakemore, Frith & Wolpert, 1999)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10c', '2026-11-08-10h')
pessoa = _h10.pessoa


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


LINES = [
    "Você não consegue fazer cócegas em você mesmo.",
    "A culpa é do cerebelo, um pedacinho no fundo do cérebro.",
    "Você vê, ele prevê o que a sua mão vai sentir... e abaixa o volume.",
    "Em Londres, cientistas puseram um robô no meio: quanto mais atraso, mais cócegas.",
    "Ou seja: cócegas só funcionam de surpresa.",
]
CAPTXT = [
    "Você não consegue fazer cócegas em você mesmo.",
    "A culpa é do cerebelo,|um pedacinho no fundo do cérebro.",
    "Você vê, ele prevê o que a sua mão vai sentir...|e abaixa o volume.",
    "Em Londres, cientistas puseram um robô no meio:|quanto mais atraso, mais cócegas.",
    "Ou seja: cócegas só funcionam de surpresa.",
]
FALA_TIKTOK = "Você já tentou? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 2
FLASH = []
CHECK = [(0, 'cocegas', 4), (0, 'mesmo', 6), (1, 'cerebelo', 4), (2, 'preve', 4), (2, 'volume', 6), (3, 'robo', 4),
         (3, 'atraso', 4), (3, 'cocegas', 6), (4, 'surpresa', 8)]

# cenários: s0 quarto (pessoa tenta fazer cócegas na própria barriga, nada) | s1 dentro do corpo (cérebro com o cerebelo
# aceso) | s2 dentro do corpo ao entardecer (cerebelo prevê e abaixa a barra de volume) | s3 laboratório (robô com pena,
# pessoa rindo com o atraso) | s4 quarto ao entardecer (amigo chega por trás de surpresa)

CER, CERD = hexc('#f4a6b5'), hexc('#d9879a')


@lru_cache(maxsize=4)
def cerebro_img(w, lit=0):
    p = Pen(500, 400)
    cb = hexc('#ffd84a') if lit else hexc('#e88ea2')
    p.shape(ell_pts(370, 300, 110, 72), cb, mul(cb, .82), 6, 10)
    for k in range(3): p.arc(370, 290 + k * 20, 80 - k * 14, 22, 200, 340, 5)
    p.shape(ell_pts(220, 170, 195, 135), CER, CERD, 6, 16)
    for (x, y, a0, a1) in ((130, 140, 200, 340), (220, 110, 20, 160), (310, 140, 200, 340), (170, 210, 20, 160), (280, 220, 200, 340)):
        p.arc(x, y, 50, 26, a0, a1, 6)
    p.line([(270, 300), (260, 390)], CERD, 40, 5)
    return p.img.resize((w, int(w * .8)), Image.LANCZOS)


@lru_cache(maxsize=4)
def pena_img(w=160):
    p = Pen(160, 300)
    p.shape(ell_pts(80, 130, 46, 120, 40), hexc('#ffffff'), hexc('#dfe6ee'), 5, 6)
    p.line([(80, 20), (80, 290)], hexc('#c9c2b0'), 6, 3)
    return p.img.resize((w, int(w * 300 / 160)), Image.LANCZOS)


@lru_cache(maxsize=2)
def robo_img():
    p = Pen(500, 700)
    p.shape([(140, 400), (360, 400), (380, 690), (120, 690)], hexc('#9aa6b5'), hexc('#7a8595'), 6, 14)
    p.shape([(170, 230), (330, 230), (330, 380), (170, 380)], hexc('#b9c2cc'), hexc('#8d97a3'), 6, 10)
    for x in (215, 285): p.dot(x, 300, 22, hexc('#59d6ff'), 4)
    p.stroke([(250, 230), (250, 170)], 8); p.dot(250, 160, 16, hexc('#ff3b30'), 4)
    p.dot(250, 520, 34, hexc('#ffd84a'), 4)
    return p.img


def SFX(s):
    s.patter(s.W(0, 'cocegas') - 4, s.W(0, 'cocegas') + 26, 10, .12)
    s.thunk(s.W(0, 'mesmo') - 2, 200, .5)
    s.ting(s.W(1, 'cerebelo'), .35)
    s.whoosh(s.W(2, 'preve') - 4, .4, .4)
    for i in range(3): s.thunk(s.W(2, 'volume') - 2 + i * 5, 300 - i * 50, .4)
    s.thunk(s.W(3, 'robo') - 2, 160, .6)
    s.patter(s.W(3, 'cocegas', 1) - 2, s.W(3, 'cocegas', 1) + 30, 14, .15)
    s.trill(s.W(4, 'surpresa'), 1.0, .3)


def tremor(c, x, y, f, n=3):
    for i in range(n):
        a = (f * 3 + i * 40) % 360
        pn = Pen(80, 60)
        pn.stroke([(5, 30), (25, 10), (45, 50), (75, 20)], 6)
        paste_c(c, pn.img, x + 60 * math.cos(math.radians(a)), y + 30 * math.sin(math.radians(a)), .8)


def s0(f):
    c = CEN('quarto', 'day').copy()
    k = wt(0, 'cocegas') - 3
    m = wt(0, 'mesmo') - 3
    put_pessoa(c, 621, 1780, 1000, f, 2, shirt='#ff8a5c', arms='ask' if f >= k else 'hang',
               expr='stern' if f >= m else 'neutral', look=0, tilt=2 * math.sin(f * .6) if f >= k else 0)
    if f >= k: tremor(c, 621, 1230, f)
    if k <= f < m: paste_c(c, txt('CÓCEGAS?', 110, -6), 621, 720, back(ramp(f, k, k + 8)))
    if f >= m: paste_c(c, txt('NADA.', 130, 6), 621, 720, back(ramp(f, m, m + 8)))
    z = lerp(1.3, 1.08, easeOut(ramp(f, 2, 40))) * (1 + .0009 * f)
    return c, (621, 1200, z, 0), 'day'


def s1(f):
    c = CEN('corpo', 'day').copy()
    k = wt(1, 'cerebelo') - 3
    lit = 1 if f >= k and (f - k) % 10 < 7 else (1 if f >= k + 20 else 0)
    paste_c(c, cerebro_img(900, lit), 621, 1050, back(ramp(f, 0, 10)))
    if f >= k: paste_c(c, txt('CEREBELO', 110, -4), 760, 680, back(ramp(f, k, k + 8)))
    t = smooth(ramp(f, k, k + 30))
    z = lerp(1.05, 1.4, t) * (1 + .0009 * f)
    return c, (lerp(621, 760, t), lerp(1050, 1150, t), z, 0), 'day'


def s2(f):
    c = CEN('corpo', 'dusk').copy()
    pv = wt(2, 'preve') - 3
    vo = wt(2, 'volume') - 3
    paste_c(c, cerebro_img(620, 1), 621, 760)
    if f >= pv:
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        hand = Pen(200, 200); hand.shape(ell_pts(100, 110, 70, 60), hexc('#f1c27d'), hexc('#d9a35f'), 5, 6)
        for k in range(4): hand.line([(60 + k * 27, 70), (55 + k * 30, 15)], hexc('#f1c27d'), 22, 4)
        cont.alpha_composite(hand.img.resize((220, 220)), (40, 40))
        thought(c, 960, 380, 200, back(ramp(f, pv, pv + 8)), cont)
    lvl = 1 - .8 * easeOut(ramp(f, vo, vo + 14))
    d = ImageDraw.Draw(c)
    for i in range(5):
        on = (i + 1) / 5 <= lvl + .01
        x0 = 300 + i * 140
        hh = 60 + i * 50
        d.rectangle((x0, 1560 - hh, x0 + 100, 1560), fill=(255, 216, 74, 255) if on else (120, 120, 140, 160), outline=INK + (255,), width=6)
    if f >= vo: paste_c(c, txt('VOLUME BAIXO', 90, -4), 621, 1200, back(ramp(f, vo, vo + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1050, z, 0), 'dusk'


def s3(f):
    c = CEN('lab', 'day').copy(); c.alpha_composite(P.lamp_glow(1))
    r = wt(3, 'robo') - 3
    a = wt(3, 'atraso') - 3
    k = wt(3, 'cocegas', 1) - 3
    s = back(ramp(f, r, r + 9))
    if s > .05:
        im = robo_img().resize((max(1, int(500 * s)), max(1, int(700 * s))))
        c.alpha_composite(im, (int(330 - im.size[0] / 2), int(1760 - im.size[1])))
        put_dust(c, 330, 1740, 90, f - r)
        wig = 30 * math.sin(f * .9) if f >= a else 0
        if s > .9: ImageDraw.Draw(c).line((420, 1420, 600, 1280), fill=(122, 133, 149, 255), width=22)
        paste_c(c, pena_img(150).rotate(-50 + wig, Image.BICUBIC, expand=True), 640, 1240, s)
    laugh = f >= k
    put_pessoa(c, 900, 1780, 950, f, 3, shirt='#ff8a5c', arms='ask' if laugh else 'hang',
               expr='grin' if laugh else 'neutral', look=-1, tilt=3 * math.sin(f * .8) if laugh else 0)
    if a <= f < k: paste_c(c, txt('ATRASO...', 90, -4), 621, 680, back(ramp(f, a, a + 8)))
    if laugh:
        paste_c(c, txt('HAHAHA!', 100, 6), 621, 680, back(ramp(f, k, k + 8)))
        tremor(c, 900, 1260, f)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1220 + kick(f, k, .5) * 10, z, 0), 'day'


def s4(f):
    c = CEN('quarto', 'dusk').copy()
    sp = wt(4, 'surpresa') - 3
    t = smooth(ramp(f, sp - 14, sp))
    put_pessoa(c, lerp(1300, 980, t), 1760, 920, f, 5, shirt='#3fa36b', hair='#7a4a2a', bun=True,
               arms='point' if f >= sp else 'hang', expr='smug', look=-1)
    hit = f >= sp
    put_pessoa(c, 520, 1780, 980, f, 2, shirt='#ff8a5c', arms='up' if hit else 'hang',
               expr='grin' if hit else 'neutral', look=0, tilt=3 * math.sin(f * .8) if hit else 0)
    if hit:
        if f < sp + 35: paste_c(c, txt('SURPRESA!', 120, -6), 680, 700, back(ramp(f, sp, sp + 8)))
        tremor(c, 520, 1250, f)
    k = kick(f, sp, .6)
    z = lerp(1.05, 1.2, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (680, 1200 + k * 10, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
