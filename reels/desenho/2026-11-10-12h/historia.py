"""Um Café com o Mundo — CURIOSIDADE (terça 10/11/2026, 12h).
Tema: as sondas gêmeas ESCAPADE, da NASA, passam rente à Terra e usam o planeta como estilingue rumo a Marte.
Fontes (conferidas em 10/11/2026):
- NASA Science, 09/11/2026 "NASA's ESCAPADE Completes Powered Earth Flybys, Now En Route to Mars": lançadas em
  13/11/2025 de Cabo Canaveral quando Terra e Marte estavam em lados opostos do Sol; órbita de espera ("loiter")
  a cerca de 1 milhão de milhas (~1,6 milhão de km) da Terra, em torno do ponto L2; 1ª sonda: sábado 07/11, ~1.000
  milhas (~1.600 km) de altitude, queima de ~9 min; 2ª sonda: segunda 09/11, ~650 milhas (~1.050 km), ~9 min;
  "primeira vez que a NASA usa um sobrevoo motorizado da Terra para mandar uma nave a Marte"; chegada/inserção em
  órbita 07 e 09/09/2027; ~10 meses de viagem; 1ª missão científica com dois orbitadores coreografados em Marte;
  objetivo: como o vento solar interage com Marte e provoca a perda da atmosfera. Jeff Parker (Advanced Space):
  o método permite lançar "quase a qualquer momento".
- NASA Science (blog ESCAPADE), 02/11/2026: missões anteriores a Marte partiam nos alinhamentos, que ocorrem a cada
  26 meses; queima leva a velocidade de ~6,3 para ~6,7 milhas/s.
- UC Berkeley News, 09/11/2026 "Berkeley's ESCAPADE spacecraft say goodbye to Earth. Next stop: Mars."
Sem logotipos; sondas, foguete e planetas genéricos."""
from kit import *
import kit

VOZ = 'pt-BR-FranciscaNeural'; RATE = '+10%'
ARROBA = 'UM CAFÉ COM O MUNDO'
SELO = 'CURIOSIDADE  ·  UM CAFÉ COM O MUNDO'

LINES = [
    "Duas sondas da NASA acabam de usar a Terra como estilingue pra ir até Marte.",
    "Elas foram lançadas há quase um ano, mas Marte estava do outro lado do Sol.",
    "Então ficaram dando voltas a mais de um milhão de quilômetros daqui, esperando.",
    "No sábado e nesta segunda, cada uma passou a menos de dois mil quilômetros da Terra e ligou o motor por nove minutos.",
    "Mas por que isso importa? Antes, as naves só partiam pra Marte quando os planetas se alinhavam, a cada vinte e seis meses.",
    "Com esse truque, inédito na NASA, dá pra lançar quase a qualquer hora.",
    "As gêmeas chegam em setembro do ano que vem, pra estudar como o vento do Sol arranca o ar de Marte.",
]
CAPTXT = [
    "Duas sondas da NASA acabam de usar a Terra|como estilingue pra ir até Marte.",
    "Elas foram lançadas há quase um ano,|mas Marte estava do outro lado do Sol.",
    "Então ficaram dando voltas a mais de 1 milhão|de quilômetros daqui, esperando.",
    "No sábado e nesta segunda, cada uma passou a menos de 2 mil km|da Terra e ligou o motor por 9 minutos.",
    "Mas por que isso importa? Antes, as naves só partiam pra Marte|quando os planetas se alinhavam, a cada 26 meses.",
    "Com esse truque, inédito na NASA,|dá pra lançar quase a qualquer hora.",
    "As gêmeas chegam em setembro do ano que vem, pra estudar|como o vento do Sol arranca o ar de Marte.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta aqui, e segue o Um Café com o Mundo pra entender o mundo em um minuto!"
CTA_TEXTO = "COMENTA AQUI!"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'estilingue', 4), (1, 'sol', 4), (2, 'milhao', 4), (3, 'dois', 4), (3, 'nove', 4),
         (4, 'vinte', 4), (5, 'inedito', 4), (6, 'setembro', 4), (6, 'marte', 6)]

