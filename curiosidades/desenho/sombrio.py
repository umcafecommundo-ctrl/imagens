"""Estilo SOMBRIO (mistério em 1ª pessoa, cores frias e dessaturadas, neblina, HUD de cartões, legenda 1 palavra).
Inspirado na referência enviada pelo Luis em 20/11/2026. Use: from sombrio import *  (depois de from kit import *)."""
import sys, math, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import kit
from kit import OW, OH, back, ramp, clamp, lerp, smooth, easeOut, blinkAt
from art import Pen, hexc, mul, ell_pts, INK

W_, H_ = 1242, 2208
GF = '/usr/share/fonts/truetype/google-fonts/'
F_CAP = GF + 'ofl/archivoblack/ArchivoBlack-Regular.ttf'
F_STAMP = GF + 'ofl/anton/Anton-Regular.ttf'
F_B = GF + 'Poppins-Bold.ttf'; F_R = GF + 'Poppins-Regular.ttf'

# ------------------------------------------------------------------ cor (grade fria e lavada)
kit.GRADES['sombrio'] = dict(gain=(.93, .99, .98), lift=(16, 20, 20), sat=.38, vig=.42)
kit.GRADES['sombrio_noite'] = dict(gain=(.66, .74, .76), lift=(8, 11, 13), sat=.32, vig=.55)
for _k in ('sombrio', 'sombrio_noite'):
    kit._VIG[_k] = (1 - kit.GRADES[_k]['vig'] * kit._Q * 2.2)[..., None].astype(np.float32)


@lru_cache(maxsize=None)
def font(path, size):
    return ImageFont.truetype(path, size)


# ------------------------------------------------------------------ legenda: 1 palavra por vez
def cap1(im, ws, lf, y0=1505):
    if not ws or lf < ws[0][1] - 2: return im
    cur = [w for w, t in ws if lf >= t - 1]
    if not cur: return im
    w = cur[-1].strip('.,:;!?…"\'').lower()
    if not w: return im
    d = ImageDraw.Draw(im); f = font(F_CAP, 62)
    tw = d.textlength(w, font=f)
    x = OW / 2 - tw / 2
    d.text((x + 4, y0 + 6), w, font=f, fill=(20, 22, 24), stroke_width=7, stroke_fill=(20, 22, 24))
    d.text((x, y0), w, font=f, fill=(250, 250, 248), stroke_width=6, stroke_fill=(24, 26, 28))
    return im


def instala_legenda():
    for nm in ('__main__', '__mp_main__', 'motor'):
        m = sys.modules.get(nm)
        if m is not None and hasattr(m, 'draw_caption'): m.draw_caption = cap1


