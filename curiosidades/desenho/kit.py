"""Kit de cena do formato DESENHO (Curiosidades da IA).

Use em historia.py:  from kit import *
Tudo aqui é desenhado em código (Pillow): nada de imagens baixadas.

Coordenadas: cada cena desenha num "palco" de 1242x2208 px (BG) e devolve a câmera
(cx, cy, zoom, roll_graus). zoom 1 = palco inteiro; 1.3 = mais perto. Saída final 1080x1920.
Pés dos personagens: put_*(c, x_centro, y_dos_pes, altura_px, ...).

Tempo: f = quadro local da cena (30 fps). Use wt(cena, 'palavra') para saber em que quadro
a narração fala uma palavra e faça a ação cair 0-3 quadros ANTES dela.
"""
import math, random, os, sys
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import art, personagens as P, cenarios
from art import Pen, INK, ell_pts, curve, hexc, mul, face, SKINS

FPS = 30; OW, OH = 1080, 1920; BW, BH = 1242, 2208

# ------------------------------------------------------------ timing (preenchido pelo motor)
class _T:
    falas = []; LEAD = .15
T = _T()


def _norm(w):
    import unicodedata, re
    w = unicodedata.normalize('NFD', w.lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in w if unicodedata.category(c) != 'Mn'))


def wt(si, word, nth=0):
    """quadro local (na cena si) em que a narração começa a palavra `word` (sem acento, tanto faz)."""
    hits = [w for w in T.falas[si]['words'] if _norm(w['w']) == _norm(word)]
    if not hits: raise KeyError(f"palavra '{word}' não está na fala da cena {si}: {[w['w'] for w in T.falas[si]['words']]}")
    return round((T.LEAD + hits[min(nth, len(hits) - 1)]['t']) * FPS)


# ------------------------------------------------------------ easing
clamp = lambda x, a=0, b=1: max(a, min(b, x))
lerp = lambda a, b, t: a + (b - a) * t
ramp = lambda f, a, b: clamp((f - a) / max(1e-6, (b - a)))
smooth = lambda t: (lambda t: t * t * t * (t * (t * 6 - 15) + 10))(clamp(t))
easeOut = lambda t: 1 - (1 - clamp(t)) ** 3
def back(t, s=1.7):
    t = clamp(t) - 1; return t * t * ((s + 1) * t + s) + 1
def blinkAt(f, seed):
    per = 38 + (seed * 17) % 31; ph = (f + seed * 13) % per
    return .5 if ph < 2 else 1 if ph < 4 else 0
def pulse(f, f0, dur=26):
    """0->1 rápido, segura `dur` quadros, solta (ótimo para cantar/gritar/pular)."""
    return clamp((f - f0) / 4) * (1 - clamp((f - f0 - dur) / 6))
def kick(f, f0, amp=1.0):
    """tremida de impacto de 7 quadros: some em cy (px*10) e roll."""
    d = f - f0
    return ((1 if d % 2 else -1) * (1 - d / 7) * amp) if 0 <= d < 7 else 0


# ------------------------------------------------------------ fundos
@lru_cache(maxsize=8)
def BG(name, W=BW):
    """'day' | 'golden' | 'dusk' = campo com céu; 'lab' = laboratório (janela de noite)."""
    if name == 'lab': return P.lab_bg()
    return art.background(name, W)


def CEN(nome, luz='day'):
    """cenário pronto pelo nome (veja cenarios.NOMES): quarto, sala, cozinha, banheiro, escola, escritorio, cidade, praia,
    fundo_mar, floresta, deserto, neve, montanha, espaco, estacao, corpo, antiga, museu, mapa, fabrica, lab, pasto.
    Escolha o lugar onde a história acontece; o pasto só para histórias de campo."""
    return cenarios.cenario(nome, luz)


