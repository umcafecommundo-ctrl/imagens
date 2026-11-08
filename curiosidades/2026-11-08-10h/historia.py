"""Formato DESENHO: para que serve o bolsinho pequeno da calça jeans (Curiosidades da IA, 08/11/2026, 10h).
Categoria: INVENÇÕES E OBJETOS.
Fatos: Wikipedia "Jacob W. Davis" (alfaiate em Reno, Nevada; uma mulher pediu calças fortes para o marido, lenhador;
as calças de trabalho rasgavam nas costuras e bolsos; ele reforçou com rebites de cobre; patente americana 139.121,
"Improvement in Fastening Pocket-Openings", de 20 de maio de 1873); Levi Strauss & Co., "Pockets Full of History"
(levistrauss.com, 2017): o bolsinho pequeno da frente é o 'watch pocket', feito para o relógio de bolso, objeto típico do
fim do século 19; as calças originais já tinham três bolsos na frente, inclusive o pequeno acima do bolso direito;
rebites de cobre impediam os bolsos de rasgar). Ipwatchdog, "Blue Jeans Patented May 20, 1873"."""
from kit import *
import kit

LINES = [
    "O bolsinho pequeno da calça jeans não foi feito pra guardar moeda.",
    "No Velho Oeste americano, uma mulher pediu a um alfaiate uma calça bem forte pro marido, que cortava lenha.",
    "É que as calças dele viviam rasgando bem nos bolsos.",
    "Então o alfaiate pregou rebites de cobre nos cantos. Em mil oitocentos e setenta e três, isso virou patente.",
    "E lá na frente, em cima do bolso grande, já tinha um bolsinho bem pequeno.",
    "Você vê, ele era o lugar do relógio de bolso, que o pessoal carregava preso numa corrente.",
    "Hoje o relógio foi pro pulso... e o bolsinho continua lá, esperando ele voltar.",
]
CAPTXT = [
    "O bolsinho pequeno da calça jeans|não foi feito pra guardar moeda.",
    "No Velho Oeste americano, uma mulher pediu a um alfaiate|uma calça bem forte pro marido, que cortava lenha.",
    "É que as calças dele viviam rasgando|bem nos bolsos.",
    "Então o alfaiate pregou rebites de cobre nos cantos.|Em 1873, isso virou patente.",
    "E lá na frente, em cima do bolso grande,|já tinha um bolsinho bem pequeno.",
    "Você vê, ele era o lugar do relógio de bolso,|que o pessoal carregava preso numa corrente.",
    "Hoje o relógio foi pro pulso...|e o bolsinho continua lá, esperando ele voltar.",
]
FALA_TIKTOK = "Você usa esse bolsinho? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 5
FLASH = [1, 6]
CHECK = [(0, 'bolsinho', 4), (0, 'moeda', 6), (1, 'alfaiate', 4), (1, 'lenha', 6), (2, 'rasgando', 4),
         (3, 'rebites', 4), (3, 'patente', 6), (4, 'bolsinho', 6), (5, 'relogio', 4), (5, 'corrente', 6),
         (6, 'pulso', 4), (6, 'esperando', 8)]

JEANS, JEANSD = hexc('#3d5a8a'), hexc('#2c4268')
COBRE = hexc('#c8763a')
LINHA = hexc('#e8a33c')


