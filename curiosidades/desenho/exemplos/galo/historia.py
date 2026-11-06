"""Exemplo do formato DESENHO: por que o galo canta de manhã (Curiosidades da IA, 05/11/2026).
Fatos: Shimmura & Yoshimura 2013 (Current Biology, Nagoya, 40 galos em luz constante);
Shimmura et al. 2015 (Scientific Reports, o galo de maior posição canta primeiro);
Claes et al. 2017 (Zoology: >100 dB; o canal do ouvido do galo se fecha com o bico aberto)."""
from kit import *

# 1 frase por cena. A narração (voz Antonio +15%) é gerada destas frases.
LINES = [
    "O galo não canta por causa do sol.",
    "No Japão, cientistas deixaram quarenta galos numa sala com a luz acesa o tempo todo.",
    "Sem nascer do sol, sem janela aberta... e mesmo assim, de manhãzinha: cocoricó!",
    "E tem fila: o galo chefe canta primeiro. Os outros esperam a vez.",
    "Você vê, o galo tem um relógio interno, como o nosso, que avisa que o dia está chegando.",
    "O canto passa de cem decibéis, igual a uma motosserra. Mas quando ele abre o bico, o ouvido se fecha sozinho.",
    "Ou seja: quem acorda o galo... é o próprio galo.",
]
# legenda na tela (mesmas palavras; números podem virar algarismos; '|' quebra em 2 frases)
CAPTXT = ["O galo não canta por causa do sol.",
          "No Japão, cientistas deixaram quarenta galos|numa sala com a luz acesa o tempo todo.",
          "Sem nascer do sol, sem janela aberta...|e mesmo assim, de manhãzinha: cocoricó!",
          "E tem fila: o galo chefe canta primeiro.|Os outros esperam a vez.",
          "Você vê, o galo tem um relógio interno, como o nosso,|que avisa que o dia está chegando.",
          "O canto passa de 100 decibéis, igual a uma motosserra.|Mas quando ele abre o bico, o ouvido se fecha sozinho.",
          "Ou seja: quem acorda o galo... é o próprio galo."]
# fim só do TikTok (fala + texto grande na tela). O YouTube termina na virada (loop).
FALA_TIKTOK = "Você sabia dessa? Comenta sim ou não, e segue pra mais curiosidades!"
CTA_TEXTO = "SIM OU NÃO?"
TWIST = 6          # cena da virada: a música para e entra o sting
FLASH = [6]        # cenas que começam com flash branco (salto de tempo)
CHECK = [(0, 'sol', 4), (2, 'cocorico', 6), (3, 'chefe', 8), (5, 'motosserra', 4), (5, 'fecha', 6), (6, 'quem', 10)]


def SFX(s):
    s.whoosh(2, .4, .4)
    for i in range(2): s.thunk(s.W(1, 'cientistas') - 3 + i * 5)
    for i in range(5): s.thunk(s.W(1, 'quarenta') - 2 + i * 3, 220, .5)
    s.ting(s.W(1, 'luz'))
    s.patter(s.W(1, 'tempo'), s.W(1, 'tempo') + 30, 12, .12)
    s.thunk(s.W(2, 'cocorico') - 3, 140, .9)
    s.ting(s.W(3, 'chefe'), .25)
    for i in range(3): s.thunk(s.W(3, 'vez') + 2 + i * 7, 260, .4)
    s.thunk(s.W(4, 'relogio') - 4, 200, .5); s.ting(s.W(4, 'dia'), .3)
    s.thunk(s.W(5, 'decibeis') - 2, 120, 1.0); s.thunk(s.W(5, 'motosserra') - 2, 160, .7)
    s.whoosh(s.W(5, 'abre') - 6, .5, .5); s.thunk(s.W(5, 'fecha') - 2, 300, .8)
    s.trill(s.W(6, 'quem'), 1.0, .3)


# ---------------------------------------------------------------- scenes (f = local frame)
def s0(f):
    c = BG('golden').copy()
    cr = pulse(f, 0, 30)
    side = f >= wt(0, 'sol') - 2
    put_roo(c, 520, 2160, 1500, crow=cr, expr='side' if side else 'calm', look=1, blink=blinkAt(f, 3) if not cr else 0)
    if f < 34: paste_c(c, txt('COCORICÓ!', 120, 8), 760, 560, back(ramp(f, 2, 10)) * (1 - ramp(f, 28, 34)))
    rings(c, 830, 760, f, 0, 30, 1.3)
    z = lerp(1.38, 1.05, easeOut(ramp(f, 4, 40))) * (1 + .0006 * f)
    return c, (621, 1240, z, 0), 'golden'


