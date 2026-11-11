"""anima.futebol — 11/11/2026 21h — Série B: Vojvoda volta ao Fortaleza sem custo de contrato para os 3 jogos finais.
Fontes (conferidas em 11/11/2026): site oficial fortaleza1918.com.br (10/11, 22h20: retorno para os 3 jogos finais da Série B,
"sem custos de contrato", 2021-2025: 310 jogos, 5 títulos — Cearense 2021/22/23 e Copa do Nordeste 2022/24 —, 3 Libertadores,
vice da Sul-Americana 2023); O Povo (10/11: recusou na segunda, 9, e mudou de ideia; sábado 14 x Vila Nova no Castelão;
playoff x Criciúma pela vaga na Série A 2027); A Gazeta (Autuori demitido após derrota para o Novorizontino; playoff ida e volta,
quem vencer sobe); Mix Vale (11/11: mesmos títulos, Autuori saiu no início da semana).
Sem escudos/logos nem rostos reais: bonecos genéricos com camisa nas cores e plaquinha do nome."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''
SELO = 'SÉRIE B  ·  RETA FINAL'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Juan Pablo Vojvoda está de volta ao Fortaleza, e sem custo de contrato.",
    "O anúncio saiu na noite de terça, um dia depois de ele recusar o primeiro convite.",
    "Ele chega no lugar de Paulo Autuori, que caiu depois da derrota para o Novorizontino.",
    "Na primeira passagem, de dois mil e vinte e um a dois mil e vinte e cinco, foram trezentos e dez jogos e cinco títulos.",
    "Ele ainda levou o Fortaleza a três Libertadores e à final da Sul-Americana de dois mil e vinte e três.",
    "Agora a missão é curta: três jogos para voltar à Série A.",
    "Primeiro, o Vila Nova, no sábado, no Castelão. Depois, o playoff de ida e volta contra o Criciúma.",
    "Quem vencer o mata-mata sobe para a elite.",
]
CAPTXT = [
    "Juan Pablo Vojvoda está de volta ao Fortaleza,|e sem custo de contrato.",
    "O anúncio saiu na noite de terça, um dia depois|de ele recusar o 1º convite.",
    "Ele chega no lugar de Paulo Autuori, que caiu|depois da derrota para o Novorizontino.",
    "Na 1ª passagem, de 2021 a 2025,|foram 310 jogos e 5 títulos.",
    "Ele ainda levou o Fortaleza a 3 Libertadores|e à final da Sul-Americana de 2023.",
    "Agora a missão é curta:|3 jogos para voltar à Série A.",
    "Primeiro, o Vila Nova, no sábado, no Castelão.|Depois, o playoff de ida e volta contra o Criciúma.",
    "Quem vencer o mata-mata|sobe para a elite.",
]
FALA_TIKTOK = "O Fortaleza volta pra Série A? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SOBE OU NÃO?"
TWIST = 5
FLASH = [5]
CHECK = [(0, 'Fortaleza', 4), (0, 'contrato', 4), (1, 'terça', 4), (1, 'recusar', 4), (2, 'Autuori', 4),
         (2, 'Novorizontino', 4), (3, 'trezentos', 6), (3, 'títulos', 4), (4, 'Libertadores', 4), (4, 'Sul-Americana', 4),
         (5, 'três', 4), (6, 'Vila', 4), (6, 'Criciúma', 4), (7, 'elite', 4)]

FOR, FOR_F = time_('FORTALEZA')
VIL, VIL_F = time_('VILA NOVA')
CRI, CRI_F = time_('CRICIÚMA')
NOV, NOV_F = time_('NOVORIZONTINO')
TEC = ('#1c2233', '#1c2233', '#2b3245')   # agasalho escuro do treinador
TEC2 = ('#5b5f6b', '#5b5f6b', '#3a3d46')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def put_cal(c, dia, x, y, f, f0, h=380):
    if f < f0: return
    im = calendario(dia, 'NOV'); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def vojvoda(c, f, x=640, y=2030, h=900, arms='hang', expr='proud', placa_f0=0, py=None):
    put_jog(c, x, y, h, f, 7, cores=TEC, faixa=None, arms=arms, expr=expr, skin=0, hair='#6b4a2e')
    put_placa(c, 'VOJVODA', FOR, x, (y - h - 70) if py is None else py, f, placa_f0, 60, -3)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    fo = wt(0, 'Fortaleza') - 3; co = wt(0, 'contrato') - 3
    put_jog(c, 220, 1960, 620, f, 1, cores=FOR, faixa=FOR_F, arms='up', expr='grin', skin=2, hair='#151515')
    put_jog(c, 1030, 1960, 620, f, 2, cores=FOR, faixa=FOR_F, arms='up', expr='grin', skin=1, hair='#2b1d14')
    vojvoda(c, f, arms='up' if f >= fo else 'hang', expr='grin' if f >= fo else 'proud', placa_f0=0)
    num(c, 'VOLTOU!', 640, 720, f, fo, 170, -4)
    put_placa(c, 'FORTALEZA', FOR, 640, 900, f, fo + 2, 64, 3)
    num(c, 'CUSTO ZERO', 640, 1240, f, co, 90, -3)
    z = lerp(1.28, 1.04, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, co, .7)
    return c, (640, 1440 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    te = wt(1, 'terça') - 3; re = wt(1, 'recusar') - 3
    put_cal(c, '10', 330, 1010, f, te, 360)
    num(c, 'TERÇA À NOITE', 640, 720, f, te, 92, -3)
    vojvoda(c, f, x=850, h=860, arms='shrug' if re <= f < re + 40 else 'joinha' if f >= re + 40 else 'hang',
            expr='nervous' if re <= f < re + 40 else 'grin', placa_f0=0)
    num(c, 'NÃO...', 380, 1300, f, re, 100, -5)
    num(c, 'SIM!', 420, 1460, f, re + 40, 130, 4)
    return c, (640 + 25 * math.sin(f * .03), 1430, lerp(1.04, 1.14, smooth(f / 110)), 0), 'dusk'


def s2(f):
    c = estadio('day').copy()
    au = wt(2, 'Autuori') - 3; no = wt(2, 'Novorizontino') - 3
    put_jog(c, 380, 2030, 840, f, 8, cores=TEC2, faixa=None, arms='cheek' if f >= no else 'hang',
            expr='pained' if f >= no else 'neutral', skin=0, hair='#d9d9d9')
    put_placa(c, 'AUTUORI', TEC2, 380, 1110, f, au, 56, -3)
    put_jog(c, 900, 2000, 720, f, 9, cores=NOV, faixa=NOV_F, arms='up', expr='grin', skin=2, hair='#151515')
    put_placa(c, 'NOVORIZONTINO', NOV, 900, 1210, f, no, 50, 3)
    num(c, 'DERROTA', 640, 720, f, no, 140, -4)
    z = lerp(1.16, 1.05, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f)
    return c, (lerp(600, 680, smooth(f / 120)), 1430, z, 0), 'golden'


def s3(f):
    c = estadio('dusk').copy()
    an = wt(3, 'dois') - 3; tr = wt(3, 'trezentos') - 3; ti = wt(3, 'títulos') - 3
    num(c, '2021-2025', 640, 700, f, an, 130, -4)
    put_trofeu(c, 930, 1300, 440, f, ti)
    vojvoda(c, f, x=420, h=880, arms='up' if f >= ti else 'cintura', expr='grin' if f >= ti else 'proud', placa_f0=99999)
    num(c, '310 JOGOS', 640, 870, f, tr, 130, 3)
    num(c, '5 TÍTULOS', 640, 1030, f, ti, 120, -4)
    k = kick(f, ti, .8)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s4(f):
    c = estadio('day').copy()
    gx, gy = put_gol(c)
    li = wt(4, 'Libertadores') - 3; su = wt(4, 'Sul-Americana') - 4
    put_goleiro(c, f, ('#555a66', '#555a66', '#555a66'), None, arms='shrug', expr='shock' if f >= su else 'nervous', skin=0, hair='#3a3d46')
    put_jog(c, 470, 1990, 860, f, 3, cores=FOR, faixa=FOR_F, arms='up' if f >= su + 8 else 'run', kick=pulse(f, su - 5, 5),
            expr='grin' if f >= su else 'stern', skin=2, hair='#151515', num_='9')
    rb = raio_bola(860)
    if f < su - 5: bx, by, r = 640, 1990 - rb, rb
    else:
        t = ramp(f, su - 5, su + 3)
        bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, '3 LIBERTADORES', 640, 710, f, li, 92, -4)
    num(c, 'FINAL DA SULA 2023', 640, 870, f, su, 80, 3)
    k = kick(f, su)
    return c, (lerp(600, 680, smooth(f / 120)), 1470 + k * 10, 1.1 * (1 + .0007 * f), k), 'golden'


def s5(f):
    c = estadio('dusk').copy()
    tr = wt(5, 'três') - 3; se = wt(5, 'Série') - 3
    vojvoda(c, f, x=640, h=880, arms='point' if f >= tr else 'cintura', expr='stern', placa_f0=0)
    num(c, '3 JOGOS', 640, 720, f, tr, 180, -4)
    num(c, 'SÉRIE A', 640, 900, f, se, 130, 3)
    k = kick(f, tr)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 30))) * (1 + .0008 * f)
    return c, (640 + 15 * math.sin(f * .03), 1440 + k * 10, z, k), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    vi = wt(6, 'Vila') - 3; sa = wt(6, 'sábado') - 3; ca = wt(6, 'Castelão') - 3
    pl = wt(6, 'playoff') - 3; cr = wt(6, 'Criciúma') - 3
    ph = ramp(f, pl - 6, pl + 4)
    if ph < 1:
        put_jog(c, 360, 2030, 800, f, 1, cores=FOR, faixa=FOR_F, arms='run', expr='stern', skin=2, hair='#151515')
        put_jog(c, 900, 2030, 800, f, 4, cores=VIL, faixa=VIL_F, arms='run', expr='stern', skin=1, hair='#2b1d14', flip=True)
        put_placa(c, 'FORTALEZA', FOR, 360, 1150, f, 0, 52, -3)
        put_placa(c, 'VILA NOVA', VIL, 900, 1150, f, vi, 52, 3)
        put_cal(c, '14', 640, 1000, f, sa, 300)
        num(c, 'NO CASTELÃO', 640, 720, f, ca, 100, -3)
    else:
        put_jog(c, 360, 2030, 800, f, 1, cores=FOR, faixa=FOR_F, arms='run', expr='stern', skin=2, hair='#151515')
        put_jog(c, 900, 2030, 800, f, 5, cores=CRI, faixa=CRI_F, arms='run', expr='stern', skin=0, hair='#3a2414', flip=True)
        put_placa(c, 'FORTALEZA', FOR, 360, 1150, f, pl, 52, -3)
        put_placa(c, 'CRICIÚMA', CRI, 900, 1150, f, cr, 52, 3)
        num(c, 'PLAYOFF', 640, 720, f, pl, 150, -4)
        num(c, 'IDA E VOLTA', 640, 900, f, pl + 8, 90, 3)
    k = kick(f, pl)
    z = lerp(1.0, 1.08, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    return c, (640 + 20 * math.sin(f * .03), 1420 + k * 10, z, k), 'dusk'


def s7(f):
    c = estadio('dusk').copy()
    el = wt(7, 'elite') - 3
    put_trofeu(c, 640, 1150, 460, f, 0)
    put_jog(c, 300, 2040, 760, f, 1, cores=FOR, faixa=FOR_F, arms='up' if f >= el else 'cintura', expr='grin', skin=2, hair='#151515')
    put_jog(c, 980, 2040, 760, f, 5, cores=CRI, faixa=CRI_F, arms='up' if f >= el else 'cintura', expr='grin', skin=0, hair='#3a2414')
    num(c, 'SÉRIE A 2027', 640, 720, f, el, 110, -3)
    num(c, '?', 640, 1500, f, el + 6, 160, 4)
    z = lerp(1.0, 1.12, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1380, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'Fortaleza') - 3, 160, .9)
    s.ting(s.W(0, 'contrato') - 3, .3)
    s.thunk(s.W(1, 'recusar') - 3, 120, .6)
    s.thunk(s.W(2, 'Novorizontino') - 3, 140, .7)
    s.ting(s.W(3, 'títulos') - 3, .35)
    s.thunk(s.W(4, 'Sul-Americana') - 4, 120, 1.0)
    s.thunk(s.W(5, 'três') - 3, 180, .9)
    s.thunk(s.W(6, 'playoff') - 3, 140, .8)
    s.ting(s.W(7, 'elite') - 3, .3)