# ------------------------------------------------------------------ personagens e objetos novos
def pessoa(expr='neutral', arms='hang', blink=0, look=0.0, tilt=0.0, skin=1, hair='#3b2a1e', shirt='#ff8a5c',
           pants='#3d5a8a', hat='', mous=False, bun=False, dress='', vest='', susp=False, tape=False, rip=0,
           pocket=True, wrist=False, swing=0.0):
    """pessoa feijão (600x1000, pés em y≈975). hat: ''|'cowboy'; dress = cor do vestido; vest = cor do colete;
    susp = suspensório; tape = fita métrica no pescoço; rip = bolso rasgado; pocket = bolsinho com rebites visível;
    wrist = relógio de pulso; arms: hang, point, up, cheek, shrug, hammer, axe, watch, wrist, ask."""
    p = Pen(600, 1000)
    sh, shd = hexc(shirt), mul(hexc(shirt), .78)
    pc, pcd = hexc(pants), mul(hexc(pants), .74)
    if dress:
        dc = hexc(dress)
        for s in (-1, 1):
            p.shape(ell_pts(300 + s * 40 + 12, 960, 34, 16), hexc('#3b2a1e'), None, 4)
        p.shape([(220, 600), (380, 600), (450, 945), (150, 945)], dc, mul(dc, .78), 5, 14)
    else:
        for s in (-1, 1):
            top = (300 + s * 40, 690); ft = (300 + s * 44, 950)
            p.line([top, (top[0] + s * 4, 820), ft], pc, 24, 4)
            p.shape(ell_pts(ft[0] + 12, ft[1] + 10, 36, 18), hexc('#5a3d24'), None, 4)
    p.line([(300, 350), (300, 430)], SKINS[skin], 40, 4)
    tc = (300 + tilt * 3, 540 if dress else 560)
    p.shape(ell_pts(tc[0], tc[1], 112, 140 if not dress else 120, 56, math.radians(tilt), 0.12), sh, shd, 5, 16)
    p.arc(300, 420, 40, 22, 10, 170, 5)
    if not dress:
            p.shape([(204, 640), (396, 640), (400, 716), (200, 716)], pc, pcd, 5, 8)
            if pocket:
                p.shape([(222, 650), (262, 650), (262, 690), (222, 690)], pc, pcd, 3, 4)
                p.stroke([(222, 650), (262, 650)], 3, LINHA)
                for x in (222, 262): p.dot(x, 652, 5, COBRE, 2)
            if rip:
                p.poly([(330, 650), (378, 650), (384, 700), (360, 690), (350, 712), (336, 692)], hexc('#f4ead2'), 3)
                p.stroke([(330, 650), (338, 662), (346, 652), (356, 664), (366, 652), (378, 662)], 4)
    if vest:
        vc = hexc(vest)
        p.shape([(196, 470), (282, 440), (290, 690), (210, 680)], vc, mul(vc, .75), 4, 8)
        p.shape([(404, 470), (318, 440), (310, 690), (390, 680)], vc, mul(vc, .75), 4, 8)
        for y in (520, 580, 640): p.dot(296, y, 6, hexc('#d9b44a'), 2)
    if susp:
        for s in (-1, 1): p.line([(300 + s * 60, 440), (300 + s * 54, 690)], hexc('#5a3d24'), 12, 3)
    if tape:
        for s in (-1, 1): p.line([(300 + s * 40, 420), (300 + s * 70, 470), (300 + s * 64, 640)], hexc('#f2d54a'), 12, 3)
    shL, shR = (205, 470), (395, 470)
    A = {'hang': [((185, 560), (190, 650)), ((415, 560), (410, 650))],
         'point': [((185, 560), (190, 650)), ((470, 430), (560, 380))],
         'cheek': [((150, 420), (225, 300)), ((450, 420), (375, 300))],
         'shrug': [((140, 540), (120, 440)), ((460, 540), (480, 440))],
         'up': [((150, 380), (140, 240)), ((450, 380), (460, 240))],
         'hammer': [((180, 560), (250, 600)), ((480, 420), (470, 300))],
         'axe': [((200, 330), (285, 170)), ((400, 330), (315, 170))],
         'axedown': [((190, 560), (380, 600)), ((410, 560), (420, 610))],
         'watch': [((185, 560), (190, 650)), ((470, 500), (430, 410))],
         'wrist': [((185, 560), (190, 650)), ((450, 560), (330, 520))],
         'ask': [((170, 560), (270, 560)), ((430, 560), (330, 560))]}[arms]
    hands = []
    for s_, (el, hd) in zip((shL, shR), A):
        p.line(curve(s_, el, hd, 10), sh, 16, 4)
        p.dot(hd[0], hd[1], 17, SKINS[skin], 4)
        hands.append(hd)
    if arms == 'hammer':
        p.line([(470, 300), (500, 170)], hexc('#9b6b3d'), 14, 4)
        p.shape([(450, 140), (560, 160), (552, 200), (442, 180)], hexc('#8d939e'), hexc('#5f6470'), 4, 6)
    if arms == 'axe':
        p.line([(300, 190), (300, 10)], hexc('#9b6b3d'), 16, 4)
        p.shape([(300, 20), (390, -10), (400, 90), (300, 70)], hexc('#b9c0cb'), hexc('#7f8794'), 4, 8)
    if arms == 'axedown':
        p.line([(395, 600), (560, 700)], hexc('#9b6b3d'), 16, 4)
        p.shape([(540, 640), (600, 650), (580, 760), (520, 720)], hexc('#b9c0cb'), hexc('#7f8794'), 4, 8)
    if arms == 'watch':
        p.stroke(curve((430, 430), (330, 600), (242, 660), 14), 4, hexc('#d9b44a'))
        p.shape(ell_pts(430, 400, 34, 34, 32), hexc('#e8c25a'), hexc('#b8902a'), 4, 6)
        p.dot(430, 400, 24, (255, 255, 255))
        p.stroke([(430, 400), (430, 384)], 4); p.stroke([(430, 400), (442, 404)], 4)
    if wrist or arms == 'wrist':
        hx, hy = hands[1]
        p.shape(ell_pts(hx + 26, hy + 6, 22, 22, 24), hexc('#333a48'), None, 4)
        p.dot(hx + 26, hy + 6, 14, (255, 255, 255))
    hc = (300 + tilt * 6, 262)
    hcol = hexc(hair)
    p.shape(ell_pts(hc[0], hc[1] - 30, 124, 100, 48), hcol, mul(hcol, .7), 5, 10)
    if bun: p.shape(ell_pts(hc[0], hc[1] - 130, 46, 36, 32), hcol, mul(hcol, .7), 5, 6)
    p.shape(ell_pts(hc[0], hc[1], 118, 106, 56, math.radians(tilt * 1.5), 0.08, 2.4), SKINS[skin], mul(SKINS[skin], .86), 5, 16)
    p.dot(hc[0] - 112, hc[1] + 10, 16, SKINS[skin], 4); p.dot(hc[0] + 112, hc[1] + 10, 16, SKINS[skin], 4)
    if not hat:
        fr = [(hc[0] - 122, hc[1] - 6), (hc[0] - 116, hc[1] - 84), (hc[0] - 50, hc[1] - 118), (hc[0] + 50, hc[1] - 118), (hc[0] + 116, hc[1] - 84),
              (hc[0] + 122, hc[1] - 10), (hc[0] + 80, hc[1] - 56), (hc[0] + 20, hc[1] - 74), (hc[0] - 50, hc[1] - 60), (hc[0] - 96, hc[1] - 36)]
        p.shape(fr, hcol, mul(hcol, .7), 5, 8)
    face(p, hc[0], hc[1] + 10, expr, blink, look)
    if mous:
        p.poly([(hc[0] - 40, hc[1] + 46), (hc[0], hc[1] + 38), (hc[0] + 40, hc[1] + 46), (hc[0] + 28, hc[1] + 56), (hc[0], hc[1] + 48), (hc[0] - 28, hc[1] + 56)], hexc('#5b3a22'), 3)
    if hat == 'cowboy':
        hb, hd_ = hexc('#9b6a3a'), hexc('#6f4a26')
        p.shape([(hc[0] - 80, hc[1] - 70), (hc[0] - 70, hc[1] - 170), (hc[0], hc[1] - 150), (hc[0] + 70, hc[1] - 170), (hc[0] + 80, hc[1] - 70)], hb, hd_, 5, 10)
        p.shape(ell_pts(hc[0], hc[1] - 72, 175, 30, 40), hb, hd_, 5, 6)
        p.poly([(hc[0] - 78, hc[1] - 104), (hc[0] + 78, hc[1] - 104), (hc[0] + 79, hc[1] - 84), (hc[0] - 79, hc[1] - 84)], hexc('#3b2a1e'))
    return p.img


