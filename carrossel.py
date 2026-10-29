"""Gera carrossel 1080x1350 do @umcafecommundo a partir de um JSON.

Uso: python3 carrossel.py noticias.json pasta_saida

JSON:
{
  "edicao": "Giro da manhã",          # Giro da manhã | Giro do almoço | Giro da noite
  "data": "28 de outubro de 2026",
  "chamada": "O que aconteceu no mundo enquanto você dormia",
  "noticias": [
    {"local": "ESTADOS UNIDOS", "titulo": "...", "resumo": "...", "importa": "...", "fonte": "Reuters"}
  ]
}
"""
import json, math, os, sys, textwrap
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1350
BG = (58, 36, 24)        # marrom café
CREAM = (243, 230, 211)
TEAL = (240, 178, 72)    # cor de destaque: âmbar (nome mantido por compatibilidade com reel.py)
ON_ACCENT = BG           # texto sobre fundo âmbar
MUTED = (201, 180, 156)
PAD = 90

# Globo terrestre do logo
OCEAN = (46, 118, 168)
OCEAN_HI = (86, 160, 205)
LAND = (104, 168, 92)
CONTINENTES = [
    [(-.80, -.50), (-.62, -.72), (-.38, -.82), (-.10, -.78), (.02, -.62), (-.06, -.48), (-.20, -.40), (-.18, -.28), (-.30, -.18), (-.34, -.06), (-.46, -.10), (-.58, -.24), (-.72, -.30), (-.86, -.36)],
    [(.08, -.92), (.30, -.95), (.36, -.80), (.22, -.70), (.10, -.76)],
    [(-.34, -.06), (-.24, .02), (-.16, .08), (-.20, .12), (-.30, .04)],
    [(-.18, .10), (.04, .08), (.22, .16), (.40, .30), (.36, .46), (.20, .58), (.08, .76), (-.02, .92), (-.10, .80), (-.10, .56), (-.16, .40), (-.26, .26)],
    [(.62, -.50), (.76, -.66), (.96, -.62), (1.05, -.40), (.82, -.32), (.66, -.36)],
    [(.60, -.18), (.84, -.24), (1.05, -.10), (1.05, .50), (.88, .62), (.78, .42), (.70, .18), (.58, .04)],
]

def font_serif(size, bold=True):
    for p in ["/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"]:
        if os.path.exists(p):
            f = ImageFont.truetype(p, size)
            try:
                f.set_variation_by_name("Bold" if bold else "Regular")
            except Exception:
                pass
            return f
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", size)

def font_sans(size, weight="Regular"):
    p = f"/usr/share/fonts/opentype/inter/Inter-{weight}.otf"
    if os.path.exists(p):
        return ImageFont.truetype(p, size)
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)

def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def fit_block(draw, text, max_w, max_h, start, minimum, serif=True, weight="Regular", spacing=1.22):
    size = start
    while size >= minimum:
        f = font_serif(size) if serif else font_sans(size, weight)
        lines = wrap(draw, text, f, max_w)
        h = len(lines) * size * spacing
        if h <= max_h:
            return f, lines, size
        size -= 2
    f = font_serif(minimum) if serif else font_sans(minimum, weight)
    return f, wrap(draw, text, f, max_w), minimum

def draw_lines(draw, xy, lines, f, size, fill, spacing=1.22):
    x, y = xy
    for ln in lines:
        draw.text((x, y), ln, font=f, fill=fill)
        y += size * spacing
    return y

def globo(D):
    """Globo terrestre (oceano azul, continentes verdes) de diâmetro D, RGBA."""
    k = 4
    S = D * k
    r = S / 2
    g = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    d.ellipse([0, 0, S - 1, S - 1], fill=OCEAN)
    hi = Image.new("L", (S, S), 0)
    ImageDraw.Draw(hi).ellipse([S * .08, S * .06, S * .62, S * .58], fill=110)
    hi = hi.filter(ImageFilter.GaussianBlur(S * .12))
    g = Image.composite(Image.new("RGBA", (S, S), OCEAN_HI + (255,)), g, hi)
    d = ImageDraw.Draw(g)
    for pts in CONTINENTES:
        d.polygon([(r + x * r, r + (y - .14) * r) for x, y in pts], fill=LAND)
    lines = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    dl = ImageDraw.Draw(lines)
    a = (255, 255, 255, 55)
    w = max(2, int(S * .008))
    for f in (.35, .72):
        dl.ellipse([r - r * f, 0, r + r * f, S - 1], outline=a, width=w)
    dl.line([r, 0, r, S], fill=a, width=w)
    for yy in (-.5, 0, .5):
        hw = r * math.sqrt(1 - yy * yy)
        dl.line([r - hw, r + yy * r, r + hw, r + yy * r], fill=a, width=w)
    g = Image.alpha_composite(g, lines)
    sh = Image.new("L", (S, S), 0)
    ImageDraw.Draw(sh).ellipse([S * .30, S * .25, S * 1.35, S * 1.3], fill=90)
    sh = sh.filter(ImageFilter.GaussianBlur(S * .12))
    g = Image.composite(Image.new("RGBA", (S, S), (10, 30, 50, 255)), g, Image.eval(sh, lambda v: int(v * .6)))
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, S - 1, S - 1], fill=255)
    out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    out.paste(g, (0, 0), mask)
    ImageDraw.Draw(out).ellipse([0, 0, S - 1, S - 1], outline=CREAM + (255,), width=int(S * .025))
    return out.resize((D, D), Image.LANCZOS)

