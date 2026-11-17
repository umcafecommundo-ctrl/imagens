"""Formato DESENHO: o botão de ligar é um 1 e um 0 (Curiosidades da IA, 17/11/2026, 21h).
Categoria: TECNOLOGIA.
Fatos: 99% Invisible ("Modern Hieroglyphs: Binary Logic Behind the Universal Power Symbol"): o símbolo de ligar é uma
combinação abstrata de 1 e 0, que no binário querem dizer ligado e desligado; é uma alternativa ao texto em inglês
"On/Off"; os símbolos de aparelhos vêm do padrão IEC 60417 / ISO 7000; o símbolo da linha dentro do círculo é o botão
único que alterna entre ligado e desligado. Hunker e Gizmodo confirmam: a barra é o 1 (ligado), o círculo é o 0 (desligado).
Cenários: s0 escritório (Professor aponta o botão de ligar gigante) | s1 escritório (risquinho = 1, bolinha = 0) |
s2 escritório (binário: 1 acende a lâmpada, 0 apaga) | s3 escritório ao entardecer (o símbolo junta os dois) |
s4 sala ao entardecer (Professor liga a TV: fala a língua dos computadores)."""
from kit import *

LINES = [
    "O botão de ligar tem um número escondido.",
    "Aquele risquinho em pé é o número um. E a bolinha é o zero.",
    "Na língua dos computadores, um quer dizer ligado, e zero, desligado.",
    "Você vê, o símbolo junta os dois: liga e desliga no mesmo botão.",
    "Ou seja: todo dia, sem perceber, você fala a língua dos computadores.",
]
CAPTXT = [
    "O botão de ligar tem um número escondido.",
    "Aquele risquinho em pé é o número 1.|E a bolinha é o 0.",
    "Na língua dos computadores, 1 quer dizer ligado,|e 0, desligado.",
    "Você vê, o símbolo junta os dois:|liga e desliga no mesmo botão.",
    "Ou seja: todo dia, sem perceber,|você fala a língua dos computadores.",
]
FALA_TIKTOK = "Você já tinha reparado nisso? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'ligar', 4), (0, 'escondido', 6), (1, 'um', 4), (1, 'zero', 6), (2, 'ligado', 4), (2, 'desligado', 6),
         (3, 'junta', 4), (3, 'botao', 6), (4, 'computadores', 8)]

AZ = (70, 170, 255); VERDE = (60, 200, 110)


@lru_cache(maxsize=64)
def icone(size, risco=1.0, bola=1.0, gap=True, cor=(70, 170, 255), sep=0):
    """símbolo de ligar desenhado: círculo aberto em cima + risco. sep separa as partes (0..1)."""
    S = 4; W = size * S
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx, cy, r = W / 2, W / 2 + W * .05, W * .33
    lw = int(W * .085)
    dx = sep * W * .18
    if bola > 0:
        a0 = -90 + (35 if gap else 0); a1 = 270 - (35 if gap else 0)
        a1 = a0 + (a1 - a0) * bola
        box = (cx - r + dx, cy - r, cx + r + dx, cy + r)
        d.arc(box, a0, a1, fill=INK + (255,), width=lw + 22)
        d.arc(box, a0, a1, fill=cor + (255,), width=lw)
    if risco > 0:
        y0 = cy - r * 1.15; y1 = y0 + (cy - y0) * risco
        x = cx - dx
        d.line([(x, y0), (x, y1)], fill=INK + (255,), width=lw + 22)
        d.line([(x, y0), (x, y1)], fill=cor + (255,), width=lw)
        for yy in (y0, y1):
            d.ellipse((x - (lw + 22) / 2, yy - (lw + 22) / 2, x + (lw + 22) / 2, yy + (lw + 22) / 2), fill=INK + (255,))
            d.ellipse((x - lw / 2, yy - lw / 2, x + lw / 2, yy + lw / 2), fill=cor + (255,))
    return im.resize((size, size), Image.LANCZOS)


