"""Kit de FUTEBOL 2 (visual caprichado, teste de 14/11/2026). Use em historia.py:
    from kit import *; import kit; from futebol import *; from futebol2 import *

Novidades (tudo genérico, sem escudo/logo/rosto real):
- put_atleta(c, x, pés, altura, f, seed, cores, faixa, arms, expr, run=fase|None, kick=0..1, skin=0..5, hair, hs, num_, gk)
  jogador com proporção de atleta: cabeça menor, ombros largos, manga com punho, gola V, número, calção com
  friso, meião com faixa, chuteira, sombra no chão. braços: hang, up, run, point, shrug, cheek, cintura, joinha,
  aviao, punho. hs (cabelo): curto, raspado, cacheado, topete, careca.
- estadio2('dusk'|'day'|'golden'): estádio com 2 anéis de arquibancada, cobertura curva, refletores com feixe de
  luz, faixa de LED, gramado em perspectiva com corte em listras e linhas do campo. Gramado a partir de y≈1330.
- Ênfase no assunto: foco(c, x, y, r, k) (escurece tudo menos o personagem), rastro(c, ...) da bola,
  linhas_vel(...) de velocidade, rede_estufa(...), confete(...), explosao(c, x, y, f, f0) atrás do "GOL!".
- Em tela (OVERLAY, por cima da câmera): placar_tv(im, ...) estilo transmissão e destaque(im, ...) faixa de
  manchete; use def OVERLAY(im, si, lf) na historia.py (o motor chama depois da cor e antes da legenda).
"""
import math, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from kit import *
import kit
from futebol import *
import futebol as _F

SK2 = [hexc('#ffe0c4'), hexc('#f3c39a'), hexc('#d9a074'), hexc('#b47a50'), hexc('#8a5636'), hexc('#5e3a24')]
BOOT = hexc('#1d1d24')
FONTB = kit.FONT.path


def _seg(a, ang, L):
    return (a[0] + math.sin(ang) * L, a[1] + math.cos(ang) * L)