def logo(img, draw, cx, cy, s):
    """Xícara com globo terrestre, em escala s (1 = 100px de largura aprox.)."""
    D = int(80 * s)
    gy = int(cy - 16 * s)
    gl = globo(D)
    img.paste(gl, (int(cx - D / 2), int(gy - D / 2)), gl)
    top = cy + 2 * s
    draw.polygon([(cx - 44 * s, top), (cx + 44 * s, top), (cx + 36 * s, top + 44 * s), (cx - 36 * s, top + 44 * s)], fill=CREAM)
    draw.arc([cx + 30 * s, top + 6 * s, cx + 60 * s, top + 34 * s], -90, 90, fill=CREAM, width=max(2, int(7 * s)))
    draw.ellipse([cx - 58 * s, top + 40 * s, cx + 58 * s, top + 52 * s], fill=CREAM)

def base(n, total):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # rodapé
    d.line([PAD, H - 120, W - PAD, H - 120], fill=(92, 64, 48), width=2)
    d.text((PAD, H - 92), "@umcafecommundo", font=font_sans(28, "SemiBold"), fill=MUTED)
    t = f"{n}/{total}"
    d.text((W - PAD - d.textlength(t, font=font_sans(28, "Medium")), H - 92), t, font=font_sans(28, "Medium"), fill=MUTED)
    return img, d

def capa(dados, total):
    img, d = base(1, total)
    logo(img, d, W // 2, 250, 2.2)
    y = 470
    ed = dados.get("edicao", "Giro do mundo").upper()
    f = font_sans(30, "Bold")
    d.text(((W - d.textlength(ed, font=f)) / 2, y), ed, font=f, fill=TEAL)
    y += 50
    dt = dados.get("data", "")
    f = font_sans(30, "Medium")
    d.text(((W - d.textlength(dt, font=f)) / 2, y), dt, font=f, fill=MUTED)
    y += 90
    f, lines, size = fit_block(d, dados["chamada"], W - 2 * PAD, 360, 84, 54)
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=CREAM)
        y += size * 1.2
    y += 50
    n = len(dados["noticias"])
    cta = f"{n} notícias em 1 minuto  →"
    f = font_sans(34, "SemiBold")
    d.text(((W - d.textlength(cta, font=f)) / 2, y), cta, font=f, fill=CREAM)
    return img

def slide_noticia(nt, idx, total):
    img, d = base(idx, total)
    y = PAD + 10
    tag = nt.get("local", "MUNDO").upper()
    f = font_sans(28, "Bold")
    tw = d.textlength(tag, font=f)
    d.rounded_rectangle([PAD, y, PAD + tw + 44, y + 58], radius=29, fill=TEAL)
    d.text((PAD + 22, y + 12), tag, font=f, fill=ON_ACCENT)
    y += 110
    f, lines, size = fit_block(d, nt["titulo"], W - 2 * PAD, 380, 72, 48)
    y = draw_lines(d, (PAD, y), lines, f, size, CREAM, 1.18) + 40
    f, lines, size = fit_block(d, nt["resumo"], W - 2 * PAD, 330, 38, 30, serif=False)
    y = draw_lines(d, (PAD, y), lines, f, size, MUTED, 1.4) + 40
    imp = nt.get("importa")
    if imp:
        box_top = y
        fl = font_sans(26, "Bold")
        f, lines, size = fit_block(d, imp, W - 2 * PAD - 70, H - 170 - box_top - 110, 34, 26, serif=False, weight="Medium")
        box_h = 60 + len(lines) * size * 1.35 + 40
        d.rounded_rectangle([PAD, box_top, W - PAD, box_top + box_h], radius=24, fill=(78, 52, 37))
        d.text((PAD + 35, box_top + 28), "POR QUE IMPORTA", font=fl, fill=TEAL)
        draw_lines(d, (PAD + 35, box_top + 74), lines, f, size, CREAM, 1.35)
    fonte = nt.get("fonte")
    if fonte:
        d.text((PAD, H - 170), f"Fonte: {fonte}", font=font_sans(26, "Regular"), fill=MUTED)
    return img

def final(dados, total):
    img, d = base(total, total)
    logo(img, d, W // 2, 330, 2.2)
    y = 560
    for txt, f, col in [
        ("Gostou do giro?", font_serif(76), CREAM),
        ("Siga para receber as notícias do mundo", font_sans(36, "Medium"), MUTED),
        ("às 10h, 12h e 18h", font_sans(36, "Medium"), MUTED),
    ]:
        d.text(((W - d.textlength(txt, font=f)) / 2, y), txt, font=f, fill=col)
        y += 100 if txt == "Gostou do giro?" else 52
    y += 60
    f = font_sans(36, "Bold")
    t = "@umcafecommundo"
    tw = d.textlength(t, font=f)
    d.rounded_rectangle([(W - tw) / 2 - 40, y, (W + tw) / 2 + 40, y + 80], radius=40, fill=TEAL)
    d.text(((W - tw) / 2, y + 18), t, font=f, fill=ON_ACCENT)
    return img

def main(src, out):
    dados = json.load(open(src, encoding="utf-8"))
    os.makedirs(out, exist_ok=True)
    total = len(dados["noticias"]) + 2
    imgs = [capa(dados, total)]
    for i, nt in enumerate(dados["noticias"]):
        imgs.append(slide_noticia(nt, i + 2, total))
    imgs.append(final(dados, total))
    paths = []
    for i, im in enumerate(imgs, 1):
        p = os.path.join(out, f"slide_{i:02d}.jpg")
        im.save(p, "JPEG", quality=85, optimize=True)
        paths.append(p)
    print("\n".join(paths))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
