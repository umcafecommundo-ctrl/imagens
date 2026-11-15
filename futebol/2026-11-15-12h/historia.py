"""anima.futebol — 15/11/2026 12h — Copa do Brasil Feminina: final de volta hoje, Internacional x Flamengo no Beira-Rio.
Fontes (conferidas em 15/11/2026): O Tempo (14/11, onde assistir: volta dom 15/11 16h Beira-Rio; ida Inter 3 x 1 Flamengo
no Luso-Brasileiro; Inter campeão até perdendo por 1 gol; Fla precisa de 3 gols, 2 gols = pênaltis); Flashscore Brasil
(ida 11/11 Luso-Brasileiro, Flamengo 1 x 3 Internacional; volta 15/11 16h Beira-Rio; 1ª final do Inter; campeão R$ 1,1 milhão,
vice R$ 550 mil; torneio voltou em 2025 com Palmeiras campeão; Inter passou o Bragantino nos pênaltis 5 x 4 com defesa de
Gabi Barbieri); Jornal do Comércio (Inter supera o Bragantino nos pênaltis, Gabi Barbieri decisiva, vaga inédita na final);
Imirante (volta com mando do Inter; nenhum dos dois clubes ganhou o torneio: título inédito); site oficial do Inter (serviço
de jogo: Beira-Rio, 16h). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'COPA DO BRASIL FEMININA  ·  FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Hoje à tarde, a Copa do Brasil feminina vai ter um campeão inédito.",
    "Internacional e Flamengo decidem o título às quatro da tarde, no Beira-Rio, em Porto Alegre.",
    "Na ida, no Rio de Janeiro, o Inter venceu por três a um.",
    "Com essa vantagem, o Inter é campeão até se perder por um gol de diferença.",
    "O Flamengo precisa vencer por três gols, e uma vitória por dois leva a decisão para os pênaltis.",
    "O Inter chegou à primeira final da sua história nos pênaltis, com defesa da goleira Gabi Barbieri.",
    "E quem levantar a taça leva um milhão e cem mil reais de prêmio.",
]
CAPTXT = [
    "Hoje à tarde, a Copa do Brasil feminina|vai ter um campeão inédito.",
    "Internacional e Flamengo decidem o título às 16h,|no Beira-Rio, em Porto Alegre.",
    "Na ida, no Rio de Janeiro,|o Inter venceu por 3 a 1.",
    "Com essa vantagem, o Inter é campeão|até se perder por 1 gol de diferença.",
    "O Flamengo precisa vencer por 3 gols, e uma vitória|por 2 leva a decisão para os pênaltis.",
    "O Inter chegou à primeira final da sua história|nos pênaltis, com defesa da goleira Gabi Barbieri.",
    "E quem levantar a taça leva|R$ 1,1 milhão de prêmio.",
]
FALA_TIKTOK = "Quem fica com a taça, Inter ou Flamengo? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "QUEM LEVA?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'inedito', 4), (1, 'Beira-Rio', 4), (2, 'tres', 8), (3, 'perder', 4), (4, 'penaltis', 4),
         (5, 'defesa', 6), (6, 'milhao', 4)]

INT, INT_F = time_('INTERNACIONAL')
FLA, FLA_F = time_('FLAMENGO')
BRG, BRG_F = time_('BRAGANTINO')
GKI = ('#2b2b2b', '#f2c94c', '#2b2b2b')
GKF = ('#2fa35a', '#111111', '#111111')


def inter(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'rabo'); kw.setdefault('hair', '#3a2414')
    put_atleta(c, x, y, h, f, seed, cores=INT, faixa=INT_F, **kw)


def fla(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 4); kw.setdefault('hs', 'coque'); kw.setdefault('hair', '#111111')
    put_atleta(c, x, y, h, f, seed, cores=FLA, faixa=FLA_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def gol_txt(c, f, f0, x=640, y=880, s='GOL!', cor=(255, 216, 74)):
    explosao(c, x, y, f, f0, 260, cor)
    num(c, s, x, y, f, f0 + 2, 150, -4)


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y + 12 * math.sin(f * .08), s)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio2('day').copy()
    ta = wt(0, 'Copa') - 3; ine = wt(0, 'inedito') - 3
    put_trofeu(c, 640, 1080, 520, f, ta)
    num(c, 'CAMPEÃO INÉDITO', 640, 720, f, ine, 100, -3)
    xi = lerp(-300, 290, easeOut(ramp(f, 0, 20))); xf = lerp(1550, 990, easeOut(ramp(f, 0, 20)))
    inter(c, xi, 2030, 820, f, 1, arms='cheek' if f >= ine else 'run', expr='shock' if f >= ine else 'grin', run=(f * .08) % 1 if f < 20 else None, look=1)
    fla(c, xf, 2030, 820, f, 2, arms='cheek' if f >= ine else 'run', expr='shock' if f >= ine else 'grin', run=(f * .08) % 1 if f < 20 else None, look=-1, flip=True)
    confete(c, 640, 900, f, ine, 70, 800)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, ine, .8)
    return c, (640, 1420 + k * 10, z, k), 'golden'


def s1(f):
    c = estadio2('golden').copy()
    ii = wt(1, 'Internacional') - 3; ff = wt(1, 'Flamengo') - 3; qu = wt(1, 'quatro') - 3; be = wt(1, 'Beira-Rio') - 3
    vx = lerp(-260, 340, easeOut(ramp(f, ii - 10, ii + 8)))
    px = lerp(1500, 940, easeOut(ramp(f, ff - 10, ff + 8)))
    inter(c, vx, 2030, 720, f, 3, arms='cintura', expr='stern', look=1, num_='9', run=(f * .08) % 1 if f < ii + 8 else None)
    fla(c, px, 2030, 720, f, 4, arms='cintura', expr='stern', look=-1, flip=True, num_='10', run=(f * .08) % 1 if f < ff + 8 else None)
    put_placa(c, 'INTERNACIONAL', INT, 340, 1210, f, ii + 4, 44, -4)
    put_placa(c, 'FLAMENGO', FLA, 940, 1210, f, ff + 4, 50, 4)
    if f >= qu: paste_c(c, calendario('15', 'NOV'), 640, 770, .45 * back(ramp(f, qu, qu + 8)))
    num(c, 'HOJE 16H', 640, 950, f, qu + 4, 84, -3)
    num(c, 'BEIRA-RIO', 640, 1070, f, be, 84, 3)
    z = lerp(1.12, 1.0, easeOut(ramp(f, 0, 35))) * (1 + .0005 * f)
    k = kick(f, qu, .6) + kick(f, be, .5)
    return c, (640, 1420 + k * 8, z, k), 'golden'


def s2(f):
    c = estadio2('dusk').copy()
    ve = wt(2, 'venceu') - 3; tr = wt(2, 'tres') - 3
    kf = max(ve, 18)
    gx, gy = put_gol2(c, x=760, estufa=pulse(f, kf + 9, 10))
    put_goleiro(c, f, GKF, None, gx=780 + 70 * clamp((f - kf) / 7), arms='up', expr='shock', skin=3)
    num(c, 'IDA  ·  RIO DE JANEIRO', 640, 700, f, wt(2, 'ida') - 3, 70, -2) if f < kf + 8 else None
    x = lerp(-150, 520, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, x, 2030, 860, f)
    inter(c, x, 2030, 860, f, 5, arms='run' if f < kf + 10 else 'punho', run=(f * .1) % 1 if f < kf - 4 else None,
          kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0, expr='grin', num_='7')
    rb = raio_bola(860)
    bola_voo(c, f, kf, x + 112, 2030 - rb, gx + 90, gy, rb, raio_bola(300))
    if f >= kf + 9: gol_txt(c, f, kf + 9, 640, 860)
    num(c, 'INTER 3 x 1', 640, 1040, f, max(tr, kf + 16), 110, 3)
    k = kick(f, kf + 9)
    return c, (lerp(580, 680, smooth(f / 70)), 1430 + k * 10, lerp(1.0, 1.08, smooth(f / 70)), k), 'dusk'


def s3(f):
    c = estadio2('golden').copy()
    va = wt(3, 'vantagem') - 3; pe = wt(3, 'perder') - 3; ca = wt(3, 'campeao') - 3
    inter(c, 640, 2040, 860, f, 6, arms='joinha' if f >= ca else 'cintura', expr='proud' if f >= ca else 'smug', num_='10')
    foco(c, 640, 1620, 420, .7 * pulse(f, va, 40))
    put_placa(c, 'INTER', INT, 640, 1050, f, wt(3, 'Inter') - 3, 70, -3)
    num(c, 'VENCE = CAMPEÃO', 640, 700, f, ca, 70, -3)
    num(c, 'EMPATA = CAMPEÃO', 640, 800, f, ca + 8, 70, 2)
    num(c, 'PERDE POR 1 = CAMPEÃO', 640, 900, f, pe, 64, -2)
    k = kick(f, pe, .6)
    return c, (640 + 20 * math.sin(f * .04), 1430 + k * 8, lerp(1.0, 1.06, smooth(f / 110)), k), 'golden'


def s4(f):
    c = estadio2('golden').copy()
    tg = wt(4, 'tres') - 3; dg = wt(4, 'dois') - 3; pe = wt(4, 'penaltis') - 3
    fla(c, 640, 2040, 920, f, 7, arms='point' if f < pe else 'punho', expr='stern', num_='9', look=1)
    put_placa(c, 'FLAMENGO', FLA, 640, 1060, f, wt(4, 'Flamengo') - 3, 66, 3)
    num(c, 'VENCER POR 3 = TÍTULO', 640, 720, f, tg, 66, -3)
    num(c, 'POR 2 = PÊNALTIS', 640, 860, f, dg, 70, 3)
    if f >= pe:
        rb = raio_bola(920); put_bola(c, 900, 2040 - rb, rb, 0)
        paste_c(c, cartaz_pen(), 900, 1500, .7 * back(ramp(f, pe, pe + 8)))
    k = kick(f, pe, .7)
    return c, (640, 1430 + k * 10, lerp(1.0, 1.06, smooth(f / 110)), k), 'golden'


@lru_cache(maxsize=1)
def cartaz_pen():
    im = Image.new('RGBA', (300, 120), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([4, 4, 296, 116], 26, fill=(255, 255, 255, 255), outline=INK + (255,), width=8)
    fo = ImageFont.truetype(FONTB, 56); t = 'PÊNALTI'; tw = d.textlength(t, font=fo)
    d.text((150 - tw / 2, 28), t, font=fo, fill=INK + (255,))
    return im


def s5(f):
    c = estadio2('dusk').copy()
    pe = wt(5, 'penaltis') - 3; de = wt(5, 'defesa') - 3; ga = wt(5, 'Gabi') - 3
    kf = max(de - 8, 14)
    salto = clamp((f - kf) / 6)
    gx, gy = put_gol2(c, x=700)
    put_goleiro(c, f, GKI, None, gx=720 + 110 * salto, arms='up', expr='grin' if f >= kf + 8 else 'stern', skin=1)
    put_atleta(c, 360, 2030, 860, f, 8, cores=BRG, faixa=BRG_F, skin=2, hs='rabo', hair='#151010',
               arms='run' if f < kf + 8 else 'cheek', kick=pulse(f, kf - 4, 5) if f >= kf - 4 else 0,
               expr='stern' if f < kf + 8 else 'pained', num_='11')
    rb = raio_bola(860)
    if f < kf + 7:
        bola_voo(c, f, kf, 475, 2030 - rb, gx + 150, gy - 20, rb, raio_bola(300), 120, 7)
    else:
        t = ramp(f, kf + 7, kf + 22)
        put_bola(c, lerp(gx + 150, 1150, t), lerp(gy - 20, 1500, t) - 160 * math.sin(t * math.pi), lerp(raio_bola(300), raio_bola(600), t), f)
    if kf + 8 <= f < kf + 22: gol_txt(c, f, kf + 8, 640, 840, 'DEFENDEU!', (120, 220, 255))
    put_placa(c, 'GABI BARBIERI', GKI, 760, 1080, f, max(ga, kf + 14), 50, 3)
    num(c, 'PÊNALTIS 5 x 4', 640, 800, f, kf + 22, 100, -3) if f >= kf + 22 else None
    k = kick(f, kf + 8)
    return c, (lerp(600, 680, smooth(f / 80)), 1430 + k * 10, lerp(1.0, 1.08, smooth(f / 80)), k), 'dusk'


def s6(f):
    c = estadio2('dusk').copy()
    ta = wt(6, 'taca') - 3; mi = wt(6, 'milhao') - 3
    put_trofeu(c, 640, 1150, 560, f, 0)
    if f >= mi: explosao(c, 640, 760, f, mi, 280)
    num(c, 'R$ 1,1 MILHÃO', 640, 760, f, mi, 110, -3)
    inter(c, 250, 2040, 780, f, 1, arms='up' if f >= ta else 'cintura', expr='grin', look=1)
    fla(c, 1030, 2040, 780, f, 2, arms='up' if f >= ta else 'cintura', expr='grin', look=-1, flip=True)
    num(c, '?', 640, 1600, f, ta, 180, 6)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    k = kick(f, mi, .6)
    return c, (640, 1380 + k * 8, z, lerp(0, -2, smooth(ramp(f, 0, 60))) + k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def OVERLAY(im, si, lf):
    if si in (2, 3, 4):
        k = max(wt(2, 'venceu') - 3, 18) + 9
        if si == 2: im = placar_tv(im, 'FLA', 'INT', 1, 3, FLA, INT, 'IDA', lf, pulse_b=k if lf >= k else -1)
        else: im = placar_tv(im, 'FLA', 'INT', 1, 3, FLA, INT, 'IDA', lf + 99)
    D = {0: ('CAMPEÃO INÉDITO', 'COPA DO BRASIL FEMININA', wt(0, 'inedito') + 6),
         1: ('INTER x FLAMENGO', 'HOJE, 16H, NO BEIRA-RIO', 99999),
         2: ('IDA: FLAMENGO 1 x 3 INTER', 'NO RIO DE JANEIRO', max(wt(2, 'venceu') - 3, 18) + 20),
         3: ('INTER TEM A VANTAGEM', 'ATÉ PERDER POR 1 GOL', wt(3, 'perder') - 3),
         4: ('FLAMENGO PRECISA DE 3 GOLS', 'POR 2 GOLS: PÊNALTIS', wt(4, 'penaltis') - 3),
         5: ('PRIMEIRA FINAL DO INTER', 'NOS PÊNALTIS CONTRA O BRAGANTINO', wt(5, 'Barbieri') + 4),
         6: ('PRÊMIO DO CAMPEÃO', 'R$ 1,1 MILHÃO', wt(6, 'premio') - 3)}
    t, sub, f0 = D[si]
    return destaque(im, t, lf, f0, sub)


def SFX(s):
    s.ting(s.W(0, 'inedito') - 3, .35)
    s.thunk(s.W(1, 'quatro') - 3, 150, .7)
    s.thunk(max(s.W(2, 'venceu') - 3, 18) + 9, 160, .9)
    s.thunk(s.W(3, 'perder') - 3, 200, .6)
    s.thunk(s.W(4, 'penaltis') - 3, 160, .7)
    s.thunk(max(s.W(5, 'defesa') - 8, 14) + 8, 150, .9)
    s.ting(s.W(6, 'milhao') - 3, .35)