# ------------------------------------------------------------------ atleta
def atleta(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, run=-1.0, kick=0.0, skin=1, cores=('#ffd84a', '#1f7a4a', '#1d4fa8'),
           faixa=None, hair='#1b1410', hs='curto', num_=None, gk=False, sock=None):
    p = Pen(600, 1000)
    c1, c2, c3 = hexc(cores[0]), hexc(cores[1]), hexc(cores[2])
    sk = SK2[skin]; skd = mul(sk, .8)
    short = c3 if faixa != 'h' else c2
    if cores[0] == cores[2]: short = mul(c1, .75)
    meia = hexc(sock) if sock else (c1 if faixa != 'v' else c3)
    # ---------------- pernas (ângulos a partir do quadril; 0 = para baixo, + = para frente/direita)
    hipY = 690; legs = []
    for s in (-1, 1):
        if run >= 0:
            ph = 2 * math.pi * run + (0 if s > 0 else math.pi)
            a = math.radians(30) * math.sin(ph)
            bend = math.radians(60) * max(0, -math.cos(ph))
        else:
            a, bend = math.radians(3 * s), 0
        if s == 1 and kick > 0:
            a = math.radians(lerp(-35, 70, kick)); bend = math.radians(70 * (1 - kick) * (kick < .55))
        if s == -1 and kick > 0: a = math.radians(-8)
        hip = (300 + s * 44, hipY)
        knee = _seg(hip, a, 125)
        ank = _seg(knee, a - bend, 150)
        legs.append((s, hip, knee, ank, a - bend))
    legs.sort(key=lambda L: 0 if (L[0] == -1) else 1)
    for s, hip, knee, ank, ang in legs:
        p.line([hip, knee], sk, 46, 4)              # coxa
        p.line([knee, ank], meia, 38, 4)            # meião
        band = _seg(knee, ang, 18)
        p.line([band, _seg(knee, ang, 34)], c2 if faixa != 'h' else (255, 255, 255), 38, 0)
        toe = (ank[0] + 34 * math.cos(ang), ank[1] - 34 * math.sin(ang) * .3 + 6)
        p.shape(ell_pts((ank[0] + toe[0]) / 2 + 6, (ank[1] + toe[1]) / 2 + 12, 44, 20, 28, -ang * .8), BOOT, None, 4)
        for k in (-18, 0, 18): p.dot((ank[0] + toe[0]) / 2 + 6 + k, (ank[1] + toe[1]) / 2 + 30, 4, (220, 220, 220))
    # ---------------- calção
    p.shape([(198, 548), (402, 548), (428, 700), (316, 712), (300, 668), (284, 712), (172, 700)], short, mul(short, .8), 5, 14)
    p.poly([(400, 556), (412, 556), (436, 696), (424, 698)], c2 if c2 != short else (255, 255, 255))
    p.poly([(200, 556), (188, 556), (164, 696), (176, 698)], c2 if c2 != short else (255, 255, 255))
    # ---------------- tronco (camisa em V, ombros largos)
    tl = tilt * 4
    torso = curve((176 + tl, 318), (300 + tl, 296), (424 + tl, 318), 10) + curve((440 + tl, 340), (420, 470), (404, 584), 8) + \
        curve((404, 584), (300, 600), (196, 584), 8) + curve((196, 584), (180, 470), (160 + tl, 340), 8)
    p.line([(300 + tl, 250), (300 + tl, 320)], sk, 64, 4)     # pescoço
    p.shape(torso, c1, mul(c1, .78), 5, 20)
    if faixa == 'v':
        for x0 in (214, 300, 386):
            p.poly([(x0 - 16 + tl, 322), (x0 + 16 + tl, 322), (x0 + 14, 586), (x0 - 14, 586)], c2)
    elif faixa == 'h':
        for y0 in (380, 470):
            p.poly([(178, y0), (424, y0), (420, y0 + 40), (182, y0 + 40)], c2)
    p.poly([(262 + tl, 304), (338 + tl, 304), (300 + tl, 360)], sk)             # decote
    p.stroke([(258 + tl, 304), (300 + tl, 364), (342 + tl, 304)], 9, c2 if c2 != c1 else mul(c1, .6))
    if num_:
        fo = ImageFont.truetype(FONTB, 92 * 2); d = ImageDraw.Draw(p.img); tw = d.textlength(num_, font=fo)
        d.text(((300 + tl) * 2 - tw / 2, 400 * 2), num_, font=fo, fill=(255, 255, 255, 255) if sum(c1) < 600 else INK + (255,),
               stroke_width=7, stroke_fill=INK + (255,) if sum(c1) < 600 else (255, 255, 255, 255))
    # ---------------- braços (ombro, cotovelo, mão)
    shL, shR = (176 + tl, 345), (424 + tl, 345)
    if arms == 'run':
        ph = 2 * math.pi * max(run, 0)
        sw = math.sin(ph)
        A = [((150 - 40 * sw, 470), (190 - 70 * sw, 420 + 30 * abs(sw))), ((450 + 40 * sw, 470), (410 + 70 * sw, 420 + 30 * abs(sw)))]
    else:
        A = {'hang': [((150, 470), (150, 590)), ((450, 470), (450, 590))],
             'up': [((112, 240), (100, 120)), ((488, 240), (500, 120))],
             'aviao': [((60, 350), (-5, 360)), ((540, 350), (605, 360))],
             'cheek': [((120, 230), (240, 150)), ((480, 230), (360, 150))],
             'shrug': [((120, 470), (90, 380)), ((480, 470), (510, 380))],
             'point': [((150, 470), (150, 590)), ((520, 300), (595, 255))],
             'cintura': [((112, 450), (196, 560)), ((488, 450), (404, 560))],
             'joinha': [((150, 470), (150, 590)), ((500, 460), (470, 330))],
             'punho': [((150, 470), (150, 590)), ((500, 240), (470, 120))]}[arms]
    for sh, (el, hd) in zip((shL, shR), A):
        p.line([sh, el, hd], sk, 40, 4)                                   # braço inteiro
        se = (sh[0] + (el[0] - sh[0]) * .62, sh[1] + (el[1] - sh[1]) * .62)
        cf = (sh[0] + (el[0] - sh[0]) * .5, sh[1] + (el[1] - sh[1]) * .5)
        p.line([sh, se], c1, 58, 4)                                        # manga
        p.line([cf, se], c2 if c2 != c1 else mul(c1, .7), 50, 0)           # punho da manga
        if gk: p.dot(hd[0], hd[1], 32, hexc('#f2f2f2'), 4)
        else: p.dot(hd[0], hd[1], 26, sk, 4)
        if arms == 'joinha' and sh == shR: p.line([(hd[0], hd[1] - 10), (hd[0], hd[1] - 48)], sk, 14, 4)
    # ---------------- cabeça
    hc = (300 + tilt * 7, 178)
    p.dot(hc[0] - 86, hc[1] + 14, 18, sk, 4); p.dot(hc[0] + 86, hc[1] + 14, 18, sk, 4)
    p.shape(ell_pts(hc[0], hc[1], 92, 96, 56, math.radians(tilt * 1.5), 0.12, 2.3), sk, skd, 5, 14)
    hr = hexc(hair)
    if hs == 'curto':
        p.shape([(x, min(y, hc[1] - 34 + abs(x - hc[0]) * .25)) for x, y in ell_pts(hc[0], hc[1] - 30, 94, 82, 48, 0, 0, 2.2)], hr, mul(hr, .6), 5, 8)
    elif hs == 'raspado':
        p.shape([(x, min(y, hc[1] - 50 + abs(x - hc[0]) * .35)) for x, y in ell_pts(hc[0], hc[1] - 14, 93, 92, 48)], hr, mul(hr, .7), 3, 4)
    elif hs == 'cacheado':
        for i in range(11):
            a = math.pi * (1.05 + .9 * i / 10)
            p.dot(hc[0] + 88 * math.cos(a), hc[1] - 18 + 92 * math.sin(a), 32, hr, 4)
        p.shape(ell_pts(hc[0], hc[1] - 74, 80, 40), hr, None, 0)
    elif hs == 'topete':
        p.shape([(hc[0] - 92, hc[1] - 20), (hc[0] - 80, hc[1] - 80), (hc[0] - 20, hc[1] - 130), (hc[0] + 60, hc[1] - 140),
                 (hc[0] + 96, hc[1] - 90), (hc[0] + 92, hc[1] - 30), (hc[0] + 60, hc[1] - 58), (hc[0] - 60, hc[1] - 58)], hr, mul(hr, .6), 5, 10)
    face(p, hc[0], hc[1] + 8, expr, blink, look, u=2.0)
    return p.img


