"""Formato DESENHO — FICÇÃO em 2 partes (pedido do Luis em 15/11/2026): "O elevador do 13º andar", PARTE 2.
História inventada (não é fato), narrada pelo Professor Bigode. Parte 1 em 2026-11-16-12h. Mais longa (~1 min).
SEM música de fundo: só voz e sons ambientes.
Cenários: s0 corredor à noite (Professor + PARTE 2, resumo) | s1 corredor do 13º (porteiro cochicha) | s2 corredor do 13º
(virada: é o prédio de amanhã) | s3 elevador (quem desce volta sabendo o futuro) | s4 portaria antiga (30 anos atrás) |
s5 portaria (porteiro sabe quem vai chegar) | s6 corredor do 13º (jornal: elevador quebrado) | s7 corredor (Davi entende) |
s8 elevador (2:59, segura a porta) | s9 corredor do 13º (porteiro hesita e entra) | s10 elevador (luz pisca, 12º, hoje) |
s11 portaria de dia (elevador quebrado, vazio) | s12 portaria (Professor e porteiro: não sabe o amanhã)."""
from kit import *
import kit, os, importlib.util
from art import Pen, hexc, mul, ell_pts

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_p1 = _load('h1116p1', '2026-11-16-12h')
pessoa, porteiro = _p1.pessoa, _p1.porteiro
elevador_bg, corredor_bg, portas, visor, jornal_img, cam = _p1.elevador_bg, _p1.corredor_bg, _p1.portas, _p1.visor, _p1.jornal_img, _p1.cam
DAVI, PORT, _fin, W_, H_ = _p1.DAVI, _p1.PORT, _p1._fin, _p1.W_, _p1.H_
PORT_JOVEM = dict(PORT, hair='#2b1d14')


