"""Formato MISTÉRIO: "A lousa que responde", PARTE 2 (21/11/2026, 12h). História inventada. Mesma narradora (Lia) da parte 1.
Virada: a resposta "sim, foi você" era para a pergunta do Téo ("alguém vai descobrir quem escreve?"); Lia se esconde no armário
da sala; à meia-noite um gato cinza sobe na mesa, passa a pata no giz e escreve as respostas dos bilhetes; olha pra ela e
escreve "obrigado por guardar o segredo". Fim: "se alguém perguntar... não fui eu que contei."
Cenários/cores: s0 sala com neblina (sombrio) | s1 corredor de dia (vivo) | s2 sala ao anoitecer (tarde) | s3 sala à noite
+ CLOSE (sombrio_noite) | s4-s7 sala à noite, gato (sombrio_noite) | s8 corredor de manhã + CLOSE final (vivo)."""
from kit import *
import kit, os, importlib.util
from sombrio import *

_aqui = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('p1lousa', os.path.join(_aqui, '..', '2026-11-21-07h', 'historia.py'))
P1 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(P1)
EU, lia, colega, lousa, papel, corredor_bg, sala_bg = P1.EU, P1.lia, P1.colega, P1.lousa, P1.papel, P1.corredor_bg, P1.sala_bg

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'

LINES = [
    "Na parte um, a lousa da escola me respondeu sem eu perguntar nada: sim, foi você.",
    "Aí o Téo confessou. A pergunta era dele: alguém vai descobrir quem escreve as respostas?",
    "Então, naquela noite, eu me escondi no armário do fundo da sala.",
    "À meia-noite, ouvi passos. Leves demais pra ser gente.",
    "Um gato cinza subiu na mesa, passou a pata no giz, e começou a escrever.",
    "Ele lia os bilhetes do armário sem número, e respondia um por um.",
    "Quando acabou, olhou direto pra mim. E escreveu mais uma linha.",
    "Obrigado por guardar o segredo.",
    "Então, se alguém perguntar... não fui eu que contei.",
]
FALA_TIKTOK = "Você entendeu o final? Comenta sim ou não, e segue pra mais histórias!"
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
TWIST = 4
FLASH = []
CHECK = [(0, 'voce', 6), (1, 'dele', 6), (2, 'escondi', 6), (3, 'passos', 4), (3, 'gente', 6), (4, 'gato', 4),
         (4, 'escrever', 6), (5, 'bilhetes', 6), (6, 'mim', 6), (7, 'segredo', 8), (8, 'contei', 10)]
CAM = {}


def SFX(s):
    for si in (0, 1): s.patter(s.W(si, LINES[si].split()[0].strip(',.:')) - 4, s.W(si, LINES[si].split()[0].strip(',.:')) + 40, 4, .05)
    s.ting(s.W(0, 'voce'), .25)
    s.thunk(s.W(1, 'dele') - 2, 120, .6)
    s.whoosh(s.W(2, 'escondi') - 6, .5, .2); s.thunk(s.W(2, 'armario') - 2, 200, .4)
    for i in range(4): s.thunk(s.W(3, 'passos') - 2 + i * 7, 600, .15)
    s.thunk(s.W(3, 'gente') - 2, 80, .8)
    s.thunk(s.W(4, 'mesa') - 2, 300, .4); s.ting(s.W(4, 'giz'), .2)
    for i in range(5): s.thunk(s.W(4, 'escrever') + i * 5, 900, .08)
    for i in range(6): s.thunk(s.W(5, 'respondia') + i * 6, 900, .08)
    s.thunk(s.W(6, 'mim') - 2, 70, .9)
    for i in range(6): s.thunk(s.W(7, 'obrigado') + i * 6, 900, .08)
    s.ting(s.W(7, 'segredo'), .3)
    s.trill(s.W(8, 'contei'), .6, .12)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


# ---------------------------------------------------------------- gato cinza (de frente, sentado)
CINZA, CINZAD = hexc('#8d9299'), hexc('#6c7178')


