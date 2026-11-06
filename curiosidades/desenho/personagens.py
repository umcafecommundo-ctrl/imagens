"""Rooster, scientist and lab/farm sets in the same toon style (uses emu/art.py Pen)."""
import sys, math, random
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from art import Pen, INK, ell_pts, curve, hexc, mul, face, SKINS, background, dust

R = dict(body=hexc('#c2512c'), bodyD=hexc('#8e3519'), wing=hexc('#9a3b1d'), hackle=hexc('#eda33c'), hackleD=hexc('#c47d22'),
         head=hexc('#e2672c'), comb=hexc('#e3262b'), combD=hexc('#a8161b'), beak=hexc('#f2c03c'), leg=hexc('#e9b23a'),
         tail=hexc('#26493a'), tail2=hexc('#1a3026'), tailHi=hexc('#3f7a5c'))


def rooster(crow=0.0, blink=0, expr='calm', look=0.4, sleep=0.0, chief=False, step=0.0, ear=None):
    """Side view facing right, 600x800 design, feet at y~780.
    crow 0..1 = head back + beak open; sleep 0..1 = head tucked + eyes shut; ear: None|'open'|'closed' (draw ear hole)."""
    p = Pen(600, 800)
    chest = crow * 14
    bc = (290 - chest * .3, 540 - sleep * 12)
    # legs
    for k, dx in ((0, -26), (1, 24)):
        lift = max(0, math.sin(step * 2 * math.pi + k * math.pi)) * 30 if step else 0
        top = (bc[0] + dx, bc[1] + 100); ft = (bc[0] + dx + (lift * .6), 768 - lift)
        col = mul(R['leg'], .8) if k == 0 else R['leg']
        p.line([top, ((top[0] + ft[0]) / 2 - 8, (top[1] + ft[1]) / 2), ft], col, 13, 4)
        for tx, ty in ((40, 4), (28, -4), (-18, 2)):
            p.line([ft, (ft[0] + tx, ft[1] + ty)], col, 7, 3)
    # tail sickles (behind body)
    for i, (a, L, col) in enumerate(((-.25, 1.0, R['tail2']), (.05, 1.1, R['tail']), (.35, 1.0, R['tail2']), (.6, .85, R['tail']))):
        b = (bc[0] - 120, bc[1] - 40)
        tip = (b[0] - 150 * L * math.cos(a - .2), b[1] - 170 * L * math.sin(a + .9) + 40)
        mid = (b[0] - 30, b[1] - 230 * L + i * 40)
        pts = curve(b, mid, tip, 14)
        p.line(pts, col, 30 - i * 3, 5)
        p.stroke(pts[2:11], 4, R['tailHi'])
    # body + wing
    body = ell_pts(bc[0], bc[1], 165 + chest * .4, 130, 64, -.08, .1)
    p.shape(body, R['body'], R['bodyD'], 6, 22)
    wing = ell_pts(bc[0] - 10, bc[1] + 8, 96, 58, 40, -.18)
    p.shape(wing, R['wing'], mul(R['wing'], .75), 5, 10)
    for i in range(5):
        x = bc[0] - 70 + i * 26
        p.stroke([(x, bc[1] + 22), (x - 14, bc[1] + 52)], 4, mul(R['wing'], .6))
    # neck / hackles: from body front-top to head
    ha = -crow * .9 + sleep * .55
    hx = bc[0] + 130 - crow * 20 - sleep * 45
    hy = bc[1] - 250 + crow * 10 + sleep * 170
    nb1, nb2 = (bc[0] + 70, bc[1] - 80), (bc[0] + 145, bc[1] - 20)
    neck = [nb1, (hx - 45, hy + 10), (hx + 10, hy - 30), (hx + 40, hy + 20), nb2]
    neck = curve(nb1, (hx - 60, hy + 40), (hx - 30, hy), 8) + curve((hx + 40, hy + 10), (hx + 60, hy + 90), nb2, 8)
    p.shape(neck, R['hackle'], R['hackleD'], 6, 14)
    for i in range(7):
        t = i / 7; x = nb1[0] + (hx - nb1[0]) * t + 10; y = nb1[1] + (hy - nb1[1]) * t + 30
        p.stroke([(x, y), (x + 10, y + 34)], 4, R['hackleD'])
    H = lambda dx, dy: (hx + dx * math.cos(ha) - dy * math.sin(ha), hy + dx * math.sin(ha) + dy * math.cos(ha))
    # comb (behind head outline)
    cs = 1.35 if chief else 1.0
    comb = [H(-38, -30)]
    for i, (dx, h) in enumerate(((-30, 46), (-8, 58), (14, 54), (32, 40))):
        comb += [H(dx * cs - 8, -40 - h * cs), H(dx * cs + 8, -40 - h * cs)]
        comb.append(H(dx * cs + 14, -48))
    comb.append(H(42, -30))
    p.shape(comb, R['comb'], R['combD'], 5, 8)
    # wattle
    w = [H(22, 22), H(42, 26), H(40, 72 * cs), H(20, 76 * cs), H(12, 40)]
    p.shape(w, R['comb'], R['combD'], 5, 6)
    # head
    head = ell_pts(hx, hy, 50, 46, 36, ha)
    p.shape(head, R['head'], mul(R['head'], .8), 6, 10)
    # beak
    op = crow * .9
    up = [H(30, -26), H(104, -4 - op * 34), H(34, 6)]
    lo = [H(30, 4), H(96, 14 + op * 42), H(30, 26)]
    if op > .1: p.poly([H(44, 0), H(96, -op * 26), H(92, 12 + op * 34)], hexc('#5a1414'))
    p.poly(lo, mul(R['beak'], .85), 5); p.poly(up, R['beak'], 5)
    # ear patch
    if ear:
        e = H(-34, 22)
        if ear == 'open': p.dot(e[0], e[1], 15, hexc('#3a1a10'), 4)
        else:
            p.dot(e[0], e[1], 15, hexc('#f2efe6'), 4); p.stroke([(e[0] - 11, e[1]), (e[0] + 11, e[1])], 5)
    # eye
    ec = H(4, -12); er = 22 if expr == 'shock' else 17
    p.dot(ec[0], ec[1], er, (255, 255, 255), 4)
    lid = .5 if expr == 'side' else .42 if expr == 'smug' else 0
    L = max(lid, blink, 1.0 if sleep > .5 or expr == 'sleep' else 0)
    if L < .75:
        lk = max(-1, min(1, look))
        p.dot(ec[0] + lk * (er - 8), ec[1] + 2, 6 if expr == 'shock' else 7.5, INK)
        p.dot(ec[0] + lk * (er - 8) - 2, ec[1] - 2, 2.2, (255, 255, 255))
    if L > .02:
        top = ec[1] - er; yb = top + 2 * er * min(1, L)
        p.poly([(ec[0] - er - 1, top - 2), (ec[0] + er + 1, top - 2), (ec[0] + er + 1, yb), (ec[0] - er - 1, yb)], R['head'])
        if L >= 1: p.arc(ec[0], ec[1] - 2, er - 4, 7, 20, 160, 4)
        else: p.stroke([(ec[0] - er, yb), (ec[0] + er, yb)], 4)
    if expr in ('smug', 'side'): p.stroke([H(-6, -34), H(30, -28)], 5)
    if expr == 'shock': p.arc(ec[0], ec[1] - 30, 14, 5, 200, 340, 4)
    return p.img


