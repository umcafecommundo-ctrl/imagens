"""Formato MISTÉRIO: "A lousa que responde", PARTE 1 (21/11/2026, 07h). História inventada.
Narradora: Lia, menina de coque preto, blusa verde-água e calça roxa (mesmas cores na parte 2).
Premissa: no fim do corredor da escola há um armário sem número; quem passa uma pergunta pela fresta acha a resposta escrita
na lousa na manhã seguinte; as respostas nunca erram; regra: 1 pergunta por aluno, uma vez na vida; ninguém sabe quem escreve
(a escola fica trancada); Lia nunca usou a dela; hoje a lousa tem uma resposta com o nome dela: "SIM. FOI VOCÊ."
Cenários/cores: s0 corredor de manhã (vivo) | s1 corredor -> sala com lousa (vivo) | s2 sala de aula (vivo) |
s3 corredor fim de tarde (tarde) | s4 corredor à noite, vazio (sombrio_noite) | s5 quarto, lembrança (tarde) |
s6 sala de manhã cedo, fria (frio) + CLOSE | s7 sala com neblina/estranheza (sombrio) + CLOSE final."""
from kit import *
import kit
from sombrio import *

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='coque', cabelo='#2b1d16', pele='#c8956b', roupa='#3fa7a0', calca='#4a3b6b')

LINES = [
    "Na minha escola, no fim do corredor, tem um armário sem número.",
    "Quem passa uma pergunta pela fresta, acha a resposta escrita na lousa, na manhã seguinte.",
    "E as respostas nunca erram. A prova cai na quinta. O gato sumido está no telhado.",
    "A regra é uma só: cada aluno pode fazer uma pergunta. Uma vez na vida.",
    "Ninguém sabe quem escreve. A escola fica trancada a noite inteira.",
    "Eu nunca usei a minha pergunta. Estava guardando pra algo importante.",
    "Mas hoje de manhã, tinha uma resposta na lousa. Com o meu nome.",
    "E dizia só: sim. Foi você.",
]
FALA_TIKTOK = "Quer a parte dois? Comenta parte dois, e segue pra não perder!"
CTA_TEXTO = "PARTE 2?"
CTA_CARD = cta_card
TWIST = 6
FLASH = []
CHECK = [(0, 'numero', 6), (1, 'fresta', 4), (1, 'lousa', 6), (2, 'quinta', 4), (2, 'telhado', 4), (3, 'regra', 4),
         (3, 'vida', 6), (4, 'trancada', 6), (5, 'guardando', 6), (6, 'nome', 8), (7, 'voce', 10)]
CAM = {}


