"""Formato DESENHO: quem choca o ovo do pinguim-imperador é o pai (Curiosidades da IA, 11/11/2026, 07h). Categoria: ANIMAIS.
Fatos: WWF-UK "Top 10 facts about emperor penguins": a fêmea bota um ovo em maio/junho, passa para o macho e passa cerca de
nove semanas no mar se alimentando; o macho equilibra o ovo em cima dos pés, coberto por uma bolsa de pele (brood pouch),
por cerca de 65 a 75 dias; fica sem comer e perde quase metade do peso; no inverno pode fazer cerca de -50 °C.
Animal Diversity Web (Univ. de Michigan, Aptenodytes forsteri): incubação de ~65 dias pelo macho, que jejua o tempo todo e
perde ~40% da massa; a fêmea vai de 50 a 120 km até o mar para comer e volta perto do nascimento."""
from kit import *
import kit

LINES = [
    "Quem choca o ovo do pinguim-imperador é o pai.",
    "No inverno da Antártida, a mãe bota o ovo, passa pro pai e vai pro mar comer.",
    "Ele fica uns dois meses com o ovo em cima dos pés, sem comer nada.",
    "Você vê, se o ovo encostar no gelo, congela. E lá faz até cinquenta graus negativos.",
    "Quando a mãe volta, ele está bem mais magrinho... e finalmente vai jantar.",
]
CAPTXT = [
    "Quem choca o ovo do pinguim-imperador é o pai.",
    "No inverno da Antártida, a mãe bota o ovo,|passa pro pai e vai pro mar comer.",
    "Ele fica uns dois meses com o ovo em cima dos pés,|sem comer nada.",
    "Você vê, se o ovo encostar no gelo, congela.|E lá faz até 50 graus negativos.",
    "Quando a mãe volta, ele está bem mais magrinho...|e finalmente vai jantar.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = [2]
CHECK = [(0, 'pai', 4), (1, 'passa', 6), (1, 'mar', 6), (2, 'pes', 4), (2, 'nada', 6), (3, 'gelo', 4), (3, 'congela', 6),
         (3, 'cinquenta', 6), (4, 'magrinho', 4), (4, 'jantar', 8)]

# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 neve (Antártida, o pai com o ovo nos pés) | s1 neve (mãe passa o ovo e sai para o mar, com faixa de mar ao fundo)
# s2 neve dourada com neve caindo (tempo passando, dois meses parado) | s3 neve ao entardecer (close no ovo, gelo, -50)
# s4 neve ao entardecer (mãe volta, pai magrinho sai para o mar jantar)

DARK, DARKD = hexc('#2b2d3a'), hexc('#1b1c26')
WHITE, WHITED = hexc('#f6f4ee'), hexc('#d9d6cc')
ORG, ORGD = hexc('#f2b23a'), hexc('#c98a1e')


def imperador(blink=0, look=0.3, expr='calm', ovo=0, fat=1.0, chick=0):
    """pinguim-imperador de frente (400x600): manchas amarelas no pescoço; ovo=1 põe o ovo nos pés coberto pela dobra."""
    p = Pen(400, 600)
    bw = 120 + 30 * fat
    for s in (-1, 1): p.shape(ell_pts(200 + s * 52, 582, 52, 16, 24), hexc('#3a3a44'), hexc('#24242c'), 4, 4)
    p.shape(ell_pts(200, 340, bw, 240, 56, 0, .12), DARK, DARKD, 6, 16)
    p.shape(ell_pts(200, 390, bw - 38, 190, 48), WHITE, WHITED, 0, 10)
    # manchas amarelas do pescoço
    for s in (-1, 1): p.shape(ell_pts(200 + s * 70, 230, 34, 46, 24, s * .4), ORG, ORGD, 0, 4)
    p.shape(ell_pts(200, 268, 60, 26, 24), hexc('#f7e08a'), None, 0, 0)
    p.shape([(200 - bw + 10, 280), (200 - bw - 40, 420), (200 - bw + 30, 450)], DARK, None, 5)
    p.shape([(200 + bw - 10, 280), (200 + bw + 40, 420), (200 + bw - 30, 450)], DARK, None, 5)
    for dx in (-36, 36):
        if blink: p.stroke([(200 + dx - 14, 175), (200 + dx + 14, 175)], 5)
        else:
            p.dot(200 + dx, 175, 22, (255, 255, 255), 4); p.dot(200 + dx + look * 8, 177, 9, INK)
            if expr == 'tired': p.stroke([(200 + dx - 20, 160), (200 + dx + 20, 166 if dx < 0 else 154)], 5)
    p.shape([(178, 205), (222, 205), (204, 262), (196, 262)], DARKD, None, 4)
    p.shape([(186, 238), (214, 238), (200, 262)], ORG, None, 3)
    if expr == 'smug': p.arc(200, 282, 20, 10, 20, 160, 5)
    if expr == 'shock': p.dot(200, 290, 12, INK)
    if ovo:
        p.shape(ell_pts(200, 545, 50, 44, 40), hexc('#f3efe2'), hexc('#d8d2bf'), 5, 10)
        # dobra de pele por cima do ovo
        p.shape([(142, 514), (200, 502), (258, 514), (252, 530), (200, 524), (148, 530)], WHITE, WHITED, 4, 6)
    if chick:
        p.shape(ell_pts(200, 520, 50, 60, 40), hexc('#9a9aa2'), hexc('#7a7a84'), 5, 8)
        p.shape(ell_pts(200, 486, 34, 30, 32), WHITE, None, 0, 0)
        for dx in (-14, 14): p.dot(200 + dx, 486, 6, INK)
    return p.img


kit.imperador = imperador
import art as _art; _art.imperador = imperador


def put_imp(c, x, feet, h, f, seed=1, bob=True, **kw):
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'look' in kw: kw['look'] = round(kw['look'] * 4) / 4
    if 'fat' in kw: kw['fat'] = round(kw['fat'] * 8) / 8
    im = sprite('imperador', tuple(sorted(kw.items())), int(h), 400 / 600, False)
    put(c, im, x, feet + (4 * math.sin((f + seed * 5) * .15) if bob else 0))


@lru_cache(maxsize=2)
def ovo_img(size=150):
    p = Pen(200, 240)
    p.shape(ell_pts(100, 128, 76, 100, 40), hexc('#f3efe2'), hexc('#d8d2bf'), 5, 12)
    return p.img.resize((size, int(size * 1.2)), Image.LANCZOS)


@lru_cache(maxsize=4)
def mar_band(luz):
    """faixa de mar gelado no horizonte com blocos de gelo."""
    im = Image.new('RGBA', (1242, 2208), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    col = {'day': (70, 130, 190), 'dusk': (60, 80, 140), 'golden': (90, 120, 160)}[luz]
    d.rectangle((0, 1180, 1242, 1300), fill=col + (255,))
    d.line((0, 1180, 1242, 1180), fill=(36, 23, 38, 255), width=6)
    for x in (120, 480, 900):
        d.polygon([(x, 1240), (x + 60, 1210), (x + 150, 1220), (x + 170, 1250)], fill=(240, 246, 250, 255), outline=(36, 23, 38, 255))
    return im


def flocos(c, f, n=26, seed=2):
    d = ImageDraw.Draw(c)
    rnd = random.Random(seed)
    for i in range(n):
        x0, sp, r = rnd.uniform(0, 1242), rnd.uniform(4, 9), rnd.uniform(6, 12)
        y = (rnd.uniform(0, 2208) + f * sp) % 2208
        x = x0 + 30 * math.sin((f + i * 7) * .05)
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, 220))


