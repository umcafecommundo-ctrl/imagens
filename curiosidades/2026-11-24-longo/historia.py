"""VÍDEO LONGO (YouTube normal, horizontal 16:9, ~2 min) no formato MISTÉRIO: "A máquina sete" (24/11/2026). História inventada,
completa (sem partes). Renderize com MOTOR_H=1.
Narrador: Léo, menino de cabelo castanho curto, pele morena, moletom mostarda e calça azul. Mãe: cabelo preto longo, blusa verde.
Dona Neide: dona da lavanderia, coque branco, óculos, blusa azul.
Premissa: na lavanderia do bairro, a máquina número sete sempre devolve uma meia a mais; regra: a meia extra vai pro mural até
o dono aparecer (e ele sempre aparece); uma meinha amarela de bebê, com patinho bordado, ninguém busca; a mãe do Léo reconhece:
é a meia que ele perdeu no primeiro dia em casa (ela guardava o outro pé). Segunda regra: ninguém usa a máquina sete depois que
escurece. Léo usa: a luz fica verde e sai uma meia cinza de velhinho com o nome dele bordado na linha torta da mãe. Dona Neide:
a máquina devolve antes o que a gente ainda vai perder. Fim: a meia está na gaveta, e toda noite ele confere se ainda está lá.
Cenários/cores: s0 CAPA close (vivo) -> lavanderia de dia (vivo) | s1 máquina 7, 11 meias (vivo) | s2 balcão + mural, a regra (vivo) |
s3 mural, donos (tarde) | s4 porta da máquina 7 (sombrio) | s5 meinha de bebê no mural (tarde) | s6 três meses -> sábado (tarde/vivo) |
s7 mãe + CLOSE (vivo) | s8 lembrança, berço (tarde) | s9 as duas meias (tarde) | s10 Dona Neide sorri (vivo) | s11 a outra regra (tarde) |
s12 sexta, escurece (tarde -> sombrio_noite) | s13 luz verde (sombrio_noite) | s14 duas meias (sombrio) | s15 nome + CLOSE (frio) |
s16 Dona Neide com a meia (sombrio_noite) | s17 CLOSE Dona Neide (sombrio) | s18 gaveta + CLOSE final (frio)."""
from kit import *
import kit
from sombrio import *
from longo import *
from PIL import ImageChops
from longo import _sky

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='curto', cabelo='#4a2e1e', pele='#c8956b', roupa='#e0a43c', calca='#3b5a8a')
MAE = dict(penteado='longo', cabelo='#26241f', pele='#c8956b', roupa='#5aa36f', calca='#4a4036')
NE = dict(penteado='coque', cabelo='#e4e4e0', pele='#f0c8a0', roupa='#4f8fc0', calca='#4a4036', oculos=True, velho=True)

LINES = [
    "Na lavanderia do meu bairro, a máquina número sete sempre devolve uma meia a mais.",
    "Eu coloco dez meias, e tiro onze. Toda vez. E a meia extra nunca é minha.",
    "A dona da lavanderia, Dona Neide, tem uma regra: a meia extra vai pro mural da parede, até o dono aparecer.",
    "E o dono sempre aparece. Uma senhora achou a meia que perdeu numa viagem. Um menino achou a meia do uniforme de futebol.",
    "Ninguém sabe de onde vêm as meias. A máquina é igual às outras. Só tem um sete pintado à mão na porta.",
    "Mas teve uma meia que ninguém veio buscar. Uma meinha amarela, de bebê, com um patinho bordado.",
    "Ela ficou no mural por três meses. Até que, num sábado, a minha mãe foi comigo buscar a roupa.",
    "Ela olhou pro mural e parou. Ficou pálida. E disse baixinho: essa meia é sua.",
    "Eu perdi essa meia quando era bebê, no meu primeiro dia em casa. A minha mãe procurou por anos.",
    "Ela ainda guardava o outro pé numa caixinha. Os dois eram iguais. Até o pontinho torto no bico do pato.",
    "A Dona Neide só sorriu e disse: a máquina sete nunca erra.",
    "Só que tinha uma coisa que a Dona Neide nunca deixava ninguém fazer: usar a máquina sete depois que escurece.",
    "Na sexta, eu fiquei até a lavanderia fechar. Quando escureceu, eu coloquei uma meia sozinha na máquina sete.",
    "A máquina girou sem fazer barulho nenhum. E a luzinha do painel ficou verde. Ela nunca fica verde.",
    "Quando a porta abriu, tinham duas meias. A minha. E uma meia cinza, enorme, de velhinho.",
    "Bordado nela, com a mesma linha torta da minha mãe, estava o meu nome.",
    "A Dona Neide pegou a meia, olhou bem e disse: essa máquina não devolve só o que a gente perdeu.",
    "Ela devolve antes. O que a gente ainda vai perder.",
    "Hoje, aquela meia de velhinho está guardada na minha gaveta. E toda noite, eu confiro se ela ainda está lá.",
]
FALA_TIKTOK = "Você colocaria uma meia na máquina sete? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 17
FLASH = []
CHECK = [(0, 'sete', 6), (1, 'onze', 8), (2, 'regra', 6), (2, 'mural', 10), (3, 'senhora', 8), (3, 'menino', 8), (4, 'igual', 6),
         (4, 'pintado', 6), (5, 'patinho', 6), (6, 'sabado', 10), (7, 'parou', 4), (7, 'sua', 6), (8, 'casa', 6), (8, 'anos', 6),
         (9, 'iguais', 6), (9, 'pato', 6), (10, 'erra', 6), (11, 'escurece', 6), (12, 'sozinha', 6), (13, 'verde', 8),
         (14, 'cinza', 8), (15, 'torta', 4), (15, 'nome', 10), (16, 'perdeu', 6), (17, 'perder', 6), (18, 'gaveta', 6), (18, 'la', 8)]
CAM = {}
CAPA = 38

M7 = 1340                       # centro da máquina sete
MX = [760, 1050, 1340, 1630, 1920]
NUMS = ['5', '6', '7', '8', '9']
DY = 885                        # centro das portas
ROXA = '#7a5ab0'


