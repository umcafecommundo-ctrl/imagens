"""Estilo SOMBRIO (mistério em 1ª pessoa, cores frias e dessaturadas, neblina, HUD de cartões, legenda 1 palavra).
Inspirado na referência enviada pelo Luis em 20/11/2026. Use: from sombrio import *  (depois de from kit import *)."""
import sys, math, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import kit
from kit import OW, OH, back, ramp, clamp, lerp, smooth, easeOut, blinkAt
from art import Pen, hexc, mul, ell_pts, INK

W_, H_ = kit.BW, kit.BH   # 1242x2208 (vertical) ou 2208x1242 (MOTOR_H=1, horizontal)
GF = '/usr/share/fonts/truetype/google-fonts/'
F_CAP = GF + 'ofl/archivoblack/ArchivoBlack-Regular.ttf'
F_STAMP = GF + 'ofl/anton/Anton-Regular.ttf'
F_B = GF + 'Poppins-Bold.ttf'; F_R = GF + 'Poppins-Regular.ttf'

# ------------------------------------------------------------------ cor (grade fria e lavada)
kit.GRADES['sombrio'] = dict(gain=(.93, .99, .98), lift=(16, 20, 20), sat=.38, vig=.42)
kit.GRADES['sombrio_noite'] = dict(gain=(.66, .74, .76), lift=(8, 11, 13), sat=.32, vig=.55)
kit.GRADES['vivo'] = dict(gain=(1.02, 1.01, .99), lift=(4, 4, 4), sat=.92, vig=.22)      # dia claro, interiores, praia
kit.GRADES['tarde'] = dict(gain=(1.06, .97, .86), lift=(8, 5, 2), sat=.8, vig=.3)        # fim de tarde, memória, calor
kit.GRADES['frio'] = dict(gain=(.9, .97, 1.06), lift=(6, 9, 14), sat=.6, vig=.32)         # neve, hospital, madrugada
for _k in ('sombrio', 'sombrio_noite', 'vivo', 'tarde', 'frio'):
    kit._VIG[_k] = (1 - kit.GRADES[_k]['vig'] * kit._Q * 2.2)[..., None].astype(np.float32)


@lru_cache(maxsize=None)
def font(path, size):
    return ImageFont.truetype(path, size)


# ------------------------------------------------------------------ legenda: 1 palavra por vez
def cap1(im, ws, lf, y0=None):
    if y0 is None: y0 = 1505 if OH > OW else 930
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
    a = Image.new('RGBA', (OW, OH), (128, 128, 128, 0)); a.putalpha(im.point(lambda v: int(abs(v - 128) / 128 * 9)))
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


IRIS, IRIS_D = hexc('#4f8fb8'), hexc('#3c7aa3')   # íris azul viva (antes cinza apagado)