def put_pessoa(c, x, feet, h, f, seed, **kw):
    kit._bean(c, 'pessoa', x, feet, h, f, seed, **kw)


def calca(eyes=0, expr='calm', look=0.0, blink=0, rip=0, rivets=1, glow=0):
    """calça jeans de frente (600x820). eyes=1 põe carinha no bolsinho; rip = bolso rasgado; glow = destaque no bolsinho."""
    p = Pen(600, 820)
    p.shape([(95, 110), (505, 110), (560, 800), (330, 800), (300, 360), (270, 800), (40, 800)], JEANS, JEANSD, 6, 22)
    p.shape([(90, 50), (510, 50), (505, 115), (95, 115)], JEANS, JEANSD, 6, 8)
    for x in (120, 230, 370, 480): p.shape([(x - 12, 46), (x + 12, 46), (x + 12, 122), (x - 12, 122)], JEANS, None, 3)
    p.dot(300, 82, 14, COBRE, 3)
    p.stroke([(300, 115), (300, 330)], 4, LINHA)
    for s in (-1, 1):
        pts = [(300 + s * 195, 125), (300 + s * 150, 175), (300 + s * 110, 205), (300 + s * 75, 210)]
        pts2 = pts if s < 0 else pts
        p.stroke(curve((300 + s * 195, 270), (300 + s * 110, 140), (300 + s * 70, 125), 14), 5)
        p.stroke(curve((300 + s * 185, 285), (300 + s * 105, 160), (300 + s * 60, 140), 14), 3, LINHA)
        if rivets:
            p.dot(300 + s * 195, 270, 10, COBRE, 3); p.dot(300 + s * 70, 125, 10, COBRE, 3)
    # bolsinho (lado esquerdo de quem olha = lado direito de quem veste)
    bx0, by0, bx1, by1 = 120, 150, 235, 255
    p.shape([(bx0, by0), (bx1, by0), (bx1, by1), (bx0, by1)], JEANS, JEANSD, 5, 6)
    p.stroke([(bx0 + 6, by0 + 12), (bx1 - 6, by0 + 12)], 3, LINHA)
    if rivets:
        p.dot(bx0, by0, 9, COBRE, 3); p.dot(bx1, by0, 9, COBRE, 3)
    if glow:
        p.stroke([(bx0 - 12, by0 - 12), (bx1 + 12, by0 - 12), (bx1 + 12, by1 + 12), (bx0 - 12, by1 + 12), (bx0 - 12, by0 - 12)], 8, hexc('#ffd84a'))
    if eyes:
        cx, cy = (bx0 + bx1) / 2, by0 + 58
        for dx in (-22, 22):
            if blink: p.stroke([(cx + dx - 12, cy), (cx + dx + 12, cy)], 5)
            else:
                p.dot(cx + dx, cy, 16 if expr == 'shock' else 13, (255, 255, 255), 4)
                p.dot(cx + dx + look * 5, cy + 2, 6, INK)
        if expr == 'sad': p.arc(cx, cy + 34, 14, 7, 200, 340, 4)
        elif expr == 'shock': p.dot(cx, cy + 32, 8, hexc('#7a2e2e'), 3)
        else: p.arc(cx, cy + 22, 14, 7, 20, 160, 4)
    if rip:
        p.poly([(380, 210), (470, 230), (480, 330), (440, 300), (420, 350), (395, 300)], hexc('#f4ead2'), 4)
    return p.img


