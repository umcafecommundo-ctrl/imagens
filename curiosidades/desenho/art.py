"""Drawing kit: Pen (toon fill + plum ink), soldier bean card, emu sprite, truck, backgrounds."""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops

INK = (36, 23, 38)
K = 2  # supersample for sprites


def hexc(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mul(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c)


def ell_pts(cx, cy, rx, ry, n=48, rot=0.0, egg=0.0, sq=2.0):
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        c, s = math.cos(a), math.sin(a)
        # superellipse
        x = rx * math.copysign(abs(c) ** (2 / sq), c)
        y = ry * math.copysign(abs(s) ** (2 / sq), s)
        if s > 0: x *= 1 + egg * s
        xr = x * math.cos(rot) - y * math.sin(rot)
        yr = x * math.sin(rot) + y * math.cos(rot)
        pts.append((cx + xr, cy + yr))
    return pts


def curve(a, b, c, n=12):
    return [((1 - t) ** 2 * a[0] + 2 * (1 - t) * t * b[0] + t * t * c[0],
             (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * b[1] + t * t * c[1]) for t in [i / (n - 1) for i in range(n)]]


class Pen:
    def __init__(self, w, h):
        self.W, self.H = w, h
        self.img = Image.new('RGBA', (w * K, h * K), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)

    def _p(self, pts):
        return [(x * K, y * K) for x, y in pts]

    def shape(self, pts, fill, dark=None, ow=5, sh=14):
        """Filled polygon with toon shadow crescent (light from upper-left) and ink outline thicker lower-right."""
        pts = self._p(pts)
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        pad = int((ow + 6) * K)
        x0, y0 = max(0, int(min(xs)) - pad), max(0, int(min(ys)) - pad)
        x1, y1 = min(self.W * K, int(max(xs)) + pad), min(self.H * K, int(max(ys)) + pad)
        if x1 <= x0 or y1 <= y0: return
        w, h = x1 - x0, y1 - y0
        loc = [(x - x0, y - y0) for x, y in pts]
        m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).polygon(loc, fill=255)
        if ow > 0:
            r = int(ow * K)
            ink = m.filter(ImageFilter.MaxFilter(2 * (r // 2) + 1)) if r > 1 else m
            ink2 = ImageChops.offset(ink, int(1.6 * K), int(1.6 * K))
            ink = ImageChops.lighter(ink, ink2)
            ink = ink.filter(ImageFilter.MaxFilter(3))
            self.img.paste(INK + (255,), (x0, y0), ink)
        self.img.paste(tuple(fill) + (255,), (x0, y0), m)
        if dark is not None:
            m2 = ImageChops.offset(m, int(-sh * K), int(-sh * K))
            shadow = ImageChops.subtract(m, m2).filter(ImageFilter.GaussianBlur(K * 1.2))
            shadow = ImageChops.multiply(shadow, m)
            self.img.paste(tuple(dark) + (255,), (x0, y0), shadow)

    def line(self, pts, color, w, ow=4):
        pts = self._p(pts)
        if ow > 0:
            self._ln(pts, INK, (w + 2 * ow) * K)
        self._ln(pts, color, w * K)

    def _ln(self, pts, color, w):
        self.d.line(pts, fill=tuple(color) + (255,), width=int(w), joint='curve')
        r = w / 2
        for x, y in (pts[0], pts[-1]):
            self.d.ellipse([x - r, y - r, x + r, y + r], fill=tuple(color) + (255,))

    def stroke(self, pts, w, color=INK):
        self._ln(self._p(pts), color, w * K)

    def dot(self, x, y, r, color, ow=0):
        x, y, r = x * K, y * K, r * K
        if ow: self.d.ellipse([x - r - ow * K, y - r - ow * K, x + r + ow * K, y + r + ow * K], fill=INK + (255,))
        self.d.ellipse([x - r, y - r, x + r, y + r], fill=tuple(color) + (255,))

    def arc(self, cx, cy, rx, ry, a0, a1, w, color=INK):
        pts = [(cx + rx * math.cos(math.radians(a)), cy + ry * math.sin(math.radians(a))) for a in np.linspace(a0, a1, 16)]
        self.stroke(pts, w, color)

    def poly(self, pts, color, ow=0):
        p = self._p(pts)
        if ow: self.d.polygon(p, fill=tuple(color) + (255,), outline=INK + (255,), width=int(ow * K))
        else: self.d.polygon(p, fill=tuple(color) + (255,))


# ---------------------------------------------------------------- SOLDIER (bean card 600x1000, soles y=975)
SKINS = [hexc('#ffe2c2'), hexc('#f5c9a0'), hexc('#ecd0b6'), hexc('#c99067')]
KHAKI = hexc('#b8a063'); KHAKI_D = hexc('#8f7a44'); LEG = hexc('#7d6a3c'); BOOT = hexc('#3b2a1e')
HELM = hexc('#6f7a4a'); HELM_D = hexc('#4f5733'); BELT = hexc('#5a3d24')


def face(p, cx, cy, expr, blink, look=0.0, u=2.36):
    ex = 13 * u
    lx = look * 6
    # brows
    brow = {'neutral': 0, 'stern': 14, 'grin': -6, 'shock': -18, 'pained': -16, 'smug': 8, 'proud': -4, 'nervous': -14}.get(expr, 0)
    by = cy - 38 - (14 if expr == 'shock' else 0)
    for s in (-1, 1):
        a = math.radians(brow) * s
        x0, x1 = cx + s * ex - 15, cx + s * ex + 15
        p.stroke([(x0, by + math.sin(a) * -15 * s), (x1, by + math.sin(a) * 15 * s)], 6)
    for s in (-1, 1):
        x, y = cx + s * ex, cy
        if blink > 0.6:
            p.stroke([(x - 12, y), (x + 12, y)], 5)
        elif expr in ('grin', 'proud', 'laugh'):
            p.arc(x, y + 6, 13, 11, 200, 340, 6)
        elif expr == 'shock':
            p.dot(x, y, 19, (255, 255, 255), 4); p.dot(x + lx, y, 6, INK)
        elif expr == 'smug':
            p.dot(x + 6, y + 2, 8, INK); p.stroke([(x - 14, y - 4), (x + 14, y - 4)], 6)
        elif expr == 'pained':
            p.stroke([(x - 12, y - 6), (x + 10, y), (x - 12, y + 6)] if s < 0 else [(x + 12, y - 6), (x - 10, y), (x + 12, y + 6)], 5)
        else:
            p.dot(x + lx, y, 9, INK); p.dot(x + lx - 3, y - 3, 2.5, (255, 255, 255))
    my = cy + 48
    if expr in ('grin', 'proud'):
        p.poly([(cx - 34, my - 6), (cx + 34, my - 6), (cx + 20, my + 22), (cx - 20, my + 22)], hexc('#7a2e2e'), 4)
        p.poly([(cx - 30, my - 4), (cx + 30, my - 4), (cx + 26, my + 4), (cx - 26, my + 4)], (255, 255, 255))
    elif expr == 'shock':
        p.dot(cx, my + 10, 17, hexc('#7a2e2e'), 4)
    elif expr == 'pained':
        pts = [(cx - 28 + i * 8, my + 6 + (5 if i % 2 else -5)) for i in range(8)]
        p.stroke(pts, 5)
    elif expr == 'smug':
        p.arc(cx + 6, my - 6, 24, 12, 20, 160, 6)
    else:
        p.stroke([(cx - 18, my + 4), (cx + 18, my + 4)], 6)


def soldier(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, walk=0.0, skin=0, mous=False, sweat=False):
    p = Pen(600, 1000)
    u = 2.36
    hip = (300, 690)
    # legs
    for s in (-1, 1):
        sw = math.sin(walk * 2 * math.pi) * 40 * s if walk else 0
        lift = max(0, math.sin(walk * 2 * math.pi) * s) * 22 if walk else 0
        top = (300 + s * 34, 680); foot = (300 + s * 40 + sw, 950 - lift)
        p.line([top, ((top[0] + foot[0]) / 2 + s * 4, 820), foot], LEG, 15, 4)
        p.shape(ell_pts(foot[0] + 12, foot[1] + 10, 34, 18), BOOT, None, 4)
    # torso + skirt
    tc = (300 + tilt * 3, 560)
    p.shape([(208, 640), (392, 640), (412, 712), (188, 712)], KHAKI, KHAKI_D, 5, 10)
    p.shape(ell_pts(tc[0], tc[1], 112, 150, 56, math.radians(tilt), 0.12), KHAKI, KHAKI_D, 5, 16)
    p.poly([(196, 628), (404, 628), (404, 652), (196, 652)], BELT, 3)
    p.dot(300, 640, 12, hexc('#d9b44a'), 3)
    for y in (480, 540, 600): p.dot(300 + tilt * 2, y, 6, hexc('#d9b44a'), 2)
    p.poly([(236, 500), (276, 500), (276, 530), (236, 530)], KHAKI_D, 3)
    # arms
    shL, shR = (205, 470), (395, 470)
    A = {
        'hang': [((185, 560), (190, 650)), ((415, 560), (410, 650))],
        'salute': [((185, 560), (190, 650)), ((470, 350), (395, 200))],
        'thumb': [((185, 560), (190, 650)), ((480, 520), (470, 410))],
        'cheek': [((150, 420), (225, 300)), ((450, 420), (375, 300))],
        'shrug': [((140, 540), (120, 440)), ((460, 540), (480, 440))],
        'point': [((185, 560), (190, 650)), ((470, 430), (560, 400))],
    }[arms]
    for sh, (el, hd) in zip((shL, shR), A):
        p.line(curve(sh, el, hd, 10), hexc('#a28a50'), 14, 4)
        p.dot(hd[0], hd[1], 17, SKINS[skin], 4)
    if arms == 'thumb':
        p.line([(470, 395), (470, 360)], SKINS[skin], 10, 4)
    # head
    hc = (300 + tilt * 6, 262)
    p.shape(ell_pts(hc[0], hc[1], 118, 106, 56, math.radians(tilt * 1.5), 0.08, 2.4), SKINS[skin], mul(SKINS[skin], .86), 5, 16)
    p.dot(hc[0] - 112, hc[1] + 10, 16, SKINS[skin], 4)
    p.dot(hc[0] + 112, hc[1] + 10, 16, SKINS[skin], 4)
    face(p, hc[0], hc[1] + 10, expr, blink, look)
    if mous:
        p.poly([(hc[0] - 40, hc[1] + 46), (hc[0], hc[1] + 38), (hc[0] + 40, hc[1] + 46), (hc[0] + 28, hc[1] + 56), (hc[0], hc[1] + 48), (hc[0] - 28, hc[1] + 56)], hexc('#5b3a22'), 3)
    # Brodie helmet
    p.shape([(x, min(y, hc[1] - 92)) for x, y in ell_pts(hc[0], hc[1] - 92, 96, 78, 48, 0, 0, 2.2)], HELM, HELM_D, 5, 12)
    p.shape(ell_pts(hc[0], hc[1] - 92, 158, 24, 40), HELM, HELM_D, 5, 6)
    if arms == 'salute':  # flat hand drawn over the brim
        p.shape(ell_pts(395, 196, 40, 14, 24, -0.3), SKINS[skin], None, 4)
    if sweat:
        p.shape([(hc[0] + 120, hc[1] - 70), (hc[0] + 108, hc[1] - 40), (hc[0] + 120, hc[1] - 28), (hc[0] + 132, hc[1] - 40)], hexc('#9fd3ff'), None, 3)
    return p.img


# ---------------------------------------------------------------- EMU (side view 600x800, feet y=780, faces right)
EMU = dict(body=hexc('#4d3b2c'), bodyDk=hexc('#2f241b'), streak=hexc('#7a6048'), neck=hexc('#7f90ad'), neckDk=hexc('#56627c'),
           head=hexc('#3a2f28'), beak=hexc('#cdb68e'), leg=hexc('#8c8780'), legDk=hexc('#5e5a55'))


def ik2(h, f, L1, L2):
    dx, dy = f[0] - h[0], f[1] - h[1]
    d = min(L1 + L2 - 1, math.hypot(dx, dy))
    a = math.atan2(dy, dx)
    c = math.acos(max(-1, min(1, (L1 * L1 + d * d - L2 * L2) / (2 * L1 * d))))
    return (h[0] + math.cos(a + c) * L1, h[1] + math.sin(a + c) * L1)


def emu(phase=0.0, run=0.0, peck=0.0, blink=0, expr='calm', look=0.3, seed=1, helmet=False):
    p = Pen(600, 800)
    two = 2 * math.pi
    bob = run * 16 * abs(math.sin(two * phase)) + (1 - run) * 3 * math.sin(seed * 3.1)
    lean = run * 0.16 + peck * 0.12
    hip = (292, 528 + bob * .6)
    bc = (290, 432 + bob)

    def rot(pt, a):
        x, y = pt[0] - bc[0], pt[1] - bc[1]
        return (bc[0] + x * math.cos(a) - y * math.sin(a), bc[1] + x * math.sin(a) + y * math.cos(a))

    legs = []
    for k in (1, 0):
        ph = phase + k * .5
        sx, sy = math.cos(two * ph), max(0, math.sin(two * ph))
        h = (hip[0] + (-14 if k else 14), hip[1])
        foot = (h[0] + run * 135 * sx + (1 - run) * (-22 if k else 26), 772 - run * 92 * sy)
        legs.append((h, ik2(h, foot, 138, 150), foot, sy * run))

    def leg(L, far):
        col = EMU['legDk'] if far else EMU['leg']
        h, kn, ft, lift = L
        p.line([h, kn, ft], col, 15, 3)
        for dx, dy in ((34, 2), (26, -6), (-14, 0)):
            p.line([ft, (ft[0] + dx, ft[1] + dy - lift * 10)], col, 7, 3)
    leg(legs[0], True)
    # neck
    nb = rot((392, 372 + bob), -lean * .4)
    hd = (448 + run * 70, 128 + run * 72 + bob * .5)
    hd = (hd[0] * (1 - peck) + 548 * peck, hd[1] * (1 - peck) + 700 * peck)
    nm = ((nb[0] + hd[0]) / 2 + 30 - run * 10 + peck * 40, (nb[1] + hd[1]) / 2 + (-60 * peck if peck else 10))
    npts = curve(nb, nm, hd, 14)
    p.line(npts, EMU['neck'], 40, 5)
    for x, y in npts[2:12]: p.stroke([(x - 6, y + 4), (x + 2, y - 4)], 3, EMU['neckDk'])
    # shaggy body
    bp = []
    for i in range(64):
        a = two * i / 64; c, s = math.cos(a), math.sin(a)
        rx, ry = 168, 112
        if c < -.3: rx *= 1 + .12 * (-c - .3)
        x = bc[0] + rx * c; y = bc[1] + ry * s + (26 * -c * (1 if s > -.2 else .2) if c < 0 else 0)
        if s > .15: y += (1 if i % 2 else -.4) * (16 + 6 * math.sin(i * 1.7 + seed))
        bp.append(rot((x, y), -lean))
    p.shape(bp, EMU['body'], EMU['bodyDk'], 6, 22)
    rnd = random.Random(seed)
    for i in range(22):
        x = bc[0] - 130 + rnd.random() * 250; y = bc[1] - 70 + rnd.random() * 130
        p.stroke([(x, y), (x - 24, y + 22)], 4, EMU['streak'] if i % 2 else EMU['bodyDk'])
    leg(legs[1], False)
    # head
    hx, hy = hd; ha = peck * 1.1 + run * .25
    H = lambda dx, dy: (hx + dx * math.cos(ha) - dy * math.sin(ha), hy + dx * math.sin(ha) + dy * math.cos(ha))
    p.poly([H(22, -10), H(76, 2), H(74, 8), H(20, 14)], EMU['beak'], 5)
    p.stroke([H(28, 4), H(70, 5)], 2.5)
    p.shape(ell_pts(hx, hy, 46, 38, 32, ha), EMU['head'], mul(EMU['head'], .7), 6, 10)
    if not helmet:
        p.stroke([H(-18, -28), H(-26, -44)], 5, EMU['head']); p.stroke([H(-4, -31), H(-6, -48)], 5, EMU['head'])
    ec = H(8, -6); er = 22 if expr == 'shock' else 18
    p.dot(ec[0], ec[1], er, (255, 255, 255), 4)
    lid = .5 if expr == 'side' else .42 if expr == 'smug' else 0
    lk = max(-1, min(1, look))
    if blink < .75:
        p.dot(ec[0] + lk * (er - 9), ec[1] + 2, 6 if expr == 'shock' else 8, INK)
        p.dot(ec[0] + lk * (er - 9) - 2, ec[1] - 2, 2.4, (255, 255, 255))
    L = max(lid, blink)
    if L > .02:
        top = ec[1] - er; yb = top + 2 * er * L
        p.poly([(ec[0] - er - 1, top - 2), (ec[0] + er + 1, top - 2), (ec[0] + er + 1, yb), (ec[0] - er - 1, yb)], EMU['head'])
        p.stroke([(ec[0] - er, yb), (ec[0] + er, yb)], 4)
    if expr in ('smug', 'side'): p.stroke([H(-8, -30), H(26, -24)], 5)
    if expr == 'shock': p.arc(ec[0], ec[1] - 30, 14, 5, 200, 340, 4)
    if helmet:
        p.shape([(x, min(y, hy - 30)) for x, y in ell_pts(hx - 4, hy - 30, 44, 36, 40, ha)], HELM, HELM_D, 5, 6)
        p.shape(ell_pts(hx - 4, hy - 30, 72, 11, 32, ha), HELM, HELM_D, 5, 4)
    return p.img


# ---------------------------------------------------------------- TRUCK (side 900x520, wheels bottom y~515)
def truck(wheel_rot=0.0):
    p = Pen(900, 520)
    G = hexc('#5b6b3f'); Gd = hexc('#3f4b2b'); W = hexc('#8a6a42'); Wd = hexc('#6a4f30')
    p.shape([(90, 330), (850, 330), (850, 420), (90, 420)], Gd, None, 5)
    p.shape([(100, 250), (560, 250), (560, 340), (100, 340)], W, Wd, 5, 8)
    for x in range(150, 560, 70): p.stroke([(x, 256), (x, 334)], 3, Wd)
    p.stroke([(104, 292), (556, 292)], 3, Wd)
    p.shape([(570, 170), (770, 170), (800, 260), (800, 360), (570, 360)], G, Gd, 5, 12)
    p.poly([(600, 190), (750, 190), (772, 255), (600, 255)], hexc('#bfe0f0'), 4)
    p.shape([(800, 255), (880, 270), (880, 360), (800, 360)], G, Gd, 5, 8)
    for x in range(820, 875, 14): p.stroke([(x, 290), (x, 345)], 3, Gd)
    p.dot(882, 290, 12, hexc('#fff3b0'), 3)
    for wx in (220, 700):
        p.dot(wx, 440, 72, hexc('#2a2328'), 5); p.dot(wx, 440, 36, hexc('#9a9a8e'), 4)
        for k in range(4):
            a = wheel_rot + k * math.pi / 2
            p.stroke([(wx, 440), (wx + 30 * math.cos(a), 440 + 30 * math.sin(a))], 5)
    return p.img


# ---------------------------------------------------------------- BACKGROUNDS
LIGHTS = {
    'day': dict(top='#2d74d4', hor='#cfe3f5', field='#e2bf5c', fieldD='#c79c3e', hill='#8fae6a', far='#a9c3c8', sun=None),
    'golden': dict(top='#6474c0', hor='#ffc485', field='#e7ae55', fieldD='#bf8338', hill='#b19a62', far='#d3a98e', sun='#fff0c0'),
    'dusk': dict(top='#18234f', hor='#d18a7c', field='#8a6f74', fieldD='#5f4c5c', hill='#5c5a72', far='#8e7488', sun=None),
}


def background(light, W=1242, H=2208, horizon=1060, seed=3):
    L = LIGHTS[light]; S = 2
    w, h = W * S, H * S
    y = np.linspace(0, 1, h)[:, None]
    top, hor = np.array(hexc(L['top'])), np.array(hexc(L['hor']))
    t = np.clip(y / (horizon / H), 0, 1) ** 1.8
    sky = (top * (1 - t) + hor * t)
    img = Image.fromarray(np.repeat(sky[:, None, :], 1, axis=1).astype(np.uint8).repeat(w, axis=1)[:, :, :] if False else np.broadcast_to(sky[:, None, :], (h, w, 3)).astype(np.uint8))
    d = ImageDraw.Draw(img)
    rnd = random.Random(seed)
    hz = horizon * S
    if L['sun']:
        cx, cy = w * .72, hz - 160 * S
        for r, a in ((260, .25), (170, .5), (95, 1)):
            col = tuple(int(c1 * a + c0 * (1 - a)) for c1, c0 in zip(hexc(L['sun']), hexc(L['hor'])))
            d.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], fill=col)
    # clouds
    for i in range(int(W / 300) + 2):
        cx = rnd.random() * w; cy = (150 + rnd.random() * 520) * S
        col = (255, 255, 255) if light == 'day' else mul(hexc(L['hor']), 1.08)
        for j in range(5):
            rx = (60 + rnd.random() * 70) * S; dx = (j - 2) * 70 * S
            d.ellipse([cx + dx - rx, cy - rx * .6, cx + dx + rx, cy + rx * .5], fill=col)
    # far mesas / hills
    far = hexc(L['far']); hill = hexc(L['hill'])
    for i in range(int(W / 200) + 3):
        cx = rnd.random() * w; r = (160 + rnd.random() * 220) * S
        d.ellipse([cx - r, hz - r * .45, cx + r, hz + r * .45], fill=far, outline=mul(far, .7), width=3 * S)
    for i in range(int(W / 260) + 3):
        cx = rnd.random() * w; r = (220 + rnd.random() * 260) * S
        d.ellipse([cx - r, hz - r * .3, cx + r, hz + r * .3], fill=hill, outline=INK, width=4 * S)
    # trees
    for i in range(int(W / 280) + 2):
        tx = rnd.random() * w; ty = hz - 8 * S; s = (.6 + rnd.random() * .5) * S
        d.rectangle([tx - 8 * s, ty - 70 * s, tx + 8 * s, ty], fill=hexc('#6b4a2f'), outline=INK, width=int(3 * S))
        for k in range(5):
            ox, oy, r = (rnd.random() - .5) * 70 * s, -90 * s - rnd.random() * 50 * s, (30 + rnd.random() * 18) * s
            d.ellipse([tx + ox - r, ty + oy - r * .8, tx + ox + r, ty + oy + r * .8], fill=mul(hill, .78), outline=INK, width=int(3 * S))
    # field
    f0, f1 = np.array(hexc(L['field'])), np.array(hexc(L['fieldD']))
    gy = np.linspace(0, 1, h - hz)[:, None]
    gcol = f1 * (1 - gy) * .35 + f0 * (.65 + .35 * gy)
    arr = np.array(img)
    arr[hz:] = np.broadcast_to(gcol[:, None, :], (h - hz, w, 3)).astype(np.uint8)
    img = Image.fromarray(arr); d = ImageDraw.Draw(img)
    d.line([(0, hz), (w, hz)], fill=INK, width=4 * S)
    # wheat strokes, denser & bigger toward viewer
    for i in range(int(W * 9)):
        yy = hz + (rnd.random() ** 1.6) * (h - hz)
        dep = (yy - hz) / (h - hz)
        xx = rnd.random() * w; ln = (6 + 34 * dep) * S
        col = mul(hexc(L['fieldD']), .9 + rnd.random() * .25) if i % 3 else mul(hexc(L['field']), 1.12)
        d.line([(xx, yy), (xx + ln * .25, yy - ln)], fill=col, width=max(1, int((1 + 3 * dep) * S)))
    # fence
    fy = hz + 90 * S
    for x in range(0, w, 160 * S):
        d.rectangle([x, fy - 60 * S, x + 10 * S, fy], fill=hexc('#8a6a42'), outline=INK, width=2 * S)
    for yy in (fy - 48 * S, fy - 26 * S):
        d.line([(0, yy), (w, yy)], fill=hexc('#7a5a36'), width=4 * S)
    return img.resize((W, H), Image.LANCZOS).convert('RGBA')


def dust(r, alpha, col=(232, 214, 170)):
    S = 2; s = int(r * 2.4) + 8
    im = Image.new('RGBA', (s * S, s * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = s * S / 2
    for dx, dy, k in ((0, 0, 1), (-.5, .2, .7), (.5, .25, .75), (0, -.35, .6)):
        rr = r * k * S
        d.ellipse([c + dx * r * S - rr - 6, c + dy * r * S - rr - 6, c + dx * r * S + rr + 6, c + dy * r * S + rr + 6], fill=INK + (255,))
    for dx, dy, k in ((0, 0, 1), (-.5, .2, .7), (.5, .25, .75), (0, -.35, .6)):
        rr = r * k * S
        d.ellipse([c + dx * r * S - rr, c + dy * r * S - rr, c + dx * r * S + rr, c + dy * r * S + rr], fill=col + (255,))
    im = im.resize((s, s), Image.LANCZOS)
    a = np.array(im); a[..., 3] = (a[..., 3] * alpha).astype(np.uint8)
    return Image.fromarray(a)
