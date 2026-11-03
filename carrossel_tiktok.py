"""Gera o carrossel do TikTok (1080x1920, 9:16) no formato "uma ideia por slide" (decisão do Luis em 03/11/2026).

Uso: python3 carrossel_tiktok.py noticias.json pasta_saida

Usa o mesmo JSON do Reel. Estrutura:
  1. capa: só o gancho ("chamada") em letra enorme + "arrasta"
  2 slides por notícia (e pelo "esporte", se houver):
     A) rótulo + título grande          B) resumo + "por que importa" + fonte
  último: pergunta para comentar (campo opcional "pergunta") + "Segue @umcafecomomundo"
=> 10 slides com esporte, 8 sem.

O perfil do TikTok é @umcafecomomundo (diferente do Instagram, @umcafecommundo).
Margens livres para a interface do TikTok: topo ~170px, base ~380px, direita ~150px.
"""
import json, os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carrossel as c

W, H = 1080, 1920
X0, X1 = 90, 930            # área útil (direita livre para os botões do TikTok)
HANDLE = "@umcafecomomundo"
ROTULOS = ["O MUNDO EXPLICADO", "NO SEU BOLSO", "CURIOSIDADE"]
BOX = (78, 52, 37)


def wrap_fit(d, text, max_w, max_h, start, minimum, serif=True, weight="Bold", sp=1.18):
    size = start
    while True:
        f = c.font_serif(size) if serif else c.font_sans(size, weight)
        lines = c.wrap(d, text, f, max_w)
        if len(lines) * size * sp <= max_h or size <= minimum:
            return f, lines, size
        size -= 4


def lines_at(d, lines, f, size, y, fill, sp=1.18, center=False):
    for ln in lines:
        x = (W - d.textlength(ln, font=f)) / 2 if center else X0
        d.text((x, y), ln, font=f, fill=fill)
        y += size * sp
    return y


def base(n, total):
    img = Image.new("RGB", (W, H), c.BG)
    d = ImageDraw.Draw(img)
    f = c.font_sans(30, "Bold")
    d.text((X0, 190), "NOTÍCIAS DO MUNDO", font=f, fill=c.TEAL)
    t = f"{n}/{total}"
    d.text((X1 - d.textlength(t, font=f), 190), t, font=f, fill=c.MUTED)
    d.line([X0, 245, X1, 245], fill=(92, 64, 48), width=2)
    fh = c.font_sans(30, "SemiBold")
    d.text((X0, 1500), HANDLE, font=fh, fill=c.MUTED)
    return img, d


def chip(d, text, y, fill=None, color=None):
    f = c.font_sans(34, "Bold")
    tw = d.textlength(text, font=f)
    d.rounded_rectangle([X0, y, X0 + tw + 50, y + 66], radius=33, fill=fill or c.TEAL)
    d.text((X0 + 25, y + 13), text, font=f, fill=color or c.ON_ACCENT)
    return y + 66


