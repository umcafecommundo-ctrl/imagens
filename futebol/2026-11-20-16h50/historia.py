"""anima.futebol — 20/11/2026 16h50 — FIM DE JOGO · EP. 1 — Al-Ahli x Al-Nassr (Campeonato Saudita, 20/11, 14h30 de Brasília).
Fontes (conferidas em 20/11/2026, ver fatos.txt): CNN Brasil, Goal, Bolavip, NC News, 365Scores, A Bola (liveblog):
Cristiano Ronaldo abriu o placar no 1º tempo (13'/14'), gol 986 da carreira, a 14 dos mil; minutos depois perdeu um pênalti
que bateu na trave/poste; Galeno empatou nos acréscimos do 1º tempo; no 2º tempo o Al-Ahli fez mais 2 (Toney de pênalti,
Ibañez) e venceu 3x1 (A Bola + confirmação final). Sem escudos/logos/rostos reais: times por plaquinhas e cores, Ronaldo = boneco genérico + placa."""
from kit import *
import kit
from futebol import *
from futebol2 import *
from futebol3 import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+15%'
ARROBA = ''
SELO = 'CAMPEONATO SAUDITA  ·  CLÁSSICO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))
MUSICA = False

LINES = [
    "Cristiano Ronaldo ainda chega aos mil gols? Olha o jogo de hoje.",
    "Contra o Al-Ahli, ele abriu o placar no primeiro tempo. Gol número... novecentos e oitenta e seis.",
    "Minutos depois, pênalti para o Al-Nassr. Ele bateu... e a bola explodiu no poste.",
    "O Al-Ahli empatou antes do intervalo, virou no segundo tempo e venceu... três a um.",
    "Para chegar aos mil gols, agora faltam... quatorze.",
    "E aí, ele chega lá?",
]
CAPTXT = [
    "Cristiano Ronaldo ainda chega aos 1000 gols?|Olha o jogo de hoje.",
    "Contra o Al-Ahli, ele abriu o placar no 1º tempo.|Gol número... 986.",
    "Minutos depois, pênalti para o Al-Nassr.|Ele bateu... e a bola explodiu no poste.",
    "O Al-Ahli empatou antes do intervalo, virou|no 2º tempo e venceu... 3 a 1.",
    "Para chegar aos 1000 gols,|agora faltam... 14.",
    "E aí, ele chega lá?",
]
FALA_TIKTOK = "Ele chega aos mil gols? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "CHEGA AOS MIL?"
TWIST = 3
FLASH = [3]
CHECK = [(0, 'Ronaldo', 4), (0, 'mil', 4), (1, 'Al-Ahli', 4), (1, 'novecentos', 4), (2, 'penalti', 4), (2, 'poste', 4),
         (3, 'empatou', 4), (3, 'tres', 4), (4, 'mil', 4), (4, 'quatorze', 4), (5, 'la', 4)]

NAS, NAS_F = time_('AL-NASSR')
AHL, AHL_F = time_('AL-AHLI')


def cr(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 2); kw.setdefault('hs', 'topete'); kw.setdefault('hair', '#1b1410')
    put_atleta(c, x, y, h, f, seed, cores=NAS, faixa=NAS_F, **kw)


def ahl(c, x, y, h, f, seed, **kw):
    kw.setdefault('skin', 3); kw.setdefault('hs', 'curto'); kw.setdefault('hair', '#151010')
    put_atleta(c, x, y, h, f, seed, cores=AHL, faixa=AHL_F, **kw)


def bola_voo(c, f, k0, x0, y0, x1, y1, r0, r1, arco=160, dur=10):
    def pos(t):
        return lerp(x0, x1, t), lerp(y0, y1, t) - arco * math.sin(t * math.pi), lerp(r0, r1, t)
    if f < k0: put_bola(c, x0, y0, r0, f); return
    t = ramp(f, k0, k0 + dur)
    if t < 1: rastro(c, [pos(max(0, t - k * .06))[:2] for k in range(6, 0, -1)], pos(t)[2], f)
    x, y, r = pos(t); put_bola(c, x, y, r, f)


