"""Formato DESENHO — FICÇÃO em 2 partes (pedido do Luis em 15/11/2026): "O elevador do 13º andar", PARTE 1.
História inventada (não é fato), narrada pelo Professor Bigode. Parte 2 em 2026-11-16-18h. Mais longa (~1 min).
SEM música de fundo (pedido do Luis em 15/11/2026): só voz e sons ambientes.
Cenários: s0 rua à noite (prédio, Professor) | s1 dentro do elevador (painel 13) | s2 quarto (Davi ri) |
s3 quarto de madrugada (relógio 2:59) | s4 elevador | s5 elevador (12 -> 13, porta abre) | s6 corredor do 13º (claro) |
s7 corredor do 13º (jornal de amanhã) | s8 elevador (volta correndo) | s9 cidade com chuva (tudo acontece) |
s10 elevador (toda noite) | s11 corredor do 13º (porteiro esperando) | s12 corredor (cochicho) | s13 quarto à noite (Professor: continua)."""
from kit import *
import kit, os, importlib.util
from art import Pen, hexc, mul, ell_pts

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1108', '2026-11-08-10h')
pessoa = _m.pessoa

MUSICA = False
W_, H_ = 1242, 2208
DAVI = dict(skin=1, hair='#3b2a1e', shirt='#3fa7d6', pants='#2f3f66', pocket=False)
PORT = dict(skin=2, hair='#9a9a9a', shirt='#1f3b6e', pants='#1f3b6e', mous=True, pocket=False)


def porteiro(**kw):
    im = pessoa(**kw).copy()
    p = Pen(600, 1000)
    p.shape([(178, 170), (422, 170), (430, 205), (170, 205)], hexc('#1f3b6e'), hexc('#142a52'), 5, 4)   # aba
    p.shape([(195, 175), (200, 105), (300, 85), (400, 105), (405, 175)], hexc('#1f3b6e'), hexc('#142a52'), 5, 6)
    p.dot(300, 140, 14, hexc('#ffd84a'), 3)
    im.alpha_composite(p.img.resize(im.size, Image.LANCZOS))
    return im


def put_pes(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def put_port(c, x, feet, h, f, seed=9, **kw):
    kit._bean(c, 'porteiro', x, feet, h, f, seed, **kw)


def _fin(p, base=None, cor='#000000'):
    b = base if base is not None else Image.new('RGBA', (W_, H_), hexc(cor) + (255,))
    b.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS)); return b


@lru_cache(maxsize=4)
def elevador_bg(luz='day'):
    p = Pen(W_, H_)
    wall = hexc('#b9c2cc') if luz != 'dusk' else hexc('#8d97a6')
    p.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], wall)
    for x in range(0, W_, 140): p.stroke([(x, 0), (x, 1560)], 3, mul(wall, .9))
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], hexc('#5b5f6b'))
    for y in range(1600, H_, 90): p.stroke([(0, y), (W_, y)], 3, hexc('#4b4f5a'))
    p.stroke([(0, 1560), (W_, 1560)], 7)
    # corrimão
    p.line([(0, 1180), (W_, 1180)], hexc('#d9dde3'), 22, 5)
    # painel de botões à direita
    p.shape([(1010, 620), (1200, 620), (1200, 1120), (1010, 1120)], hexc('#3d424c'), hexc('#2b2f37'), 6, 6)
    for r in range(6):
        for col in range(2):
            p.dot(1060 + col * 90, 700 + r * 70, 22, hexc('#c9d0d8'), 4)
    # visor
    p.shape([(470, 120), (770, 120), (770, 300), (470, 300)], hexc('#1b1d22'), None, 6, 0)
    # lâmpada
    p.poly([(380, 0), (860, 0), (840, 40), (400, 40)], hexc('#fff6d6'))
    return _fin(p)


def visor(c, n, f=0, red=False):
    paste_c(c, txt(str(n), 120, 0), 620, 212)
    if red: ImageDraw.Draw(c).rectangle((470, 120, 770, 300), outline=(226, 59, 59, 255), width=8)


