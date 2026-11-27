"""Formato FÁBULA: "A casa que encolhia" (28/11/2026, 11h). Fábula ORIGINAL (pedido do Luis em 27/11/2026: outra fábula, diferente
das premissas do @aprendendocomvitinho1). Tema: a avó e as visitas que a gente adia. Moral: "Quem ama não cobra visita. Só deixa a luz acesa."
CTA: "Manda pra sua vó." LIPE e família com o visual fixo de fabula.py (LIPE, MAE, PAI). Vó Cida = VO (cabelo branco de coque, óculos, lilás).
Cenas/cores: s0 CAPA close Lipe + rua (vivo) | s1 casa da festa cresce (vivo) | s2 casa sozinha encolhe (tarde) | s3 casinha amarela da vó (vivo) |
s4 Lipe passa correndo (vivo) | s5 vó acena na janela (vivo) | s6 jogo/prova/celular (vivo) | s7 Lipe para e se assusta (tarde, música triste) |
s8 casa do tamanho de casinha de cachorro (tarde) | s9 de joelhos na porta -> salinha de teto baixo (tarde) | s10 CLOSE Lipe | s11 CLOSE vó |
s12 abajur na janela às cinco (tarde) | s13 janela acesa + CLOSE Lipe com lágrima (tarde) | s14 Lipe sentado no chão (tarde, música inspiradora) |
s15 risadas, o teto sobe (vivo) | s16 bolo de fubá, vó de pé (vivo) | s17 domingo, a família chega (vivo) | s18 a casa mais alta da rua (vivo) |
s19 Lipe bate na porta + CLOSE final (tarde) | s20 MORAL (tarde)."""
from kit import *
import kit
from sombrio import *
from fabula import *
from fabula import _piso, _escuro

CHAVES = ['casa', 'casas', 'crescem', 'encolhem', 'visita', 'sozinhas', 'diminuindo', 'vo', 'depois', 'susto', 'cachorro', 'joelhos',
          'sozinha', 'chamou', 'luz', 'acesa', 'abajur', 'cinco', 'riu', 'risada', 'bolo', 'domingo', 'alta', 'porta', 'atrapalhar']
instala_legenda_fab(CHAVES)
MUSICA = True
MUSICA_NIVEL = .14
STING = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+2%'; PITCH = '-2Hz'

LINES = [
    "Nesta cidade, as casas crescem quando recebem visita, e encolhem quando ficam sozinhas.",
    "Casa com festa de aniversário fica enorme. Casa com criança brincando ganha até um andar a mais.",
    "Mas casa onde ninguém aparece vai diminuindo. Um pouquinho por dia. Sem fazer barulho.",
    "No fim da rua do Lipe, morava a vó Cida, numa casinha amarela de janela azul.",
    "Todo dia, indo pra escola, o Lipe passava correndo na frente dela e gritava: depois eu venho, vó!",
    "E a vó acenava da janela, sorrindo, como se depois fosse logo ali.",
    "Mas depois virou semana. E semana virou mês. Teve jogo, teve prova, teve celular.",
    "Até que, numa tarde, o Lipe parou na frente da casa amarela... e levou um susto.",
    "A casa estava do tamanho de uma casinha de cachorro. A chaminé soltava uma fumaça fina, fininha.",
    "A porta só dava pra passar de joelhos. E lá dentro, encolhida, a vó Cida tricotava sozinha.",
    "Vó, por que você não me chamou?",
    "Eu não queria atrapalhar, meu amor. Você tem tanta coisa pra fazer.",
    "Foi aí que o Lipe viu, na janela, um abajur aceso. Todo dia, às cinco da tarde. A hora em que ele passava correndo.",
    "A vó nunca pediu visita. Ela só deixava a luz acesa. Pra caso ele quisesse entrar.",
    "O Lipe entrou de joelhos, sentou no chão da salinha, e pediu: vó, me conta uma história?",
    "Ela contou. E ele riu. E a cada risada, a parede estalava, o teto subia, a janela crescia.",
    "Quando o bolo de fubá saiu do forno, a vó já conseguia ficar de pé.",
    "No domingo, o Lipe voltou. Com a mãe, com o pai, e até com o cachorro.",
    "E a casinha amarela virou a casa mais alta da rua. Dava pra ver a janela azul lá de longe.",
    "Desde então, às cinco da tarde, o Lipe não passa mais correndo. Ele bate na porta.",
    "Quem ama não cobra visita. Só deixa a luz acesa.",
]
FALA_TIKTOK = "Manda pra sua vó."
CTA_TEXTO = "MANDA PRA SUA VÓ"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 13
FLASH = []
CAPA = 36
CHECK = [(0, 'crescem', 6), (0, 'encolhem', 8), (1, 'andar', 6), (2, 'diminuindo', 8), (3, 'amarela', 6), (4, 'depois', 6), (5, 'acenava', 6),
         (6, 'prova', 4), (6, 'celular', 6), (7, 'susto', 6), (8, 'cachorro', 6), (9, 'joelhos', 6), (9, 'tricotava', 6), (10, 'chamou', 2),
         (11, 'fazer', 2), (12, 'abajur', 6), (12, 'correndo', 6), (13, 'acesa', 6), (13, 'entrar', 6), (14, 'historia', 4), (15, 'subia', 6),
         (16, 'pe', 4), (17, 'cachorro', 6), (18, 'longe', 4), (19, 'porta', 6), (20, 'acesa', 6)]