# ------------------------------------------------------------ sprites com cache
@lru_cache(maxsize=1024)
def sprite(fn_name, key, h, aspect, flip):
    fn = getattr(P, fn_name, None) or getattr(art, fn_name, None) or getattr(sys.modules.get('historia'), fn_name)
    im = fn(**dict(key)).resize((max(1, int(h * aspect)), max(1, int(h))), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im


def put(c, im, x, feet_y):
    w, h = im.size
    c.alpha_composite(im, (int(x - w / 2), int(feet_y - h)))


def put_sprite(c, fn_name, x, feet, h, aspect, flip=False, quant=None, **kw):
    """desenha qualquer função de personagem fn(**kw)->RGBA. quant={'param': passos} arredonda para o cache."""
    if h < 8: return
    for k, n in (quant or {}).items():
        if k in kw: kw[k] = round(kw[k] * n) / n
    put(c, sprite(fn_name, tuple(sorted(kw.items())), int(h), aspect, flip), x, feet + h * .025)


def put_roo(c, x, feet, h, flip=False, **kw):
    """galo (de lado, olha p/ direita). kw: crow, sleep, expr, look, blink, chief, ear, step"""
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    put_sprite(c, 'rooster', x, feet, h, .75, flip, {'crow': 6, 'sleep': 6, 'step': 8}, **kw)


def put_emu(c, x, feet, h, flip=False, **kw):
    """emu/ave de lado. kw: phase, run, peck, expr, look, blink, seed, helmet"""
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    put_sprite(c, 'emu', x, feet, h, .75, flip, {'phase': 16, 'peck': 6, 'run': 4}, **kw)


def _bean(c, fn, x, feet, h, f, seed, cut=1.0, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    kw['tilt'] = round(1.2 * math.sin((f + seed * 7) * .05) * 2) / 2 + kw.get('tilt', 0)
    if h < 8: return
    bob = .006 * math.sin((f + seed * 11) * .11) * h
    im = sprite(fn, tuple(sorted(kw.items())), int(h), .6, False)
    if cut < 1: im = im.crop((0, 0, im.size[0], int(im.size[1] * cut)))
    put(c, im, x, feet + h * .025 + bob - h * (1 - cut))


def put_sci(c, x, feet, h, f, seed, **kw):
    """cientista de jaleco. kw: expr, arms('clip','hang','ears','cheek','point','up'), skin 0-3, hair, glasses, bun, look"""
    _bean(c, 'scientist', x, feet, h, f, seed, **kw)


def put_soldier(c, x, feet, h, f, seed, cut=1.0, **kw):
    """soldado/pessoa de capacete. kw: expr, arms('hang','salute','thumb','cheek','shrug','point'), mous, skin, sweat, walk"""
    _bean(c, 'soldier', x, feet, h, f, seed, cut, **kw)


@lru_cache(maxsize=64)
def clock_img(ha, ma, size, ring=False):
    return P.clock(ha, ma, size, ring)


@lru_cache(maxsize=128)
def txt(s, size, rot=0):
    """texto de efeito (COCORICÓ!, 100 dB...). Só letras/números/acentos — sem emoji."""
    return P.bubble_text(s, size, rot=rot)


def paste_c(c, im, x, y, s=1.0):
    """cola centrado em (x,y) com escala s (use back(ramp(...)) para 'pular' na tela)."""
    if s <= .02: return
    if s != 1: im = im.resize((max(1, int(im.size[0] * s)), max(1, int(im.size[1] * s))), Image.BILINEAR)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(y - im.size[1] / 2)))


def put_dust(c, x, y, r, age, life=14):
    if age < 0 or age >= life: return
    t = age / life
    im = art.dust(r * (0.5 + t), 1 - t * t)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(y - im.size[1] / 2 - t * r * .6)))


def rings(c, x, y, f, f0, dur=26, big=1.0, flip=False):
    """ondas de som saindo de (x,y)."""
    for k in range(3):
        a = f - f0 - k * 7
        if 0 <= a < 16 and f - f0 < dur:
            im = P.sound_rings((60 + a * 16) * big, 1 - a / 16)
            if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
            c.alpha_composite(im, (int(x - im.size[0] / 2), int(y - im.size[1] / 2)))


def zzz(c, x, y, f):
    for i in range(3):
        a = (f + i * 14) % 42
        paste_c(c, txt('Z', 70 + i * 16), x + a * 3 + i * 40, y - a * 5 - i * 60, 1 - a / 42)


def thought(c, x, y, r, s, content=None):
    """balão de pensamento centrado em (x,y), raio r, escala s; content = RGBA dentro."""
    if s <= .02: return
    p = Pen(int(2.4 * r) + 40, int(2.2 * r) + 40)
    cx, cy = p.W / 2, r * .9 + 20
    p.shape(ell_pts(cx, cy, r * 1.1, r * .85, 64), (255, 255, 255), (230, 232, 240), 6, 12)
    p.dot(cx - r * .55, cy + r * 1.0, r * .12, (255, 255, 255), 5); p.dot(cx - r * .75, cy + r * 1.22, r * .07, (255, 255, 255), 5)
    im = p.img.resize((p.W, p.H), Image.LANCZOS)
    if content is not None: im.alpha_composite(content, (int(cx - content.size[0] / 2), int(cy - content.size[1] / 2)))
    paste_c(c, im, x, y, s)


