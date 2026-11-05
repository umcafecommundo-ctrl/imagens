#!/usr/bin/env python3
"""Gera um video narrado (voz neural da Microsoft via edge-tts) a partir dos slides de um post,
no estilo "short" (v2, 05/11/2026): zoom lento nos slides, legenda grande que acompanha a fala
palavra por palavra, figurinhas "recorte de jornal" que pulam na tela quando a voz fala de cada
coisa, contagem regressiva 3-2-1 nas pausas do quiz e musica de fundo baixinha (gerada aqui
mesmo, sem direitos autorais), que abaixa sozinha quando a voz fala.

Uso:
  python3 curiosidades/video.py <pasta_dos_slides> <narracao.json> <saida.mp4>
          [--plataforma tiktok|youtube] [--final-slide <jpg>] [--voz pt-BR-AntonioNeural] [--rate +15%]
          [--sem-musica]

Normalmente quem chama este script e o produzir.py (gera slides + os dois videos de uma vez).

Os slides devem ser gerados com:  gerar.py ... --video sim
(sem "arrasta pro lado", texto no topo e zonas.json com o espaco livre de cada slide).

narracao.json: lista com 1 item por slide, na ordem (slide_01, slide_02, ...). Cada item:
  "fala simples"
  ou {"fala": "...", "pausa": 3,
      "fala_youtube": "...",            (opcional: usada no lugar de "fala" com --plataforma youtube)
      "imagens": [{"emoji": "🦩", "legenda": "flamingo adulto", "palavra": "flamingo"}, ...]}
  - pausa: segundos extras parado no slide depois da fala (padrao 0.35). Com pausa >= 2 aparece
    a contagem regressiva no lugar da legenda (use 3 nas perguntas do quiz).
  - imagens: ate 2 por slide. A figurinha aparece quando a voz diz "palavra" (que precisa
    estar na fala); sem "palavra", aparece no inicio da fala. "emoji" = 1 emoji (imagem 3D
    Fluent Emoji da Microsoft, licenca MIT). "legenda" = 1 a 3 palavras.
--plataforma youtube: usa "fala_youtube" quando existir e, no ultimo slide, a imagem de --final-slide
(o slide final com o @ do canal do YouTube).

Requer: pip install --break-system-packages edge-tts pillow fonttools brotli numpy ; ffmpeg ; npm (baixa os emojis).
"""
import argparse, asyncio, glob, json, math, os, random, re, ssl, subprocess, sys, tempfile, unicodedata, wave

import edge_tts
import edge_tts.communicate as comm
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.expanduser("~/.cache/curiosidades")
EMOJI_DIR = os.path.join(CACHE, "fluent-emoji-3d")
W, H, FPS = 1080, 1920, 30
AMARELO = (255, 214, 10)

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
                palavras.append((ch["offset"] / 1e7, ch["text"], ch.get("duration", 0) / 1e7))
    return palavras


def quando(palavra, fala, palavras, d_audio):
    if not palavra:
        return 0.0
    alvo = norm(palavra).split()
    if not alvo:
        return 0.0
    ws = [(p[0], norm(p[1])) for p in palavras]
    for i, (t, w) in enumerate(ws):
        if w.startswith(alvo[0]) and all(i + k < len(ws) and ws[i + k][1].startswith(a) for k, a in enumerate(alvo)):
            return t
    pos = norm(fala).find(norm(palavra))
    if pos < 0:
        print(f"  aviso: '{palavra}' nao esta na fala; figurinha no inicio", file=sys.stderr)
        return 0.0
    return d_audio * pos / max(1, len(norm(fala)))