VOC = dict(VO)


def TRILHA(SC, N, SR):
    return trilha(SC, N, SR, [(0, 'misteriosa'), (7, 'triste'), (14, 'inspiradora')])


def SFX(s):
    s.ting(s.W(0, 'crescem'), .2); s.thunk(s.W(0, 'encolhem') - 2, 140, .4)
    s.ting(s.W(1, 'festa'), .2); s.thunk(s.W(1, 'andar') - 2, 200, .4)
    s.trill(s.W(2, 'diminuindo'), .6, .06)
    s.patter(s.W(4, 'passava'), s.W(4, 'gritava') + 30, 7, .08)
    s.ting(s.W(5, 'acenava'), .18)
    for w in ('jogo', 'prova', 'celular'): s.whoosh(s.W(6, w) - 4, .35, .25)
    s.thunk(s.W(7, 'susto') - 2, 90, .6)
    s.thunk(s.W(8, 'cachorro') - 2, 160, .4)
    s.ting(s.W(12, 'abajur'), .22)
    for w in ('riu', 'estalava', 'subia', 'crescia'): s.thunk(s.W(15, w) - 2, 260, .3)
    s.ting(s.W(16, 'forno'), .2)
    s.patter(s.W(17, 'domingo'), s.W(17, 'cachorro') + 20, 5, .06)
    s.ting(s.W(18, 'alta'), .2)
    for k in range(3): s.thunk(s.W(19, 'bate') + k * 8, 300, .5)
    s.ting(s.W(20, 'acesa'), .25)


# ---------------------------------------------------------------- desenhos novos
AMA, TELHA, AZ = '#f6d56a', '#c0453a', '#4d79b3'


@lru_cache(maxsize=16)
def casa_base(cor=AMA, andares=1, acesa=False, vazada=False, baloes=False):
    """casinha de 800 de largura; base em y = altura da imagem. vazada=True deixa o vidro da janela transparente."""
    H = 760 + 300 * (andares - 1); p = Pen(820, H + 40)
    top = H - 520 - 300 * (andares - 1)
    p.shape([(620, top - 160), (700, top - 160), (700, top + 40), (620, top + 40)], hexc('#b86a4a'), hexc('#9a5038'), 7, 0)   # chaminé
    p.shape([(60, top + 40), (760, top + 40), (760, H), (60, H)], hexc(cor), mul(hexc(cor), .86), 8, 18)
    p.shape([(20, top + 70), (410, top - 210), (800, top + 70)], hexc(TELHA), mul(hexc(TELHA), .8), 8, 12)
    for k in range(andares - 1):
        y = top + 100 + k * 300
        for x in (150, 520):
            p.shape([(x, y), (x + 150, y), (x + 150, y + 150), (x, y + 150)], hexc('#fbf7ee'), None, 6, 0)
            p.poly([(x + 14, y + 14), (x + 136, y + 14), (x + 136, y + 136), (x + 14, y + 136)], hexc('#bfe3f5'))
    yb = H - 330
    p.shape([(450, yb - 20), (710, yb - 20), (710, yb + 200), (450, yb + 200)], hexc(AZ), mul(hexc(AZ), .8), 8, 0)   # janela azul
    if not vazada:
        p.poly([(474, yb + 4), (686, yb + 4), (686, yb + 176), (474, yb + 176)], hexc('#ffe39a') if acesa else hexc('#bfe3f5'))
    p.shape([(150, H - 300), (330, H - 300), (330, H), (150, H)], hexc('#8a5a32'), hexc('#6a4428'), 7, 0)   # porta
    p.dot(300, H - 150, 12, hexc('#f4d48a'), 4)
    p.shape([(470, yb + 200), (690, yb + 200), (670, yb + 250), (490, yb + 250)], hexc('#c96b4a'), None, 6, 0)   # floreira
    for x in (510, 570, 630): p.dot(x, yb + 190, 20, hexc('#f2a6c8'), 4)
    im = p.img.resize((820, H + 40), Image.LANCZOS)
    if vazada:   # recorta o vidro
        a = im.split()[3]; d = ImageDraw.Draw(a); d.rectangle((474, yb + 4, 686, yb + 176), fill=0); im.putalpha(a)
    if acesa:
        g = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((380, yb - 90, 780, yb + 290), fill=(255, 220, 120, 90))
        g = g.filter(ImageFilter.GaussianBlur(40)); g.alpha_composite(im); im = g
    if baloes:
        d = ImageDraw.Draw(im)
        for i, (x, y, c) in enumerate(((120, top - 40, (224, 88, 58)), (210, top - 120, (77, 121, 179)), (300, top - 60, (244, 182, 63)))):
            d.line((x, y + 50, 330, top + 80), fill=INK + (255,), width=4)
            d.ellipse((x - 40, y - 52, x + 40, y + 52), fill=c + (255,), outline=INK + (255,), width=6)
    return im


