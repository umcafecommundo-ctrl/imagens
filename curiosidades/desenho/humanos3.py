"""Propostas de personagem fixo humano (3ª rodada, 14/11/2026): PROFESSOR BIGODE, TINA e BETO.
Cards 600x1000, pés em y≈975 (padrão do motor). expr: neutral, grin, shock, smug, pained, stern ;
arms: hang, point, up, wave, chin, shrug
"""
import math
from art import Pen, hexc, mul, ell_pts, curve, INK, face

SK = [hexc('#ffe2c2'), hexc('#f5c9a0'), hexc('#d9a77c'), hexc('#a8714a')]
ARMS = {'hang': [((185, 560), (190, 650)), ((415, 560), (410, 650))],
        'point': [((185, 560), (190, 650)), ((470, 430), (560, 380))],
        'up': [((150, 380), (140, 240)), ((450, 380), (460, 240))],
        'wave': [((185, 560), (190, 650)), ((480, 400), (500, 280))],
        'chin': [((185, 560), (190, 650)), ((420, 470), (340, 380))],
        'shrug': [((140, 540), (120, 440)), ((460, 540), (480, 440))]}


def _legs(p, pants, shoe, boots=False):
    for s in (-1, 1):
        p.line([(300 + s * 40, 690), (300 + s * 44, 820), (300 + s * 44, 945)], pants, 26, 4)
        if boots:
            p.shape([(300 + s * 44 - 26, 880), (300 + s * 44 + 26, 880), (300 + s * 44 + 30 + 14 * s, 975), (300 + s * 44 - 30, 975)], shoe, mul(shoe, .75), 5, 6)
        else:
            p.shape(ell_pts(300 + s * 44 + 12 * s, 958, 40, 20), shoe, mul(shoe, .75), 5, 4)


def _arms(p, arms, sleeve, skin, w=18):
    for s_, (el, hd) in zip(((205, 470), (395, 470)), ARMS[arms]):
        p.line(curve(s_, el, hd, 10), sleeve, w, 4)
        p.dot(hd[0], hd[1], 18, skin, 4)


def _head(p, skin):
    hc = (300, 262)
    p.line([(300, 350), (300, 430)], skin, 40, 4)
    p.dot(hc[0] - 114, hc[1] + 10, 17, skin, 4); p.dot(hc[0] + 114, hc[1] + 10, 17, skin, 4)
    p.shape(ell_pts(hc[0], hc[1], 118, 108, 56, 0, 0.08, 2.4), skin, mul(skin, .86), 5, 16)
    return hc


# ------------------------------------------------------------ PROFESSOR BIGODE
def bigode(expr='neutral', arms='hang', blink=0, look=0.0):
    p = Pen(600, 1000)
    sk = SK[1]
    _legs(p, hexc('#6b4a2f'), hexc('#3b2a1e'))
    p.shape(ell_pts(300, 560, 122, 150, 56, 0, 0.18), hexc('#ffffff'), hexc('#d9dde3'), 5, 14)  # camisa / barriga
    vc = hexc('#7c5a3c')
    p.shape([(186, 470), (276, 440), (286, 700), (200, 690)], vc, mul(vc, .75), 4, 8)
    p.shape([(414, 470), (324, 440), (314, 700), (400, 690)], vc, mul(vc, .75), 4, 8)
    for y in (520, 580, 640): p.dot(300, y, 6, hexc('#d9b44a'), 2)
    p.shape([(204, 660), (396, 660), (400, 716), (200, 716)], hexc('#6b4a2f'), None, 5, 0)
    _arms(p, arms, hexc('#ffffff'), sk)
    hc = _head(p, sk)
    # gravata-borboleta vermelha
    p.shape([(300, 440), (250, 418), (250, 466)], hexc('#e23b3b'), None, 4, 0)
    p.shape([(300, 440), (350, 418), (350, 466)], hexc('#e23b3b'), None, 4, 0)
    p.dot(300, 441, 11, hexc('#b82a2a'), 3)
    # careca brilhante com tufos brancos dos lados
    for s in (-1, 1):
        p.shape(ell_pts(hc[0] + s * 112, hc[1] - 22, 22, 34, 24), hexc('#f2f2f2'), hexc('#cfcfcf'), 5, 4)
    p.dot(hc[0] - 40, hc[1] - 74, 16, mul(sk, 1.12))
    face(p, hc[0], hc[1] - 6, expr, blink, look)
    # sobrancelhas fartas
    for s in (-1, 1):
        p.shape(ell_pts(hc[0] + s * 31, hc[1] - 50 - (12 if expr == 'shock' else 0), 26, 10, 20, s * (-.2 if expr == 'stern' else .1)), hexc('#f2f2f2'), None, 4, 0)
    # BIGODÃO de guidão
    my = hc[1] + 24
    for s in (-1, 1):
        pts = [(hc[0], my - 6), (hc[0] + s * 46, my - 10), (hc[0] + s * 84, my + 2), (hc[0] + s * 104, my - 22),
               (hc[0] + s * 94, my - 38), (hc[0] + s * 112, my - 34), (hc[0] + s * 116, my - 8),
               (hc[0] + s * 88, my + 18), (hc[0] + s * 46, my + 12), (hc[0], my + 6)]
        p.shape(pts, hexc('#ffffff'), hexc('#d6d6d6'), 5, 6)
    return p.img


