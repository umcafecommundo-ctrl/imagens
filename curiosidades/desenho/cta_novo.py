"""PROPOSTAS de cartão final novo do Anima Futebol (para o Luis escolher, 15/11/2026).
Cada função tem a mesma assinatura do CTA_CARD atual: f(im, cl, h) -> im (1080x1920, cl = quadro local do fim).
Zona segura: conteúdo entre y≈300 e y≈1480 (topo = cabeçalho do Instagram/TikTok; baixo = legenda da voz);
lado direito abaixo de y≈1100 fica livre (botões de curtir/comentar do app).
"""
import math
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import kit
from kit import *
from futebol import bola, put_bola, raio_bola
from futebol2 import put_atleta, confete

FB = kit.FONT.path
VERDE = (22, 92, 52); VERDE2 = (31, 157, 85); AMARELO = (255, 216, 74); VERMELHO = (214, 60, 60)
AZUL = (24, 34, 64)


def F(s): return ImageFont.truetype(FB, s)


def ease(t): return 1 - (1 - t) ** 3


# ------------------------------------------------------------------ fundo
def fundo(im, cl, tint=VERDE):
    """desfoca, escurece e tinge a última cena (degradê + vinheta)."""
    k = clamp(cl / 8)
    if k > 0: im = im.filter(ImageFilter.GaussianBlur(14 * k))
    a = np.asarray(im.convert('RGB')).astype(np.float32)
    H, W = a.shape[:2]
    y = np.linspace(0, 1, H)[:, None, None]
    x = np.linspace(-1, 1, W)[None, :, None]
    vin = 1 - .55 * np.clip((x ** 2) * .6 + ((y - .45) * 1.6) ** 2, 0, 1)
    tintc = np.array(tint, np.float32)[None, None, :]
    dark = a * (1 - .72 * k) * (vin * k + (1 - k))
    dark = dark + tintc * .35 * k * (1 - y)          # tinta verde vindo do topo
    return Image.fromarray(np.clip(dark, 0, 255).astype(np.uint8)).convert('RGBA')


def raios(im, cl, cx, cy, cor=AMARELO, alpha=40, n=14):
    """raios de luz girando devagar atrás do destaque."""
    L = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    R = 1400; a0 = cl * .012
    for i in range(n):
        a = a0 + i * 2 * math.pi / n
        d.polygon([(cx, cy), (cx + R * math.cos(a - .09), cy + R * math.sin(a - .09)),
                   (cx + R * math.cos(a + .09), cy + R * math.sin(a + .09))], fill=cor + (alpha,))
    L = L.filter(ImageFilter.GaussianBlur(6))
    im.alpha_composite(L)


def sombra(im, box, r, off=14, a=120):
    L = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(L).rounded_rectangle([box[0] + off * .3, box[1] + off, box[2] + off * .3, box[3] + off], r, fill=(0, 0, 0, a))
    im.alpha_composite(L.filter(ImageFilter.GaussianBlur(10)))


def colar(im, el, cx, cy, s=1.0, rot=0):
    if s <= .02: return
    if rot: el = el.rotate(rot, expand=True, resample=Image.BICUBIC)
    if s != 1: el = el.resize((max(1, int(el.size[0] * s)), max(1, int(el.size[1] * s))), Image.LANCZOS)
    im.alpha_composite(el, (int(cx - el.size[0] / 2), int(cy - el.size[1] / 2)))


