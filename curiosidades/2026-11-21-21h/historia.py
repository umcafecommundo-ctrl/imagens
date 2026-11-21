"""Formato MISTÉRIO: "O espantalho que aponta", PARTE 2 (21/11/2026, 21h). História inventada. Mesmo narrador e mesma avó da parte 1.
Virada: o narrador revira o quarto e não acha nada; vigia o milharal à noite com uma lanterna; às 3h uma coruja enorme pousa no
ombro do espantalho, olha pra janela e empurra o braço dele com a cabeça na direção da cama; debaixo da cama, uma tábua solta
esconde a aliança da avó. Quem mexia no espantalho era a coruja, que enxerga no escuro o que a gente perde.
Fim: "quando eu perco alguma coisa, eu não procuro. Eu pergunto pra coruja."
Cenários/cores: s0 fazenda manhã fria (frio) | s1 quarto de dia (vivo) | s2-s4 fazenda à noite (sombrio_noite) |
s5-s6 quarto à noite + CLOSE (sombrio_noite) | s7 fazenda à noite, coruja (sombrio_noite) | s8 cozinha de manhã + CLOSE final (vivo)."""
from kit import *
import kit, os, importlib.util
from sombrio import *

_aqui = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('p1espantalho', os.path.join(_aqui, '..', '2026-11-21-19h', 'historia.py'))
P1 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(P1)
EU, VO, eu, avo = P1.EU, P1.VO, P1.eu, P1.avo
fazenda_bg, put_esp, braco_ang, put_obj, brilho, JANELA = P1.fazenda_bg, P1.put_esp, P1.braco_ang, P1.put_obj, P1.brilho, P1.JANELA

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'

LINES = [
    "Na parte um, o espantalho da fazenda amanheceu apontando pra janela do meu quarto.",
    "Eu revirei o quarto inteiro. E não achei nada.",
    "Então, à noite, fiquei vigiando o milharal com uma lanterna.",
    "Às três da manhã, uma coruja enorme pousou no ombro dele.",
    "Ela olhou pra minha janela, e empurrou o braço do espantalho com a cabeça.",
    "Agora ele apontava pra um lugar só: debaixo da minha cama.",
    "Lá embaixo, uma tábua do chão estava solta. E dentro, brilhava a aliança da minha avó.",
    "Quem mexia no espantalho era a coruja. Ela enxerga tudo o que a gente perde no escuro.",
    "Agora, quando eu perco alguma coisa, eu não procuro. Eu pergunto pra coruja.",
]
FALA_TIKTOK = "Você entendeu o final? Comenta sim ou não, e segue pra mais histórias!"
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
TWIST = 7
FLASH = []
CHECK = [(0, 'quarto', 6), (1, 'nada', 6), (2, 'lanterna', 6), (3, 'coruja', 4), (3, 'ombro', 6), (4, 'empurrou', 4),
         (5, 'cama', 6), (6, 'tabua', 4), (6, 'alianca', 6), (7, 'coruja', 6), (8, 'coruja', 10)]
CAM = {}


def SFX(s):
    s.patter(s.W(0, 'Na') - 4, s.W(0, 'Na') + 40, 4, .05)
    s.whoosh(s.W(0, 'janela') - 6, .5, .2)
    for i in range(4): s.thunk(s.W(1, 'revirei') - 2 + i * 9, 260, .3)
    s.ting(s.W(2, 'lanterna'), .2)
    s.whoosh(s.W(3, 'coruja') - 8, .9, .3); s.thunk(s.W(3, 'pousou') - 2, 200, .5)
    s.thunk(s.W(4, 'empurrou') - 2, 260, .5)
    s.thunk(s.W(5, 'cama') - 2, 90, .8)
    s.thunk(s.W(6, 'tabua') - 2, 300, .5); s.ting(s.W(6, 'alianca'), .4)
    s.trill(s.W(7, 'escuro'), .6, .12)
    s.ting(s.W(8, 'coruja'), .25)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


# ---------------------------------------------------------------- coruja (de frente)
MARROM, MARROMD, BARRIGA = hexc('#8a6440'), hexc('#6a4a2e'), hexc('#e8d6b0')


