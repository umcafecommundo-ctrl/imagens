#!/usr/bin/env python3
"""Gera um video narrado (voz neural da Microsoft via edge-tts) a partir dos slides de um post,
com figurinhas estilo "recorte de jornal" que aparecem quando a voz fala de cada coisa.

Uso:
  python3 curiosidades/video.py <pasta_dos_slides> <narracao.json> <saida.mp4> [--voz pt-BR-AntonioNeural] [--rate +8%]

Os slides devem ser gerados com:  gerar.py ... --video sim
(sem "arrasta pro lado", texto no topo e zonas.json com o espaco livre de cada slide).

narracao.json: lista com 1 item por slide, na ordem (slide_01, slide_02, ...). Cada item:
  "fala simples"
  ou {"fala": "...", "pausa": 2.5,
      "imagens": [{"emoji": "🦩", "legenda": "flamingo adulto", "palavra": "flamingo"}, ...]}
  - pausa: segundos extras parado no slide depois da fala (padrao 0.7)
  - imagens: ate 2 por slide. A figurinha aparece quando a voz diz "palavra" (que precisa
    estar na fala); sem "palavra", aparece no inicio da fala. "emoji" = 1 emoji (imagem 3D
    Fluent Emoji da Microsoft, licenca MIT). "legenda" = 1 a 3 palavras.

Requer: pip install --break-system-packages edge-tts pillow fonttools brotli ; ffmpeg ; npm (baixa os emojis).
"""
import argparse, asyncio, glob, json, math, os, random, re, ssl, subprocess, sys, tempfile, unicodedata

import edge_tts
import edge_tts.communicate as comm
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.expanduser("~/.cache/curiosidades")
EMOJI_DIR = os.path.join(CACHE, "fluent-emoji-3d")

# Atras do proxy da sessao o certificado vem de /root/.ccr/ca-bundle.crt
for ca in ("/root/.ccr/ca-bundle.crt", os.environ.get("SSL_CERT_FILE", "")):
    if ca and os.path.exists(ca):
        comm._SSL_CTX = ssl.create_default_context(cafile=ca)
        break


