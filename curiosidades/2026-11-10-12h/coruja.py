from kit import *


def coruja(ang=0, blink=0, look=0.0, expr='calm', glow=0):
    """coruja de frente (600x800, pés em y≈780). ang = graus que a cabeça girou (0 frente, 180 nuca, 270 = perfil esquerdo)."""
    p = Pen(600, 800)
    br, brd = hexc('#9a6a3e'), hexc('#7a5030')
    bel = hexc('#e8d2a8')
    # corpo
    p.shape(ell_pts(300, 560, 190, 220), br, brd, 6, 18)
    p.shape(ell_pts(300, 600, 120, 160), bel, mul(bel, .85), 4, 8)
    for r in range(3):
        for k in range(3):
            x, y = 250 + k * 50 + (r % 2) * 25 - 12, 540 + r * 60
            p.stroke([(x - 12, y - 8), (x, y + 6), (x + 12, y - 8)], 5, brd)
    # asas
    for s in (-1, 1):
        p.shape([(300 + s * 150, 430), (300 + s * 205, 560), (300 + s * 170, 720), (300 + s * 115, 600)], brd, mul(brd, .8), 5, 0)
    # pés
    for s in (-1, 1):
        for t in (-1, 0, 1):
            p.line([(300 + s * 60, 760), (300 + s * 60 + t * 16, 790)], hexc('#e3a33c'), 9, 4)
    # cabeça
    a = math.radians(ang)
    sx, cs = math.sin(a), math.cos(a)
    p.shape(ell_pts(300, 270, 180, 160), br, brd, 6, 16)
    # tufos
    for s in (-1, 1):
        bx = 300 + s * 110 * max(.35, abs(cs)) * (1 if cs >= 0 else -1) - sx * 30
        p.shape([(bx - 40, 150), (bx + s * 30, 70), (bx + 40, 140)], brd, None, 5, 0)
    if cs > -.25:
        fw = max(.3, cs)
        cx = 300 - sx * 95
        p.shape(ell_pts(cx, 280, 150 * fw, 120), bel, mul(bel, .88), 4, 6)
        for s in (-1, 1):
            ex = cx + s * 68 * fw
            p.shape(ell_pts(ex, 260, 62 * fw, 62), hexc('#f2a91f'), None, 5, 0)
            if blink:
                p.stroke([(ex - 50 * fw, 262), (ex + 50 * fw, 262)], 7)
            else:
                p.dot(ex + look * 10 * fw, 262, 30 * fw, INK)
                p.dot(ex + look * 10 * fw - 10 * fw, 250, 9 * fw, (255, 255, 255))
            if expr == 'smug' and not blink:
                p.poly([(ex - 64 * fw, 200), (ex + 64 * fw, 200), (ex + 64 * fw, 245), (ex - 64 * fw, 245)], br)
                p.stroke([(ex - 60 * fw, 245), (ex + 60 * fw, 245)], 6)
        p.shape([(cx - 20 * fw, 300), (cx + 20 * fw, 300), (cx, 350)], hexc('#e3a33c'), None, 4, 0)
    else:
        # nuca: penas
        for k in range(4):
            y = 220 + k * 30
            p.stroke([(220, y), (300, y + 20), (380, y)], 5, brd)
    return p.img
