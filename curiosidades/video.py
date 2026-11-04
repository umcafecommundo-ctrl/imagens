#!/usr/bin/env python3
"""Gera um video narrado (voz neural da Microsoft via edge-tts) a partir dos slides de um post.

Uso:
  python3 curiosidades/video.py <pasta_dos_slides> <narracao.json> <saida.mp4> [--voz pt-BR-AntonioNeural] [--rate +8%]

narracao.json: lista com 1 item por slide, na ordem (slide_01, slide_02, ...).
Cada item e uma string (a fala) ou {"fala": "...", "pausa": 2.5}
("pausa" = segundos extras parado no slide depois da fala; padrao 0.7).

Requer: pip install --break-system-packages edge-tts ; ffmpeg no PATH.
"""
import argparse, asyncio, glob, json, os, ssl, subprocess, sys, tempfile

import edge_tts
import edge_tts.communicate as comm

# Atras do proxy da sessao o certificado vem de /root/.ccr/ca-bundle.crt
for ca in ("/root/.ccr/ca-bundle.crt", os.environ.get("SSL_CERT_FILE", "")):
    if ca and os.path.exists(ca):
        comm._SSL_CTX = ssl.create_default_context(cafile=ca)
        break


def dur(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", path])
    return float(out.strip())


async def tts(texto, voz, rate, path):
    await edge_tts.Communicate(texto, voz, rate=rate).save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slides")
    ap.add_argument("narracao")
    ap.add_argument("saida")
    ap.add_argument("--voz", default="pt-BR-AntonioNeural")
    ap.add_argument("--rate", default="+8%")
    a = ap.parse_args()

    slides = sorted(glob.glob(os.path.join(a.slides, "slide_*.jpg")))
    falas = json.load(open(a.narracao, encoding="utf-8"))
    if len(falas) != len(slides):
        sys.exit(f"ERRO: {len(slides)} slides e {len(falas)} falas; precisa ser 1 fala por slide")

    tmp = tempfile.mkdtemp(prefix="video_")
    lista = os.path.join(tmp, "lista.txt")
    total = 0.0
    with open(lista, "w") as L:
        for i, (sl, f) in enumerate(zip(slides, falas), 1):
            if isinstance(f, str):
                f = {"fala": f}
            mp3 = os.path.join(tmp, f"a{i}.mp3")
            for tent in range(3):
                try:
                    asyncio.run(tts(f["fala"], a.voz, a.rate, mp3))
                    if os.path.getsize(mp3) > 1000:
                        break
                except Exception as e:
                    print(f"tts falhou (slide {i}, tentativa {tent+1}): {e}", file=sys.stderr)
            else:
                sys.exit(f"ERRO: nao consegui gerar a voz do slide {i}")
            D = round(dur(mp3) + 0.2 + float(f.get("pausa", 0.7)), 2)
            total += D
            parte, final = os.path.join(tmp, f"tmp_s{i}.mp4"), os.path.join(tmp, f"s{i}.mp4")
            subprocess.run([
                "ffmpeg", "-v", "error", "-y", "-framerate", "30", "-i", sl, "-i", mp3,
                "-filter_complex",
                f"[0:v]scale=1080:1920,format=yuv420p,loop=-1:1,trim=duration={D},setpts=PTS-STARTPTS[v];"
                f"[1:a]adelay=200|200,apad,atrim=duration={D},aresample=44100[a]",
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
                "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ac", "2", parte],
                check=True)
            os.rename(parte, final)
            L.write(f"file '{final}'\n")
    saida_tmp = a.saida[:-4] + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista,
                    "-c", "copy", "-movflags", "+faststart", saida_tmp], check=True)
    os.rename(saida_tmp, a.saida)
    print(f"video: {a.saida} ({total:.1f} s, {len(slides)} slides, voz {a.voz})")


if __name__ == "__main__":
    main()