def menino(phase=0.0, walk=0.0, expr='neutro', look=0.0, blink=0, tilt=0.0, pele='#e6c8ad', cabelo='#26241f',
           penteado='curto', roupa='#7b7863', calca='#2d2f32', oculos=False, barba=False, velho=False):
    """pessoa de olhos grandes (estilo MISTÉRIO), 600x1000, pés em y≈975. walk 0..1 = caminhada; phase = fase.
    penteado: curto, coque, longo, careca; velho=True põe rugas e cabelo ralo; expr: neutro, curioso, preocupado, desconfiado, choque, medo, sorriso."""
    PELE, PELED = hexc(pele), mul(hexc(pele), .87)
    JAQ, JAQD = hexc(roupa), mul(hexc(roupa), .77)
    CALCA, CABELO = hexc(calca), hexc(cabelo)
    p = Pen(600, 1000)
    sw = math.sin(phase) * walk
    if penteado == 'longo':   # cabelo comprido fica atrás da cabeça
        p.shape([(150, 250), (140, 590), (230, 560), (370, 560), (460, 590), (450, 250)], CABELO, None, 6, 0)
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
    if penteado == 'careca':
        for side in (-1, 1): p.shape(ell_pts(300 + side * 150, 260, 30, 46, 16), CABELO, None, 5, 0)
    else:
        p.shape(hair, CABELO, None, 6, 0)
    if penteado == 'coque': p.shape(ell_pts(300, 128, 62, 50, 24), CABELO, None, 6, 0)
    if velho:
        for side in (-1, 1): p.arc(300 + side * 112, 365, 22, 14, 200, 340, 4, PELED)
    if barba:
        p.shape([(170, 360), (190, 450), (250, 470), (350, 470), (410, 450), (430, 360), (380, 420), (220, 420)], CABELO, None, 5, 0)
    # olhos grandes e ACORDADOS (24/11/2026: sem olheiras, íris viva, sobrancelha que mostra a emoção)
    for i, ex in enumerate((238, 362)):
        ey = 318
        sg = -1 if i == 0 else 1
        if blink:
            p.arc(ex, ey - 4, 40, 14, 20, 160, 8)
        else:
            r = 56 if expr in ('choque', 'medo') else 50
            p.dot(ex, ey, r, hexc('#fbfbf7'), 7)
            lx = ex + look * 12
            p.dot(lx, ey + 2, 34 if expr not in ('choque', 'medo') else 26, IRIS, 4)
            p.dot(lx, ey + 2, 19 if expr not in ('choque', 'medo') else 10, hexc('#111214'))
            p.dot(lx + 10, ey - 10, 9, hexc('#ffffff')); p.dot(lx - 8, ey + 10, 4, hexc('#ffffff'))
        # sobrancelhas sempre visíveis
        by = 264
        if expr in ('preocupado', 'medo'):
            p.stroke([(ex - 40 * sg, by - 4), (ex + 40 * sg, by + 14)], 9, CABELO)
        elif expr == 'choque':
            p.arc(ex, by - 14, 42, 16, 200, 340, 9, CABELO)
        elif expr == 'curioso':
            p.arc(ex, by - (16 if i == 1 else 0), 40, 12, 200, 340, 9, CABELO)
        elif expr == 'desconfiado':
            p.stroke([(ex - 40 * sg, by + 14), (ex + 40 * sg, by)], 9, CABELO)
        else:
            p.arc(ex, by - 6, 40, 12, 200, 340, 8, CABELO)
    if oculos:
        for ex in (238, 362): p.arc(ex, 318, 60, 60, 0, 360, 7)
        p.stroke([(298, 318), (302, 318)], 7)
    # boca
    if expr == 'sorriso':
        p.arc(300, 410, 34, 20, 20, 160, 7)
    elif expr in ('choque', 'medo'):
        p.shape(ell_pts(300, 418, 24, 30 if expr == 'choque' else 20, 20), hexc('#7a2e2e'), None, 5, 0)
    elif expr == 'curioso':
        p.shape(ell_pts(306, 420, 14, 14, 16), hexc('#7a2e2e'), None, 5, 0)
    elif expr == 'preocupado':
        p.arc(300, 428, 26, 12, 200, 340, 7)
    else:   # neutro: leve sorriso de canto (antes era uma linha reta, parecia sono)
        p.arc(302, 408, 24, 12, 30, 150, 7)
    im = p.img.resize((600, 1000), Image.LANCZOS)
    return im.rotate(tilt, Image.BICUBIC, center=(300, 975)) if tilt else im


kit.menino = menino
import art as _art; _art.menino = menino


def put_menino(c, x, feet, h, f, walk=0.0, seed=2, flip=False, dorme=False, **kw):
    if h < 8: return
    ph = round(((f * .28) % (2 * math.pi)) / (2 * math.pi) * 12) / 12 * 2 * math.pi if walk else 0.0
    kw['blink'] = 1 if (dorme or blinkAt(f, seed) > .6) else 0
    kw['look'] = round(kw.get('look', 0) * 4) / 4
    im = kit.sprite('menino', tuple(sorted(dict(kw, phase=round(ph, 3), walk=walk).items())), int(h), .6, flip)
    bob = (abs(math.sin(f * .28)) * .018 * h * walk) + .005 * math.sin(f * .11) * h
    kit.put(c, im, x, feet + h * .025 - bob)


