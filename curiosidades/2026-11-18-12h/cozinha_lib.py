"""Ovo, batata, novelos de proteína, células da batata e garfo (dupla ovo/batata, 18/11/2026)."""
from kit import *
import os, importlib.util
from functools import lru_cache

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1007_ovo', '2026-11-10-07h')
panela, fogo, termo = _m.panela, _m.fogo, _m.termo

SHELL = hexc('#f3e6cf'); SHELLD = hexc('#d8c3a0')
POT = hexc('#c99a5b'); POTD = hexc('#9c7038')
YARN = [hexc('#f2a93b'), hexc('#e9677a'), hexc('#5fb0e0'), hexc('#8bc34a'), hexc('#b07ad8')]


@lru_cache(maxsize=8)
def ovo_img(w, cozido=0, eyes=0):
    p = Pen(300, 380)
    if not cozido:
        p.shape(ell_pts(150, 200, 120, 160, 48, 0, .18), SHELL, SHELLD, 6, 18)
        p.dot(110, 130, 14, (255, 255, 255))
    else:
        p.shape(ell_pts(150, 200, 120, 160, 48, 0, .18), (255, 255, 255), hexc('#e3e3e3'), 6, 14)
        p.shape(ell_pts(150, 225, 62, 62, 36), hexc('#ffc93c'), hexc('#e8a417'), 5, 8)
    if eyes:
        for x in (115, 185):
            p.dot(x, 170, 20, (255, 255, 255), 4); p.dot(x + 4, 172, 9, INK)
        p.arc(150, 215, 22, 12, 20, 160, 4)
    im = p.img
    return im.resize((int(w), int(w * 380 / 300)), Image.LANCZOS)


@lru_cache(maxsize=8)
def batata_img(w, eyes=0, cozida=0):
    p = Pen(420, 300)
    p.shape(ell_pts(210, 160, 185, 120, 56, .08, .06), POT if not cozida else hexc('#e8c98a'), POTD, 6, 16)
    for x, y in ((120, 120), (250, 100), (300, 190), (170, 210)):
        p.dot(x, y, 7, POTD)
    if cozida:
        p.shape(ell_pts(210, 150, 120, 70, 40), hexc('#f6e3a8'), None, 0, 0)
    if eyes:
        for x in (175, 245):
            p.dot(x, 140, 20, (255, 255, 255), 4); p.dot(x + 4, 142, 9, INK)
        p.arc(210, 185, 22, 12, 20, 160, 4)
    return p.img.resize((int(w), int(w * 300 / 420)), Image.LANCZOS)


def lupa(c, cx, cy, R, fill=(255, 250, 225), alpha=235):
    """círculo de 'zoom' (dentro do ovo/batata); devolve (layer, draw) para desenhar dentro e depois `lupa_fim`."""
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=fill + (alpha,))
    return lay, d


def lupa_fim(c, lay, cx, cy, R):
    mask = Image.new('L', c.size, 0); ImageDraw.Draw(mask).ellipse((cx - R, cy - R, cx + R, cy + R), fill=255)
    out = Image.new('RGBA', c.size, (0, 0, 0, 0)); out.paste(lay, (0, 0), mask)
    c.alpha_composite(out)
    d = ImageDraw.Draw(c)
    d.ellipse((cx - R - 12, cy - R - 12, cx + R + 12, cy + R + 12), outline=INK + (255,), width=14)
    d.ellipse((cx - R - 4, cy - R - 4, cx + R + 4, cy + R + 4), outline=(250, 250, 250, 255), width=6)