# ---------------------------------------------------------------- scientist (bean card, lab coat)
COAT = hexc('#f3f3ee'); COAT_D = hexc('#c9ccd0'); PANTS = hexc('#4a4f5a'); SHOE = hexc('#2b2526')


def scientist(expr='neutral', arms='clip', blink=0, look=0.0, tilt=0.0, skin=0, hair='#3b2a1e', glasses=True, bun=False):
    p = Pen(600, 1000)
    for s in (-1, 1):
        top = (300 + s * 34, 690); ft = (300 + s * 40, 950)
        p.line([top, (top[0] + s * 4, 820), ft], PANTS, 15, 4)
        p.shape(ell_pts(ft[0] + 12, ft[1] + 10, 34, 18), SHOE, None, 4)
    tc = (300 + tilt * 3, 560)
    p.shape([(206, 600), (394, 600), (418, 735), (182, 735)], COAT, COAT_D, 5, 10)  # coat skirt
    p.shape(ell_pts(tc[0], tc[1], 112, 150, 56, math.radians(tilt), 0.12), COAT, COAT_D, 5, 16)
    p.poly([(270, 418), (330, 418), (300, 520)], hexc('#9cc3e6'), 3)  # shirt V
    p.stroke([(270, 420), (296, 560)], 4); p.stroke([(330, 420), (304, 560)], 4)
    p.stroke([(300, 560), (300, 730)], 3)
    p.poly([(330, 500), (372, 500), (372, 540), (330, 540)], COAT_D, 3)
    for x, c in ((340, '#e3262b'), (352, '#2c6bd6')): p.stroke([(x, 488), (x, 512)], 5, hexc(c))
    shL, shR = (205, 470), (395, 470)
    A = {'hang': [((185, 560), (190, 650)), ((415, 560), (410, 650))],
         'clip': [((180, 560), (250, 590)), ((420, 560), (350, 590))],
         'ears': [((150, 400), (188, 285)), ((450, 400), (412, 285))],
         'cheek': [((150, 420), (225, 300)), ((450, 420), (375, 300))],
         'point': [((185, 560), (190, 650)), ((470, 430), (560, 380))],
         'up': [((150, 380), (140, 240)), ((450, 380), (460, 240))]}[arms]
    if arms == 'clip':
        p.shape([(222, 520), (380, 520), (380, 640), (222, 640)], hexc('#9b6b3d'), None, 4)
        p.poly([(234, 536), (368, 536), (368, 632), (234, 632)], (255, 255, 255))
        for y in (556, 576, 596, 616): p.stroke([(246, y), (350, y)], 3, hexc('#9aa4b4'))
        p.poly([(280, 512), (322, 512), (322, 528), (280, 528)], hexc('#9aa0a8'), 3)
    for sh, (el, hd) in zip((shL, shR), A):
        p.line(curve(sh, el, hd, 10), COAT, 16, 4)
        p.dot(hd[0], hd[1], 17, SKINS[skin], 4)
    hc = (300 + tilt * 6, 262)
    hcol = hexc(hair)
    p.shape(ell_pts(hc[0], hc[1] - 30, 126, 100, 48), hcol, mul(hcol, .7), 5, 10)  # hair back
    if bun: p.shape(ell_pts(hc[0], hc[1] - 130, 46, 36, 32), hcol, mul(hcol, .7), 5, 6)
    p.shape(ell_pts(hc[0], hc[1], 118, 106, 56, math.radians(tilt * 1.5), 0.08, 2.4), SKINS[skin], mul(SKINS[skin], .86), 5, 16)
    p.dot(hc[0] - 112, hc[1] + 10, 16, SKINS[skin], 4); p.dot(hc[0] + 112, hc[1] + 10, 16, SKINS[skin], 4)
    fr = [(hc[0] - 120, hc[1] - 10), (hc[0] - 110, hc[1] - 80), (hc[0] - 40, hc[1] - 112), (hc[0] + 60, hc[1] - 110), (hc[0] + 118, hc[1] - 50),
          (hc[0] + 120, hc[1] - 20), (hc[0] + 60, hc[1] - 70), (hc[0] - 20, hc[1] - 62), (hc[0] - 90, hc[1] - 40)]
    p.shape(fr, hcol, mul(hcol, .7), 5, 8)
    face(p, hc[0], hc[1] + 10, expr, blink, look)
    if glasses:
        for s in (-1, 1):
            cx = hc[0] + s * 31; cy = hc[1] + 10
            p.d.ellipse([(cx - 25) * 2, (cy - 21) * 2, (cx + 25) * 2, (cy + 21) * 2], outline=INK + (255,), width=10)
        p.stroke([(hc[0] - 6, hc[1] + 6), (hc[0] + 6, hc[1] + 6)], 5)
    return p.img


