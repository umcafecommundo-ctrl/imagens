"""Formato DESENHO — FICÇÃO em 2 partes (pedido do Luis em 20/11/2026): "Os achados e perdidos de amanhã", PARTE 2.
História inventada (não é fato). SEM o Professor Bigode e SEM música (pedidos do Luis). Parte 1 em 2026-11-20-09h
(este arquivo carrega de lá a estação, o balcão, a Marina, a atendente e os objetos).
Cenários: s0-s6 estação de metrô (envelope, lista, balcão some, recado) | s7-s9 a mesma estação 50 anos depois (balcão
aparece, a senhora chama a Marina) | s10 estação à noite (era ela mesma)."""
from kit import *
import kit, os, importlib.util
from art import Pen, hexc, mul, ell_pts
from functools import lru_cache

_aqui = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('p1achados', os.path.join(_aqui, '..', '2026-11-20-09h', 'historia.py'))
P1 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(P1)
metro_bg, balcao, brilho, guarda_chuva, chave_img, envelope_img, icone, fala, cam, mao = (
    P1.metro_bg, P1.balcao, P1.brilho, P1.guarda_chuva, P1.chave_img, P1.envelope_img, P1.icone, P1.fala, P1.cam, P1.mao)
put_pes, put_at, MARINA, VELHA, INKA = P1.put_pes, P1.put_at, P1.MARINA, P1.VELHA, P1.INKA
pessoa, atendente = P1.pessoa, P1.atendente

MUSICA = False

LINES = [
    "Na parte um, um balcão de achados e perdidos devolvia as coisas da Marina antes de ela perder. Até entregar um envelope com a letra dela.",
    "A Marina abriu o envelope ali mesmo, na frente da senhora.",
    "Dentro, tinha uma lista comprida, com tudo que ela ia perder na vida.",
    "Guarda-chuva, chave, carteira... e óculos. Muitos óculos.",
    "E o último item da lista era: o balcão.",
    "A Marina levantou os olhos... e o balcão tinha sumido. Só sobrou a parede de azulejo.",
    "No pé da lista, tinha um recado: agora é a sua vez de cuidar dele.",
    "Cinquenta anos depois, numa estação de metrô, apareceu um balcão que ninguém lembra de ter visto antes.",
    "Atrás dele, uma senhora de óculos redondos vê uma moça distraída passando.",
    "Ela pega um guarda-chuva amarelo, sorri, e chama: Marina!",
    "Ou seja: a atendente sempre foi a Marina. A única coisa que ela nunca perdeu... foi ela mesma.",
]
CAPTXT = [
    "Na parte um, um balcão de achados e perdidos devolvia as coisas|da Marina antes de ela perder. Até entregar um envelope com a letra dela.",
    "A Marina abriu o envelope ali mesmo,|na frente da senhora.",
    "Dentro, tinha uma lista comprida,|com tudo que ela ia perder na vida.",
    "Guarda-chuva, chave, carteira...|e óculos. Muitos óculos.",
    "E o último item da lista era: o balcão.",
    "A Marina levantou os olhos... e o balcão tinha sumido.|Só sobrou a parede de azulejo.",
    "No pé da lista, tinha um recado:|agora é a sua vez de cuidar dele.",
    "Cinquenta anos depois, numa estação de metrô, apareceu|um balcão que ninguém lembra de ter visto antes.",
    "Atrás dele, uma senhora de óculos redondos|vê uma moça distraída passando.",
    "Ela pega um guarda-chuva amarelo, sorri,|e chama: Marina!",
    "Ou seja: a atendente sempre foi a Marina.|A única coisa que ela nunca perdeu... foi ela mesma.",
]
FALA_TIKTOK = "Você entendeu o final? Comenta sim ou não, e segue pra mais histórias!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 10
FLASH = [7]
CHECK = [(0, 'envelope', 4), (1, 'abriu', 4), (2, 'lista', 4), (3, 'oculos', 4), (4, 'balcao', 6), (5, 'sumido', 4),
         (6, 'vez', 6), (7, 'cinquenta', 4), (8, 'redondos', 4), (9, 'marina', 6), (10, 'mesma', 8)]


