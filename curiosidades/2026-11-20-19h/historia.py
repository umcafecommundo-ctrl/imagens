"""Formato DESENHO: por que o relógio gira para a direita (Curiosidades da IA, 20/11/2026, 19h).
Categoria: INVENÇÕES E OBJETOS.
Fatos: Wikipedia "Clockwise" e Science Focus (BBC), "Why do clocks go clockwise?": os relógios mecânicos surgiram na
Europa (hemisfério norte), por volta do fim do séc. 13 / começo do séc. 14, e imitaram o relógio de sol, cuja sombra no
hemisfério norte anda no sentido que hoje chamamos de horário; no hemisfério sul a sombra do relógio de sol anda no
sentido contrário. Country Life e History Facts ("Why do clocks move clockwise?"): mesma explicação; se o relógio tivesse
sido inventado no hemisfério sul, o sentido horário provavelmente seria o outro. Ao sul do trópico de Capricórnio a
sombra gira sempre ao contrário (por isso a narração fala em 'longe do equador').
Cenários: s0 museu (Professor e o relógio grande) | s1 cidade antiga (relógio de sol, sombra andando) |
s2 cidade antiga (sombra anda pro mesmo lado do ponteiro) | s3 oficina/fábrica com engrenagens (relógio mecânico
copiando a sombra) | s4 cidade antiga ao entardecer (relógio de sol + relógio lado a lado) | s5 praia, sul do planeta
(Professor vê a sombra girar ao contrário) | s6 sala ao entardecer (relógio andando ao contrário, Professor ri)."""
from kit import *
from functools import lru_cache

