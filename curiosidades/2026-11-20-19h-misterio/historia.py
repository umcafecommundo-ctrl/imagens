"""Formato MISTÉRIO: "A praia das garrafas", PARTE 1 (20/11/2026, 19h; 1ª história do formato novo, pedido do Luis).
História inventada. Narradora: menina de cabelo comprido castanho, blusa coral (mesmas cores na parte 2).
Premissa: toda manhã a maré traz uma garrafa com um bilhete com o nome de um morador e um pedido simples; quem cumpre ganha
um presente no dia seguinte; ninguém sabe quem joga; hoje a garrafa veio com o nome dela e um aviso: não vem à praia amanhã.
Cenários/cores: s0-s1 praia de manhã (dia, cores vivas) | s2 rua de dia (vivo, andando) | s3 praia no fim de tarde (tarde) |
s4 praia com neblina (sombrio) | s5-s6 praia de madrugada fria (frio) | s7 praia à noite (sombrio_noite)."""
from kit import *
import kit
from sombrio import *

instala_legenda()
MUSICA = False
VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'
EU = dict(penteado='longo', cabelo='#6b3e26', roupa='#e07a5f', calca='#2f3f66')

LINES = [
    "Na praia da minha cidade, toda manhã, a maré traz uma garrafa com um bilhete dentro.",
    "Cada bilhete tem o nome de um morador, e um pedido simples.",
    "Rega a planta da vizinha. Devolve o livro da biblioteca. Liga pra sua avó.",
    "A regra é antiga: quem cumpre o pedido antes do pôr do sol ganha um presente na garrafa do dia seguinte.",
    "Ninguém nunca descobriu quem joga as garrafas no mar.",
    "Hoje cedo, a garrafa veio com o meu nome.",
    "Mas o bilhete não tinha pedido nenhum. Só um aviso.",
    "Não vem à praia amanhã.",
]
FALA_TIKTOK = "Quer a parte dois? Comenta parte dois, e segue pra não perder!"
CTA_TEXTO = "PARTE 2?"
CTA_CARD = cta_card
TWIST = 5
FLASH = []
CHECK = [(0, 'garrafa', 6), (1, 'nome', 4), (1, 'pedido', 4), (2, 'planta', 3), (2, 'livro', 3), (2, 'avo', 3),
         (3, 'regra', 4), (3, 'presente', 6), (4, 'mar', 6), (5, 'nome', 6), (6, 'aviso', 6), (7, 'amanha', 10)]
CAM = {}


def SFX(s):
    for si in range(8): s.patter(s.W(si, LINES[si].split()[0].strip(',.:')) - 4, s.W(si, LINES[si].split()[0].strip(',.:')) + 40, 4, .05)
    s.splash(s.W(0, 'garrafa') - 3, .3); s.ting(s.W(0, 'bilhete'), .25)
    s.ting(s.W(1, 'nome'), .2)
    for w in ('planta', 'livro', 'avo'): s.thunk(s.W(2, w) - 2, 500, .3)
    s.thunk(s.W(3, 'regra') - 2, 90, .7); s.ting(s.W(3, 'presente'), .35)
    s.whoosh(s.W(4, 'mar') - 6, .8, .3)
    s.splash(s.W(5, 'garrafa') - 3, .3); s.thunk(s.W(5, 'nome') - 2, 120, .8)
    s.whoosh(s.W(6, 'aviso') - 4, .5, .3)
    s.thunk(s.W(7, 'amanha') - 2, 60, 1.0)


def to_out(si, x, y):
    cx, cy, z, _ = CAM.get(si, (621, 1104, 1, 0))
    k = OW / W_ * z
    return (x - cx) * k + OW / 2, (y - cy) * k + OH / 2


@lru_cache(maxsize=4)
def presente_img(w):
    p = Pen(300, 300)
    p.shape([(30, 110), (270, 110), (270, 290), (30, 290)], hexc('#d9534f'), hexc('#b03a36'), 6, 10)
    p.shape([(15, 70), (285, 70), (285, 120), (15, 120)], hexc('#e8635f'), None, 6, 0)
    p.shape([(130, 70), (170, 70), (170, 290), (130, 290)], hexc('#ffd23f'), None, 5, 0)
    for s in (-1, 1): p.shape(ell_pts(150 + s * 50, 50, 50, 28, 20), hexc('#ffd23f'), None, 5, 0)
    return p.img.resize((w, w), Image.LANCZOS)


