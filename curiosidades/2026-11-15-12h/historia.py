"""Formato DESENHO: por que o lápis é amarelo (Curiosidades da IA, 15/11/2026, 12h).
Categoria: INVENÇÕES E OBJETOS.
Fatos: Mental Floss ("Why Are Pencils Yellow?") e Reader's Digest ("Why Are Pencils Yellow?"): no fim do século 19 a
grafite mais famosa/de melhor qualidade vinha da China; na cultura chinesa o amarelo era ligado à realeza; em 1889 uma
fábrica da Boêmia (hoje República Tcheca) lançou na Exposição Universal de Paris um lápis "de luxo" pintado de amarelo
para sinalizar grafite de primeira; outras fábricas copiaram; a cor não muda em nada a escrita.
Cenários: s0 escola (Professor + lápis gigante) | s1 mapa (China, grafite) | s2 museu (coroa e manto amarelo da realeza) |
s3 fábrica (lápis pintado de amarelo, 1889, Paris) | s4 fábrica (selo "digno de rei") | s5 fábrica (outras fábricas copiam) |
s6 escola ao entardecer (Professor escreve: a cor não muda nada) | s7 escola ao entardecer (lápis de coroa, Professor ri)."""
from kit import *

LINES = [
    "O lápis é amarelo só pra parecer chique.",
    "No fim do século dezenove, a grafite mais famosa do mundo vinha da China.",
    "E na China, o amarelo era a cor da realeza.",
    "Em mil oitocentos e oitenta e nove, uma fábrica da Europa mostrou numa feira em Paris um lápis pintado de amarelo.",
    "O recado era: aqui dentro tem grafite de primeira, digna de rei.",
    "Fez tanto sucesso que as outras fábricas copiaram a cor.",
    "Você vê, a tinta amarela não muda nada na escrita. É só a roupa do lápis.",
    "Ou seja: o lápis da escola... anda vestido de rei.",
]
CAPTXT = [
    "O lápis é amarelo só pra parecer chique.",
    "No fim do século 19, a grafite mais famosa|do mundo vinha da China.",
    "E na China, o amarelo era a cor da realeza.",
    "Em 1889, uma fábrica da Europa mostrou numa feira|em Paris um lápis pintado de amarelo.",
    "O recado era: aqui dentro tem grafite de primeira,|digna de rei.",
    "Fez tanto sucesso que as outras fábricas copiaram a cor.",
    "Você vê, a tinta amarela não muda nada na escrita.|É só a roupa do lápis.",
    "Ou seja: o lápis da escola... anda vestido de rei.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 6
FLASH = [3]
CHECK = [(0, 'chique', 6), (1, 'china', 4), (2, 'realeza', 4), (3, 'amarelo', 4), (4, 'rei', 4),
         (5, 'copiaram', 4), (6, 'roupa', 4), (7, 'rei', 8)]

AM = '#ffcf33'; AMD = '#d9a514'


@lru_cache(maxsize=64)
def lapis_img(h, cor=AM, cord=AMD, crown=False, face_=''):
    """lápis em pé (ponta para cima), card 260x1100."""
    p = Pen(260, 1100)
    p.shape([(40, 980), (220, 980), (220, 1060), (40, 1060)], hexc('#f29aa6'), hexc('#d06d7c'), 6, 6)   # borracha
    p.shape([(36, 900), (224, 900), (224, 985), (36, 985)], hexc('#c9d0d8'), hexc('#99a3ae'), 6, 6)     # metal
    for y in (925, 955): p.stroke([(40, y), (220, y)], 4)
    p.shape([(40, 300), (220, 300), (220, 900), (40, 900)], hexc(cor), hexc(cord), 6, 14)               # corpo
    for x in (100, 160): p.stroke([(x, 305), (x, 895)], 3, mul(hexc(cord), .9))
    p.shape([(40, 300), (220, 300), (130, 110)], hexc('#f3d3a6'), hexc('#d9b07a'), 6, 6)              # madeira
    p.shape([(98, 175), (162, 175), (130, 110)], hexc('#3a3a42'), None, 5, 0)                          # grafite
    if face_:
        face(p, 130, 560, face_, 0, .3, u=2.2)
    if crown:
        p.shape([(40, 110), (40, 10), (85, 60), (130, 0), (175, 60), (220, 10), (220, 110)], hexc('#ffd84a'), hexc('#d9a514'), 6, 6)
        for x in (85, 130, 175): p.dot(x, 85, 12, hexc('#e23b3b'), 3)
        # sobe a coroa para a ponta: desenhada por cima da ponta mesmo
    return p.img.resize((max(1, int(h * 260 / 1100)), h), Image.LANCZOS)


def lapis(c, x, y, h, rot=0, s=1.0, **kw):
    """y = centro."""
    h = int(h * s)
    if h < 10: return
    im = lapis_img(h, **kw)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


@lru_cache(maxsize=8)
def coroa_img(w):
    p = Pen(400, 260)
    p.shape([(20, 240), (20, 60), (110, 150), (200, 30), (290, 150), (380, 60), (380, 240)], hexc('#ffd84a'), hexc('#d9a514'), 6, 14)
    for x in (110, 200, 290): p.dot(x, 200, 22, hexc('#e23b3b'), 4)
    return p.img.resize((w, int(w * 260 / 400)), Image.LANCZOS)


@lru_cache(maxsize=4)
def manto_img(w):
    p = Pen(500, 700)
    p.shape([(250, 40), (420, 120), (480, 680), (20, 680), (80, 120)], hexc(AM), hexc(AMD), 6, 20)
    p.shape([(250, 40), (300, 680), (200, 680)], mul(hexc(AM), .92), None, 0, 0)
    for i in range(6):
        p.dot(150 + (i % 3) * 100, 300 + (i // 3) * 200, 22, hexc('#e23b3b'), 4)
    p.shape([(60, 640), (440, 640), (480, 690), (20, 690)], hexc('#ffffff'), hexc('#d9dde3'), 5, 4)
    return p.img.resize((w, int(w * 700 / 500)), Image.LANCZOS)


@lru_cache(maxsize=4)
def pedestal_img(w):
    p = Pen(400, 300)
    p.shape([(20, 40), (380, 40), (380, 290), (20, 290)], hexc('#e7e1d6'), hexc('#c4bcae'), 6, 10)
    p.shape([(0, 10), (400, 10), (400, 50), (0, 50)], hexc('#f4efe6'), hexc('#d6cfc2'), 6, 4)
    return p.img.resize((w, int(w * 300 / 400)), Image.LANCZOS)


@lru_cache(maxsize=4)
def balde_img(w):
    p = Pen(300, 300)
    p.shape([(30, 60), (270, 60), (240, 290), (60, 290)], hexc('#9aa4b0'), hexc('#6f7783'), 6, 10)
    p.shape(ell_pts(150, 60, 120, 30), hexc(AM), hexc(AMD), 6, 0)
    p.stroke([(40, 70), (60, 160)], 10, hexc(AM))
    return p.img.resize((w, w), Image.LANCZOS)


@lru_cache(maxsize=4)
def selo_img(w):
    p = Pen(400, 400)
    pts = []
    for i in range(32):
        r = 190 if i % 2 == 0 else 160
        a = i / 32 * 2 * math.pi
        pts.append((200 + r * math.cos(a), 200 + r * math.sin(a)))
    p.shape(pts, hexc('#e23b3b'), hexc('#b82a2a'), 6, 10)
    p.shape(ell_pts(200, 200, 130, 130), hexc('#ff5a5a'), None, 5, 0)
    return p.img.resize((w, w), Image.LANCZOS)


def SFX(s):
    s.ting(s.W(0, 'chique'), .3)
    s.whoosh(s.W(1, 'china') - 6, .5, .4); s.thunk(s.W(1, 'china') - 2, 200, .6)
    s.ting(s.W(2, 'realeza'), .35)
    s.thunk(s.W(3, 'amarelo') - 2, 220, .7)
    s.thunk(s.W(4, 'rei') - 2, 160, .8)
    for i in range(5): s.thunk(s.W(5, 'copiaram') - 2 + i * 4, 260, .4)
    s.whoosh(s.W(6, 'roupa') - 4, .5, .4)
    s.trill(s.W(7, 'rei'), 1.0, .3)


def s0(f):
    c = CEN('escola', 'day').copy()
    k = wt(0, 'chique') - 3
    lp = wt(0, 'lapis') - 3
    lapis(c, 860, 1250, 900, -8 + 3 * math.sin(f * .1), back(ramp(f, lp, lp + 9)), crown=False, face_='smug' if f >= k else 'neutral')
    put_prof(c, 380, 1780, 940, f, expr='smug' if f >= k else 'grin', arms='point' if f >= lp else 'wave', look=1)
    if f >= k: paste_c(c, txt('CHIQUE!', 130, -6), 640, 640, back(ramp(f, k, k + 8)))
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, k, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('mapa', 'day').copy()
    k = wt(1, 'china') - 3
    g = wt(1, 'grafite') - 3
    if f >= g:
        s = back(ramp(f, g, g + 8))
        for i in range(3):
            paste_c(c, Image.new('RGBA', (1, 1)), 0, 0)
            pts_x = 520 + i * 90
            if s > .05:
                bl = Pen(200, 160); bl.shape([(20, 140), (40, 40), (120, 20), (180, 70), (170, 140)], hexc('#3a3a42'), hexc('#24242a'), 5, 8)
                paste_c(c, bl.img.resize((int(150 * s) or 1, int(120 * s) or 1)), pts_x, 1120 + (i % 2) * 40)
    if f >= k: paste_c(c, txt('CHINA', 150, -5), 621, 820, back(ramp(f, k, k + 8)))
    if f >= g: paste_c(c, txt('GRAFITE TOP', 90, 5), 621, 1360, back(ramp(f, g, g + 8)))
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.0, 1.2, t) * (1 + .0009 * f)
    return c, (621, 1150 + kick(f, k, .6) * 10, z, 0), 'day'


def s2(f):
    c = CEN('museu', 'day').copy()
    a = wt(2, 'amarelo') - 3
    r = wt(2, 'realeza') - 3
    paste_c(c, pedestal_img(380), 621, 1620)
    paste_c(c, manto_img(360), 621, 1220, back(ramp(f, a, a + 9)))
    if f >= r: paste_c(c, coroa_img(300), 621, 880, back(ramp(f, r, r + 9)))
    if f >= r: paste_c(c, txt('REALEZA', 120, -5), 621, 660, back(ramp(f, r + 2, r + 10)))
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.2, 1.05, t) * (1 + .0009 * f)
    return c, (621, lerp(1100, 1250, t) + kick(f, r, .6) * 10, z, 0), 'day'


def s3(f):
    c = CEN('fabrica', 'day').copy()
    am = wt(3, 'amarelo') - 3
    pa = wt(3, 'paris') - 3
    paint = ramp(f, am - 10, am)
    paste_c(c, balde_img(200), 560, 1690)
    lapis(c, 760, 1200, 760, -10, 1.0, cor=AM if paint >= 1 else '#c79a6a', cord=AMD if paint >= 1 else '#a07448')
    put_prof(c, 300, 1780, 880, f, expr='proud' if f >= am else 'neutral', arms='point' if f >= am - 10 else 'chin', look=1)
    ml = wt(3, 'mil') - 3
    if f >= ml: paste_c(c, txt('1889', 140, -5), 640, 600, back(ramp(f, ml, ml + 8)))
    if f >= pa: paste_c(c, txt('FEIRA DE PARIS', 80, 4), 640, 760, back(ramp(f, pa, pa + 8)))
    z = lerp(1.25, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, am, .6) * 10, z, 0), 'day'


