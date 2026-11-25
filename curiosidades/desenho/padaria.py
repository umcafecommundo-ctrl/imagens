"""Cenários da história "A padaria das três" (25/11/2026): fachada da padaria na rua, interior com balcão e forno,
e os pães com formato (comum, guarda-chuva, peixe, estrela, rosto). Palco 1242x2208."""
from functools import lru_cache
from kit import *
import kit
from sombrio import *

PAO, PAOD, PAOC = hexc('#d9a05b'), hexc('#b07a3c'), hexc('#f0c98a')


@lru_cache(maxsize=8)
def fachada_img(luz='dia', acesa=False):
    """fachada 860x900 (base em y=900)."""
    p = Pen(860, 900)
    parede = {'dia': '#f3d9b1', 'tarde': '#e8c095', 'noite': '#6e6258', 'neblina': '#b9ae9e'}[luz]
    p.shape([(20, 890), (20, 120), (840, 120), (840, 890)], hexc(parede), mul(hexc(parede), .85), 6, 0)
    # toldo listrado
    for i in range(8):
        x0 = 10 + i * 105
        col = hexc('#d8423a') if i % 2 == 0 else hexc('#f6efd9')
        if luz == 'noite': col = mul(col, .55)
        p.shape([(x0, 250), (x0 + 105, 250), (x0 + 105, 330), (x0 + 52, 355), (x0, 330)], col, None, 5, 0)
    # placa
    p.shape([(140, 40), (720, 40), (720, 200), (140, 200)], hexc('#6b3e26'), None, 6, 0)
    # vitrine
    vid = hexc('#ffd77a') if acesa else ({'dia': hexc('#bfe0ee'), 'tarde': hexc('#e6c79a'), 'noite': hexc('#2c3438'), 'neblina': hexc('#a9b6b8')}[luz])
    p.shape([(60, 430), (500, 430), (500, 760), (60, 760)], vid, None, 7, 0)
    # porta
    p.shape([(580, 890), (580, 420), (790, 420), (790, 890)], hexc('#8a5a38'), None, 6, 0)
    p.shape([(615, 460), (755, 460), (755, 640), (615, 640)], vid, None, 5, 0)
    p.dot(605, 680, 12, hexc('#e0c060'), 4)
    im = p.img.resize((860, 900), Image.LANCZOS)
    d = ImageDraw.Draw(im); fnt = font(F_STAMP, 92); tw = d.textlength('PADARIA', font=fnt)
    d.text((430 - tw / 2, 70), 'PADARIA', font=fnt, fill=(250, 230, 180) if luz != 'noite' else (190, 170, 130))
    # pãezinhos na vitrine
    if luz != 'noite' or acesa:
        for k in range(4):
            pi = pao_img('comum', 120)
            im.alpha_composite(pi, (90 + k * 100, 650))
    if acesa:
        gl = Image.new('RGBA', im.size, (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
        dg.rectangle((40, 410, 520, 780), fill=(255, 210, 110, 90)); dg.rectangle((595, 440, 775, 660), fill=(255, 210, 110, 90))
        im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(30)))
    return im


@lru_cache(maxsize=8)
def rua_padaria(luz='dia', acesa=False):
    """rua com a padaria no meio (porta em x≈841..1010 do palco, chão y≈1540)."""
    c = rua(0, 300, luz=luz, neb=0 if luz != 'neblina' else .6)
    c.alpha_composite(fachada_img(luz, acesa), (191, 1545 - 900))
    if luz == 'noite':
        d = ImageDraw.Draw(c); rnd = random.Random(4)
        for i in range(60):
            x, y = rnd.randint(0, W_), rnd.randint(0, 600); d.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(240, 240, 220, 255))
    return c


