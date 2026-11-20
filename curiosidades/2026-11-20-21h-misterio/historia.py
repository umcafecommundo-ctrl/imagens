"""Formato MISTÉRIO: "A praia das garrafas", PARTE 2 (20/11/2026, 21h). História inventada. Mesma narradora da parte 1.
Virada: ela tenta vigiar o mar, dorme, acorda com areia nos pés, segue as pegadas da casa até o mar, acha rolhas, papel e o
rascunho do aviso com a própria letra: quem jogava as garrafas era ela, sonâmbula. Fim: o bilhete de hoje tem o nome de quem assiste.
Cenários/cores: s0 praia à noite (sombrio_noite) | s1-s2 quarto à noite (sombrio_noite) | s3 quarto de manhã (vivo) |
s4 praia de manhã (vivo) | s5 quarto de manhã (vivo) | s6 quarto, revelação (frio) | s7 praia à noite (sombrio_noite) |
s8 quarto à noite (sombrio_noite)."""
from kit import *
import kit, os, importlib.util
from sombrio import *

_aqui = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('p1garrafas', os.path.join(_aqui, '..', '2026-11-20-19h-misterio', 'historia.py'))
P1 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(P1)
EU, menina = P1.EU, P1.menina

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'

LINES = [
    "Na parte um, a garrafa chegou com o meu nome, e um aviso: não vem à praia amanhã.",
    "Eu decidi passar a noite acordada, vigiando o mar pela janela.",
    "Mas, em algum momento, eu dormi.",
    "Acordei com o sol na cara, e com os pés cheios de areia.",
    "Da minha casa até o mar, tinha uma trilha de pegadas. Do meu tamanho.",
    "Na escrivaninha, achei rolhas, papel e uma garrafa vazia.",
    "E o rascunho de um bilhete, com a minha letra: não vem à praia amanhã.",
    "Quem jogava as garrafas no mar... era eu, dormindo.",
    "E o bilhete de hoje já está pronto. Com o seu nome.",
]
FALA_TIKTOK = "Você entendeu o final? Comenta sim ou não, e segue pra mais histórias!"
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
TWIST = 7
FLASH = [3]
CHECK = [(0, 'amanha', 6), (1, 'janela', 6), (2, 'dormi', 6), (3, 'areia', 6), (4, 'tamanho', 6), (5, 'vazia', 6),
         (6, 'letra', 6), (7, 'dormindo', 8), (8, 'nome', 10)]
CAM = {}


