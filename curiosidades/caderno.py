"""Layout "caderno" da página Curiosidades da IA (TikTok, 1080x1920).

Papel quadriculado com textura, marca-texto nas palavras de destaque,
anotações à mão em caneta azul, cartões com fita adesiva e resposta do
quiz circulada. Usa o mesmo JSON do layout padrão, com campos opcionais
"nota" (comentário à mão) na capa, nos slides, nas perguntas e nas respostas.
"""
import base64, html, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
FONTES = AQUI / "fonts"

INK = "#151413"
PAPER = "#F2ECDF"
ORANGE = "#FF6A13"
PEN = "#1F4FC9"
CINZA = "#4A4740"


def e(t):
    return html.escape(str(t or ""))


def _du(nome):
    return "data:font/woff2;base64," + base64.b64encode((FONTES / nome).read_bytes()).decode()


FONTES_CSS = (
    f"@font-face{{font-family:Anton;src:url({_du('anton.woff2')})}}"
    + "".join(f"@font-face{{font-family:Inter;font-weight:{w};src:url({_du(f'inter-{w}.woff2')})}}" for w in (400, 600, 800))
    + f"@font-face{{font-family:Caveat;font-weight:700;src:url({_du('caveat-700.woff2')})}}"
    + f"@font-face{{font-family:Marker;src:url({_du('marker.woff2')})}}"
)

CSS = f"""
{FONTES_CSS}
*{{box-sizing:border-box}}
body{{margin:0;width:1080px;height:1920px;overflow:hidden;font-family:Inter,sans-serif;color:{INK};background:{PAPER};--s:1}}
.paper{{position:absolute;inset:0;background-image:linear-gradient(rgba(31,79,201,.10) 2px,transparent 2px),linear-gradient(90deg,rgba(31,79,201,.10) 2px,transparent 2px);background-size:60px 60px;background-position:-2px -2px}}
.grain{{position:absolute;inset:0;opacity:.55;mix-blend-mode:multiply}}
.pg{{position:absolute;inset:0;padding:170px 150px 400px 90px;display:flex;flex-direction:column;gap:30px}}
.top{{display:flex;justify-content:space-between;align-items:center;flex:none}}
.tag{{font-family:Marker,cursive;font-size:34px;background:{INK};color:{PAPER};padding:10px 22px;transform:rotate(-2deg)}}
.pgn{{font-family:Caveat,cursive;font-weight:700;font-size:58px;color:{PEN}}}
.miolo{{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:calc(var(--s)*44px);overflow:hidden;padding:24px 30px 24px 10px;margin:-24px -30px -24px -10px}}
.rod{{flex:none;font-family:Caveat,cursive;font-weight:700;font-size:58px;color:{PEN}}}
.hand{{font-family:Caveat,cursive;font-weight:700;color:{PEN};margin:0}}
h1,h2{{font-family:Anton,sans-serif;font-weight:400;text-transform:uppercase;line-height:1.14;margin:0;padding-top:.06em}}
.h1{{font-size:calc(var(--s)*160px)}}
.h2{{font-size:calc(var(--s)*104px)}}
.hl{{display:inline-block;position:relative;z-index:0;padding:0 .1em}}
.hl::before{{content:"";position:absolute;z-index:-1;left:0;right:0;top:.1em;bottom:.12em;background:{ORANGE};transform:rotate(-1.4deg);border-radius:.05em .12em .06em .1em}}
.nw{{white-space:nowrap}}
.t1{{font-size:calc(var(--s)*42px);font-weight:800;line-height:1.35;margin:0}}
.t2{{font-size:calc(var(--s)*36px);line-height:1.45;margin:0;color:{CINZA}}}
.num{{font-family:Marker,cursive;font-size:calc(var(--s)*120px);line-height:1.1;color:{ORANGE};transform:rotate(-3deg);align-self:flex-start}}
.card{{position:relative;background:#FFFDF8;border-radius:6px;padding:calc(var(--s)*52px) 52px;display:flex;flex-direction:column;gap:calc(var(--s)*28px);box-shadow:0 2px 0 rgba(0,0,0,.04),0 18px 40px -18px rgba(40,30,10,.35)}}
.tape{{position:absolute;width:190px;height:58px;background:rgba(236,220,170,.78);box-shadow:0 1px 2px rgba(0,0,0,.08)}}
.stamp{{position:absolute;border:6px solid {ORANGE};color:{ORANGE};border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Marker,cursive;line-height:1.05}}
.op{{background:#FFFDF8;border-radius:6px;padding:calc(var(--s)*30px) 40px;font-size:calc(var(--s)*48px);font-weight:800;box-shadow:0 2px 0 rgba(0,0,0,.04),0 14px 30px -16px rgba(40,30,10,.35)}}
.op b{{font-family:Marker,cursive;font-weight:400;color:{ORANGE};margin-right:26px}}
.post{{background:#FFE58A;padding:calc(var(--s)*24px) 28px;display:flex;flex-direction:column;gap:4px;box-shadow:0 12px 24px -14px rgba(40,30,10,.4)}}
.post i{{font-style:normal;font-family:Marker,cursive;font-size:calc(var(--s)*60px);color:{INK}}}
.post span{{font-family:Caveat,cursive;font-weight:700;font-size:calc(var(--s)*44px);line-height:1.05;color:{INK}}}
.arroba{{flex:none;align-self:flex-start;font-family:Marker,cursive;font-size:46px;background:{INK};color:{PAPER};padding:18px 34px;transform:rotate(-1.5deg)}}
.lista{{display:flex;flex-direction:column;gap:calc(var(--s)*14px)}}
.lista span{{font-family:Caveat,cursive;font-weight:700;font-size:calc(var(--s)*56px);color:{PEN}}}
"""

