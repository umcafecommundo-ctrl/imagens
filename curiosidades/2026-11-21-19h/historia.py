"""Formato MISTÉRIO: "O espantalho que aponta", PARTE 1 (21/11/2026, 19h). História inventada.
Narrador: menino de cabelo castanho-avermelhado, camiseta amarela e calça azul (mesmas cores na parte 2). Avó: cabelo branco
em coque, óculos, vestido lilás.
Premissa: na fazenda da avó há um espantalho no milharal que amanhece todo dia com o braço apontando pra um lugar diferente; onde
ele aponta aparece algo perdido (chave do trator, balde); regra: ninguém encosta nele; ninguém sabe quem mexe (a fazenda dorme
às nove); em trinta anos achou tudo, menos a aliança que a avó perdeu; hoje o braço aponta pra janela do quarto do narrador.
Cenários/cores: s0-s2 fazenda de manhã (vivo) | s3 fazenda fim de tarde (tarde) | s4 fazenda à noite (sombrio_noite) |
s5 cozinha, lembrança (tarde) | s6 fazenda com neblina + CLOSE (sombrio) | s7 casa de manhã fria + CLOSE final (frio)."""
from kit import *
import kit
from sombrio import *

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#8a4a2a', pele='#f0c8a0', roupa='#e8b04a', calca='#3b6ea5')
VO = dict(penteado='coque', cabelo='#e4e4e0', pele='#e8c4a4', roupa='#9b6fb0', calca='#6a5480', oculos=True, velho=True)

LINES = [
    "Na fazenda da minha avó, tem um espantalho no meio do milharal.",
    "Toda manhã, ele amanhece com o braço apontando pra um lugar diferente.",
    "E onde ele aponta, sempre aparece alguma coisa perdida. A chave do trator. O balde sumido.",
    "A regra da minha avó é uma só: ninguém encosta no espantalho.",
    "Ninguém sabe quem mexe nele. A fazenda inteira dorme às nove.",
    "Em trinta anos, ele achou tudo. Menos a aliança que a minha avó perdeu.",
    "Mas hoje de manhã, o braço dele não apontava pro milharal.",
    "Apontava direto pra janela do meu quarto.",
]
FALA_TIKTOK = "Quer a parte dois? Comenta parte dois, e segue pra não perder!"
CTA_TEXTO = "PARTE 2?"
CTA_CARD = cta_card
TWIST = 6
FLASH = []
CHECK = [(0, 'espantalho', 6), (1, 'braco', 4), (2, 'chave', 4), (2, 'balde', 4), (3, 'regra', 4), (3, 'encosta', 6),
         (4, 'nove', 6), (5, 'alianca', 6), (6, 'milharal', 6), (7, 'quarto', 10)]
CAM = {}