@lru_cache(maxsize=12)
def silhueta(k):
    im = menino(phase=k / 12 * 6.283, walk=1)
    a = im.getchannel('A')
    out = Image.new('RGBA', im.size, (44, 50, 52, 255)); out.putalpha(a.point(lambda v: int(v * .85)))
    return out


def menina(c, x, f, feet=1760, h=960, **kw):
    put_menino(c, x, feet, h, f, **dict(EU, **kw))


# ---------------------------------------------------------------- cenas
def s0(f):
    c = praia_bg('dia').copy(); espuma(c, f)
    g = wt(0, 'garrafa') - 3
    t = easeOut(ramp(f, 0, g + 20))
    put_garrafa(c, lerp(1000, 820, t), lerp(1080, 1420, t) + 10 * math.sin(f * .15), 190, rot=lerp(70, 15, t) + 8 * math.sin(f * .12))
    menina(c, 380, f, expr='neutro', look=.75)
    cam = (lerp(800, 640, smooth(ramp(f, 0, 90))), 1250, lerp(1.3, 1.08, smooth(ramp(f, 0, 90))) * (1 + .0008 * f), 0)
    CAM[0] = cam
    return c, cam, 'vivo'


def s1(f):
    c = praia_bg('dia').copy(); espuma(c, f)
    menina(c, 400, f, expr='neutro', look=.5)
    hx, hy = mao_dir(400, 1760, 960)
    put_garrafa(c, hx + 20, hy, 190, rolha=False, bilhete=False)
    cam = (640, 1200, 1.12 * (1 + .0008 * f), 0); CAM[1] = cam
    return c, cam, 'vivo'


def s2(f):
    c = rua(f, f * 9, luz='dia', neb=0)
    menina(c, 430, f, walk=1, expr='sorriso', look=.5)
    cam = (621, 1180, 1.12 * (1 + .0006 * f), 0); CAM[2] = cam
    return c, cam, 'vivo'


def s3(f):
    c = praia_bg('tarde').copy(); espuma(c, f, 'tarde')
    pr = wt(3, 'presente') - 3
    menina(c, 380, f, expr='sorriso' if f >= pr else 'neutro', look=.75)
    if f >= pr:
        put_garrafa(c, 820, 1440, 220, rot=20)
        im = presente_img(int(180 * back(ramp(f, pr, pr + 10))) or 4)
        c.alpha_composite(im, (int(900 - im.width / 2), int(1260 - im.height / 2)))
    cam = (640, 1220, lerp(1.05, 1.15, smooth(ramp(f, 0, 120))) * (1 + .0006 * f), 0); CAM[3] = cam
    return c, cam, 'tarde'


def s4(f):
    c = praia_bg('neblina').copy(); espuma(c, f, 'neblina')
    sil = silhueta(int(((f * .28) % 6.283) / 6.283 * 12)).resize((200, 333), Image.LANCZOS)
    c.alpha_composite(sil, (int(880 - f * .5 - 100), 1300 - 333))
    put_garrafa(c, 915 - f * .5, 1215, 60, rot=20)
    nb = neblina_img(1.6); o2 = int(f * 1.5) % W_
    c.alpha_composite(nb.crop((o2, 0, o2 + W_, 420)), (0, 880))
    t = smooth(ramp(f, 0, 120))
    cam = (621, lerp(1150, 1050, t), lerp(1.0, 1.25, t), 0); CAM[4] = cam
    return c, cam, 'sombrio'


def s5(f):
    c = praia_bg('frio').copy(); espuma(c, f, 'frio')
    no = wt(5, 'nome') - 3
    menina(c, 400, f, expr='choque' if f >= no else 'neutro', look=.5 if f < no else .25)
    hx, hy = mao_dir(400, 1760, 960)
    put_garrafa(c, hx + 20, hy, 190)
    cam = (640, 1200 + kick(f, no, .8) * 12, 1.1 * (1 + .0008 * f), 0); CAM[5] = cam
    return c, cam, 'frio'


def s6(f):
    c = praia_bg('frio').copy(); espuma(c, f, 'frio')
    menina(c, 360, f, expr='preocupado', look=.75)
    t = smooth(ramp(f, 0, 100))
    cam = (lerp(640, 600, t), lerp(1200, 1080, t), lerp(1.1, 1.3, t), 0); CAM[6] = cam
    return c, cam, 'frio'