def put_casa(c, x, base, s, f=0, cor=AMA, andares=1, acesa=False, vazada=False, baloes=False, fumaca=1.0):
    """casa centrada em x com a base (chão) em y=base; s = escala (1 = 820 px de largura)."""
    s = max(.05, round(s * 40) / 40)
    im = casa_base(cor, andares, acesa, vazada, baloes)
    im = im.resize((max(4, int(im.width * s)), max(4, int(im.height * s))), Image.BILINEAR)
    x0, y0 = int(x - im.width / 2), int(base - im.height + 40 * s)
    c.alpha_composite(im, (x0, y0))
    if fumaca > 0:   # fumaça da chaminé
        H = 760 + 300 * (andares - 1); top = H - 520 - 300 * (andares - 1)
        cx, cy = x0 + 660 * s, y0 + (top - 170) * s
        d = ImageDraw.Draw(c)
        for k in range(4):
            a = (f * .02 + k / 4) % 1
            r = (18 + 40 * a) * s * fumaca
            px, py = cx + 40 * s * math.sin(a * 5 + k), cy - a * 320 * s
            d.ellipse((px - r, py - r, px + r, py + r), fill=(240, 240, 236, int(200 * (1 - a))))
    return x0, y0, s


def janela_casa(x, base, s, andares=1):
    """retângulo do vidro da janela azul (x0, y0, x1, y1) para a casa de put_casa."""
    H = 760 + 300 * (andares - 1)
    im_h = H + 40; x0 = x - 410 * s; y0 = base - im_h * s + 40 * s
    yb = H - 330
    return x0 + 474 * s, y0 + (yb + 4) * s, x0 + 686 * s, y0 + (yb + 176) * s


@lru_cache(maxsize=4)
def salinha_fab(luz='tarde'):
    """salinha da vó: papel de parede florido, janela à esquerda (x 300..760, y 700..1150) com abajur no peitoril,
    retrato na parede, poltrona verde (assento y≈1350, x 1150..1650), tapete."""
    c = Image.new('RGBA', (SW, SH), (0, 0, 0, 255))
    p = _base_vo()
    c.alpha_composite(p)
    sky = ceu_fab('tarde' if luz == 'tarde' else 'dia').crop((300, 300, 760, 750)); c.alpha_composite(sky, (300, 700))
    q = Pen(SW, SH)
    q.stroke([(530, 700), (530, 1150)], 14, hexc('#fbf7ee')); q.stroke([(300, 925), (760, 925)], 14, hexc('#fbf7ee'))
    q.stroke([(300, 700), (760, 700), (760, 1150), (300, 1150), (300, 700)], 7)
    q.shape([(270, 1150), (790, 1150), (790, 1190), (270, 1190)], hexc('#fbf7ee'), None, 6, 0)   # peitoril
    c.alpha_composite(q.img.resize((SW, SH), Image.LANCZOS))
    return _escuro(c, luz)