def s1(f):
    c = BG('lab').copy()
    on = 1.0 if f >= wt(1, 'luz') else 0.35
    if wt(1, 'luz') <= f < wt(1, 'luz') + 8: on = 1 + .6 * (1 - (f - wt(1, 'luz')) / 8)
    c.alpha_composite(P.lamp_glow(min(1, on)))
    spin = ramp(f, wt(1, 'tempo'), wt(1, 'tempo') + 30)
    paste_c(c, clock_img(round((1 + spin * 6) * 8) / 8, round((spin * 75) * 4) / 4, 280), 640, 420)
    p0 = wt(1, 'cientistas') - 3
    for i, (x, sd, kw) in enumerate(((800, 1, dict(arms='clip', hair='#9a9a9a', skin=3, expr='stern')), (1060, 2, dict(arms='clip', bun=True, expr='neutral')))):
        s = back(ramp(f, p0 + i * 5, p0 + i * 5 + 9))
        put_sci(c, x, 1560, 820 * s, f, sd, **kw)
        put_dust(c, x, 1540, 90, f - p0 - i * 5)
    g0 = wt(1, 'quarenta') - 2
    rnd = random.Random(5)
    for i, x in enumerate((150, 380, 610, 840, 1070)):
        s = back(ramp(f, g0 + i * 3, g0 + i * 3 + 8))
        put_roo(c, x, 1880, 470 * s, flip=i % 2 == 1, blink=blinkAt(f, 10 + i), look=rnd.random() - .5)
        put_dust(c, x, 1860, 70, f - g0 - i * 3)
    rail = P.pen_rail(1242, 260)
    c.alpha_composite(rail, (0, 1700))
    z = lerp(1.3, 1.08, smooth(ramp(f, 0, 50)))
    return c, (lerp(900, 640, smooth(ramp(f, 0, 50))), 1250, z, 0), 'day'