@lru_cache(maxsize=4)
def porta_img(w, h):
    p = Pen(600, 1200)
    p.shape([(0, 0), (300, 0), (300, 1200), (0, 1200)], hexc('#c9d0d8'), hexc('#a3acb7'), 6, 10)
    p.shape([(300, 0), (600, 0), (600, 1200), (300, 1200)], hexc('#c9d0d8'), hexc('#a3acb7'), 6, 10)
    return p.img.resize((w, h), Image.LANCZOS)


def portas(c, abre, glow=False):
    """portas do elevador no fundo (x 330..910, y 380..1560); abre 0..1."""
    x0, x1, y0, y1 = 330, 910, 380, 1560
    d = ImageDraw.Draw(c)
    col = (255, 248, 214, 255) if glow else (40, 42, 50, 255)
    d.rectangle((x0, y0, x1, y1), fill=col)
    half = int((x1 - x0) / 2 * (1 - abre))
    if half > 2:
        im = porta_img(x1 - x0, y1 - y0)
        L = im.crop((0, 0, (x1 - x0) // 2, y1 - y0)).crop(((x1 - x0) // 2 - half, 0, (x1 - x0) // 2, y1 - y0))
        R = im.crop(((x1 - x0) // 2, 0, x1 - x0, y1 - y0)).crop((0, 0, half, y1 - y0))
        c.alpha_composite(L, (x0, y0)); c.alpha_composite(R, (x1 - half, y0))
    d.rectangle((x0 - 12, y0 - 12, x1 + 12, y1), outline=(36, 23, 38, 255), width=8)


@lru_cache(maxsize=4)
def corredor_bg(luz='day', claro=False):
    p = Pen(W_, H_)
    wall = hexc('#fff4d8') if claro else (hexc('#e8dcc6') if luz == 'day' else hexc('#9a8fa3'))
    p.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], wall)
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], hexc('#b98d5e') if claro else hexc('#8a6a4a'))
    for y in range(1610, H_, 100): p.stroke([(0, y), (W_, y)], 3, hexc('#9a734c'))
    p.stroke([(0, 1560), (W_, 1560)], 7)
    for x in (120, 760):
        p.shape([(x, 640), (x + 340, 640), (x + 340, 1560), (x, 1560)], hexc('#9a6a40'), hexc('#6f4a2a'), 6, 10)
        p.dot(x + 290, 1120, 16, hexc('#ffd84a'), 3)
        p.shape([(x + 120, 560), (x + 220, 560), (x + 220, 610), (x + 120, 610)], hexc('#ffffff'), None, 4, 0)
    if claro:
        p.shape(ell_pts(621, 240, 520, 140), hexc('#fffbe8'), None, 0, 0)
    else:
        p.poly([(560, 0), (680, 0), (660, 30), (580, 30)], hexc('#fff6d6'))
    return _fin(p)


