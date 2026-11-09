"""Um Café com o Mundo — CURIOSIDADE (segunda 09/11/2026, 17h).
Tema: robô ASTRA, do Caltech, faz a primeira montagem automática de uma estrutura no espaço.
Fontes (conferidas em 09/11/2026):
- DARPA, 05/11/2026 "NOM4D program demonstrates automated in-space assembly": "first ever demonstration of automated
  in-space assembly"; robô tipo pórtico que se move em 3 eixos lineares conectou varetas de compósito com juntas
  próprias e abriu uma malha refletora fina (prova de conceito de antenas); lançado no Transporter-16 da SpaceX no
  fim de março, a bordo do Vigoride (Momentus); programa visa estruturas de centenas de metros ou quilômetros.
- Caltech / ScienceDaily 09/11/2026: ASTRA (Autonomous In-Space Tensioned Reflector Assembly); lançado 30/03/2026;
  ~1 metro cúbico dobrado; antena planejada de 1,4 m; começou com 2 módulos prontos e montou um 3º em órbita
  (projeto completo: 11); ~6 meses em órbita, termina em dezembro; 7 ou 8 contatos por dia de ~15 min;
  "primeira vez que uma estrutura é construída de forma autônoma no espaço"; permitiria telescópios, antenas e
  painéis solares maiores do que cabe na ponta de um foguete.
Sem logotipos; robô, foguete e cientistas genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Pela primeira vez, um robô montou sozinho uma estrutura lá no espaço.",
    "Ele se chama ASTRA, foi criado no Caltech, nos Estados Unidos, e subiu em março, dobrado numa caixa de um metro cúbico.",
    "Em órbita, deslizando em três trilhos, ele encaixou varetas e montou mais um módulo de antena, com uma malha que reflete sinais.",
    "Da Terra, a equipe só falava com ele sete ou oito vezes por dia, quinze minutos por vez.",
    "Mas por que isso importa? Nenhum foguete consegue levar um telescópio ou uma antena gigante já montados.",
    "A ideia é que robôs assim montem, em órbita, estruturas de centenas de metros, ou até de quilômetros.",
    "A antena completa teria só um metro e quarenta, e a missão acaba em dezembro. Mas o primeiro tijolo já foi posto.",
]
CAPTXT = [
    "Pela primeira vez, um robô montou sozinho|uma estrutura lá no espaço.",
    "Ele se chama ASTRA, foi criado no Caltech, nos Estados Unidos,|e subiu em março, dobrado numa caixa de 1 metro cúbico.",
    "Em órbita, deslizando em 3 trilhos, ele encaixou varetas|e montou mais um módulo de antena, com uma malha que reflete sinais.",
    "Da Terra, a equipe só falava com ele 7 ou 8 vezes por dia,|15 minutos por vez.",
    "Mas por que isso importa? Nenhum foguete consegue levar|um telescópio ou uma antena gigante já montados.",
    "A ideia é que robôs assim montem, em órbita,|estruturas de centenas de metros, ou até de quilômetros.",
    "A antena completa teria só 1,4 metro, e a missão acaba em dezembro.|Mas o primeiro tijolo já foi posto.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'primeira', 4), (1, 'astra', 4), (1, 'metro', 4), (2, 'tres', 4), (2, 'malha', 6), (3, 'quinze', 4),
         (4, 'gigante', 4), (5, 'quilometros', 4), (6, 'tijolo', 4)]

WHITE = (255, 255, 255)
GOLD = hexc('#e8b440'); GOLD_D = hexc('#b8862a')
SILV = hexc('#dfe3ea'); SILV_D = hexc('#a9b0bd')
ORG = hexc('#f08a2c'); ORG_D = hexc('#c0661a')
RED = hexc('#d8443c')
ROD = (236, 238, 244)
MESH = (150, 210, 255)


# ------------------------------------------------------------------ desenhos novos
def astra(look=0.0, blink=0, expr='calm', slide=0.5, grip=0.0):
    """robô de pórtico genérico: moldura cinza com trilho em cima, carrinho laranja com olho que desliza, garra.
    700x700, base em y≈660."""
    p = Pen(700, 700)
    # base dourada
    p.shape([(60, 600), (640, 600), (620, 670), (80, 670)], GOLD, GOLD_D, 6, 12)
    for i in range(6): p.stroke([(100 + i * 95, 610), (110 + i * 95, 660)], 3, hexc('#f4d27a'))
    # colunas e trilho
    for x in (110, 590):
        p.shape([(x - 20, 140), (x + 20, 140), (x + 20, 600), (x - 20, 600)], SILV, SILV_D, 5, 8)
    p.shape([(80, 110), (620, 110), (620, 160), (80, 160)], hexc('#8a8f99'), hexc('#6b6b70'), 6, 8)
    for x in range(110, 600, 40): p.stroke([(x, 120), (x + 20, 150)], 3, hexc('#b0b4bd'))
    # carrinho
    cx = 200 + 300 * slide
    p.line([(cx, 330), (cx, 330 + 120 + 60 * grip)], hexc('#6b6b70'), 22, 5)
    gy = 450 + 60 * grip
    for s in (-1, 1):
        p.line([(cx, gy), (cx + s * 40, gy + 30), (cx + s * (24 - 10 * grip), gy + 70)], hexc('#6b6b70'), 12, 4)
    p.shape([(cx - 110, 150), (cx + 110, 150), (cx + 110, 340), (cx - 110, 340)], ORG, ORG_D, 6, 14)
    ex, ey, er = cx, 245, 62 if expr == 'shock' else 56
    p.dot(ex, ey, er, WHITE, 5)
    L = max(.45 if expr == 'proud' else 0, blink)
    if L < .75:
        lk = max(-1, min(1, look))
        p.dot(ex + lk * (er - 24), ey + 4, 16 if expr == 'shock' else 22, INK)
        p.dot(ex + lk * (er - 24) - 6, ey - 4, 6, WHITE)
    if L > .02:
        top = ey - er; yb = top + 2 * er * L
        p.poly([(ex - er - 1, top - 2), (ex + er + 1, top - 2), (ex + er + 1, yb), (ex - er - 1, yb)], ORG)
        p.stroke([(ex - er, yb), (ex + er, yb)], 5)
    if expr == 'shock': p.arc(ex, ey - 82, 30, 10, 200, 340, 5)
    if expr == 'proud': p.arc(ex, ey + 30, 26, 14, 20, 160, 5)
    # antena de comunicação
    p.line([(cx + 80, 150), (cx + 100, 70)], hexc('#6b6b70'), 8, 4)
    p.dot(cx + 100, 64, 14, RED, 4)
    return p.img


def foguete(fire=0.0):
    """foguete genérico branco com bico vermelho. 400x1100, base em y≈900 (chama abaixo)."""
    p = Pen(400, 1100)
    if fire > 0:
        for i, (col, s) in enumerate(((hexc('#f7d046'), 1.0), (hexc('#f08a2c'), .75), (hexc('#fff3c0'), .45))):
            L = 220 * fire * s
            p.poly([(200 - 90 * s, 880), (200 + 90 * s, 880), (200 + 30 * s, 880 + L * .6), (200, 880 + L), (200 - 30 * s, 880 + L * .6)], col, 0 if i else 4)
    for s in (-1, 1):
        p.shape([(200 + s * 95, 650), (200 + s * 175, 860), (200 + s * 175, 900), (200 + s * 95, 860)], RED, mul(RED, .75), 6, 8)
    p.shape([(105, 300), (295, 300), (295, 880), (105, 880)], WHITE, hexc('#d6dbe4'), 6, 18)
    p.shape(curve((105, 300), (200, -40), (295, 300), 16), RED, mul(RED, .75), 6, 10)
    p.dot(200, 450, 48, hexc('#2b2f3e'), 6); p.dot(200, 450, 32, hexc('#7fc3ff'))
    p.stroke([(105, 620), (295, 620)], 5, hexc('#a9b0bd'))
    return p.img


def antena_gigante():
    """prato de antena gigante genérico. 900x900."""
    p = Pen(900, 900)
    p.line([(450, 560), (450, 860)], hexc('#8a8f99'), 40, 6)
    p.shape([(330, 850), (570, 850), (600, 890), (300, 890)], hexc('#8a8f99'), hexc('#6b6b70'), 6, 6)
    p.shape(curve((40, 160), (450, 900), (860, 160), 30), SILV, SILV_D, 7, 30)
    p.shape(ell_pts(450, 160, 410, 70, 40), hexc('#f2f4f8'), None, 6)
    for k in range(1, 4): p.poly(ell_pts(450, 160, 410 * k / 4, 70 * k / 4, 30), None, 3) if False else p.stroke(ell_pts(450, 160, 410 * k / 4, 70 * k / 4, 30) + [ell_pts(450, 160, 410 * k / 4, 70 * k / 4, 30)[0]], 3, SILV_D)
    p.line([(450, 160), (450, 10)], hexc('#6b6b70'), 12, 4)
    p.dot(450, 10, 20, RED, 4)
    return p.img


@lru_cache(maxsize=4)
def orbita_bg(atm=0):
    """espaço com estrelas e a Terra grande embaixo."""
    p = Pen(BW, BH)
    base = Image.new('RGBA', (BW, BH), hexc('#0e1436') + (255,))
    rnd = random.Random(11)
    for i in range(190):
        p.dot(rnd.randint(0, BW), rnd.randint(0, 1700), rnd.choice((2, 2, 3, 4)), (255, 255, 230))
    cx, cy, R = 621, 3300, 1650
    p.poly(ell_pts(cx, cy, R + 40, R + 40, 160), hexc('#7fc3ff'))
    p.shape(ell_pts(cx, cy, R, R, 160), hexc('#3a7fd0'), hexc('#2a5fa4'), 7, 40)
    for lx, ly, rx, ry in ((300, 1760, 260, 120), (880, 1820, 220, 150), (620, 2000, 300, 140)):
        p.shape(ell_pts(lx, ly, rx, ry, 40, .2), hexc('#7fb05a'), hexc('#5f8a40'), 5, 12)
    for wx, wy in ((150, 1900), (520, 1700), (1050, 1950)):
        p.shape(ell_pts(wx, wy, 120, 34, 30), WHITE, hexc('#dfe6ef'), 0, 6)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


@lru_cache(maxsize=2)
def base_lancamento():
    """céu de dia com mar e torre de lançamento ao longe."""
    p = Pen(BW, BH)
    base = Image.new('RGBA', (BW, BH), hexc('#8fd0f5') + (255,))
    p.poly([(0, 1450), (BW, 1450), (BW, BH), (0, BH)], hexc('#d9c48f'))
    p.poly([(0, 1380), (BW, 1380), (BW, 1460), (0, 1460)], hexc('#4f9bd0'))
    p.shape([(0, 1450), (BW, 1450), (BW, 1520), (0, 1520)], hexc('#c9b37c'), None, 0)
    for cx, cy in ((240, 360), (900, 520), (1100, 260)):
        for dx, r in ((-60, 60), (0, 85), (70, 60)):
            p.dot(cx + dx, cy, r, WHITE)
    # torre
    p.shape([(220, 600), (300, 600), (300, 1470), (220, 1470)], hexc('#d8443c'), hexc('#a8302a'), 6, 8)
    for y in range(640, 1460, 80):
        p.stroke([(225, y), (295, y + 70)], 4, hexc('#8a2420'))
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


def put_astra(c, x, base, w, rot=0, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    for k in ('slide', 'grip'):
        if k in kw: kw[k] = round(kw[k] * 12) / 12
    im = sprite('astra', tuple(sorted(kw.items())), int(w), 1.0, False)
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, base - w * .44)


def put_fog(c, x, base, h, fire=0.0):
    im = sprite('foguete', (('fire', round(fire * 6) / 6),), int(h), 400 / 1100, False)
    paste_c(c, im, x, base - h * (900 - 550) / 1100)


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def treliça(c, x0, y, bw, h, bays, part=1.0, mesh=0.0, wid=8):
    """treliça horizontal: `bays` módulos completos a partir de x0 (para a direita) + 1 módulo parcial (part 0..1)."""
    d = ImageDraw.Draw(c, 'RGBA')
    def rod(a, b, t=1.0):
        if t <= 0: return
        b = (lerp(a[0], b[0], t), lerp(a[1], b[1], t))
        d.line([a, b], fill=INK, width=wid + 6); d.line([a, b], fill=ROD, width=wid)
    for i in range(bays):
        xa, xb = x0 + i * bw, x0 + (i + 1) * bw
        if mesh > 0:
            m = int(110 * mesh)
            d.rectangle([xa, y - h / 2, xa + (xb - xa) * mesh, y + h / 2], fill=MESH + (m,))
            for gx in range(int(xa), int(xa + (xb - xa) * mesh), 22): d.line([(gx, y - h / 2), (gx, y + h / 2)], fill=(220, 240, 255, 140), width=2)
            for gy in range(int(y - h / 2), int(y + h / 2), 22): d.line([(xa, gy), (xa + (xb - xa) * mesh, gy)], fill=(220, 240, 255, 140), width=2)
        for a, b in (((xa, y - h / 2), (xb, y - h / 2)), ((xa, y + h / 2), (xb, y + h / 2)), ((xa, y - h / 2), (xb, y + h / 2)),
                     ((xb, y - h / 2), (xb, y + h / 2)), ((xa, y - h / 2), (xa, y + h / 2))):
            rod(a, b)
    if part > 0:
        xa, xb = x0 + bays * bw, x0 + (bays + 1) * bw
        segs = (((xa, y - h / 2), (xb, y - h / 2)), ((xa, y + h / 2), (xb, y + h / 2)), ((xa, y - h / 2), (xb, y + h / 2)), ((xb, y - h / 2), (xb, y + h / 2)))
        for k, (a, b) in enumerate(segs):
            rod(a, b, clamp(part * 4 - k))
    for i in range(bays + (1 if part >= 1 else 0) + 1):
        xx = x0 + i * bw
        for yy in (y - h / 2, y + h / 2):
            d.ellipse([xx - wid * 1.4, yy - wid * 1.4, xx + wid * 1.4, yy + wid * 1.4], fill=ORG, outline=INK, width=3)


def estrelas(c, f, seed=5, n=60, y1=1300):
    d = ImageDraw.Draw(c, 'RGBA'); rnd = random.Random(seed)
    for i in range(n):
        x, y = rnd.randint(0, BW), rnd.randint(0, y1)
        r = 2 + 2 * (0.5 + 0.5 * math.sin(f * .15 + i))
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 230, 220))


def caixa(c, x, y, s, lab=True):
    """caixa (cubo) aberta: 1 metro cúbico."""
    d = ImageDraw.Draw(c)
    w = 260 * s
    d.polygon([(x - w / 2, y - w / 2), (x + w / 2, y - w / 2), (x + w / 2, y + w / 2), (x - w / 2, y + w / 2)], fill=hexc('#c99a5a'), outline=INK, width=7)
    d.polygon([(x - w / 2, y - w / 2), (x - w / 4, y - w * .8), (x + w * .75, y - w * .8), (x + w / 2, y - w / 2)], fill=hexc('#ddb478'), outline=INK, width=7)
    d.polygon([(x + w / 2, y - w / 2), (x + w * .75, y - w * .8), (x + w * .75, y + w * .2), (x + w / 2, y + w / 2)], fill=hexc('#a87c44'), outline=INK, width=7)


# ------------------------------------------------------------------ cenas
def s0(f):
    # gancho: ASTRA em órbita encaixando a última vareta de um módulo; "1ª VEZ!"
    c = orbita_bg(0).copy()
    p0 = wt(0, 'primeira') - 3
    m0 = wt(0, 'montou') - 3
    part = ramp(f, 0, m0 + 6)
    treliça(c, 840, 1000, 230, 260, 1, part, 0, 10)
    sl = .55 + .4 * math.sin(f * .12) if f < m0 + 6 else .95
    put_astra(c, 560, 1250, 640, look=1, blink=blinkAt(f, 3) if f < p0 else 0,
              expr='proud' if f >= m0 + 6 else ('shock' if f >= p0 else 'calm'), slide=sl, grip=.5 + .5 * math.sin(f * .3))
    num(c, '1ª VEZ!', 640, 470, f, p0, 170, -5)
    num(c, 'SOZINHO', 900, 680, f, wt(0, 'sozinho') - 3, 100, 4)
    z = lerp(1.45, 1.08, easeOut(ramp(f, 0, 45))) * (1 + .0006 * f)
    k = kick(f, p0)
    return c, (680 + 10 * math.sin(f * .05), 1000 + k * 10, z, k), 'day'


def s1(f):
    # base de lançamento -> caixa de 1 m³ e foguete subindo
    c = base_lancamento().copy()
    l0 = wt(1, 'subiu') - 6
    t = ramp(f, l0, l0 + 70)
    fy = 1470 - 1400 * (t ** 1.8)
    put_fog(c, 640, fy, 1000, fire=ramp(f, l0 - 4, l0 + 4))
    if f >= l0:
        d = ImageDraw.Draw(c, 'RGBA')
        for i in range(10):
            r = 70 + i * 18 + (f - l0) * 1.5
            d.ellipse([640 - r * 1.6 + (i - 5) * 50, 1470 - r * .5, 640 + r * .4 + (i - 5) * 50, 1470 + r * .3], fill=(240, 240, 240, 170))
    num(c, 'ASTRA', 640, 330, f, wt(1, 'astra') - 3, 160, -3)
    num(c, 'CALTECH (EUA)', 640, 500, f, wt(1, 'caltech') - 3, 90, 3)
    num(c, 'MARÇO 2026', 640, 680, f, wt(1, 'marco') - 3, 90, -4)
    b0 = wt(1, 'caixa') - 3
    if f >= b0:
        s = back(ramp(f, b0, b0 + 8))
        caixa(c, 920, 1120, s)
        paste_c(c, txt('1 METRO CÚBICO', 64, -3), 880, 900, s)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 120)))
    cy = lerp(1000, 900, smooth(t))
    k = kick(f, l0 + 4, .6)
    return c, (640, cy + k * 10, z, k), 'day'


def s2(f):
    # close: o carrinho desliza nos trilhos, encaixa varetas, a malha se abre
    c = CEN('espaco', 'day').copy()
    t0 = wt(2, 'tres') - 3
    v0 = wt(2, 'varetas') - 3
    m0 = wt(2, 'modulo') - 3
    ml = wt(2, 'malha') - 3
    part = ramp(f, v0, m0 + 4)
    treliça(c, 700, 980, 210, 300, 1, part, 0, 10)
    mesh = smooth(ramp(f, ml, ml + 25))
    if mesh > 0:
        treliça(c, 700, 980, 210, 300, 2 if part >= 1 else 1, 0, mesh, 10)
    sl = .5 + .5 * math.sin(f * .16) if f >= t0 else .5
    put_astra(c, 470, 1260, 600, look=1, blink=blinkAt(f, 5), expr='proud' if f >= m0 else 'calm', slide=sl,
              grip=.5 + .5 * math.sin(f * .35) if f >= v0 else 0)
    if False:
        d = ImageDraw.Draw(c)
        for i, (dx, dy) in enumerate(((1, 0), (0, 1), (.7, -.7))):
            a0 = t0 + i * 6
            if f >= a0:
                s = back(ramp(f, a0, a0 + 8))
                x, y = 300, 520
                x2, y2 = x + dx * 150 * s, y + dy * 150 * s
                d.line([(x, y), (x2, y2)], fill=INK, width=18); d.line([(x, y), (x2, y2)], fill=ORG, width=10)
    num(c, '3 TRILHOS', 640, 470, f, t0, 100, -4)
    num(c, '+1 MÓDULO', 760, 640, f, m0, 110, 3)
    num(c, 'MALHA QUE REFLETE', 800, 1200, f, ml, 62, -3)
    z = lerp(1.05, 1.25, smooth(ramp(f, 0, 140)))
    cx = lerp(560, 760, smooth(ramp(f, v0 - 10, ml + 20)))
    return c, (cx, 980, z * (1 + .0004 * f), 0), 'day'


def s3(f):
    # sala de controle na Terra: 2 cientistas no computador, relógio, 7-8x/dia, 15 min
    c = CEN('escritorio', 'day').copy()
    d = ImageDraw.Draw(c)
    # monitor com o robô
    d.rounded_rectangle([420, 820, 860, 1120], 16, fill=hexc('#2b2f3e'), outline=INK, width=8)
    d.rectangle([440, 840, 840, 1100], fill=hexc('#0e1436'))
    im = sprite('astra', (('blink', 0), ('expr', 'calm'), ('grip', 0.0), ('look', -1.0), ('slide', round((.5 + .5 * math.sin(f * .1)) * 12) / 12)), 220, 1.0, False)
    paste_c(c, im, 640, 960)
    d.rectangle([620, 1120, 660, 1200], fill=hexc('#8a8f99'), outline=INK, width=5)
    d.rectangle([520, 1195, 760, 1225], fill=hexc('#8a8f99'), outline=INK, width=5)
    s0_ = wt(3, 'sete') - 3
    q0 = wt(3, 'quinze') - 3
    put_sci(c, 250, 1700, 760, f, 2, arms='point' if f >= s0_ else 'clip', skin=1, glasses=True, expr='neutral', look=1)
    put_sci(c, 1010, 1700, 740, f, 6, arms='cheek' if f >= q0 else 'clip', skin=3, glasses=False, bun=True,
            expr='nervous' if f >= q0 else 'neutral', look=-1)
    num(c, '7 A 8 VEZES POR DIA', 640, 430, f, s0_, 84, -3)
    if f >= q0:
        s = back(ramp(f, q0, q0 + 8))
        mm = int(15 * ramp(f, q0, q0 + 60))
        paste_c(c, clock_img(12, mm * 4 % 60 if mm < 15 else 15, 200), 640, 640, s)
        paste_c(c, txt('15 MIN', 110, 4), 900, 640, s)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 110)))
    return c, (640 + 12 * math.sin(f * .04), 1000, z, 0), 'day'


def s4(f):
    # por que importa: a antena gigante não cabe no foguete
    c = orbita_bg(0).copy()
    g0 = wt(4, 'gigante') - 3
    n0 = wt(4, 'nenhum') - 3
    put_fog(c, 330, 1450, 900, fire=.5 + .2 * math.sin(f * .8))
    if f >= g0 - 12:
        s = back(ramp(f, g0 - 12, g0 - 2))
        im = sprite('antena_gigante', (), int(900 * s) + 1, 1.0, False)
        paste_c(c, im.rotate(-8 + 3 * math.sin(f * .1), resample=Image.BICUBIC), 860, 860)
    num(c, 'POR QUE IMPORTA?', 640, 330, f, 0, 100, -3)
    num(c, 'NÃO CABE!', 640, 1330, f, g0 + 4, 150, 5)
    if f >= n0:
        d = ImageDraw.Draw(c)
        x, y = 330, 450
        s = back(ramp(f, n0, n0 + 8))
        r = 70 * s
        d.ellipse([x - r, y - r, x + r, y + r], fill=WHITE, outline=INK, width=7)
        if r > 20: paste_c(c, txt('?', 100, 0), x, y, s)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 100)))
    k = kick(f, g0 + 4, .8)
    return c, (640, 950 + k * 10, z, k + lerp(0, 2, smooth(ramp(f, g0, g0 + 20)))), 'dusk'


def s5(f):
    # futuro: estrutura enorme com vários robôs, câmera abre
    c = orbita_bg(0).copy()
    estrelas(c, f, 9, 40, 700)
    c0 = wt(5, 'centenas') - 3
    k0 = wt(5, 'quilometros') - 3
    nb = 2 + int(9 * ramp(f, 0, k0 + 10))
    treliça(c, -60, 900, 150, 180, nb, ramp(f, 0, k0 + 10) * 9 % 1, 1.0 if True else 0, 7)
    treliça(c, -60, 1120, 150, 180, max(1, nb - 2), 0, 1.0, 7)
    for i, x in enumerate((260, 620, 980)):
        if f >= i * 12:
            s = back(ramp(f, i * 12, i * 12 + 8))
            put_astra(c, x, 900 - 80 + 10 * math.sin(f * .1 + i), 230 * s + 1, look=1, blink=blinkAt(f, 4 + i),
                      expr='proud', slide=.5 + .5 * math.sin(f * .2 + i), grip=.5 + .5 * math.sin(f * .3 + i))
    num(c, 'CENTENAS DE METROS', 640, 420, f, c0, 90, -3)
    num(c, 'ATÉ QUILÔMETROS!', 640, 1380, f, k0, 110, 3)
    z = lerp(1.35, .98, smooth(ramp(f, 0, k0 + 20)))
    return c, (640, 1000, z, lerp(-2, 1, smooth(ramp(f, 0, k0 + 20)))), 'dusk'


def s6(f):
    # fim: ASTRA com o módulo e a malha, Terra ao fundo; 1,4 m; dezembro; tijolo
    c = orbita_bg(0).copy()
    estrelas(c, f, 3, 50, 800)
    um0 = wt(6, 'um') - 3
    de0 = wt(6, 'dezembro') - 3
    ti0 = wt(6, 'tijolo') - 3
    treliça(c, 780, 980, 190, 240, 2, ramp(f, ti0 - 6, ti0 + 6), 1.0, 9)
    put_astra(c, 520, 1220, 560, look=1 if f < ti0 else -.3, blink=blinkAt(f, 8),
              expr='proud' if f >= ti0 else 'calm', slide=.5 + .3 * math.sin(f * .1), grip=.3)
    if f >= um0:
        d = ImageDraw.Draw(c)
        s = back(ramp(f, um0, um0 + 8))
        y = 800; x0, x1 = 780, 780 + 380 * s
        d.line([(x0, y), (x1, y)], fill=INK, width=16); d.line([(x0, y), (x1, y)], fill=WHITE, width=8)
        paste_c(c, txt('1,4 M', 110, -3), 970, 700, s)
    num(c, 'DEZEMBRO', 640, 420, f, de0, 110, 3)
    num(c, '1º TIJOLO!', 640, 1360, f, ti0, 130, -4)
    z = lerp(1.05, 1.25, smooth(ramp(f, 0, 160)))
    return c, (680, lerp(980, 1020, smooth(ramp(f, 0, 160))), z, 0), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'primeira') - 3, 140, .9)
    s.ting(s.W(0, 'montou') + 3, .3)
    s.ting(s.W(1, 'astra') - 3, .3)
    s.engine(s.W(1, 'subiu') - 6, s.W(1, 'subiu') + 60, .3)
    s.thunk(s.W(1, 'caixa') - 3, 180, .7)
    for w in ('tres', 'varetas', 'modulo'): s.ting(s.W(2, w) - 3, .25)
    s.whoosh(s.W(2, 'malha') - 3, .3, .4)
    s.thunk(s.W(3, 'sete') - 3, 160, .6)
    s.ting(s.W(3, 'quinze') - 3, .3)
    s.thunk(s.W(4, 'gigante') + 4, 140, .9)
    s.thunk(s.W(5, 'centenas') - 3, 160, .7)
    s.whoosh(s.W(5, 'quilometros') - 3, .4, .5)
    s.thunk(s.W(6, 'dezembro') - 3, 180, .6)
    s.ting(s.W(6, 'tijolo') - 3, .4)