def capa(dados, total):
    img, d = base(1, total)
    c.logo(img, d, W // 2, 380, 1.6)
    f = c.font_sans(32, "Bold")
    t = f"{dados.get('edicao', '').upper()}  ·  {dados.get('data', '')}"
    d.text(((W - d.textlength(t, font=f)) / 2, 520), t, font=f, fill=c.MUTED)
    f, lines, size = wrap_fit(d, dados["chamada"], X1 - X0, 640, 128, 80)
    y = 620 + (640 - len(lines) * size * 1.15) / 2
    lines_at(d, lines, f, size, y, c.CREAM, 1.15, center=True)
    fa = c.font_sans(44, "Bold")
    t = "arrasta  →"
    tw = d.textlength(t, font=fa)
    d.rounded_rectangle([(W - tw) / 2 - 50, 1330, (W + tw) / 2 + 50, 1420], radius=45, fill=c.TEAL)
    d.text(((W - tw) / 2, 1350), t, font=fa, fill=c.ON_ACCENT)
    return img


def slide_titulo(nt, rotulo, n, total):
    img, d = base(n, total)
    y = chip(d, rotulo, 330)
    f = c.font_sans(36, "SemiBold")
    d.text((X0, y + 40), nt.get("local", "").upper(), font=f, fill=c.MUTED)
    f, lines, size = wrap_fit(d, nt["titulo"], X1 - X0, 820, 118, 76)
    y = 520 + (820 - len(lines) * size * 1.15) / 2
    lines_at(d, lines, f, size, y, c.CREAM, 1.15)
    return img


def slide_explica(nt, n, total):
    img, d = base(n, total)
    f, lines, size = wrap_fit(d, nt["resumo"], X1 - X0, 560, 54, 40, serif=False, weight="Medium")
    y = lines_at(d, lines, f, size, 320, c.CREAM, 1.38) + 50
    imp = nt.get("importa")
    if imp:
        fl = c.font_sans(30, "Bold")
        f, lines, size = wrap_fit(d, imp, X1 - X0 - 80, 1400 - y - 150, 52, 36, serif=True)
        h = 90 + len(lines) * size * 1.25 + 40
        d.rounded_rectangle([X0, y, X1, y + h], radius=28, fill=BOX)
        d.text((X0 + 40, y + 34), "POR QUE IMPORTA", font=fl, fill=c.TEAL)
        yy = y + 90
        for ln in lines:
            d.text((X0 + 40, yy), ln, font=f, fill=c.CREAM)
            yy += size * 1.25
    if nt.get("fonte"):
        d.text((X0, 1440), f"Fonte: {nt['fonte']}", font=c.font_sans(28), fill=c.MUTED)
    return img


def final(dados, total):
    img, d = base(total, total)
    f = c.font_sans(36, "Bold")
    d.text(((W - d.textlength("E VOCÊ?", font=f)) / 2, 380), "E VOCÊ?", font=f, fill=c.TEAL)
    perg = dados.get("pergunta") or "Qual dessas notícias te surpreendeu mais?"
    f, lines, size = wrap_fit(d, perg, X1 - X0, 480, 100, 64)
    y = lines_at(d, lines, f, size, 470, c.CREAM, 1.15, center=True) + 30
    f = c.font_sans(44, "SemiBold")
    t = "Responde nos comentários"
    d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=c.MUTED)
    c.logo(img, d, W // 2, 1110, 1.2)
    f = c.font_sans(40, "Bold")
    t1 = "Segue para não perder o próximo"
    d.text(((W - d.textlength(t1, font=f)) / 2, 1230), t1, font=f, fill=c.CREAM)
    f = c.font_sans(44, "Bold")
    tw = d.textlength(HANDLE, font=f)
    d.rounded_rectangle([(W - tw) / 2 - 45, 1310, (W + tw) / 2 + 45, 1400], radius=45, fill=c.TEAL)
    d.text(((W - tw) / 2, 1330), HANDLE, font=f, fill=c.ON_ACCENT)
    return img


def main(src, out):
    dados = json.load(open(src, encoding="utf-8"))
    os.makedirs(out, exist_ok=True)
    itens = []
    for i, nt in enumerate(dados["noticias"]):
        itens.append((nt, nt.get("rotulo") or ROTULOS[min(i, 2)]))
    if dados.get("esporte"):
        itens.append((dados["esporte"], dados["esporte"].get("rotulo") or "ESPORTE"))
    total = 2 + 2 * len(itens)
    slides = [capa(dados, total)]
    n = 2
    for nt, rot in itens:
        slides.append(slide_titulo(nt, rot, n, total))
        slides.append(slide_explica(nt, n + 1, total))
        n += 2
    slides.append(final(dados, total))
    for i, s in enumerate(slides, 1):
        p = os.path.join(out, f"slide_{i:02d}.jpg")
        s.save(p, "JPEG", quality=85, optimize=True)
        print(p)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
