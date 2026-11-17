"""Lontra-marinha boiando de costas (card 900x520, linha d'água em y~330) e fundos de mar aberto."""
from kit import *
import cenarios
from functools import lru_cache

FUR = hexc('#8a5a3a'); FURD = hexc('#6a4026'); FACE = hexc('#e9dcc4'); FACED = hexc('#cbb89a')
KELP = hexc('#7a8f2e'); KELPD = hexc('#5a6b1e')


def lontra(sleep=0.0, expr='calm', look=0.3, blink=0, kelp=0.0, bob=0.0):
    p = Pen(900, 520)
    b = bob * 8
    # rabo (esquerda) e pés para cima
    p.shape([(150, 300 + b), (40, 270 + b), (30, 300 + b), (150, 330 + b)], FUR, FURD, 5, 8)
    for dx in (0, 46):
        p.shape(ell_pts(210 + dx, 230 + b, 26, 44, 24, -.4), FURD, mul(FURD, .8), 5, 6)
    # corpo deitado
    p.shape(ell_pts(390, 300 + b, 250, 95, 48), FUR, FURD, 6, 18)
    p.shape(ell_pts(410, 262 + b, 190, 42, 40), mul(FUR, 1.12), None, 0, 0)
    # alga amarrada na barriga
    if kelp > 0.01:
        for i, x in enumerate((330, 420)):
            if kelp > i * .4:
                p.shape([(x - 18, 200 + b), (x + 18, 200 + b), (x + 34, 400 + b), (x - 2, 400 + b)], KELP, KELPD, 5, 6)
                for y in (240, 300, 350): p.dot(x + (y - 200) * .09, y + b, 6, KELPD)
    # cabeça (direita), levantada
    hx, hy = 690, 210 + b
    p.shape(ell_pts(hx, hy, 105, 92, 40), FACE, FACED, 6, 14)
    p.shape(ell_pts(hx - 70, hy - 70, 22, 20, 20), FUR, FURD, 5, 4)   # orelha
    p.shape(ell_pts(hx + 70, hy + 22, 46, 34, 28), hexc('#f4ead8'), FACED, 5, 6)  # focinho
    p.dot(hx + 104, hy + 6, 15, INK)  # nariz
    for dy in (-6, 10, 26):
        p.stroke([(hx + 80, hy + 26 + dy * .3), (hx + 150, hy + 14 + dy)], 3)
    # olho
    ex, ey, er = hx + 12, hy - 22, 26 if expr == 'shock' else 22
    shut = max(sleep, 1.0 if blink else 0)
    if shut > .5:
        p.arc(ex, ey - 4, er * .8, 10, 20, 160, 6)
    else:
        p.dot(ex, ey, er, (255, 255, 255), 5)
        lk = max(-1, min(1, look))
        p.dot(ex + lk * (er - 10), ey + 2, 11 if expr != 'shock' else 8, INK)
        p.dot(ex + lk * (er - 10) - 3, ey - 2, 3.5, (255, 255, 255))
        if expr == 'smug':
            p.poly([(ex - er - 2, ey - er - 2), (ex + er + 2, ey - er - 2), (ex + er + 2, ey - 4), (ex - er - 2, ey - 4)], FACE)
            p.stroke([(ex - er, ey - 4), (ex + er, ey - 4)], 5)
    # boca
    if expr == 'shock': p.shape(ell_pts(hx + 70, hy + 60, 12, 14, 16), hexc('#7a2a2a'), None, 4, 0)
    else: p.arc(hx + 66, hy + 50, 18, 10, 20, 160, 4)
    # patinhas no peito
    p.shape(ell_pts(560, 225 + b, 34, 22, 20, .5), FURD, mul(FURD, .8), 5, 4)
    p.shape(ell_pts(600, 240 + b, 32, 20, 20, .3), FURD, mul(FURD, .8), 5, 4)
    # água por cima da parte de baixo
    for y0, col in ((330, (47, 143, 207, 235)),):
        d = ImageDraw.Draw(p.img)
    return p.img


def put_lontra(c, x, water_y, w, flip=False, **kw):
    """x = centro, water_y = linha d'água no palco, w = largura."""
    if w < 12: return
    h = w * 520 / 900
    put_sprite(c, 'lontra', x, water_y + h * (190 / 520) - h * .025, h, 900 / 520, flip, {'sleep': 2, 'kelp': 5, 'bob': 6}, **kw)