WHITE = (255, 255, 255)
GOLD = hexc('#e8b440'); GOLD_D = hexc('#b8862a')
BLUE = hexc('#4f8fe0'); BLUE_D = hexc('#2f63a8')
PANEL = hexc('#2b3f7a'); PANEL_D = hexc('#1c2a55')
RED = hexc('#d8443c')
MARS = hexc('#d9653a'); MARS_D = hexc('#a8452a')
SUN = hexc('#f7c948'); SUN_D = hexc('#e09a2a')


# ------------------------------------------------------------------ desenhos novos
def sonda(cor='gold', look=1.0, blink=0, expr='calm', fire=0.0):
    """sonda genérica de lado, olhando para a direita: corpo-caixa com olho grande, 2 painéis solares, bocal atrás.
    800x480, centro em (400, 240)."""
    p = Pen(800, 480)
    C, CD = (GOLD, GOLD_D) if cor == 'gold' else (BLUE, BLUE_D)
    # chama do motor (à esquerda)
    if fire > 0:
        for i, (col, s) in enumerate(((hexc('#f7d046'), 1.0), (hexc('#f08a2c'), .7), (hexc('#fff3c0'), .4))):
            L = 230 * fire * s
            p.poly([(270, 240 - 50 * s), (270, 240 + 50 * s), (270 - L * .6, 240 + 22 * s), (270 - L, 240), (270 - L * .6, 240 - 22 * s)], col, 0 if i else 4)
    # bocal
    p.shape([(300, 200), (300, 280), (255, 300), (255, 180)], hexc('#8a8f99'), hexc('#6b6b70'), 5, 6)
    # painéis solares (cima e baixo)
    for s in (-1, 1):
        y0, y1 = (240 + s * 120, 240 + s * 225)
        p.line([(400, 240 + s * 95), (400, y0)], hexc('#8a8f99'), 14, 4)
        p.shape([(300, min(y0, y1)), (500, min(y0, y1)), (500, max(y0, y1)), (300, max(y0, y1))], PANEL, PANEL_D, 5, 8)
        for gx in (350, 400, 450): p.stroke([(gx, min(y0, y1) + 6), (gx, max(y0, y1) - 6)], 3, hexc('#6f88c8'))
        p.stroke([(306, (y0 + y1) / 2), (494, (y0 + y1) / 2)], 3, hexc('#6f88c8'))
    # corpo
    p.shape([(300, 140), (520, 140), (540, 160), (540, 330), (520, 345), (300, 345)], C, CD, 6, 16)
    # antena prato na frente
    p.line([(540, 200), (600, 180)], hexc('#6b6b70'), 8, 4)
    p.shape(ell_pts(612, 176, 22, 46, 30, .3), hexc('#f2f4f8'), hexc('#c9ced8'), 5, 6)
    # olho
    ex, ey, er = 440, 238, 64 if expr == 'shock' else 58
    p.dot(ex, ey, er, WHITE, 5)
    L = max(.45 if expr in ('proud', 'sleep') else 0, blink, .7 if expr == 'sleep' else 0)
    if L < .75:
        lk = max(-1, min(1, look))
        p.dot(ex + lk * (er - 24), ey + 4, 16 if expr == 'shock' else 22, INK)
        p.dot(ex + lk * (er - 24) - 6, ey - 4, 6, WHITE)
    if L > .02:
        top = ey - er; yb = top + 2 * er * L
        p.poly([(ex - er - 1, top - 2), (ex + er + 1, top - 2), (ex + er + 1, yb), (ex - er - 1, yb)], C)
        p.stroke([(ex - er, yb), (ex + er, yb)], 5)
    if expr == 'shock': p.arc(ex, ey - 84, 30, 10, 200, 340, 5)
    if expr == 'proud': p.arc(ex, ey + 92, 24, 12, 20, 160, 5)
    return p.img


def put_sonda(c, x, y, w, rot=0, flip=False, **kw):
    if 'blink' in kw: kw['blink'] = 1 if kw['blink'] > .6 else 0
    if 'fire' in kw: kw['fire'] = round(kw['fire'] * 6) / 6
    if 'look' in kw: kw['look'] = round(kw['look'] * 4) / 4
    if w < 8: return
    im = sprite('sonda', tuple(sorted(kw.items())), int(w * 480 / 800), 800 / 480, flip)
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    paste_c(c, im, x, y)


