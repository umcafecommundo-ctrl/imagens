"""Formato DESENHO: os tubarões são mais velhos que as árvores (Curiosidades da IA, 20/11/2026, 07h).
Categoria: ANIMAIS.
Fatos: Live Science, "Are sharks really older than trees?" (os tubarões mais antigos têm ~450 milhões de anos, pelas
escamas fósseis; as primeiras árvores, ~385-390 milhões de anos); BBC Discover Wildlife, "This prehistoric apex
predator is older than trees" (biólogo: tubarões ~450 milhões de anos, árvores ~385 milhões); EarthDate (Univ. do
Texas) sobre as primeiras florestas no Devoniano; antes das árvores a terra tinha só plantas baixas (musgos e hepáticas).
Cenários: s0 museu (Professor apresenta o tubarão e a árvore) | s1 fundo do mar (tubarão nada, 450 milhões de anos) |
s2 terra antiga sem árvores, só musgo (desenhada aqui) | s3 floresta no fim de tarde (tempo passando, árvores crescem) |
s4 fundo do mar ao entardecer (tubarão veterano vê a arvorezinha num balão) | s5 praia ao entardecer (Professor + barbatana)."""
from kit import *
from functools import lru_cache

LINES = [
    "Os tubarões são mais velhos que as árvores.",
    "Eles já nadavam no mar há cerca de quatrocentos e cinquenta milhões de anos.",
    "Nessa época, a terra não tinha nenhuma árvore. Só musguinho.",
    "As primeiras árvores só apareceram uns sessenta milhões de anos depois.",
    "Você vê, quando a primeira árvore nasceu, o tubarão já era veterano.",
    "Ou seja: o tubarão é mais antigo que qualquer floresta.",
]
CAPTXT = [
    "Os tubarões são mais velhos que as árvores.",
    "Eles já nadavam no mar há cerca de|450 milhões de anos.",
    "Nessa época, a terra não tinha nenhuma árvore.|Só musguinho.",
    "As primeiras árvores só apareceram|uns 60 milhões de anos depois.",
    "Você vê, quando a primeira árvore nasceu,|o tubarão já era veterano.",
    "Ou seja: o tubarão é mais antigo que qualquer floresta.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 4
FLASH = [3]
CHECK = [(0, 'arvores', 4), (1, 'quatrocentos', 6), (2, 'musguinho', 6), (3, 'sessenta', 6), (4, 'veterano', 6),
         (5, 'floresta', 8)]

SH = hexc('#7f97ad'); SHD = hexc('#5b7187'); BEL = hexc('#eef2f4')
TRUNK = hexc('#8a5a32'); TRUNKD = hexc('#653f20'); LEAF = hexc('#4fae4a'); LEAFD = hexc('#357e33')
MOSS = hexc('#6cbf4a'); MOSSD = hexc('#468a30')


def SFX(s):
    s.whoosh(s.W(0, 'tubaroes') - 6, .4, .4)
    s.thunk(s.W(0, 'velhos') - 2, 200, .6); s.ting(s.W(0, 'arvores'), .3)
    s.splash(s.W(1, 'nadavam') - 4, .3)
    s.patter(s.W(1, 'mar'), s.W(1, 'mar') + 40, 8, .08)
    s.thunk(s.W(1, 'quatrocentos') - 2, 140, .9)
    s.whoosh(s.W(2, 'terra') - 4, .3, .3)
    s.thunk(s.W(2, 'nenhuma') - 2, 260, .5)
    for i in range(3): s.thunk(s.W(2, 'musguinho') - 2 + i * 5, 520, .3)
    for i in range(5): s.thunk(s.W(3, 'arvores') - 2 + i * 4, 180, .45)
    s.ting(s.W(3, 'sessenta'), .3)
    s.ting(s.W(4, 'nasceu'), .3); s.thunk(s.W(4, 'veterano') - 2, 160, .7)
    s.trill(s.W(5, 'floresta'), 1.0, .3)


def tubarao(mouth=0.0, blink=0, look=0.3, expr='calm', tail=0.0):
    """tubarão de lado, 800x420, olhando para a direita. tail = -1..1 balanço do rabo."""
    p = Pen(800, 420)
    ty = 40 * tail
    # rabo
    p.shape([(150, 215), (40, 70 + ty), (80, 210), (50, 330 + ty), (150, 235)], SH, SHD, 6, 10)
    # barbatana de cima
    p.shape([(330, 140), (400, 30), (450, 145)], SH, SHD, 6, 10)
    # barbatana de baixo de trás
    p.shape([(260, 270), (230, 330), (320, 280)], SHD, None, 5)
    # corpo
    body = [(140, 225)] + [(140 + 600 * t, 225 - 100 * math.sin(math.pi * t ** .85) ** .9) for t in np.linspace(0, 1, 26)][1:] + \
           [(140 + 600 * t, 225 + 85 * math.sin(math.pi * t ** .85) ** .9) for t in np.linspace(1, 0, 26)][1:]
    p.shape(body, SH, SHD, 7, 18)
    # barriga clara
    belly = [(200, 240)] + [(200 + 520 * t, 240 + 62 * math.sin(math.pi * t ** .8)) for t in np.linspace(0, 1, 20)][1:] + \
            [(200 + 520 * t, 250 + 20 * math.sin(math.pi * t)) for t in np.linspace(1, 0, 14)][1:]
    p.shape(belly, BEL, hexc('#cfd8de'), 0, 6)
    # guelras
    for k in range(3):
        p.arc(560 - k * 24, 225, 14, 40, -60, 60, 4, SHD)
    # nadadeira peitoral
    p.shape([(470, 270), (420, 360), (530, 285)], SH, SHD, 6, 8)
    # olho grande
    ex, ey = 640, 190
    if blink > .6:
        p.stroke([(ex - 22, ey), (ex + 22, ey)], 6)
    else:
        r = 30 if expr == 'shock' else 26
        p.dot(ex, ey, r, (255, 255, 255), 5)
        p.dot(ex + 4 + look * 8, ey + 2, 11, INK); p.dot(ex + look * 8, ey - 4, 4, (255, 255, 255))
        if expr in ('smug', 'side'): p.stroke([(ex - 28, ey - 14), (ex + 28, ey - 14)], 7)
    # boca com dentinhos
    my = 262
    if mouth > .1:
        p.shape([(600, my), (720, my - 6), (700, my + 30 * mouth)], hexc('#7a2e2e'), None, 5)
        for x in (630, 655, 680):
            p.shape([(x, my - 2), (x + 10, my - 2), (x + 5, my + 10)], (255, 255, 255), None, 2)
    else:
        p.arc(665, my - 20, 50, 16, 20, 160, 5)
    return p.img


def put_tub(c, x, y, h, flip=False, **kw):
    put_sprite(c, 'tubarao', x, y, h, 800 / 420, flip, {'mouth': 4, 'look': 4, 'tail': 6}, **kw)


@lru_cache(maxsize=8)
def arvore_img(h):
    h = int(h)
    p = Pen(500, 800)
    p.shape([(220, 790), (230, 420), (270, 420), (285, 790)], TRUNK, TRUNKD, 6, 10)
    for cx, cy, r in ((250, 330, 170), (150, 410, 110), (350, 410, 110), (250, 200, 130)):
        p.shape(ell_pts(cx, cy, r, r * .85, 36), LEAF, LEAFD, 6, 16)
    return p.img.resize((max(4, int(h * 500 / 800)), max(4, h)), Image.LANCZOS)


def put_arv(c, x, feet, h):
    if h < 8: return
    im = arvore_img(int(h // 4 * 4))
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - im.height)))