@lru_cache(maxsize=64)
def gato_img(h, pata=0, look=0, blink=0, brilho=0):
    """600x800, pés em y≈780. pata 0..4 = pata direita levantando até a lousa; look -1..1; brilho=1 olhos brilham."""
    p = Pen(600, 800)
    # rabo
    p.line([(400, 740), (500, 700), (540, 600), (520, 520)], CINZA, 34, 6)
    # corpo
    p.shape(ell_pts(300, 600, 150, 180, 40), CINZA, CINZAD, 7, 18)
    p.shape(ell_pts(300, 640, 80, 110, 30), hexc('#c9cdd2'), None, 0, 0)
    # patas
    for x in (240, 360):
        if x == 360 and pata: continue
        p.shape(ell_pts(x, 760, 46, 26, 20), hexc('#c9cdd2'), None, 6, 0)
    if pata:
        a = pata / 4
        ex, ey = lerp(380, 470, a), lerp(720, 330, a)
        p.line([(350, 560), (ex, ey)], CINZA, 44, 6)
        p.dot(ex, ey, 26, hexc('#eef0ea'), 6)   # pata branca de giz
    # cabeça
    for s in (-1, 1):
        p.shape([(300 + s * 70, 250), (300 + s * 140, 150), (300 + s * 150, 300)], CINZA, None, 7, 0)
        p.shape([(300 + s * 95, 245), (300 + s * 133, 185), (300 + s * 135, 280)], hexc('#d9a3a8'), None, 0, 0)
    p.shape(ell_pts(300, 330, 150, 125, 40), CINZA, CINZAD, 7, 14)
    for ex in (245, 355):
        if blink:
            p.stroke([(ex - 34, 320), (ex + 34, 320)], 8); continue
        p.dot(ex, 320, 40, hexc('#f2e27a') if brilho else hexc('#e8e4c8'), 6)
        p.shape(ell_pts(ex + look * 10, 322, 9 + 4 * (1 - brilho), 30, 14), hexc('#111214'), None, 0, 0)
        p.dot(ex + look * 10 + 8, 308, 6, hexc('#ffffff'))
    p.shape([(288, 372), (312, 372), (300, 386)], hexc('#d77c86'), None, 4, 0)
    p.arc(288, 392, 12, 10, 0, 160, 5); p.arc(312, 392, 12, 10, 20, 180, 5)
    for s in (-1, 1):
        for k in (-1, 0, 1): p.stroke([(300 + s * 60, 385 + k * 12), (300 + s * 170, 375 + k * 28)], 3)
    return p.img.resize((max(4, int(h * .75)), h), Image.LANCZOS)


def put_gato(c, x, feet, h, f, **kw):
    if h < 8: return
    kw.setdefault('blink', 1 if blinkAt(f, 7) > .6 else 0)
    im = gato_img(int(h // 4 * 4), **kw)
    bob = 3 * math.sin(f * .12)
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - im.height * 780 / 800 - bob)))


def mesa(c):
    p = Pen(W_, H_)
    p.shape([(380, 1240), (860, 1240), (860, 1290), (380, 1290)], hexc('#c98a4a'), hexc('#9a6430'), 6, 6)
    for x in (400, 820): p.stroke([(x, 1290), (x, 1560)], 12, hexc('#6b6f78'))
    c.alpha_composite(p.img.resize((W_, H_), Image.LANCZOS))


@lru_cache(maxsize=4)
def armario_img():
    p = Pen(360, 760)
    p.shape([(20, 20), (340, 20), (340, 740), (20, 740)], hexc('#8a5a32'), hexc('#6b4424'), 7, 12)
    p.shape([(178, 40), (184, 40), (184, 720), (178, 720)], hexc('#1c1d20'), None, 0, 0)
    p.dot(150, 380, 10, hexc('#d9c27a'), 4); p.dot(212, 380, 10, hexc('#d9c27a'), 4)
    return p.img.resize((360, 760), Image.LANCZOS)


def armario(c, olhos=0.0, f=0):
    im = armario_img(); c.alpha_composite(im, (880, 1560 - 760))
    if olhos > .05:   # olhos espiando pela fresta
        d = ImageDraw.Draw(c)
        d.rectangle((1052, 1000, 1076, 1120), fill=(10, 10, 12, 255))
        for y in (1030, 1080):
            r = 11 * olhos
            if blinkAt(f, 3) > .6: d.line((1056, y, 1072, y), fill=(240, 240, 235, 255), width=3); continue
            d.ellipse((1064 - r, y - r, 1064 + r, y + r), fill=(244, 244, 240, 255))
            d.ellipse((1064 - r * .45, y - r * .45, 1064 + r * .45, y + r * .45), fill=(17, 18, 20, 255))


