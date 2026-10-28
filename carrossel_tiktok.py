"""Gera o carrossel do @umcafecommundo em formato TikTok (1080x1920, 9:16).

Uso: python3 carrossel_tiktok.py noticias.json pasta_saida

Usa o mesmo JSON do carrossel do Instagram. Cada slide 1080x1350 é centralizado
num fundo 9:16, com o topo "NOTÍCIAS DO MUNDO" e "Siga @umcafecommundo" embaixo,
deixando livres as margens que a interface do TikTok cobre.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carrossel as c
from reel import frame_from_slide


def main(src, out):
    dados = json.load(open(src, encoding="utf-8"))
    os.makedirs(out, exist_ok=True)
    total = len(dados["noticias"]) + 2
    slides = [c.capa(dados, total)]
    slides += [c.slide_noticia(nt, i + 2, total) for i, nt in enumerate(dados["noticias"])]
    slides.append(c.final(dados, total))
    topo = dados.get("topo", "NOTÍCIAS DO MUNDO")
    for i, s in enumerate(slides, 1):
        p = os.path.join(out, f"slide_{i:02d}.jpg")
        frame_from_slide(s, topo).save(p, "JPEG", quality=85, optimize=True)
        print(p)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
