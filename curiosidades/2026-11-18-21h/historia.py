"""Formato DESENHO: por que o dedo estala (Curiosidades da IA, 18/11/2026, 21h).
Categoria: CORPO HUMANO.
Fatos: Science News Explores, "Mystery solved: Why knuckles crack" (estudo de Gregory Kawchuk, Universidade de Alberta,
PLOS ONE, abril de 2015, com ressonância magnética): entre os ossos do dedo há um líquido (líquido sinovial); ao puxar o
dedo, a junta se separa e uma cavidade/bolha se forma no líquido, junto com o estalo; a bolha pode durar até 20 minutos
e o dedo não estala de novo até ela sumir. EurekAlert (Univ. de Alberta, 2015).
Cenários: s0 sala (Professor estala o dedo, CREC!) | s1 sala + lupa dentro do dedo (líquido entre os ossos) |
s2 sala + lupa (puxa, junta abre, bolha, estalo) | s3 sala ao entardecer + lupa e relógio (bolha leva ~20 min, não estala) |
s4 sala ao entardecer (Professor com xícara: o dedo de intervalo)."""
from kit import *
from functools import lru_cache

LINES = [
    "Sabe o estalo do dedo? Não é osso batendo.",
    "Entre os ossinhos do dedo tem um líquido que deixa a junta lisinha.",
    "Quando você puxa o dedo, a junta se abre, e aparece uma bolha nesse líquido. Créc!",
    "Você vê, a bolha pode levar uns vinte minutos pra sumir. Até lá, o dedo não estala de novo.",
    "Ou seja: até o seu dedo tira intervalo.",
]
CAPTXT = [
    "Sabe o estalo do dedo? Não é osso batendo.",
    "Entre os ossinhos do dedo tem um líquido|que deixa a junta lisinha.",
    "Quando você puxa o dedo, a junta se abre,|e aparece uma bolha nesse líquido. Créc!",
    "Você vê, a bolha pode levar uns 20 minutos pra sumir.|Até lá, o dedo não estala de novo.",
    "Ou seja: até o seu dedo tira intervalo.",
]
FALA_TIKTOK = "Você estala o dedo? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'estalo', 4), (0, 'osso', 6), (1, 'liquido', 6), (2, 'puxa', 4), (2, 'bolha', 4), (2, 'crec', 4),
         (3, 'vinte', 6), (3, 'novo', 6), (4, 'intervalo', 8)]

SKIN = hexc('#f2c29b'); SKIND = hexc('#d89d72')
BONE = hexc('#f3ead6'); BONED = hexc('#d8c8a6')
FLU = (150, 210, 245)


def SFX(s):
    s.thunk(s.W(0, 'estalo') - 1, 420, 1.0)
    s.thunk(s.W(0, 'osso') - 2, 200, .5)
    s.patter(s.W(1, 'liquido'), s.W(1, 'liquido') + 40, 8, .08)
    s.whoosh(s.W(2, 'puxa') - 4, .4, .4)
    s.thunk(s.W(2, 'crec') - 1, 460, 1.0); s.ting(s.W(2, 'bolha'), .3)
    for i in range(6): s.thunk(s.W(3, 'vinte') + i * 6, 700, .25)
    s.thunk(s.W(3, 'novo') - 2, 160, .6)
    s.trill(s.W(4, 'intervalo'), 1.0, .3)


@lru_cache(maxsize=16)
def dedo_img(w, bend=0):
    """um dedo sozinho, deitado, apontando para a direita; bend 0..1 dobra a ponta."""
    p = Pen(300, 600)
    a = math.radians(-25 * bend)
    cx, cy = 150, 390
    def r(x, y):
        dx, dy = x - cx, y - cy
        return (cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a))
    cap = [(150 + 45 * math.cos(math.radians(a)), 95 + 50 * math.sin(math.radians(a))) for a in range(180, 361, 15)]
    p.shape([r(105, 395)] + [r(x, y) for x, y in cap] + [r(195, 395)], SKIN, SKIND, 6, 10)
    nail = [(150 + 28 * math.cos(math.radians(a)), 100 + 30 * math.sin(math.radians(a))) for a in range(180, 361, 20)]
    p.shape([r(x, y) for x, y in nail] + [r(178, 150), r(122, 150)], hexc('#fbe3d3'), SKIND, 4, 0)
    for y in (220, 300):
        p.arc(*r(150, y), 30, 8, 200, 340, 4, SKIND)
    W_, H_ = p.img.size
    im = p.img.crop((int(W_ * .25), 0, int(W_ * .75), int(H_ * .7))).rotate(-90, Image.BICUBIC, expand=True)  # deitado, apontando p/ a direita
    return im.resize((int(w), int(w * im.size[1] / im.size[0])), Image.LANCZOS)


