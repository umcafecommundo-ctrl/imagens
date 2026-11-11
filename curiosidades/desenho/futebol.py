"""Kit de FUTEBOL do formato DESENHO (página anima.futebol).

Use em historia.py:   from kit import *;  from futebol import *
- placa(nome, cores) / put_placa(...): plaquinha com o nome do time nas cores do clube (NUNCA escudo/logo)
- put_jog(c, x, pés, altura, f, seed, cores=TIME, faixa='v'|'h'|None, arms=..., expr=..., kick=0..1, walk=0..1, skin, hair)
  braços: hang, up, cheek, shrug, point, run, cintura, joinha. Jogador genérico, sem rosto de ninguém real.
- put_bola(c, x, y, r, f), gol(), estadio('dusk'|'day'), trofeu(), calendario('19', 'NOV'), tabela(...), num(...)
- TIMES: cores prontas dos principais clubes (adicione outros em TIMES, sempre só as cores).
"""
from kit import *
import kit

# ------------------------------------------------------------------ cores dos times (sem escudo)
FLU = ('#7a1f3d', '#1f7a4a', '#ffffff')   # grená, verde, branco
VIT = ('#d4282c', '#1b1b1b', '#ffffff')   # vermelho, preto
CRU = ('#1d4fa8', '#ffffff', '#ffffff')   # azul, branco
# (cor da camisa, cor das faixas, cor do calção/faixa do meio) + tipo de faixa
TIMES = {
    'FLAMENGO': (('#c8102e', '#111111', '#ffffff'), 'h'),
    'PALMEIRAS': (('#1b6b3a', '#ffffff', '#ffffff'), None),
    'CORINTHIANS': (('#ffffff', '#111111', '#111111'), None),
    'SÃO PAULO': (('#ffffff', '#c8102e', '#111111'), 'h'),
    'SANTOS': (('#ffffff', '#111111', '#ffffff'), None),
    'VASCO': (('#111111', '#ffffff', '#111111'), 'h'),
    'FLUMINENSE': (FLU, 'v'),
    'BOTAFOGO': (('#111111', '#ffffff', '#111111'), 'v'),
    'GRÊMIO': (('#1e6fbf', '#111111', '#ffffff'), 'v'),
    'INTERNACIONAL': (('#c8102e', '#ffffff', '#ffffff'), None),
    'ATLÉTICO-MG': (('#111111', '#ffffff', '#111111'), 'v'),
    'CRUZEIRO': (CRU, None),
    'BAHIA': (('#ffffff', '#1d4fa8', '#c8102e'), 'h'),
    'VITÓRIA': (VIT, 'h'),
    'FORTALEZA': (('#1d4fa8', '#c8102e', '#ffffff'), 'h'),
    'ATHLETICO-PR': (('#c8102e', '#111111', '#111111'), 'h'),
    'BRAGANTINO': (('#ffffff', '#c8102e', '#ffffff'), None),
    'BRASIL': (('#ffd84a', '#1f7a4a', '#1d4fa8'), None),
    'ARGENTINA': (('#9fd3ff', '#ffffff', '#111111'), 'v'),
    'PORTUGAL': (('#c8102e', '#1f7a4a', '#1f7a4a'), None),
    'REAL MADRID': (('#ffffff', '#f2c94c', '#ffffff'), None),
    'BARCELONA': (('#a50044', '#004d98', '#004d98'), 'v'),
    'ATLÉTICO DE MADRID': (('#d4282c', '#ffffff', '#ffffff'), 'v'),
    'MANCHESTER UNITED': (('#da291c', '#ffffff', '#ffffff'), None),
    'ASTON VILLA': (('#7a1e3f', '#ffffff', '#ffffff'), None),
    'LIVERPOOL': (('#c8102e', '#c8102e', '#c8102e'), None),
    'NOVORIZONTINO': (('#f5c518', '#111111', '#111111'), None),
    'JUVENTUDE': (('#1f7a4a', '#ffffff', '#ffffff'), 'v'),
    'CRICIÚMA': (('#f5c518', '#111111', '#ffffff'), 'v'),
    'INTER MIAMI': (('#f7b5cd', '#111111', '#111111'), None),
    'PSG': (('#0a2a5c', '#d4282c', '#ffffff'), 'v'),
    'MANCHESTER CITY': (('#6cabdd', '#ffffff', '#ffffff'), None),
    'BAYERN': (('#dc052d', '#ffffff', '#ffffff'), None),
    'JAPÃO': (('#1d3f8f', '#ffffff', '#1d3f8f'), None),
    'SINGAPURA': (('#d4282c', '#ffffff', '#ffffff'), None),
    'REMO': (('#0d2a5c', '#ffffff', '#0d2a5c'), None),
    'CHAPECOENSE': (('#1f7a4a', '#ffffff', '#ffffff'), None),
    'MIRASSOL': (('#f5c518', '#1f7a4a', '#1f7a4a'), None),
    'BOCA JUNIORS': (('#0a3a8c', '#f5c518', '#0a3a8c'), 'h'),
    'ESTUDIANTES': (('#d4282c', '#ffffff', '#ffffff'), 'v'),
    'VILA NOVA': (('#d4282c', '#ffffff', '#ffffff'), None),
    'GENÉRICO': (('#555a66', '#555a66', '#555a66'), None),
}