# ------------------------------------------------------------------ granulado
@lru_cache(maxsize=8)
def _grao(k):
    rnd = np.random.default_rng(k)
    n = rnd.integers(0, 255, (OH // 3, OW // 3), dtype=np.uint8)
    im = Image.fromarray(n, 'L').resize((OW, OH), Image.NEAREST)
    a = Image.new('RGBA', (OW, OH), (128, 128, 128, 0)); a.putalpha(im.point(lambda v: int(abs(v - 128) / 128 * 22)))
    return a


def grao(im, lf):
    im = im.convert('RGBA'); im.alpha_composite(_grao(lf % 6)); return im.convert('RGB')


# ------------------------------------------------------------------ HUD (em coordenadas da saída 1080x1920)
@lru_cache(maxsize=64)
def card_img(titulo, sub, w=470):
    ft, fs = font(F_B, 30), font(F_R, 25)
    lines = []
    for word in sub.split():
        if lines and ImageDraw.Draw(Image.new('L', (1, 1))).textlength(lines[-1] + ' ' + word, font=fs) < w - 40: lines[-1] += ' ' + word
        else: lines.append(word)
    h = 70 + 33 * len(lines)
    im = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((8, 8, w + 8, h + 8), 18, fill=(0, 0, 0, 90))
    d.rounded_rectangle((2, 2, w, h), 18, fill=(30, 34, 37, 238), outline=(150, 158, 160, 255), width=3)
    d.ellipse((20, 29, 33, 42), fill=(214, 120, 110, 255))
    d.text((42, 14), titulo.upper(), font=ft, fill=(236, 238, 232))
    for i, l in enumerate(lines): d.text((22, 58 + 33 * i), l, font=fs, fill=(176, 184, 184))
    return im


def card(im, titulo, sub, x, y, s, alvo=None):
    """cartão de informação; alvo=(x,y) desenha linha até o objeto."""
    if s <= .02: return
    c = card_img(titulo, sub)
    if alvo and s > .5:
        d = ImageDraw.Draw(im); a = clamp((s - .5) * 2)
        x1, y1 = lerp(x, alvo[0], a), lerp(y, alvo[1], a)
        d.line((x, y, x1, y1), fill=(230, 232, 226, 255), width=4); d.ellipse((x1 - 9, y1 - 9, x1 + 9, y1 + 9), outline=(230, 232, 226, 255), width=4)
    kit.paste_c(im, c, x, y, back(s) if s < 1 else 1)


@lru_cache(maxsize=32)
def stamp_img(t, size=96, big=False):
    f = font(F_STAMP, size)
    tw = int(ImageDraw.Draw(Image.new('L', (1, 1))).textlength(t, font=f))
    pad = 34 if big else 0
    im = Image.new('RGBA', (tw + 2 * pad + 30, int(size * 1.45) + 2 * pad // 2 + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if big:
        d.rounded_rectangle((8, 8, im.width - 8, im.height - 8), 22, fill=(206, 198, 160, 255), outline=(32, 30, 28, 255), width=9)
        d.text((pad + 15, 8 + pad // 2 - size * .08), t, font=f, fill=(40, 38, 34))
    else:
        d.text((15, 10), t, font=f, fill=(92, 140, 140), stroke_width=4, stroke_fill=(28, 34, 36))
    return im


def stamp(im, t, x, y, s, size=96, big=False, rot=-4):
    if s <= .02: return
    kit.paste_c(im, stamp_img(t, size, big).rotate(rot, Image.BICUBIC, expand=True), x, y, s)


def burst(im, t, x, y, s, size=70, cor=(208, 112, 112), rot=-8):
    if s <= .02: return
    f = font(F_CAP, size)
    tw = ImageDraw.Draw(Image.new('L', (1, 1))).textlength(t, font=f)
    R = max(tw * .75, size * 1.4)
    b = Image.new('RGBA', (int(2 * R + 40), int(1.5 * R + 40)), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    cx, cy = b.width / 2, b.height / 2; pts = []
    for i in range(26):
        a = 2 * math.pi * i / 26; r = (1 if i % 2 else .78)
        pts.append((cx + R * r * math.cos(a), cy + R * .72 * r * math.sin(a)))
    d.polygon(pts, fill=cor + (255,), outline=(36, 30, 32, 255)); d.line(pts + [pts[0]], fill=(36, 30, 32, 255), width=7)
    d.text((cx - tw / 2, cy - size * .62), t, font=f, fill=(250, 248, 244), stroke_width=6, stroke_fill=(36, 30, 32))
    kit.paste_c(im, b.rotate(rot, Image.BICUBIC, expand=True), x, y, s)


def painel(im, rotulo, valor, x, y, s, glitch=0.0, w=420):
    """placar digital (rótulo pequeno em cima + número grande verde-claro)."""
    if s <= .02: return
    h = 230
    p = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(p)
    d.rounded_rectangle((4, 4, w - 4, h - 4), 26, fill=(28, 32, 33, 245), outline=(70, 76, 78, 255), width=8)
    fl = font(F_B, 22); tw = d.textlength(rotulo, font=fl)
    d.text((w / 2 - tw / 2, 22), rotulo, font=fl, fill=(150, 160, 158))
    fv = font(F_STAMP, 130); tv = d.textlength(valor, font=fv)
    if glitch > 0:
        for dx, col in ((-10, (230, 80, 80, 200)), (10, (80, 200, 230, 200))):
            d.text((w / 2 - tv / 2 + dx * glitch, 42), valor, font=fv, fill=col)
    d.text((w / 2 - tv / 2, 42), valor, font=fv, fill=(214, 240, 168), stroke_width=2, stroke_fill=(120, 150, 90))
    kit.paste_c(im, p, x, y, back(s) if s < 1 else 1)


def interrog(im, x, y, f, s):
    if s <= .02: return
    for i, (dx, dy) in enumerate(((-90, 10), (0, -30), (90, 0))):
        kit.paste_c(im, stamp_img('?', 60), x + dx, y + dy + 8 * math.sin(f * .12 + i), s * (.8 + .2 * (i == 1)))


# ------------------------------------------------------------------ personagem: menino de olhos grandes
PELE, PELED = hexc('#e6c8ad'), hexc('#c9a88c')
JAQ, JAQD = hexc('#7b7863'), hexc('#5e5c4b')
CALCA = hexc('#2d2f32'); CABELO = hexc('#26241f')


def menino(phase=0.0, walk=0.0, expr='neutro', look=0.0, blink=0, tilt=0.0):
    """menino de frente/3-4, 600x1000, pés em y≈975. walk 0..1 = intensidade da caminhada; phase = fase."""
    p = Pen(600, 1000)
    sw = math.sin(phase) * walk
    # pernas
    for side, sg in ((-1, 1), (1, -1)):
        a = .42 * sw * sg
        hx, hy = 300 + side * 45, 720
        fx, fy = hx + 250 * math.sin(a), hy + 245 * math.cos(a)
        p.line([(hx, hy), ((hx + fx) / 2 + 8 * sg * walk, (hy + fy) / 2), (fx, fy)], CALCA, 46, 6)
        p.shape(ell_pts(fx + side * 6, fy + 8, 54, 24, 24), hexc('#d9dcd8'), hexc('#a9aeab'), 6, 6)
    # braços
    for side, sg in ((-1, -1), (1, 1)):
        a = .35 * sw * sg
        sx, sy = 300 + side * 112, 500
        hx, hy = sx + side * 18 + 200 * math.sin(a), sy + 200 * math.cos(a)
        p.line([(sx, sy), (hx, hy)], JAQ, 50, 6)
        p.dot(hx, hy + 18, 26, PELE, 6)
    # jaqueta
    p.shape([(195, 470), (405, 470), (425, 560), (420, 745), (180, 745), (175, 560)], JAQ, JAQD, 7, 16)
    p.shape([(250, 600), (350, 600), (350, 680), (250, 680)], mul(JAQ, 1.06), None, 5, 0)
    p.shape([(255, 455), (345, 455), (330, 500), (270, 500)], JAQD, None, 5, 0)   # gola
    # cabeça
    hy = 300
    p.shape(ell_pts(300, hy, 165, 158, 50), PELE, PELED, 7, 22)
    for side in (-1, 1): p.shape(ell_pts(300 + side * 162, hy + 25, 26, 34, 20), PELE, PELED, 5, 4)
    # cabelo
    hair = [(140, 300), (138, 220), (180, 160), (250, 135), (330, 133), (400, 150), (450, 205), (462, 290), (430, 250),
            (400, 225), (370, 245), (345, 215), (310, 240), (280, 212), (250, 240), (220, 215), (185, 250), (160, 270)]
    p.shape(hair, CABELO, None, 6, 0)
    # olhos grandes com olheiras
    for ex in (238, 362):
        ey = 318
        p.arc(ex, ey + 42, 46, 18, 20, 160, 9, hexc('#8b7d84'))
        if blink:
            p.stroke([(ex - 44, ey), (ex + 44, ey)], 8); continue
        r = 56 if expr == 'choque' else 50
        p.dot(ex, ey, r, hexc('#f4f4f0'), 7)
        lx = ex + look * 12
        p.dot(lx, ey + 2, 33, hexc('#93a2a3'), 4)
        p.dot(lx, ey + 2, 17 if expr != 'choque' else 12, hexc('#111214'))
        p.dot(lx + 9, ey - 9, 7, hexc('#ffffff'))
        if expr == 'preocupado':
            p.stroke([(ex - 40, ey - 70 + (8 if ex < 300 else -8) * 0), (ex + 40, ey - 70 - (10 if ex < 300 else -10))], 7)
    # boca
    if expr == 'choque':
        p.shape(ell_pts(300, 418, 24, 30, 20), hexc('#7a2e2e'), None, 5, 0)
    elif expr == 'preocupado':
        p.arc(300, 428, 26, 12, 200, 340, 7)
    else:
        p.stroke([(282, 420), (318, 420)], 7)
    im = p.img.resize((600, 1000), Image.LANCZOS)
    return im.rotate(tilt, Image.BICUBIC, center=(300, 975)) if tilt else im


kit.menino = menino
import art as _art; _art.menino = menino


def put_menino(c, x, feet, h, f, walk=0.0, seed=2, flip=False, **kw):
    if h < 8: return
    ph = round(((f * .28) % (2 * math.pi)) / (2 * math.pi) * 12) / 12 * 2 * math.pi if walk else 0.0
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    kw['look'] = round(kw.get('look', 0) * 4) / 4
    im = kit.sprite('menino', tuple(sorted(dict(kw, phase=round(ph, 3), walk=walk).items())), int(h), .6, flip)
    bob = (abs(math.sin(f * .28)) * .018 * h * walk) + .005 * math.sin(f * .11) * h
    kit.put(c, im, x, feet + h * .025 - bob)


# ------------------------------------------------------------------ cenário: cidade cinza com neblina
@lru_cache(maxsize=2)
def ceu(noite=False):
    a = np.zeros((H_, W_, 3), np.float32)
    top, bot = (np.array([160, 170, 168]), np.array([208, 212, 206])) if not noite else (np.array([52, 60, 64]), np.array([96, 104, 104]))
    t = np.linspace(0, 1, H_)[:, None, None]
    a[:] = top * (1 - t) + bot * t
    im = Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    d = ImageDraw.Draw(im)
    if not noite: d.ellipse((880, 220, 1080, 420), fill=(226, 224, 210, 255))
    return im


@lru_cache(maxsize=2)
def casas_strip(noite=False):
    W = W_ * 3
    p = Pen(W, 700)
    rnd = random.Random(7)
    x = -40
    while x < W:
        w = rnd.randint(170, 260); hh = rnd.randint(150, 250); base = 560
        col = hexc('#9aa3a1') if not noite else hexc('#4c5557')
        p.shape([(x, base), (x, base - hh), (x + w / 2, base - hh - 110), (x + w, base - hh), (x + w, base)], col, mul(col, .85), 5, 10)
        for k in range(2):
            wx = x + 30 + k * (w - 90)
            lit = (not noite and rnd.random() < .2) or (noite and rnd.random() < .45)
            p.poly([(wx, base - hh + 50), (wx + 50, base - hh + 50), (wx + 50, base - hh + 110), (wx, base - hh + 110)],
                   hexc('#f2e6b4') if lit else mul(col, .75))
        x += w + rnd.randint(-10, 30)
    p.poly([(0, 560), (W, 560), (W, 700), (0, 700)], hexc('#7f8886') if not noite else hexc('#3b4345'))
    return p.img.resize((W, 700), Image.LANCZOS)


@lru_cache(maxsize=2)
def postes_strip(noite=False):
    W = W_ * 3
    p = Pen(W, 1100)
    for x in range(120, W, 560):
        p.shape([(x - 14, 1100), (x - 14, 160), (x + 14, 160), (x + 14, 1100)], hexc('#3b4042'), None, 5, 0)
        p.shape([(x - 14, 150), (x + 120, 150), (x + 120, 175), (x - 14, 175)], hexc('#3b4042'), None, 5, 0)
        p.shape(ell_pts(x + 120, 195, 40, 26, 20), hexc('#f0e6b8') if noite else hexc('#cfd2c8'), None, 5, 0)
    return p.img.resize((W, 1100), Image.LANCZOS)


@lru_cache(maxsize=2)
def chao(noite=False):
    im = Image.new('RGBA', (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rua = (78, 84, 86) if not noite else (40, 44, 46)
    d.rectangle((0, 1560, W_, H_), fill=rua + (255,))
    d.rectangle((0, 1520, W_, 1580), fill=tuple(int(v * 1.35) for v in rua) + (255,))
    d.line((0, 1520, W_, 1520), fill=(36, 30, 38, 255), width=6)
    return im


@lru_cache(maxsize=4)
def neblina_img(dens=1.0):
    W = W_ * 2
    im = Image.new('RGBA', (W, 420), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rnd = random.Random(3)
    for i in range(26):
        x = rnd.randint(-100, W); y = rnd.randint(60, 300); r = rnd.randint(120, 260)
        d.ellipse((x - r, y - r * .45, x + r, y + r * .45), fill=(236, 238, 234, int(70 * dens)))
    return im.filter(ImageFilter.GaussianBlur(18))


def rua(f, scroll=0.0, noite=False, neb=1.0):
    """cidade com rolagem lateral (scroll em px do chão)."""
    c = ceu(noite).copy()
    cs = casas_strip(noite); off = int(scroll * .35) % W_
    c.alpha_composite(cs.crop((off, 0, off + W_, 700)), (0, 860))
    nb = neblina_img(neb); o2 = int(f * 1.2 + scroll * .5) % W_
    c.alpha_composite(nb.crop((o2, 0, o2 + W_, 420)), (0, 1180))
    c.alpha_composite(chao(noite))
    ps = postes_strip(noite); o3 = int(scroll * .9) % (560 * 2)
    c.alpha_composite(ps.crop((o3, 0, o3 + W_, 1100)), (0, 440))
    d = ImageDraw.Draw(c); o4 = int(scroll) % 300
    for x in range(-o4, W_, 300): d.rectangle((x, 1850, x + 150, 1866), fill=(150, 156, 156, 255))
    return c


# ------------------------------------------------------------------ torre do relógio
@lru_cache(maxsize=2)
def torre_img(noite=False):
    p = Pen(600, 1500)
    col = hexc('#8e9693') if not noite else hexc('#4a5254')
    p.shape([(140, 1500), (140, 380), (460, 380), (460, 1500)], col, mul(col, .82), 7, 18)
    p.shape([(110, 380), (300, 120), (490, 380)], mul(col, .7), None, 7, 0)
    p.shape([(120, 380), (480, 380), (480, 420), (120, 420)], mul(col, .9), None, 6, 0)
    for y in (900, 1150):
        p.shape([(250, y), (350, y), (350, y + 160), (250, y + 160)], hexc('#f0e6b4') if noite else mul(col, .65), None, 5, 0)
    p.shape([(230, 1350), (370, 1350), (370, 1500), (230, 1500)], mul(col, .55), None, 5, 0)
    return p.img.resize((600, 1500), Image.LANCZOS)


def mostrador(c, x, y, r, hora, minuto, aro=(200, 110, 110)):
    d = ImageDraw.Draw(c)
    d.ellipse((x - r - 10, y - r - 10, x + r + 10, y + r + 10), fill=(36, 30, 32, 255))
    d.ellipse((x - r, y - r, x + r, y + r), fill=aro + (255,))
    d.ellipse((x - r * .86, y - r * .86, x + r * .86, y + r * .86), fill=(244, 242, 236, 255))
    for i in range(12):
        a = i * math.pi / 6
        d.line((x + r * .72 * math.sin(a), y - r * .72 * math.cos(a), x + r * .8 * math.sin(a), y - r * .8 * math.cos(a)), fill=(36, 30, 32, 255), width=max(2, int(r * .04)))
    ah = (hora % 12 + minuto / 60) * math.pi / 6; am = minuto * math.pi / 30
    d.line((x, y, x + r * .45 * math.sin(ah), y - r * .45 * math.cos(ah)), fill=(30, 28, 30, 255), width=max(3, int(r * .1)))
    d.line((x, y, x + r * .68 * math.sin(am), y - r * .68 * math.cos(am)), fill=(30, 28, 30, 255), width=max(3, int(r * .06)))
    d.ellipse((x - r * .07, y - r * .07, x + r * .07, y + r * .07), fill=(30, 28, 30, 255))


def put_torre(c, x, feet, h, hora, minuto, noite=False):
    im = torre_img(noite).resize((int(h * .4), int(h)), Image.LANCZOS)
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - h)))
    mostrador(c, x, feet - h * .62, h * .095, hora, minuto)