def SFX(s):
    for si in (0, 1, 2): s.patter(s.W(si, LINES[si].split()[0].strip(',.:')) - 4, s.W(si, LINES[si].split()[0].strip(',.:')) + 40, 4, .05)
    s.whoosh(s.W(0, 'espantalho') - 6, .5, .2)
    for i in range(4): s.thunk(s.W(1, 'diferente') - 30 + i * 8, 300, .25)
    s.ting(s.W(2, 'chave'), .25); s.ting(s.W(2, 'balde'), .25)
    s.thunk(s.W(3, 'regra') - 2, 90, .7)
    s.trill(s.W(4, 'nove'), .6, .12)
    s.ting(s.W(5, 'alianca'), .3)
    s.whoosh(s.W(6, 'milharal') - 6, .6, .3)
    s.thunk(s.W(7, 'janela') - 2, 90, .8); s.thunk(s.W(7, 'quarto') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


GRAMA = {'dia': '#8cc46a', 'tarde': '#b4b062', 'neblina': '#8a9a86', 'noite': '#3d4d40', 'frio': '#9db7a4'}
MORRO = {'dia': '#6fae5a', 'tarde': '#9c8e58', 'neblina': '#94a09a', 'noite': '#33423a', 'frio': '#a9bdb4'}
MILHO = {'dia': ('#5f9c3e', '#e8c75a'), 'tarde': ('#7f8a3c', '#e0a64a'), 'neblina': ('#6f7f68', '#b8b08a'),
         'noite': ('#2f4232', '#6b6a48'), 'frio': ('#7d9a84', '#c8c49a')}
JANELA = (150, 860, 330, 1040)   # janela do quarto na casa da fazenda (palco)


@lru_cache(maxsize=8)
def fazenda_bg(luz='dia'):
    """casa vermelha à esquerda (janela do quarto em JANELA), morros, milharal à direita; chão em y≈1300+."""
    c = ceu('neblina' if luz == 'frio' else luz).copy()
    p = Pen(W_, H_)
    p.poly([(0, 1000)] + [(x, 900 + 70 * math.sin(x / 210) + 40 * math.sin(x / 90)) for x in range(0, W_ + 1, 40)] + [(W_, 1300), (0, 1300)], hexc(MORRO[luz]))
    p.poly([(0, 1180), (W_, 1140), (W_, H_), (0, H_)], hexc(GRAMA[luz]))
    rnd = random.Random(4)
    for i in range(60):
        x, y = rnd.randint(0, W_), rnd.randint(1500, 2200)
        p.stroke([(x, y), (x - 6, y - 26)], 4, mul(hexc(GRAMA[luz]), .8))
    # casa
    p.shape([(40, 760), (440, 760), (440, 1290), (40, 1290)], hexc('#c4523f'), hexc('#9c3e30'), 7, 14)
    p.shape([(10, 780), (240, 600), (470, 780)], hexc('#5b4636'), None, 7, 0)
    p.shape([(180, 1110), (300, 1110), (300, 1290), (180, 1290)], hexc('#7a5230'), None, 6, 0)
    x0, y0, x1, y1 = JANELA
    p.shape([(x0 - 14, y0 - 14), (x1 + 14, y0 - 14), (x1 + 14, y1 + 14), (x0 - 14, y1 + 14)], hexc('#f4f1ea'), None, 6, 0)
    lit = luz == 'noite'
    p.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], hexc('#f2e2a0') if lit else hexc('#4b5a6a'))
    p.stroke([((x0 + x1) / 2, y0), ((x0 + x1) / 2, y1)], 8, hexc('#f4f1ea'))
    p.stroke([(x0, (y0 + y1) / 2), (x1, (y0 + y1) / 2)], 8, hexc('#f4f1ea'))
    # milharal (fileiras atrás do espantalho)
    verde, espiga = MILHO[luz]
    for row, (yb, hh) in enumerate(((1200, 300), (1290, 330), (1390, 360))):
        for x in range(520 + row * 30, W_ + 40, 70):
            xx = x + rnd.randint(-10, 10)
            p.line([(xx, yb), (xx + 6, yb - hh)], hexc(verde), 12, 4)
            for k in (.35, .6):
                yy = yb - hh * k
                p.line([(xx, yy), (xx + 50, yy - 40)], hexc(verde), 9, 3)
                p.line([(xx, yy + 20), (xx - 46, yy - 16)], hexc(verde), 9, 3)
            p.shape(ell_pts(xx + 14, yb - hh * .5, 12, 30, 12), hexc(espiga), None, 4, 0)
    base = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(base)
    if luz == 'frio': c.alpha_composite(Image.new('RGBA', (W_, H_), (200, 215, 230, 50)))
    return c


def braco_ang(alvo_x, alvo_y, x=820, feet=1480, h=900):
    sx, sy = x, feet - h * (975 - 330) / 975
    return math.degrees(math.atan2(alvo_y - sy, alvo_x - sx))


