"""Reel narrado de UMA notícia em detalhe (decisão do Luis em 04/11/2026), voz Francisca (Microsoft).

Uso: python3 reel_voz.py noticias.json saida.mp4

Lê o campo "reel" do JSON:
{
  "rotulo": "O MUNDO EXPLICADO" | "NO SEU BOLSO" | "CURIOSIDADE" | ...,
  "manchete": "gancho curto, 2 linhas no máximo (aparece inteiro no 1º quadro)",
  "fonte": "Veículo1, Veículo2",
  "cenas": [   # 5 a 7 cenas; a 1ª é sempre "manchete"; mire em 35 a 45 s no total
    {"tipo": "manchete", "fala": "..."},
    {"tipo": "numero", "valor": "75", "rotulo": "lojas atingidas", "sub": "só na Bélgica", "fala": "..."},
    {"tipo": "lista", "titulo": "ONDE", "itens": ["Bélgica", "Suécia", "Irlanda"], "fala": "..."},
    {"tipo": "frase", "texto": "Ninguém assumiu o ataque", "destaque": "Ninguém", "fala": "..."},
    {"tipo": "importa", "texto": "por que isso importa, em 1 frase", "fala": "..."}
  ]
}
A cena final ("Siga @umcafecommundo") é automática. Legenda palavra a palavra sincronizada com a voz.
Requer: pip install --break-system-packages edge-tts  (domínio speech.platform.bing.com liberado).
Sai com código 2 e "AVISO" se o vídeo ficar com menos de 30 s (acrescente detalhe nas falas).
"""
import asyncio, json, math, os, subprocess, sys, tempfile, wave
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carrossel as c

W, H, FPS = 1080, 1920, 30
VOZ = os.environ.get("VOZ", "pt-BR-FranciscaNeural")
RATE = os.environ.get("RATE", "+10%")
BG, CREAM, AMBAR, MUTED, BOX = c.BG, c.CREAM, c.TEAL, c.MUTED, (78, 52, 37)
RED = (226, 74, 51)
FIM = "Siga o Um Café com o Mundo para entender o mundo em um minuto."
GAP = 0.28


# ---------- voz ----------
async def _fala(texto, mp3):
    import edge_tts
    com = edge_tts.Communicate(texto, VOZ, rate=RATE, boundary="WordBoundary",
                               proxy=os.environ.get("HTTPS_PROXY"))
    palavras = []
    with open(mp3, "wb") as fh:
        async for ch in com.stream():
            if ch["type"] == "audio":
                fh.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                palavras.append((ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7, ch["text"]))
    return palavras


def voz(texto, tmp, i):
    mp3, wav = os.path.join(tmp, f"v{i}.mp3"), os.path.join(tmp, f"v{i}.wav")
    for tentativa in range(3):
        try:
            palavras = asyncio.run(_fala(texto, mp3))
            if os.path.getsize(mp3) > 1000:
                break
        except Exception as e:  # rede instável: tenta de novo
            err = e
    else:
        raise SystemExit(f"ERRO: voz da Microsoft indisponível ({err})")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-af", f"apad=pad_dur={GAP}",
                    "-ar", "44100", "-ac", "1", wav], check=True)
    with wave.open(wav) as w:
        dur = w.getnframes() / w.getframerate()
    # devolve a pontuação do texto original às palavras da legenda (quando a contagem bate)
    tokens = texto.split()
    if len(tokens) == len(palavras):
        palavras = [(a, b, tok) for (a, b, _), tok in zip(palavras, tokens)]
    return wav, dur, palavras


