"""Um Café com o Mundo — CURIOSIDADE em desenho (13/11/2026 17h).
Fontes: Sci.News (12/11/2026), 'South African Fossil Reveals New Species of Early Sauropodomorph Dinosaur', sobre o artigo de
Atashni Moopen (Universidade de Witwatersrand) e colegas na Royal Society Open Science, vol. 13 (11), art. 261002 (nov/2026).
Fatos: Nyana rooiwalensis, sauropodomorfo do Triássico Superior (~220 milhões de anos), Formação Elliot inferior, arredores da
vila de Qhemegha, província do Cabo Oriental, África do Sul; coletado em 2018. Crânio de 21,3 cm, juvenil de pelo menos 3 anos
(anéis de crescimento e suturas abertas); o crânio completo seria maior que o do maior adulto conhecido de Massospondylus;
na mesma idade, mais de 4x maior que juvenis de Massospondylus e Mussaurus. 1º crânio quase completo e articulado de dinossauro do
Triássico Superior sul-africano. Escaneado com raios X no ESRF (síncrotron europeu). Adultos podem ter tido várias toneladas.
Andava sobre 2 pernas. Crescimento rápido surgiu cedo nos sauropodomorfos, bem antes dos gigantes."""
from kit import *
import kit
from art import ik2

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Com só três anos de idade, esse filhote de dinossauro já tinha a cabeça maior que a de um primo adulto!",
    "Ele viveu há duzentos e vinte milhões de anos, onde hoje fica a África do Sul. E acaba de ganhar nome: Niana.",
    "O crânio tem vinte e um centímetros e foi achado em dois mil e dezoito, no Cabo Oriental.",
    "É o primeiro crânio quase completo de dinossauro dessa época no país. E foi escaneado com raios X superpotentes.",
    "Os anéis de crescimento dos ossos contam a idade. E, nessa idade, ele era mais de quatro vezes maior que filhotes de outros parentes.",
    "Por que isso importa? Crescer rápido apareceu cedo nessa família, bem antes dos gigantes de pescoço comprido.",
    "E os adultos? Podem ter passado de várias toneladas. Que bebezão!",
]
CAPTXT = [
    "Com só 3 anos de idade, esse filhote de dinossauro|já tinha a cabeça maior|que a de um primo adulto!",
    "Ele viveu há 220 milhões de anos,|onde hoje fica a África do Sul.|E acaba de ganhar nome: Nyana.",
    "O crânio tem 21 centímetros|e foi achado em 2018,|no Cabo Oriental.",
    "É o primeiro crânio quase completo|de dinossauro dessa época no país.|E foi escaneado com raios X superpotentes.",
    "Os anéis de crescimento dos ossos contam a idade.|E, nessa idade, ele era mais de 4 vezes maior|que filhotes de outros parentes.",
    "Por que isso importa? Crescer rápido apareceu cedo|nessa família, bem antes dos gigantes|de pescoço comprido.",
    "E os adultos? Podem ter passado|de várias toneladas.|Que bebezão!",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'tres', 6), (0, 'adulto', 8), (1, 'vinte', 6), (1, 'Africa', 6), (1, 'Niana', 6), (2, 'centimetros', 6),
         (2, 'dezoito', 6), (3, 'primeiro', 6), (3, 'raios', 6), (4, 'aneis', 6), (4, 'quatro', 6), (5, 'importa', 6),
         (5, 'gigantes', 6), (6, 'toneladas', 6), (6, 'bebezao', 8)]

SG = hexc('#e0a14a'); SGD = hexc('#b9782f'); BELLY = hexc('#f4dfac')
CG = hexc('#86b9c9'); CGD = hexc('#5d8fa1')
BONE = hexc('#eee3c3'); BONED = hexc('#c5b48a'); HOLE = hexc('#5a4a3a')
XR = hexc('#7fe3ff')


def fin(p):
    return p.img.resize((p.W, p.H), Image.LANCZOS)


