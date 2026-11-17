"""Formato DESENHO: o ventilador não esfria o ar (Curiosidades da IA, 17/11/2026, 12h).
Categoria: CIÊNCIA DO DIA A DIA.
Fatos: Popular Science ("Fans don't cool rooms and 3 other myths..."): ventiladores não esfriam o cômodo, só as pessoas;
o vento acelera a troca de calor da pele com o ar (efeito sensação térmica); a temperatura no termômetro não muda.
SC Energy Office (energysaver.sc.gov, texto do Energy Saver do Dep. de Energia dos EUA): "fans cool people, not rooms";
desligue o ventilador ao sair do cômodo. TechRadar ("Can fans cool a room?"): ventilador não baixa a temperatura e pode
até aumentá-la um pouco pelo calor do motor; o vento aumenta a evaporação do suor, que resfria o corpo.
Cenários: s0 quarto (Professor suado na frente do ventilador) | s1 quarto (termômetro na frente do ventilador, igual) |
s2 quarto (Professor sente o friozinho) | s3 quarto ao entardecer, perto da pele (vento leva o calor, suor evapora) |
s4 quarto ao entardecer (refresca você, motor solta calor) | s5 quarto ao entardecer (vazio, ventilador ligado, esquenta;
Professor espia da porta)."""
from kit import *
import kit, os, importlib.util

