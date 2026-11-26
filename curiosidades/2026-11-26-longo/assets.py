"""Desenhos novos da história "O cachorro do ônibus doze" (26/11/2026), palco horizontal 2208x1242 (MOTOR_H=1)."""
from kit import *
import kit
from sombrio import *
from longo import *
from longo import _sky
import numpy as np
from PIL import ImageChops

CAR, CARD = hexc('#d89a52'), hexc('#b97a3a')
BRANCO = hexc('#f6ecd8')
PRETO = hexc('#2a2426')


# ---------------------------------------------------------------- o cachorro (de lado, olhando para a direita)
def _cabeca(p, hx, hy, look=0.0, olho='aberto', boca=False):
    """cabeça com centro em (hx, hy)."""
    # orelha de trás (caramelo)
    p.shape([(hx + 30, hy - 80), (hx + 85, hy - 95), (hx + 95, hy - 40), (hx + 70, hy + 5)], CARD, None, 5, 0)
    p.shape(ell_pts(hx, hy, 105, 92, 40), CAR, CARD, 6, 16)
    p.shape(ell_pts(hx + 92, hy + 38, 72, 48, 32), BRANCO, mul(BRANCO, .9), 5, 8)       # focinho
    p.dot(hx + 156, hy + 18, 19, INK)
    p.dot(hx + 150, hy + 12, 5, hexc('#ffffff'))
    if boca:
        p.shape([(hx + 100, hy + 66), (hx + 150, hy + 58), (hx + 128, hy + 96)], hexc('#c84a4a'), None, 4, 0)
    else:
        p.arc(hx + 118, hy + 60, 30, 12, 20, 160, 6)
    # orelha da frente (PRETA, caída)
    p.shape([(hx - 70, hy - 70), (hx - 20, hy - 92), (hx + 8, hy - 60), (hx - 12, hy + 50), (hx - 52, hy + 70), (hx - 80, hy + 20)],
            PRETO, mul(PRETO, .7), 6, 10)
    # olho grande
    ex, ey = hx + 42, hy - 18
    if olho == 'fechado':
        p.arc(ex, ey + 4, 24, 12, 20, 160, 7)
    else:
        p.dot(ex, ey, 30, hexc('#fbfbf7'), 6)
        lx = ex + look * 9
        p.dot(lx, ey + 2, 19, hexc('#5a3a22'))
        p.dot(lx, ey + 2, 10, hexc('#111214'))
        p.dot(lx + 7, ey - 7, 6, hexc('#ffffff'))
    p.stroke([(ex - 24, ey - 40), (ex + 22, ey - 46)], 7, CARD)


