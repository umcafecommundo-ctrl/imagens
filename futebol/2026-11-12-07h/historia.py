"""anima.futebol — 12/11/2026 07h — Vítor Pereira admite 'erro tremendo' ao aceitar o Flamengo em 2023.
Fontes (conferidas em 12/11/2026): Mix Vale e Sportbuzz (11/11/2026, entrevista ao portal português ZeroZero:
"Foi um erro tremendo"; só duas semanas de descanso entre Corinthians e Flamengo; "Eu nem pude começar a treinar";
energia "completamente a zeros"; 18 jogos, sem títulos; 58 anos; quer voltar a trabalhar na Inglaterra);
Trivela (02/11/2026: Flamengo 2023 sem Carioca, Recopa, Supercopa e Mundial, demitido após cerca de 3 meses;
Nottingham Forest: contratado em fevereiro, salvou o time, e-mail de demissão às 23h58 de 30/06);
A Bola (02/11/2026: quer voltar à Premier League).
Sem escudos/logos: times por plaquinhas e cores; treinador é boneco genérico."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'FLAMENGO  ·  BASTIDORES'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Vítor Pereira admitiu: aceitar o Flamengo foi um erro tremendo.",
    "A confissão repercutiu nesta quarta, numa entrevista ao site português ZeroZero.",
    "No fim de dois mil e vinte e dois, ele deixou o Corinthians e, pouco mais de um mês depois, já estava no Rio.",
    "Foram só duas semanas de descanso. Ele contou que chegou com a energia zerada e nem pôde começar a treinar.",
    "Em cerca de três meses, perdeu Supercopa, Recopa, Mundial e Carioca, e saiu sem nenhum título.",
    "Na mesma conversa, lembrou que foi demitido do Nottingham Forest por e-mail, dois minutos antes da meia-noite.",
    "Agora, aos cinquenta e oito anos, ele quer voltar a trabalhar na Inglaterra.",
]
CAPTXT = [
    "Vítor Pereira admitiu: aceitar o Flamengo|foi um erro tremendo.",
    "A confissão repercutiu nesta quarta, numa entrevista|ao site português ZeroZero.",
    "No fim de 2022, ele deixou o Corinthians e,|pouco mais de 1 mês depois, já estava no Rio.",
    "Foram só 2 semanas de descanso. Ele contou que chegou|com a energia zerada e nem pôde começar a treinar.",
    "Em cerca de 3 meses, perdeu Supercopa, Recopa,|Mundial e Carioca, e saiu sem nenhum título.",
    "Na mesma conversa, lembrou que foi demitido do Nottingham Forest|por e-mail, 2 minutos antes da meia-noite.",
    "Agora, aos 58 anos, ele quer voltar|a trabalhar na Inglaterra.",
]
FALA_TIKTOK = "Foi erro mesmo ir pro Flamengo? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 4
FLASH = [4]
CHECK = [(0, 'Flamengo', 4), (0, 'tremendo', 4), (1, 'ZeroZero', 4), (2, 'Corinthians', 4), (2, 'Rio', 4),
         (3, 'semanas', 4), (3, 'treinar', 4), (4, 'Supercopa', 4), (4, 'titulo', 4), (5, 'e-mail', 4),
         (5, 'meia-noite', 4), (6, 'Inglaterra', 4)]

FLA, FLA_F = time_('FLAMENGO')
COR, COR_F = time_('CORINTHIANS')
NFO, NFO_F = time_('NOTTINGHAM FOREST')
TEC = ('#1c2233', '#1c2233', '#2b3245')   # agasalho escuro do treinador
POR = ('#1f7a4a', '#c8102e', '#ffffff')
ING = ('#ffffff', '#c8102e', '#1d3f8f')


def put_trofeu(c, x, y, h, f, f0):
    if f < f0: return
    im = trofeu(); s = back(ramp(f, f0, f0 + 8)) * h / im.size[1]
    paste_c(c, im, x, y, s)


def vp(c, f, x=640, y=2030, h=900, arms='hang', expr='neutral', placa_f0=0, py=None, walk=None, flip=False):
    kw = dict(cores=TEC, faixa=None, arms=arms, expr=expr, skin=0, hair='#a8a8a8')
    if walk is not None: kw['walk'] = walk
    put_jog(c, x, y, h, f, 7, flip=flip, **kw)
    put_placa(c, 'VÍTOR PEREIRA', TEC, x, (y - h - 70) if py is None else py, f, placa_f0, 52, -3)


@lru_cache(maxsize=2)
def envelope():
    p = Pen(420, 300)
    p.shape([(20, 30), (400, 30), (400, 280), (20, 280)], (255, 255, 255), hexc('#dcdcdc'), 6, 10)
    p.line([(20, 30), (210, 170), (400, 30)], hexc('#8a8f9e'), 10, 4)
    return p.img


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    fl = wt(0, 'Flamengo') - 3; tr = wt(0, 'tremendo') - 3
    vp(c, f, x=640, h=900, arms='cheek' if f >= tr else 'hang', expr='pained' if f >= tr else 'nervous', placa_f0=0)
    put_placa(c, 'FLAMENGO', FLA, 640, 720, f, fl, 70, 3)
    num(c, 'ERRO TREMENDO!', 640, 900, f, tr, 88, -4)
    z = lerp(1.3, 1.05, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, tr, .9)
    return c, (640, 1440 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    qu = wt(1, 'quarta') - 3; ze = wt(1, 'ZeroZero') - 3; pt = wt(1, 'portugues') - 3
    num(c, 'ENTREVISTA', 640, 720, f, 0, 130, -3)
    put_placa(c, 'PORTUGAL', POR, 640, 880, f, pt, 60, 3)
    num(c, 'ZEROZERO', 640, 1040, f, ze, 110, -3)
    vp(c, f, x=lerp(640, 700, smooth(f / 120)), h=820, arms='point' if f >= qu else 'cintura', expr='stern', placa_f0=99999)
    return c, (640 + 25 * math.sin(f * .03), 1430, lerp(1.04, 1.14, smooth(f / 110)), 0), 'dusk'


def s2(f):
    c = estadio('day').copy()
    co = wt(2, 'Corinthians') - 3; ri = wt(2, 'Rio') - 3; me = wt(2, 'mes') - 3
    num(c, 'FIM DE 2022', 640, 700, f, wt(2, 'dois') - 3, 120, -4)
    put_placa(c, 'CORINTHIANS', COR, 370, 1180, f, co, 48, -4)
    put_placa(c, 'FLAMENGO', FLA, 900, 1180, f, ri, 48, 4)
    num(c, '+1 MÊS', 640, 880, f, me, 110, 3)
    t = smooth(ramp(f, co, ri + 6))
    vp(c, f, x=lerp(400, 880, t), h=820, arms='run', expr='stern', placa_f0=99999, walk=(f % 16) / 16 if 0 < t < 1 else 0)
    return c, (lerp(610, 670, t), 1430, 1.06 * (1 + .0007 * f), 0), 'golden'


def s3(f):
    c = estadio('dusk').copy()
    se = wt(3, 'semanas') - 3; en = wt(3, 'energia') - 3; tr = wt(3, 'treinar') - 3
    num(c, 'SÓ 2 SEMANAS', 640, 700, f, se, 120, -4)
    num(c, 'ENERGIA ZERADA', 640, 870, f, en, 100, 3)
    num(c, 'SEM TREINAR!', 640, 1040, f, tr, 100, -3)
    vp(c, f, x=640, h=880, arms='shrug' if f >= tr else 'hang', expr='pained' if f >= en else 'nervous', placa_f0=99999)
    if en <= f < tr: zzz(c, 860, 1180, f)
    k = kick(f, tr, .7)
    return c, (640, 1440 + k * 10, lerp(1.16, 1.05, easeOut(ramp(f, 0, 30))) * (1 + .0007 * f), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    nomes = [('SUPERCOPA', 'Supercopa'), ('RECOPA', 'Recopa'), ('MUNDIAL', 'Mundial'), ('CARIOCA', 'Carioca')]
    for i, (n, w) in enumerate(nomes):
        f0 = wt(4, w) - 3
        y = 720 + i * 120
        put_placa(c, n, FLA, 580, y, f, f0, 46, -2 if i % 2 == 0 else 2)
        num(c, 'X', 880, y, f, f0 + 4, 80, 0)
    ti = wt(4, 'titulo') - 3
    num(c, '0 TÍTULOS', 640, 1230, f, ti, 110, -3)
    put_jog(c, 640, 2040, 700, f, 3, cores=FLA, faixa=FLA_F, arms='cheek' if f >= ti else 'hang',
            expr='pained' if f >= ti else 'nervous', skin=2, hair='#151515')
    k = kick(f, ti, .8)
    z = lerp(1.0, 1.1, easeOut(ramp(f, 0, 50))) * (1 + .0006 * f)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s5(f):
    c = estadio('dusk').copy()
    no = wt(5, 'Nottingham') - 3; em = wt(5, 'e-mail') - 3; mn = wt(5, 'meia-noite') - 3
    put_placa(c, 'NOTTINGHAM FOREST', NFO, 640, 720, f, no, 54, -3)
    if f >= em:
        s = back(ramp(f, em, em + 8)); paste_c(c, envelope(), 440, 1000, .7 * s)
    num(c, '23:58', 850, 1000, f, mn, 110, 4)
    vp(c, f, x=640, h=820, arms='cheek' if f >= em else 'hang', expr='shock' if f >= em else 'neutral', placa_f0=99999)
    k = kick(f, em, .8)
    return c, (640 + 20 * math.sin(f * .03), 1430 + k * 10, lerp(1.04, 1.13, smooth(f / 120)), k), 'dusk'


def s6(f):
    c = estadio('day').copy()
    an = wt(6, 'cinquenta') - 3; ig = wt(6, 'Inglaterra') - 3
    num(c, '58 ANOS', 640, 720, f, an, 140, -4)
    put_placa(c, 'INGLATERRA', ING, 640, 900, f, ig, 70, 3)
    vp(c, f, x=640, h=880, arms='joinha' if f >= ig else 'cintura', expr='grin' if f >= ig else 'proud', placa_f0=0)
    z = lerp(1.0, 1.12, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1400, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'tremendo') - 3, 160, .9)
    s.ting(s.W(1, 'ZeroZero') - 3, .3)
    s.thunk(s.W(2, 'Rio') - 3, 140, .6)
    s.thunk(s.W(3, 'treinar') - 3, 140, .7)
    s.thunk(s.W(4, 'Supercopa') - 3, 160, .6)
    s.thunk(s.W(4, 'titulo') - 3, 200, .9)
    s.thunk(s.W(5, 'e-mail') - 3, 140, .8)
    s.ting(s.W(6, 'Inglaterra') - 3, .3)