def s2(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    spin = f / 60
    paste_c(c, clock_img(round((spin * 2) * 8) / 8, round(spin * 24 * 4) / 4, 280), 640, 420)
    k = wt(2, 'cocorico')
    awake = f >= k - 3
    cr = pulse(f, k - 3, 32)
    put_sci(c, 1030, 1560, 820, f, 2, arms='ears' if awake else 'clip', bun=True, expr='shock' if awake else 'neutral', look=-1)
    put_roo(c, 560, 2150, 1150, sleep=0 if awake else 1, crow=cr, expr='shock' if (awake and not cr) else 'calm', look=.5)
    if not awake:
        for i in range(3):
            a = (f + i * 14) % 42
            paste_c(c, txt('Z', 70 + i * 16), 760 + a * 3 + i * 40, 1350 - a * 5 - i * 60, 1 - a / 42)
    else:
        paste_c(c, txt('COCORICÓ!', 130, 8), 760, 900, back(ramp(f, k, k + 8)))
        rings(c, 860, 1180, f, k, 32, 1.4)
    # crane from the clock down to the rooster
    t = smooth(ramp(f, 4, 70))
    kick = ((1 if (f - k) % 2 else -1) * (1 - (f - k) / 7)) if 0 <= f - k < 7 else 0
    return c, (lerp(640, 640, t), lerp(560, 1350, t) + kick * 10, lerp(1.9, 1.12, t), kick * 1.5), 'day'


def s3(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(1))
    k = wt(3, 'chefe') - 2
    v = wt(3, 'vez') + 2
    cr0 = pulse(f, k, 34)
    put_roo(c, 230, 1880, 760, crow=cr0, chief=True, expr='smug' if f < k else 'calm', look=1, blink=blinkAt(f, 1) if not cr0 else 0)
    if k <= f < k + 38: paste_c(c, txt('COCORICÓ!', 100, 6), 380, 1130, back(ramp(f, k, k + 8)))
    rings(c, 420, 1300, f, k, 34, 1.0)
    for i, x in enumerate((520, 780, 1040)):
        ci = pulse(f, v + i * 7, 18)
        wait = k <= f < v
        put_roo(c, x, 1850 - i * 20, 600, crow=ci, expr='side' if wait else 'calm', look=-1 if wait else .4, blink=blinkAt(f, 4 + i) if not ci else 0)
        rings(c, x + 170, 1450, f, v + i * 7, 18, .7)
    z = 1.12 + .0008 * f
    return c, (640, 1300, z, 0), 'day'


def s4(f):
    c = BG('lab').copy(); c.alpha_composite(P.lamp_glow(.4))
    put_roo(c, 560, 2200, 1300, blink=blinkAt(f, 6), look=.3 + .3 * math.sin(f * .05))
    r0 = wt(4, 'relogio') - 3
    d0 = wt(4, 'dia') - 2
    content = Image.new('RGBA', (560, 300), (0, 0, 0, 0))
    if f >= r0:
        tick = (f - r0) / 30
        ck = clock_img(round(tick * 2 * 4) / 4, round(tick * 24 * 4) / 4, 260)
        content.alpha_composite(ck, (20 if f >= d0 else 150, 20))
    if f >= d0:
        content.alpha_composite(sun_icon(260, easeOut(ramp(f, d0, d0 + 18))), (290, 20))
    thought(c, 760, 560, 300, back(ramp(f, r0 - 6, r0 + 4)), content)
    z = lerp(1.05, 1.2, smooth(f / 150))
    return c, (680, 1150, z, 0), 'dusk'


def s5(f):
    c = BG('day').copy()
    cr_ = 1.0 if f < wt(5, 'mas') else 0.0
    b0 = wt(5, 'abre') - 2
    cr2 = pulse(f, b0, 60)
    cr = max(cr_ * clamp(f / 4), cr2)
    closed = f >= wt(5, 'fecha') - 2
    ear = None if f < wt(5, 'mas') else ('closed' if closed else 'open')
    put_roo(c, 420, 2100, 1300, crow=cr, ear=ear, look=.6)
    if cr > .5: rings(c, 760, 1050, f % 40 if f < wt(5, 'mas') else f, 0 if f < wt(5, 'mas') else b0, 999, 1.6)
    put_sci(c, 1000, 2050, 1100, f, 2, arms='ears', bun=True, expr='shock' if f < wt(5, 'mas') else 'pained', look=-1)
    d0 = wt(5, 'decibeis') - 2
    if d0 <= f < wt(5, 'mas'): paste_c(c, txt('100 dB', 150, -6), 860, 640, back(ramp(f, d0, d0 + 8)))
    m0 = wt(5, 'motosserra') - 2
    if m0 <= f < wt(5, 'mas'): paste_c(c, txt('= MOTOSSERRA', 86, -6), 760, 800, back(ramp(f, m0, m0 + 8)))
    if closed: paste_c(c, txt('FECHOU!', 90, 6), 560, 1050, back(ramp(f, wt(5, 'fecha') - 2, wt(5, 'fecha') + 6)))
    # push into the head when he opens the beak
    t = easeOut(ramp(f, b0 - 8, b0 + 14))
    kick = ((1 if (f - d0) % 2 else -1) * (1 - (f - d0) / 7)) if 0 <= f - d0 < 7 else 0
    return c, (lerp(640, 620, t), lerp(1350, 1150, t) + kick * 10, lerp(1.08, 2.0, t), kick + t * 2), 'day'


def s6(f):
    c = BG('golden').copy()
    q = wt(6, 'quem') - 2
    p0 = wt(6, 'proprio') - 2
    awake = f >= p0
    put_roo(c, 560, 2160, 1450, sleep=0 if awake else 1, expr='smug' if awake else 'calm', look=-.3, blink=0)
    if not awake and f < q:
        for i in range(3):
            a = (f + i * 14) % 42
            paste_c(c, txt('Z', 70 + i * 16), 780 + a * 3 + i * 40, 1250 - a * 5 - i * 60, 1 - a / 42)
    if f >= q:
        shake = 6 * math.sin(f * 2.2) if f < p0 + 10 else 0
        cont = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
        cont.alpha_composite(clock_img(5 * math.pi / 3 * 0 + 6.0, 0.0, 260, True).rotate(shake, Image.BICUBIC), (20, 20))
        thought(c, 840, 560, 220, back(ramp(f, q, q + 8)), cont)
        if f < p0 + 12: paste_c(c, txt('TRIIIM!', 90, -8), 560, 470, back(ramp(f, q + 4, q + 10)))
    z = lerp(1.05, 1.3, easeOut(ramp(f, 0, 70))) * (1 + .0012 * max(0, f - 60))
    return c, (650, 1200, z, lerp(0, -3, smooth(ramp(f, 0, 70))) - .01 * max(0, f - 70)), 'golden'


SCENES = [s0, s1, s2, s3, s4, s5, s6]