@lru_cache(maxsize=64)
def coruja_img(h, asa=0, look=0, blink=0):
    """600x700, pés em y≈680. asa 0 = fechada, 1 = abertas (voando); look -1..1."""
    p = Pen(600, 700)
    if asa:
        for s in (-1, 1):
            p.shape([(300 + s * 100, 360), (300 + s * 290, 250 - 60 * asa), (300 + s * 280, 360), (300 + s * 200, 470)], MARROM, None, 7, 0)
            for k in range(3): p.stroke([(300 + s * (180 + k * 35), 300 - k * 10), (300 + s * (170 + k * 35), 420 - k * 15)], 5, MARROMD)
    p.shape(ell_pts(300, 450, 160, 210, 40), MARROM, MARROMD, 7, 18)
    p.shape(ell_pts(300, 500, 100, 150, 30), BARRIGA, None, 0, 0)
    for r in range(3):
        for k in range(3): p.arc(250 + k * 50, 440 + r * 55, 14, 10, 20, 160, 4, MARROMD)
    if not asa:
        for s in (-1, 1): p.shape([(300 + s * 150, 360), (300 + s * 175, 520), (300 + s * 120, 600)], MARROMD, None, 6, 0)
    # cabeça
    for s in (-1, 1): p.shape([(300 + s * 90, 150), (300 + s * 150, 60), (300 + s * 150, 170)], MARROM, None, 7, 0)
    p.shape(ell_pts(300, 230, 165, 130, 40), MARROM, MARROMD, 7, 12)
    for s in (-1, 1): p.shape(ell_pts(300 + s * 70, 230, 70, 70, 30), BARRIGA, None, 5, 0)
    for ex in (230, 370):
        if blink: p.stroke([(ex - 40, 230), (ex + 40, 230)], 8); continue
        p.dot(ex, 230, 46, hexc('#f2b830'), 6)
        p.dot(ex + look * 12, 232, 24, hexc('#111214'))
        p.dot(ex + look * 12 + 9, 220, 7, hexc('#ffffff'))
    p.shape([(285, 270), (315, 270), (300, 310)], hexc('#e8a03a'), None, 4, 0)
    for s in (-1, 1): p.shape(ell_pts(300 + s * 45, 670, 34, 16, 16), hexc('#e8a03a'), None, 5, 0)
    return p.img.resize((max(4, int(h * 600 / 700)), h), Image.LANCZOS)


def put_coruja(c, x, feet, h, f, **kw):
    if h < 8: return
    kw.setdefault('blink', 1 if blinkAt(f, 9) > .6 else 0)
    kw['look'] = round(kw.get('look', 0) * 4) / 4
    im = coruja_img(int(h // 4 * 4), **kw)
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - im.height * 680 / 700)))


OMBRO = (910, 930)   # ombro direito do espantalho (x=820, pés 1480, h=900) no palco


def lanterna(c, x0, y0, x1, y1, w=160, a=70):
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ang = math.atan2(y1 - y0, x1 - x0); nx, ny = -math.sin(ang), math.cos(ang)
    d.polygon([(x0, y0), (x1 + nx * w, y1 + ny * w), (x1 - nx * w, y1 - ny * w)], fill=(255, 240, 170, a))
    d.ellipse((x1 - w, y1 - w, x1 + w, y1 + w), fill=(255, 240, 170, int(a * .8)))
    c.alpha_composite(lay.filter(ImageFilter.GaussianBlur(12)))


def quarto_bg2(luz):
    c = CEN('quarto', 'dusk' if luz == 'noite' else 'day').convert('RGBA').resize((W_, H_)).copy()
    if luz == 'noite': c.alpha_composite(Image.new('RGBA', c.size, (14, 22, 52, 130)))
    return c


QUARTO_NOITE = None