def put_pes(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def put_port(c, x, feet, h, f, seed=9, **kw):
    kit._bean(c, 'porteiro', x, feet, h, f, seed, **kw)


MUSICA = False


@lru_cache(maxsize=4)
def portaria_bg(luz='day', velha=False):
    p = Pen(W_, H_)
    wall = hexc('#d9c9a8') if velha else (hexc('#dfe6ea') if luz == 'day' else hexc('#9aa2b5'))
    p.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], wall)
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], hexc('#7a6a5a') if velha else hexc('#6b7280'))
    for x in range(0, W_, 120):
        for y in range(1600, H_, 120):
            if (x // 120 + y // 120) % 2: p.poly([(x, y), (x + 120, y), (x + 120, y + 120), (x, y + 120)], hexc('#5a4d40') if velha else hexc('#5b616d'))
    p.stroke([(0, 1560), (W_, 1560)], 7)
    # porta de vidro da rua à esquerda
    p.shape([(60, 560), (420, 560), (420, 1560), (60, 1560)], hexc('#9fd0ef') if luz == 'day' else hexc('#2c3657'), None, 6, 0)
    p.stroke([(240, 560), (240, 1560)], 6)
    # balcão do porteiro
    p.shape([(640, 1240), (1220, 1240), (1220, 1600), (640, 1600)], hexc('#8a5a34'), hexc('#5e3c22'), 6, 12)
    p.shape([(620, 1200), (1240, 1200), (1240, 1250), (620, 1250)], hexc('#a8744a'), None, 5, 0)
    # interfone na parede
    p.shape([(1040, 760), (1160, 760), (1160, 960), (1040, 960)], hexc('#e9ecef'), hexc('#c4cad1'), 5, 4)
    for r in range(3): p.dot(1100, 800 + r * 50, 12, hexc('#5a5f6b'), 2)
    return _fin(p)


def SFX(s):
    s.whoosh(s.W(0, 'jornal') - 4, .5, .3)
    s.whoosh(s.W(1, 'cochichou') - 4, .6, .3)
    s.thunk(s.W(2, 'amanha') - 2, 120, .9); s.ting(s.W(2, 'amanha') + 3, .3)
    s.ting(s.W(3, 'futuro'), .3)
    s.patter(s.W(4, 'trinta') - 6, s.W(4, 'trinta') + 30, 4, .12)
    s.trill(s.W(5, 'interfone'), .7, .25)
    s.thunk(s.W(6, 'quebrado') - 2, 140, .9)
    s.thunk(s.W(7, 'sozinho') - 2, 200, .5)
    for i in range(3): s.thunk(s.W(8, 'treze') - 2 + i * 3, 900, .2)
    s.thunk(s.W(8, 'porta', 0) - 2, 260, .6)
    s.patter(s.W(9, 'entrou') - 10, s.W(9, 'entrou') + 8, 8, .2)
    s.thunk(s.W(10, 'piscou') - 2, 80, .8); s.ting(s.W(10, 'hoje'), .3)
    s.thunk(s.W(11, 'quebrou') - 2, 100, 1.0)
    s.trill(s.W(12, 'amanha'), 1.0, .3)
    for si in (3, 8, 10):
        a0 = s.W(si, LINES[si].split()[0].strip(',.:'))
        for k in range(0, 90, 30): s.thunk(a0 + k, 60, .15)


LINES = [
    "Na parte um, o Davi descobriu que o elevador do prédio para num décimo terceiro andar que não existe, e que lá o jornal chega com a data de amanhã.",
    "Até que o porteiro apareceu no corredor e cochichou: eu moro aqui.",
    "Você vê, o décimo terceiro andar não é um andar. É o prédio... de amanhã.",
    "Quem desce lá pisa no dia seguinte por alguns minutos, e volta sabendo o futuro.",
    "E o porteiro desceu lá há trinta anos, ficou tempo demais, e desde então vive sempre um dia na frente de todo mundo.",
    "É por isso que ele sabe quem vai chegar antes de tocar o interfone.",
    "Ele mostrou ao Davi o jornal de amanhã. Na primeira página: elevador do prédio quebrado.",
    "E o Davi entendeu: sem elevador, o porteiro ia ficar preso no amanhã pra sempre, sozinho.",
    "Então, às duas e cinquenta e nove, o Davi apertou o treze e segurou a porta aberta.",
    "O porteiro olhou pro corredor claro, respirou fundo... e entrou.",
    "A luz piscou, o elevador tremeu, e a porta abriu no décimo segundo, de madrugada, no dia de hoje.",
    "No dia seguinte, o elevador quebrou, como o jornal dizia. Mas não tinha ninguém preso lá dentro.",
    "Ou seja: depois de trinta anos, o porteiro finalmente voltou pro presente... e não fazia a menor ideia do que ia acontecer amanhã.",
]
CAPTXT = [
    "Na parte um, o Davi descobriu que o elevador para num 13º andar|que não existe, e que lá o jornal chega com a data de amanhã.",
    "Até que o porteiro apareceu no corredor|e cochichou: eu moro aqui.",
    "Você vê, o 13º andar não é um andar.|É o prédio... de amanhã.",
    "Quem desce lá pisa no dia seguinte por alguns minutos,|e volta sabendo o futuro.",
    "E o porteiro desceu lá há 30 anos, ficou tempo demais,|e desde então vive sempre um dia na frente de todo mundo.",
    "É por isso que ele sabe quem vai chegar|antes de tocar o interfone.",
    "Ele mostrou ao Davi o jornal de amanhã.|Na primeira página: elevador do prédio quebrado.",
    "E o Davi entendeu: sem elevador, o porteiro|ia ficar preso no amanhã pra sempre, sozinho.",
    "Então, às 2h59, o Davi apertou o 13|e segurou a porta aberta.",
    "O porteiro olhou pro corredor claro,|respirou fundo... e entrou.",
    "A luz piscou, o elevador tremeu, e a porta abriu no 12º,|de madrugada, no dia de hoje.",
    "No dia seguinte, o elevador quebrou, como o jornal dizia.|Mas não tinha ninguém preso lá dentro.",
    "Ou seja: depois de 30 anos, o porteiro finalmente voltou pro presente...|e não fazia a menor ideia do que ia acontecer amanhã.",
]
FALA_TIKTOK = "Você desceria no décimo terceiro? Comenta sim ou não, e segue pra mais histórias!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 2
FLASH = [11]
CHECK = [(0, 'amanha', 6), (1, 'moro', 4), (2, 'amanha', 6), (3, 'futuro', 4), (4, 'trinta', 4), (5, 'interfone', 4),
         (6, 'quebrado', 4), (7, 'sozinho', 4), (8, 'aberta', 4), (9, 'entrou', 4), (10, 'hoje', 4), (11, 'ninguem', 4),
         (12, 'amanha', 8)]


def s0(f):
    c = corredor_bg('dusk', False).copy()
    am = wt(0, 'amanha') - 3
    t3 = wt(0, 'terceiro') - 3
    put_prof(c, 330, 1820, 940, f, expr='grin' if f < am else 'proud', arms='point', look=1)
    if f < 50: paste_c(c, txt('PARTE 2', 120, -4), 621, 520, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)))
    if t3 <= f < am: paste_c(c, txt('13º ANDAR', 100, -5), 760, 660, back(ramp(f, t3, t3 + 8)))
    if f >= am: paste_c(c, jornal_img(380), 860, 1100, back(ramp(f, am, am + 8)))
    return c, cam(f, 1.2, 1.03, 60, 1250, am), 'dusk'


