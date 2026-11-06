"""Formato DESENHO: por que o pneu é preto (os primeiros eram brancos) (Curiosidades da IA, 06/11/2026, 20h).
Categoria: INVENÇÕES E OBJETOS.
Fatos: Mental Floss, "The reason why car tires are black" (a borracha natural é clara; os primeiros pneus, como os dos
carros do começo do século 20, eram brancos, com óxido de zinco para reforçar; a fabricante Michelin disse que a troca
para o negro de fumo (carbon black) veio 'por volta de 1917'; o negro de fumo dá durabilidade, protege dos raios UV que
racham a borracha e melhora a aderência; pneus sem ele duravam cerca de 5.000 milhas (~8.000 km), com ele '50.000 milhas
ou mais' (~80.000 km)); Bridgestone Índia, "Why is the colour of a tyre black" (pneus antigos brancos por causa do óxido
de zinco; negro de fumo aumenta resistência ao desgaste e ao calor)."""
from kit import *
import kit

LINES = [
    "Os primeiros pneus de carro eram brancos.",
    "A borracha natural é clarinha, e os fabricantes ainda misturavam um pó branco pra deixar ela mais forte.",
    "Só que esse pneu branco durava pouco: cerca de oito mil quilômetros.",
    "Lá por mil novecentos e dezessete, começaram a misturar negro de fumo: um pó preto feito de carbono.",
    "O pneu preto aguenta o sol, gruda melhor no chão e pode rodar oitenta mil quilômetros ou mais.",
    "Você vê, o preto não é enfeite: é o carbono que deixa o pneu forte.",
    "Ou seja: o pneu branco era mais bonito... mas o preto foi mais longe.",
]
CAPTXT = [
    "Os primeiros pneus de carro eram brancos.",
    "A borracha natural é clarinha, e os fabricantes ainda misturavam|um pó branco pra deixar ela mais forte.",
    "Só que esse pneu branco durava pouco:|cerca de 8 mil quilômetros.",
    "Lá por 1917, começaram a misturar negro de fumo:|um pó preto feito de carbono.",
    "O pneu preto aguenta o sol, gruda melhor no chão|e pode rodar 80 mil quilômetros ou mais.",
    "Você vê, o preto não é enfeite:|é o carbono que deixa o pneu forte.",
    "Ou seja: o pneu branco era mais bonito...|mas o preto foi mais longe.",
]
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [3]
CHECK = [(0, 'brancos', 4), (1, 'po', 4), (2, 'pouco', 4), (2, 'oito', 6), (3, 'dezessete', 4), (3, 'preto', 6), (4, 'sol', 4),
         (4, 'oitenta', 6), (5, 'carbono', 4), (6, 'longe', 8)]

BR, BRD = hexc('#f2efe6'), hexc('#cfc9b8')
PR, PRD = hexc('#2f2b30'), hexc('#1a171b')


def pneu(black=False, expr='calm', blink=0, rot=0.0, flat=0.0, look=0.5):
    """pneu de lado com carinha no meio (400x400)."""
    p = Pen(400, 400)
    col, dk = (PR, PRD) if black else (BR, BRD)
    ry = 170 * (1 - .25 * flat)
    cy = 200 + 170 * .25 * flat
    p.shape(ell_pts(200, cy, 175 + 20 * flat, ry, 64), col, dk, 7, 22)
    for i in range(16):
        a = rot + i * math.pi / 8
        x0, y0 = 200 + 150 * math.cos(a), cy + ry / 170 * 150 * math.sin(a)
        x1, y1 = 200 + 172 * math.cos(a), cy + ry / 170 * 172 * math.sin(a)
        p.stroke([(x0, y0), (x1, y1)], 6, (90, 86, 92) if black else (190, 184, 170))
    p.shape(ell_pts(200, cy, 92, 92 * (1 - .25 * flat), 48), hexc('#c9ced8'), hexc('#9aa1ad'), 5, 8)
    for dx in (-30, 30):
        ex, ey = 200 + dx, cy - 10
        if blink > .6: p.stroke([(ex - 14, ey), (ex + 14, ey)], 6)
        elif expr == 'dizzy': p.dot(ex, ey, 18, (255, 255, 255), 4); p.arc(ex, ey, 9, 9, 0, 300, 4)
        else:
            r = 22 if expr == 'shock' else 18
            p.dot(ex, ey, r, (255, 255, 255), 4); p.dot(ex + look * 6, ey + 2, 8, INK)
            if expr == 'smug': p.poly([(ex - r - 2, ey - r - 3), (ex + r + 2, ey - r - 3), (ex + r + 2, ey - 4), (ex - r - 2, ey - 4)], hexc('#c9ced8')); p.stroke([(ex - r, ey - 4), (ex + r, ey - 4)], 5)
    if expr in ('grin', 'smug'): p.arc(200, cy + 26, 26, 14, 20, 160, 6)
    elif expr in ('shock', 'dizzy'): p.dot(200, cy + 34, 12, hexc('#7a2e2e'), 4)
    elif expr == 'sad': p.arc(200, cy + 40, 22, 12, 200, 340, 6)
    else: p.arc(200, cy + 26, 18, 10, 20, 160, 6)
    return p.img


