"""Formato DESENHO: por que o ícone de salvar é um disquete (Curiosidades da IA, 06/11/2026, 18h). Categoria: TECNOLOGIA.
Fatos: Computerworld 2010 "Sony to halt floppy disk sales in 2011" (procura caiu; pico da procura em meados dos anos 90;
o disco mais popular, 'HD', guardava 1,44 MB; a Sony era uma das poucas que ainda vendiam, com 70% do mercado japonês;
fim das vendas em março de 2011); ABC News (Austrália), 10/07/2024, e The Star / Reuters, 08/07/2024: o governo do Japão
eliminou mais de mil regras e procedimentos que exigiam disquete, em 28 de junho de 2024; disquete padrão = 1,44 MB.
Foto de celular hoje: arquivo JPEG/HEIC costuma ter de 2 a 5 MB (por isso 'muitas vezes nem cabe')."""
from kit import *
import kit

LINES = [
    "O botão de salvar é o desenho de uma coisa que quase ninguém usa mais.",
    "É um disquete: um quadradinho de plástico onde, nos anos noventa, a gente guardava os arquivos do computador.",
    "Cabia só um vírgula quatro megabytes. Hoje, uma única foto de celular muitas vezes nem cabe nele.",
    "Em dois mil e onze, uma das últimas grandes fabricantes parou de vender disquete.",
    "E o governo do Japão ainda exigia disquete em mais de mil regras... até dois mil e vinte e quatro!",
    "Você vê, o desenho ficou porque virou símbolo: todo mundo entende que ele quer dizer salvar.",
    "Ou seja: tem gente que clica no disquete todo dia... sem nunca ter visto um.",
]
CAPTXT = [
    "O botão de salvar é o desenho de uma coisa|que quase ninguém usa mais.",
    "É um disquete: um quadradinho de plástico onde, nos anos 90,|a gente guardava os arquivos do computador.",
    "Cabia só 1,4 megabytes.|Hoje, uma única foto de celular muitas vezes nem cabe nele.",
    "Em 2011, uma das últimas grandes fabricantes|parou de vender disquete.",
    "E o governo do Japão ainda exigia disquete em mais de mil regras...|até 2024!",
    "Você vê, o desenho ficou porque virou símbolo:|todo mundo entende que ele quer dizer salvar.",
    "Ou seja: tem gente que clica no disquete todo dia...|sem nunca ter visto um.",
]
FALA_TIKTOK = "Você já usou um disquete? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [1, 2]
CHECK = [(0, 'ninguem', 6), (1, 'disquete', 4), (1, 'guardava', 6), (2, 'megabytes', 4), (2, 'cabe', 4), (3, 'parou', 6),
         (4, 'mil', 4), (4, 'quatro', 6), (5, 'simbolo', 4), (5, 'salvar', 4), (6, 'clica', 4), (6, 'visto', 8)]

AZ, AZD = hexc('#3a4a8c'), hexc('#27325f')


