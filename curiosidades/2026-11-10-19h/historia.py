"""Formato DESENHO: setembro quer dizer sétimo, mas é o nono mês (Curiosidades da IA, 10/11/2026, 19h). Categoria: HISTÓRIA.
Fatos: Etymonline: September vem do latim septem (sete), o sétimo mês do antigo calendário romano, que começava o ano em
março; December vem de decem (dez), o décimo mês desse calendário. Britannica ("Why Does the New Year Start on January 1?"):
numa revisão do calendário romano janeiro passou a vir antes de março; há indícios de que 1º de janeiro só virou o início
oficial do ano romano em 153 a.C.; o calendário juliano manteve 1º de janeiro. Outubro/novembro: octo (8), novem (9)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_h18 = _load('h18b', '2026-11-06-18h')
jovem = _h18.jovem
_h10 = _load('h10b', '2026-11-08-10h')
pessoa = _h10.pessoa
_h17 = _load('h17b', '2026-11-06-17h')
coroa_louro = _h17.coroa_louro


def put_jovem(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'jovem', x, feet, h, f, seed, **kw)


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


LINES = [
    "Setembro quer dizer sétimo. Mas ele é o nono mês do ano.",
    "Na Roma antiga, o ano começava em março.",
    "Então setembro era o sétimo, outubro o oitavo, novembro o nono e dezembro o décimo.",
    "Depois, janeiro e fevereiro passaram a vir antes de março.",
    "E lá por cento e cinquenta e três antes de Cristo, o ano novo virou primeiro de janeiro.",
    "Você vê, os meses andaram duas casas pra frente... mas ninguém trocou os nomes.",
    "Ou seja: faz mais de dois mil anos que dezembro diz que é o dez.",
]
CAPTXT = [
    "Setembro quer dizer sétimo.|Mas ele é o nono mês do ano.",
    "Na Roma antiga, o ano começava em março.",
    "Então setembro era o sétimo, outubro o oitavo,|novembro o nono e dezembro o décimo.",
    "Depois, janeiro e fevereiro|passaram a vir antes de março.",
    "E lá por 153 antes de Cristo,|o ano novo virou 1º de janeiro.",
    "Você vê, os meses andaram duas casas pra frente...|mas ninguém trocou os nomes.",
    "Ou seja: faz mais de 2 mil anos|que dezembro diz que é o dez.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [3]
CHECK = [(0, 'setimo', 4), (0, 'nono', 6), (1, 'marco', 6), (2, 'setimo', 4), (2, 'decimo', 6), (3, 'janeiro', 4),
         (4, 'janeiro', 6), (5, 'nomes', 6), (6, 'dez', 8)]

# cenários: s0 sala (calendário de parede em SETEMBRO, pessoa confusa) | s1 Roma antiga (romano de toga, ano novo em março) |
# s2 Roma antiga (fila de meses MAR..DEZ com números 1..10) | s3 Roma antiga ao entardecer (JAN e FEV entram na frente) |
# s4 Roma antiga ao entardecer (1º de janeiro, 153 a.C.) | s5 sala ao entardecer (números mudam +2, nomes iguais) |
# s6 sala ao entardecer (calendário em DEZEMBRO = 12)

TOGA = '#f3efe2'
def fit(im, mw, mh):
    bb = im.getchannel('A').point(lambda v: 255 if v > 60 else 0).getbbox()
    if bb: im = im.crop(bb)
    k = min(mw / im.size[0], mh / im.size[1], 1.0)
    return im.resize((max(1, int(im.size[0] * k)), max(1, int(im.size[1] * k))), Image.LANCZOS)


MESES = ['MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']


@lru_cache(maxsize=128)
def carta_img(nome, num, hl=0, w=170):
    p = Pen(170, 220)
    col = hexc('#ffd84a') if hl else hexc('#fbf6e8')
    p.shape([(8, 8), (162, 8), (162, 212), (8, 212)], col, mul(col, .86), 5, 8)
    p.poly([(8, 8), (162, 8), (162, 60), (8, 60)], hexc('#c8453c') if hl else hexc('#7a8fb0'))
    im = p.img.resize((170, 220), Image.LANCZOS)
    t = fit(txt(nome, 90), 150, 56); im.alpha_composite(t, (int(85 - t.size[0] / 2), int(34 - t.size[1] / 2)))
    if num:
        t = fit(txt(str(num), 160), 140, 120); im.alpha_composite(t, (int(85 - t.size[0] / 2), int(140 - t.size[1] / 2)))
    return im.resize((w, int(w * 220 / 170)), Image.LANCZOS)


def carta(c, x, y, nome, num, hl=0, s=1.0, w=170):
    if s * w < 8: return
    paste_c(c, carta_img(nome, num, hl, w), x, y, s)


@lru_cache(maxsize=16)
def calendario_img(mes, num=0, w=420):
    p = Pen(420, 520)
    p.shape([(10, 30), (410, 30), (410, 510), (10, 510)], hexc('#fbf6e8'), hexc('#e2dccb'), 6, 10)
    p.poly([(10, 30), (410, 30), (410, 130), (10, 130)], hexc('#c8453c'))
    for i in range(2): p.dot(130 + i * 160, 30, 16, hexc('#555555'), 4)
    for r in range(4):
        for k in range(6):
            p.poly([(40 + k * 60, 300 + r * 50), (80 + k * 60, 300 + r * 50), (80 + k * 60, 330 + r * 50), (40 + k * 60, 330 + r * 50)], hexc('#d9d2bf'))
    im = p.img.resize((420, 520), Image.LANCZOS)
    t = fit(txt(mes, 120), 380, 95); im.alpha_composite(t, (int(210 - t.size[0] / 2), int(80 - t.size[1] / 2)))
    if num:
        t = fit(txt('MÊS %d' % num, 130), 380, 120); im.alpha_composite(t, (int(210 - t.size[0] / 2), int(210 - t.size[1] / 2)))
    return im.resize((w, int(w * 520 / 420)), Image.LANCZOS)


def SFX(s):
    s.ting(s.W(0, 'setimo'), .3); s.thunk(s.W(0, 'nono') - 2, 180, .7)
    s.ting(s.W(1, 'marco'), .3)
    for w in ('setimo', 'oitavo', 'nono', 'decimo'): s.thunk(s.W(2, w) - 2, 260, .45)
    s.whoosh(s.W(3, 'janeiro') - 6, .5, .5)
    s.thunk(s.W(4, 'janeiro') - 2, 160, .7)
    s.whoosh(s.W(5, 'casas') - 6, .4, .4); s.thunk(s.W(5, 'nomes') - 2, 220, .6)
    s.trill(s.W(6, 'dez') + 2, 1.0, .3)


def s0(f):
    c = CEN('sala', 'day').copy()
    st = wt(0, 'setimo') - 3
    no = wt(0, 'nono') - 3
    paste_c(c, calendario_img('SETEMBRO', 9 if f >= no else 0, 310), 330, 1000, back(ramp(f, 0, 8)))
    put_pessoa(c, 880, 1760, 900, f, 2, shirt='#3fa36b', arms='point' if f >= no else 'hang',
               expr='shock' if f >= no else 'neutral', look=-1)
    if st <= f < no: paste_c(c, txt('SEPTEM = 7', 100, -5), 621, 600, back(ramp(f, st, st + 8)))
    if f >= no: paste_c(c, txt('9º?!', 130, 6), 621, 600, back(ramp(f, no, no + 8)))
    z = lerp(1.3, 1.08, easeOut(ramp(f, 2, 40))) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, no, .6) * 10, z, 0), 'day'


def romano(c, x, feet, h, f, seed, **kw):
    put_jovem(c, x, feet, h, f, seed, shirt=TOGA, skin=3, **kw)
    if h > 8: coroa_louro(c, x, feet - h * .84, h * .3)


def s1(f):
    c = CEN('antiga', 'day').copy()
    m = wt(1, 'marco') - 3
    romano(c, 360, 1760, 900, f, 3, arms='point' if f >= m else 'hang', expr='grin', look=1)
    carta(c, 860, 1050, 'MAR', 1 if f >= m else 0, 1 if f >= m else 0, back(ramp(f, m - 6, m + 2)) if f >= m - 6 else 0, 300)
    if f >= m: paste_c(c, txt('ANO NOVO!', 100, -5), 760, 620, back(ramp(f, m, m + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1250, z, 0), 'day'


def fila(c, f, n_vis, nums, hl=(), x0=95, dx=118, y=1050, extra=()):
    lista = list(extra) + MESES
    for i, nm in enumerate(lista[:n_vis]):
        carta(c, x0 + i * dx, y + (i % 2) * 260, nm, nums[i] if i < len(nums) else 0, 1 if nm in hl else 0, 1, 150)


def s2(f):
    c = CEN('antiga', 'day').copy()
    ks = [wt(2, w) - 3 for w in ('setimo', 'oitavo', 'nono', 'decimo')]
    hl = [MESES[6 + i] for i, k in enumerate(ks) if f >= k]
    for i, nm in enumerate(MESES):
        x = 181 + (i % 5) * 220
        y = 820 + (i // 5) * 380
        s = back(ramp(f, i * 2, i * 2 + 8))
        carta(c, x, y, nm, i + 1, 1 if nm in hl else 0, s, 175)
    if hl:
        last = len(hl) - 1
        paste_c(c, txt(['7 = SETE', '8 = OITO', '9 = NOVE', '10 = DEZ'][last], 100, -4), 621, 470, back(ramp(f, ks[last], ks[last] + 8)))
    z = lerp(1.06, 0.98, smooth(ramp(f, 0, 50))) * (1 + .0009 * f)
    return c, (621, 1100, z, 0), 'day'


def s3(f):
    c = CEN('antiga', 'golden').copy()
    j = wt(3, 'janeiro') - 3
    t = smooth(ramp(f, j, j + 16))
    lst = MESES
    def slot(q):
        a, b = int(q), min(int(q) + 1, 11)
        fr = q - int(q)
        xa, ya = 210 + (a % 4) * 275, 760 + (a // 4) * 330
        xb, yb = 210 + (b % 4) * 275, 760 + (b // 4) * 330
        return lerp(xa, xb, fr), lerp(ya, yb, fr)
    for i, nm in enumerate(lst):
        x, y = slot(i + 2 * t)
        carta(c, x, y, nm, 0, 0, 1, 170)
    for k, nm in enumerate(('JAN', 'FEV')):
        s = back(ramp(f, j + 8 + k * 6, j + 18 + k * 6))
        x, y = slot(k)
        carta(c, x, y, nm, 0, 1, s, 170)
    if f >= j: paste_c(c, txt('FURARAM A FILA!', 90, -5), 621, 460, back(ramp(f, j + 10, j + 18)))
    z = lerp(1.05, 1.12, smooth(ramp(f, 0, 80))) * (1 + .0009 * f)
    return c, (621, 1150, z, 0), 'golden'


def s4(f):
    c = CEN('antiga', 'golden').copy()
    a = wt(4, 'cento') - 3
    jn = wt(4, 'janeiro') - 3
    if f >= a: paste_c(c, txt('153 a.C.', 110, -4), 621, 430, back(ramp(f, a, a + 8)))
    carta(c, 820, 1050, 'JAN', 1 if f >= jn else 0, 1, 1, 300)
    if f >= jn:
        paste_c(c, txt('FELIZ ANO NOVO!', 80, 5), 621, 640, back(ramp(f, jn, jn + 8)))
        for i in range(10):
            ang = i * .63 + f * .05
            rr = 60 + (f - jn) * 9
            if rr < 420:
                paste_c(c, txt('*', 70), 820 + rr * math.cos(ang), 1050 + rr * math.sin(ang), 1)
    romano(c, 330, 1760, 900, f, 5, arms='up' if f >= jn else 'hang', expr='grin', look=1)
    z = lerp(1.1, 1.05, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (621, 1250 + kick(f, jn, .5) * 10, z, 0), 'golden'


def s5(f):
    c = CEN('sala', 'dusk').copy()
    k = wt(5, 'casas') - 3
    n = wt(5, 'nomes') - 3
    t = smooth(ramp(f, k, k + 12))
    for i, nm in enumerate(MESES[6:]):
        x = 240 + i * 255
        carta(c, x, 1000, nm, 7 + i + (2 if t > .5 else 0), 1 if t > .5 else 0, 1 + .15 * math.sin(t * math.pi), 200)
    if t > .5: paste_c(c, txt('+2', 120, -6), 621, 640, back(ramp(f, k + 6, k + 14)))
    if f >= n: paste_c(c, txt('MESMO NOME!', 100, 5), 621, 1420, back(ramp(f, n, n + 8)))
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (621, 1100, z, lerp(0, 2, smooth(ramp(f, 0, 90)))), 'dusk'


def s6(f):
    c = CEN('sala', 'dusk').copy()
    d = wt(6, 'dez') - 3
    paste_c(c, calendario_img('DEZEMBRO', 12, 310), 330, 1000)
    put_pessoa(c, 880, 1760, 900, f, 2, shirt='#3fa36b', arms='shrug' if f >= d else 'hang',
               expr='smug' if f >= d else 'neutral', look=-1)
    if d <= f < d + 50: paste_c(c, txt('DEZ = 12?', 110, -6), 621, 620, back(ramp(f, d, d + 8)))
    z = lerp(1.05, 1.25, easeOut(ramp(f, 0, 70))) * (1 + .0009 * f)
    return c, (621, 1200, z, lerp(0, -2, smooth(ramp(f, 0, 70)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