@lru_cache(maxsize=128)
def espantalho_img(h, ang=0):
    """600x1000, base do poste em y≈975; ang = direção do braço direito em graus (0 = direita, 180 = esquerda)."""
    p = Pen(600, 1000)
    p.shape([(288, 330), (312, 330), (312, 975), (288, 975)], hexc('#8a6a42'), None, 5, 0)
    # braço fixo (esquerdo, caído) e braço que aponta
    p.line([(240, 370), (150, 560)], hexc('#c0453a'), 40, 6)
    for k in range(3): p.stroke([(150, 560), (130 + k * 20, 610)], 6, hexc('#e3c35a'))
    a = math.radians(ang); L = 230
    sx = 240 if 90 < ang % 360 < 270 else 360
    ex, ey = sx + L * math.cos(a), 370 + L * math.sin(a)
    # camisa xadrez
    p.shape([(220, 340), (380, 340), (400, 640), (200, 640)], hexc('#c0453a'), hexc('#9a3328'), 6, 12)
    for k in range(3):
        p.stroke([(240 + k * 55, 350), (230 + k * 60, 630)], 5, hexc('#9a3328'))
        p.stroke([(215, 420 + k * 70), (390, 420 + k * 70)], 5, hexc('#9a3328'))
    p.line([(sx, 370), (ex, ey)], hexc('#c0453a'), 40, 6)
    for k in range(3): p.stroke([(ex, ey), (ex + 50 * math.cos(a + (k - 1) * .3), ey + 50 * math.sin(a + (k - 1) * .3))], 7, hexc('#e3c35a'))
    for k in range(4): p.stroke([(230 + k * 45, 640), (225 + k * 48, 700)], 7, hexc('#e3c35a'))
    # cabeça de saco
    p.shape(ell_pts(300, 230, 110, 120, 36), hexc('#e2cfa2'), hexc('#c4ae7c'), 7, 14)
    for ex2 in (255, 345):
        p.dot(ex2, 220, 30, hexc('#2a2420'), 5); p.dot(ex2 + 8, 212, 7, hexc('#f4f1ea'))
    p.stroke([(240, 290), (270, 300), (300, 292), (330, 300), (360, 290)], 6)
    for k in range(6): p.stroke([(252 + k * 20, 284), (252 + k * 20, 306)], 4)
    # chapéu de palha
    p.shape(ell_pts(300, 140, 190, 34, 30), hexc('#e8c46a'), hexc('#c9a24a'), 6, 6)
    p.shape([(210, 140), (225, 60), (375, 60), (390, 140)], hexc('#e8c46a'), hexc('#c9a24a'), 6, 8)
    p.stroke([(214, 118), (386, 118)], 12, hexc('#8a4a2a'))
    return p.img.resize((max(4, int(h * .6)), h), Image.LANCZOS)