_aqui = os.path.dirname(os.path.abspath(__file__))
def _load(nome, pasta):
    sp = importlib.util.spec_from_file_location(nome, os.path.join(_aqui, '..', pasta, 'historia.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
_m = _load('h1007v', '2026-11-10-07h')
termo = _m.termo

LINES = [
    "O ventilador não esfria o ar do quarto. Nem um pouquinho.",
    "Coloca um termômetro na frente dele: a temperatura continua a mesma.",
    "Mesmo assim, você sente aquele friozinho gostoso.",
    "Você vê, o vento leva embora o calor da sua pele e faz o suor evaporar mais rápido.",
    "Ele refresca você, não o ar. E o motor ainda solta um pouquinho de calor.",
    "Ou seja: ventilador ligado em quarto vazio... só esquenta o quarto.",
]
CAPTXT = [
    "O ventilador não esfria o ar do quarto.|Nem um pouquinho.",
    "Coloca um termômetro na frente dele:|a temperatura continua a mesma.",
    "Mesmo assim, você sente aquele friozinho gostoso.",
    "Você vê, o vento leva embora o calor da sua pele|e faz o suor evaporar mais rápido.",
    "Ele refresca você, não o ar.|E o motor ainda solta um pouquinho de calor.",
    "Ou seja: ventilador ligado em quarto vazio...|só esquenta o quarto.",
]
FALA_TIKTOK = "Você deixa o ventilador ligado quando sai? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = []
CHECK = [(0, 'esfria', 4), (0, 'pouquinho', 6), (1, 'termometro', 4), (1, 'mesma', 6), (2, 'friozinho', 6),
         (3, 'calor', 4), (3, 'suor', 4), (3, 'evaporar', 6), (4, 'voce', 4), (4, 'motor', 4), (4, 'calor', 6),
         (5, 'vazio', 4), (5, 'esquenta', 8)]

AZ = (200, 235, 255)


@lru_cache(maxsize=64)
def ventilador_img(h, ang, quente=0):
    """ventilador de pé, de frente (card 600x1100, base em y≈1090)."""
    p = Pen(600, 1100)
    G = hexc('#e9eef2'); Gd = hexc('#b9c4cc')
    p.shape([(140, 1040), (460, 1040), (480, 1090), (120, 1090)], hexc('#5c6b78'), hexc('#3f4b55'), 6, 8)
    p.shape([(280, 520), (320, 520), (320, 1045), (280, 1045)], hexc('#8a98a4'), hexc('#66737e'), 5, 6)
    # motor (atrás)
    mc = hexc('#ff8a5a') if quente else hexc('#7d8b97')
    p.shape(ell_pts(300, 480, 70, 60), mc, mul(mc, .8), 5, 8)
    # grade
    p.shape(ell_pts(300, 300, 260, 260), hexc('#cfe9f7'), None, 7, 0)
    for i in range(3):
        a = math.radians(ang + i * 120)
        b0 = [(300 + 40 * math.cos(a + .5), 300 + 40 * math.sin(a + .5))]
        tip = [(300 + 225 * math.cos(a + t), 300 + 225 * math.sin(a + t)) for t in np.linspace(-.35, .45, 8)]
        b1 = [(300 + 40 * math.cos(a - .5), 300 + 40 * math.sin(a - .5))]
        p.shape(b0 + tip[::-1] + b1, hexc('#4aa6d9'), hexc('#2f86bd'), 5, 8)
    p.shape(ell_pts(300, 300, 48, 48), G, Gd, 5, 6)
    for k in range(12):
        a = math.radians(k * 30)
        p.stroke([(300 + 55 * math.cos(a), 300 + 55 * math.sin(a)), (300 + 258 * math.cos(a), 300 + 258 * math.sin(a))], 4)
    for r in (120, 190):
        p.arc(300, 300, r, r, 0, 360, 4)
    p.arc(300, 300, 262, 262, 0, 360, 10)
    return p.img.resize((int(h * 600 / 1100), h), Image.LANCZOS)


def ventilador(c, x, base, h, f, on=True, quente=0):
    if h < 8: return
    ang = (f * 37) % 120 if on else 0
    im = ventilador_img(int(h), int(ang // 10 * 10), quente)
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(base - h)))
    return (x, base - h + h * 300 / 1100)  # centro da hélice


def vento(c, x0, y0, x1, y1, f, n=4, cor=AZ, spread=140):
    d = ImageDraw.Draw(c)
    for i in range(n):
        ph = ((f * .045 + i / n) % 1)
        dy = (i - (n - 1) / 2) * spread / max(1, n - 1) * 2
        pts = []
        for k in range(12):
            u = ph * .6 + k / 11 * .4
            x = lerp(x0, x1, u); y = lerp(y0 + dy, y1 + dy * .6, u) + 18 * math.sin(u * 12 + i)
            pts.append((x, y))
        d.line(pts, fill=INK + (255,), width=16, joint='curve')
        d.line(pts, fill=cor + (255,), width=9, joint='curve')


def gota(c, x, y, r, a=1.0, cor=(120, 200, 255)):
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.polygon([(x, y - r * 1.8), (x - r * .8, y - r * .2), (x + r * .8, y - r * .2)], fill=cor + (int(255 * a),))
    d.ellipse((x - r, y - r, x + r, y + r), fill=cor + (int(255 * a),), outline=INK + (int(255 * a),), width=4)
    c.alpha_composite(lay)


def calor_ondas(c, x, y, f, w=120, cor=(255, 120, 60)):
    d = ImageDraw.Draw(c)
    for i in range(3):
        xx = x + (i - 1) * w * .45
        yy = y - ((f * 3 + i * 20) % 60)
        pts = [(xx + 14 * math.sin(k * .9 + f * .2), yy - k * 14) for k in range(8)]
        d.line(pts, fill=INK + (255,), width=13, joint='curve')
        d.line(pts, fill=cor + (255,), width=7, joint='curve')


def SFX(s):
    s.whoosh(4, .6, .3)
    s.thunk(s.W(0, 'esfria') - 2, 160, .6); s.thunk(s.W(0, 'pouquinho') - 2, 220, .5)
    s.ting(s.W(1, 'termometro'), .3); s.thunk(s.W(1, 'mesma') - 2, 200, .6)
    s.whoosh(s.W(2, 'friozinho') - 6, .7, .45)
    s.whoosh(s.W(3, 'calor') - 6, .5, .4); s.patter(s.W(3, 'suor'), s.W(3, 'suor') + 30, 9, .1)
    s.ting(s.W(3, 'evaporar'), .25)
    s.ting(s.W(4, 'voce'), .3); s.thunk(s.W(4, 'motor') - 2, 110, .7)
    s.thunk(s.W(5, 'vazio') - 2, 200, .5); s.thunk(s.W(5, 'esquenta') - 2, 120, .9); s.trill(s.W(5, 'esquenta') + 8, 1.0, .3)


def s0(f):
    c = CEN('quarto', 'day').copy()
    e = wt(0, 'esfria') - 3
    po = wt(0, 'pouquinho') - 3
    hc = ventilador(c, 920, 1820, 900, f)
    vento(c, hc[0] - 120, hc[1], 520, hc[1] + 40, f, 3)
    put_prof(c, 400, 1830, 980, f, expr='nervous' if f < po else 'shock', arms='point' if f >= e else 'hang', look=1)
    for i in range(3):
        a = (f * 2 + i * 15) % 40
        gota(c, 330 + i * 70, 1020 + a * 3, 16, 1 - a / 40)
    if f >= e: paste_c(c, txt('NÃO ESFRIA!', 110, -5), 640, 620, back(ramp(f, e, e + 8)))
    if f >= po: paste_c(c, txt('NADA!', 100, 6), 780, 840, back(ramp(f, po, po + 8)))
    z = lerp(1.3, 1.06, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1250 + kick(f, e, .6) * 10, z, 0), 'day'


def s1(f):
    c = CEN('quarto', 'day').copy()
    t0 = wt(1, 'termometro') - 3
    me = wt(1, 'mesma') - 3
    hc = ventilador(c, 330, 1820, 900, f)
    vento(c, hc[0] + 120, hc[1], 700, hc[1] + 40, f, 3)
    if f >= t0:
        s = back(ramp(f, t0, t0 + 9))
        termo(c, 730, 1500, 620 * s, .55)
        put_dust(c, 730, 1500, 80, f - t0)
    if f >= me:
        paste_c(c, txt('30 °C', 110, -5), 740, 760, back(ramp(f, me - 12, me - 4)))
        paste_c(c, txt('IGUAL!', 100, 5), 640, 600, back(ramp(f, me, me + 8)))
    elif f >= t0 + 10:
        paste_c(c, txt('30 °C', 110, -5), 740, 760, back(ramp(f, t0 + 10, t0 + 18)))
    put_prof(c, 990, 1840, 760, f, flip=True, expr='stern' if f < me else 'shock', arms='chin', look=-1)
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.08, 1.25, t) * (1 + .0009 * f)
    return c, (lerp(640, 680, t), lerp(1250, 1200, t), z, 0), 'day'


def s2(f):
    c = CEN('quarto', 'day').copy()
    fr = wt(2, 'friozinho') - 3
    hc = ventilador(c, 950, 1820, 900, f)
    vento(c, hc[0] - 120, hc[1], 480, hc[1] - 20, f, 4)
    put_prof(c, 440, 1830, 1000, f, expr='proud' if f >= fr else 'grin', arms='up' if f >= fr else 'hang',
             look=1, tilt=-4 if f >= fr else 0)
    if f >= fr: paste_c(c, txt('AAAH!', 120, -6), 560, 640, back(ramp(f, fr, fr + 8)))
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.12, 1.3, t) * (1 + .0009 * f)
    return c, (lerp(640, 600, t), lerp(1250, 1200, t), z, lerp(0, -2, t)), 'day'