@lru_cache(maxsize=8)
def interior(luz='dia', forno=False):
    """dentro da padaria: parede de azulejo, forno de tijolo à direita, balcão de vidro (topo y≈1330)."""
    W, H = W_, H_
    c = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    p = Pen(W, H)
    par = {'dia': '#f6ead2', 'tarde': '#efd3a8', 'noite': '#5d5548', 'frio': '#cfd8dc'}[luz]
    p.poly([(0, 0), (W, 0), (W, H), (0, H)], hexc(par))
    d0 = mul(hexc(par), .9)
    for y in range(80, 1300, 110): p.stroke([(0, y), (W, y)], 3, d0)
    for x in range(0, W, 110): p.stroke([(x, 0), (x, 1300)], 3, d0)
    # janela com o céu
    ceu_c = {'dia': '#9fd3f0', 'tarde': '#f2b07a', 'noite': '#1d2440', 'frio': '#b8c7d6'}[luz]
    p.shape([(80, 250), (480, 250), (480, 700), (80, 700)], hexc(ceu_c), None, 8, 0)
    p.stroke([(280, 250), (280, 700)], 8); p.stroke([(80, 475), (480, 475)], 8)
    # prateleiras com pães
    p.shape([(560, 420), (1200, 420), (1200, 450), (560, 450)], hexc('#8a5a38'), None, 5, 0)
    p.shape([(560, 680), (1200, 680), (1200, 710), (560, 710)], hexc('#8a5a38'), None, 5, 0)
    # forno de tijolo
    p.shape([(640, 1300), (640, 860), (700, 780), (1140, 780), (1200, 860), (1200, 1300)], hexc('#b5553a'), hexc('#93432d'), 6, 0)
    for y in range(820, 1300, 60):
        p.stroke([(650, y), (1190, y)], 3, hexc('#8c3f2a'))
    boca = hexc('#ffb04a') if forno else hexc('#2b2220')
    p.shape([(780, 1250), (780, 1030), (830, 970), (1010, 970), (1060, 1030), (1060, 1250)], boca, None, 7, 0)
    if forno:
        p.shape([(820, 1250), (870, 1120), (920, 1200), (960, 1090), (1010, 1250)], hexc('#ff7a2a'), None, 0, 0)
    # chão
    p.poly([(0, 1300), (W, 1300), (W, H), (0, H)], hexc('#a7794f'))
    for x in range(-400, W + 400, 160): p.stroke([(x, 1300), (x + (x - 621) * .8, H)], 3, hexc('#8d6440'))
    # balcão de vidro
    p.shape([(30, 1700), (30, 1330), (1212, 1330), (1212, 1700)], hexc('#c79a6a'), hexc('#a87d50'), 7, 0)
    p.shape([(70, 1640), (70, 1390), (1172, 1390), (1172, 1640)], hexc('#d7eef2'), None, 5, 0)
    p.shape([(20, 1340), (20, 1300), (1222, 1300), (1222, 1340)], hexc('#8a5a38'), None, 6, 0)
    c.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    for k in range(5):
        c.alpha_composite(pao_img('comum', 140), (120 + k * 220, 1500))
    for k in range(5):
        c.alpha_composite(pao_img('comum', 110), (590 + k * 120, 330))
    if luz == 'noite' and forno:
        gl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
        dg.ellipse((520, 820, 1320, 1500), fill=(255, 170, 70, 110))
        c.alpha_composite(gl.filter(ImageFilter.GaussianBlur(60)))
    return c


@lru_cache(maxsize=32)
def pao_img(forma='comum', w=300):
    """pão dourado com contorno (largura w)."""
    p = Pen(600, 600)
    if forma == 'comum':
        p.shape(ell_pts(300, 330, 270, 140, 40), PAO, PAOD, 7, 18)
        for k in (-1, 0, 1): p.arc(300 + k * 110, 300, 50, 30, 200, 340, 8, PAOD)
    elif forma == 'guarda':
        pts = [(40, 330)] + [(300 - 260 * math.cos(a), 330 - 230 * math.sin(a)) for a in [i * math.pi / 20 for i in range(21)]]
        bico = [(560, 330), (495, 360), (430, 330), (365, 360), (300, 330), (235, 360), (170, 330), (105, 360), (40, 330)]
        p.shape(pts[1:] + bico, PAO, PAOD, 7, 18)
        p.shape([(285, 340), (315, 340), (315, 520), (285, 520)], PAO, PAOD, 6, 0)
        p.arc(255, 520, 45, 40, 0, 180, 18, PAOD)
    elif forma == 'peixe':
        p.shape(ell_pts(260, 300, 210, 130, 40), PAO, PAOD, 7, 18)
        p.shape([(440, 300), (570, 190), (570, 410)], PAO, PAOD, 7, 0)
        p.dot(150, 270, 22, PAOD)
    elif forma == 'estrela':
        pts = []
        for i in range(10):
            a = -math.pi / 2 + i * math.pi / 5; r = 270 if i % 2 == 0 else 115
            pts.append((300 + r * math.cos(a), 320 + r * math.sin(a)))
        p.shape(pts, PAO, PAOD, 7, 18)
    elif forma == 'rosto':
        p.shape(ell_pts(300, 320, 230, 250, 40), PAO, PAOD, 7, 18)
        # franja de massa (cabelo)
        p.shape([(90, 250), (120, 140), (220, 80), (380, 80), (480, 140), (510, 250), (420, 190), (300, 170), (180, 190)], PAOC, PAOD, 6, 0)
        for ex in (215, 385):
            p.dot(ex, 310, 52, PAOC, 6); p.dot(ex, 314, 22, PAOD)
        p.arc(300, 420, 60, 30, 20, 160, 9, PAOD)
    im = p.img.resize((w, w), Image.LANCZOS)
    return im


def put_pao(c, forma, x, base, w=300, s=1.0, rot=0):
    """pão centrado em x, base (fundo) em y."""
    if s <= .03: return
    ww = max(6, int(w * s))
    im = pao_img(forma, 300).resize((ww, ww), Image.LANCZOS)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height * .82)))


def vapor(c, x, y, f, s=1.0):
    if s <= .03: return
    d = ImageDraw.Draw(c)
    for k in range(3):
        ph = (f * 2 + k * 30) % 90
        a = int(140 * (1 - ph / 90) * s)
        xx = x + (k - 1) * 40 + 14 * math.sin((f + k * 20) * .12)
        d.ellipse((xx - 18, y - ph * 3 - 18, xx + 18, y - ph * 3 + 18), fill=(250, 250, 250, a))


@lru_cache(maxsize=4)
def avental_img():
    p = Pen(300, 360)
    p.shape([(60, 10), (240, 10), (280, 350), (20, 350)], hexc('#f6f2ea'), hexc('#dcd6c8'), 6, 0)
    p.shape([(110, 130), (190, 130), (190, 200), (110, 200)], hexc('#e9e3d6'), None, 4, 0)
    return p.img.resize((300, 360), Image.LANCZOS)