def s0(f):
    """conta_bg: marca da série e a pergunta polêmica."""
    c = conta_bg().copy()
    mi = wt(0, 'mil') - 3
    q = max(42, mi - 4)
    cr(c, 640, 2080, 820, f, 3, arms='cintura' if f < mi else 'point', expr='stern' if f < mi else 'smug', look=0, num_='7')
    if f < q - 2:
        num(c, 'FIM DE JOGO', 640, 860, f, 0, 120, -3)
        num(c, 'EP. 1', 640, 1050, f, 4, 130, 3)
    else:
        num(c, 'MIL GOLS?', 640, 900, f, q, 170, -3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, q, .7)
    return c, (640, 1380 + k * 10, z, k), 'dusk'


def s1(f):
    """estádio à noite: o chute de Ronaldo e o gol 986."""
    c = estadio2('dusk').copy()
    ab = wt(1, 'abriu') - 3; nv = wt(1, 'novecentos') - 3
    kf = ab
    gx, gy = put_gol2(c, estufa=ramp(f, kf + 8, kf + 14))
    put_goleiro(c, f, AHL, AHL_F, arms='shrug' if f >= kf + 8 else 'hang', expr='shock' if f >= kf + 8 else 'nervous', skin=2)
    sx = lerp(260, 470, easeOut(ramp(f, 0, kf - 4)))
    if f < kf - 4: linhas_vel(c, sx, 2010, 860, f, dir=-1)
    cr(c, sx, 2010, 860, f, 5, num_='7', arms='up' if f >= kf + 10 else 'run', run=(f * .1) % 1 if f < kf - 4 else None,
       kick=pulse(f, kf - 3, 5), expr='grin' if f >= kf + 6 else 'stern')
    rb = raio_bola(860)
    if f < kf + 40: bola_voo(c, f, kf, sx + 860 * .13, 2010 - rb, gx + 90, gy, rb, raio_bola(300), 140)
    if f < nv - 2:
        put_placa(c, 'CRISTIANO RONALDO', NAS, 640, 820, f, wt(1, 'Al-Ahli') - 3, 66, -3)
    else:
        explosao(c, 640, 860, f, nv, 220)
        num(c, 'GOL 986', 640, 860, f, nv, 150, -3)
    k = kick(f, kf, .9)
    return c, (lerp(600, 680, smooth(f / 150)), 1440 + k * 10, 1.06 * (1 + .0006 * f), k), 'dusk'


def s2(f):
    """estádio dourado: o pênalti no poste."""
    c = estadio2('golden').copy()
    pe = wt(2, 'penalti') - 3; ba = wt(2, 'bateu') - 3; po = wt(2, 'poste') - 3
    gx, gy = put_gol2(c)
    put_goleiro(c, f, AHL, AHL_F, arms='shrug' if f >= ba + 4 else 'hang', expr='shock' if f >= po else 'nervous', skin=2)
    cr(c, 470, 2010, 860, f, 7, num_='7', kick=pulse(f, ba - 3, 5),
       arms='cheek' if f >= po + 4 else 'hang', expr='pained' if f >= po + 4 else 'stern')
    rb = raio_bola(860)
    postx, posty = 878, gy - 10
    x0, y0 = 470 + 860 * .13, 2010 - rb
    if f < ba:
        put_bola(c, x0, y0, rb, f)
    elif f < po:
        bola_voo(c, f, ba, x0, y0, postx, posty, rb, raio_bola(300), 100, max(4, po - ba))
    else:
        t = ramp(f, po, po + 16)
        if t < 1:
            put_bola(c, lerp(postx, 760, t), lerp(posty, 1720, t) - 160 * math.sin(t * math.pi), lerp(raio_bola(300), raio_bola(500), t), f)
    if f < po - 2:
        num(c, 'PÊNALTI!', 640, 860, f, pe, 125, -3)
    else:
        explosao(c, postx, posty, f, po, 120, cor=(255, 255, 255))
        num(c, 'NO POSTE!', 640, 860, f, po, 125, 3)
    k = kick(f, po, 1.0)
    return c, (lerp(640, 700, smooth(f / 150)), 1440 + k * 12, 1.08 * (1 + .0006 * f), k), 'golden'


