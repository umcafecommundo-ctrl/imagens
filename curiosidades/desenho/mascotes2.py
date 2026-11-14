"""Propostas de personagem fixo (2ª rodada, 14/11/2026): BITU (robozinho de tela) e CACÁ (capivara exploradora).
Cards no padrão do motor: Bitu 600x1000 (pés em y≈975); Cacá 800x700 de lado, olhando para a direita (pés em y≈680).
expr: neutral, grin, shock, think, smug ; arms (Bitu): hang, point, up, wave, shrug
"""
import math
from art import Pen, hexc, mul, ell_pts, curve, INK

TEAL = hexc('#2ec4b6'); TEAL_D = hexc('#1f8f85')
BODY = hexc('#f1f4f8'); BODY_D = hexc('#c9d2dd')
SCREEN = hexc('#1c2433'); GLOW = hexc('#7df9ff')
ORANGE = hexc('#ff8a3d'); YEL = hexc('#ffd23f')


def bitu(expr='neutral', arms='hang', blink=0, look=0.0, glow=0.0):
    p = Pen(600, 1000)
    # pernas curtas e pés
    for s in (-1, 1):
        p.line([(300 + s * 55, 820), (300 + s * 58, 900)], hexc('#8a96a6'), 26, 4)
        p.shape(ell_pts(300 + s * 64, 935, 58, 34, 40, 0, 0, 3), TEAL, TEAL_D, 5, 8)
    # braços (atrás do corpo)
    shL, shR = (200, 640), (400, 640)
    A = {'hang': [((170, 720), (180, 800)), ((430, 720), (420, 800))],
         'point': [((170, 720), (180, 800)), ((490, 600), (575, 550))],
         'up': [((140, 540), (140, 420)), ((460, 540), (460, 420))],
         'wave': [((170, 720), (180, 800)), ((500, 560), (520, 440))],
         'shrug': [((120, 680), (95, 590)), ((480, 680), (505, 590))]}[arms]
    for s_, (el, hd) in zip((shL, shR), A):
        p.line(curve(s_, el, hd, 10), hexc('#8a96a6'), 20, 4)
        p.shape(ell_pts(hd[0], hd[1], 30, 30, 32), TEAL, TEAL_D, 5, 6)
    # corpo arredondado
    p.shape(ell_pts(300, 720, 140, 125, 64, 0, 0, 3.2), BODY, BODY_D, 6, 20)
    p.shape(ell_pts(300, 720, 46, 46, 40), ORANGE, mul(ORANGE, .78), 5, 6)
    p.dot(286, 706, 12, (255, 220, 190))
    # pescoço
    p.line([(300, 570), (300, 600)], hexc('#8a96a6'), 40, 4)
    # antena com bolinha
    ax, ay = 300, 120
    p.line([(300, 210), (300, ay + 30)], hexc('#8a96a6'), 12, 4)
    if glow > 0:
        p.dot(ax, ay, 58, mul(YEL, 1.0))
    p.dot(ax, ay, 36, YEL, 5)
    p.stroke(curve((ax - 12, ay - 10), (ax - 6, ay - 26), (ax + 8, ay - 20), 6) + [(ax + 10, ay - 8), (ax, ay + 2), (ax, ay + 10)], 7)
    p.dot(ax, ay + 22, 4, INK)
    # cabeça = moldura turquesa + tela escura
    hc = (300, 400)
    p.shape(ell_pts(hc[0], hc[1], 210, 185, 64, 0, 0, 3.6), TEAL, TEAL_D, 6, 22)
    for s in (-1, 1):  # "orelhas" de parafuso
        p.shape(ell_pts(hc[0] + s * 214, hc[1], 26, 50, 32), BODY, BODY_D, 5, 6)
    p.shape(ell_pts(hc[0], hc[1] + 5, 168, 140, 64, 0, 0, 3.6), SCREEN, None, 5, 0)
    p.dot(hc[0] - 110, hc[1] - 80, 14, (60, 74, 96))  # reflexo
    # rosto na tela
    ex, ey = 72, hc[1] - 10
    lx = look * 14
    for s in (-1, 1):
        x = hc[0] + s * ex + lx
        if blink > .6:
            p.stroke([(x - 30, ey), (x + 30, ey)], 14, GLOW)
        elif expr == 'grin':
            p.arc(x, ey + 14, 32, 30, 200, 340, 15, GLOW)
        elif expr == 'shock':
            p.arc(x, ey, 40, 44, 0, 360, 13, GLOW)
        elif expr == 'think':
            if s < 0: p.shape(ell_pts(x, ey - 10, 24, 36, 32), GLOW, None, 0, 0)
            else: p.stroke([(x - 26, ey - 4), (x + 26, ey - 14)], 14, GLOW)
        elif expr == 'smug':
            p.shape([(x - 32, ey - 6), (x + 32, ey - 6), (x + 28, ey + 26), (x - 28, ey + 26)], GLOW, None, 0, 0)
        else:
            p.shape(ell_pts(x, ey, 26, 42, 32), GLOW, None, 0, 0)
    my = hc[1] + 72
    if expr == 'grin':
        p.arc(hc[0], my - 14, 62, 34, 15, 165, 14, GLOW)
    elif expr == 'shock':
        p.arc(hc[0], my + 6, 20, 22, 0, 360, 12, GLOW)
    elif expr == 'think':
        p.stroke([(hc[0] - 40, my + 4), (hc[0] - 14, my - 8), (hc[0] + 12, my + 4), (hc[0] + 38, my - 8)], 11, GLOW)
    elif expr == 'smug':
        p.arc(hc[0] + 18, my - 14, 40, 18, 20, 150, 12, GLOW)
    else:
        p.arc(hc[0], my - 10, 36, 18, 20, 160, 12, GLOW)
    return p.img