def s4(f):
    c = CEN('fabrica', 'day').copy()
    pr = wt(4, 'primeira') - 3
    r = wt(4, 'rei') - 3
    lapis(c, 621, 1250, 900, 0, 1.0, crown=f >= r, face_='proud' if f >= r else 'neutral')
    if f >= pr:
        paste_c(c, selo_img(240), 900, 1000, back(ramp(f, pr, pr + 8)))
        paste_c(c, txt('Nº1', 80, -10), 900, 1000, back(ramp(f, pr, pr + 8)))
    if f >= r: paste_c(c, txt('DIGNO DE REI', 100, -5), 621, 640, back(ramp(f, r, r + 8)))
    t = smooth(ramp(f, 0, 80))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (621, 1200 + kick(f, r, .7) * 10, z, 0), 'day'


def s5(f):
    c = CEN('fabrica', 'golden').copy()
    k = wt(5, 'copiaram') - 3
    lapis(c, 621, 1250, 700, 0, 1.0)
    for i, x in enumerate((180, 340, 900, 1060)):
        y = 1300 + (i % 2) * 60
        col = AM if f >= k + i * 3 else '#c79a6a'
        lapis(c, x, y, 520, (-8, 6, -5, 9)[i], back(ramp(f, 4 + i * 6, 12 + i * 6)), cor=col, cord=AMD if col == AM else '#a07448')
    if f >= k: paste_c(c, txt('COPIA!', 130, 6), 621, 640, back(ramp(f, k, k + 8)))
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, k, .6) * 10, z, 0), 'golden'


