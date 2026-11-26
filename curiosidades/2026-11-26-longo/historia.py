"""VÍDEO LONGO (YouTube normal, horizontal 16:9, ~2 min) no formato MISTÉRIO: "O cachorro do ônibus doze" (26/11/2026).
História inventada, completa (sem partes). Renderize com MOTOR_H=1. Desenhos novos em assets.py (cachorro, ônibus, ponto, rua,
dentro do ônibus, esquina, casa velha da janela azul, casa do avô, campo do ponto final, sala).
Narrador: menino de cabelo escuro curto, moletom vermelho (capa de chuva amarela do avô no dia da chuva).
Avô (Tonico): careca de cabelo branco, óculos, blusa marrom. Seu Dito: motorista de barba, uniforme azul.
Premissa: todo dia às 7h15 um cachorro caramelo de orelha preta pega sozinho o ônibus 12, senta no primeiro banco da janela e desce
4 pontos depois; regra: ninguém senta no banco dele; ele vira a esquina e some; seu Dito diz que ele já pegava o ônibus quando ele era
criança. Numa segunda de chuva o narrador, com a capa amarela velha do avô, cai sentado no banco; o cachorro cheira a capa, deita nos
pés dele e não desce: vai até o ponto final e o leva a uma casa velha de janela azul; no batente, marcas de altura e "TONICO E FAROFA".
Tonico é o avô. Em casa o avô fica pálido: "Farofa?"; a foto do avô menino com o cachorro no ônibus 12; os dois iam juntos pra escola
(4 pontos); o Farofa sumiu no dia da mudança, há 60 anos. Fim: o Farofa dorme no tapete do avô e não envelheceu nem um dia.
Cores: s0 CAPA close (vivo) | s1-s4 dia (vivo) | s5 seu Dito (tarde) | s6-s15 chuva/neblina (sombrio) | s16-s18 casa do avô, foto,
lembrança em sépia (tarde) | s19 dia (vivo) -> sala (tarde) -> CLOSE final (frio). Closes: s0, s9, s15, s16 (avô), s19."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import kit
from sombrio import *
from longo import *
from assets import *

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
LINES = [
    "Na minha cidade, todo dia, às sete e quinze, um cachorro caramelo pega o ônibus doze. Sozinho.",
    "Ele tem uma orelha preta e senta sempre no mesmo lugar: o primeiro banco, do lado da janela.",
    "E desce exatamente quatro pontos depois. Nem um a mais, nem um a menos.",
    "A cidade tem uma regra: ninguém senta no banco do cachorro. Nem com o ônibus lotado.",
    "Ninguém sabe de quem ele é. Quando desce, ele vira a esquina e some.",
    "O motorista, seu Dito, jura que esse cachorro já pegava o ônibus doze quando ele era criança.",
    "Numa segunda-feira de chuva, eu saí atrasado, com a capa amarela velha do meu avô.",
    "O ônibus estava lotado. Ele deu uma freada, eu tropecei... e caí sentado no banco do cachorro.",
    "O ônibus inteiro ficou em silêncio. No ponto da praça, a porta abriu. E ele subiu.",
    "Ele me olhou por muito tempo. Cheirou a capa amarela. E deitou nos meus pés.",
    "No quarto ponto, a porta abriu. E ele não desceu.",
    "Quinto ponto. Sexto. Sétimo. Até o ponto final, onde eu nunca tinha ido.",
    "Ele desceu, olhou pra trás e ficou me esperando. Eu desci também.",
    "Ele me levou até uma casa velha, de janela azul, e arranhou a porta.",
    "No batente, tinha risquinhos de altura, de criança. E escrito com canivete: Tonico e Farofa.",
    "Tonico... é o apelido do meu avô.",
    "O cachorro me seguiu até em casa. Quando o meu avô abriu a porta, ficou pálido e disse baixinho: Farofa?",
    "Ele buscou uma caixa velha e me mostrou uma foto: ele, menino, no ônibus doze, com um cachorro de orelha preta.",
    "Todo dia, os dois iam juntos pra escola. Quatro pontos. No dia da mudança, faz sessenta anos, o Farofa sumiu.",
    "Hoje, o ônibus doze passa vazio às sete e quinze. O Farofa dorme no tapete do meu avô. E não envelheceu nem um dia.",
]
FALA_TIKTOK = "Você sentaria no banco do cachorro? Comenta sim ou não."
CTA_TEXTO = "SIM OU NÃO?"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 15
FLASH = []
CAPA = 36
CAM = {}

EU = dict(penteado='curto', cabelo='#2e2018', pele='#e0b48a', roupa='#c0453a', calca='#3b5a8a')
CAPA_ = dict(EU, roupa='#f2c230')
AVO = dict(penteado='careca', cabelo='#e8e8e2', pele='#e0b48a', roupa='#8a6a4a', calca='#4a4036', oculos=True, velho=True)
MENINO_AVO = dict(penteado='curto', cabelo='#5a3a22', pele='#e0b48a', roupa='#4f8fc0', calca='#6a5a40')
DITO = dict(penteado='curto', cabelo='#26241f', pele='#8a5a3a', roupa='#3a6a8a', calca='#2d2f32', barba=True)
PASS = [dict(penteado='longo', cabelo='#7a4a2a', pele='#f0c8a0', roupa='#5aa36f', calca='#3b3f44'),
        dict(penteado='coque', cabelo='#cfcfcf', pele='#c8956b', roupa='#7a5ab0', calca='#4a4036', velho=True),
        dict(penteado='curto', cabelo='#26241f', pele='#8a5a3a', roupa='#e0a43c', calca='#2d2f32'),
        dict(penteado='careca', cabelo='#3a2a20', pele='#f0c8a0', roupa='#4f8fc0', calca='#2d2f32', barba=True),
        dict(penteado='longo', cabelo='#26241f', pele='#e0b48a', roupa='#d9634f', calca='#3b5a8a')]

CHECK = [(0, 'onibus', 10), (0, 'sozinho', 6), (1, 'preta', 8), (1, 'primeiro', 8), (2, 'quatro', 6), (3, 'regra', 8), (3, 'lotado', 8),
         (4, 'esquina', 4), (4, 'some', 8), (5, 'crianca', 10), (6, 'capa', 8), (7, 'freada', 4), (7, 'sentado', 6), (8, 'subiu', 10),
         (9, 'cheirou', 6), (9, 'deitou', 14), (10, 'desceu', 6), (11, 'setimo', 4), (11, 'final', 12), (12, 'esperando', 4),
         (12, 'desci', 12), (13, 'janela', 8), (13, 'arranhou', 8), (14, 'risquinhos', 6), (14, 'tonico', 8), (15, 'avo', 4),
         (16, 'abriu', 8), (16, 'farofa', 6), (17, 'foto', 10), (17, 'preta', 6), (18, 'quatro', 6), (18, 'sumiu', 6),
         (19, 'quinze', 4), (19, 'tapete', 6), (19, 'dia', 6)]


def SFX(s):
    s.engine(s.W(0, 'onibus') - 30, s.W(0, 'sozinho') + 20, .2)
    s.thunk(s.W(0, 'sozinho') - 2, 90, .7)
    s.engine(0, s.W(1, 'janela') + 30, .12 + 0) if False else s.engine(s.W(1, 'ele') + 1, s.W(1, 'janela') + 30, .12)
    s.ting(s.W(1, 'preta'), .3)
    s.thunk(s.W(2, 'desce') - 2, 200, .4)
    for w in ('quatro', 'mais', 'menos'): s.ting(s.W(2, w), .2)
    s.thunk(s.W(3, 'regra') - 2, 90, .8)
    s.whoosh(s.W(4, 'esquina') - 6, .5, .25)
    s.thunk(s.W(4, 'some') - 2, 70, .8)
    s.trill(s.W(5, 'crianca'), .6, .12)
    s.patter(s.W(6, 'chuva') - 10, s.W(6, 'avo') + 30, 6, .12)
    s.patter(s.W(7, 'onibus'), s.W(10, 'desceu') + 20, 4, .05)
    s.engine(s.W(7, 'onibus'), s.W(7, 'freada'), .18)
    s.whoosh(s.W(7, 'freada') - 4, .6, .4); s.thunk(s.W(7, 'freada'), 120, .7)
    s.thunk(s.W(7, 'sentado') - 2, 80, .9)
    s.thunk(s.W(8, 'silencio') - 2, 60, .7)
    s.whoosh(s.W(8, 'porta') - 4, .5, .25)
    s.thunk(s.W(8, 'subiu') - 2, 120, .6)
    s.ting(s.W(9, 'cheirou'), .25)
    s.thunk(s.W(9, 'deitou') + 6, 60, 1.0)
    s.whoosh(s.W(10, 'porta') - 4, .5, .25)
    s.thunk(s.W(10, 'desceu') - 2, 70, .9)
    for w in ('quinto', 'sexto', 'setimo'): s.ting(s.W(11, w), .25)
    s.engine(s.W(11, 'quinto') - 10, s.W(11, 'final'), .22)
    s.thunk(s.W(11, 'final') - 2, 90, .8)
    s.thunk(s.W(12, 'desci') - 2, 160, .5)
    for i in range(5): s.thunk(s.W(13, 'arranhou') + i * 5, 300, .25)
    s.ting(s.W(14, 'risquinhos'), .25)
    s.thunk(s.W(14, 'tonico') - 2, 70, .9)
    s.thunk(s.W(16, 'abriu') - 2, 150, .5)
    s.thunk(s.W(16, 'farofa') - 2, 60, .9)
    s.whoosh(s.W(17, 'foto') - 4, .5, .3); s.ting(s.W(17, 'preta'), .3)
    s.whoosh(s.W(18, 'mudanca') - 6, .6, .3)
    s.thunk(s.W(18, 'sumiu') - 2, 70, .9)
    s.engine(s.W(19, 'onibus') - 10, s.W(19, 'quinze') + 20, .2)
    s.trill(s.W(19, 'envelheceu'), .6, .1)
    s.thunk(s.W(19, 'dia') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z_, _ = CAM.get(si, (W_ / 2, H_ / 2, 1, 0))
    k = OW / W_ * z_
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


def z(v, f, k=.0008):
    return v * (1 + k * f)


def W(si, w):
    return wt(si, w) - 3


# ---------------------------------------------------------------- figuras prontas
@lru_cache(maxsize=2)
def foto_img():
    """foto antiga (sépia): o avô menino no banco do ônibus 12 com o cachorro do lado."""
    c = interior(0, 'tarde', scroll=500).copy()
    sentado(c, BANCOS[1], 5, expr='sorriso', look=-.5, **MENINO_AVO)
    put_cao(c, BANCOS[0], ASSENTO + 20, 420, 0, pose='sentado', look=.5, cauda=0.0)
    assentos(c, 'tarde')
    ph = sepia_img(c.crop((260, 120, 1260, 1150)))
    ph = ph.resize((760, 783), Image.LANCZOS)
    fr = Image.new('RGBA', (820, 900), (244, 236, 214, 255))
    fr.alpha_composite(ph, (30, 30))
    d = ImageDraw.Draw(fr); d.rectangle((0, 0, 819, 899), outline=(36, 30, 32, 255), width=6)
    d.text((40, 830), 'ônibus 12', font=font(F_MAO_L, 40), fill=(90, 70, 60, 255))
    return fr.rotate(-4, Image.BICUBIC, expand=True)


@lru_cache(maxsize=2)
def lembranca_dito():
    c = Image.new('RGBA', (520, 420), (250, 240, 220, 255))
    put_menino(c, 170, 405, 380, 0, expr='sorriso', look=.5, **dict(DITO, barba=False, roupa='#d9634f'))
    put_cao(c, 380, 405, 300, 0, pose='sentado', look=-.5, flip=True, cauda=0.0)
    return sepia_img(c)


def passageiros(c, f, sent=(1, 2, 3, 4, 5), pe=(), expr='neutro', look=0.0):
    for k, i in enumerate(sent):
        sentado(c, BANCOS[i], f, seed=10 + i, expr=expr, look=look, **PASS[i % 5])
    return c


def em_pe(c, f, xs, expr='neutro', look=0.0, tilt=0.0):
    for k, x in enumerate(xs):
        q = dict(PASS[(k + 2) % 5])
        if tilt: q['tilt'] = tilt
        put_menino(c, x, 1215, 740, f, seed=20 + k, expr=expr, look=look, **q)


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close à direita + gancho à esquerda
        c = rua2_bg('dia').copy(); put_ponto(c, 300, 1180)
        put_onibus(c, 60, 1050, luz='dia')
        c = close_h(c, f, expr='choque', look=-.5, x=1560, s=.92, shake=.2, **EU)
        cam = (1104, 621, z(1.0, f), 0); CAM[0] = cam
        return c, cam, 'vivo'
    g = f - CAPA
    c = rua2_bg('dia').copy()
    ob = W(0, 'onibus')
    put_onibus(c, lerp(-2000, -412, easeOut(ramp(f, ob - 24, ob + 12))), 1050, luz='dia')
    put_ponto(c, 330, 1180)
    so = W(0, 'sozinho')
    put_cao(c, 760, 1180, 420, f, pose='sentado', look=-1 if ob - 20 < f < so else 1, cabeca=.5 if f >= so else 0)
    t = smooth(ramp(g, 0, 140))
    cam = (lerp(1000, 800, t), lerp(680, 760, t), z(lerp(1.2, 1.45, t), g) + .05 * kick(f, so, .6), 0); CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = interior(f, 'dia')
    passageiros(c, f, sent=(2, 4), look=-1 if f > W(1, 'lugar') else 0)
    put_cao(c, BANCOS[0], ASSENTO + 20, 420, f, pose='sentado', look=.5)
    assentos(c, 'dia')
    ex, ey = cabeca_cao(BANCOS[0], ASSENTO + 20, 420, pose='sentado')
    lu = W(1, 'lugar')
    t = smooth(ramp(f, lu - 6, lu + 20))
    cam = (lerp(ex - 60, 900, t), lerp(ey + 40, 640, t), z(lerp(2.3, 1.35, t), f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = rua2_bg('dia').copy()
    de = W(2, 'desce')
    dx = put_onibus(c, 300, 1050, luz='dia', aberta=round(ramp(f, de - 20, de - 8) * 4) / 4)
    t = ramp(f, de, de + 14)
    x = lerp(dx, dx + 160, t) + max(0, f - de - 14) * 7
    y = lerp(1050, 1180, t) - 90 * math.sin(math.pi * t)
    put_cao(c, x, y, 420, f, pose='pe', walk=1 if f > de + 14 else 0, look=.5)
    cam = (lerp(1500, 1700, ramp(f, 0, 160)), 700, z(1.3, f), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = interior(f, 'dia')
    passageiros(c, f, look=-.5)
    g = Image.new('RGBA', c.size, (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((380, 560, 820, 980), fill=(255, 230, 140, 90))
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(40)))
    assentos(c, 'dia')
    lo = W(3, 'lotado')
    em_pe(c, f, [1000, 1420, 1840] + ([1210, 1630, 2050] if f >= lo else []), look=-.75)
    t = smooth(ramp(f, W(3, 'nem') - 10, lo + 10))
    cam = (lerp(720, 1180, t), lerp(720, 640, t), z(lerp(1.8, 1.1, t), f), 0); CAM[3] = cam
    return c, cam, 'vivo'


def s4(f):
    so = W(4, 'some')
    if f >= so + 4:   # depois da esquina: rua vazia
        c = rua2_bg('dia', 600).copy()
        cam = (1104, 680, z(1.25, f - so), 0); CAM[4] = cam
        return c, cam, 'vivo'
    c = rua2_bg('dia').copy()
    de = W(4, 'quando')
    x = lerp(500, 1800, ramp(f, de, so))
    put_cao(c, x, 1180, 420, f, pose='pe', walk=1 if de <= f < so else 0, look=.5)
    c.alpha_composite(esquina_img('dia'), (1500, 0))
    cam = (lerp(900, 1250, smooth(ramp(f, 0, so))), 700, z(1.2, f), 0); CAM[4] = cam
    return c, cam, 'vivo'


def s5(f):
    c = rua2_bg('tarde').copy()
    put_onibus(c, -230, 1050, luz='tarde')
    put_cao(c, 1080, 1180, 420, f, pose='sentado', look=1)
    put_menino(c, 1500, 1180, 760, f, seed=4, flip=True, expr='sorriso' if f < W(5, 'jura') else 'curioso', look=-.5, **DITO)
    cr = W(5, 'crianca')
    thought(c, 1880, 330, 230, back(ramp(f, cr - 4, cr + 8)), lembranca_dito().resize((380, 307), Image.LANCZOS))
    t = smooth(ramp(f, 0, cr))
    cam = (lerp(1250, 1480, t), lerp(700, 620, t), z(lerp(1.35, 1.3, t), f), 0); CAM[5] = cam
    return c, cam, 'tarde'


def s6(f):
    c = rua2_bg('neblina', int(f * 12)).copy()
    put_menino(c, 1000, 1180, 700, f, walk=1, expr='preocupado' if f < W(6, 'capa') else 'neutro', look=.75, **CAPA_)
    chuva(c, f)
    cam = (1050, lerp(700, 760, ramp(f, 0, 150)), z(1.35, f), 0); CAM[6] = cam
    return c, cam, 'frio'


def s7(f):
    fr = W(7, 'freada'); se = W(7, 'cai')
    c = interior(f, 'neblina', anda=1 if f < fr else .3, rain=True)
    passageiros(c, f)
    if f >= se:
        sentado(c, BANCOS[0], f, expr='choque', look=.5, **CAPA_)
    assentos(c, 'neblina')
    tl = 8 * pulse(f, fr, 20) if f < se else 0
    em_pe(c, f, [1210, 1630, 2030], expr='choque' if f >= fr else 'neutro', look=-.5, tilt=round(tl))
    if f < se:
        put_menino(c, 780 + 40 * ramp(f, fr, se) - 60 * ramp(f, se - 6, se), 1215, 720, f, expr='choque' if f >= fr else 'neutro',
                   look=-.5, tilt=round(tl * 1.5), **CAPA_)
    put_dust(c, BANCOS[0], 900, 160, f - se)
    roll = 3 * pulse(f, fr, 24)
    cam = (lerp(1000, 760, smooth(ramp(f, fr, se + 10))), 680, z(lerp(1.25, 1.5, smooth(ramp(f, fr, se + 10))), f) + .06 * kick(f, se, .7), roll)
    CAM[7] = cam
    return c, cam, 'frio'


def s8(f):
    po = W(8, 'porta'); su = W(8, 'subiu')
    c = interior(f, 'neblina', aberta=ramp(f, po, po + 10), scroll=1300, rain=True)
    passageiros(c, f, expr='choque', look=-1)
    sentado(c, BANCOS[0], f, expr='preocupado' if f < su else 'choque', look=-1 if f >= po else 0, **CAPA_)
    assentos(c, 'neblina')
    if f >= su:
        put_cao(c, lerp(250, 330, ramp(f, su, su + 20)), 1195, 440, f, pose='pe', walk=1 if f < su + 20 else 0, look=.5)
    em_pe(c, f, [1420, 1880], expr='choque', look=-1)
    t = smooth(ramp(f, 0, po))
    cam = (lerp(1100, 700, t), lerp(640, 820, t), z(lerp(1.15, 1.4, t), f) + .05 * kick(f, su, .6), 0); CAM[8] = cam
    return c, cam, 'frio'


def s9(f):
    ch = W(9, 'cheirou'); de = W(9, 'deitou')
    c = interior(f, 'neblina', anda=.5, rain=True)
    passageiros(c, f, sent=(2, 3, 4, 5), expr='choque', look=-1)
    sentado(c, BANCOS[0], f, expr='preocupado' if f < ch else 'choque', look=.75, **CAPA_)
    assentos(c, 'neblina')
    if f < de:
        put_cao(c, lerp(980, 860, ramp(f, ch - 4, ch + 10)), 1200, 440, f, pose='pe', flip=True, look=.5,
                cabeca=1 if f >= ch else .5, cauda=0.0)
    else:
        put_cao(c, 800, 1210, 440, f, pose='deitado', flip=True, look=.5)
    if f >= de + 8:   # CLOSE (descoberta)
        c = close_h(c, f, expr='choque', look=.5, s=.92, shake=.3, **CAPA_)
        cam = (1104, 621, z(lerp(1.2, 1.03, easeOut(ramp(f, de + 8, de + 18))), f - de), 0); CAM[9] = cam
        return c, cam, 'frio'
    cam = (lerp(820, 760, ramp(f, 0, de)), lerp(800, 840, ramp(f, ch, de)), z(lerp(1.5, 1.75, smooth(ramp(f, 0, de))), f), 0); CAM[9] = cam
    return c, cam, 'frio'


def s10(f):
    po = W(10, 'porta'); de = W(10, 'desceu')
    c = interior(f, 'neblina', aberta=ramp(f, po, po + 8), scroll=2600, rain=True)
    passageiros(c, f, sent=(2, 3, 4, 5), look=-1)
    sentado(c, BANCOS[0], f, expr='preocupado' if f < de else 'choque', look=-1 if f < de else .75, **CAPA_)
    assentos(c, 'neblina')
    put_cao(c, 800, 1210, 440, f, pose='deitado', flip=True, look=-.5 if f < de else .5)
    cam = (lerp(560, 700, ramp(f, 0, 110)), 840, z(lerp(1.4, 1.55, ramp(f, 0, 110)), f) + .05 * kick(f, de, .6), 0); CAM[10] = cam
    return c, cam, 'frio'


def s11(f):
    fi = W(11, 'final')
    if f < fi:
        c = interior(f, 'neblina', anda=2.2)
        passageiros(c, f, sent=(3,), look=-.5)
        sentado(c, BANCOS[0], f, expr='preocupado', look=1 if (f // 30) % 2 else .25, **CAPA_)
        assentos(c, 'neblina')
        put_cao(c, 800, 1210, 440, f, pose='deitado', flip=True, look=.5)
        cam = (lerp(900, 1050, ramp(f, 0, fi)), 780, z(1.3, f), 0); CAM[11] = cam
        return c, cam, 'sombrio'
    g = f - fi
    c = campo_bg('neblina').copy()
    put_ponto(c, 1950, 1180, .95, 'neblina')
    put_onibus(c, lerp(-1700, 0, easeOut(ramp(g, 0, 30))), 1050, luz='neblina', gente=False)
    cam = (lerp(1104, 1150, ramp(g, 0, 90)), 640, z(1.1, g), 0); CAM[11] = cam
    return c, cam, 'sombrio'


def s12(f):
    de = W(12, 'desceu'); ol = W(12, 'olhou'); fi = W(12, 'ficou'); dc = W(12, 'desci')
    c = campo_bg('neblina').copy()
    put_ponto(c, 1950, 1180, .95, 'neblina')
    dx = put_onibus(c, 0, 1050, luz='neblina', gente=False, aberta=1.0)
    t = ramp(f, de, de + 14)
    x = lerp(dx, dx + 120, t) + 9 * clamp(f - de - 14, 0, ol - de - 14)
    y = lerp(1050, 1180, t) - 80 * math.sin(math.pi * t)
    put_cao(c, x, y, 420, f, pose='sentado' if f >= fi else 'pe', walk=1 if de + 14 < f < ol else 0, flip=f >= ol, look=.5)
    if f >= dc:
        t2 = ramp(f, dc, dc + 14)
        put_menino(c, lerp(dx, dx + 40, t2), lerp(1060, 1180, t2) - 60 * math.sin(math.pi * t2), 700, f, expr='preocupado', look=.75, **CAPA_)
    cam = (lerp(1200, 1450, smooth(ramp(f, 0, ol))), lerp(700, 760, ramp(f, 0, dc)), z(1.35, f), 0); CAM[12] = cam
    return c, cam, 'sombrio'


def s13(f):
    ar = W(13, 'arranhou')
    c = casa_bg('velha', 'neblina').copy()
    xd = lerp(150, 940, smooth(ramp(f, 0, ar - 4)))
    if f >= ar: xd = 940 + 10 * math.sin(f * 1.6)
    put_menino(c, lerp(-100, 560, smooth(ramp(f, 0, ar))), 1190, 720, f, walk=1 if f < ar else 0,
               expr='curioso' if f < ar else 'preocupado', look=.75, **CAPA_)
    put_cao(c, xd, 1190, 420, f, pose='pe', walk=1 if f < ar - 4 else 0, look=.5, cabeca=.5 if f >= ar else 0)
    t = smooth(ramp(f, 0, ar))
    cam = (lerp(1150, 980, t), lerp(660, 760, t), z(lerp(1.12, 1.45, t), f), 0); CAM[13] = cam
    return c, cam, 'sombrio'


def s14(f):
    c = casa_bg('velha', 'neblina').copy()
    put_cao(c, 1450, 1190, 420, f, pose='sentado', look=-1)
    ca = W(14, 'canivete')
    t = smooth(ramp(f, 0, 30)); t2 = smooth(ramp(f, ca - 6, ca + 16))
    cx = lerp(lerp(900, 800, t), 640, t2); cy = lerp(lerp(800, 860, t), 740, t2)
    cam = (cx, cy, z(lerp(lerp(1.6, 3.0, t), 3.3, t2), f), 0); CAM[14] = cam
    return c, cam, 'sombrio'


def s15(f):
    c = casa_bg('velha', 'neblina').copy()
    c = close_h(c, f, expr='choque', look=0, s=.92, shake=.4, **CAPA_)
    cam = (1104, 621, z(lerp(1.22, 1.03, easeOut(ramp(f, 0, 10))), f, .0015) + .05 * kick(f, W(15, 'avo'), .6), 0); CAM[15] = cam
    return c, cam, 'sombrio'


def s16(f):
    ab = W(16, 'abriu'); pa = W(16, 'palido')
    if f >= pa:   # CLOSE do avô
        c = casa_bg('avo', 'tarde', 1.0).copy()
        c = close_h(c, f, expr='choque', look=-.5, s=.92, shake=.25, **dict(AVO, pele='#f3e2cf'))
        cam = (1104, 621, z(lerp(1.2, 1.03, easeOut(ramp(f, pa, pa + 10))), f - pa), 0); CAM[16] = cam
        return c, cam, 'tarde'
    c = casa_bg('avo', 'tarde', round(ramp(f, ab, ab + 10) * 4) / 4).copy()
    if f >= ab + 4:
        put_menino(c, 960, 1100, 640, f, seed=3, expr='neutro', look=.5, **AVO)
    put_menino(c, lerp(-80, 520, smooth(ramp(f, 0, ab))), 1190, 720, f, walk=1 if f < ab else 0, expr='neutro', look=.75, **CAPA_)
    put_cao(c, lerp(-300, 760, smooth(ramp(f, 0, ab))), 1190, 420, f, pose='pe' if f < ab else 'sentado', walk=1 if f < ab else 0, look=.5)
    t = smooth(ramp(f, 0, ab + 10))
    cam = (lerp(900, 860, t), lerp(700, 780, t), z(lerp(1.15, 1.45, t), f), 0); CAM[16] = cam
    return c, cam, 'tarde'


def s17(f):
    c = sala_bg('tarde').filter(ImageFilter.GaussianBlur(8)).convert('RGBA')
    cx_ = W(17, 'caixa'); fo = W(17, 'foto'); orl = W(17, 'orelha')
    s_ = back(ramp(f, cx_, cx_ + 10))
    if s_ > .05: kit.paste_c(c, caixa_img(), 1104, 1000, s_ * 1.2)
    sf = back(ramp(f, fo, fo + 12))
    if sf > .05: kit.paste_c(c, foto_img(), 1104, lerp(900, 580, ramp(f, fo, fo + 12)), sf * 1.15)
    # o cachorro na foto fica perto de (950, 480) com a foto no lugar
    t = smooth(ramp(f, orl - 6, orl + 14))
    cam = (lerp(1104, 960, t), lerp(660, 470, t), z(lerp(1.1, 2.0, t), f), 0); CAM[17] = cam
    return c, cam, 'tarde'


def s18(f):
    mu = W(18, 'mudanca')
    if f < mu:
        c = rua2_bg('tarde', int(f * 10)).copy()
        put_menino(c, 900, 1180, 640, f, walk=1, expr='sorriso', look=.75, **MENINO_AVO)
        put_cao(c, 1260, 1180, 400, f, pose='pe', walk=1, look=-.5)
        c = sepia_img(c)
        cam = (1080, 700, z(1.3, f), 0); CAM[18] = cam
        return c, cam, 'tarde'
    g = f - mu
    c = casa_bg('velha', 'tarde', caixas=True).copy()
    su = W(18, 'sumiu')
    put_menino(c, 600, 1190, 640, f, seed=3, expr='preocupado' if f < su else 'choque', look=-.75 if (g // 25) % 2 else .75, **MENINO_AVO)
    c = sepia_img(c)
    cam = (lerp(900, 750, ramp(g, 0, 120)), 720, z(lerp(1.2, 1.4, ramp(g, 0, 120)), g) + .05 * kick(f, su, .6), 0); CAM[18] = cam
    return c, cam, 'tarde'


def s19(f):
    fa = W(19, 'farofa'); en = W(19, 'envelheceu'); fim = wt(19, 'dia') + 26
    if f < fa:
        c = rua2_bg('dia').copy(); put_ponto(c, 330, 1180)
        put_onibus(c, lerp(-1700, 2300, ramp(f, 10, fa)), 1050, luz='dia', gente=False)
        cam = (1104, 680, z(1.15, f), 0); CAM[19] = cam
        return c, cam, 'vivo'
    c = sala_bg('tarde').copy()
    put_menino(c, 1740, 1190, 740, f, seed=3, expr='sorriso', look=-.75, **AVO)
    put_cao(c, 1050, 1175, 430, f, pose='deitado', olho='fechado', cauda=0.0)
    if f < en or f >= fim:
        if f < en: zzz(c, 1250, 860, f)
        g = f - fa
        cam = (lerp(1250, 1150, ramp(g, 0, 90)), 760, z(1.3 if f < en else 1.05, g), 0); CAM[19] = cam
        return c, cam, 'tarde'
    c = close_h(c, f, expr='desconfiado', look=0, s=.92, escurece=.3, **EU)
    cam = (1104, 621, z(lerp(1.2, 1.03, easeOut(ramp(f, en, en + 10))), f - en, .0012), 0); CAM[19] = cam
    return c, cam, 'frio'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19]


# ---------------------------------------------------------------- HUD (saída 1920x1080)
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        if f < CAPA:
            stamp(im, 'HISTÓRIA COMPLETA', 420, 170, 1, 56, big=True)
            gancho_h(im, ['UM CACHORRO', 'PEGA O ÔNIBUS', 'SOZINHO'], 90, 290, 1, 118)
        else:
            stamp(im, 'NA MINHA CIDADE', 420, 110, back(ramp(f, CAPA + 2, CAPA + 10)), 64)
            se = W(0, 'sete')
            painel(im, 'HORA', '07:15', 1600, 190, ramp(f, se, se + 10))
            so = W(0, 'sozinho')
            if f >= so: burst(im, 'SOZINHO!', 1500, 470, back(ramp(f, so, so + 8)), 54)
    elif si == 1:
        pr = W(1, 'preta'); pm = W(1, 'primeiro')
        if f < pm - 4:
            card(im, 'Orelha preta', 'e o resto caramelo', 1500, 170, ramp(f, pr, pr + 10))
        stamp(im, 'O PRIMEIRO BANCO', 420, 110, back(ramp(f, pm, pm + 8)), 64)
    elif si == 2:
        de = W(2, 'desce'); qu = W(2, 'quatro'); ma = W(2, 'mais')
        n = 1 + int(3 * ramp(f, de, qu)) if f >= de else 1
        painel(im, 'PONTOS', str(n), 330, 200, ramp(f, de - 10, de), glitch=1 if qu <= f < qu + 8 and f % 4 < 2 else 0, w=320)
        stamp(im, 'NEM UM A MAIS', 1450, 110, back(ramp(f, ma, ma + 8)), 64)
    elif si == 3:
        r = W(3, 'regra'); b = W(3, 'banco')
        stamp(im, 'A REGRA', 420, 130, back(ramp(f, r, r + 8)), 100, big=True)
        card(im, 'Banco do cachorro', 'ninguém senta', 1500, 160, ramp(f, b, b + 10))
    elif si == 4:
        ni = W(4, 'ninguem'); so = W(4, 'some')
        interrog(im, 960, 150, f, ramp(f, ni, ni + 8) * (1 - ramp(f, so - 6, so)))
        if f >= so: burst(im, 'SUMIU!', 960, 250, back(ramp(f, so + 2, so + 10)), 64)
    elif si == 5:
        di = W(5, 'dito')
        stamp(im, 'SEU DITO, O MOTORISTA', 470, 110, back(ramp(f, di, di + 8)), 60)
    elif si == 6:
        sg = W(6, 'segunda-feira'); ca = W(6, 'capa')
        stamp(im, 'SEGUNDA-FEIRA', 420, 110, back(ramp(f, sg, sg + 8)), 64)
        card(im, 'Capa amarela', 'velha, do meu avô', 1500, 170, ramp(f, ca, ca + 10))
    elif si == 7:
        fr = W(7, 'freada'); b = W(7, 'banco')
        if f < b: burst(im, 'FREADA!', 1450, 200, back(ramp(f, fr, fr + 6)), 60)
        stamp(im, 'NO BANCO DO CACHORRO', 1300, 120, back(ramp(f, b, b + 8)), 60)
    elif si == 8:
        si_ = W(8, 'silencio'); su = W(8, 'subiu')
        stamp(im, 'SILÊNCIO', 1500, 110, back(ramp(f, si_, si_ + 8)), 70)
        if f >= su: burst(im, '!', 1500, 330, back(ramp(f, su, su + 6)), 80)
    elif si == 9:
        ch = W(9, 'cheirou'); de = W(9, 'deitou')
        if f < de + 8: card(im, 'Cheirou devagar', 'a capa amarela do meu avô', 1500, 160, ramp(f, ch, ch + 10))
        else: burst(im, '?!', 1580, 220, back(ramp(f, de + 10, de + 18)), 70)
    elif si == 10:
        qu = W(10, 'quarto'); de = W(10, 'desceu')
        painel(im, 'PONTO', '4', 1600, 200, ramp(f, qu, qu + 8), w=300)
        stamp(im, 'ELE NÃO DESCEU', 1300, 440, back(ramp(f, de, de + 8)), 70)
    elif si == 11:
        fi = W(11, 'final')
        if f < fi:
            n = '7' if f >= W(11, 'setimo') else '6' if f >= W(11, 'sexto') else '5'
            painel(im, 'PONTO', n, 1600, 200, ramp(f, W(11, 'quinto'), W(11, 'quinto') + 8), w=300,
                   glitch=1 if f % 30 < 4 else 0)
        else:
            stamp(im, 'PONTO FINAL', 420, 120, back(ramp(f, fi, fi + 8)), 80, big=True)
    elif si == 12:
        es = W(12, 'esperando')
        stamp(im, 'ME ESPERANDO', 420, 110, back(ramp(f, es, es + 8)), 64)
    elif si == 13:
        ja = W(13, 'janela'); ar = W(13, 'arranhou')
        if f < ar: card(im, 'Janela azul', 'casa velha, no fim da linha', 1500, 160, ramp(f, ja, ja + 10), alvo=to_out(13, 1490, 640))
        else: burst(im, 'RASC RASC', 1400, 220, back(ramp(f, ar, ar + 6)), 50)
    elif si == 14:
        ri = W(14, 'risquinhos'); to = W(14, 'tonico')
        if f < to - 8: card(im, 'Risquinhos', 'marcas de altura de criança', 1500, 160, ramp(f, ri, ri + 10))
        stamp(im, 'TONICO E FAROFA', 1350, 130, back(ramp(f, to, to + 8)), 80, big=True)
    elif si == 15:
        av = W(15, 'avo')
        stamp(im, 'O MEU AVÔ', 420, 150, back(ramp(f, av, av + 8)), 90, big=True)
    elif si == 16:
        ca = W(16, 'casa'); fa = W(16, 'farofa')
        if f < W(16, 'palido'): stamp(im, 'EM CASA', 420, 110, back(ramp(f, ca, ca + 8)), 64)
        if f >= fa: stamp(im, 'FAROFA?', 420, 150, back(ramp(f, fa, fa + 8)), 90, rot=3)
    elif si == 17:
        me = W(17, 'menino'); pr = W(17, 'preta')
        if f < W(17, 'orelha') - 6: card(im, 'A foto', 'meu avô, menino, no ônibus doze', 1500, 160, ramp(f, me, me + 10))
        stamp(im, 'ORELHA PRETA', 420, 120, back(ramp(f, pr, pr + 8)), 80)
    elif si == 18:
        qu = W(18, 'quatro'); mu = W(18, 'mudanca'); se = W(18, 'sessenta'); su = W(18, 'sumiu')
        if f < mu: painel(im, 'ATÉ A ESCOLA', '4 PONTOS', 1560, 200, ramp(f, qu, qu + 10), w=560)
        else:
            painel(im, 'FAZ', '60 ANOS', 1560, 200, ramp(f, se, se + 10), w=520)
            if f >= su: burst(im, 'SUMIU!', 420, 230, back(ramp(f, su, su + 8)), 60)
    elif si == 19:
        fa = W(19, 'farofa'); en = W(19, 'envelheceu'); di = W(19, 'dia')
        if f < fa:
            stamp(im, 'HOJE', 420, 110, back(ramp(f, 2, 10)), 80)
            painel(im, 'HORA', '07:15', 1600, 190, ramp(f, W(19, 'sete'), W(19, 'sete') + 10))
        elif f < wt(19, 'dia') + 26:
            if f >= di: stamp(im, 'NEM UM DIA', 420, 150, back(ramp(f, di, di + 8)), 90, big=True)
    return grao(im.convert('RGB'), lf)
