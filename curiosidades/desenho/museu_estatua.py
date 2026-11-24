"""Museu com a estátua de pedra da menina de mão aberta (história "A estátua de mão aberta", 24/11/2026).
museu_bg(luz): 'dia' | 'tarde' | 'noite' | 'frio' (museu do cenarios.py tingido pela luz; à noite, luz vermelha do alarme).
put_estatua(c, x, pes, h, f, obj): menina de pedra sobre o pedestal com o braço direito estendido e a mão aberta;
  obj = None | 'pena' | 'bolinha' | 'chave' | 'chaveiro' | 'flor' (objeto na palma). mao_estatua(x, pes, h) = posição da palma.
objeto_img(nome, s): objeto solto (para mostrar grande na mão do narrador).
"""
from kit import *
import kit
from sombrio import *
import cenarios

PEDRA = dict(pele='#b9b6ae', cabelo='#9c9890', penteado='longo', roupa='#a9a59c', calca='#97938a')
TINTA = {'dia': None, 'tarde': ((255, 190, 120), 50), 'noite': ((14, 18, 40), 170), 'frio': ((150, 180, 210), 70)}


@lru_cache(maxsize=8)
def museu_bg(luz='dia'):
    base = cenarios.museu('day').convert('RGBA').copy()
    t = TINTA[luz]
    if t:
        base.alpha_composite(Image.new('RGBA', base.size, t[0] + (t[1],)))
    return base


def mao_estatua(x, pes, h):
    return x + .44 * h, pes - .45 * h


@lru_cache(maxsize=16)
def objeto_img(nome, s=200):
    p = Pen(400, 400)
    if nome == 'pena':
        p.shape([(120, 330), (150, 200), (230, 90), (300, 60), (280, 150), (200, 260)], hexc('#f4f1ea'), hexc('#cfc9b8'), 6, 8)
        p.stroke([(110, 350), (290, 70)], 6)
    elif nome == 'bolinha':
        p.shape(ell_pts(200, 220, 110, 110, 48), hexc('#5aa9e6'), hexc('#2f78b8'), 6, 12)
        p.stroke([(140, 190), (200, 240), (260, 200)], 12, hexc('#f2c14e'))
        p.dot(165, 170, 22, hexc('#e8f6ff'))
    elif nome in ('chave', 'chaveiro'):
        ouro = hexc('#e0b84a')
        p.shape(ell_pts(130, 200, 80, 80, 40), ouro, hexc('#b08a2a'), 6, 10)
        p.dot(130, 200, 32, hexc('#f4efe2') if nome == 'chave' else hexc('#fff0d8'))
        p.shape([(200, 185), (360, 185), (360, 215), (200, 215)], ouro, hexc('#b08a2a'), 6, 4)
        p.shape([(300, 215), (325, 215), (325, 260), (300, 260)], ouro, None, 5, 0)
        p.shape([(335, 215), (358, 215), (358, 250), (335, 250)], ouro, None, 5, 0)
        if nome == 'chaveiro':   # plaquinha com o nome
            p.stroke([(95, 150), (60, 90)], 7)
            p.shape([(20, 20), (150, 20), (150, 100), (20, 100)], hexc('#f2c14e'), hexc('#c99a2a'), 6, 6)
            p.dot(85, 60, 14, hexc('#e8655a'))
    elif nome == 'flor':
        cor = hexc('#b9b6ae')
        for a in range(5):
            ang = a * 2 * math.pi / 5
            p.shape(ell_pts(200 + 70 * math.cos(ang), 200 + 70 * math.sin(ang), 60, 60, 32), cor, mul(cor, .85), 6, 8)
        p.shape(ell_pts(200, 200, 45, 45, 32), hexc('#d6d2c8'), None, 6, 0)
    return p.img.resize((s, s), Image.LANCZOS)


@lru_cache(maxsize=64)
def estatua_img(h, obj=None, so=0, olho=False):
    """menina de pedra (largura 1.0*h, pés em y = .975h), braço direito estendido com a palma para cima; so = escala do objeto (0..4)."""
    w = int(h * 1.0); hh = int(h)
    im = Image.new('RGBA', (w, hh + 4), (0, 0, 0, 0))
    m = kit.sprite('menino', tuple(sorted(dict(PEDRA, expr='neutro', look=0.0, blink=0 if olho else 1, phase=0.0, walk=0.0).items())), hh, .6, False)
    im.alpha_composite(m, (int(w * .3 - m.width / 2), 0))
    p = Pen(400, 400); sc = 400 / h
    cx = w * .3
    sx, sy = cx + .13 * h, .975 * h - .5 * h
    mx, my = cx + .42 * h, .975 * h - .45 * h
    P_ = lambda pts: [(a * sc, b * sc) for a, b in pts]
    p.shape(P_([(sx - .03 * h, sy - .02 * h), (mx - .02 * h, my - .035 * h), (mx, my + .015 * h), (sx + .0 * h, sy + .06 * h)]),
            hexc('#a9a59c'), hexc('#8f8b82'), 3, 0)
    p.shape(P_(ell_pts(mx + .02 * h, my, .07 * h, .03 * h, 32)), hexc('#b9b6ae'), hexc('#a09c94'), 3, 0)
    im.alpha_composite(p.img.resize((w, int(400 / sc)), Image.LANCZOS).crop((0, 0, w, hh + 4)))
    if obj and so:
        o = objeto_img(obj, max(8, int(.22 * h * so / 4)))
        im.alpha_composite(o, (int(mx + .02 * h - o.width / 2), max(0, int(my - .01 * h - o.height * .62))))
    return im


def put_estatua(c, x, pes, h, f, obj=None, s_obj=1.0, olho=False):
    """x = centro do corpo; pedra: não pisca nem respira."""
    if h < 8: return
    so = int(round(max(0, min(1, s_obj)) * 4)) if obj else 0
    im = estatua_img(int(h // 4 * 4), obj if so else None, so, olho)
    c.alpha_composite(im, (int(x - im.width * .3), int(pes - .975 * h)))