def texto_contorno(s, size, fill=(255, 255, 255), stroke=INK, sw=None, maxw=None):
    fo = F(size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    while maxw and d0.textlength(s, font=fo) > maxw and size > 30: size -= 4; fo = F(size)
    sw = sw or max(4, size // 11)
    w = int(d0.textlength(s, font=fo)) + sw * 2 + 10; hh = int(size * 1.25) + sw * 2
    im = Image.new('RGBA', (w, hh), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.text((sw + 5 + 6, sw + 8), s, font=fo, fill=(0, 0, 0, 110), stroke_width=sw, stroke_fill=(0, 0, 0, 110))
    d.text((sw + 5, sw), s, font=fo, fill=fill + (255,), stroke_width=sw, stroke_fill=stroke + (255,))
    return im


# ------------------------------------------------------------------ peças
@lru_cache(maxsize=1)
def avatar(d=150):
    """mascote da página num círculo verde (camisa verde e amarela, como a foto de perfil)."""
    c = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    put_atleta(c, 300, 1500, 1500, 0, 3, sombra=False, cores=('#ffd84a', '#1f7a4a', '#ffffff'), faixa='v',
               arms='hang', expr='grin', skin=1, hs='curto', hair='#2a1a10')
    bg = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    ImageDraw.Draw(bg).ellipse([0, 0, 599, 599], fill=(60, 170, 90, 255))
    bg.alpha_composite(c)
    m = Image.new('L', (600, 600), 0); ImageDraw.Draw(m).ellipse([0, 0, 599, 599], fill=255)
    out = Image.new('RGBA', (600, 600), (0, 0, 0, 0)); out.paste(bg, (0, 0), m)
    ImageDraw.Draw(out).ellipse([4, 4, 595, 595], outline=(255, 255, 255, 255), width=22)
    return out.resize((d, d), Image.LANCZOS)


def card_seguir(im, cl, t0, cx=520, cy=1310, w=900):
    """cartão branco 'Anima Futebol' com botão SEGUIR que é 'tocado' e vira SEGUINDO."""
    s = back(ramp(cl, t0, t0 + 9))
    if s <= .03: return
    hh = 190
    L = Image.new('RGBA', (w + 40, hh + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([20, 20, w + 20, hh + 20], 48, fill=(255, 255, 255, 250), outline=INK + (255,), width=6)
    L.alpha_composite(avatar(140), (44, 45))
    d.text((200, 56), 'Anima Futebol', font=F(48), fill=INK + (255,))
    d.text((202, 120), 'futebol em 1 minuto', font=F(32), fill=(110, 115, 130, 255))
    tap = t0 + 26
    bw, bh = 236, 96; bx, by = w + 20 - bw - 26, 20 + (hh - bh) // 2
    if cl < tap + 3:
        pz = 1 + .06 * math.sin(cl * .45) if cl > t0 + 10 else 1
        d.rounded_rectangle([bx - 6 * (pz - 1) * 20, by, bx + bw, by + bh], 30, fill=AMARELO + (255,), outline=INK + (255,), width=5)
        t = 'SEGUIR'; tw = d.textlength(t, font=F(46)); d.text((bx + (bw - tw) / 2, by + 20), t, font=F(46), fill=INK + (255,))
    else:
        d.rounded_rectangle([bx, by, bx + bw, by + bh], 30, fill=VERDE2 + (255,), outline=INK + (255,), width=5)
        t = 'SEGUINDO'; tw = d.textlength(t, font=F(32)); d.text((bx + 62 + (bw - 70 - tw) / 2, by + 30), t, font=F(32), fill=(255, 255, 255, 255))
        d.line([(bx + 20, by + 50), (bx + 32, by + 64), (bx + 54, by + 34)], fill=(255, 255, 255, 255), width=8)
    sombra(im, (cx - w / 2, cy - hh / 2, cx + w / 2, cy + hh / 2), 48)
    colar(im, L, cx, cy, s)
    # dedinho tocando (círculo + onda)
    if t0 + 14 <= cl < tap + 16:
        px, py = cx - w / 2 - 20 + bx + bw * .6, cy - hh / 2 - 20 + by + bh * .7
        mv = ease(ramp(cl, t0 + 14, tap)); fx, fy = lerp(px + 160, px, mv), lerp(py + 200, py, mv)
        D = ImageDraw.Draw(im)
        if cl >= tap:
            r = 20 + (cl - tap) * 7; a = int(255 * (1 - (cl - tap) / 16))
            D.ellipse([px - r, py - r, px + r, py + r], outline=(255, 255, 255, a), width=6)
        D.ellipse([fx - 30, fy - 30, fx + 30, fy + 30], fill=(255, 255, 255, 210), outline=INK + (255,), width=5)


def seta_baixo(im, cl, t0, x, y, cor=AMARELO):
    s = back(ramp(cl, t0, t0 + 8))
    if s <= .03: return
    b = 14 * abs(math.sin(cl * .22))
    L = Image.new('RGBA', (120, 130), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.polygon([(30, 6), (90, 6), (90, 60), (114, 60), (60, 124), (6, 60), (30, 60)], fill=cor + (255,), outline=INK + (255,))
    d.line([(30, 6), (90, 6), (90, 60), (114, 60), (60, 124), (6, 60), (30, 60), (30, 6)], fill=INK + (255,), width=6)
    colar(im, L, x, y + b, s)


def botao_voto(lbl, cor, icone, w=380, hh=190):
    L = Image.new('RGBA', (w + 20, hh + 30), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([6, 20, w + 6, hh + 20], 46, fill=tuple(int(v * .6) for v in cor) + (255,))
    d.rounded_rectangle([6, 6, w + 6, hh + 6], 46, fill=cor + (255,), outline=INK + (255,), width=7)
    d.rounded_rectangle([24, 18, w - 12, 60], 20, fill=(255, 255, 255, 60))
    cx0, cy0 = 90, hh / 2 + 6
    d.ellipse([cx0 - 50, cy0 - 50, cx0 + 50, cy0 + 50], fill=(255, 255, 255, 255), outline=INK + (255,), width=5)
    if icone == 'ok': d.line([(cx0 - 26, cy0), (cx0 - 6, cy0 + 22), (cx0 + 28, cy0 - 20)], fill=cor + (255,), width=14)
    else:
        d.line([(cx0 - 22, cy0 - 22), (cx0 + 22, cy0 + 22)], fill=cor + (255,), width=14)
        d.line([(cx0 - 22, cy0 + 22), (cx0 + 22, cy0 - 22)], fill=cor + (255,), width=14)
    fo = F(84); tw = d.textlength(lbl, font=fo)
    d.text((165 + (w - 165 - tw) / 2, hh / 2 - 44), lbl, font=fo, fill=(255, 255, 255, 255), stroke_width=6, stroke_fill=INK + (255,))
    return L


def pergunta(h): return getattr(h, 'CTA_TEXTO', 'COMENTA AQUI!')


# ================================================================== A) ENQUETE
def cta_enquete(im, cl, h):
    im = fundo(im, cl)
    raios(im, cl, 540, 640, alpha=int(34 * clamp(cl / 10)))
    # etiqueta
    colar(im, _pill('ENQUETE DO DIA', VERMELHO, (255, 255, 255), 46), 540, 360, back(ramp(cl, 2, 10)), -3)
    # pergunta (entra grande e respira)
    sq = back(ramp(cl, 4, 13)) * (1 + .025 * math.sin(cl * .18))
    colar(im, texto_contorno(pergunta(h), 128, AMARELO, maxw=940), 540, 560, sq)
    # botões
    for i, (lbl, cor, ic, x) in enumerate((('SIM', VERDE2, 'ok', 300), ('NÃO', VERMELHO, 'x', 780))):
        t0 = 12 + i * 5
        s = back(ramp(cl, t0, t0 + 9))
        p = 1 + .05 * max(0, math.sin((cl - 30) * .25 + i * math.pi)) if cl > 30 else 1
        colar(im, botao_voto(lbl, cor, ic), x, 820, s * p)
    # chamada para comentar
    s = back(ramp(cl, 22, 30))
    colar(im, texto_contorno('VOTA NOS COMENTÁRIOS', 64, (255, 255, 255)), 540, 1010, s)
    seta_baixo(im, cl, 28, 540, 1110)
    card_seguir(im, cl, 34)
    return im.convert('RGB')


@lru_cache(maxsize=16)
def _pill(t, bg, fg, size):
    fo = F(size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); tw = d0.textlength(t, font=fo)
    w, hh = int(tw + 80), int(size * 1.7)
    L = Image.new('RGBA', (w + 10, hh + 10), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([4, 4, w + 4, hh + 4], hh // 2, fill=bg + (255,), outline=INK + (255,), width=6)
    d.text((44, (hh - size * 1.15) / 2 + 2), t, font=fo, fill=fg + (255,))
    return L


# ================================================================== B) TELÃO DO ESTÁDIO
def _led(w, hh, cl):
    L = Image.new('RGBA', (w, hh), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle([0, 0, w - 1, hh - 1], 40, fill=(30, 30, 38, 255), outline=INK + (255,), width=8)
    d.rounded_rectangle([18, 18, w - 19, hh - 19], 28, fill=(10, 14, 26, 255), outline=(255, 216, 74, 255), width=6)
    for yy in range(34, hh - 30, 14):
        for xx in range(34, w - 30, 14):
            d.point((xx, yy), fill=(40, 50, 80, 255))
    return L


def cta_telao(im, cl, h):
    im = fundo(im, cl, tint=(20, 30, 70))
    # refletores acendendo
    D = ImageDraw.Draw(im)
    for x in (130, 950):
        a = int(150 * clamp(cl / 6))
        G = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(G).ellipse([x - 160, 200, x + 160, 420], fill=(255, 250, 220, a))
        im.alpha_composite(G.filter(ImageFilter.GaussianBlur(40)))
    s = back(ramp(cl, 2, 12))
    W, Hh = 980, 660
    tel = _led(W, Hh, cl); d = ImageDraw.Draw(tel)
    # cabeçalho piscando
    hd = 'PERGUNTA DO DIA'
    if cl % 16 < 12 or cl > 40:
        tw = d.textlength(hd, font=F(48)); d.text(((W - tw) / 2, 52), hd, font=F(48), fill=(255, 160, 60, 255))
    q = texto_contorno(pergunta(h), 118, AMARELO, maxw=W - 90)
    tel.alpha_composite(q, ((W - q.size[0]) // 2, 140))
    # placar SIM x NÃO
    y0 = 360
    for lbl, cor, xx in (('SIM', VERDE2, 150), ('NÃO', VERMELHO, W - 150 - 260)):
        d.rounded_rectangle([xx, y0, xx + 260, y0 + 120], 24, fill=cor + (255,), outline=INK + (255,), width=6)
        tw = d.textlength(lbl, font=F(76)); d.text((xx + (260 - tw) / 2, y0 + 16), lbl, font=F(76), fill=(255, 255, 255, 255))
    xq = 'x'; tw = d.textlength(xq, font=F(80)); d.text(((W - tw) / 2, y0 + 10), xq, font=F(80), fill=(255, 255, 255, 255))
    for xx in (150, W - 150 - 260):
        dig = '?' if (cl // 4) % 2 else '0'
        d.rounded_rectangle([xx + 70, y0 + 140, xx + 190, y0 + 270], 18, fill=(0, 0, 0, 255), outline=(255, 216, 74, 255), width=4)
        tw = d.textlength(dig, font=F(96)); d.text((xx + 130 - tw / 2, y0 + 150), dig, font=F(96), fill=(255, 216, 74, 255))
    # suportes
    sup = Image.new('RGBA', (W, Hh + 80), (0, 0, 0, 0)); sd = ImageDraw.Draw(sup)
    for xx in (200, W - 200): sd.rectangle([xx - 18, Hh - 20, xx + 18, Hh + 80], fill=(60, 64, 80, 255), outline=INK + (255,), width=5)
    sup.alpha_composite(tel, (0, 0))
    sombra(im, (540 - W / 2, 300, 540 + W / 2, 280 + Hh), 40)
    colar(im, sup, 540, 280 + (Hh + 80) / 2, s)
    sc = back(ramp(cl, 20, 28))
    colar(im, texto_contorno('RESPONDE NOS COMENTÁRIOS', 56, (255, 255, 255), maxw=940), 540, 1080, sc)
    seta_baixo(im, cl, 26, 540, 1150)
    card_seguir(im, cl, 32)
    return im.convert('RGB')


# ================================================================== C) MASCOTE COM BALÃO
def cta_mascote(im, cl, h):
    im = fundo(im, cl)
    raios(im, cl, 260, 1000, alpha=int(30 * clamp(cl / 10)))
    if cl >= 10: confete(im, 540, 500, cl, 10, 60, 900)
    # mascote entra correndo pela esquerda e acena
    x = lerp(-250, 220, ease(ramp(cl, 0, 12)))
    arms = 'up' if (cl // 10) % 2 and cl > 14 else 'point'
    put_atleta(im, x, 1130, 600, cl, 3, cores=('#ffd84a', '#1f7a4a', '#ffffff'), faixa='v', arms=arms, expr='grin',
               skin=1, hs='curto', hair='#2a1a10', num_='10', run=(cl * .09) % 1 if cl < 12 else None)
    rb = raio_bola(600); put_bola(im, x + 140, 1130 - rb, rb, cl)
    # balão de fala
    s = back(ramp(cl, 8, 17))
    if s > .03:
        bw, bh = 700, 470
        L = Image.new('RGBA', (bw + 40, bh + 140), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        d.polygon([(120, bh - 20), (40, bh + 120), (260, bh - 20)], fill=(255, 255, 255, 255), outline=INK + (255,))
        d.rounded_rectangle([10, 10, bw + 10, bh + 10], 70, fill=(255, 255, 255, 255), outline=INK + (255,), width=9)
        d.line([(126, bh + 4), (40, bh + 120), (254, bh + 4)], fill=INK + (255,), width=9)
        d.polygon([(130, bh - 4), (60, bh + 96), (240, bh - 4)], fill=(255, 255, 255, 255))
        tw = d.textlength('E AÍ, TORCEDOR?', font=F(46)); d.text(((bw + 20 - tw) / 2, 50), 'E AÍ, TORCEDOR?', font=F(46), fill=(120, 125, 140, 255))
        q = texto_contorno(pergunta(h), 108, AMARELO, maxw=bw - 60)
        L.alpha_composite(q, ((bw + 20 - q.size[0]) // 2, 120))
        p = _pill('COMENTA AÍ!', VERDE2, (255, 255, 255), 54)
        L.alpha_composite(p, ((bw + 20 - p.size[0]) // 2, 300))
        sombra(im, (680 - bw / 2, 290, 680 + bw / 2, 290 + bh), 70)
        colar(im, L, 680, 290 + (bh + 140) / 2, s, 2 * math.sin(cl * .08))
    card_seguir(im, cl, 30)
    return im.convert('RGB')


OPCOES = {'A_enquete': cta_enquete, 'B_telao': cta_telao, 'C_mascote': cta_mascote}
