"""Formato FÁBULA: "O pote de tempo" (27/11/2026, 11h). Roteiro 1 do doc do Luis "5 Fábulas Emocionantes — Roteiros".
Tema: presença de pai e filho. Moral: "O tempo não volta. Mas a presença pode começar hoje." CTA: "Manda pro seu pai."

LIPE (protagonista FIXO de todas as fábulas, mesmo visual sempre): menino de uns 8 anos, pele clara-pêssego (#f3c9a2), cabelo
castanho curto (#5b3a1e), camiseta AMARELA (#f4b63f), calça AZUL (#3e6fb8), olhos grandes de íris azul. De pijama: pijama
azul-claro (#8ec3e8 / #6fa8d6), mesmo rosto e cabelo. Pai: barba e cabelo castanho-escuros, camisa azul, calça cinza.
Mãe: cabelo comprido ruivo-escuro, blusa coral. (Cores em fabula.py: LIPE, LIPE_PIJAMA, PAI, MAE, VO.)

Palco quadrado 2208x2208 (fabula.py): as mesmas cenas servem para a vertical e para a horizontal (MOTOR_H=1).
Cenas/cores: s0 CAPA close Lipe + rua de dia (vivo) | s1 potes com nome (vivo) | s2 sala, mãe e Lipe no sofá (vivo) |
s3 jantar no celular (noite_fab) -> sofá sem conversa (tarde) | s4 vó e neto na rua (tarde) | s5 quarto à noite (noite_fab) |
s6 potes da mãe e do pai (noite_fab) | s7 escritório + CLOSE Lipe (noite_fab) | s8 pai, pote, relógio (noite_fab) |
s9 sala, calendário (tarde, música triste) | s10 escritório fim de tarde (tarde) | s11 pote vazio (tarde) |
s12 quarto, balão de pensamento (tarde) | s13 escritório, Lipe deixa o pote (noite_fab) | s14 bilhete (noite_fab) |
s15 pai e o pote rachado (noite_fab) | s16 CLOSE pai com lágrima (noite_fab) | s17 escritório de dia, fecha o notebook (vivo, música
inspiradora) | s18 quintal, bola, areia caindo (tarde) | s19 quintal + CLOSE final Lipe (tarde) | s20 MORAL (tarde)."""
from kit import *
import kit
from sombrio import *
from fabula import *
from fabula import _linhas_txt

CHAVES = ['pote', 'potes', 'areia', 'dourada', 'presente', 'tempo', 'vazio', 'cheio', 'fiozinho', 'sozinho', 'espaco', 'rachado',
          'perdendo', 'dinheiro', 'devolve', 'presenca', 'hoje', 'quintal', 'bola', 'juntos', 'nunca', 'amado', 'ferias', 'grao', 'pai']
instala_legenda_fab(CHAVES)
MUSICA = True
MUSICA_NIVEL = .14
STING = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+2%'; PITCH = '-2Hz'

LINES = [
    "Nesta cidade, todo mundo carrega um pote que mostra quanto tempo passou de verdade com quem ama.",
    "Cada pote tem o nome de alguém. O pote da mãe. O pote do melhor amigo. Até o pote do cachorro.",
    "E a areia dourada só cai quando você está presente. Presente de verdade.",
    "Olhar o celular do lado de alguém não conta. Estar no mesmo sofá sem conversar, também não.",
    "Por isso, nesta cidade, ninguém precisa perguntar se é amado. É só olhar o pote.",
    "Numa noite, o Lipe, de pijama, foi comparar os potes dele.",
    "O pote da mãe estava quase cheio. O pote do pai... tinha só um fiozinho de areia.",
    "Pai, por que o seu pote tá tão vazio?",
    "O pai olhou pro pote, depois pro relógio, e disse que precisava terminar um trabalho. Amanhã eles conversavam.",
    "Mas amanhã virou semana que vem. E semana que vem virou: quando eu tiver férias.",
    "O Lipe tentou encher o pote sozinho. Sentou do lado do pai, no escritório, bem quietinho.",
    "A areia não caiu. Nem um grão.",
    "E o Lipe descobriu uma coisa: não dá pra encher o pote de alguém sozinho. Os dois precisam estar ali.",
    "Uma noite, ele deixou o próprio pote em cima da mesa do pai, com um bilhete.",
    "Pai, eu guardei espaço pra você.",
    "O pai pegou o pote dele, o que tinha o nome do Lipe. E viu que também estava quase vazio. E rachado.",
    "Naquela hora, o pai entendeu que ele também estava perdendo. Tem coisa que o trabalho paga. Mas tem coisa que nenhum dinheiro devolve.",
    "No dia seguinte, o pai fechou o notebook e chamou o Lipe pro quintal.",
    "Os dois jogaram bola até o sol ir embora. E a areia começou a cair nos dois potes, ao mesmo tempo.",
    "Naquela tarde, a areia caiu como nunca. Não porque fizeram algo grande. Só porque, pela primeira vez, ninguém estava em outro lugar.",
    "O tempo não volta. Mas a presença pode começar hoje.",
]
FALA_TIKTOK = "Manda pro seu pai."
CTA_TEXTO = "MANDA PRO SEU PAI"
CTA_CARD = cta_card
ARROBA = ''
TWIST = 16
FLASH = []
CAPA = 36
CHECK = [(0, 'carrega', 6), (1, 'mae', 6), (1, 'cachorro', 8), (2, 'cai', 8), (2, 'verdade', 8), (3, 'conta', 6), (3, 'sofa', 6),
         (4, 'pote', 6), (6, 'fiozinho', 8), (7, 'vazio', 4), (8, 'relogio', 6), (8, 'amanha', 6), (9, 'ferias', 6), (11, 'grao', 6),
         (12, 'dois', 6), (13, 'bilhete', 6), (15, 'rachado', 8), (16, 'dinheiro', 6), (17, 'fechou', 8), (18, 'areia', 10),
         (19, 'primeira', 10), (20, 'hoje', 6)]


