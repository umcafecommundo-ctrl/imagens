"""Cenários NOVOS do anima.futebol (pedido do Luis em 20/11/2026: variar o cenário, não só o estádio).

Use em historia.py:  from kit import *; import kit; from futebol import *; from futebol2 import *; from futebol3 import *
Todos têm 1242x2208 (o palco), sem escudos, logos ou marcas.
- telao('dusk'|'day')  -> estádio com um TELÃO gigante; escreva nele com telao_txt(c, linhas, f, f0)
                          ou ponha a tabela dentro (tabela(c, ..., 640, 820, f, f0)). Área útil do telão: x 150-1092, y 640-1260.
- vestiario(cores)     -> vestiário com armários e camisas penduradas nas cores do time; chão em y≈1560.
- prancheta()          -> prancheta tática em tela cheia (campo verde visto de cima, giz). Use pino(c, x, y, cores, f, f0, rotulo)
                          e seta(c, (x0,y0), (x1,y1), f, f0) para explicar lances e esquemas. Campo: x 120-1122, y 560-1900.
- coletiva(cores)      -> sala de entrevista coletiva: painel liso nas cores do time (SEM logo), mesa com microfones;
                          ponha o técnico/jogador com put_atleta(c, 640, 2000, 980, f, seed, ...) ANTES de mesa_coletiva(c) (mesa em y=1760).
- conta_bg()           -> fundo de "estúdio" escuro para contas/números grandes (série CONTA DO TÍTULO / QUEM CAI?).
"""
import math, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from kit import *
import kit
from futebol import *
from futebol2 import *

W3, H3 = 1242, 2208
_FB = kit.FONT.path


def _f(s): return ImageFont.truetype(_FB, s)


def _grad3(top, bot, h, w=W3):
    y = np.linspace(0, 1, h)[:, None, None]
    a = np.array(hexc(top)) * (1 - y) + np.array(hexc(bot)) * y
    return Image.fromarray(np.broadcast_to(a, (h, w, 3)).astype(np.uint8)).convert('RGBA')