GRAIN = """<svg class="grain" width="1080" height="1920" aria-hidden="true"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .45  0 0 0 0 .38  0 0 0 0 .25  0 0 0 .22 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>"""

SETA = f"""<svg aria-hidden="true" width="150" height="90" viewBox="0 0 200 120" fill="none" stroke="{PEN}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" style="flex:none;transform:rotate(215deg)"><path d="M8 20 C 60 10, 120 30, 168 92"/><path d="M140 88 L170 96 L176 64"/></svg>"""

CIRCULO = f"""<svg aria-hidden="true" style="position:absolute;left:-7%;top:-18%;width:114%;height:136%" viewBox="0 0 400 140" preserveAspectRatio="none" fill="none" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round" vector-effect="non-scaling-stroke"><path vector-effect="non-scaling-stroke" d="M60 22 C 150 2, 330 4, 380 40 C 418 70, 360 124, 210 130 C 80 136, 8 110, 14 70 C 20 34, 90 18, 170 14"/></svg>"""


def carimbo(txt):
    return f'<div class="stamp" style="position:relative;flex:none;width:210px;height:210px;font-size:{30 if max(len(w) for w in txt.split("<br>")) > 6 else 36}px;transform:rotate(10deg)">{txt}</div>'


def titulo(tag, cls, t, d, fim=""):
    """Título com marca-texto em cada palavra do destaque; a pontuação final fica colada."""
    t = e(t)
    if not d:
        return f'<{tag} class="{cls}">{t}{e(fim)}</{tag}>'
    ws = e(d).split()
    # pontuação no fim do destaque (ex.: "humano?") fica fora do grifo
    pont = ""
    while ws and ws[-1] and ws[-1][-1] in "?!.,:;":
        pont = ws[-1][-1] + pont
        ws[-1] = ws[-1][:-1]
    partes = [f'<span class="hl">{w}</span>' for w in ws if w]
    if partes:
        partes[-1] = f'<span class="nw">{partes[-1]}{pont}{e(fim)}</span>'
    return f'<{tag} class="{cls}">{t} {" ".join(partes)}</{tag}>'