@lru_cache(maxsize=8)
def jornal_img(w, data='AMANHÃ'):
    p = Pen(600, 420)
    p.shape([(20, 20), (580, 20), (580, 400), (20, 400)], hexc('#f4f1e8'), hexc('#d6d1c2'), 6, 10)
    for y in (150, 200, 250, 300, 350):
        p.stroke([(50, y), (300, y)], 6, hexc('#9a9a9a')); p.stroke([(330, y), (550, y)], 6, hexc('#9a9a9a'))
    im = p.img.resize((w, int(w * .7)), Image.LANCZOS)
    t = txt(data, int(w * .16), 0)
    im.alpha_composite(t, ((im.size[0] - t.size[0]) // 2, int(im.size[1] * .06)))
    return im


def SFX(s):
    s.patter(0, 40, 5, .08)
    s.ting(s.W(1, 'tres'), .3)
    s.thunk(s.W(1, 'para') - 2, 120, .6)
    s.trill(s.W(3, 'testar'), .5, .15)
    for i in range(3): s.thunk(s.W(4, 'apertou') - 2 + i * 3, 900, .2)
    s.ting(s.W(5, 'treze'), .35); s.whoosh(s.W(5, 'abriu') - 4, .7, .4)
    s.thunk(s.W(7, 'jornal') - 2, 300, .4)
    s.patter(s.W(8, 'correndo') - 4, s.W(8, 'correndo') + 30, 9, .2)
    s.patter(s.W(9, 'chuva') - 2, s.W(9, 'chuva') + 60, 22, .1)
    s.ting(s.W(10, 'noite'), .3)
    s.thunk(s.W(11, 'porteiro') - 2, 140, .7)
    s.whoosh(s.W(12, 'cochichou') - 4, .6, .3)
    s.thunk(s.W(12, 'chao') - 2, 300, .5)
    s.trill(s.W(13, 'dois'), 1.0, .3)
    # zumbido do elevador nas cenas dentro dele
    for si in (1, 4, 5, 8, 10):
        a0 = s.W(si, LINES[si].split()[0].strip(',.:'))
        for k in range(0, 90, 30): s.thunk(a0 + k, 60, .15)


LINES = [
    "Esse prédio tem vinte andares, mas não tem o décimo terceiro. Do doze, o botão pula direto pro catorze.",
    "Só que, toda noite, às três da manhã, o elevador para num andar que não existe.",
    "O Davi, que mora no décimo segundo, sempre achou que isso era lenda de vizinho.",
    "Até que, numa madrugada sem sono, ele resolveu testar.",
    "Entrou no elevador às duas e cinquenta e nove e apertou o térreo.",
    "Mas o elevador subiu. Doze... treze. E a porta abriu.",
    "Lá fora, um corredor igualzinho ao do prédio, só que claro, como se já fosse de manhã.",
    "Na porta do apartamento dele, tinha um jornal no chão, com a data de amanhã.",
    "O Davi pegou o jornal, voltou correndo pro elevador e não contou pra ninguém.",
    "No dia seguinte, tudo que estava no jornal aconteceu: a chuva, o placar do jogo, até a prova surpresa.",
    "E ele passou a descer no décimo terceiro toda noite.",
    "Até que, numa noite, quem estava esperando no corredor era o porteiro do prédio, sorrindo.",
    "Ele chegou perto, cochichou uma frase, e o Davi deixou o jornal cair no chão.",
    "E o que o porteiro disse... fica pra parte dois.",
]
CAPTXT = [
    "Esse prédio tem 20 andares, mas não tem o 13º.|Do 12, o botão pula direto pro 14.",
    "Só que, toda noite, às 3 da manhã,|o elevador para num andar que não existe.",
    "O Davi, que mora no 12º,|sempre achou que isso era lenda de vizinho.",
    "Até que, numa madrugada sem sono,|ele resolveu testar.",
    "Entrou no elevador às 2h59|e apertou o térreo.",
    "Mas o elevador subiu. Doze... treze.|E a porta abriu.",
    "Lá fora, um corredor igualzinho ao do prédio,|só que claro, como se já fosse de manhã.",
    "Na porta do apartamento dele, tinha um jornal no chão,|com a data de amanhã.",
    "O Davi pegou o jornal, voltou correndo pro elevador|e não contou pra ninguém.",
    "No dia seguinte, tudo que estava no jornal aconteceu:|a chuva, o placar do jogo, até a prova surpresa.",
    "E ele passou a descer no 13º toda noite.",
    "Até que, numa noite, quem estava esperando no corredor|era o porteiro do prédio, sorrindo.",
    "Ele chegou perto, cochichou uma frase,|e o Davi deixou o jornal cair no chão.",
    "E o que o porteiro disse... fica pra parte dois.",
]
FALA_TIKTOK = "Quer a parte dois? Comenta sim, e segue pra não perder!"
CTA_TEXTO = "COMENTA: SIM!"
TWIST = 5
FLASH = [9]
CHECK = [(0, 'terceiro', 6), (1, 'tres', 4), (2, 'lenda', 4), (3, 'testar', 4), (4, 'terreo', 4), (5, 'abriu', 4),
         (6, 'claro', 4), (7, 'amanha', 6), (8, 'correndo', 4), (9, 'chuva', 4), (10, 'noite', 4),
         (11, 'porteiro', 6), (12, 'chao', 4), (13, 'dois', 8)]


def cam(f, z0, z1, dur=80, cy=1280, k=0):
    return (621, cy + kick(f, k, .6) * 10 if k else cy, lerp(z0, z1, smooth(ramp(f, 0, dur))) * (1 + .0009 * f), 0)


@lru_cache(maxsize=2)
def predio_bg():
    base = CEN('cidade', 'dusk').copy()
    p = Pen(W_, H_)
    p.shape([(700, 120), (1120, 120), (1120, 1600), (700, 1600)], hexc('#6b6f8a'), hexc('#50536b'), 7, 16)
    for r in range(20):
        for col in range(4):
            y = 160 + r * 70; x = 730 + col * 98
            on = (r * 7 + col * 3) % 5 == 0
            p.poly([(x, y), (x + 60, y), (x + 60, y + 44), (x, y + 44)], hexc('#ffd86b') if on else hexc('#3a3d52'))
    p.dot(910, 120, 0, hexc('#000000'))
    return _fin(p, base)


def s0(f):
    c = predio_bg().copy()
    t = wt(0, 'terceiro') - 3
    pu = wt(0, 'catorze') - 3
    put_prof(c, 360, 1800, 940, f, expr='shock' if f >= t else 'grin', arms='point', look=1)
    if f < 50: paste_c(c, txt('PARTE 1', 120, -4), 621, 520, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)))
    if t <= f: paste_c(c, txt('SEM 13º?', 110, -5), 520, 660, back(ramp(f, t, t + 8)))
    if f >= pu: paste_c(c, txt('12 > 14', 100, 5), 560, 860, back(ramp(f, pu, pu + 8)))
    return c, cam(f, 1.2, 1.02, 50, 1250, t), 'dusk'