def planeta(c, x, y, r, col, cold, ring=None):
    p = Pen(int(2 * r + 40), int(2 * r + 40))
    q = r + 20
    if ring: p.poly(ell_pts(q, q, r + 16, r + 16, 60), ring)
    p.shape(ell_pts(q, q, r, r, 60), col, cold, max(4, int(r / 25)), max(6, int(r / 8)))
    if col == hexc('#3a7fd0'):
        for lx, ly, rx, ry in ((-.35, -.2, .35, .22), (.3, .25, .3, .2), (.1, -.5, .2, .1)):
            p.shape(ell_pts(q + lx * r, q + ly * r, rx * r, ry * r, 30, .2), hexc('#7fb05a'), hexc('#5f8a40'), max(3, int(r / 40)), 4)
    if col == MARS:
        for lx, ly, rr in ((-.3, -.2, .14), (.35, .2, .1), (0, .45, .12), (.2, -.45, .08)):
            p.dot(q + lx * r, q + ly * r, rr * r, MARS_D)
        p.shape(ell_pts(q, q - r * .86, r * .32, r * .1, 30), WHITE, None, 0, 0)
    paste_c(c, p.img.resize((int(2 * r + 40), int(2 * r + 40)), Image.LANCZOS), x, y)


def sol(c, x, y, r, f):
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(12):
        a = i * math.pi / 6 + f * .01
        r1, r2 = r + 20, r + 60 + 10 * math.sin(f * .2 + i)
        d.line([(x + r1 * math.cos(a), y + r1 * math.sin(a)), (x + r2 * math.cos(a), y + r2 * math.sin(a))], fill=SUN + (255,), width=16)
    planeta(c, x, y, r, SUN, SUN_D, (255, 230, 140))


@lru_cache(maxsize=2)
def ceu_bg(seed=11):
    base = Image.new('RGBA', (BW, BH), hexc('#0e1436') + (255,))
    p = Pen(BW, BH)
    rnd = random.Random(seed)
    for i in range(200):
        p.dot(rnd.randint(0, BW), rnd.randint(0, BH), rnd.choice((2, 2, 3, 4)), (255, 255, 230))
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


@lru_cache(maxsize=2)
def terra_bg():
    """espaço com a Terra grande embaixo."""
    p = Pen(BW, BH)
    base = ceu_bg(7).copy()
    cx, cy, R = 621, 3300, 1650
    p.poly(ell_pts(cx, cy, R + 40, R + 40, 160), hexc('#7fc3ff'))
    p.shape(ell_pts(cx, cy, R, R, 160), hexc('#3a7fd0'), hexc('#2a5fa4'), 7, 40)
    for lx, ly, rx, ry in ((300, 1760, 260, 120), (880, 1820, 220, 150), (620, 2000, 300, 140)):
        p.shape(ell_pts(lx, ly, rx, ry, 40, .2), hexc('#7fb05a'), hexc('#5f8a40'), 5, 12)
    for wx, wy in ((150, 1900), (520, 1700), (1050, 1950)):
        p.shape(ell_pts(wx, wy, 120, 34, 30), WHITE, hexc('#dfe6ef'), 0, 6)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


def num(c, s, x, y, f, f0, size=170, rot=-4):
    if f >= f0: paste_c(c, txt(s, size, rot), x, y, back(ramp(f, f0, f0 + 8)))


def trilha(c, pts, upto, col=(255, 255, 255, 170), w=6):
    n = max(2, int(len(pts) * clamp(upto)))
    d = ImageDraw.Draw(c, 'RGBA')
    for i in range(0, n - 1, 2):
        d.line([pts[i], pts[i + 1]], fill=col, width=w)


def ang(a, b):
    return -math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))