# ---------------------------------------------------------------- utilidades
def dur(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", path])
    return float(out.strip())


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn" and (c.isalnum() or c == " ")).strip()


def fonte(nome, tam):
    os.makedirs(CACHE, exist_ok=True)
    ttf = os.path.join(CACHE, nome.replace(".woff2", ".ttf"))
    if not os.path.exists(ttf):
        from fontTools.ttLib import TTFont
        f = TTFont(os.path.join(AQUI, "fonts", nome))
        f.flavor = None
        f.save(ttf)
    return ImageFont.truetype(ttf, tam)


def emoji_png(e):
    if not os.path.isdir(EMOJI_DIR):
        os.makedirs(CACHE, exist_ok=True)
        tmp = tempfile.mkdtemp(prefix="emoji_")
        subprocess.run(["npm", "pack", "@lobehub/fluent-emoji-3d@1.1.0", "-q"], cwd=tmp, check=True,
                       stdout=subprocess.DEVNULL)
        tgz = glob.glob(os.path.join(tmp, "*.tgz"))[0]
        subprocess.run(["tar", "xzf", tgz, "-C", tmp], check=True)
        os.rename(os.path.join(tmp, "package", "assets"), EMOJI_DIR)
    cps = [f"{ord(c):x}" for c in e]
    for nome in ("-".join(cps), "-".join(c for c in cps if c != "fe0f")):
        p = os.path.join(EMOJI_DIR, nome + ".webp")
        if os.path.exists(p):
            return Image.open(p).convert("RGBA")
    raise SystemExit(f"ERRO: emoji {e!r} nao existe no Fluent Emoji 3D; escolha outro")


# ---------------------------------------------------------------- figurinha "recorte de jornal"
def recorte(img, legenda, altura, seed):
    rnd = random.Random(seed)
    H = int(altura)
    W = int(H * 0.86)
    pad = 60  # espaco para sombra/rotacao
    card = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # papel com borda rasgada
    pts = []
    passo = 14
    for x in range(0, W + 1, passo):
        pts.append((x, rnd.uniform(0, 7)))
    for y in range(0, H + 1, passo):
        pts.append((W - rnd.uniform(0, 7), y))
    for x in range(W, -1, -passo):
        pts.append((x, H - rnd.uniform(0, 7)))
    for y in range(H, -1, -passo):
        pts.append((rnd.uniform(0, 7), y))
    papel = Image.new("L", (W, H), 0)
    ImageDraw.Draw(papel).polygon(pts, fill=255)
    base = Image.new("RGBA", (W, H), (244, 239, 226, 255))
    d = ImageDraw.Draw(base)
    # textura de jornal: graos e colunas de "texto" bem claras
    for _ in range(int(W * H / 90)):
        x, y = rnd.randrange(W), rnd.randrange(H)
        g = rnd.randrange(205, 235)
        d.point((x, y), fill=(g, g - 3, g - 12, 255))
    m = int(W * 0.08)
    d.line((m, m, W - m, m), fill=(40, 40, 40, 255), width=4)
    d.line((m, m + 10, W - m, m + 10), fill=(40, 40, 40, 255), width=2)
    # emoji
    lado = int(min(W - 2 * m, H * 0.58))
    e = img.resize((lado, lado), Image.LANCZOS)
    ey = m + 26
    base.alpha_composite(e, ((W - lado) // 2, ey))
    # legenda estilo manchete
    leg = (legenda or "").upper()
    if leg:
        tam = int(H * 0.11)
        while tam > 18:
            f = fonte("anton.woff2", tam)
            if d.textlength(leg, font=f) <= W - 2 * m:
                break
            tam -= 2
        ty = ey + lado + int(H * 0.035)
        d.text((W // 2, ty), leg, font=f, fill=(25, 25, 25, 255), anchor="mt")
        bb = d.textbbox((W // 2, ty), leg, font=f, anchor="mt")
        # linhas de "texto de jornal" embaixo da manchete
        yy = bb[3] + 16
        while yy < H - m:
            fim = W - m - (rnd.randrange(0, W // 3) if rnd.random() < 0.3 else 0)
            d.line((m, yy, fim, yy), fill=(185, 180, 168, 255), width=5)
            yy += 15
    card.paste(base, (0, 0), papel)
    # fita adesiva
    fita = Image.new("RGBA", (int(W * 0.42), int(H * 0.085)), (238, 222, 160, 170))
    fita = fita.rotate(rnd.uniform(-8, 8), expand=True, resample=Image.BICUBIC)
    tela = Image.new("RGBA", (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0))
    # sombra
    sombra = Image.new("RGBA", tela.size, (0, 0, 0, 0))
    sm = Image.new("RGBA", (W, H), (0, 0, 0, 120))
    sombra.paste(sm, (pad + 10, pad + 16), papel)
    sombra = sombra.filter(ImageFilter.GaussianBlur(14))
    tela.alpha_composite(sombra)
    tela.alpha_composite(card, (pad, pad))
    tela.alpha_composite(fita, (pad + (W - fita.width) // 2, pad - fita.height // 2))
    ang = rnd.choice([-1, 1]) * rnd.uniform(2.5, 6)
    return tela.rotate(ang, expand=True, resample=Image.BICUBIC)


# ---------------------------------------------------------------- voz
async def tts(texto, voz, rate, path):
    c = edge_tts.Communicate(texto, voz, rate=rate, boundary="WordBoundary")
    palavras = []
    with open(path, "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio":
                f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                palavras.append((ch["offset"] / 1e7, ch["text"]))
    return palavras


def quando(palavra, fala, palavras, d_audio):
    if not palavra:
        return 0.0
    alvo = norm(palavra).split()
    if not alvo:
        return 0.0
    ws = [(t, norm(w)) for t, w in palavras]
    for i, (t, w) in enumerate(ws):
        if w.startswith(alvo[0]) and all(i + k < len(ws) and ws[i + k][1].startswith(a) for k, a in enumerate(alvo)):
            return t
    pos = norm(fala).find(norm(palavra))
    if pos < 0:
        print(f"  aviso: '{palavra}' nao esta na fala; figurinha no inicio", file=sys.stderr)
        return 0.0
    return d_audio * pos / max(1, len(norm(fala)))


# ---------------------------------------------------------------- principal
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
    zp = os.path.join(a.slides, "zonas.json")
    zonas = json.load(open(zp)) if os.path.exists(zp) else {}

    tmp = tempfile.mkdtemp(prefix="video_")
    lista = os.path.join(tmp, "lista.txt")
    total, n_fig = 0.0, 0
    with open(lista, "w") as L:
        for i, (sl, f) in enumerate(zip(slides, falas), 1):
            if isinstance(f, str):
                f = {"fala": f}
            mp3 = os.path.join(tmp, f"a{i}.mp3")
            palavras = None
            for tent in range(3):
                try:
                    palavras = asyncio.run(tts(f["fala"], a.voz, a.rate, mp3))
                    if os.path.getsize(mp3) > 1000:
                        break
                except Exception as e:
                    print(f"tts falhou (slide {i}, tentativa {tent+1}): {e}", file=sys.stderr)
            else:
                sys.exit(f"ERRO: nao consegui gerar a voz do slide {i}")
            da = dur(mp3)
            D = round(da + 0.2 + float(f.get("pausa", 0.7)), 2)
            total += D

            # figurinhas
            figs = (f.get("imagens") or [])[:2]
            z = zonas.get(os.path.basename(sl))
            entradas, filtros, ultimo = [], [], "[v0]"
            if figs and not z:
                print(f"  aviso: slide {i} sem zonas.json (gere os slides com --video sim); figurinhas ignoradas", file=sys.stderr)
                figs = []
            if figs:
                livre_h = z["y1"] - z["y0"]
                alt = min(540, livre_h - 30)
                if len(figs) == 2:
                    alt = min(alt, int((z["x1"] - z["x0"]) / 2 / 0.86 * 0.82))
                if alt < 230:
                    print(f"  aviso: slide {i} sem espaco livre ({livre_h}px); figurinhas ignoradas", file=sys.stderr)
                    figs = []
            for k, fig in enumerate(figs):
                png = os.path.join(tmp, f"fig{i}_{k}.png")
                im = recorte(emoji_png(fig["emoji"]), fig.get("legenda", ""), alt, seed=i * 10 + k)
                im.save(png)
                t0 = round(0.2 + quando(fig.get("palavra"), f["fala"], palavras, da), 2)
                cx = (z["x0"] + z["x1"]) / 2 if len(figs) == 1 else z["x0"] + (z["x1"] - z["x0"]) * (0.27 + 0.46 * k)
                cy = z["y0"] + (z["y1"] - z["y0"]) / 2
                x, y = int(cx - im.width / 2), int(cy - im.height / 2)
                idx = 2 + k
                entradas += ["-i", png]
                filtros.append(f"[{idx}:v]format=rgba,loop=-1:1,trim=duration={D},setpts=PTS-STARTPTS,"
                               f"fade=in:st={t0}:d=0.25:alpha=1[f{k}]")
                filtros.append(f"{ultimo}[f{k}]overlay=x={x}:y='{y}+70*max(0\\,1-(t-{t0})/0.3)':eval=frame:"
                               f"enable='gte(t\\,{t0})'[v{k+1}]")
                ultimo = f"[v{k+1}]"
                n_fig += 1
            fc = (f"[0:v]scale=1080:1920,format=yuv420p,loop=-1:1,trim=duration={D},setpts=PTS-STARTPTS[v0];"
                  + "".join(x + ";" for x in filtros)
                  + f"{ultimo}format=yuv420p[vout];"
                  f"[1:a]adelay=200|200,apad,atrim=duration={D},aresample=44100[a]")
            parte, final = os.path.join(tmp, f"tmp_s{i}.mp4"), os.path.join(tmp, f"s{i}.mp4")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", "30", "-i", sl, "-i", mp3] + entradas +
                           ["-filter_complex", fc, "-map", "[vout]", "-map", "[a]", "-c:v", "libx264", "-crf", "18",
                            "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k",
                            "-ac", "2", "-t", str(D), parte], check=True)
            os.rename(parte, final)
            L.write(f"file '{final}'\n")
    saida_tmp = a.saida[:-4] + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista,
                    "-c", "copy", "-movflags", "+faststart", saida_tmp], check=True)
    os.rename(saida_tmp, a.saida)
    print(f"video: {a.saida} ({total:.1f} s, {len(slides)} slides, {n_fig} figurinhas, voz {a.voz})")


if __name__ == "__main__":
    main()