# ---------------------------------------------------------------- props
def clock(hour_a, min_a, size=400, ring=False):
    p = Pen(500, 500)
    c = 250
    if ring:
        for s in (-1, 1): p.dot(c + s * 120, 70, 50, hexc('#d8382f'), 5)
        for s in (-1, 1): p.stroke([(c + s * 100, 470), (c + s * 140, 495)], 10)
    p.dot(c, c, 200, hexc('#d8382f') if ring else hexc('#5b6b8f'), 6)
    p.dot(c, c, 170, (252, 250, 240), 4)
    for i in range(12):
        a = i * math.pi / 6; r0 = 140 if i % 3 else 120
        p.stroke([(c + r0 * math.sin(a), c - r0 * math.cos(a)), (c + 158 * math.sin(a), c - 158 * math.cos(a))], 8 if i % 3 == 0 else 4)
    p.stroke([(c, c), (c + 90 * math.sin(hour_a), c - 90 * math.cos(hour_a))], 16)
    p.stroke([(c, c), (c + 140 * math.sin(min_a), c - 140 * math.cos(min_a))], 9)
    p.dot(c, c, 14, INK)
    return p.img.resize((size, size), Image.LANCZOS)


def lab_bg(W=1242, H=2208, floor=1500, night=True):
    S = 2; w, h = W * S, H * S; fy = floor * S
    img = Image.new('RGB', (w, h), hexc('#cfe0d6')); d = ImageDraw.Draw(img)
    # wall gradient
    a = np.array(img).astype(float)
    g = np.linspace(.92, 1.04, fy)[:, None, None]; a[:fy] *= g
    img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(img)
    d.rectangle([0, fy - 60 * S, w, fy], fill=hexc('#9fb8aa'), outline=INK, width=4 * S)  # baseboard
    # floor tiles
    for yy in range(fy, h, 90 * S):
        k = (yy - fy) // (90 * S)
        for xx in range(-90 * S if k % 2 else 0, w, 180 * S):
            col = hexc('#e6e2d8') if ((xx // (180 * S)) + k) % 2 else hexc('#d2cdbf')
            d.rectangle([xx, yy, xx + 180 * S, yy + 90 * S], fill=col, outline=hexc('#b5ae9c'), width=2 * S)
    d.line([(0, fy), (w, fy)], fill=INK, width=5 * S)
    # window (night) on the left
    wx0, wy0, wx1, wy1 = 90 * S, 620 * S, 520 * S, 1050 * S
    d.rectangle([wx0 - 20 * S, wy0 - 20 * S, wx1 + 20 * S, wy1 + 20 * S], fill=hexc('#f3f3ee'), outline=INK, width=5 * S)
    sky = np.linspace(0, 1, wy1 - wy0)[:, None, None] * (np.array(hexc('#2a3a78')) - np.array(hexc('#0f1636'))) + np.array(hexc('#0f1636'))
    img.paste(Image.fromarray(np.broadcast_to(sky, (wy1 - wy0, wx1 - wx0, 3)).astype(np.uint8)), (wx0, wy0)); d = ImageDraw.Draw(img)
    if night:
        d.ellipse([wx1 - 170 * S, wy0 + 50 * S, wx1 - 80 * S, wy0 + 140 * S], fill=hexc('#fff3c4'))
        d.ellipse([wx1 - 140 * S, wy0 + 40 * S, wx1 - 60 * S, wy0 + 120 * S], fill=hexc('#14204a'))
        rnd = random.Random(2)
        for i in range(14):
            x = rnd.randint(wx0 + 10 * S, wx1 - 10 * S); y = rnd.randint(wy0 + 10 * S, wy1 - 10 * S); r = rnd.choice((2, 3, 4)) * S
            d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 230))
    d.line([((wx0 + wx1) // 2, wy0), ((wx0 + wx1) // 2, wy1)], fill=hexc('#f3f3ee'), width=14 * S)
    d.line([(wx0, (wy0 + wy1) // 2), (wx1, (wy0 + wy1) // 2)], fill=hexc('#f3f3ee'), width=14 * S)
    d.rectangle([wx0, wy0, wx1, wy1], outline=INK, width=4 * S)
    # shelf with flasks on the right
    sx0, sy = 700 * S, 900 * S
    d.rectangle([sx0, sy, w - 60 * S, sy + 22 * S], fill=hexc('#a8794a'), outline=INK, width=4 * S)
    for i, col in enumerate(('#7fd18b', '#f28aa0', '#8ec5ff', '#ffd25e')):
        x = sx0 + (60 + i * 110) * S
        d.polygon([(x - 18 * S, sy - 90 * S), (x + 18 * S, sy - 90 * S), (x + 18 * S, sy - 60 * S), (x + 45 * S, sy), (x - 45 * S, sy), (x - 18 * S, sy - 60 * S)], fill=(235, 245, 250), outline=INK, width=4 * S)
        d.polygon([(x - 33 * S, sy - 25 * S), (x + 33 * S, sy - 25 * S), (x + 45 * S, sy - 2 * S), (x - 45 * S, sy - 2 * S)], fill=hexc(col))
    # ceiling lamps
    for lx in (330, 930):
        x = lx * S
        d.line([(x, 0), (x, 180 * S)], fill=INK, width=5 * S)
        d.polygon([(x - 110 * S, 260 * S), (x - 50 * S, 180 * S), (x + 50 * S, 180 * S), (x + 110 * S, 260 * S)], fill=hexc('#5b6b8f'), outline=INK, width=4 * S)
    return img.resize((W, H), Image.LANCZOS).convert('RGBA')


def lamp_glow(on=1.0, W=1242, H=2208):
    """additive warm cone under the lamps."""
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    if on <= 0: return g
    for lx in (330, 930):
        d.polygon([(lx - 110, 260), (lx + 110, 260), (lx + 420, 1500), (lx - 420, 1500)], fill=(255, 244, 190, int(60 * on)))
        d.ellipse([lx - 70, 230, lx + 70, 300], fill=(255, 250, 210, int(255 * on)))
    return g


def pen_rail(W=900, H=240):
    p = Pen(W, H)
    for x in range(20, W, 110): p.shape([(x, 10), (x + 22, 10), (x + 22, H - 6), (x, H - 6)], hexc('#b98b59'), hexc('#8e6438'), 4, 6)
    for y in (50, 150): p.shape([(0, y), (W, y), (W, y + 26), (0, y + 26)], hexc('#c99a66'), hexc('#9b6f3f'), 4, 6)
    return p.img.resize((W, H), Image.LANCZOS)


import os as _os
FONT_B = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'fonts', 'DejaVuSans-Bold.ttf')


def bubble_text(text, size=110, color=(255, 255, 255), rot=0):
    f = ImageFont.truetype(FONT_B, size)
    tw = int(ImageDraw.Draw(Image.new('L', (1, 1))).textlength(text, font=f))
    im = Image.new('RGBA', (tw + 60, size + 60), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((30, 20), text, font=f, fill=color + (255,), stroke_width=10, stroke_fill=INK + (255,))
    return im.rotate(rot, Image.BICUBIC, expand=True) if rot else im


def sound_rings(r, alpha, width=12):
    s = int(r * 2 + 40)
    im = Image.new('RGBA', (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = s / 2
    for k in (1, .72, .46):
        rr = r * k
        d.arc([c - rr, c - rr, c + rr, c + rr], -50, 50, fill=INK + (int(255 * alpha),), width=width + 8)
        d.arc([c - rr, c - rr, c + rr, c + rr], -50, 50, fill=(255, 216, 74, int(255 * alpha)), width=width)
    return im
