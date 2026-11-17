"""Formato DESENHO: a palavra OK nasceu de uma piada com erro de ortografia (Curiosidades da IA, 17/11/2026, 19h).
Categoria: HISTÓRIA.
Fatos: Smithsonian Magazine ("How One Man Discovered the Obscure Origins of the Word OK", sobre a pesquisa do linguista
Allen Walker Read): o OK apareceu impresso em 23/03/1839 num jornal de Boston; havia na Nova Inglaterra uma moda
("craze") de abreviações; muitas sumiram, como "SP" (small potatoes) e "KG" ("know go", grafia errada de "no go");
OK = "oll korrect", grafia de brincadeira de "all correct"; em 1840 o uso cresceu com a campanha presidencial
("Vote for OK", clubes OK); depois se espalhou pelo mundo. Confirmado também em wordorigins.org e New England Historical Society.
Cenários: s0 escola (Professor mostra o OK no quadro) | s1 redação de jornal de 1839 (moda de abreviar) |
s2 redação (all correct -> oll korrect) | s3 redação (nasce o O.K.) | s4 praça antiga em 1840 (campanha "VOTE OK") |
s5 redação ao entardecer (as outras abreviações somem) | s6 escola ao entardecer (Professor: foi escrita errada)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h10 = _load('h0810v', '2026-11-08-10h')
pessoa = _h10.pessoa

LINES = [
    "A palavra OK começou como uma piada... com erro de ortografia.",
    "Em mil oitocentos e trinta e nove, em Boston, os jornais viviam uma moda: abreviar tudo.",
    "E a graça era abreviar errado: em vez de all correct, que é tudo certo em inglês, escreviam ól korrect.",
    "Daí saiu o O K.",
    "No ano seguinte, ele virou slogan de campanha pra presidente e se espalhou pelo país.",
    "Você vê, as outras abreviações da moda sumiram. Só o OK sobreviveu.",
    "Ou seja: a palavra que a gente usa pra dizer que tá tudo certo... nasceu escrita errada.",
]
CAPTXT = [
    "A palavra OK começou como uma piada...|com erro de ortografia.",
    "Em 1839, em Boston, os jornais viviam uma moda:|abreviar tudo.",
    "E a graça era abreviar errado: em vez de \"all correct\",|que é tudo certo em inglês, escreviam \"oll korrect\".",
    "Daí saiu o O.K.",
    "No ano seguinte, ele virou slogan de campanha|pra presidente e se espalhou pelo país.",
    "Você vê, as outras abreviações da moda sumiram.|Só o OK sobreviveu.",
    "Ou seja: a palavra que a gente usa pra dizer|que tá tudo certo... nasceu escrita errada.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 5
FLASH = [4]
CHECK = [(0, 'piada', 4), (0, 'ortografia', 6), (1, 'boston', 4), (1, 'abreviar', 6), (2, 'errado', 4), (2, 'all', 4),
         (2, 'korrect', 6), (3, 'k', 6), (4, 'slogan', 4), (4, 'pais', 6), (5, 'sumiram', 4), (5, 'sobreviveu', 6),
         (6, 'certo', 4), (6, 'errada', 8)]

PAPEL = hexc('#f4ecd6'); PAPELD = hexc('#d8cba8')


def put_p(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


@lru_cache(maxsize=3)
def redacao(luz='day'):
    """redação de jornal de 1839: parede de madeira, janela, mesa com tinteiro e pena, lampião, prensa, pilhas de jornal."""
    W, H = 1242, 2208
    base = Image.new('RGBA', (W, H), hexc('#8a5f3c') + (255,))
    p = Pen(W, H)
    for x in range(0, W, 130):
        p.poly([(x, 0), (x + 124, 0), (x + 124, 1560), (x, 1560)], hexc('#9b6c45') if (x // 130) % 2 else hexc('#93653f'))
        p.stroke([(x, 0), (x, 1560)], 4, hexc('#6e4a2c'))
    ceu = {'day': ('#7fb6e6', '#d9ecf8'), 'golden': ('#e9a15c', '#ffd8a0'), 'dusk': ('#2b2f5c', '#c9837a')}[luz]
    p.shape([(140, 330), (560, 330), (560, 830), (140, 830)], hexc('#f2e6cc'), hexc('#d8c8a6'), 6, 6)
    p.poly([(165, 355), (535, 355), (535, 590), (165, 590)], hexc(ceu[0]))
    p.poly([(165, 590), (535, 590), (535, 805), (165, 805)], hexc(ceu[1]))
    p.line([(350, 355), (350, 805)], hexc('#f2e6cc'), 14, 3); p.line([(165, 580), (535, 580)], hexc('#f2e6cc'), 14, 3)
    # piso
    p.poly([(0, 1560), (W, 1560), (W, H), (0, H)], hexc('#6b4a30'))
    for y in range(1600, H, 110): p.stroke([(0, y), (W, y)], 4, hexc('#55392a'))
    p.stroke([(0, 1560), (W, 1560)], 7)
    # prensa (direita)
    pr = hexc('#3b3f46'); prd = hexc('#24272c')
    p.shape([(860, 900), (900, 900), (900, 1580), (860, 1580)], pr, prd, 6, 6)
    p.shape([(1140, 900), (1180, 900), (1180, 1580), (1140, 1580)], pr, prd, 6, 6)
    p.shape([(840, 860), (1200, 860), (1200, 930), (840, 930)], pr, prd, 6, 8)
    p.shape([(900, 1220), (1140, 1220), (1140, 1290), (900, 1290)], pr, prd, 6, 6)
    p.line([(1020, 930), (1020, 1220)], hexc('#8a8f99'), 26, 5)
    p.line([(950, 1000), (1090, 1000)], hexc('#8a8f99'), 16, 5)
    for i in range(5):  # pilha de jornais
        y = 1560 - i * 26
        p.shape([(900, y - 26), (1140, y - 26), (1140, y), (900, y)], PAPEL, PAPELD, 4, 4)
    # lampião pendurado
    p.stroke([(700, 0), (700, 180)], 5)
    p.shape([(660, 180), (740, 180), (760, 300), (640, 300)], hexc('#ffd77a') if luz != 'day' else hexc('#f4e3a8'), hexc('#d9b45a'), 5, 6)
    p.shape([(650, 300), (750, 300), (740, 330), (660, 330)], hexc('#3b3f46'), None, 4, 0)
    base.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    return base


@lru_cache(maxsize=2)
def mesa_img(w):
    p = Pen(900, 420)
    p.shape([(0, 0), (900, 0), (900, 60), (0, 60)], hexc('#5a3a22'), hexc('#43291a'), 6, 8)
    p.shape([(40, 60), (100, 60), (100, 420), (40, 420)], hexc('#43291a'), None, 5, 0)
    p.shape([(800, 60), (860, 60), (860, 420), (800, 420)], hexc('#43291a'), None, 5, 0)
    return p.img.resize((w, int(w * 420 / 900)), Image.LANCZOS)


@lru_cache(maxsize=32)
def folha_img(w, titulo='', corpo=('',), riscado=-1):
    """folha de jornal antiga com título e linhas de texto (corpo em letras grandes)."""
    p = Pen(700, 900)
    p.shape([(20, 20), (680, 20), (680, 880), (20, 880)], PAPEL, PAPELD, 6, 12)
    p.stroke([(50, 150), (650, 150)], 6); p.stroke([(50, 165), (650, 165)], 3)
    for y in range(620, 860, 50):
        p.stroke([(60, y), (330, y)], 6, hexc('#a89a7c')); p.stroke([(370, y), (640, y)], 6, hexc('#a89a7c'))
    im = p.img.resize((w, int(w * 900 / 700)), Image.LANCZOS)
    s = w / 700
    if titulo:
        t = txt(titulo, int(80 * s)); im.alpha_composite(t, ((im.size[0] - t.size[0]) // 2, int(40 * s)))
    for i, linha in enumerate(corpo):
        if not linha: continue
        t = txt(linha, int(90 * s)); x0 = (im.size[0] - t.size[0]) // 2; y0 = int((210 + i * 150) * s)
        im.alpha_composite(t, (x0, y0))
        if i == riscado:
            d = ImageDraw.Draw(im)
            yy = y0 + t.size[1] // 2
            d.line([(x0, yy), (x0 + t.size[0], yy)], fill=(220, 40, 40, 255), width=max(4, int(14 * s)))
    return im


@lru_cache(maxsize=2)
def praca_1840(luz='golden'):
    """praça de cidade em 1840: sobrados de tijolo, chão de pedra, palanque com bandeirolas."""
    W, H = 1242, 2208
    import cenarios
    base = cenarios._ceu(luz, 1300)
    p = Pen(W, H)
    rnd = random.Random(4)
    x = -40
    cores = ['#a5533c', '#8e4a36', '#b8664a', '#7d4a3a']
    while x < W:
        w = rnd.randint(260, 340); h = rnd.randint(520, 760); col = hexc(rnd.choice(cores))
        p.shape([(x, 1320 - h), (x + w, 1320 - h), (x + w, 1320), (x, 1320)], col, mul(col, .8), 6, 10)
        p.shape([(x - 10, 1320 - h - 30), (x + w + 10, 1320 - h - 30), (x + w + 10, 1320 - h), (x - 10, 1320 - h)], hexc('#5a3a2a'), None, 5, 0)
        for wy in range(1320 - h + 60, 1220, 150):
            for wx in range(x + 40, x + w - 60, 110):
                p.shape([(wx, wy), (wx + 60, wy), (wx + 60, wy + 90), (wx, wy + 90)], hexc('#f2e6c0') if luz != 'day' else hexc('#cfe3f2'), None, 4, 0)
        x += w + 8
    p.poly([(0, 1320), (W, 1320), (W, H), (0, H)], hexc('#a59a88'))
    for y in range(1350, H, 70):
        off = (y // 70) % 2 * 60
        for xx in range(-off, W, 120): p.arc(xx + 60, y, 54, 26, 0, 360, 3, hexc('#857a6a'))
    p.stroke([(0, 1320), (W, 1320)], 6)
    # palanque
    p.shape([(200, 1180), (1040, 1180), (1040, 1260), (200, 1260)], hexc('#8a5f3c'), hexc('#6b4a30'), 6, 8)
    for xx in (240, 620, 1000): p.shape([(xx - 14, 1260), (xx + 14, 1260), (xx + 14, 1400), (xx - 14, 1400)], hexc('#6b4a30'), None, 5, 0)
    # bandeirolas
    pts = [(xx, 480 + 40 * math.sin(xx / 200)) for xx in range(0, W + 1, 20)]
    p.stroke(pts, 4)
    for i, xx in enumerate(range(30, W, 90)):
        y = 480 + 40 * math.sin(xx / 200)
        col = hexc(('#c0392b', '#f4f1e6', '#2f5aa8')[i % 3])
        p.shape([(xx - 30, y), (xx + 30, y), (xx, y + 60)], col, None, 4, 0)
    base.alpha_composite(p.img.resize((W, H), Image.LANCZOS))
    return base


@lru_cache(maxsize=8)
def faixa_img(w, texto):
    p = Pen(1000, 300)
    p.shape([(20, 40), (980, 40), (950, 150), (980, 260), (20, 260), (50, 150)], hexc('#f4f1e6'), hexc('#d9d4c2'), 6, 10)
    p.poly([(20, 40), (980, 40), (980, 75), (20, 75)], hexc('#c0392b'))
    p.poly([(20, 225), (980, 225), (980, 260), (20, 260)], hexc('#2f5aa8'))
    im = p.img.resize((w, int(w * .3)), Image.LANCZOS)
    t = txt(texto, int(w * .11)); im.alpha_composite(t, ((im.size[0] - t.size[0]) // 2, (im.size[1] - t.size[1]) // 2))
    return im


def lousa(c, x, y, w, texto='', f=0, f0=0):
    p_ = Image.new('RGBA', (w, int(w * .6)), (0, 0, 0, 0)); d = ImageDraw.Draw(p_)
    d.rectangle((0, 0, w - 1, int(w * .6) - 1), fill=(46, 84, 60, 255), outline=(120, 80, 40, 255), width=18)
    if texto:
        t = txt(texto, int(w * .32))
        p_.alpha_composite(t, ((w - t.size[0]) // 2, (p_.size[1] - t.size[1]) // 2))
    paste_c(c, p_, x, y)


def SFX(s):
    s.ting(s.W(0, 'ok'), .3); s.thunk(s.W(0, 'ortografia') - 2, 160, .7)
    s.thunk(s.W(1, 'boston') - 2, 200, .5)
    for i in range(3): s.thunk(s.W(1, 'abreviar') - 2 + i * 6, 700, .25)
    s.thunk(s.W(2, 'errado') - 2, 140, .7); s.whoosh(s.W(2, 'korrect') - 6, .4, .4); s.ting(s.W(2, 'korrect'), .3)
    s.thunk(s.W(3, 'k') - 2, 100, 1.0)
    s.patter(s.W(4, 'slogan') - 4, s.W(4, 'pais') + 20, 14, .12)
    s.whoosh(s.W(5, 'sumiram') - 6, .5, .4); s.ting(s.W(5, 'sobreviveu'), .3)
    s.thunk(s.W(6, 'errada') - 2, 120, .9); s.trill(s.W(6, 'errada') + 8, 1.0, .3)


def s0(f):
    c = CEN('escola', 'day').copy()
    k = wt(0, 'ok') - 3
    pi = wt(0, 'piada') - 3
    o = wt(0, 'ortografia') - 3
    if f >= k: lousa(c, 760, 760, 620, 'OK', f, k)
    put_prof(c, 330, 1830, 980, f, expr='grin' if f < o else 'shock', arms='point' if f >= k else 'wave', look=1)
    if pi <= f < o: paste_c(c, txt('UMA PIADA?', 90, -5), 760, 470, back(ramp(f, pi, pi + 8)))
    if f >= o: paste_c(c, txt('ERRO!', 120, 6), 820, 470, back(ramp(f, o, o + 8)))
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1200 + kick(f, o, .6) * 10, z, 0), 'day'


def s1(f):
    c = redacao('day').copy()
    b = wt(1, 'boston') - 3
    a = wt(1, 'abreviar') - 3
    paste_c(c, mesa_img(760), 470, 1620)
    paste_c(c, folha_img(260, '1839', ('',)), 380, 1330)
    put_p(c, 560, 1800, 900, f, 2, expr='grin' if f >= a else 'neutral', arms='point' if f >= a else 'hang',
          shirt='#f4f1e6', vest='#4b3a2a', mous=True, look=1)
    if f >= b: paste_c(c, txt('BOSTON, 1839', 96, -4), 640, 520, back(ramp(f, b, b + 8)))
    if f >= a:
        for i, ab in enumerate(('S.P.', 'K.G.')):
            paste_c(c, txt(ab, 100, (-1) ** i * 8), 660 + i * 220, 720 + (i % 2) * 120, back(ramp(f, a + i * 6, a + i * 6 + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.1, 1.25, t) * (1 + .0009 * f)
    return c, (lerp(640, 680, t), lerp(1200, 1150, t), z, 0), 'day'


def s2(f):
    c = redacao('day').copy()
    er = wt(2, 'errado') - 3
    al = wt(2, 'all') - 3
    ko = wt(2, 'korrect') - 3
    if f < ko:
        im = folha_img(640, 'JORNAL', ('all correct',) if f >= al else ('',))
    else:
        im = folha_img(640, 'JORNAL', ('all correct', 'oll korrect'), riscado=0)
    paste_c(c, im, 640, 1150, back(ramp(f, 0, 8)))
    if er <= f < al + 20: paste_c(c, txt('ERRADO!', 110, -6), 640, 420, back(ramp(f, er, er + 8)))
    if al + 20 <= f < ko: paste_c(c, txt('= TUDO CERTO', 90, -4), 640, 420, back(ramp(f, al + 20, al + 28)))
    if f >= ko: paste_c(c, txt('DE PROPÓSITO!', 90, 5), 640, 420, back(ramp(f, ko, ko + 8)))
    t = smooth(ramp(f, 0, 140))
    z = lerp(1.15, 1.3, t) * (1 + .0009 * f)
    return c, (640, lerp(1100, 1050, t) + kick(f, ko, .5) * 8, z, 0), 'day'


def s3(f):
    c = redacao('golden').copy()
    k = wt(3, 'k') - 3
    o = wt(3, 'o', 1) - 3
    im = folha_img(560, 'JORNAL', ('oll korrect',))
    paste_c(c, im, 640, 1150)
    # O e K grandes saltam das iniciais
    if f >= o: paste_c(c, txt('O', 220, -6), 520, 640, back(ramp(f, o, o + 8)))
    if f >= k: paste_c(c, txt('K', 220, 6), 760, 640, back(ramp(f, k, k + 8)))
    put_p(c, 1030, 1850, 760, f, 2, expr='shock' if f >= k else 'grin', arms='up' if f >= k else 'hang',
          shirt='#f4f1e6', vest='#4b3a2a', mous=True, look=-1)
    z = lerp(1.25, 1.1, easeOut(ramp(f, 0, 30))) * (1 + .0009 * f)
    return c, (680, 1150 + kick(f, k, .8) * 12, z, kick(f, k, 2)), 'golden'


def s4(f):
    c = praca_1840('golden').copy()
    sl = wt(4, 'slogan') - 3
    pa = wt(4, 'pais') - 3
    paste_c(c, txt('1840', 110, -5), 640, 370, back(ramp(f, 2, 10)))
    if f >= sl: paste_c(c, faixa_img(760, 'VOTE OK!'), 620, 900, back(ramp(f, sl, sl + 9)))
    for i, (x, sd, kw) in enumerate(((180, 3, dict(hat='cowboy', shirt='#c0392b', susp=True)),
                                     (430, 4, dict(dress='#7a5c9e', bun=True)),
                                     (820, 5, dict(shirt='#f4f1e6', vest='#4b3a2a', mous=True)),
                                     (1070, 6, dict(shirt='#2fa38a', hat='cowboy')))):
        jump = 30 * abs(math.sin((f + i * 7) * .25)) if f >= sl else 0
        put_p(c, x, 1900 - jump, 760, f, sd, expr='grin', arms='up' if f >= sl else 'hang', look=0, **kw)
    if f >= pa: paste_c(c, txt('NO PAÍS INTEIRO!', 84, 5), 640, 660, back(ramp(f, pa, pa + 8)))
    t = smooth(ramp(f, 0, 100))
    z = lerp(1.2, 1.05, t) * (1 + .0009 * f)
    return c, (640, lerp(1150, 1220, t), z, 0), 'golden'


def s5(f):
    c = redacao('dusk').copy()
    su = wt(5, 'sumiram') - 3
    so = wt(5, 'sobreviveu') - 3
    for i, ab in enumerate(('S.P.', 'K.G.')):
        x = 400 + i * 440
        fall = clamp((f - su - i * 4) / 18) if f >= su else 0
        a = 1 - fall
        if a > 0: paste_c(c, txt(ab, 110, (-1) ** i * 8), x, 760 + fall * 500, a)
        if 0 < fall < 1: put_dust(c, x, 760 + fall * 500, 70, f - su - i * 4)
    s = 1 + .15 * back(ramp(f, so, so + 10)) if f >= so else 1
    paste_c(c, txt('OK', int(240 * s), -4), 640, 1200)
    if f >= so: paste_c(c, txt('SOBREVIVEU!', 96, 5), 640, 480, back(ramp(f, so, so + 8)))
    t = smooth(ramp(f, 0, 120))
    z = lerp(1.08, 1.3, t) * (1 + .0009 * f)
    return c, (640, lerp(1050, 1150, t), z, 0), 'dusk'


def s6(f):
    c = CEN('escola', 'dusk').copy()
    ce = wt(6, 'certo') - 3
    er = wt(6, 'errada') - 3
    lousa(c, 760, 760, 620, 'OK')
    if f >= ce:
        d = ImageDraw.Draw(c)
        k = clamp((f - ce) / 8)
        d.line([(890, 830), (930, 880), (930 + 80 * k, 880 - 140 * k)], fill=(255, 255, 255, 255), width=16)
    put_prof(c, 330, 1830, 1000, f, expr='smug' if f < er else 'shock', arms='point' if f < er else 'up', look=1)
    if er <= f < er + 32:
        paste_c(c, txt('ESCRITA', 100, -5), 600, 360, back(ramp(f, er, er + 8)))
        paste_c(c, txt('ERRADA!', 100, -5), 640, 480, back(ramp(f, er + 3, er + 11)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (620, lerp(1220, 1170, t) + kick(f, er, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
