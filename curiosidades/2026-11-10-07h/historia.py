"""Formato DESENHO: na montanha a água ferve mais fria (Curiosidades da IA, 10/11/2026, 07h). Categoria: CIÊNCIA DO DIA A DIA.
Fatos: LibreTexts Chemistry (CK-12, 13.9 Boiling): a água ferve a 100 °C no nível do mar e só a cerca de 70 °C no topo do
Everest; o ponto de ebulição é a temperatura em que a pressão de vapor iguala a pressão de fora, e cai com a altitude.
Cozinhar em altitude demora mais porque a água fervendo está menos quente (LibreTexts; guias de cozinha em altitude)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h = _load('h10p', '2026-11-08-10h')
pessoa = _h.pessoa
put_pessoa = _h.put_pessoa

LINES = [
    "No alto da montanha, a água ferve... mais fria.",
    "Na cozinha de casa, ela ferve a cem graus.",
    "No topo do Everest, borbulha com uns setenta.",
    "Você vê, lá em cima tem menos ar apertando a água, e as bolhas escapam mais fácil.",
    "Ou seja: a água ferve rapidinho... e o macarrão continua duro.",
]
CAPTXT = [
    "No alto da montanha, a água ferve... mais fria.",
    "Na cozinha de casa, ela ferve a 100 graus.",
    "No topo do Everest, borbulha com uns 70.",
    "Você vê, lá em cima tem menos ar apertando a água,|e as bolhas escapam mais fácil.",
    "Ou seja: a água ferve rapidinho...|e o macarrão continua duro.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'ferve', 4), (0, 'fria', 6), (1, 'cem', 6), (2, 'everest', 4), (2, 'setenta', 6), (3, 'ar', 4),
         (3, 'bolhas', 6), (4, 'macarrao', 4), (4, 'duro', 8)]

# cenários: s0 neve (topo da montanha: panela no fogareiro) | s1 cozinha (panela no fogão, termômetro 100) |
# s2 neve (topo do Everest, termômetro desce p/ 70) | s3 neve ao entardecer (explicação: setas de ar sobre a panela) |
# s4 neve ao entardecer (macarrão duro saindo da panela)

JAQ = '#2f7fd1'


@lru_cache(maxsize=32)
def panela_img(w, boil=1, ph=0, mac=0):
    p = Pen(500, 460)
    if mac:  # fios de macarrão duros saindo em leque
        for i, a in enumerate((-.5, -.25, 0, .22, .45)):
            x0 = 250 + i * 14 - 28
            p.line([(x0, 200), (x0 + 330 * math.sin(a), 200 - 330 * math.cos(a))], hexc('#f2c65a'), 12, 4)
    body = [(70, 170), (430, 170), (410, 420), (90, 420)]
    p.shape(body, hexc('#b9c2cc'), hexc('#8d97a3'), 6, 18)
    p.shape([(20, 190), (75, 190), (75, 225), (20, 225)], hexc('#5a5f68'), None, 5, 0)
    p.shape([(425, 190), (480, 190), (480, 225), (425, 225)], hexc('#5a5f68'), None, 5, 0)
    p.shape(ell_pts(250, 172, 182, 30), hexc('#7fc4ef'), hexc('#5aa6d6'), 5, 6)
    if boil:
        rnd = random.Random(ph)
        for i in range(9):
            x = 110 + i * 35 + rnd.uniform(-8, 8)
            y = 170 + rnd.uniform(-12, 10)
            r = rnd.uniform(8, 16)
            p.shape(ell_pts(x, y - r * .6, r, r), hexc('#d9f1ff'), None, 3, 0)
        for i in range(3):
            x = 160 + i * 90 + 10 * math.sin(ph + i)
            p.stroke([(x, 120), (x + 18, 80), (x - 6, 40), (x + 14, 5)], 7, (238, 244, 250))
    im = p.img
    return im.resize((w, int(w * 460 / 500)), Image.LANCZOS)


def panela(c, x, base, w, boil=1, f=0, mac=0):
    if w < 8: return
    im = panela_img(int(w), 1 if boil else 0, (f // 3) % 6 if boil else 0, mac)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(base - im.size[1] * 420 / 460)))


@lru_cache(maxsize=8)
def fogo_img(w, ph):
    p = Pen(500, 200)
    p.shape([(60, 120), (440, 120), (420, 190), (80, 190)], hexc('#3b3d44'), hexc('#26282d'), 5, 0)
    for i in range(5):
        x = 110 + i * 70
        hgt = 70 + 18 * math.sin(ph * 1.3 + i * 2)
        p.shape([(x - 22, 120), (x, 120 - hgt), (x + 22, 120)], hexc('#4fa3ff'), hexc('#2f6fd1'), 3, 0)
    return p.img.resize((w, int(w * 200 / 500)), Image.LANCZOS)


def fogo(c, x, base, w, f):
    im = fogo_img(int(w), (f // 3) % 6)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(base - im.size[1] * 190 / 200)))


@lru_cache(maxsize=64)
def termo_img(h, v):
    p = Pen(200, 760)
    p.shape([(70, 40), (130, 40), (130, 600), (70, 600)], hexc('#f6f6f6'), hexc('#d9d9d9'), 6, 0)
    p.shape(ell_pts(100, 40, 30, 30), hexc('#f6f6f6'), None, 6, 0)
    top = 590 - v * 520
    p.poly([(85, top), (115, top), (115, 640), (85, 640)], hexc('#e23b3b'))
    p.shape(ell_pts(100, 670, 62, 62), hexc('#e23b3b'), hexc('#b82a2a'), 6, 10)
    for i in range(6):
        y = 590 - i * 104
        p.line([(130, y), (160, y)], INK, 6, 0)
    return p.img.resize((int(h * 200 / 760), h), Image.LANCZOS)


def termo(c, x, base, h, v):
    if h < 8: return
    im = termo_img(int(h), round(v * 40) / 40)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(base - h)))


@lru_cache(maxsize=4)
def seta_img(h):
    p = Pen(160, 300)
    p.shape([(55, 10), (105, 10), (105, 170), (150, 170), (80, 290), (10, 170), (55, 170)], hexc('#ffffff'), hexc('#cfd8e3'), 6, 0)
    return p.img.resize((int(h * 160 / 300), h), Image.LANCZOS)


def SFX(s):
    s.patter(0, 40, 10, .1)
    s.ting(s.W(0, 'fria'), .35)
    s.thunk(s.W(1, 'cem') - 2, 200, .6)
    s.thunk(s.W(2, 'everest') - 2, 160, .5)
    s.whoosh(s.W(2, 'setenta') - 6, .4, .4); s.thunk(s.W(2, 'setenta') - 2, 260, .6)
    for i in range(3): s.thunk(s.W(3, 'ar') - 2 + i * 5, 300, .35)
    s.patter(s.W(3, 'bolhas'), s.W(3, 'bolhas') + 30, 12, .14)
    s.thunk(s.W(4, 'duro') - 2, 120, .8); s.trill(s.W(4, 'duro') + 4, 1.0, .3)


def s0(f):
    c = CEN('neve', 'day').copy()
    fogo(c, 470, 1720, 420, f)
    panela(c, 470, 1600, 460, 1, f)
    k = wt(0, 'fria') - 3
    fe = wt(0, 'ferve') - 3
    put_pessoa(c, 960, 1740, 900, f, 2, shirt=JAQ, pants='#3a3f4a', arms='point' if f >= k else 'hang',
               expr='shock' if f >= k else 'grin', look=-1)
    if fe <= f < k: paste_c(c, txt('FERVEU!', 110, 6), 470, 1050, back(ramp(f, fe, fe + 8)))
    if f >= k: paste_c(c, txt('MAIS FRIA?!', 100, -6), 430, 1080, back(ramp(f, k, k + 8)))
    z = lerp(1.35, 1.08, easeOut(ramp(f, 2, 40))) * (1 + .0009 * f)
    return c, (640, 1300, z, 0), 'day'


def s1(f):
    c = CEN('cozinha', 'day').copy()
    fogo(c, 560, 1760, 460, f)
    panela(c, 560, 1640, 500, 1, f)
    k = wt(1, 'cem') - 3
    v = .2 + .8 * easeOut(ramp(f, k - 14, k + 2))
    termo(c, 970, 1720, 720 * back(ramp(f, 2, 12)), v)
    put_pessoa(c, 290, 1760, 820, f, 3, shirt='#ff8a5c', arms='point' if f >= k else 'hang', expr='grin', look=1)
    if f >= k: paste_c(c, txt('100 GRAUS', 100, -5), 760, 900, back(ramp(f, k, k + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (640, 1300 + kick(f, k, .6) * 10, z, 0), 'day'


def s2(f):
    c = CEN('neve', 'day').copy()
    e = wt(2, 'everest') - 3
    k = wt(2, 'setenta') - 3
    if f >= e: paste_c(c, txt('EVEREST', 90, 0), 621, 560, back(ramp(f, e, e + 8)))
    fogo(c, 600, 1760, 420, f)
    panela(c, 600, 1640, 460, 1, f)
    v = 1 - .3 * easeOut(ramp(f, k - 10, k + 6))
    termo(c, 980, 1720, 720, v)
    if f >= k: paste_c(c, txt('70 GRAUS', 100, 5), 760, 900, back(ramp(f, k, k + 8)))
    put_pessoa(c, 290, 1760, 820, f, 2, shirt=JAQ, pants='#3a3f4a', arms='cheek' if f >= k else 'hang',
               expr='shock' if f >= k else 'neutral', look=1)
    t = smooth(ramp(f, 0, 50))
    z = lerp(1.6, 1.1, t) * (1 + .0009 * f)
    return c, (640, lerp(700, 1300, t) + kick(f, k, .6) * 10, z, 0), 'day'


def s3(f):
    c = CEN('neve', 'dusk').copy()
    a = wt(3, 'ar') - 3
    b = wt(3, 'bolhas') - 3
    fogo(c, 621, 1760, 520, f)
    panela(c, 621, 1640, 560, 1, f)
    for i, x in enumerate((380, 621, 862)):
        s = back(ramp(f, a + i * 4, a + i * 4 + 8))
        if s > .05:
            y = 900 + 25 * math.sin(f * .2 + i)
            paste_c(c, seta_img(260), x, y, s)
    if f >= a: paste_c(c, txt('MENOS AR', 100, -4), 621, 640, back(ramp(f, a, a + 8)))
    if f >= b:
        for i in range(8):
            age = (f - b + i * 6) % 40
            x = 420 + i * 55 + 12 * math.sin(f * .3 + i)
            y = 1380 - age * 14
            r = 18 + i % 3 * 6
            if y > 700:
                c.alpha_composite(Image.new('RGBA', (1, 1), (0, 0, 0, 0)))
                d = ImageDraw.Draw(c)
                d.ellipse((x - r, y - r, x + r, y + r), fill=(217, 241, 255, 255), outline=INK + (255,), width=4)
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.1, 1.35, t) * (1 + .0009 * f)
    return c, (621, lerp(1250, 1200, t), z, lerp(0, 2, t)), 'dusk'


def s4(f):
    c = CEN('neve', 'dusk').copy()
    m = wt(4, 'macarrao') - 3
    d = wt(4, 'duro') - 3
    fogo(c, 470, 1760, 460, f)
    panela(c, 470, 1640, 500, 1, f, mac=1 if f >= m else 0)
    put_pessoa(c, 900, 1760, 860, f, 2, shirt=JAQ, pants='#3a3f4a', arms='shrug' if f >= d else 'hang',
               expr='pained' if f >= d else 'neutral', look=-1)
    if d <= f < d + 45: paste_c(c, txt('DURO!', 130, -8), 520, 900, back(ramp(f, d, d + 8)))
    k = kick(f, d, .8)
    z = lerp(1.05, 1.25, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (640, 1300 + k * 10, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