def put_calca(c, x, y, h, f, seed=1, rot=0, **kw):
    """y = centro."""
    if 'eyes' in kw: kw['blink'] = 1 if blinkAt(f, seed) > .6 else 0
    im = sprite('calca', tuple(sorted(kw.items())), int(h), 600 / 820, False)
    if rot: im = im.rotate(rot, Image.BICUBIC, expand=True)
    paste_c(c, im, x, y + 3 * math.sin((f + seed * 9) * .1))


def moeda(size=120):
    p = Pen(200, 200)
    p.shape(ell_pts(100, 100, 80, 80, 40), hexc('#f2c94c'), hexc('#c99a2e'), 6, 10)
    p.dot(100, 100, 50, hexc('#f7d978'))
    p.stroke([(100, 70), (100, 130)], 8, hexc('#c99a2e'))
    return p.img.resize((size, size), Image.LANCZOS)


def relogio_bolso(size=260, ang=0.0):
    p = Pen(300, 340)
    p.dot(150, 40, 26, hexc('#e8c25a'), 5); p.dot(150, 40, 12, (255, 255, 255, 0) if False else hexc('#fff3c4'))
    p.shape(ell_pts(150, 190, 130, 130, 56), hexc('#e8c25a'), hexc('#b8902a'), 6, 12)
    p.dot(150, 190, 104, (255, 255, 255))
    for i in range(12):
        a = i * math.pi / 6
        p.stroke([(150 + 86 * math.cos(a), 190 + 86 * math.sin(a)), (150 + 96 * math.cos(a), 190 + 96 * math.sin(a))], 5)
    p.stroke([(150, 190), (150 + 70 * math.sin(ang), 190 - 70 * math.cos(ang))], 7)
    p.stroke([(150, 190), (150 + 45 * math.sin(ang / 12 + 1), 190 - 45 * math.cos(ang / 12 + 1))], 9)
    p.dot(150, 190, 9, INK)
    return p.img.resize((int(size * 300 / 340), size), Image.LANCZOS)


