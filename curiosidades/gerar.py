#!/usr/bin/env python3
"""Gera os slides da página Curiosidades da IA a partir de um JSON.

Uso: python3 gerar.py <post.json> <pasta_saida> [--formato tiktok|instagram]

tiktok    = 1080x1920 (9:16), com margem de segurança para os botões do app
instagram = 1080x1350 (4:5)

Tipos de post (campo "tipo"):
  "explica": capa + 3 a 6 slides de fatos + slide final
  "quiz":    capa + 3 perguntas (cada uma com slide de resposta) + placar

Veja exemplo_explica.json e exemplo_quiz.json nesta pasta.
"""
import base64, html, json, os, pathlib, sys

from PIL import Image
from playwright.sync_api import sync_playwright

AQUI = pathlib.Path(__file__).resolve().parent
FONTES = AQUI / "fonts"

LARANJA = "#FF6A13"
ESCURO = "#0E1116"
CREME = "#F4F1EA"
AZUL = "#0B2233"
LARANJA_TXT = "#D9480F"  # laranja escuro, legível sobre creme

# fundo, texto, texto secundário, rótulo do topo, destaque, cor do "continua"
TEMAS = {
    "escuro": (ESCURO, CREME, "#C9CED8", "#9AA3B2", LARANJA, LARANJA),
    "azul": (AZUL, CREME, "#C3D2DC", "#9DB4C4", LARANJA, LARANJA),
    "creme": (CREME, ESCURO, "#3A414C", "#4A5260", LARANJA_TXT, LARANJA_TXT),
    "laranja": (LARANJA, ESCURO, ESCURO, ESCURO, CREME, ESCURO),
}
ROTACAO = ["escuro", "creme", "azul", "escuro", "creme", "azul"]


def e(t):
    return html.escape(str(t or ""))


def data_uri(nome):
    return "data:font/woff2;base64," + base64.b64encode((FONTES / nome).read_bytes()).decode()


def css_fontes():
    s = f"@font-face{{font-family:Anton;src:url({data_uri('anton.woff2')})}}"
    for w in (400, 600, 800, 900):
        s += f"@font-face{{font-family:Inter;font-weight:{w};src:url({data_uri(f'inter-{w}.woff2')})}}"
    return s