@lru_cache(maxsize=1)
def _base_vo():
    p = Pen(SW, SH)
    p.poly([(0, 0), (SW, 0), (SW, FY), (0, FY)], hexc('#f7e3c8'))
    rnd = random.Random(2)
    for y in range(80, FY - 60, 150):
        for x in range(60 + (y // 150 % 2) * 75, SW, 150):
            for k in range(5): p.dot(x + 12 * math.cos(k * 1.256), y + 12 * math.sin(k * 1.256), 9, hexc('#f2b8b0'))
            p.dot(x, y, 6, hexc('#f4b63f'))
    p.shape([(0, FY - 60), (SW, FY - 60), (SW, FY), (0, FY)], hexc('#d9b48a'), None, 5, 0)
    p.shape([(270, 680), (790, 680), (790, 1170), (270, 1170)], hexc('#fbf7ee'), hexc('#ddd6c6'), 7, 8)   # moldura (o vidro é colado depois)
    p.shape([(1260, 560), (1520, 560), (1520, 860), (1260, 860)], hexc('#8a5a32'), None, 7, 0)   # retrato
    p.poly([(1285, 585), (1495, 585), (1495, 835), (1285, 835)], hexc('#f4e1a1'))
    p.dot(1390, 680, 50, hexc('#e8bd96'), 5); p.shape([(1320, 835), (1460, 835), (1440, 760), (1340, 760)], hexc('#9b6bb5'), None, 5, 0)
    _piso(p, '#b98a58')
    p.shape(ell_pts(1104, 1920, 760, 170, 60), hexc('#e06a55'), hexc('#b8432a'), 7, 14)   # tapete
    p.shape([(1120, 1050), (1680, 1050), (1700, 1360), (1100, 1360)], hexc('#5aa36f'), hexc('#3f8a52'), 8, 18)   # encosto da poltrona
    im = p.img.resize((SW, SH), Image.LANCZOS)
    return im


@lru_cache(maxsize=1)
def poltrona_frente():
    p = Pen(SW, SH)
    p.shape([(1090, 1340), (1710, 1340), (1710, 1580), (1090, 1580)], hexc('#6ab57e'), hexc('#4a9a60'), 8, 16)
    for x0 in (1030, 1650):
        p.shape([(x0, 1200), (x0 + 120, 1200), (x0 + 120, 1580), (x0, 1580)], hexc('#5aa36f'), hexc('#3f8a52'), 8, 12)
    for x in (1120, 1680): p.shape([(x - 18, 1580), (x + 18, 1580), (x + 12, 1630), (x - 12, 1630)], hexc('#6a4428'), None, 5, 0)
    return p.img.resize((SW, SH), Image.LANCZOS)


def teto(c, y, luz='tarde'):
    """teto descendo: faixa de madeira de 0 até y (quanto mais baixo, mais a casa encolheu)."""
    if y <= 0: return
    d = ImageDraw.Draw(c)
    col = (176, 128, 84) if luz != 'noite' else (110, 80, 60)
    d.rectangle((0, 0, SW, y), fill=col + (255,))
    for x in range(-40, SW, 260): d.rectangle((x, y - 70, x + 60, y), fill=(140, 98, 62, 255))
    d.rectangle((0, y - 24, SW, y), fill=(120, 84, 52, 255)); d.line((0, y, SW, y), fill=INK + (255,), width=10)


def rachaduras(c, y, s):
    if s <= 0: return
    d = ImageDraw.Draw(c)
    for x0 in (600, 1500, 2000):
        pts = [(x0, y), (x0 - 30, y + 60 * s), (x0 + 20, y + 120 * s), (x0 - 10, y + 190 * s)]
        d.line(pts, fill=INK + (255,), width=8)


def abajur(c, x, y, aceso=True, s=1.0):
    """abajur no peitoril (base em y)."""
    d = ImageDraw.Draw(c)
    if aceso:
        g = Image.new('RGBA', (int(700 * s), int(700 * s)), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((0, 0, 700 * s, 700 * s), fill=(255, 220, 120, 110))
        c.alpha_composite(g.filter(ImageFilter.GaussianBlur(50 * s)), (int(x - 350 * s), int(y - 520 * s)))
    d.rectangle((x - 50 * s, y - 40 * s, x + 50 * s, y), fill=(154, 106, 64, 255), outline=INK + (255,), width=6)
    d.line((x, y - 40 * s, x, y - 150 * s), fill=INK + (255,), width=int(10 * s))
    d.polygon([(x - 100 * s, y - 150 * s), (x + 100 * s, y - 150 * s), (x + 60 * s, y - 270 * s), (x - 60 * s, y - 270 * s)],
              fill=(255, 213, 106, 255) if aceso else (220, 200, 160, 255), outline=INK + (255,))
    d.line([(x - 100 * s, y - 150 * s), (x + 100 * s, y - 150 * s), (x + 60 * s, y - 270 * s), (x - 60 * s, y - 270 * s), (x - 100 * s, y - 150 * s)], fill=INK + (255,), width=6)


def trico(c, x, y, f):
    """novelo + agulhas nas mãos (x, y = meio das mãos)."""
    d = ImageDraw.Draw(c); a = math.sin(f * .4) * 12
    d.line((x - 80, y - 60 + a, x + 20, y + 30), fill=(200, 200, 205, 255), width=10)
    d.line((x + 80, y - 60 - a, x - 20, y + 30), fill=(200, 200, 205, 255), width=10)
    d.rounded_rectangle((x - 70, y + 10, x + 70, y + 90), 20, fill=(77, 121, 179, 255), outline=INK + (255,), width=6)
    for k in range(4): d.line((x - 60 + k * 40, y + 20, x - 60 + k * 40, y + 80), fill=(60, 96, 150, 255), width=4)
    d.ellipse((x + 90, y + 120, x + 190, y + 220), fill=(224, 88, 58, 255), outline=INK + (255,), width=6)
    d.arc((x + 100, y + 130, x + 180, y + 210), 200, 340, fill=(180, 60, 40, 255), width=5)


def bolo(c, x, y, s=1.0, f=0):
    """bolo de fubá com furo no meio, em cima de um prato (y = base do prato)."""
    d = ImageDraw.Draw(c)
    d.ellipse((x - 200 * s, y - 40 * s, x + 200 * s, y + 20 * s), fill=(250, 250, 246, 255), outline=INK + (255,), width=6)
    d.rectangle((x - 150 * s, y - 150 * s, x + 150 * s, y - 20 * s), fill=(236, 186, 80, 255))
    d.ellipse((x - 150 * s, y - 60 * s, x + 150 * s, y + 10 * s), fill=(236, 186, 80, 255), outline=INK + (255,), width=6)
    d.line((x - 150 * s, y - 150 * s, x - 150 * s, y - 25 * s), fill=INK + (255,), width=6); d.line((x + 150 * s, y - 150 * s, x + 150 * s, y - 25 * s), fill=INK + (255,), width=6)
    d.ellipse((x - 150 * s, y - 190 * s, x + 150 * s, y - 110 * s), fill=(246, 206, 110, 255), outline=INK + (255,), width=6)
    d.ellipse((x - 36 * s, y - 166 * s, x + 36 * s, y - 134 * s), fill=(160, 110, 50, 255), outline=INK + (255,), width=5)
    for k in range(3):   # vapor
        a = (f * .03 + k / 3) % 1
        d.arc((x - 60 * s + k * 50 * s, y - 330 * s - a * 120 * s, x - 20 * s + k * 50 * s, y - 230 * s - a * 120 * s), 90, 270, fill=(255, 255, 255, int(220 * (1 - a))), width=6)


def moita(c, x, y, w=420):
    p = Pen(w + 40, 260)
    for dx, r in ((60, 70), (150, 95), (250, 90), (w - 60, 70)): p.dot(dx + 20, 170, r + 6, INK)
    for dx, r in ((60, 70), (150, 95), (250, 90), (w - 60, 70)): p.dot(dx + 20, 170, r, hexc('#5aa36f'))
    im = p.img.resize((w + 40, 260), Image.LANCZOS); a = im.split()[3]; ImageDraw.Draw(a).rectangle((0, 236, w + 40, 260), fill=0); im.putalpha(a)
    c.alpha_composite(im, (int(x - im.width / 2), int(y - 236)))


def vo_sentada(c, f, h=900, expr='sorriso', look=.5, x=1400):
    feet = 1350 + .28 * h
    pessoa(c, x, feet, h, f, VOC, seed=6, expr=expr, look=look)
    c.alpha_composite(poltrona_frente())
    return feet


def lipe_chao(c, x, f, expr='sorriso', look=.75, y=1820, flip=False):
    """Lipe sentado no chão (pernas escondidas pelo tapete da frente)."""
    pessoa(c, x, y + .3 * KID, KID, f, LIPE, seed=2, expr=expr, look=look, flip=flip)
    d = ImageDraw.Draw(c)
    d.ellipse((x - 300, y - 30, x + 300, y + 140), fill=(224, 106, 85, 255), outline=INK + (255,), width=8)


# ---------------------------------------------------------------- cenas
def bgc(fn, luz):
    return fn(luz).copy()


def rua_casas(f, luz='dia', scroll=0):
    return rua_fab(f, scroll=scroll, luz=luz)


def s0(f):
    if f < CAPA:
        c = rua_casas(0)
        put_casa(c, 1104, 1640, .5, f, fumaca=0)
        c = close_fab(c, f, 1104, 1150, expr='choque', look=0, s=V(.9, .95), dx=V(0, 480), **LIPE)
        if HOR: put_casa(c, 420, 1220, .45, f, fumaca=0)
        else: put_casa(c, 1000, 2180, .42, f, fumaca=0)
        return c, cam_close(f, 1.04, 1.0), 'vivo'
    g = f - CAPA
    c = rua_casas(f)
    cr = wt(0, 'crescem') - 3; en = wt(0, 'encolhem') - 3
    put_casa(c, 700, 1640, lerp(.55, .85, easeOut(ramp(f, cr, cr + 20))), f, cor='#f2a6c8')
    put_casa(c, 1500, 1640, lerp(.8, .45, easeOut(ramp(f, en, en + 30))), f, cor='#a8d0e6', fumaca=.4)
    pessoa(c, 520 + g * 2, 1760, ADU, f, GENTE[1], walk=1, seed=3, expr='sorriso', look=.75)
    pessoa(c, 380 + g * 2, 1780, 620, f, GENTE[3], walk=1, seed=5, expr='sorriso', look=.75)
    t = smooth(ramp(g, 0, 140))
    return c, cam(lerp(V(800, 1104), V(1300, 1104), smooth(ramp(f, en - 10, en + 10))), V(1250, 1180), lerp(1.15, 1.25, t), lerp(1.0, 1.08, t)), 'vivo'


def s1(f):
    c = rua_casas(f)
    an = wt(1, 'andar') - 3; cr = wt(1, 'crianca') - 3
    andares = 2 if f >= an else 1
    put_casa(c, 1104, 1640, lerp(.9, 1.05, ramp(f, 0, 40)) * (1 + .06 * back(ramp(f, an, an + 8)) - .06 * ramp(f, an + 8, an + 16)), f, cor='#f2a6c8', andares=andares, baloes=True)
    for i, (x, cr_) in enumerate(((760, GENTE[3]), (1450, GENTE[4]), (900, GENTE[0]))):
        pessoa(c, x + 30 * math.sin(f * .1 + i), 1790 + 10 * i, 600 if i < 2 else ADU, f, cr_, seed=3 + i, walk=.5, expr='sorriso', look=.5 - i * .5)
    t = smooth(ramp(f, 0, 160))
    return c, cam(1104, V(1200, 1150), lerp(1.05, 1.15, t), lerp(1.0, 1.06, t)), 'vivo'


def s2(f):
    c = rua_casas(f, 'tarde')
    di = wt(2, 'diminuindo') - 3
    put_casa(c, 1104, 1640, lerp(.95, .45, smooth(ramp(f, di - 20, di + 120))), f, cor='#a8d0e6', fumaca=.3)
    d = ImageDraw.Draw(c)
    for k in range(5):   # folhas caindo
        a = (f * .012 + k / 5) % 1
        x = 800 + k * 140 + 40 * math.sin(f * .05 + k); y = 700 + a * 900
        d.ellipse((x - 18, y - 10, x + 18, y + 10), fill=(214, 140, 60, 255), outline=INK + (255,), width=4)
    return c, cam(1104, V(1300, 1250), zf(1.2, f), zf(1.0, f, .0006)), 'tarde'


def s3(f):
    c = rua_casas(f)
    put_casa(c, 1400, 1640, 1.0, f)
    pessoa(c, 830, 1760, ADU, f, VOC, seed=6, expr='sorriso', look=.75)
    t = smooth(ramp(f, 0, 150))
    return c, cam(lerp(V(1050, 1104), V(1150, 1104), t), V(1200, 1150), lerp(1.12, 1.2, t), lerp(1.0, 1.08, t)), 'vivo'


def s4(f):
    sc = f * 14
    c = rua_casas(f, scroll=sc)
    xc = 1700 - sc * .5
    if xc > -400: put_casa(c, xc, 1640, 1.0, f)
    pessoa(c, 1104, 1780, KID, f, LIPE, walk=1, seed=2, expr='sorriso', look=-.5)
    return c, cam(1104, V(1350, 1250), zf(1.3, f), zf(1.08, f)), 'vivo'


def janela_vo(c, f, x, base, s, expr='sorriso', look=.5, acesa=False):
    """casa com a vó aparecendo na janela (desenha o interior, a vó e a casa vazada)."""
    x0, y0, x1, y1 = janela_casa(x, base, s)
    d = ImageDraw.Draw(c); d.rectangle((x0, y0, x1, y1), fill=(255, 226, 150, 255) if acesa else (247, 227, 200, 255))
    w = x1 - x0; hh = w * 2.4
    cut = c.crop((int(x0), int(y0), int(x1), int(y1)))
    put_menino(cut, w / 2, hh * .95, hh, f, seed=6, expr=expr, look=look, **VOC)
    c.alpha_composite(cut, (int(x0), int(y0)))
    put_casa(c, x, base, s, f, vazada=True, acesa=acesa)


def s5(f):
    c = rua_casas(f)
    janela_vo(c, f, 1104, 1640, 1.0, expr='sorriso', look=-.25)
    x0, y0, x1, y1 = janela_casa(1104, 1640, 1.0)
    ac = wt(5, 'acenava') - 3
    if f >= ac:   # mão acenando
        d = ImageDraw.Draw(c); a = math.sin(f * .5) * 20
        hx, hy = x0 + 50 + a, y0 + 60
        d.ellipse((hx - 30, hy - 30, hx + 30, hy + 30), fill=hexc(VOC['pele']) + (255,), outline=INK + (255,), width=6)
    t = smooth(ramp(f, 0, 60))
    return c, cam((x0 + x1) / 2, (y0 + y1) / 2 + 60, lerp(1.6, 2.6, t) * (1 + .0008 * f), lerp(1.3, 2.0, t) * (1 + .0008 * f)), 'vivo'


def s6(f):
    pr, ce = wt(6, 'prova') - 3, wt(6, 'celular') - 3
    jo = wt(6, 'jogo') - 3
    if f < jo:   # o tempo passando: calendário na parede do quarto
        c = bgc(quarto_fab, 'dia')
        pessoa(c, 900, 1760, KID, f, LIPE, seed=2, expr='neutro', look=.5)
        return c, cam(1104, V(1250, 1150), zf(1.2, f), zf(1.0, f)), 'vivo'
    if f < pr:
        c = bgc(quintal_fab, 'dia')
        x = 1000 + 200 * math.sin(f * .08)
        pessoa(c, x, 1800, KID, f, LIPE, seed=2, walk=1, expr='sorriso', look=.75)
        bola(c, x + 170, 1740 - 120 * abs(math.sin(f * .2)), 60, f * .3)
        return c, cam(1104, V(1350, 1250), zf(1.25, f - jo), zf(1.0, f - jo)), 'vivo'
    if f < ce:
        c = bgc(quarto_fab, 'dia')
        pessoa(c, 1104, 1760, KID, f, LIPE, seed=2, expr='preocupado', look=0)
        d = ImageDraw.Draw(c); hx, hy = mao_dir(1104, 1760, KID)
        d.polygon([(hx - 150, hy - 140), (hx + 30, hy - 160), (hx + 40, hy + 40), (hx - 140, hy + 60)], fill=(252, 248, 236, 255), outline=INK + (255,))
        for k in range(4): d.line((hx - 120, hy - 110 + k * 40, hx + 10, hy - 116 + k * 40), fill=(90, 90, 110, 255), width=5)
        return c, cam(1104, V(1300, 1200), zf(1.4, f - pr), zf(1.1, f - pr)), 'vivo'
    c = bgc(sala_fab, 'dia')
    pessoa(c, 1104, 1526, KID, f, LIPE, seed=2, expr='neutro', look=0)
    celular(c, 1104, 1526 - .47 * KID, 100, LIPE['pele'])
    c.alpha_composite(sofa_frente())
    return c, cam(1104, V(1300, 1200), zf(1.45, f - ce), zf(1.15, f - ce)), 'vivo'


def s7(f):
    su = wt(7, 'susto') - 3
    c = rua_casas(f, 'tarde', scroll=min(f, su) * 6)
    pessoa(c, 1104, 1780, KID, f, LIPE, walk=1 if f < su - 10 else 0, seed=2, expr='choque' if f >= su else 'neutro', look=.75)
    t = easeOut(ramp(f, su, su + 10))
    return c, cam(1104, lerp(V(1350, 1250), V(1250, 1200), t), lerp(1.25, 1.7, t) * (1 + .0006 * f), lerp(1.05, 1.4, t)), 'tarde'


def s8(f):
    c = rua_casas(f, 'tarde')
    ca = wt(8, 'cachorro') - 3
    put_casa(c, 1300, 1700, .34, f, fumaca=.25)
    pessoa(c, 1000, 1780, KID, f, LIPE, seed=2, expr='choque', look=.75)
    t = smooth(ramp(f, ca - 10, ca + 20))
    return c, cam(lerp(1104, 1180, t), lerp(V(1350, 1250), V(1450, 1420), t), lerp(1.25, 1.9, t), lerp(1.05, 1.6, t)), 'tarde'


def salinha(f, teto_y=760, luz='tarde', aceso=True):
    c = bgc(salinha_fab, luz)
    abajur(c, 530, 1150, aceso)
    relogio(c, 17, 0, 950, 520, 80)
    teto(c, teto_y, luz)
    return c


def s9(f):
    la = wt(9, 'la') - 3
    if f < la:
        c = rua_casas(f, 'tarde')
        put_casa(c, 1250, 1700, .34, f, fumaca=.25)
        pessoa(c, 1020, 1850, KID, f, LIPE, seed=2, expr='preocupado', look=.75)
        moita(c, 1000, 1760, 480)
        return c, cam(1150, V(1450, 1400), zf(1.8, f), zf(1.45, f)), 'tarde'
    g = f - la
    c = salinha(f, 760)
    vo_sentada(c, f, 820, expr='neutro', look=-.25)
    trico(c, 1400, 1350 + .28 * 820 - .3 * 820, f)
    return c, cam(1300, V(1200, 1150), lerp(1.5, 1.3, easeOut(ramp(g, 0, 14))) * (1 + .0008 * g), lerp(1.15, 1.05, easeOut(ramp(g, 0, 14)))), 'tarde'


def s10(f):
    c = salinha(f, 760)
    vo_sentada(c, f, 820, expr='neutro', look=-.5)
    lipe_chao(c, 760, f, expr='preocupado', look=.75)
    c = close_fab(c, f, 760, 1300, expr='preocupado', look=.5, s=V(.95, .95), dx=V(0, -250), **LIPE)
    return c, cam_close(f, 1.15, 1.0), 'tarde'


def s11(f):
    c = salinha(f, 760)
    vo_sentada(c, f, 820, expr='sorriso', look=-.5)
    c = close_fab(c, f, 1400, 1150, expr='sorriso', look=-.25, s=V(.95, .95), dx=V(0, 250), **VOC)
    return c, cam_close(f, 1.12, 1.0), 'tarde'


def s12(f):
    c = salinha(f, 760)
    vo_sentada(c, f, 820, expr='neutro', look=-.75)
    lipe_chao(c, 900, f, expr='curioso', look=-.75, flip=True)
    ab = wt(12, 'abajur') - 4; ci = wt(12, 'cinco') - 4; co = wt(12, 'correndo') - 4
    if f < ci: cx, cy, z = 530, 1000, 2.0
    elif f < co: cx, cy, z = 950, 600, 2.2
    else: cx, cy, z = 900, 1300, 1.4
    t = easeOut(ramp(f, ab, ab + 10))
    return c, cam(V(cx, max(cx, 960)), V(cy, max(cy, 900)), zf(lerp(1.3, z, t), f), zf(lerp(1.05, z * .8, t), f)), 'tarde'


def s13(f):
    en = wt(13, 'pra') - 3
    c = rua_casas(f, 'tarde')
    put_casa(c, 1250, 1700, .34, f, fumaca=.25, acesa=True)
    pessoa(c, 860, 1780, KID, f, LIPE, seed=2, expr='preocupado', look=.75)
    if f >= en:   # CLOSE virada
        c = close_fab(c, f, 1000, 1300, expr='preocupado', look=.5, s=V(.95, .95), lagrima=((f - en) / 45) % 1, **LIPE)
        return c, cam_close(f, 1.15, 1.0, en), 'tarde'
    return c, cam(1150, V(1450, 1350), zf(1.7, f), zf(1.4, f)), 'tarde'


def s14(f):
    c = salinha(f, 760)
    vo_sentada(c, f, 820, expr='sorriso', look=-.5)
    x = lerp(300, 820, smooth(ramp(f, 0, 50)))
    lipe_chao(c, x, f, expr='sorriso', look=.75)
    t = smooth(ramp(f, 0, 120))
    return c, cam(lerp(900, 1104, t), V(1250, 1180), lerp(1.3, 1.2, t) * (1 + .0006 * f), lerp(1.05, 1.0, t) * (1 + .0006 * f)), 'tarde'


def s15(f):
    ri = wt(15, 'riu') - 3; cr = wt(15, 'crescia') + 10
    k = ramp(f, ri, cr)
    c = salinha(f, int(lerp(760, 160, smooth(k))), luz='tarde')
    rachaduras(c, int(lerp(760, 160, smooth(k))), math.sin(math.pi * k))
    vo_sentada(c, f, lerp(820, 1000, smooth(k)), expr='sorriso', look=-.5)
    lipe_chao(c, 820, f, expr='sorriso', look=.75)
    kk = sum(kick(f, wt(15, w) - 2, .6) for w in ('riu', 'estalava', 'subia', 'crescia'))
    return c, cam(1104, V(1200, 1130) + kk * 10, lerp(1.25, 1.05, smooth(k)) * (1 + .0005 * f), lerp(1.05, 1.0, smooth(k)) * (1 + .0006 * f)), 'vivo'


def s16(f):
    pe = wt(16, 'pe') - 3
    c = salinha(f, 0, luz='dia')
    if f < pe:
        vo_sentada(c, f, 1000, expr='sorriso', look=-.5)
    else:
        c.alpha_composite(poltrona_frente())
        pessoa(c, 1250, 1780, ADU, f, VOC, seed=6, expr='sorriso', look=-.5)
    hx, hy = (1250 + .13 * ADU, 1780 - .26 * ADU) if f >= pe else (1260, 1500)
    bolo(c, hx - 130, hy + 20, .8, f)
    lipe_chao(c, 760, f, expr='sorriso', look=.75)
    t = smooth(ramp(f, pe - 10, pe + 20))
    return c, cam(1104, lerp(V(1250, 1180), V(1200, 1150), t), zf(1.2, f), zf(1.0, f, .0007)), 'vivo'


def s17(f):
    c = rua_casas(f)
    ca = wt(17, 'cachorro') - 3
    put_casa(c, 1550, 1640, lerp(.6, .95, smooth(ramp(f, 30, 170))), f)
    xs = lerp(-100, 600, smooth(ramp(f, 0, 150)))
    pessoa(c, xs, 1760, ADU, f, PAI, walk=1, seed=5, expr='sorriso', look=.75)
    pessoa(c, xs + 230, 1770, ADU, f, MAE, walk=1, seed=3, expr='sorriso', look=.75)
    pessoa(c, xs + 430, 1790, KID, f, LIPE, walk=1, seed=2, expr='sorriso', look=.75)
    if f >= ca - 6: put_cachorro(c, xs + lerp(-200, 600, ramp(f, ca - 6, ca + 20)), 1810, 260, f, andando=True)
    t = smooth(ramp(f, 0, 160))
    return c, cam(lerp(V(800, 1104), V(1200, 1104), t), V(1250, 1180), zf(1.1, f), zf(1.0, f, .0006)), 'vivo'


def s18(f):
    c = rua_casas(f)
    put_casa(c, 1104, 1640, lerp(1.0, 1.25, smooth(ramp(f, 0, 60))), f, andares=3, acesa=False)
    for i, (x, cr_, h) in enumerate(((640, PAI, ADU), (1600, MAE, ADU), (850, LIPE, KID))):
        pessoa(c, x, 1790, h, f, cr_, seed=5 + i, expr='sorriso', look=.5 if x < 1104 else -.5)
    t = smooth(ramp(f, 0, 150))
    return c, cam(1104, lerp(V(1500, 1300), V(1000, 1000), t), lerp(1.2, 1.05, t), lerp(1.0, 1.0, t) * (1 + .0006 * f)), 'vivo'


def s19(f):
    ba = wt(19, 'bate') - 3; po = wt(19, 'porta') - 3
    c = rua_casas(f, 'tarde')
    put_casa(c, 1250, 1640, 1.0, f, andares=3, acesa=True)
    x = lerp(400, 940, smooth(ramp(f, 0, ba)))
    pessoa(c, x, 1760, KID, f, LIPE, walk=1 if f < ba else 0, seed=2, expr='sorriso', look=.75)
    if f >= po + 6:   # CLOSE final
        c = close_fab(c, f, 1000, 1300, expr='sorriso', look=0, s=V(.95, .95), **LIPE)
        return c, cam_close(f, 1.15, 1.0, po + 6), 'tarde'
    return c, cam(lerp(V(800, 1104), V(1000, 1104), smooth(ramp(f, 0, ba))), V(1250, 1180), zf(1.2, f), zf(1.0, f, .0007)), 'tarde'


def s20(f):
    c = rua_casas(f, 'tarde')
    put_casa(c, 1104, 1640, 1.0, f, andares=3, acesa=True)
    return c, cam(1104, V(1150, 1150), zf(1.1, f, .0006), zf(1.0, f, .0006)), 'tarde'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]


def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0 and f < CAPA:
        if HOR: capa_txt(im, ['NESTA CIDADE, AS CASAS', '*ENCOLHEM* QUANDO', 'NINGUÉM *VISITA*'], size=104, y=200)
        else: capa_txt(im, ['NESTA CIDADE, AS CASAS', '*ENCOLHEM* QUANDO', 'NINGUÉM *VISITA*'], size=96)
    elif si == 4:
        de = wt(4, 'depois') - 3
        selo_txt(im, 'DEPOIS EU VENHO, VÓ!', V(540, 960), V(330, 140), ramp(f, de, de + 8), V(64, 64))
    elif si == 6:
        jo, pr, ce = wt(6, 'jogo') - 3, wt(6, 'prova') - 3, wt(6, 'celular') - 3
        se = wt(6, 'semana') - 3
        if f < jo: selo_txt(im, 'UM MÊS DEPOIS...' if f >= wt(6, 'mes') - 3 else 'UMA SEMANA DEPOIS...', V(540, 960), V(330, 140), ramp(f, se, se + 8), V(64, 64), cor=(77, 121, 179))
    elif si == 8:
        ca = wt(8, 'cachorro') - 3
        selo_txt(im, 'ENCOLHEU!', V(540, 960), V(330, 140), ramp(f, ca, ca + 8), V(80, 76))
    elif si == 12:
        ci = wt(12, 'cinco') - 3
        selo_txt(im, 'TODO DIA, 17:00', V(540, 960), V(330, 140), ramp(f, ci, ci + 8), V(72, 68), cor=(214, 150, 40))
    elif si == 15:
        ri = wt(15, 'estalava') - 3
        selo_txt(im, 'CREC! CREC!', V(540, 960), V(330, 140), ramp(f, ri, ri + 8), V(80, 76))
    elif si == 17:
        selo_txt(im, 'DOMINGO', V(540, 960), V(330, 140), ramp(f, 0, 8), V(76, 72), cor=(90, 160, 80))
    elif si == 20:
        ac = wt(20, 'so') - 3
        if HOR: moral_txt(im, ['QUEM AMA NÃO COBRA VISITA.'] + (['SÓ DEIXA A *LUZ ACESA*.'] if f >= ac else []), ramp(f, 0, 8))
        else: moral_txt(im, ['QUEM AMA', 'NÃO COBRA', 'VISITA.'] + (['SÓ DEIXA A', '*LUZ ACESA*.'] if f >= ac else []), ramp(f, 0, 8))
    return im.convert('RGB')