def time_(nome):
    """(cores, faixa) do time pelo nome (TIMES); desconhecido -> cinza genérico."""
    return TIMES.get(nome.upper(), TIMES['GENÉRICO'])


FONTB = kit.FONT.path


# ------------------------------------------------------------------ plaquinha com o nome do time
@lru_cache(maxsize=32)
def placa(nome, cores, size=78):
    """plaquinha arredondada com faixas nas cores do clube e o nome em branco (no lugar do escudo)."""
    S = 2
    f = ImageFont.truetype(FONTB, size * S)
    tw = int(ImageDraw.Draw(Image.new('L', (1, 1))).textlength(nome, font=f))
    w, h = tw + 110 * S, int(size * 1.75) * S
    base = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], h // 3, fill=255)
    fill = Image.new('RGBA', (w, h), hexc(cores[0]) + (255,)); d = ImageDraw.Draw(fill)
    band = max(14 * S, h // 6)
    d.rectangle([0, h - band * 2, w, h - band], fill=hexc(cores[1]) + (255,))
    d.rectangle([0, h - band, w, h], fill=hexc(cores[2]) + (255,) if cores[2] != cores[1] else hexc(cores[0]) + (255,))
    d.rectangle([0, 0, w, band // 2], fill=mul(hexc(cores[0]), 1.25) + (255,))
    base.paste(fill, (0, 0), m)
    ImageDraw.Draw(base).rounded_rectangle([3, 3, w - 4, h - 4], h // 3, outline=INK + (255,), width=7 * S)
    ImageDraw.Draw(base).text(((w - tw) / 2, (h - band * 2) / 2 - size * S * .62), nome, font=f, fill=(255, 255, 255, 255),
                              stroke_width=5 * S, stroke_fill=INK + (255,))
    return base.resize((w // S, h // S), Image.LANCZOS)


def put_placa(c, nome, cores, x, y, f, f0, size=78, rot=0):
    if f < f0: return
    im = placa(nome, cores, size)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y, back(ramp(f, f0, f0 + 8)))


def num(c, s, x, y, f, f0, size=150, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


# ------------------------------------------------------------------ jogador (feijão de chuteira)
def _faixa_v(cx, cy, rx, ry, x0, x1, n=10):
    xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
    hy = lambda x: ry * math.sqrt(max(0, 1 - ((x - cx) / rx) ** 2))
    return [(x, cy - hy(x)) for x in xs] + [(x, cy + hy(x)) for x in reversed(xs)]


def _faixa_h(cx, cy, rx, ry, y0, y1, n=10):
    ys = [y0 + (y1 - y0) * i / (n - 1) for i in range(n)]
    hx = lambda y: rx * math.sqrt(max(0, 1 - ((y - cy) / ry) ** 2))
    return [(cx - hx(y), y) for y in ys] + [(cx + hx(y), y) for y in reversed(ys)]


def jogador(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, walk=0.0, skin=0, cores=FLU, faixa='v',
            hair='#2b1d14', kick=0.0, num_=None):
    """jogador genérico (sem rosto de ninguém real), camisa nas cores do time. 600x1000, pés y≈975."""
    p = Pen(600, 1000)
    c1, c2, c3 = hexc(cores[0]), hexc(cores[1]), hexc(cores[2])
    sk = SKINS[skin]
    short = c3 if faixa == 'v' else c2
    meia = c1
    # pernas (perna direita chuta com kick)
    for s in (-1, 1):
        sw = math.sin(walk * 2 * math.pi) * 40 * s if walk else 0
        lift = max(0, math.sin(walk * 2 * math.pi) * s) * 22 if walk else 0
        top = (300 + s * 34, 690); foot = (300 + s * 40 + sw, 950 - lift)
        if s == 1 and kick:
            foot = (300 + 40 + 190 * kick, 950 - 230 * kick)
        knee = ((top[0] + foot[0]) / 2 + s * 4, (top[1] + foot[1]) / 2 + 10)
        p.line([top, knee], sk, 17, 4)
        p.line([knee, foot], meia, 19, 4)
        p.shape(ell_pts(foot[0] + 14, foot[1] + 8, 36, 17, 28, -kick * .6 if s == 1 else 0), hexc('#1b1b1b'), None, 4)
    # calção
    p.shape([(200, 628), (400, 628), (418, 728), (312, 728), (300, 700), (288, 728), (182, 728)], short, mul(short, .82), 5, 10)
    # camisa
    tc = (300 + tilt * 3, 545); rx, ry = 112, 140
    p.shape([(262, 330), (338, 330), (342, 430), (258, 430)], sk, mul(sk, .85), 5, 8)  # pescoço
    p.shape(ell_pts(tc[0], tc[1], rx, ry, 56, math.radians(tilt), 0.1), c1, mul(c1, .8), 5, 16)
    if faixa == 'v':
        for x0, col in ((tc[0] - 74, c2), (tc[0] - 18, c3), (tc[0] + 38, c2)):
            p.poly(_faixa_v(tc[0], tc[1], rx - 6, ry - 6, x0, x0 + 34), col)
    elif faixa == 'h':
        for y0 in (tc[1] - 70, tc[1] + 10):
            p.poly(_faixa_h(tc[0], tc[1], rx - 6, ry - 6, y0, y0 + 40), c2)
    p.arc(tc[0], tc[1] - ry + 14, 40, 22, 20, 160, 6, mul(c1, .6))  # gola
    if num_:
        f = ImageFont.truetype(FONTB, 70 * 2)
        d = ImageDraw.Draw(p.img); tw = d.textlength(num_, font=f)
        d.text((tc[0] * 2 - tw / 2, (tc[1] - 40) * 2), num_, font=f, fill=(255, 255, 255, 255), stroke_width=8, stroke_fill=INK + (255,))
    # braços
    shL, shR = (205, 460), (395, 460)
    A = {
        'hang': [((185, 560), (190, 650)), ((415, 560), (410, 650))],
        'up': [((150, 330), (175, 190)), ((450, 330), (425, 190))],
        'cheek': [((150, 410), (225, 290)), ((450, 410), (375, 290))],
        'shrug': [((140, 540), (120, 440)), ((460, 540), (480, 440))],
        'point': [((185, 560), (190, 650)), ((470, 430), (560, 400))],
        'run': [((160, 560), (220, 640)), ((450, 520), (470, 420))],
        'cintura': [((120, 560), (215, 655)), ((480, 560), (385, 655))],
        'joinha': [((120, 560), (215, 655)), ((480, 520), (470, 400))],
    }[arms]
    for sh, (el, hd) in zip((shL, shR), A):
        p.line(curve(sh, el, el, 6), c1, 22, 4)
        p.line(curve(el, el, hd, 6), sk, 15, 4)
        p.dot(hd[0], hd[1], 17, sk, 4)
    # cabeça + cabelo
    hc = (300 + tilt * 6, 262)
    p.shape(ell_pts(hc[0], hc[1], 118, 106, 56, math.radians(tilt * 1.5), 0.08, 2.4), sk, mul(sk, .86), 5, 16)
    p.dot(hc[0] - 112, hc[1] + 10, 16, sk, 4); p.dot(hc[0] + 112, hc[1] + 10, 16, sk, 4)
    hr = hexc(hair)
    p.shape([(x, min(y, hc[1] - 40)) for x, y in ell_pts(hc[0], hc[1] - 40, 116, 96, 48, 0, 0, 2.2)], hr, mul(hr, .7), 5, 10)
    face(p, hc[0], hc[1] + 16, expr, blink, look)
    return p.img


def put_jog(c, x, feet, h, f, seed, flip=False, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    kw['tilt'] = round(1.2 * math.sin((f + seed * 7) * .05) * 2) / 2 + kw.get('tilt', 0)
    for k, n in (('walk', 8), ('kick', 6)):
        if k in kw: kw[k] = round(kw[k] * n) / n
    if h < 8: return
    bob = .006 * math.sin((f + seed * 11) * .11) * h
    im = sprite('jogador', tuple(sorted(kw.items())), int(h), .6, flip)
    put(c, im, x, feet + h * .025 + bob)


# ------------------------------------------------------------------ bola, gol, estádio
@lru_cache(maxsize=80)
def bola(r=60, rot=0):
    """bola de futebol clássica (gomos pretos de 5 lados + costuras dos hexágonos brancos), vista de frente.
    rot (graus) gira o desenho. Imagem (2r+20)x(2r+20)."""
    S = 4; R = r * S; W = 2 * R + 20 * S; cx = cy = W / 2
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    pat = Image.new('RGBA', (W, W), (255, 255, 255, 255)); pd = ImageDraw.Draw(pat)
    a0 = math.radians(rot - 90)
    P = lambda ang, dist: (cx + dist * math.cos(ang), cy + dist * math.sin(ang))
    pent = lambda c_, rr, ang: [(c_[0] + rr * math.cos(ang + k * 2 * math.pi / 5), c_[1] + rr * math.sin(ang + k * 2 * math.pi / 5)) for k in range(5)]
    seam = (70, 70, 80, 255); lw = max(2, int(R * .035))
    # pentágono central
    cen = pent((cx, cy), R * .30, a0)
    # costuras: de cada vértice central sai uma linha até o anel, que se divide em duas
    for k in range(5):
        v = cen[k]; ang = a0 + k * 2 * math.pi / 5
        m = P(ang, R * .58)
        pd.line([v, m], fill=seam, width=lw)
        for s_ in (-1, 1):
            e = P(ang + s_ * math.radians(24), R * .80); pd.line([m, e], fill=seam, width=lw)
            pd.line([e, P(ang + s_ * math.radians(24), R * 1.2)], fill=seam, width=lw)
    # 5 pentágonos pretos na borda (entre as costuras), aparecem achatados pela curva da bola
    for k in range(5):
        ang = a0 + (k + .5) * 2 * math.pi / 5
        c_ = P(ang, R * .86)
        pts = pent(c_, R * .25, ang)
        pts = [(cx + (x - cx), cy + (y - cy)) for x, y in pts]
        pd.polygon(pts, fill=(28, 24, 32, 255))
    pd.polygon(cen, fill=(28, 24, 32, 255))
    # recorta no círculo
    m = Image.new('L', (W, W), 0); ImageDraw.Draw(m).ellipse([cx - R, cy - R, cx + R, cy + R], fill=255)
    im.paste(pat, (0, 0), m)
    # sombra de volume (luz de cima à esquerda) + brilho
    sh = Image.new('L', (W, W), 0); sd = ImageDraw.Draw(sh)
    sd.ellipse([cx - R * .75, cy - R * .75, cx + R * 1.35, cy + R * 1.35], fill=0)
    ring = Image.new('L', (W, W), 0); ImageDraw.Draw(ring).ellipse([cx - R, cy - R, cx + R, cy + R], fill=90)
    ImageDraw.Draw(ring).ellipse([cx - R * 1.15, cy - R * 1.15, cx + R * .8, cy + R * .8], fill=0)
    from PIL import ImageFilter, ImageChops
    ring = ImageChops.multiply(ring.filter(ImageFilter.GaussianBlur(R * .12)), m)
    im.paste((40, 40, 70, 255), (0, 0), ring)
    gl = Image.new('L', (W, W), 0); ImageDraw.Draw(gl).ellipse([cx - R * .62, cy - R * .7, cx - R * .25, cy - R * .38], fill=120)
    im.paste((255, 255, 255, 255), (0, 0), ImageChops.multiply(gl.filter(ImageFilter.GaussianBlur(R * .06)), m))
    d = ImageDraw.Draw(im); d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=INK + (255,), width=max(3, int(R * .06)))
    return im.resize((2 * r + 20, 2 * r + 20), Image.LANCZOS)


def raio_bola(h_jogador):
    """raio da bola em proporção REAL com o jogador de altura h (bola 22 cm, pessoa ~1,75 m -> diâmetro ≈ 12% da altura)."""
    return .06 * h_jogador


def put_bola(c, x, y, r=40, f=0):
    """bola centrada em (x, y) com raio r. Para ficar proporcional use r = raio_bola(altura do jogador perto dela);
    no chão, y = pés do jogador - r. Quando ela vai para o gol no fundo, diminua r até ~raio_bola(300)."""
    r = max(4, int(r))
    im = bola(r, int(f * 25) % 72)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(y - im.size[1] / 2)))


@lru_cache(maxsize=2)
def gol():
    p = Pen(520, 420)
    for x in range(40, 500, 34): p.stroke([(x, 40), (x - 20, 400)], 2, hexc('#d9d9d9'))
    for y in range(60, 400, 34): p.stroke([(30, y), (490, y)], 2, hexc('#d9d9d9'))
    p.line([(30, 400), (30, 30), (490, 30), (490, 400)], (255, 255, 255), 16, 5)
    return p.img


@lru_cache(maxsize=4)
def estadio(luz='dusk'):
    """estádio genérico à noite (refletores, arquibancada cheia, gramado listrado). 1242x2208, gramado a partir de y≈1300."""
    noite = luz == 'dusk'
    base = Image.new('RGBA', (BW, BH), (0, 0, 0, 255))
    top, bot = ('#0d1533', '#2f3f78') if noite else ('#3f86dc', '#cfe6f7')
    y = np.linspace(0, 1, 700)[:, None, None]
    g = np.array(hexc(top)) * (1 - y) + np.array(hexc(bot)) * y
    base.paste(Image.fromarray(np.broadcast_to(g, (700, BW, 3)).astype(np.uint8)), (0, 0))
    p = Pen(BW, BH); rnd = random.Random(7)
    if noite:
        for i in range(60): p.dot(rnd.random() * BW, rnd.random() * 520, 2 + rnd.random() * 2, (255, 255, 230))
    # arquibancada
    p.shape([(-20, 620), (BW + 20, 620), (BW + 20, 1270), (-20, 1270)], hexc('#3b3f52'), hexc('#2b2e3d'), 6, 10)
    for yy in range(660, 1270, 64): p.stroke([(0, yy), (BW, yy)], 3, hexc('#2b2e3d'))
    torc = ['#d4282c', '#d4282c', '#1b1b1b', '#d4282c', '#1b1b1b', '#ffffff', '#f2c94c']
    for row, yy in enumerate(range(650, 1250, 32)):
        for xx in range(-10, BW + 20, 30):
            x = xx + (row % 2) * 15 + rnd.uniform(-4, 4)
            col = hexc(rnd.choice(torc))
            if 400 < x < 560 and row < 6: col = hexc(rnd.choice(FLU))   # cantinho da torcida visitante
            p.dot(x, yy + rnd.uniform(-3, 3), 10, col, 2)
    # placas de publicidade lisas (sem marcas)
    for i, xx in enumerate(range(0, BW, 310)):
        col = hexc(['#1f7a4a', '#2a5fb0', '#1f7a4a', '#2a5fb0', '#1f7a4a'][i % 5])
        p.shape([(xx, 1270), (xx + 310, 1270), (xx + 310, 1340), (xx, 1340)], col, mul(col, .8), 5, 6)
    # gramado listrado
    for i, yy in enumerate(range(1340, BH, 120)):
        col = hexc('#3e9b4f') if i % 2 == 0 else hexc('#48ab5a')
        p.poly([(0, yy), (BW, yy), (BW, yy + 120), (0, yy + 120)], col)
    p.stroke([(0, 1340), (BW, 1340)], 6)
    p.stroke([(40, 1420), (BW - 40, 1420)], 8, (245, 245, 245))
    # refletores
    for tx in (110, 1130):
        p.line([(tx, 640), (tx, 160)], hexc('#8a8f9e'), 18, 4)
        p.shape([(tx - 90, 70), (tx + 90, 70), (tx + 90, 170), (tx - 90, 170)], hexc('#5b6070'), None, 5)
        for j in range(3):
            for k in range(4): p.dot(tx - 66 + k * 44, 96 + j * 30, 12, hexc('#fff6c8'), 2)
    out = Image.alpha_composite(base, p.img.resize((BW, BH), Image.LANCZOS))
    if noite:
        glow = Image.new('RGBA', (BW, BH), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
        for tx in (110, 1130):
            for r, a in ((320, 26), (220, 34), (130, 48)): gd.ellipse([tx - r, 120 - r, tx + r, 120 + r], fill=(255, 246, 200, a))
        out.alpha_composite(glow)
    return out



@lru_cache(maxsize=2)
def trofeu():
    """taça genérica dourada (não é a taça real de nenhum torneio). 500x700."""
    p = Pen(500, 700)
    ouro, ouroD = hexc('#f2c94c'), hexc('#c99a2e')
    p.shape([(150, 600), (350, 600), (380, 690), (120, 690)], hexc('#5b3a22'), hexc('#3e2716'), 6, 10)
    p.shape([(215, 420), (285, 420), (300, 600), (200, 600)], ouro, ouroD, 6, 10)
    p.shape(curve((90, 90), (110, 420), (250, 440), 14) + curve((250, 440), (390, 420), (410, 90), 14), ouro, ouroD, 6, 26)
    p.line(curve((95, 130), (10, 170), (110, 300), 10), ouro, 22, 5)
    p.line(curve((405, 130), (490, 170), (390, 300), 10), ouro, 22, 5)
    p.shape(ell_pts(250, 92, 162, 26, 40), hexc('#f7dc7a'), ouroD, 6, 4)
    p.stroke([(170, 160), (190, 330)], 10, (255, 248, 210))
    return p.img.resize((500, 700), Image.LANCZOS)


def calendario(dia, mes='NOV'):
    p = Pen(420, 460)
    p.shape([(20, 60), (400, 60), (400, 440), (20, 440)], (255, 255, 255), hexc('#dcdcdc'), 6, 12)
    p.shape([(20, 60), (400, 60), (400, 160), (20, 160)], hexc('#1f7a4a'), None, 6)
    for x in (110, 310): p.line([(x, 30), (x, 100)], hexc('#8a8f9e'), 14, 4)
    d = ImageDraw.Draw(p.img)
    fo = ImageFont.truetype(FONTB, 150 * 2); tw = d.textlength(dia, font=fo)
    d.text((420 - tw / 2, 200 * 2), dia, font=fo, fill=INK + (255,))
    fo2 = ImageFont.truetype(FONTB, 50 * 2); t = mes; tw = d.textlength(t, font=fo2)
    d.text((420 - tw / 2, 82 * 2), t, font=fo2, fill=(255, 255, 255, 255))
    return p.img.resize((420, 460), Image.LANCZOS)


def tabela(c, linhas, x0, y0, f, f0):
    """linhas: [(pos, nome, cores, pts, destaque)] — tabelinha desenhada."""
    for i, (pos, nome, cores, pts, dest) in enumerate(linhas):
        s = back(ramp(f, f0 + i * 4, f0 + i * 4 + 8))
        if s <= .05: continue
        y = y0 + i * 190
        bgc = (255, 255, 255, 235) if not dest else (255, 236, 160, 245)
        row = Image.new('RGBA', (980, 160), (0, 0, 0, 0)); d = ImageDraw.Draw(row)
        d.rounded_rectangle([4, 4, 975, 155], 40, fill=bgc, outline=INK + (255,), width=7)
        fo = ImageFont.truetype(FONTB, 70)
        d.text((40, 38), pos, font=fo, fill=INK + (255,))
        pl = placa(nome, cores, 54); row.alpha_composite(pl, (170, (160 - pl.size[1]) // 2))
        tw = d.textlength(pts, font=fo); d.text((935 - tw, 38), pts, font=fo, fill=INK + (255,))
        paste_c(c, row, x0, y, s)




# ------------------------------------------------------------------ gol no fundo (proporção certa)
GOL_X, GOL_BASE, GOL_S = 1040, 1590, .74


def put_gol(c, x=None, base=None, s=None):
    """gol mais LONGE, atrás dos jogadores (pés dos jogadores em y≈1950-2030 ficam bem à frente).
    Devolve (x, y) do meio do gol para mirar a bola."""
    x = GOL_X if x is None else x; base = GOL_BASE if base is None else base; s = GOL_S if s is None else s
    g = gol(); h = g.size[1] * s
    paste_c(c, g, x, base - h / 2, s)
    return x + 20, base - h * .45


def put_goleiro(c, f, cores, faixa, gx=None, base=None, **kw):
    """goleiro/zagueiro pequeno dentro do gol (longe), para dar profundidade."""
    gx = GOL_X if gx is None else gx; base = GOL_BASE if base is None else base
    put_jog(c, gx - 40, base + 10, 300, f, 21, cores=cores, faixa=faixa, **kw)


# ------------------------------------------------------------------ cartão final (chamada) da página
def cta_card(im, cl, h):
    """escurece o fundo e mostra um cartão verde com a pergunta (CTA_TEXTO) e "SIGA PARA MAIS". Sem @."""
    import numpy as np
    from PIL import ImageFilter
    k = clamp(cl / 8)
    if k > 0: im = im.filter(ImageFilter.GaussianBlur(9 * k))
    a = np.asarray(im).astype(np.float32) * (1 - .6 * k)
    im = Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    pa = back(ramp(cl, 0, 9))
    if pa > .05:
        w, hh = 900, 560; cx, cy = OW / 2, 760
        card = Image.new('RGBA', (w, hh), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
        d.rounded_rectangle([6, 6, w - 6, hh - 6], 56, fill=(22, 92, 52, 245), outline=INK + (255,), width=10)
        d.rounded_rectangle([22, 22, w - 22, hh - 22], 44, outline=(255, 216, 74, 255), width=8)
        b = bola(60, int(cl * 12) % 72).resize((150, 150), Image.LANCZOS)
        card.alpha_composite(b, (w // 2 - 75, 40))
        t = txt(getattr(h, 'CTA_TEXTO', 'COMENTA AQUI!'), 104, 0)
        if t.size[0] > w - 60: t = t.resize((w - 60, int(t.size[1] * (w - 60) / t.size[0])), Image.LANCZOS)
        card.alpha_composite(t, ((w - t.size[0]) // 2, 210))
        s2 = back(ramp(cl, 8, 16))
        if s2 > .05:
            pill = Image.new('RGBA', (640, 120), (0, 0, 0, 0)); pd = ImageDraw.Draw(pill)
            pd.rounded_rectangle([4, 4, 636, 116], 58, fill=(255, 216, 74, 255), outline=INK + (255,), width=7)
            fo = ImageFont.truetype(FONTB, 60); tx = 'SIGA PARA MAIS'; tw = pd.textlength(tx, font=fo)
            pd.text(((640 - tw) / 2, 24), tx, font=fo, fill=INK + (255,))
            pill = pill.resize((max(1, int(640 * s2)), max(1, int(120 * s2))), Image.LANCZOS)
            card.alpha_composite(pill, ((w - pill.size[0]) // 2, 400 + (120 - pill.size[1]) // 2))
        card = card.resize((max(1, int(w * pa)), max(1, int(hh * pa))), Image.LANCZOS)
        im.alpha_composite(card, (int(cx - card.size[0] / 2), int(cy - card.size[1] / 2)))
    return im.convert('RGB')


CTA_CARD = cta_card
