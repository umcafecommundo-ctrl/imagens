"""Parque de diversões e carrossel no traço MISTÉRIO (história "O cavalo treze", 22/11/2026).
parque_bg(luz): céu pela luz, gramado, roda-gigante ao fundo à esquerda, barraquinhas; chão em y≈1500.
carrossel(c, f, luz, n=12, fase=0, extra=False, x=621, feet=1500, s=1.0): carrossel girando (fase em radianos);
  extra=True acrescenta o 13º cavalo (branco, crina dourada).
cavalo_img(cor, crina, h, flip): cavalo de carrossel de lado com o poste.
bilheteria_bg(luz): guichê de madeira com janelinha; ficha(c, x, y, r, num): ficha redonda com número.
"""
from kit import *
import kit
from sombrio import *

GRAMA_P = {'dia': '#8cc46a', 'tarde': '#b8a866', 'neblina': '#8a9a8c', 'noite': '#2f3d3a', 'frio': '#9db7a8'}
CORES_CAV = ['#c9824a', '#6a4a3a', '#d9b98a', '#8a5a3a', '#a86a4a', '#5a3a2a']


def _ceu_luz(luz):
    return {'frio': 'neblina'}.get(luz, luz)


@lru_cache(maxsize=8)
def parque_bg(luz='dia'):
    c = ceu(_ceu_luz(luz)).copy()
    noite = luz == 'noite'
    p = Pen(W_, H_)
    # roda-gigante ao fundo (à esquerda)
    cx, cy, R = 230, 760, 330
    aro = hexc('#d8d2c4') if not noite else hexc('#5a6266')
    for k in range(12):
        a = 2 * math.pi * k / 12
        p.stroke([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], 6, mul(aro, .8))
    p.arc(cx, cy, R, R, 0, 360, 12, mul(aro, .7))
    p.arc(cx, cy, R * .55, R * .55, 0, 360, 7, mul(aro, .7))
    p.stroke([(cx, cy), (cx - 160, 1320)], 14, mul(aro, .6)); p.stroke([(cx, cy), (cx + 160, 1320)], 14, mul(aro, .6))
    cab = ['#e86a5a', '#f0c050', '#5aa6d8', '#6ac08a']
    for k in range(12):
        a = 2 * math.pi * k / 12
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        col = hexc(cab[k % 4]) if not noite else mul(hexc(cab[k % 4]), .45)
        p.shape([(x - 30, y), (x + 30, y), (x + 26, y + 46), (x - 26, y + 46)], col, None, 4, 0)
    # gramado
    p.poly([(0, 1260), (W_, 1230), (W_, H_), (0, H_)], hexc(GRAMA_P[luz]))
    rnd = random.Random(5)
    for i in range(70):
        x, y = rnd.randint(0, W_), rnd.randint(1560, 2200)
        p.stroke([(x, y), (x - 6, y - 24)], 4, mul(hexc(GRAMA_P[luz]), .8))
    # barraquinhas ao fundo à direita
    for bx, col in ((1000, '#e86a5a'), (1160, '#5aa6d8')):
        cc = hexc(col) if not noite else mul(hexc(col), .45)
        p.shape([(bx - 70, 1300), (bx + 70, 1300), (bx + 70, 1150), (bx - 70, 1150)], hexc('#f4ead2') if not noite else hexc('#4a4e50'), None, 5, 0)
        p.shape([(bx - 90, 1150), (bx, 1060), (bx + 90, 1150)], cc, None, 5, 0)
    # caminho de terra
    p.poly([(380, H_), (560, 1500), (700, 1500), (900, H_)], mul(hexc('#d8c49a'), .5 if noite else 1))
    base = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(base)
    if noite:   # luzinhas
        d = ImageDraw.Draw(c)
        for k in range(24):
            a = 2 * math.pi * k / 24
            x, y = cx + R * math.cos(a), cy + R * math.sin(a)
            d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=(250, 226, 150, 255))
    if luz == 'frio': c.alpha_composite(Image.new('RGBA', (W_, H_), (200, 215, 230, 50)))
    if luz == 'neblina': c.alpha_composite(Image.new('RGBA', (W_, H_), (190, 196, 196, 60)))
    return c