@lru_cache(maxsize=256)
def cachorro(pose='pe', phase=0.0, look=0.0, olho='aberto', cauda=0.0, cabeca=0.0, boca=False):
    """800x600, pés em y≈585. pose: pe, sentado, deitado. phase = fase da caminhada (0 = parado);
    cauda = ângulo do rabo (-1..1); cabeca = cabeça mais pra cima (+) ou mais pra baixo (-)."""
    p = Pen(800, 600)
    sw = math.sin(phase) * (1 if phase else 0)
    if pose == 'pe':
        a = .35 * sw
        for x0, sg in ((540, -1), (230, 1)):    # pernas de trás (mais escuras)
            p.line([(x0, 380), (x0 + 120 * math.sin(a * sg), 575)], CARD, 40, 5)
        ta = -.9 + .5 * cauda
        p.line([(150, 300), (150 + 60 * math.cos(ta + 3.4), 300 + 60 * math.sin(ta + 3.4)),
                (150 + 110 * math.cos(ta + 3.9), 300 + 110 * math.sin(ta + 3.9))], CAR, 30, 5)
        p.shape(ell_pts(350, 340, 215, 100, 48), CAR, CARD, 7, 18)
        p.shape(ell_pts(380, 400, 140, 36, 32), BRANCO, None, 4, 0)
        for x0, sg in ((500, 1), (210, -1)):    # pernas da frente
            fx = x0 + 120 * math.sin(a * sg)
            p.line([(x0, 380), (fx, 570)], CAR, 46, 6)
            p.shape(ell_pts(fx + 14, 576, 34, 16, 20), BRANCO, None, 5, 0)
        p.shape(ell_pts(520, 330, 70, 80, 32), BRANCO, None, 5, 0)   # peito
        _cabeca(p, 580, 205 - 40 * cabeca, look, olho, boca)
    elif pose == 'sentado':
        ta = .2 * cauda
        p.line([(250, 560), (170, 570 - 20 * ta), (90, 545 - 40 * ta)], CAR, 30, 5)
        p.line([(470, 380), (490, 572)], CARD, 40, 5)
        p.shape(ell_pts(330, 400, 130, 175, 48, rot=.35), CAR, CARD, 7, 18)
        p.shape(ell_pts(265, 480, 125, 100, 40), CAR, CARD, 6, 14)
        p.shape(ell_pts(300, 572, 80, 22, 24), BRANCO, None, 5, 0)
        p.shape(ell_pts(430, 360, 62, 95, 32, rot=.2), BRANCO, None, 5, 0)
        p.line([(420, 400), (432, 570)], CAR, 46, 6)
        p.shape(ell_pts(446, 576, 34, 16, 20), BRANCO, None, 5, 0)
        _cabeca(p, 470, 175 - 40 * cabeca, look, olho, boca)
    else:   # deitado
        p.line([(130, 510), (70, 545), (20, 575)], CAR, 30, 5)
        p.shape(ell_pts(330, 495, 230, 82, 48), CAR, CARD, 7, 18)
        p.shape(ell_pts(330, 560, 170, 22, 32), BRANCO, None, 4, 0)
        for dx in (0, 46):
            p.line([(480 + dx, 540), (640 + dx, 568)], CAR, 40, 5)
            p.shape(ell_pts(650 + dx, 568, 34, 16, 20), BRANCO, None, 5, 0)
        _cabeca(p, 560, 420 - 30 * cabeca, look, olho, boca)
    return p.img.resize((800, 600), Image.LANCZOS)


def put_cao(c, x, feet, h=400, f=0, flip=False, pose='pe', walk=0, look=0.0, olho='aberto', cauda=None, cabeca=0.0, boca=False):
    """x = centro do corpo; h = altura do quadro do desenho (o cachorro em pé mede ~0,7 h)."""
    if h < 10: return
    ph = round(((f * .35) % (2 * math.pi)) / (2 * math.pi) * 10) / 10 * 2 * math.pi if walk else 0.0
    if cauda is None: cauda = round(math.sin(f * .5) * 4) / 4
    im = kit.sprite('cachorro', tuple(sorted(dict(pose=pose, phase=round(ph, 3) or 0.0, look=round(look * 4) / 4, olho=olho,
                                                    cauda=cauda, cabeca=round(cabeca * 4) / 4, boca=boca).items())), int(h), 800 / 600, flip)
    bob = abs(math.sin(f * .35)) * .02 * h * (1 if walk else 0)
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - im.height * .975 - bob)))


def cabeca_cao(x, feet, h, flip=False, pose='pe'):
    """posição do olho do cachorro na tela (para cartões)."""
    k = h / 600
    lx, ly = {'pe': (622, 187), 'sentado': (512, 157), 'deitado': (602, 402)}[pose]
    dx = (lx - 400) * k
    return x + (-dx if flip else dx), feet - (585 - ly) * k


# ---------------------------------------------------------------- ônibus por fora (de lado, frente para a direita)
AMAR = '#e8b23a'