def s7(f):
    c = praia_bg('noite').copy(); espuma(c, f, 'noite')
    menina(c, 621, f, expr='choque', look=0)
    t = smooth(ramp(f, 0, 120))
    cam = (621, lerp(1250, 1000, t), lerp(1.05, 1.6, t), 0); CAM[7] = cam
    return c, cam, 'sombrio_noite'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


# ---------------------------------------------------------------- HUD
def OVERLAY(im, si, lf):
    im = im.convert('RGBA'); f = lf
    if si == 0:
        stamp(im, 'PARTE 1', 540, 330, back(ramp(f, 0, 8)) * (1 - ramp(f, 40, 46)), 110, big=True)
        stamp(im, 'NA MINHA PRAIA', 540, 150, back(ramp(f, 46, 54)), 70)
        g = wt(0, 'garrafa') - 3
        gx, gy = to_out(0, 820, 1420)
        card(im, 'Garrafa', 'chega toda manhã com a maré', 640, 560, ramp(f, g + 6, g + 16), alvo=(gx, gy - 60))
    elif si == 1:
        n = wt(1, 'nome') - 3; pd = wt(1, 'pedido') - 3
        b = bilhete_img('MORADOR:|_______', 420) if f < pd else bilhete_img('MORADOR:|PEDIDO:', 420)
        kit.paste_c(im, b, 700, 520, back(ramp(f, n - 6, n + 4)))
        card(im, 'Regra 1', '1 nome e 1 pedido simples', 640, 1200, ramp(f, pd, pd + 10))
    elif si == 2:
        ws = [('planta', 'REGA A PLANTA|DA VIZINHA'), ('livro', 'DEVOLVE O LIVRO|DA BIBLIOTECA'), ('avo', 'LIGA PRA|SUA AVÓ')]
        ks = [wt(2, w) - 6 for w, _ in ws] + [10 ** 6]
        for i, (w, t) in enumerate(ws):
            if ks[i] <= f < ks[i + 1]:
                kit.paste_c(im, bilhete_img(t, 460).rotate((-4, 3, -2)[i], Image.BICUBIC, expand=True), 640, 460, back(ramp(f, ks[i], ks[i] + 8)))
    elif si == 3:
        rg = wt(3, 'regra') - 3
        a = ramp(f, rg + 20, rg + 32)
        stamp(im, 'A REGRA', lerp(540, 220, a), lerp(330, 170, a), back(ramp(f, rg, rg + 8)) * lerp(1.3, .7, a), 96, big=True)
        cu = wt(3, 'cumpre') - 3
        card(im, 'Antes do pôr do sol', 'pedido cumprido = presente amanhã', 600, 470, ramp(f, cu, cu + 10))
    elif si == 4:
        n = wt(4, 'ninguem') - 3
        interrog(im, 540, 430, f, back(ramp(f, n, n + 8)))
        card(im, 'Quem joga as garrafas?', 'ninguém nunca descobriu', 540, 600, ramp(f, n + 8, n + 18))
    elif si == 5:
        stamp(im, 'HOJE CEDO', 230, 150, back(ramp(f, 0, 8)), 64)
        no = wt(5, 'nome') - 3
        kit.paste_c(im, bilhete_img('PARA:|EU', 360).rotate(-4, Image.BICUBIC, expand=True), 760, 470, back(ramp(f, no - 4, no + 6)))
        hx, hy = to_out(5, 400, 1760 - 960 * .78)
        burst(im, '?!', hx + 150, hy - 40, back(ramp(f, no, no + 8)), 60)
    elif si == 6:
        pd = wt(6, 'pedido') - 3; av = wt(6, 'aviso') - 3
        card(im, 'Sem pedido', 'nenhuma tarefa dessa vez', 640, 420, ramp(f, pd, pd + 10) * (1 - ramp(f, av - 4, av)))
        stamp(im, 'AVISO', 640, 420, back(ramp(f, av, av + 8)), 110, big=True, rot=3)
    elif si == 7:
        n = wt(7, 'nao') - 6
        kit.paste_c(im, bilhete_img('NÃO VEM À PRAIA|AMANHÃ.', 600).rotate(-3, Image.BICUBIC, expand=True), 540, 420, back(ramp(f, n, n + 10)))
    return grao(im.convert('RGB'), lf)