def junta(c, cx, cy, R, f, abre=0.0, bolha=0.0, some=0.0):
    """lupa com a junta do dedo em corte: dois ossos, cápsula com líquido, bolha que aparece."""
    if R < 8: return
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=(242, 170, 160, 255))
    gap = 26 + 70 * abre
    # cápsula com líquido
    d.rounded_rectangle((cx - R * .55, cy - gap - 60, cx + R * .55, cy + gap + 60), radius=60,
                        fill=FLU + (255,), outline=INK + (255,), width=6)
    # ondinhas do líquido
    for k in range(3):
        y = cy - gap * .5 + k * gap * .5
        xs = [(cx - R * .45 + i * 20, y + 6 * math.sin(i * .9 + f * .2)) for i in range(int(R * .9 / 20))]
        if len(xs) > 1: d.line(xs, fill=(210, 240, 255, 255), width=4)
    # ossos
    s = R * .42
    d.rounded_rectangle((cx - s, cy - gap - R, cx + s, cy - gap), radius=50, fill=BONE + (255,), outline=INK + (255,), width=7)
    d.rounded_rectangle((cx - s, cy + gap, cx + s, cy + gap + R), radius=50, fill=BONE + (255,), outline=INK + (255,), width=7)
    for yy in (cy - gap - R * .5, cy + gap + R * .5):
        d.line([(cx - s * .5, yy), (cx + s * .5, yy)], fill=BONED + (255,), width=6)
    if bolha > 0:
        br = (gap * .9) * bolha * (1 - some) + 2
        if br > 4:
            wob = 1 + .06 * math.sin(f * .5)
            d.ellipse((cx - br * 1.6 * wob, cy - br, cx + br * 1.6 * wob, cy + br), fill=(255, 255, 255, 255), outline=INK + (255,), width=6)
            d.ellipse((cx - br * .9, cy - br * .6, cx - br * .4, cy - br * .2), fill=(220, 240, 255, 255))
    mask = Image.new('L', c.size, 0); ImageDraw.Draw(mask).ellipse((cx - R, cy - R, cx + R, cy + R), fill=255)
    out = Image.new('RGBA', c.size, (0, 0, 0, 0)); out.paste(lay, (0, 0), mask)
    c.alpha_composite(out)
    dd = ImageDraw.Draw(c)
    dd.ellipse((cx - R - 12, cy - R - 12, cx + R + 12, cy + R + 12), outline=INK + (255,), width=14)
    dd.ellipse((cx - R - 4, cy - R - 4, cx + R + 4, cy + R + 4), outline=(250, 250, 250, 255), width=6)


@lru_cache(maxsize=2)
def xicara_img(w):
    p = Pen(300, 260)
    p.shape([(40, 60), (230, 60), (210, 230), (60, 230)], hexc('#ffffff'), hexc('#dcdcdc'), 6, 10)
    p.arc(245, 130, 40, 50, -80, 80, 12)
    p.shape(ell_pts(135, 62, 95, 18, 30), hexc('#7a4a2a'), None, 5, 0)
    return p.img.resize((int(w), int(w * 260 / 300)), Image.LANCZOS)