def SFX(s):
    s.thunk(2, 120, .8)
    s.patter(s.W(0, 'lavanderia') - 4, s.W(0, 'lavanderia') + 60, 4, .05)
    s.whoosh(s.W(0, 'devolve') - 6, .4, .2)
    for i in range(6): s.thunk(s.W(1, 'coloco') + i * 8, 260, .12)
    s.ting(s.W(1, 'onze'), .35)
    s.thunk(s.W(2, 'regra') - 2, 90, .7)
    s.thunk(s.W(2, 'mural') + 6, 300, .3)
    s.ting(s.W(3, 'senhora'), .2); s.ting(s.W(3, 'menino'), .2)
    s.whoosh(s.W(4, 'igual') - 6, .4, .2)
    s.ting(s.W(5, 'patinho'), .25)
    s.thunk(s.W(6, 'sabado') - 2, 140, .5)
    s.thunk(s.W(7, 'parou') - 2, 70, .9)
    s.thunk(s.W(7, 'sua') - 2, 60, .8)
    s.whoosh(s.W(8, 'casa') - 6, .6, .3)
    s.ting(s.W(9, 'iguais'), .3)
    s.ting(s.W(10, 'erra'), .3)
    s.thunk(s.W(11, 'escurece') - 2, 80, .8)
    s.patter(s.W(12, 'escureceu') - 4, s.W(12, 'sete') + 20, 4, .04)
    s.thunk(s.W(12, 'sozinha') - 2, 200, .4)
    s.whoosh(s.W(13, 'girou') - 6, .8, .3)
    s.trill(s.W(13, 'verde'), .6, .1); s.thunk(s.W(13, 'verde') - 2, 70, .8)
    s.thunk(s.W(14, 'porta') - 2, 160, .6)
    s.thunk(s.W(14, 'cinza') - 2, 70, .9)
    s.thunk(s.W(15, 'nome') - 2, 60, 1.0)
    s.whoosh(s.W(16, 'perdeu') - 6, .6, .3)
    s.thunk(s.W(17, 'antes') - 2, 70, 1.0)
    s.trill(s.W(18, 'noite'), .5, .08)
    s.thunk(s.W(18, 'confiro') - 2, 70, .9)


def to_out(si, x, y):
    cx, cy, z_, _ = CAM.get(si, (W_ / 2, H_ / 2, 1, 0))
    k = OW / W_ * z_
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def z(v, f, k=.0007):
    return v * (1 + k * f)