RESP = ['A CHAVE ESTÁ', 'NA MOCHILA.', 'SÁBADO CHOVE.']


# ---------------------------------------------------------------- cenas
def s0(f):
    c = sala_bg('neblina').copy()
    lousa(c, ['LIA:'], 1, 120, 420); lousa(c, ['SIM.', 'FOI VOCÊ.'], 1, 110, 570)
    lia(c, 621, f, feet=1640, h=680, expr='preocupado', look=0)
    t = smooth(ramp(f, 0, 140))
    cam = (621, lerp(1000, 820, t), lerp(1.0, 1.15, t) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'sombrio'


def s1(f):
    c = corredor_bg('dia').copy()
    de = wt(1, 'dele') - 3
    lia(c, 380, f, expr='choque' if f >= de else 'neutro', look=.75)
    colega(c, 820, f, expr='preocupado', look=-.75)
    cam = (600, 1180, lerp(1.05, 1.15, smooth(ramp(f, 0, 150))) * (1 + .0009 * f), 0)
    cam = (cam[0], cam[1] + kick(f, de, .6) * 10, cam[2], 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = sala_bg('tarde').copy()
    es = wt(2, 'escondi') - 3
    armario(c, 1.0 if f >= es + 8 else 0, f)
    if f < es + 8:
        lia(c, lerp(700, 1000, ramp(f, es - 6, es + 8)), f, walk=1 if es - 6 <= f < es + 8 else 0, expr='preocupado', look=.75)
    t = smooth(ramp(f, 0, 120))
    cam = (lerp(760, 960, t), lerp(1150, 1080, t), lerp(1.05, 1.4, t) * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    c = sala_bg('noite').copy()
    armario(c, 1.0, f)
    lv = wt(3, 'leves') - 3
    if f >= lv:   # CLOSE: escondida, escutando
        c = put_close(c, f, expr='medo', look=-.75, escurece=.5, shake=.2, **EU)
        cam = (621, 1104 + kick(f, lv, .7) * 10, lerp(1.3, 1.08, easeOut(ramp(f, lv, lv + 10))) * (1 + .0009 * f), 0); CAM[3] = cam
        return c, cam, 'sombrio_noite'
    cam = (lerp(700, 640, smooth(ramp(f, 0, 40))), 1150, 1.1 * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'sombrio_noite'


def s4(f):
    c = sala_bg('noite').copy()
    mesa(c)
    su = wt(4, 'subiu') - 3; pa = wt(4, 'pata') - 3; es = wt(4, 'escrever') - 3
    u = easeOut(ramp(f, su, su + 10))
    feet = lerp(1560, 1250, u) - 120 * math.sin(math.pi * u)
    x = lerp(300, 620, u)
    pata = 4 if f >= es else (2 if f >= pa else 0)
    if f < su: x, feet = 300, 1560
    lousa(c, RESP[:1], ramp(f, es, es + 40), 76, 420)
    put_gato(c, x, feet, 520, f, pata=pata, look=0)
    if f >= pa:   # nuvem de giz
        d = ImageDraw.Draw(c); rnd = random.Random(int(f / 3))
        for i in range(8):
            px, py = x + 120 + rnd.randint(-40, 40), feet - 300 - rnd.randint(0, 120) - (f - pa)
            d.ellipse((px - 6, py - 6, px + 6, py + 6), fill=(236, 240, 232, 120))
    t = smooth(ramp(f, 0, 140))
    cam = (621, lerp(1150, 980, t), lerp(1.0, 1.15, t) * (1 + .0009 * f), 0); CAM[4] = cam
    return c, cam, 'sombrio_noite'


def s5(f):
    c = sala_bg('noite').copy()
    mesa(c)
    re = wt(5, 'respondia') - 3
    lousa(c, RESP, lerp(.35, 1, ramp(f, re, re + 50)), 76, 420)
    papel(c, 470, 1225, .9, rot=6); papel(c, 520, 1215, .9, rot=-8); papel(c, 760, 1220, .9, rot=4)
    put_gato(c, 620, 1250, 520, f, pata=4 if f >= re and (f // 8) % 2 == 0 else 1, look=0)
    cam = (621, lerp(1000, 1080, smooth(ramp(f, 0, 120))), lerp(1.15, 1.05, smooth(ramp(f, 0, 120))) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'sombrio_noite'


def s6(f):
    c = sala_bg('noite').copy()
    mesa(c)
    lousa(c, RESP, 1, 76, 420)
    mi = wt(6, 'olhou') - 3
    put_gato(c, 620, 1250, 520, f, pata=0, look=1 if f >= mi else 0, brilho=1 if f >= mi else 0, **({'blink': 0} if f >= mi else {}))
    t = easeOut(ramp(f, mi, mi + 12))
    cam = (621, lerp(1080, 1060, t), lerp(1.05, 1.45, t) * (1 + .0009 * f), 0)
    cam = (cam[0], cam[1] + kick(f, wt(6, 'mim') - 3, .7) * 10, cam[2], 0); CAM[6] = cam
    return c, cam, 'sombrio_noite'


def s7(f):
    c = sala_bg('noite').copy()
    mesa(c)
    ob = wt(7, 'obrigado') - 3; fim = wt(7, 'segredo') + 4
    lousa(c, ['OBRIGADO POR', 'GUARDAR', 'O SEGREDO.'], ramp(f, ob, fim), 84, 420)
    put_gato(c, 620, 1250, 520, f, pata=4 if f < fim else 0, look=0)
    t = smooth(ramp(f, 0, 100))
    cam = (621, lerp(900, 820, t), lerp(1.12, 1.2, t) * (1 + .0009 * f), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


def s8(f):
    c = corredor_bg('dia').copy()
    put_gato(c, 1105, 650, 200, f, look=-1)   # em cima do armário sem número
    lia(c, 520, f, expr='sorriso', look=.75)
    se = wt(8, 'nao') - 3
    if f >= se:   # CLOSE final olhando pra câmera
        c = put_close(c, f, expr='sorriso', look=0, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, se, se + 12))) * (1 + .0012 * (f - se)), 0); CAM[8] = cam
        return c, cam, 'vivo'
    t = smooth(ramp(f, 0, 80))
    cam = (lerp(800, 700, t), 1100, lerp(1.2, 1.08, t) * (1 + .0009 * f), 0); CAM[8] = cam
    return c, cam, 'vivo'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        stamp(im, 'PARTE 2', 540, 200, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)), 110, big=True)
    elif si == 1:
        de = wt(1, 'dele') - 3; al = wt(1, 'alguem') - 3
        stamp(im, 'O TÉO', 230, 150, back(ramp(f, 0, 8)), 64)
        card(im, 'A pergunta do Téo', 'alguém vai descobrir quem escreve?', 540, 380, ramp(f, al, al + 10))
    elif si == 2:
        n = wt(2, 'noite') - 3; es = wt(2, 'escondi') - 3
        stamp(im, 'NAQUELA NOITE', 540, 180, back(ramp(f, n, n + 8)), 64)
        card(im, 'Esconderijo', 'armário do fundo', 330, 420, ramp(f, es + 8, es + 18))
    elif si == 3:
        pa = wt(3, 'passos') - 3; lv = wt(3, 'leves') - 3
        if f < lv:
            painel(im, 'HORA', '00:00', 540, 300, ramp(f, 0, 10))
            burst(im, 'TIP TIP', 320, 1100, back(ramp(f, pa, pa + 8)), 56)
        else:
            burst(im, 'TIP TIP', 540, 250, back(ramp(f, lv, lv + 8)), 56)
    elif si == 4:
        g = wt(4, 'gato') - 3
        burst(im, 'MIAU?!', 830, 1050, back(ramp(f, g, g + 8)) * (1 - ramp(f, g + 40, g + 46)), 60)
    elif si == 5:
        b = wt(5, 'bilhetes') - 3
        card(im, 'Bilhetes', 'do armário sem número', 540, 170, ramp(f, b, b + 10))
    elif si == 6:
        m = wt(6, 'mim') - 3
        burst(im, '!!', 200, 900, back(ramp(f, m, m + 8)), 70)
    elif si == 8:
        se = wt(8, 'nao') - 3
        if f < se:
            stamp(im, 'NO DIA SEGUINTE', 540, 180, back(ramp(f, 0, 8)), 64)
        else:
            stamp(im, 'SEGREDO', 540, 260, back(ramp(f, se + 6, se + 14)), 90, rot=3)
    return grao(im.convert('RGB'), lf)
