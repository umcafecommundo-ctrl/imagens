"""anima.futebol — 19/11/2026 21h — Brasileirão 35ª rodada: Gabigol nos acréscimos, VAR confirma e Santos vence o Coritiba fora.
Fontes (conferidas em 19/11/2026): Gazeta Esportiva (18/11 21h47), O Curioso do Futebol (18/11) e Sportbuzz (19/11):
Coritiba 0x1 Santos, quarta 18/11, 19h30, Couto Pereira, 35ª rodada. Gol de Gabigol nos acréscimos do 2º tempo (47'/48'/49'
divergem -> "nos acréscimos"), no rebote de chute de Neymar defendido por Pedro Rangel, jogada iniciada em contra-ataque de
Rollheiser; assistente marcou impedimento e o VAR confirmou o gol (as 3 fontes). Neymar teve chances no 2º tempo paradas pelo
goleiro (Gazeta e Curioso). Santos chega a 50 pontos (Gazeta; post de 18/11 19h: Santos tinha 47). Próximo: Santos x Grêmio,
segunda 23/11, 21h, Morumbis (Gazeta, Curioso e Sportbuzz). Confusões/provocações pós-jogo ficaram de fora (tom neutro).
Sem escudos/logos/taças reais: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'BRASILEIRÃO  ·  35ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "O bandeirinha marcou impedimento, mas o VAR deu o gol, e o Santos venceu no último lance.",
    "Foi ontem à noite, no Couto Pereira, contra o Coritiba.",
    "No segundo tempo, Neymar teve chances, mas parou no goleiro Pedro Rangel.",
    "Já nos acréscimos, Rollheiser puxou o contra-ataque e achou Neymar, que chutou.",
    "O goleiro defendeu, e Gabigol, no rebote, fez um a zero.",
    "A bandeira subiu, mas o VAR checou o lance e confirmou o gol.",
    "Com a vitória fora de casa, o Santos chegou a cinquenta pontos.",
    "E na segunda, às nove da noite, recebe o Grêmio no Morumbis.",
]
CAPTXT = [
    "O bandeirinha marcou impedimento, mas o VAR deu o gol,|e o Santos venceu no último lance.",
    "Foi ontem à noite, no Couto Pereira,|contra o Coritiba.",
    "No 2º tempo, Neymar teve chances,|mas parou no goleiro Pedro Rangel.",
    "Já nos acréscimos, Rollheiser puxou o contra-ataque|e achou Neymar, que chutou.",
    "O goleiro defendeu, e Gabigol,|no rebote, fez 1 a 0.",
    "A bandeira subiu, mas o VAR|checou o lance e confirmou o gol.",
    "Com a vitória fora de casa,|o Santos chegou a 50 pontos.",
    "E na segunda, às 21h,|recebe o Grêmio no Morumbis.",
]
FALA_TIKTOK = "Valeu o gol? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "VALEU O GOL?"
TWIST = 5
FLASH = [4]
CHECK = [(0, 'impedimento', 4), (0, 'VAR', 4), (0, 'ultimo', 4), (1, 'noite', 4), (1, 'Coritiba', 4), (2, 'Neymar', 4),
         (2, 'Rangel', 4), (3, 'acrescimos', 4), (3, 'Rollheiser', 4), (3, 'chutou', 4), (4, 'defendeu', 4), (4, 'Gabigol', 4),
         (4, 'zero', 4), (5, 'bandeira', 4), (5, 'confirmou', 4), (6, 'cinquenta', 4), (7, 'nove', 4), (7, 'Gremio', 4)]

SAN, SAN_F = time_('SANTOS')
CFC, CFC_F = time_('CORITIBA')
GRE, GRE_F = time_('GRÊMIO')
AUX = ('#f5c518', '#111111', '#111111')


def san(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=SAN, faixa=SAN_F, **kw)


def cfc(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#3a2a1e')
    put_atleta(c, x, y, h, f, seed, cores=CFC, faixa=CFC_F, **kw)


def bandeira(c, x, y, h, up, f):
    """bandeirinha do assistente (haste + pano quadriculado amarelo/vermelho). up 0..1 levanta."""
    L = h * .5; ang = math.radians(lerp(200, 280, up))
    x1, y1 = x + L * math.cos(ang) * .3, y + L * math.sin(ang)
    d = ImageDraw.Draw(c)
    d.line([(x, y), (x1, y1)], fill=INK + (255,), width=max(4, int(h * .012)))
    w = h * .16 * (1 + .06 * math.sin(f * .5)); hh = h * .11
    pts = [(x1, y1), (x1 + w, y1 + hh * .15), (x1 + w, y1 + hh * 1.15), (x1, y1 + hh)]
    d.polygon(pts, fill=(212, 40, 44, 255), outline=INK + (255,))
    d.polygon([(x1, y1), (x1 + w / 2, y1 + hh * .08), (x1 + w / 2, y1 + hh * .58), (x1, y1 + hh / 2)], fill=(245, 197, 24, 255))
    d.polygon([(x1 + w / 2, y1 + hh * .58), (x1 + w, y1 + hh * .65), (x1 + w, y1 + hh * 1.15), (x1 + w / 2, y1 + hh * 1.08)],
              fill=(245, 197, 24, 255))


def var_tela(c, x, y, f, f0, ok_f, ww=760, hh_=470):
    w, h = 760, 470
    """telão do VAR: 'VAR' checando e depois 'GOL CONFIRMADO'."""
    if f < f0: return
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, w - 6, h - 6], 40, fill=(20, 24, 46, 245), outline=INK + (255,), width=10)
    d.rounded_rectangle([24, 24, w - 24, h - 24], 30, outline=(120, 200, 255, 255), width=5)
    fo = ImageFont.truetype(FONTB, 170); t = 'VAR'; tw = d.textlength(t, font=fo)
    d.text(((w - tw) / 2, 50), t, font=fo, fill=(255, 255, 255, 255), stroke_width=6, stroke_fill=INK + (255,))
    fo2 = ImageFont.truetype(FONTB, 62)
    if f < ok_f:
        t2 = 'CHECANDO' + '.' * (1 + (f // 6) % 3); col = (120, 200, 255, 255)
    else:
        t2 = 'GOL CONFIRMADO'; col = (90, 230, 120, 255)
        d.rounded_rectangle([40, 280, w - 40, 420], 30, fill=(22, 92, 52, 255), outline=INK + (255,), width=6)
    tw = d.textlength(t2, font=fo2)
    d.text(((w - tw) / 2, 315), t2, font=fo2, fill=col if f < ok_f else (255, 255, 255, 255), stroke_width=4, stroke_fill=INK + (255,))
    paste_c(c, im, x, y, back(ramp(f, f0, f0 + 8)) * ww / 760)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('dusk').copy()
    im_ = wt(0, 'impedimento') - 3; va = wt(0, 'VAR') - 3; ul = wt(0, 'ultimo') - 3
    gx, gy = put_gol2(c, estufa=.6)
    put_goleiro(c, f, CFC, CFC_F, arms='shrug', expr='shock', skin=1)
    # assistente com a bandeira levantada (esquerda, ao fundo)
    put_atleta(c, 200, 1720, 420, f, 31, cores=AUX, faixa=None, skin=2, hs='careca', arms='hang', expr='stern', look=1)
    bandeira(c, 260, 1480, 420, ramp(f, im_, im_ + 6), f)
    num(c, 'IMPEDIMENTO?', 400, 1310, f, im_, 66, -4)
    var_tela(c, 800, 840, f, va, ul - 6, 600, 370)
    san(c, 760, 2040, 820, f, 3, arms='up' if f >= ul else 'cintura', expr='grin' if f >= ul else 'nervous', look=-1, num_='9')
    if f >= ul: confete(c, 760, 1300, f, ul, 50, 500)
    z = lerp(1.28, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, va, .8)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio2('dusk').copy()
    no = wt(1, 'noite') - 3; cp = wt(1, 'Couto') - 3; co = wt(1, 'Coritiba') - 3
    if f >= no: paste_c(c, calendario('18', 'NOV'), 330, 1000, .62 * back(ramp(f, no, no + 8)))
    num(c, 'QUARTA, 19H30', 820, 760, f, no, 84, 3)
    num(c, 'COUTO PEREIRA', 640, 1430, f, cp, 96, -3)
    cfc(c, 260, 2120, 560, f, 4, arms='cintura', expr='stern', look=1)
    san(c, 1000, 2120, 560, f, 8, arms='cintura', expr='stern', look=-1, flip=True)
    put_placa(c, 'CORITIBA', CFC, 260, 1600, f, co, 40, -3)
    put_placa(c, 'SANTOS', SAN, 1000, 1600, f, co + 4, 40, 3)
    num(c, 'x', 640, 1820, f, co + 4, 120, 0)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 20 * math.sin(f * .03), 1360, z, 0), 'dusk'


def s2(f):
    c = estadio2('dusk').copy()
    ne = wt(2, 'Neymar') - 3; pa = wt(2, 'parou') - 3; ra = wt(2, 'Rangel') - 3
    gx, gy = put_gol2(c)
    put_goleiro(c, f, CFC, CFC_F, arms='up' if f >= pa else 'hang', expr='grin' if f >= pa else 'stern', skin=1)
    sx = lerp(300, 480, easeOut(ramp(f, 0, ne)))
    if f < ne: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    san(c, sx, 2010, 860, f, 5, num_='10', hs='topete', arms='run' if f < pa + 6 else 'cheek',
        run=(f * .1) % 1 if f < ne else None, kick=pulse(f, ne + 4, 5), expr='pained' if f >= pa + 6 else 'stern')
    rb = raio_bola(860)
    k0 = ne + 6
    if f < pa + 2:
        bola_voo(c, f, k0, sx + 860 * .13, 2010 - rb, gx + 30, gy - 10, rb, raio_bola(300), 140, max(6, pa - k0))
    else:
        put_bola(c, gx - 70 + (f - pa) * 3, gy + 60, raio_bola(300), f)
    put_placa(c, 'NEYMAR', SAN, 480, 880, f, ne, 56, -3)
    put_placa(c, 'PEDRO RANGEL', CFC, 640, 720, f, ra, 44, 3)
    num(c, 'DEFENDEU!', 760, 1060, f, pa, 90, 4)
    k = kick(f, pa, .7)
    return c, (lerp(600, 680, smooth(f / 150)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s3(f):
    c = estadio2('dusk').copy()
    ac = wt(3, 'acrescimos') - 3; ro = wt(3, 'Rollheiser') - 3; ac2 = wt(3, 'achou') - 3; ch = wt(3, 'chutou') - 3
    num(c, 'ACRÉSCIMOS', 640, 720, f, ac, 110, -3)
    # Rollheiser corre e passa (esquerda -> direita)
    rx = lerp(-200, 420, easeOut(ramp(f, ro - 14, ac2)))
    if f < ac2: linhas_vel(c, rx, 2030, 820, f, dir=-1)
    san(c, rx, 2030, 820, f, 6, num_='11', skin=1, hair='#3a2a1e', hs='cacheado', run=(f * .1) % 1 if f < ac2 else None,
        arms='run' if f < ac2 else 'point', kick=pulse(f, ac2 - 2, 5), expr='stern')
    put_placa(c, 'ROLLHEISER', SAN, 420, 980, f, ro, 46, -3)
    # Neymar recebe à direita, mais ao fundo
    san(c, 930, 1840, 560, f, 5, num_='10', hs='topete', flip=True, arms='run', kick=pulse(f, ch, 5), expr='stern', look=-1)
    put_placa(c, 'NEYMAR', SAN, 930, 1180, f, ac2, 40, 3)
    rb = raio_bola(820)
    if f < ac2: put_bola(c, rx + 120, 2030 - rb, rb, f)
    else:
        t = ramp(f, ac2, ac2 + 8)
        put_bola(c, lerp(rx + 120, 900, t), lerp(2030 - rb, 1840 - raio_bola(560), t) - 60 * math.sin(t * math.pi),
                 lerp(rb, raio_bola(560), t), f)
    if f >= ch: num(c, 'CHUTE!', 900, 1420, f, ch, 90, 4)
    k = kick(f, ch, .7)
    return c, (lerp(560, 700, smooth(f / 120)), 1420 + k * 8, 1.08 * (1 + .0005 * f), k), 'dusk'


def s4(f):
    c = estadio2('dusk').copy()
    de = wt(4, 'defendeu') - 3; ga = wt(4, 'Gabigol') - 3; re = wt(4, 'rebote') - 3; ze = wt(4, 'zero') - 3
    gx, gy = put_gol2(c, estufa=ramp(f, re + 8, re + 14))
    put_goleiro(c, f, CFC, CFC_F, arms='up' if f < re else 'shrug', expr='stern' if f < re else 'shock', skin=1)
    sx = lerp(300, 470, easeOut(ramp(f, ga - 10, re - 4)))
    if ga - 10 <= f < re - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    san(c, sx, 2010, 860, f, 9, num_='9', skin=3, hs='raspado', arms='up' if f >= re + 10 else 'run',
        run=(f * .1) % 1 if ga - 10 <= f < re - 4 else None, kick=pulse(f, re - 3, 5), expr='grin' if f >= re + 6 else 'stern')
    rb = raio_bola(860)
    if f < re - 3:
        # bola rebatida pelo goleiro vindo do fundo até o pé do Gabigol
        t = ramp(f, de, re - 3)
        put_bola(c, lerp(gx - 40, sx + 860 * .13, t), lerp(gy + 40, 2010 - rb, t) - 80 * math.sin(t * math.pi),
                 lerp(raio_bola(300), rb, t), f)
    elif f < re + 40:
        bola_voo(c, f, re, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 120)
    num(c, 'DEFENDEU...', 640, 720, f, de, 90, -3)
    put_placa(c, 'GABIGOL', SAN, 360, 900, f, ga, 60, -4)
    if f >= re + 8: explosao(c, 760, 1100, f, re + 8, 170)
    num(c, 'GOL!', 760, 1100, f, re + 8, 130, 3)
    num(c, 'CFC 0 x 1 SAN', 640, 1290, f, ze, 80, -2)
    if f >= re + 10: confete(c, 500, 1400, f, re + 10, 40, 400)
    k = kick(f, re, .9)
    return c, (640, 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s5(f):
    c = estadio2('dusk').copy()
    ba = wt(5, 'bandeira') - 3; ch = wt(5, 'checou') - 3; co = wt(5, 'confirmou') - 3
    put_atleta(c, 260, 2060, 760, f, 31, cores=AUX, faixa=None, skin=2, hs='careca', arms='hang', expr='stern', look=1)
    bandeira(c, 360, 1640, 760, ramp(f, ba, ba + 6) * (1 - ramp(f, co, co + 8)), f)
    num(c, 'IMPEDIMENTO?', 440, 1240, f, ba, 70, -4)
    var_tela(c, 820, 880, f, ch, co, 600, 370)
    san(c, 900, 2060, 700, f, 9, num_='9', skin=3, hs='raspado', flip=True, look=-1,
        arms='up' if f >= co else 'cheek', expr='grin' if f >= co else 'nervous')
    if f >= co: confete(c, 820, 1300, f, co, 50, 500)
    z = lerp(1.0, 1.1, smooth(ramp(f, 0, co + 20)))
    k = kick(f, co, .8)
    return c, (640, 1400 + k * 8, z, lerp(0, 2, smooth(ramp(f, ba, ch)))), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    fo = wt(6, 'fora') - 3; ci = wt(6, 'cinquenta') - 3
    san(c, 640, 2060, 820, f, 3, num_='9', skin=3, hs='raspado', arms='joinha' if f >= ci else 'cintura', expr='proud', look=0)
    put_placa(c, 'SANTOS', SAN, 640, 1190, f, 0, 50, -3)
    num(c, 'VITÓRIA FORA', 640, 740, f, fo, 100, -3)
    if f >= ci: explosao(c, 640, 920, f, ci, 150)
    num(c, '50 PONTOS', 640, 920, f, ci, 120, 3)
    z = lerp(1.15, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, ci, .6)
    return c, (640, 1380 + k * 8, z, k), 'dusk'


def s7(f):
    c = estadio2('day').copy()
    se = wt(7, 'segunda') - 3; no = wt(7, 'nove') - 3; gr = wt(7, 'Gremio') - 3; mo = wt(7, 'Morumbis') - 3
    sx = lerp(-260, 360, easeOut(ramp(f, 0, 22)))
    gx_ = lerp(1500, 900, easeOut(ramp(f, 0, 22)))
    if f < 22:
        linhas_vel(c, sx, 2010, 860, f, dir=-1); linhas_vel(c, gx_, 2010, 860, f, dir=1)
    san(c, sx, 2010, 860, f, 3, num_='10', hs='topete', arms='cintura', expr='stern', look=1,
        run=(f * .1) % 1 if f < 22 else None)
    put_atleta(c, gx_, 2010, 860, f, 7, cores=GRE, faixa=GRE_F, skin=1, hs='curto', hair='#3a2a1e', arms='cintura',
               expr='stern', look=-1, flip=True, num_='9', run=(f * .1) % 1 if f < 22 else None)
    put_placa(c, 'SANTOS', SAN, 360, 1110, f, gr + 4, 54, -3)
    put_placa(c, 'GRÊMIO', GRE, 900, 1110, f, gr + 4, 54, 3)
    if f >= se: paste_c(c, calendario('23', 'NOV'), 380, 820, .48 * back(ramp(f, se, se + 8)))
    num(c, '21H', 900, 800, f, no, 150, 4)
    num(c, 'MORUMBIS', 640, 965, f, mo, 84, -2)
    z = lerp(1.2, 1.03, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, gr, .6)
    return c, (640, 1400 + k * 8, z, k), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def OVERLAY(im, si, lf):
    D = {0: ('SANTOS VENCE NO ÚLTIMO LANCE', 'GOL CONFIRMADO PELO VAR', wt(0, 'ultimo') + 4),
         1: ('CORITIBA x SANTOS', 'QUARTA, 18/11, 35ª RODADA', wt(1, 'Coritiba') + 6),
         2: ('NEYMAR PARA NO GOLEIRO', '2º TEMPO NO COUTO PEREIRA', wt(2, 'Rangel') + 4),
         3: ('CONTRA-ATAQUE NOS ACRÉSCIMOS', 'ROLLHEISER ACHA NEYMAR', wt(3, 'chutou') + 4),
         4: ('CORITIBA 0 x 1 SANTOS', 'GABIGOL NO REBOTE', wt(4, 'zero') + 4),
         5: ('VAR CONFIRMA O GOL', 'IMPEDIMENTO MARCADO E ANULADO', wt(5, 'confirmou') + 6),
         6: ('SANTOS CHEGA A 50 PONTOS', 'VITÓRIA FORA DE CASA', wt(6, 'pontos') + 2),
         7: ('', '', 4)}
    if si == 7: return im
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.thunk(s.W(0, 'impedimento') - 3, 180, .6)
    s.ting(s.W(0, 'VAR') - 3, .3)
    s.thunk(s.W(0, 'ultimo') - 3, 140, .9)
    s.thunk(s.W(1, 'noite') - 3, 160, .6)
    s.thunk(s.W(2, 'parou') - 3, 130, .8)
    s.whoosh(s.W(3, 'Rollheiser') - 3, .4)
    s.thunk(s.W(3, 'chutou') - 3, 130, .8)
    s.thunk(s.W(4, 'rebote') - 3, 120, 1.0)
    s.ting(s.W(4, 'zero') - 3, .3)
    s.thunk(s.W(5, 'bandeira') - 3, 180, .5)
    s.ting(s.W(5, 'confirmou') - 3, .35)
    s.thunk(s.W(6, 'cinquenta') - 3, 150, .8)
    s.thunk(s.W(7, 'Gremio') - 3, 140, .8)
