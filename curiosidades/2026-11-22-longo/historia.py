"""VÍDEO LONGO (YouTube normal, horizontal 16:9, ~2 min) no formato MISTÉRIO: "O livro que respondeu" (22/11/2026). História inventada,
completa (sem partes). Renderize com MOTOR_H=1.
Narradora: Bia, menina ruiva de coque, pele clara, blusa roxa e calça azul. Dona Lurdes: bibliotecária de coque branco, óculos, blusa vermelha.
Premissa: na biblioteca da cidade há um livro de capa verde que nunca fica no mesmo lugar (já apareceu no aquário); regra: ninguém
leva o livro verde pra casa; sem nome, páginas em branco; Bia acha o livro na própria mochila; a 1ª página diz que choveu no recreio,
mas na cidade dela fez sol; depois, o gato da vizinha subiu na antena (ela não tem vizinha com gato); o livro conta a vida de outra
pessoa; Bia escreve "quem é você?"; às três da manhã vem a resposta: Clara, que achou que ninguém ia responder; as duas se escrevem
todo dia; Clara mora no Vale das Corujas, que não existe em nenhum mapa; fim: lá também há um livro que muda de lugar, de capa azul,
com o nome da Bia na capa.
Cenários/cores: s0 CAPA close (tarde) -> biblioteca de dia (vivo) | s1 biblioteca, aquário (vivo) | s2 balcão, a regra (tarde) |
s3 livro em branco, neblina (sombrio) | s4 biblioteca fim de tarde -> quarto (tarde) | s5 quarto + CLOSE (tarde) | s6 livro, chuva (frio) |
s7 rua de sol (vivo) | s8 livro de manhã (frio) | s9 casa com antena imaginada (tarde) | s10 quarto + CLOSE (sombrio) |
s11 livro, lápis (tarde) | s12 quarto à noite (sombrio_noite) | s13 três da manhã (sombrio_noite) | s14 resposta azul (frio) |
s15 quarto de dia, sorriso (vivo) | s16 Vale das Corujas imaginado (tarde) | s17 mapa (sombrio) | s18 biblioteca azul + CLOSE final (sombrio_noite)."""
from kit import *
import kit
from sombrio import *
from longo import *

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='coque', cabelo='#b8562a', pele='#f0c8a0', roupa='#7a5ab0', calca='#3b5a8a')
LU = dict(penteado='coque', cabelo='#e4e4e0', pele='#c8956b', roupa='#c0453a', calca='#4a4036', oculos=True, velho=True)
AZUL = (40, 70, 160)

LINES = [
    "Na biblioteca da minha cidade, tem um livro de capa verde que nunca fica no mesmo lugar.",
    "Toda manhã, ele aparece numa prateleira diferente. Uma vez, apareceu dentro do aquário.",
    "A bibliotecária, Dona Lurdes, tem uma regra: ninguém leva o livro verde pra casa.",
    "Ele não tem nome na capa. E quem abre, só encontra páginas em branco. Uma vez, um menino tentou levar escondido. No dia seguinte, o livro estava de volta na estante.",
    "Na sexta, eu fui devolver um livro de dinossauros. Quando cheguei em casa, abri a mochila.",
    "O livro verde estava lá dentro. E eu juro que não peguei.",
    "Na primeira página, tinha uma frase escrita à mão: hoje choveu na hora do recreio.",
    "Só que na minha cidade, não choveu. Fez sol o dia inteiro.",
    "Na manhã seguinte, tinha outra frase: o gato da vizinha subiu na antena de novo.",
    "Eu não tenho vizinha com gato. E ninguém na minha rua tem antena.",
    "Aquele livro não falava da minha vida. Falava da vida de outra pessoa.",
    "Então, eu peguei um lápis e escrevi embaixo: quem é você?",
    "Fiquei a noite inteira acordada, com o livro fechado no colo.",
    "Às três da manhã, as páginas viraram sozinhas.",
    "E apareceu uma resposta, com uma letra redonda: meu nome é Clara. Achei que ninguém ia responder. Eu li aquela frase dez vezes, com o coração disparado.",
    "Desde então, eu e a Clara escrevemos todo dia. Ela tem a minha idade, e também odeia matemática.",
    "Ela mora numa cidade chamada Vale das Corujas.",
    "Eu procurei em todos os mapas. Até no globo da escola. Essa cidade não existe.",
    "E ontem, ela escreveu: aqui também tem um livro que nunca fica no mesmo lugar. A capa é azul. E nela, tem o seu nome.",
]
FALA_TIKTOK = "Você responderia o livro? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 17
FLASH = []
CHECK = [(0, 'verde', 6), (1, 'aquario', 6), (2, 'regra', 4), (3, 'branco', 6), (4, 'mochila', 6), (5, 'juro', 6),
         (6, 'recreio', 6), (7, 'sol', 6), (8, 'antena', 6), (9, 'antena', 6), (10, 'outra', 6), (11, 'voce', 6),
         (12, 'colo', 6), (13, 'sozinhas', 6), (14, 'clara', 6), (15, 'matematica', 6), (16, 'corujas', 6),
         (17, 'existe', 6), (18, 'azul', 6), (18, 'nome', 10)]
