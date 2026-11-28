"""Formato FÁBULA: "As palavras que pesam" (29/11/2026, 11h). Roteiro do doc nº 3 ("5 Fábulas Emocionantes — Roteiros", do Luis).
Tema: o peso das palavras e a gentileza (mãe). Moral: "Todo mundo carrega uma mochila que você não vê. Uma palavra sua pode deixar ela mais leve."
CTA: "Manda pra sua mãe." Voz ElevenLabs Marcio (eleven_v3) — pedido do Luis em 28/11/2026 — montada com curiosidades/desenho/eleven.py.
Animação mais viva (pedido do Luis em 28/11/2026): gestos (pessoa(..., gesto=)), boca que mexe na fala (boca_fala), sombra no chão, balanço.
Cenas: s0 CAPA close + rua com mochilas | s1 palavras duras -> pedras (balão + mochila) | s2 escola: leve x curvada | s3 recreio, TUM |
s4 devagar / sala de aula / sem rir | s5 mãe leve na cozinha | s6 noite, luz da cozinha (triste) | s7 mãe e a mochila gigante |
s8 pedras do chefe e das contas | s9 escondia no armário | s10 Lipe chega perto | s11 CLOSE Lipe fala | s12 pedra vira poeira dourada |
s13 CLOSE segredo (virada) | s14 abraço (inspiradora) | s15 CLOSE mãe fala | s16 pedra do Lipe some | s17 elogios na escola |
s18 pátio dourado | s19 volta pra casa leve | s20 MORAL."""
from kit import *
import kit
from sombrio import *
from fabula import *
from fabula import _piso, _escuro, _base, _nuvem

CHAVES = ['palavra', 'dura', 'pedra', 'mochila', 'leve', 'curvada', 'sozinho', 'tum', 'devagar', 'rir', 'sorrindo', 'bem', 'luz', 'gigante',
          'chefe', 'contas', 'escondia', 'forte', 'poeira', 'dourada', 'segredo', 'boas', 'tiram', 'corajoso', 'sumiu', 'elogiou', 'arrastando',
          'carrega', 'mais', 'esforcava']
instala_legenda_fab(CHAVES)
MUSICA = True
MUSICA_NIVEL = .14
STING = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+2%'; PITCH = '-2Hz'   # só se precisar voltar para a voz reserva

LINES = [
    "Nesta cidade, toda palavra dura que você ouve vira uma pedra na sua mochila.",
    "Você é burro. Pedra. Ninguém quer jogar com você. Pedra. Para de chorar. Pedra.",
    "Tem criança que chega na escola leve, pulando. E tem criança que chega curvada, arrastando a mochila. E ninguém consegue tirar as pedras sozinho.",
    "Um dia, no recreio, um menino maior riu do Lipe na frente de todo mundo. Tum. Uma pedra caiu dentro da mochila dele.",
    "Depois disso, o Lipe começou a andar mais devagar. Parou de levantar a mão na aula. Parou de rir alto.",
    "Em casa, a mãe parecia sempre leve. Sempre sorrindo. Sempre dizendo que estava tudo bem.",
    "Mas uma noite, o Lipe acordou com sede, e viu a luz da cozinha acesa.",
    "A mãe estava sentada sozinha. E no chão, do lado dela, tinha uma mochila gigante. Maior que a mesa.",
    "Era cheia de pedras. Do chefe. Das contas. De gente que nunca percebeu o quanto ela se esforçava.",
    "Ela só escondia a mochila antes de ele acordar.",
    "O Lipe chegou perto, bem devagar. Ficou um tempo em silêncio. E depois falou baixinho:",
    "Mãe... você é a pessoa mais forte que eu conheço.",
    "Uma pedra saiu flutuando da mochila da mãe. E virou poeira dourada.",
    "Foi aí que o Lipe descobriu o segredo da cidade. Palavras duras colocam pedras. Mas palavras boas tiram.",
    "A mãe, com os olhos cheios d'água, abraçou o filho e disse no ouvido dele:",
    "E você é o menino mais corajoso que eu conheço.",
    "E uma pedra sumiu da mochila do Lipe também.",
    "No dia seguinte, o Lipe elogiou o colega quieto. Elogiou a professora. E elogiou até o menino que riu dele.",
    "E, uma por uma, as pedras da escola foram virando poeira dourada.",
    "Naquele dia, ninguém chegou em casa arrastando a mochila.",
    "Todo mundo carrega uma mochila que você não vê. Uma palavra sua pode deixar ela mais leve.",
]
FALA_TIKTOK = "Manda pra sua mãe."
CTA_TEXTO = "MANDA PRA SUA MÃE"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 13
FLASH = []
CAPA = 36
CHECK = [(0, 'pedra', 6), (0, 'mochila', 10), (1, 'burro', 4), (1, 'pedra', 6), (1, 'ninguem', 6), (1, 'pedra', 8), (1, 'chorar', 2),
         (2, 'leve', 6), (2, 'curvada', 8), (2, 'sozinho', 4), (3, 'riu', 6), (3, 'tum', 6), (3, 'dele', 4), (4, 'devagar', 4), (4, 'aula', 4),
         (4, 'alto', 6), (5, 'sorrindo', 4), (5, 'bem', 4), (6, 'acordou', 4), (6, 'acesa', 6), (7, 'sozinha', 4), (7, 'gigante', 8),
         (8, 'chefe', 6), (8, 'contas', 6), (8, 'esforcava', 4), (9, 'escondia', 6), (10, 'perto', 4), (10, 'baixinho', 4), (11, 'forte', 2),
         (12, 'flutuando', 8), (12, 'dourada', 6), (13, 'segredo', 4), (13, 'tiram', 6), (14, 'abracou', 6), (15, 'corajoso', 2),
         (16, 'sumiu', 10), (17, 'colega', 8), (17, 'professora', 8), (17, 'riu', 8), (18, 'dourada', 6), (19, 'arrastando', 6),
         (20, 'veja', 0) if False else (20, 've', 4), (20, 'leve', 6)]

KIDB = dict(pele='#d9a47a', cabelo='#2a2a2a', penteado='curto', roupa='#5a5f6b', calca='#2f3540')            # o menino maior
KID1 = dict(pele='#f0d0b0', cabelo='#c8902e', penteado='longo', roupa='#d65a8a', calca='#3b4f7a')             # menina leve
KID2 = dict(pele='#8a5a3c', cabelo='#141010', penteado='curto', roupa='#3aa0b0', calca='#5a3a30')             # criança curvada / colega quieto
KID3 = dict(pele='#e4b48c', cabelo='#3a2a20', penteado='curto', roupa='#e08a3a', calca='#4a4036')
PROFA = dict(pele='#c98d62', cabelo='#1e1a18', penteado='coque', roupa='#5aa36f', calca='#3a3a48', oculos=True)
MAE_PIJ = dict(MAE, roupa='#c9a0d8', calca='#8a6aa0')
VERM, AZUL_M, VERDE_M = '#e0473a', '#4d79b3', '#5aa36f'