# ------------------------------------------------------------------ desenhos novos
def sauro(phase=0.0, mouth=0.0, blink=0, expr='calm', look=0.4, baby=0, cor=0):
    """sauropodomorfo bípede de pescoço comprido, de lado olhando p/ direita. 800x800, pés y~785."""
    p = Pen(800, 800)
    two = 2 * math.pi
    body, dark = ((SG, SGD), (CG, CGD))[cor]
    bob = 6 * abs(math.sin(two * phase))
    hip = (330, 540 + bob)
    legs = []
    for k in (1, 0):
        ph = phase + k * .5
        foot = (hip[0] + (-10 if k else 25) + 60 * math.cos(two * ph), 775 - 24 * max(0, math.sin(two * ph)))
        legs.append((hip, ik2(hip, foot, 120, 125), foot))

    def leg(L, far):
        h, kn, ft = L
        col = mul(body, .82) if far else body
        p.line([h, kn], col, 60, 5); p.line([kn, ft], col, 36, 5)
        for dx in (34, 16, -8):
            p.line([ft, (ft[0] + dx, ft[1] + 6)], col, 10, 3)
    leg(legs[0], True)
    sway = 10 * math.sin(two * phase)
    tail = curve((260, 480 + bob), (120, 430 + sway), (10, 470 + sway * 2), 14)
    tail2 = curve((15, 490 + sway * 2), (130, 490 + sway), (270, 570 + bob), 14)
    p.shape(tail + tail2, body, dark, 6, 16)
    p.shape(ell_pts(380, 510 + bob, 150, 105, 48, -.2), body, dark, 6, 22)
    p.shape(ell_pts(410, 560 + bob, 105, 45, 32, -.2), BELLY, None, 0)
    for i in range(5):
        x = 310 + i * 36
        p.dot(x, 445 + bob - i * 6, 7, dark)
    # pescoço comprido
    nb = (480, 460 + bob)
    hx, hy = (610, 150 + bob * .5) if not baby else (600, 230 + bob * .5)
    p.line(curve(nb, (600, 420 + bob), (hx - 30, hy + 50), 12), body, 66, 6)
    # braço com mão
    sh = (500, 520 + bob)
    p.line([sh, (525, 590 + bob), (560, 600 + bob)], mul(body, .9), 18, 4)
    p.line([(560, 600 + bob), (580, 590 + bob)], mul(body, .9), 8, 3)
    leg(legs[1], False)
    # cabeça pequena e arredondada
    m = mouth * .4
    jaw = [(hx - 50, hy + 15), (hx + 85, hy + 22), (hx + 80, hy + 40), (hx - 40, hy + 42)]
    jc, js = math.cos(m), math.sin(m)
    jaw = [(hx - 45 + (x - hx + 45) * jc - (y - hy - 15) * js, hy + 15 + (x - hx + 45) * js + (y - hy - 15) * jc) for x, y in jaw]
    if mouth > .05:
        p.poly([(hx - 30, hy + 15), (hx + 88, hy + 17), jaw[2], jaw[3]], hexc('#7a2430'))
    p.shape(jaw, body, dark, 6, 8)
    up = [(hx - 65, hy - 5), (hx - 30, hy - 55), (hx + 45, hy - 50), (hx + 95, hy - 10), (hx + 92, hy + 20), (hx - 55, hy + 25)]
    p.shape(up, body, dark, 6, 12)
    p.stroke([(hx + 78, hy - 14), (hx + 86, hy - 8)], 4)
    ec = (hx + 5, hy - 18)
    er = (27 if baby else 20) + (3 if expr == 'shock' else 0)
    p.dot(ec[0], ec[1], er, (255, 255, 255), 4)
    if blink < .75:
        lk = max(-1, min(1, look))
        pr = 11 if baby else 9
        p.dot(ec[0] + lk * (er - pr - 1), ec[1] + 2, pr, INK)
        p.dot(ec[0] + lk * (er - pr - 1) - 3, ec[1] - 3, 4, (255, 255, 255))
    else:
        p.poly([(ec[0] - er - 1, ec[1] - er - 2), (ec[0] + er + 1, ec[1] - er - 2), (ec[0] + er + 1, ec[1] + er), (ec[0] - er - 1, ec[1] + er)], body)
        p.stroke([(ec[0] - er, ec[1] + 4), (ec[0] + er, ec[1] + 4)], 4)
    if expr == 'grin' and mouth <= .05:
        p.stroke(curve((hx + 20, hy + 22), (hx + 50, hy + 32), (hx + 78, hy + 20), 8), 4)
    return fin(p)