def SFX(s):
    for si in (0, 1, 3): s.patter(s.W(si, LINES[si].split()[0].strip(',.:')) - 4, s.W(si, LINES[si].split()[0].strip(',.:')) + 40, 4, .05)
    s.thunk(s.W(0, 'numero') - 2, 140, .6)
    s.whoosh(s.W(1, 'fresta') - 6, .5, .2); s.ting(s.W(1, 'lousa'), .25)
    s.ting(s.W(2, 'quinta'), .2); s.ting(s.W(2, 'telhado'), .2)
    s.thunk(s.W(3, 'regra') - 2, 90, .7); s.thunk(s.W(3, 'vida') - 2, 110, .5)
    s.thunk(s.W(4, 'trancada') - 2, 70, .9)
    s.trill(s.W(5, 'guardando'), .6, .12)
    s.thunk(s.W(6, 'nome') - 2, 80, 1.0)
    s.thunk(s.W(7, 'voce') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


TINT = {'dia': None, 'tarde': (255, 150, 80, 46), 'noite': (14, 22, 52, 150), 'frio': (180, 205, 230, 70),
        'neblina': (150, 158, 160, 80)}
CEU = {'dia': 'dia', 'tarde': 'tarde', 'noite': 'noite', 'frio': 'neblina', 'neblina': 'neblina'}


def _tinge(c, luz):
    t = TINT[luz]
    if t: c.alpha_composite(Image.new('RGBA', c.size, t))
    return c


@lru_cache(maxsize=8)
def corredor_bg(luz='dia'):
    """corredor da escola: janelas altas, fileira de armários coloridos, o último (à direita) cinza, sem número, com fresta."""
    c = Image.new('RGBA', (W_, H_), (0, 0, 0, 255))
    p = Pen(W_, H_)
    p.poly([(0, 0), (W_, 0), (W_, 1560), (0, 1560)], hexc('#f1e3c0'))
    p.poly([(0, 1180), (W_, 1180), (W_, 1560), (0, 1560)], hexc('#9cc9b4'))   # barrado
    p.poly([(0, 1560), (W_, 1560), (W_, H_), (0, H_)], hexc('#d8c9a8'))
    for y in range(1620, H_, 120): p.stroke([(0, y), (W_, y)], 3, hexc('#c2b28f'))
    for x in range(-200, W_ + 400, 200): p.stroke([(x, 1560), (x - 260, H_)], 3, hexc('#c2b28f'))
    p.stroke([(0, 1560), (W_, 1560)], 7)
    base = p.img.resize((W_, H_), Image.LANCZOS)
    sky = ceu(CEU[luz])
    for x0 in (60, 460, 860):
        base.alpha_composite(sky.crop((x0, 260, x0 + 320, 560)), (x0, 230))
    p2 = Pen(W_, H_)
    for x0 in (60, 460, 860):
        p2.stroke([(x0, 230), (x0 + 320, 230), (x0 + 320, 530), (x0, 530), (x0, 230)], 10, hexc('#f7f4ec'))
        p2.stroke([(x0 + 160, 230), (x0 + 160, 530)], 8, hexc('#f7f4ec'))
        p2.stroke([(x0 - 6, 224), (x0 + 326, 224), (x0 + 326, 536), (x0 - 6, 536), (x0 - 6, 224)], 4)
    cores = ['#4f8fc0', '#e0a43c', '#d9634f', '#5aa36f', '#4f8fc0', '#e0a43c']
    for i, col in enumerate(cores):
        x = 40 + i * 160
        p2.shape([(x, 680), (x + 150, 680), (x + 150, 1500), (x, 1500)], hexc(col), mul(hexc(col), .8), 6, 10)
        for k in range(4): p2.stroke([(x + 40, 740 + k * 22), (x + 110, 740 + k * 22)], 6, mul(hexc(col), .7))
        p2.shape([(x + 115, 1060), (x + 128, 1060), (x + 128, 1130), (x + 115, 1130)], hexc('#d0d4d6'), None, 3, 0)
        p2.shape([(x + 45, 600 + 10), (x + 105, 610), (x + 105, 650), (x + 45, 650)], hexc('#f7f4ec'), None, 3, 0)
    x = 1010   # o armário sem número
    p2.shape([(x, 640), (x + 190, 640), (x + 190, 1500), (x, 1500)], hexc('#6d7175'), hexc('#53575b'), 7, 12)
    p2.shape([(x + 30, 880), (x + 160, 880), (x + 160, 900), (x + 30, 900)], hexc('#1c1d20'), None, 4, 0)   # fresta
    p2.shape([(x + 150, 1060), (x + 166, 1060), (x + 166, 1140), (x + 150, 1140)], hexc('#b9bec1'), None, 3, 0)
    for k in range(4): p2.stroke([(x + 50, 720 + k * 22), (x + 140, 720 + k * 22)], 6, hexc('#55595d'))
    base.alpha_composite(p2.img.resize((W_, H_), Image.LANCZOS))
    c.alpha_composite(base)
    return _tinge(c, luz)


@lru_cache(maxsize=8)
def sala_bg(luz='dia'):
    c = Image.new('RGBA', (W_, H_), (0, 0, 0, 255))
    c.alpha_composite(CEN('escola', 'day').convert('RGBA').resize((W_, H_)))
    # apaga os rabiscos da lousa
    d = ImageDraw.Draw(c); d.rectangle((150, 360, 1090, 850), fill=(47, 93, 74, 255))
    return _tinge(c, luz)


F_GIZ = GF + 'ofl/comicrelief/ComicRelief-Bold.ttf'


def lousa(c, linhas, t=1.0, size=80, y0=440, cor=(238, 242, 234)):
    """escreve na lousa (coordenadas do palco) com 'giz'; t = 0..1 quanto do texto já apareceu."""
    if t <= 0: return
    d = ImageDraw.Draw(c); fnt = font(F_GIZ, size)
    total = sum(len(l) for l in linhas); n = int(round(total * min(1, t)))
    for i, l in enumerate(linhas):
        vis = l[:max(0, n)]; n -= len(l)
        tw = d.textlength(l, font=fnt)
        d.text((620 - tw / 2, y0 + i * (size + 26)), vis, font=fnt, fill=cor + (255,))


def papel(c, x, y, s=1.0, rot=0):
    if s <= .05: return
    im = Image.new('RGBA', (130, 70), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon([(4, 10), (124, 4), (126, 62), (6, 66)], fill=(250, 246, 232, 255), outline=(36, 30, 32, 255))
    d.line([(4, 10), (124, 4), (126, 62), (6, 66), (4, 10)], fill=(36, 30, 32, 255), width=4)
    d.line([(65, 7), (66, 64)], fill=(190, 180, 160, 255), width=3)
    im = im.resize((max(4, int(130 * s)), max(4, int(70 * s))), Image.LANCZOS)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))