@lru_cache(maxsize=64)
def cavalo_img(cor='#c9824a', crina='#3a2a22', h=300, flip=False, brilho=False):
    """cavalo de carrossel de lado (olhando p/ direita), poste dourado atravessando. 500x600, poste de y 0 a 600."""
    p = Pen(500, 600)
    col = hexc(cor); dk = mul(col, .8)
    p.shape([(244, 4), (256, 4), (256, 596), (244, 596)], hexc('#e8c45a'), None, 4, 0)
    # pernas (dobradas, estilo carrossel)
    p.line([(170, 360), (120, 430), (150, 480)], mul(col, .9), 26, 5)
    p.line([(200, 360), (190, 470)], mul(col, .9), 26, 5)
    p.line([(320, 350), (380, 400), (360, 460)], mul(col, .9), 26, 5)
    p.line([(300, 360), (300, 470)], mul(col, .9), 26, 5)
    # rabo
    p.line([(110, 290), (60, 330), (70, 420)], hexc(crina), 26, 5)
    # corpo
    p.shape(ell_pts(240, 300, 140, 75), col, dk, 6, 14)
    # pescoço e cabeça
    p.shape([(310, 280), (350, 160), (400, 150), (380, 300)], col, dk, 6, 10)
    p.shape(ell_pts(410, 170, 60, 36, rot=.5), col, dk, 6, 8)
    p.shape([(350, 130), (365, 95), (380, 135)], col, None, 5, 0)   # orelha
    # crina
    for k in range(5):
        y = 150 + k * 30
        p.line([(345 - k * 8, y), (318 - k * 8, y + 22)], hexc(crina), 18, 4)
    # sela
    p.shape([(190, 235), (290, 235), (300, 290), (180, 290)], hexc('#c0453a'), hexc('#9a3328'), 5, 8)
    p.shape([(178, 285), (302, 285), (302, 300), (178, 300)], hexc('#e8c45a'), None, 4, 0)
    # olho grande
    p.dot(415, 158, 17, (250, 250, 246), 4)
    p.dot(421, 160, 8, (30, 26, 28))
    p.dot(448, 182, 5, (60, 40, 40))
    im = p.img.resize((500, 600), Image.LANCZOS)
    if brilho:
        g = Image.new('RGBA', im.size, (0, 0, 0, 0)); a = im.split()[3].filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(14))
        g.putalpha(a.point(lambda v: int(v * .7))); gl = Image.new('RGBA', im.size, (255, 236, 160, 0)); gl.putalpha(g.split()[3])
        gl.alpha_composite(im); im = gl
    im = im.resize((int(h * 500 / 600), int(h)), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im


@lru_cache(maxsize=8)
def carrossel_fundo(luz='dia', s=1.0):
    """teto listrado e piso do carrossel (sem cavalos), tamanho 1100x1100*s com centro em x=550; piso em y=1000."""
    noite = luz == 'noite'
    p = Pen(1100, 1100)
    escu = .5 if noite else 1.0
    # piso (plataforma)
    p.shape(ell_pts(550, 980, 520, 80), mul(hexc('#b8834e'), escu), mul(hexc('#8a5a32'), escu), 7, 12)
    p.shape([(30, 980), (1070, 980), (1070, 1030), (30, 1030)], mul(hexc('#8a5a32'), escu), None, 6, 0)
    p.shape(ell_pts(550, 1030, 520, 50), mul(hexc('#8a5a32'), escu), None, 6, 0)
    p.shape(ell_pts(550, 975, 516, 76), mul(hexc('#c9965e'), escu), None, 0, 0)
    # poste central
    p.shape([(520, 330), (580, 330), (580, 980), (520, 980)], mul(hexc('#e8c45a'), escu), mul(hexc('#c09a3a'), escu), 6, 10)
    # teto em cone listrado
    cores = ['#e86a5a', '#f4ead2']
    n = 12
    for k in range(n):
        x0 = 40 + k * (1020 / n); x1 = 40 + (k + 1) * (1020 / n)
        p.poly([(550, 60), (x0, 300), (x1, 300)], mul(hexc(cores[k % 2]), escu))
    p.stroke([(550, 60), (40, 300)], 7); p.stroke([(550, 60), (1060, 300)], 7)
    # barrado com franjas
    p.shape([(30, 300), (1070, 300), (1070, 360), (30, 360)], mul(hexc('#f0c050'), escu), None, 6, 0)
    for k in range(13):
        x = 30 + k * 80
        p.shape([(x, 360), (x + 80, 360), (x + 40, 400)], mul(hexc(cores[k % 2]), escu), None, 4, 0)
    p.dot(550, 52, 22, mul(hexc('#f0c050'), escu), 5)
    im = p.img.resize((1100, 1100), Image.LANCZOS)
    if s != 1: im = im.resize((int(1100 * s), int(1100 * s)), Image.LANCZOS)
    return im


def carrossel(c, f, luz='dia', n=12, fase=0.0, extra=False, x=621, feet=1500, s=1.0, so_extra=False):
    """desenha o carrossel; devolve (x, y) na tela do palco do 13º cavalo (ou None)."""
    fundo = carrossel_fundo(luz, round(s, 2))
    ox, oy = int(x - fundo.width / 2), int(feet - 1000 * s)
    # cavalos de trás (escuros), depois poste/teto, depois cavalos da frente
    tot = n + (1 if extra else 0)
    cav = []
    for i in range(tot):
        a = fase + 2 * math.pi * i / tot
        dep = math.cos(a)
        cx_ = x + 430 * s * math.sin(a)
        bob = 30 * s * math.sin(a * 2 + fase * 3)
        cav.append((dep, cx_, bob, i))
    cav.sort()
    escu = luz == 'noite'
    pos13 = None
    c.alpha_composite(fundo, (ox, oy))
    for dep, cx_, bob, i in cav:
        if dep < -.2: continue   # escondidos atrás do poste/teto
        e13 = extra and i == tot - 1
        if so_extra and not e13: continue
        hh = 520 * s * (.82 + .18 * dep)
        if e13: col, cr = '#f4f2ec', '#e8b83a'
        else:
            col, cr = CORES_CAV[i % len(CORES_CAV)], '#3a2a22'
            if escu: col = '#%02x%02x%02x' % tuple(int(v * .55) for v in hexc(col))
        im = cavalo_img(col, cr, int(hh / 8) * 8, False, brilho=e13 and escu)
        yy = int(oy + 360 * s + (1000 - 360) * s * .5 - hh / 2 + bob + 40 * s * dep)
        c.alpha_composite(im, (int(cx_ - im.width / 2), yy))
        if e13: pos13 = (cx_, yy + hh * .4)
    return pos13


def _bil(luz):
    return luz


@lru_cache(maxsize=8)
def bilheteria_bg(luz='dia'):
    """bilheteria de madeira com janelinha (x 380..860, y 700..1100) e balcão em y 1100."""
    c = parque_bg(luz).copy()
    noite = luz == 'noite'
    e = .55 if noite else 1
    p = Pen(W_, H_)
    p.shape([(250, 520), (990, 520), (990, 1560), (250, 1560)], mul(hexc('#d9634f'), e), mul(hexc('#b04a3a'), e), 8, 16)
    p.shape([(200, 520), (621, 330), (1040, 520)], mul(hexc('#f0c050'), e), None, 8, 0)
    p.shape([(380, 680), (860, 680), (860, 1100), (380, 1100)], hexc('#f2e2a0') if noite else hexc('#3b4a5a'), None, 8, 0)
    p.shape([(330, 1100), (910, 1100), (910, 1150), (330, 1150)], mul(hexc('#8a5a32'), e), None, 6, 0)
    p.shape([(470, 560), (770, 560), (770, 640), (470, 640)], hexc('#f4ead2'), None, 5, 0)
    base = p.img.resize((W_, H_), Image.LANCZOS)
    d = ImageDraw.Draw(base); fnt = font(F_STAMP, 56)
    t = 'FICHAS'; tw = d.textlength(t, font=fnt); d.text((621 - tw / 2, 562), t, font=fnt, fill=(60, 40, 34, 255))
    c.alpha_composite(base)
    return c


@lru_cache(maxsize=16)
def ficha_img(num, r):
    im = Image.new('RGBA', (2 * r + 20, 2 * r + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx = r + 10
    d.ellipse((cx - r - 6, cx - r - 6, cx + r + 6, cx + r + 6), fill=(36, 30, 32, 255))
    d.ellipse((cx - r, cx - r, cx + r, cx + r), fill=(232, 190, 80, 255))
    d.ellipse((cx - r * .8, cx - r * .8, cx + r * .8, cx + r * .8), outline=(180, 140, 50, 255), width=max(2, r // 14))
    fnt = font(F_STAMP, int(r * 1.0)); t = str(num); tw = d.textlength(t, font=fnt)
    d.text((cx - tw / 2, cx - r * .7), t, font=fnt, fill=(70, 50, 30, 255))
    return im


def ficha(c, x, y, r, num, rot=0):
    if r < 6: return
    im = ficha_img(num, int(r))
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def lua(c, x, y, r, s=1.0):
    if s <= .02: return
    r = r * s
    g = Image.new('RGBA', (int(4 * r), int(4 * r)), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    d.ellipse((r * .6, r * .6, r * 3.4, r * 3.4), fill=(240, 236, 210, 60))
    g = g.filter(ImageFilter.GaussianBlur(r * .3)); d = ImageDraw.Draw(g)
    d.ellipse((r, r, 3 * r, 3 * r), fill=(244, 240, 220, 255), outline=(36, 30, 32, 255), width=5)
    d.ellipse((r * 1.6, r * 1.5, r * 2.0, r * 1.9), fill=(222, 216, 196, 255))
    d.ellipse((r * 2.2, r * 2.2, r * 2.5, r * 2.5), fill=(222, 216, 196, 255))
    c.alpha_composite(g, (int(x - 2 * r), int(y - 2 * r)))


def gancho(im, linhas, y, s, size=92, cor=(250, 246, 236)):
    """texto grande do primeiro quadro (capa) em coordenadas da saída; até 2 linhas centralizadas."""
    if s <= .02: return
    d = ImageDraw.Draw(im); fnt = font(F_STAMP, size)
    for i, l in enumerate(linhas):
        tw = d.textlength(l, font=fnt)
        x = OW / 2 - tw / 2; yy = y + i * size * 1.12
        d.text((x + 5, yy + 7), l, font=fnt, fill=(18, 18, 20), stroke_width=9, stroke_fill=(18, 18, 20))
        d.text((x, yy), l, font=fnt, fill=cor, stroke_width=8, stroke_fill=(24, 22, 26))