def pagina(fmt, tema, rotulo, contador, miolo, rodape, arroba):
    W = 1080
    H = 1920 if fmt == "tiktok" else 1350
    # margens: no TikTok os botões ficam à direita e a legenda embaixo
    pad = "170px 150px 400px 96px" if fmt == "tiktok" else "96px 96px 96px 96px"
    bg, fg, fg2, lab, dest, cont = TEMAS[tema]
    rod = f'<div class="rod" style="color:{cont}">{rodape}</div>' if rodape else ""
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
{FONTES_CSS}
*{{box-sizing:border-box}}
body{{margin:0;width:{W}px;height:{H}px;background:{bg};color:{fg};font-family:Inter,sans-serif;--s:1;--dest:{dest};--fg2:{fg2}}}
.pg{{width:{W}px;height:{H}px;padding:{pad};display:flex;flex-direction:column;gap:40px}}
.topo{{display:flex;justify-content:space-between;font-size:26px;font-weight:600;letter-spacing:3px;color:{lab};flex:none}}
.miolo{{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:calc(var(--s)*44px);overflow:hidden}}
.rod{{flex:none;font-size:28px;font-weight:800;letter-spacing:2px}}
h1,h2{{margin:0;font-family:Anton,sans-serif;font-weight:400;text-transform:uppercase;line-height:1.14;padding-top:.06em}}
.h1{{font-size:calc(var(--s)*160px)}}
.h2{{font-size:calc(var(--s)*118px)}}
.d{{color:var(--dest)}}
p{{margin:0}}
.t1{{font-size:calc(var(--s)*44px);line-height:1.35;font-weight:800}}
.t2{{font-size:calc(var(--s)*36px);line-height:1.45;color:var(--fg2)}}
.num{{font-family:Anton,sans-serif;font-size:calc(var(--s)*200px);line-height:1.05;color:var(--dest)}}
.pill{{align-self:flex-start;font-weight:800;font-size:calc(var(--s)*30px);letter-spacing:3px;padding:14px 28px;border-radius:999px}}
.op{{display:flex;align-items:center;gap:32px;border:3px solid rgba(128,128,128,.35);border-radius:20px;padding:calc(var(--s)*28px) 36px;font-size:calc(var(--s)*44px);font-weight:800}}
.op b{{font-family:Anton,sans-serif;font-weight:400;font-size:calc(var(--s)*56px);color:var(--dest);width:40px;flex:none}}
.ok{{display:flex;align-items:center;gap:28px;background:{LARANJA};color:{ESCURO};border-radius:24px;padding:calc(var(--s)*36px) 44px}}
.ok span{{font-family:Anton,sans-serif;font-size:calc(var(--s)*84px);line-height:1.14;text-transform:uppercase}}
.ok svg{{margin-left:auto;flex:none}}
.grade{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}}
.card{{background:{ESCURO};color:{CREME};border-radius:20px;padding:calc(var(--s)*28px) 32px;display:flex;flex-direction:column;gap:8px}}
.card i{{font-style:normal;font-family:Anton,sans-serif;font-size:calc(var(--s)*64px);color:{LARANJA}}}
.card span{{font-size:calc(var(--s)*30px);font-weight:800}}
.arroba{{flex:none;background:{ESCURO};color:{CREME};border-radius:18px;padding:32px 44px;font-size:44px;font-weight:800}}
</style></head><body><div class="pg">
<div class="topo"><span>{e(rotulo)}</span><span>{e(contador)}</span></div>
<div class="miolo" id="m">{miolo}</div>
{rod}{f'<div class="arroba">{e(arroba)}</div>' if arroba else ''}
</div></body></html>"""


SETA = '<svg aria-hidden="true" width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg aria-hidden="true" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#0E1116" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>'


def titulo(tag, cls, t, d):
    d = f' <span class="d">{e(d)}</span>' if d else ""
    return f'<{tag} class="{cls}">{e(t)}{d}</{tag}>'


def slides_explica(p, fmt, arroba):
    corpo = p["slides"]
    n = len(corpo) + 2
    rot = p.get("rotulo", "CURIOSIDADE")
    out = []
    c = p["capa"]
    miolo = ""
    if c.get("selo"):
        miolo += f'<span class="pill" style="background:{LARANJA};color:{ESCURO}">{e(c["selo"])}</span>'
    miolo += titulo("h1", "h1", c["titulo"], c.get("destaque"))
    if c.get("sub"):
        miolo += f'<p class="t2" style="font-size:calc(var(--s)*42px)">{e(c["sub"])}</p>'
    out.append(pagina(fmt, "escuro", rot, f"01 / {n:02d}", miolo, f"ARRASTA PRO LADO {SETA}", None))
    for i, s in enumerate(corpo):
        tema = s.get("tema") or ROTACAO[i % len(ROTACAO)]
        miolo = ""
        if s.get("numero"):
            miolo += f'<div class="num">{e(s["numero"])}</div>'
        miolo += titulo("h2", "h2", s["titulo"], s.get("destaque"))
        if s.get("texto"):
            miolo += f'<p class="t1">{e(s["texto"])}</p>'
        if s.get("extra"):
            miolo += f'<p class="t2">{e(s["extra"])}</p>'
        out.append(pagina(fmt, tema, rot, f"{i + 2:02d} / {n:02d}", miolo, "CONTINUA →", None))
    f = p.get("final", {})
    acoes = f.get("acoes") or ["Salva pra mostrar pra alguém", "Manda pra um amigo curioso", "Segue pra mais curiosidades"]
    miolo = titulo("h2", "h1", f.get("titulo", "Você sabia disso?"), f.get("destaque"))
    miolo += f'<p class="t1">{e(f.get("texto", "Comenta qual curiosidade te surpreendeu mais."))}</p>'
    miolo += '<div style="display:flex;flex-direction:column;gap:20px;font-size:calc(var(--s)*36px);font-weight:800">' + "".join(f"<span>{e(a)}</span>" for a in acoes) + "</div>"
    out.append(pagina(fmt, "laranja", rot, f"{n:02d} / {n:02d}", miolo, None, arroba))
    return out


def slides_quiz(p, fmt, arroba):
    qs = p["perguntas"]
    n = 2 + 2 * len(qs)
    out = []
    c = p["capa"]
    miolo = f'<span class="pill" style="background:{ESCURO};color:{LARANJA}">{e(c.get("selo", f"{len(qs)} PERGUNTAS"))}</span>'
    miolo += titulo("h1", "h1", c["titulo"], c.get("destaque"))
    miolo += f'<p class="t1">{e(c.get("sub", "Responde de cabeça, sem pesquisar. A resposta vem no slide seguinte."))}</p>'
    out.append(pagina(fmt, "laranja", "QUIZ DA IA", f"01 / {n:02d}", miolo, f"VALENDO! ARRASTA PRO LADO {SETA}", None))
    letras = "ABCD"
    for i, q in enumerate(qs):
        k = 2 + 2 * i
        miolo = titulo("h2", "h2", q["pergunta"], q.get("destaque"))
        miolo += '<div style="display:flex;flex-direction:column;gap:22px">' + "".join(
            f'<div class="op"><b>{letras[j]}</b>{e(o)}</div>' for j, o in enumerate(q["opcoes"])) + "</div>"
        out.append(pagina(fmt, "escuro", f"PERGUNTA {i + 1} DE {len(qs)}", f"{k:02d} / {n:02d}", miolo, "PENSOU? ARRASTA PRA VER →", None))
        cert = q["certa"]
        miolo = f'<div class="ok"><span>{letras[cert]} - {e(q["opcoes"][cert])}</span>{CHECK}</div>'
        miolo += f'<p class="t1">{e(q["explicacao"])}</p>'
        if q.get("extra"):
            miolo += f'<p class="t2">{e(q["extra"])}</p>'
        prox = "VER SEU RESULTADO →" if i == len(qs) - 1 else ("ÚLTIMA PERGUNTA →" if i == len(qs) - 2 else "PRÓXIMA PERGUNTA →")
        out.append(pagina(fmt, "creme", f"RESPOSTA {i + 1}", f"{k + 1:02d} / {n:02d}", miolo, prox, None))
    pl = p.get("placar") or ["Segue a página, urgente", "Tá no caminho", "Mandou bem", "Gênio. Prova nos comentários"]
    miolo = '<h2 class="h1">Quantas você acertou?</h2>'
    miolo += '<div class="grade">' + "".join(f'<div class="card"><i>{j}</i><span>{e(t)}</span></div>' for j, t in enumerate(pl)) + "</div>"
    miolo += '<p class="t1">Comenta seu placar e marca um amigo pra ver se ele bate.</p>'
    out.append(pagina(fmt, "laranja", "QUIZ DA IA", f"{n:02d} / {n:02d}", miolo, None, arroba))
    return out


# reduz a escala do texto até caber no espaço
AJUSTE = """() => { const m = document.getElementById('m'); let s = 1;
  while ((m.scrollHeight > m.clientHeight + 1 || m.scrollWidth > m.clientWidth + 1) && s > 0.5) {
    s -= 0.03; document.body.style.setProperty('--s', s); }
  return s; }"""


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fmt = "instagram" if "--formato" in sys.argv and sys.argv[sys.argv.index("--formato") + 1] == "instagram" else "tiktok"
    if fmt == "instagram" and "instagram" in args:
        args.remove("instagram")
    if "tiktok" in args:
        args.remove("tiktok")
    post = json.loads(pathlib.Path(args[0]).read_text())
    saida = pathlib.Path(args[1])
    saida.mkdir(parents=True, exist_ok=True)
    arroba = post.get("arroba", "@curiosidadesda.iia" if fmt == "tiktok" else "@curiosidadesda.ia")
    htmls = (slides_quiz if post["tipo"] == "quiz" else slides_explica)(post, fmt, arroba)
    H = 1920 if fmt == "tiktok" else 1350
    chrome = "/usr/bin/google-chrome"
    avisos = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=chrome) if os.path.exists(chrome) else pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": H})
        for i, h in enumerate(htmls, 1):
            pg.set_content(h)
            pg.evaluate("document.fonts.ready")
            s = pg.evaluate(AJUSTE)
            if s < 0.75:
                avisos.append(f"slide_{i:02d}: texto reduzido para {s:.2f}x, considere encurtar")
            png = saida / f"slide_{i:02d}.png"
            pg.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": 1080, "height": H})
            Image.open(png).convert("RGB").save(saida / f"slide_{i:02d}.jpg", quality=92)
            png.unlink()
        b.close()
    print(f"{len(htmls)} slides em {saida}")
    for a in avisos:
        print("AVISO:", a)


FONTES_CSS = css_fontes()

if __name__ == "__main__":
    main()