@lru_cache(maxsize=2)
def terra_antiga(luz='day'):
    """terra de 450 milhões de anos: mar, rochas, chão marrom, sem árvore nenhuma, só tufos de musgo."""
    c = Image.new('RGBA', (1242, 2208))
    d = ImageDraw.Draw(c)
    top, bot = ((120, 170, 220), (240, 205, 170)) if luz == 'day' else ((70, 70, 120), (240, 160, 120))
    for y in range(0, 1100):
        t = y / 1100
        d.line([(0, y), (1242, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)) + (255,))
    p = Pen(1242, 2208)
    p.shape([(0, 1000), (1242, 1000), (1242, 1250), (0, 1250)], hexc('#3f7fb0'), hexc('#2f6690'), 0, 0)
    for k in range(5):
        y = 1040 + k * 40
        p.stroke([(80 + k * 90, y), (260 + k * 90, y)], 4, hexc('#7fb3d6'))
        p.stroke([(700 - k * 40, y + 20), (900 - k * 40, y + 20)], 4, hexc('#7fb3d6'))
    ground = [(0, 1250)] + [(x, 1220 + 30 * math.sin(x / 140)) for x in range(0, 1243, 40)] + [(1242, 2208), (0, 2208)]
    p.shape(ground, hexc('#a07850'), hexc('#7d5a38'), 6, 20)
    # montanhas peladas ao fundo
    p.shape([(700, 1010), (900, 760), (1080, 900), (1242, 800), (1242, 1010)], hexc('#8d7a6a'), hexc('#6d5c4f'), 5, 14)
    rnd = random.Random(3)
    for i in range(9):
        x = rnd.randint(60, 1180); y = rnd.randint(1350, 2100)
        p.shape(ell_pts(x, y, rnd.randint(40, 90), rnd.randint(25, 50), 24), hexc('#9a958c'), hexc('#76726a'), 5, 10)
    for i in range(16):
        x = rnd.randint(40, 1200); y = rnd.randint(1300, 2150)
        for j in range(4):
            p.shape(ell_pts(x + j * 22 - 33, y - 8 * math.sin(j * 1.3), 20, 14, 16), MOSS, MOSSD, 4, 4)
    c.alpha_composite(p.img.resize((1242, 2208), Image.LANCZOS))
    return c


