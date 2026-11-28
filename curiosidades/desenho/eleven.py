#!/usr/bin/env python3
"""Narração com a ElevenLabs (pedido do Luis em 28/11/2026), no lugar do edge-tts do `motor.py narrar`.

Fluxo (feito pelo Claude com o conector ElevenLabs, depois este script):
  1. creative_generate_speech: o texto TODO numa chamada só (LINES + FALA_TIKTOK, separadas por linha em branco),
     voz Welliton VtMklhKDP2Y2mBvBbLwL, modelo eleven_multilingual_v2, generations_count 1.
  2. creative_add_flow_asset_node (generation_id) + creative_transcribe_audio (eleven_scribe_v1, connect_from o nó do áudio):
     devolve o tempo de cada palavra (de graça) e um words_download_url.
  3. python3 curiosidades/desenho/eleven.py <pasta> <url_ou_arquivo_mp3> <url_ou_arquivo_words.json>
     -> corta o áudio por frase em <pasta>/voz/l{i}.wav e escreve <pasta>/falas.json (mesmo formato do motor).
     Depois siga normal: stills, render, final.
Se faltar crédito na ElevenLabs (ou falhar 2 vezes), volte para `motor.py narrar` (voz Antonio) — decisão do Luis.
"""
import os, sys, json, re, subprocess, urllib.request, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from kit import _norm

PRE, POS = .06, .10   # folga antes da 1ª palavra e depois da última de cada frase (s)


def baixa(src, dst):
    if re.match(r'https?://', src):
        urllib.request.urlretrieve(src, dst)
    else:
        if os.path.abspath(src) != os.path.abspath(dst):
            import shutil; shutil.copy(src, dst)
    return dst


def main(pasta, mp3, words_json):
    spec = importlib.util.spec_from_file_location('historia', os.path.join(pasta, 'historia.py'))
    linhas = None
    src = open(os.path.join(pasta, 'historia.py')).read()
    ns = {}
    # pega LINES e FALA_TIKTOK sem rodar o resto (que precisa do falas.json)
    for nome in ('LINES', 'FALA_TIKTOK'):
        m = re.search(rf'^{nome}\s*=\s*', src, re.M)
        i = m.end(); depth = 0; j = i
        if src[i] == '[':
            while True:
                c = src[j]
                if c == '[': depth += 1
                elif c == ']':
                    depth -= 1
                    if depth == 0: j += 1; break
                j += 1
        else:
            j = src.index('\n', i)
        ns[nome] = eval(src[i:j])
    linhas = list(ns['LINES']) + [ns['FALA_TIKTOK']]
    os.makedirs(os.path.join(pasta, 'voz'), exist_ok=True)
    full = os.path.join(pasta, 'voz', 'full.mp3'); baixa(mp3, full)
    wj = os.path.join(pasta, 'voz', 'words.json'); baixa(words_json, wj)
    W = json.load(open(wj))
    if isinstance(W, dict): W = W.get('words', W)
    W = [w for w in W if w.get('type', 'word') == 'word']
    wav = os.path.join(pasta, 'voz', 'full.wav')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', full, '-ar', '48000', '-ac', '1', wav], check=True)
    total = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', wav]))
    k = 0; grupos = []
    for li, txt in enumerate(linhas):
        alvo = [x for x in (_norm(p) for p in txt.split()) if x]
        g = []
        for a in alvo:
            # procura a palavra a partir de k (tolerante a 3 palavras fora do lugar)
            hit = next((j for j in range(k, min(len(W), k + 4)) if _norm(W[j]['text']) == a), None)
            if hit is None: raise SystemExit(f'frase {li}: palavra "{a}" não achada perto de "{W[k]["text"] if k < len(W) else "FIM"}"')
            g.append(W[hit]); k = hit + 1
        grupos.append(g)
    out = []
    for li, (txt, g) in enumerate(zip(linhas, grupos)):
        prev_end = grupos[li - 1][-1]['end'] if li else 0.0
        nxt = grupos[li + 1][0]['start'] if li + 1 < len(grupos) else total
        a = max(prev_end + .01, g[0]['start'] - PRE, 0.0)
        b = min(nxt - .01, g[-1]['end'] + POS, total)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-ss', f'{a:.3f}', '-to', f'{b:.3f}', '-af', 'afade=t=in:d=0.02,areverse,afade=t=in:d=0.04,areverse',
                        os.path.join(pasta, 'voz', f'l{li}.wav')], check=True)
        out.append({'text': txt, 'words': [{'w': w['text'].strip('.,:;!?…"\''), 't': round(w['start'] - a, 3), 'd': round(w['end'] - w['start'], 3)} for w in g]})
        print(f"{'cta' if li == len(linhas) - 1 else li}: {b - a:.2f}s  {txt[:70]}")
    json.dump(out, open(os.path.join(pasta, 'falas.json'), 'w'), ensure_ascii=False, indent=1)
    for f in (full, wav): os.remove(f)
    print(f'narração ElevenLabs: {grupos[-2][-1]["end"]:.1f}s de história + fim')


if __name__ == '__main__':
    main(*sys.argv[1:4])