def s1(f):
    c = corredor_bg('day', True).copy()
    co = wt(1, 'cochichou') - 3
    mo = wt(1, 'moro') - 3
    put_pes(c, 420, 1820, 860, f, 6, expr='shock' if f >= mo else 'nervous', arms='hang', look=1, **DAVI)
    put_port(c, 820, 1820, 900, f, 9, expr='smug', arms='cheek' if f >= co else 'hang', look=-1, **PORT)
    if f >= mo: paste_c(c, txt('EU MORO AQUI', 100, 5), 621, 580, back(ramp(f, mo, mo + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, mo), 'day'


def s2(f):
    c = corredor_bg('day', True).copy()
    an = wt(2, 'andar', 1) - 3
    am = wt(2, 'amanha') - 3
    put_prof(c, 380, 1820, 920, f, expr='stern' if f < am else 'proud', arms='point', look=1)
    cal = Image.new('RGBA', (1, 1))
    if f >= an:
        paste_c(c, txt('NÃO É ANDAR', 90, -4), 621, 600, back(ramp(f, an, an + 8)) * (1 - ramp(f, am - 4, am)))
    if f >= am:
        paste_c(c, txt('É AMANHÃ!', 105, 5), 621, 600, back(ramp(f, am, am + 8)))
        paste_c(c, jornal_img(320), 880, 1100, back(ramp(f, am, am + 8)))
    t = easeOut(ramp(f, am - 10, am + 14))
    return c, (621, 1250 + kick(f, am, .8) * 12, lerp(1.05, 1.2, t) * (1 + .0009 * f), lerp(0, 2, t)), 'day'


def s3(f):
    c = elevador_bg('day').copy()
    fu = wt(3, 'futuro') - 3
    ab = wt(3, 'minutos') - 3
    portas(c, easeOut(ramp(f, 4, 24)) * (1 - easeOut(ramp(f, ab, ab + 20))), glow=True)
    visor(c, 13, red=True)
    put_pes(c, 560, 1820, 900, f, 4, expr='smug' if f >= fu else 'neutral', arms='hang', look=1, **DAVI)
    if f >= fu:
        paste_c(c, jornal_img(240), 760, 1300)
        paste_c(c, txt('SABE O FUTURO', 90, -5), 621, 560, back(ramp(f, fu, fu + 8)))
    return c, cam(f, 1.0, 1.1, 80, 1080, fu), 'day'


def s4(f):
    c = portaria_bg('golden', True).copy()
    tr = wt(4, 'trinta') - 3
    fr = wt(4, 'frente') - 3
    put_port(c, 621, 1820, 900, f, 9, expr='neutral' if f < fr else 'nervous', arms='hang', look=0, **(PORT_JOVEM if f < fr else PORT))
    if f >= tr: paste_c(c, txt('30 ANOS ATRÁS', 90, -5), 621, 560, back(ramp(f, tr, tr + 8)) * (1 - ramp(f, fr - 4, fr)))
    if f >= fr: paste_c(c, txt('+1 DIA', 120, 5), 621, 600, back(ramp(f, fr, fr + 8)))
    return c, cam(f, 1.1, 1.0, 100, 1250, fr), 'golden'


def s5(f):
    c = portaria_bg('day').copy()
    ch = wt(5, 'chegar') - 3
    it = wt(5, 'interfone') - 3
    put_port(c, 930, 1700, 860, f, 9, expr='smug', arms='point' if f >= ch else 'hang', look=-1, **PORT)
    if f >= it - 14:
        put_pes(c, lerp(-100, 240, easeOut(ramp(f, it - 14, it + 4))), 1820, 820, f, 12, expr='shock' if f >= it + 6 else 'neutral',
                arms='hang', look=1, skin=3, hair='#2b1d14', shirt='#ff8a5c', pants='#3d5a8a', pocket=False)
    if f >= ch: paste_c(c, txt('OI, DONA ANA!', 90, -5), 760, 600, back(ramp(f, ch, ch + 8)))
    if f >= it: paste_c(c, txt('TRIM?', 80, 5), 960, 800, back(ramp(f, it, it + 8)))
    return c, cam(f, 1.05, 1.12, 80, 1250, it), 'day'


def s6(f):
    c = corredor_bg('day', True).copy()
    jo = wt(6, 'jornal') - 3
    qb = wt(6, 'quebrado') - 3
    put_port(c, 330, 1820, 880, f, 9, expr='nervous', arms='point' if f >= jo else 'hang', look=1, **PORT)
    if f >= jo:
        s = back(ramp(f, jo, jo + 8))
        paste_c(c, jornal_img(max(20, int(460 * s)), 'QUEBROU!'), 780, 1050)
    if f >= qb: paste_c(c, txt('QUEBRADO!', 110, -5), 621, 600, back(ramp(f, qb, qb + 8)))
    return c, cam(f, 1.05, 1.15, 80, 1250, qb), 'day'


def s7(f):
    c = corredor_bg('day', True).copy()
    pr = wt(7, 'preso') - 3
    so = wt(7, 'sozinho') - 3
    put_pes(c, 330, 1820, 860, f, 6, expr='pained' if f >= so else 'nervous', arms='hang', look=1, **DAVI)
    put_port(c, 880, 1820, 900, f, 9, expr='pained' if f >= pr else 'neutral', arms='hang', look=-1, **PORT)
    if f >= pr: paste_c(c, txt('PRESO NO AMANHÃ', 68, 4), 621, 600, back(ramp(f, pr, pr + 8)))
    t = smooth(ramp(f, 0, 100))
    return c, (621, 1250, lerp(1.05, 1.2, t) * (1 + .0009 * f), lerp(0, -2, t)), 'day'


def s8(f):
    c = elevador_bg('dusk').copy()
    tz = wt(8, 'treze') - 3
    ab = wt(8, 'aberta') - 3
    dz = wt(8, 'duas') - 3
    portas(c, easeOut(ramp(f, tz + 4, tz + 20)), glow=True)
    visor(c, 13 if f >= tz else 12, red=f >= tz)
    put_pes(c, 560, 1820, 900, f, 4, expr='stern', arms='point' if f >= tz else 'hang', look=1, **DAVI)
    if f >= dz: paste_c(c, txt('2:59', 110, -4), 300, 700, back(ramp(f, dz, dz + 8)))
    if f >= ab: paste_c(c, txt('SEGURA!', 90, 5), 820, 700, back(ramp(f, ab, ab + 8)))
    return c, cam(f, 1.0, 1.1, 80, 1050, ab), 'dusk'


def s9(f):
    c = corredor_bg('day', True).copy()
    rf = wt(9, 'respirou') - 3
    en = wt(9, 'entrou') - 3
    x = lerp(800, 400, easeOut(ramp(f, en - 8, en + 14)))
    put_port(c, x, 1820, 900, f, 9, expr='nervous' if f < en else 'proud', arms='hang', look=-1 if f < rf else 1, **PORT)
    if f >= en: paste_c(c, txt('ENTROU!', 120, -5), 621, 600, back(ramp(f, en, en + 8)))
    return c, cam(f, 1.05, 1.12, 80, 1250, en), 'day'


def s10(f):
    pi = wt(10, 'piscou') - 3
    tr = wt(10, 'tremeu') - 3
    ab = wt(10, 'abriu') - 3
    ho = wt(10, 'hoje') - 3
    c = elevador_bg('dusk').copy()
    portas(c, easeOut(ramp(f, ab, ab + 16)))
    visor(c, 12 if f >= ab else 13, red=f < ab)
    put_pes(c, 450, 1820, 880, f, 4, expr='shock' if f < ab else 'grin', arms='hang', look=1, **DAVI)
    put_port(c, 800, 1820, 900, f, 9, expr='shock' if f < ab else 'grin', arms='hang', look=-1, **PORT)
    if pi <= f < pi + 12 and (f // 2) % 2:
        c.alpha_composite(Image.new('RGBA', c.size, (10, 10, 20, 200)))
    if f >= ho: paste_c(c, txt('HOJE!', 120, 5), 621, 560, back(ramp(f, ho, ho + 8)))
    shake = 7 * math.sin(f * 1.9) if tr <= f < ab else 0
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 100))) * (1 + .0009 * f)
    return c, (621 + shake, 1000, z, shake * .25), 'dusk'