@lru_cache(maxsize=4)
def loja(luz='day'):
    """alfaiataria do Velho Oeste: parede de tábuas, prateleira com rolos de tecido, janela para o deserto."""
    import cenarios as C
    fy = 1560
    base = Image.new('RGBA', (BW, BH), (0, 0, 0, 255)); p = Pen(BW, BH)
    p.poly([(0, 0), (BW, 0), (BW, fy), (0, fy)], hexc('#c9935a'))
    for x in range(0, BW, 110): p.stroke([(x, 0), (x, fy)], 5, hexc('#a8743f'))
    # janela com deserto e cacto
    t, b = C.CEUS.get(luz, C.CEUS['day'])
    x0, y0, x1, y1 = 760, 330, 1120, 760
    p.shape([(x0 - 24, y0 - 24), (x1 + 24, y0 - 24), (x1 + 24, y1 + 24), (x0 - 24, y1 + 24)], hexc('#7a4f2a'), hexc('#5a3a1e'), 6, 6)
    p.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], hexc(b)); p.poly([(x0, y0), (x1, y0), (x1, 520), (x0, 520)], hexc(t))
    p.poly([(x0, 640), (x1, 610), (x1, y1), (x0, y1)], hexc('#e9b96a'))
    p.line([(1010, 700), (1010, 560)], hexc('#5f9a4a'), 34, 5); p.line([(1010, 640), (970, 640), (970, 590)], hexc('#5f9a4a'), 22, 5)
    p.stroke([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], 6)
    p.stroke([((x0 + x1) / 2, y0), ((x0 + x1) / 2, y1)], 10, hexc('#7a4f2a'))
    # prateleira com rolos de tecido
    for sy in (520, 820):
        p.shape([(60, sy), (620, sy), (620, sy + 30), (60, sy + 30)], hexc('#7a4f2a'), hexc('#5a3a1e'), 5, 6)
        for i, col in enumerate(('#3d5a8a', '#a0522d', '#d9c9a3', '#3d5a8a', '#6b8e5a')):
            cx = 120 + i * 110
            p.shape(ell_pts(cx, sy - 95, 50, 95, 32), hexc(col), mul(hexc(col), .75), 5, 10)
            p.dot(cx, sy - 95, 14, mul(hexc(col), .6))
    # mesa de corte à direita
    p.shape([(700, 1250), (1242, 1250), (1242, 1300), (700, 1300)], hexc('#8a5f35'), hexc('#65452a'), 6, 8)
    for x in (740, 1200): p.line([(x, 1300), (x, 1560)], hexc('#65452a'), 26, 5)
    p.shape([(780, 1215), (1020, 1215), (1040, 1250), (760, 1250)], JEANS, JEANSD, 4, 6)
    p.poly([(0, fy), (BW, fy), (BW, BH), (0, BH)], hexc('#9a6a3e'))
    for y in range(fy + 80, BH, 120): p.stroke([(0, y), (BW, y)], 4, hexc('#7d5430'))
    p.stroke([(0, fy), (BW, fy)], 8)
    base.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return base


