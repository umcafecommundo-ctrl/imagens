#!/usr/bin/env python3
"""Motor do formato DESENHO (Curiosidades da IA) — desenho animado narrado, 100% em código.

Cada post é uma pasta com um historia.py (veja exemplos/galo/historia.py e o LEIA.md).

  python3 curiosidades/desenho/motor.py narrar  <pasta>   # voz pt-BR-AntonioNeural +15% (edge-tts) e tempos de cada palavra
  python3 curiosidades/desenho/motor.py stills  <pasta>   # folha <pasta>/conferir_cenas.jpg (meio de cada cena + CHECK)
  python3 curiosidades/desenho/motor.py quadro  <pasta> <cena> <quadro_local>   # 1 quadro em <pasta>/quadro.jpg
  python3 curiosidades/desenho/motor.py render  <pasta>   # cenas em vídeo (2 processos) + cena final do TikTok
  python3 curiosidades/desenho/motor.py final   <pasta>   # áudio (voz + música/efeitos baixos), junta, confere:
        -> <pasta>/video_tiktok.mp4 (história + "comenta/segue")  e  <pasta>/video_youtube.mp4 (só a história)
        -> <pasta>/conferir_video.jpg ; apaga scenes/ (voz/ fica, ignorada pelo git)

Áudio: a voz manda. Música ~15 dB abaixo da voz, efeitos ~12 dB abaixo, tudo a -14 LUFS.
"""
import os, sys, json, re, wave, glob, shutil, subprocess, importlib.util, asyncio
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import numpy as np
import kit
from kit import *
from PIL import ImageDraw, ImageFont

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
LEAD, TAIL, END_HOLD = .15, .35, 1.6
ARROBA = '@curiosidadesda.iia'


def load(pasta):
    spec = importlib.util.spec_from_file_location('historia', os.path.join(pasta, 'historia.py'))
    h = importlib.util.module_from_spec(spec); sys.modules['historia'] = h
    fj = os.path.join(pasta, 'falas.json')
    if os.path.exists(fj):
        kit.T.falas = json.load(open(fj)); kit.T.LEAD = LEAD
    spec.loader.exec_module(h)
    return h


# ------------------------------------------------------------------ narração
def narrar(pasta):
    h = load(pasta)
    import edge_tts
    os.makedirs(os.path.join(pasta, 'voz'), exist_ok=True)
    proxy = os.environ.get('HTTPS_PROXY') or None
    linhas = list(h.LINES) + [getattr(h, 'FALA_TIKTOK', 'Você sabia dessa? Comenta aqui, e segue pra mais curiosidades!')]

    async def one(i, text):
        c = edge_tts.Communicate(text, getattr(h, 'VOZ', VOZ), rate=getattr(h, 'RATE', RATE), proxy=proxy, boundary='WordBoundary')
        words = []
        mp3 = os.path.join(pasta, 'voz', f'l{i}.mp3')
        with open(mp3, 'wb') as f:
            async for ch in c.stream():
                if ch['type'] == 'audio': f.write(ch['data'])
                elif ch['type'] == 'WordBoundary': words.append({'w': ch['text'], 't': ch['offset'] / 1e7, 'd': ch['duration'] / 1e7})
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp3, '-ar', '48000', '-ac', '1', mp3[:-4] + '.wav'], check=True)
        os.remove(mp3)
        return {'text': text, 'words': words}

    async def main():
        return [await one(i, t) for i, t in enumerate(linhas)]
    out = asyncio.run(main())
    json.dump(out, open(os.path.join(pasta, 'falas.json'), 'w'), ensure_ascii=False, indent=1)
    tot = 0
    for i, o in enumerate(out):
        w = o['words'][-1]; d = w['t'] + w['d']; tot += d + LEAD + TAIL
        print(f"{'cta' if i == len(out) - 1 else i}: {d:.2f}s  {' '.join(x['w'] for x in o['words'])}")
    print(f'duração aproximada da história: {tot - out[-1]["words"][-1]["t"]:.1f}s (+ fim do TikTok)')