# ------------------------------------------------------------------ cenário: cidade cinza com neblina
PALETAS = {   # céu topo, céu base, sol
    'dia': ((118, 178, 226), (206, 230, 240), (255, 238, 170)),
    'tarde': ((236, 156, 110), (250, 214, 160), (255, 230, 170)),
    'neblina': ((160, 170, 168), (208, 212, 206), (226, 224, 210)),
    'noite': ((52, 60, 64), (96, 104, 104), None),
}


def _luz(noite):
    return 'noite' if noite is True else ('neblina' if noite is False else noite)


@lru_cache(maxsize=8)
def ceu(noite='neblina'):
    noite = _luz(noite)
    a = np.zeros((H_, W_, 3), np.float32)
    t0, b0, sol = PALETAS[noite]
    top, bot = np.array(t0), np.array(b0)
    t = np.linspace(0, 1, H_)[:, None, None]
    a[:] = top * (1 - t) + bot * t
    im = Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    d = ImageDraw.Draw(im)
    if sol: d.ellipse((880, 220, 1080, 420), fill=sol + (255,))
    else: d.ellipse((900, 240, 1020, 360), fill=(230, 230, 214, 255))
    return im


CASAS = {'dia': ['#f2c6a0', '#a8d0e6', '#f4e1a1', '#c9e2b3', '#e8b4b8'], 'tarde': ['#e9b48a', '#d8a0a0', '#f0cf8e', '#c8b08a'],
         'neblina': ['#9aa3a1'], 'noite': ['#4c5557']}


@lru_cache(maxsize=8)
def casas_strip(noite='neblina'):
    noite = _luz(noite); cores = CASAS[noite]; escuro = noite == 'noite'
    W = W_ * 3
    p = Pen(W, 700)
    rnd = random.Random(7)
    x = -40
    while x < W:
        w = rnd.randint(170, 260); hh = rnd.randint(150, 250); base = 560
        col = hexc(rnd.choice(cores))
        p.shape([(x, base), (x, base - hh), (x + w / 2, base - hh - 110), (x + w, base - hh), (x + w, base)], col, mul(col, .85), 5, 10)
        for k in range(2):
            wx = x + 30 + k * (w - 90)
            lit = (not escuro and rnd.random() < .2) or (escuro and rnd.random() < .45)
            p.poly([(wx, base - hh + 50), (wx + 50, base - hh + 50), (wx + 50, base - hh + 110), (wx, base - hh + 110)],
                   hexc('#f2e6b4') if lit else mul(col, .75))
        x += w + rnd.randint(-10, 30)
    p.poly([(0, 560), (W, 560), (W, 700), (0, 700)], hexc({'dia': '#9fbf8a', 'tarde': '#b9a37a', 'neblina': '#7f8886', 'noite': '#3b4345'}[noite]))
    return p.img.resize((W, 700), Image.LANCZOS)


@lru_cache(maxsize=8)
def postes_strip(noite='neblina'):
    noite = _luz(noite) == 'noite'
    W = W_ * 3
    p = Pen(W, 1100)
    for x in range(120, W, 560):
        p.shape([(x - 14, 1100), (x - 14, 160), (x + 14, 160), (x + 14, 1100)], hexc('#3b4042'), None, 5, 0)
        p.shape([(x - 14, 150), (x + 120, 150), (x + 120, 175), (x - 14, 175)], hexc('#3b4042'), None, 5, 0)
        p.shape(ell_pts(x + 120, 195, 40, 26, 20), hexc('#f0e6b8') if noite else hexc('#cfd2c8'), None, 5, 0)
    return p.img.resize((W, 1100), Image.LANCZOS)