def put_atleta(c, x, feet, h, f, seed, flip=False, sombra=True, **kw):
    """jogador caprichado. run = fase 0..1 (use (f*.08) % 1 para correr), kick = 0..1 (use pulse)."""
    if h < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    kw['tilt'] = round(1.2 * math.sin((f + seed * 7) * .05) * 2) / 2 + kw.get('tilt', 0)
    if 'run' in kw and kw['run'] is not None and kw['run'] >= 0: kw['run'] = round((kw['run'] % 1) * 12) / 12
    if 'kick' in kw: kw['kick'] = round(kw['kick'] * 8) / 8
    if kw.get('run') is None: kw['run'] = -1.0
    if sombra:
        sh = Image.new('RGBA', (int(h * .62), int(h * .09)), (0, 0, 0, 0))
        ImageDraw.Draw(sh).ellipse([0, 0, sh.size[0] - 1, sh.size[1] - 1], fill=(10, 20, 10, 95))
        sh = sh.filter(ImageFilter.GaussianBlur(h * .012))
        c.alpha_composite(sh, (int(x - sh.size[0] / 2), int(feet - sh.size[1] * .45)))
    bob = .008 * math.sin((f + seed * 11) * .11) * h * (0 if kw.get('run', -1) >= 0 else 1)
    if kw.get('run', -1) >= 0: bob = -abs(math.sin(kw['run'] * 2 * math.pi)) * h * .03
    n = kw.pop('num_', None) if flip else None   # número não pode sair espelhado
    im = sprite('atleta', tuple(sorted(kw.items())), int(h), .6, flip)
    put(c, im, x, feet + h * .025 + bob)
    if n:
        sz = int(92 * h / 1000); cores = kw.get('cores', ('#ffd84a',))
        light = sum(hexc(cores[0])) >= 600
        fo = ImageFont.truetype(FONTB, max(8, sz)); d = ImageDraw.Draw(c)
        tl = kw.get('tilt', 0) * 4 * h / 1000
        cx = x - tl; top = feet + h * .025 + bob - h + 400 * h / 1000
        tw = d.textlength(n, font=fo)
        d.text((cx - tw / 2, top), n, font=fo, fill=INK if light else (255, 255, 255),
               stroke_width=max(1, int(3.5 * h / 1000)), stroke_fill=(255, 255, 255) if light else INK)