def lia(c, x, f, feet=1760, h=960, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


COLEGA = dict(penteado='curto', cabelo='#d9a441', pele='#efc9a4', roupa='#7a9bd6', calca='#3a3f46')


def colega(c, x, f, feet=1740, h=900, **kw):
    put_menino(c, x, feet, h, f, seed=5, **dict(COLEGA, **kw))


# ---------------------------------------------------------------- cenas
def s0(f):
    c = corredor_bg('dia').copy()
    lia(c, 520, f, expr='neutro', look=.75)
    t = smooth(ramp(f, 0, 100))
    cam = (lerp(820, 700, t), lerp(1100, 1180, t), lerp(1.3, 1.08, t) * (1 + .0009 * f), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    lo = wt(1, 'resposta') - 3
    if f < lo:
        c = corredor_bg('dia').copy()
        fr = wt(1, 'fresta') - 3
        x = lerp(820, 860, ramp(f, 0, fr))
        colega(c, x, f, walk=0, expr='neutro', look=.75)
        hx, hy = x + 120, 1080
        u = easeOut(ramp(f, fr - 10, fr + 6))
        papel(c, lerp(hx, 1105, u), lerp(hy, 890, u), 1 - .6 * ramp(f, fr + 2, fr + 8), rot=lerp(-10, 0, u))
        cam = (900, 1050, 1.25 * (1 + .0009 * f), 0); CAM[1] = cam
        return c, cam, 'vivo'
    c = sala_bg('dia').copy()
    lousa(c, ['?  ->  !'], 1, 120, 520)
    g = f - lo
    cam = (621, 900 + 60 * smooth(ramp(g, 0, 60)), lerp(1.35, 1.15, easeOut(ramp(g, 0, 14))) * (1 + .0009 * f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = sala_bg('dia').copy()
    q = wt(2, 'prova') - 3; g = wt(2, 'gato') - 3
    lousa(c, ['A PROVA CAI', 'NA QUINTA.'], ramp(f, q, q + 25), 78, 410)
    lousa(c, ['O GATO ESTÁ', 'NO TELHADO.'], ramp(f, g, g + 25), 78, 640)
    lia(c, 300, f, feet=1980, h=1000, expr='sorriso' if f >= q else 'neutro', look=.5)
    colega(c, 980, f, feet=1960, h=940, expr='choque' if f >= g else 'sorriso', look=-.5)
    cam = (621, 1150, lerp(1.0, 1.1, smooth(ramp(f, 0, 140))) * (1 + .0009 * f), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = corredor_bg('tarde').copy()
    lia(c, 560, f, expr='neutro', look=.75)
    hx, hy = mao_dir(560, 1760, 960)
    papel(c, hx + 10, hy - 10, .9, rot=8)
    t = smooth(ramp(f, 0, 120))
    cam = (lerp(700, 820, t), 1150, lerp(1.05, 1.2, t) * (1 + .0009 * f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = corredor_bg('noite').copy()
    d = ImageDraw.Draw(c)
    for x0 in (60, 460, 860):   # luar no chão
        d.polygon([(x0, 1580), (x0 + 320, 1580), (x0 + 200, 2100), (x0 - 140, 2100)], fill=(150, 170, 210, 26))
    tr = wt(4, 'trancada') - 3
    t = smooth(ramp(f, 0, 140))
    cam = (lerp(560, 960, t), lerp(1150, 1000, t), lerp(1.0, 1.35, t) * (1 + .0009 * f), 0)
    cam = (cam[0], cam[1] + kick(f, tr, .8) * 10, cam[2], 0); CAM[4] = cam
    return c, cam, 'sombrio_noite'


def s5(f):
    c = quarto_bg('tarde').copy()
    lia(c, 560, f, expr='neutro', look=.5)
    hx, hy = mao_dir(560, 1760, 960)
    papel(c, hx + 10, hy - 30, 1.1, rot=-6)
    cam = (640, lerp(1200, 1260, smooth(ramp(f, 0, 120))), lerp(1.08, 1.22, smooth(ramp(f, 0, 120))) * (1 + .0009 * f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = sala_bg('frio').copy()
    no = wt(6, 'nome') - 3; lo = wt(6, 'lousa') - 3
    lousa(c, ['LIA:'], ramp(f, lo, lo + 10), 120, 470)
    lia(c, 621, f, feet=1900, h=960, expr='choque' if f >= no else 'neutro', look=0)
    if f >= no:   # CLOSE no susto
        c = put_close(c, f, expr='choque', look=0, shake=.3, **EU)
        cam = (621, 1104 + kick(f, no, .8) * 12, lerp(1.3, 1.08, easeOut(ramp(f, no, no + 10))) * (1 + .0009 * f), 0); CAM[6] = cam
        return c, cam, 'frio'
    t = smooth(ramp(f, 0, 90))
    cam = (621, lerp(1300, 900, t), lerp(1.0, 1.2, t) * (1 + .0009 * f), 0); CAM[6] = cam
    return c, cam, 'frio'


def s7(f):
    c = sala_bg('neblina').copy()
    si_ = wt(7, 'sim') - 3; vo = wt(7, 'foi') - 3
    lousa(c, ['LIA:'], 1, 120, 420)
    lousa(c, ['SIM.', 'FOI VOCÊ.'], ramp(f, si_, vo + 14), 110, 570)
    fim = wt(7, 'voce') + 8
    if f >= fim:   # CLOSE final
        c = put_close(c, f, expr='medo', look=0, escurece=.45, suor=1, **EU)
        cam = (621, 1104, lerp(1.3, 1.08, easeOut(ramp(f, fim, fim + 10))) * (1 + .0012 * (f - fim)), 0); CAM[7] = cam
        return c, cam, 'sombrio'
    lia(c, 621, f, feet=1760, h=760, expr='preocupado', look=0)
    cam = (621, lerp(850, 800, smooth(ramp(f, 0, 60))), 1.15 * (1 + .0012 * f), 0); CAM[7] = cam
    return c, cam, 'sombrio'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        stamp(im, 'PARTE 1', 540, 300, back(ramp(f, 0, 8)) * (1 - ramp(f, 44, 50)), 110, big=True)
        stamp(im, 'NA MINHA ESCOLA', 540, 300, back(ramp(f, 50, 58)), 80)
        n = wt(0, 'numero') - 3
        ax, ay = to_out(0, 1105, 900)
        card(im, 'Armário', 'sem número', 330, 620, ramp(f, n, n + 10), alvo=(ax, ay))
    elif si == 1:
        fr = wt(1, 'fresta') - 3; lo = wt(1, 'resposta') - 3
        if f < lo: card(im, '1 pergunta', 'pela fresta', 330, 300, ramp(f, fr, fr + 10))
        else: stamp(im, 'NA MANHÃ SEGUINTE', 540, 200, back(ramp(f, lo, lo + 8)), 64)
    elif si == 2:
        e = wt(2, 'erram') - 3
        painel(im, 'ACERTOS', '100%', 540, 830, ramp(f, e, e + 10))
    elif si == 3:
        r = wt(3, 'regra') - 3; v = wt(3, 'vez') - 3
        stamp(im, 'A REGRA', 540, 300, back(ramp(f, r, r + 8)), 110, big=True)
        card(im, '1 pergunta', 'uma vez na vida', 330, 560, ramp(f, v, v + 10))
    elif si == 4:
        tr = wt(4, 'trancada') - 3
        painel(im, 'HORA', '00:00', 540, 260, ramp(f, 2, 12), glitch=1 if tr <= f < tr + 10 and f % 4 < 2 else 0)
        interrog(im, 760, 760, f, ramp(f, wt(4, 'sabe') - 3, wt(4, 'sabe') + 7))
    elif si == 5:
        g = wt(5, 'guardando') - 3
        stamp(im, 'LEMBRANÇA', 230, 150, back(ramp(f, 0, 8)), 60)
        card(im, 'Minha pergunta', 'guardada há três anos', 330, 560, ramp(f, g, g + 10))
    elif si == 6:
        no = wt(6, 'nome') - 3
        stamp(im, 'HOJE DE MANHÃ', 540, 160, back(ramp(f, 0, 8)) * (1 - ramp(f, no - 6, no)), 64)
        burst(im, '?!', 860, 280, back(ramp(f, no, no + 8)), 70)
    elif si == 7:
        fim = wt(7, 'voce') + 8
        if f >= fim: stamp(im, 'NÃO FIZ PERGUNTA', 540, 250, back(ramp(f, fim + 4, fim + 12)), 64, rot=3)
    return grao(im.convert('RGB'), lf)