def s11(f):
    c = portaria_bg('day').copy()
    qb = wt(11, 'quebrou') - 3
    ni = wt(11, 'ninguem') - 3
    d = ImageDraw.Draw(c)
    d.rectangle((640, 560, 1060, 1200), fill=(201, 208, 216, 255), outline=(36, 23, 38, 255), width=8)
    d.line((850, 560, 850, 1200), fill=(36, 23, 38, 255), width=6)
    if f >= qb:
        paste_c(c, txt('QUEBRADO', 70, -8), 850, 880, back(ramp(f, qb, qb + 8)))
    if f >= ni: paste_c(c, txt('VAZIO!', 110, 5), 621, 520, back(ramp(f, ni, ni + 8)))
    put_pes(c, 330, 1820, 860, f, 6, expr='proud' if f >= ni else 'nervous', arms='hang', look=1, **DAVI)
    return c, cam(f, 1.05, 1.12, 90, 1200, qb), 'day'


def s12(f):
    c = portaria_bg('day').copy()
    am = wt(12, 'amanha') - 3
    pr = wt(12, 'presente') - 3
    put_prof(c, 300, 1820, 920, f, expr='smug' if f < am else 'grin', arms='chin' if f < am else 'shrug', look=1)
    put_port(c, 900, 1700, 860, f, 9, expr='grin' if f < pr else 'shock', arms='shrug' if f >= am else 'hang', look=-1, **PORT)
    if f >= am: paste_c(c, txt('E AGORA?!', 110, -5), 700, 620, back(ramp(f, am, am + 8)))
    t = easeOut(ramp(f, 0, 70))
    return c, (621, lerp(1300, 1260, t), lerp(1.03, 1.12, t) * (1 + .0006 * f), 0), 'day'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
