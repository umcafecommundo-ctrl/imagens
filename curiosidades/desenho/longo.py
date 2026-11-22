"""Kit do VÍDEO LONGO horizontal (YouTube normal, 16:9) no estilo MISTÉRIO. Rode o motor com MOTOR_H=1.
Palco 2208x1242 (chão em y≈1080), saída 1920x1080, legenda de 1 palavra em y≈930 da saída.
close_h(c, f, ...): close no rosto no palco horizontal (x = centro do rosto; use x=1500 na capa para deixar o texto à esquerda).
gancho_h(im, linhas, x, y, size): texto grande da capa alinhado à esquerda (coordenadas da saída).
biblioteca_bg(luz), quarto_h(luz), rua_h(luz): cenários horizontais; livro(c, ...): livro aberto com texto à mão.
"""
from kit import *
import kit
from sombrio import *

assert kit.OW > kit.OH, 'longo.py precisa de MOTOR_H=1'
F_MAO_L = GF + 'ofl/comicrelief/ComicRelief-Bold.ttf'


def close_h(c, f, expr='neutro', look=0.0, x=1104, s=1.0, fundo_blur=14, escurece=0.0, shake=0.0, seed=2, **kw):
    bg = c.filter(ImageFilter.GaussianBlur(fundo_blur)) if fundo_blur else c.copy()
    if escurece > 0: bg.alpha_composite(Image.new('RGBA', bg.size, (10, 12, 14, int(150 * escurece))))
    kw['blink'] = 1 if blinkAt(f, seed) > .6 and expr not in ('choque', 'medo') else 0
    q = dict(kw); q['look'] = round(look * 4) / 4
    q['tremor'] = round(f / 3) if shake > 0 else 0
    h = int(1300 * s)
    im = kit.sprite('rosto', tuple(sorted(dict(q, expr=expr).items())), h, 1000 / 1700, False)
    bob = 5 * math.sin(f * .11); sx = shake * 8 * math.sin(f * 2.3)
    bg.alpha_composite(im, (int(x - im.width / 2 + sx), int(1242 - h * .93 + bob)))
    return bg


def gancho_h(im, linhas, x, y, s=1.0, size=100, cor=(250, 246, 236)):
    if s <= .02: return
    d = ImageDraw.Draw(im); fnt = font(F_STAMP, size)
    for i, l in enumerate(linhas):
        yy = y + i * size * 1.12
        d.text((x + 5, yy + 7), l, font=fnt, fill=(18, 18, 20), stroke_width=9, stroke_fill=(18, 18, 20))
        d.text((x, yy), l, font=fnt, fill=cor, stroke_width=8, stroke_fill=(24, 22, 26))


def _sky(luz):
    return ceu({'frio': 'neblina', 'azul': 'noite'}.get(luz, luz)).copy()


LIVROS = ['#c0453a', '#4f8fc0', '#e0a43c', '#5aa36f', '#7a5ab0', '#d9634f', '#3a6a8a', '#b58a5a']