def cranio(xr=0.0):
    """crânio fóssil de lado. 700x400. xr=1 -> brilho de raio X."""
    p = Pen(700, 400)
    if xr:
        p.shape(ell_pts(350, 200, 340, 190, 48), hexc('#1d3550'), None, 0)
    col, dk = (BONE, BONED) if not xr else (hexc('#cfefff'), XR)
    out = [(40, 210), (120, 110), (300, 70), (480, 100), (640, 180), (660, 230), (600, 270), (420, 300), (200, 310), (70, 280)]
    p.shape(out, col, dk, 7, 16)
    p.shape(ell_pts(230, 170, 62, 55, 28), HOLE, None, 0)    # órbita
    p.shape(ell_pts(110, 220, 36, 46, 20), HOLE, None, 0)    # janela atrás
    p.shape(ell_pts(560, 175, 34, 22, 20), HOLE, None, 0)    # narina
    p.shape(ell_pts(390, 190, 55, 30, 20), HOLE, None, 0)    # antorbital
    for i in range(9):
        x = 330 + i * 32
        p.poly([(x, 282 - i * 2), (x + 20, 282 - i * 2), (x + 10, 312 - i * 2)], (255, 255, 255), 2)
    p.stroke([(150, 300), (620, 260)], 5, dk)
    for (x, y) in ((300, 110), (180, 260), (470, 250)):
        p.stroke([(x, y), (x + 20, y + 12), (x + 10, y + 28)], 4, dk)
    return fin(p)


def anel(n=0.0):
    """corte de osso com anéis de crescimento (n = quantos aparecem, 0-1). 700x700."""
    p = Pen(700, 700)
    p.shape(ell_pts(350, 350, 320, 320, 64), BONE, BONED, 7, 26)
    p.dot(350, 350, 70, hexc('#7a5c46'))
    for i, r in enumerate((130, 200, 270)):
        if n * 3 >= i + .5:
            p.arc(350, 350, r, r, 0, 360, 12, hexc('#9b7b4f'))
    return fin(p)


def bandeira_za():
    """bandeira da África do Sul simplificada. 420x280."""
    p = Pen(420, 280)
    p.shape([(10, 10), (410, 10), (410, 270), (10, 270)], hexc('#de3831'), None, 6)
    p.poly([(10, 140), (410, 140), (410, 270), (10, 270)], hexc('#002395'))
    p.poly([(10, 10), (60, 10), (200, 110), (410, 110), (410, 170), (200, 170), (60, 270), (10, 270)], (255, 255, 255))
    p.poly([(10, 30), (35, 30), (175, 125), (410, 125), (410, 155), (175, 155), (35, 250), (10, 250)], hexc('#007a4d'))
    p.poly([(10, 55), (150, 140), (10, 225)], hexc('#ffb612'))
    p.poly([(10, 75), (120, 140), (10, 205)], INK)
    p.stroke([(10, 10), (410, 10), (410, 270), (10, 270), (10, 10)], 6)
    return fin(p)


def scanner(on=0.0):
    """máquina de raio X (síncrotron) estilizada: anel grande. 800x700."""
    p = Pen(800, 700)
    p.shape([(60, 600), (740, 600), (760, 690), (40, 690)], hexc('#3c4c6e'), hexc('#28344d'), 6, 10)
    p.shape(ell_pts(400, 330, 330, 290, 64), hexc('#e6ebf2'), hexc('#aeb8c6'), 7, 18)
    p.shape(ell_pts(400, 330, 210, 180, 48), hexc('#1d3550') if on else hexc('#2c2f3d'), None, 6)
    for i in range(8):
        a = i * math.pi / 4
        p.dot(400 + 270 * math.cos(a), 330 + 235 * math.sin(a), 16, XR if on else hexc('#8d98a8'), 3)
    return fin(p)