def SFX(s):
    for si in (0, 4, 7): s.patter(s.W(si, LINES[si].split()[0].strip(',.:')) - 4, s.W(si, LINES[si].split()[0].strip(',.:')) + 50, 4, .05)
    s.ting(s.W(0, 'aviso'), .25)
    s.whoosh(s.W(1, 'janela') - 6, .6, .2)
    s.trill(s.W(2, 'dormi'), .8, .15)
    s.thunk(s.W(3, 'areia') - 2, 160, .7)
    for i in range(6): s.thunk(s.W(4, 'trilha') - 2 + i * 6, 400, .2)
    s.thunk(s.W(4, 'tamanho') - 2, 120, .7)
    for w in ('rolhas', 'papel', 'garrafa'): s.ting(s.W(5, w), .2)
    s.thunk(s.W(6, 'letra') - 2, 90, .9)
    s.splash(s.W(7, 'mar') - 3, .3); s.thunk(s.W(7, 'dormindo') - 2, 60, 1.0)
    s.thunk(s.W(8, 'nome') - 2, 70, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def areia_pes(c, x, feet, s=1.0):
    if s <= .05: return
    d = ImageDraw.Draw(c); rnd = random.Random(9)
    for i in range(26):
        px = x + rnd.randint(-120, 120); py = feet + rnd.randint(-30, 20)
        r = rnd.randint(5, 12) * s
        d.ellipse((px - r, py - r, px + r, py + r), fill=(226, 198, 140, 255), outline=(150, 120, 80, 255), width=2)


def pegadas(c, t, luz='dia'):
    """trilha de pegadas do canto de baixo à esquerda até o mar; t = 0..1 quanto da trilha aparece."""
    d = ImageDraw.Draw(c); n = 16
    col = (196, 168, 118, 255) if luz == 'dia' else (90, 86, 74, 255)
    for i in range(int(n * t)):
        u = i / n
        x = lerp(160, 820, u) + (30 if i % 2 else -30)
        y = lerp(2120, 1360, u)
        r = lerp(30, 12, u)
        d.ellipse((x - r * .6, y - r, x + r * .6, y + r), fill=col)


def mesa_coisas(c, s=1.0):
    if s <= .05: return
    put_garrafa(c, 1080, 1140, int(170 * s) or 4, rolha=False, bilhete=False)
    d = ImageDraw.Draw(c)
    for x in (840, 900, 960):
        d.rounded_rectangle((x, 1180, x + 34, 1218), 8, fill=(184, 134, 90, 255), outline=(36, 30, 32, 255), width=4)
    for i in range(3):
        d.polygon([(790 + i * 20, 1218 - i * 6), (930 + i * 20, 1212 - i * 6), (935 + i * 20, 1222 - i * 6), (792 + i * 20, 1226 - i * 6)],
                  fill=(246, 239, 217, 255), outline=(36, 30, 32, 255))


# ---------------------------------------------------------------- cenas
def s0(f):
    c = praia_bg('noite').copy(); espuma(c, f, 'noite')
    menina(c, 621, f, expr='preocupado', look=0)
    t = smooth(ramp(f, 0, 120))
    cam = (621, lerp(1250, 1150, t), lerp(1.08, 1.25, t), 0); CAM[0] = cam
    return c, cam, 'sombrio_noite'


def s1(f):
    c = quarto_bg('noite').copy()
    menina(c, 900, f, expr='neutro', look=.25)
    cam = (760, 1150, lerp(1.05, 1.18, smooth(ramp(f, 0, 100))) * (1 + .0006 * f), 0); CAM[1] = cam
    return c, cam, 'sombrio_noite'


def s2(f):
    c = quarto_bg('noite').copy()
    dm = wt(2, 'dormi') - 3
    menina(c, 900, f, expr='neutro', look=.25, dorme=f >= dm, tilt=-4 * ramp(f, dm, dm + 12))
    cam = (760, 1150, 1.2 * (1 + .0006 * f), 0); CAM[2] = cam
    return c, cam, 'sombrio_noite'


def s3(f):
    c = quarto_bg('dia').copy()
    ar = wt(3, 'areia') - 3
    menina(c, 621, f, expr='choque' if f >= ar else 'neutro', look=0)
    areia_pes(c, 621, 1760, back(ramp(f, ar - 4, ar + 6)))
    t = easeOut(ramp(f, ar - 8, ar + 10))
    cam = (621, lerp(1150, 1500, t), lerp(1.1, 1.6, t) * (1 + .0006 * f), 0); CAM[3] = cam
    return c, cam, 'vivo'


def s4(f):
    c = praia_bg('dia').copy(); espuma(c, f)
    tr = wt(4, 'trilha') - 3
    pegadas(c, ramp(f, tr, tr + 30))
    menina(c, 1000, f, feet=1900, h=900, expr='preocupado', look=-.75)
    cam = (640, 1500 - 300 * smooth(ramp(f, tr, tr + 40)), 1.05 * (1 + .0008 * f), 0); CAM[4] = cam
    return c, cam, 'vivo'


def s5(f):
    c = quarto_bg('dia').copy()
    ro = wt(5, 'rolhas') - 3
    mesa_coisas(c, back(ramp(f, ro - 4, ro + 6)))
    menina(c, 400, f, expr='preocupado', look=.75)
    cam = (760, 1200, lerp(1.05, 1.2, smooth(ramp(f, 0, 90))) * (1 + .0006 * f), 0); CAM[5] = cam
    return c, cam, 'vivo'


def s6(f):
    c = quarto_bg('frio').copy()
    le = wt(6, 'letra') - 3
    mesa_coisas(c)
    menina(c, 400, f, expr='choque' if f >= le else 'preocupado', look=.75)
    cam = (700, 1200 + kick(f, le, .8) * 12, 1.12 * (1 + .0008 * f), 0); CAM[6] = cam
    return c, cam, 'frio'


def s7(f):
    c = praia_bg('noite').copy(); espuma(c, f, 'noite')
    x = lerp(200, 760, ramp(f, 0, 150))
    menina(c, x, f, walk=1, dorme=True, expr='neutro', look=.5)
    hx, hy = mao_dir(x, 1760, 960)
    put_garrafa(c, hx + 20, hy, 180)
    cam = (lerp(560, 760, ramp(f, 0, 150)), 1200, 1.12 * (1 + .0008 * f), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


def s8(f):
    c = quarto_bg('noite').copy()
    no = wt(8, 'nome') - 3
    mesa_coisas(c)
    put_garrafa(c, 960, 1130, 190)
    menina(c, 450, f, expr='sorriso' if f >= no else 'neutro', look=0 if f >= no else .75)
    t = smooth(ramp(f, 0, 110))
    cam = (lerp(700, 480, t), lerp(1200, 1020, t), lerp(1.08, 1.6, t), 0); CAM[8] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        stamp(im, 'PARTE 2', 540, 330, back(ramp(f, 0, 8)) * (1 - ramp(f, 40, 46)), 110, big=True)
        av = wt(0, 'aviso') - 3
        kit.paste_c(im, bilhete_img('NÃO VEM À PRAIA|AMANHÃ.', 520).rotate(-3, Image.BICUBIC, expand=True), 540, 380, back(ramp(f, av, av + 10)))
    elif si == 1:
        stamp(im, 'A NOITE', 220, 150, back(ramp(f, 0, 8)), 64)
        v = wt(1, 'vigiando') - 3
        card(im, 'Vigília', 'olhar o mar a noite toda', 330, 1080, ramp(f, v, v + 10))
    elif si == 2:
        dm = wt(2, 'dormi') - 3
        painel(im, 'HORA', '03:00', 330, 330, ramp(f, 2, 12), glitch=1 if dm <= f < dm + 10 and f % 4 < 2 else 0)
        for i in range(3):
            a = (f + i * 14) % 42
            if f >= dm: kit.paste_c(im, stamp_img('Z', 54 + i * 12), 640 + a * 2 + i * 40, 760 - a * 4 - i * 50, 1 - a / 42)
    elif si == 3:
        ar = wt(3, 'areia') - 3
        burst(im, '?!', 800, 520, back(ramp(f, ar, ar + 8)), 64)
        card(im, 'Areia', 'nos pés, na cama, no chão', 540, 1150, ramp(f, ar + 6, ar + 16))
    elif si == 4:
        tm = wt(4, 'tamanho') - 3
        stamp(im, 'DE MANHÃ', 230, 150, back(ramp(f, 0, 8)), 64)
        card(im, 'Pegadas', 'do meu tamanho', 330, 560, ramp(f, tm, tm + 10))
    elif si == 5:
        es = wt(5, 'escrivaninha') - 3
        card(im, 'Escrivaninha', 'rolhas, papel e garrafa vazia', 600, 420, ramp(f, es, es + 10))
    elif si == 6:
        rs = wt(6, 'rascunho') - 3; le = wt(6, 'letra') - 3
        kit.paste_c(im, bilhete_img('NÃO VEM À PRAIA|AMANHÃ.', 560).rotate(4, Image.BICUBIC, expand=True), 560, 400, back(ramp(f, rs, rs + 10)))
        burst(im, 'MINHA LETRA!', 800, 780, back(ramp(f, le, le + 8)), 48, rot=6)
    elif si == 7:
        e = wt(7, 'era') - 3
        stamp(im, 'ERA EU', 540, 330, back(ramp(f, e, e + 8)), 110, big=True, rot=-3)
        dd = wt(7, 'dormindo') - 3
        card(im, 'Sonâmbula', 'toda noite, sem lembrar', 540, 560, ramp(f, dd, dd + 10))
    elif si == 8:
        sn = wt(8, 'seu') - 6
        kit.paste_c(im, bilhete_img('PARA:|VOCÊ', 400).rotate(-4, Image.BICUBIC, expand=True), 760, 380, back(ramp(f, sn, sn + 10)))
    return grao(im.convert('RGB'), lf)