@lru_cache(maxsize=8)
def biblioteca_bg(luz='dia'):
    """janelão em arco no centro (x 850..1350, y 120..760), estantes dos lados, balcão à direita (x 1650..2150, y 760..1080)."""
    noite = luz in ('noite', 'azul')
    c = Image.new('RGBA', (W_, H_), (0, 0, 0, 255))
    sky = _sky(luz)
    c.alpha_composite(sky.crop((300, 0, 300 + 500, 640)).resize((500, 640)), (850, 120))
    p = Pen(W_, H_)
    parede = {'dia': '#ead9b6', 'tarde': '#e2c49a', 'neblina': '#b9bcb4', 'noite': '#4d5560', 'frio': '#c9d3d8', 'azul': '#3a4a6a'}[luz]
    w = hexc(parede)
    # parede com buraco da janela (desenhada por partes)
    p.poly([(0, 0), (850, 0), (850, 1080), (0, 1080)], w)
    p.poly([(1350, 0), (W_, 0), (W_, 1080), (1350, 1080)], w)
    p.poly([(850, 0), (1350, 0), (1350, 120), (850, 120)], w)
    p.poly([(850, 760), (1350, 760), (1350, 1080), (850, 1080)], w)
    p.stroke([(850, 120), (1350, 120), (1350, 760), (850, 760), (850, 120)], 12, hexc('#f4f1ea'))
    p.stroke([(1100, 120), (1100, 760)], 10, hexc('#f4f1ea')); p.stroke([(850, 440), (1350, 440)], 10, hexc('#f4f1ea'))
    p.stroke([(842, 112), (1358, 112), (1358, 768), (842, 768), (842, 112)], 5)
    # piso de madeira
    pis = mul(hexc('#a8835c'), .6 if noite else 1)
    p.poly([(0, 1080), (W_, 1080), (W_, H_), (0, H_)], pis)
    for y in range(1120, H_, 50): p.stroke([(0, y), (W_, y)], 3, mul(pis, .8))
    p.stroke([(0, 1080), (W_, 1080)], 7)
    # estantes
    rnd = random.Random(11)
    e = .55 if noite else 1
    for x0, x1 in ((40, 760), (1420, 2170)):
        p.shape([(x0, 160), (x1, 160), (x1, 1080), (x0, 1080)], mul(hexc('#8a5a32'), e), mul(hexc('#6f4a2a'), e), 7, 12)
        for k in range(5):
            y = 260 + k * 165
            x = x0 + 30
            while x < x1 - 60:
                bw = rnd.randint(28, 46); bh = rnd.randint(95, 130)
                col = mul(hexc(rnd.choice(LIVROS)), e)
                p.poly([(x, y + 130 - bh), (x + bw, y + 130 - bh), (x + bw, y + 130), (x, y + 130)], col, 3)
                x += bw + rnd.randint(0, 6)
            p.shape([(x0 + 14, y + 130), (x1 - 14, y + 130), (x1 - 14, y + 150), (x0 + 14, y + 150)], mul(hexc('#6f4a2a'), e), None, 4, 0)
    im = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(im)
    if luz == 'azul': c.alpha_composite(Image.new('RGBA', c.size, (40, 80, 200, 50)))
    return c


@lru_cache(maxsize=4)
def balcao_img(luz='dia'):
    p = Pen(700, 400)
    e = .55 if luz in ('noite', 'azul') else 1
    p.shape([(20, 60), (680, 60), (680, 390), (20, 390)], mul(hexc('#9a6a40'), e), mul(hexc('#7a5230'), e), 7, 12)
    p.shape([(0, 30), (700, 30), (700, 70), (0, 70)], mul(hexc('#7a5230'), e), None, 6, 0)
    for x in (140, 350, 560): p.stroke([(x, 90), (x, 370)], 5, mul(hexc('#7a5230'), e))
    return p.img.resize((700, 400), Image.LANCZOS)


@lru_cache(maxsize=8)
def quarto_h(luz='dia', chuva=False):
    """quarto: janela à esquerda (x 150..650, y 200..700), cama à direita (x 1350..2100), escrivaninha no meio; chão y 1080."""
    noite = luz in ('noite',)
    c = Image.new('RGBA', (W_, H_), (0, 0, 0, 255))
    c.alpha_composite(_sky(luz).crop((200, 0, 700, 500)), (150, 200))
    if chuva:
        d = ImageDraw.Draw(c); rnd = random.Random(2)
        for i in range(60):
            x, y = rnd.randint(150, 650), rnd.randint(200, 700); d.line((x, y, x - 14, y + 40), fill=(200, 210, 230, 180), width=3)
    p = Pen(W_, H_)
    w = hexc({'dia': '#cfe3d6', 'tarde': '#e2c7a6', 'neblina': '#b9bcb4', 'noite': '#3f4a5a', 'frio': '#c9d3d8'}[luz])
    p.poly([(0, 0), (150, 0), (150, 1080), (0, 1080)], w); p.poly([(650, 0), (W_, 0), (W_, 1080), (650, 1080)], w)
    p.poly([(150, 0), (650, 0), (650, 200), (150, 200)], w); p.poly([(150, 700), (650, 700), (650, 1080), (150, 1080)], w)
    for x in range(0, W_, 140): p.stroke([(x, 0), (x, 1080)], 3, mul(w, .94))
    p.stroke([(150, 200), (650, 200), (650, 700), (150, 700), (150, 200)], 14, hexc('#f4f1ea'))
    p.stroke([(400, 200), (400, 700)], 10, hexc('#f4f1ea')); p.stroke([(142, 192), (658, 192), (658, 708), (142, 708), (142, 192)], 5)
    pis = mul(hexc('#a8835c'), .6 if noite else 1)
    p.poly([(0, 1080), (W_, 1080), (W_, H_), (0, H_)], pis)
    for y in range(1120, H_, 50): p.stroke([(0, y), (W_, y)], 3, mul(pis, .8))
    p.stroke([(0, 1080), (W_, 1080)], 7)
    e = .6 if noite else 1
    # cama
    p.shape([(1350, 820), (2120, 820), (2120, 1100), (1350, 1100)], mul(hexc('#7a5ab0'), e), mul(hexc('#5f4590'), e), 7, 12)
    p.shape([(2080, 600), (2160, 600), (2160, 1120), (2080, 1120)], mul(hexc('#8a5a32'), e), None, 6, 0)
    p.shape([(1880, 760), (2060, 760), (2060, 840), (1880, 840)], mul(hexc('#f4f1ea'), e), None, 6, 0)
    # escrivaninha + abajur
    p.shape([(780, 760), (1220, 760), (1220, 800), (780, 800)], mul(hexc('#9a6a40'), e), None, 6, 0)
    for x in (800, 1180): p.shape([(x, 800), (x + 22, 800), (x + 22, 1080), (x, 1080)], mul(hexc('#7a5230'), e), None, 5, 0)
    p.shape([(1110, 600), (1190, 600), (1210, 680), (1090, 680)], mul(hexc('#e0a43c'), e), None, 5, 0)
    p.stroke([(1150, 680), (1150, 760)], 8)
    im = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(im)
    if noite:   # luz do abajur
        g = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
        d.ellipse((800, 500, 1500, 1100), fill=(255, 220, 150, 70)); c.alpha_composite(g.filter(ImageFilter.GaussianBlur(70)))
    return c