def tabua(c, s=0.0, f=0, anel=True):
    """tábua solta no chão em frente à cama; s = 0..1 levantada; aliança brilhando dentro."""
    p = Pen(W_, H_)
    p.poly([(240, 1640), (520, 1640), (520, 1700), (240, 1700)], hexc('#2a1c12'))
    lift = 70 * s
    p.shape([(240, 1640 - lift), (520, 1640 - lift * .3), (520, 1700 - lift * .3), (240, 1700 - lift)], hexc('#b07a48'), hexc('#8a5a32'), 6, 6)
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))
    if anel and s > .3:
        put_obj(c, 'alianca', 390, 1672, 60); brilho(c, 390, 1672, f, s)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = fazenda_bg('frio').copy()
    put_esp(c, 820, 1480, 900, braco_ang(240, 950), f)
    t = smooth(ramp(f, 0, 140))
    cam = (lerp(800, 380, t), lerp(1050, 1000, t), lerp(1.15, 1.45, t) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'frio'


def s1(f):
    c = quarto_bg2('dia')
    d = ImageDraw.Draw(c); rnd = random.Random(2)
    rv = wt(1, 'revirei') - 3
    if f >= rv:   # coisas espalhadas
        for i in range(7):
            x, y = rnd.randint(120, 1150), rnd.randint(1640, 1900)
            col = rnd.choice([(232, 176, 74), (111, 159, 200), (196, 82, 63), (240, 240, 235)])
            s = back(ramp(f, rv + i * 3, rv + i * 3 + 8))
            if s > .05: d.rounded_rectangle((x - 50 * s, y - 24 * s, x + 50 * s, y + 24 * s), 8, fill=col + (255,), outline=(36, 30, 32, 255), width=4)
    x = 620 + 220 * math.sin(f * .06) if f >= rv else 620
    eu(c, x, f, feet=1900, h=900, walk=1 if f >= rv else 0, flip=math.cos(f * .06) < 0 and f >= rv, expr='preocupado', look=0)
    cam = (621, 1200, lerp(1.0, 1.1, smooth(ramp(f, 0, 100))) * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = fazenda_bg('noite').copy()
    put_esp(c, 820, 1480, 900, braco_ang(240, 950), f)
    eu(c, 300, f, feet=1900, h=900, expr='neutro', look=.75)
    la = wt(2, 'lanterna') - 3
    hx, hy = P1.mao_dir(300, 1900, 900)
    if f >= la: lanterna(c, hx + 10, hy, 820, 1000 + 40 * math.sin(f * .05), 150, int(80 * ramp(f, la, la + 6)))
    t = smooth(ramp(f, 0, 120))
    cam = (lerp(560, 640, t), lerp(1250, 1150, t), lerp(1.05, 1.1, t) * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'sombrio_noite'


def s3(f):
    c = fazenda_bg('noite').copy()
    put_esp(c, 820, 1480, 900, braco_ang(240, 950), f)
    lanterna(c, 200, 1600, 860, 900, 170, 60)
    co = wt(3, 'coruja') - 8; po = wt(3, 'pousou') - 3
    u = easeOut(ramp(f, co, po))
    if f >= co:
        x = lerp(1300, OMBRO[0] + 20, u); y = lerp(300, OMBRO[1], u)
        put_coruja(c, x, y, 340, f, asa=1 if f < po + 4 else 0, look=-.5)
    cam = (lerp(760, 860, smooth(ramp(f, 0, 80))), 980, lerp(1.2, 1.5, smooth(ramp(f, po - 6, po + 14))) * (1 + .0009 * f), 0)
    cam = (cam[0], cam[1] + kick(f, po, .7) * 10, cam[2], 0); CAM[3] = cam
    return c, cam, 'sombrio_noite'


def s4(f):
    c = fazenda_bg('noite').copy()
    em = wt(4, 'empurrou') - 3
    a0 = braco_ang(240, 950); a1 = braco_ang(240, 1060)
    put_esp(c, 820, 1480, 900, lerp(a0, a1, easeOut(ramp(f, em, em + 14))), f)
    lanterna(c, 200, 1600, 860, 900, 170, 60)
    push = math.sin(math.pi * ramp(f, em - 4, em + 14))
    put_coruja(c, OMBRO[0] + 20 - 30 * push, OMBRO[1] + 8 * push, 340, f, look=-1)
    t = smooth(ramp(f, 0, 130))
    cam = (lerp(860, 600, t), lerp(980, 1000, t), lerp(1.5, 1.15, t) * (1 + .0009 * f), 0); CAM[4] = cam
    return c, cam, 'sombrio_noite'


def s5(f):
    c = quarto_bg2('noite')
    tabua(c, 0, f, anel=False)
    eu(c, 700, f, feet=1820, h=880, expr='preocupado', look=-.75)
    ca = wt(5, 'cama') - 3
    t = easeOut(ramp(f, ca - 6, ca + 12))
    cam = (lerp(700, 420, t), lerp(1150, 1450, t), lerp(1.05, 1.35, t) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'sombrio_noite'


def s6(f):
    c = quarto_bg2('noite')
    ta = wt(6, 'tabua') - 3; al = wt(6, 'alianca') - 3
    tabua(c, easeOut(ramp(f, ta, ta + 14)), f)
    eu(c, 700, f, feet=1820, h=880, expr='choque' if f >= ta + 10 else 'preocupado', look=-.75)
    lanterna(c, 820, 1300, 390, 1672, 90, 60)
    if f >= al:   # CLOSE na descoberta
        c = put_close(c, f, expr='sorriso', look=0, shake=.15, **EU)
        cam = (621, 1104 + kick(f, al, .7) * 10, lerp(1.3, 1.08, easeOut(ramp(f, al, al + 10))) * (1 + .0009 * f), 0); CAM[6] = cam
        return c, cam, 'sombrio_noite'
    cam = (lerp(480, 520, smooth(ramp(f, 0, 60))), 1500, 1.3 * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'sombrio_noite'


def s7(f):
    c = fazenda_bg('noite').copy()
    put_esp(c, 820, 1480, 900, braco_ang(240, 1060), f)
    put_coruja(c, OMBRO[0] + 20, OMBRO[1], 340, f, look=-1 if f < wt(7, 'enxerga') else 0)
    t = smooth(ramp(f, 0, 160))
    cam = (lerp(780, 900, t), lerp(1000, 830, t), lerp(1.2, 1.9, t) * (1 + .0009 * f), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


def s8(f):
    c = CEN('cozinha', 'day').convert('RGBA').resize((W_, H_)).copy()
    put_coruja(c, 620, 700, 150, f, look=0)
    avo(c, 400, f, expr='sorriso', look=.5)
    hx, hy = P1.mao_dir(400, 1760, 900)
    put_obj(c, 'alianca', hx + 6, hy + 30, 40)
    eu(c, 860, f, feet=1780, h=860, expr='sorriso', look=-.5)
    pe = wt(8, 'pergunto') - 3
    if f >= pe:   # CLOSE final
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, pe, pe + 12))) * (1 + .0012 * (f - pe)), 0); CAM[8] = cam
        return c, cam, 'vivo'
    t = smooth(ramp(f, 0, 90))
    cam = (621, lerp(1150, 1100, t), lerp(1.05, 1.15, t) * (1 + .0009 * f), 0); CAM[8] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        stamp(im, 'PARTE 2', 540, 260, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)), 110, big=True)
        j = wt(0, 'janela') - 3
        card(im, 'Meu quarto', 'pra onde o braço aponta', 760, 1150, ramp(f, j, j + 10))
    elif si == 1:
        n = wt(1, 'nada') - 3
        burst(im, 'NADA!', 800, 330, back(ramp(f, n, n + 8)), 64)
    elif si == 2:
        n = wt(2, 'noite') - 3
        stamp(im, 'À NOITE', 230, 160, back(ramp(f, n, n + 8)), 64)
        la = wt(2, 'lanterna') - 3
        card(im, 'Vigília', 'de olho no espantalho', 760, 420, ramp(f, la, la + 10))
    elif si == 3:
        painel(im, 'HORA', '03:00', 540, 240, ramp(f, 2, 12))
        co = wt(3, 'coruja') - 3
        burst(im, 'UHU!', 300, 520, back(ramp(f, co, co + 8)), 60)
    elif si == 4:
        em = wt(4, 'empurrou') - 3
        burst(im, 'TOC', 330, 520, back(ramp(f, em, em + 8)) * (1 - ramp(f, em + 30, em + 36)), 60)
    elif si == 5:
        ca = wt(5, 'cama') - 3
        stamp(im, 'DEBAIXO DA CAMA', 540, 220, back(ramp(f, ca, ca + 8)), 64)
    elif si == 6:
        al = wt(6, 'alianca') - 3
        if f < al:
            ta = wt(6, 'tabua') - 3
            card(im, 'Tábua solta', 'no chão do quarto', 540, 360, ramp(f, ta, ta + 10))
        else:
            ring = P1.obj_img('alianca', 160)
            kit.paste_c(im, ring, 540, 230, back(ramp(f, al, al + 8)))
    elif si == 7:
        q = wt(7, 'coruja') - 3; en = wt(7, 'enxerga') - 3
        stamp(im, 'ERA A CORUJA', 540, 240, back(ramp(f, q, q + 8)), 90, big=True)
        card(im, 'Olhos de coruja', 'enxergam no escuro', 540, 1180, ramp(f, en, en + 10))
    elif si == 8:
        pe = wt(8, 'pergunto') - 3
        if f < pe: stamp(im, 'NO DIA SEGUINTE', 540, 180, back(ramp(f, 0, 8)), 64)
    return grao(im.convert('RGB'), lf)
