"""anima.futebol — 21/11/2026 22h20 — FIM DE JOGO · EP. 2 — final da Copa Sul-Americana: Boca Juniors 2x0 Atlético-MG.
Fontes (conferidas em 21/11/2026, ver fatos.txt): Gazeta Esportiva (Barranquilla, Ascacíbar 15' no rebote, Merentiel 2' do 2º
tempo após cruzamento de Villa, 3º título do Boca 2004/2005/2026, Galo vice pelo 2º ano seguido, 2025 Lanús nos pênaltis),
GCMais (2x0, 3º título, vice em 2025), Sportbuzz (gols e Lanús 2025), Brasil 247 (2x0, 1x0 no intervalo).
Sem escudos/logos/taça real: times por plaquinhas e cores, taça genérica."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *
from sombrio import put_close

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'SUL-AMERICANA  ·  FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "O Galo perdeu a final de novo? Olha como foi.",
    "Em Barranquilla, Ascacíbar abriu o placar para o Boca no primeiro tempo.",
    "No começo do segundo tempo, Merentiel ampliou... dois a zero.",
    "É o terceiro título do Boca na Sul-Americana.",
    "E o Galo... é vice pelo segundo ano seguido.",
    "Em dois mil e vinte e cinco, perdeu para o Lanús, nos pênaltis.",
]
CAPTXT = [
    "O Galo perdeu a final de novo?|Olha como foi.",
    "Em Barranquilla, Ascacíbar abriu o placar|para o Boca no 1º tempo.",
    "No começo do 2º tempo, Merentiel ampliou...|2 a 0.",
    "É o 3º título do Boca|na Sul-Americana.",
    "E o Galo...|é vice pelo 2º ano seguido.",
    "Em 2025, perdeu para o Lanús,|nos pênaltis.",
]
FALA_TIKTOK = "O Galo volta mais forte? Comenta sim ou não."
CTA_TEXTO = "VOLTA FORTE?"
CTA_PALAVRA = 'SIM ou NÃO'
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Galo', 4), (0, 'final', 4), (1, 'Barranquilla', 4), (1, 'Ascacibar', 4), (1, 'Boca', 4), (2, 'Merentiel', 4),
         (2, 'dois', 4), (3, 'terceiro', 4), (4, 'vice', 4), (4, 'segundo', 4), (5, 'Lanus', 4), (5, 'penaltis', 4)]

CAM, CAM_F = time_('ATLÉTICO-MG')
BOC, BOC_F = time_('BOCA JUNIORS')


def galo(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=CAM, faixa=CAM_F, **kw)


def boca(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 1); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#2a1a10')
    put_atleta(c, x, y, h, f, seed, cores=BOC, faixa=BOC_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


CLOSE_F = 40   # quadros do close de abertura (~1,3 s)


def s0(f):
    """quadro 0 = capa: close do torcedor do Galo + série + pergunta; depois o jogador do Galo cabisbaixo."""
    c = conta_bg().copy()
    if f < CLOSE_F:
        c = put_close(c, f, expr='choque', s=.9, roupa='#111111', pele='#8a5a3c', cabelo='#151010')
        num(c, 'FIM DE JOGO', 621, 300, f, 0, 100, -2)
        num(c, 'EP. 2', 621, 430, f, 0, 100, 2)
        num(c, 'O GALO PERDEU', 621, 1350, f, 0, 120, -2)
        num(c, 'DE NOVO?', 621, 1520, f, 0, 145, 2)
        z = 1.0 + .0015 * f
        return c, (621, 1104, z, 0), 'dusk'
    galo(c, 640, 2080, 880, f, 6, arms='cheek', expr='pained', look=0, num_='7')
    num(c, 'BOCA x GALO', 640, 880, f, CLOSE_F, 140, -3)
    z = lerp(1.2, 1.03, easeOut(ramp(f, CLOSE_F, CLOSE_F + 30))) * (1 + .0006 * f)
    k = kick(f, CLOSE_F, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio à noite: Ascacíbar chuta a bola que sobrou na área, gol no fundo."""
    c = estadio2('dusk').copy()
    ba = wt(1, 'Barranquilla') - 3; asc = wt(1, 'Ascacibar') - 3; bo = wt(1, 'Boca') - 3
    kf = asc
    gx, gy = put_gol2(c, estufa=ramp(f, kf + 8, kf + 14))
    put_goleiro(c, f, CAM, CAM_F, arms='shrug' if f >= kf + 8 else 'hang', expr='shock' if f >= kf + 8 else 'nervous', skin=2)
    sx = 480; H = 860
    boca(c, sx, 2010, H, f, 5, num_='5', arms='up' if f >= kf + 10 else 'run', kick=pulse(f, kf - 3, 5),
         expr='grin' if f >= kf + 6 else 'stern')
    rb = raio_bola(H)
    if f < kf + 40: bola_voo(c, f, kf, sx + H * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 120)
    if f < asc - 2:
        if f >= ba: num(c, 'BARRANQUILLA', 640, 780, f, ba, 110, -3)
    else:
        put_placa(c, 'ASCACÍBAR', BOC, 640, 760, f, asc + 2, 72, 2)
    k = kick(f, kf, .9)
    return c, (lerp(600, 680, smooth(f / 150)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s2(f):
    """estádio dourado: Merentiel completa o cruzamento, 2 a 0."""
    c = estadio2('golden').copy()
    me = wt(2, 'Merentiel') - 3; am = wt(2, 'ampliou') - 3; do = wt(2, 'dois') - 3
    kf = am
    gx, gy = put_gol2(c, estufa=ramp(f, kf + 8, kf + 14))
    put_goleiro(c, f, CAM, CAM_F, arms='shrug' if f >= kf + 8 else 'hang', expr='shock' if f >= kf + 8 else 'nervous', skin=2)
    sx = lerp(260, 470, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    boca(c, sx, 2010, 860, f, 9, num_='16', arms='up' if f >= kf + 10 else 'run', run=(f * .1) % 1 if f < kf - 4 else None,
         kick=pulse(f, kf - 3, 5), expr='grin' if f >= kf + 6 else 'stern', skin=4, hs='cacheado')
    rb = raio_bola(860)
    if f < kf + 40: bola_voo(c, f, kf, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 140)
    if f >= do:
        explosao(c, 640, 860, f, do, 200)
        num(c, '2 x 0', 640, 860, f, do, 170, 3)
    elif f >= me:
        put_placa(c, 'MERENTIEL', BOC, 640, 800, f, me, 72, -3)
    k = kick(f, kf, .9)
    return c, (lerp(680, 610, smooth(f / 120)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'golden'


def s3(f):
    """telão: 3º título do Boca, com taça genérica e jogadores do Boca."""
    c = telao('dusk').copy()
    te = wt(3, 'terceiro') - 3
    telao_txt(c, [('3º TÍTULO', 130)], f, te, y=740)
    tk = back(ramp(f, 0, 10))
    if tk > .03: paste_c(c, trofeu(), 640, 1350, .7 * tk)
    boca(c, 300, 2090, 700, f, 3, arms='up', expr='grin', look=1, num_='10')
    boca(c, 980, 2090, 700, f, 8, arms='up', expr='grin', look=-1, flip=True, num_='9', skin=3)
    if f >= te: confete(c, 640, 800, f, te, 60, 600)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    k = kick(f, te, .6)
    return c, (640 + 20 * math.sin(f * .04), 1360 + k * 8, z, k), 'dusk'


def s4(f):
    """vestiário do Galo: vice pelo 2º ano seguido (resposta da pergunta)."""
    c = vestiario(CAM, CAM_F).copy()
    vi = wt(4, 'vice') - 3
    galo(c, 360, 2110, 780, f, 3, arms='cheek', expr='pained', look=1, num_='9')
    galo(c, 920, 2110, 780, f, 8, arms='hang', expr='pained', look=-1, flip=True, num_='11', skin=1, hair='#3a2a1e')
    if f >= vi:
        numero_gigante(c, 'VICE DE NOVO', 640, 1330, f, vi, 120, -3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, vi, .7)
    return c, (640, 1380 + k * 8, z, k), 'golden'


def s5(f):
    """a conta: 2025 = Lanús nos pênaltis."""
    c = conta_bg().copy()
    an = wt(5, 'dois') - 3; la = wt(5, 'Lanus') - 3; pe = wt(5, 'penaltis') - 3
    galo(c, 640, 2090, 860, f, 6, arms='hang', expr='pained', look=0, num_='7')
    if f < la - 2:
        if f >= an: num(c, '2025', 640, 900, f, an, 170, -3)
    elif f < pe - 2:
        num(c, 'LANÚS', 640, 900, f, la, 170, 2)
    else:
        num(c, 'NOS PÊNALTIS', 640, 900, f, pe, 120, -2)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, pe if f >= pe else la, .7)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(0, 150, .9)
    s.thunk(s.cut(0) + CLOSE_F, 120, .8)
    s.apito(s.W(1, 'Barranquilla') - 4)
    s.thunk(s.W(1, 'Barranquilla') - 3, 150, .6)
    s.chute(s.W(1, 'Ascacibar') - 3); s.rede(s.W(1, 'Ascacibar') + 6); s.rugido(s.W(1, 'Ascacibar') + 7, 2.2, .7)
    s.thunk(s.W(2, 'Merentiel') - 3, 150, .7)
    s.chute(s.W(2, 'ampliou') - 3); s.rede(s.W(2, 'ampliou') + 6); s.rugido(s.W(2, 'ampliou') + 7)
    s.thunk(s.W(2, 'dois') - 3, 120, 1.0)
    s.apito(s.W(3, 'terceiro') - 8, longo=True)
    s.thunk(s.W(3, 'terceiro') - 3, 150, .9)
    s.thunk(s.W(4, 'vice') - 3, 110, 1.0)
    s.ting(s.W(4, 'vice') - 3, .35)
    s.thunk(s.W(5, 'dois') - 3, 130, .8)
    s.thunk(s.W(5, 'Lanus') - 3, 130, .9)
    s.thunk(s.W(5, 'penaltis') - 3, 120, .8)