# ------------------------------------------------------------------ personagens e objetos novos
def jovem(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=2, hair='#2b2b2b', shirt='#ff8a5c', tie=False):
    """pessoa de camiseta e calça jeans (600x1000, pés em y≈975)."""
    p = Pen(600, 1000)
    sh, shd = hexc(shirt), mul(hexc(shirt), .78)
    for s in (-1, 1):
        top = (300 + s * 40, 690); ft = (300 + s * 44, 950)
        p.line([top, (top[0] + s * 4, 820), ft], hexc('#3d5a8a'), 22, 4)
        p.shape(ell_pts(ft[0] + 12, ft[1] + 10, 36, 18), hexc('#f2f2f2'), hexc('#c9c9c9'), 4, 4)
    p.shape([(212, 640), (388, 640), (396, 712), (204, 712)], hexc('#3d5a8a'), hexc('#2c4268'), 5, 8)
    p.line([(300, 350), (300, 430)], SKINS[skin], 40, 4)
    tc = (300 + tilt * 3, 560)
    p.shape(ell_pts(tc[0], tc[1], 112, 140, 56, math.radians(tilt), 0.12), sh, shd, 5, 16)
    p.arc(300, 420, 40, 22, 10, 170, 5)
    if tie:
        p.poly([(288, 430), (312, 430), (322, 560), (300, 590), (278, 560)], hexc('#c0392b'), 3)
    shL, shR = (205, 470), (395, 470)
    A = {'hang': [((185, 560), (190, 650)), ((415, 560), (410, 650))],
         'point': [((185, 560), (190, 650)), ((470, 430), (560, 380))],
         'type': [((175, 570), (250, 620)), ((425, 570), (350, 620))],
         'cheek': [((150, 420), (225, 300)), ((450, 420), (375, 300))],
         'shrug': [((140, 540), (120, 440)), ((460, 540), (480, 440))],
         'up': [((150, 380), (140, 240)), ((450, 380), (460, 240))]}[arms]
    for s_, (el, hd) in zip((shL, shR), A):
        p.line(curve(s_, el, hd, 10), SKINS[skin], 15, 4)
        p.dot(hd[0], hd[1], 17, SKINS[skin], 4)
    hc = (300 + tilt * 6, 262)
    hcol = hexc(hair)
    p.shape(ell_pts(hc[0], hc[1] - 30, 124, 100, 48), hcol, mul(hcol, .7), 5, 10)
    p.shape(ell_pts(hc[0], hc[1], 118, 106, 56, math.radians(tilt * 1.5), 0.08, 2.4), SKINS[skin], mul(SKINS[skin], .86), 5, 16)
    p.dot(hc[0] - 112, hc[1] + 10, 16, SKINS[skin], 4); p.dot(hc[0] + 112, hc[1] + 10, 16, SKINS[skin], 4)
    fr = [(hc[0] - 122, hc[1] - 6), (hc[0] - 116, hc[1] - 84), (hc[0] - 50, hc[1] - 118), (hc[0] + 50, hc[1] - 118), (hc[0] + 116, hc[1] - 84),
          (hc[0] + 122, hc[1] - 10), (hc[0] + 80, hc[1] - 56), (hc[0] + 20, hc[1] - 74), (hc[0] - 50, hc[1] - 60), (hc[0] - 96, hc[1] - 36)]
    p.shape(fr, hcol, mul(hcol, .7), 5, 8)
    face(p, hc[0], hc[1] + 10, expr, blink, look)
    return p.img


def put_jovem(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'jovem', x, feet, h, f, seed, **kw)


def disquete(expr='calm', blink=0, look=0.5, face_on=True):
    """disquete 3,5 polegadas (400x400) com carinha opcional."""
    p = Pen(400, 400)
    body = [(30, 30), (330, 30), (370, 70), (370, 370), (30, 370)]
    p.shape(body, AZ, AZD, 6, 18)
    p.shape([(110, 30), (290, 30), (290, 140), (110, 140)], hexc('#c9ced8'), hexc('#9aa1ad'), 5, 6)  # metal
    p.poly([(230, 48), (266, 48), (266, 124), (230, 124)], AZD, 3)
    p.shape([(80, 200), (320, 200), (320, 370), (80, 370)], hexc('#f4f1e8'), hexc('#d8d3c4'), 5, 6)  # etiqueta
    for y in (240, 280): p.stroke([(110, y), (290, y)], 4, hexc('#b7b0a0'))
    if face_on:
        for dx in (-50, 50):
            ex, ey = 200 + dx, 300
            if blink > .6: p.stroke([(ex - 18, ey), (ex + 18, ey)], 6)
            else:
                r = 28 if expr == 'shock' else 22
                p.dot(ex, ey, r, (255, 255, 255), 5)
                p.dot(ex + look * 8, ey + 2, 10 if expr != 'shock' else 7, INK)
        if expr == 'shock': p.dot(200, 345, 13, hexc('#7a2e2e'), 4)
        elif expr == 'sad': p.arc(200, 356, 24, 12, 200, 340, 6)
        else: p.arc(200, 330, 24, 12, 20, 160, 6)
    return p.img