def put_sauro(c, x, feet, h, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    put_sprite(c, 'sauro', x, feet, h, 1.0, flip, {'phase': 16, 'mouth': 6, 'look': 4}, **kw)


def put_img(c, fn, x, feet, h, aspect, **kw):
    put_sprite(c, fn, x, feet, h, aspect, False, {'n': 6, 'xr': 4, 'on': 4}, **kw)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def blk(f, seed):
    return 1 if blinkAt(f, seed) > .6 else 0


# ------------------------------------------------------------------ cenas
def s0(f):
    # gancho: filhote grande ao lado do primo adulto menor, na paisagem do Triássico (floresta)
    c = CEN('floresta', 'day').copy()
    tr = wt(0, 'tres') - 3
    ca = wt(0, 'cabeca') - 3
    ad = wt(0, 'adulto') - 3
    put_sauro(c, 420, 1640, 520, flip=False, cor=1, phase=(f * .02) % 1, blink=blk(f, 3), look=.8,
              expr='shock' if f >= ad else 'calm')
    put_sauro(c, 820, 1660, 860, flip=True, baby=1, phase=0, blink=blk(f, 1), look=.6,
              mouth=.6 * math.sin(clamp((f - ca) / 20) * math.pi) if f >= ca else 0, expr='grin')
    num(c, '3 ANOS', 820, 560, f, tr, 130, -4)
    num(c, 'FILHOTE', 820, 700, f, tr + 6, 80, 3)
    num(c, 'ADULTO', 400, 900, f, ad, 80, -3)
    z = lerp(1.35, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ad)
    return c, (640, 1180 + k * 10, z, k), 'day'


def s1(f):
    c = CEN('mapa', 'day').copy()
    vi = wt(1, 'vinte') - 3
    af = wt(1, 'Africa') - 3
    ni = wt(1, 'Niana') - 3
    num(c, '220 MILHÕES', 640, 520, f, vi, 120, -4)
    num(c, 'DE ANOS', 640, 650, f, vi + 5, 90, 3)
    if f >= af:
        paste_c(c, sprite('bandeira_za', (), 220, 1.5, False), 640, 860, back(ramp(f, af, af + 10)))
        num(c, 'ÁFRICA DO SUL', 640, 1040, f, af + 2, 80, -3)
    if f >= ni:
        num(c, 'NYANA', 640, 1230, f, ni, 130, 4)
        num(c, 'ROOIWALENSIS', 640, 1370, f, ni + 4, 70, -3)
    t = smooth(ramp(f, 0, 90))
    return c, (640, lerp(1050, 1120, t), lerp(1.1, 1.0, t) * (1 + .0006 * f), 1.2 * math.sin(f * .04)), 'day'


def s2(f):
    c = CEN('montanha', 'golden').copy()
    ce = wt(2, 'centimetros') - 3
    de = wt(2, 'dezoito') - 3
    cb = wt(2, 'Cabo') - 3
    put_img(c, 'cranio', 520, 1650, 300, 700 / 400)
    put_dust(c, 520, 1560, 160, f - 4)
    put_sci(c, 1000, 1720, 760, f, 2, arms='point' if f >= ce else 'clip', expr='grin' if f >= ce else 'neutral',
            skin=2, look=-1, glasses=True)
    num(c, '21 CM', 520, 1220, f, ce, 130, -4)
    num(c, '2018', 640, 560, f, de, 140, 3)
    num(c, 'CABO ORIENTAL', 640, 720, f, cb, 80, -3)
    t = smooth(ramp(f, 0, 100))
    k = kick(f, ce, .6)
    return c, (lerp(700, 620, t), lerp(1150, 1250, t) + k * 8, lerp(1.0, 1.15, t), k), 'golden'


def s3(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    pr = wt(3, 'primeiro') - 3
    ra = wt(3, 'raios') - 3
    on = 1 if f >= ra else 0
    if f < ra:
        put_img(c, 'cranio', 640, 1350, 420, 700 / 400)
        num(c, '1º CRÂNIO', 640, 560, f, pr, 120, -4)
        num(c, 'QUASE COMPLETO', 640, 700, f, pr + 6, 80, 3)
    else:
        put_img(c, 'scanner', 640, 1600, 860, 800 / 700, on=1)
        put_img(c, 'cranio', 640, 1290, 260, 700 / 400, xr=1)
        num(c, 'RAIOS X!', 640, 560, f, ra, 130, -4)
        put_dust(c, 640, 1150, 220, f - ra)
    z = lerp(1.05, 1.2, smooth(ramp(f, 0, 140))) * (1 + .0005 * f)
    k = kick(f, ra)
    return c, (640, 1150 + k * 10, z, k), 'day'


def s4(f):
    c = BG('lab').copy()
    an = wt(4, 'aneis') - 3
    id_ = wt(4, 'idade', 1) - 3
    qu = wt(4, 'quatro') - 3
    if f < id_:
        put_img(c, 'anel', 640, 1450, 780, 1, n=ramp(f, an, an + 30))
        num(c, 'ANÉIS DE CRESCIMENTO', 640, 560, f, an, 62, -3)
        z = lerp(1.0, 1.15, smooth(ramp(f, 0, id_)))
        return c, (640, 1120, z, 0), 'day'
    c = CEN('floresta', 'day').copy()
    put_sauro(c, 820, 1660, 820, flip=True, baby=1, phase=(f * .02) % 1, blink=blk(f, 1), look=.6, expr='grin')
    for i, x in enumerate((240, 420)):
        put_sauro(c, x, 1650, 220, cor=1, baby=1, phase=((f + i * 9) * .03) % 1, blink=blk(f, 5 + i), look=.9,
                  expr='shock' if f >= qu else 'calm')
    num(c, 'MAIS DE 4X', 640, 560, f, qu, 140, -4)
    num(c, 'MAIOR', 640, 700, f, qu + 5, 100, 3)
    k = kick(f, qu)
    z = lerp(1.15, 1.05, smooth(ramp(f, id_, id_ + 40))) * (1 + .0005 * f)
    return c, (640, 1200 + k * 10, z, k), 'day'


def s5(f):
    c = CEN('floresta', 'dusk').copy()
    im = wt(5, 'importa') - 3
    cr = wt(5, 'rapido') - 3
    gi = wt(5, 'gigantes') - 3
    put_sauro(c, 760, 1650, 640, flip=True, baby=1, phase=0, blink=blk(f, 1), look=.4)
    num(c, 'POR QUE IMPORTA?', 640, 540, f, im, 80, -4)
    num(c, 'CRESCER RÁPIDO', 640, 680, f, cr, 80, 3)
    if f >= gi:
        s = back(ramp(f, gi, gi + 12))
        put_sauro(c, 360, 1660, 760 * s, cor=1, phase=(f * .02) % 1, blink=blk(f, 4), look=.5)
        num(c, 'GIGANTES', 640, 820, f, gi + 2, 90, -3)
    k = kick(f, gi)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 90))) * (1 + .0004 * f)
    return c, (640, 1200 + k * 10, z, k + 1.5 * math.sin(f * .04)), 'dusk'