def s0(f):
    c = CEN('sala', 'day').copy()
    e = wt(0, 'estalo') - 2
    o = wt(0, 'osso') - 3
    bend = pulse(f, e - 6, 4) if f < e + 10 else 0
    paste_c(c, dedo_img(460, round(bend * 4) / 4), 870, 860)
    put_prof(c, 380, 1880, 980, f, expr='shock' if f >= e else 'grin', arms='point', look=1)
    if e <= f < o: paste_c(c, txt('CRÉC!', 130, 8), 860, 600, back(ramp(f, e, e + 8)))
    if f >= o: paste_c(c, txt('NÃO É OSSO!', 100, -5), 720, 640, back(ramp(f, o, o + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1230 + kick(f, e, .8) * 12, z, 0), 'day'


def s1(f):
    c = CEN('sala', 'day').copy()
    l = wt(1, 'liquido') - 3
    R = 400 * back(ramp(f, 0, 10)) if f < 10 else 400
    junta(c, 700, 880, R, f)
    put_prof(c, 300, 1830, 700, f, expr='grin' if f >= l else 'neutral', arms='point' if f >= l else 'chin', look=1)
    if f >= l: paste_c(c, txt('LÍQUIDO', 100, -5), 700, 400, back(ramp(f, l, l + 8)))
    z = lerp(1.05, 1.18, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (660, 1130, z, 0), 'day'


def s2(f):
    c = CEN('sala', 'day').copy()
    p = wt(2, 'puxa') - 3
    b = wt(2, 'bolha') - 3
    k = wt(2, 'crec') - 2
    ab = smooth(ramp(f, p, p + 14))
    junta(c, 700, 880, 400, f, ab, back(ramp(f, b, b + 8)) if f >= b else 0)
    put_prof(c, 300, 1830, 700, f, expr='shock' if f >= k else 'neutral', arms='up' if f >= k else 'point', look=1)
    if p <= f < b: paste_c(c, txt('PUXA!', 100, 5), 700, 400, back(ramp(f, p, p + 8)))
    if b <= f < k: paste_c(c, txt('BOLHA', 100, -5), 700, 400, back(ramp(f, b, b + 8)))
    if f >= k: paste_c(c, txt('CRÉC!', 140, 8), 700, 400, back(ramp(f, k, k + 8)))
    z = lerp(1.18, 1.1, smooth(ramp(f, 0, 50))) * (1 + .0009 * f)
    return c, (660, 1120 + kick(f, k, .9) * 14, z, kick(f, k, .9) * 2), 'day'


def s3(f):
    c = CEN('sala', 'dusk').copy()
    v = wt(3, 'vinte') - 3
    n = wt(3, 'novo') - 3
    ab = 1 - .7 * smooth(ramp(f, n, n + 30))
    junta(c, 700, 860, 360, f, max(.3, ab), 1, .9 * smooth(ramp(f, v, n + 30)))
    if f >= v:
        spin = (f - v) / 18
        paste_c(c, clock_img(2.0 + spin * .05, spin * 2, 220), 1030, 1300, back(ramp(f, v, v + 8)))
        paste_c(c, txt('20 MIN', 100, -5), 700, 380, back(ramp(f, v, v + 8)))
    put_prof(c, 300, 1830, 700, f, expr='pained' if f >= n else 'neutral', arms='shrug' if f >= n else 'point', look=1)
    if f >= n: paste_c(c, txt('NADA...', 90, 5), 880, 1500, back(ramp(f, n, n + 8)))
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.22, 1.1, t) * (1 + .0009 * f)
    return c, (660, 1110, z, lerp(2, 0, t)), 'dusk'


def s4(f):
    c = CEN('sala', 'dusk').copy()
    i = wt(4, 'intervalo') - 3
    paste_c(c, dedo_img(420, 0), 880, 1180 + 10 * math.sin(f * .15))
    put_prof(c, 380, 1880, 980, f, expr='grin' if f >= i else 'smug', arms='point' if f >= i else 'chin', look=1)
    if f >= i:
        paste_c(c, xicara_img(200), 930, 880, back(ramp(f, i, i + 8)))
        paste_c(c, txt('INTERVALO!', 110, -5), 700, 640, back(ramp(f, i, i + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (640, lerp(1250, 1200, t) + kick(f, i, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