def _proteina(i, cx, cy, R, f, u):
    rnd = random.Random(i * 7 + 1)
    gx = (i % 3 - 1) * R * .55 + rnd.uniform(-30, 30)
    gy = (i // 3 - 1) * R * .55 + rnd.uniform(-30, 30)
    x0 = cx + gx + 10 * math.sin(f * .07 + i); y0 = cy + gy + 10 * math.cos(f * .06 + i * 2)
    th = rnd.uniform(0, math.pi)
    L = R * .7
    pts = []
    for k in range(40):
        t = k / 39
        a = t * 4.2 * math.pi + i
        r = 8 + t * R * .14
        sx, sy = x0 + r * math.cos(a), y0 + r * math.sin(a)
        ux = x0 + (t - .5) * L * math.cos(th) - 18 * math.sin(t * 14 + f * .1) * math.sin(th)
        uy = y0 + (t - .5) * L * math.sin(th) + 18 * math.sin(t * 14 + f * .1) * math.cos(th)
        pts.append((lerp(sx, ux, u), lerp(sy, uy, u)))
    return pts


def clara(c, cx, cy, R, f, u=0.0, link=0.0, white=0.0, agua=0.0):
    """dentro da clara: novelos (u=0) que se abrem em fios (u=1), se agarram (link) e a clara fica branca (white)."""
    if R < 8: return
    base = tuple(int(lerp(a, b, white)) for a, b in zip((255, 246, 200), (255, 255, 255)))
    lay, d = lupa(c, cx, cy, R, base, int(lerp(200, 255, white)))
    allp = [_proteina(i, cx, cy, R, f, u) for i in range(9)]
    if link > 0:
        for i in range(9):
            for j in (i + 1, i + 3):
                if j < 9 and (j != i + 1 or i % 3 != 2):
                    a = allp[i][int(39 * .8)]; b = allp[j][int(39 * .2)]
                    e = clamp(link * 1.6 - (i % 4) * .15)
                    if e > 0:
                        bx, by = lerp(a[0], b[0], e), lerp(a[1], b[1], e)
                        d.line([a, (bx, by)], fill=INK + (255,), width=16)
                        d.line([a, (bx, by)], fill=YARN[(i + 2) % 5] + (255,), width=9)
                        if e >= 1: d.ellipse((bx - 12, by - 12, bx + 12, by + 12), fill=INK + (255,))
    for i, pts in enumerate(allp):
        d.line(pts, fill=INK + (255,), width=18, joint='curve')
        d.line(pts, fill=YARN[i % 5] + (255,), width=10, joint='curve')
    if agua > 0:
        rnd = random.Random(11)
        for k in range(14):
            x = cx + rnd.uniform(-.75, .75) * R; y = cy + rnd.uniform(-.75, .75) * R
            r = 20 * clamp(agua * 1.5 - k * .04)
            if r > 2:
                d.ellipse((x - r, y - r * 1.1, x + r, y + r * 1.1), fill=(90, 170, 230, 255), outline=INK + (255,), width=4)
    lupa_fim(c, lay, cx, cy, R)


def celulas(c, cx, cy, R, f, cola=1.0, solta=0.0, brilho=0.0):
    """dentro da batata: células-tijolinho com cola (pectina) entre elas; solta=1 -> células separadas e arredondadas."""
    if R < 8: return
    lay, d = lupa(c, cx, cy, R, (240, 205, 120), 255)
    cw, ch, gap = 150, 110, 18
    rows = range(-5, 6); cols = range(-4, 5)
    if cola > 0:
        a = int(255 * cola)
        g = tuple(int(lerp(x, y, brilho)) for x, y in zip((214, 160, 60), (255, 220, 90)))
        d.rectangle((cx - R, cy - R, cx + R, cy + R), fill=g + (a,))
    rnd = random.Random(4)
    for r in rows:
        for q in cols:
            off = (cw + gap) / 2 if r % 2 else 0
            x = cx + q * (cw + gap) + off; y = cy + r * (ch + gap)
            dx = rnd.uniform(-1, 1); dy = rnd.uniform(-1, 1)
            x += solta * (dx * 40 + (x - cx) * .15) + solta * 6 * math.sin(f * .1 + q + r)
            y += solta * (dy * 40 + (y - cy) * .15) + solta * 6 * math.cos(f * .1 + q)
            rr = lerp(14, 50, solta)
            s = lerp(1, .82, solta)
            d.rounded_rectangle((x - cw / 2 * s, y - ch / 2 * s, x + cw / 2 * s, y + ch / 2 * s), radius=rr,
                                fill=(252, 236, 180, 255), outline=INK + (255,), width=6)
            d.ellipse((x - 12, y - 10, x + 12, y + 10), fill=(230, 200, 130, 255))
    lupa_fim(c, lay, cx, cy, R)


@lru_cache(maxsize=2)
def garfo_img(h):
    p = Pen(160, 700)
    p.shape([(65, 300), (95, 300), (100, 690), (60, 690)], hexc('#c9ced6'), hexc('#9aa1ab'), 5, 6)
    p.shape([(20, 160), (140, 160), (140, 240), (100, 320), (60, 320), (20, 240)], hexc('#dfe3ea'), hexc('#9aa1ab'), 5, 8)
    for x in (32, 80, 128):
        p.shape([(x - 12, 10), (x + 12, 10), (x + 12, 200), (x - 12, 200)], hexc('#dfe3ea'), hexc('#9aa1ab'), 5, 4)
    return p.img.resize((int(h * 160 / 700), int(h)), Image.LANCZOS)