def s1(f):
    c = elevador_bg('dusk').copy()
    tr = wt(1, 'tres') - 3
    p_ = wt(1, 'para') - 3
    portas(c, 0)
    visor(c, 13 if f >= p_ else (12 if f > tr else 11), red=f >= p_)
    paste_c(c, clock_img(math.pi / 2 * 0 + 3.0, 0.0, 220), 621, 760, back(ramp(f, tr, tr + 8)) if f >= tr else 0)
    if f >= p_: paste_c(c, txt('3:00', 110, -5), 621, 1000, back(ramp(f, p_, p_ + 8)))
    return c, cam(f, 1.0, 1.12, 90, 1000, p_), 'dusk'


def s2(f):
    c = CEN('quarto', 'day').copy()
    l = wt(2, 'lenda') - 3
    put_pes(c, 621, 1800, 900, f, 2, expr='grin' if f >= l else 'neutral', arms='shrug' if f >= l else 'hang', look=0, **DAVI)
    paste_c(c, txt('DAVI', 90, -4), 621, 640, back(ramp(f, 4, 12)) * (1 - ramp(f, l - 4, l)))
    if f >= l: paste_c(c, txt('LENDA!', 110, 5), 621, 660, back(ramp(f, l, l + 8)))
    return c, cam(f, 1.15, 1.05, 60, 1280, l), 'day'


def s3(f):
    c = CEN('quarto', 'dusk').copy()
    t = wt(3, 'testar') - 3
    put_pes(c, 500, 1800, 880, f, 3, expr='stern' if f >= t else 'nervous', arms='point' if f >= t else 'hang', look=1, **DAVI)
    paste_c(c, clock_img(2.95 + f * .0005, 11.8, 240), 900, 900)
    if f >= t: paste_c(c, txt('VOU TESTAR!', 100, -5), 621, 620, back(ramp(f, t, t + 8)))
    return c, cam(f, 1.05, 1.18, 80, 1250, t), 'dusk'