# ------------------------------------------------------------------ cenas
def s0(f):
    # gancho: duas sondas passam rente à Terra (embaixo) e são arremessadas para Marte (no alto)
    c = terra_bg().copy()
    e0 = wt(0, 'estilingue') - 3
    m0 = wt(0, 'marte') - 3
    planeta(c, 1030, 300, 150, MARS, MARS_D)
    num(c, 'MARTE', 1030, 500, f, m0, 80, 3)
    # caminho: vem da esquerda alto, desce rente à Terra, sobe para a direita
    pts = [(lerp(-100, 1100, t), 1500 - 900 * (2 * t - 1) ** 2 * (1 if t < .5 else 1.15)) for t in [i / 80 for i in range(81)]]
    T = ramp(f, 0, m0 + 30)
    for k, (cor, dt) in enumerate((('gold', 0), ('blue', .1))):
        t = clamp(T - dt)
        i = min(79, int(t * 80))
        a, b = pts[i], pts[i + 1]
        trilha(c, pts, t)
        put_sonda(c, a[0], a[1] - 60 * k, 480, ang(a, b), cor=cor, look=1, blink=blinkAt(f, 3 + k),
                  expr='shock' if f >= e0 else 'calm', fire=1 if (f >= e0 and t > .45) else 0)
    num(c, 'ESTILINGUE!', 640, 560, f, e0, 150, -5)
    num(c, 'NASA', 260, 330, f, wt(0, 'nasa') - 3, 110, 4)
    z = lerp(1.25, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0005 * f)
    k = kick(f, e0)
    return c, (640 + 10 * math.sin(f * .05), 1050 + k * 10, z, k), 'day'


def s1(f):
    # Sol no meio, Terra de um lado, Marte do outro
    c = ceu_bg(3).copy()
    sol(c, 640, 1000, 120, f)
    a = f * .003
    ex, ey = 640 - 330 * math.cos(a), 1000 - 330 * math.sin(a)
    mx, my = 640 + 440 * math.cos(a * .6), 1000 + 440 * math.sin(a * .6)
    d = ImageDraw.Draw(c, 'RGBA')
    d.ellipse([640 - 330, 1000 - 330, 640 + 330, 1000 + 330], outline=(255, 255, 255, 70), width=4)
    d.ellipse([640 - 440, 1000 - 440, 640 + 440, 1000 + 440], outline=(255, 255, 255, 70), width=4)
    planeta(c, ex, ey, 90, hexc('#3a7fd0'), hexc('#2a5fa4'))
    planeta(c, mx, my, 75, MARS, MARS_D)
    l0 = wt(1, 'lancadas') - 3
    o0 = wt(1, 'outro') - 3
    if f >= l0:
        s = back(ramp(f, l0, l0 + 8))
        for k, cor in enumerate(('gold', 'blue')):
            put_sonda(c, ex - 60 + 120 * k, ey - 170 - 60 * k, 200 * s, 0, True, cor=cor, look=1, blink=blinkAt(f, 5 + k))
    num(c, 'NOV 2025', 640, 360, f, l0, 110, -3)
    num(c, 'TERRA', ex, ey + 130, f, 0, 56, 0)
    num(c, 'MARTE', mx, my + 115, f, 0, 56, 0)
    num(c, 'OUTRO LADO DO SOL!', 640, 1520, f, o0, 90, 3)
    z = lerp(.95, 1.08, smooth(ramp(f, 0, 120)))
    k = kick(f, o0, .6)
    return c, (640, 1000 + k * 8, z, k), 'day'


def s2(f):
    # dando voltas longe da Terra, esperando (feijão de órbita), sondas com sono
    c = ceu_bg(9).copy()
    planeta(c, 220, 1150, 190, hexc('#3a7fd0'), hexc('#2a5fa4'))
    cx, cy = 820, 1000
    pts = [(cx + 260 * math.cos(t) - 40 * math.cos(2 * t), cy + 380 * math.sin(t)) for t in [i / 60 * 2 * math.pi for i in range(61)]]
    trilha(c, pts, 1.0, (255, 255, 255, 120), 5)
    for k, cor in enumerate(('gold', 'blue')):
        t = (f * .02 + k * .25) * 2 * math.pi
        x, y = cx + 260 * math.cos(t) - 40 * math.cos(2 * t), cy + 380 * math.sin(t)
        put_sonda(c, x, y, 340, 0, math.sin(t) > 0, cor=cor, look=1, blink=blinkAt(f, 7 + k),
                  expr='sleep' if f >= wt(2, 'esperando') - 3 else 'calm')
    m0 = wt(2, 'milhao') - 3
    if f >= m0:
        d = ImageDraw.Draw(c)
        s = back(ramp(f, m0, m0 + 8))
        x1 = 360 + (520 - 360) * s
        d.line([(420, 1150), (x1 + 40, 1150)], fill=INK, width=14); d.line([(420, 1150), (x1 + 40, 1150)], fill=WHITE, width=6)
    num(c, '+1 MILHÃO DE KM', 640, 440, f, m0, 88, -3)
    e0 = wt(2, 'esperando') - 3
    if f >= e0: zzz(c, 900, 600, f - e0)
    num(c, 'ESPERANDO...', 640, 1450, f, e0, 100, 3)
    z = lerp(1.15, 1.0, smooth(ramp(f, 0, 120)))
    return c, (640 + 30 * math.sin(f * .03), 1000, z, lerp(-2, 1, smooth(ramp(f, 0, 140)))), 'golden'