def s6(f):
    c = CEN('escola', 'dusk').copy()
    n = wt(6, 'nada') - 3
    ro = wt(6, 'roupa') - 3
    put_prof(c, 330, 1780, 900, f, expr='stern' if f < ro else 'grin', arms='point', look=1)
    lapis(c, 820, 1150, 640, -15, 1.0, cor=AM if (f // 12) % 2 == 0 or f >= ro else '#4ea3e0', cord=AMD if (f // 12) % 2 == 0 or f >= ro else '#2f78ad')
    if n <= f < ro: paste_c(c, txt('ESCREVE IGUAL', 90, -4), 640, 620, back(ramp(f, n, n + 8)))
    if f >= ro: paste_c(c, txt('SÓ A ROUPA!', 110, 5), 640, 620, back(ramp(f, ro, ro + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, ro, .6) * 8, z, lerp(0, 2, t)), 'dusk'


def s7(f):
    c = CEN('escola', 'dusk').copy()
    r = wt(7, 'rei') - 3
    put_prof(c, 360, 1780, 920, f, expr='smug' if f < r else 'grin', arms='chin' if f < r else 'shrug', look=1)
    lapis(c, 860, 1180, 760, -6 + 2 * math.sin(f * .12), 1.0, crown=f >= r, face_='smug' if f >= r else 'neutral')
    if f >= r: paste_c(c, txt('MAJESTADE!', 110, -6), 640, 700, back(ramp(f, r, r + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.03, 1.15, t) * (1 + .0006 * f)
    return c, (640, lerp(1280, 1240, t), z, lerp(0, -3, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