@lru_cache(maxsize=8)
def rua_h(luz='dia'):
    c = _sky(luz)
    cs = casas_strip(luz if luz in ('dia', 'tarde', 'neblina', 'noite') else 'neblina')
    c.alpha_composite(cs.crop((0, 0, W_, 700)), (0, 400))
    d = ImageDraw.Draw(c)
    ru = {'dia': (110, 116, 120), 'tarde': (112, 104, 100), 'neblina': (78, 84, 86), 'noite': (40, 44, 46), 'frio': (100, 108, 114)}[luz]
    d.rectangle((0, 1040, W_, H_), fill=tuple(int(v * 1.35) for v in ru) + (255,))
    d.rectangle((0, 1100, W_, H_), fill=ru + (255,)); d.line((0, 1040, W_, 1040), fill=(36, 30, 38, 255), width=6)
    return c


def livro(c, x, y, s=1.0, esq=(), dir_=(), t=1.0, capa='#3f8f5a', cor_txt=(70, 70, 78), cor2=None, t2=1.0, dir2=()):
    """livro aberto grande (1200x760 * s). esq/dir_ = linhas de texto à mão (lápis); dir2 = linhas com a 2ª letra (cor2)."""
    if s <= .05: return
    W, H = 1200, 760
    im = Image.new('RGBA', (W + 40, H + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((10, 20, W + 30, H + 30), 26, fill=hexc(capa) + (255,), outline=(36, 30, 32, 255), width=7)
    d.rectangle((40, 30, W / 2 + 16, H + 6), fill=(248, 241, 220, 255), outline=(36, 30, 32, 255), width=4)
    d.rectangle((W / 2 + 24, 30, W, H + 6), fill=(248, 241, 220, 255), outline=(36, 30, 32, 255), width=4)
    for k in range(11):
        yy = 110 + k * 58
        d.line((70, yy, W / 2 - 10, yy), fill=(214, 204, 184, 255), width=2); d.line((W / 2 + 50, yy, W - 30, yy), fill=(214, 204, 184, 255), width=2)
    fnt = font(F_MAO_L, 42)

    def escreve(linhas, x0, y0, tt, col):
        tot = sum(len(l) for l in linhas); n = int(round(tot * clamp(tt)))
        for i, l in enumerate(linhas):
            vis = l[:max(0, n)]; n -= len(l)
            d.text((x0, y0 + i * 58), vis, font=fnt, fill=col + (255,))
    escreve(esq, 80, 62, t, cor_txt)
    escreve(dir_, W / 2 + 60, 62, t, cor_txt)
    if dir2: escreve(dir2, W / 2 + 60, 62 + 58 * (len(dir_) + 1), t2, cor2 or (40, 70, 160))
    im = im.resize((int((W + 40) * s), int((H + 40) * s)), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


@lru_cache(maxsize=16)
def livro_fechado(cor='#3f8f5a', h=200, brilho=False):
    w = int(h * .72)
    im = Image.new('RGBA', (w + 60, h + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if brilho:
        d.rounded_rectangle((0, 0, w + 60, h + 60), 30, fill=(255, 240, 170, 110)); im = im.filter(ImageFilter.GaussianBlur(14)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((30, 30, w + 30, h + 30), 10, fill=hexc(cor) + (255,), outline=(36, 30, 32, 255), width=6)
    d.rectangle((30, 30, 52, h + 30), fill=mul(hexc(cor), .75) + (255,), outline=(36, 30, 32, 255), width=4)
    d.rectangle((70, 30 + h * .3, w + 10, 30 + h * .42), fill=(230, 200, 110, 255))
    return im


def put_livro(c, x, y, h, cor='#3f8f5a', rot=0, brilho=False):
    if h < 10: return
    im = livro_fechado(cor, int(h / 4) * 4, brilho)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


@lru_cache(maxsize=4)
def aquario_img():
    p = Pen(520, 420)
    p.shape([(30, 60), (490, 60), (490, 380), (30, 380)], hexc('#9fd3e6'), None, 6, 0)
    p.poly([(36, 120), (484, 120), (484, 374), (36, 374)], hexc('#5aa6d8'))
    p.shape([(140, 230), (220, 200), (250, 230), (220, 260)], hexc('#f08a3a'), None, 4, 0)
    p.shape([(360, 300), (420, 280), (440, 300), (420, 320)], hexc('#f0c050'), None, 4, 0)
    p.shape([(0, 380), (520, 380), (520, 420), (0, 420)], hexc('#7a5230'), None, 5, 0)
    return p.img.resize((520, 420), Image.LANCZOS)


@lru_cache(maxsize=2)
def mochila_img():
    p = Pen(420, 460)
    p.shape([(60, 120), (360, 120), (380, 440), (40, 440)], hexc('#d9634f'), hexc('#b04a3a'), 7, 14)
    p.shape([(90, 280), (330, 280), (330, 400), (90, 400)], hexc('#e0a43c'), None, 6, 0)
    p.arc(210, 120, 90, 80, 180, 360, 16, hexc('#8a3a2a'))
    return p.img.resize((420, 460), Image.LANCZOS)


@lru_cache(maxsize=2)
def mapa_img():
    p = Pen(1300, 860)
    p.shape([(20, 40), (1280, 20), (1270, 840), (30, 820)], hexc('#efe0b8'), hexc('#d8c69a'), 7, 16)
    p.shape([(200, 200), (420, 140), (600, 260), (560, 480), (330, 560), (180, 420)], hexc('#9cc98a'), None, 5, 0)
    p.shape([(760, 360), (980, 300), (1120, 460), (1000, 680), (780, 640)], hexc('#9cc98a'), None, 5, 0)
    p.stroke([(450, 300), (620, 420), (850, 450), (980, 520)], 5, hexc('#c0453a'))
    for x, y in ((450, 300), (850, 450), (980, 520)): p.dot(x, y, 14, hexc('#c0453a'), 4)
    return p.img.resize((1300, 860), Image.LANCZOS)


@lru_cache(maxsize=2)
def casa_antena_img():
    """casinha com antena e um gato no telhado (desenho 'imaginado', em tom sépia)."""
    p = Pen(700, 700)
    p.shape([(120, 360), (580, 360), (580, 680), (120, 680)], hexc('#e0c49a'), hexc('#c8a87a'), 7, 12)
    p.shape([(80, 380), (350, 170), (620, 380)], hexc('#b8835a'), None, 7, 0)
    p.stroke([(470, 260), (470, 80)], 8); p.stroke([(410, 110), (530, 110)], 8); p.stroke([(430, 150), (510, 150)], 8)
    p.shape(ell_pts(560, 300, 50, 32), hexc('#5a5a62'), None, 5, 0)          # gato
    p.shape(ell_pts(605, 268, 26, 24), hexc('#5a5a62'), None, 5, 0)
    p.shape([(588, 250), (594, 222), (604, 248)], hexc('#5a5a62'), None, 4, 0); p.shape([(610, 248), (620, 222), (626, 252)], hexc('#5a5a62'), None, 4, 0)
    p.line([(512, 300), (480, 250)], hexc('#5a5a62'), 10, 4)
    p.shape([(300, 520), (400, 520), (400, 680), (300, 680)], hexc('#8a5a32'), None, 5, 0)
    return p.img.resize((700, 700), Image.LANCZOS)
