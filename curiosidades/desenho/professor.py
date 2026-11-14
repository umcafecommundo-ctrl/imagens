"""PROFESSOR BIGODE — personagem fixo do Curiosidades da IA (escolhido pelo Luis em 14/11/2026).
Aparece em TODOS os posts (veja LEIA.md, seção "Personagem fixo"). Senhor careca com tufos brancos dos lados,
bigodão branco de guidão, gravata-borboleta vermelha, camisa branca, colete marrom com botões dourados.
Card 600x1000, pés em y≈975. Use pelo kit: put_prof(c, x, pés, altura, f, seed=1, flip=False, expr=..., arms=..., look=...)
expr: neutral, grin, shock, smug, pained, stern, proud, nervous ; arms: hang, point, up, wave, chin, shrug
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
def professor(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0):
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