def SFX(s):
    for k in range(0, 60, 20): s.thunk(k, 70, .15)
    s.whoosh(s.W(1, 'abriu') - 4, .4, .3)
    s.whoosh(s.W(2, 'lista') - 4, .6, .3)
    for w in ('guarda-chuva', 'chave', 'carteira'): s.ting(s.W(3, w) - 1, .2)
    for i in range(5): s.thunk(s.W(3, 'muitos') - 2 + i * 4, 600, .25)
    s.thunk(s.W(4, 'balcao') - 2, 100, .9)
    s.whoosh(s.W(5, 'sumido') - 6, .7, .5); s.ting(s.W(5, 'sumido'), .3)
    s.ting(s.W(6, 'vez'), .3)
    s.trill(s.W(7, 'cinquenta'), .6, .2); s.ting(s.W(7, 'balcao'), .3)
    s.ting(s.W(9, 'marina'), .35)
    s.trill(s.W(10, 'mesma'), 1.0, .3)


@lru_cache(maxsize=8)
def lista_img(w, n=6, ultimo=False):
    p = Pen(500, 700)
    p.shape([(20, 20), (480, 20), (480, 680), (20, 680)], hexc('#fbf6e8'), hexc('#e0d6bd'), 6, 8)
    for i in range(n):
        y = 90 + i * 70
        p.stroke([(60, y), (80, y)], 6); p.stroke([(100, y), (100 + 260 + (i * 37) % 90, y)], 6, hexc('#7a6a8a'))
    im = p.img.resize((500, 700), Image.LANCZOS)
    if ultimo:
        t = txt('O BALCÃO', 64, -3)
        im.alpha_composite(t, (250 - t.width // 2, 600 - t.height // 2))
    return im.resize((w, int(w * 1.4)), Image.LANCZOS)


@lru_cache(maxsize=4)
def oculos_img(w):
    p = Pen(400, 200)
    for x in (110, 290):
        p.dot(x, 100, 70, hexc('#d9f0ff'), 8)
    p.arc(200, 100, 22, 18, 200, 340, 8)
    return p.img.resize((w, w // 2), Image.LANCZOS)


def s0(f):
    c = metro_bg('dusk').copy()
    en = wt(0, 'envelope') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='smug', arms='hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='nervous', arms='hang', look=-1, **MARINA)
    if f < 48: paste_c(c, txt('PARTE 2', 120, -4), 621, 760, back(ramp(f, 0, 8)) * (1 - ramp(f, 42, 48)))
    for i, w in enumerate(('guarda-chuva', 'chave')):
        k = wt(0, 'coisas') - 3 + i * 8
        if k <= f < en:
            im = guarda_chuva(300) if i == 0 else chave_img(200)
            paste_c(c, im, 560 + i * 200, 900, back(ramp(f, k, k + 8)))
    if f >= en: paste_c(c, envelope_img(240), 880, 1470, back(ramp(f, en, en + 8)))
    return c, cam(f, 1.05, 1.15, 120, 1250, en), 'dusk'


def s1(f):
    c = metro_bg('dusk').copy()
    ab = wt(1, 'abriu') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='smug', arms='hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 880, 1820, 860, f, 2, expr='nervous', arms='hang', look=-1, **MARINA)
    paste_c(c, envelope_img(240, aberto=f >= ab), 880, 1470)
    if f >= ab: paste_c(c, txt('RASG!', 100, -5), 640, 640, back(ramp(f, ab, ab + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, ab), 'dusk'


def s2(f):
    c = metro_bg('dusk').copy()
    li = wt(2, 'lista') - 3
    vi = wt(2, 'vida') - 3
    put_pes(c, 880, 1820, 860, f, 2, expr='shock' if f >= vi else 'nervous', arms='hang', look=-1, **MARINA)
    t = easeOut(ramp(f, li - 4, li + 14))
    paste_c(c, lista_img(int(lerp(200, 460, t))), lerp(880, 520, t), lerp(1460, 1050, t))
    if f >= vi: paste_c(c, txt('A VIDA TODA?!', 90, 5), 640, 560, back(ramp(f, vi, vi + 8)))
    return c, cam(f, 1.05, 1.12, 80, 1200, li), 'dusk'


def s3(f):
    c = metro_bg('dusk').copy()
    put_pes(c, 880, 1820, 860, f, 2, expr='nervous', arms='hang', look=-1, **MARINA)
    paste_c(c, lista_img(380), 480, 1080)
    items = [('guarda-chuva', lambda: guarda_chuva(260), 300, 640), ('chave', lambda: chave_img(220), 660, 640),
             ('carteira', lambda: icone('carteira', 200), 1000, 640)]
    for w, fn, x, y in items:
        k = wt(3, w) - 3
        if f >= k: paste_c(c, fn(), x, y, back(ramp(f, k, k + 8)))
    mu = wt(3, 'muitos') - 3
    oc = wt(3, 'oculos') - 3
    if f >= oc:
        rnd = random.Random(3)
        n = 1 + int(14 * ramp(f, mu, mu + 30))
        for i in range(n):
            x = rnd.randint(150, 1100); y = rnd.randint(820, 1500)
            paste_c(c, oculos_img(160).rotate(rnd.randint(-30, 30), Image.BICUBIC, expand=True), x, y, back(ramp(f, oc + i * 2, oc + i * 2 + 6)))
    if f >= mu: paste_c(c, txt('MUITOS!', 110, -5), 640, 520, back(ramp(f, mu, mu + 8)))
    return c, cam(f, 1.0, 1.08, 100, 1150), 'dusk'


def s4(f):
    c = metro_bg('dusk').copy()
    ul = wt(4, 'ultimo') - 3
    ba = wt(4, 'balcao') - 3
    paste_c(c, lista_img(560, ultimo=f >= ba), 621, 1100)
    if f >= ba: brilho(c, 621, 1460, f, .7 * back(ramp(f, ba, ba + 8)))
    t = easeOut(ramp(f, ul - 10, ba + 6))
    return c, (621, lerp(1100, 1350, t) + kick(f, ba, .8) * 10, lerp(1.0, 1.5, t) * (1 + .0006 * f), 0), 'dusk'


def s5(f):
    c = metro_bg('dusk').copy()
    le = wt(5, 'levantou') - 3
    su = wt(5, 'sumido') - 3
    az = wt(5, 'azulejo') - 3
    gone = ramp(f, su - 6, su + 4)
    if gone < 1:
        put_at(c, 380, 1650, 760 * (1 - gone), f, 9, expr='smug', arms='wave' if False else 'hang', look=1, **VELHA)
        balcao(c, 380, 1270, 1 - gone)
    brilho(c, 380, 1350, f, back(ramp(f, su - 6, su + 4)) * (1 - ramp(f, su + 20, su + 30)))
    put_pes(c, 880, 1820, 860, f, 2, expr='shock' if f >= su else 'nervous', arms='up' if f >= su else 'hang', look=-1, **MARINA)
    paste_c(c, lista_img(160), 880 - 140, 1340)
    if su <= f < az: paste_c(c, txt('SUMIU!', 120, -5), 621, 600, back(ramp(f, su, su + 8)))
    if f >= az: paste_c(c, txt('SÓ AZULEJO', 100, 4), 621, 600, back(ramp(f, az, az + 8)))
    return c, cam(f, 1.05, 1.15, 100, 1250, su), 'dusk'


def s6(f):
    c = metro_bg('night').copy()
    re = wt(6, 'recado') - 3
    vz = wt(6, 'vez') - 3
    put_pes(c, 621, 1820, 900, f, 2, expr='shock' if f >= vz else 'nervous', arms='hang', look=0, **MARINA)
    paste_c(c, lista_img(200), 621, 1500)
    if f >= re: fala(c, 'AGORA É A SUA VEZ.', 621, 700, 60, back(ramp(f, re, re + 8)))
    t = easeOut(ramp(f, 0, 80))
    return c, (621, lerp(1300, 1200, t) + kick(f, vz, .6) * 10, lerp(1.05, 1.25, t) * (1 + .0006 * f), 0), 'dusk'


def s7(f):
    c = metro_bg('day').copy()
    ci = wt(7, 'cinquenta') - 3
    ba = wt(7, 'balcao') - 3
    a = ramp(f, ba - 6, ba + 10)
    if f >= ba - 6:
        put_at(c, 380, 1650, 760 * back(ramp(f, ba, ba + 10)), f, 9, expr='neutral', arms='hang', look=.5, **VELHA)
    balcao(c, 380, 1270, a)
    brilho(c, 380, 1350, f, back(ramp(f, ba - 4, ba + 8)) * (1 - ramp(f, ba + 30, ba + 40)))
    if f >= ci: paste_c(c, txt('50 ANOS DEPOIS', 80, -4), 621, 600, back(ramp(f, ci, ci + 8)) * (1 - ramp(f, ba - 4, ba)))
    if f >= ba: paste_c(c, txt('DE NOVO?!', 100, 5), 640, 720, back(ramp(f, ba, ba + 8)))
    return c, cam(f, 1.15, 1.02, 80, 1250, ba), 'day'


def s8(f):
    c = metro_bg('day').copy()
    re = wt(8, 'redondos') - 3
    mo = wt(8, 'moca') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='grin' if f >= mo else 'neutral', arms='hang', look=1, **VELHA)
    balcao(c)
    x = lerp(1350, 900, easeOut(ramp(f, mo - 10, mo + 30)))
    put_pes(c, x, 1820, 860, f, 3, expr='neutral', arms='hang', look=1, **MARINA)
    if re <= f < mo: paste_c(c, txt('ÓCULOS REDONDOS', 74, -4), 621, 640, back(ramp(f, re, re + 8)))
    if f >= mo + 6: paste_c(c, txt('DISTRAÍDA...', 90, 4), 700, 640, back(ramp(f, mo + 6, mo + 14)))
    t = easeOut(ramp(f, 0, re))
    return c, (lerp(500, 621, t), 1290, lerp(1.6, 1.15, t) * (1 + .0006 * f), 0), 'day'


def s9(f):
    c = metro_bg('day').copy()
    gu = wt(9, 'guarda-chuva') - 3
    so = wt(9, 'sorri') - 3
    ma = wt(9, 'marina') - 3
    put_at(c, 380, 1650, 760, f, 9, expr='grin' if f >= so else 'neutral', arms='point' if f >= gu - 6 else 'hang', look=1, **VELHA)
    balcao(c)
    put_pes(c, 900, 1820, 860, f, 3, expr='shock' if f >= ma + 6 else 'neutral', arms='hang', look=-1 if f >= ma + 6 else 1, **MARINA)
    if f >= gu - 6:
        hx, hy = mao(380, 1650, 760)
        paste_c(c, guarda_chuva(380).rotate(-70, Image.BICUBIC, expand=True), hx + 60, hy + 10, back(ramp(f, gu - 6, gu + 2)))
    if f >= ma: fala(c, 'MARINA!', 520, 760, 90, back(ramp(f, ma, ma + 8)))
    return c, P1.cam(f, 1.05, 1.15, 90, 1250, ma), 'day'


def s10(f):
    c = metro_bg('dusk').copy()
    at = wt(10, 'atendente') - 3
    me = wt(10, 'mesma') - 3
    put_at(c, 400, 1820, 880, f, 9, expr='smug' if f < me else 'grin', arms='hang', look=1, **VELHA)
    put_pes(c, 840, 1820, 880, f, 3, expr='shock' if f < me else 'grin', arms='hang', look=-1, **MARINA)
    if f >= at and f < me: paste_c(c, txt('ERA ELA!', 110, -5), 621, 600, back(ramp(f, at + 6, at + 14)))
    if f >= me: paste_c(c, txt('ELA MESMA.', 110, 4), 621, 600, back(ramp(f, me, me + 8)))
    if f >= at:
        d = ImageDraw.Draw(c)
        s_ = back(ramp(f, at, at + 12))
        if s_ > .05:
            d.line((520, 1150, 720, 1150), fill=INKA, width=int(18 * s_))
            d.line((520, 1150, 720, 1150), fill=(255, 210, 60, 255), width=int(10 * s_))
            paste_c(c, txt('=', 120, 0), 621, 1060, s_)
    t = easeOut(ramp(f, 0, 90))
    return c, (621, lerp(1300, 1220, t) + kick(f, me, .7) * 10, lerp(1.05, 1.22, t) * (1 + .0006 * f), lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