def TRILHA(SC, N, SR):
    return trilha(SC, N, SR, [(0, 'misteriosa'), (6, 'triste'), (14, 'inspiradora')])


def SFX(s):
    s.thunk(s.W(0, 'pedra') + 6, 120, .5)
    for k in range(3): s.thunk(s.W(1, 'pedra', k) + 4, 110, .55)
    s.patter(s.W(2, 'leve'), s.W(2, 'pulando') + 20, 5, .07)
    s.thunk(s.W(3, 'tum') - 1, 90, .7)
    s.patter(s.W(4, 'andar'), s.W(4, 'devagar') + 20, 3, .05)
    s.ting(s.W(6, 'luz'), .18)
    s.thunk(s.W(7, 'gigante') - 2, 80, .4)
    for w in ('chefe', 'contas'): s.thunk(s.W(8, w) - 2, 140, .35)
    s.thunk(s.W(9, 'escondia') + 10, 160, .3)
    s.trill(s.W(12, 'flutuando'), .6, .06); s.ting(s.W(12, 'poeira'), .3)
    s.ting(s.W(13, 'boas'), .2)
    s.trill(s.W(16, 'sumiu'), .5, .05); s.ting(s.W(16, 'sumiu') + 12, .25)
    for w in ('colega', 'professora'): s.ting(s.W(17, w) + 8, .18)
    s.ting(s.W(17, 'riu') + 8, .22)
    s.ting(s.W(18, 'dourada'), .25)
    s.patter(s.cut(19), s.cut(19) + 60, 7, .06)
    s.ting(s.W(20, 'leve'), .25)


# ---------------------------------------------------------------- pedras e mochilas
@lru_cache(maxsize=16)
def pedra_img(w=120, seed=0, rotulo=''):
    rnd = random.Random(seed)
    p = Pen(400, 340)
    pts = [(200 + 170 * math.cos(a) * rnd.uniform(.85, 1.05), 180 + 140 * math.sin(a) * rnd.uniform(.8, 1.05)) for a in [k * math.pi / 8 for k in range(16)]]
    p.shape(pts, hexc('#9b9ca6'), hexc('#7a7b86'), 8, 18)
    p.shape(ell_pts(150, 120, 50, 26, 16, -.4), hexc('#c3c4cc'), None, 0, 0)
    for _ in range(4):
        x, y = rnd.randint(140, 280), rnd.randint(150, 260); p.dot(x, y, 8, hexc('#868792'))
    im = p.img.resize((400, 340), Image.LANCZOS)
    if rotulo:
        d = ImageDraw.Draw(im); fs = 66
        while d.textlength(rotulo, font=font(F_STAMP, fs)) > 300: fs -= 4
        fnt = font(F_STAMP, fs); tw = d.textlength(rotulo, font=fnt)
        d.text((200 - tw / 2, 180 - fs * .62), rotulo, font=fnt, fill=(255, 246, 226), stroke_width=6, stroke_fill=(36, 24, 34))
    return im.resize((w, int(w * 340 / 400)), Image.LANCZOS)