@lru_cache(maxsize=2)
def braco_img(w):
    """braço/pele bem de perto (card 1000x500)."""
    p = Pen(1000, 500)
    sk = hexc('#f5c9a0'); skd = hexc('#d9a77c')
    p.shape([(0, 120), (900, 160), (980, 260), (900, 360), (0, 400)], sk, skd, 7, 26)
    for x in range(80, 860, 90):
        p.stroke([(x, 175), (x + 14, 150)], 4, hexc('#c08a5e'))
    p.shape([(0, 360), (900, 340), (900, 500), (0, 500)], hexc('#ffffff'), hexc('#d9d9d0'), 7, 10)  # manga
    return p.img.resize((w, int(w * .5)), Image.LANCZOS)


def s3(f):
    c = CEN('quarto', 'dusk').copy()
    ca = wt(3, 'calor') - 3
    su = wt(3, 'suor') - 3
    ev = wt(3, 'evaporar') - 3
    paste_c(c, braco_img(1100), 640, 1250)
    # camada de calor saindo da pele
    if f < ca + 40:
        for i in range(5): calor_ondas(c, 220 + i * 190, 1150, f, 80)
    vento(c, -100, 1060, 1300, 1000, f, 4, spread=120)
    if f >= ca: paste_c(c, txt('LEVA O CALOR', 96, -4), 640, 700, back(ramp(f, ca, ca + 8)))
    if f >= su:
        for i in range(4):
            x = 260 + i * 220
            age = f - su - i * 3
            if age < 0: continue
            up = clamp((f - ev) / 30) if f >= ev else 0
            gota(c, x + up * 140, 1170 - up * 260, 26 * (1 - up * .7), 1 - up * .8)
            if f >= ev:
                d = ImageDraw.Draw(c)
                yy = 1100 - up * 300
                d.arc((x + up * 140 - 40, yy - 30, x + up * 140 + 40, yy + 30), 200, 340, fill=(255, 255, 255, int(255 * (1 - up * .5))), width=8)
    if f >= ev: paste_c(c, txt('EVAPORA!', 100, 5), 640, 860, back(ramp(f, ev, ev + 8)))
    z = lerp(1.1, 1.3, smooth(ramp(f, 0, 120))) * (1 + .0009 * f)
    return c, (640, 1150 + kick(f, ev, .5) * 8, z, 0), 'dusk'