def agua_frente(c, y, f, cor=(47, 143, 207), alpha=255, top=None):
    """faixa de água na frente (cobre a parte de baixo do bicho), com ondinha."""
    W_ = c.size[0]
    pts = [(x, y + 10 * math.sin(x / 70 + f * .12)) for x in range(-20, W_ + 40, 20)]
    poly = pts + [(W_ + 20, top or c.size[1]), (-20, top or c.size[1])]
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.polygon(poly, fill=cor + (alpha,))
    d.line(pts, fill=INK + (255,), width=6)
    for x in range(40, W_, 180):
        yy = y + 70 + (x * 37) % 120
        d.arc((x, yy, x + 90, yy + 24), 200, 340, fill=(143, 208, 245, 255), width=5)
    c.alpha_composite(lay)


@lru_cache(maxsize=3)
def mar_aberto(luz='day'):
    hz = 1000
    base = cenarios._ceu(luz, hz); p = Pen(1242, 2208)
    cenarios._nuvens(p, 3, 160, 420, 7, (255, 255, 255) if luz == 'day' else mul(hexc(cenarios.CEUS[luz][1]), 1.05))
    p.poly([(0, hz), (1242, hz), (1242, 2208), (0, 2208)], hexc('#2f8fcf'))
    p.poly([(0, hz), (1242, hz), (1242, hz + 30), (0, hz + 30)], hexc('#5fb0e0'))
    for y in range(hz + 70, 2200, 110):
        for x in range((y // 110) % 2 * 130, 1242, 260): p.arc(x + 60, y, 50, 14, 200, 340, 5, hexc('#8fd0f5'))
    p.stroke([(0, hz), (1242, hz)], 6)
    return cenarios._done(base, p)


@lru_cache(maxsize=2)
def mar_corte(luz='dusk'):
    """céu em cima, superfície em y=760, água em corte até o fundo de areia (~1950), com algas compridas."""
    hz = 760
    base = cenarios._ceu(luz, hz)
    agua = cenarios._grad('#3fa0d8', '#0d3a66', 2208 - hz)
    base.paste(agua, (0, hz))
    p = Pen(1242, 2208)
    for i in range(5):
        x = 80 + i * 260
        p.poly([(x, hz), (x + 80, hz), (x + 220, 1950), (x + 70, 1950)], hexc('#4aa6d9'))
    pts = [(-20, 1960)] + [(x, 1940 + 30 * math.sin(x / 140)) for x in range(0, 1302, 60)] + [(1262, 2208), (-20, 2208)]
    p.shape(pts, hexc('#e6cf94'), hexc('#c4ab6e'), 6, 16)
    for x, top in ((120, 1000), (260, 1150), (1000, 1050), (1150, 900)):
        p.line([(x + 30 * math.sin(y / 70), y) for y in range(top, 1960, 30)], hexc('#5a8a2e'), 24, 5)
    p.stroke([(0, hz), (1242, hz)], 6)
    return cenarios._done(base, p)


def alga_corda(c, x_top, y_top, x_bot, y_bot, t, f):
    """alga comprida do fundo (x_bot,y_bot) até a lontra (x_top,y_top); t = quanto já cresceu (0..1)."""
    if t <= 0: return
    n = 30
    pts = []
    for i in range(n + 1):
        u = i / n
        if u > t: break
        y = lerp(y_bot, y_top, u)
        x = lerp(x_bot, x_top, u) + 40 * math.sin(u * 7 + f * .08) * (1 - u) * u * 4
        pts.append((x, y))
    if len(pts) < 2: return
    d = ImageDraw.Draw(c)
    d.line(pts, fill=INK + (255,), width=40, joint='curve')
    d.line(pts, fill=KELP + (255,), width=28, joint='curve')
    for i, (x, y) in enumerate(pts[2::3]):
        s = 1 if i % 2 else -1
        d.ellipse((x + s * 14 - 16, y - 10, x + s * 14 + 16, y + 10), fill=KELPD + (255,), outline=INK + (255,), width=4)
    # raiz no fundo
    d.ellipse((x_bot - 40, y_bot - 16, x_bot + 40, y_bot + 16), fill=KELPD + (255,), outline=INK + (255,), width=5)