@lru_cache(maxsize=4)
def mata(luz='day'):
    """floresta com toco e lenha (onde o lenhador trabalha)."""
    c = CEN('floresta', luz).copy()
    p = Pen(BW, BH)
    p.shape([(830, 1660), (1070, 1660), (1090, 1820), (810, 1820)], hexc('#8a5f35'), hexc('#65452a'), 6, 10)
    p.shape(ell_pts(950, 1660, 120, 34, 40), hexc('#e7c08a'), hexc('#c99a62'), 5, 6)
    for i in range(3):
        p.shape(ell_pts(150 + i * 80, 1900 - (i % 2) * 40, 90, 40, 32), hexc('#9b6b3d'), hexc('#6f4a26'), 5, 8)
    c.alpha_composite(p.img.resize((BW, BH), Image.LANCZOS))
    return c


def SFX(s):
    s.ting(s.W(0, 'moeda'), .3)
    s.thunk(s.W(0, 'moeda') + 8, 300, .6)
    s.whoosh(s.W(1, 'alfaiate') - 6, .4, .4)
    s.thunk(s.W(1, 'lenha') - 2, 160, .7)
    s.thunk(s.W(2, 'rasgando') - 2, 120, .9)
    for i in range(3): s.thunk(s.W(3, 'rebites') - 2 + i * 6, 420, .5)
    s.ting(s.W(3, 'patente'), .35)
    s.ting(s.W(4, 'bolsinho'), .3)
    s.whoosh(s.W(5, 'relogio') - 6, .5, .4)
    s.trill(s.W(6, 'esperando'), .9, .3)


# ---------------------------------------------------------------- cenas
# s0 quarto (calça jeans no quarto, moeda) | s1 alfaiataria do Velho Oeste (mulher pede ao alfaiate) | s2 floresta (lenhador, bolso rasga)
# s3 alfaiataria (alfaiate prega rebites, patente 1873) | s4 floresta (lenhador, zoom no bolsinho) | s5 floresta (relógio de bolso)
# s6 quarto (jovem com relógio de pulso, bolsinho esperando)
FY = 1560


def s0(f):
    c = CEN('quarto', 'day').copy()
    b0 = wt(0, 'bolsinho') - 3
    m0 = wt(0, 'moeda') - 3
    put_calca(c, 640, 1100, 1100, f, 1, eyes=1, expr='shock' if f >= m0 else 'calm', look=-.5, glow=1 if f >= b0 else 0)
    if f >= m0:
        t = ramp(f, m0, m0 + 10)
        x = lerp(1000, 470, t); y = lerp(500, 880, t) - 140 * math.sin(t * math.pi)
        if f < m0 + 16: paste_c(c, moeda(150), x, y)
        else: paste_c(c, moeda(150), 470 + (f - m0 - 16) * 6, 900 + (f - m0 - 16) ** 2 * .9)
        paste_c(c, txt('MOEDA? NÃO!', 100, -5), 640, 420, back(ramp(f, m0 + 4, m0 + 12)))
    elif f >= b0:
        paste_c(c, txt('ESSE AQUI', 90, 5), 520, 560, back(ramp(f, b0, b0 + 8)))
    t = easeOut(ramp(f, 0, 40))
    kk = kick(f, m0 + 10)
    return c, (lerp(560, 620, t), 1000 + kk * 10, lerp(1.7, 1.2, t), kk), 'day'


