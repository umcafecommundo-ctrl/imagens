"""anima.futebol — 25/11/2026 19h15 — FIM DE JOGO · EP. 5 — PSG 2x2 Roma em Paris (Champions, fase de liga, 5ª rodada).
Fontes (conferidas em 25/11/2026, ver fatos.txt): Gazeta Esportiva, A Bola (liveblog), La Tercera, beIN Sports, Diário 24 Horas, Fanpage.it, ESPN, VAVEL.
Hermoso abre para a Roma (5'); Zabarnyi empata de cabeça após escanteio (31'); pênalti de Wesley em Hakimi e Dembélé vira (62');
Malen empata de pênalti após o VAR (77'); PSG chega a 13 pontos e perde a ponta para o Real Madrid (15). Sem escudos/logos: times por plaquinhas e cores."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+18%'
ARROBA = ''
SELO = 'CHAMPIONS  ·  5ª RODADA'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O PSG ainda é favorito? Olha esse empate em Paris.",
    "A Roma saiu na frente cedo, com Hermoso.",
    "Zabarnyi empatou de cabeça, depois de escanteio.",
    "Wesley fez pênalti em Hakimi... e Dembélé virou.",
    "Mas a Roma também teve pênalti... e Malen empatou. Dois a dois.",
    "Com treze pontos, o PSG perdeu a ponta... pro Real.",
]
CAPTXT = [
    "O PSG ainda é favorito?|Olha esse empate em Paris.",
    "A Roma saiu na frente cedo,|com Hermoso.",
    "Zabarnyi empatou de cabeça,|depois de escanteio.",
    "Wesley fez pênalti em Hakimi...|e Dembélé virou.",
    "Mas a Roma também teve pênalti...|e Malen empatou. 2 a 2.",
    "Com 13 pontos, o PSG perdeu|a ponta... pro Real.",
]
FALA_TIKTOK = "Comenta sim ou não."
CTA_TEXTO = "PSG FAVORITO?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 5
FLASH = [3]
CHECK = [(0, 'PSG', 4), (0, 'empate', 4), (1, 'Roma', 4), (1, 'Hermoso', 4), (2, 'Zabarnyi', 4), (2, 'cabeca', 4),
         (2, 'escanteio', 4), (3, 'Wesley', 4), (3, 'Hakimi', 4), (3, 'Dembele', 4), (3, 'virou', 4), (4, 'Malen', 4),
         (4, 'Dois', 4), (5, 'treze', 4), (5, 'ponta', 4), (5, 'Real', 4)]

PSG_, PSG_F = time_('PSG')
ROM, ROM_F = time_('ROMA')
TORC = dict(roupa='#0a2a5c', pele='#e0ac85', cabelo='#3a2a1e')


def psg(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=PSG_, faixa=PSG_F, **kw)


def rom(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=ROM, faixa=ROM_F, **kw)


def voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=120, dur=10):
    t = ramp(f, k0, k0 + dur)
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if 0 < t < 1:
        rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 36


def s0(f):
    """quadro 0 = capa: close do torcedor do PSG (camisa azul-marinho) + série + pergunta; depois o vestiário do PSG."""
    c = vestiario(PSG_, PSG_F).copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, **TORC)
        num(c, 'FIM DE JOGO', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 5', 621, 430, f, 0, 100, 2)
        num(c, 'PSG AINDA É', 621, 1350, f, 0, 130, -2)
        num(c, 'FAVORITO?', 621, 1530, f, 0, 150, 2)
        return c, (621, 1104, 1.0 + .0015 * f, 0), 'dusk'
    em = wt(0, 'empate') - 3
    psg(c, 640, 2100, 860, f, 6, arms='cintura' if f < em else 'shrug', expr='stern' if f < em else 'nervous',
        look=0 if f < em else 1, num_='10')
    if f < em - 2:
        put_placa(c, 'PSG', PSG_, 640, 1000, f, CLOSE_F, 110, -3)
    else:
        num(c, 'EMPATE', 640, 1000, f, em, 170, 3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0008 * f)
    k = kick(f, em if f >= em else CLOSE_F, .7)
    return c, (640, 1400 + k * 10, z, k), 'day'


def s1(f):
    """estádio à noite: Hermoso faz Roma 1 x 0."""
    c = estadio2('dusk').copy()
    he = wt(1, 'Hermoso') - 3
    ks = max(14, he - 16)
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, ('#2d2d2d', '#2d2d2d', '#2d2d2d'), None, arms='up' if f >= ks + 2 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    H = 860
    sx = lerp(300, 500, easeOut(ramp(f, 0, ks - 2)))
    if f < ks - 2: linhas_vel(c, sx, 2010, H, f, dir=-1)
    rom(c, sx, 2010, H, f, 4, num_='22', arms='up' if f >= ks + 10 else 'run', run=(f * .1) % 1 if f < ks - 2 else None,
        kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
    rb = raio_bola(H)
    if f < ks:
        put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
    elif f < ks + 40:
        voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 60, 9)
    if f >= ks + 12: confete(c, 500, 700, f, ks + 12, 40, 400)
    if f < ks + 8:
        put_placa(c, 'ROMA', ROM, 640, 860, f, 0, 110, -2)
    elif f < he - 2:
        explosao(c, 640, 860, f, ks + 8, 200)
        num(c, '0 x 1', 640, 860, f, ks + 8, 170, 3)
    else:
        put_placa(c, 'HERMOSO', ROM, 640, 860, f, he, 100, -2)
    k = kick(f, ks + 8, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0008 * f), k), 'dusk'


def s2(f):
    """prancheta: escanteio no primeiro pau e cabeçada de Zabarnyi, 1 x 1."""
    c = prancheta().copy()
    za = wt(2, 'Zabarnyi') - 3; ca = wt(2, 'cabeca') - 3; es = wt(2, 'escanteio') - 3
    for i, (x, y) in enumerate(((520, 800), (700, 760), (860, 840))):
        pino(c, x, y + 10 * math.sin(f * .2 + i), ROM, f, 2 + i * 2, '', 70)
    pino(c, 1080, 600, PSG_, f, 0, '', 60)
    pino(c, 460, 700 + 8 * math.sin(f * .2), PSG_, f, za, 'Z', 90)
    seta(c, (1060, 620), (480, 690), f, 2, 14, (255, 255, 255), 10)
    seta(c, (460, 700), (560, 580), f, ca, 8, (255, 216, 74), 16)
    if f < ca - 2:
        put_placa(c, 'ZABARNYI', PSG_, 640, 1300, f, za, 96, -2)
    else:
        explosao(c, 640, 1300, f, ca, 180)
        num(c, '1 x 1', 640, 1300, f, ca, 170, 3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .08 * pulse(f, ca, 10))
    k = kick(f, ca if f >= ca else za, .7)
    return c, (640 + 12 * math.sin(f * .06), 1150 + k * 8, z, lerp(0, -1, smooth(ramp(f, 0, 60)))), 'day'


def s3(f):
    """estádio golden: pênalti de Wesley em Hakimi, Dembélé converte, PSG 2 x 1."""
    c = estadio2('golden').copy()
    we = wt(3, 'Wesley') - 3; ha = wt(3, 'Hakimi') - 3; de = wt(3, 'Dembele') - 3; vr = wt(3, 'virou') - 3
    ks = vr - 8
    gx, gy = put_gol2(c, estufa=ramp(f, ks + 8, ks + 14))
    put_goleiro(c, f, ('#f5c518', '#f5c518', '#f5c518'), None, arms='shrug' if f >= ks + 8 else 'hang',
                expr='shock' if f >= ks + 8 else 'nervous', skin=1)
    H = 860
    if f < de - 2:
        rom(c, 420, 2010, H, f, 5, num_='43', skin=3, hair='#151010', arms='shrug' if f >= ha else 'hang',
            expr='nervous' if f >= ha else 'stern', look=1)
        psg(c, 860, 1990, 820, f, 8, num_='2', skin=3, hair='#151010', arms='point' if f >= ha else 'hang',
            expr='pained' if f >= ha else 'stern', flip=True)
    else:
        sx = 520
        psg(c, sx, 2010, H, f, 9, num_='10', skin=4, hair='#151010', arms='up' if f >= ks + 10 else 'hang',
            kick=pulse(f, ks - 3, 5), expr='grin' if f >= ks + 6 else 'stern')
        rb = raio_bola(H)
        if f < ks:
            put_bola(c, sx + H * .13 + 30, 2010 - rb, rb, f)
        elif f < ks + 40:
            voo(c, f, ks, sx + H * .13 + 30, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 40, 9)
        if f >= vr: confete(c, 640, 600, f, vr, 50, 500)
    if f < ha - 2:
        put_placa(c, 'WESLEY', ROM, 640, 860, f, we, 100, -2)
    elif f < de - 2:
        num(c, 'PÊNALTI', 640, 860, f, ha, 150, 3)
    elif f < vr - 2:
        put_placa(c, 'DEMBÉLÉ', PSG_, 640, 860, f, de, 100, -2)
    else:
        explosao(c, 640, 860, f, vr, 200)
        num(c, '2 x 1', 640, 860, f, vr, 170, -3)
    z = lerp(1.12, 1.04, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f) * (1 + .1 * pulse(f, ha, 10))
    k = kick(f, vr if f >= vr else ha, .9)
    return c, (640 + 20 * math.sin(f * .04), 1440 + k * 10, z, k), 'golden'


def s4(f):
    """telão: Malen comemora o empate, 2 x 2."""
    c = telao('dusk').copy()
    pe = wt(4, 'penalti') - 3; ma = wt(4, 'Malen') - 3; do = wt(4, 'Dois') - 3
    rom(c, 640, 2090, 820, f, 7, num_='17', skin=4, hs='curto', hair='#151010',
        arms='run' if f < ma else ('punho' if f < do else 'up'), run=(f * .1) % 1 if f < ma else None,
        expr='stern' if f < ma else 'grin', look=0)
    if f < pe - 2:
        telao_txt(c, [('ROMA', 190)], f, 0, y=720)
    elif f < ma - 2:
        telao_txt(c, [('PÊNALTI', 170)], f, pe, y=720)
    elif f < do - 2:
        telao_txt(c, [('MALEN', 180)], f, ma, y=720)
    else:
        telao_txt(c, [('2 x 2', 230)], f, do, y=700)
    if f >= do: confete(c, 640, 500, f, do, 70, 600)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .1 * pulse(f, do, 10))
    k = kick(f, do if f >= do else ma, .8)
    return c, (640 - 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s5(f):
    """a conta: PSG perde os 100% e chega a 13 pontos; fecha no close preocupado."""
    c = conta_bg().copy()
    tr = wt(5, 'treze') - 3; ce = wt(5, 'ponta') - 3; re_ = wt(5, 'Real') - 3; fim = re_ + 20
    psg(c, 640, 2090, 780, f, 6, num_='10', arms='cintura' if f < ce else 'cheek',
        expr='stern' if f < ce else 'pained', look=0)
    if f < re_ - 2:
        numero_gigante(c, '13 PTS', 640, 1000, f, max(0, tr), 230, 3)
    else:
        numero_gigante(c, 'REAL 15', 640, 1000, f, re_, 200, -3)
    if f >= fim:
        c = put_close(c, f, expr='preocupado', look=-1 if f < fim + 15 else 0, s=.9, **TORC)
        num(c, 'FAVORITO?', 621, 1450, f, fim, 160, -3)
        return c, (621, 1104, 1.03 * (1 + .002 * (f - fim)), 0), 'dusk'
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0012 * f) * (1 + .08 * pulse(f, tr, 10)) * (1 + .1 * pulse(f, ce, 10))
    k = kick(f, tr if f >= tr else (ce if f >= ce else 0), .7)
    return c, (640 + 25 * math.sin(f * .05), 1380 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(CLOSE_F, 120, .8)
    s.thunk(s.W(0, 'empate') - 3, 140, .9)
    s.apito(s.W(1, 'Roma') - 4)
    k1 = s.W(1, 'Hermoso') - 16
    s.chute(k1); s.rede(k1 + 9); s.rugido(k1 + 10, 1.5, .5)
    s.thunk(k1 + 8, 150, .9)
    s.thunk(s.W(1, 'Hermoso') - 3, 130, .8)
    s.thunk(s.W(2, 'Zabarnyi') - 3, 140, .8)
    s.thunk(s.W(2, 'cabeca') - 3, 160, 1.0)
    s.rugido(s.W(2, 'cabeca') - 2, 1.4, .5)
    s.apito(s.W(3, 'Hakimi') - 4)
    s.thunk(s.W(3, 'Hakimi') - 3, 150, .9)
    k2 = s.W(3, 'virou') - 8
    s.chute(k2); s.rede(k2 + 9); s.rugido(k2 + 10, 1.6, .6)
    s.thunk(s.W(3, 'virou') - 3, 160, 1.0)
    s.thunk(s.W(4, 'Malen') - 3, 140, .8)
    s.thunk(s.W(4, 'Dois') - 3, 170, 1.0)
    s.apito(s.W(4, 'Dois') + 6, longo=True)
    s.thunk(s.W(5, 'treze') - 3, 160, 1.0)
    s.thunk(s.W(5, 'Real') - 3, 150, .9)
    s.ting(s.W(5, 'Real') + 17, .35)
