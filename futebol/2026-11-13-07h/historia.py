"""anima.futebol — 13/11/2026 07h — Seleção Brasileira: na véspera do Japão, Ancelotti confirma Raphinha de camisa 9.
Fontes (conferidas em 13/11/2026): Terra (coletiva na véspera em Singapura: "Raphinha faz bem o centroavante e não quero
mudar essa ideia"; 4-3-3; Estêvão, Vini Jr. e Raphinha prováveis; Raphinha com a 9; Bruno dúvida; "A saúde do jogador é a
nossa prioridade. Se ele treina 100%, joga."); Portal Democrata 13/11 (Raphinha centroavante titular com a 9, 4-3-3,
"A saúde do jogador é a nossa prioridade", "Se ele treina 100%, joga", Bruno não treinou por precaução); Gazeta Esportiva
11/11 e ABCD Jornal 11/11 (Raphinha capitão; Brasil x Japão sábado 14/11 7h15 de Brasília, Singapura; Bruno Guimarães
poupado dos treinos intensos); CNN Brasil 11/11 (7h15).
Sem escudos/logos: times por plaquinhas e cores; jogadores genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD)
SELO = 'SELEÇÃO BRASILEIRA  ·  AMISTOSO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Raphinha é o camisa nove: Ancelotti confirmou o atacante no comando do ataque contra o Japão.",
    "Na entrevista em Singapura, o técnico disse que Raphinha faz bem o centroavante e que não quer mudar essa ideia.",
    "E tem mais: além da camisa nove, Raphinha também vai usar a faixa de capitão.",
    "O esquema deve ser o quatro, três, três, com Estêvão e Vini Júnior abertos pelos lados.",
    "A dúvida é Bruno Guimarães, que ficou fora de treinos por precaução nesta semana.",
    "Ancelotti avisou: a saúde do jogador é prioridade, e quem treina cem por cento, joga.",
    "Brasil e Japão jogam amanhã, sábado, às sete e quinze da manhã de Brasília, em Singapura.",
]
CAPTXT = [
    "Raphinha é o camisa 9: Ancelotti confirmou|o atacante no comando do ataque contra o Japão.",
    "Na entrevista em Singapura, o técnico disse que|Raphinha faz bem o centroavante e que não quer mudar essa ideia.",
    "E tem mais: além da camisa 9, Raphinha|também vai usar a faixa de capitão.",
    "O esquema deve ser o 4-3-3, com Estêvão|e Vini Júnior abertos pelos lados.",
    "A dúvida é Bruno Guimarães, que ficou fora|de treinos por precaução nesta semana.",
    "Ancelotti avisou: a saúde do jogador é prioridade,|e quem treina 100%, joga.",
    "Brasil e Japão jogam amanhã, sábado, às 7h15|de Brasília, em Singapura.",
]
FALA_TIKTOK = "Raphinha de camisa nove: aprova ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "APROVA?"
TWIST = 3
FLASH = [2]
CHECK = [(0, 'Raphinha', 4), (0, 'Japao', 4), (1, 'Singapura', 4), (1, 'ideia', 4), (2, 'capitao', 4),
         (3, 'tres', 4), (3, 'Vini', 4), (4, 'Bruno', 4), (4, 'precaucao', 4), (5, 'saude', 4), (5, 'joga', 4),
         (6, 'quinze', 4), (6, 'Singapura', 4)]

BRA, BRA_F = time_('BRASIL')
JAP, JAP_F = time_('JAPÃO')
TEC = ('#23283a', '#23283a', '#23283a')


def put_cal(c, dia, x, y, s, f, f0):
    if f >= f0: paste_c(c, calendario(dia, 'NOV'), x, y, s * back(ramp(f, f0, f0 + 8)))


def raph(c, x, y, h, f, **kw):
    put_jog(c, x, y, h, f, 3, cores=BRA, faixa=BRA_F, skin=1, hair='#2b1d14', num_='9', **kw)


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    ra = wt(0, 'Raphinha') - 3; nv = wt(0, 'nove') - 3; an = wt(0, 'Ancelotti') - 3; ja = wt(0, 'Japao') - 3
    y = lerp(2600, 2030, easeOut(ramp(f, ra - 6, ra + 6)))
    raph(c, 640, y, 900, f, arms='up' if f >= nv else 'cintura', expr='grin')
    put_placa(c, 'RAPHINHA', BRA, 640, 1060, f, ra, 60, -3)
    num(c, 'CAMISA 9', 640, 760, f, nv, 150, -4)
    num(c, 'CONTRA O JAPÃO', 640, 910, f, ja, 84, 3)
    if f >= an - 6:
        xx = lerp(1550, 1060, easeOut(ramp(f, an - 6, an + 6)))
        put_jog(c, xx, 2000, 640, f, 9, cores=TEC, faixa=None, arms='point', expr='proud', skin=0, hair='#9a9a9a', flip=True)
        put_placa(c, 'ANCELOTTI', TEC, 1040, 1300, f, an, 36, 3)
    z = lerp(1.25, 1.03, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    k = kick(f, nv, .7)
    return c, (640, 1420 + k * 10, z, k), 'dusk'


def s1(f):
    c = CEN('cidade', 'dusk').copy()
    si = wt(1, 'Singapura') - 3; ce = wt(1, 'centroavante') - 3; mu = wt(1, 'mudar') - 3
    xx = lerp(-400, 420, easeOut(ramp(f, 0, 20)))
    put_jog(c, xx, 2010, 840, f, 9, cores=TEC, faixa=None, arms='point' if f >= ce else 'cintura', expr='proud', skin=0, hair='#9a9a9a')
    put_placa(c, 'ANCELOTTI', TEC, 420, 1170, f, 4, 46, -3)
    if f >= ce - 6:
        rx = lerp(1550, 900, easeOut(ramp(f, ce - 6, ce + 6)))
        raph(c, rx, 1990, 780, f, arms='joinha', expr='grin')
    num(c, 'SINGAPURA', 640, 720, f, si, 110, -4)
    num(c, 'FAZ BEM O CENTROAVANTE', 640, 860, f, ce, 56, 3)
    num(c, 'NÃO VAI MUDAR', 640, 990, f, mu, 84, -3)
    return c, (lerp(600, 680, smooth(f / 120)), 1420, 1.06 * (1 + .0008 * f), 0), 'dusk'


def s2(f):
    c = estadio('dusk').copy()
    nv = wt(2, 'nove') - 3; fa = wt(2, 'faixa') - 3; ca = wt(2, 'capitao') - 3
    raph(c, 640, 2030, 880, f, arms='up' if f >= ca else 'cintura', expr='proud' if f >= ca else 'grin')
    num(c, '9', 360, 1150, f, nv, 170, -6)
    if f >= fa:
        s = back(ramp(f, fa, fa + 8))
        band = Image.new('RGBA', (220, 90), (0, 0, 0, 0)); d = ImageDraw.Draw(band)
        d.rounded_rectangle([4, 4, 216, 86], 20, fill=(255, 216, 74, 255), outline=INK + (255,), width=6)
        fo = ImageFont.truetype(FONTB, 64); tw = d.textlength('C', font=fo); d.text(((220 - tw) / 2, 4), 'C', font=fo, fill=INK + (255,))
        paste_c(c, band, 940, 1150, s)
    num(c, 'CAPITÃO!', 640, 780, f, ca, 150, -4)
    for x, sd, sk in ((200, 11, 3), (1080, 12, 2)):
        put_jog(c, x, 1960, 620, f, sd, cores=BRA, faixa=BRA_F, arms='up' if f >= ca + 4 else 'hang', expr='grin', skin=sk,
                hair='#111111', flip=x > 640)
    k = kick(f, ca, .8)
    return c, (640, 1440 + k * 10, lerp(1.0, 1.08, smooth(f / 90)), k), 'dusk'


def s3(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c, x=700)
    tr = wt(3, 'tres') - 3; es = wt(3, 'Estevao') - 3; vi = wt(3, 'Vini') - 3; la = wt(3, 'lados') - 3
    put_goleiro(c, f, JAP, JAP_F, gx=720, arms='shrug', expr='shock' if f >= la else 'nervous', skin=0, hair='#111111')
    raph(c, 560, 2030, 860, f, arms='run', expr='grin', kick=pulse(f, la - 5, 5))
    put_placa(c, 'RAPHINHA', BRA, 560, 1000, f, 0, 36, -3)
    for w, nome, x, sd, sk, f0 in (('Estevao', 'ESTÊVÃO', 1020, 4, 2, es), ('Vini', 'VINI JR.', 220, 2, 3, vi)):
        if f < f0 - 4: continue
        yy = lerp(2500, 1990, easeOut(ramp(f, f0 - 4, f0 + 6)))
        put_jog(c, x, yy, 740, f, sd, cores=BRA, faixa=BRA_F, arms='up' if f >= la + 8 else 'run', expr='grin', skin=sk,
                hair='#111111', flip=x > 640)
        put_placa(c, nome, BRA, x, 1130, f, f0, 36, -3 if x < 640 else 3)
    rb = raio_bola(860)
    if f < la - 3: bx, by, r = 660, 2030 - rb, rb
    else:
        t = ramp(f, la - 3, la + 6)
        bx, by, r = lerp(660, gx + 90, t), lerp(2030 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, '4-3-3', 640, 780, f, tr, 170, -3)
    k = kick(f, la + 4)
    return c, (640 + 30 * math.sin(f * .03), 1420 + k * 10, lerp(1.0, 1.05, smooth(f / 110)), k), 'dusk'


def s4(f):
    c = estadio('day').copy()
    du = wt(4, 'duvida') - 3; br = wt(4, 'Bruno') - 3; pr = wt(4, 'precaucao') - 3
    num(c, 'DÚVIDA', 640, 740, f, du, 140, -4)
    bxp = lerp(-300, 560, easeOut(ramp(f, br - 8, br + 6)))
    put_jog(c, bxp, 2030, 860, f, 6, cores=BRA, faixa=BRA_F, arms='shrug' if f >= br + 6 else 'run', expr='nervous', skin=1,
            walk=(f * .06) % 1 if f < br + 6 else 0)
    put_placa(c, 'BRUNO GUIMARÃES', BRA, 560, 1100, f, br, 40, -3)
    num(c, '?', 1000, 1200, f, br + 6, 220, 8)
    num(c, 'POR PRECAUÇÃO', 640, 900, f, pr, 84, 3)
    z = lerp(1.08, 1.0, easeOut(ramp(f, 0, 50))) * (1 + .0012 * f)
    return c, (640 + 25 * math.sin(f * .05), lerp(1380, 1440, smooth(f / 120)), z, .8 * math.sin(f * .04)), 'golden'


def s5(f):
    c = estadio('dusk').copy()
    sa = wt(5, 'saude') - 3; ce = wt(5, 'cem') - 3; jo = wt(5, 'joga') - 3
    put_jog(c, 420, 2030, 860, f, 9, cores=TEC, faixa=None, arms='point' if f >= sa else 'cintura', expr='stern' if f < jo else 'proud',
            skin=0, hair='#9a9a9a')
    put_placa(c, 'ANCELOTTI', TEC, 420, 1110, f, 0, 46, -3)
    num(c, 'SAÚDE EM 1º LUGAR', 640, 740, f, sa, 82, -3)
    num(c, '100% = JOGA', 680, 900, f, ce, 96, 4)
    if f >= jo - 4:
        xx = lerp(1550, 960, easeOut(ramp(f, jo - 4, jo + 6)))
        put_jog(c, xx, 1990, 760, f, 7, cores=BRA, faixa=BRA_F, arms='joinha', expr='grin', skin=2, hair='#111111', flip=True)
    k = kick(f, jo, .6)
    return c, (640 + 20 * math.sin(f * .04), 1420 + k * 8, lerp(1.04, 1.1, smooth(f / 100)), k), 'dusk'


def s6(f):
    c = estadio('dusk').copy()
    br = wt(6, 'Brasil') - 3; ja = wt(6, 'Japao') - 3
    bx = lerp(-300, 330, easeOut(ramp(f, br - 8, br + 8)))
    ax = lerp(1550, 930, easeOut(ramp(f, ja - 8, ja + 8)))
    raph(c, bx, 2010, 860, f, arms='cintura', expr='stern', look=1)
    put_jog(c, ax, 2010, 860, f, 6, cores=JAP, faixa=JAP_F, arms='cintura', expr='smug', skin=0, hair='#111111', look=-1)
    put_placa(c, 'BRASIL', BRA, 330, 1180, f, br + 2, 64, -4)
    put_placa(c, 'JAPÃO', JAP, 930, 1180, f, ja + 2, 64, 4)
    num(c, 'X', 640, 1520, f, ja + 4, 160)
    put_cal(c, '14', 300, 790, .6, f, wt(6, 'sabado') - 3)
    num(c, '7H15', 840, 790, f, wt(6, 'quinze') - 3, 140, -4)
    num(c, 'SINGAPURA', 640, 980, f, wt(6, 'Singapura') - 3, 90, 3)
    z = lerp(1.2, 1.05, easeOut(ramp(f, 0, 35))) * (1 + .0007 * f)
    k = kick(f, ja, .6)
    return c, (640, 1400 + k * 8, z, k), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6]


def SFX(s):
    s.thunk(s.W(0, 'nove') - 3, 140, .8)
    s.ting(s.W(1, 'centroavante') - 3, .3)
    s.thunk(s.W(2, 'capitao') - 3, 180, .9)
    s.thunk(s.W(3, 'lados') - 3, 140, .8)
    s.ting(s.W(4, 'duvida') - 3, .25)
    s.ting(s.W(5, 'joga') - 3, .3)
    s.ting(s.W(6, 'quinze') - 3, .3)