def s1(f):
    c = loja('day').copy()
    a0 = wt(1, 'alfaiate') - 3
    l0 = wt(1, 'lenha') - 3
    put_pessoa(c, 330, 1900, 1050, f, 1, expr='neutral' if f < l0 else 'grin', arms='ask' if f < l0 else 'point', dress='#7a5c9e', bun=True,
               hair='#6b3a1e', shirt='#7a5c9e', skin=0, look=1)
    s = back(ramp(f, a0, a0 + 9))
    put_pessoa(c, 900, 1920, 1080 * s, f, 2, expr='neutral' if f < l0 else 'shock', arms='hang', shirt='#f4f1e6', vest='#4b3a2a',
               pants='#55505a', mous=True, tape=True, pocket=False, skin=2, hair='#2b2b2b', look=-1)
    put_dust(c, 900, 1900, 90, f - a0)
    if f >= l0:
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        cont.alpha_composite(sprite('pessoa', tuple(sorted(dict(arms='axe', hat='cowboy', shirt='#c0392b', susp=True, skin=1, expr='grin', blink=0, tilt=0.0).items())), 280, .6, False), (66, 10))
        thought(c, 430, 800, 220, back(ramp(f, l0 - 4, l0 + 6)), cont)
    t = smooth(ramp(f, 0, 120))
    return c, (lerp(560, 640, t), 1260, lerp(1.25, 1.12, t), 0), 'day'