def pagina(rotulo, contador, miolo, rodape=None, arroba=None):
    rod = f'<div class="rod">{rodape}</div>' if rodape else ""
    arr = f'<div class="arroba">{e(arroba)}</div>' if arroba else ""
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="paper"></div>{GRAIN}
<div class="pg"><div class="top"><span class="tag">{e(rotulo)}</span><span class="pgn">{e(contador)}</span></div>
<div class="miolo" id="m">{miolo}</div>{rod}{arr}</div></body></html>"""


def nota_com_seta(n):
    if not n:
        return ""
    return f'<div style="display:flex;align-items:flex-start;gap:18px;padding-left:30px">{SETA}<p class="hand" style="font-size:calc(var(--s)*62px);line-height:1.05;transform:rotate(-3deg);padding-top:30px">{e(n)}</p></div>'


ROT = [-1.5, 1.2, -0.8, 1.6, -1.2, 0.9]
TAPES = [
    '<div class="tape" style="left:-36px;top:-22px;transform:rotate(-28deg)"></div><div class="tape" style="right:-30px;bottom:-20px;transform:rotate(-24deg)"></div>',
    '<div class="tape" style="left:40%;top:-28px;transform:rotate(3deg)"></div>',
    '<div class="tape" style="right:-34px;top:-20px;transform:rotate(26deg)"></div><div class="tape" style="left:-30px;bottom:-22px;transform:rotate(22deg)"></div>',
]


def slides_explica(p, arroba):
    corpo = p["slides"]
    n = len(corpo) + 2
    rot = p.get("rotulo", "CURIOSIDADE")
    out = []
    c = p["capa"]
    selo = e(c.get("selo", "VOCÊ SABIA?")).replace(" ", "<br>", 1)
    nota = f'<p class="hand" style="font-size:calc(var(--s)*64px);line-height:1.05;transform:rotate(-3deg);flex:1">{e(c["nota"])}</p>' if c.get("nota") else '<span style="flex:1"></span>'
    miolo = f'<div style="display:flex;align-items:center;gap:24px">{nota}{carimbo(selo)}</div>'
    miolo += titulo("h1", "h1", c["titulo"], c.get("destaque"))
    if c.get("sub"):
        miolo += f'<p class="t1" style="font-weight:600;max-width:800px">{e(c["sub"])}</p>'
    out.append(pagina("CURIOSIDADES DA IA", f"1/{n}", miolo, "arrasta pro lado →"))
    for i, s in enumerate(corpo):
        card = TAPES[i % len(TAPES)]
        if s.get("numero"):
            card += f'<div class="num">{e(s["numero"])}</div>'
        card += titulo("h2", "h2", s["titulo"], s.get("destaque"))
        if s.get("texto"):
            card += f'<p class="t1">{e(s["texto"])}</p>'
        if s.get("extra"):
            card += f'<p class="t2">{e(s["extra"])}</p>'
        miolo = f'<div class="card" style="transform:rotate({ROT[i % len(ROT)]}deg)">{card}</div>' + nota_com_seta(s.get("nota"))
        out.append(pagina(rot, f"{i + 2}/{n}", miolo, "continua →"))
    f = p.get("final", {})
    acoes = f.get("acoes") or ["Salva pra mostrar pra alguém", "Manda pra um amigo curioso", "Segue pra mais curiosidades"]
    miolo = titulo("h2", "h1", f.get("titulo", "Você sabia disso?"), f.get("destaque"))
    miolo += f'<p class="t1">{e(f.get("texto", "Comenta qual curiosidade te surpreendeu mais."))}</p>'
    miolo += '<div class="lista">' + "".join(f"<span>☐ {e(a)}</span>" for a in acoes) + "</div>"
    out.append(pagina(rot, f"{n}/{n}", miolo, None, arroba))
    return out


def slides_quiz(p, arroba):
    qs = p["perguntas"]
    n = 2 + 2 * len(qs)
    out = []
    c = p["capa"]
    selo = e(c.get("selo", f"{len(qs)} PERGUNTAS"))
    curto, _, tema = selo.partition(" · ")
    nota = c.get("nota") or (tema.capitalize() if tema else "")
    nota = f'<p class="hand" style="font-size:calc(var(--s)*64px);line-height:1.05;transform:rotate(-3deg);flex:1">{nota}</p>' if nota else '<span style="flex:1"></span>'
    miolo = f'<div style="display:flex;align-items:center;gap:24px">{nota}{carimbo(curto.replace(" ", "<br>", 1))}</div>'
    miolo += titulo("h1", "h1", c["titulo"], c.get("destaque"))
    miolo += f'<p class="t1" style="font-weight:600">{e(c.get("sub", "Responde de cabeça, sem pesquisar. A resposta vem no slide seguinte."))}</p>'
    out.append(pagina("QUIZ DA IA", f"1/{n}", miolo, "valendo! arrasta →"))
    letras = "ABCD"
    for i, q in enumerate(qs):
        k = 2 + 2 * i
        miolo = titulo("h2", "h2", q["pergunta"], q.get("destaque"))
        miolo += '<div style="display:flex;flex-direction:column;gap:calc(var(--s)*28px)">' + "".join(
            f'<div class="op" style="transform:rotate({ROT[j % len(ROT)] * .6}deg)"><b>{letras[j]}</b>{e(o)}</div>' for j, o in enumerate(q["opcoes"])) + "</div>"
        miolo += f'<p class="hand" style="font-size:calc(var(--s)*62px);transform:rotate(-3deg)">{e(q.get("nota", "sem pesquisar, hein!"))}</p>'
        out.append(pagina(f"QUIZ · {i + 1} DE {len(qs)}", f"{k}/{n}", miolo, "pensou? arrasta →"))
        cert = q["certa"]
        resp = f'{letras[cert]} - {q["opcoes"][cert]}'
        miolo = f'<div style="display:flex;flex-direction:column;align-items:flex-start;gap:8px;padding:40px 30px 0 40px"><div style="position:relative">{CIRCULO}<h2 class="h2" style="font-size:calc(var(--s)*96px);position:relative">{e(resp)}</h2></div>'
        miolo += f'<p class="hand" style="font-size:calc(var(--s)*62px);transform:rotate(-4deg);white-space:nowrap;align-self:flex-end;padding-top:24px">{e(q.get("nota_resposta", "acertou?"))}</p></div>'
        card = TAPES[1] + f'<p class="t1">{e(q["explicacao"])}</p>'
        if q.get("extra"):
            card += f'<p class="t2">{e(q["extra"])}</p>'
        miolo += f'<div class="card" style="transform:rotate(1deg)">{card}</div>'
        prox = "ver seu resultado →" if i == len(qs) - 1 else ("última pergunta →" if i == len(qs) - 2 else "próxima pergunta →")
        out.append(pagina(f"RESPOSTA {i + 1}", f"{k + 1}/{n}", miolo, prox))
    pl = p.get("placar") or ["Segue a página, urgente", "Tá no caminho", "Mandou bem", "Gênio. Prova nos comentários"]
    miolo = '<h2 class="h1">Quantas você <span class="nw"><span class="hl">acertou</span>?</span></h2>'
    miolo += '<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px">' + "".join(
        f'<div class="post" style="transform:rotate({ROT[j] * 1.2}deg)"><i>{j}</i><span>{e(t)}</span></div>' for j, t in enumerate(pl)) + "</div>"
    miolo += '<p class="t1">Comenta seu placar e marca um amigo pra ver se ele bate.</p>'
    out.append(pagina("QUIZ DA IA", f"{n}/{n}", miolo, None, arroba))
    return out