@lru_cache(maxsize=8)
def botao_img(size, aceso=False):
    """botão redondo grande com o símbolo."""
    S = 2; W = size * S
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((10, 26, W - 10, W - 4), fill=(40, 44, 52, 255))
    d.ellipse((10, 10, W - 10, W - 20), fill=(70, 76, 88, 255), outline=INK + (255,), width=12)
    d.ellipse((50, 46, W - 50, W - 56), fill=(52, 58, 68, 255))
    im = im.resize((size, size), Image.LANCZOS)
    ic = icone(int(size * .7), cor=(120, 255, 150) if aceso else AZ)
    im.alpha_composite(ic, ((size - ic.size[0]) // 2, (size - ic.size[1]) // 2 - int(size * .03)))
    return im


@lru_cache(maxsize=4)
def lampada(size, on):
    S = 2; W = size * S
    im = Image.new('RGBA', (W, int(W * 1.4)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if on:
        for r, a in ((W * .62, 50), (W * .52, 80)):
            d.ellipse((W / 2 - r, W * .5 - r, W / 2 + r, W * .5 + r), fill=(255, 230, 120, a))
    col = (255, 226, 90, 255) if on else (190, 196, 204, 255)
    d.ellipse((W * .14, W * .1, W * .86, W * .82), fill=col, outline=INK + (255,), width=14)
    d.rectangle((W * .32, W * .78, W * .68, W * 1.1), fill=(150, 156, 166, 255), outline=INK + (255,), width=12)
    for y in (.88, .98): d.line([(W * .32, W * y), (W * .68, W * y)], fill=INK + (255,), width=8)
    return im.resize((size, int(size * 1.4)), Image.LANCZOS)


@lru_cache(maxsize=4)
def tv_img(w, on):
    p = Pen(800, 620)
    p.shape([(20, 20), (780, 20), (780, 500), (20, 500)], hexc('#2b2f36'), hexc('#1c1f24'), 7, 10)
    p.poly([(60, 60), (740, 60), (740, 460), (60, 460)], hexc('#5fb6e3') if on else hexc('#11141a'))
    p.shape([(340, 500), (460, 500), (480, 580), (320, 580)], hexc('#2b2f36'), None, 6, 0)
    p.shape([(220, 580), (580, 580), (580, 610), (220, 610)], hexc('#2b2f36'), None, 6, 0)
    im = p.img.resize((w, int(w * 620 / 800)), Image.LANCZOS)
    if on:
        ic = icone(int(w * .3), cor=(255, 255, 255))
        im.alpha_composite(ic, ((w - ic.size[0]) // 2, int(w * .1)))
    return im


def SFX(s):
    s.thunk(s.W(0, 'ligar') - 2, 160, .7); s.ting(s.W(0, 'escondido'), .3)
    s.thunk(s.W(1, 'um') - 2, 220, .6); s.thunk(s.W(1, 'zero') - 2, 180, .6)
    s.ting(s.W(2, 'ligado') - 1, .35); s.thunk(s.W(2, 'desligado') - 2, 120, .6)
    s.whoosh(s.W(3, 'junta') - 6, .4, .4); s.thunk(s.W(3, 'junta') + 2, 140, .8)
    s.ting(s.W(3, 'botao'), .3)
    s.thunk(s.W(4, 'perceber') - 2, 260, .5); s.trill(s.W(4, 'computadores') + 4, 1.0, .3)


def s0(f):
    c = CEN('escritorio', 'day').copy()
    li = wt(0, 'ligar') - 3
    es = wt(0, 'escondido') - 3
    if f >= li: paste_c(c, botao_img(560), 820, 980, back(ramp(f, li, li + 9)))
    put_prof(c, 330, 1830, 980, f, expr='grin' if f < es else 'smug', arms='point' if f >= li else 'wave', look=1)
    if f >= es: paste_c(c, txt('UM NÚMERO?!', 100, -5), 700, 560, back(ramp(f, es, es + 8)))
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1220 + kick(f, li, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('escritorio', 'day').copy()
    um = wt(1, 'um') - 3
    ze = wt(1, 'zero') - 3
    sep = easeOut(ramp(f, um - 16, um)) if f < ze else 1
    paste_c(c, icone(700, sep=sep), 640, 1000)
    if f >= um: paste_c(c, txt('1', 220, -6), 400, 560, back(ramp(f, um, um + 8)))
    if f >= ze: paste_c(c, txt('0', 220, 6), 880, 560, back(ramp(f, ze, ze + 8)))
    put_prof(c, 990, 1860, 680, f, flip=True, expr='shock' if f >= um else 'neutral', arms='chin', look=-1)
    t = smooth(ramp(f, 0, 100))
    z = lerp(1.12, 1.25, t) * (1 + .0009 * f)
    return c, (700, lerp(1150, 1100, t) + kick(f, ze, .5) * 8, z, 0), 'day'


def s2(f):
    c = CEN('escritorio', 'day').copy()
    li = wt(2, 'ligado') - 3
    de = wt(2, 'desligado') - 3
    on = li <= f < de
    paste_c(c, lampada(420, on), 640, 820)
    lab = '1' if on else '0'
    if f >= li: paste_c(c, txt(lab, 200, -6), 330, 760, back(ramp(f, li if on else de, (li if on else de) + 8)))
    if f >= li: paste_c(c, txt('LIGADO' if on else 'DESLIGADO', 96, 5), 640, 1250, back(ramp(f, li if on else de, (li if on else de) + 8)))
    for i in range(8):  # números binários correndo no fundo
        y = (f * 6 + i * 260) % 2000 + 100
        paste_c(c, txt('0' if (i * 7 + f // 20) % 2 else '1', 70), 120 + (i % 2) * 1000, y, .45)
    z = lerp(1.25, 1.1, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1050 + kick(f, de, .5) * 8, z, 0), 'day'


def s3(f):
    c = CEN('escritorio', 'dusk').copy()
    ju = wt(3, 'junta') - 3
    bo = wt(3, 'botao') - 3
    sep = 1 - easeOut(ramp(f, ju - 4, ju + 6))
    if f < bo:
        paste_c(c, icone(700, sep=sep, cor=VERDE if f >= ju else AZ), 640, 1000)
        if f < ju + 4:
            paste_c(c, txt('1', 180, -6), 400 + (1 - sep) * 240, 560, sep)
            paste_c(c, txt('0', 180, 6), 880 - (1 - sep) * 240, 560, sep)
    else:
        aceso = ((f - bo) // 12) % 2 == 0
        paste_c(c, botao_img(620, aceso), 640, 1000, 1 - .06 * (1 if (f - bo) % 12 < 3 else 0))
        paste_c(c, txt('LIGA' if aceso else 'DESLIGA', 110, 5), 640, 520, back(ramp(f, bo, bo + 8)))
    if ju + 4 <= f < bo: paste_c(c, txt('1 + 0', 140, -5), 640, 540, back(ramp(f, ju + 4, ju + 12)))
    t = smooth(ramp(f, 0, 120))
    z = lerp(1.1, 1.3, t) * (1 + .0009 * f)
    return c, (640, 1050 + kick(f, ju + 2, .6) * 10, z, 0), 'dusk'


def s4(f):
    c = CEN('sala', 'dusk').copy()
    pe = wt(4, 'perceber') - 3
    co = wt(4, 'computadores') - 3
    on = f >= pe
    if on:
        d = ImageDraw.Draw(c); d.rectangle((716, 536, 1144, 784), fill=(95, 182, 227, 255))
        ic = icone(220, cor=(255, 255, 255)); paste_c(c, ic, 930, 660, back(ramp(f, pe, pe + 8)))
    put_prof(c, 360, 1840, 990, f, expr='grin' if f < co else 'proud', arms='point', look=1)
    if co <= f < co + 30:
        paste_c(c, txt('1010', 110, -5), 820, 960, back(ramp(f, co, co + 8)))
        paste_c(c, txt('BINÁRIO!', 96, 5), 840, 1090, back(ramp(f, co + 3, co + 11)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (660, lerp(1200, 1150, t) + kick(f, pe, .6) * 10, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4]