def put_pneu(c, x, y, size, f, seed=1, **kw):
    kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    if 'rot' in kw: kw['rot'] = round((kw['rot'] % (math.pi / 8)) * 24) / 24
    if 'flat' in kw: kw['flat'] = round(kw['flat'] * 6) / 6
    im = sprite('pneu', tuple(sorted(kw.items())), int(size), 1.0, False)
    paste_c(c, im, x, y)


@lru_cache(maxsize=2)
def carro_img():
    """carro antigo de lado, sem rodas (900x520); rodas em x≈220 e 690, y≈430."""
    p = Pen(900, 520)
    G, Gd = hexc('#2f5f8f'), hexc('#1f4266')
    p.shape([(80, 300), (820, 300), (840, 420), (60, 420)], G, Gd, 6, 12)
    p.shape([(300, 120), (600, 120), (620, 300), (290, 300)], G, Gd, 6, 12)
    p.poly([(330, 150), (440, 150), (440, 280), (320, 280)], hexc('#bfe0f0'), 4)
    p.poly([(470, 150), (580, 150), (595, 280), (470, 280)], hexc('#bfe0f0'), 4)
    p.shape([(270, 110), (630, 110), (630, 128), (270, 128)], hexc('#1b1b1b'), None, 4)
    p.dot(840, 330, 22, hexc('#fff3b0'), 4)
    for x0 in (120, 590):
        p.shape([(x0, 380), (x0 + 200, 380), (x0 + 220, 420), (x0 - 20, 420)], Gd, None, 4)
    return p.img.resize((900, 520), Image.LANCZOS)


def carro(c, x, ground, f, black=False, speed=1.0, w=900, expr='grin'):
    s = w / 900
    im = carro_img() if s == 1 else carro_img().resize((int(900 * s), int(520 * s)), Image.LANCZOS)
    bob = 4 * math.sin(f * .6) * s
    c.alpha_composite(im, (int(x - im.size[0] / 2), int(ground - 470 * s + bob - 40 * s)))
    for wx in (220, 690):
        put_pneu(c, x - im.size[0] / 2 + wx * s, ground - 85 * s, 190 * s, f, int(wx), black=black, rot=f * .3 * speed, expr=expr, look=1)


@lru_cache(maxsize=2)
def estrada_bg(light='day'):
    c = BG(light).copy()
    p = Pen(BW, 600)
    p.shape([(-20, 80), (BW + 20, 80), (BW + 20, 600), (-20, 600)], hexc('#5b5b62'), hexc('#45454b'), 6, 10)
    for x in range(0, BW, 220): p.shape([(x, 330), (x + 120, 330), (x + 120, 350), (x, 350)], hexc('#f2d34a'), None, 0)
    c.alpha_composite(p.img.resize((BW, 600), Image.LANCZOS), (0, 1500))
    return c


def saco(c, x, y, black, s=1.0, pour=0.0, f=0):
    p = Pen(300, 360)
    col = hexc('#e9e3d3') if not black else hexc('#7a7068')
    p.shape([(60, 60), (240, 60), (270, 340), (30, 340)], col, mul(col, .8), 6, 14)
    p.stroke([(70, 70), (230, 70)], 8, mul(col, .6))
    paste_c(c, p.img.resize((300, 360), Image.LANCZOS).rotate(-60 * pour, Image.BICUBIC, expand=True), x, y, s)
    if pour > .5:
        rnd = random.Random(f)
        for i in range(30):
            px, py = x - 150 + rnd.random() * 60, y + 40 + rnd.random() * 300
            ImageDraw.Draw(c).ellipse([px - 7, py - 7, px + 7, py + 7], fill=(35, 32, 36, 255) if black else (250, 250, 245, 255), outline=INK + (255,))