# ------------------------------------------------------------------ tempo e legendas
def timing(h):
    F = kit.T.falas; n = len(h.LINES)
    SC, st = [], 0
    for i in range(n):
        w = F[i]['words'][-1]
        k = round((LEAD + w['t'] + w['d'] + (END_HOLD if i == n - 1 else TAIL)) * FPS)
        SC.append((st, st + k)); st += k
    w = F[n]['words'][-1]
    cta = round((LEAD + w['t'] + w['d'] + .7) * FPS)
    return SC, st, cta


def caps(h):
    F = kit.T.falas; out = []
    txts = list(getattr(h, 'CAPTXT', h.LINES)) + [getattr(h, 'CTA_LEGENDA', None) or F[len(h.LINES)]['text']]
    for si, txt in enumerate(txts):
        tw = F[si]['words']; j = 0
        for phrase in txt.split('|'):
            ws = []
            for cw in phrase.split():
                k = next((k for k in range(j, min(len(tw), j + 7)) if kit._norm(tw[k]['w']) == kit._norm(cw)), None)
                if k is None: k = min(j, len(tw) - 1)
                j = k + 1
                ws.append((cw, round((LEAD + tw[k]['t']) * FPS)))
            out.append((si, ws))
    return out


def selo(h, im):
    """etiqueta fixa no topo (ex.: marca/rótulo). historia.SELO = 'TEXTO', SELO_CORES = (fundo, texto)."""
    t = getattr(h, 'SELO', None)
    if not t: return im
    bg, fg = getattr(h, 'SELO_CORES', ((74, 44, 29), (255, 196, 92)))
    d = ImageDraw.Draw(im); fs = 40; f = ImageFont.truetype(kit.FONT.path, fs)
    while d.textlength(t, font=f) > OW - 110 and fs > 26:  # rótulo longo: diminui a fonte para caber
        fs -= 1; f = ImageFont.truetype(kit.FONT.path, fs)
    w = d.textlength(t, font=f); x0 = (OW - w) / 2 - 28
    d.rounded_rectangle([x0, 92, x0 + w + 56, 160], 34, fill=bg, outline=INK, width=5)
    d.text((x0 + 28, 103 + (40 - fs) / 2), t, font=f, fill=fg)
    return im


def frame(h, SC, CAPS, g, total, cta_len):
    return selo(h, _frame(h, SC, CAPS, g, total, cta_len))


def _frame(h, SC, CAPS, g, total, cta_len):
    n = len(h.LINES)
    if g >= total:  # cena final do TikTok: última cena continua + chamada
        si, lf = n - 1, g - SC[-1][0]; cl = g - total
        c, cam, light = h.SCENES[si](lf)
        im = grade(camera(c, cam), light)
        if getattr(h, 'CTA_CARD', None):  # cartão final próprio (ex.: futebol.py)
            im = h.CTA_CARD(im, cl, h)
            act = [ws for s, ws in CAPS if s == n and cl >= ws[0][1] - 2]
            return draw_caption(im, act[-1], cl) if act else im
        a = Image.new('RGBA', im.size, (0, 0, 0, 0))
        pa = back(ramp(cl, 0, 8))
        if pa > .05:
            ImageDraw.Draw(a).rounded_rectangle([OW / 2 - 470 * pa, 600 - 190 * pa, OW / 2 + 470 * pa, 600 + 190 * pa], 40, fill=(30, 20, 30, 225))
        paste_c(a, txt(getattr(h, 'CTA_TEXTO', 'COMENTA AQUI!'), 96, -4), OW / 2, 540, back(ramp(cl, 2, 10)))
        paste_c(a, txt(getattr(h, 'ARROBA', ARROBA), 60), OW / 2, 690, back(ramp(cl, 8, 16)))
        im = im.convert('RGBA'); im.alpha_composite(a); im = im.convert('RGB')
        act = [ws for s, ws in CAPS if s == n and cl >= ws[0][1] - 2]
        return draw_caption(im, act[-1], cl) if act else im
    si = next(i for i, (a, b) in enumerate(SC) if a <= g < b)
    lf = g - SC[si][0]
    c, cam, light = h.SCENES[si](lf)
    flash = (1 - lf / 6) if (si in getattr(h, 'FLASH', []) and lf < 6) else 0
    im = grade(camera(c, cam), light, flash)
    act = [ws for s, ws in CAPS if s == si and lf >= ws[0][1] - 2]
    return draw_caption(im, act[-1], lf) if act else im