def s2(f):
    c = mata('day').copy()
    r0 = wt(2, 'rasgando') - 3
    ph = (f // 9) % 2
    ripped = f >= r0
    put_pessoa(c, 560, 1960, 1150, f, 3, arms='axe' if (ph == 0 and not ripped) else 'axedown', hat='cowboy', shirt='#c0392b', susp=True,
               skin=1, expr='shock' if ripped else 'stern', rip=1 if ripped else 0, look=.5)
    if ripped:
        paste_c(c, txt('RASGOU!', 120, -6), 600, 800, back(ramp(f, r0, r0 + 8)))
    kk = kick(f, r0)
    t = smooth(ramp(f, 0, 70))
    return c, (600, lerp(1300, 1380, t) + kk * 12, lerp(1.15, 1.3, t), kk * 1.5), 'day'


def s3(f):
    c = loja('day').copy()
    r0 = wt(3, 'rebites') - 3
    p0 = wt(3, 'patente') - 3
    hit = ((f - r0) % 12) < 4 if f >= r0 and f < p0 else False
    put_pessoa(c, 400, 1900, 1080, f, 2, expr='grin' if f >= p0 else 'stern', arms='hammer', shirt='#f4f1e6', vest='#4b3a2a',
               pants='#55505a', mous=True, tape=True, pocket=False, skin=2, hair='#2b2b2b', look=1)
    put_calca(c, 870, 1000, 560, f, 3, rivets=1 if f >= r0 else 0)
    if f >= r0:
        for i in range(min(4, (f - r0) // 6 + 1)):
            if f < p0: paste_c(c, txt('TOC!', 60, -10 + i * 7), 760 + (i % 2) * 220, 700 + i * 40, back(ramp(f, r0 + i * 6, r0 + i * 6 + 5)))
    if f >= p0:
        paste_c(c, txt('PATENTE', 110, -5), 760, 520, back(ramp(f, p0, p0 + 8)))
        paste_c(c, txt('1873', 130, 4), 760, 660, back(ramp(f, p0 + 4, p0 + 12)))
    kk = kick(f, p0) if f >= p0 else 0
    t = smooth(ramp(f, 0, 140))
    return c, (lerp(600, 680, t), 1150 + kk * 10, lerp(1.12, 1.2, t), kk), 'day'


def s4(f):
    c = mata('golden').copy()
    b0 = wt(4, 'bolsinho') - 3
    put_pessoa(c, 620, 2000, 1250, f, 3, arms='hang', hat='cowboy', shirt='#c0392b', susp=True, skin=1, expr='neutral', look=-.5)
    # bolsinho da pessoa: hip block em (222-262, 650-690) no desenho de 600x1000 -> palco
    sc = 1250 / 1000
    px, py = 620 + (242 - 300) * sc, 2000 + 1250 * .025 - (1000 - 670) * sc
    if f >= b0:
        p = Pen(200, 200); p.stroke([(100, 10), (100, 150)], 14, hexc('#ffd84a')); p.poly([(60, 130), (140, 130), (100, 190)], hexc('#ffd84a'), 5)
        paste_c(c, p.img.resize((140, 140), Image.LANCZOS), px, py - 140 - 8 * math.sin(f * .3), back(ramp(f, b0, b0 + 8)))
        paste_c(c, txt('BOLSINHO!', 76, -4), px + 160, py - 330, back(ramp(f, b0 + 2, b0 + 10)))
    t = smooth(ramp(f, 0, 50)); t2 = easeOut(ramp(f, b0 - 10, b0 + 12))
    z = lerp(lerp(1.15, 1.2, t), 1.6, t2)
    return c, (lerp(620, px + 120, t2), lerp(1300, py - 300, t2), z, 0), 'golden'


def s5(f):
    c = mata('dusk').copy()
    r0 = wt(5, 'relogio') - 3
    k0 = wt(5, 'corrente') - 3
    out = f >= r0
    put_pessoa(c, 520, 2000, 1250, f, 3, arms='watch' if out else 'hang', hat='cowboy', shirt='#c0392b', susp=True, skin=1,
               expr='proud' if out else 'neutral', look=1)
    if out:
        paste_c(c, relogio_bolso(300, f * .2), 900, 760 - 10 * math.sin(f * .15), back(ramp(f, r0, r0 + 8)))
        paste_c(c, txt('RELÓGIO DE BOLSO', 76, -4), 700, 430, back(ramp(f, r0 + 2, r0 + 10)))
    if f >= k0: paste_c(c, txt('NA CORRENTE', 70, 4), 760, 1010, back(ramp(f, k0, k0 + 8)))
    t = smooth(ramp(f, 0, 120))
    return c, (lerp(620, 700, t), lerp(1200, 1100, t), lerp(1.12, 1.25, t), 0), 'dusk'


def s6(f):
    c = CEN('quarto', 'dusk').copy()
    p0 = wt(6, 'pulso') - 3
    e0 = wt(6, 'esperando') - 3
    put_pessoa(c, 420, 1960, 1150, f, 4, arms='wrist' if f >= p0 else 'hang', shirt='#2fa38a', skin=3, hair='#2b2b2b', expr='grin' if f >= p0 else 'neutral', look=1)
    put_calca(c, 940, 1150, 700, f, 5, eyes=1, expr='sad' if f >= e0 else 'calm', look=-1)
    if f >= p0 and f < e0: paste_c(c, txt('NO PULSO', 90, -5), 520, 520, back(ramp(f, p0, p0 + 8)))
    if f >= e0: paste_c(c, txt('ESPERANDO...', 76, 5), 900, 760, back(ramp(f, e0, e0 + 8)))
    t = easeOut(ramp(f, 0, 80)); t2 = smooth(ramp(f, e0 - 10, e0 + 30))
    return c, (lerp(640, lerp(700, 820, t2), t), lerp(1250, 1150, t2), lerp(1.1, 1.35, t2), lerp(0, 2.5, t2)), 'dusk'


def _drift(fn):
    def g(f):
        c, (cx, cy, z, r), luz = fn(f)
        return c, (cx, cy, z * (1 + .0009 * f), r), luz
    g.__name__ = fn.__name__
    return g


SCENES = [_drift(s) for s in (s0, s1, s2, s3, s4, s5, s6)]