def sun_icon(size, rise):
    p = Pen(300, 300); y = 230 - rise * 110
    for i in range(8):
        a = i * math.pi / 4
        p.stroke([(150 + 70 * math.cos(a), y + 70 * math.sin(a)), (150 + 100 * math.cos(a), y + 100 * math.sin(a))], 10, hexc('#f6a524'))
    p.dot(150, y, 55, hexc('#ffd25e'), 5)
    p.poly([(0, 232), (300, 232), (300, 300), (0, 300)], (255, 255, 255)); p.stroke([(20, 232), (280, 232)], 7)
    return p.img.resize((size, size), Image.LANCZOS)


# ------------------------------------------------------------ câmera, cor, legenda
_yy, _xx = np.mgrid[0:OH, 0:OW]
_Q = ((_xx / OW - .5) ** 2 + ((_yy / OH - .5) * .75) ** 2)
GRADES = {'day': dict(gain=(1, 1, 1), lift=(0, 0, 0), sat=1.12, vig=.2),
          'golden': dict(gain=(1.06, .96, .86), lift=(0, 0, 0), sat=1.15, vig=.26),
          'dusk': dict(gain=(.82, .86, 1.04), lift=(4, 5, 11), sat=1.05, vig=.34)}
_VIG = {k: (1 - g['vig'] * _Q * 2.2)[..., None].astype(np.float32) for k, g in GRADES.items()}


def camera(c, cam):
    cx, cy, z, roll = cam
    W, H = c.size; pad = 1 + abs(roll) * .065
    vw = min(BW / z, W / pad, H / pad * 9 / 16); vh = vw * 16 / 9
    vw2, vh2 = vw * pad, vh * pad
    cx = clamp(cx, vw2 / 2, W - vw2 / 2); cy = clamp(cy, vh2 / 2, H - vh2 / 2)
    im = c.crop((int(cx - vw2 / 2), int(cy - vh2 / 2), int(cx + vw2 / 2), int(cy + vh2 / 2))).convert('RGB')
    if abs(roll) > .01:
        im = im.rotate(roll, Image.BICUBIC)
        w, h = im.size; iw, ih = w / pad, h / pad
        im = im.crop((int((w - iw) / 2), int((h - ih) / 2), int((w + iw) / 2), int((h + ih) / 2)))
    return im.resize((OW, OH), Image.BILINEAR)


def grade(im, light, flash=0.0):
    g = GRADES[light]
    a = np.asarray(im).astype(np.float32)
    l = (a @ np.array([.299, .587, .114], np.float32))[..., None]
    a = (l + (a - l) * g['sat']) * np.array(g['gain'], np.float32) + np.array(g['lift'], np.float32)
    a *= _VIG[light]
    if flash > 0: a = a * (1 - flash) + 255 * flash
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


FONT = ImageFont.truetype(os.path.join(AQUI, '..', 'fonts', 'DejaVuSans-Bold.ttf') if os.path.exists(os.path.join(AQUI, '..', 'fonts', 'DejaVuSans-Bold.ttf')) else '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 76)


def wrap(words, d, maxw=940):
    lines, cur = [], []
    for w in words:
        if d.textlength(' '.join(cur + [w]), font=FONT) > maxw and cur: lines.append(cur); cur = [w]
        else: cur.append(w)
    lines.append(cur); return lines


def draw_caption(im, ws, lf, y0=1600):
    """ws = [(palavra, quadro), ...]; palavra atual em amarelo, já ditas em branco."""
    if not ws or lf < ws[0][1] - 2: return im
    shown = sum(1 for _, t in ws if lf >= t - 1)
    d = ImageDraw.Draw(im); lines = wrap([w for w, _ in ws], d)
    y = y0 - (len(lines) - 1) * 46; idx = 0
    for ln in lines:
        x = (OW - d.textlength(' '.join(ln), font=FONT)) / 2
        for w in ln:
            if idx < shown:
                cur = idx == shown - 1; age = lf - (ws[idx][1] - 1)
                dy = -10 * (1 - clamp(age / 4)) if cur else 0
                d.text((x, y + dy), w, font=FONT, fill=(255, 216, 74) if cur else (255, 255, 255), stroke_width=8, stroke_fill=INK)
            x += d.textlength(w + ' ', font=FONT); idx += 1
        y += 92
    return im