CAPI = hexc('#a8744a'); CAPI_D = hexc('#7f5534'); FOCINHO = hexc('#6b4429')
CHAPEU = hexc('#e9d3a1'); CHAPEU_D = hexc('#c4a86f'); LENCO = hexc('#e23b3b')


def caca(expr='neutral', blink=0, look=0.3, glow=0.0, step=0.0):
    """capivara de lado (olhando p/ a direita), chapéu de explorador e lenço vermelho. 800x700, pés y≈680."""
    p = Pen(800, 700)
    sw = 14 * math.sin(step * math.pi * 2)
    # pernas de trás (escuras) e da frente
    for x, ph in ((170, 0), (240, 1), (460, 1), (530, 0)):
        d = sw if ph else -sw
        p.line([(x, 470), (x + d, 640)], CAPI_D, 40, 5)
        p.shape(ell_pts(x + d + 8, 660, 30, 16, 24), FOCINHO, None, 4, 0)
    # corpo barril
    p.shape(ell_pts(340, 430, 250, 150, 64, 0, 0, 2.3), CAPI, CAPI_D, 6, 22)
    # cabeça "tijolinho"
    hx, hy = 540, 310
    head = [(hx - 70, hy - 70), (hx + 90, hy - 80), (hx + 160, hy - 40), (hx + 170, hy + 40),
            (hx + 140, hy + 80), (hx - 40, hy + 110), (hx - 100, hy + 40)]
    p.shape(head, CAPI, CAPI_D, 6, 16)
    p.shape(ell_pts(hx + 150, hy + 22, 34, 46, 24), FOCINHO, None, 5, 0)  # focinho
    p.dot(hx + 166, hy + 2, 8, INK)  # narina
    # boca
    if expr == 'grin': p.arc(hx + 110, hy + 60, 30, 16, 20, 160, 6)
    elif expr == 'shock': p.dot(hx + 120, hy + 72, 14, hexc('#7a2e2e'), 5)
    elif expr == 'smug': p.arc(hx + 118, hy + 58, 24, 10, 30, 150, 6)
    else: p.stroke([(hx + 96, hy + 66), (hx + 130, hy + 62)], 6)
    # lenço vermelho no pescoço
    p.shape([(hx - 110, hy + 40), (hx - 30, hy + 110), (hx - 10, hy + 150), (hx - 70, hy + 190), (hx - 130, hy + 90)], LENCO, mul(LENCO, .78), 5, 8)
    for i in range(3): p.dot(hx - 80 + i * 22, hy + 110 + i * 18, 6, (255, 255, 255))
    # orelha
    p.shape(ell_pts(hx - 30, hy - 82, 22, 28, 24), CAPI_D, None, 5, 0)
    # olho grande
    ex, ey = hx + 50, hy - 6
    if blink > .6:
        p.stroke([(ex - 24, ey), (ex + 24, ey)], 7)
    else:
        r = 34 if expr == 'shock' else 28
        p.dot(ex, ey, r, (255, 255, 255), 5)
        py = ey - (12 if expr == 'think' else 0)
        p.dot(ex + look * 12, py, 13, INK); p.dot(ex + look * 12 - 4, py - 5, 4, (255, 255, 255))
        if expr == 'smug': p.poly([(ex - 36, ey - 36), (ex + 36, ey - 36), (ex + 36, ey - 2), (ex - 36, ey - 2)], CAPI)
    p.stroke([(ex - 24, ey - 44 - (10 if expr == 'shock' else 0)), (ex + 24, ey - 48 + (8 if expr == 'think' else 0))], 7)
    # chapéu de explorador
    p.shape(ell_pts(hx + 30, hy - 90, 140, 28, 48), CHAPEU, CHAPEU_D, 5, 6)
    p.shape([(hx - 50, hy - 92), (hx - 30, hy - 180), (hx + 30, hy - 200), (hx + 90, hy - 180), (hx + 110, hy - 92)], CHAPEU, CHAPEU_D, 5, 10)
    p.poly([(hx - 46, hy - 120), (hx + 106, hy - 120), (hx + 108, hy - 100), (hx - 48, hy - 100)], hexc('#5a3d24'))
    if glow > 0:
        gx, gy = hx + 30, hy - 260
        p.dot(gx, gy, 46, YEL, 5)
        p.stroke(curve((gx - 14, gy - 12), (gx - 6, gy - 32), (gx + 12, gy - 24), 6) + [(gx + 12, gy - 8), (gx, gy + 4), (gx, gy + 14)], 9)
        p.dot(gx, gy + 28, 5, INK)
    # rabinho/patas de trás
    p.dot(90, 400, 16, CAPI_D, 5)
    return p.img