def s6(f):
    c = CEN('floresta', 'dusk').copy()
    to = wt(6, 'toneladas') - 3
    be = wt(6, 'bebezao') - 3
    put_sauro(c, 640, 1690, 900, flip=True, baby=0, phase=(f * .015) % 1, blink=blk(f, 2), look=.3,
              expr='grin' if f >= be else 'calm')
    num(c, 'VÁRIAS TONELADAS', 640, 520, f, to, 80, -4)
    num(c, 'QUE BEBEZÃO!', 640, 650, f, be, 100, 4)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 70))) * (1 + .0006 * f)
    k = kick(f, be, .7)
    return c, (640 + .12 * f, 1200 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'tres') - 3, 140, .8)
    s.ting(s.W(0, 'adulto') - 3, .3)
    s.thunk(s.W(1, 'vinte') - 3, 120, .7)
    s.ting(s.W(1, 'Niana') - 3, .35)
    s.thunk(s.W(2, 'centimetros') - 3, 140, .6)
    s.whoosh(s.W(3, 'raios') - 3, .4, .6)
    for i in range(3): s.ting(s.W(4, 'aneis') - 3 + i * 8, .12)
    s.thunk(s.W(4, 'quatro') - 3, 180, .7)
    s.thunk(s.W(5, 'gigantes') - 3, 220, .7)
    s.ting(s.W(6, 'bebezao') - 3, .3)
