"""Formato DESENHO: por que a bolinha de tênis é amarela (Curiosidades da IA, 19/11/2026, 19h).
Categoria: INVENÇÕES E OBJETOS.
Fatos: Wikipedia, "Tennis ball" ("Until 1972, tennis balls were white (or sometimes black)"; a Federação Internacional de
Tênis (ITF) introduziu bolas amarelas em 1972 porque eram mais fáceis de ver na televisão; Wimbledon continuou com bolas
brancas até 1986); NBC Sports, "Why tennis balls are yellow" (mesma história: amarelo aparece melhor na TV em cores).
Cenários: s0 quadra de tênis (Professor com a bolinha, que fica branca) | s1 quadra antiga ao entardecer dourado (bolinhas
brancas e pretas) | s2 sala com TV (Professor no sofá não acha a bolinha na tela) | s3 sala com TV (a bolinha fica amarela, 1972) |
s4 quadra ao entardecer dourado (torneio tradicional só em 1986) | s5 sala ao entardecer (Professor: quem escolheu foi a TV)."""
from kit import *
from functools import lru_cache

LINES = [
    "A bolinha de tênis nem sempre foi amarela.",
    "Por muito tempo, ela era branca, e às vezes até preta.",
    "Aí a televisão começou a mostrar os jogos, e o povo em casa não achava a bolinha na tela.",
    "Você vê, na TV o amarelo aparece muito melhor. Por isso, em mil novecentos e setenta e dois, o tênis adotou a bolinha amarela.",
    "E um dos torneios mais tradicionais resistiu, e só trocou em mil novecentos e oitenta e seis.",
    "Ou seja: quem escolheu a cor da bolinha... foi a televisão.",
]
CAPTXT = [
    "A bolinha de tênis nem sempre foi amarela.",
    "Por muito tempo, ela era branca,|e às vezes até preta.",
    "Aí a televisão começou a mostrar os jogos,|e o povo em casa não achava a bolinha na tela.",
    "Você vê, na TV o amarelo aparece muito melhor.|Por isso, em 1972, o tênis adotou a bolinha amarela.",
    "E um dos torneios mais tradicionais resistiu,|e só trocou em 1986.",
    "Ou seja: quem escolheu a cor da bolinha... foi a televisão.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
MUSICA = False
TWIST = 3
FLASH = [1]
CHECK = [(0, 'amarela', 4), (1, 'branca', 4), (1, 'preta', 4), (2, 'televisao', 4), (2, 'achava', 6),
         (3, 'amarelo', 4), (3, 'setenta', 6), (4, 'resistiu', 4), (4, 'oitenta', 6), (5, 'televisao', 8)]

YEL = (222, 236, 60); YELD = (176, 190, 30)
WHT = (250, 250, 245); WHTD = (205, 205, 200)
BLK = (50, 50, 56); BLKD = (25, 25, 30)
CORES = {'y': (YEL, YELD), 'w': (WHT, WHTD), 'k': (BLK, BLKD)}


def SFX(s):
    for i in range(3): s.thunk(s.W(0, 'tenis') - 6 + i * 9, 380, .5)
    s.ting(s.W(0, 'amarela'), .3)
    s.thunk(s.W(1, 'branca') - 2, 360, .5); s.thunk(s.W(1, 'preta') - 2, 300, .5)
    s.ting(s.W(2, 'televisao'), .25); s.thunk(s.W(2, 'achava') - 2, 200, .5)
    s.ting(s.W(3, 'amarelo'), .35); s.thunk(s.W(3, 'setenta') - 2, 260, .7)
    for i in range(4): s.thunk(s.W(3, 'bolinha') + i * 8, 380, .35)
    s.thunk(s.W(4, 'resistiu') - 2, 160, .6); s.thunk(s.W(4, 'oitenta') - 2, 260, .7)
    s.trill(s.W(5, 'televisao'), 1.0, .3)


@lru_cache(maxsize=16)
def bola_img(size, cor='y'):
    col, dk = CORES[cor]
    p = Pen(200, 200)
    p.shape(ell_pts(100, 100, 86, 86, 40), col, dk, 6, 14)
    seam = (255, 255, 255) if cor != 'w' else (190, 190, 185)
    p.arc(20, 100, 50, 60, -70, 70, 7, seam)
    p.arc(180, 100, 50, 60, 110, 250, 7, seam)
    s = max(4, int(size))
    return p.img.resize((s, s), Image.LANCZOS)


def bola(c, x, y, size, cor='y'):
    if size < 8: return
    paste_c(c, bola_img(int(round(size / 4) * 4), cor), x, y)


@lru_cache(maxsize=4)
def quadra_bg(luz='day'):
    c = CEN('cidade', luz).copy()
    p = Pen(1242, 2208)
    hz = 1180
    p.poly([(0, hz - 260), (1242, hz - 260), (1242, hz), (0, hz)], hexc('#2f6b3a'))      # cerca/muro verde
    for x in range(0, 1242, 60): p.stroke([(x, hz - 260), (x + 60, hz)], 3, hexc('#24552d'))
    for x in range(60, 1242, 60): p.stroke([(x, hz - 260), (x - 60, hz)], 3, hexc('#24552d'))
    p.poly([(0, hz), (1242, hz), (1242, 2208), (0, 2208)], hexc('#3b8a4f'))              # quadra de grama
    p.poly([(140, hz + 40), (1102, hz + 40), (1242, 2208), (0, 2208)], hexc('#4ea061'))
    for pts in ([(140, hz + 40), (1102, hz + 40)], [(140, hz + 40), (0, 2208)], [(1102, hz + 40), (1242, 2208)],
                [(80, 1640), (1162, 1640)], [(621, 1640), (621, 2208)]):
        p.stroke(pts, 10, (250, 250, 250))
    # rede
    p.poly([(40, 1350), (1202, 1350), (1202, 1520), (40, 1520)], (30, 30, 30))
    for x in range(40, 1202, 26): p.stroke([(x, 1350), (x, 1520)], 2, (120, 120, 120))
    for y in range(1350, 1520, 26): p.stroke([(40, y), (1202, y)], 2, (120, 120, 120))
    p.stroke([(40, 1350), (1202, 1350)], 14, (250, 250, 250))
    p.line([(40, 1300), (40, 1540)], hexc('#555555'), 14, 4); p.line([(1202, 1300), (1202, 1540)], hexc('#555555'), 14, 4)
    c.alpha_composite(p.img.resize((1242, 2208), Image.LANCZOS))
    return c


def tela(c, f, cor='w', achou=0.0, a=1.0):
    """conteúdo da TV da sala: quadrinha de tênis com a bolinha pequena."""
    x0, y0, x1, y1 = 712, 532, 1148, 788
    d = ImageDraw.Draw(c)
    d.rectangle((x0, y0, x1, y1), fill=(70, 140, 85, 255))
    d.rectangle((x0 + 30, y0 + 30, x1 - 30, y1 - 20), outline=(240, 240, 240, 255), width=4)
    d.line([(x0 + 10, (y0 + y1) / 2), (x1 - 10, (y0 + y1) / 2)], fill=(30, 30, 30, 255), width=8)
    t = (f % 40) / 40
    bx = lerp(x0 + 60, x1 - 60, abs(2 * t - 1)); by = lerp(y0 + 60, y1 - 50, abs(math.sin(t * math.pi * 2)))
    col = {'w': (232, 238, 232), 'y': YEL}[cor]
    r = 9 if cor == 'w' else 16
    d.ellipse((bx - r, by - r, bx + r, by + r), fill=col + (255,))
    # chuvisco de TV antiga (ruído leve) no modo branco
    if cor == 'w':
        rnd = random.Random(f // 2)
        for _ in range(120):
            xx, yy = rnd.randint(x0, x1), rnd.randint(y0, y1)
            d.point((xx, yy), fill=(230, 230, 230, 255))
    return bx, by


def s0(f):
    c = quadra_bg('day').copy()
    a_ = wt(0, 'amarela') - 3
    ns = wt(0, 'amarela') - 1
    cor = 'y' if f < ns else 'w'
    bnc = abs(math.sin(f * .18)) * 140
    put_prof(c, 380, 1880, 980, f, expr='shock' if f >= ns else 'grin', arms='point', look=1)
    bola(c, 880, 1250 - bnc, 150 * (1 + .25 * pulse(f, ns, 10)), cor)
    if f >= ns: put_dust(c, 880, 1250 - bnc, 120, f - ns)
    if f >= a_: paste_c(c, txt('NEM SEMPRE!', 110, -5), 700, 620, back(ramp(f, a_, a_ + 8)))
    z = lerp(1.25, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0009 * f)
    return c, (640, 1230 + kick(f, ns, .8) * 12, z, 0), 'day'


def s1(f):
    c = quadra_bg('golden').copy()
    b_ = wt(1, 'branca') - 3
    p_ = wt(1, 'preta') - 3
    if f >= b_:
        bn = abs(math.sin((f - b_) * .2)) * 160
        bola(c, 480, 1300 - bn, 170 * back(ramp(f, b_, b_ + 8)), 'w')
        paste_c(c, txt('BRANCA', 90, -5), 420, 760, back(ramp(f, b_, b_ + 8)))
    if f >= p_:
        bn = abs(math.sin((f - p_) * .2 + 1)) * 160
        bola(c, 860, 1300 - bn, 170 * back(ramp(f, p_, p_ + 8)), 'k')
        paste_c(c, txt('PRETA', 90, 5), 880, 900, back(ramp(f, p_, p_ + 8)))
    put_prof(c, 640, 1900, 720, f, expr='neutral' if f < p_ else 'shock', arms='chin', look=0)
    if f < b_: paste_c(c, txt('ANTIGAMENTE...', 96, -4), 640, 620, back(ramp(f, 0, 8)))
    z = lerp(1.1, 1.2, smooth(ramp(f, 0, 90))) * (1 + .0009 * f)
    return c, (640, 1180, z, 0), 'golden'


def s2(f):
    c = CEN('sala', 'day').copy()
    tv = wt(2, 'televisao') - 3
    ac = wt(2, 'achava') - 3
    on = f >= tv
    if on: tela(c, f, 'w')
    put_prof(c, 420, 1880, 960, f, expr='nervous' if f >= ac else ('grin' if on else 'neutral'), arms='chin' if f >= ac else 'point', look=1)
    if f >= ac: paste_c(c, txt('CADÊ A BOLINHA?', 78, -4), 720, 1010, back(ramp(f, ac, ac + 8)))
    t = smooth(ramp(f, tv, tv + 30))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (lerp(640, 700, t), lerp(1200, 1050, t), z, 0), 'day'


def s3(f):
    c = CEN('sala', 'day').copy()
    am = wt(3, 'amarelo') - 3
    an = wt(3, 'setenta') - 6
    tela(c, f, 'y' if f >= am else 'w')
    put_prof(c, 420, 1880, 960, f, expr='proud' if f >= am else 'nervous', arms='point' if f >= am else 'chin', look=1)
    if f >= am: bola(c, 930, 1020 + 30 * math.sin(f * .2), 150 * back(ramp(f, am, am + 8)), 'y')
    if am <= f < an: paste_c(c, txt('AGORA SIM!', 86, -5), 890, 1330, back(ramp(f, am, am + 8)))
    if f >= an: paste_c(c, txt('1972', 140, 5), 900, 1330, back(ramp(f, an, an + 8)))
    t = easeOut(ramp(f, 0, 40))
    z = lerp(1.2, 1.1, t) * (1 + .0009 * f)
    return c, (lerp(700, 680, t), lerp(1050, 1120, t) + kick(f, an, .8) * 12, z, 0), 'dusk'


def s4(f):
    c = quadra_bg('golden').copy()
    r_ = wt(4, 'resistiu') - 3
    o_ = wt(4, 'oitenta') - 6
    cor = 'y' if f >= o_ else 'w'
    bn = abs(math.sin(f * .2)) * 150
    bola(c, 820, 1300 - bn, 160 * (1 + .25 * pulse(f, o_, 10)), cor)
    if f >= o_: put_dust(c, 820, 1300 - bn, 120, f - o_)
    put_prof(c, 380, 1880, 820, f, expr='stern' if r_ <= f < o_ else ('grin' if f >= o_ else 'neutral'),
             arms='shrug' if f >= o_ else 'chin', look=1)
    if r_ <= f < o_: paste_c(c, txt('SÓ BRANCA!', 100, -5), 760, 700, back(ramp(f, r_, r_ + 8)))
    if f >= o_: paste_c(c, txt('1986', 150, 5), 760, 700, back(ramp(f, o_, o_ + 8)))
    z = lerp(1.15, 1.05, smooth(ramp(f, 0, 60))) * (1 + .0009 * f)
    return c, (640, 1180 + kick(f, o_, .8) * 12, z, 0), 'golden'


def s5(f):
    c = CEN('sala', 'dusk').copy()
    t_ = wt(5, 'televisao') - 3
    bx, by = tela(c, f, 'y')
    put_prof(c, 400, 1880, 980, f, expr='grin' if f >= t_ else 'smug', arms='point' if f >= t_ else 'chin', look=1)
    if f >= t_: paste_c(c, txt('A TV ESCOLHEU!', 70, 5), 790, 1330, back(ramp(f, t_, t_ + 8)))
    t = easeOut(ramp(f, 0, 60))
    z = lerp(1.05, 1.2, t) * (1 + .0009 * f)
    return c, (680, lerp(1200, 1120, t) + kick(f, t_, .7) * 12, z, lerp(0, -2, t)), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]