CAM = {}
CAPA = 38


def SFX(s):
    s.thunk(2, 120, .8)
    s.patter(s.W(0, 'biblioteca') - 4, s.W(0, 'biblioteca') + 40, 4, .05)
    s.whoosh(s.W(1, 'prateleira') - 6, .4, .2); s.splash(s.W(1, 'aquario'), .4) if hasattr(s, 'splash') else s.ting(s.W(1, 'aquario'), .3)
    s.thunk(s.W(2, 'regra') - 2, 90, .7)
    s.whoosh(s.W(3, 'abre') - 6, .4, .2)
    s.thunk(s.W(4, 'mochila') - 2, 140, .5)
    s.thunk(s.W(5, 'juro') - 2, 70, .9)
    s.ting(s.W(6, 'recreio'), .25)
    s.ting(s.W(7, 'sol'), .2)
    s.trill(s.W(8, 'antena'), .5, .1)
    s.whoosh(s.W(10, 'outra') - 6, .6, .3)
    for i in range(4): s.thunk(s.W(11, 'escrevi') + i * 6, 340, .15)
    s.trill(s.W(12, 'noite'), .6, .1)
    s.whoosh(s.W(13, 'viraram') - 6, .8, .4); s.thunk(s.W(13, 'sozinhas') - 2, 70, .9)
    s.ting(s.W(14, 'clara'), .3)
    s.ting(s.W(16, 'corujas'), .25)
    s.thunk(s.W(17, 'existe') - 2, 70, 1.0)
    s.thunk(s.W(18, 'azul') - 2, 90, .7); s.thunk(s.W(18, 'nome') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (W_ / 2, H_ / 2, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def bia(c, x, f, feet=1180, h=760, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


def lurdes(c, x, f, feet=1150, h=760, **kw):
    put_menino(c, x, feet, h, f, seed=6, flip=True, **dict(LU, **kw))


def z(v, f, k=.0007):
    return v * (1 + k * f)


C0 = (1104, 621)

# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close à direita + gancho à esquerda
        c = quarto_h('tarde').copy(); put_livro(c, 960, 700, 220, brilho=True)
        c = close_h(c, f, expr='choque', look=-.5, x=1560, s=.92, shake=.2, **EU)
        cam = (1104, 621, z(1.0, f), 0); CAM[0] = cam
        return c, cam, 'tarde'
    g = f - CAPA
    c = biblioteca_bg('dia').copy()
    v = wt(0, 'verde') - 3
    put_livro(c, 1660, 905, 120, brilho=f >= v)
    bia(c, lerp(500, 800, smooth(ramp(g, 0, 90))), f, walk=1 if g < 90 else 0, expr='neutro', look=.75)
    t = smooth(ramp(g, 0, 140))
    cam = (lerp(900, 1300, t), lerp(700, 680, t), z(lerp(1.15, 1.35, t), f), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = biblioteca_bg('dia').copy()
    c.alpha_composite(aquario_img(), (850, 700))
    pr = wt(1, 'prateleira') - 3; aq = wt(1, 'aquario') - 3
    spots = [(300, 410), (1700, 575), (520, 740)]
    if f < aq:
        i = min(2, max(0, (f - pr) // 14)) if f >= pr else 0
        x, y = spots[i]; put_livro(c, x, y, 120, brilho=True)
    else:
        put_livro(c, 1110 + 10 * math.sin(f * .1), 960 + 6 * math.sin(f * .13), 140, rot=12, brilho=True)
    t = smooth(ramp(f, aq - 10, aq + 6))
    cam = (lerp(1104, 1110, t), lerp(621, 860, t), z(lerp(1.0, 1.9, t), f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = biblioteca_bg('tarde').copy()
    lurdes(c, 1900, f, feet=1130, h=760, expr='neutro', look=-.75)
    c.alpha_composite(balcao_img('tarde'), (1580, 790))
    bia(c, 1250, f, expr='preocupado', look=.75)
    r = wt(2, 'regra') - 3
    cam = (1500, 650, z(1.3, f) + .05 * kick(f, r, .6), 0); CAM[2] = cam
    return c, cam, 'tarde'


def s3(f):
    c = biblioteca_bg('neblina').copy().filter(ImageFilter.GaussianBlur(8)).convert('RGBA')
    ab = wt(3, 'abre') - 3
    if f < ab: put_livro(c, 1104, 640, 420 * back(ramp(f, 0, 10)), brilho=True)
    else: livro(c, 1104, 620, back(ramp(f, ab, ab + 8)) * 1.15)
    cam = (1104, 621, z(1.0, f, .001), 0); CAM[3] = cam
    return c, cam, 'sombrio'


def s4(f):
    q = wt(4, 'quando') - 3
    if f < q:
        c = biblioteca_bg('tarde').copy()
        lurdes(c, 1900, f, feet=1130, h=760, expr='sorriso', look=-.75)
        c.alpha_composite(balcao_img('tarde'), (1580, 790))
        put_livro(c, lerp(1500, 1700, ramp(f, 30, 60)), 800, 110, cor='#e0a43c')
        bia(c, 1300, f, expr='sorriso', look=.75)
        cam = (1450, 650, z(1.2, f), 0); CAM[4] = cam
        return c, cam, 'tarde'
    c = quarto_h('tarde').copy()
    c.alpha_composite(mochila_img(), (1250, 680))
    bia(c, 1000, f, expr='neutro', look=.75)
    cam = (1250, 700, z(lerp(1.4, 1.25, easeOut(ramp(f, q, q + 14))), f), 0); CAM[4] = cam
    return c, cam, 'tarde'


def s5(f):
    c = quarto_h('tarde').copy()
    c.alpha_composite(mochila_img(), (1250, 680))
    u = back(ramp(f, 4, 16))
    put_livro(c, 1460, lerp(860, 600, u), 220, brilho=True, rot=-8)
    ju = wt(5, 'juro') - 3
    if f >= ju:   # CLOSE 1
        c = close_h(c, f, expr='choque', look=.5, s=.92, shake=.3, **EU)
        cam = (1104, 621 + kick(f, ju, .8) * 10, z(lerp(1.2, 1.03, easeOut(ramp(f, ju, ju + 10))), f), 0); CAM[5] = cam
        return c, cam, 'tarde'
    bia(c, 1000, f, expr='choque', look=.75)
    cam = (1250, 650, z(1.25, f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = quarto_h('frio', True).copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
    h_ = wt(6, 'hoje') - 3
    livro(c, 1104, 600, 1.2, esq=['Hoje choveu', 'na hora do', 'recreio.'], t=ramp(f, h_ - 4, h_ + 50))
    cam = (lerp(880, 820, smooth(ramp(f, 0, 160))), 560, z(1.25, f, .001), 0); CAM[6] = cam
    return c, cam, 'frio'


def s7(f):
    c = rua_h('dia').copy()
    bia(c, lerp(400, 1500, ramp(f, 0, 170)), f, feet=1200, h=720, walk=1, expr='sorriso', look=.75)
    cam = (lerp(800, 1300, smooth(ramp(f, 0, 170))), 700, z(1.15, f), 0); CAM[7] = cam
    return c, cam, 'vivo'


def s8(f):
    c = quarto_h('frio').copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
    ou = wt(8, 'outra') - 3
    livro(c, 1104, 600, 1.2, esq=['Hoje choveu', 'na hora do', 'recreio.'], dir_=['O gato da', 'vizinha subiu', 'na antena', 'de novo.'] if f >= ou else [],
          t=1 if f < ou else 1)
    if f >= ou:   # só a página da direita se escreve
        c2 = quarto_h('frio').copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
        livro(c2, 1104, 600, 1.2, esq=['Hoje choveu', 'na hora do', 'recreio.'])
        tt = ramp(f, wt(8, 'gato') - 4, wt(8, 'novo') + 4)
        # escreve a direita aos poucos
        livro(c2, 1104, 600, 1.2, esq=['Hoje choveu', 'na hora do', 'recreio.'], dir_=['O gato da', 'vizinha subiu', 'na antena', 'de novo.'], t=1) if tt >= 1 else None
        if tt < 1:
            c2 = quarto_h('frio').copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
            livro(c2, 1104, 600, 1.2, esq=['Hoje choveu', 'na hora do', 'recreio.'], dir_=[], t=1)
            livro_dir(c2, tt)
        c = c2
    cam = (lerp(1250, 1350, smooth(ramp(f, 0, 160))), 560, z(1.25, f, .001), 0); CAM[8] = cam
    return c, cam, 'frio'


def livro_dir(c, tt):
    """escreve só a página da direita do livro (posição do s8) por cima, aos poucos."""
    linhas = ['O gato da', 'vizinha subiu', 'na antena', 'de novo.']
    s = 1.2; W, H = 1240, 800
    x0 = 1104 - W * s / 2 + (1200 / 2 + 60) * s; y0 = 600 - H * s / 2 + 62 * s
    d = ImageDraw.Draw(c); fnt = font(F_MAO_L, int(42 * s))
    tot = sum(len(l) for l in linhas); n = int(round(tot * clamp(tt)))
    for i, l in enumerate(linhas):
        vis = l[:max(0, n)]; n -= len(l)
        d.text((x0, y0 + i * 58 * s), vis, font=fnt, fill=(70, 70, 78, 255))


def s9(f):
    c = rua_h('tarde').copy()
    an = wt(9, 'antena') - 3
    im = casa_antena_img()
    if f >= wt(9, 'gato') - 3 - 0 or True:
        s_ = back(ramp(f, 2, 12))
        if s_ > .05:
            im2 = im.resize((int(700 * s_), int(700 * s_)), Image.LANCZOS)
            c.alpha_composite(im2, (int(1450 - im2.width / 2), int(1040 - im2.height)))
    if f >= an:
        d = ImageDraw.Draw(c); a = int(220 * ramp(f, an, an + 6))
        d.line((1150, 380, 1750, 1000), fill=(200, 60, 60, a), width=22); d.line((1750, 380, 1150, 1000), fill=(200, 60, 60, a), width=22)
    bia(c, 600, f, feet=1200, h=720, expr='preocupado', look=.75)
    cam = (1104, 650, z(1.05, f), 0); CAM[9] = cam
    return c, cam, 'tarde'


def s10(f):
    c = quarto_h('neblina').copy()
    ou = wt(10, 'outra') - 3
    if f >= ou:   # CLOSE 2 (descoberta)
        put_livro(c, 960, 700, 220, brilho=True)
        c = close_h(c, f, expr='desconfiado', look=.5, s=.92, **EU)
        cam = (1104, 621, z(lerp(1.2, 1.03, easeOut(ramp(f, ou, ou + 10))), f), 0); CAM[10] = cam
        return c, cam, 'sombrio'
    bia(c, 1000, f, expr='preocupado', look=.5)
    hx, hy = mao_dir(1000, 1180, 760)
    put_livro(c, hx + 30, hy - 40, 150, brilho=True)
    cam = (1050, 650, z(1.25, f), 0); CAM[10] = cam
    return c, cam, 'sombrio'


def s11(f):
    c = quarto_h('tarde').copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
    es = wt(11, 'escrevi') - 3
    livro(c, 1104, 600, 1.2, esq=['Hoje choveu', 'na hora do', 'recreio.'], dir_=['O gato da', 'vizinha subiu', 'na antena', 'de novo.'])
    # 'Quem é você?' a lápis, embaixo, na esquerda
    d = ImageDraw.Draw(c); fnt = font(F_MAO_L, 54)
    txt_ = 'Quem é você?'; n = int(len(txt_) * ramp(f, es, wt(11, 'voce') + 8))
    s = 1.2; x0 = 1104 - 1240 * s / 2 + 80 * s; y0 = 600 - 800 * s / 2 + (62 + 58 * 5) * s
    d.text((x0, y0), txt_[:n], font=fnt, fill=(50, 50, 60, 255))
    if n > 0:   # lápis
        tw = d.textlength(txt_[:n], font=fnt)
        d.line((x0 + tw + 10, y0 + 50, x0 + tw + 120, y0 - 80), fill=(36, 30, 32, 255), width=34)
        d.line((x0 + tw + 10, y0 + 50, x0 + tw + 120, y0 - 80), fill=(240, 192, 80, 255), width=24)
    cam = (lerp(900, 800, smooth(ramp(f, 0, 120))), 640, z(1.3, f, .001), 0); CAM[11] = cam
    return c, cam, 'tarde'


def s12(f):
    c = quarto_h('noite').copy()
    bia(c, 1500, f, feet=1060, h=700, expr='preocupado', look=-.5, flip=True)
    put_livro(c, 1480, 900, 160, rot=80)
    cam = (1400, 640, z(lerp(1.0, 1.3, smooth(ramp(f, 0, 160))), f), 0); CAM[12] = cam
    return c, cam, 'sombrio_noite'


def s13(f):
    c = quarto_h('noite').copy()
    vi = wt(13, 'viraram') - 3
    if f < vi:
        put_livro(c, 1104, 700, 360, rot=0)
    else:
        livro(c, 1104, 640, .9)
        d = ImageDraw.Draw(c)
        for k in range(4):   # páginas virando
            a = (f * .5 + k * .8) % math.pi
            x2 = 1104 + 520 * math.cos(a)
            d.polygon([(1104, 320), (x2, 330 - 40 * math.sin(a)), (x2, 960 - 40 * math.sin(a)), (1104, 950)], fill=(248, 241, 220, 255), outline=(36, 30, 32, 255))
        g = Image.new('RGBA', c.size, (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((600, 200, 1600, 1100), fill=(255, 230, 160, 80))
        c.alpha_composite(g.filter(ImageFilter.GaussianBlur(60)))
    cam = (1104, 640, z(1.15, f) + .06 * kick(f, vi, .8), 1.5 * math.sin(f * .2) * ramp(f, vi, vi + 6)); CAM[13] = cam
    return c, cam, 'sombrio_noite'


def s14(f):
    c = quarto_h('frio').copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
    me = wt(14, 'meu') - 3
    livro(c, 1104, 600, 1.2, esq=['Hoje choveu', 'na hora do', 'recreio.', '', '', 'Quem é você?'], dir_=[],
          dir2=['Meu nome é', 'Clara. Achei', 'que ninguém', 'ia responder.'], cor2=AZUL, t2=ramp(f, me - 4, wt(14, 'responder') + 6))
    cam = (lerp(1250, 1350, smooth(ramp(f, 0, 200))), 560, z(1.25, f, .001), 0); CAM[14] = cam
    return c, cam, 'frio'


def s15(f):
    c = quarto_h('dia').copy()
    bia(c, 1000, f, expr='sorriso', look=.75)
    hx, hy = mao_dir(1000, 1180, 760)
    put_livro(c, hx + 40, hy - 40, 160, brilho=True)
    cam = (1150, 650, z(lerp(1.05, 1.2, smooth(ramp(f, 0, 200))), f), 0); CAM[15] = cam
    return c, cam, 'vivo'


def s16(f):
    c = rua_h('tarde').copy()
    d = ImageDraw.Draw(c)
    for k, (x, y) in enumerate(((300, 300), (700, 220), (1500, 260), (1900, 330))):   # corujas no céu (silhuetas)
        yy = y + 10 * math.sin(f * .1 + k)
        d.ellipse((x - 40, yy - 30, x + 40, yy + 30), fill=(90, 70, 60, 255))
        d.polygon([(x - 40, yy), (x - 110, yy - 30 + 20 * math.sin(f * .3 + k)), (x - 30, yy + 10)], fill=(90, 70, 60, 255))
        d.polygon([(x + 40, yy), (x + 110, yy - 30 + 20 * math.sin(f * .3 + k)), (x + 30, yy + 10)], fill=(90, 70, 60, 255))
        d.ellipse((x - 22, yy - 14, x - 4, yy + 4), fill=(250, 220, 120, 255)); d.ellipse((x + 4, yy - 14, x + 22, yy + 4), fill=(250, 220, 120, 255))
    cam = (1104, lerp(700, 560, smooth(ramp(f, 0, 120))), z(1.05, f), 0); CAM[16] = cam
    return c, cam, 'tarde'


def s17(f):
    c = quarto_h('neblina').copy().filter(ImageFilter.GaussianBlur(8)).convert('RGBA')
    im = mapa_img(); c.alpha_composite(im, (int(1104 - 650), int(600 - 430)))
    cam = (1104, 600, z(lerp(1.0, 1.15, smooth(ramp(f, 0, 120))), f), lerp(0, -2, smooth(ramp(f, 0, 120)))); CAM[17] = cam
    return c, cam, 'sombrio'


def s18(f):
    az = wt(18, 'azul') - 3; no = wt(18, 'nome') - 3
    fim = no + 26
    if f < az:
        c = quarto_h('noite').copy().filter(ImageFilter.GaussianBlur(6)).convert('RGBA')
        livro(c, 1104, 600, 1.2, esq=['Aqui também', 'tem um livro', 'que nunca fica', 'no mesmo lugar.'], cor_txt=AZUL, t=ramp(f, wt(18, 'aqui') - 4, az))
        cam = (lerp(850, 900, smooth(ramp(f, 0, az))), 560, z(1.25, f, .001), 0); CAM[18] = cam
        return c, cam, 'sombrio_noite'
    c = biblioteca_bg('azul').copy()
    put_livro(c, 1104, 640, 330 * back(ramp(f, az, az + 10)), cor='#3a6ac0', brilho=True)
    if f >= no:
        d = ImageDraw.Draw(c); fnt = font(F_MAO_L, 44); t_ = 'BIA'
        tw = d.textlength(t_, font=fnt); d.text((1110 - tw / 2, 560), t_, font=fnt, fill=(250, 236, 160, int(255 * ramp(f, no, no + 6))))
    if f >= fim:   # CLOSE final
        c = close_h(c, f, expr='medo', look=0, s=.92, escurece=.35, **EU)
        cam = (1104, 621, z(lerp(1.2, 1.03, easeOut(ramp(f, fim, fim + 10))), f - fim, .0012), 0); CAM[18] = cam
        return c, cam, 'sombrio_noite'
    cam = (1104, 640, z(lerp(1.0, 1.5, smooth(ramp(f, az, fim))), f), 0); CAM[18] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18]


# ---------------------------------------------------------------- HUD (saída 1920x1080)
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'HISTÓRIA COMPLETA', 420, 170, 1, 56, big=True)
            gancho_h(im, ['O LIVRO QUE', 'ME RESPONDEU', 'DE VOLTA'], 90, 290, 1, 118)
        else:
            stamp(im, 'NA MINHA CIDADE', 420, 110, back(ramp(f, CAPA + 2, CAPA + 10)), 64)
            v = wt(0, 'verde') - 3
            card(im, 'Livro verde', 'nunca fica no mesmo lugar', 1500, 160, ramp(f, v, v + 10), alvo=to_out(0, 1660, 905))
    elif si == 1:
        aq = wt(1, 'aquario') - 3; pr = wt(1, 'prateleira') - 3
        if f < aq: stamp(im, 'TODA MANHÃ', 1500, 110, back(ramp(f, pr - 8, pr)), 64)
        else: burst(im, 'NO AQUÁRIO?!', 1500, 200, back(ramp(f, aq, aq + 8)), 56)
    elif si == 2:
        r = wt(2, 'regra') - 3; lu = wt(2, 'lurdes') - 3
        stamp(im, 'DONA LURDES', 1500, 110, back(ramp(f, lu - 4, lu + 4)), 60)
        stamp(im, 'A REGRA', 420, 140, back(ramp(f, r, r + 8)), 100, big=True)
        card(im, 'Proibido', 'levar o livro verde pra casa', 420, 340, ramp(f, r + 10, r + 20))
    elif si == 3:
        n = wt(3, 'nome') - 3; b = wt(3, 'branco') - 3
        card(im, 'Sem nome', 'nem na capa, nem na lombada', 330, 120, ramp(f, n, n + 10))
        interrog(im, 1650, 160, f, ramp(f, b, b + 8))
        vo = wt(3, 'volta') - 3
        burst(im, 'DE VOLTA!', 1600, 420, back(ramp(f, vo, vo + 8)), 56)
    elif si == 4:
        se = wt(4, 'sexta') - 3; q = wt(4, 'quando') - 3
        if f < q: stamp(im, 'SEXTA-FEIRA', 420, 110, back(ramp(f, se, se + 8)), 64)
        else: stamp(im, 'EM CASA', 420, 110, back(ramp(f, q, q + 8)), 64)
    elif si == 5:
        ju = wt(5, 'juro') - 3
        if f < ju: burst(im, '?!', 1500, 200, back(ramp(f, 4, 12)), 70)
        else: stamp(im, 'EU NÃO PEGUEI', 420, 150, back(ramp(f, ju + 2, ju + 10)), 70, rot=3)
    elif si == 6:
        pr = wt(6, 'primeira') - 3
        stamp(im, 'PÁGINA 1', 1600, 110, back(ramp(f, pr, pr + 8)), 64)
    elif si == 7:
        so = wt(7, 'sol') - 3
        painel(im, 'CHUVA HOJE', '0 mm', 1560, 200, ramp(f, so, so + 10), w=460)
    elif si == 8:
        ma = wt(8, 'manha') - 3
        stamp(im, 'PÁGINA 2', 960, 70, back(ramp(f, ma, ma + 8)), 64)
    elif si == 9:
        v = wt(9, 'vizinha') - 3
        card(im, 'Minha rua', 'sem gato, sem antena', 330, 140, ramp(f, v, v + 10))
    elif si == 10:
        ou = wt(10, 'outra') - 3
        if f >= ou: stamp(im, 'DE OUTRA PESSOA', 420, 150, back(ramp(f, ou + 2, ou + 10)), 70)
    elif si == 11:
        es = wt(11, 'lapis') - 3
        burst(im, 'RISC RISC', 260, 960, back(ramp(f, es, es + 8)), 48)
    elif si == 12:
        no = wt(12, 'noite') - 3
        painel(im, 'HORA', '23:47' if f < no + 40 else '01:12', 1560, 200, ramp(f, 2, 12))
    elif si == 13:
        tr = wt(13, 'tres') - 3; vi = wt(13, 'viraram') - 3
        painel(im, 'HORA', '03:00', 330, 200, ramp(f, tr - 6, tr + 4), glitch=1 if vi <= f < vi + 10 and f % 4 < 2 else 0)
        burst(im, 'FRRRR!', 1600, 200, back(ramp(f, vi, vi + 8)), 60)
    elif si == 14:
        cl = wt(14, 'clara') - 3
        card(im, 'Letra redonda', 'tinta azul', 330, 120, ramp(f, wt(14, 'letra') - 3, wt(14, 'letra') + 7))
        burst(im, 'CLARA', 1650, 150, back(ramp(f, cl, cl + 8)), 56, cor=(90, 130, 200))
    elif si == 15:
        id_ = wt(15, 'idade') - 3; ma = wt(15, 'matematica') - 3
        card(im, 'Clara', 'tem a minha idade', 330, 140, ramp(f, id_, id_ + 10))
        card(im, 'Também odeia', 'matemática', 330, 330, ramp(f, ma, ma + 10))
    elif si == 16:
        vc = wt(16, 'vale') - 3
        stamp(im, 'VALE DAS CORUJAS', 960, 560, back(ramp(f, vc, vc + 8)), 110, big=True)
    elif si == 17:
        ex = wt(17, 'existe') - 3
        burst(im, 'NÃO EXISTE', 1450, 300, back(ramp(f, ex, ex + 8)), 64)
        stamp(im, 'TODOS OS MAPAS', 420, 110, back(ramp(f, wt(17, 'mapas') - 8, wt(17, 'mapas'))), 60)
    elif si == 18:
        az = wt(18, 'azul') - 3; no = wt(18, 'nome') - 3; fim = no + 26
        if f < az: stamp(im, 'A LETRA DA CLARA', 1500, 110, back(ramp(f, 2, 10)), 60)
        elif f < fim: card(im, 'Capa azul', 'com o meu nome', 330, 140, ramp(f, no, no + 10))
        else: stamp(im, 'O MEU NOME?', 420, 150, back(ramp(f, fim + 4, fim + 12)), 80, rot=3)
    return grao(im.convert('RGB'), lf)