# ---------------------------------------------------------------- legenda palavra por palavra
def blocos(palavras, d_audio, max_pal=3, max_chars=18, fala=""):
    """Agrupa as palavras faladas em blocos curtos de legenda: [(inicio, fim, [(ini, fim, texto)])]."""
    # palavras da fala seguidas de pontuacao: o bloco termina ali
    toks = [t for t in re.split(r"\s+", fala.strip()) if re.search(r"\w", t)]
    quebra = set()
    if len(toks) == len(palavras):
        quebra = {k for k, t in enumerate(toks) if re.search(r"[.,!?:;]$", t)}
    ws = []
    for k, (t, w, d) in enumerate(palavras):
        fim = t + d if d else (palavras[k + 1][0] if k + 1 < len(palavras) else d_audio)
        ws.append((t, fim, w))
    out, atual = [], []
    for k, (t, fim, w) in enumerate(ws):
        if atual:
            gap = t - atual[-1][1]
            chars = sum(len(x[2]) + 1 for x in atual) + len(w)
            if len(atual) >= max_pal or chars > max_chars or gap > 0.32 or (k - 1) in quebra:
                out.append(atual)
                atual = []
        atual.append((t, fim, w))
    if atual:
        out.append(atual)
    res = []
    for k, b in enumerate(out):
        ini = b[0][0]
        fim = b[-1][1]
        if k + 1 < len(out) and out[k + 1][0][0] - fim < 0.4:
            fim = out[k + 1][0][0]
        else:
            fim += 0.25
        res.append((ini, fim, b))
    return res


_leg_cache = {}