@lru_cache(maxsize=8)
def chao(noite='neblina'):
    noite = _luz(noite)
    im = Image.new('RGBA', (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rua = {'dia': (110, 116, 120), 'tarde': (112, 104, 100), 'neblina': (78, 84, 86), 'noite': (40, 44, 46)}[noite]
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


def rua(f, scroll=0.0, noite=False, neb=1.0, luz=None):
    """cidade com rolagem lateral (scroll em px do chão). luz: 'dia', 'tarde', 'neblina' ou 'noite' (conforme a história);
    neb = densidade da neblina (0 = sem neblina)."""
    noite = luz or _luz(noite)
    c = ceu(noite).copy()
    cs = casas_strip(noite); off = int(scroll * .35) % W_
    c.alpha_composite(cs.crop((off, 0, off + W_, 700)), (0, 860))
    if neb > 0:
        nb = neblina_img(round(neb, 1)); o2 = int(f * 1.2 + scroll * .5) % W_
        c.alpha_composite(nb.crop((o2, 0, o2 + W_, 420)), (0, 1180))
    c.alpha_composite(chao(noite))
    ps = postes_strip(noite); o3 = int(scroll * .9) % (560 * 2)
    c.alpha_composite(ps.crop((o3, 0, o3 + W_, 1100)), (0, 440))
    d = ImageDraw.Draw(c); o4 = int(scroll) % 300
    for x in range(-o4, W_, 300): d.rectangle((x, 1850, x + 150, 1866), fill=(150, 156, 156, 255))
    return c


# ------------------------------------------------------------------ torre do relógio
@lru_cache(maxsize=8)
def torre_img(noite=False):
    noite = _luz(noite) == 'noite'
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


def cta_card(im, cl, h):
    """cartão final do TikTok no estilo MISTÉRIO (use CTA_CARD = cta_card no historia.py)."""
    im = im.convert('RGBA')
    s_ = back(ramp(cl, 0, 8))
    if s_ > .02:
        c = Image.new('RGBA', (820, 330), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
        d.rounded_rectangle((6, 6, 814, 324), 30, fill=(30, 34, 37, 240), outline=(150, 158, 160, 255), width=5)
        f1 = font(F_STAMP, 96); t = getattr(h, 'CTA_TEXTO', 'COMENTA!')
        tw = d.textlength(t, font=f1); d.text((410 - tw / 2, 40), t, font=f1, fill=(214, 240, 168))
        f2 = font(F_B, 40); a = getattr(h, 'ARROBA', '@curiosidadesda.iia')
        tw = d.textlength(a, font=f2); d.text((410 - tw / 2, 220), a, font=f2, fill=(220, 224, 220))
        kit.paste_c(im, c, OW / 2, 560, s_)
    return im.convert('RGB')


# ------------------------------------------------------------------ praia e quarto no traço MISTÉRIO (cores pela luz)
MAR = {'dia': ('#4aa3c9', '#2f7fa6'), 'tarde': ('#5d8fb0', '#3f6f8f'), 'neblina': ('#7f9a9e', '#62797d'),
       'noite': ('#2c3d4a', '#1e2c36'), 'frio': ('#7fa9c4', '#5c86a3')}
AREIA = {'dia': '#ecd6a4', 'tarde': '#e3c08c', 'neblina': '#b9b39e', 'noite': '#6b6658', 'frio': '#d9d4c4'}


@lru_cache(maxsize=8)
def praia_bg(luz='dia'):
    """praia sem guarda-sol: céu pela luz, mar com 2 tons, areia, pedras; mar em y 980..1300, areia de 1300 para baixo."""
    c = ceu('neblina' if luz == 'frio' else luz).copy()
    p = Pen(W_, H_)
    m1, m2 = MAR[luz]
    p.poly([(0, 980), (W_, 980), (W_, 1320), (0, 1320)], hexc(m1))
    p.poly([(0, 980), (W_, 980), (W_, 1060), (0, 1060)], hexc(m2))
    sand = [(0, 1300)] + [(x, 1300 + 18 * math.sin(x / 90)) for x in range(0, W_ + 1, 40)] + [(W_, H_), (0, H_)]
    p.shape(sand, hexc(AREIA[luz]), mul(hexc(AREIA[luz]), .88), 6, 14)
    rnd = random.Random(5)
    for i in range(5):
        x, y = rnd.randint(40, 1200), rnd.randint(1700, 2150)
        p.shape(ell_pts(x, y, rnd.randint(40, 80), rnd.randint(22, 40), 20), mul(hexc(AREIA[luz]), .7), None, 5, 0)
    for i in range(40):
        x, y = rnd.randint(0, W_), rnd.randint(1380, 2200)
        p.dot(x, y, 4, mul(hexc(AREIA[luz]), .78))
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    if luz == 'frio':
        f = Image.new('RGBA', (W_, H_), (200, 215, 230, 60)); c.alpha_composite(f)
    return c


def espuma(c, f, luz='dia'):
    """ondas chegando na areia (anima com f)."""
    d = ImageDraw.Draw(c)
    for k in range(3):
        t = ((f * .012 + k / 3) % 1)
        y = 1080 + t * 230
        a = int(220 * (1 - t))
        pts = [(x, y + 10 * math.sin(x / 70 + f * .05 + k)) for x in range(-20, W_ + 40, 30)]
        d.line(pts, fill=(245, 250, 250, a), width=8)


@lru_cache(maxsize=8)
def quarto_bg(luz='dia'):
    """quarto: parede pela luz, janela para o mar (céu pela luz), cama e escrivaninha. chão em y 1560."""
    paredes = {'dia': '#e8dcc4', 'tarde': '#e2c7a6', 'neblina': '#b9bcb4', 'noite': '#4d5560', 'frio': '#c9d3d8'}
    p = Pen(W_, H_)
    w = hexc(paredes[luz])
    p.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], w)
    for x in range(0, W_, 120): p.stroke([(x, 0), (x, 1560)], 3, mul(w, .94))
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], mul(hexc('#a8835c'), .6 if luz == 'noite' else 1))
    for y in range(1620, H_, 110): p.stroke([(0, y), (W_, y)], 3, mul(hexc('#a8835c'), .75))
    p.stroke([(0, 1560), (W_, 1560)], 7)
    # janela (moldura)
    p.shape([(700, 360), (1140, 360), (1140, 900), (700, 900)], hexc('#f4f1ea'), hexc('#d6d1c6'), 7, 8)
    base = p.img.resize((W_, H_), Image.LANCZOS)
    # céu e mar pela janela
    sky = ceu('neblina' if luz == 'frio' else luz).crop((300, 300, 300 + 400, 300 + 500)).resize((400, 500))
    win = Image.new('RGBA', (400, 500)); win.alpha_composite(sky)
    d = ImageDraw.Draw(win); m1, m2 = MAR[luz]
    d.rectangle((0, 330, 400, 500), fill=hexc(m1) + (255,)); d.rectangle((0, 330, 400, 360), fill=hexc(m2) + (255,))
    base.alpha_composite(win, (720, 380))
    d = ImageDraw.Draw(base)
    d.line((920, 380, 920, 880), fill=(244, 241, 234, 255), width=16); d.line((720, 630, 1120, 630), fill=(244, 241, 234, 255), width=16)
    d.rectangle((720, 380, 1120, 880), outline=(36, 30, 32, 255), width=7)
    # cama à esquerda e escrivaninha à direita
    p2 = Pen(W_, H_)
    p2.shape([(40, 1300), (520, 1300), (520, 1620), (40, 1620)], hexc('#6f8fb5') if luz != 'noite' else hexc('#3e5270'), None, 7, 12)
    p2.shape([(40, 1180), (90, 1180), (90, 1660), (40, 1660)], hexc('#8a5a32'), None, 6, 0)
    p2.shape([(110, 1250), (260, 1250), (260, 1310), (110, 1310)], hexc('#f4f1ea'), None, 6, 0)
    p2.shape([(760, 1220), (1200, 1220), (1200, 1260), (760, 1260)], hexc('#9a6a40'), hexc('#6f4a2a'), 6, 6)
    for x in (780, 1160): p2.shape([(x, 1260), (x + 26, 1260), (x + 26, 1560), (x, 1560)], hexc('#7a5230'), None, 5, 0)
    base.alpha_composite(p2.img.resize((W_, H_), Image.LANCZOS))
    return base