def broto(c, x, feet, s):
    if s <= .05: return
    p = Pen(200, 300)
    p.stroke([(100, 290), (100, 120)], 10, TRUNKD)
    p.shape(ell_pts(70, 120, 40, 22, 20, rot=.4), LEAF, LEAFD, 5, 6)
    p.shape(ell_pts(130, 100, 40, 22, 20, rot=-.4), LEAF, LEAFD, 5, 6)
    im = p.img.resize((max(4, int(140 * s)), max(4, int(210 * s))), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - im.height)))


def bolhas(c, f, x0, y0):
    for i in range(6):
        a = (f * 3 + i * 37) % 220
        r = 8 + (i % 3) * 4
        x = x0 + 30 * math.sin((f + i * 20) * .08) + i * 14; y = y0 - a
        ImageDraw.Draw(c).ellipse((x - r, y - r, x + r, y + r), outline=(255, 255, 255, 200), width=4)


def s0(f):
    c = CEN('museu', 'day').copy()
    v_ = wt(0, 'velhos') - 3
    a_ = wt(0, 'arvores') - 3
    put_tub(c, 860, 1080 + 12 * math.sin(f * .12), 380 * back(ramp(f, 2, 12)), flip=False, tail=math.sin(f * .3),
            look=-.6, expr='smug' if f >= v_ else 'calm', blink=blinkAt(f, 3), mouth=.5 * pulse(f, v_, 16))
    put_arv(c, 1010, 1560, 520 * back(ramp(f, a_, a_ + 10)))
    put_prof(c, 330, 1880, 1000, f, expr='shock' if f >= v_ else 'grin', arms='up' if f >= a_ else 'point', look=1)
    if f >= v_: paste_c(c, txt('MAIS VELHOS?!', 92, -5), 700, 560, back(ramp(f, v_, v_ + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1230 + kick(f, v_, .8) * 12, z, 0), 'day'


def s1(f):
    c = CEN('fundo_mar', 'day').copy()
    q_ = wt(1, 'quatrocentos') - 3
    x = lerp(-300, 640, smooth(ramp(f, 0, q_ + 10)))
    put_tub(c, x, 1250 + 30 * math.sin(f * .1), 440, tail=math.sin(f * .35), look=.3, blink=blinkAt(f, 5))
    bolhas(c, f, 300, 1500)
    if f >= q_:
        paste_c(c, txt('450 MILHÕES', 116, -4), 640, 560, back(ramp(f, q_, q_ + 8)))
        paste_c(c, txt('DE ANOS', 96, 4), 640, 720, back(ramp(f, q_ + 4, q_ + 12)))
    z = lerp(1.1, 1.2, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (lerp(560, 680, smooth(ramp(f, 0, 90))), 1150, z, 0), 'day'


def s2(f):
    c = terra_antiga('day').copy()
    n_ = wt(2, 'nenhuma') - 3
    m_ = wt(2, 'musguinho') - 3
    if f >= n_ and f < m_: paste_c(c, txt('NENHUMA ÁRVORE', 84, -4), 640, 760, back(ramp(f, n_, n_ + 8)))
    if f >= m_:
        paste_c(c, txt('SÓ MUSGUINHO', 90, 4), 640, 760, back(ramp(f, m_, m_ + 8)))
    # desce de grua do céu até o chão com musgo
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.0, 1.25, t) * (1 + .0009 * f)
    return c, (640, lerp(1050, 1300, t), z, 0), 'day'


def s3(f):
    c = CEN('floresta', 'golden').copy()
    a_ = wt(3, 'arvores') - 3
    s_ = wt(3, 'sessenta') - 3
    for i, (x, fe, h) in enumerate(((220, 1700, 640), (520, 1760, 760), (820, 1700, 660), (1080, 1780, 720))):
        put_arv(c, x, fe, h * back(ramp(f, a_ + i * 4, a_ + i * 4 + 12)))
        put_dust(c, x, fe - 20, 80, f - a_ - i * 4)
    if f >= s_: paste_c(c, txt('+60 MILHÕES', 110, -4), 640, 600, back(ramp(f, s_, s_ + 8)))
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (640, 1250, z, 0), 'golden'


def s4(f):
    c = CEN('fundo_mar', 'dusk').copy()
    n_ = wt(4, 'nasceu') - 3
    v_ = wt(4, 'veterano') - 3
    put_tub(c, 600, 1350 + 20 * math.sin(f * .1), 520, tail=math.sin(f * .3) * .6, look=.6,
            expr='smug' if f >= v_ else 'calm', blink=blinkAt(f, 2))
    if f >= n_ - 6:
        cont = Image.new('RGBA', (560, 300), (0, 0, 0, 0))
        broto(cont, 280, 290, 1.3)
        thought(c, 860, 620, 280, back(ramp(f, n_ - 6, n_ + 4)), cont)
    if f >= v_: paste_c(c, txt('VETERANO!', 96, -5), 640, 900, back(ramp(f, v_, v_ + 8)))
    bolhas(c, f, 900, 1500)
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (660, 1150, z, lerp(0, 2, t)), 'dusk'


def s5(f):
    c = CEN('praia', 'dusk').copy()
    fl = wt(5, 'floresta') - 3
    # barbatana no mar
    p = Pen(260, 220)
    p.shape([(20, 210), (140, 20), (240, 210)], SH, SHD, 6, 10)
    fin = p.img.resize((180, 152), Image.LANCZOS)
    fx = int(800 + 120 * math.sin(f * .04))
    c.alpha_composite(fin, (fx, 1180 - 152))
    broto(c, 980, 1560, 1.0 + .4 * back(ramp(f, fl, fl + 10)))
    put_prof(c, 380, 1880, 1000, f, expr='grin' if f >= fl else 'smug', arms='shrug' if f >= fl else 'point', look=1)
    if f >= fl:
        paste_c(c, txt('RESPEITA', 96, 4), 660, 560, back(ramp(f, fl, fl + 8)))
        paste_c(c, txt('O TUBARÃO!', 96, 4), 660, 700, back(ramp(f, fl + 3, fl + 11)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (640, lerp(1250, 1200, t) + kick(f, fl, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