def img_legenda(palavras_bloco, ativa, largura_max=940):
    chave = (tuple(p[2] for p in palavras_bloco), ativa)
    if chave in _leg_cache:
        return _leg_cache[chave]
    txts = [p[2].upper() for p in palavras_bloco]
    tam = 104
    while True:
        f = fonte("anton.woff2", tam)
        esp = int(tam * 0.28)
        larg = sum(f.getlength(t) for t in txts) + esp * (len(txts) - 1)
        if larg <= largura_max - 40 or tam <= 56:
            break
        tam -= 4
    pad = 26
    asc, desc = f.getmetrics()
    alt = asc + desc
    im = Image.new("RGBA", (int(larg) + 2 * pad, alt + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = pad
    for k, t in enumerate(txts):
        cor = AMARELO if k == ativa else (255, 255, 255)
        d.text((x, pad), t, font=f, fill=cor, stroke_width=max(6, tam // 11), stroke_fill=(10, 10, 10))
        x += f.getlength(t) + esp
    # sombra leve para destacar em qualquer fundo
    sombra = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sombra.paste((0, 0, 0, 110), (0, 0), im.split()[3])
    sombra = sombra.filter(ImageFilter.GaussianBlur(8))
    fim = Image.new("RGBA", im.size, (0, 0, 0, 0))
    fim.alpha_composite(sombra, (0, 6))
    fim.alpha_composite(im)
    _leg_cache[chave] = fim
    return fim


_cont_cache = {}


def img_contagem(n):
    if n in _cont_cache:
        return _cont_cache[n]
    lado = 230
    im = Image.new("RGBA", (lado + 40, lado + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((20, 26, 20 + lado, 26 + lado), fill=(0, 0, 0, 90))
    d.ellipse((20, 20, 20 + lado, 20 + lado), fill=(255, 106, 19), outline=(10, 10, 10), width=8)
    f = fonte("anton.woff2", 150)
    d.text((20 + lado / 2, 20 + lado / 2 + 6), str(n), font=f, fill=(255, 255, 255), anchor="mm",
           stroke_width=8, stroke_fill=(10, 10, 10))
    _cont_cache[n] = im
    return im


# ---------------------------------------------------------------- musica de fundo (gerada, sem direitos)
def musica(duracao, path, seed=0):
    sr = 44100
    rnd = random.Random(seed)
    bpm = 96
    beat = 60 / bpm
    n = int(sr * (duracao + 1))
    out = np.zeros(n, dtype=np.float64)
    # progressoes suaves em do maior / la menor (frequencias em Hz)
    nota = lambda m: 440.0 * 2 ** ((m - 69) / 12)
    progs = [[(48, 52, 55, 59), (45, 48, 52, 55), (41, 45, 48, 52), (43, 47, 50, 55)],
             [(45, 48, 52, 55), (41, 45, 48, 52), (48, 52, 55, 59), (43, 47, 50, 55)],
             [(41, 45, 48, 52), (43, 47, 50, 55), (45, 48, 52, 55), (48, 52, 55, 59)]]
    prog = progs[seed % len(progs)]
    compasso = 4 * beat
    t_acorde = np.arange(int(sr * compasso)) / sr
    k = 0
    pos = 0
    padrao = [0, 2, 1, 3, 2, 1, 3, 2]
    while pos < n:
        ac = prog[k % len(prog)]
        # pad: acorde grave bem suave
        seg = np.zeros_like(t_acorde)
        for m in ac:
            fr = nota(m)
            seg += 0.10 * np.sin(2 * np.pi * fr * t_acorde) + 0.03 * np.sin(2 * np.pi * 2 * fr * t_acorde)
        env = np.minimum(1, t_acorde / 0.4) * np.minimum(1, (compasso - t_acorde) / 0.4)
        seg *= env
        # arpejo tipo marimba em colcheias, uma oitava acima
        for c in range(8):
            if rnd.random() < 0.12:
                continue
            m = ac[padrao[c]] + 12
            ini = int(c * beat / 2 * sr)
            tt = np.arange(int(0.6 * sr)) / sr
            fr = nota(m)
            pl = (np.sin(2 * np.pi * fr * tt) + 0.35 * np.sin(2 * np.pi * 4 * fr * tt) * np.exp(-tt * 30)) \
                * np.exp(-tt * 6) * 0.22
            fim = min(len(seg), ini + len(pl))
            seg[ini:fim] += pl[:fim - ini]
        fim = min(n, pos + len(seg))
        out[pos:fim] += seg[:fim - pos]
        pos += len(seg)
        k += 1
    out = out[:int(sr * duracao)]
    # fade in/out
    fi = int(sr * 0.8)
    fo = int(sr * 1.5)
    out[:fi] *= np.linspace(0, 1, fi)
    out[-fo:] *= np.linspace(1, 0, fo)
    out = out / (np.max(np.abs(out)) + 1e-9) * 0.9
    pcm = (out * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


# ---------------------------------------------------------------- render de um slide
def ease_pop(x):
    """0 -> 1 com um pequeno 'quique' (passa um pouco de 1 e volta)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    return 1 + 2.2 * (x - 1) ** 3 + 1.2 * (x - 1) ** 2


def render_slide(i, sl, f, fala, mp3, palavras, da, z, figs_png, D, saida):
    base = Image.open(sl).convert("RGB").resize((W, H))
    # legenda e figurinhas: posicoes
    legs = blocos(palavras, da, fala=fala)
    pausa = float(f.get("pausa", 0.35))
    cont_ini = 0.2 + da + 0.1 if pausa >= 2 else None
    leg_y = None
    fig_area = None
    if z:
        y0, y1 = z["y0"], z["y1"]
        leg_cy = min(y1 - 90, 1500)
        if leg_cy - 80 < y0 - 20 and y0 + 80 <= 1530:
            leg_cy = y0 + 80  # pouco espaco: legenda logo abaixo do texto, sem figurinha
        if leg_cy - 80 >= y0 - 20:
            leg_y = leg_cy
            fig_area = (y0, leg_cy - 110)
        else:
            print(f"  aviso: slide {i} sem espaco para a legenda; legenda omitida", file=sys.stderr)
            fig_area = (y0, y1)
    else:
        leg_y = 1450
    figs = []
    if figs_png and fig_area:
        livre = fig_area[1] - fig_area[0]
        alt = min(520, livre - 20)
        if len(figs_png) == 2:
            alt = min(alt, int((z["x1"] - z["x0"]) / 2 / 0.86 * 0.82))
        if alt < 200:
            print(f"  aviso: slide {i} sem espaco livre ({livre}px); figurinhas ignoradas", file=sys.stderr)
        else:
            for k, (png, t0) in enumerate(figs_png):
                im = Image.open(png)
                fator = alt / 520  # o recorte foi gerado com altura 520
                im = im.resize((int(im.width * fator), int(im.height * fator)), Image.LANCZOS)
                cx = (z["x0"] + z["x1"]) / 2 if len(figs_png) == 1 else z["x0"] + (z["x1"] - z["x0"]) * (0.27 + 0.46 * k)
                cy = (fig_area[0] + fig_area[1]) / 2
                figs.append((im, cx, cy, t0, k))
    cache_fig = {}

    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-i", mp3, "-filter_complex",
           f"[1:a]adelay=200|200,apad,atrim=duration={D},aresample=44100[a]",
           "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "19", "-preset", "veryfast",
           "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "160k", "-ac", "2", "-t", str(D), saida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    nfr = int(round(D * FPS))
    cx0, cy0 = W / 2, 760
    for fr in range(nfr):
        t = fr / FPS
        s = 1.0 + 0.045 * (t / D)
        frame = base.transform((W, H), Image.AFFINE, (1 / s, 0, cx0 - cx0 / s, 0, 1 / s, cy0 - cy0 / s),
                               resample=Image.BILINEAR)
        for im, cx, cy, t0, k in figs:
            if t < t0:
                continue
            x = (t - t0) / 0.35
            e = ease_pop(x)
            esc = 0.55 + 0.45 * e
            chave = (k, round(esc, 2))
            if chave not in cache_fig:
                cache_fig[chave] = im if esc == 1 else im.resize((max(1, int(im.width * esc)), max(1, int(im.height * esc))), Image.BILINEAR)
            fi = cache_fig[chave]
            boia = 6 * math.sin(2 * math.pi * (t - t0) / 2.6 + k)
            frame.paste(fi, (int(cx - fi.width / 2), int(cy - fi.height / 2 + boia)), fi)
        if cont_ini is not None and t >= cont_ini:
            resta = D - t
            nnum = max(1, min(3, math.ceil(resta - 0.15)))
            ci = img_contagem(nnum)
            frame.paste(ci, (int(W / 2 - ci.width / 2), int((leg_y or 1450) - ci.height / 2)), ci)
        elif leg_y is not None:
            tv = t - 0.2
            for ini, fim, bl in legs:
                if ini <= tv < fim:
                    ativa = 0
                    for kk, (a, b, _) in enumerate(bl):
                        if tv >= a:
                            ativa = kk
                    li = img_legenda(bl, ativa)
                    dy = int(18 * max(0, 1 - (tv - ini) / 0.12))
                    frame.paste(li, (int(W / 2 - li.width / 2), int(leg_y - li.height / 2 + dy)), li)
                    break
        p.stdin.write(frame.tobytes())
    p.stdin.close()
    if p.wait() != 0:
        sys.exit(f"ERRO: ffmpeg falhou no slide {i}")


# ---------------------------------------------------------------- principal
def voz(fala, a, mp3, i):
    for tent in range(3):
        try:
            palavras = asyncio.run(tts(fala, a.voz, a.rate, mp3))
            if os.path.getsize(mp3) > 1000:
                return palavras
        except Exception as e:
            print(f"tts falhou (slide {i}, tentativa {tent+1}): {e}", file=sys.stderr)
    sys.exit(f"ERRO: nao consegui gerar a voz do slide {i}")


def finalizar(segs, total, saida, tmp, a, nome):
    lista = os.path.join(tmp, f"lista_{nome}.txt")
    with open(lista, "w") as L:
        for s in segs:
            L.write(f"file '{s}'\n")
    junto = os.path.join(tmp, f"junto_{nome}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista,
                    "-c", "copy", junto], check=True)
    saida_tmp = saida[:-4] + ".tmp.mp4"
    if a.sem_musica:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", junto, "-c", "copy", "-movflags", "+faststart", saida_tmp], check=True)
    else:
        wav = os.path.join(tmp, f"musica_{nome}.wav")
        musica(total, wav, seed=sum(map(ord, os.path.basename(os.path.abspath(a.slides)))))
        fc = ("[0:a]asplit=2[v1][v2];[1:a]volume=0.18,aformat=channel_layouts=stereo,aresample=44100[m0];"
              "[m0][v1]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=350[m];"
              "[v2][m]amix=inputs=2:duration=first:normalize=0[a]")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", junto, "-i", wav, "-filter_complex", fc,
                        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                        "-movflags", "+faststart", saida_tmp], check=True)
    os.rename(saida_tmp, saida)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slides")
    ap.add_argument("narracao")
    ap.add_argument("saida", help="video do TikTok (ou da --plataforma escolhida)")
    ap.add_argument("--plataforma", default="tiktok", choices=["tiktok", "youtube"])
    ap.add_argument("--saida-youtube", default=None,
                    help="gera tambem a versao do YouTube neste arquivo (reaproveita os slides iguais)")
    ap.add_argument("--final-slide", default=None, help="slide final com o @ do YouTube")
    ap.add_argument("--voz", default="pt-BR-AntonioNeural")
    ap.add_argument("--rate", default="+15%")
    ap.add_argument("--sem-musica", action="store_true")
    a = ap.parse_args()

    slides = sorted(glob.glob(os.path.join(a.slides, "slide_*.jpg")))
    falas = json.load(open(a.narracao, encoding="utf-8"))
    if len(falas) != len(slides):
        sys.exit(f"ERRO: {len(slides)} slides e {len(falas)} falas; precisa ser 1 fala por slide")
    zp = os.path.join(a.slides, "zonas.json")
    zonas = json.load(open(zp)) if os.path.exists(zp) else {}
    versoes = [(a.plataforma, a.saida)]
    if a.saida_youtube:
        versoes.append(("youtube", a.saida_youtube))

    tmp = tempfile.mkdtemp(prefix="video_")
    segs = {p: [] for p, _ in versoes}
    totais = {p: 0.0 for p, _ in versoes}
    n_fig = 0
    for i, (sl0, f) in enumerate(zip(slides, falas), 1):
        if isinstance(f, str):
            f = {"fala": f}
        z = zonas.get(os.path.basename(sl0))
        feito = None  # (fala, slide) -> segmento ja renderizado
        for plat, _ in versoes:
            fala = f.get("fala_youtube") if plat == "youtube" and f.get("fala_youtube") else f["fala"]
            sl = a.final_slide if plat == "youtube" and i == len(slides) and a.final_slide else sl0
            if feito and feito[0] == (fala, sl):
                segs[plat].append(feito[1])
                totais[plat] += feito[2]
                continue
            mp3 = os.path.join(tmp, f"a{i}_{plat}.mp3")
            palavras = voz(fala, a, mp3, i)
            da = dur(mp3)
            D = round(da + 0.2 + float(f.get("pausa", 0.35)), 2)
            figs = (f.get("imagens") or [])[:2]
            if figs and not z:
                print(f"  aviso: slide {i} sem zonas.json (gere os slides com --video sim); figurinhas ignoradas", file=sys.stderr)
                figs = []
            figs_png = []
            for k, fig in enumerate(figs):
                png = os.path.join(tmp, f"fig{i}_{k}.png")
                if not os.path.exists(png):
                    recorte(emoji_png(fig["emoji"]), fig.get("legenda", ""), 520, seed=i * 10 + k).save(png)
                    n_fig += 1
                t0 = round(0.2 + quando(fig.get("palavra"), fala, palavras, da), 2)
                figs_png.append((png, t0))
            seg = os.path.join(tmp, f"s{i}_{plat}.mp4")
            render_slide(i, sl, f, fala, mp3, palavras, da, z, figs_png, D, seg)
            segs[plat].append(seg)
            totais[plat] += D
            feito = ((fala, sl), seg, D)
    tempos = {}
    for plat, saida in versoes:
        t, lst = 0.0, []
        for sg in segs[plat]:
            d_ = dur(sg)
            lst.append([round(t, 2), round(t + d_, 2)])
            t += d_
        tempos[os.path.basename(saida)] = lst
    try:
        json.dump(tempos, open(os.path.join(a.slides, "tempos.json"), "w"), indent=1)
    except OSError:
        pass
    for plat, saida in versoes:
        finalizar(segs[plat], totais[plat], saida, tmp, a, plat)
        print(f"video: {saida} ({totais[plat]:.1f} s, {len(slides)} slides, {n_fig} figurinhas, voz {a.voz} {a.rate}, {plat})")


if __name__ == "__main__":
    main()