def leo(c, x, f, feet=1180, h=680, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def mae(c, x, f, feet=1180, h=790, **kw):
    put_menino(c, x, feet, h, f, seed=5, **dict(MAE, **kw))


def neide(c, x, f, feet=1150, h=790, **kw):
    put_menino(c, x, feet, h, f, seed=6, **dict(NE, **kw))


# ---------------------------------------------------------------- desenhos novos (Pen)
@lru_cache(maxsize=64)
def meia_img(cor, h, listra='', pato=False, nome='', ponta=''):
    """meia de lado (cano em cima, bico para a direita), 340x400 * h/400."""
    p = Pen(340, 400)
    C = hexc(cor); D = mul(C, .8)
    pts = [(70, 20), (230, 20), (230, 225), (290, 240), (325, 270), (332, 310), (315, 350), (275, 372), (120, 375), (72, 358),
           (52, 318), (62, 270), (70, 240)]
    p.shape(pts, C, D, 6, 14)
    p.poly([(72, 22), (228, 22), (228, 72), (72, 72)], mul(C, .88))
    for x in range(90, 228, 22): p.stroke([(x, 26), (x, 68)], 4, mul(C, .78))
    p.stroke([(70, 74), (230, 74)], 5)
    pc = hexc(ponta) if ponta else mul(C, .86)
    p.poly([(282, 244), (325, 272), (332, 310), (315, 350), (278, 370), (266, 310)], pc)
    p.poly([(72, 300), (56, 320), (74, 356), (120, 372), (124, 330)], pc)
    if listra:
        for y in (110, 160): p.poly([(72, y), (228, y), (228, y + 26), (72, y + 26)], hexc(listra))
    if pato:
        p.shape(ell_pts(140, 185, 46, 30, 24), hexc('#f4f1ea'), None, 4, 0)
        p.shape(ell_pts(178, 148, 24, 22, 20), hexc('#f4f1ea'), None, 4, 0)
        p.shape([(198, 142), (226, 150), (198, 160)], hexc('#f08a3a'), None, 3, 0)
        p.dot(182, 142, 5, INK)
        p.stroke([(206, 146), (213, 152)], 4, hexc('#7a2e2e'))     # o pontinho torto
    p.stroke([(70, 20), (230, 20)], 6)
    im = p.img.resize((340, 400), Image.LANCZOS)
    if nome:
        d = ImageDraw.Draw(im); fnt = font(F_MAO_L, 64)
        tw = d.textlength(nome, font=fnt)
        d.text((150 - tw / 2 + 4, 120), nome, font=fnt, fill=(190, 50, 50, 255))
        for k in range(4): d.line((110 + k * 30, 205 + (k % 2) * 6, 130 + k * 30, 200 - (k % 2) * 6), fill=(190, 50, 50, 255), width=5)
    w = max(4, int(h * 340 / 400))
    return im.resize((w, max(4, int(h))), Image.LANCZOS)


def cola(c, im, x, y):
    """alpha_composite que aceita posição negativa ou fora da tela."""
    l, t = max(0, -x), max(0, -y)
    r, b = min(im.width, c.width - x), min(im.height, c.height - y)
    if r <= l or b <= t: return
    c.alpha_composite(im.crop((l, t, r, b)), (x + l, y + t))


def put_meia(c, x, y, h, cor, rot=0, pino=False, **kw):
    if h < 10: return
    im = meia_img(cor, int(h // 4 * 4), **kw)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    cola(c, im, int(x - im.width / 2), int(y - im.height / 2))
    if pino:
        d = ImageDraw.Draw(c); r = max(4, h * .05)
        px, py = x - h * .06, y - h * .42
        d.ellipse((px - r, py - r, px + r, py + r), fill=(200, 60, 60, 255), outline=(36, 30, 32, 255), width=3)


def bico(x, y, h):
    """posição do bico do pato (pontinho torto) numa meia desenhada em (x, y) com altura h, sem rotação."""
    return x + (210 - 170) * h / 400, y + (149 - 200) * h / 400


def nome_pos(x, y, h):
    return x + (150 - 170) * h / 400 + 20 * h / 400, y + (160 - 200) * h / 400


PAREDE = {'dia': '#bfe3dc', 'tarde': '#ebcaa0', 'neblina': '#b9c4c0', 'noite': '#34465a'}
MURAL_MEIAS = [(720, 290, '#d9634f', '#f4f1ea'), (850, 300, '#4f8fc0', ''), (985, 280, '#5aa36f', '#f4f1ea'),
               (760, 455, '#e0a43c', ''), (900, 460, '#c0453a', '#26241f'), (1040, 445, '#f4f1ea', '#4f8fc0'), (1180, 455, '#7a5ab0', '')]


@lru_cache(maxsize=12)
def lavanderia_bg(luz='dia', mural='cheio'):
    """lavanderia: janela à esquerda (x 70..540, y 170..760), mural de cortiça (x 620..1250, y 150..560), placa (x 1420..2120),
    5 máquinas (centros MX, portas em y=DY, a 7 em x=1340); chão em y 1080."""
    noite = luz == 'noite'
    c = Image.new('RGBA', (W_, H_), (0, 0, 0, 255))
    c.alpha_composite(_sky(luz).crop((250, 0, 720, 590)), (70, 170))
    if luz in ('dia', 'tarde'):   # casinhas do outro lado da rua
        cs = casas_strip(luz).crop((0, 300, 470, 700))
        c.alpha_composite(cs, (70, 420))
    p = Pen(W_, H_)
    w = hexc(PAREDE[luz])
    p.poly([(0, 0), (70, 0), (70, 1080), (0, 1080)], w); p.poly([(540, 0), (W_, 0), (W_, 1080), (540, 1080)], w)
    p.poly([(70, 0), (540, 0), (540, 170), (70, 170)], w); p.poly([(70, 760), (540, 760), (540, 1080), (70, 1080)], w)
    p.poly([(0, 560), (W_, 560), (W_, 600), (0, 600)], mul(w, .9))    # faixa na parede
    p.stroke([(70, 170), (540, 170), (540, 760), (70, 760), (70, 170)], 14, hexc('#f4f1ea'))
    p.stroke([(305, 170), (305, 760)], 10, hexc('#f4f1ea'))
    p.stroke([(62, 162), (548, 162), (548, 768), (62, 768), (62, 162)], 5)
    # chão quadriculado
    e = .55 if noite else 1
    a1, a2 = mul(hexc('#f2efe6'), e), mul(hexc('#7fbfb4'), e)
    p.poly([(0, 1080), (W_, 1080), (W_, H_), (0, H_)], a1)
    for i, y in enumerate(range(1080, H_, 80)):
        for j, x in enumerate(range(-80, W_, 160)):
            xo = x + (80 if i % 2 else 0)
            p.poly([(xo, y), (xo + 80, y), (xo + 80, y + 80), (xo, y + 80)], a2)
    p.stroke([(0, 1080), (W_, 1080)], 7)
    # mural de cortiça
    p.shape([(620, 150), (1250, 150), (1250, 560), (620, 560)], mul(hexc('#c79a62'), e), mul(hexc('#a87d4a'), e), 7, 10)
    p.stroke([(620, 150), (1250, 150), (1250, 560), (620, 560), (620, 150)], 16, mul(hexc('#8a5a32'), e))
    # placa
    p.shape([(1420, 180), (2120, 180), (2120, 350), (1420, 350)], mul(hexc('#2f7f6f'), e), mul(hexc('#24685a'), e), 7, 10)
    # máquinas
    for mx, n in zip(MX, NUMS):
        body = mul(hexc('#eef2f2'), e)
        p.shape([(mx - 135, 640), (mx + 135, 640), (mx + 135, 1085), (mx - 135, 1085)], body, mul(body, .86), 7, 12)
        p.poly([(mx - 131, 644), (mx + 131, 644), (mx + 131, 712), (mx - 131, 712)], mul(hexc('#c9d2d4'), e))
        p.stroke([(mx - 135, 714), (mx + 135, 714)], 5)
        p.dot(mx + 40, 678, 18, mul(hexc('#8a9496'), e), 4)
        p.dot(mx + 100, 678, 12, mul(hexc('#6a7a7a'), e), 4)
        p.dot(mx, DY, 112, mul(hexc('#c9cfd2'), e), 6)
        p.dot(mx, DY, 90, mul(hexc('#3f6278'), e), 5)
        p.arc(mx - 20, DY - 25, 50, 50, 200, 260, 10, mul(hexc('#8fb3c8'), e))
        p.stroke([(mx - 120, 1060), (mx + 120, 1060)], 4, mul(body, .8))
    im = p.img.resize((W_, H_), Image.LANCZOS)
    c.alpha_composite(im)
    d = ImageDraw.Draw(c)
    ft = font(F_STAMP, 104); t = 'LAVANDERIA'; tw = d.textlength(t, font=ft)
    d.text((1770 - tw / 2, 198), t, font=ft, fill=mul(hexc('#f4e6b8'), e) + (255,))
    fn = font(F_B, 34)
    for mx, n in zip(MX, NUMS):
        if n == '7':
            d.text((mx - 128, 700), '7', font=font(F_MAO_L, 96), fill=mul(hexc('#c8302a'), e) + (255,), stroke_width=3, stroke_fill=(36, 30, 32, 255))
        else:
            d.text((mx - 118, 656), n, font=fn, fill=(50, 56, 60, 255))
    if mural == 'cheio':
        for x, y, cor, li in MURAL_MEIAS:
            put_meia(c, x, y, 120, cor, rot=-8 if x % 2 else 6, pino=True, listra=li)
    if noite:
        g = Image.new('RGBA', c.size, (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((900, 300, 1800, 1150), fill=(255, 226, 160, 40))
        c.alpha_composite(g.filter(ImageFilter.GaussianBlur(80)))
    return c


def porta7(c, f, gira=0.0, verde=0.0, aberta=0.0, cores=('#e0a43c', '#4f8fc0', '#d9634f'), mx=M7):
    """roupa girando na porta da máquina (gira 0..1 = velocidade), luz verde (0..1) e porta abrindo (0..1)."""
    r = 86
    if gira > 0 and aberta < .5:
        g = Image.new('RGBA', (2 * r, 2 * r), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
        a0 = f * .35 * gira
        for k, col in enumerate(cores):
            a = a0 + k * 2.1
            x, y = r + 40 * math.cos(a), r + 40 * math.sin(a)
            d.ellipse((x - 34, y - 24, x + 34, y + 24), fill=hexc(col) + (230,))
        d.ellipse((0, r * .9, 2 * r, 2 * r), fill=(150, 190, 215, 120))
        m = Image.new('L', g.size, 0); ImageDraw.Draw(m).ellipse((4, 4, 2 * r - 4, 2 * r - 4), fill=255)
        g.putalpha(ImageChops.multiply(g.getchannel('A'), m))
        c.alpha_composite(g, (mx - r, DY - r))
    if verde > 0:
        gl = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(gl)
        d.ellipse((mx - 260, 440, mx + 460, 1000), fill=(90, 255, 140, int(70 * verde)))
        c.alpha_composite(gl.filter(ImageFilter.GaussianBlur(60)))
        d = ImageDraw.Draw(c)
        d.ellipse((mx + 86, 664, mx + 114, 692), fill=(120, 255, 150, int(255 * verde)), outline=(36, 30, 32, 255), width=4)
    if aberta > 0:
        d = ImageDraw.Draw(c)
        d.ellipse((mx - 90, DY - 90, mx + 90, DY + 90), fill=(30, 36, 40, 255))
        w = 112 * (1 - .75 * aberta)
        x0 = mx - 112 - w * 0 - 112 * aberta * .9
        d.ellipse((x0 - w, DY - 112, x0 + w, DY + 112), fill=(201, 207, 210, 255), outline=(36, 30, 32, 255), width=6)
        d.ellipse((x0 - w * .78, DY - 88, x0 + w * .78, DY + 88), fill=(63, 98, 120, 255), outline=(36, 30, 32, 255), width=5)


@lru_cache(maxsize=4)
def cesto_img():
    p = Pen(360, 260)
    p.shape([(20, 40), (340, 40), (310, 250), (50, 250)], hexc('#5aa6d8'), hexc('#3f86b8'), 6, 12)
    for x in range(70, 320, 40): p.stroke([(x, 70), (x - 4 if x < 180 else x + 4, 230)], 6, hexc('#3f86b8'))
    p.shape([(10, 30), (350, 30), (350, 58), (10, 58)], hexc('#7fc0e6'), None, 5, 0)
    return p.img.resize((360, 260), Image.LANCZOS)


@lru_cache(maxsize=4)
def berco_img(luz='tarde'):
    p = Pen(700, 560)
    wd = hexc('#e8d2b0')
    p.shape([(40, 140), (80, 140), (80, 540), (40, 540)], wd, mul(wd, .85), 6, 8)
    p.shape([(620, 140), (660, 140), (660, 540), (620, 540)], wd, mul(wd, .85), 6, 8)
    p.shape([(60, 330), (640, 330), (640, 420), (60, 420)], hexc('#a8d0e6'), hexc('#86b0c8'), 6, 10)
    p.shape([(70, 290), (620, 300), (630, 350), (70, 350)], hexc('#f4e1a1'), None, 5, 0)
    for x in range(120, 620, 55): p.line([(x, 160), (x, 330)], wd, 14, 4)
    p.shape([(40, 140), (660, 140), (660, 168), (40, 168)], wd, None, 5, 0)
    return p.img.resize((700, 560), Image.LANCZOS)


@lru_cache(maxsize=2)
def caixinha_img():
    p = Pen(520, 360)
    p.shape([(40, 140), (480, 140), (460, 340), (60, 340)], hexc('#a8d0e6'), hexc('#86b0c8'), 7, 12)
    p.shape([(20, 40), (500, 40), (480, 140), (40, 140)], hexc('#c5e1ef'), None, 6, 0)   # tampa aberta atrás
    p.poly([(52, 140), (468, 140), (458, 170), (62, 170)], hexc('#f6efd9'))
    p.stroke([(40, 140), (480, 140)], 7)
    return p.img.resize((520, 360), Image.LANCZOS)


@lru_cache(maxsize=4)
def comoda_img(luz='noite'):
    e = .65 if luz == 'noite' else 1
    p = Pen(620, 520)
    wd = mul(hexc('#9a6a40'), e)
    p.shape([(20, 60), (600, 60), (600, 500), (20, 500)], wd, mul(wd, .82), 7, 12)
    p.shape([(0, 40), (620, 40), (620, 80), (0, 80)], mul(wd, .85), None, 6, 0)
    for y in (260, 380):
        p.shape([(50, y), (570, y), (570, y + 100), (50, y + 100)], mul(wd, 1.08), None, 5, 0)
        p.dot(310, y + 50, 12, mul(hexc('#e0c070'), e), 4)
    return p.img.resize((620, 520), Image.LANCZOS)


def gaveta(c, x, y, abre, luz='noite'):
    """cômoda com a gaveta de cima saindo (abre 0..1); a meia cinza aparece dentro. x = centro, y = base (chão)."""
    im = comoda_img(luz); c.alpha_composite(im, (int(x - 310), int(y - 500)))
    e = .65 if luz == 'noite' else 1
    dy = 70 * abre
    top = y - 500 + 110
    if abre > .05:
        p = Pen(620, 300); wd = mul(hexc('#9a6a40'), e)
        p.shape([(60, 20), (560, 20), (560, 130), (60, 130)], mul(hexc('#5a3a22'), e), None, 5, 0)
        dr = p.img.resize((620, 300), Image.LANCZOS)
        c.alpha_composite(dr, (int(x - 310), int(top - 40)))
        put_meia(c, x + 10, top + 10, 150, '#9aa0a4', rot=-80, nome='LÉO')
    p2 = Pen(620, 200); wd = mul(hexc('#9a6a40'), e)
    p2.shape([(30, 20), (590, 20), (590, 120), (30, 120)], mul(wd, 1.08), mul(wd, .9), 6, 8)
    p2.dot(310, 70, 12, mul(hexc('#e0c070'), e), 4)
    c.alpha_composite(p2.img.resize((620, 200), Image.LANCZOS), (int(x - 310), int(top + 20 + dy)))


C0 = (1104, 621)


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close à direita + gancho à esquerda
        c = lavanderia_bg('dia').copy(); porta7(c, f, gira=1)
        put_meia(c, 760, 560, 200, '#9aa0a4', rot=-10)
        c = close_h(c, f, expr='choque', look=-.5, x=1560, s=.92, shake=.2, **EU)
        cam = (1104, 621, z(1.0, f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    c = lavanderia_bg('dia').copy(); porta7(c, f, gira=1)
    leo(c, lerp(300, 820, smooth(ramp(g, 0, 80))), f, walk=1 if g < 80 else 0, expr='neutro', look=.75)
    t = smooth(ramp(g, 0, 150))
    cam = (lerp(900, 1250, t), lerp(660, 720, t), z(lerp(1.05, 1.4, t), f), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = lavanderia_bg('dia').copy()
    co = wt(1, 'coloco') - 3; dz = wt(1, 'dez'); on = wt(1, 'onze') - 3
    porta7(c, f, gira=1 if f < on else .3)
    c.alpha_composite(cesto_img(), (1460, 880))
    cores = ['#d9634f', '#4f8fc0', '#5aa36f', '#e0a43c', '#f4f1ea']
    n = int(clamp((f - co) / max(1, dz + 10 - co)) * 10) if f >= co else 0
    for k in range(n):
        put_meia(c, 1560 + (k % 4) * 45 - 40, 900 - (k // 4) * 26, 95, cores[k % 5], rot=80 + 20 * (k % 3))
    if f >= on:   # a meia número onze pula da porta
        t = ramp(f, on, on + 14)
        x = lerp(M7, 1720, t); y = lerp(DY, 800, t) - 220 * math.sin(math.pi * t)
        put_meia(c, x, y, 130 * back(ramp(f, on, on + 6)), ROXA, rot=int(-360 * t * (t < 1)), listra='#f4f1ea')
    leo(c, 1960, f, expr='choque' if f >= on else 'neutro', look=-.75)
    cam = (1580, 800, z(1.5, f) + .06 * kick(f, on + 3, .6), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = lavanderia_bg('dia').copy(); porta7(c, f, gira=.5)
    mu = wt(2, 'mural') - 3
    neide(c, 290, f, expr='sorriso', look=.75)
    c.alpha_composite(balcao_img('dia'), (-60, 760))
    hx, hy = mao_dir(820, 1180, 680)
    if f < mu + 8:
        leo(c, 820, f, expr='preocupado', look=-.75, flip=True)
        put_meia(c, 820 - (hx - 820) - 10, hy - 50, 110, ROXA, rot=-90, listra='#f4f1ea')
    else:
        leo(c, 820, f, expr='neutro', look=.5)
    if f >= mu:
        put_meia(c, 1180, lerp(330, 300, back(ramp(f, mu, mu + 10))), 120, ROXA, rot=6, pino=f >= mu + 8, listra='#f4f1ea')
    t = smooth(ramp(f, mu - 6, mu + 18))
    cam = (lerp(560, 950, t), lerp(660, 520, t), z(lerp(1.35, 1.4, t), f), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = lavanderia_bg('tarde').copy()
    se = wt(3, 'senhora') - 3; me = wt(3, 'menino') - 3
    put_meia(c, 1180, 300, 120, ROXA, rot=6, pino=True, listra='#f4f1ea')
    if f < me:
        x = 900
        put_menino(c, x, 1180, 780, f, seed=8, penteado='coque', cabelo='#cfcfcf', pele='#f0c8a0', roupa='#d9634f', calca='#4a4036',
                   velho=True, expr='sorriso', look=.5)
        hx, hy = mao_dir(x, 1180, 780)
        put_meia(c, hx + 40, lerp(hy - 60, hy - 140, back(ramp(f, se + 6, se + 16))), 130, '#4f8fc0', rot=-20)
        cam = (900, 620, z(1.4, f), 0)
    else:
        x = 940
        put_menino(c, x, 1180, 600, f, seed=9, penteado='curto', cabelo='#26241f', pele='#8a5a3a', roupa='#5aa36f', calca='#2d2f32',
                   expr='sorriso', look=.5)
        hx, hy = mao_dir(x, 1180, 600)
        put_meia(c, hx + 40, lerp(hy - 40, hy - 160, back(ramp(f, me + 4, me + 14))), 140, '#f4f1ea', rot=-15, listra='#3f8f5a')
        cam = (980, 660, z(lerp(1.4, 1.5, ramp(f, me, me + 60)), f), 0)
    CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = lavanderia_bg('dia').copy(); porta7(c, f, gira=.6, cores=('#9aa0a4', '#7a5ab0', '#c0453a'))
    ig = wt(4, 'igual') - 3; se = wt(4, 'sete') - 3
    t1 = smooth(ramp(f, ig - 6, ig + 14)); t2 = smooth(ramp(f, se - 4, se + 12))
    zz = lerp(lerp(2.2, 1.25, t1), 2.6, t2)
    cx = lerp(lerp(M7, 1340, t1), M7 - 80, t2); cy = lerp(lerp(DY, 860, t1), 760, t2)
    cam = (cx, cy, z(zz, f), 0); CAM[4] = cam
    return c, cam, 'sombrio'


def s5(f):
    c = lavanderia_bg('tarde', 'vazio').copy()
    am = wt(5, 'amarela') - 3
    put_meia(c, 940, 360, 170, '#f4d35e', rot=-6, pino=True, pato=True)
    t = smooth(ramp(f, 0, am + 20))
    cam = (lerp(1000, 940, t), lerp(600, 380, t), z(lerp(1.3, 2.4, t), f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    sa = wt(6, 'sabado') - 3
    if f < sa:
        c = lavanderia_bg('tarde', 'vazio').copy()
        put_meia(c, 940, 360, 170, '#f4d35e', rot=-6 + 3 * math.sin(f * .05), pino=True, pato=True)
        cam = (940, 400, z(2.0, f, -.0015), 0); CAM[6] = cam
        return c, cam, 'tarde'
    c = lavanderia_bg('dia', 'vazio').copy(); porta7(c, f, gira=1)
    put_meia(c, 940, 360, 170, '#f4d35e', rot=-6, pino=True, pato=True)
    g = f - sa
    mae(c, lerp(1700, 1180, smooth(ramp(g, 0, 80))), f, walk=1 if g < 80 else 0, flip=True, expr='sorriso', look=-.75)
    leo(c, lerp(1950, 1480, smooth(ramp(g, 4, 84))), f, walk=1 if g < 84 else 0, flip=True, expr='sorriso', look=-.75)
    c.alpha_composite(cesto_img(), (int(lerp(2050, 1580, smooth(ramp(g, 4, 84)))), 920))
    cam = (lerp(1400, 1250, smooth(ramp(g, 0, 90))), 680, z(1.2, f), 0); CAM[6] = cam
    return c, cam, 'vivo'


def s7(f):
    c = lavanderia_bg('dia', 'vazio').copy(); porta7(c, f, gira=1)
    put_meia(c, 940, 360, 170, '#f4d35e', rot=-6, pino=True, pato=True)
    pa = wt(7, 'palida') - 3
    if f >= pa:   # CLOSE 1 (a mãe)
        c = close_h(c, f, expr='choque', look=-.5, s=.92, shake=.25, **dict(MAE, pele='#d8ad86'))
        cam = (1104, 621 + kick(f, pa, .8) * 10, z(lerp(1.2, 1.03, easeOut(ramp(f, pa, pa + 10))), f), 0); CAM[7] = cam
        return c, cam, 'vivo'
    mae(c, 1180, f, flip=True, expr='choque' if f >= wt(7, 'parou') - 3 else 'neutro', look=-.75)
    leo(c, 1480, f, flip=True, expr='neutro', look=-.75)
    c.alpha_composite(cesto_img(), (1580, 920))
    cam = (1100, 600, z(1.3, f), 0); CAM[7] = cam
    return c, cam, 'vivo'


def s8(f):
    c = quarto_h('tarde').copy()
    ca = wt(8, 'casa') - 3; an = wt(8, 'anos') - 3
    c.alpha_composite(berco_img(), (1350, 560))
    if f < ca:
        put_meia(c, 1700, 840, 90, '#f4d35e', rot=-10, pato=True)
    elif f < ca + 12:
        put_dust(c, 1700, 840, 90, f - ca)
    mae(c, 900, f, flip=False, expr='sorriso' if f < ca else 'preocupado', look=.75 if f < an else -.75 * math.copysign(1, math.sin(f * .08)))
    cam = (lerp(1300, 1200, smooth(ramp(f, 0, 160))), 680, z(1.2, f), 0); CAM[8] = cam
    return c, cam, 'tarde'


def s9(f):
    c = quarto_h('tarde').copy().filter(ImageFilter.GaussianBlur(7)).convert('RGBA')
    cx_ = wt(9, 'caixinha') - 3; ig = wt(9, 'iguais') - 3; po = wt(9, 'pontinho') - 3
    s_ = back(ramp(f, cx_, cx_ + 10))
    if s_ > .05:
        im = caixinha_img().resize((int(520 * s_ * 1.4), int(360 * s_ * 1.4)), Image.LANCZOS)
        c.alpha_composite(im, (int(820 - im.width / 2), int(820 - im.height / 2)))
    if f >= cx_ + 4: put_meia(c, 820, lerp(700, 560, back(ramp(f, cx_ + 4, cx_ + 14))), 400, '#f4d35e', pato=True)
    if f >= ig:
        put_meia(c, lerp(1900, 1340, back(ramp(f, ig, ig + 12))), 560, 400, '#f4d35e', pato=True)
    t = smooth(ramp(f, po - 4, po + 16))
    bx, by = bico(1080, 560, 400)
    cam = (lerp(1080, bx, t), lerp(620, by, t), z(lerp(1.15, 2.3, t), f), 0); CAM[9] = cam
    return c, cam, 'tarde'


def s10(f):
    c = lavanderia_bg('dia', 'vazio').copy(); porta7(c, f, gira=1)
    neide(c, 290, f, expr='sorriso', look=.75)
    c.alpha_composite(balcao_img('dia'), (-60, 760))
    mae(c, 760, f, flip=True, expr='sorriso', look=-.75)
    leo(c, 1040, f, flip=True, expr='sorriso', look=-.75)
    hx, hy = mao_dir(1040, 1180, 680)
    put_meia(c, 1040 - (hx - 1040), hy - 30, 100, '#f4d35e', rot=-30, pato=True)
    cam = (lerp(700, 480, smooth(ramp(f, 0, 110))), 640, z(lerp(1.3, 1.6, smooth(ramp(f, 0, 110))), f), 0); CAM[10] = cam
    return c, cam, 'vivo'


def s11(f):
    c = lavanderia_bg('tarde', 'vazio').copy(); porta7(c, f, gira=.4)
    es = wt(11, 'escurece') - 3
    if f >= es - 10:   # a janela escurece
        sh = Image.new('RGBA', (470, 590), (30, 40, 70, int(170 * ramp(f, es - 10, es + 10))))
        c.alpha_composite(sh, (70, 170))
    neide(c, 290, f, expr='neutro', look=.75)
    c.alpha_composite(balcao_img('tarde'), (-60, 760))
    t = smooth(ramp(f, 20, es))
    cam = (lerp(500, 1250, t), lerp(560, 760, t), z(lerp(1.4, 1.6, t), f), 0); CAM[11] = cam
    return c, cam, 'tarde'


def s12(f):
    ec = wt(12, 'escureceu') - 3; so = wt(12, 'sozinha') - 3
    if f < ec:
        c = lavanderia_bg('tarde', 'vazio').copy(); porta7(c, f, gira=0)
        leo(c, 1650, f, expr='neutro', look=-.5, flip=True)
        cam = (1300, 680, z(1.25, f), 0); CAM[12] = cam
        return c, cam, 'tarde'
    c = lavanderia_bg('noite', 'vazio').copy()
    leo(c, 1620, f, expr='preocupado', look=-.75, flip=True)
    hx, hy = mao_dir(1620, 1180, 680)
    if f < so:
        put_meia(c, 1620 - (hx - 1620) - 20, hy - 40, 100, '#c0453a', rot=-80, listra='#f4f1ea')
    else:
        t = ramp(f, so, so + 12)
        put_meia(c, lerp(1460, M7, t), lerp(hy - 40, DY, t), 100 * (1 - .4 * t), '#c0453a', rot=-80, listra='#f4f1ea')
    cam = (lerp(1500, 1450, smooth(ramp(f, ec, ec + 120))), 760, z(lerp(1.4, 1.55, smooth(ramp(f, ec, ec + 120))), f), 0); CAM[12] = cam
    return c, cam, 'sombrio_noite'


def s13(f):
    c = lavanderia_bg('noite', 'vazio').copy()
    gi = wt(13, 'girou') - 3; ve = wt(13, 'verde') - 3
    porta7(c, f, gira=ramp(f, gi, gi + 10), verde=ramp(f, ve, ve + 6), cores=('#c0453a', '#f4f1ea', '#9aa0a4'))
    leo(c, 1720, f, expr='choque' if f >= ve else 'preocupado', look=-.75, flip=True)
    cam = (lerp(1450, 1420, ramp(f, 0, 200)), 780, z(lerp(1.5, 1.8, smooth(ramp(f, 0, 200))), f) + .05 * kick(f, ve, .6), 0); CAM[13] = cam
    return c, cam, 'sombrio_noite'


def s14(f):
    c = lavanderia_bg('noite', 'vazio').copy()
    po = wt(14, 'porta') - 3; mi = wt(14, 'minha') - 3; ci = wt(14, 'cinza') - 3
    porta7(c, f, gira=1 if f < po else 0, verde=1, aberta=ramp(f, po, po + 8), cores=('#c0453a', '#f4f1ea', '#9aa0a4'))
    if f >= mi:
        put_meia(c, lerp(M7, 1180, ramp(f, mi, mi + 10)), lerp(DY, 560, back(ramp(f, mi, mi + 10))), 150, '#c0453a', rot=-10, listra='#f4f1ea')
    if f >= ci:
        put_meia(c, lerp(M7, 1520, ramp(f, ci, ci + 10)), lerp(DY, 500, back(ramp(f, ci, ci + 10))), 300, '#9aa0a4', rot=8)
    cam = (1350, 700, z(lerp(1.6, 1.75, ramp(f, 0, 200)), f) + .05 * kick(f, ci, .6), 0); CAM[14] = cam
    return c, cam, 'sombrio'


def s15(f):
    no = wt(15, 'nome') - 3
    c = lavanderia_bg('noite', 'vazio').copy().filter(ImageFilter.GaussianBlur(8)).convert('RGBA')
    porta7(c, f, verde=1, aberta=1)
    put_meia(c, 1104, 640, 900, '#9aa0a4', nome='LÉO')
    nx, ny = nome_pos(1104, 640, 900)
    if f >= no + 6:   # CLOSE 2 (descoberta)
        c = close_h(c, f, expr='choque', look=0, s=.92, shake=.35, **EU)
        cam = (1104, 621, z(lerp(1.2, 1.03, easeOut(ramp(f, no + 6, no + 16))), f), 0); CAM[15] = cam
        return c, cam, 'frio'
    t = smooth(ramp(f, 0, no))
    cam = (lerp(1104, nx, t), lerp(640, ny + 60, t), z(lerp(1.0, 1.6, t), f), 0); CAM[15] = cam
    return c, cam, 'frio'


def s16(f):
    c = lavanderia_bg('noite', 'vazio').copy(); porta7(c, f, verde=.6, aberta=1)
    neide(c, 1000, f, feet=1180, expr='preocupado', look=.25)
    hx, hy = mao_dir(1000, 1180, 790)
    ol = wt(16, 'olhou') - 3
    put_meia(c, hx + 30, lerp(hy - 40, hy - 260, smooth(ramp(f, ol - 8, ol + 8))), 220, '#9aa0a4', rot=-10, nome='LÉO')
    leo(c, 1560, f, flip=True, expr='preocupado', look=-.75)
    cam = (lerp(1300, 1150, smooth(ramp(f, 0, 150))), 640, z(lerp(1.3, 1.5, smooth(ramp(f, 0, 150))), f), 0); CAM[16] = cam
    return c, cam, 'sombrio_noite'


def s17(f):
    c = lavanderia_bg('noite', 'vazio').copy(); porta7(c, f, verde=1, aberta=1)
    c = close_h(c, f, expr='desconfiado', look=0, s=.92, escurece=.3, **NE)
    an = wt(17, 'antes') - 3
    cam = (1104, 621 + kick(f, an, .8) * 8, z(lerp(1.25, 1.03, easeOut(ramp(f, 0, 12))), f, .0012), 0); CAM[17] = cam
    return c, cam, 'sombrio'


def s18(f):
    ga = wt(18, 'gaveta') - 3; cf = wt(18, 'confiro') - 3
    c = quarto_h('noite').copy()
    gaveta(c, 760, 1080, ramp(f, ga - 4, ga + 10))
    if f >= cf:   # CLOSE final
        c = close_h(c, f, expr='medo', look=0, s=.92, escurece=.35, **EU)
        cam = (1104, 621, z(lerp(1.2, 1.03, easeOut(ramp(f, cf, cf + 10))), f - cf, .0012), 0); CAM[18] = cam
        return c, cam, 'frio'
    leo(c, 1250, f, flip=True, expr='preocupado', look=-.75)
    t = smooth(ramp(f, 0, cf))
    cam = (lerp(1050, 820, t), lerp(700, 620, t), z(lerp(1.25, 1.7, t), f), 0); CAM[18] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18]


# ---------------------------------------------------------------- HUD (saída 1920x1080)
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'HISTÓRIA COMPLETA', 420, 170, 1, 56, big=True)
            gancho_h(im, ['A MÁQUINA SETE', 'DEVOLVE UMA', 'MEIA A MAIS'], 90, 290, 1, 118)
        else:
            stamp(im, 'NO MEU BAIRRO', 420, 110, back(ramp(f, CAPA + 2, CAPA + 10)), 64)
            v = wt(0, 'sete') - 3
            card(im, 'Máquina 7', 'sempre uma meia a mais', 1500, 160, ramp(f, v, v + 10), alvo=to_out(0, M7, DY))
    elif si == 1:
        co = wt(1, 'coloco') - 3; dz = wt(1, 'dez'); on = wt(1, 'onze') - 3
        n = int(clamp((f - co) / max(1, dz + 10 - co)) * 10) if f >= co else 0
        painel(im, 'MEIAS', str(11 if f >= on else n), 330, 200, ramp(f, co - 6, co + 4), glitch=1 if on <= f < on + 10 and f % 4 < 2 else 0)
        mi = wt(1, 'minha') - 3
        stamp(im, 'NÃO É MINHA', 1500, 110, back(ramp(f, mi, mi + 8)), 64)
    elif si == 2:
        ne = wt(2, 'neide') - 3; r = wt(2, 'regra') - 3; mu = wt(2, 'mural') - 3
        if f < r: stamp(im, 'DONA NEIDE', 420, 110, back(ramp(f, ne - 4, ne + 4)), 60)
        else: stamp(im, 'A REGRA', 420, 130, back(ramp(f, r, r + 8)), 100, big=True)
        card(im, 'Meia extra', 'vai pro mural até o dono aparecer', 1500, 820, ramp(f, mu + 6, mu + 16))
    elif si == 3:
        se = wt(3, 'senhora') - 3; me = wt(3, 'menino') - 3
        if f < me: card(im, 'Perdida', 'numa viagem', 1480, 160, ramp(f, wt(3, 'viagem') - 3, wt(3, 'viagem') + 7))
        else: card(im, 'Do uniforme', 'de futebol', 1480, 160, ramp(f, wt(3, 'futebol') - 3, wt(3, 'futebol') + 7))
        stamp(im, 'O DONO SEMPRE APARECE', 520, 100, back(ramp(f, 2, 10)), 56)
    elif si == 4:
        ni = wt(4, 'ninguem') - 3; ig = wt(4, 'igual') - 3; pi = wt(4, 'pintado') - 3
        interrog(im, 1650, 160, f, ramp(f, ni, ni + 8) * (1 - ramp(f, pi - 6, pi)))
        card(im, 'Igual às outras', 'sem cano diferente, sem porta secreta', 330, 140, ramp(f, ig, ig + 10) * (1 - ramp(f, pi - 6, pi)))
        if f >= pi: stamp(im, 'PINTADO À MÃO', 1500, 120, back(ramp(f, pi, pi + 8)), 64)
    elif si == 5:
        bu = wt(5, 'buscar') - 3; am = wt(5, 'amarela') - 3
        stamp(im, 'NINGUÉM BUSCOU', 420, 110, back(ramp(f, bu, bu + 8)), 64)
        card(im, 'Meinha amarela', 'de bebê, com um patinho bordado', 1500, 180, ramp(f, am + 6, am + 16))
    elif si == 6:
        tr = wt(6, 'tres') - 3; sa = wt(6, 'sabado') - 3
        if f < sa: painel(im, 'NO MURAL HÁ', '3 MESES', 1560, 210, ramp(f, tr, tr + 10), w=560)
        else: stamp(im, 'SÁBADO', 420, 110, back(ramp(f, sa, sa + 8)), 70)
    elif si == 7:
        pa = wt(7, 'parou') - 3; pl = wt(7, 'palida') - 3; su = wt(7, 'sua') - 3
        if f < pl: burst(im, '!', 1100, 200, back(ramp(f, pa, pa + 6)), 80)
        if f >= su - 6: stamp(im, 'ESSA MEIA É SUA', 420, 140, back(ramp(f, su - 6, su + 2)), 70, rot=3)
    elif si == 8:
        ca = wt(8, 'casa') - 3; an = wt(8, 'anos') - 3
        stamp(im, 'QUANDO EU ERA BEBÊ', 1450, 110, back(ramp(f, 2, 10)), 60)
        if f >= ca: burst(im, 'SUMIU!', 1500, 330, back(ramp(f, ca, ca + 8)), 54)
        painel(im, 'PROCURANDO HÁ', 'ANOS', 330, 210, ramp(f, an, an + 10), w=480)
    elif si == 9:
        ig = wt(9, 'iguais') - 3; po = wt(9, 'pontinho') - 3
        if f < po: stamp(im, 'O OUTRO PÉ', 420, 110, back(ramp(f, wt(9, 'caixinha') - 3, wt(9, 'caixinha') + 5)), 64)
        if ig <= f < po: burst(im, 'IGUAIS!', 1550, 200, back(ramp(f, ig, ig + 8)), 56)
        if f >= po + 14: card(im, 'Pontinho torto', 'no bico do pato, nas duas', 330, 150, ramp(f, po + 14, po + 24))
    elif si == 10:
        er = wt(10, 'erra') - 3
        stamp(im, 'NUNCA ERRA', 1450, 140, back(ramp(f, er, er + 8)), 90, big=True)
    elif si == 11:
        nu = wt(11, 'nunca') - 3; es = wt(11, 'escurece') - 3
        stamp(im, 'A OUTRA REGRA', 420, 130, back(ramp(f, nu, nu + 8)), 80, big=True)
        card(im, 'Máquina 7', 'proibida depois que escurece', 1480, 160, ramp(f, es, es + 10), alvo=to_out(11, M7, DY))
    elif si == 12:
        se = wt(12, 'sexta') - 3; ec = wt(12, 'escureceu') - 3
        stamp(im, 'SEXTA-FEIRA', 420, 110, back(ramp(f, se, se + 8)), 64)
        painel(im, 'HORA', '17:58' if f < ec else '18:31', 1560, 200, ramp(f, wt(12, 'fechar') - 4, wt(12, 'fechar') + 6),
               glitch=1 if ec <= f < ec + 8 and f % 4 < 2 else 0)
    elif si == 13:
        ba = wt(13, 'barulho') - 3; ve = wt(13, 'verde') - 3
        if f < ve: stamp(im, 'SEM BARULHO', 420, 120, back(ramp(f, ba, ba + 8)), 70)
        else: burst(im, 'VERDE?!', 420, 200, back(ramp(f, ve, ve + 8)), 60, cor=(90, 170, 110))
    elif si == 14:
        du = wt(14, 'duas') - 3; ci = wt(14, 'cinza') - 3
        painel(im, 'MEIAS', '2', 330, 200, ramp(f, du, du + 8), w=300)
        card(im, 'Meia cinza', 'enorme, de velhinho', 1500, 900, ramp(f, ci + 8, ci + 18))
    elif si == 15:
        to = wt(15, 'torta') - 3; no = wt(15, 'nome') - 3
        if f < no + 6: card(im, 'Linha torta', 'igual à da minha mãe', 1500, 150, ramp(f, to, to + 10))
        else: stamp(im, 'O MEU NOME', 420, 150, back(ramp(f, no + 8, no + 16)), 80, rot=3)
    elif si == 16:
        pe = wt(16, 'perdeu') - 3
        card(im, 'Não devolve só', 'o que a gente já perdeu', 330, 150, ramp(f, pe - 10, pe))
    elif si == 17:
        an = wt(17, 'antes') - 3; pe = wt(17, 'perder') - 3
        stamp(im, 'ELA DEVOLVE ANTES', 420, 150, back(ramp(f, an, an + 8)), 70)
        burst(im, '?!', 1580, 220, back(ramp(f, pe, pe + 8)), 70)
    elif si == 18:
        ga = wt(18, 'gaveta') - 3; cf = wt(18, 'confiro') - 3
        if f < cf:
            stamp(im, 'HOJE', 1500, 110, back(ramp(f, 2, 10)), 70)
            card(im, 'Gaveta', 'a meia de velhinho, guardada', 1480, 300, ramp(f, ga + 6, ga + 16))
        else: stamp(im, 'AINDA ESTÁ LÁ?', 420, 150, back(ramp(f, cf + 6, cf + 14)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