def s4(f):
    c = elevador_bg('dusk').copy()
    a = wt(4, 'apertou') - 3
    portas(c, 0)
    visor(c, 12)
    put_pes(c, 560, 1820, 900, f, 4, expr='nervous', arms='point' if f >= a else 'hang', look=1, **DAVI)
    if f >= wt(4, 'cinquenta') - 3: paste_c(c, txt('2:59', 110, -4), 300, 700, back(ramp(f, wt(4, 'cinquenta') - 3, wt(4, 'cinquenta') + 5)))
    if f >= a: paste_c(c, txt('TÉRREO', 90, 5), 900, 560, back(ramp(f, a, a + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, a), 'dusk'


def s5(f):
    c = elevador_bg('dusk').copy()
    su = wt(5, 'subiu') - 3
    tz = wt(5, 'treze') - 3
    ab = wt(5, 'abriu') - 3
    portas(c, easeOut(ramp(f, ab, ab + 20)), glow=True)
    visor(c, 13 if f >= tz else 12, red=f >= tz)
    put_pes(c, 560, 1820, 900, f, 4, expr='shock' if f >= su else 'nervous', arms='up' if f >= ab else 'hang', look=0, **DAVI)
    if su <= f < tz: paste_c(c, txt('SUBIU?!', 100, -5), 621, 520, back(ramp(f, su, su + 8)))
    shake = 6 * math.sin(f * 1.7) if su <= f < tz + 10 else 0
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 100))) * (1 + .0009 * f)
    return c, (621 + shake, 1050, z, shake * .2), 'dusk'