# ------------------------------------------------------------------ telão
@lru_cache(maxsize=4)
def telao(luz='dusk'):
    """estádio com um telão gigante no lugar da arquibancada (para placar, conta, tabela)."""
    out = estadio2(luz).copy(); d = ImageDraw.Draw(out)
    x0, y0, x1, y1 = 110, 600, 1132, 1300
    # estrutura
    d.rectangle([x0 + 200, y1, x0 + 240, 1345], fill=(60, 64, 80, 255)); d.rectangle([x1 - 240, y1, x1 - 200, 1345], fill=(60, 64, 80, 255))
    d.rounded_rectangle([x0 - 18, y0 - 18, x1 + 18, y1 + 18], 26, fill=(22, 24, 34, 255), outline=INK + (255,), width=10)
    scr = _grad3('#0c1a3a', '#05080f', y1 - y0, x1 - x0)
    # textura de LED
    sd = ImageDraw.Draw(scr)
    for yy in range(0, y1 - y0, 8): sd.line([(0, yy), (x1 - x0, yy)], fill=(255, 255, 255, 10), width=1)
    out.alpha_composite(scr, (x0, y0))
    # brilho
    glow = Image.new('RGBA', (W3, H3), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle([x0 - 40, y0 - 40, x1 + 40, y1 + 40], 40, outline=(120, 170, 255, 70), width=30)
    out.alpha_composite(glow.filter(ImageFilter.GaussianBlur(18)))
    return out


def telao_txt(c, linhas, f, f0, y=760, gap=None, cor=(255, 255, 255)):
    """escreve linhas GRANDES no telão (uma após a outra, 6 quadros de intervalo). linhas = [(texto, tamanho)]."""
    yy = y
    for i, (t, s) in enumerate(linhas):
        k = back(ramp(f, f0 + i * 6, f0 + i * 6 + 8))
        if k > .03:
            im = Image.new('RGBA', (1000, int(s * 1.35)), (0, 0, 0, 0)); d = ImageDraw.Draw(im); fo = _f(s)
            tw = d.textlength(t, font=fo)
            while tw > 940 and fo.size > 40: fo = _f(fo.size - 4); tw = d.textlength(t, font=fo)
            d.text(((1000 - tw) / 2, 0), t, font=fo, fill=cor + (255,), stroke_width=4, stroke_fill=(0, 0, 0, 255))
            paste_c(c, im, 621, yy + s * .6, k)
        yy += (gap or int(s * 1.45))


# ------------------------------------------------------------------ vestiário
@lru_cache(maxsize=16)
def vestiario(cores=('#c8102e', '#111111', '#ffffff'), faixa=None):
    fy = 1560; p = Pen(W3, H3); base = Image.new('RGBA', (W3, H3), (0, 0, 0, 255))
    p.poly([(0, 0), (W3, 0), (W3, fy), (0, fy)], hexc('#d8dde6'))
    for x in range(0, W3, 120): p.stroke([(x, 0), (x, 420)], 3, hexc('#c4cad6'))
    p.poly([(0, 0), (W3, 0), (W3, 140), (0, 140)], hexc(cores[0]))
    # armários
    for i, x in enumerate(range(30, W3 - 100, 236)):
        p.shape([(x, 420), (x + 220, 420), (x + 220, fy - 20), (x, fy - 20)], hexc('#4a5568'), hexc('#3b4455'), 6, 8)
        for k in range(3): p.stroke([(x + 70 + k * 40, 470), (x + 150 + k * 0, 470)], 5, hexc('#2d3443'))
        # camisa pendurada
        c1, c2 = hexc(cores[0]), hexc(cores[1])
        cx, cy = x + 110, 760
        p.stroke([(cx, 560), (cx, 610)], 6, hexc('#8a8f9e'))
        shirt = [(cx - 95, 640), (cx - 40, 610), (cx + 40, 610), (cx + 95, 640), (cx + 120, 730), (cx + 80, 745), (cx + 78, 940),
                 (cx - 78, 940), (cx - 80, 745), (cx - 120, 730)]
        p.shape(shirt, c1, mul(c1, .8), 6, 10)
        if faixa == 'h':
            for yy in (700, 820): p.poly([(cx - 78, yy), (cx + 78, yy), (cx + 78, yy + 40), (cx - 78, yy + 40)], c2)
        elif faixa == 'v':
            for xx in (cx - 50, cx + 10): p.poly([(xx, 640), (xx + 34, 640), (xx + 34, 938), (xx, 938)], c2)
        d = ImageDraw.Draw(p.img); fo = _f(110 * 2); n = str([10, 9, 7, 11, 8][i % 5]); tw = d.textlength(n, font=fo)
        d.text((cx * 2 - tw / 2, 760 * 2 - 40), n, font=fo, fill=(255, 255, 255, 255), stroke_width=10, stroke_fill=INK + (255,))
        p.stroke([(x, fy - 20), (x + 220, fy - 20)], 5)
    # banco
    p.shape([(0, 1380), (W3, 1380), (W3, 1440), (0, 1440)], hexc('#b07a46'), hexc('#8d5f33'), 6, 6)
    # piso
    for yy in range(fy, H3, 110):
        k = (yy - fy) // 110
        for xx in range(0, W3, 160):
            p.poly([(xx, yy), (xx + 160, yy), (xx + 160, yy + 110), (xx, yy + 110)], hexc('#9aa3b2') if (xx // 160 + k) % 2 else hexc('#8a93a3'))
    p.stroke([(0, fy), (W3, fy)], 8)
    base.alpha_composite(p.img.resize((W3, H3), Image.LANCZOS))
    return base


# ------------------------------------------------------------------ prancheta tática
@lru_cache(maxsize=2)
def prancheta():
    base = _grad3('#1a2b22', '#0f1a14', H3).copy(); p = Pen(W3, H3)
    p.shape([(60, 480), (W3 - 60, 480), (W3 - 60, 1980), (60, 1980)], hexc('#2e8a4c'), hexc('#24713c'), 10, 10)
    for i in range(8):
        y0 = 560 + i * 167.5
        if i % 2: p.poly([(120, y0), (W3 - 120, y0), (W3 - 120, y0 + 167.5), (120, y0 + 167.5)], hexc('#33964f'))
    giz = (240, 245, 240)
    p.stroke([(120, 560), (W3 - 120, 560), (W3 - 120, 1900), (120, 1900), (120, 560)], 6, giz)
    p.stroke([(120, 1230), (W3 - 120, 1230)], 5, giz)
    p.line(ell_pts(621, 1230, 150, 150, 60) + [ell_pts(621, 1230, 150, 150, 60)[0]], giz, 5, 0)
    for yb, s in ((560, 1), (1900, -1)):
        p.stroke([(361, yb), (361, yb + s * 260), (881, yb + s * 260), (881, yb)], 5, giz)
        p.stroke([(501, yb), (501, yb + s * 100), (741, yb + s * 100), (741, yb)], 5, giz)
    # clipe da prancheta
    p.shape([(470, 420), (772, 420), (742, 520), (500, 520)], hexc('#b8bec9'), hexc('#8d94a1'), 8, 6)
    base.alpha_composite(p.img.resize((W3, H3), Image.LANCZOS))
    return base


@lru_cache(maxsize=64)
def _pino(cor, rot, s=70):
    im = Image.new('RGBA', (s * 2 + 20, s * 2 + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([10, 16, 10 + s * 2, 16 + s * 2], fill=(0, 0, 0, 90))
    d.ellipse([8, 8, 8 + s * 2, 8 + s * 2], fill=hexc(cor) + (255,), outline=INK + (255,), width=8)
    if rot:
        fo = _f(int(s * .9)); tw = d.textlength(rot, font=fo)
        d.text((8 + s - tw / 2, 8 + s - s * .55), rot, font=fo, fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=INK + (255,))
    return im


def pino(c, x, y, cores, f, f0, rotulo='', s=70):
    """ímã de jogador na prancheta (cor da camisa + número/letra)."""
    if f < f0: return
    paste_c(c, _pino(cores[0], rotulo, s), x, y, back(ramp(f, f0, f0 + 8)))


def seta(c, a, b, f, f0, dur=12, cor=(255, 216, 74), w=14):
    """seta de giz que se desenha de a até b."""
    if f < f0: return
    t = easeOut(ramp(f, f0, f0 + dur)); d = ImageDraw.Draw(c)
    x = lerp(a[0], b[0], t); y = lerp(a[1], b[1], t)
    d.line([a, (x, y)], fill=cor + (255,), width=w)
    if t > .6:
        ang = math.atan2(b[1] - a[1], b[0] - a[0]); L = 46
        pts = [(x, y), (x - L * math.cos(ang - .5), y - L * math.sin(ang - .5)), (x - L * math.cos(ang + .5), y - L * math.sin(ang + .5))]
        d.polygon(pts, fill=cor + (255,))


# ------------------------------------------------------------------ entrevista coletiva
@lru_cache(maxsize=16)
def coletiva(cores=('#1d4fa8', '#ffffff', '#ffffff')):
    p = Pen(W3, H3); base = Image.new('RGBA', (W3, H3), (0, 0, 0, 255))
    c1, c2 = hexc(cores[0]), hexc(cores[1] if cores[1] != cores[0] else '#ffffff')
    p.poly([(0, 0), (W3, 0), (W3, 1700), (0, 1700)], mul(c1, .55))
    # painel liso quadriculado (sem logo)
    for j, y in enumerate(range(200, 1500, 180)):
        for i, x in enumerate(range(-60, W3, 220)):
            col = mul(c1, .9) if (i + j) % 2 else mul(c1, .75)
            p.poly([(x, y), (x + 210, y), (x + 210, y + 170), (x, y + 170)], col)
    p.poly([(0, 1500), (W3, 1500), (W3, 1700), (0, 1700)], mul(c1, .45))
    p.poly([(0, 1700), (W3, 1700), (W3, H3), (0, H3)], hexc('#2a2d3a'))
    base.alpha_composite(p.img.resize((W3, H3), Image.LANCZOS))
    return base


@lru_cache(maxsize=2)
def _mesa():
    p = Pen(W3, 900)
    p.shape([(40, 260), (W3 - 40, 260), (W3 - 40, 800), (40, 800)], hexc('#1c1f2b'), hexc('#121420'), 8, 10)
    p.shape([(20, 220), (W3 - 20, 220), (W3 - 20, 290), (20, 290)], hexc('#3a3f52'), hexc('#2c3040'), 8, 6)
    for x in (470, 620, 770):
        p.line([(x, 230), (x + (621 - x) * .3, 70)], hexc('#2a2a2a'), 14, 4)
        p.shape(ell_pts(x + (621 - x) * .3, 50, 34, 46, 30), hexc('#3b3b3b'), hexc('#222222'), 6, 6)
    return p.img


def mesa_coletiva(c, y=1760):
    """mesa com microfones na frente de quem fala (desenhe a pessoa antes)."""
    im = _mesa(); c.alpha_composite(im.resize((W3, 900), Image.LANCZOS), (0, int(y - 260)))


# ------------------------------------------------------------------ estúdio para contas
@lru_cache(maxsize=2)
def conta_bg():
    base = _grad3('#0b1430', '#1b2c5c', H3).copy()
    st = Image.new('RGBA', (W3, H3), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
    for i in range(-H3, W3, 110): sd.line([(i, 0), (i + H3, H3)], fill=(255, 255, 255, 14), width=30)
    base.alpha_composite(st); d = ImageDraw.Draw(base)
    glow = Image.new('RGBA', (W3, H3), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.ellipse([120, 600, 1120, 1500], fill=(80, 140, 255, 60))
    base.alpha_composite(glow.filter(ImageFilter.GaussianBlur(80)))
    d.rectangle([0, 1720, W3, H3], fill=(10, 14, 30, 255)); d.line([(0, 1720), (W3, 1720)], fill=(255, 216, 74, 255), width=8)
    return base


def numero_gigante(c, s, x, y, f, f0, size=260, rot=-3):
    """número/placar ENORME (para a conta); entra com pulo."""
    num(c, s, x, y, f, f0, size, rot)