def TRILHA(SC, N, SR):
    return trilha(SC, N, SR, [(0, 'misteriosa'), (9, 'triste'), (17, 'inspiradora')])


def SFX(s):
    w0 = s.W(0, 'nesta'); s.patter(s.cut(0) + CAPA, s.cut(0) + CAPA + 120, 3, .05)
    for w in ('mae', 'amigo', 'cachorro'): s.ting(s.W(1, w), .22)
    s.trill(s.W(2, 'cai'), .6, .08); s.ting(s.W(2, 'verdade'), .2)
    s.thunk(s.W(3, 'conta') - 2, 120, .5); s.thunk(s.W(3, 'tambem') - 2, 120, .4)
    s.ting(s.W(4, 'pote'), .25)
    s.patter(s.W(5, 'noite'), s.W(5, 'comparar') + 20, 3, .04)
    s.ting(s.W(6, 'cheio'), .22); s.thunk(s.W(6, 'fiozinho') - 2, 90, .4)
    s.ting(s.W(8, 'relogio'), .15)
    for w, n in (('amanha', 0), ('semana', 1), ('ferias', 0)): s.whoosh(s.W(9, w, n) - 4, .35, .25)
    s.thunk(s.W(11, 'grao') - 2, 80, .35)
    s.patter(s.W(13, 'noite'), s.W(13, 'mesa'), 2, .03); s.thunk(s.W(13, 'mesa') - 2, 260, .25)
    s.ting(s.W(14, 'espaco'), .2)
    s.thunk(s.W(15, 'rachado') - 2, 300, .6); s.thunk(s.W(15, 'rachado') + 4, 500, .3)
    s.thunk(s.W(17, 'fechou') + 4, 200, .4)
    for k in range(4): s.thunk(s.W(18, 'bola') + 4 + k * 26, 150, .35)
    s.trill(s.W(18, 'areia'), .7, .08); s.ting(s.W(18, 'tempo'), .2)
    s.ting(s.W(19, 'nunca'), .2); s.ting(s.W(19, 'primeira'), .2)
    s.ting(s.W(20, 'hoje'), .25)


def bgc(fn, luz):
    return fn(luz).copy()


# ---------------------------------------------------------------- cenas
def s0(f):
    if f < CAPA:   # CAPA: close no Lipe + frase
        c = rua_fab(0, 0, 'dia')
        pessoa(c, 800, 1700, ADU, 0, GENTE[0]); pessoa(c, 1500, 1700, ADU, 0, GENTE[2])
        c = close_fab(c, f, 1104, 1150, expr='curioso', look=0, s=V(.9, .95), dx=V(0, 480), **LIPE)
        bw, bh = kit.BW, kit.BH
        if HOR: put_pote(c, 470, 1220, 250, .55, 'PAI', brilho=True)
        else: put_pote(c, 1010, 2160, 300, .55, 'PAI', brilho=True)
        return c, cam_close(f, 1.04, 1.0), 'vivo'
    g = f - CAPA
    c = rua_fab(f, scroll=g * 7, luz='dia')
    xa = 650 + g * .6
    pessoa(c, xa, 1690, ADU, f, GENTE[1], walk=1, seed=3, expr='sorriso', look=.75)
    pote_cintura(c, xa, 1690, ADU, f, .75, 'FILHA', cai=1, seed=1)
    pessoa(c, xa - 200, 1720, 620, f, GENTE[3], walk=1, seed=5, expr='sorriso', look=.75)
    xb = 1750 - g * 5
    pessoa(c, xb, 1700, ADU, f, GENTE[2], walk=1, seed=7, flip=True, expr='neutro', look=-.5)
    pote_cintura(c, xb, 1700, ADU, f, .3, 'IRMÃO', lado=-1)
    put_cachorro(c, 300 + g * 2, 1760, 260, f, andando=True)
    pessoa(c, 1104, 1730, KID, f, LIPE, walk=1, seed=2, expr='curioso', look=.25)
    pote_cintura(c, 1104, 1730, KID, f, .5, 'MÃE')
    t = smooth(ramp(g, 0, 150))
    return c, cam(1104, lerp(1250, 1300, t), lerp(1.12, 1.25, t) , lerp(1.0, 1.08, t)), 'vivo'