def s4(f):
    c = CEN('quarto', 'dusk').copy()
    vo = wt(4, 'voce') - 3
    mo = wt(4, 'motor') - 3
    ca = wt(4, 'calor') - 3
    hc = ventilador(c, 900, 1820, 900, f, quente=1 if f >= mo else 0)
    vento(c, hc[0] - 120, hc[1], 500, hc[1] + 20, f, 3)
    put_prof(c, 380, 1830, 960, f, expr='grin' if f < mo else 'shock', arms='point' if f >= vo else 'hang', look=-1 if f < mo else 1)
    if vo <= f < mo: paste_c(c, txt('VOCÊ, NÃO O AR', 84, -4), 620, 640, back(ramp(f, vo, vo + 8)))
    if f >= mo:
        calor_ondas(c, 900, 1440, f, 140)
        paste_c(c, txt('MOTOR', 100, 5), 880, 1180, back(ramp(f, mo, mo + 8)))
    if f >= ca: paste_c(c, txt('+ CALOR', 100, -5), 700, 680, back(ramp(f, ca, ca + 8)))
    t = smooth(ramp(f, mo - 10, mo + 30))
    z = lerp(1.08, 1.2, t) * (1 + .0009 * f)
    return c, (lerp(640, 680, t), lerp(1250, 1280, t), z, 0), 'dusk'


def s5(f):
    c = CEN('quarto', 'dusk').copy()
    va = wt(5, 'vazio') - 3
    es = wt(5, 'esquenta') - 3
    ventilador(c, 700, 1820, 900, f, quente=1)
    calor_ondas(c, 700, 1440, f, 140)
    v = .55 + .1 * clamp((f - es) / 20) if f >= es else .55
    termo(c, 1010, 1700, 560, v)
    if va <= f < es: paste_c(c, txt('VAZIO', 100, -5), 600, 620, back(ramp(f, va, va + 8)))
    if es <= f < es + 30: paste_c(c, txt('ESQUENTA!', 100, 5), 680, 1000, back(ramp(f, es, es + 8)))
    # Professor espia da beira esquerda e leva um susto
    px = lerp(-320, 290, easeOut(ramp(f, es - 4, es + 8)))
    put_prof(c, px, 1840, 960, f, expr='shock' if f >= es else 'nervous', arms='up' if f >= es else 'chin', look=1)
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (600, 1250 + kick(f, es, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
