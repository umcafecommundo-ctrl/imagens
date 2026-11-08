"""Formato DESENHO: para que servem os três quadrados do QR code (Curiosidades da IA, 08/11/2026, 18h). Categoria: TECNOLOGIA.
Fatos: Wikipedia "QR code" (inventado em 1994 pela Denso Wave, empresa japonesa de peças de automóvel, para rastrear tipos e
quantidades de peças; um só rótulo substituiu os vários códigos de barras que eram lidos em cada caixa; três padrões de
posição, quadrados concêntricos, nos cantos superior esquerdo, superior direito e inferior esquerdo; a proporção 1:1:3:1:1
foi escolhida por ser a sequência de áreas pretas e brancas menos usada em impressos); Keyence, "What is a QR code?"
(os padrões de posição permitem ler o código de qualquer direção; correção de erro: até 7%, 15%, 25% ou 30% do código
pode estar estragado, conforme o nível; criado pela Denso Wave em 1994)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10c', '2026-11-08-10h')
pessoa = _h10.pessoa

LINES = [
    "Os três quadrados nos cantos do QR code não estão ali de enfeite.",
    "O QR code nasceu no Japão, em mil novecentos e noventa e quatro, numa empresa de peças de carro.",
    "Cada caixa da fábrica tinha vários códigos de barras, e era um bipe atrás do outro.",
    "Os três quadrados mostram pro leitor onde está o código e como ele está virado. Dá pra ler de qualquer lado.",
    "E o desenho deles foi escolhido de propósito: é a sequência de preto e branco que menos aparece em coisas impressas.",
    "Você vê, por isso a câmera não confunde o QR code com mais nada. E ele funciona até com trinta por cento estragado.",
    "Ou seja: o quadradinho que você usa pra ver o cardápio... foi feito pra contar peça de carro.",
]
CAPTXT = [
    "Os três quadrados nos cantos do QR code|não estão ali de enfeite.",
    "O QR code nasceu no Japão, em 1994,|numa empresa de peças de carro.",
    "Cada caixa da fábrica tinha vários códigos de barras,|e era um bipe atrás do outro.",
    "Os três quadrados mostram pro leitor onde está o código e como ele está virado.|Dá pra ler de qualquer lado.",
    "E o desenho deles foi escolhido de propósito:|é a sequência de preto e branco que menos aparece em coisas impressas.",
    "Você vê, por isso a câmera não confunde o QR code com mais nada.|E ele funciona até com 30% estragado.",
    "Ou seja: o quadradinho que você usa pra ver o cardápio...|foi feito pra contar peça de carro.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [1, 6]
CHECK = [(0, 'quadrados', 4), (0, 'enfeite', 6), (1, 'japao', 4), (1, 'carro', 6), (2, 'barras', 4), (2, 'outro', 6),
         (3, 'virado', 4), (3, 'lado', 6), (4, 'proposito', 4), (4, 'impressas', 6), (5, 'confunde', 4), (5, 'estragado', 6),
         (6, 'cardapio', 4), (6, 'carro', 8)]


# ------------------------------------------------------------------ objetos novos
def qr(seed=1, eyes=0, look=0.0, glow=0, dano=0, blink=0):
    """QR code 21x21 desenhado (600x600). eyes = olhinhos nos 3 quadrados; glow = destaca os quadrados; dano = mancha/rasgo."""
    N = 21; m = 600 / (N + 4)
    p = Pen(600, 600)
    p.shape([(0, 0), (600, 0), (600, 600), (0, 600)], (255, 255, 255), hexc('#e6e6e6'), 6, 8)
    rnd = random.Random(seed)
    finder = set()
    for (fx, fy) in ((0, 0), (N - 7, 0), (0, N - 7)):
        for i in range(-1, 8):
            for j in range(-1, 8): finder.add((fx + i, fy + j))
    for i in range(N):
        for j in range(N):
            if (i, j) in finder: continue
            if rnd.random() < .5:
                x, y = (i + 2) * m, (j + 2) * m
                p.poly([(x, y), (x + m + .5, y), (x + m + .5, y + m + .5), (x, y + m + .5)], INK)
    for (fx, fy) in ((0, 0), (N - 7, 0), (0, N - 7)):
        x0, y0 = (fx + 2) * m, (fy + 2) * m
        if glow:
            p.poly([(x0 - m * .8, y0 - m * .8), (x0 + 7.8 * m, y0 - m * .8), (x0 + 7.8 * m, y0 + 7.8 * m), (x0 - m * .8, y0 + 7.8 * m)], hexc('#ffd84a'))
            p.poly([(x0 - m * .2, y0 - m * .2), (x0 + 7.2 * m, y0 - m * .2), (x0 + 7.2 * m, y0 + 7.2 * m), (x0 - m * .2, y0 + 7.2 * m)], (255, 255, 255))
        p.poly([(x0, y0), (x0 + 7 * m, y0), (x0 + 7 * m, y0 + 7 * m), (x0, y0 + 7 * m)], INK)
        p.poly([(x0 + m, y0 + m), (x0 + 6 * m, y0 + m), (x0 + 6 * m, y0 + 6 * m), (x0 + m, y0 + 6 * m)], (255, 255, 255))
        if eyes:
            cx, cy = x0 + 3.5 * m, y0 + 3.5 * m
            if blink: p.stroke([(cx - 1.4 * m, cy), (cx + 1.4 * m, cy)], 10)
            else:
                p.dot(cx, cy, 1.9 * m, (255, 255, 255)); p.dot(cx + look * .6 * m, cy, 1.1 * m, INK)
                p.dot(cx + look * .6 * m - .3 * m, cy - .3 * m, .3 * m, (255, 255, 255))
        else:
            p.poly([(x0 + 2 * m, y0 + 2 * m), (x0 + 5 * m, y0 + 2 * m), (x0 + 5 * m, y0 + 5 * m), (x0 + 2 * m, y0 + 5 * m)], INK)
    if dano:
        p.shape([(330, 330), (600, 300), (600, 600), (300, 600), (360, 470)], hexc('#8a5f35'), hexc('#65452a'), 0, 10)
        p.stroke([(330, 330), (600, 300)], 6); p.stroke([(330, 330), (360, 470), (300, 600)], 6)
    return p.img


def put_qr(c, x, y, size, f=0, seed=1, rot=0, **kw):
    if 'eyes' in kw: kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'look' in kw: kw['look'] = round(kw['look'] * 2) / 2
    im = sprite('qr', tuple(sorted(dict(seed=seed, **kw).items())), int(size), 1.0, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def caixa(c, x, feet, w, rot=0, label='qr', f=0, seed=1, glow=0):
    """caixa de papelão com etiqueta (QR ou vários códigos de barras)."""
    im = _caixa_img(int(w), label, seed, glow)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(feet - im.size[1])))


@lru_cache(maxsize=32)
def _caixa_img(w, label, seed, glow):
    h = int(w * .8)
    p = Pen(500, 400)
    p.shape([(20, 40), (480, 40), (480, 390), (20, 390)], hexc('#c9935a'), hexc('#a8743f'), 6, 16)
    p.stroke([(250, 40), (250, 120)], 10, hexc('#e8c79a'))
    if label == 'barras':
        for k, (bx, by) in enumerate(((50, 150), (270, 140), (60, 280), (280, 270))):
            p.shape([(bx, by), (bx + 170, by), (bx + 170, by + 90), (bx, by + 90)], (255, 255, 255), None, 4)
            rr = random.Random(k)
            xx = bx + 12
            while xx < bx + 158:
                ww = rr.choice((3, 5, 8)); p.poly([(xx, by + 10), (xx + ww, by + 10), (xx + ww, by + 80), (xx, by + 80)], INK); xx += ww + rr.choice((3, 5))
    im = p.img.resize((w, h), Image.LANCZOS)
    if label == 'qr':
        q = sprite('qr', tuple(sorted(dict(seed=seed, glow=glow).items())), int(w * .5), 1.0, False)
        im.alpha_composite(q, (int(w * .25), int(h * .3)))
    return im


def leitor(c, x, y, s=1.0, beam=0, flip=False):
    """pistola leitora com feixe vermelho."""
    if s <= .02: return
    p = Pen(420, 300)
    if beam:
        p.poly([(10, 60), (130, 90), (130, 120), (10, 200)], hexc('#ff5a4f'))
    p.shape([(130, 70), (360, 70), (380, 140), (130, 140)], hexc('#f2c230'), hexc('#c9971c'), 5, 8)
    p.shape([(250, 130), (310, 130), (340, 290), (270, 290)], hexc('#3b3f4a'), hexc('#262830'), 5, 8)
    im = p.img.resize((int(420 * s), int(300 * s)), Image.LANCZOS)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    paste_c(c, im, x, y)


def celular(c, x, y, h, f, conteudo=None, s=1.0):
    """celular de pé com tela (conteúdo RGBA opcional)."""
    if s <= .02: return
    w = int(h * .52)
    im = _cel_img(w, h).copy()
    if conteudo is not None:
        cc = conteudo.resize((int(w * .7), int(w * .7)), Image.LANCZOS)
        im.alpha_composite(cc, (int(w * .15), int(h * .3)))
    paste_c(c, im, x, y, s)


@lru_cache(maxsize=4)
def _cel_img(w, h):
    p = Pen(260, 500)
    p.shape([(10, 10), (250, 10), (250, 490), (10, 490)], hexc('#2b2d3a'), hexc('#1b1c26'), 6, 10)
    p.poly([(26, 40), (234, 40), (234, 450), (26, 450)], hexc('#eaf2ff'))
    return p.img.resize((w, h), Image.LANCZOS)


@lru_cache(maxsize=4)
def restaurante(luz='day'):
    """restaurante: parede, janela, mesa com toalha e plaquinha com QR do cardápio."""
    import cenarios as C
    fy = 1560
    base = Image.new('RGBA', (BW, BH), (0, 0, 0, 255)); p = Pen(BW, BH)
    p.poly([(0, 0), (BW, 0), (BW, fy), (0, fy)], hexc('#f2d7b6'))
    p.poly([(0, 900), (BW, 900), (BW, fy), (0, fy)], hexc('#b5523b'))
    p.stroke([(0, 900), (BW, 900)], 6)
    C._janela(p, 140, 300, 520, 720, luz)
    for x in (760, 1060):
        p.stroke([(x, 0), (x, 220)], 5); p.shape(ell_pts(x, 260, 80, 50, 32), hexc('#f2c230'), hexc('#c9971c'), 5, 6)
    C._piso_madeira(p, fy)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


def mesa(c, cx, top, w=900):
    c.alpha_composite(_mesa_img(w), (int(cx - w / 2), int(top)))


@lru_cache(maxsize=4)
def _mesa_img(w):
    p = Pen(w, 700)
    for x in (120, w - 120): p.line([(x, 100), (x, 690)], hexc('#65452a'), 30, 5)
    p.shape([(0, 0), (w, 0), (w - 30, 260), (30, 260)], (255, 255, 255), hexc('#e1e1e1'), 6, 12)
    for k in range(0, w, 90):
        p.poly([(k, 0), (k + 45, 0), (k + 45 - 2, 260), (k + 2, 260)], hexc('#e3463b'))
    p.stroke([(0, 0), (w, 0)], 6)
    return p.img.resize((w, 700), Image.LANCZOS)


@lru_cache(maxsize=4)
def _plaq_img(size):
    p = Pen(300, 380)
    p.shape([(20, 20), (280, 20), (280, 330), (20, 330)], hexc('#2b2d3a'), hexc('#1b1c26'), 5, 8)
    p.shape([(100, 330), (200, 330), (230, 370), (70, 370)], hexc('#2b2d3a'), None, 5)
    return p.img.resize((size, int(size * 380 / 300)), Image.LANCZOS)


def plaquinha(c, x, base, size, f, **kw):
    im = _plaq_img(size)
    c.alpha_composite(im, (int(x - size / 2), int(base - im.size[1])))
    put_qr(c, x, base - im.size[1] + size * .58, size * .78, f, **kw)


def SFX(s):
    s.ting(s.W(0, 'quadrados'), .3)
    s.thunk(s.W(0, 'enfeite') - 2, 260, .6)
    s.whoosh(s.W(1, 'japao') - 6, .4, .4)
    s.thunk(s.W(1, 'carro') - 2, 160, .6)
    for i in range(6): s.ting(s.W(2, 'bipe') + i * 5, .18)
    s.thunk(s.W(3, 'virado') - 2, 300, .5)
    s.ting(s.W(3, 'lado'), .35)
    s.ting(s.W(4, 'proposito'), .3)
    s.thunk(s.W(5, 'estragado') - 2, 140, .7)
    s.trill(s.W(6, 'carro'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 restaurante (QR do cardápio na mesa, quadrados com olhinhos) | s1 fábrica de peças de carro no Japão (1994)
# s2 fábrica (caixa com vários códigos de barras, bipe atrás do outro) | s3 fábrica (caixas viradas, leitor lê de qualquer lado)
# s4 escritório (papéis impressos e lupa procurando o padrão) | s5 escritório ao entardecer (celular reconhece o QR; QR estragado ainda lê)
# s6 restaurante (cliente lê o cardápio; pensamento: peças de carro)
def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def s0(f):
    c = restaurante('day').copy()
    q0 = wt(0, 'quadrados') - 3
    e0 = wt(0, 'enfeite') - 3
    mesa(c, 621, 1380)
    plaquinha(c, 621, 1390, 420, f, seed=1, eyes=1 if f >= q0 else 0, glow=1 if f >= q0 else 0, look=math.sin(f * .08))
    if f >= q0 and f < e0: placa = txt('3 QUADRADOS', 84, -5); paste_c(c, placa, 621, 560, back(ramp(f, q0, q0 + 8)))
    if f >= e0: paste_c(c, txt('NÃO É ENFEITE!', 84, 5), 621, 560, back(ramp(f, e0, e0 + 8)))
    t = easeOut(ramp(f, 0, 50))
    kk = kick(f, e0)
    return c, (621, lerp(1000, 1050, t) + kk * 10, lerp(1.7, 1.3, t), kk), 'day'


def s1(f):
    c = CEN('fabrica', 'day').copy()
    j0 = wt(1, 'japao') - 3
    k0 = wt(1, 'carro') - 3
    for i, x in enumerate((200, 480, 760)):
        caixa(c, x - (f * 3) % 280 + 280, 1290, 220, label='barras', f=f, seed=i)
    put_pessoa(c, 880, 1980, 1000, f, 1, shirt='#f28c28', pants='#3b3f4a', pocket=False, skin=1, hair='#2b2b2b', arms='hang', expr='neutral', look=-1)
    if f >= j0: paste_c(c, txt('JAPÃO, 1994', 90, -5), 621, 560, back(ramp(f, j0, j0 + 8)))
    if f >= k0:
        p = Pen(400, 300)  # engrenagem + pneu = peça de carro
        p.dot(200, 150, 120, hexc('#3b3f4a'), 6); p.dot(200, 150, 60, hexc('#9aa0a8'), 5); p.dot(200, 150, 20, hexc('#3b3f4a'))
        paste_c(c, p.img.resize((220, 165), Image.LANCZOS), 360, 860, back(ramp(f, k0, k0 + 8)))
        paste_c(c, txt('PEÇAS DE CARRO', 70, 5), 660, 720, back(ramp(f, k0, k0 + 8)))
    t = smooth(ramp(f, 0, 140))
    return c, (lerp(600, 660, t), 1200, lerp(1.15, 1.22, t), 0), 'day'


def s2(f):
    c = CEN('fabrica', 'day').copy()
    b0 = wt(2, 'barras') - 3
    p0 = wt(2, 'bipe') - 3
    caixa(c, 560, 1700, 520, label='barras')
    beep = f >= p0 and ((f - p0) // 5) % 2 == 0
    put_pessoa(c, 980, 2000, 1000, f, 2, shirt='#f28c28', pants='#3b3f4a', pocket=False, skin=1, hair='#2b2b2b',
               arms='ask', expr='pained' if f >= p0 + 20 else 'neutral', look=-1)
    leitor(c, 900, 1545, .8, beam=beep, flip=False)
    if f >= b0 and f < p0: paste_c(c, txt('VÁRIOS CÓDIGOS', 76, -5), 600, 620, back(ramp(f, b0, b0 + 8)))
    if f >= p0:
        for i in range(min(5, (f - p0) // 5 + 1)):
            paste_c(c, txt('BIP!', 64, -12 + i * 6), 420 + (i % 3) * 200, 660 + (i // 3) * 140, back(ramp(f, p0 + i * 5, p0 + i * 5 + 4)))
    t = smooth(ramp(f, 0, 110))
    return c, (lerp(640, 680, t), 1250, lerp(1.15, 1.25, t), 0), 'day'


def s3(f):
    c = CEN('fabrica', 'day').copy()
    v0 = wt(3, 'virado') - 3
    l0 = wt(3, 'lado') - 3
    rots = (0, 90, 180)
    for i, (x, r) in enumerate(zip((260, 620, 980), rots)):
        rot = r if f >= v0 else 0
        caixa(c, x, 1520, 330, rot=rot, label='qr', seed=2 + i, glow=1 if f >= v0 else 0)
        if f >= l0 + i * 6:
            paste_c(c, txt('LEU!', 70, -6 + i * 6), x, 1060, back(ramp(f, l0 + i * 6, l0 + i * 6 + 6)))
    put_qr(c, 621, 600, 380, f, 9, eyes=1, look=math.sin(f * .1), glow=1)
    t = smooth(ramp(f, 0, 130))
    return c, (621, lerp(1150, 1200, t), lerp(1.15, 1.2, t), 0), 'day'


def s4(f):
    c = CEN('escritorio', 'day').copy()
    p0 = wt(4, 'proposito') - 3
    i0 = wt(4, 'impressas') - 3
    c.alpha_composite(_papeis(), (300, 1100))
    if f >= p0:
        s = back(ramp(f, p0, p0 + 8))
        paste_c(c, _regua(), 650, 820, s)
        paste_c(c, txt('1 : 1 : 3 : 1 : 1', 70, 0), 650, 700, s)
    if f >= i0:
        paste_c(c, txt('QUASE NUNCA APARECE', 60, -4), 650, 560, back(ramp(f, i0, i0 + 8)))
    t = smooth(ramp(f, 0, 150))
    return c, (lerp(620, 650, t), lerp(1100, 1050, t), lerp(1.15, 1.25, t), 0), 'day'


@lru_cache(maxsize=1)
def _papeis():
    p = Pen(700, 400)
    for k in range(4):
        p.shape([(60 + k * 30, 40 + k * 12), (620 + k * 10, 20 + k * 12), (640 + k * 10, 360), (40 + k * 30, 380)], (255, 255, 255), hexc('#e6e6e6'), 4, 6)
    rr = random.Random(3)
    for y in range(90, 340, 26):
        xx = 140
        while xx < 600:
            ww = rr.randint(30, 90); p.stroke([(xx, y), (xx + ww, y)], 7, hexc('#7b8090')); xx += ww + 14
    return p.img.resize((700, 400), Image.LANCZOS)


@lru_cache(maxsize=1)
def _regua():
    if True:
        q = Pen(560, 120)
        x = 20
        for k, wmod in enumerate((1, 1, 3, 1, 1)):
            q.poly([(x, 20), (x + wmod * 70, 20), (x + wmod * 70, 100), (x, 100)], INK if k % 2 == 0 else (255, 255, 255))
            x += wmod * 70
        q.stroke([(20, 20), (x, 20), (x, 100), (20, 100), (20, 20)], 5)
        return q.img.resize((560, 120), Image.LANCZOS)


def s5(f):
    c = CEN('escritorio', 'dusk').copy()
    c0 = wt(5, 'confunde') - 3
    e0 = wt(5, 'estragado') - 3
    dano = f >= e0 - 4
    put_qr(c, 380, 760, 420, f, 11, dano=1 if dano else 0)
    found = f >= c0
    cont = sprite('qr', tuple(sorted(dict(seed=11, dano=1 if dano else 0).items())), 300, 1.0, False)
    celular(c, 900, 900, 620, f, cont)
    if found:
        # moldura verde de 'achei' na tela
        p = Pen(220, 220); p.stroke([(10, 10), (210, 10), (210, 210), (10, 210), (10, 10)], 12, hexc('#3ad66d'))
        paste_c(c, p.img.resize((240, 240), Image.LANCZOS), 900, 905, back(ramp(f, c0, c0 + 8)))
        if f < e0: paste_c(c, txt('ACHEI!', 90, -5), 900, 470, back(ramp(f, c0, c0 + 8)))
    if f >= e0: paste_c(c, txt('30% ESTRAGADO? LEU!', 60, 4), 621, 470, back(ramp(f, e0, e0 + 8)))
    t = smooth(ramp(f, 0, 150))
    return c, (lerp(620, 660, t), lerp(950, 900, t), lerp(1.12, 1.25, t), 0), 'dusk'


def s6(f):
    c = restaurante('golden').copy()
    k0 = wt(6, 'cardapio') - 3
    r0 = wt(6, 'carro') - 3
    mesa(c, 621, 1380)
    plaquinha(c, 760, 1390, 300, f, seed=1, eyes=1, look=-1)
    put_pessoa(c, 330, 1980, 1050, f, 3, shirt='#2fa38a', skin=3, hair='#2b2b2b', expr='grin' if f < r0 else 'shock', arms='point', look=1)
    if f >= k0 and f < r0: paste_c(c, txt('CARDÁPIO', 90, -5), 621, 560, back(ramp(f, k0, k0 + 8)))
    if f >= r0:
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        caixa(cont, 150, 270, 240, label='qr', seed=2)
        thought(c, 740, 620, 220, back(ramp(f, r0 - 2, r0 + 8)), cont)
        paste_c(c, txt('PEÇA DE CARRO!', 72, 5), 621, 450, back(ramp(f, r0, r0 + 8)))
    t = easeOut(ramp(f, 0, 70)); t2 = smooth(ramp(f, r0 - 10, r0 + 30))
    return c, (lerp(600, 640, t), lerp(1150, 1000, t2), lerp(1.15, 1.3, t2), lerp(0, 2, t2)), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