@lru_cache(maxsize=16)
def onibus_img(luz='dia', aberta=0.0, gente=True, sepia=False):
    """1800x760, rodas encostam em y≈745. Porta da frente em x 1420..1540; placa '12' em cima do para-brisa."""
    e = {'dia': 1, 'tarde': .95, 'neblina': .82, 'noite': .6}.get(luz, 1)
    p = Pen(1800, 760)
    body = mul(hexc(AMAR), e)
    p.shape([(30, 110), (1700, 110), (1770, 170), (1775, 650), (30, 650)], body, mul(body, .84), 8, 18)
    p.poly([(34, 470), (1772, 470), (1772, 520), (34, 520)], mul(hexc('#3a6a8a'), e))
    vid = mul(hexc('#a9d4e8'), e)
    for k in range(5):
        x0 = 90 + k * 262
        p.shape([(x0, 160), (x0 + 230, 160), (x0 + 230, 380), (x0, 380)], vid, mul(vid, .88), 6, 10)
        p.stroke([(x0 + 20, 340), (x0 + 80, 180)], 6, mul(vid, 1.08))
        if gente and k in (1, 3, 4):
            cor = hexc(['#5a3a22', '#26241f', '#c8a060', '#7a5a40', '#26241f'][k])
            p.shape(ell_pts(x0 + 115, 300, 46, 50, 32), mul(cor, .9), None, 0, 0)
            p.shape([(x0 + 40, 378), (x0 + 55, 345), (x0 + 175, 345), (x0 + 190, 378)], mul(hexc('#7a8a9a'), e), None, 0, 0)
    # para-brisa
    p.shape([(1585, 150), (1700, 150), (1760, 200), (1765, 420), (1585, 420)], vid, mul(vid, .88), 6, 10)
    # placa do destino
    p.shape([(1585, 116), (1735, 116), (1735, 146), (1585, 146)], hexc('#1e2224'), None, 4, 0)
    # porta (2 folhas de vidro que abrem para os lados)
    p.poly([(1420, 150), (1550, 150), (1550, 650), (1420, 650)], mul(hexc('#2e3438'), e), 5)
    w = 62 * (1 - .8 * aberta)
    for x0, sg in ((1420, 1), (1550, -1)):
        xa = x0 if sg > 0 else x0 - w
        p.shape([(xa, 152), (xa + w, 152), (xa + w, 648), (xa, 648)], mul(hexc('#8a9aa4'), e), None, 5, 0)
        if w > 20: p.poly([(xa + 10, 170), (xa + w - 10, 170), (xa + w - 10, 620), (xa + 10, 620)], vid)
    # rodas
    for x in (330, 1290):
        p.dot(x, 660, 92, mul(hexc('#2a2c2e'), e), 6)
        p.dot(x, 660, 42, mul(hexc('#9aa0a4'), e), 5)
    p.poly([(1745, 560), (1775, 560), (1775, 600), (1745, 600)], hexc('#f4e6b8'), 4)
    im = p.img.resize((1800, 760), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    d.text((1610, 112), '12', font=font(F_STAMP, 36), fill=(255, 190, 70, 255))
    d.text((40, 527), ' 12', font=font(F_STAMP, 100), fill=mul(hexc('#3a6a8a'), e) + (255,), stroke_width=4, stroke_fill=(36, 30, 32, 255))
    if sepia: im = sepia_img(im)
    return im


def put_onibus(c, x0, base, s=.85, **kw):
    """x0 = borda esquerda; base = y onde as rodas tocam o chão. Devolve o x do meio da porta."""
    im = onibus_img(**kw)
    if s != 1:
        im = im.resize((int(im.width * s), int(im.height * s)), Image.BILINEAR)
    cola(c, im, int(x0), int(base - 745 * s))
    return x0 + 1485 * s


def cola(c, im, x, y):
    l, t = max(0, -x), max(0, -y)
    r, b = min(im.width, c.width - x), min(im.height, c.height - y)
    if r <= l or b <= t: return
    c.alpha_composite(im.crop((l, t, r, b)), (x + l, y + t))


def sepia_img(im):
    a = np.asarray(im).astype(np.float32)
    l = a[..., :3] @ np.array([.299, .587, .114], np.float32)
    out = np.stack([l * 1.05 + 30, l * .92 + 18, l * .72 + 4], -1)
    a[..., :3] = np.clip(out, 0, 255)
    return Image.fromarray(a.astype(np.uint8), 'RGBA')


# ---------------------------------------------------------------- ponto de ônibus
@lru_cache(maxsize=8)
def ponto_img(luz='dia'):
    """620x760, pés em y 750: abrigo com teto, banco e placa redonda '12'."""
    e = {'dia': 1, 'tarde': .95, 'neblina': .85, 'noite': .6}.get(luz, 1)
    p = Pen(620, 760)
    met = mul(hexc('#3f6f8f'), e)
    for x in (60, 440):
        p.shape([(x, 180), (x + 22, 180), (x + 22, 750), (x, 750)], met, None, 5, 0)
    p.shape([(20, 150), (500, 150), (520, 190), (40, 190)], met, mul(met, .8), 6, 8)
    p.poly([(84, 200), (438, 200), (438, 520), (84, 520)], mul(hexc('#cfe6ee'), e) )
    p.stroke([(84, 200), (438, 200), (438, 520), (84, 520), (84, 200)], 5)
    p.shape([(80, 560), (450, 560), (450, 590), (80, 590)], mul(hexc('#9a6a40'), e), None, 5, 0)
    for x in (110, 410): p.stroke([(x, 590), (x, 680)], 8)
    p.shape([(560, 140), (576, 140), (576, 750), (560, 750)], hexc('#6a7074'), None, 5, 0)
    p.dot(568, 120, 52, mul(hexc('#2f7f6f'), e), 6)
    im = p.img.resize((620, 760), Image.LANCZOS)
    d = ImageDraw.Draw(im); ft = font(F_STAMP, 50)
    tw = d.textlength('12', font=ft); d.text((568 - tw / 2, 88), '12', font=ft, fill=(250, 246, 236, 255))
    return im


def put_ponto(c, x, feet, s=1.0, luz='dia'):
    im = ponto_img(luz)
    if s != 1: im = im.resize((int(620 * s), int(760 * s)), Image.LANCZOS)
    cola(c, im, int(x - im.width / 2), int(feet - 750 * s))


# ---------------------------------------------------------------- rua com calçada da frente (pés em y≈1180) e rua atrás
@lru_cache(maxsize=8)
def rua2_bg(luz='dia', scroll=0):
    """céu, casas (y 300..860), calçada de trás, asfalto (y 880..1070, ônibus com base≈1050), calçada da frente (1080..1242)."""
    c = _sky(luz).copy()
    cs = casas_strip(luz if luz in ('dia', 'tarde', 'neblina', 'noite') else 'neblina')
    off = int(scroll) % (cs.width - W_)
    c.alpha_composite(cs.crop((off, 0, off + W_, 600)), (0, 290))
    d = ImageDraw.Draw(c)
    asf = {'dia': (96, 102, 108), 'tarde': (104, 96, 94), 'neblina': (76, 82, 84), 'noite': (40, 44, 46)}[luz]
    cal = {'dia': (206, 200, 186), 'tarde': (214, 190, 160), 'neblina': (150, 154, 150), 'noite': (80, 84, 86)}[luz]
    d.rectangle((0, 850, W_, 885), fill=cal + (255,)); d.line((0, 885, W_, 885), fill=(36, 30, 38, 255), width=5)
    d.rectangle((0, 885, W_, 1075), fill=asf + (255,))
    for x in range(-int(scroll * 1.6) % 320 - 320, W_, 320): d.rectangle((x, 972, x + 170, 984), fill=(236, 226, 180, 255))
    d.rectangle((0, 1075, W_, H_), fill=cal + (255,)); d.line((0, 1075, W_, 1075), fill=(36, 30, 38, 255), width=7)
    for x in range(-int(scroll * 2) % 260 - 260, W_, 260): d.line((x, 1080, x - 70, H_), fill=tuple(int(v * .86) for v in cal) + (255,), width=4)
    return c


@lru_cache(maxsize=4)
def chuva_layer(k):
    im = Image.new('RGBA', (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(im); rnd = random.Random(k)
    for i in range(170):
        x, y = rnd.randint(-100, W_), rnd.randint(-60, H_)
        d.line((x, y, x - 22, y + 70), fill=(220, 228, 240, 150), width=3)
    return im


def chuva(c, f):
    c.alpha_composite(chuva_layer(f % 4))


# ---------------------------------------------------------------- dentro do ônibus
JAN = [(560, 1010), (1090, 1540), (1620, 2070)]     # janelas (x0, x1), y 170..540
PORTA = (110, 430)                                   # porta (x0, x1)
BANCOS = [600 + i * 250 for i in range(6)]          # x do centro de cada banco; o 0 é o banco do cachorro
ASSENTO = 860                                        # y do assento


@lru_cache(maxsize=8)
def interior_img(luz='dia', aberta=0.0):
    e = {'dia': 1, 'tarde': .95, 'neblina': .85, 'noite': .62}.get(luz, 1)
    p = Pen(W_, H_)
    par = mul(hexc('#efe6d2'), e)
    p.poly([(0, 0), (W_, 0), (W_, 1080), (0, 1080)], par)
    p.poly([(0, 0), (W_, 0), (W_, 90), (0, 90)], mul(par, .85))
    p.poly([(0, 600), (W_, 600), (W_, 620), (0, 620)], mul(hexc('#3a6a8a'), e))
    # piso
    p.poly([(0, 1080), (W_, 1080), (W_, H_), (0, H_)], mul(hexc('#5a6066'), e))
    for y in range(1110, H_, 36): p.stroke([(0, y), (W_, y)], 3, mul(hexc('#4a5056'), e))
    p.stroke([(0, 1080), (W_, 1080)], 7)
    im = p.img.resize((W_, H_), Image.LANCZOS)
    # janelas e porta = buracos transparentes
    m = Image.new('L', (W_, H_), 255); d = ImageDraw.Draw(m)
    for x0, x1 in JAN: d.rounded_rectangle((x0, 170, x1, 540), 30, fill=0)
    px0, px1 = PORTA
    w = (px1 - px0) / 2 * (1 - .85 * aberta)
    d.rectangle((px0, 150, px1, 1080), fill=0)
    im.putalpha(ImageChops.multiply(im.getchannel('A'), m))
    q = Pen(W_, H_)
    for x0, x1 in JAN:
        q.stroke([(x0, 170), (x1, 170), (x1, 540), (x0, 540), (x0, 170)], 16, mul(hexc('#8a949a'), e))
        q.stroke([(x0 - 8, 162), (x1 + 8, 162), (x1 + 8, 548), (x0 - 8, 548), (x0 - 8, 162)], 4)
        q.stroke([((x0 + x1) / 2, 170), ((x0 + x1) / 2, 300)], 10, mul(hexc('#8a949a'), e))
    # folhas da porta
    q.stroke([(px0, 150), (px1, 150), (px1, 1080), (px0, 1080), (px0, 150)], 14, mul(hexc('#2e3438'), e))
    for xa in (px0, px1 - w):
        if w > 8:
            q.shape([(xa, 156), (xa + w, 156), (xa + w, 1076), (xa, 1076)], mul(hexc('#8a9aa4'), e), None, 5, 0)
            q.poly([(xa + 12, 176), (xa + w - 12, 176), (xa + w - 12, 1050), (xa + 12, 1050)], mul(hexc('#bcdbe8'), e) )
    # barras amarelas
    am = mul(hexc('#f0c040'), e)
    q.line([(0, 120), (W_, 120)], am, 16, 5)
    for x in (480, 2150): q.line([(x, 120), (x, 1080)], am, 18, 5)
    for x in range(700, W_, 300):
        q.line([(x, 120), (x, 200)], mul(hexc('#3a3a3a'), e), 8, 3)
        q.shape(ell_pts(x, 222, 24, 26, 20), mul(hexc('#3a3a3a'), e), None, 4, 0)
        q.dot(x, 222, 12, par)
    # encostos dos bancos (contra a parede)
    for i, bx in enumerate(BANCOS):
        col = mul(hexc('#e07a3a' if i == 0 else '#3f6f9f'), e)
        q.shape([(bx - 110, 640), (bx + 110, 640), (bx + 115, ASSENTO), (bx - 115, ASSENTO)], col, mul(col, .82), 6, 12)
    q2 = q.img.resize((W_, H_), Image.LANCZOS)
    im.alpha_composite(q2)
    return im


@lru_cache(maxsize=8)
def assentos_img(luz='dia'):
    """frente dos assentos (por cima das pernas de quem está sentado)."""
    e = {'dia': 1, 'tarde': .95, 'neblina': .85, 'noite': .62}.get(luz, 1)
    p = Pen(W_, H_)
    for i, bx in enumerate(BANCOS):
        col = mul(hexc('#e07a3a' if i == 0 else '#3f6f9f'), e)
        p.shape([(bx - 120, ASSENTO - 10), (bx + 120, ASSENTO - 10), (bx + 116, ASSENTO + 40), (bx - 116, ASSENTO + 40)], mul(col, 1.08), None, 6, 0)
        p.shape([(bx - 110, ASSENTO + 40), (bx + 110, ASSENTO + 40), (bx + 100, 1060), (bx - 100, 1060)], mul(hexc('#6a7076'), e), None, 5, 0)
    return p.img.resize((W_, H_), Image.LANCZOS)


@lru_cache(maxsize=8)
def fora_strip(luz='dia'):
    """paisagem que passa pelas janelas (céu + casas), largura 3 telas."""
    W = W_ * 3
    sky = _sky(luz)
    c = Image.new('RGBA', (W, H_), (0, 0, 0, 255))
    for k in range(3): c.alpha_composite(sky, (k * W_, 0))
    cs = casas_strip(luz if luz in ('dia', 'tarde', 'neblina', 'noite') else 'neblina')
    c.alpha_composite(cs, (0, 140))
    return c


def interior(f, luz='dia', anda=1.0, aberta=0.0, fora=None, rain=False, scroll=None):
    """fundo do ônibus por dentro. anda = velocidade da paisagem; fora = imagem fixa (ex.: o ponto) vista pela porta/janelas."""
    if fora is not None:
        c = fora.copy()
    else:
        fs = fora_strip(luz)
        off = int(f * 22 * anda if scroll is None else scroll) % (fs.width - W_)
        c = fs.crop((off, 0, off + W_, H_))
    if rain: chuva(c, f)
    c.alpha_composite(interior_img(luz, round(aberta * 8) / 8))
    return c


def sentado(c, x, f, h=680, **kw):
    """pessoa sentada num banco (o assento cobre as pernas): desenhe ANTES de assentos()."""
    put_menino(c, x, ASSENTO + .27 * h, h, f, **kw)


def assentos(c, luz='dia'):
    c.alpha_composite(assentos_img(luz))


# ---------------------------------------------------------------- esquina (prédio na frente, à direita)
@lru_cache(maxsize=4)
def esquina_img(luz='dia'):
    p = Pen(900, 1242)
    e = {'dia': 1, 'tarde': .95}.get(luz, .85)
    w = mul(hexc('#e8b4b8'), e)
    p.shape([(60, 0), (900, 0), (900, 1242), (60, 1242)], w, mul(w, .85), 8, 20)
    for y in (120, 460):
        for x in (200, 520):
            p.shape([(x, y), (x + 200, y), (x + 200, y + 220), (x, y + 220)], mul(hexc('#a9d4e8'), e), None, 6, 0)
    p.shape([(40, 700), (900, 700), (900, 780), (80, 780)], mul(hexc('#5aa36f'), e), None, 6, 0)
    for x in range(80, 900, 80): p.poly([(x, 780), (x + 80, 780), (x + 40, 820)], mul(hexc('#5aa36f'), e), 4)
    p.shape([(200, 850), (440, 850), (440, 1180), (200, 1180)], mul(hexc('#8a5a32'), e), None, 6, 0)
    return p.img.resize((900, 1242), Image.LANCZOS)


# ---------------------------------------------------------------- casas de frente (casa velha da janela azul / casa do avô)
@lru_cache(maxsize=8)
def casa_bg(tipo='velha', luz='neblina', porta=0.0, caixas=False):
    """casa grande de frente: parede x 380..1900, porta x 830..1090 (y 560..1080), batente esquerdo x 770..830, janela x 1290..1690."""
    c = _sky(luz).copy()
    p = Pen(W_, H_)
    velha = tipo == 'velha'
    e = {'dia': 1, 'tarde': .96, 'neblina': .9, 'noite': .62}.get(luz, 1)
    # mato / grama
    p.poly([(0, 880), (W_, 860), (W_, H_), (0, H_)], mul(hexc('#7fae6a' if not velha else '#8fa872'), e))
    for x in range(0, W_, 28):
        hh = 30 + (x * 37 % 50)
        p.poly([(x, 1080), (x + 10, 1080 - hh), (x + 20, 1080)], mul(hexc('#5f9050'), e))
    parede = hexc('#e8d8a8' if velha else '#a8d0e6')
    parede = mul(parede, e)
    p.shape([(380, 380), (1900, 380), (1900, 1080), (380, 1080)], parede, mul(parede, .86), 8, 18)
    tel = mul(hexc('#b8644a' if velha else '#c0453a'), e)
    p.shape([(300, 400), (1140, 120), (1980, 400)], tel, mul(tel, .82), 8, 18)
    if velha:   # rachaduras e manchas
        p.stroke([(500, 470), (530, 520), (515, 570), (545, 620)], 4, mul(parede, .7))
        p.stroke([(1780, 860), (1750, 910), (1770, 960)], 4, mul(parede, .7))
        p.shape(ell_pts(1500, 960, 140, 50, 24), mul(parede, .9), None, 0, 0)
    # batente + porta
    bat = mul(hexc('#f2ead6' if velha else '#f4f1ea'), e)
    p.shape([(770, 520), (1150, 520), (1150, 1080), (770, 1080)], bat, None, 6, 0)
    p.poly([(830, 560), (1090, 560), (1090, 1080), (830, 1080)], hexc('#2a2224'))
    pc = mul(hexc('#8a5a32' if velha else '#d9634f'), e)
    w = 260 * (1 - .8 * porta)
    p.shape([(830, 560), (830 + w, 560), (830 + w, 1080), (830, 1080)], pc, mul(pc, .85), 6, 10)
    if w > 120:
        p.shape([(860, 600), (830 + w - 30, 600), (830 + w - 30, 780), (860, 780)], mul(pc, 1.1), None, 4, 0)
        p.dot(830 + w - 40, 840, 12, hexc('#e0c070'), 4)
    # janela azul
    jc = mul(hexc('#3f7fc0'), e)
    p.shape([(1290, 540), (1690, 540), (1690, 860), (1290, 860)], hexc('#2a3440'), None, 6, 0)
    p.shape([(1290, 540), (1480, 540), (1480, 860), (1290, 860)], jc, mul(jc, .82), 6, 10)
    p.shape([(1500, 540), (1690, 540), (1690, 860), (1500, 860)], jc, mul(jc, .82), 6, 10)
    for x0 in (1290, 1500):
        for y in range(570, 850, 40): p.stroke([(x0 + 14, y), (x0 + 176, y)], 4, mul(jc, .75))
    if velha:
        p.shape(ell_pts(1360, 640, 30, 22, 20), mul(hexc('#d8d0c0'), e), None, 0, 0)   # tinta descascando
        p.shape(ell_pts(1600, 760, 24, 18, 20), mul(hexc('#d8d0c0'), e), None, 0, 0)
    else:   # flores
        for x in range(420, 760, 60):
            p.line([(x, 1080), (x, 990)], hexc('#3f8f5a'), 6, 3)
            p.dot(x, 980, 18, hexc(['#e0a43c', '#d9634f', '#f4f1ea'][x // 60 % 3]), 4)
    if caixas:
        for x, y, ww in ((1250, 1000, 200), (1480, 1010, 170), (1360, 880, 180)):
            p.shape([(x, y - 120), (x + ww, y - 120), (x + ww, y + 80), (x, y + 80)], mul(hexc('#c89a62'), e), mul(hexc('#a87d4a'), e), 6, 10)
            p.stroke([(x + ww / 2, y - 120), (x + ww / 2, y - 60)], 5)
    im = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(im)
    if velha and not caixas:   # risquinhos de altura e o nome no batente
        d = ImageDraw.Draw(c)
        for k, y in enumerate((980, 925, 872, 822, 776, 735)):
            d.line((776, y, 822, y), fill=(120, 80, 60, 255), width=4)
        ft = font(F_MAO_L, 34)
        d.text((470, 700), 'TONICO', font=ft, fill=(110, 70, 50, 255))
        d.text((520, 742), 'E FAROFA', font=ft, fill=(110, 70, 50, 255))
    return c


# ---------------------------------------------------------------- campo do ponto final
@lru_cache(maxsize=4)
def campo_bg(luz='neblina'):
    c = _sky(luz).copy()
    p = Pen(W_, H_)
    e = {'dia': 1, 'tarde': .96, 'neblina': .9}.get(luz, .7)
    for k, (y, col) in enumerate(((560, '#9cc98a'), (640, '#86b878'))):
        top = [(x, y + 60 * math.sin(x / 300 + k * 2)) for x in range(0, W_ + 1, 60)]
        p.poly([(0, H_)] + top + [(W_, H_)], mul(hexc(col), e)); p.stroke(top, 5)
    for x in range(0, W_, 160):  # cerca
        p.shape([(x, 760), (x + 16, 760), (x + 16, 870), (x, 870)], mul(hexc('#9a6a40'), e), None, 4, 0)
    p.stroke([(0, 790), (W_, 790)], 8, mul(hexc('#9a6a40'), e)); p.stroke([(0, 830), (W_, 830)], 8, mul(hexc('#9a6a40'), e))
    p.poly([(0, 885), (W_, 885), (W_, 1075), (0, 1075)], mul(hexc('#8a7a64'), e))
    p.poly([(0, 1075), (W_, 1075), (W_, H_), (0, H_)], mul(hexc('#c8b896'), e))
    p.stroke([(0, 1075), (W_, 1075)], 7)
    p.shape(ell_pts(1900, 520, 160, 130, 32), mul(hexc('#5f9050'), e), mul(hexc('#4a7a40'), e), 6, 14)  # árvore
    p.shape([(1885, 640), (1915, 640), (1915, 860), (1885, 860)], mul(hexc('#7a5230'), e), None, 5, 0)
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    return c


# ---------------------------------------------------------------- sala do avô
@lru_cache(maxsize=4)
def sala_bg(luz='tarde'):
    """sala: janela à esquerda (x 140..620), poltrona à direita (x 1500..1980), tapete redondo no centro (x≈1050, y≈1150)."""
    c = Image.new('RGBA', (W_, H_), (0, 0, 0, 255))
    c.alpha_composite(_sky(luz).crop((200, 0, 680, 480)), (140, 220))
    p = Pen(W_, H_)
    e = {'dia': 1, 'tarde': 1, 'neblina': .9, 'noite': .62}.get(luz, 1)
    w = mul(hexc('#f0d9a8'), e)
    p.poly([(0, 0), (140, 0), (140, 1080), (0, 1080)], w); p.poly([(620, 0), (W_, 0), (W_, 1080), (620, 1080)], w)
    p.poly([(140, 0), (620, 0), (620, 220), (140, 220)], w); p.poly([(140, 700), (620, 700), (620, 1080), (140, 1080)], w)
    for x in range(0, W_, 120): p.stroke([(x, 0), (x, 1080)], 3, mul(w, .95))
    p.stroke([(140, 220), (620, 220), (620, 700), (140, 700), (140, 220)], 14, hexc('#f4f1ea'))
    p.stroke([(380, 220), (380, 700)], 10, hexc('#f4f1ea'))
    p.poly([(0, 1080), (W_, 1080), (W_, H_), (0, H_)], mul(hexc('#a8835c'), e))
    for y in range(1120, H_, 50): p.stroke([(0, y), (W_, y)], 3, mul(hexc('#8a6a48'), e))
    p.stroke([(0, 1080), (W_, 1080)], 7)
    # quadros
    p.shape([(820, 300), (1060, 300), (1060, 480), (820, 480)], mul(hexc('#7fae6a'), e), None, 7, 0)
    p.shape([(1140, 340), (1300, 340), (1300, 520), (1140, 520)], mul(hexc('#e0a43c'), e), None, 7, 0)
    # tapete
    p.shape(ell_pts(1050, 1150, 430, 70, 48), mul(hexc('#c0453a'), e), mul(hexc('#a03a30'), e), 6, 10)
    p.shape(ell_pts(1050, 1150, 330, 48, 48), mul(hexc('#e0a43c'), e), None, 0, 0)
    p.shape(ell_pts(1050, 1150, 230, 32, 48), mul(hexc('#c0453a'), e), None, 0, 0)
    # poltrona
    pt = mul(hexc('#5aa36f'), e)
    p.shape([(1520, 620), (1960, 620), (1980, 1000), (1500, 1000)], pt, mul(pt, .82), 7, 16)
    p.shape([(1470, 820), (1580, 820), (1580, 1080), (1470, 1080)], pt, mul(pt, .82), 7, 10)
    p.shape([(1900, 820), (2010, 820), (2010, 1080), (1900, 1080)], pt, mul(pt, .82), 7, 10)
    p.shape([(1580, 880), (1900, 880), (1900, 1000), (1580, 1000)], mul(pt, 1.08), None, 6, 0)
    # abajur
    p.shape([(300, 1080), (340, 1080), (340, 760), (300, 760)], mul(hexc('#6a5a4a'), e), None, 5, 0)
    p.shape([(230, 640), (410, 640), (440, 760), (200, 760)], mul(hexc('#f4e1a1'), e), None, 6, 0)
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    return c


@lru_cache(maxsize=2)
def caixa_img():
    p = Pen(560, 360)
    p.shape([(40, 120), (520, 120), (500, 340), (60, 340)], hexc('#b8835a'), hexc('#9a6a40'), 7, 12)
    p.shape([(20, 40), (540, 40), (520, 120), (40, 120)], hexc('#d0a070'), None, 6, 0)
    p.stroke([(40, 120), (520, 120)], 7)
    return p.img.resize((560, 360), Image.LANCZOS)