def SFX(s):
    s.ting(s.W(0, 'pai'), .3)
    s.thunk(s.W(1, 'ovo') - 2, 300, .5); s.whoosh(s.W(1, 'passa') - 4, .4, .4); s.splash(s.W(1, 'mar'), .4)
    s.thunk(s.W(2, 'meses') - 2, 200, .5); s.thunk(s.W(2, 'nada') - 2, 140, .6)
    s.thunk(s.W(3, 'congela') - 2, 300, .8); s.thunk(s.W(3, 'cinquenta') - 2, 120, .9)
    s.ting(s.W(4, 'magrinho'), .25); s.trill(s.W(4, 'jantar'), 1.0, .3)


def s0(f):
    c = CEN('neve', 'day').copy()
    k = wt(0, 'pai') - 3
    put_imp(c, 621, 1700, 900, f, 1, ovo=1, look=.0, expr='smug' if f >= k else 'calm')
    if f >= k: paste_c(c, txt('PAPAI!', 120, 8), 930, 820, back(ramp(f, k, k + 8)))
    z = lerp(1.35, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1280, z, 0), 'day'


def s1(f):
    c = CEN('neve', 'day').copy()
    c.alpha_composite(mar_band('day'))
    o = wt(1, 'ovo') - 3
    pa = wt(1, 'passa') - 3
    m = wt(1, 'mar') - 3
    # ovo aparece nos pés da mãe, escorrega para o pai
    t = smooth(ramp(f, pa, pa + 14))
    mx = 820 if f < pa + 16 else lerp(820, 1300, smooth(ramp(f, pa + 16, m + 24)))
    put_imp(c, 380, 1700, 640, f, 2, ovo=1 if f >= pa + 14 else 0, look=.75)
    put_imp(c, mx, 1700, 600, f, 3, look=-.75 if f < pa + 16 else .75)
    if o <= f < pa + 14:
        ex = lerp(820, 380, t); ey = 1690 - 120 * math.sin(math.pi * t)
        paste_c(c, ovo_img(80), ex, ey - 30, back(ramp(f, o, o + 6)))
    if f >= m: paste_c(c, txt('VOU COMER!', 90, -6), 900, 980, back(ramp(f, m, m + 8)))
    z = 1.08 * (1 + .0009 * f)
    return c, (lerp(600, 680, smooth(ramp(f, 0, 120))), 1330, z, 0), 'day'