# ---------- desenho ----------
def ease(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def centro(d, y, txt, f, fill, stroke=0):
    d.text(((W - d.textlength(txt, font=f)) / 2, y), txt, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=(30, 18, 10))


def wrap_fit(d, text, max_w, max_lines, start, minimum, serif=True, weight="Bold"):
    size = start
    while True:
        f = c.font_serif(size) if serif else c.font_sans(size, weight)
        lines = c.wrap(d, text, f, max_w)
        if len(lines) <= max_lines or size <= minimum:
            return f, lines, size
        size -= 4


_GLOBO = None


def fundo(t, total, rotulo, fonte, cena_final=False):
    global _GLOBO
    img = Image.new("RGB", (W, H), BG)
    if _GLOBO is None:
        g = c.globo(1500)
        a = g.split()[3].point(lambda v: int(v * 0.10))
        g.putalpha(a)
        _GLOBO = g
    # globo gigante e translúcido que desliza devagar (movimento constante)
    x = int(330 - 60 * math.sin(t * 0.35))
    y = int(1050 + 40 * math.cos(t * 0.3))
    img.paste(_GLOBO, (x, y), _GLOBO)
    d = ImageDraw.Draw(img)
    # barra de progresso no topo
    d.rounded_rectangle((90, 150, W - 90, 160), 5, fill=(92, 64, 48))
    d.rounded_rectangle((90, 150, 90 + (W - 180) * min(1, t / total), 160), 5, fill=AMBAR)
    if not cena_final:
        f = c.font_sans(34, "Bold")
        tw = d.textlength(rotulo, font=f)
        d.rounded_rectangle(((W - tw) / 2 - 28, 200, (W + tw) / 2 + 28, 262), 31, fill=AMBAR)
        centro(d, 211, rotulo, f, c.ON_ACCENT)
        if fonte:
            centro(d, H - 300, f"Fonte: {fonte}", c.font_sans(30, "Medium"), MUTED)
    return img, d


def legenda(d, palavras, ts):
    """Blocos de até 3 palavras, sincronizados com a voz; a palavra falada fica em âmbar."""
    if not palavras:
        return
    k = 0
    for i, (a, b, w) in enumerate(palavras):
        if ts >= a:
            k = i
    # blocos de até 3 palavras, quebrando no fim de cada frase
    blocos, cur = [], []
    for i, w in enumerate(palavras):
        cur.append(i)
        if len(cur) == 3 or w[2].endswith((".", "?", "!", ":")):
            blocos.append(cur)
            cur = []
    if cur:
        blocos.append(cur)
    idx = next(bl for bl in blocos if k in bl)
    bloco0 = idx[0]
    bloco = [palavras[i] for i in idx]
    f = c.font_sans(84, "Bold")
    ws = [d.textlength(w[2], font=f) for w in bloco]
    sp = d.textlength(" ", font=f)
    tot = sum(ws) + sp * (len(ws) - 1)
    if tot > W - 140:
        f = c.font_sans(int(84 * (W - 140) / tot), "Bold")
        ws = [d.textlength(w[2], font=f) for w in bloco]
        sp = d.textlength(" ", font=f)
        tot = sum(ws) + sp * (len(ws) - 1)
    x = (W - tot) / 2
    for j, w in enumerate(bloco):
        cor = AMBAR if bloco0 + j == k else CREAM
        d.text((x, 1440), w[2], font=f, fill=cor, stroke_width=7, stroke_fill=(30, 18, 10))
        x += ws[j] + sp


def cena_manchete(img, d, cena, p, t, R):
    f, lines, size = wrap_fit(d, R["manchete"], W - 160, 4, 124, 76)
    y = 360 + (760 - len(lines) * size * 1.12) / 2
    pulso = 1 + 0.015 * math.sin(t * 4)
    for j, ln in enumerate(lines):
        fz = c.font_serif(int(size * pulso))
        cor = AMBAR if j == len(lines) - 1 else CREAM
        centro(d, y, ln, fz, cor, 3)
        y += size * 1.12


def cena_numero(img, d, cena, p, t, R):
    v = str(cena.get("valor", ""))
    alvo = None
    if v.replace(".", "").isdigit():
        alvo = int(v.replace(".", ""))
    if alvo is not None and alvo > 1:
        n = int(alvo * ease(p / 0.45))
        txt = f"{n:,}".replace(",", ".")
    else:
        txt = v
    f, _, size = wrap_fit(d, txt, W - 160, 1, 300, 120)
    esc = 0.85 + 0.15 * ease(p / 0.2)
    f = c.font_serif(int(size * esc))
    centro(d, 470 + (300 - size * esc) / 2, txt, f, AMBAR)
    f2, lines, s2 = wrap_fit(d, cena.get("rotulo", ""), W - 200, 2, 72, 50, serif=False)
    y = 830
    for ln in lines:
        centro(d, y, ln, f2, CREAM)
        y += s2 * 1.2
    if cena.get("sub"):
        f3, lines, s3 = wrap_fit(d, cena["sub"], W - 200, 2, 52, 38, serif=False, weight="Medium")
        for ln in lines:
            centro(d, y + 10, ln, f3, MUTED)
            y += s3 * 1.25


def cena_lista(img, d, cena, p, t, R):
    if cena.get("titulo"):
        centro(d, 340, cena["titulo"].upper(), c.font_sans(44, "Bold"), AMBAR)
    itens = cena.get("itens", [])[:6]
    f = c.font_sans(62, "Bold")
    passo = 140 if len(itens) <= 5 else 120
    y0 = 430 + (5 - len(itens)) * passo / 2
    for i, it in enumerate(itens):
        a = ease((p - i * 0.11) / 0.18)
        if a <= 0:
            continue
        y = y0 + i * passo
        x = 140 + (1 - a) * 90
        f_it, _, _ = wrap_fit(d, it, 680, 1, 62, 40, serif=False)
        d.rounded_rectangle((x, y, x + 800, y + 112), 56, fill=BOX, outline=AMBAR, width=3)
        d.ellipse((x + 40, y + 40, x + 72, y + 72), fill=AMBAR)
        d.text((x + 100, y + 22), it, font=f_it, fill=CREAM)


def cena_frase(img, d, cena, p, t, R):
    texto, dest = cena.get("texto", ""), cena.get("destaque", "")
    f, lines, size = wrap_fit(d, texto, W - 180, 5, 104, 64)
    y = 380 + (800 - len(lines) * size * 1.18) / 2
    a = ease(p / 0.15)
    for ln in lines:
        x = (W - d.textlength(ln, font=f)) / 2
        for w in ln.split(" "):
            cor = AMBAR if dest and w.strip(".,!?;:").lower() in dest.lower().split() else CREAM
            d.text((x, y + (1 - a) * 40), w, font=f, fill=cor, stroke_width=3, stroke_fill=(30, 18, 10))
            x += d.textlength(w + " ", font=f)
        y += size * 1.18


def cena_importa(img, d, cena, p, t, R):
    f, lines, size = wrap_fit(d, cena.get("texto", ""), W - 280, 6, 72, 48)
    h = 130 + len(lines) * size * 1.25 + 50
    y0 = 360 + (800 - h) / 2
    a = ease(p / 0.15)
    d.rounded_rectangle((110, y0 + (1 - a) * 60, W - 110, y0 + h + (1 - a) * 60), 36, fill=BOX)
    d.text((170, y0 + 50 + (1 - a) * 60), "POR QUE IMPORTA", font=c.font_sans(38, "Bold"), fill=AMBAR)
    y = y0 + 130 + (1 - a) * 60
    for ln in lines:
        d.text((170, y), ln, font=f, fill=CREAM)
        y += size * 1.25


def cena_final(img, d, cena, p, t, R):
    c.logo(img, d, W // 2, 640, 2.0)
    f = c.font_serif(96)
    centro(d, 820, "Um Café", f, CREAM)
    centro(d, 930, "com o Mundo", f, CREAM)
    f2 = c.font_sans(56, "Bold")
    tw = d.textlength("@umcafecommundo", font=f2)
    esc = 1 + 0.03 * math.sin(t * 5)
    d.rounded_rectangle((W / 2 - tw / 2 - 50 * esc, 1100, W / 2 + tw / 2 + 50 * esc, 1210), 55, fill=AMBAR)
    centro(d, 1122, "@umcafecommundo", f2, c.ON_ACCENT)


DESENHO = {"manchete": cena_manchete, "numero": cena_numero, "lista": cena_lista,
           "frase": cena_frase, "importa": cena_importa, "final": cena_final}


def main(src, out):
    dados = json.load(open(src, encoding="utf-8"))
    R = dados["reel"]
    cenas = list(R["cenas"]) + [{"tipo": "final", "fala": FIM}]
    if cenas[0]["tipo"] != "manchete":
        raise SystemExit("ERRO: a 1ª cena precisa ser do tipo 'manchete'")
    tmp = tempfile.mkdtemp()
    faixas = []
    for i, ce in enumerate(cenas):
        faixas.append(voz(ce["fala"], tmp, i))
    total = sum(dur for _, dur, _ in faixas)
    if total < 30:
        print(f"AVISO: o Reel ficou com {total:.1f} s (mínimo 30 s). Acrescente detalhe nas falas.")
        sys.exit(2)
    rot = R.get("rotulo", "O MUNDO EXPLICADO").upper()
    fonte = R.get("fonte", "")
    fdir = os.path.join(tmp, "frames")
    os.makedirs(fdir)
    fr, t0 = 0, 0.0
    for ce, (wav, dur, palavras) in zip(cenas, faixas):
        n = int(round(dur * FPS))
        for k in range(n):
            t = t0 + k / FPS
            img, d = fundo(t, total, rot, fonte, ce["tipo"] == "final")
            DESENHO[ce["tipo"]](img, d, ce, k / n, t, R)
            d = ImageDraw.Draw(img)
            if ce["tipo"] != "final":
                legenda(d, palavras, k / FPS)
            else:
                centro(d, 1300, "Entenda o mundo em 1 minuto", c.font_sans(54, "Bold"), CREAM)
            img.save(os.path.join(fdir, f"f{fr:05d}.jpg"), quality=90)
            fr += 1
        t0 += n / FPS
    lst = os.path.join(tmp, "a.txt")
    with open(lst, "w") as fh:
        for wav, _, _ in faixas:
            fh.write(f"file '{wav}'\n")
    voz_wav = os.path.join(tmp, "voz.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-af", "loudnorm=I=-15:TP=-1.5", "-ar", "44100", voz_wav], check=True)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
                    "-i", os.path.join(fdir, "f%05d.jpg"), "-i", voz_wav,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", out], check=True)
    print(f"{out} ({total:.1f} s)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
