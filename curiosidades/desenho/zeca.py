"""Zeca Porquê — personagem fixo/narrador do Curiosidades da IA (proposta de 14/11/2026).
Traços de memória: topete em forma de PONTO DE INTERROGAÇÃO, óculos redondos turquesa enormes,
moletom amarelo-mostarda com "?" branco no peito, tênis vermelhos. Cabeça grande (estilo chibi).
Card 600x1000, pés em y≈975 (igual às outras pessoas do motor).
expr: neutral, grin, shock, smug, think, pained ; arms: hang, point, up, wave, chin, shrug
"""
import math
from art import Pen, hexc, mul, ell_pts, curve, INK

SKIN = hexc('#f5c9a0'); SKIN_D = mul(SKIN, .86)
HAIR = hexc('#4a2c1a'); HAIR_D = mul(HAIR, .7)
HOOD = hexc('#ffb627'); HOOD_D = hexc('#d98e0f')
PANTS = hexc('#2f3e66'); PANTS_D = mul(PANTS, .75)
SHOE = hexc('#e23b3b'); GLASS = hexc('#1fa6a0')
MOUTH = hexc('#7a2e2e')


def zeca(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, glow=0.0):
    p = Pen(600, 1000)
    # pernas e tênis
    for s in (-1, 1):
        p.line([(300 + s * 42, 760), (300 + s * 46, 900)], PANTS, 30, 4)
        p.shape(ell_pts(300 + s * 50 + 14 * s, 930, 48, 26), SHOE, mul(SHOE, .75), 5, 6)
    # corpo: moletom
    tc = (300 + tilt * 3, 640)
    p.shape(ell_pts(tc[0], tc[1], 130, 150, 56, math.radians(tilt), 0.10), HOOD, HOOD_D, 5, 18)
    p.shape([(190, 735), (410, 735), (405, 785), (195, 785)], HOOD_D, None, 5, 0)  # barra
    # "?" no peito
    qx, qy = tc[0], tc[1] - 10
    p.stroke(curve((qx - 34, qy - 40), (qx - 30, qy - 88), (qx + 8, qy - 86), 10) +
             curve((qx + 8, qy - 86), (qx + 52, qy - 80), (qx + 20, qy - 30), 10) +
             [(qx + 2, qy - 14), (qx + 2, qy + 14)], 18, (255, 255, 255))
    p.dot(qx + 2, qy + 46, 11, (255, 255, 255))
    # gola de capuz
    p.shape(ell_pts(300, 505, 92, 34, 40), HOOD_D, None, 5, 0)
    # braços
    shL, shR = (190, 560), (410, 560)
    A = {'hang': [((165, 650), (175, 740)), ((435, 650), (425, 740))],
         'point': [((165, 650), (175, 740)), ((490, 520), (575, 470))],
         'up': [((130, 450), (120, 320)), ((470, 450), (480, 320))],
         'wave': [((165, 650), (175, 740)), ((500, 470), (520, 340))],
         'chin': [((165, 650), (175, 740)), ((420, 520), (360, 455))],
         'shrug': [((120, 620), (95, 520)), ((480, 620), (505, 520))]}[arms]
    for s_, (el, hd) in zip((shL, shR), A):
        p.line(curve(s_, el, hd, 10), HOOD, 30, 4)
        p.dot(hd[0], hd[1], 22, SKIN, 4)
    # pescoço + cabeça grande
    hc = (300 + tilt * 6, 310)
    p.line([(300, 440), (300, 490)], SKIN, 44, 4)
    p.dot(hc[0] - 150, hc[1] + 20, 26, SKIN, 4); p.dot(hc[0] + 150, hc[1] + 20, 26, SKIN, 4)  # orelhas
    p.shape(ell_pts(hc[0], hc[1], 150, 140, 64, math.radians(tilt * 1.5), 0.06, 2.4), SKIN, SKIN_D, 5, 18)
    # cabelo (franja) + topete em interrogação
    top = [pt for pt in ell_pts(hc[0], hc[1] + 4, 158, 150, 64, 0, 0, 2.4) if pt[1] <= hc[1] - 6]
    top = sorted(top, key=lambda q: q[0])
    fr = top[::-1] + [(hc[0] - 156, hc[1] - 6), (hc[0] - 120, hc[1] - 52), (hc[0] - 92, hc[1] - 30), (hc[0] - 60, hc[1] - 78),
                      (hc[0] - 20, hc[1] - 56), (hc[0] + 20, hc[1] - 86), (hc[0] + 60, hc[1] - 60), (hc[0] + 100, hc[1] - 84),
                      (hc[0] + 126, hc[1] - 46), (hc[0] + 156, hc[1] - 6)]
    fr = [q for q in fr]
    fr = sorted(top, key=lambda q: -q[0]) + fr[len(top):]
    p.shape(fr, HAIR, HAIR_D, 5, 8)
    gx, gy = hc[0] + 10, hc[1] - 140
    curl = (curve((gx - 10, gy + 10), (gx - 18, gy - 40), (gx - 50, gy - 70), 10) +
            curve((gx - 50, gy - 70), (gx - 48, gy - 128), (gx + 8, gy - 128), 10) +
            curve((gx + 8, gy - 128), (gx + 62, gy - 122), (gx + 40, gy - 78), 10))
    if glow > 0:
        p.line(curl, mul(hexc('#ffe46b'), 1.0), 46, 0)
    p.line(curl, HAIR, 26, 5)
    p.dot(gx + 34, gy - 36, 15, HAIR, 5)  # o pingo do "?" (fica no ar, separado)
    # bochechas
    for s in (-1, 1): p.dot(hc[0] + s * 92, hc[1] + 50, 18, hexc('#f4a08a'))
    # olhos grandes atrás dos óculos
    ex, ey = 56, hc[1] + 6
    lx = look * 9
    br = {'neutral': 0, 'grin': -6, 'shock': -22, 'smug': 10, 'think': 14, 'pained': -16}.get(expr, 0)
    for s in (-1, 1):
        x = hc[0] + s * ex
        by = ey - 68 - (10 if expr == 'shock' else 0)
        a = math.radians(br) * s
        p.stroke([(x - 22, by + math.sin(a) * -18 * s + (8 if expr == 'think' and s > 0 else 0)),
                  (x + 22, by + math.sin(a) * 18 * s)], 8)
        if blink > .6 or expr == 'grin':
            if expr == 'grin' and blink <= .6: p.arc(x, ey + 8, 20, 16, 200, 340, 8)
            else: p.stroke([(x - 20, ey), (x + 20, ey)], 7)
        elif expr == 'pained':
            p.stroke([(x - 18 * s, ey - 12), (x + 14 * s, ey), (x - 18 * s, ey + 12)], 7)
        else:
            rr = 30 if expr == 'shock' else 26
            p.dot(x, ey, rr, (255, 255, 255), 3)
            pr = 9 if expr == 'shock' else 13
            py = ey + (-8 if expr == 'think' else 0)
            p.dot(x + lx, py, pr, INK); p.dot(x + lx - 4, py - 5, 4, (255, 255, 255))
            if expr == 'smug': p.poly([(x - 30, ey - 30), (x + 30, ey - 30), (x + 30, ey - 4), (x - 30, ey - 4)], SKIN)
    # óculos
    for s in (-1, 1):
        x = hc[0] + s * ex
        p.arc(x, ey, 46, 44, 0, 360, 11, GLASS)
    p.arc(hc[0], ey - 6, 12, 8, 200, 340, 9, GLASS)
    # nariz e boca
    p.arc(hc[0], ey + 44, 10, 7, 20, 160, 5)
    my = hc[1] + 86
    if expr == 'grin':
        p.poly([(hc[0] - 44, my - 6), (hc[0] + 44, my - 6), (hc[0] + 26, my + 28), (hc[0] - 26, my + 28)], MOUTH, 5)
        p.poly([(hc[0] - 38, my - 3), (hc[0] + 38, my - 3), (hc[0] + 33, my + 7), (hc[0] - 33, my + 7)], (255, 255, 255))
    elif expr == 'shock':
        p.dot(hc[0], my + 12, 22, MOUTH, 5)
    elif expr == 'smug':
        p.arc(hc[0] + 12, my - 4, 30, 14, 20, 160, 7)
    elif expr == 'think':
        p.stroke([(hc[0] - 20, my + 6), (hc[0] + 4, my + 2), (hc[0] + 24, my + 8)], 7)
    elif expr == 'pained':
        p.stroke([(hc[0] - 30 + i * 10, my + 6 + (5 if i % 2 else -5)) for i in range(7)], 6)
    else:
        p.arc(hc[0], my - 2, 24, 12, 20, 160, 7)
    return p.img