def _render_part(args):
    pasta, name, a, b = args
    h = load(pasta); SC, total, cta = timing(h); CAPS = caps(h)
    tmp = os.path.join(pasta, 'scenes', f'{name}.tmp.mp4'); out = os.path.join(pasta, 'scenes', f'{name}.mp4')
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{OW}x{OH}', '-r', '30', '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
    for g in range(a, b): p.stdin.write(frame(h, SC, CAPS, g, total, cta).tobytes())
    p.stdin.close()
    if p.wait() != 0: raise SystemExit(f'ffmpeg falhou em {name}')
    os.replace(tmp, out); return name


def render(pasta):
    h = load(pasta); SC, total, cta = timing(h)
    os.makedirs(os.path.join(pasta, 'scenes'), exist_ok=True)
    parts = [(pasta, f's{i}', a, b) for i, (a, b) in enumerate(SC)] + [(pasta, 'cta', total, total + cta)]
    parts.sort(key=lambda p: -(p[3] - p[2]))
    from multiprocessing import Pool
    with Pool(2) as pool:
        for nm in pool.imap_unordered(_render_part, parts): print('pronta', nm, flush=True)
    print(f'{total} quadros ({total / FPS:.1f}s) + fim TikTok {cta / FPS:.1f}s')


def stills(pasta):
    h = load(pasta); SC, total, cta = timing(h); CAPS = caps(h)
    gs = [(a + b) // 2 for a, b in SC]
    for si, word, off in getattr(h, 'CHECK', []):
        gs.append(SC[si][0] + wt(si, word) + off)
    gs.append(total + cta - 5); gs = sorted(set(gs))
    ims = [frame(h, SC, CAPS, g, total, cta) for g in gs]
    W, H_ = 270, 480; cols = 6; rows = (len(ims) + cols - 1) // cols
    s = Image.new('RGB', (W * cols, H_ * rows), 'white')
    for i, im in enumerate(ims): s.paste(im.resize((W, H_)), ((i % cols) * W, (i // cols) * H_))
    s.save(os.path.join(pasta, 'conferir_cenas.jpg'), quality=85)
    print('quadros:', gs, '->', os.path.join(pasta, 'conferir_cenas.jpg'))


def quadro(pasta, si, lf):
    h = load(pasta); SC, total, cta = timing(h); CAPS = caps(h)
    frame(h, SC, CAPS, SC[int(si)][0] + int(lf), total, cta).save(os.path.join(pasta, 'quadro.jpg'), quality=90)


# ------------------------------------------------------------------ áudio
SR = 48000


def build_audio(h, SC, total, cta_len, with_cta, pasta):
    N = int((total + (cta_len if with_cta else 0)) / FPS * SR) + 1
    rng = np.random.default_rng(1)
    fr = lambda f: int(f / FPS * SR)
    music = np.zeros(N); sfx = np.zeros(N); voice = np.zeros(N)

    def add(buf, sig, start):
        s = max(0, start); e = min(len(buf), start + len(sig))
        if e > s: buf[s:e] += sig[s - start:e - start]

    def env(n, a=.005, d=.2):
        t = np.arange(n) / SR; return np.minimum(1, t / a) * np.exp(-t / d)

    lp = lambda x, k=8: np.convolve(x, np.ones(k) / k, 'same')

    def pluck(freq, dur, bright=1.0):
        n = int(dur * SR); t = np.arange(n) / SR
        return (np.sign(np.sin(2 * np.pi * freq * t)) * .35 + np.sin(2 * np.pi * freq * t) * .65) * env(n, .003, .12 * bright)

    twist = SC[getattr(h, 'TWIST', len(SC) - 1)][0]
    stop = twist / FPS; beat = 60 / 120
    notes = dict(C=261.63, D=293.66, E=329.63, F=349.23, G=392.0, A=440.0, B=493.88)
    mel = 'E G A G E C D E G E D C D G E C'.split(); bass = [130.81, 98.0, 110.0, 98.0]
    b, i = 0.0, 0
    while b < stop - .01:
        st = int(b * SR)
        if i % 2 == 0:
            n = int(.18 * SR); tt = np.arange(n) / SR
            add(music, np.sin(2 * np.pi * (50 + 90 * np.exp(-tt * 30)) * tt) * env(n, .001, .08) * .9, st)
        else:
            n = int(.15 * SR); add(music, lp(rng.standard_normal(n), 3) * env(n, .001, .05) * .35, st)
        add(music, pluck(bass[(i // 2) % 4], beat * .9, 1.6) * .55, st)
        for k in range(2):
            if (i * 2 + k) % 8 != 7: add(music, pluck(notes[mel[(i * 2 + k) % 16]] * 2, beat / 4 * 1.8) * .28, st + int(k * beat / 2 * SR))
        b += beat; i += 1
    e = int(stop * SR); fs = int(.02 * SR); music[max(0, e - fs):e] *= np.linspace(1, 0, min(fs, e)); music[e:] = 0
    dn = N - fr(twist); td = np.arange(dn) / SR
    add(music, (np.sin(2 * np.pi * 55 * td) + .5 * np.sin(2 * np.pi * 82.4 * td)) * np.minimum(1, td / .6) * np.clip((dn / SR - td) / .4, 0, 1) * .25, fr(twist))

    class S:  # efeitos para historia.SFX(s)
        W = staticmethod(lambda si, w, nth=0: SC[si][0] + wt(si, w, nth))
        cut = staticmethod(lambda si: SC[si][0])
        @staticmethod
        def whoosh(at, dur=.45, g=.5):
            n = int(dur * SR); x = lp(rng.standard_normal(n), 30)
            add(sfx, x * np.sin(np.pi * np.arange(n) / n) ** 2 * g * 3, fr(at) - n // 2)
        @staticmethod
        def thunk(at, f0=180, g=.7):
            n = int(.22 * SR); tt = np.arange(n) / SR
            add(sfx, (np.sin(2 * np.pi * (f0 * np.exp(-tt * 9)) * tt) * env(n, .001, .07) + lp(rng.standard_normal(n), 6) * env(n, .001, .02) * .4) * g, fr(at))
        @staticmethod
        def ting(at, g=.35):
            n = int(.8 * SR); tt = np.arange(n) / SR
            add(sfx, (np.sin(2 * np.pi * 2637 * tt) + .5 * np.sin(2 * np.pi * 3520 * tt)) * env(n, .001, .25) * g, fr(at))
        @staticmethod
        def patter(a, b_, rate=7, g=.18):
            f = a
            while f < b_:
                n = int(.05 * SR); add(sfx, lp(rng.standard_normal(n), 4) * env(n, .001, .012) * g, fr(f)); f += 30 / rate
        @staticmethod
        def engine(a, b_, g=.22):
            n = fr(b_) - fr(a); tt = np.arange(n) / SR
            s_ = lp((np.sin(2 * np.pi * 28 * tt) > .6).astype(float), 40) * (1 + .3 * np.sin(2 * np.pi * 3 * tt))
            add(sfx, (s_ - s_.mean()) * np.minimum(1, np.minimum(tt / .3, (n / SR - tt) / .3)) * g * 2, fr(a))
        @staticmethod
        def trill(at, dur=.9, g=.3):
            n = int(dur * SR); tt = np.arange(n) / SR
            add(sfx, np.sin(2 * np.pi * 2900 * tt) * (np.sin(2 * np.pi * 28 * tt) > 0) * np.minimum(1, (dur - tt) / .1) * g, fr(at))
        @staticmethod
        def splash(at, g=.5):
            n = int(.6 * SR); add(sfx, lp(rng.standard_normal(n), 3) * env(n, .005, .18) * g, fr(at))

    for si in range(1, len(SC)): S.whoosh(SC[si][0], .5, .45)
    if hasattr(h, 'SFX'): h.SFX(S)
    n = int(2.2 * SR); tt = np.arange(n) / SR  # sting na virada
    stab = sum(np.sign(np.sin(2 * np.pi * f * tt)) for f in (110, 130.8, 164.8)) / 3
    add(sfx, np.sin(2 * np.pi * 41 * tt) * env(n, .002, .9) * .9 + lp(rng.standard_normal(n), 5) * env(n, .001, .08) * .6 + lp(stab, 6) * env(n, .01, .35) * .35, fr(twist))
    if with_cta: S.ting(total + 2, .3)

    nL = len(h.LINES)
    for i in range(nL + (1 if with_cta else 0)):
        with wave.open(os.path.join(pasta, 'voz', f'l{i}.wav')) as w:
            v = np.frombuffer(w.readframes(w.getnframes()), np.int16) / 32768
        add(voice, v, fr(SC[i][0] if i < nL else total) + int(LEAD * SR))

    def rms(x): return np.sqrt(np.mean(x ** 2) + 1e-12)
    def gated(x):
        blk = int(.4 * SR); r = np.array([rms(x[k:k + blk]) for k in range(0, len(x) - blk, blk)])
        r = r[r > np.abs(x).max() * 10 ** (-2)]; return np.sqrt(np.mean(r ** 2)) if len(r) else 1e-6
    vg = gated(voice)
    music *= .18 * vg / gated(music); sfx *= .25 * vg / gated(sfx)
    lim = .45 * np.abs(voice).max(); sfx = np.clip(sfx, -lim, lim)
    mix = voice + music + sfx; mix *= .5 / np.abs(mix).max()
    raw = os.path.join(pasta, 'scenes', 'mix_raw.wav')
    with wave.open(raw, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    L = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', subprocess.run(['ffmpeg', '-hide_banner', '-i', raw, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr)[-1])
    out = os.path.join(pasta, 'scenes', 'mix_cta.wav' if with_cta else 'mix.wav')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-af', f'volume={-14 - L:.2f}dB,alimiter=limit=0.89:level=false', '-ar', '48000', out], check=True)
    return out


def final(pasta):
    h = load(pasta); SC, total, cta = timing(h)
    sd = os.path.join(pasta, 'scenes')
    for nm in [f's{i}' for i in range(len(SC))] + ['cta']:
        if not os.path.exists(os.path.join(sd, f'{nm}.mp4')): raise SystemExit(f'falta {nm}.mp4 — rode render')
    for with_cta, name in ((False, 'video_youtube.mp4'), (True, 'video_tiktok.mp4')):
        lst = os.path.join(sd, 'list.txt')
        with open(lst, 'w') as f:
            for i in range(len(SC)): f.write(f"file 's{i}.mp4'\n")
            if with_cta: f.write("file 'cta.mp4'\n")
        vid = os.path.join(sd, 'v.mp4')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', vid], check=True)
        mix = build_audio(h, SC, total, cta, with_cta, pasta)
        out = os.path.join(pasta, name)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', vid, '-i', mix, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
                        '-movflags', '+faststart', out], check=True)
        dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out]))
        qa = subprocess.run(['ffmpeg', '-hide_banner', '-i', out, '-vf', 'freezedetect=n=0.0005:d=0.4,blackdetect', '-an', '-f', 'null', '-'], capture_output=True, text=True).stderr
        prob = re.findall(r'(freeze_start: [\d.]+|black_start:[\d.]+)', qa)
        print(f'{name}: {dur:.1f}s', 'AVISO quadro parado/preto em ' + ', '.join(prob) if prob else 'ok (sem quadro parado ou preto)')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(pasta, 'video_tiktok.mp4'), '-vf', 'fps=1,scale=180:320,tile=8x6', '-frames:v', '1',
                    os.path.join(pasta, 'conferir_video.jpg')], check=True)
    shutil.rmtree(sd, ignore_errors=True)
    # voz/ fica (está no .gitignore) para poder renderizar de novo sem narrar outra vez
    for f in ('quadro.jpg',):
        if os.path.exists(os.path.join(pasta, f)): os.remove(os.path.join(pasta, f))
    print('pronto:', os.path.join(pasta, 'video_tiktok.mp4'), os.path.join(pasta, 'video_youtube.mp4'), os.path.join(pasta, 'conferir_video.jpg'))


if __name__ == '__main__':
    cmd, pasta = sys.argv[1], os.path.abspath(sys.argv[2])
    {'narrar': narrar, 'stills': stills, 'render': render, 'final': final}.get(cmd, lambda p: quadro(p, *sys.argv[3:5]))(pasta)
