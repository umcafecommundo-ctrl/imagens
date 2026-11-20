"""Formato DESENHO — FICÇÃO em 2 partes (pedido do Luis em 20/11/2026): "Os achados e perdidos de amanhã", PARTE 1.
História inventada (não é fato). SEM o Professor Bigode (pedido do Luis em 20/11/2026) e SEM música.
Parte 2 em 2026-11-20-12h (que carrega as funções de desenho deste arquivo).
Cenários: s0 estação de metrô (balcão aparece) | s1-s2 estação (atendente chama a Marina, guarda-chuva) | s3 cidade com
temporal | s4 estação (chave) | s5-s6 calçada da cidade (bolsa abre em cima do bueiro) | s7 estação ao entardecer
(ela entende) | s8 estação (luva, fone, carteira) | s9-s11 estação (envelope com a letra dela) | s12 estação à noite (continua)."""
from kit import *
import kit, os, importlib.util
from art import Pen, hexc, mul, ell_pts
from functools import lru_cache

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1108a', '2026-11-08-10h')
pessoa = _m.pessoa

MUSICA = False
W_, H_ = 1242, 2208
ROXO = '#7a5cc7'
MARINA = dict(skin=1, hair='#3b2a1e', bun=True, shirt=ROXO, pants='#2f3f66', pocket=False)
VELHA = dict(skin=1, hair='#dcdcdc', bun=True, shirt=ROXO, pants='#3b3b5a', pocket=False)
AMARELO = hexc('#ffd23f'); AMARELOD = hexc('#e0a81c'); INKA = INK + (255,)


def atendente(**kw):
    """a senhora do balcão: pessoa + óculos redondos."""
    im = pessoa(**kw).copy()
    p = Pen(600, 1000)
    lk = kw.get('look', 0) * 0
    for x in (268, 332):
        p.arc(x + lk, 272, 30, 30, 0, 360, 6)
    p.stroke([(298, 272), (302, 272)], 6)
    im.alpha_composite(p.img.resize(im.size, Image.LANCZOS))
    return im


kit.atendente = atendente
import art as _art; _art.atendente = atendente; _art.pessoa = pessoa; kit.pessoa = pessoa


def put_pes(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def put_at(c, x, feet, h, f, seed=9, **kw):
    kit._bean(c, 'atendente', x, feet, h, f, seed, **kw)


def mao(x, feet, h, flip=False):
    """posição da mão do braço 'point' da pessoa."""
    return x + (-1 if flip else 1) * .26 * h, feet - .595 * h


def _fin(p, base=None, cor='#000000'):
    b = base if base is not None else Image.new('RGBA', (W_, H_), hexc(cor) + (255,))
    b.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS)); return b


@lru_cache(maxsize=4)
def metro_bg(luz='day'):
    """estação de metrô: parede de azulejo, placa, túnel, plataforma."""
    p = Pen(W_, H_)
    wall = hexc('#e9eef2') if luz == 'day' else (hexc('#c9c3d6') if luz == 'dusk' else hexc('#8f8aa6'))
    p.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], wall)
    for y in range(0, 1560, 70): p.stroke([(0, y), (W_, y)], 3, mul(wall, .9))
    for r, y in enumerate(range(0, 1560, 70)):
        for x in range(-70 if r % 2 else 0, W_, 140): p.stroke([(x, y), (x, y + 70)], 3, mul(wall, .9))
    p.poly([(0, 560), (W_, 560), (W_, 640), (0, 640)], hexc('#2f8f6a'))   # faixa verde
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], hexc('#8d8f99'))
    p.poly([(0, 1560), (W_, 1560), (W_, 1610), (0, 1610)], hexc('#f2c84b'))  # faixa amarela
    p.stroke([(0, 1560), (W_, 1560)], 7)
    # túnel à direita
    p.shape([(1040, 700), (1242, 700), (1242, 1560), (1040, 1560)], hexc('#2a2a33'), None, 6, 0)
    # placa METRÔ
    p.shape([(420, 160), (820, 160), (820, 300), (420, 300)], hexc('#1f3b6e'), hexc('#142a52'), 6, 6)
    for x in (300, 900):
        p.poly([(x, 0), (x + 40, 0), (x + 30, 60), (x + 10, 60)], hexc('#fff6d6'))
    base = _fin(p)
    paste_c(base, txt('METRÔ', 90, 0), 620, 232)
    return base