def put_disk(c, x, y, size, f, seed=1, rot=0, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('disquete', tuple(sorted(kw.items())), int(size), 1.0, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def crt(expr='calm', blink=0, look=0.0, slot=0.0):
    """computador antigo (monitor de tubo + gabinete) com carinha na tela (700x700)."""
    p = Pen(700, 700)
    beige, bd = hexc('#e8dcc0'), hexc('#c4b48e')
    p.shape([(90, 470), (610, 470), (630, 660), (70, 660)], beige, bd, 6, 12)  # gabinete
    p.shape([(370, 530), (560, 530), (560, 560), (370, 560)], hexc('#3a3236'), None, 4)  # entrada do disquete
    p.shape([(130, 40), (570, 40), (590, 440), (110, 440)], beige, bd, 6, 16)  # monitor
    p.shape([(170, 80), (530, 80), (545, 390), (155, 390)], hexc('#1f3a2e'), None, 5)
    for dx in (-70, 70):
        ex, ey = 350 + dx, 220
        if blink > .6: p.stroke([(ex - 22, ey), (ex + 22, ey)], 8, hexc('#7dff9a'))
        else:
            p.dot(ex, ey, 30 if expr == 'shock' else 26, hexc('#7dff9a'))
            p.dot(ex + look * 8, ey + 2, 11, hexc('#1f3a2e'))
    if expr in ('grin', 'happy'): p.arc(350, 290, 50, 30, 20, 160, 8, hexc('#7dff9a'))
    elif expr == 'shock': p.dot(350, 315, 20, hexc('#7dff9a'))
    else: p.stroke([(320, 310), (380, 310)], 8, hexc('#7dff9a'))
    return p.img


def laptop(icon=1.0, glow=0.0):
    """notebook visto de frente com o ícone de salvar na tela (700x520)."""
    p = Pen(700, 520)
    p.shape([(120, 20), (580, 20), (580, 380), (120, 380)], hexc('#3b3f4a'), hexc('#2a2d35'), 6, 10)
    p.poly([(145, 45), (555, 45), (555, 355), (145, 355)], hexc('#eaf2ff') if glow < .5 else hexc('#fff6c8'))
    p.shape([(40, 380), (660, 380), (690, 470), (10, 470)], hexc('#b9bec9'), hexc('#8d93a0'), 6, 8)
    return p.img


@lru_cache(maxsize=4)
def laptop_img(w=700, glow=0):
    im = laptop(glow=glow).resize((w, int(w * 520 / 700)), Image.LANCZOS)
    ic = disquete(face_on=False).resize((int(w * .3), int(w * .3)), Image.LANCZOS)
    im.alpha_composite(ic, (int(w / 2 - ic.size[0] / 2), int(w * 200 / 700 - ic.size[1] / 2)))
    return im


@lru_cache(maxsize=2)
def quarto_bg(night=False):
    W, H, fy = BW, BH, 1560
    p = Pen(W, H)
    p.poly([(0, 0), (W, 0), (W, fy), (0, fy)], hexc('#f3e3c3') if not night else hexc('#c9b6a0'))
    for x in range(0, W, 90): p.stroke([(x, 0), (x, fy)], 3, hexc('#ead5ae'))
    p.poly([(0, fy), (W, fy), (W, H), (0, H)], hexc('#b48a5a'))
    for y in range(fy + 60, H, 110): p.stroke([(0, y), (W, y)], 4, hexc('#9a7347'))
    p.stroke([(0, fy), (W, fy)], 8)
    # janela
    p.shape([(780, 360), (1140, 360), (1140, 760), (780, 760)], hexc('#f7f7f2'), None, 6)
    p.poly([(805, 385), (1115, 385), (1115, 735), (805, 735)], hexc('#9fd3ff'))
    p.stroke([(960, 385), (960, 735)], 10, hexc('#f7f7f2')); p.stroke([(805, 560), (1115, 560)], 10, hexc('#f7f7f2'))
    # quadro na parede
    p.shape([(140, 420), (420, 420), (420, 640), (140, 640)], hexc('#8a5a3a'), None, 6)
    p.poly([(165, 445), (395, 445), (395, 615), (165, 615)], hexc('#8fd6a0'))
    p.poly([(165, 615), (260, 520), (330, 580), (395, 500), (395, 615)], hexc('#4c9a5c'))
    return p.img.resize((W, H), Image.LANCZOS)


def mesa(c, y, x0=60, x1=1180):
    p = Pen(x1 - x0 + 40, 420)
    p.shape([(20, 20), (x1 - x0 + 20, 20), (x1 - x0 + 20, 70), (20, 70)], hexc('#9a6b3d'), hexc('#74502c'), 5, 8)
    for x in (60, x1 - x0 - 20): p.shape([(x - 20, 70), (x + 20, 70), (x + 20, 400), (x - 20, 400)], hexc('#8a5f35'), hexc('#65452a'), 5, 6)
    c.alpha_composite(p.img, (x0 - 20, int(y) - 20))


@lru_cache(maxsize=2)
def foto_img(w=300):
    p = Pen(300, 360)
    p.shape([(20, 20), (280, 20), (280, 340), (20, 340)], (255, 255, 255), hexc('#dddddd'), 5, 6)
    p.poly([(40, 40), (260, 40), (260, 260), (40, 260)], hexc('#9fd3ff'))
    p.poly([(40, 260), (110, 160), (170, 220), (220, 150), (260, 200), (260, 260)], hexc('#4cc36a'))
    p.dot(210, 90, 26, hexc('#ffd84a'), 3)
    return p.img.resize((w, int(w * 1.2)), Image.LANCZOS)


@lru_cache(maxsize=4)
def fabrica_img(smoke=1):
    p = Pen(900, 760)
    p.shape([(60, 330), (840, 330), (840, 740), (60, 740)], hexc('#c9b8a6'), hexc('#a08d78'), 6, 14)
    for i in range(4):
        x = 60 + i * 195
        p.shape([(x, 330), (x + 195, 230), (x + 195, 330)], hexc('#a65a4a'), hexc('#7d4034'), 5, 8)
    p.shape([(680, 150), (760, 150), (760, 330), (680, 330)], hexc('#8a6a5a'), hexc('#6a4f42'), 5, 8)
    for i, x in enumerate((140, 330, 520)):
        p.shape([(x, 450), (x + 120, 450), (x + 120, 560), (x, 560)], hexc('#9fd3ff'), None, 4)
    p.shape([(620, 560), (760, 560), (760, 740), (620, 740)], hexc('#6b4a2f'), None, 5)
    if smoke:
        for i, (dx, dy, r) in enumerate(((725, 100, 34), (770, 60, 42), (820, 30, 48))):
            p.dot(dx, dy, r, (235, 235, 235), 4)
    return p.img


@lru_cache(maxsize=2)
def papelada_img():
    """pilhas de papel de regras com disquetes em cima (900x700)."""
    p = Pen(900, 700); rnd = random.Random(8)
    for k, x in enumerate((60, 330, 600)):
        n = 9 + k * 2
        for i in range(n):
            y = 680 - i * 38
            dx = rnd.randint(-10, 10)
            p.shape([(x + dx, y - 34), (x + 240 + dx, y - 34), (x + 240 + dx, y), (x + dx, y)], hexc('#fbfbf6'), hexc('#dddccf'), 3, 4)
            p.stroke([(x + 20 + dx, y - 18), (x + 200 + dx, y - 18)], 3, hexc('#b8b6a8'))
    return p.img


def SFX(s):
    s.ting(s.W(0, 'salvar'), .3)
    s.thunk(s.W(0, 'ninguem') - 2, 180, .6)
    s.whoosh(s.W(1, 'disquete') - 6, .4, .4); s.thunk(s.W(1, 'disquete') - 1, 200, .5)
    s.thunk(s.W(1, 'guardava') - 2, 260, .7)
    s.ting(s.W(2, 'megabytes'), .3)
    s.thunk(s.W(2, 'cabe') - 2, 120, .9)
    s.thunk(s.W(3, 'parou') - 2, 110, .9)
    s.thunk(s.W(4, 'mil') - 2, 160, .7)
    for i in range(4): s.thunk(s.W(4, 'regras') + i * 4, 300, .35)
    s.ting(s.W(4, 'quatro'), .4)
    s.ting(s.W(5, 'salvar'), .35)
    s.thunk(s.W(6, 'clica') - 1, 400, .5)
    s.trill(s.W(6, 'visto'), .9, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = quarto_bg().copy()
    mesa(c, 1500)
    s0_ = wt(0, 'salvar') - 3
    n0 = wt(0, 'ninguem') - 3
    put_jovem(c, 340, 2120, 1050, f, 1, arms='type' if f < n0 else 'shrug', expr='neutral' if f < n0 else 'nervous', look=1)
    lw = laptop_img(560)
    paste_c(c, lw, 820, 1290)
    if f >= s0_:
        paste_c(c, txt('SALVAR', 100, -5), 820, 900, back(ramp(f, s0_, s0_ + 8)))
    if f >= n0: paste_c(c, txt('ISSO É O QUÊ?', 90, 5), 640, 700, back(ramp(f, n0, n0 + 8)))
    t = easeOut(ramp(f, 0, 45))
    kk = kick(f, n0 + 2)
    return c, (lerp(820, 640, t), lerp(1250, 1300, t) + kk * 10, lerp(1.7, 1.1, t), kk), 'day'


def s1(f):
    c = quarto_bg().copy()
    mesa(c, 1500)
    d0 = wt(1, 'disquete') - 3
    g0 = wt(1, 'guardava') - 3
    a0 = wt(1, 'noventa') - 3
    paste_c(c, sprite('crt', (('blink', 1 if blinkAt(f, 2) > .6 else 0), ('expr', 'grin' if f >= g0 + 8 else 'calm'), ('look', 0.0), ('slot', 0.0)), 640, 1.0, False), 780, 1180)
    if f >= d0:
        if f < g0:
            put_disk(c, 340, 1100 + 20 * math.sin(f * .3), 300 * back(ramp(f, d0, d0 + 8)), f, 1, expr='calm', look=1)
        else:
            u = smooth(ramp(f, g0, g0 + 12))
            sz = lerp(300, 120, u)
            if u < 1: put_disk(c, lerp(340, 860, u), lerp(1100, 1385, u), sz, f, 1, rot=-90 * u, expr='grin', look=1)
        if f < min(g0, a0): paste_c(c, txt('DISQUETE', 110, -5), 640, 650, back(ramp(f, d0, d0 + 8)))
    if f >= a0: paste_c(c, txt('ANOS 90', 110, 5), 640, 820, back(ramp(f, a0, a0 + 8)))
    z = lerp(1.05, 1.18, smooth(f / 150))
    return c, (640, 1200, z, 0), 'golden'


def s2(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(.7))
    m0 = wt(2, 'megabytes') - 3
    f0 = wt(2, 'foto') - 3
    cb = wt(2, 'cabe') - 3
    put_disk(c, 440, 1250, 460, f, 1, expr='calm' if f < cb else 'shock', look=1)
    if m0 <= f < f0: paste_c(c, txt('1,4 MB', 130, -5), 440, 760, back(ramp(f, m0, m0 + 8)))
    if f >= f0:
        g = lerp(.4, 1.25, easeOut(ramp(f, f0, cb + 4)))
        paste_c(c, foto_img(), 880, 1250, g * back(ramp(f, f0, f0 + 6)) if f < f0 + 6 else g)
        if f < cb: paste_c(c, txt('FOTO DE CELULAR', 76, 5), 640, 760, back(ramp(f, f0, f0 + 8)))
    if f >= cb: paste_c(c, txt('NÃO CABE!', 120, 6), 640, 760, back(ramp(f, cb, cb + 8)))
    kk = kick(f, cb + 2)
    z = lerp(1.05, 1.15, smooth(f / 120))
    return c, (640, 1220 + kk * 10, z, kk), 'day'


def s3(f):
    c = BG('golden').copy()
    a0 = wt(3, 'onze') - 3
    p0 = wt(3, 'parou') - 3
    paste_c(c, fabrica_img(1 if f < p0 else 0).resize((700, 591), Image.LANCZOS), 560, 1450)
    if f >= a0: paste_c(c, txt('2011', 140, -5), 640, 650, back(ramp(f, a0, a0 + 8)))
    if f >= p0:
        paste_c(c, txt('FECHADO', 100, 6), 560, 1480, back(ramp(f, p0, p0 + 8)))
    # disquetes tristes saindo da porta
    for i in range(3):
        x = 640 + i * 150 + (max(0, f - p0) * 3 if f >= p0 else 0)
        put_disk(c, min(x, 1500), 1690 - (i % 2) * 20, 170, f, i + 3, expr='calm' if f < p0 else 'sad', look=1)
    z = lerp(1.0, 1.12, smooth(f / 120))
    return c, (640, 1300, z, 0), 'golden'


def s4(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    j0 = wt(4, 'japao') - 3
    m0 = wt(4, 'mil') - 3
    q0 = wt(4, 'quatro') - 3
    pa = papelada_img()
    s = back(ramp(f, m0, m0 + 10)) if f >= m0 else 0
    if s > .02:
        im = pa.resize((900, max(1, int(700 * s))))
        c.alpha_composite(im, (170, 1420 - im.size[1]))
    for i, x in enumerate((300, 560, 820)):
        if f >= j0 + i * 3: put_disk(c, x, 1420 - 700 * s - 60 if s > .02 else 1350, 140, f, 6 + i, rot=8 - i * 8, expr='calm', look=0)
    put_jovem(c, 640, 2120, 900, f, 4, arms='hang' if f < q0 else 'up', expr='neutral' if f < m0 else ('shock' if f < q0 else 'grin'),
              tie=True, shirt='#f2f2f2', hair='#1e1e1e', skin=0, look=0)
    if j0 <= f < m0: paste_c(c, txt('JAPÃO', 120, -5), 640, 520, back(ramp(f, j0, j0 + 8)))
    if m0 <= f < q0: paste_c(c, txt('+ DE 1.000 REGRAS', 84, -5), 640, 520, back(ramp(f, m0, m0 + 8)))
    if f >= q0: paste_c(c, txt('ATÉ 2024!', 120, 6), 640, 520, back(ramp(f, q0, q0 + 8)))
    kk = kick(f, q0 + 2)
    z = lerp(1.05, 1.12, smooth(f / 150))
    return c, (640, 1240 + kk * 10, z, kk), 'day'


def s5(f):
    c = quarto_bg().copy()
    mesa(c, 1500)
    s0_ = wt(5, 'simbolo') - 3
    v0 = wt(5, 'salvar') - 3
    put_jovem(c, 340, 2120, 1050, f, 1, arms='cheek', expr='neutral' if f < v0 else 'grin', look=1)
    paste_c(c, laptop_img(560, 1 if f >= v0 else 0), 820, 1290)
    cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
    cont.alpha_composite(disquete(face_on=False).resize((240, 240), Image.LANCZOS), (30, 30))
    thought(c, 760, 720, 230, back(ramp(f, s0_ - 6, s0_ + 4)), cont)
    if f >= v0: paste_c(c, txt('= SALVAR', 110, 5), 760, 1000, back(ramp(f, v0, v0 + 8)))
    z = lerp(1.05, 1.22, smooth(f / 120))
    return c, (680, 1180, z, lerp(0, -2, smooth(f / 120))), 'dusk'


def s6(f):
    c = quarto_bg().copy()
    mesa(c, 1500)
    k = wt(6, 'clica') - 3
    v = wt(6, 'sem') - 3
    put_jovem(c, 340, 2120, 1050, f, 1, arms='type' if f < v else 'cheek', expr='grin' if f < v else 'shock', look=1)
    paste_c(c, laptop_img(560, 1 if k <= f < k + 6 else 0), 820, 1290)
    if k <= f < v: paste_c(c, txt('CLIC!', 100, -6), 900, 900, back(ramp(f, k, k + 6)))
    if f >= v:
        put_disk(c, 820, 900 + 10 * math.sin(f * .2), 260 * back(ramp(f, v, v + 8)), f, 2, expr='calm', look=-1)
        paste_c(c, txt('?', 160, 10), 580, 1080, back(ramp(f, v + 6, v + 14)))
    z = lerp(1.08, 1.3, easeOut(ramp(f, 0, 70)))
    return c, (620, 1250, z, lerp(0, 2.5, smooth(ramp(f, 0, 70)))), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