def SFX(s):
    s.ting(s.W(0, 'brancos'), .3); s.engine(0, s.W(0, 'brancos') + 20, .15)
    s.whoosh(s.W(1, 'po') - 4, .5, .35)
    s.thunk(s.W(2, 'pouco') - 2, 120, .7); s.thunk(s.W(2, 'oito') - 2, 160, .6)
    s.ting(s.W(3, 'dezessete'), .3); s.whoosh(s.W(3, 'preto') - 4, .6, .4)
    s.engine(s.W(4, 'pneu'), s.W(4, 'oitenta') + 30, .18); s.ting(s.W(4, 'oitenta'), .35)
    s.thunk(s.W(5, 'carbono') - 2, 150, .6)
    s.whoosh(s.W(6, 'longe') - 6, .8, .5); s.trill(s.W(6, 'longe') + 4, .8, .25)


# ---------------------------------------------------------------- cenas
def s0(f):
    c = estrada_bg().copy()
    k = wt(0, 'brancos') - 3
    x = lerp(-300, 640, easeOut(ramp(f, 0, k)))
    carro(c, x, 1680, f, False, 1.0, 900, 'grin' if f < k else 'shock')
    if f >= k: paste_c(c, txt('PNEU BRANCO?!', 110, -5), 640, 900, back(ramp(f, k, k + 8)))
    kk = kick(f, k + 2)
    return c, (640, 1250 + kk * 10, lerp(1.25, 1.1, smooth(f / 60)), kk), 'golden'