@lru_cache(maxsize=2)
def balcao_img():
    p = Pen(560, 420)
    p.shape([(0, 40), (560, 40), (560, 420), (0, 420)], hexc('#9a6a40'), hexc('#6f4a2a'), 6, 14)
    p.shape([(-10, 0), (570, 0), (570, 50), (-10, 50)], hexc('#c08a5a'), hexc('#9a6a40'), 6, 6)
    p.shape([(60, 130), (500, 130), (500, 330), (60, 330)], hexc('#f4ecd8'), hexc('#d9ccb0'), 5, 6)
    im = p.img.resize((560, 420), Image.LANCZOS)
    t1 = txt('ACHADOS', 58, 0); t2 = txt('E PERDIDOS', 52, 0)
    im.alpha_composite(t1, (280 - t1.width // 2, 165 - t1.height // 2 + 20))
    im.alpha_composite(t2, (280 - t2.width // 2, 260 - t2.height // 2 + 10))
    return im


def balcao(c, x=380, top=1270, a=1.0):
    if a <= .02: return
    im = balcao_img()
    if a < 1:
        im = im.copy(); im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
    c.alpha_composite(im, (int(x - 280), int(top)))


def brilho(c, x, y, f, s=1.0):
    if s <= .05: return
    d = ImageDraw.Draw(c)
    for i in range(6):
        a = f * .08 + i * math.pi / 3
        r = (220 + 30 * math.sin(f * .3 + i)) * s
        px, py = x + r * math.cos(a), y + r * .6 * math.sin(a)
        k = 18 * s
        d.polygon([(px, py - k * 2), (px + k * .5, py), (px, py + k * 2), (px - k * .5, py)], fill=(255, 230, 120, 255), outline=INKA)
        d.polygon([(px - k * 2, py), (px, py + k * .5), (px + k * 2, py), (px, py - k * .5)], fill=(255, 230, 120, 255))


# ---------------------------------------------------------------- objetos
@lru_cache(maxsize=8)
def guarda_chuva(w, aberto=False):
    if aberto:
        p = Pen(600, 600)
        dome = [(300 + 280 * math.cos(a), 260 - 220 * math.sin(a)) for a in np.linspace(0, math.pi, 30)]
        bot = [(20 + i * 70, 260 + (20 if i % 2 else 0)) for i in range(9)]
        p.shape(dome + bot[::-1] if False else dome + list(reversed(bot)), AMARELO, AMARELOD, 6, 16)
        p.stroke([(300, 40), (300, 0)], 8)
        p.line([(300, 260), (300, 520), (290, 560), (250, 560), (240, 530)], INK, 12, 0)
        for x in (160, 440): p.stroke([(300, 40), (x, 262)], 4, AMARELOD)
        return p.img.resize((w, w), Image.LANCZOS)
    p = Pen(200, 600)
    p.shape([(100, 40), (140, 380), (100, 400), (60, 380)], AMARELO, AMARELOD, 6, 8)
    p.line([(100, 380), (100, 520), (90, 560), (55, 560), (45, 530)], INK, 12, 0)
    p.stroke([(100, 40), (100, 10)], 8)
    return p.img.resize((int(w / 3), w), Image.LANCZOS)


@lru_cache(maxsize=8)
def chave_img(w):
    p = Pen(400, 200)
    p.shape(ell_pts(90, 100, 70, 70, 30), AMARELO, AMARELOD, 6, 8)
    p.dot(90, 100, 26, (255, 255, 255, 0) if False else hexc('#ffffff'), 5)
    p.shape([(150, 85), (380, 85), (380, 115), (150, 115)], AMARELO, AMARELOD, 6, 4)
    p.shape([(300, 115), (330, 115), (330, 160), (300, 160)], AMARELO, AMARELOD, 5, 2)
    p.shape([(345, 115), (370, 115), (370, 150), (345, 150)], AMARELO, AMARELOD, 5, 2)
    return p.img.resize((w, w // 2), Image.LANCZOS)


@lru_cache(maxsize=8)
def envelope_img(w, nome='MARINA', aberto=False):
    p = Pen(500, 340)
    p.shape([(10, 10), (490, 10), (490, 330), (10, 330)], hexc('#fbf6e8'), hexc('#e0d6bd'), 6, 8)
    if aberto:
        p.shape([(10, 10), (250, -120), (490, 10)], hexc('#efe6cc'), None, 6, 0)
    else:
        p.line([(10, 10), (250, 190), (490, 10)], INK, 6, 0)
    im = p.img.resize((500, 340), Image.LANCZOS)
    if nome:
        t = txt(nome, 70, -4)
        im.alpha_composite(t, (250 - t.width // 2, 250 - t.height // 2))
    return im.resize((w, int(w * .68)), Image.LANCZOS)


@lru_cache(maxsize=8)
def icone(nome, w):
    p = Pen(400, 400)
    if nome == 'luva':
        p.shape([(110, 380), (100, 200), (90, 110), (130, 100), (150, 190), (160, 70), (200, 60), (210, 180), (230, 60),
                 (270, 70), (265, 190), (300, 100), (335, 115), (300, 260), (300, 380)], hexc('#e2362f'), hexc('#a8231e'), 6, 10)
        p.shape([(100, 330), (310, 330), (310, 390), (100, 390)], hexc('#ffffff'), hexc('#dddddd'), 5, 4)
    elif nome == 'fone':
        p.arc(200, 220, 140, 150, 180, 360, 22)
        for x in (60, 340):
            p.shape(ell_pts(x, 250, 50, 80, 24), hexc('#3fa7d6'), hexc('#2b7ea3'), 6, 8)
    elif nome == 'carteira':
        p.shape([(40, 110), (360, 110), (360, 320), (40, 320)], hexc('#8a5a32'), hexc('#653f20'), 6, 10)
        p.shape([(220, 170), (380, 170), (380, 260), (220, 260)], hexc('#a8703f'), hexc('#8a5a32'), 5, 4)
        p.dot(310, 215, 14, AMARELO, 3)
    elif nome == 'bolsa':
        p.arc(200, 150, 110, 110, 180, 360, 14)
        p.shape([(50, 150), (350, 150), (370, 380), (30, 380)], hexc('#c0563a'), hexc('#8e3a24'), 6, 12)
        p.shape([(50, 150), (350, 150), (330, 210), (70, 210)], hexc('#d86a4a'), None, 5, 0)
    return p.img.resize((w, w), Image.LANCZOS)


def bueiro(c, x, y, w):
    d = ImageDraw.Draw(c)
    d.ellipse((x - w / 2, y - w / 6, x + w / 2, y + w / 6), fill=(40, 40, 48, 255), outline=INKA, width=7)
    for i in range(1, 6):
        xx = x - w / 2 + i * w / 6
        d.line((xx, y - w / 6 + 10, xx, y + w / 6 - 10), fill=(110, 110, 120, 255), width=8)


def chuva(c, f, n=80, a=200):
    d = ImageDraw.Draw(c); rnd = random.Random(f // 2)
    for i in range(n):
        x, y = rnd.randint(0, W_), rnd.randint(0, 1800)
        d.line((x, y, x - 14, y + 50), fill=(150, 190, 240, a), width=5)


def fala(c, s, x, y, size=80, sc=1.0, rot=-3):
    """balão de fala com texto."""
    if sc <= .02: return
    t = txt(s, size, 0)
    w, h = t.width + 80, t.height + 60
    b = Image.new('RGBA', (w + 20, h + 70), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.rounded_rectangle((6, 6, w + 6, h + 6), 40, fill=(255, 255, 255, 255), outline=INKA, width=7)
    d.polygon([(60, h), (90, h + 60), (130, h)], fill=(255, 255, 255, 255), outline=INKA)
    d.line([(64, h + 1), (126, h + 1)], fill=(255, 255, 255, 255), width=8)
    b.alpha_composite(t, (46, 36))
    b = b.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, b, x, y, sc)


def cam(f, z0, z1, dur=80, cy=1250, k=0, cx=621):
    return (cx, cy + 40 + (kick(f, k, .6) * 10 if k else 0), 1.12 * lerp(z0, z1, smooth(ramp(f, 0, dur))) * (1 + .0009 * f), 0)


# ---------------------------------------------------------------- roteiro
LINES = [
    "Numa estação de metrô, apareceu um balcão de achados e perdidos que ninguém lembra de ter visto antes.",
    "Numa segunda-feira, a Marina passou por ali, e a atendente, uma senhora de óculos redondos, chamou o nome dela.",
    "Ela entregou um guarda-chuva amarelo. Era da Marina... mas ela não tinha perdido nada.",
    "Na saída, desabou um temporal que ninguém esperava.",
    "Na terça, a senhora devolveu a chave de casa dela.",
    "Uma hora depois, a Marina tropeçou na calçada, e a bolsa abriu bem em cima de um bueiro.",
    "Se a chave estivesse lá dentro, tinha sumido pra sempre.",
    "Aí ela entendeu: aquele balcão devolvia as coisas antes de ela perder.",
    "Todo dia, uma coisa nova: a luva, o fone, a carteira. Sempre um passo antes do azar.",
    "Até que, na sexta, a senhora não tinha objeto nenhum pra devolver.",
    "Ela entregou um envelope fechado, com o nome da Marina escrito... na letra da própria Marina.",
    "E disse só uma frase: esse aqui, você vai perder hoje.",
    "O que tinha dentro do envelope... fica pra parte dois.",
]
CAPTXT = [
    "Numa estação de metrô, apareceu um balcão de achados|e perdidos que ninguém lembra de ter visto antes.",
    "Numa segunda-feira, a Marina passou por ali, e a atendente,|uma senhora de óculos redondos, chamou o nome dela.",
    "Ela entregou um guarda-chuva amarelo.|Era da Marina... mas ela não tinha perdido nada.",
    "Na saída, desabou um temporal que ninguém esperava.",
    "Na terça, a senhora devolveu a chave de casa dela.",
    "Uma hora depois, a Marina tropeçou na calçada,|e a bolsa abriu bem em cima de um bueiro.",
    "Se a chave estivesse lá dentro, tinha sumido pra sempre.",
    "Aí ela entendeu: aquele balcão devolvia as coisas|antes de ela perder.",
    "Todo dia, uma coisa nova: a luva, o fone, a carteira.|Sempre um passo antes do azar.",
    "Até que, na sexta, a senhora não tinha objeto nenhum|pra devolver.",
    "Ela entregou um envelope fechado, com o nome da Marina|escrito... na letra da própria Marina.",
    "E disse só uma frase: esse aqui, você vai perder hoje.",
    "O que tinha dentro do envelope... fica pra parte dois.",
]
FALA_TIKTOK = "Quer a parte dois? Comenta sim, e segue pra não perder!"
CTA_TEXTO = "COMENTA: SIM!"
TWIST = 7
FLASH = [3, 5]
CHECK = [(0, 'balcao', 4), (1, 'nome', 4), (2, 'amarelo', 4), (2, 'nada', 6), (3, 'temporal', 4), (4, 'chave', 4),
         (5, 'bueiro', 4), (6, 'sempre', 4), (7, 'antes', 6), (8, 'luva', 4), (8, 'fone', 4), (8, 'carteira', 4),
         (9, 'nenhum', 4), (10, 'envelope', 4), (10, 'propria', 6), (11, 'hoje', 6), (12, 'dois', 8)]


def SFX(s):
    for k in range(0, 60, 20): s.thunk(k, 70, .15)
    s.ting(s.W(0, 'balcao'), .35); s.trill(s.W(0, 'antes'), .5, .15)
    s.ting(s.W(1, 'nome'), .3)
    s.whoosh(s.W(2, 'guarda-chuva') - 4, .4, .3); s.thunk(s.W(2, 'nada') - 2, 200, .5)
    s.thunk(s.W(3, 'temporal') - 2, 70, 1.0); s.patter(s.W(3, 'temporal'), s.W(3, 'temporal') + 70, 24, .12)
    s.ting(s.W(4, 'chave'), .35)
    s.thunk(s.W(5, 'tropecou') - 2, 160, .7); s.whoosh(s.W(5, 'abriu') - 4, .4, .3); s.thunk(s.W(5, 'bueiro') - 2, 320, .4)
    s.splash(s.W(6, 'sumido') - 2, .25)
    s.ting(s.W(7, 'entendeu'), .3)
    for w in ('luva', 'fone', 'carteira'): s.ting(s.W(8, w) - 1, .25)
    s.thunk(s.W(9, 'nenhum') - 2, 150, .5)
    s.whoosh(s.W(10, 'envelope') - 4, .4, .3); s.thunk(s.W(10, 'propria') - 2, 120, .8)
    s.whoosh(s.W(11, 'frase') - 4, .5, .2); s.thunk(s.W(11, 'hoje') - 2, 90, .9)
    s.trill(s.W(12, 'dois'), 1.0, .3)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = metro_bg('day').copy()
    b = wt(0, 'balcao') - 3
    ni = wt(0, 'ninguem') - 3
    a = ramp(f, b - 6, b + 10)
    put_at(c, 380, 1650, 760 * back(ramp(f, b, b + 10)), f, 9, expr='neutral', arms='hang', look=.5, **VELHA)
    balcao(c, 380, 1270, a)
    brilho(c, 380, 1350, f, back(ramp(f, b - 4, b + 8)) * (1 - ramp(f, b + 30, b + 40)))
    if f < 48: paste_c(c, txt('PARTE 1', 120, -4), 621, 760, back(ramp(f, 0, 8)) * (1 - ramp(f, 42, 48)))
    if f >= ni: paste_c(c, txt('APARECEU?!', 100, 5), 640, 760, back(ramp(f, ni, ni + 8)))
    return c, cam(f, 1.25, 1.05, 70, 1250, b), 'day'


def s1(f):
    c = metro_bg('day').copy()
    se = wt(1, 'senhora') - 3
    no = wt(1, 'nome') - 3
    x = lerp(1300, 900, easeOut(ramp(f, 0, 50)))
    put_at(c, 380, 1650, 760, f, 9, expr='grin' if f >= no else 'neutral', arms='point' if f >= no else 'hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, x, 1820, 860, f, 2, expr='shock' if f >= no else 'neutral', arms='hang', look=-1, **MARINA)
    paste_c(c, txt('MARINA', 80, -4), x, 760, back(ramp(f, 10, 18)) * (1 - ramp(f, se - 6, se)))
    if f >= se and f < no:
        d = ImageDraw.Draw(c)
        for xx in (380 - 32 * .76, 380 + 32 * .76):
            pass
        paste_c(c, txt('ÓCULOS REDONDOS', 70, 4), 621, 720, back(ramp(f, se, se + 8)))
    if f >= no: fala(c, 'MARINA!', 520, 760, 90, back(ramp(f, no, no + 8)))
    return c, cam(f, 1.05, 1.12, 90, 1250, no), 'day'


def s2(f):
    c = metro_bg('day').copy()
    g = wt(2, 'guarda-chuva') - 3
    na = wt(2, 'nada') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='grin', arms='point' if f >= g - 10 else 'hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='shock' if f >= na else 'nervous', arms='ask' if f >= na else 'hang', look=-1, **MARINA)
    if f >= g - 10:
        hx, hy = mao(380, 1650, 760)
        paste_c(c, guarda_chuva(380).rotate(-70, Image.BICUBIC, expand=True), hx + 60, hy + 10, back(ramp(f, g - 10, g)))
    if f >= g and f < na: paste_c(c, txt('É MEU!', 100, -5), 880, 700, back(ramp(f, g + 10, g + 18)))
    if f >= na: paste_c(c, txt('MAS EU NÃO PERDI!', 72, 4), 640, 720, back(ramp(f, na, na + 8)))
    return c, cam(f, 1.05, 1.15, 100, 1250, na), 'day'


def s3(f):
    c = CEN('cidade', 'dusk').copy()
    t = wt(3, 'temporal') - 3
    if f >= t: chuva(c, f)
    op = easeOut(ramp(f, t + 2, t + 14))
    put_pes(c, 621, 1820, 900, f, 3, expr='grin' if f >= t + 14 else 'neutral', arms='up' if f >= t else 'hang', look=0, **MARINA)
    if op > .1: paste_c(c, guarda_chuva(620, True), 621, 900, op)
    else: paste_c(c, guarda_chuva(320), 760, 1450)
    if f >= t: paste_c(c, txt('TEMPORAL!', 110, -5), 621, 520, back(ramp(f, t, t + 8)))
    sh = 5 * math.sin(f * 1.9) if t <= f < t + 12 else 0
    return c, (621 + sh, 1150, lerp(1.0, 1.1, smooth(ramp(f, 0, 80))) * (1 + .0009 * f), sh * .2), 'dusk'


def s4(f):
    c = metro_bg('day').copy()
    ch = wt(4, 'chave') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='grin', arms='point' if f >= ch - 8 else 'hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='shock' if f >= ch else 'neutral', arms='hang', look=-1, **MARINA)
    paste_c(c, txt('TERÇA', 100, -4), 621, 560, back(ramp(f, 2, 10)) * (1 - ramp(f, ch - 6, ch)))
    if f >= ch - 8:
        hx, hy = mao(380, 1650, 760)
        paste_c(c, chave_img(220), hx + 80, hy, back(ramp(f, ch - 8, ch)))
        brilho(c, hx + 80, hy, f, .4 * back(ramp(f, ch, ch + 8)))
    if f >= ch: paste_c(c, txt('MINHA CHAVE?', 90, 5), 640, 640, back(ramp(f, ch, ch + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, ch), 'day'


def s5(f):
    c = CEN('cidade', 'day').copy()
    tr = wt(5, 'tropecou') - 3
    ab = wt(5, 'abriu') - 3
    bu = wt(5, 'bueiro') - 3
    bueiro(c, 700, 1760, 300)
    x = lerp(300, 560, ramp(f, 0, tr))
    tilt = 'shock' if f >= tr else 'neutral'
    put_pes(c, x, 1820, 860, f, 4, expr=tilt, arms='up' if f >= tr else 'hang', look=1, **MARINA)
    if f < ab: paste_c(c, icone('bolsa', 200), x + 170, 1350)
    else:
        bx = lerp(x + 170, 700, easeOut(ramp(f, ab, ab + 12))); by = lerp(1350, 1640, easeOut(ramp(f, ab, ab + 12)))
        paste_c(c, icone('bolsa', 200).rotate(-30 * ramp(f, ab, ab + 12), Image.BICUBIC, expand=True), bx, by)
        for i in range(4):
            t = ramp(f, ab + 6 + i * 3, ab + 22 + i * 3)
            if 0 < t < 1:
                d = ImageDraw.Draw(c); yy = lerp(1650, 1770, t); xx = 640 + i * 40
                d.ellipse((xx - 16, yy - 16, xx + 16, yy + 16), fill=(255, 210, 60, 255), outline=INKA, width=4)
    if f >= bu: paste_c(c, txt('BUEIRO!', 110, -5), 621, 820, back(ramp(f, bu, bu + 8)))
    sh = 8 * math.sin(f * 2) if tr <= f < tr + 8 else 0
    return c, (621 + sh, lerp(1250, 1380, smooth(ramp(f, tr, bu + 10))), lerp(1.05, 1.2, smooth(ramp(f, 0, 100))) * (1 + .0009 * f), sh * .3), 'day'


def s6(f):
    c = CEN('cidade', 'day').copy()
    so = wt(6, 'sempre') - 3
    bueiro(c, 621, 1720, 420)
    put_pes(c, 360, 1820, 820, f, 4, expr='nervous' if f < so else 'pained', arms='point', look=1, **MARINA)
    hx, hy = mao(360, 1820, 820)
    paste_c(c, chave_img(200), hx + 60, hy)
    cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
    k = chave_img(220); cont.alpha_composite(k, (40, 100))
    d = ImageDraw.Draw(cont); d.line((40, 40, 260, 260), fill=(226, 59, 59, 255), width=20); d.line((260, 40, 40, 260), fill=(226, 59, 59, 255), width=20)
    thought(c, 880, 760, 230, back(ramp(f, 4, 14)), cont)
    if f >= so: paste_c(c, txt('UFA!', 110, -5), 560, 560, back(ramp(f, so, so + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, so), 'day'


def s7(f):
    c = metro_bg('dusk').copy()
    en = wt(7, 'entendeu') - 3
    an = wt(7, 'antes') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='smug', arms='hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='shock' if f >= en else 'nervous', arms='ask' if f >= an else 'hang', look=-1, **MARINA)
    if f >= an:
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        cont.alpha_composite(clock_img(-(f - an) * .08, -(f - an) * .9, 260), (20, 20))
        thought(c, 880, 680, 220, back(ramp(f, an, an + 8)), cont)
        paste_c(c, txt('ANTES DE PERDER!', 70, -4), 640, 1060, back(ramp(f, an + 4, an + 12)))
    return c, cam(f, 1.05, 1.18, 90, 1250, an), 'dusk'


def s8(f):
    c = metro_bg('day').copy()
    put_at(c, 380, 1650, 760, f, 9, expr='grin', arms='point', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='grin', arms='hang', look=-1, **MARINA)
    hx, hy = mao(380, 1650, 760)
    ws = ['luva', 'fone', 'carteira']
    ks = [wt(8, w) - 3 for w in ws] + [wt(8, 'azar') - 3]
    for i, w in enumerate(ws):
        if ks[i] <= f < ks[i + 1]:
            paste_c(c, icone(w, 200), hx + 70, hy, back(ramp(f, ks[i], ks[i] + 6)))
            paste_c(c, txt(w.upper(), 100, (-5, 4, -3)[i]), 640, 620, back(ramp(f, ks[i], ks[i] + 6)))
    az = wt(8, 'azar') - 3
    if f >= az: paste_c(c, txt('UM PASSO ANTES', 84, 4), 640, 620, back(ramp(f, az, az + 8)))
    return c, (621, 1250, (1.06 + .03 * math.sin(f * .05)) * (1 + .0006 * f), 0), 'day'


def s9(f):
    c = metro_bg('day').copy()
    se = wt(9, 'sexta') - 3
    ne = wt(9, 'nenhum') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='stern' if f >= ne else 'neutral', arms='shrug' if f >= ne else 'hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='nervous' if f >= ne else 'grin', arms='hang', look=-1, **MARINA)
    if se <= f < ne: paste_c(c, txt('SEXTA', 110, -4), 621, 600, back(ramp(f, se, se + 8)))
    if f >= ne: paste_c(c, txt('NADA?', 120, 5), 640, 620, back(ramp(f, ne, ne + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, ne), 'day'


def s10(f):
    c = metro_bg('dusk').copy()
    en = wt(10, 'envelope') - 3
    le = wt(10, 'letra') - 3
    pr = wt(10, 'propria') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='smug', arms='point' if f >= en - 8 else 'hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='shock' if f >= pr else 'nervous', arms='up' if f >= pr else 'hang', look=-1, **MARINA)
    if f >= en - 8:
        hx, hy = mao(380, 1650, 760)
        t = easeOut(ramp(f, le - 10, le + 6))
        w = int(lerp(200, 520, t))
        paste_c(c, envelope_img(w), lerp(hx + 80, 621, t), lerp(hy, 820, t), back(ramp(f, en - 8, en)))
    if f >= pr: paste_c(c, txt('A LETRA DELA!', 84, -4), 640, 560, back(ramp(f, pr, pr + 8)))
    return c, cam(f, 1.05, 1.15, 90, 1200, pr), 'dusk'


def s11(f):
    c = metro_bg('dusk').copy()
    fr = wt(11, 'frase') - 3
    ho = wt(11, 'hoje') - 3
    put_at(c, 560, 1650, 900, f, 9, expr='stern' if f >= ho else 'neutral', arms='hang', look=0, **VELHA)
    balcao(c, 560, 1330)
    if f >= fr: fala(c, 'VOCÊ VAI PERDER HOJE.', 600, 700, 54, back(ramp(f, fr, fr + 8)))
    t = smooth(ramp(f, 0, 90))
    return c, (lerp(621, 580, t), lerp(1200, 1080, t) + kick(f, ho, .7) * 10, lerp(1.05, 1.35, t) * (1 + .0006 * f), 0), 'dusk'


def s12(f):
    c = metro_bg('night').copy()
    d2 = wt(12, 'dois') - 3
    put_pes(c, 621, 1820, 900, f, 2, expr='nervous', arms='hang', look=0, **MARINA)
    paste_c(c, envelope_img(260), 621, 1480)
    if f >= d2: paste_c(c, txt('CONTINUA...', 110, -5), 621, 600, back(ramp(f, d2, d2 + 8)))
    t = easeOut(ramp(f, 0, 70))
    return c, (621, lerp(1300, 1220, t), lerp(1.03, 1.18, t) * (1 + .0006 * f), lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