@lru_cache(maxsize=8)
def garrafa_img(h, rolha=True, bilhete=True):
    p = Pen(200, 520)
    p.shape([(70, 40), (130, 40), (132, 160), (175, 230), (178, 500), (22, 500), (25, 230), (68, 160)],
            hexc('#bfe3d4'), hexc('#8fc2ad'), 6, 14)
    if rolha: p.shape([(72, 10), (128, 10), (126, 60), (74, 60)], hexc('#b8865a'), None, 5, 0)
    if bilhete: p.shape([(60, 260), (140, 250), (145, 420), (65, 430)], hexc('#f6efd9'), None, 4, 0)
    p.stroke([(55, 250), (55, 470)], 8, hexc('#e8f6f0'))
    return p.img.resize((max(4, int(h * 200 / 520)), max(4, h)), Image.LANCZOS)


def put_garrafa(c, x, y, h, rot=0, **kw):
    if h < 8: return
    im = garrafa_img(int(h // 4 * 4), **kw)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


F_MAO = GF + 'ofl/comicrelief/ComicRelief-Bold.ttf'


@lru_cache(maxsize=32)
def bilhete_img(texto, w=520):
    """papel com texto escrito à mão ('|' quebra linha)."""
    linhas = texto.split('|')
    f = font(F_MAO, 46)
    h = 120 + 64 * len(linhas)
    im = Image.new('RGBA', (w + 20, h + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle((14, 14, w + 14, h + 14), fill=(0, 0, 0, 70))
    d.polygon([(4, 8), (w, 2), (w + 6, h), (8, h + 4)], fill=(246, 239, 217, 255), outline=(36, 30, 32, 255))
    d.line([(4, 8), (w, 2), (w + 6, h), (8, h + 4), (4, 8)], fill=(36, 30, 32, 255), width=5)
    for i, l in enumerate(linhas):
        tw = d.textlength(l, font=f)
        d.text(((w - tw) / 2, 60 + 64 * i), l, font=f, fill=(52, 58, 92))
    return im


def mao_dir(x, feet, h):
    """posição da mão direita (braço caído) da pessoa de put_menino."""
    return x + .13 * h, feet - .26 * h


# ------------------------------------------------------------------ CLOSE no rosto (pedido do Luis em 20/11/2026)
def rosto(expr='neutro', look=0.0, blink=0, pele='#e6c8ad', cabelo='#26241f', penteado='curto', roupa='#7b7863',
          oculos=False, barba=False, velho=False, suor=0, tremor=0, calca=None):
    """rosto em close (1000x1700): cabeça grande + ombros até embaixo. expr: neutro, curioso, preocupado, choque, sorriso, medo, desconfiado.
    24/11/2026 (pedido do Luis, "cara de sono"): sem olheiras, íris viva, sobrancelhas altas, piscada em arco."""
    K = 2.6
    def T(x, y): return (500 + (x - 300) * K, 560 + (y - 300) * K)
    def TP(pts): return [T(x, y) for x, y in pts]
    PELE, PELED = hexc(pele), mul(hexc(pele), .87)
    JAQ, JAQD = hexc(roupa), mul(hexc(roupa), .77)
    CAB = hexc(cabelo)
    p = Pen(1000, 1700)
    if penteado == 'longo':
        p.shape(TP([(150, 250), (130, 640), (230, 600), (370, 600), (470, 640), (450, 250)]), CAB, None, 8, 0)
    # ombros e pescoço
    p.shape([(40, 1675), (90, 1120), (300, 1000), (700, 1000), (910, 1120), (960, 1675)], JAQ, JAQD, 9, 12)
    p.poly([(36, 1660), (964, 1660), (964, 1700), (36, 1700)], JAQ)
    p.shape([(400, 900), (600, 900), (590, 1040), (410, 1040)], PELED, None, 8, 0)
    p.shape([(360, 1000), (640, 1000), (600, 1070), (400, 1070)], JAQD, None, 8, 0)
    # cabeça
    p.shape([T(x, y) for x, y in ell_pts(300, 300, 165, 158, 60)], PELE, PELED, 9, 22)
    for side in (-1, 1): p.shape([T(x, y) for x, y in ell_pts(300 + side * 162, 325, 26, 34, 20)], PELE, PELED, 7, 6)
    hair = [(140, 300), (138, 220), (180, 160), (250, 135), (330, 133), (400, 150), (450, 205), (462, 290), (430, 250),
            (400, 225), (370, 245), (345, 215), (310, 240), (280, 212), (250, 240), (220, 215), (185, 250), (160, 270)]
    if penteado == 'careca':
        for side in (-1, 1): p.shape([T(x, y) for x, y in ell_pts(300 + side * 150, 260, 30, 46, 16)], CAB, None, 7, 0)
    else:
        p.shape(TP(hair), CAB, None, 8, 0)
    if penteado == 'coque': p.shape([T(x, y) for x, y in ell_pts(300, 128, 62, 50, 24)], CAB, None, 8, 0)
    if barba:
        p.shape(TP([(170, 360), (190, 450), (250, 470), (350, 470), (410, 450), (430, 360), (380, 420), (220, 420)]), CAB, None, 7, 0)
    # bochechas
    if expr in ('sorriso', 'medo'):
        for ex in (215, 385): p.dot(*T(ex, 385), 34, hexc('#f0a3a0'))
    # olhos
    for i, ex in enumerate((238, 362)):
        ey = 318
        cx, cy = T(ex, ey)
        if blink:
            p.arc(cx, cy - 10, 40 * K, 14 * K, 20, 160, 12)
        else:
            r = (56 if expr in ('choque', 'medo') else 50) * K
            if expr == 'desconfiado': r = 46 * K
            p.dot(cx, cy, r, hexc('#f4f4f0'), 10)
            lx = cx + look * 30 + (math.sin(tremor * 7 + i) * 6 if tremor else 0)
            iris = 33 * K * (.8 if expr in ('choque', 'medo') else 1)
            p.dot(lx, cy + 4, iris, IRIS, 6)
            p.dot(lx, cy + 4, iris * .82, IRIS_D)
            pup = (8 if expr in ('choque', 'medo') else 17) * K
            p.dot(lx, cy + 4, pup, hexc('#111214'))
            p.dot(lx + 24, cy - 26, 20, hexc('#ffffff')); p.dot(lx - 20, cy + 22, 9, hexc('#ffffff'))
            if expr == 'desconfiado':
                p.poly([(cx - r - 10, cy - r - 10), (cx + r + 10, cy - r - 10), (cx + r + 10, cy - r * .25), (cx - r - 10, cy - r * .25)], PELE)
                p.stroke([(cx - r, cy - r * .25), (cx + r, cy - r * .25)], 10)
        # sobrancelhas
        sg = -1 if i == 0 else 1
        bx, by = T(ex, 266)
        if expr in ('preocupado', 'medo'):
            p.stroke([(bx - 70, by + sg * -14 + 10), (bx + 70, by - sg * -14 + 10)], 14, CAB)
            p.stroke([(bx - 70 * sg, by + 20), (bx + 70 * sg, by - 16)], 14, CAB) if False else None
        elif expr == 'choque':
            p.arc(bx, by - 10, 70, 26, 200, 340, 14, CAB)
        elif expr in ('desconfiado',):
            p.stroke([(bx - 70, by + (20 if i == 0 else -6)), (bx + 70, by + (-6 if i == 0 else 20))], 14, CAB)
        elif expr == 'curioso':
            p.arc(bx, by - (34 if i == 1 else 6), 70, 22, 200, 340, 14, CAB)
        else:   # neutro/sorriso: sobrancelha alta e arqueada (olhar atento, não sonolento)
            p.arc(bx, by - 18, 68, 22, 200, 340, 13, CAB)
    if oculos:
        for ex in (238, 362): p.arc(*T(ex, 318), 60 * K, 60 * K, 0, 360, 12)
    # boca
    mx, my = T(300, 420)
    if expr == 'sorriso':
        p.shape([(mx - 80, my - 10), (mx + 80, my - 10), (mx + 50, my + 50), (mx - 50, my + 50)], hexc('#7a2e2e'), None, 8, 0)
        p.poly([(mx - 70, my - 6), (mx + 70, my - 6), (mx + 60, my + 12), (mx - 60, my + 12)], hexc('#ffffff'))
    elif expr in ('choque', 'medo'):
        p.shape([T(x, y) for x, y in ell_pts(300, 425, 22, 30 if expr == 'choque' else 18, 24)], hexc('#7a2e2e'), None, 8, 0)
    elif expr == 'preocupado':
        p.arc(mx, my + 14, 50, 20, 200, 340, 11)
    elif expr == 'desconfiado':
        p.stroke([(mx - 40, my + 6), (mx + 50, my - 6)], 11)
    elif expr == 'curioso':
        p.shape([T(x, y) for x, y in ell_pts(306, 425, 14, 14, 20)], hexc('#7a2e2e'), None, 8, 0)
    else:   # neutro: leve sorriso de canto
        p.arc(mx + 6, my - 16, 52, 24, 30, 150, 11)
    if suor:
        sx, sy = T(440, 210)
        p.shape([(sx, sy - 40), (sx + 24, sy + 10), (sx, sy + 34), (sx - 24, sy + 10)], hexc('#bfe3f5'), None, 6, 0)
    return p.img.resize((1000, 1700), Image.LANCZOS)


kit.rosto = rosto
_art.rosto = rosto


@lru_cache(maxsize=16)
def _fundo_borrado(key, im_bytes_id):
    return None


def put_close(c, f, expr='neutro', look=0.0, seed=2, s=1.0, fundo_blur=14, escurece=0.0, shake=0.0, **kw):
    """CLOSE no rosto: borra o cenário (c) e desenha o rosto grande no centro, com leve respiração e tremida.
    s = escala (1 = rosto ocupa ~80% da largura). escurece 0..1 escurece o fundo (suspense). Mantenha as cores do personagem (**kw)."""
    if s <= .02: return c
    bg = c.filter(ImageFilter.GaussianBlur(fundo_blur)) if fundo_blur else c.copy()
    if escurece > 0:
        bg.alpha_composite(Image.new('RGBA', bg.size, (10, 12, 14, int(150 * escurece))))
    kw['blink'] = 1 if blinkAt(f, seed) > .6 and expr not in ('choque', 'medo') else 0
    q = dict(kw); q['look'] = round(look * 4) / 4
    q['tremor'] = round(f / 3) if shake > 0 else 0
    im = kit.sprite('rosto', tuple(sorted(dict(q, expr=expr).items())), int(1700 * s), 1000 / 1700, False)
    bob = 6 * math.sin(f * .11)
    sx = shake * 8 * math.sin(f * 2.3)
    bg.alpha_composite(im, (int(621 - im.width / 2 + sx), int(1040 - 560 * s + bob)))
    return bg