def put_pedra(c, x, y, w, seed=0, rot=0, rotulo='', alpha=1.0):
    im = pedra_img(int(w // 4 * 4), seed, rotulo)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    if alpha < 1:
        a = im.split()[3].point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def _SX(x, h, sx, flip=False): return x + (-1 if flip else 1) * (sx - 300) * h / 1000
def _SY(feet, h, sy): return feet + .025 * h - h + sy * h / 1000


def mochila_costas(c, x, feet, h, carga=.1, cor=VERM, f=0, seed=1):
    """mochila nas costas (desenhe ANTES da pessoa); carga 0..1 deixa maior e com pedras saindo por cima."""
    bw = h * .27 * (1 + .45 * carga); bh = h * .30 * (1 + .5 * carga)
    top = _SY(feet, h, 470) - h * (.06 + .26 * carga); x0 = x - bw / 2
    d = ImageDraw.Draw(c); col = hexc(cor); dk = mul(col, .78)
    if carga > .25:   # pedras saindo por cima
        n = int(2 + 5 * carga)
        for k in range(n):
            put_pedra(c, x0 + bw * (k + .5) / n, top + 10 - 18 * math.sin(k * 1.7), int(h * .12), seed + k, rot=k * 23)
    d.rounded_rectangle((x0, top, x0 + bw, top + bh), int(bw * .18), fill=col + (255,), outline=INK + (255,), width=max(4, int(h * .008)))
    d.rounded_rectangle((x0 - bw * .06, top + bh * .5, x0 + bw * 1.06, top + bh * .9), int(bw * .1), fill=dk + (255,), outline=INK + (255,), width=max(3, int(h * .006)))


def alcas(c, x, feet, h, cor=VERM, flip=False):
    """alças da mochila por cima da roupa (desenhe DEPOIS da pessoa)."""
    d = ImageDraw.Draw(c); dk = mul(hexc(cor), .7); w = max(5, int(h * .028))
    for sx0, sx1 in ((250, 238), (350, 362)):
        d.line([(_SX(x, h, sx0), _SY(feet, h, 470)), (_SX(x, h, sx1), _SY(feet, h, 650))], fill=dk + (255,), width=w)


@lru_cache(maxsize=8)
def mochila_chao_img(w=600, cor=VERM, pedras=4, rot_seed=0):
    """mochila em pé no chão, aberta em cima com pedras aparecendo. Imagem w x 1.15w."""
    H = int(w * 1.15); im = Image.new('RGBA', (w + 40, H + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    col = hexc(cor); dk = mul(col, .78); ow = max(5, w // 70)
    d.ellipse((30, H - 10, w + 10, H + 30), fill=(30, 20, 30, 70))
    top = int(H * .16)
    if pedras:
        for k in range(pedras):
            pw = int(w * .28); pi = pedra_img(pw // 4 * 4, rot_seed + k)
            im.alpha_composite(pi, (int(40 + (w - 60) * (k + .5) / pedras - pw / 2), int(top - pw * .35 - 10 * (k % 2))))
    d.rounded_rectangle((20, top, w + 20, H), int(w * .2), fill=col + (255,), outline=INK + (255,), width=ow)
    d.ellipse((50, top - w * .08, w - 10, top + w * .1), fill=(60, 30, 30, 255), outline=INK + (255,), width=ow)
    d.rounded_rectangle((20 + w * .18, H * .55, w + 20 - w * .18, H * .9), int(w * .08), fill=dk + (255,), outline=INK + (255,), width=ow)
    d.line((20 + w * .3, H * .63, w + 20 - w * .3, H * .63), fill=(240, 220, 120, 255), width=ow)
    for sx in (.28, .72):
        d.arc((20 + w * sx - w * .12, top - w * .22, 20 + w * sx + w * .12, top + w * .06), 180, 360, fill=mul(col, .6) + (255,), width=ow * 2)
    return im


def mochila_chao(c, x, base, w, cor=VERM, pedras=4, seed=0):
    im = mochila_chao_img(int(w // 8 * 8), cor, pedras, seed)
    c.alpha_composite(im, (int(x - im.width / 2), int(base - im.height + 30)))
    return x, base - im.height + 30 + int(w * 1.15 * .16)   # boca da mochila


def cai_pedra(c, bx, by, f, f0, w=140, seed=0, alto=700):
    """pedra caindo dentro de (bx, by) a partir do quadro f0 (some ao entrar)."""
    t = ramp(f, f0, f0 + 9)
    if 0 < t < 1:
        put_pedra(c, bx, by - alto * (1 - t * t), w, seed, rot=t * 40)
    if f0 + 9 <= f < f0 + 20:
        put_dust(c, bx, by - w * .2, w * .45, f - f0 - 9)


def poeira_dourada(c, x, y, f, f0, r=260, n=26, seed=3):
    """pedra virando poeira dourada a partir de f0 (brilhos subindo e espalhando)."""
    age = f - f0
    if age < 0 or age > 70: return
    rnd = random.Random(seed); d = ImageDraw.Draw(c)
    for k in range(n):
        a = rnd.uniform(0, 2 * math.pi); sp = rnd.uniform(.4, 1.0)
        rr = r * sp * easeOut(age / 40)
        px, py = x + rr * math.cos(a), y + rr * math.sin(a) - age * 3 * sp
        al = clamp(1 - age / 70)
        s_ = rnd.choice((8, 11, 14))
        d.ellipse((px - s_, py - s_, px + s_, py + s_), fill=(255, 214, 90, int(255 * al)))
        if k % 4 == 0: brilho(c, px, py, 26 * al * sp)


def pedra_flutua(c, x, y, f, f0, f1, w=170, seed=5, sobe=420):
    """pedra sai de (x, y) subindo entre f0 e f1 e vira poeira dourada em f1."""
    if f < f0: return
    if f < f1:
        t = smooth(ramp(f, f0, f1)); put_pedra(c, x + 30 * math.sin(f * .2), y - sobe * t, w, seed, rot=12 * math.sin(f * .15))
        brilho(c, x + 80, y - sobe * t - 40, 22 * math.sin(f * .3) ** 2)
    else:
        poeira_dourada(c, x, y - sobe, f, f1, seed=seed)


# ---------------------------------------------------------------- cenários novos
@lru_cache(maxsize=2)
def escola_img():
    W, H = 1900, 1000; p = Pen(W, H)
    p.shape([(60, 260), (W - 60, 260), (W - 60, H), (60, H)], hexc('#f2c6a0'), hexc('#d9a882'), 8, 18)
    p.shape([(20, 270), (W / 2, 40), (W - 20, 270)], hexc('#c0453a'), hexc('#9a3328'), 8, 14)
    for r in range(2):
        for k in range(6):
            x = 160 + k * 280 - (0 if k < 3 else -40); y = 360 + r * 260
            if 760 < x < 1100: continue
            p.shape([(x, y), (x + 170, y), (x + 170, y + 160), (x, y + 160)], hexc('#fbf7ee'), None, 7, 0)
            p.poly([(x + 14, y + 14), (x + 156, y + 14), (x + 156, y + 146), (x + 14, y + 146)], hexc('#bfe3f5'))
    p.shape([(800, 620), (1100, 620), (1100, H), (800, H)], hexc('#5aa36f'), hexc('#3f8a52'), 8, 0)
    p.stroke([(950, 620), (950, H)], 7)
    p.shape([(700, 520), (1200, 520), (1200, 600), (700, 600)], hexc('#4d79b3'), None, 7, 0)
    im = p.img.resize((W, H), Image.LANCZOS); d = ImageDraw.Draw(im)
    fnt = font(F_STAMP, 64); t = 'ESCOLA'; tw = d.textlength(t, font=fnt)
    d.text((950 - tw / 2, 524), t, font=fnt, fill=(255, 246, 226))
    return im


@lru_cache(maxsize=2)
def escola_bg(luz='dia'):
    c = rua_base(luz).copy()
    p = Pen(SW, SH)
    if luz == 'dia': _nuvem(p, 300, 300, .8)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    e = escola_img(); c.alpha_composite(e, (int(1104 - e.width / 2), 1460 - e.height))
    if luz == 'tarde': c.alpha_composite(Image.new('RGBA', c.size, (255, 140, 60, 26)))
    return c


@lru_cache(maxsize=2)
def patio_bg(luz='dia'):
    c = ceu_fab(luz).copy(); p = Pen(SW, SH)
    if luz == 'dia': _nuvem(p, 1600, 260, .8)
    p.shape([(-20, 520), (SW + 20, 520), (SW + 20, 1380), (-20, 1380)], hexc('#e9b48a'), hexc('#d19a70'), 8, 16)   # muro da escola
    for y in range(600, 1380, 90):
        off = 0 if (y // 90) % 2 else 70
        for x in range(-70 + off, SW, 140): p.stroke([(x, y), (x + 120, y)], 4, hexc('#d19a70'))
    for x in (300, 1000, 1700):
        p.shape([(x, 640), (x + 260, 640), (x + 260, 860), (x, 860)], hexc('#fbf7ee'), None, 7, 0)
        p.poly([(x + 16, 656), (x + 244, 656), (x + 244, 844), (x + 16, 844)], hexc('#bfe3f5'))
    p.poly([(0, 1380), (SW, 1380), (SW, SH), (0, SH)], hexc('#d8cfc0'))
    p.stroke([(0, 1380), (SW, 1380)], 8)
    p.stroke([(200, 2100), (700, 1500), (1500, 1500), (2000, 2100)], 9, hexc('#fbf7ee'))
    p.arc(1104, 1760, 260, 90, 0, 360, 9, hexc('#fbf7ee'))
    p.shape([(1900, 1380), (1990, 1380), (1990, 900), (1900, 900)], hexc('#8a5a32'), hexc('#6a4428'), 8, 8)   # árvore
    for dx, dy, r in ((-130, -40, 190), (120, -70, 200), (0, -230, 210)):
        p.dot(1945 + dx, 880 + dy, r + 8, INK)
    for dx, dy, r in ((-130, -40, 190), (120, -70, 200), (0, -230, 210)):
        p.dot(1945 + dx, 880 + dy, r, hexc('#5aa36f'))
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    return _escuro(c, luz)


@lru_cache(maxsize=1)
def banco_frente():
    p = Pen(SW, SH)
    p.shape([(1380, 1560), (1980, 1560), (1980, 1610), (1380, 1610)], hexc('#b07a48'), None, 7, 0)
    for x in (1420, 1940): p.shape([(x - 16, 1610), (x + 16, 1610), (x + 16, 1720), (x - 16, 1720)], hexc('#6a4428'), None, 5, 0)
    return p.img.resize((SW, SH), Image.LANCZOS)


@lru_cache(maxsize=2)
def sala_aula_bg(luz='dia'):
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = _base('#d6e8d0', '#cbdfc4')
    _piso(p, '#c99a62')
    p.shape([(560, 380), (1660, 380), (1660, 1000), (560, 1000)], hexc('#8a5a32'), None, 8, 0)
    p.poly([(590, 410), (1630, 410), (1630, 970), (590, 970)], hexc('#2f6a4a'))
    p.shape([(560, 1000), (1660, 1000), (1660, 1030), (560, 1030)], hexc('#9a6a40'), None, 6, 0)
    p.shape([(100, 450), (440, 450), (440, 900), (100, 900)], hexc('#fbf7ee'), hexc('#ddd6c6'), 7, 8)
    c.alpha_composite(p.img.resize((SW, SH), Image.LANCZOS))
    sky = ceu_fab(luz).crop((120, 250, 420, 680)); c.alpha_composite(sky, (120, 470))
    d = ImageDraw.Draw(c); fnt = font(F_MAO, 96)
    d.text((680, 470), '2 + 2 = 4', font=fnt, fill=(240, 240, 230))
    d.text((680, 640), 'A B C', font=fnt, fill=(240, 240, 230))
    for k in range(5):
        a = k * 1.256; d.line((1450, 600, 1450 + 80 * math.cos(a), 600 + 80 * math.sin(a)), fill=(240, 220, 120), width=8)
    d.ellipse((1410, 560, 1490, 640), outline=(240, 220, 120), width=8)
    relogio(c, 10, 10, 1900, 520, 90)
    return _escuro(c, luz)


CARTEIRAS = (420, 900, 1380, 1860)


@lru_cache(maxsize=1)
def carteiras_frente():
    p = Pen(SW, SH)
    for x in CARTEIRAS:
        p.shape([(x - 200, 1390), (x + 200, 1390), (x + 200, 1430), (x - 200, 1430)], hexc('#d9a05b'), None, 7, 0)
        p.shape([(x - 180, 1428), (x + 180, 1428), (x + 180, 1640), (x - 180, 1640)], hexc('#b07a48'), hexc('#8a5a32'), 7, 10)
    return p.img.resize((SW, SH), Image.LANCZOS)


def sentado_carteira(c, x, f, cores, h=640, **kw):
    pessoa(c, x, 1390 + .3 * h, h, f, cores, sombra=False, **kw)


def avental(c, x, feet, h):
    d = ImageDraw.Draw(c)
    pts = [(_SX(x, h, 240), _SY(feet, h, 540)), (_SX(x, h, 360), _SY(feet, h, 540)), (_SX(x, h, 390), _SY(feet, h, 760)), (_SX(x, h, 210), _SY(feet, h, 760))]
    d.polygon(pts, fill=(250, 246, 232, 255)); d.line(pts + [pts[0]], fill=INK + (255,), width=max(4, int(h * .007)))
    d.line([(_SX(x, h, 245), _SY(feet, h, 545)), (_SX(x, h, 270), _SY(feet, h, 470))], fill=(250, 246, 232, 255), width=max(4, int(h * .012)))
    d.line([(_SX(x, h, 355), _SY(feet, h, 545)), (_SX(x, h, 330), _SY(feet, h, 470))], fill=(250, 246, 232, 255), width=max(4, int(h * .012)))
    for k in range(3):
        cx = _SX(x, h, 260 + k * 40); cy = _SY(feet, h, 680); r = h * .012
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(224, 106, 85, 255))


def porta_quarto(c, luz_on=1.0):
    """porta do quarto do Lipe entreaberta com a luz da cozinha passando por baixo e pela fresta."""
    d = ImageDraw.Draw(c)
    d.rectangle((800, 880, 1030, 1560), fill=(138, 90, 50, 255), outline=INK + (255,), width=8)
    if luz_on > 0:
        g = Image.new('RGBA', c.size, (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        gd.polygon([(1000, 1560), (1030, 1560), (1300, 2200), (900, 2200)], fill=(255, 220, 120, int(110 * luz_on)))
        gd.rectangle((995, 880, 1030, 1560), fill=(255, 226, 140, int(255 * luz_on)))
        c.alpha_composite(g.filter(ImageFilter.GaussianBlur(6)))
    d.ellipse((960, 1200, 985, 1225), fill=(244, 212, 138, 255), outline=INK + (255,), width=4)


def balao(im, t, x, y, s=1.0, size=58):
    """balão de fala (coordenadas da saída) com a frase dura."""
    if s <= .02: return
    fnt = font(F_CAP, size); dd = ImageDraw.Draw(Image.new('L', (1, 1)))
    maxw = V(860, 1300); ws_ = t.split(); linhas = [t]
    if dd.textlength(t, font=fnt) > maxw:
        meio = len(ws_) // 2 + 1; linhas = [' '.join(ws_[:meio]), ' '.join(ws_[meio:])]
    tw = max(dd.textlength(l, font=fnt) for l in linhas)
    w, h = int(tw + 90), int(size * (1.0 + 1.15 * len(linhas)))
    b = Image.new('RGBA', (w + 20, h + 70), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.polygon([(w * .3, h - 6), (w * .45, h - 6), (w * .25, h + 55)], fill=(255, 255, 255, 255), outline=(36, 24, 34, 255))
    d.rounded_rectangle((6, 6, w, h), 40, fill=(255, 255, 255, 255), outline=(36, 24, 34, 255), width=8)
    d.polygon([(w * .3 + 4, h - 10), (w * .45 - 4, h - 10), (w * .26, h + 44)], fill=(255, 255, 255, 255))
    for i, l in enumerate(linhas):
        d.text((48, h / 2 - size * .62 * len(linhas) + i * size * 1.2 + (size * .55 if len(linhas) > 1 else 0) - (size * .5 if len(linhas) > 1 else 0)), l, font=fnt, fill=(200, 50, 40))
    paste_c(im, b, x, y, back(s) if s < 1 else 1)


# ---------------------------------------------------------------- ajudantes de cena
def lipe_mochila(c, x, feet, f, carga=.1, h=KID, cores=LIPE, **kw):
    mochila_costas(c, x, feet, h, carga, VERM, f)
    pessoa(c, x, feet, h, f, cores, seed=2, **kw)
    alcas(c, x, feet, h, VERM)


def kid_mochila(c, x, feet, f, cores, cor=AZUL_M, carga=.1, h=640, seed=4, **kw):
    mochila_costas(c, x, feet, h, carga, cor, f, seed)
    pessoa(c, x, feet, h, f, cores, seed=seed, **kw)
    alcas(c, x, feet, h, cor)


def mae_sentada(c, x, f, cores=MAE_PIJ, expr='preocupado', look=0.0, **kw):
    pessoa(c, x, 1300 + .28 * ADU, ADU, f, cores, seed=3, expr=expr, look=look, sombra=False, **kw)


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:
        c = patio_bg('dia').copy()
        c = close_fab(c, f, 1104, 1200, expr='preocupado', look=0, s=V(.9, .95), dx=V(0, 480), lagrima=.35, **LIPE)
        if HOR:
            for k in range(3): put_pedra(c, 300 + k * 230, 1050 - 40 * (k % 2), 170, k, rot=k * 30)
        else:
            for k in range(3): put_pedra(c, 160 + k * 120, 2120 - 50 * (k % 2), 150, k, rot=k * 30)
        return c, cam_close(f, 1.04, 1.0), 'vivo'
    g = f - CAPA
    pe = wt(0, 'pedra') - 2; mo = wt(0, 'mochila') - 3
    c = rua_fab(f, scroll=g * 9, luz='dia')
    kid_mochila(c, 650, 1790, f, KID1, VERDE_M, .05, walk=1, expr='sorriso', look=.75, seed=5)
    lipe_mochila(c, 1104, 1780, f, .1 + .1 * (f >= pe + 9), walk=1, expr='neutro', look=.75)
    cai_pedra(c, 1104, _SY(1780, KID, 455), f, pe, 110, 1)
    k = easeOut(ramp(f, mo, mo + 14))
    return c, cam(lerp(V(950, 1104), 1104, k), lerp(V(1350, 1250), V(1350, 1300), k), lerp(1.2, 2.0, k) * (1 + .0006 * f), lerp(1.05, 1.6, k) * (1 + .0006 * f)), 'vivo'


INSULTOS = [('voce', 'burro', 'VOCÊ É BURRO.'), ('ninguem', 'voce', 'NINGUÉM QUER JOGAR COM VOCÊ.'), ('para', 'chorar', 'PARA DE CHORAR.')]


def _seg1(f):
    """qual pedaço da frase 1: (k, 'fala'|'pedra', quadro do começo)."""
    marcos = []
    for k, (a, b, _) in enumerate(INSULTOS):
        marcos.append((wt(1, a, 1 if (k == 1 and a == 'voce') else 0) - 3, k, 'fala'))
        marcos.append((wt(1, 'pedra', k) - 3, k, 'pedra'))
    marcos.sort(); cur = (0, 0, 'fala')
    for m in marcos:
        if f >= m[0]: cur = m
    return cur[1], cur[2], cur[0]


def s1(f):
    k, tipo, f0 = _seg1(f)
    g = f - f0
    if tipo == 'fala':
        c = patio_bg('dia').copy()
        quem = [KIDB, KID3, GENTE[3]][k]; h = [820, 700, ADU][k]
        a, b, _ = INSULTOS[k]
        x = 1000
        pessoa(c, x, 1800, h, f, quem, seed=7 + k, expr='desconfiado' if k < 2 else 'preocupado', look=.75,
               boca=boca_fala(1, f, a, b), gesto='aponta' if k < 2 else 'ombros')
        kid_mochila(c, 1560, 1820, f, LIPE, VERM, .1 + .12 * k, expr='preocupado', look=-.75, seed=2)
        return c, cam(lerp(1150, 1250, ramp(g, 0, 40)), V(1350, 1300), (1.45 + .3 * k) * (1 + .002 * g), (1.15 + .15 * k) * (1 + .002 * g), [-2, 2, -2][k]), 'vivo'
    c = patio_bg('dia').copy()
    bx, by = mochila_chao(c, 1104, 1800, 620, VERM, k + 1, 3)
    cai_pedra(c, bx, by, f, f0 + 2, 200, 10 + k, 800)
    kk = kick(f, f0 + 11, 1.0)
    return c, cam(1104, V(1350, 1300) + kk * 14, (2.1 + .1 * k) * (1 + .002 * g), (1.6 + .1 * k) * (1 + .002 * g), kk * 2), 'vivo'


def s2(f):
    cu, so = wt(2, 'curvada') - 3, wt(2, 'sozinho') - 3; ni = wt(2, 'ninguem') - 3
    c = escola_bg('dia').copy()
    if f < cu:
        x = lerp(200, 1300, ramp(f, 0, cu))
        hop = abs(math.sin(f * .25)) * 60
        kid_mochila(c, x, 1790 - hop, f, KID1, VERDE_M, .02, walk=1, expr='sorriso', look=.75, seed=5)
        return c, cam(lerp(V(600, 1104), V(1200, 1104), ramp(f, 0, cu)), V(1300, 1150), 1.3 * (1 + .0008 * f), 1.05 * (1 + .0008 * f)), 'vivo'
    g = f - cu
    x = lerp(300, 900, ramp(g, 0, 160))
    kid_mochila(c, x, 1800, f, KID2, AZUL_M, .9, walk=1, expr='preocupado', look=.5, seed=6, tilt=6)
    if f >= ni:
        k = easeOut(ramp(f, ni, ni + 14))
        return c, cam(x, lerp(V(1350, 1300), 1250, k), lerp(1.35, 2.4, k) * (1 + .001 * g), lerp(1.1, 1.9, k) * (1 + .001 * g)), 'vivo'
    return c, cam(x + 150, V(1350, 1300), 1.35 * (1 + .001 * g), 1.1 * (1 + .001 * g)), 'vivo'


def s3(f):
    ri, tu = wt(3, 'riu') - 3, wt(3, 'tum') - 2
    c = patio_bg('dia').copy()
    rindo = ri <= f < tu + 30
    bo = (.4 + .6 * abs(math.sin(f * .5))) if rindo else 0
    for i, (xx, cr_) in enumerate(((420, KID1), (1820, KID3))):
        kid_mochila(c, xx, 1760, f, cr_, [VERDE_M, AZUL_M][i], .05, expr='sorriso', look=[.5, -.5][i], seed=10 + i, boca=bo * .7)
    pessoa(c, 820, 1800, 840, f, KIDB, seed=7, expr='sorriso' if rindo else 'neutro', look=.75, boca=bo, gesto='aponta' if f >= ri else None)
    carga = .1 + .25 * (f >= tu + 9)
    lipe_mochila(c, 1380, 1810, f, carga, expr='preocupado' if f >= ri else 'neutro', look=-.75)
    cai_pedra(c, 1380, _SY(1810, KID, 455), f, tu, 120, 2, 900)
    kk = kick(f, tu + 9, 1.2)
    if f >= tu:
        z = lerp(1.3, 1.9, easeOut(ramp(f, tu, tu + 10)))
        return c, cam(1380, V(1300, 1250) + kk * 12, z * (1 + .001 * (f - tu)), z * .8 * (1 + .001 * (f - tu)), kk * 3), 'vivo'
    return c, cam(lerp(V(820, 1104), V(1100, 1104), ramp(f, 0, ri + 20)), V(1300, 1200), zf(1.25, f), zf(1.02, f)), 'vivo'


def s4(f):
    au, ri = wt(4, 'levantar') - 3, wt(4, 'rir') - 3
    if f < au:
        c = rua_fab(f, scroll=f * 4, luz='dia')
        lipe_mochila(c, 1104, 1780, f, .4, walk=.6, expr='preocupado', look=.25, tilt=4)
        return c, cam(1104, V(1350, 1250), zf(1.4, f), zf(1.15, f)), 'vivo'
    if f < ri:
        g = f - au
        c = sala_aula_bg('dia').copy()
        for i, (x, cr_) in enumerate(zip(CARTEIRAS, (KID1, LIPE, KID3, KID2))):
            if cr_ is LIPE:
                mochila_costas(c, x, 1390 + .3 * 640, 640, .45, VERM, f)
                sentado_carteira(c, x, f, cr_, expr='preocupado', look=0)
            else:
                sentado_carteira(c, x, f, cr_, expr='sorriso', look=.25, braco_d=round((2.9 + .1 * math.sin(f * .4 + i)) * 10) / 10)
        c.alpha_composite(carteiras_frente())
        return c, cam(lerp(1200, 900, smooth(ramp(g, 0, 60))), V(1150, 1150), (1.3 + .4 * smooth(ramp(g, 0, 60))) * (1 + .001 * g), 1.05 * (1 + .001 * g)), 'vivo'
    g = f - ri
    c = patio_bg('dia').copy()
    for i, (x, cr_) in enumerate(((420, KID1), (760, KID3), (1100, KID2))):
        pessoa(c, x, 1760 - abs(math.sin(f * .3 + i)) * 40, 640, f, cr_, seed=10 + i, expr='sorriso', boca=.5 + .5 * abs(math.sin(f * .45 + i)), gesto='comemora')
    mochila_costas(c, 1680, 1560 + .28 * KID, KID, .45, VERM, f)
    pessoa(c, 1680, 1560 + .28 * KID, KID, f, LIPE, seed=2, expr='preocupado', look=-.75, sombra=False)
    c.alpha_composite(banco_frente())
    return c, cam(lerp(1300, 1600, smooth(ramp(g, 0, 60))), V(1300, 1250), zf(1.4, g, .0015), zf(1.1, g, .0015)), 'vivo'


def s5(f):
    so, be = wt(5, 'sorrindo') - 3, wt(5, 'bem') - 3
    c = jantar_fab('dia').copy()
    pessoa(c, 1000, 1780, ADU, f, MAE, seed=3, expr='sorriso', look=.75, gesto='acena' if f >= so else ('ombros' if f >= be else None))
    avental(c, 1000, 1780, ADU)
    lipe_mochila(c, 1560, 1800, f, .45, expr='neutro', look=-.75)
    k = smooth(ramp(f, be - 10, be + 20))
    return c, cam(lerp(1150, 1050, k), lerp(V(1250, 1200), V(1100, 1050), k), lerp(1.25, 1.7, k) * (1 + .0008 * f), lerp(1.02, 1.35, k) * (1 + .0008 * f)), 'vivo'


def s6(f):
    lu = wt(6, 'luz') - 3; ac = wt(6, 'acordou') - 3
    c = quarto_fab('noite').copy()
    porta_quarto(c, ramp(f, lu - 6, lu + 6))
    pessoa(c, 1860, 1290 + .28 * KID, KID, f, LIPE_PIJAMA, seed=2, expr='curioso' if f >= ac else 'neutro', look=-.75 if f >= lu else 0, sombra=False, blink=0)
    d = ImageDraw.Draw(c); cob = [(1600, 1390), (2110, 1370), (2110, 1575), (1600, 1575)]
    d.polygon(cob, fill=(120, 170, 220, 255)); d.line(cob + [cob[0]], fill=INK + (255,), width=8)
    if f < lu:
        return c, cam(1800, V(1200, 1150), zf(1.6, f), zf(1.3, f)), 'noite_fab'
    k = smooth(ramp(f, lu, lu + 24))
    return c, cam(lerp(1800, 960, k), V(1250, 1200), lerp(1.6, 1.5, k) * (1 + .001 * f), lerp(1.3, 1.2, k)), 'noite_fab'


def cozinha_noite(f, pedras=6, mochila=True, flut=None, mae_expr='preocupado', mae_look=0.0, **kw):
    c = jantar_fab('noite').copy()
    mae_sentada(c, 1104, f, MAE, expr=mae_expr, look=mae_look, **kw)
    c.alpha_composite(mesa_frente())
    boca_ = None
    if mochila: boca_ = mochila_chao(c, 1750, 1840, 760, '#7a5ab0', pedras, 20)
    return c, boca_


def s7(f):
    gi = wt(7, 'gigante') - 3
    c, _ = cozinha_noite(f)
    if f < gi:
        return c, cam(1104, V(1050, 1000), lerp(2.2, 1.9, smooth(ramp(f, 0, gi))), lerp(1.7, 1.5, smooth(ramp(f, 0, gi)))), 'noite_fab'
    k = smooth(ramp(f, gi, gi + 24))
    return c, cam(lerp(1104, 1450, k), lerp(V(1050, 1000), V(1300, 1200), k), lerp(1.9, 1.05, k) * (1 + .0006 * f), lerp(1.5, 1.0, k) * (1 + .0006 * f)), 'noite_fab'


def s8(f):
    ch, co, es = wt(8, 'chefe') - 3, wt(8, 'contas') - 3, wt(8, 'gente') - 3
    c = jantar_fab('noite').copy()
    mae_sentada(c, 1104, f, MAE, expr='preocupado', look=.75)
    c.alpha_composite(mesa_frente())
    bx, by = mochila_chao(c, 1750, 1840, 760, '#7a5ab0', 0, 20)
    for i, (w0, rot) in enumerate(((ch, 'CHEFE'), (co, 'CONTAS'), (es, '?'))):
        s_ = back(ramp(f, w0, w0 + 8)) if f >= w0 else 0
        if s_ > .05:
            put_pedra(c, bx - 230 + i * 230, by - 70 - 60 * (i % 2) - 40 * (1 - s_), int(250 * max(.3, s_)), 30 + i, rot=(-12, 6, 14)[i], rotulo=rot)
    for k in range(4): put_pedra(c, bx - 260 + k * 170, by + 10, 170, 40 + k, rot=k * 20)
    t = smooth(ramp(f, 0, 40))
    return c, cam(lerp(1500, 1700, t), lerp(V(1200, 1150), V(1150, 1100), t), lerp(1.4, 1.9, t) * (1 + .001 * f), lerp(1.2, 1.5, t) * (1 + .001 * f)), 'noite_fab'


def s9(f):
    es = wt(9, 'escondia') - 3
    c = jantar_fab('tarde').copy()
    d = ImageDraw.Draw(c)
    d.rectangle((150, 710, 550, 1550), fill=(40, 26, 20, 255))   # armário aberto
    entra = smooth(ramp(f, es, es + 40))
    x = lerp(900, 380, entra)
    mochila_chao(c, x, 1600, int(lerp(600, 420, entra)), '#7a5ab0', 5, 20)
    porta_w = lerp(0, 380, ramp(f, es + 30, es + 48))
    if porta_w > 4: d.rectangle((550 - porta_w, 700, 550, 1560), fill=(138, 90, 50, 255), outline=INK + (255,), width=8)
    pessoa(c, lerp(1250, 800, entra), 1780, ADU, f, MAE, seed=3, expr='preocupado', look=-.75, gesto='segura', walk=1 if 0 < entra < 1 else 0)
    avental(c, lerp(1250, 800, entra), 1780, ADU)
    return c, cam(lerp(1000, 700, entra), V(1250, 1200), zf(1.35, f), zf(1.1, f)), 'tarde'


def s10(f):
    pe = wt(10, 'perto') - 3; si = wt(10, 'silencio') - 3
    c, _ = cozinha_noite(f, mae_expr='choque' if pe + 10 <= f < si else 'neutro', mae_look=-.75)
    x = lerp(150, 620, smooth(ramp(f, 0, pe + 20)))
    pessoa(c, x, 1800, KID, f, LIPE_PIJAMA, seed=2, walk=.5 if f < pe + 20 else 0, expr='preocupado', look=.75)
    k = smooth(ramp(f, si - 10, si + 30))
    return c, cam(lerp(V(820, 1000), 900, k), V(1250, 1150), lerp(1.25, 1.7, k) * (1 + .0008 * f), lerp(1.05, 1.4, k) * (1 + .0008 * f)), 'noite_fab'


def s11(f):
    c, _ = cozinha_noite(f, mae_look=-.75)
    pessoa(c, 620, 1800, KID, f, LIPE_PIJAMA, seed=2, expr='preocupado', look=.75)
    fo = wt(11, 'forte') - 3
    c = close_fab(c, f, 700, 1300, expr='sorriso' if f >= fo else 'preocupado', look=V(.5, .5), s=V(.95, .95), dx=V(0, -350),
                  boca=boca_fala(11, f), **LIPE_PIJAMA)
    return c, cam_close(f, 1.12, 1.0), 'noite_fab'


def s12(f):
    fl, po = wt(12, 'flutuando') - 6, wt(12, 'poeira') - 3
    c, bm = cozinha_noite(f, pedras=5, mae_expr='choque' if f >= fl else 'neutro', mae_look=.75 if f >= fl else -.75)
    pessoa(c, 620, 1800, KID, f, LIPE_PIJAMA, seed=2, expr='curioso' if f >= fl else 'preocupado', look=.75)
    pedra_flutua(c, bm[0], bm[1], f, fl, po, 200, 50, 520)
    k = smooth(ramp(f, fl, po))
    return c, cam(lerp(1200, 1500, k), lerp(V(1250, 1150), V(1050, 1000), k), lerp(1.2, 1.5, k) * (1 + .0008 * f), lerp(1.02, 1.2, k) * (1 + .0008 * f)), 'noite_fab'


def s13(f):
    se, bo = wt(13, 'segredo') - 3, wt(13, 'boas') - 3
    c, _ = cozinha_noite(f, pedras=4)
    pessoa(c, 620, 1800, KID, f, LIPE_PIJAMA, seed=2, expr='curioso', look=.75)
    for k in range(3): poeira_dourada(c, 700 + k * 300, 1000 + 80 * k, (f + k * 23) % 70, 0, 200, 14, 60 + k)
    c = close_fab(c, f, 800, 1250, expr='sorriso' if f >= bo else 'curioso', look=V(.25, .5), s=V(.95, .95), dx=V(0, 380), **LIPE_PIJAMA)
    d_ = c
    for k in range(6):   # brilhos em volta do rosto
        ph = (f * .04 + k / 6) % 1
        brilho(d_, kit.BW / 2 + V(0, 380) + 420 * math.cos(k + f * .02), kit.BH * .45 + 300 * math.sin(k * 2.1 + f * .02), 40 * math.sin(ph * math.pi))
    return c, cam_close(f, 1.15, 1.0), 'tarde'


def s14(f):
    ab = wt(14, 'abracou') - 3
    c = jantar_fab('noite').copy()
    if f < ab:
        mae_sentada(c, 1104, f, MAE, expr='sorriso', look=-.75)
        c.alpha_composite(mesa_frente())
        pessoa(c, 700, 1800, KID, f, LIPE_PIJAMA, seed=2, expr='sorriso', look=.75)
        return c, cam(950, V(1150, 1100), zf(1.6, f), zf(1.3, f)), 'tarde'
    g = f - ab
    pessoa(c, 1180, 1820, KID, f, LIPE_PIJAMA, seed=2, expr='sorriso', look=-.25, gesto='abraco')
    pessoa(c, 960, 1800, ADU, f, MAE, seed=3, expr='sorriso', look=.5, braco_e=1.6, braco_d=.5)
    for k in range(2): poeira_dourada(c, 1000 + k * 300, 900, (f + k * 31) % 70, 0, 260, 18, 70 + k)
    return c, cam(1080, V(1150, 1100), lerp(1.4, 1.75, smooth(ramp(g, 0, 60))) * (1 + .001 * g), lerp(1.15, 1.4, smooth(ramp(g, 0, 60)))), 'tarde'


def s15(f):
    c = jantar_fab('noite').copy()
    pessoa(c, 960, 1800, ADU, f, MAE, seed=3, expr='sorriso', look=.5)
    c = close_fab(c, f, 960, 1150, expr='sorriso', look=V(0, -.25), s=V(.95, .95), dx=V(0, -380), lagrima=(f / 50) % 1, boca=boca_fala(15, f), **MAE)
    return c, cam_close(f, 1.1, 1.0), 'tarde'


def s16(f):
    su = wt(16, 'sumiu') - 8
    c = quarto_fab('dia').copy()
    carga = .35 if f < su + 30 else .12
    mochila_costas(c, 1104, 1780, KID, carga, VERM, f)
    pessoa(c, 1104, 1780, KID, f, LIPE, seed=2, expr='sorriso' if f >= su + 20 else 'curioso', look=0, gesto='comemora' if f >= su + 30 else None)
    alcas(c, 1104, 1780, KID, VERM)
    top = _SY(1780, KID, 455) - KID * .22 * .35
    pedra_flutua(c, 1104, top, f, su, su + 30, 120, 77, 360)
    return c, cam(1104, V(1250, 1200), lerp(1.5, 1.3, smooth(ramp(f, su, su + 40))) * (1 + .001 * f), 1.15 * (1 + .001 * f)), 'vivo'


def s17(f):
    co, pr, ri = wt(17, 'colega') - 3, wt(17, 'professora') - 3, wt(17, 'menino') - 3
    if f < pr:
        c = patio_bg('dia').copy()
        kid_mochila(c, 900, 1790, f, KID2, AZUL_M, .5 if f < co + 14 else .2, expr='sorriso' if f >= co + 10 else 'preocupado', look=.75, seed=6)
        lipe_mochila(c, 1380, 1800, f, .12, expr='sorriso', look=-.75, gesto='ombros' if f >= co else None, boca=(.5 if (f // 4) % 2 and co <= f < co + 24 else 0))
        poeira_dourada(c, 900, _SY(1790, 640, 400), f, co + 14, 200, 18, 81)
        return c, cam(1140, V(1300, 1250), zf(1.55, f, .0015), zf(1.25, f, .0015)), 'vivo'
    if f < ri:
        g = f - pr
        c = sala_aula_bg('dia').copy()
        pessoa(c, 1200, 1760, ADU, f, PROFA, seed=12, expr='sorriso' if g > 12 else 'neutro', look=-.75, gesto='maos_peito' if g > 12 else None)
        lipe_mochila(c, 800, 1800, f, .12, expr='sorriso', look=.75, boca=(.5 if (f // 4) % 2 and g < 24 else 0))
        poeira_dourada(c, 1200, 1250, f, pr + 14, 220, 18, 82)
        return c, cam(1000, V(1250, 1150), zf(1.4, g, .0015), zf(1.15, g, .0015)), 'vivo'
    g = f - ri
    c = patio_bg('dia').copy()
    pessoa(c, 1250, 1800, 840, f, KIDB, seed=7, expr='choque' if g < 18 else 'sorriso', look=-.75)
    lipe_mochila(c, 820, 1810, f, .12, expr='sorriso', look=.75, gesto='acena', boca=(.5 if (f // 4) % 2 and g < 24 else 0))
    poeira_dourada(c, 1250, 1300, f, ri + 18, 240, 20, 83)
    return c, cam(1050, V(1250, 1200), lerp(1.3, 1.6, smooth(ramp(g, 0, 30))) * (1 + .001 * g), lerp(1.05, 1.3, smooth(ramp(g, 0, 30)))), 'vivo'


def s18(f):
    c = patio_bg('dia').copy()
    pos = ((350, KID1, VERDE_M), (700, KIDB, '#e08a3a'), (1050, LIPE, VERM), (1400, KID2, AZUL_M), (1750, KID3, '#d65a8a'))
    for i, (x, cr_, cor) in enumerate(pos):
        h = 840 if cr_ is KIDB else (KID if cr_ is LIPE else 640)
        y = 1780 - abs(math.sin(f * .22 + i)) * 50
        mochila_costas(c, x, y, h, .03, cor, f, 90 + i)
        pessoa(c, x, y, h, f, cr_, seed=20 + i, expr='sorriso', look=.5 - .25 * i, gesto='comemora' if i % 2 == 0 else 'acena')
        alcas(c, x, y, h, cor)
        poeira_dourada(c, x, y - h * .7, (f + i * 13) % 70, 0, 200, 12, 100 + i)
    t = smooth(ramp(f, 0, 150))
    return c, cam(lerp(V(700, 1104), V(1500, 1104), t), V(1250, 1200), lerp(1.3, 1.15, t), lerp(1.05, 1.0, t) * (1 + .0006 * f)), 'vivo'


def s19(f):
    c = rua_fab(f, scroll=f * 12, luz='tarde')
    kid_mochila(c, 600, 1790 - abs(math.sin(f * .25)) * 50, f, KID1, VERDE_M, .02, walk=1, expr='sorriso', look=.75, seed=5)
    lipe_mochila(c, 1104, 1780 - abs(math.sin(f * .25 + 1)) * 60, f, .03, walk=1, expr='sorriso', look=.75)
    kid_mochila(c, 1600, 1790 - abs(math.sin(f * .25 + 2)) * 50, f, KID2, AZUL_M, .02, walk=1, expr='sorriso', look=.75, seed=6)
    return c, cam(1104, V(1300, 1250), zf(1.25, f), zf(1.02, f)), 'tarde'


def s20(f):
    c = jantar_fab('tarde').copy()
    pessoa(c, 1180, 1820, KID, f, LIPE, seed=2, expr='sorriso', look=-.25, gesto='abraco')
    pessoa(c, 960, 1800, ADU, f, MAE, seed=3, expr='sorriso', look=.5, braco_e=1.6, braco_d=.5)
    avental(c, 960, 1800, ADU)
    mochila_chao(c, 1650, 1800, 300, VERM, 0, 1)
    return c, cam(1104, V(1250, 1150), zf(1.25, f, .0006), zf(1.0, f, .0006)), 'tarde'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]


def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0 and f < CAPA:
        if HOR: capa_txt(im, ['NESTA CIDADE, TODA', '*PALAVRA* *DURA* VIRA', 'UMA *PEDRA*'], size=104, y=200)
        else: capa_txt(im, ['NESTA CIDADE, TODA', '*PALAVRA* *DURA* VIRA', 'UMA *PEDRA* NA MOCHILA'], size=92)
    elif si == 1:
        k, tipo, f0 = _seg1(f)
        if tipo == 'fala': balao(im, INSULTOS[k][2], V(560, 980), V(420, 200), ramp(f, f0, f0 + 6), V(54, 56))
        else: selo_txt(im, 'PEDRA!', V(540, 960), V(330, 140), ramp(f, f0 + 10, f0 + 16), V(84, 80))
    elif si == 3:
        tu = wt(3, 'tum') - 2
        if f >= tu + 9: selo_txt(im, 'TUM!', V(540, 960), V(330, 140), ramp(f, tu + 9, tu + 15), V(96, 90))
    elif si == 6:
        selo_txt(im, '3:00', V(540, 960), V(300, 130), ramp(f, 0, 8), V(64, 60), cor=(77, 121, 179))
    elif si == 13:
        ti = wt(13, 'tiram') - 3
        if f >= wt(13, 'palavras') - 3:
            selo_txt(im, 'PALAVRA BOA TIRA PEDRA' if f >= ti else 'PALAVRA DURA = PEDRA', V(540, 960), V(300, 140), ramp(f, wt(13, 'palavras') - 3, wt(13, 'palavras') + 5), V(64, 64), cor=(214, 150, 40) if f >= ti else (224, 88, 58))
    elif si == 17:
        if f < 60: selo_txt(im, 'NO DIA SEGUINTE', V(540, 960), V(300, 130), ramp(f, 0, 8), V(64, 60), cor=(90, 160, 80))
    elif si == 20:
        um = wt(20, 'uma') - 3
        if HOR: moral_txt(im, ['TODO MUNDO CARREGA UMA MOCHILA', 'QUE VOCÊ NÃO VÊ.'] + (['UMA PALAVRA SUA PODE', 'DEIXAR ELA *MAIS LEVE*.'] if f >= um else []), ramp(f, 0, 8))
        else: moral_txt(im, ['TODO MUNDO', 'CARREGA UMA', 'MOCHILA QUE', 'VOCÊ NÃO VÊ.'] + (['UMA PALAVRA', 'SUA DEIXA ELA', '*MAIS LEVE*.'] if f >= um else []), ramp(f, 0, 8))
    return im.convert('RGB')