def s3(f):
    # passagem rasante: sonda cruza perto da Terra e liga o motor; relógio 9 min
    c = terra_bg().copy()
    d0 = wt(3, 'dois') - 3
    m0 = wt(3, 'motor') - 3
    n0 = wt(3, 'nove') - 3
    t = ramp(f, 0, n0 + 60)
    x = lerp(-150, 1350, t)
    y = 1300 - 120 * math.sin(t * math.pi)
    put_sonda(c, x, y, 600, lerp(-8, 14, t), cor='gold', look=1, blink=blinkAt(f, 2),
              expr='proud' if f >= m0 else 'calm', fire=(.7 + .3 * math.sin(f * .9)) if f >= m0 else 0)
    num(c, 'SÁBADO E SEGUNDA', 640, 360, f, wt(3, 'sabado') - 3, 90, -3)
    num(c, '< 2.000 KM', 640, 560, f, d0, 140, 4)
    if f >= n0:
        s = back(ramp(f, n0, n0 + 8))
        mm = min(9, int(9 * ramp(f, n0, n0 + 50)))
        paste_c(c, clock_img(12, mm * 6, 190), 470, 820, s)
        paste_c(c, txt('9 MIN', 110, -4), 760, 820, s)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, 140)))
    k = kick(f, m0, .7)
    return c, (lerp(560, 720, t), 1000 + k * 10, z, k), 'day'


def s4(f):
    # por que importa: planetas se alinhando, calendário 26 meses
    c = ceu_bg(5).copy()
    sol(c, 640, 950, 110, f)
    a0 = wt(4, 'alinhavam') - 3
    al = smooth(ramp(f, a0 - 20, a0 + 10))
    ae = math.pi + .3
    am = lerp(math.pi * .25, ae, al)
    ex, ey = 640 + 250 * math.cos(ae), 950 + 250 * math.sin(ae)
    mx, my = 640 + 430 * math.cos(am), 950 + 430 * math.sin(am)
    d = ImageDraw.Draw(c, 'RGBA')
    d.ellipse([640 - 250, 950 - 250, 640 + 250, 950 + 250], outline=(255, 255, 255, 60), width=4)
    d.ellipse([640 - 430, 950 - 430, 640 + 430, 950 + 430], outline=(255, 255, 255, 60), width=4)
    planeta(c, ex, ey, 75, hexc('#3a7fd0'), hexc('#2a5fa4'))
    planeta(c, mx, my, 65, MARS, MARS_D)
    if al > .95:
        d.line([(ex, ey), (mx, my)], fill=(255, 220, 120, 200), width=6)
    num(c, 'POR QUE IMPORTA?', 640, 330, f, 0, 100, -3)
    v0 = wt(4, 'vinte') - 3
    if f >= v0:
        s = back(ramp(f, v0, v0 + 8))
        q = Pen(300, 300)
        q.shape([(20, 50), (280, 50), (280, 280), (20, 280)], WHITE, hexc('#d6dbe4'), 6, 8)
        q.shape([(20, 50), (280, 50), (280, 110), (20, 110)], RED, mul(RED, .75), 6, 0)
        for gx in (80, 220): q.line([(gx, 20), (gx, 80)], INK, 14, 0)
        paste_c(c, q.img.resize((200, 200), Image.LANCZOS), 1010, 1480, s)
        paste_c(c, txt('26', 80, 0), 1010, 1505, s)
        paste_c(c, txt('A CADA 26 MESES', 90, 3), 640, 470, s)
    z = lerp(1.0, 1.08, smooth(ramp(f, 0, 140)))
    k = kick(f, v0, .6)
    return c, (640, 1000 + k * 8, z, k + lerp(0, 2, smooth(ramp(f, a0, a0 + 20)))), 'dusk'


