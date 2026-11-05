"""Visual novo dos reels (prévia de 05/11/2026): fundo azul-noite de alto contraste,
destaques amarelo e vermelho, cortes com "zoom-soco" e flash a cada cena, legenda com a
palavra falada em caixa amarela. Mesmo JSON e mesmo uso de reel_voz.py:

    python3 reel_novo.py noticias.json saida.mp4
"""
import math, os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carrossel as c
import reel_voz as rv

W, H, FPS = rv.W, rv.H, rv.FPS
NAVY_TOP, NAVY_BOT = (8, 12, 26), (22, 34, 68)
WHITE, YEL, RED = (255, 255, 255), (255, 206, 0), (230, 40, 52)
MUTED, BOX, INK = (160, 175, 205), (26, 38, 72), (12, 12, 16)
COR_ROTULO = {"O MUNDO EXPLICADO": RED, "NO SEU BOLSO": (22, 163, 74),
              "CURIOSIDADE": (124, 58, 237), "ESPORTE": (2, 132, 199),
              "RESUMO DA SEMANA": RED}


def black(size):
    return c.font_sans(size, "Black")


def centro(d, y, txt, f, fill, stroke=0, sfill=INK):
    d.text(((W - d.textlength(txt, font=f)) / 2, y), txt, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=sfill)


def wrap_fit(d, text, max_w, max_lines, start, minimum, weight="Black"):
    size = start
    while True:
        f = c.font_sans(size, weight)
        lines = c.wrap(d, text, f, max_w)
        if len(lines) <= max_lines or size <= minimum:
            return f, lines, size
        size -= 4


_BASE = None
_GLOBO = None


def _base():
    global _BASE, _GLOBO
    if _BASE is None:
        g = Image.new("RGB", (1, H))
        for y in range(H):
            k = y / H
            g.putpixel((0, y), tuple(int(NAVY_TOP[i] + (NAVY_BOT[i] - NAVY_TOP[i]) * k) for i in range(3)))
        _BASE = g.resize((W, H))
        gl = c.globo(1500).convert("RGBA")
        # globo em tons de azul, bem translúcido
        r, gg, b, a = gl.split()
        lum = Image.merge("RGB", (r, gg, b)).convert("L")
        azul = Image.merge("RGB", (lum.point(lambda v: v * 0.35), lum.point(lambda v: v * 0.6), lum.point(lambda v: min(255, v * 1.1))))
        azul.putalpha(a.point(lambda v: int(v * 0.16)))
        _GLOBO = azul
    return _BASE, _GLOBO


def fundo(t, total, rotulo, fonte, cena_final=False):
    base, globo = _base()
    img = base.copy()
    x = int(330 - 60 * math.sin(t * 0.35))
    y = int(1050 + 40 * math.cos(t * 0.3))
    img.paste(globo, (x, y), globo)
    d = ImageDraw.Draw(img, "RGBA")
    # linhas diagonais finas que andam (movimento constante, sensação de "plantão")
    off = (t * 60) % 120
    for k in range(-20, 30):
        x0 = k * 120 + off
        d.line((x0, 0, x0 - 700, H), fill=(255, 255, 255, 9), width=2)
    # barra de progresso amarela
    d.rounded_rectangle((70, 120, W - 70, 134), 7, fill=(255, 255, 255, 40))
    d.rounded_rectangle((70, 120, 70 + (W - 140) * min(1, t / total), 134), 7, fill=YEL)
    if not cena_final:
        f = c.font_sans(36, "ExtraBold")
        tw = d.textlength(rotulo, font=f)
        cor = COR_ROTULO.get(rotulo, RED)
        x0 = (W - tw) / 2 - 40
        d.rounded_rectangle((x0 - 20, 180, (W + tw) / 2 + 30, 248), 12, fill=cor)
        # bolinha que pisca
        a = int(140 + 115 * (0.5 + 0.5 * math.sin(t * 6)))
        d.ellipse((x0 - 2, 202, x0 + 22, 226), fill=(255, 255, 255, a))
        d.text((x0 + 40, 192), rotulo, font=f, fill=WHITE)
        if fonte:
            centro(d, H - 250, f"Fonte: {fonte}", c.font_sans(30, "Medium"), MUTED)
    return img, ImageDraw.Draw(img)


