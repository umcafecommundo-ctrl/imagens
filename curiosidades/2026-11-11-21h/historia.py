"""Formato DESENHO: para que serve o furinho na janela do avião (Curiosidades da IA, 11/11/2026, 21h).
Categoria: INVENÇÕES E OBJETOS.
Fatos: TIME ("Here's why airplane windows have tiny holes", a partir de coluna do piloto Mark Vanhoenacker na Slate): a janela
tem três painéis (externo, do meio e interno); o furinho ("breather/bleed hole") fica no painel do meio; em altitude de
cruzeiro a pressão da cabine é muito maior que a de fora; o furo faz o painel externo receber a carga, e o do meio fica como
reserva; também deixa a umidade sair do espaço entre os painéis, e a janela fica quase sem embaçar.
AFAR ("Why is there a tiny hole in the airplane window?"): três camadas de acrílico; o furo equaliza a pressão entre o espaço
dos painéis e a cabine; o painel do meio dá proteção extra numa emergência; o furo ajuda a evitar condensação."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h10e', '2026-11-08-10h')
pessoa = _h10.pessoa
kit.pessoa = pessoa
import art as _art; _art.pessoa = pessoa


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


LINES = [
    "Esse furinho na janela do avião está lá de propósito.",
    "A janela tem três camadas, e o furinho fica na do meio.",
    "Lá em cima, o ar de dentro do avião empurra muito mais que o de fora.",
    "Você vê, o furinho faz a camada de fora segurar o empurrão, e a do meio fica de reserva.",
    "E ainda deixa a umidade sair, pra janela não embaçar.",
    "Ou seja: é um buraco no avião... que deixa tudo mais seguro.",
]
CAPTXT = [
    "Esse furinho na janela do avião está lá de propósito.",
    "A janela tem três camadas,|e o furinho fica na do meio.",
    "Lá em cima, o ar de dentro do avião|empurra muito mais que o de fora.",
    "Você vê, o furinho faz a camada de fora segurar o empurrão,|e a do meio fica de reserva.",
    "E ainda deixa a umidade sair, pra janela não embaçar.",
    "Ou seja: é um buraco no avião...|que deixa tudo mais seguro.",
]
FALA_TIKTOK = "Você já tinha reparado? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 3
FLASH = []
CHECK = [(0, 'furinho', 4), (1, 'tres', 4), (1, 'meio', 6), (2, 'dentro', 4), (3, 'fora', 4), (3, 'reserva', 6),
         (4, 'embacar', 6), (5, 'seguro', 8)]

# ------------------------------------------------------------------ cenários (escritos antes de montar)
# s0 dentro do avião (cabine com poltrona; close na janela com o furinho) | s1 dentro do avião (as 3 camadas da janela
# separadas) | s2 dentro do avião, céu de altitude na janela (setas do ar de dentro empurrando) | s3 dentro do avião ao
# entardecer (camadas: a de fora segura, a do meio de reserva) | s4 dentro do avião (janela embaçada que desembaça)
# s5 dentro do avião ao entardecer (passageiro tranquilo na janela)

WIN = (621, 1000)  # centro da janela grande na cabine


@lru_cache(maxsize=4)
def cabine(luz='day'):
    p = Pen(1242, 2208)
    p.poly([(0, 0), (1242, 0), (1242, 2208), (0, 2208)], hexc('#e9e4da'))
    p.shape([(-20, 300), (1262, 300), (1262, 380), (-20, 380)], hexc('#d6d0c3'), None, 5)  # bagageiro
    p.shape([(-20, 120), (1262, 120), (1262, 330), (-20, 330)], hexc('#cfc8b9'), hexc('#b9b2a2'), 6, 12)
    sky = {'day': ('#5aa0e6', '#bfe0ff'), 'dusk': ('#3a3f7a', '#f0a070'), 'golden': ('#7a90d0', '#ffd08a')}[luz]
    for cx in (180, 621, 1062):
        big = cx == 621
        rx, ry = (230, 330) if big else (110, 160)
        cy = WIN[1] if big else 900
        p.shape(ell_pts(cx, cy, rx + 40, ry + 40, 60), hexc('#f4f0e8'), hexc('#d8d2c4'), 6, 10)
        p.shape(ell_pts(cx, cy, rx, ry, 60), hexc(sky[1]), hexc(sky[0]), 5, 60)
    p.shape([(-20, 1500), (1262, 1500), (1262, 2208), (-20, 2208)], hexc('#3b4a6b'), hexc('#2c3850'), 6, 10)  # piso
    # poltronas
    for x in (120, 1120):
        p.shape([(x - 150, 1180), (x + 150, 1180), (x + 170, 1700), (x - 170, 1700)], hexc('#2f6fb3'), hexc('#24568c'), 6, 14)
        p.shape([(x - 110, 1130), (x + 110, 1130), (x + 110, 1230), (x - 110, 1230)], hexc('#f4f0e8'), None, 5)
    img = p.img.resize((1242, 2208), Image.LANCZOS)
    base = Image.new('RGBA', (1242, 2208), (0, 0, 0, 255)); base.alpha_composite(img)
    # nuvens na janela grande
    d = ImageDraw.Draw(base)
    for (x, y, r) in ((540, 1120, 60), (610, 1100, 80), (700, 1130, 55)):
        d.ellipse((x - r, y - r * .6, x + r, y + r * .6), fill=(255, 255, 255, 230))
    return base


def furo(c, x, y, r=12, glow=0.0):
    d = ImageDraw.Draw(c)
    if glow > 0:
        R = 40 + 30 * glow
        d.ellipse((x - R, y - R, x + R, y + R), outline=(255, 210, 60, 255), width=10)
    d.ellipse((x - r, y - r, x + r, y + r), fill=(36, 23, 38, 255))


def camadas(c, sep, f, hl=None, push=0.0):
    """3 painéis da janela vistos de lado (de perfil): fora à esquerda, meio, dentro à direita."""
    d = ImageDraw.Draw(c)
    names = ['FORA', 'MEIO', 'DENTRO']
    xs = [621 - 260 * sep, 621, 621 + 260 * sep]
    for i, x in enumerate(xs):
        bow = -30 * push if i == 0 else 0
        col = (170, 215, 250, 230) if hl != i else (255, 225, 110, 240)
        pts = [(x - 26, 640), (x + 26, 640), (x + 26 + bow, 1000), (x + 26, 1360), (x - 26, 1360), (x - 26 + bow, 1000)]
        d.polygon(pts, fill=col, outline=(36, 23, 38, 255))
        d.line(pts + [pts[0]], fill=(36, 23, 38, 255), width=6)
        if sep > .5: paste_c(c, txt(names[i], 54, 0), x, 1430, clamp((sep - .5) * 2))
    if sep > .3:
        d.ellipse((621 - 14, 1000 - 14, 621 + 14, 1000 + 14), fill=(36, 23, 38, 255))


def seta(c, x0, y, x1, col=(230, 80, 60), s=1.0):
    if s <= 0: return
    d = ImageDraw.Draw(c)
    x1 = lerp(x0, x1, s)
    d.line((x0, y, x1, y), fill=col + (255,), width=26)
    dirx = 1 if x1 > x0 else -1
    d.polygon([(x1 + dirx * 40, y), (x1 - dirx * 10, y - 40), (x1 - dirx * 10, y + 40)], fill=col + (255,), outline=(36, 23, 38, 255))


def SFX(s):
    s.ting(s.W(0, 'furinho'), .3); s.trill(s.W(0, 'proposito'), .6, .2)
    for i in range(3): s.thunk(s.W(1, 'tres') + i * 6, 280, .4)
    s.ting(s.W(1, 'meio'), .3)
    s.whoosh(s.W(2, 'empurra') - 4, .5, .5)
    s.thunk(s.W(3, 'segurar') - 2, 160, .7); s.ting(s.W(3, 'reserva'), .3)
    s.whoosh(s.W(4, 'umidade') - 4, .4, .4)
    s.trill(s.W(5, 'seguro'), 1.0, .3)


def s0(f):
    c = cabine('day').copy()
    k = wt(0, 'furinho') - 3
    furo(c, 621, 1260, 12, back(ramp(f, k, k + 8)) if f >= k else 0)
    if f >= k: paste_c(c, txt('ESSE AQUI!', 90, -6), 621, 600, back(ramp(f, k, k + 8)))
    t = easeOut(ramp(f, 0, k + 10))
    z = lerp(1.0, 2.2, t) * (1 + .0009 * f)
    return c, (621, lerp(1150, 1200, t), z, 0), 'day'


def s1(f):
    c = cabine('day').copy()
    g = Image.new('RGBA', c.size, (233, 228, 218, 235))
    c.alpha_composite(g)
    tr = wt(1, 'tres') - 3
    me = wt(1, 'meio') - 3
    sep = back(ramp(f, tr, tr + 12)) if f >= tr else 0
    camadas(c, sep, f, hl=1 if f >= me else None)
    if f >= tr: paste_c(c, txt('3 CAMADAS', 100, -5), 621, 480, back(ramp(f, tr, tr + 8)))
    if f >= me: paste_c(c, txt('FURINHO', 70, 5), 760, 880, back(ramp(f, me, me + 8)))
    z = 1.15 * (1 + .0009 * f)
    return c, (621, 1000, z, 0), 'day'


def s2(f):
    c = cabine('day').copy()
    de = wt(2, 'dentro') - 3
    fo = wt(2, 'fora') - 3
    put_pessoa(c, 1000, 1950, 900, f, 1, shirt='#f28c28', pants='#3b3f4a', pocket=False, skin=1, hair='#2b2b2b',
               expr='nervous' if f >= de else 'neutral', arms='hang', look=-1)
    if f >= de:
        for i, y in enumerate((860, 1000, 1140)):
            seta(c, 1000, y, 760, s=back(ramp(f, de + i * 3, de + i * 3 + 10)))
        paste_c(c, txt('DENTRO: MUITO', 60, -4), 760, 700, back(ramp(f, de, de + 8)))
    if f >= fo:
        seta(c, 200, 1000, 340, (90, 150, 220), back(ramp(f, fo, fo + 10)))
        paste_c(c, txt('FORA: POUCO', 58, 4), 450, 800, back(ramp(f, fo, fo + 8)))
    k = kick(f, de, .5)
    z = 1.1 * (1 + .0012 * f)
    return c, (lerp(600, 680, smooth(ramp(f, 0, 100))), 1150 + k * 8, z, k), 'dusk'


def s3(f):
    c = cabine('day').copy()
    g = Image.new('RGBA', c.size, (233, 228, 218, 235))
    c.alpha_composite(g)
    se = wt(3, 'segurar') - 3
    re = wt(3, 'reserva') - 3
    push = smooth(ramp(f, se - 10, se + 6))
    hl = 0 if se <= f < re else (1 if f >= re else None)
    camadas(c, 1.0, f, hl=hl, push=push)
    for i, y in enumerate((800, 1000, 1200)):
        seta(c, 1150, y, 920, s=1.0)
    if se <= f < re: paste_c(c, txt('SEGURA!', 90, -6), 361, 520, back(ramp(f, se, se + 8)))
    if f >= re: paste_c(c, txt('RESERVA', 80, 5), 700, 560, back(ramp(f, re, re + 8)))
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 140))) * (1 + .0009 * f)
    return c, (621, 1000, z, 0), 'dusk'


def s4(f):
    c = cabine('day').copy()
    u = wt(4, 'umidade') - 3
    e = wt(4, 'embacar') - 3
    fog = 1 - smooth(ramp(f, u, e + 4))
    if fog > 0:
        m = Image.new('L', c.size, 0)
        ImageDraw.Draw(m).ellipse((621 - 230, WIN[1] - 330, 621 + 230, WIN[1] + 330), fill=int(200 * fog))
        g = Image.new('RGBA', c.size, (240, 240, 245, 255)); g.putalpha(m)
        c.alpha_composite(g)
    furo(c, 621, 1260, 12)
    if f >= u:
        d = ImageDraw.Draw(c)
        for i in range(5):
            a = (f - u - i * 6)
            if 0 < a < 40:
                d.ellipse((621 - 10 + i * 8, 1260 - a * 6 - 10, 621 + 10 + i * 8, 1260 - a * 6 + 10), fill=(200, 220, 255, 220 - a * 5))
    if f >= e: paste_c(c, txt('SEM EMBAÇAR!', 80, -5), 621, 560, back(ramp(f, e, e + 8)))
    z = 1.5 * (1 + .0012 * f)
    return c, (621, 1050, z, 0), 'day'


def s5(f):
    c = cabine('day').copy()
    sg = wt(5, 'seguro') - 3
    b = wt(5, 'buraco') - 3
    put_pessoa(c, 950, 1950, 950, f, 2, shirt='#2fa38a', pants='#3b3f4a', pocket=False, skin=3, hair='#5a3a2a',
               expr='smug' if f >= sg else ('shock' if f >= b else 'neutral'), arms='shrug' if f >= sg else 'hang', look=-1)
    furo(c, 621, 1260, 12, 1 if f >= b else 0)
    if f >= sg: paste_c(c, txt('SEGURO!', 110, 6), 600, 720, back(ramp(f, sg, sg + 8)))
    z = lerp(1.05, 1.25, easeOut(ramp(f, 0, 70))) * (1 + .0012 * f)
    return c, (lerp(640, 720, smooth(ramp(f, 0, 70))), 1200, z, lerp(0, -2, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