def s5(f):
    # truque inédito: sonda orgulhosa, calendário girando, "quase a qualquer hora"
    c = terra_bg().copy()
    i0 = wt(5, 'inedito') - 3
    q0 = wt(5, 'qualquer') - 3
    put_sonda(c, 640, 1000 + 15 * math.sin(f * .1), 820, 3 * math.sin(f * .05), cor='blue', look=1 if f < i0 else -.5,
              blink=blinkAt(f, 4), expr='proud' if f >= i0 else 'calm', fire=.5 + .2 * math.sin(f * .8))
    num(c, 'TRUQUE', 640, 380, f, wt(5, 'truque') - 3, 120, -4)
    num(c, 'INÉDITO NA NASA!', 640, 560, f, i0, 92, 3)
    if f >= q0:
        s = back(ramp(f, q0, q0 + 8))
        paste_c(c, clock_img((f * .5) % 12, (f * 6) % 60, 180), 640, 1330, s)
        paste_c(c, txt('QUASE A QUALQUER HORA', 80, -3), 640, 1500, s)
    z = lerp(1.15, 1.02, smooth(ramp(f, 0, 100)))
    k = kick(f, i0, .7)
    return c, (640, 980 + k * 10, z, k), 'dusk'


def s6(f):
    # Marte com as duas gêmeas em órbita; vento do Sol arrancando o ar
    c = ceu_bg(13).copy()
    mx, my = 640, 1130
    v0 = wt(6, 'vento') - 3
    ar0 = wt(6, 'arranca') - 3
    d = ImageDraw.Draw(c, 'RGBA')
    if f >= v0:
        for i in range(14):
            yy = 600 + i * 60
            xx = ((f - v0) * 22 + i * 137) % 1500 - 300
            d.line([(xx, yy), (xx + 160, yy)], fill=(255, 220, 120, 190), width=6)
    # atmosfera (halo) que vai sendo soprada
    h = ramp(f, ar0, ar0 + 30)
    for i in range(8):
        a = i * math.pi / 4
        r = 360 + 25 * math.sin(f * .2 + i)
        px = mx + r * math.cos(a) + 140 * h * (1 + math.cos(a))
        py = my + r * math.sin(a)
        d.ellipse([px - 22, py - 22, px + 22, py + 22], fill=(200, 230, 255, int(90 * (1 - .6 * h))))
    planeta(c, mx, my, 330, MARS, MARS_D, (255, 210, 180))
    for k, cor in enumerate(('gold', 'blue')):
        t = f * .03 + k * math.pi
        x, y = mx + 450 * math.cos(t), my + 150 * math.sin(t)
        if True:
            put_sonda(c, x, y, 300, 0, math.sin(t) > 0, cor=cor, look=1, blink=blinkAt(f, 9 + k), expr='proud')
    num(c, 'SETEMBRO 2027', 640, 360, f, wt(6, 'setembro') - 3, 100, 3)
    num(c, 'VENTO DO SOL', 640, 520, f, v0, 90, -3)
    num(c, 'O AR DE MARTE', 640, 1460, f, ar0, 100, 4)
    z = lerp(1.0, 1.12, smooth(ramp(f, 0, 180)))
    return c, (640, lerp(960, 1000, smooth(ramp(f, 0, 180))), z, 0), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.whoosh(s.W(0, 'duas') - 3, .4, .5)
    s.thunk(s.W(0, 'estilingue') - 3, 140, .9)
    s.ting(s.W(1, 'lancadas') - 3, .3)
    s.thunk(s.W(1, 'outro') - 3, 160, .7)
    s.ting(s.W(2, 'milhao') - 3, .3)
    s.engine(s.W(3, 'motor') - 3, s.W(3, 'motor') + 60, .3)
    s.thunk(s.W(3, 'dois') - 3, 160, .6)
    s.ting(s.W(3, 'nove') - 3, .3)
    s.thunk(s.W(4, 'vinte') - 3, 160, .8)
    s.ting(s.W(5, 'inedito') - 3, .4)
    s.thunk(s.W(6, 'setembro') - 3, 180, .6)
    s.whoosh(s.W(6, 'vento') - 3, .4, .5)