def s6(f):
    c = corredor_bg('day', True).copy()
    cl = wt(6, 'claro') - 3
    put_pes(c, 621, 1820, 860, f, 5, expr='shock', arms='hang', look=1 if (f // 40) % 2 else -1, **DAVI)
    if f >= cl: paste_c(c, txt('DE MANHÃ?!', 100, -5), 621, 520, back(ramp(f, cl, cl + 8)))
    return c, cam(f, 1.2, 1.03, 90, 1200, cl), 'day'


def s7(f):
    c = corredor_bg('day', True).copy()
    j = wt(7, 'jornal') - 3
    am = wt(7, 'amanha') - 3
    put_pes(c, 420, 1820, 860, f, 6, expr='shock' if f >= am else 'neutral', arms='point' if f >= j else 'hang', look=1, **DAVI)
    if f >= j:
        s = back(ramp(f, j, j + 8))
        w = int((260 if f < am else 520) * s) or 1
        y = 1600 if f < am else lerp(1600, 1000, easeOut(ramp(f, am, am + 12)))
        x = 800 if f < am else lerp(800, 760, easeOut(ramp(f, am, am + 12)))
        paste_c(c, jornal_img(max(20, w)), x, y)
    if f >= am: paste_c(c, txt('AMANHÃ!', 110, 5), 760, 640, back(ramp(f, am, am + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, am), 'day'


def s8(f):
    c = elevador_bg('dusk').copy()
    cr = wt(8, 'correndo') - 3
    ni = wt(8, 'ninguem') - 3
    portas(c, 1 - easeOut(ramp(f, cr + 10, cr + 30)), glow=True)
    visor(c, 13, red=True)
    x = lerp(900, 560, easeOut(ramp(f, cr - 6, cr + 12)))
    put_pes(c, x, 1820, 900, f, 4, expr='nervous' if f < ni else 'smug', arms='hang', look=-1, **DAVI)
    paste_c(c, jornal_img(220), x + 150, 1300)
    if f >= ni: paste_c(c, txt('SEGREDO...', 100, -5), 621, 560, back(ramp(f, ni, ni + 8)))
    return c, cam(f, 1.1, 1.15, 60, 1250, cr), 'dusk'


def s9(f):
    c = CEN('cidade', 'day').copy()
    ws = [(wt(9, 'chuva') - 3, 'CHUVA'), (wt(9, 'placar') - 3, '2 X 1'), (wt(9, 'prova') - 3, 'PROVA!')]
    if f >= ws[0][0]:
        d = ImageDraw.Draw(c); rnd = random.Random(f // 2)
        for i in range(70):
            x, y = rnd.randint(0, W_), rnd.randint(0, 1700)
            d.line((x, y, x - 14, y + 50), fill=(120, 170, 230, 200), width=5)
    put_pes(c, 621, 1820, 880, f, 7, expr='smug', arms='chin' if False else 'shrug', look=0, **DAVI)
    for i, (k, w) in enumerate(ws):
        if f >= k: paste_c(c, txt(w, 90, (-6, 5, -3)[i]), (360, 880, 621)[i], (700, 820, 560)[i], back(ramp(f, k, k + 8)))
    paste_c(c, jornal_img(240), 900, 1300)
    return c, cam(f, 1.05, 1.15, 100, 1250, ws[0][0]), 'day'


def s10(f):
    c = elevador_bg('dusk').copy()
    n = wt(10, 'noite') - 3
    portas(c, 0)
    visor(c, [12, 13][(f // 12) % 2], red=(f // 12) % 2 == 1)
    put_pes(c, 560, 1820, 900, f, 4, expr='smug', arms='hang', look=1, **DAVI)
    if f >= n: paste_c(c, txt('TODA NOITE', 100, -5), 621, 560, back(ramp(f, n, n + 8)))
    return c, cam(f, 1.05, 1.15, 70, 1250, n), 'dusk'


def s11(f):
    c = corredor_bg('day', True).copy()
    p = wt(11, 'porteiro') - 3
    so = wt(11, 'sorrindo') - 3
    put_pes(c, 330, 1820, 860, f, 6, expr='shock' if f >= p else 'neutral', arms='hang', look=1, **DAVI)
    if f >= p - 8:
        put_port(c, 900, 1820, 900 * back(ramp(f, p - 8, p)), f, 9, expr='grin' if f >= so else 'neutral', arms='hang', look=-1, **PORT)
    if f >= p: paste_c(c, txt('O PORTEIRO?!', 100, 5), 621, 560, back(ramp(f, p, p + 8)))
    return c, cam(f, 1.05, 1.12, 80, 1250, p), 'day'


def s12(f):
    c = corredor_bg('day', True).copy()
    co = wt(12, 'cochichou') - 3
    ch = wt(12, 'chao') - 3
    x = lerp(900, 720, easeOut(ramp(f, 0, co)))
    put_pes(c, 470, 1820, 860, f, 6, expr='shock' if f >= co + 10 else 'nervous', arms='up' if f >= ch else 'hang', look=1, **DAVI)
    put_port(c, x, 1820, 900, f, 9, expr='smug', arms='cheek' if f >= co else 'hang', look=-1, **PORT)
    if f >= co: paste_c(c, txt('PSST...', 90, -5), 621, 640, back(ramp(f, co, co + 8)))
    if f < ch: paste_c(c, jornal_img(200), 600, 1300)
    else: paste_c(c, jornal_img(200).rotate(-20, expand=True), 560, lerp(1300, 1720, easeOut(ramp(f, ch, ch + 10))))
    t = easeOut(ramp(f, co - 10, co + 20))
    z = lerp(1.05, 1.15, t) * (1 + .0009 * f)
    return c, (lerp(621, 600, t), lerp(1250, 1180, t) + kick(f, ch, .6) * 10, z, 0), 'day'


def s13(f):
    c = corredor_bg('dusk', False).copy()
    d2 = wt(13, 'dois') - 3
    put_prof(c, 621, 1820, 960, f, expr='nervous' if f < d2 else 'smug', arms='chin', look=0)
    if f >= d2: paste_c(c, txt('CONTINUA...', 110, -5), 621, 600, back(ramp(f, d2, d2 + 8)))
    t = easeOut(ramp(f, 0, 70))
    return c, (621, lerp(1300, 1250, t), lerp(1.03, 1.15, t) * (1 + .0006 * f), lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13]