def s2(f):
    c = CEN('neve', 'golden').copy()
    me = wt(2, 'meses') - 3
    n = wt(2, 'nada') - 3
    spin = f / 40
    paste_c(c, clock_img(round(spin * 2 * 8) / 8, round(spin * 24 * 4) / 4, 240), 980, 560)
    put_imp(c, 560, 1720, 900, f, 4, ovo=1, look=.25, expr='tired' if f >= n else 'calm')
    if f >= me: paste_c(c, txt('2 MESES', 100, -6), 620, 520, back(ramp(f, me, me + 8)))
    if f >= n: paste_c(c, txt('NADA!', 110, 6), 940, 900, back(ramp(f, n, n + 8)))
    flocos(c, f)
    # grua: do relógio até os pés com o ovo
    t = smooth(ramp(f, 4, 60))
    return c, (lerp(700, 600, t), lerp(900, 1350, t), lerp(1.3, 1.15, t) * (1 + .0009 * f), 0), 'golden'


def s3(f):
    c = CEN('neve', 'dusk').copy()
    g = wt(3, 'gelo') - 3
    cg = wt(3, 'congela') - 3
    ci = wt(3, 'cinquenta') - 3
    lift = smooth(ramp(f, g - 4, g + 6)) * (1 - smooth(ramp(f, cg + 18, cg + 28)))
    put_imp(c, 621, 1720, 820, f, 5, ovo=1 if lift < .05 else 0, look=.0, expr='shock' if lift > .05 else 'calm', bob=False)
    if lift >= .05:
        oy = 1700 - 60 * (1 - lift) + 60 * lift
        froz = f >= cg
        paste_c(c, ovo_img(120), 621, oy - 60)
        if froz:
            d = ImageDraw.Draw(c)
            a = int(160 * back(ramp(f, cg, cg + 6)))
            d.ellipse((540, oy - 150, 702, oy + 40), fill=(150, 210, 255, max(0, min(160, a))), outline=(36, 23, 38, 255), width=5)
            paste_c(c, txt('CONGELA!', 100, -5), 621, 1480, back(ramp(f, cg, cg + 8)))
    if f >= ci: paste_c(c, txt('-50 °C', 130, 6), 621, 850, back(ramp(f, ci, ci + 8)))
    flocos(c, f, 30, 5)
    k = kick(f, cg, .8)
    z = lerp(1.1, 1.5, smooth(ramp(f, 0, 50))) * (1 + .0009 * f)
    return c, (621, lerp(1250, 1380, smooth(ramp(f, 0, 50))) + k * 10, z, k), 'dusk'


def s4(f):
    c = CEN('neve', 'dusk').copy()
    c.alpha_composite(mar_band('dusk'))
    mg = wt(4, 'magrinho') - 3
    j = wt(4, 'jantar') - 3
    # mãe chega da esquerda
    mx = lerp(-200, 330, smooth(ramp(f, 0, 30)))
    put_imp(c, mx, 1700, 620, f, 6, look=.75, expr='smug', ovo=1 if f >= j else 0)
    fat = lerp(1.0, 0.25, smooth(ramp(f, mg - 4, mg + 6)))
    px = 820 if f < j else lerp(820, 1500, smooth(ramp(f, j, j + 40)))
    hop = 18 * abs(math.sin(f * .6)) if f >= j else 0
    put_imp(c, px, 1700 - hop, 640, f, 7, ovo=1 if f < j else 0, fat=fat, look=-.75 if f < j else .75, expr='tired' if f < j else 'smug')
    if mg <= f < j: paste_c(c, txt('MAGRINHO...', 80, -6), 820, 960, back(ramp(f, mg, mg + 8)))
    if f >= j: paste_c(c, txt('JANTAR!', 120, 6), 760, 760, back(ramp(f, j, j + 8)))
    z = lerp(1.05, 1.2, smooth(ramp(f, 0, 100))) * (1 + .0009 * f)
    return c, (lerp(600, 700, smooth(ramp(f, 0, 100))), 1320, z, 0), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