@lru_cache(maxsize=2)
def rua_borrada(luz):
    c = rua_fab(0, 300, luz)
    return c.resize((SW // 4, SH // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(4)).resize((SW, SH), Image.BILINEAR)


def s1(f):
    c = rua_borrada('dia').copy()
    m, a, ca = wt(1, 'mae') - 3, wt(1, 'amigo') - 3, wt(1, 'cachorro') - 3
    xs = V((760, 1104, 1450), (560, 1104, 1650)); by = V((1000, 960, 1000), (1060, 980, 1060)); w = V(300, 260)
    if f < m:
        put_pote(c, 1104, by[1] + 10 * math.sin(f * .2), w * back(ramp(f, 2, 12)), .45, '?')
    for i, (k, nm, nv) in enumerate(((m, 'MÃE', .8), (a, 'AMIGO', .6), (ca, 'CACHORRO', .9))):
        if f >= k:
            put_pote(c, xs[i], by[i] + 8 * math.sin(f * .12 + i), w * back(ramp(f, k, k + 9)), nv, nm)
    pessoa(c, 1104, V(1980, 1880), V(860, 760), f, LIPE, expr='curioso' if f < ca else 'sorriso', look=lerp(-.75, .75, smooth(ramp(f, m, ca))))
    if f >= ca - 4:
        x = lerp(2300, 1560, easeOut(ramp(f, ca - 4, ca + 18)))
        put_cachorro(c, x, V(2000, 1900), 300, f, andando=f < ca + 18, flip=True)
        put_pote(c, x - 70, V(1930, 1830), 90, .9)
    return c, cam(1104, V(1240, 1210), zf(1.15, f), zf(1.0, f, .0005)), 'vivo'


def s2(f):
    c = bgc(sala_fab, 'dia')
    pessoa(c, 960, 1610, ADU, f, MAE, seed=3, expr='sorriso', look=.75)
    pessoa(c, 1260, 1526, KID, f, LIPE, seed=2, expr='sorriso', look=-.75)
    c.alpha_composite(sofa_frente())
    ca, ve = wt(2, 'cai') - 4, wt(2, 'verdade') - 6
    jb = V(1760, 1650)
    put_pote(c, 860, jb, 240, lerp(.35, .6, ramp(f, ca, ca + 120)), 'LIPE', brilho=f >= ve)
    put_pote(c, 1350, jb, 240, lerp(.4, .65, ramp(f, ca, ca + 120)), 'MÃE', brilho=f >= ve)
    if f >= ca:
        graos(c, *boca_pote(860, jb, 240), f, 240, ramp(f, ca, ca + 8), 1)
        graos(c, *boca_pote(1350, jb, 240), f, 240, ramp(f, ca, ca + 8), 2)
    t = easeOut(ramp(f, ve, ve + 14))
    return c, cam(1104, lerp(V(1300, 1220), V(1560, 1420), t), lerp(1.35, 2.0, t) * (1 + .0006 * f), lerp(1.0, 1.55, t) * (1 + .0005 * f)), 'vivo'


def s3(f):
    es = wt(3, 'estar') - 3
    if f < es:
        c = bgc(jantar_fab, 'noite')
        for i, (x, cr) in enumerate(((760, GENTE[4]), (1104, GENTE[3]), (1450, GENTE[1]))):
            pessoa(c, x, 1570, ADU, f, cr, seed=3 + i, expr='neutro', look=0)
            celular(c, x, 1570 - .47 * ADU, 110, cr['pele'])
        c.alpha_composite(mesa_frente())
        for x in (930, 1280, 1620): put_pote(c, x, 1250, 150, .08 + .05 * (x % 3), '')
        return c, cam(1104, V(1180, 1120), zf(1.25, f), zf(1.0, f, .0006)), 'noite_fab'
    g = f - es
    c = bgc(sala_fab, 'tarde')
    pessoa(c, 820, 1610, ADU, f, GENTE[0], seed=4, expr='neutro', look=-.75)
    pessoa(c, 1390, 1610, ADU, f, GENTE[2], seed=6, expr='neutro', look=.75)
    celular(c, 820, 1610 - .47 * ADU, 110, GENTE[0]['pele'])
    c.alpha_composite(sofa_frente())
    put_pote(c, 1104, V(1760, 1650), 220, .1, '')
    return c, cam(1104, V(1300, 1220), lerp(1.45, 1.3, easeOut(ramp(g, 0, 12))) * (1 + .0006 * g), zf(1.0, g, .0006)), 'tarde'


def s4(f):
    c = rua_fab(f, scroll=f * 4, luz='tarde')
    xv, xn = 1000, 1260
    pessoa(c, xv, 1700, 960, f, VO, walk=1, seed=4, expr='sorriso', look=.75)
    pote_cintura(c, xv, 1700, 960, f, .92, 'NETO', cai=.7, brilho_=True, seed=3)
    pessoa(c, xn, 1720, 640, f, GENTE[4], walk=1, seed=6, expr='sorriso', look=-.75)
    pote_cintura(c, xn, 1720, 640, f, .9, 'VÓ', cai=.7, brilho_=True, seed=4)
    ol = wt(4, 'olhar') - 4
    px, py = cintura(xv, 1700, 960)
    t = easeOut(ramp(f, ol, ol + 14))
    return c, cam(lerp(1104, px, t), lerp(V(1250, 1180), py - 40, t), lerp(1.2, 2.3, t) * (1 + .0006 * f), lerp(1.0, 1.9, t) * (1 + .0005 * f)), 'tarde'


def prateleira(c, nv_pai=.03, w=160, xs=(1150, 1340, 1530), brilho_mae=True):
    put_pote(c, xs[0], 982, w, .88, 'MÃE', brilho=brilho_mae)
    put_pote(c, xs[1], 982, w, nv_pai, 'PAI')
    put_pote(c, xs[2], 982, w, .6, 'VÓ')


def s5(f):
    c = bgc(quarto_fab, 'noite')
    prateleira(c)
    x = lerp(620, 1150, smooth(ramp(f, 0, 70)))
    pessoa(c, x, 1760, KID, f, LIPE_PIJAMA, walk=1 if f < 70 else 0, seed=2, expr='curioso', look=.5)
    t = smooth(ramp(f, 0, 110))
    return c, cam(lerp(950, 1250, t), V(1280, 1200), lerp(1.1, 1.3, t), lerp(1.0, 1.15, t)), 'noite_fab'


def s6(f):
    c = bgc(quarto_fab, 'noite')
    pa = wt(6, 'pai') - 4; fi = wt(6, 'fiozinho') - 4
    put_pote(c, 1130, 982, 300, .88, 'MÃE', brilho=True)
    put_pote(c, 1520, 982, 300, .03, 'PAI')
    graos(c, *boca_pote(1130, 982, 300), f, 300, .5, 5)
    t = smooth(ramp(f, pa - 6, pa + 10)); u = easeOut(ramp(f, fi, fi + 12))
    cx = lerp(1130, 1520, t)
    return c, cam(cx, lerp(800, 860, u), lerp(2.2, 2.7, u) * (1 + .0008 * f), lerp(2.0, 2.5, u) * (1 + .0008 * f)), 'noite_fab'


def escritorio(luz, f, pai=True, pexpr='neutro', plook=-.75, aberto=1.0, pfeet=1640):
    c = bgc(escritorio_fab, luz)
    relogio(c, 21, 40, 1880, 560, 100)
    if pai: pessoa(c, 1360, pfeet, ADU, f, PAI, seed=5, expr=pexpr, look=plook)
    c.alpha_composite(mesa_trab())
    notebook(c, 1720, 1240, aberto)
    return c


def s7(f):
    pq = wt(7, 'por') - 3
    c = escritorio('noite', f, plook=-.75)
    pessoa(c, 640, 1760, KID, f, LIPE_PIJAMA, seed=2, expr='preocupado', look=.75)
    hx, hy = mao_dir(640, 1760, KID); put_pote(c, hx + 10, hy + 60, 150, .03, 'PAI')
    if f >= pq:   # CLOSE 2
        c = close_fab(c, f, 700, 1250, expr='preocupado', look=.5, s=V(.95, .95), dx=V(0, -250), **LIPE_PIJAMA)
        return c, cam_close(f, 1.18, 1.0, pq), 'noite_fab'
    return c, cam(V(900, 1104), V(1250, 1150), 1.2, 1.0), 'noite_fab'


def s8(f):
    po, re, di, am = wt(8, 'pote') - 3, wt(8, 'relogio') - 3, wt(8, 'disse') - 3, wt(8, 'amanha') - 3
    look = -1 if f < re else (1 if f < di else -.5)
    ex = 'preocupado' if po <= f < re else ('neutro' if f < am else 'preocupado')
    c = escritorio('noite', f, pexpr=ex, plook=look)
    pessoa(c, 640, 1760, KID, f, LIPE_PIJAMA, seed=2, expr='preocupado' if f >= am else 'curioso', look=.75)
    hx, hy = mao_dir(640, 1760, KID); put_pote(c, hx + 10, hy + 60, 150, .03, 'PAI')
    if f < re: cx, cy, z = 1150, 1150, 1.4
    elif f < di: cx, cy, z = 1600, 1050, 1.3
    elif f < am: cx, cy, z = 1450, 1150, 1.45
    else: cx, cy, z = 1080, 1250, 1.0
    return c, cam(V(cx, max(1104, cx - 100)), V(cy, min(cy, 1150)), zf(z, f), zf(max(1.0, z * .75), f)), 'noite_fab'


def calendario(im, texto, x, y, s=1.0, w=None):
    if s <= .02: return
    w = w or V(620, 560); h = int(w * .72)
    b = Image.new('RGBA', (w + 20, h + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.rounded_rectangle((10, 10, w + 10, h + 10), 26, fill=(0, 0, 0, 80))
    d.rounded_rectangle((2, 2, w, h), 26, fill=(255, 252, 244, 255), outline=(36, 24, 34, 255), width=8)
    d.rounded_rectangle((2, 2, w, 110), 26, fill=(224, 88, 58, 255), outline=(36, 24, 34, 255), width=8)
    d.rectangle((6, 70, w - 4, 110), fill=(224, 88, 58, 255)); d.line((2, 110, w, 110), fill=(36, 24, 34, 255), width=8)
    for k in range(4):
        xx = w * (k + 1) / 5; d.rounded_rectangle((xx - 12, -10, xx + 12, 50), 8, fill=(200, 200, 205, 255), outline=(36, 24, 34, 255), width=5)
    linhas = texto.split('|'); fs = 92
    while fs > 30 and max(d.textlength(l, font=font(F_STAMP, fs)) for l in linhas) > w - 70: fs -= 4
    fnt = font(F_STAMP, fs); y0 = 110 + (h - 110 - len(linhas) * fs * 1.15) / 2
    for i, l in enumerate(linhas):
        tw = d.textlength(l, font=fnt); d.text((w / 2 - tw / 2, y0 + i * fs * 1.15), l, font=fnt, fill=(60, 44, 54))
    b = b.resize((b.width, max(2, int(b.height * clamp(s)))), Image.BILINEAR)
    paste_c(im, b, x, y)


def s9(f):
    e = wt(9, 'e') - 3; fe = wt(9, 'quando') - 3
    c = bgc(sala_fab, 'tarde')
    if f < e:
        pessoa(c, 1250, 1740, KID, f, LIPE, seed=2, expr='preocupado', look=-.75)
        hx, hy = mao_dir(1250, 1740, KID); bola(c, hx + 40, hy + 10, 70)
        return c, cam(1150, V(1250, 1180), zf(1.3, f), zf(1.05, f)), 'tarde'
    if f < fe:
        pessoa(c, 1104, 1526, KID, f, LIPE, seed=2, expr='preocupado', look=-.5)
        c.alpha_composite(sofa_frente())
        bola(c, 1300, 1700, 70)
        return c, cam(1104, V(1300, 1200), zf(1.45, f - e), zf(1.15, f - e)), 'tarde'
    pessoa(c, 620, 1700, KID, f, LIPE, seed=2, flip=True, expr='preocupado', look=-1)
    bola(c, 800, 1720, 70)
    return c, cam(V(800, 1104), V(1250, 1150), zf(1.3, f - fe), zf(1.05, f - fe)), 'tarde'


def s10(f):
    se = wt(10, 'sentou') - 3; qu = wt(10, 'quietinho') - 3
    c = bgc(escritorio_fab, 'tarde')
    relogio(c, 17, 50, 1880, 560, 100)
    pessoa(c, 1360, 1640, ADU, f, PAI, seed=5, expr='neutro', look=.75)
    c.alpha_composite(mesa_trab())
    notebook(c, 1720, 1240, 1.0)
    put_pote(c, 1010, 1245, 150, .03, 'PAI')
    d = ImageDraw.Draw(c)   # banquinho
    d.rectangle((640, 1540, 860, 1580), fill=(224, 88, 58, 255), outline=INK + (255,), width=6)
    for x in (660, 820): d.rectangle((x, 1580, x + 20, 1770), fill=(150, 60, 40, 255), outline=INK + (255,), width=5)
    x = lerp(500, 750, smooth(ramp(f, 0, se))) if f < se + 10 else 750
    pessoa(c, x, 1760 if f < se else 1720, KID, f, LIPE, seed=2, walk=1 if f < se else 0, expr='sorriso' if f < qu else 'neutro', look=.75)
    return c, cam(V(1080, 1104), V(1230, 1150), zf(1.15, f, .001), zf(1.0, f, .0006)), 'tarde'


def s11(f):
    c = bgc(escritorio_fab, 'tarde')
    pessoa(c, 1360, 1640, ADU, f, PAI, seed=5, expr='neutro', look=.75)
    c.alpha_composite(mesa_trab())
    notebook(c, 1720, 1240, 1.0)
    put_pote(c, 980, 1245, 220, .03, 'PAI')
    gr = wt(11, 'grao') - 3
    bx, by = boca_pote(980, 1245, 220)
    if f < gr + 14:   # um grão que hesita e some
        a = 1 - ramp(f, gr, gr + 14)
        d = ImageDraw.Draw(c); yy = by - 120 + 8 * math.sin(f * .3)
        d.ellipse((bx - 12, yy - 12, bx + 12, yy + 12), fill=(150, 100, 20, int(255 * a))); d.ellipse((bx - 9, yy - 9, bx + 9, yy + 9), fill=(255, 214, 110, int(255 * a)))
    return c, cam(V(940, 1000), V(1080, 1060), zf(2.5, f, .0015), zf(2.0, f, .0015)), 'tarde'


@lru_cache(maxsize=1)
def pensamento():
    c2 = Image.new('RGBA', (700, 520), (0, 0, 0, 0))
    put_menino(c2, 240, 500, 440, 0, expr='sorriso', look=.75, **PAI)
    put_menino(c2, 470, 500, 310, 0, expr='sorriso', look=-.75, **LIPE)
    put_pote(c2, 355, 230, 120, .7, '', brilho=True)
    return c2.resize((440, 327), Image.LANCZOS)


def s12(f):
    c = bgc(quarto_fab, 'tarde')
    do = wt(12, 'dois') - 4; de = wt(12, 'descobriu') - 4
    pessoa(c, 1830, 1500, KID, f, LIPE, seed=2, expr='curioso' if f < do else 'sorriso', look=-.5)
    thought(c, 1330, 900, 300, back(ramp(f, de, de + 10)), pensamento() if f >= do else None)
    if f >= de and f < do:
        paste_c(c, pote_img(.0, '', 0.0, False, 120), 1330, 860, 1)
    return c, cam(V(1550, 1300), V(1150, 1100), zf(1.2, f), zf(1.05, f)), 'tarde'


def s13(f):
    me = wt(13, 'mesa') - 3; bi = wt(13, 'bilhete') - 3
    c = escritorio('noite', f, pai=False, aberto=0.0)
    x = lerp(300, 820, smooth(ramp(f, 0, me)))
    pessoa(c, x, 1760, KID, f, LIPE_PIJAMA, seed=2, walk=1 if f < me else 0, expr='sorriso', look=.75)
    if f < me:
        hx, hy = mao_dir(x, 1760, KID); put_pote(c, hx + 10, hy + 60, 150, .03, 'PAI')
    else:
        put_pote(c, 980, 1245, 150, .03, 'PAI')
    if f >= bi:
        d = ImageDraw.Draw(c); s_ = back(ramp(f, bi, bi + 8))
        d.polygon([(1060, 1236), (1060 + 150 * s_, 1226), (1066 + 150 * s_, 1240), (1062, 1246)], fill=(250, 244, 222, 255), outline=INK + (255,))
    t = smooth(ramp(f, 0, 140))
    return c, cam(V(lerp(700, 950, t), 1104), V(1250, 1150), lerp(1.15, 1.4, t), lerp(1.0, 1.15, t)), 'noite_fab'


def s14(f):
    c = escritorio('noite', f, pai=False, aberto=0.0)
    put_pote(c, 980, 1245, 220, .03, 'PAI')
    return c, cam(1050, 1100, zf(2.2, f, .001), zf(1.8, f, .001)), 'noite_fab'


def s15(f):
    vi, qu, ra = wt(15, 'viu') - 3, wt(15, 'quase') - 4, wt(15, 'rachado') - 3
    c = escritorio('noite', f, pai=False, aberto=0.0)
    put_pote(c, 980, 1245, 150, .03, 'PAI')
    ex = 'neutro' if f < vi else ('preocupado' if f < ra else 'choque')
    pessoa(c, 1250, 1760, ADU, f, PAI, seed=5, expr=ex, look=.5)
    hx, hy = mao_dir(1250, 1760, ADU)
    put_pote(c, hx + 20, hy + 90, 200, .05, 'LIPE', rachado=ramp(f, ra, ra + 8))
    t = easeOut(ramp(f, qu, qu + 14)); k = kick(f, ra, .8)
    return c, cam(lerp(V(1250, 1200), hx + 20, t), lerp(V(1250, 1150), hy - 40, t) + k * 14, lerp(1.2, 2.4, t), lerp(1.0, 1.9, t), k * 1.5), 'noite_fab'


def s16(f):
    pe = wt(16, 'perdendo') - 3
    c = escritorio('noite', f, pai=False, aberto=0.0)
    put_pote(c, 980, 1245, 150, .03, 'PAI')
    c = close_fab(c, f, 1250, 1150, expr='preocupado', look=0 if f < pe else .25, s=V(.95, .95), escurece=.15,
                  lagrima=ramp(f, pe, pe + 1) * ((f - pe) / 45 % 1) if f >= pe else 0, **PAI)
    return c, cam_close(f, 1.12, 1.0), 'noite_fab'


def s17(f):
    fe, ch = wt(17, 'fechou') - 3, wt(17, 'chamou') - 3
    c = escritorio('dia', f, pexpr='neutro' if f < fe + 8 else 'sorriso', plook=.75, aberto=1 - ramp(f, fe, fe + 8))
    if f >= ch - 6:
        x = lerp(2350, 1950, easeOut(ramp(f, ch - 6, ch + 16)))
        pessoa(c, x, 1760, KID, f, LIPE, seed=2, walk=1 if f < ch + 16 else 0, flip=True, expr='curioso' if f < ch + 12 else 'sorriso', look=-.75)
    t = smooth(ramp(f, ch - 6, ch + 20))
    return c, cam(lerp(V(1350, 1104), V(1600, 1300), t), V(1200, 1130), lerp(1.35, 1.2, t) * (1 + .0006 * f), lerp(1.05, 1.0, t)), 'vivo'


def s18(f):
    c = bgc(quintal_fab, 'tarde')
    ar = wt(18, 'areia') - 3
    xp = 760 + 30 * math.sin(f * .07); xl = 1450 - 30 * math.sin(f * .07 + 1)
    per = 52; ph = (f % per) / per; ida = (f // per) % 2 == 0
    bx = lerp(xp + 120, xl - 90, ph if ida else 1 - ph); by = 1780 - 380 * math.sin(math.pi * ph)
    pessoa(c, xp, 1800, ADU, f, PAI, seed=5, walk=.6, expr='sorriso', look=.75)
    pessoa(c, xl, 1820, KID, f, LIPE, seed=2, walk=.6, flip=True, expr='sorriso', look=-.75)
    cai = ramp(f, ar, ar + 10)
    nv = lerp(.06, .35, ramp(f, ar, ar + 150))
    pote_cintura(c, xp, 1800, ADU, f, nv, 'LIPE', cai=cai, seed=7)
    pote_cintura(c, xl, 1820, KID, f, nv, 'PAI', lado=-1, cai=cai, seed=8)
    bola(c, bx, by, 60, f * .3)
    t = easeOut(ramp(f, ar, ar + 20))
    return c, cam(1104, lerp(V(1350, 1250), V(1450, 1330), t), lerp(1.05, 1.3, t) * (1 + .0005 * f), lerp(1.0, 1.15, t)), 'tarde'


def s19(f):
    pr = wt(19, 'primeira') - 3
    c = bgc(quintal_fab, 'tarde')
    nv = lerp(.4, .95, ramp(f, 0, pr))
    pessoa(c, 960, 1800, ADU, f, PAI, seed=5, expr='sorriso', look=.75)
    pessoa(c, 1250, 1820, KID, f, LIPE, seed=2, expr='sorriso', look=-.75)
    pote_cintura(c, 960, 1800, ADU, f, nv, 'LIPE', lado=-1, cai=1, brilho_=True, seed=9)
    pote_cintura(c, 1250, 1820, KID, f, nv, 'PAI', cai=1, brilho_=True, seed=10)
    for k in range(10):
        a = (f * .02 + k * .1) % 1
        brilho(c, 700 + k * 90 + 30 * math.sin(f * .05 + k), 1700 - a * 900, 26 * math.sin(a * math.pi))
    if f >= pr:   # CLOSE final
        c = close_fab(c, f, 1104, 1250, expr='sorriso', look=0, s=V(.95, .95), **LIPE)
        for k in range(8):
            a = (f * .02 + k * .125) % 1
            brilho(c, kit.BW * (.1 + .8 * ((k * .37) % 1)), kit.BH * (1 - a), 30 * math.sin(a * math.pi))
        return c, cam_close(f, 1.15, 1.0, pr), 'tarde'
    t = smooth(ramp(f, 0, pr))
    return c, cam(1104, V(1300, 1250), lerp(1.15, 1.35, t), lerp(1.0, 1.1, t)), 'tarde'


def s20(f):
    c = bgc(quintal_fab, 'tarde')
    pessoa(c, 700, 1700, ADU, f, PAI, seed=5, expr='sorriso', look=.75)
    pessoa(c, 1500, 1720, KID, f, LIPE, seed=2, flip=True, expr='sorriso', look=-.75)
    put_pote(c, 960, 1900, 300, .95, 'LIPE', brilho=True)
    put_pote(c, 1250, 1900, 300, .95, 'PAI', brilho=True)
    for k in range(10):
        a = (f * .02 + k * .1) % 1
        brilho(c, 650 + k * 100 + 30 * math.sin(f * .05 + k), 1800 - a * 1000, 26 * math.sin(a * math.pi))
    return c, cam(1104, V(1350, 1350), zf(1.15, f, .0006), zf(1.0, f, .0005)), 'tarde'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]


# ---------------------------------------------------------------- HUD (coordenadas da saída)
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0 and f < CAPA:
        if HOR: capa_txt(im, ['NESTA CIDADE, UM', '*POTE* MOSTRA SEU *TEMPO*', 'COM QUEM VOCÊ AMA'], size=104, y=200)
        else: capa_txt(im, ['NESTA CIDADE,', 'UM *POTE* MOSTRA SEU', '*TEMPO* COM QUEM AMA'], size=96)
    elif si == 3:
        es = wt(3, 'estar') - 3; co = wt(3, 'conta') - 3; tb = wt(3, 'tambem') - 3
        if f < es: selo_txt(im, 'NÃO CONTA', V(540, 960), V(330, 140), ramp(f, co, co + 8), V(80, 76))
        else: selo_txt(im, 'TAMBÉM NÃO', V(540, 960), V(330, 140), ramp(f, tb, tb + 8), V(80, 76))
    elif si == 8:
        am = wt(8, 'amanha') - 3
        selo_txt(im, 'AMANHÃ...', V(540, 1500), V(330, 160), ramp(f, am, am + 8), V(80, 72), cor=(77, 121, 179))
    elif si == 9:
        e = wt(9, 'e') - 3; fe = wt(9, 'quando') - 3; am = wt(9, 'amanha') - 3
        if f < e: txt_, k0 = 'AMANHÃ', am
        elif f < fe: txt_, k0 = 'SEMANA|QUE VEM', e
        else: txt_, k0 = 'QUANDO EU|TIVER FÉRIAS', fe
        calendario(im, txt_, V(540, 1500), V(290, 240), ramp(f, k0, k0 + 6), w=V(540, 500))
    elif si == 11:
        gr = wt(11, 'grao') - 3
        selo_txt(im, 'NEM UM GRÃO', V(540, 960), V(330, 150), ramp(f, gr, gr + 8), V(84, 76), cor=(77, 121, 179))
    elif si == 14:
        kit.paste_c(im, sombrio.bilhete_img('Pai, eu guardei|espaço pra você.', V(760, 720)).rotate(-3, Image.BICUBIC, expand=True),
                    OW / 2, V(560, 330), 1.45 * back(ramp(f, 0, 10)))
    elif si == 17:
        selo_txt(im, 'NO DIA SEGUINTE', V(540, 960), V(300, 130), ramp(f, 0, 8), V(72, 68), cor=(90, 160, 80))
    elif si == 20:
        ma = wt(20, 'mas') - 3
        if HOR: moral_txt(im, ['O TEMPO NÃO VOLTA.'] + (['MAS A *PRESENÇA*', 'PODE COMEÇAR *HOJE*.'] if f >= ma else []), ramp(f, 0, 8))
        else: moral_txt(im, ['O TEMPO', 'NÃO VOLTA.'] + (['MAS A *PRESENÇA*', 'PODE COMEÇAR', '*HOJE*.'] if f >= ma else []), ramp(f, 0, 8))
    return im.convert('RGB')
