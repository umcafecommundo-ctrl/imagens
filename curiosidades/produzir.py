#!/usr/bin/env python3
"""Produz um post completo da Curiosidades da IA em video (v2, 05/11/2026).

Passo 1 - slides:
  python3 curiosidades/produzir.py slides <post.json> <pasta> --layout padrao|caderno
    gera os slides do video (gerar.py --video sim), copia o JSON para <pasta>/post.json e cria
    <pasta>/final_youtube.jpg (o slide final com o @ do canal do YouTube).
Passo 2 - escreva <pasta>/narracao.json (1 item por slide; veja o cabecalho do video.py).
Passo 3 - videos:
  python3 curiosidades/produzir.py video <pasta>
    gera <pasta>/video_tiktok.mp4 e <pasta>/video_youtube.mp4 (mesmo conteudo; muda o fim:
    no TikTok "comenta e segue" com o @ do TikTok, no YouTube "se inscreve" com o @ do canal)
    e as folhas de conferencia <pasta>/conferir_slides.jpg e <pasta>/conferir_video.jpg
    (quadros perto do fim de cada slide do video do TikTok).
"""
import glob, json, os, shutil, subprocess, sys, tempfile

from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
ARROBA_TIKTOK = "@curiosidadesda.iia"
ARROBA_YOUTUBE = "@Curiosidadesda_iia"


def folha(imgs, saida, largura=360, cols=4):
    ims = [Image.open(f) if isinstance(f, str) else f for f in imgs]
    h = int(ims[0].height * largura / ims[0].width)
    linhas = (len(ims) + cols - 1) // cols
    s = Image.new("RGB", (largura * cols, h * linhas), "white")
    for i, im in enumerate(ims):
        s.paste(im.convert("RGB").resize((largura, h)), ((i % cols) * largura, (i // cols) * h))
    s.save(saida, quality=85)


def slides(post, pasta, layout):
    os.makedirs(pasta, exist_ok=True)
    for f in glob.glob(os.path.join(pasta, "slide_*.jpg")):
        os.remove(f)
    ger = os.path.join(AQUI, "gerar.py")
    subprocess.run([sys.executable, ger, post, pasta, "--formato", "tiktok", "--layout", layout, "--video", "sim"], check=True)
    dados = json.load(open(post, encoding="utf-8"))
    json.dump(dados, open(os.path.join(pasta, "post.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tmp = tempfile.mkdtemp(prefix="yt_")
    dados_yt = dict(dados, arroba=ARROBA_YOUTUBE)
    if dados.get("final", {}).get("acoes"):
        ac = [x.replace("Segue a página", "Se inscreve no canal").replace("Segue", "Se inscreve") for x in dados["final"]["acoes"]]
        dados_yt["final"] = dict(dados["final"], acoes=ac)
    jy = os.path.join(tmp, "post.json")
    json.dump(dados_yt, open(jy, "w", encoding="utf-8"), ensure_ascii=False)
    subprocess.run([sys.executable, ger, jy, tmp, "--formato", "tiktok", "--layout", layout, "--video", "sim"],
                   check=True, stdout=subprocess.DEVNULL)
    ult = sorted(glob.glob(os.path.join(tmp, "slide_*.jpg")))[-1]
    shutil.copy(ult, os.path.join(pasta, "final_youtube.jpg"))
    sl = sorted(glob.glob(os.path.join(pasta, "slide_*.jpg")))
    folha(sl + [os.path.join(pasta, "final_youtube.jpg")], os.path.join(pasta, "conferir_slides.jpg"))
    print(f"{len(sl)} slides (+ final_youtube.jpg); conferencia em {pasta}/conferir_slides.jpg")


def video(pasta):
    vt, vy = os.path.join(pasta, "video_tiktok.mp4"), os.path.join(pasta, "video_youtube.mp4")
    subprocess.run([sys.executable, os.path.join(AQUI, "video.py"), pasta, os.path.join(pasta, "narracao.json"), vt,
                    "--saida-youtube", vy, "--final-slide", os.path.join(pasta, "final_youtube.jpg")], check=True)
    tempos = json.load(open(os.path.join(pasta, "tempos.json")))
    quadros = []
    tmp = tempfile.mkdtemp(prefix="q_")
    for nome, arq in (("video_tiktok.mp4", vt), ("video_youtube.mp4", vy)):
        lst = tempos[nome]
        pontos = [max(0.1, b - 0.4) for a, b in lst] if nome == "video_tiktok.mp4" else [max(0.1, lst[-1][1] - 0.4)]
        for k, t in enumerate(pontos):
            q = os.path.join(tmp, f"{nome}_{k:02d}.jpg")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", arq, "-frames:v", "1", q], check=True)
            quadros.append(q)
        d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", arq]))
        print(f"{nome}: {d:.1f} s")
    folha(quadros, os.path.join(pasta, "conferir_video.jpg"))
    print(f"conferencia: {pasta}/conferir_video.jpg (ultimo quadro = fim do video do YouTube)")


if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[1] == "slides":
        layout = sys.argv[sys.argv.index("--layout") + 1] if "--layout" in sys.argv else "padrao"
        slides(sys.argv[2], sys.argv[3], layout)
    elif len(sys.argv) >= 3 and sys.argv[1] == "video":
        video(sys.argv[2])
    else:
        sys.exit(__doc__)