# ------------------------------------------------------------------ estádio caprichado
@lru_cache(maxsize=4)
def estadio2(luz='dusk'):
    noite = luz == 'dusk'; gold = luz == 'golden'
    W, H = BW, BH; rnd = random.Random(11)
    out = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    # céu
    top, bot = (('#070c22', '#24356e') if noite else (('#f0a35e', '#ffe0a8') if gold else ('#2f78d6', '#bfe1fa')))
    y = np.linspace(0, 1, 620)[:, None, None]
    g = np.array(hexc(top)) * (1 - y) + np.array(hexc(bot)) * y
    out.paste(Image.fromarray(np.broadcast_to(g, (620, W, 3)).astype(np.uint8)), (0, 0))
    d = ImageDraw.Draw(out)
    if noite:
        for i in range(90):
            x, yy = rnd.random() * W, rnd.random() * 420; r = rnd.choice((1.5, 2, 2.5, 3.5))
            d.ellipse([x - r, yy - r, x + r, yy + r], fill=(255, 255, 230, 255))
    else:
        for i in range(5):
            cx, cy = rnd.uniform(0, W), rnd.uniform(80, 360)
            for k in range(6): r = rnd.uniform(40, 80); d.ellipse([cx + k * 50 - r, cy - r * .6, cx + k * 50 + r, cy + r * .6], fill=(255, 255, 255, 235))
    arcY = lambda x, y0, amp: y0 + amp * ((x - W / 2) / (W / 2)) ** 2
    # arquibancada superior + inferior (multidão)
    stands = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(stands)
    sd.polygon([(x, arcY(x, 470, 70)) for x in range(0, W + 1, 20)] + [(W, 1300), (0, 1300)], fill=(46, 50, 68, 255))
    crowd_cols = ['#ffd84a', '#ffd84a', '#1f7a4a', '#1d3f8f', '#ffffff', '#1d3f8f', '#d4282c', '#ffd84a', '#2a2a36']
    def crowd(y0, y1, r, dark):
        for row, yy in enumerate(np.arange(y0, y1, r * 2.3)):
            for xx in np.arange(-10, W + 20, r * 2.4):
                x = xx + (row % 2) * r * 1.2 + rnd.uniform(-2, 2); yb = yy + 18 * ((x - W / 2) / (W / 2)) ** 2
                col = mul(hexc(rnd.choice(crowd_cols)), dark * rnd.uniform(.8, 1.05))
                sk = mul(SK2[rnd.randrange(6)], dark)
                sd.ellipse([x - r, yb - r * .2, x + r, yb + r * 1.6], fill=col + (255,))          # corpo
                sd.ellipse([x - r * .62, yb - r * 1.3, x + r * .62, yb], fill=sk + (255,))        # cabeça
                if rnd.random() < .08:
                    sd.line([(x + r * .6, yb), (x + r * 1.1, yb - r * 1.8)], fill=sk + (255,), width=max(2, int(r * .35)))
    crowd(560, 830, 8, .7 if noite else .85)
    # faixa de LED entre os anéis
    sd.rectangle([0, 840, W, 900], fill=(16, 18, 28, 255))
    for i in range(0, W, 8):
        t = i / W; col = (int(40 + 60 * t), int(200 - 40 * t), int(120 + 100 * t))
        sd.rectangle([i, 852, i + 6, 888], fill=col + (255,))
    crowd(930, 1250, 11, .85 if noite else 1.0)
    upper = stands.crop((0, 0, W, 840)).filter(ImageFilter.GaussianBlur(1.6))
    stands.paste(upper, (0, 0))
    out.alpha_composite(stands)
    # cobertura curva com luzes
    roof = [(x, arcY(x, 400, 70)) for x in range(0, W + 1, 20)]
    d.polygon(roof + [(x, arcY(x, 500, 70)) for x in range(W, -1, -20)], fill=(22, 24, 34, 255))
    d.line([(x, arcY(x, 500, 70)) for x in range(0, W + 1, 20)], fill=(70, 74, 92, 255), width=8)
    for x in range(30, W, 70):
        yy = arcY(x, 488, 70); d.ellipse([x - 9, yy - 6, x + 9, yy + 6], fill=(255, 250, 220, 255))
    # placas de LED da beira do campo (sem marcas)
    for i, xx in enumerate(range(-40, W, 260)):
        col = [(26, 130, 80), (40, 90, 200), (230, 190, 40), (26, 130, 80), (200, 60, 70)][i % 5]
        d.rectangle([xx, 1262, xx + 256, 1330], fill=col + (255,), outline=(12, 12, 18, 255), width=6)
        for k in range(4): d.polygon([(xx + 30 + k * 55, 1276), (xx + 60 + k * 55, 1296), (xx + 30 + k * 55, 1316)], fill=mul(col, 1.5) + (255,))
    # gramado em perspectiva
    vx, vy = W / 2, 200
    grass = Image.new('RGB', (W, H - 1330)); gd = ImageDraw.Draw(grass)
    base1, base2 = ((48, 128, 64), (60, 148, 74)) if not noite else ((44, 122, 62), (56, 142, 72))
    gd.rectangle([0, 0, W, H], fill=base1)
    n = 14
    for i in range(-n, n + 1):
        if i % 2: continue
        xb0, xb1 = vx + (i - .5) * 230, vx + (i + .5) * 230
        t0 = (1330 - vy) / (H - vy)
        pts = [(vx + (xb0 - vx) * t0, 0), (vx + (xb1 - vx) * t0, 0), (xb1, H - 1330), (xb0, H - 1330)]
        gd.polygon(pts, fill=base2)
    a = np.asarray(grass).astype(np.float32)
    yy = np.linspace(0, 1, a.shape[0])[:, None, None]
    a *= (.78 + .3 * yy)
    a += np.random.default_rng(3).normal(0, 4, a.shape[:2])[..., None]
    grass = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    out.paste(grass, (0, 1330))
    d = ImageDraw.Draw(out)
    d.line([(0, 1345), (W, 1345)], fill=(240, 240, 240, 255), width=7)
    d.arc([W / 2 - 520, 1760, W / 2 + 520, 2120], 180, 360, fill=(235, 235, 235, 200), width=7)
    d.line([(W / 2, 1345), (W / 2, 2208)], fill=(235, 235, 235, 160), width=6)
    # refletores + feixes
    if noite or True:
        beams = Image.new('RGBA', (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(beams)
        for tx, ty, dx in ((120, 330, 1), (W - 120, 330, -1)):
            if noite:
                bd.polygon([(tx - 40, ty + 40), (tx + 40, ty + 40), (tx + dx * 900 + 260, 1900), (tx + dx * 900 - 360, 1900)], fill=(255, 248, 210, 34))
            out_d = ImageDraw.Draw(out)
            out_d.line([(tx, ty + 60), (tx, 560)], fill=(90, 94, 110, 255), width=16)
            out_d.rounded_rectangle([tx - 100, ty - 70, tx + 100, ty + 60], 14, fill=(60, 64, 80, 255), outline=(20, 20, 28, 255), width=6)
            for j in range(3):
                for k in range(4): out_d.ellipse([tx - 82 + k * 44, ty - 52 + j * 36, tx - 50 + k * 44, ty - 24 + j * 36], fill=(255, 250, 215, 255))
        beams = beams.filter(ImageFilter.GaussianBlur(30))
        out.alpha_composite(beams)
        if noite:
            glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd2 = ImageDraw.Draw(glow)
            for tx in (120, W - 120):
                for r, al in ((330, 30), (210, 44), (120, 70)): gd2.ellipse([tx - r, 330 - r, tx + r, 330 + r], fill=(255, 246, 200, al))
            out.alpha_composite(glow.filter(ImageFilter.GaussianBlur(20)))
    # névoa no horizonte
    haze = Image.new('RGBA', (W, 240), (0, 0, 0, 0)); hd = ImageDraw.Draw(haze)
    for i in range(240): hd.line([(0, i), (W, i)], fill=(200, 210, 255, int(40 * (1 - abs(i - 120) / 120))) if noite else (255, 255, 255, int(28 * (1 - abs(i - 120) / 120))))
    out.alpha_composite(haze, (0, 1180))
    return out


# ------------------------------------------------------------------ gol com rede que estufa
def put_gol2(c, x=None, base=None, s=None, estufa=0.0):
    gx, gy = put_gol(c, x, base, s)
    if estufa > 0:
        x = _F.GOL_X if x is None else x; base = _F.GOL_BASE if base is None else base; s = _F.GOL_S if s is None else s
        r = 120 * s * estufa
        im = Image.new('RGBA', (int(r * 2.4) + 4, int(r * 1.6) + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        for k in range(5):
            d.ellipse([k * r * .1, k * r * .08, im.size[0] - k * r * .1, im.size[1] - k * r * .08], outline=(235, 235, 235, 200), width=3)
        paste_c(c, im, gx + 60 * s, gy - 30 * s)
    return gx, gy


# ------------------------------------------------------------------ ênfase
def foco(c, x, y, r, k):
    """holofote: escurece o palco todo menos um círculo em (x, y). k = 0..1 (intensidade)."""
    if k <= .02: return
    W, H = c.size
    m = Image.new('L', (W // 4, H // 4), int(150 * k)); d = ImageDraw.Draw(m)
    d.ellipse([(x - r) / 4, (y - r * 1.25) / 4, (x + r) / 4, (y + r * 1.25) / 4], fill=0)
    m = m.filter(ImageFilter.GaussianBlur(18)).resize((W, H), Image.BILINEAR)
    dark = Image.new('RGBA', (W, H), (8, 6, 20, 255)); dark.putalpha(m)
    c.alpha_composite(dark)


def rastro(c, pts, r, f):
    """rastro da bola: pts = posições anteriores (mais antiga primeiro)."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        a = (i + 1) / (n + 1)
        g = Image.new('RGBA', (int(r * 2.2) + 2, int(r * 2.2) + 2), (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse([0, 0, g.size[0] - 1, g.size[1] - 1], fill=(255, 255, 240, int(110 * a)))
        paste_c(c, g, x, y, .5 + .5 * a)


def linhas_vel(c, x, y, h, f, dir=-1, n=6):
    d = ImageDraw.Draw(c); rnd = random.Random(int(f // 2))
    for i in range(n):
        yy = y - h * (.2 + .6 * rnd.random()); L = h * (.3 + .4 * rnd.random()); x0 = x + dir * h * (.3 + .2 * rnd.random())
        d.line([(x0, yy), (x0 + dir * L, yy)], fill=(255, 255, 255, 170), width=max(3, int(h * .012)))


def confete(c, x, y, f, f0, n=70, spread=600):
    if f < f0: return
    t = f - f0; rnd = random.Random(5); d = ImageDraw.Draw(c)
    cols = [(255, 216, 74), (31, 160, 90), (255, 255, 255), (60, 120, 230), (230, 70, 80)]
    for i in range(n):
        vx = rnd.uniform(-1, 1) * spread / 22; vy = rnd.uniform(-38, -18)
        px = x + vx * t; py = y + vy * t + .9 * t * t
        if py > c.size[1]: continue
        a = t * .3 + i; s = 10 + 6 * rnd.random()
        pts = [(px + s * math.cos(a + k * math.pi / 2) * (1 if k % 2 else .4), py + s * math.sin(a + k * math.pi / 2)) for k in range(4)]
        d.polygon(pts, fill=rnd.choice(cols) + (255,))


@lru_cache(maxsize=4)
def _burst(r, cor):
    im = Image.new('RGBA', (2 * r, 2 * r), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    pts = []
    for i in range(32):
        a = math.pi * i / 16; rr = r if i % 2 == 0 else r * .62
        pts.append((r + rr * math.cos(a), r + rr * math.sin(a)))
    d.polygon(pts, fill=cor + (255,), outline=INK + (255,), width=10)
    return im


def explosao(c, x, y, f, f0, r=330, cor=(255, 216, 74)):
    """estrela de impacto atrás de 'GOL!' (gira devagar)."""
    if f < f0: return
    im = _burst(r, cor).rotate((f - f0) * 1.5, Image.BILINEAR)
    paste_c(c, im, x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ em tela (OVERLAY)
def _font(s): return ImageFont.truetype(FONTB, s)


def placar_tv(im, a, b, ga, gb, ca, cb, minuto='', f=0, pulse_b=-1, pulse_a=-1):
    """placar de transmissão no topo-esquerdo (abaixo do selo). ca/cb = cores (camisa, faixa, calção)."""
    im = im.convert('RGBA'); L = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    x0, y0, h = 60, 196, 86
    fo, fs = _font(44), _font(52)
    wa = d.textlength(a, font=fo); wb = d.textlength(b, font=fo)
    w = 30 + 16 + wa + 30 + 150 + 30 + wb + 16 + 30 + (d.textlength(minuto, font=_font(36)) + 50 if minuto else 0)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 22, fill=(16, 20, 34, 235), outline=(255, 255, 255, 60), width=3)
    x = x0 + 22
    d.rounded_rectangle([x, y0 + 16, x + 14, y0 + h - 16], 6, fill=hexc(ca[0]) + (255,)); x += 26
    d.text((x, y0 + 18), a, font=fo, fill=(255, 255, 255, 255)); x += wa + 22
    sx = x
    d.rounded_rectangle([sx, y0 + 8, sx + 150, y0 + h - 8], 16, fill=(255, 216, 74, 255))
    sc = f'{ga} - {gb}'; tw = d.textlength(sc, font=fs)
    d.text((sx + 75 - tw / 2, y0 + 14), sc, font=fs, fill=INK + (255,))
    x = sx + 150 + 22
    d.text((x, y0 + 18), b, font=fo, fill=(255, 255, 255, 255)); x += wb + 10
    d.rounded_rectangle([x, y0 + 16, x + 14, y0 + h - 16], 6, fill=hexc(cb[0]) + (255,)); x += 30
    if minuto:
        d.rounded_rectangle([x, y0 + 14, x + d.textlength(minuto, font=_font(36)) + 30, y0 + h - 14], 14, fill=(214, 40, 44, 255))
        d.text((x + 15, y0 + 22), minuto, font=_font(36), fill=(255, 255, 255, 255))
    for pf in (pulse_a, pulse_b):
        if pf >= 0 and 0 <= f - pf < 14:
            k = 1 - (f - pf) / 14
            d.rounded_rectangle([sx - 10 * k, y0 + 8 - 10 * k, sx + 150 + 10 * k, y0 + h - 8 + 10 * k], 20, outline=(255, 255, 255, int(255 * k)), width=6)
    s = back(ramp(f, 0, 8)) if f < 10 else 1
    if s < 1:
        L = L.crop((0, 0, im.size[0], y0 + h + 20)); im.alpha_composite(L.resize((L.size[0], L.size[1])), (int(-w * (1 - s)), 0))
    else: im.alpha_composite(L)
    return im.convert('RGB')


def destaque(im, texto, f, f0, sub=None, cor=(255, 216, 74), y=1330):
    """faixa de manchete que entra pela esquerda (ênfase no assunto). Fica acima da legenda."""
    if f < f0: return im
    im = im.convert('RGBA'); fo = _font(70); fs = _font(40)
    d0 = ImageDraw.Draw(im); tw = d0.textlength(texto, font=fo)
    while tw > OW - 200 and fo.size > 44: fo = _font(fo.size - 4); tw = d0.textlength(texto, font=fo)
    w = int(tw + 90); h = 118 + (54 if sub else 0)
    L = Image.new('RGBA', (w + 30, h + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.polygon([(0, 0), (w + 20, 0), (w, h), (0, h)], fill=INK + (240,))
    d.rectangle([0, 0, 22, h], fill=cor + (255,))
    d.text((50, 18), texto, font=fo, fill=(255, 255, 255, 255))
    if sub:
        d.rectangle([22, 118, w - 4, h], fill=cor + (255,))
        d.text((50, 122), sub, font=fs, fill=INK + (255,))
    k = easeOut(ramp(f, f0, f0 + 8))
    im.alpha_composite(L, (int(-L.size[0] + (L.size[0] + 40) * k), y))
    return im.convert('RGB')


P.atleta = atleta   # registra para o cache de sprites do kit