def s3(f):
    """telão: a virada do Al-Ahli e o placar final."""
    c = telao('dusk').copy()
    em = wt(3, 'empatou') - 3; vi = wt(3, 'virou') - 3; tr = wt(3, 'tres') - 3
    if f < tr - 2:
        if f >= em: put_placa(c, 'AL-AHLI', AHL, 621, 900, f, em, 90, -3)
        if f >= vi: num(c, 'VIROU!', 621, 1100, f, vi, 130, 3)
    else:
        telao_txt(c, [('AL-AHLI', 120), ('3 x 1', 230)], f, tr, y=700)
    ahl(c, 330, 2080, 760, f, 4, arms='up' if f >= vi else 'punho', expr='grin', look=1, num_='9')
    cr(c, 940, 2080, 700, f, 8, arms='hang', expr='pained' if f >= vi else 'nervous', look=-1, flip=True, num_='7')
    if f >= tr: confete(c, 330, 1500, f, tr, 50, 500)
    z = lerp(1.0, 1.07, smooth(f / 120))
    k = kick(f, tr, .6)
    return c, (640 + 18 * math.sin(f * .03), 1320 + k * 8, z, k), 'dusk'


def s4(f):
    """conta_bg: faltam 14 para os mil."""
    c = conta_bg().copy()
    mi = wt(4, 'mil') - 3; qu = wt(4, 'quatorze') - 3
    cr(c, 640, 2100, 760, f, 6, arms='cintura', expr='stern', look=0, num_='7')
    if f < qu - 2:
        num(c, '1000', 640, 960, f, mi, 220, -3)
    else:
        numero_gigante(c, 'FALTAM 14', 640, 960, f, qu, 170, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0006 * f)
    k = kick(f, qu, .8)
    return c, (640, 1400 + k * 10, z, k), 'dusk'


def s5(f):
    """vestiário do Al-Nassr: a pergunta final."""
    c = vestiario(NAS, NAS_F).copy()
    la = wt(5, 'la') - 3
    cr(c, 640, 2110, 840, f, 9, arms='cintura' if f < la else 'point', expr='stern' if f < la else 'smug', look=0, num_='7')
    num(c, 'CHEGA LÁ?', 640, 1100, f, la, 150, 3)
    z = lerp(1.15, 1.03, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    k = kick(f, la, .6)
    return c, (640, 1400 + k * 10, z, k), 'day'


SCENES = [s0, s1, s2, s3, s4, s5]


def OVERLAY(im, si, lf):
    return im


def SFX(s):
    s.thunk(s.W(0, 'Ronaldo') - 3, 150, .8)
    s.thunk(s.W(0, 'mil') - 3, 120, .9)
    s.apito(s.W(1, 'Contra') - 3)
    s.chute(s.W(1, 'abriu') - 3); s.rede(s.W(1, 'abriu') + 6); s.rugido(s.W(1, 'abriu') + 7, 2.2, .7)
    s.thunk(s.W(1, 'novecentos') - 3, 120, 1.0)
    s.thunk(s.W(2, 'penalti') - 3, 150, .8)
    s.chute(s.W(2, 'bateu') - 3)
    s.thunk(s.W(2, 'poste') - 3, 90, 1.0)
    s.thunk(s.W(3, 'empatou') - 3, 150, .7)
    s.thunk(s.W(3, 'virou') - 3, 140, .8)
    s.apito(s.W(3, 'tres') - 6, longo=True)
    s.thunk(s.W(3, 'tres') - 3, 120, 1.0)
    s.thunk(s.W(4, 'mil') - 3, 150, .8)
    s.thunk(s.W(4, 'quatorze') - 3, 120, 1.0)
    s.ting(s.W(4, 'quatorze') - 3, .35)
    s.ting(s.W(5, 'la') - 3, .3)
