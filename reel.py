"""Gera um Reel 1080x1920 (MP4, sem música) do @umcafecommundo a partir do mesmo JSON do carrossel.

Uso: python3 reel.py noticias.json saida.mp4

Cada slide do carrossel vira uma cena: capa 3s, cada notícia 6s, final 3s,
com transição suave e leve zoom. Inclui faixa de áudio silenciosa.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carrossel as c

VW, VH = 1080, 1920
FPS = 30


def frame_from_slide(slide, topo):
    img = Image.new("RGB", (VW, VH), c.BG)
    y = (VH - c.H) // 2 + 40
    img.paste(slide, (0, y))
    d = ImageDraw.Draw(img)
    f = c.font_sans(34, "Bold")
    d.text(((VW - d.textlength(topo, font=f)) / 2, 170), topo, font=f, fill=c.TEAL)
    f2 = c.font_sans(30, "Medium")
    t = "Siga @umcafecommundo"
    d.text(((VW - d.textlength(t, font=f2)) / 2, VH - 190), t, font=f2, fill=c.MUTED)
    return img


def main(src, out):
    dados = json.load(open(src, encoding="utf-8"))
    total = len(dados["noticias"]) + 2
    slides = [c.capa(dados, total)]
    slides += [c.slide_noticia(nt, i + 2, total) for i, nt in enumerate(dados["noticias"])]
    slides.append(c.final(dados, total))
    durs = [3.0] + [6.0] * len(dados["noticias"]) + [3.0]
    topo = dados.get("topo", "NOTÍCIAS DO MUNDO")

    tmp = tempfile.mkdtemp()
    clips = []
    for i, (s, dur) in enumerate(zip(slides, durs)):
        png = os.path.join(tmp, f"f{i}.png")
        frame_from_slide(s, topo).save(png)
        clip = os.path.join(tmp, f"c{i}.mp4")
        n = int(dur * FPS)
        vf = (f"scale=2160:-1,zoompan=z='min(zoom+0.0004,1.04)':d={n}:"
              f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={VW}x{VH}:fps={FPS},"
              f"fade=t=in:st=0:d=0.35,fade=t=out:st={dur - 0.35:.2f}:d=0.35,format=yuv420p")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png,
                        "-vf", vf, "-t", f"{dur}", "-r", str(FPS),
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", clip], check=True)
        clips.append(clip)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{p}'\n" for p in clips)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
                    "-shortest", "-c:v", "copy", "-c:a", "aac", "-b:a", "64k",
                    "-movflags", "+faststart", out], check=True)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