def legenda(d, palavras, ts):
    if not palavras:
        return
    k = 0
    for i, (a, b, w) in enumerate(palavras):
        if ts >= a:
            k = i
    blocos, cur = [], []
    for i, w in enumerate(palavras):
        cur.append(i)
        if len(cur) == 3 or w[2].endswith((".", "?", "!", ":")):
            blocos.append(cur)
            cur = []
    if cur:
        blocos.append(cur)
    idx = next(bl for bl in blocos if k in bl)
    bloco = [palavras[i] for i in idx]
    size = 88
    f = black(size)
    ws = [d.textlength(w[2], font=f) for w in bloco]
    sp = d.textlength(" ", font=f) + 26
    tot = sum(ws) + sp * (len(ws) - 1)
    if tot > W - 160:
        size = int(size * (W - 160) / tot)
        f = black(size)
        ws = [d.textlength(w[2], font=f) for w in bloco]
        sp = d.textlength(" ", font=f) + 26
        tot = sum(ws) + sp * (len(ws) - 1)
    x, y = (W - tot) / 2, 1420
    for j, w in enumerate(bloco):
        if idx[0] + j == k:
            d.rounded_rectangle((x - 14, y - 6, x + ws[j] + 14, y + size * 1.18), 14, fill=YEL)
            d.text((x, y), w[2], font=f, fill=INK)
        else:
            d.text((x, y), w[2], font=f, fill=WHITE, stroke_width=8, stroke_fill=INK)
        x += ws[j] + sp


def cena_manchete(img, d, cena, p, t, R):
    f, lines, size = wrap_fit(d, R["manchete"].upper(), W - 150, 4, 118, 70)
    lh = size * 1.18
    y = 360 + (800 - len(lines) * lh) / 2
    for j, ln in enumerate(lines):
        ultima = j == len(lines) - 1
        tw = d.textlength(ln, font=f)
        if ultima:  # marca-texto amarelo na última linha
            d.rectangle(((W - tw) / 2 - 22, y - 4, (W + tw) / 2 + 22, y + size * 1.12), fill=YEL)
            centro(d, y, ln, f, INK)
        else:
            centro(d, y, ln, f, WHITE, 4)
        y += lh + (10 if j == len(lines) - 2 else 0)


def cena_numero(img, d, cena, p, t, R):
    v = str(cena.get("valor", ""))
    alvo = int(v.replace(".", "")) if v.replace(".", "").isdigit() else None
    txt = f"{int(alvo * rv.ease(p / 0.45)):,}".replace(",", ".") if alvo and alvo > 1 else v
    f, _, size = wrap_fit(d, txt, W - 160, 1, 320, 120)
    esc = 0.8 + 0.2 * rv.ease(p / 0.2)
    f = black(int(size * esc))
    centro(d, 440 + (320 - size * esc) / 2, txt, f, YEL, 6)
    d.rectangle((W / 2 - 90, 800, W / 2 + 90, 812), fill=RED)
    f2, lines, s2 = wrap_fit(d, cena.get("rotulo", "").upper(), W - 200, 2, 70, 48, "ExtraBold")
    y = 850
    for ln in lines:
        centro(d, y, ln, f2, WHITE)
        y += s2 * 1.2
    if cena.get("sub"):
        f3, lines, s3 = wrap_fit(d, cena["sub"], W - 200, 2, 50, 36, "Medium")
        for ln in lines:
            centro(d, y + 14, ln, f3, MUTED)
            y += s3 * 1.25