# ------------------------------------------------------------ TINA
def tina(expr='neutral', arms='hang', blink=0, look=0.0):
    p = Pen(600, 1000)
    sk = SK[3]
    _legs(p, hexc('#2f4a6b'), hexc('#5a3d24'), boots=True)
    cap = hexc('#ffc93c')
    p.shape(ell_pts(300, 560, 118, 150, 56, 0, 0.12), cap, mul(cap, .8), 5, 16)  # capa de chuva
    p.stroke([(300, 440), (300, 700)], 4)
    for y in (500, 560, 620): p.dot(318, y, 7, hexc('#2f4a6b'), 2)
    for s in (-1, 1): p.line([(300 + s * 70, 450), (300 + s * 84, 640)], hexc('#3fae6a'), 16, 4)  # alças da mochila
    _arms(p, arms, cap, sk, 22)
    hc = (300, 262)
    hair = hexc('#2a1a10')
    # cabelão cacheado (atrás)
    for i in range(16):
        a = math.pi * 2 * i / 16
        p.dot(hc[0] + 150 * math.cos(a), hc[1] - 20 + 135 * math.sin(a), 62, hair, 5)
    p.shape(ell_pts(hc[0], hc[1] - 20, 175, 160, 48), hair, None, 0, 0)
    # lápis preso no cabelo
    p.line([(hc[0] + 70, hc[1] - 170), (hc[0] + 180, hc[1] - 250)], hexc('#ffb627'), 16, 4)
    p.shape([(hc[0] + 172, hc[1] - 262), (hc[0] + 200, hc[1] - 270), (hc[0] + 188, hc[1] - 244)], hexc('#f5d6a8'), None, 3, 0)
    hc = _head(p, sk)
    for i in range(7):  # franja de cachos
        p.dot(hc[0] - 96 + i * 32, hc[1] - 92 + (6 if i % 2 else 0), 30, hair, 4)
    for s in (-1, 1): p.dot(hc[0] + s * 70, hc[1] + 44, 15, hexc('#c96a5a'))
    face(p, hc[0], hc[1] + 10, expr, blink, look)
    # brincos de argola
    for s in (-1, 1): p.arc(hc[0] + s * 116, hc[1] + 40, 14, 16, 0, 360, 5, hexc('#e8c25a'))
    return p.img


# ------------------------------------------------------------ BETO
def beto(expr='neutral', arms='hang', blink=0, look=0.0):
    p = Pen(600, 1000)
    sk = SK[2]
    _legs(p, hexc('#3d5a8a'), hexc('#ffffff'))
    tee = hexc('#7b4fd6')
    p.shape(ell_pts(300, 560, 112, 140, 56, 0, 0.1), tee, mul(tee, .78), 5, 16)
    p.shape([(300, 500), (330, 560), (304, 560), (322, 630), (276, 548), (300, 548), (284, 500)], hexc('#ffd23f'), None, 4, 0)  # raio na camiseta
    p.shape([(204, 640), (396, 640), (400, 716), (200, 716)], hexc('#3d5a8a'), None, 5, 0)
    _arms(p, arms, tee, sk)
    hc = _head(p, sk)
    # fone de ouvido no pescoço
    p.arc(300, 410, 62, 34, 0, 180, 12, hexc('#2ec4b6'))
    for s in (-1, 1): p.shape(ell_pts(300 + s * 62, 412, 20, 24, 24), hexc('#2ec4b6'), hexc('#1f8f85'), 5, 4)
    # barba curta
    p.shape([(hc[0] - 108, hc[1] + 30), (hc[0] - 70, hc[1] + 92), (hc[0], hc[1] + 110), (hc[0] + 70, hc[1] + 92),
             (hc[0] + 108, hc[1] + 30), (hc[0] + 60, hc[1] + 80), (hc[0], hc[1] + 88), (hc[0] - 60, hc[1] + 80)], hexc('#5a3d24'), None, 0, 0)
    face(p, hc[0], hc[1] + 6, expr, blink, look)
    # boné vermelho virado pra trás
    cp = hexc('#e23b3b')
    p.shape([(hc[0] - 122, hc[1] - 30), (hc[0] - 110, hc[1] - 100), (hc[0] - 40, hc[1] - 130), (hc[0] + 50, hc[1] - 130),
             (hc[0] + 115, hc[1] - 96), (hc[0] + 124, hc[1] - 30)], cp, mul(cp, .78), 5, 10)
    p.shape([(hc[0] - 124, hc[1] - 40), (hc[0] - 190, hc[1] - 30), (hc[0] - 196, hc[1] - 10), (hc[0] - 120, hc[1] - 16)], mul(cp, .82), None, 5, 0)
    p.dot(hc[0], hc[1] - 128, 10, mul(cp, .7), 3)
    return p.img