def put_esp(c, x, feet, h, ang, f=0):
    if h < 8: return
    im = espantalho_img(int(h // 4 * 4), round(ang / 3) * 3)
    sway = 2 * math.sin(f * .07)
    if sway: im = im.rotate(sway, Image.BICUBIC, center=(im.width / 2, im.height))
    c.alpha_composite(im, (int(x - im.width / 2), int(feet - im.height * 975 / 1000)))


@lru_cache(maxsize=8)
def obj_img(nome, h):
    p = Pen(300, 300)
    if nome == 'chave':
        p.shape(ell_pts(90, 150, 60, 60, 30), hexc('#e8c24a'), hexc('#c49a2a'), 6, 8)
        p.dot(90, 150, 22, hexc('#8cc46a'), 5)
        p.shape([(140, 135), (280, 135), (280, 165), (140, 165)], hexc('#e8c24a'), None, 6, 0)
        for x in (220, 255): p.shape([(x, 165), (x + 18, 165), (x + 18, 200), (x, 200)], hexc('#e8c24a'), None, 5, 0)
    elif nome == 'balde':
        p.shape([(60, 90), (240, 90), (210, 280), (90, 280)], hexc('#6f9fc8'), hexc('#4f7fa8'), 6, 12)
        p.shape(ell_pts(150, 90, 92, 22, 24), hexc('#3d5f80'), None, 6, 0)
        p.arc(150, 90, 95, 70, 180, 360, 8)
    elif nome == 'alianca':
        p.shape(ell_pts(150, 150, 110, 110, 40), hexc('#f2d060'), hexc('#c9a030'), 8, 14)
        p.shape(ell_pts(150, 150, 72, 72, 40), hexc('#2a2420'), None, 6, 0)
    return p.img.resize((h, h), Image.LANCZOS)


def put_obj(c, nome, x, y, h):
    if h < 8: return
    im = obj_img(nome, int(h // 4 * 4)); c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def eu(c, x, f, feet=1760, h=960, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def avo(c, x, f, feet=1760, h=900, **kw):
    put_menino(c, x, feet, h, f, seed=4, **dict(VO, **kw))


def brilho(c, x, y, f, s=1.0):
    if s <= .05: return
    d = ImageDraw.Draw(c)
    for k in range(4):
        a = k * math.pi / 2 + f * .05; r = 60 * s
        d.line((x + 20 * math.cos(a), y + 20 * math.sin(a), x + r * math.cos(a), y + r * math.sin(a)), fill=(255, 246, 190, 230), width=7)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = fazenda_bg('dia').copy()
    put_esp(c, 820, 1480, 900, -20, f)
    eu(c, 440, f, feet=1900, h=980, expr='neutro', look=.75)
    t = smooth(ramp(f, 0, 110))
    cam = (lerp(700, 640, t), lerp(1000, 1180, t), lerp(1.3, 1.05, t) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'vivo'


ANGS = [-20, 200, 30, 160, -40, 10]


def s1(f):
    c = fazenda_bg('dia').copy()
    br = wt(1, 'braco') - 3
    k = max(0, int((f - br) / 10)) if f >= br else 0
    ang = ANGS[min(k, len(ANGS) - 1)]
    put_esp(c, 820, 1480, 900, ang, f)
    cam = (820, 1030 + kick(f, br + k * 10, .4) * 6 if f >= br else 1030, 1.4 * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = fazenda_bg('dia').copy()
    ch = wt(2, 'chave') - 3; ba = wt(2, 'balde') - 3
    ang = 40 if f < ba else 155
    put_esp(c, 820, 1480, 900, ang, f)
    if f >= ch:
        put_obj(c, 'chave', 1110, 1620, int(140 * back(ramp(f, ch, ch + 8))) or 4); brilho(c, 1110, 1620, f, ramp(f, ch, ch + 8))
    if f >= ba:
        put_obj(c, 'balde', 520, 1640, int(190 * back(ramp(f, ba, ba + 8))) or 4)
    cam = (800, 1250, 1.05 * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = fazenda_bg('tarde').copy()
    put_esp(c, 900, 1440, 820, -20, f)
    avo(c, 380, f, expr='neutro', look=.75)
    eu(c, 640, f, feet=1800, h=860, expr='preocupado', look=-.5)
    t = smooth(ramp(f, 0, 120))
    cam = (lerp(560, 620, t), 1220, lerp(1.05, 1.15, t) * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = fazenda_bg('noite').copy()
    put_esp(c, 820, 1480, 900, -20, f)
    t = smooth(ramp(f, 0, 140))
    cam = (lerp(500, 760, t), lerp(1100, 1000, t), lerp(1.0, 1.3, t) * (1 + .0009 * f), 0); CAM[4] = cam
    return c, cam, 'sombrio_noite'


def s5(f):
    c = CEN('cozinha', 'golden').convert('RGBA').resize((W_, H_)).copy()
    al = wt(5, 'alianca') - 3
    avo(c, 440, f, feet=1760, h=920, expr='preocupado' if f >= al else 'neutro', look=.5)
    eu(c, 860, f, feet=1780, h=860, expr='neutro', look=-.75)
    t = smooth(ramp(f, 0, 120))
    cam = (lerp(640, 560, t), lerp(1250, 1150, t), lerp(1.05, 1.2, t) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = fazenda_bg('neblina').copy()
    ang = braco_ang(240, 950)
    put_esp(c, 820, 1480, 900, ang, f)
    nb = neblina_img(1.4); o2 = int(f * 1.5) % W_
    c.alpha_composite(nb.crop((o2, 0, o2 + W_, 420)), (0, 1150))
    na = wt(6, 'nao') - 3; mi = wt(6, 'milharal') - 3
    if f >= na:   # CLOSE: susto
        c = put_close(c, f, expr='choque', look=-.75, shake=.3, **EU)
        cam = (621, 1104 + kick(f, na, .8) * 12, lerp(1.3, 1.08, easeOut(ramp(f, na, na + 10))) * (1 + .0009 * f), 0); CAM[6] = cam
        return c, cam, 'sombrio'
    cam = (lerp(820, 760, smooth(ramp(f, 0, 60))), 1050, 1.3 * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'sombrio'


def s7(f):
    c = fazenda_bg('frio').copy()
    ang = braco_ang(240, 950)
    put_esp(c, 820, 1480, 900, ang, f)
    ja = wt(7, 'janela') - 3; qu = wt(7, 'quarto') + 6
    if f >= qu:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.4, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, qu, qu + 10))) * (1 + .0012 * (f - qu)), 0); CAM[7] = cam
        return c, cam, 'frio'
    t = easeOut(ramp(f, 0, ja + 6))
    cam = (lerp(760, 300, t), lerp(1000, 980, t), lerp(1.2, 1.8, t) * (1 + .0009 * f), 0); CAM[7] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        stamp(im, 'PARTE 1', 540, 300, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)), 110, big=True)
        stamp(im, 'NA FAZENDA DA MINHA AVÓ', 540, 300, back(ramp(f, 50, 58)), 64)
        e = wt(0, 'espantalho') - 3
        ax, ay = to_out(0, 820, 900)
        card(im, 'Espantalho', 'no meio do milharal', 790, 1080, ramp(f, e, e + 10), alvo=(ax, ay))
    elif si == 1:
        d = wt(1, 'diferente') - 3
        painel(im, 'DIA', '%03d' % (101 + min(5, max(0, int((f - wt(1, 'braco') + 3) / 10)))), 540, 230, ramp(f, 2, 12))
        card(im, 'Toda manhã', 'um lugar diferente', 790, 1150, ramp(f, d, d + 10))
    elif si == 2:
        ch = wt(2, 'chave') - 3; ba = wt(2, 'balde') - 3
        card(im, 'Achado', 'a chave do trator', 790, 1100, ramp(f, ch, ch + 10) * (1 - ramp(f, ba - 4, ba)))
        card(im, 'Achado', 'o balde sumido', 300, 1100, ramp(f, ba, ba + 10))
    elif si == 3:
        r = wt(3, 'regra') - 3; e = wt(3, 'encosta') - 3
        stamp(im, 'A REGRA', 540, 260, back(ramp(f, r, r + 8)), 110, big=True)
        card(im, 'Ninguém encosta', 'no espantalho', 300, 440, ramp(f, e, e + 10))
    elif si == 4:
        n = wt(4, 'nove') - 3
        painel(im, 'HORA', '21:00', 540, 240, ramp(f, n, n + 10))
        interrog(im, 820, 640, f, ramp(f, wt(4, 'sabe') - 3, wt(4, 'sabe') + 7))
    elif si == 5:
        al = wt(5, 'alianca') - 3
        stamp(im, 'TRINTA ANOS', 540, 200, back(ramp(f, 0, 8)), 64)
        card(im, 'Aliança da vó', 'nunca achada', 540, 420, ramp(f, al, al + 10))
    elif si == 6:
        stamp(im, 'HOJE DE MANHÃ', 540, 200, back(ramp(f, 0, 8)) * (1 - ramp(f, wt(6, 'nao') - 6, wt(6, 'nao') - 2)), 64)
        mi = wt(6, 'nao') - 3
        burst(im, '?!', 850, 280, back(ramp(f, mi, mi + 8)), 70)
    elif si == 7:
        qu = wt(7, 'quarto') + 6
        if f < qu:
            ja = wt(7, 'janela') - 3
            card(im, 'Meu quarto', 'a janela da frente', 540, 300, ramp(f, ja, ja + 10))
    return grao(im.convert('RGB'), lf)