LINES = [
    "O ponteiro do relógio gira pra direita por causa de uma sombra.",
    "Antes dos relógios mecânicos, as pessoas viam a hora pela sombra de um relógio de sol.",
    "Na Europa, essa sombra andava sempre pro mesmo lado, igualzinho ao ponteiro de hoje.",
    "Quando os relógios mecânicos foram inventados lá, há uns setecentos anos, eles copiaram o caminho da sombra.",
    "Você vê, o sentido horário é a sombra do norte do planeta.",
    "Lá no sul, longe do equador, a sombra do relógio de sol gira pro outro lado.",
    "Ou seja: se o relógio fosse inventado no sul, o horário seria anti-horário.",
]
CAPTXT = [
    "O ponteiro do relógio gira pra direita|por causa de uma sombra.",
    "Antes dos relógios mecânicos, as pessoas viam a hora|pela sombra de um relógio de sol.",
    "Na Europa, essa sombra andava sempre pro mesmo lado,|igualzinho ao ponteiro de hoje.",
    "Quando os relógios mecânicos foram inventados lá,|há uns 700 anos, eles copiaram o caminho da sombra.",
    "Você vê, o sentido horário é a sombra do norte do planeta.",
    "Lá no sul, longe do equador,|a sombra do relógio de sol gira pro outro lado.",
    "Ou seja: se o relógio fosse inventado no sul,|o horário seria anti-horário.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 4
FLASH = [3]
CHECK = [(0, 'sombra', 4), (1, 'sol', 6), (2, 'lado', 6), (3, 'setecentos', 6), (3, 'copiaram', 6),
         (4, 'norte', 6), (5, 'outro', 6), (6, 'anti-horario', 8)]

STONE = hexc('#d9cfbd'); STONED = hexc('#b3a790'); BRONZE = hexc('#c08a3e'); BRONZED = hexc('#8a5f24')


def SFX(s):
    for i in range(4): s.thunk(s.W(0, 'relogio') - 2 + i * 8, 600, .25)
    s.whoosh(s.W(0, 'sombra') - 6, .5, .4)
    s.ting(s.W(1, 'sol'), .3)
    s.whoosh(s.W(2, 'andava') - 4, .6, .3); s.ting(s.W(2, 'hoje'), .25)
    for i in range(6): s.thunk(s.W(3, 'mecanicos') - 2 + i * 6, 500, .3)
    s.thunk(s.W(3, 'setecentos') - 2, 160, .7); s.ting(s.W(3, 'copiaram'), .3)
    s.thunk(s.W(4, 'norte') - 2, 200, .6)
    s.whoosh(s.W(5, 'outro') - 6, .6, .4)
    for i in range(4): s.thunk(s.W(6, 'anti-horario') - 2 + i * 8, 600, .25)
    s.trill(s.W(6, 'anti-horario'), 1.0, .3)


@lru_cache(maxsize=4)
def dial_base(w):
    p = Pen(800, 520)
    p.shape([(60, 260), (740, 260), (740, 330), (60, 330)], STONED, None, 6, 0)
    p.shape(ell_pts(400, 330, 340, 130, 60), STONED, hexc('#9a8f78'), 6, 10)
    p.shape(ell_pts(400, 260, 340, 130, 60), STONE, STONED, 6, 12)
    p.shape(ell_pts(400, 260, 290, 105, 60), hexc('#efe6d4'), None, 4, 0)
    for i in range(13):
        a = math.pi * i / 12
        x0 = 400 - 250 * math.cos(a); y0 = 260 - 90 * math.sin(a)
        x1 = 400 - 285 * math.cos(a); y1 = 260 - 103 * math.sin(a)
        p.stroke([(x0, y0), (x1, y1)], 5)
    # pedestal
    p.shape([(330, 380), (470, 380), (500, 515), (300, 515)], STONE, STONED, 6, 8)
    return p.img.resize((w, int(w * 520 / 800)), Image.LANCZOS)


def relogio_sol(c, x, y, w, ang, dir_=1):
    """relógio de sol (vista de cima inclinada) com sombra. ang 0..1 = caminho da sombra; dir_=1 esquerda->direita."""
    im = dial_base(int(w))
    k = w / 800
    ox, oy = x - im.width / 2, y - im.height / 2
    c.alpha_composite(im, (int(ox), int(oy)))
    d = ImageDraw.Draw(c)
    cx, cy = ox + 400 * k, oy + 260 * k
    a = math.pi * (ang if dir_ == 1 else 1 - ang)
    ex, ey = cx - 270 * k * math.cos(a), cy - 98 * k * math.sin(a)
    d.polygon([(cx - 8 * k, cy), (cx + 8 * k, cy), (ex, ey)], fill=(70, 60, 80, 200))
    d.line([(cx, cy), (ex, ey)], fill=(70, 60, 80, 230), width=max(2, int(18 * k)))
    # ponteiro de bronze (gnômon)
    d.polygon([(cx - 6 * k, cy + 4 * k), (cx + 6 * k, cy + 4 * k), (cx, cy - 150 * k)], fill=BRONZE + (255,), outline=INK + (255,))
    d.line([(cx - 6 * k, cy + 4 * k), (cx, cy - 150 * k), (cx + 6 * k, cy + 4 * k)], fill=INK + (255,), width=max(2, int(6 * k)))


def seta_curva(c, x, y, r, a0, a1, s=1.0, col=(240, 90, 60)):
    """seta em arco (graus, sentido de tela); de a0 até a1."""
    if s <= 0: return
    d = ImageDraw.Draw(c)
    a1 = a0 + (a1 - a0) * s
    lo, hi = min(a0, a1), max(a0, a1)
    d.arc((x - r, y - r, x + r, y + r), lo, hi, fill=INK + (255,), width=34)
    d.arc((x - r, y - r, x + r, y + r), lo, hi, fill=col + (255,), width=22)
    t = math.radians(a1); sgn = 1 if a1 > a0 else -1
    tx, ty = x + r * math.cos(t), y + r * math.sin(t)
    dx, dy = -math.sin(t) * sgn, math.cos(t) * sgn
    nx, ny = math.cos(t), math.sin(t)
    pts = [(tx + dx * 50, ty + dy * 50), (tx + nx * 34, ty + ny * 34), (tx - nx * 34, ty - ny * 34)]
    d.polygon(pts, fill=col + (255,), outline=INK + (255,))


@lru_cache(maxsize=4)
def engrenagem(r, n=10, col='#9aa3ad'):
    p = Pen(400, 400)
    pts = []
    for i in range(n * 4):
        a = 2 * math.pi * i / (n * 4)
        rr = 180 if (i % 4) in (1, 2) else 140
        pts.append((200 + rr * math.cos(a), 200 + rr * math.sin(a)))
    p.shape(pts, hexc(col), mul(hexc(col), .75), 6, 10)
    p.dot(200, 200, 45, mul(hexc(col), .6), 5)
    return p.img.resize((int(2 * r), int(2 * r)), Image.LANCZOS)


def put_gear(c, x, y, r, rot, col='#9aa3ad'):
    if r < 8: return
    im = engrenagem(int(r), 10, col).rotate(rot, Image.BICUBIC)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def s0(f):
    c = CEN('museu', 'day').copy()
    so = wt(0, 'sombra') - 3
    t = f / 30
    paste_c(c, clock_img(t * .5, t * 6, 520), 860, 760)
    seta_curva(c, 860, 760, 320, -150, -30, back(ramp(f, 6, 20)))
    put_prof(c, 330, 1880, 1000, f, expr='shock' if f >= so else 'grin', arms='up' if f >= so else 'point', look=1)
    if f >= so: paste_c(c, txt('UMA SOMBRA?!', 84, -5), 730, 1300, back(ramp(f, so, so + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1180 + kick(f, so, .8) * 12, z, 0), 'day'


def s1(f):
    c = CEN('antiga', 'day').copy()
    so = wt(1, 'sol') - 3
    relogio_sol(c, 621, 1380, 900, .2 + .1 * ramp(f, 0, 150))
    put_prof(c, 1030, 1850, 760, f, flip=True, expr='grin' if f >= so else 'neutral', arms='point' if f >= so else 'chin', look=-1)
    if f >= so: paste_c(c, txt('RELÓGIO DE SOL', 92, -4), 621, 640, back(ramp(f, so, so + 8)))
    t = smooth(ramp(f, 0, 70))
    z = lerp(1.0, 1.2, t) * (1 + .0009 * f)
    return c, (lerp(621, 660, t), lerp(1100, 1250, t), z, 0), 'day'


def s2(f):
    c = CEN('antiga', 'golden').copy()
    an = wt(2, 'andava') - 3
    ho = wt(2, 'hoje') - 3
    a = .1 + .8 * smooth(ramp(f, an, an + 60))
    relogio_sol(c, 621, 1350, 980, a)
    seta_curva(c, 621, 1300, 380, -170, -10, back(ramp(f, an, an + 50)))
    if f >= ho:
        tt = (f - ho) / 30
        paste_c(c, clock_img(tt * .5, tt * 6, 300), 1000, 700, back(ramp(f, ho, ho + 8)))
        paste_c(c, txt('IGUALZINHO!', 90, 5), 560, 640, back(ramp(f, ho, ho + 8)))
    z = 1.1 * (1 + .0009 * f)
    return c, (621, 1150, z, 0), 'golden'


def s3(f):
    c = CEN('fabrica', 'golden').copy()
    me = wt(3, 'mecanicos') - 3
    se = wt(3, 'setecentos') - 3
    co = wt(3, 'copiaram') - 3
    for (x, y, r, sp, col) in ((300, 1150, 170, 1, '#9aa3ad'), (560, 1050, 120, -1.4, BRONZE and '#c08a3e'), (980, 1180, 200, .8, '#9aa3ad')):
        put_gear(c, x, y, r * back(ramp(f, me - 4, me + 6)), f * 3 * sp, col)
    tt = f / 30
    paste_c(c, clock_img(tt * .5, tt * 6, 420), 700, 640)
    if se <= f < co: paste_c(c, txt('UNS 700 ANOS', 96, -4), 640, 1500, back(ramp(f, se, se + 8)))
    if f >= co:
        relogio_sol(c, 330, 1560, 420, .2 + .6 * ramp(f, co, co + 40))
        seta_curva(c, 700, 640, 260, -150, -30, back(ramp(f, co, co + 30)))
        paste_c(c, txt('COPIOU!', 100, 5), 900, 1460, back(ramp(f, co, co + 8)))
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (640, 1150, z, 0), 'golden'


def s4(f):
    c = CEN('antiga', 'dusk').copy()
    ho = wt(4, 'horario') - 3
    no = wt(4, 'norte') - 3
    relogio_sol(c, 400, 1450, 620, .3 + .5 * ramp(f, 0, 120))
    tt = f / 30
    paste_c(c, clock_img(tt * .5, tt * 6, 380), 900, 1180)
    seta_curva(c, 900, 1180, 240, -150, -30, back(ramp(f, ho, ho + 20)))
    if f >= no: paste_c(c, txt('SOMBRA DO NORTE', 88, -4), 621, 640, back(ramp(f, no, no + 8)))
    t = smooth(ramp(f, 0, 90))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (621, 1150, z, 0), 'dusk'


def s5(f):
    c = CEN('praia', 'day').copy()
    su = wt(5, 'sul') - 3
    ou = wt(5, 'outro') - 3
    a = .1 + .8 * smooth(ramp(f, ou - 20, ou + 40))
    relogio_sol(c, 480, 1450, 700, a, dir_=-1)
    if f >= ou: seta_curva(c, 480, 1410, 320, -10, -170, back(ramp(f, ou, ou + 40)), (60, 140, 240))
    put_prof(c, 960, 1880, 820, f, flip=True, expr='shock' if f >= ou else 'neutral', arms='up' if f >= ou else 'chin', look=-1)
    if su <= f < ou: paste_c(c, txt('SUL', 120, -4), 660, 660, back(ramp(f, su, su + 8)))
    if f >= ou: paste_c(c, txt('AO CONTRÁRIO!', 86, 4), 660, 660, back(ramp(f, ou, ou + 8)))
    z = lerp(1.05, 1.15, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (660, 1180 + kick(f, ou, .7) * 10, z, 0), 'day'


def s6(f):
    c = CEN('sala', 'dusk').copy()
    an = wt(6, 'anti-horario') - 3
    tt = f / 30
    back_ = f >= an
    m = -tt * 6 if back_ else tt * 6
    paste_c(c, clock_img(m / 12, m, 420), 860, 700)
    if back_: seta_curva(c, 860, 700, 270, -30, -150, back(ramp(f, an, an + 20)), (60, 140, 240))
    put_prof(c, 380, 1880, 1000, f, expr='grin' if back_ else 'smug', arms='shrug' if back_ else 'point', look=1)
    if back_: paste_c(c, txt('ANTI-HORÁRIO!', 70, 5), 800, 985, back(ramp(f, an, an + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.18, t) * (1 + .0009 * f)
    return c, (640, 1200 + kick(f, an, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
