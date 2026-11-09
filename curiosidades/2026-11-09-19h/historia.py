"""Formato DESENHO: Saturno boiaria numa banheira (Curiosidades da IA, 09/11/2026, 19h). Categoria: ESPAÇO.
Fatos: BBC Sky at Night Magazine, "Saturn, the enormous gas giant, could float on water (if you could find a big enough
bathtub)": densidade média de Saturno 0,687 g/cm³ contra 1 g/cm³ da água (cerca de 30% menos denso); diâmetro de
116.460 km, cerca de 9 vezes o da Terra; massa cerca de 95 vezes a da Terra; feito principalmente de hidrogênio e hélio,
os elementos mais leves; a banheira precisaria ter uns 120.000 km de largura. (Experimento mental: na prática não daria.)"""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10s', '2026-11-06-10h')
space_bg = lru_cache(maxsize=1)(_h10.space_bg); terra_img = _h10.terra_img

LINES = [
    "Saturno, o segundo maior planeta do Sistema Solar, boiaria numa banheira.",
    "Ele é tão largo que cabem umas nove Terras enfileiradas, de um lado ao outro.",
    "E pesa cerca de noventa e cinco vezes mais que a Terra.",
    "Mas ele é feito quase todo de hidrogênio e hélio, os gases mais leves que existem.",
    "Você vê, um copo cheio de Saturno pesaria menos que o mesmo copo cheio de água. E o que é mais leve que a água... boia.",
    "Só falta achar uma banheira com uns cento e vinte mil quilômetros de largura.",
]
CAPTXT = [
    "Saturno, o segundo maior planeta do Sistema Solar,|boiaria numa banheira.",
    "Ele é tão largo que cabem umas 9 Terras enfileiradas,|de um lado ao outro.",
    "E pesa cerca de 95 vezes mais que a Terra.",
    "Mas ele é feito quase todo de hidrogênio e hélio,|os gases mais leves que existem.",
    "Você vê, um copo cheio de Saturno pesaria menos|que o mesmo copo cheio de água.|E o que é mais leve que a água... boia.",
    "Só falta achar uma banheira|com uns 120 mil quilômetros de largura.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [5]
CHECK = [(0, 'saturno', 4), (0, 'banheira', 6), (1, 'nove', 4), (2, 'pesa', 4), (3, 'hidrogenio', 4), (3, 'helio', 4),
         (4, 'copo', 4), (4, 'agua', 6), (4, 'boia', 6), (5, 'banheira', 4), (5, 'largura', 8)]

SAT, SATD = hexc('#e9c98a'), hexc('#c9a35f')


# ------------------------------------------------------------------ personagens e objetos novos
def saturno(expr='calm', blink=0, look=0.0):
    """Saturno com carinha e anéis (900x560)."""
    p = Pen(900, 560)
    # anel de trás
    p.arc(450, 290, 420, 110, 180, 360, 26, hexc('#d9b67a'))
    p.arc(450, 290, 360, 88, 180, 360, 12, hexc('#f1dcae'))
    p.shape(ell_pts(450, 280, 230, 230, 64), SAT, SATD, 6, 26)
    for i, y in enumerate((170, 230, 330, 390)):
        w = math.sqrt(max(0, 230 ** 2 - (y - 280) ** 2)) - 10
        p.stroke([(450 - w, y), (450 + w, y)], 14, hexc('#d8b06e') if i % 2 else hexc('#f3dcaa'))
    ey = 260
    for dx in (-70, 70):
        ex = 450 + dx
        if blink: p.stroke([(ex - 24, ey), (ex + 24, ey)], 6)
        else:
            r = 40 if expr == 'shock' else 34
            p.dot(ex, ey, r, (255, 255, 255), 5); p.dot(ex + look * 12, ey + 4, 15, INK)
            if expr in ('smug',):
                p.poly([(ex - r - 4, ey - r - 4), (ex + r + 4, ey - r - 4), (ex + r + 4, ey - 6), (ex - r - 4, ey - 6)], SAT); p.stroke([(ex - r, ey - 6), (ex + r, ey - 6)], 6)
    if expr == 'shock': p.dot(450, ey + 80, 20, INK)
    elif expr == 'grin': p.arc(450, ey + 70, 50, 26, 10, 170, 7)
    else: p.arc(450, ey + 66, 34, 16, 20, 160, 6)
    # anel da frente
    p.arc(450, 290, 420, 110, 0, 180, 26, hexc('#d9b67a'))
    p.arc(450, 290, 360, 88, 0, 180, 12, hexc('#f1dcae'))
    return p.img


def put_sat(c, x, y, w, f, seed=1, rot=0, **kw):
    """y = centro do planeta."""
    if w < 8: return
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('saturno', tuple(sorted(kw.items())), int(w * 560 / 900), 900 / 560, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y + 8 * math.sin((f + seed * 5) * .1))


@lru_cache(maxsize=4)
def balao_img(letra, cor, size=220):
    p = Pen(220, 320)
    col = hexc(cor)
    p.stroke([(110, 200), (100, 260), (115, 318)], 4)
    p.shape(ell_pts(110, 100, 90, 100, 40), col, mul(col, .8), 5, 12)
    p.shape([(100, 196), (120, 196), (110, 212)], col, None, 4)
    im = p.img
    t = txt(letra, 80)
    im.alpha_composite(t, (110 - t.size[0] // 2, 100 - t.size[1] // 2))
    return im.resize((size, int(size * 320 / 220)), Image.LANCZOS)


@lru_cache(maxsize=4)
def copo_img(kind, w=240):
    """kind 'agua' | 'saturno'."""
    p = Pen(260, 340)
    p.shape([(20, 20), (240, 20), (215, 330), (45, 330)], hexc('#eef7fc'), hexc('#d3e5ef'), 6, 6)
    if kind == 'agua':
        p.shape([(30, 70), (230, 70), (210, 322), (50, 322)], hexc('#7cc0ec'), hexc('#5aa3d6'), 0, 6)
    else:
        p.shape([(30, 70), (230, 70), (210, 322), (50, 322)], SAT, SATD, 0, 6)
        for y in (120, 190, 260): p.stroke([(36 + (y - 70) * .07, y), (224 - (y - 70) * .07, y)], 12, hexc('#d8b06e'))
    return p.img.resize((w, int(w * 340 / 260)), Image.LANCZOS)


@lru_cache(maxsize=32)
def balanca_img(tilt, w=900):
    """balança de dois pratos (900x700); tilt -1..1 (positivo = lado direito desce)."""
    p = Pen(900, 700)
    p.shape([(380, 640), (520, 640), (560, 690), (340, 690)], hexc('#8a8f99'), hexc('#6a6f79'), 5, 6)
    p.shape([(435, 200), (465, 200), (465, 650), (435, 650)], hexc('#9aa1ad'), hexc('#7a818d'), 5, 6)
    a = tilt * .25
    ca, sa = math.cos(a), math.sin(a)
    L = (450 - 340 * ca, 200 - 340 * sa); R = (450 + 340 * ca, 200 + 340 * sa)
    p.line([L, R], hexc('#9aa1ad'), 22, 5)
    p.dot(450, 200, 22, hexc('#f2c14e'), 5)
    for (x, y) in (L, R):
        p.stroke([(x, y), (x - 110, y + 230)], 4); p.stroke([(x, y), (x + 110, y + 230)], 4)
        p.shape([(x - 150, y + 230), (x + 150, y + 230), (x + 110, y + 270), (x - 110, y + 270)], hexc('#c7ccd6'), hexc('#9aa1ad'), 5, 6)
    return p.img.resize((w, int(w * 700 / 900)), Image.LANCZOS)


def pratos(tilt, x, top, w=900):
    """posição (x, y do prato) esquerda e direita no palco, para a balança colada com o topo em `top`."""
    s = w / 900
    a = tilt * .25
    L = (450 - 340 * math.cos(a), 200 - 340 * math.sin(a) + 230); R = (450 + 340 * math.cos(a), 200 + 340 * math.sin(a) + 230)
    return [(x - w / 2 + px * s, top + py * s) for px, py in (L, R)]


@lru_cache(maxsize=1)
def agua_banho():
    """água da banheira do cenário banheiro (borda em y=1260, x 40-620)."""
    im = Image.new('RGBA', (BW, BH), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.polygon([(52, 1300), (608, 1300), (582, 1580), (78, 1580)], fill=(120, 190, 235, 255))
    return im


def borda_banho(c):
    """redesenha a frente da banheira por cima do planeta (deixa ele 'dentro' da água)."""
    p = Pen(BW, BH)
    p.shape([(40, 1330), (620, 1330), (580, 1600), (80, 1600)], (255, 255, 255), hexc('#dcdcdc'), 6, 14)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))


@lru_cache(maxsize=1)
def banho_frente():
    c = Image.new('RGBA', (BW, BH), (0, 0, 0, 0)); borda_banho(c); return c


# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 banheiro (Saturno boiando na banheira) | s1 espaço (Saturno + 9 Terras enfileiradas) | s2 espaço (balança: Saturno x Terra)
# s3 espaço (Saturno cheio de balões H e He) | s4 cozinha (balança com copo de Saturno x copo de água; depois o copo boia)
# s5 banheiro ao entardecer (banheira gigante, régua 120.000 km, Saturno boiando)

def SFX(s):
    s.splash(s.W(0, 'banheira') - 2, .5)
    for i in range(9): s.thunk(s.W(1, 'nove') - 2 + i * 3, 260 + i * 10, .35)
    s.thunk(s.W(2, 'pesa') - 2, 120, 1.0)
    s.ting(s.W(3, 'hidrogenio'), .3); s.ting(s.W(3, 'helio'), .3)
    s.thunk(s.W(4, 'copo') - 2, 300, .5); s.thunk(s.W(4, 'agua') - 2, 200, .6); s.splash(s.W(4, 'boia') - 2, .5)
    s.trill(s.W(5, 'largura'), 1.0, .3)


def s0(f):
    c = CEN('banheiro').copy()
    b = wt(0, 'banheira') - 3
    c.alpha_composite(agua_banho())
    dip = back(ramp(f, b - 10, b + 4))
    put_sat(c, 330, lerp(700, 1300, dip), 560, f, 1, rot=4 * math.sin(f * .12), expr='grin' if f >= b else 'calm', look=.3)
    c.alpha_composite(banho_frente())
    if f >= b:
        paste_c(c, txt('SPLASH!', 100, -6), 340, 980, back(ramp(f, b, b + 8)) * (1 - ramp(f, b + 30, b + 36)))
        for i in range(6):
            t = (f - b) / 18
            if t < 1: paste_c(c, txt('•', 70), 330 + (i - 2.5) * 80 * (1 + t), 1290 - 200 * t + 260 * t * t, 1)
    z = lerp(1.15, 1.35, smooth(ramp(f, 0, 80)))
    return c, (lerp(500, 400, smooth(ramp(f, 0, 80))), 1250, z, 0), 'day'


def s1(f):
    c = space_bg().copy()
    n = wt(1, 'nove') - 3
    put_sat(c, 621, 900, 1700, f, 2, look=.6 * math.sin(f * .05))
    if f >= n:
        d = ImageDraw.Draw(c)
        for x in (621 - 434, 621 + 434):
            for y in range(1000, 1400, 40): d.line((x, y, x, y + 20), fill=(255, 255, 255, 220), width=6)
        for i in range(9):
            s = back(ramp(f, n + i * 3, n + i * 3 + 8))
            if s > .05: paste_c(c, terra_img(100), 621 - 4 * 96.5 + i * 96.5, 1440, s)
        paste_c(c, txt('9 TERRAS', 100, -4), 621, 1580, back(ramp(f, n + 24, n + 32)))
    z = lerp(1.25, 1.02, easeOut(ramp(f, 0, 50)))
    return c, (621, 1200, z, 0), 'day'


def s2(f):
    c = space_bg().copy()
    pe = wt(2, 'pesa') - 3
    tilt = -back(ramp(f, pe, pe + 10)) * .9
    top = 1000
    c.alpha_composite(balanca_img(round(tilt * 20) / 20, 1000), (121, top))
    (lx, ly), (rx, ry) = pratos(round(tilt * 20) / 20, 621, top, 1000)
    put_sat(c, lx, ly - 80, 340, f, 3, expr='smug' if f >= pe else 'calm', look=.6)
    paste_c(c, terra_img(120), rx, ry - 60)
    if f >= pe: paste_c(c, txt('95x MAIS PESADO', 80, -4), 621, 620, back(ramp(f, pe + 4, pe + 12)))
    z = 1.0
    return c, (621, 1250 + kick(f, pe + 8) * 10, z, kick(f, pe + 8)), 'day'


def s3(f):
    c = space_bg().copy()
    hh = wt(3, 'hidrogenio') - 3
    he = wt(3, 'helio') - 3
    for i in range(6):
        k0 = hh if i % 2 == 0 else he
        s = back(ramp(f, k0 + i * 2, k0 + i * 2 + 8))
        if s > .05:
            x = 240 + i * 150
            y = 640 + 40 * math.sin((f + i * 9) * .08) - (i % 2) * 60
            paste_c(c, balao_img('H' if i % 2 == 0 else 'He', '#8ecae6' if i % 2 == 0 else '#f4a261', 200), x, y, s)
    put_sat(c, 621, 1250 - 30 * ramp(f, he, he + 60), 1000, f, 4, expr='grin' if f >= he else 'calm', look=-.3)
    l = wt(3, 'leves') - 3
    if f >= l: paste_c(c, txt('LEVINHO!', 100, 6), 621, 1620, back(ramp(f, l, l + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 100)))
    return c, (621, 1150, z, 0), 'day'


def s4(f):
    c = CEN('cozinha', 'dusk').copy()
    co = wt(4, 'copo') - 3
    ag = wt(4, 'agua') - 3
    bo = wt(4, 'boia') - 3
    if f < bo - 8:
        tilt = back(ramp(f, ag, ag + 10)) * .8 if f >= ag else 0
        top = 820
        c.alpha_composite(balanca_img(round(tilt * 20) / 20, 800), (221, top))
        (lx, ly), (rx, ry) = pratos(round(tilt * 20) / 20, 621, top, 800)
        if f >= co: paste_c(c, copo_img('saturno', 170), lx, ly - 105, back(ramp(f, co, co + 8)))
        if f >= ag - 12: paste_c(c, copo_img('agua', 170), rx, ry - 105, back(ramp(f, ag - 12, ag - 4)))
        if f >= ag: paste_c(c, txt('MAIS LEVE!', 90, -6), 621, 640, back(ramp(f, ag + 4, ag + 12)))
    else:
        # aquário/pote d'água com o "pedaço de Saturno" boiando
        d = ImageDraw.Draw(c)
        d.rectangle((260, 900, 980, 1540), fill=(150, 205, 240, 255), outline=(36, 23, 38), width=8)
        d.rectangle((268, 1060, 972, 1532), fill=(110, 180, 230, 255))
        bob = 14 * math.sin(f * .2)
        put_sat(c, 621, 1050 + bob - 260 * (1 - back(ramp(f, bo - 8, bo + 6))), 600, f, 5, expr='grin', look=.4)
        d2 = ImageDraw.Draw(c)
        d2.line((268, 1060, 972, 1060), fill=(36, 23, 38), width=5)
        paste_c(c, txt('BOIA!', 120, 6), 621, 640, back(ramp(f, bo, bo + 8)))
    z = lerp(1.1, 1.22, smooth(ramp(f, 0, 160)))
    return c, (621, 1180, z, 0), 'dusk'


@lru_cache(maxsize=1)
def tub_back():
    p = Pen(BW, BH)
    p.shape([(60, 1050), (1180, 1050), (1120, 1500), (120, 1500)], (255, 255, 255), hexc('#dcdcdc'), 7, 18)
    for x in (220, 1020): p.shape(ell_pts(x, 1540, 50, 40, 24), hexc('#c9b07a'), hexc('#a78f5c'), 5, 6)
    p.line([(1100, 1050), (1100, 900), (1000, 900)], hexc('#9aa1ad'), 20, 5)
    return p.img.resize((BW, BH), Image.LANCZOS)


@lru_cache(maxsize=1)
def tub_front():
    p2 = Pen(BW, BH)
    p2.shape([(70, 1140), (1170, 1140), (1120, 1500), (120, 1500)], (255, 255, 255), hexc('#dcdcdc'), 7, 18)
    return p2.img.resize((BW, BH), Image.LANCZOS)


def s5(f):
    c = space_bg().copy()
    # banheira gigante no espaço
    c.alpha_composite(tub_back())
    d = ImageDraw.Draw(c)
    d.polygon([(78, 1110), (1162, 1110), (1150, 1170), (90, 1170)], fill=(120, 190, 235, 255))
    put_sat(c, 621, 1000 + 10 * math.sin(f * .15), 760, f, 6, expr='smug', look=.5, rot=3 * math.sin(f * .1))
    c.alpha_composite(tub_front())
    l = wt(5, 'banheira') - 3
    if f >= l:
        s = easeOut(ramp(f, l, l + 14))
        d = ImageDraw.Draw(c)
        x1 = 120 + 1000 * s
        d.line((120, 1640, x1, 1640), fill=(242, 193, 78, 255), width=12)
        d.line((120, 1610, 120, 1670), fill=(242, 193, 78, 255), width=10)
        if s > .95: d.line((1120, 1610, 1120, 1670), fill=(242, 193, 78, 255), width=10)
    q = wt(5, 'cento') - 3
    if f >= q: paste_c(c, txt('120.000 km', 110, -4), 621, 620, back(ramp(f, q, q + 8)))
    z = lerp(1.0, 1.15, smooth(ramp(f, 0, 120)))
    return c, (621, 1150, z, lerp(0, -2, smooth(ramp(f, 0, 120)))), 'dusk'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5)]