def s1(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    b0 = wt(1, 'borracha') - 3
    p0 = wt(1, 'po') - 3
    fo = wt(1, 'forte') - 3
    put_pneu(c, 520, 1350, 560, f, 1, black=False, expr='calm' if f < fo else 'grin', rot=0, look=1)
    if f >= b0 and f < p0: paste_c(c, txt('CLARINHA', 110, -5), 640, 700, back(ramp(f, b0, b0 + 8)))
    if f >= p0 - 6:
        saco(c, 960, 900, False, 1.0, smooth(ramp(f, p0 - 6, p0 + 4)), f)
        if f < fo: paste_c(c, txt('PÓ BRANCO', 110, 5), 640, 700, back(ramp(f, p0, p0 + 8)))
    if f >= fo: paste_c(c, txt('MAIS FORTE!', 110, 5), 640, 700, back(ramp(f, fo, fo + 8)))
    z = lerp(1.08, 1.2, smooth(f / 150))
    return c, (640, 1200, z, 0), 'day'


def s2(f):
    c = estrada_bg().copy()
    pc = wt(2, 'pouco') - 3
    o0 = wt(2, 'oito') - 3
    fl = smooth(ramp(f, pc, pc + 14))
    put_pneu(c, 640 + 30 * math.sin(f * .1), 1500 + 90 * fl, 560, f, 2, black=False, expr='calm' if f < pc else 'dizzy', rot=f * .25 * (1 - fl), flat=fl, look=1)
    if f >= pc: paste_c(c, txt('PSSSS...', 100, 6), 900, 1150, back(ramp(f, pc, pc + 8)))
    if f >= o0: paste_c(c, txt('~8.000 km', 120, -5), 640, 760, back(ramp(f, o0, o0 + 8)))
    kk = kick(f, pc + 2)
    return c, (640, 1300 + kk * 10, 1.15, kk), 'day'


def s3(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(.8))
    a0 = wt(3, 'dezessete') - 3
    n0 = wt(3, 'negro') - 3
    p0 = wt(3, 'preto') - 3
    blk = f >= p0 + 6
    put_pneu(c, 520, 1380, 560, f, 3, black=blk, expr='shock' if (n0 <= f < p0 + 6) else ('grin' if blk else 'calm'), rot=0, look=1)
    if a0 <= f < n0: paste_c(c, txt('1917', 140, -5), 640, 700, back(ramp(f, a0, a0 + 8)))
    if f >= n0 - 6: saco(c, 960, 900, True, 1.0, smooth(ramp(f, n0 - 6, n0 + 4)), f)
    if f >= n0: paste_c(c, txt('NEGRO DE FUMO', 96, 5), 640, 800, back(ramp(f, n0, n0 + 8)))
    if p0 <= f < p0 + 8: put_dust(c, 520, 1380, 220, f - p0, 8)
    z = lerp(1.05, 1.15, smooth(f / 150))
    return c, (640, 1150, z, 0), 'golden'


def s4(f):
    c = estrada_bg().copy()
    s0_ = wt(4, 'sol') - 3
    g0 = wt(4, 'gruda') - 3
    o0 = wt(4, 'oitenta') - 3
    paste_c(c, _sol(), 1000, 380)
    put_pneu(c, 640, 1480, 560, f, 4, black=True, expr='grin' if f < o0 else 'smug', rot=f * .35, look=1)
    if s0_ <= f < g0: paste_c(c, txt('SOL? DE BOA!', 100, -5), 600, 760, back(ramp(f, s0_, s0_ + 8)))
    if g0 <= f < o0: paste_c(c, txt('GRUDA!', 120, 5), 600, 760, back(ramp(f, g0, g0 + 8)))
    if f >= o0: paste_c(c, txt('80.000 km!', 130, -5), 640, 760, back(ramp(f, o0, o0 + 8)))
    for i in range(3):
        a = (f + i * 9) % 27
        ImageDraw.Draw(c).line([(260 - a * 8, 1400 + i * 70), (360 - a * 8, 1400 + i * 70)], fill=INK + (int(255 * (1 - a / 27)),), width=10)
    kk = kick(f, o0 + 2)
    return c, (640, 1250 + kk * 10, 1.12, kk), 'day'


@lru_cache(maxsize=1)
def _sol():
    p = Pen(400, 400)
    for i in range(12):
        a = i * math.pi / 6
        p.line([(200 + 120 * math.cos(a), 200 + 120 * math.sin(a)), (200 + 175 * math.cos(a), 200 + 175 * math.sin(a))], hexc('#ffd84a'), 12, 4)
    p.shape(ell_pts(200, 200, 100, 100, 48), hexc('#ffe27a'), hexc('#f5b83a'), 6, 14)
    return p.img.resize((300, 300), Image.LANCZOS)


def s5(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(.5))
    e0 = wt(5, 'enfeite') - 3
    k0 = wt(5, 'carbono') - 3
    put_pneu(c, 640, 1350, 640, f, 5, black=True, expr='calm' if f < k0 else 'smug', rot=f * .05, look=0)
    if e0 <= f < k0: paste_c(c, txt('ENFEITE? NÃO!', 100, -5), 640, 760, back(ramp(f, e0, e0 + 8)))
    if f >= k0: paste_c(c, txt('CARBONO = FORÇA', 76, 4), 640, 760, back(ramp(f, k0, k0 + 8)))
    z = lerp(1.05, 1.22, smooth(f / 120))
    return c, (640, 1200, z, lerp(0, -2, smooth(f / 120))), 'dusk'


def s6(f):
    c = estrada_bg('golden').copy()
    b0 = wt(6, 'bonito') - 3
    l0 = wt(6, 'longe') - 6
    put_pneu(c, 330, 1600, 380, f, 6, black=False, expr='grin' if f < l0 else 'shock', rot=0, look=1)
    xb = 900 if f < l0 else 900 + (f - l0) ** 1.6 * 2
    if xb < 1600: put_pneu(c, xb, 1600, 380, f, 7, black=True, expr='smug', rot=f * .5 if f >= l0 else 0, look=1)
    if b0 <= f < l0: paste_c(c, txt('BONITO!', 100, -6), 460, 1200, back(ramp(f, b0, b0 + 8)))
    if f >= l0: paste_c(c, txt('FUI!', 140, 6), 900, 1150, back(ramp(f, l0, l0 + 8)))
    z = lerp(1.05, 1.2, easeOut(ramp(f, 0, 70)))
    return c, (620, 1350, z, lerp(0, 2, smooth(ramp(f, 0, 70)))), 'golden'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