def cena_lista(img, d, cena, p, t, R):
    if cena.get("titulo"):
        centro(d, 330, cena["titulo"].upper(), c.font_sans(46, "Black"), YEL)
    itens = cena.get("itens", [])[:6]
    passo = 150 if len(itens) <= 5 else 128
    y0 = 430 + (5 - len(itens)) * passo / 2
    for i, it in enumerate(itens):
        a = rv.ease((p - i * 0.11) / 0.16)
        if a <= 0:
            continue
        y = y0 + i * passo
        x = 110 + (1 - a) * 140
        f_it, _, _ = wrap_fit(d, it, 680, 1, 58, 38, "ExtraBold")
        d.rounded_rectangle((x, y, x + 860, y + 118), 18, fill=BOX)
        d.rectangle((x, y, x + 110, y + 118), fill=YEL)
        centro_x = x + 55 - d.textlength(str(i + 1), font=black(64)) / 2
        d.text((centro_x, y + 20), str(i + 1), font=black(64), fill=INK)
        d.text((x + 140, y + 28), it, font=f_it, fill=WHITE)


def cena_frase(img, d, cena, p, t, R):
    texto, dest = cena.get("texto", "").upper(), cena.get("destaque", "").upper().split()
    f, lines, size = wrap_fit(d, texto, W - 170, 5, 108, 64)
    lh = size * 1.24
    y = 380 + (800 - len(lines) * lh) / 2
    a = rv.ease(p / 0.15)
    for ln in lines:
        x = (W - d.textlength(ln, font=f)) / 2
        for w in ln.split(" "):
            ww = d.textlength(w, font=f)
            yy = y + (1 - a) * 50
            if w.strip(".,!?;:") in dest:
                d.rectangle((x - 10, yy - 2, x + ww + 10, yy + size * 1.14), fill=YEL)
                d.text((x, yy), w, font=f, fill=INK)
            else:
                d.text((x, yy), w, font=f, fill=WHITE, stroke_width=4, stroke_fill=INK)
            x += ww + d.textlength(" ", font=f)
        y += lh


def cena_importa(img, d, cena, p, t, R):
    f, lines, size = wrap_fit(d, cena.get("texto", ""), W - 300, 6, 70, 46, "ExtraBold")
    h = 140 + len(lines) * size * 1.28 + 50
    y0 = 360 + (800 - h) / 2 + (1 - rv.ease(p / 0.15)) * 70
    d.rounded_rectangle((100, y0, W - 100, y0 + h), 24, fill=BOX)
    d.rectangle((100, y0, 118, y0 + h), fill=RED)
    d.text((160, y0 + 50), "POR QUE IMPORTA", font=c.font_sans(40, "Black"), fill=YEL)
    y = y0 + 140
    for ln in lines:
        d.text((160, y), ln, font=f, fill=WHITE)
        y += size * 1.28


def cena_final(img, d, cena, p, t, R):
    c.logo(img, d, W // 2, 640, 2.0)
    d = ImageDraw.Draw(img)
    centro(d, 820, "UM CAFÉ", black(100), WHITE)
    centro(d, 935, "COM O MUNDO", black(100), YEL)
    f2 = black(58)
    txt = "SIGA O PERFIL"
    tw = d.textlength(txt, font=f2)
    esc = 1 + 0.04 * math.sin(t * 6)
    d.rounded_rectangle((W / 2 - tw / 2 - 60 * esc, 1110, W / 2 + tw / 2 + 60 * esc, 1222), 18, fill=RED)
    centro(d, 1132, txt, f2, WHITE)


def efeito(img, k, n):
    """Zoom-soco + flash no começo de cada cena e leve aproximação contínua."""
    p0 = k / max(1, int(0.28 * FPS))
    z = 1 + 0.07 * (1 - rv.ease(p0)) + 0.025 * (k / max(1, n))
    if z > 1.001:
        cw, ch = int(W / z), int(H / z)
        x0, y0 = (W - cw) // 2, (H - ch) // 2
        img = img.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR)
    if k < 4:
        img = Image.blend(img, Image.new("RGB", (W, H), WHITE), 0.35 * (1 - k / 4))
    return img


# liga o visual novo no gerador original
rv.fundo, rv.legenda = fundo, legenda
rv.DESENHO.update({"manchete": cena_manchete, "numero": cena_numero, "lista": cena_lista,
                   "frase": cena_frase, "importa": cena_importa, "final": cena_final})
rv.centro = centro
rv.EFEITO = efeito

if __name__ == "__main__":
    rv.main(sys.argv[1], sys.argv[2])
