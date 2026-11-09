"""anima.futebol — 09/11/2026 19h — FIFPro: Messi na seleção do ano pela 18ª vez (recorde).
Fontes (conferidas em 09/11/2026): CNN Brasil ("FIFPro divulga seleção do ano com Messi e sem o Bola de Ouro Harry Kane"),
Record (Portugal, "FIFPro elege dois portugueses para o onze do ano"), FIFPro.org (World 11: anúncio na segunda 09/11).
Time: Raya (Arsenal); Cubarsí (Barcelona), Hakimi (PSG), Nuno Mendes (PSG); Bellingham (Real Madrid), Rodri (Man. City),
Vitinha (PSG); Haaland (Man. City), Mbappé (Real Madrid), Messi (Inter Miami), Lamine Yamal (Barcelona).
Messi: 18ª escolha, recorde; 39 anos. Harry Kane (Bayern), Bola de Ouro, fora. PSG com 3, o clube com mais. Nenhum brasileiro.
Sem escudos/logos: times por plaquinhas e cores; jogadores são bonecos genéricos."""
from kit import *
import kit
from futebol import *

VOZ = 'pt-BR-AntonioNeural'; RATE = '+12%'
ARROBA = ''  # cartão final vem de futebol.py (CTA_CARD): pergunta + SIGA PARA MAIS, sem @
SELO = 'FIFPRO  ·  SELEÇÃO DO ANO'
SELO_CORES = ((22, 92, 52), (255, 255, 255))

LINES = [
    "Messi entrou de novo na seleção do ano, e bateu um recorde que ninguém mais tem.",
    "Nesta segunda-feira, a FIFPro, o sindicato mundial dos jogadores, revelou o time ideal da temporada.",
    "E quem vota são os próprios jogadores profissionais, do mundo inteiro.",
    "Aos trinta e nove anos, jogando pelo Inter Miami, Messi foi escolhido pela décima oitava vez, mais do que qualquer um na história.",
    "No ataque, ele divide espaço com Mbappé, Haaland e Lamine Yamal.",
    "O PSG é o clube com mais nomes: Hakimi, Nuno Mendes e Vitinha.",
    "E a surpresa: Harry Kane, que acabou de ganhar a Bola de Ouro, ficou de fora.",
    "E nenhum brasileiro entrou no time deste ano.",
]
CAPTXT = [
    "Messi entrou de novo na seleção do ano,|e bateu um recorde que ninguém mais tem.",
    "Nesta segunda-feira, a FIFPro, o sindicato mundial|dos jogadores, revelou o time ideal da temporada.",
    "E quem vota são os próprios jogadores|profissionais, do mundo inteiro.",
    "Aos 39 anos, jogando pelo Inter Miami, Messi foi escolhido|pela 18ª vez, mais do que qualquer um na história.",
    "No ataque, ele divide espaço com|Mbappé, Haaland e Lamine Yamal.",
    "O PSG é o clube com mais nomes:|Hakimi, Nuno Mendes e Vitinha.",
    "E a surpresa: Harry Kane, que acabou de ganhar|a Bola de Ouro, ficou de fora.",
    "E nenhum brasileiro|entrou no time deste ano.",
]
FALA_TIKTOK = "Messi mereceu estar no time do ano? Sim ou não? Comenta aqui, e segue o Anima Futebol pra mais!"
CTA_TEXTO = "MERECEU?"
TWIST = 6
FLASH = [6]
CHECK = [(0, 'recorde', 4), (1, 'FIFPro', 4), (2, 'jogadores', 4), (3, 'oitava', 4), (4, 'Yamal', 4),
         (5, 'Vitinha', 4), (6, 'fora', 4), (7, 'brasileiro', 4)]

MIA, MIA_F = time_('INTER MIAMI')
RMA, RMA_F = time_('REAL MADRID')
MCI, MCI_F = time_('MANCHESTER CITY')
BAR, BAR_F = time_('BARCELONA')
PSG, PSG_F = time_('PSG')
BAY, BAY_F = time_('BAYERN')
BRA, BRA_F = time_('BRASIL')
CINZA, _ = time_('GENÉRICO')
VERDE = ('#1f7a4a', '#ffffff', '#ffffff')


# ------------------------------------------------------------------ cenas
def s0(f):
    c = estadio('dusk').copy()
    gx, gy = put_gol(c)
    re = wt(0, 'recorde') - 4
    put_goleiro(c, f, CINZA, None, arms='shrug', expr='shock' if f >= re else 'nervous', skin=2, hair='#3a3d46')
    put_jog(c, 470, 1990, 860, f, 3, cores=MIA, faixa=MIA_F, arms='up' if f >= re + 8 else 'run', kick=pulse(f, re - 5, 5),
            expr='grin' if f >= re else 'stern', skin=0, hair='#5a3a22')
    put_placa(c, 'MESSI', MIA, 470, 1090, f, 2, 70, -3)
    rb = raio_bola(860)
    if f < re - 5: bx, by, r = 640, 1990 - rb, rb
    else:
        t = ramp(f, re - 5, re + 3)
        bx, by, r = lerp(640, gx + 90, t), lerp(1990 - rb, gy, t) - 120 * math.sin(t * math.pi), lerp(rb, raio_bola(300), t)
    put_bola(c, bx, by, r, f)
    num(c, 'SELEÇÃO DO ANO', 640, 720, f, wt(0, 'selecao') - 3, 100, -3)
    num(c, 'RECORDE!', 640, 900, f, re, 160, 4)
    z = lerp(1.3, 1.08, easeOut(ramp(f, 0, 40))) * (1 + .0008 * f)
    k = kick(f, re)
    return c, (640, 1440 + k * 10, z, k), 'dusk'


def s1(f):
    c = estadio('dusk').copy()
    d0 = wt(1, 'segunda-feira') - 3
    if f >= d0: paste_c(c, calendario('09', 'NOV'), 330, 980, .75 * back(ramp(f, d0, d0 + 8)))
    put_placa(c, 'FIFPRO', VERDE, 880, 980, f, wt(1, 'FIFPro') - 3, 80, 4)
    num(c, 'TIME IDEAL', 640, 720, f, wt(1, 'time') - 3, 140, -3)
    t0 = wt(1, 'FIFPro') - 3
    for i, (x, sd, sk) in enumerate(((230, 4, 1), (520, 5, 3), (800, 6, 0), (1060, 7, 2))):
        if f >= t0 + i * 3:
            s = back(ramp(f, t0 + i * 3, t0 + i * 3 + 8))
            put_jog(c, x, 2010, 640 * s, f, sd, cores=CINZA, faixa=None, arms='cintura', expr='proud', skin=sk, hair='#2b1d14')
    z = lerp(1.0, 1.12, smooth(f / 110))
    return c, (640 + 20 * math.sin(f * .03), 1400, z, 0), 'dusk'


def s2(f):
    c = estadio('day').copy()
    v0 = wt(2, 'vota') - 3
    times = [(MIA, MIA_F), (PSG, PSG_F), (RMA, RMA_F), (BAR, BAR_F), (MCI, MCI_F), (BRA, BRA_F)]
    pos = [(170, 1840, 560), (430, 1880, 600), (700, 1840, 560), (960, 1880, 600), (300, 2060, 700), (850, 2060, 700)]
    for i, ((cx_, fy, h), (co, fa)) in enumerate(zip(pos, times)):
        up = f >= v0 + i * 2
        put_jog(c, cx_, fy, h, f, 10 + i, cores=co, faixa=fa, arms='up' if up else 'hang', expr='grin' if up else 'neutral',
                skin=i % 4, hair=['#2b1d14', '#111111', '#5a3a22', '#3a2a1a'][i % 4])
    num(c, 'QUEM VOTA?', 640, 720, f, wt(2, 'quem') - 3, 130, -3)
    num(c, 'OS JOGADORES!', 640, 890, f, wt(2, 'jogadores') - 3, 110, 3)
    z = lerp(1.15, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    return c, (640, 1440, z, 0), 'golden'


def s3(f):
    c = estadio('dusk').copy()
    oi = wt(3, 'oitava') - 3
    put_jog(c, 640, 2030, 820, f, 3, cores=MIA, faixa=MIA_F, arms='up' if f >= oi else 'joinha', expr='grin' if f >= oi else 'proud',
            skin=0, hair='#5a3a22')
    put_placa(c, 'MESSI', MIA, 640, 1110, f, 0, 64, -3)
    put_placa(c, 'INTER MIAMI', MIA, 640, 1235, f, wt(3, 'Inter') - 3, 46, 3)
    num(c, '39 ANOS', 640, 690, f, wt(3, 'trinta') - 3, 100, -4)
    num(c, '18ª VEZ!', 640, 830, f, oi, 120, 4)
    num(c, 'RECORDE NA HISTÓRIA', 640, 965, f, wt(3, 'historia') - 3, 76, -2)
    k = kick(f, oi, .8)
    return c, (640, 1420 + k * 10, lerp(1.0, 1.08, smooth(f / 150)), k), 'dusk'


def s4(f):
    c = estadio('dusk').copy()
    at = [('MESSI', MIA, MIA_F, 'Messi' if False else None), ('MBAPPÉ', RMA, RMA_F, 'Mbappe'),
          ('HAALAND', MCI, MCI_F, 'Haaland'), ('L. YAMAL', BAR, BAR_F, 'Yamal')]
    xs = (175, 470, 770, 1065)
    num(c, 'ATAQUE', 640, 720, f, wt(4, 'ataque') - 3, 140, -3)
    for i, (nome, co, fa, w) in enumerate(at):
        f0 = 0 if w is None else wt(4, w) - 3
        if f < f0: continue
        s = back(ramp(f, f0, f0 + 8))
        put_jog(c, xs[i], 2000, 620 * s, f, 20 + i, cores=co, faixa=fa, arms='cintura' if i % 2 else 'joinha', expr='proud',
                skin=[0, 3, 0, 2][i], hair=['#5a3a22', '#111111', '#e0c070', '#111111'][i])
        put_placa(c, nome, co, min(max(xs[i], 230), 1010), 1200 + (i % 2) * 120, f, f0, 44, -3 if i % 2 else 3)
    z = lerp(1.0, 1.08, smooth(f / 120))
    return c, (640 + 15 * math.sin(f * .04), 1420, z, 0), 'dusk'


def s5(f):
    c = estadio('day').copy()
    nm = [('HAKIMI', 'Hakimi', 260, 2), ('NUNO MENDES', 'Nuno', 640, 3), ('VITINHA', 'Vitinha', 1010, 0)]
    put_placa(c, 'PSG', PSG, 640, 720, f, wt(5, 'PSG') - 3, 90, -3)
    num(c, '3 NO TIME', 640, 880, f, wt(5, 'mais') - 3, 120, 3)
    for i, (n, w, x, sk) in enumerate(nm):
        f0 = wt(5, w) - 3; fj = wt(5, 'PSG') - 3 + i * 3
        if f < fj: continue
        s = back(ramp(f, fj, fj + 8))
        put_jog(c, x, 2010, 700 * s, f, 30 + i, cores=PSG, faixa=PSG_F, arms='up', expr='grin', skin=sk, hair='#111111')
        put_placa(c, n, PSG, min(max(x, 300), 980), 1180 + (i % 2) * 110, f, f0, 42, 3 if i % 2 else -3)
    z = lerp(1.12, 1.02, easeOut(ramp(f, 0, 40))) * (1 + .0006 * f)
    return c, (640, 1420, z, 0), 'golden'


def s6(f):
    c = estadio('dusk').copy()
    fo = wt(6, 'fora') - 3; bo = wt(6, 'Bola') - 3
    put_jog(c, 640, 2030, 920, f, 40, cores=BAY, faixa=BAY_F, arms='shrug' if f >= fo else 'cintura',
            expr='shock' if f >= fo else 'proud', skin=0, hair='#c9a35a')
    put_placa(c, 'HARRY KANE', BAY, 640, 1110, f, wt(6, 'Harry') - 3, 60, -3)
    num(c, 'SURPRESA!', 640, 720, f, wt(6, 'surpresa') - 3, 140, -4)
    if f < fo: num(c, 'BOLA DE OURO', 640, 900, f, bo, 100, 3)
    else: num(c, 'FICOU DE FORA!', 640, 900, f, fo, 110, 3)
    if f >= bo and f < fo:
        rr = 50 * back(ramp(f, bo, bo + 8)); put_bola(c, 950, 1250, rr, f)
    k = kick(f, fo, 1.0)
    return c, (640, 1420 + k * 10, lerp(1.04, 1.2, smooth(f / 120)), k + lerp(0, 2, smooth(ramp(f, fo, fo + 20)))), 'dusk'


def s7(f):
    c = estadio('dusk').copy()
    br = wt(7, 'brasileiro') - 3
    put_jog(c, 640, 2030, 900, f, 50, cores=BRA, faixa=BRA_F, arms='shrug' if f >= br else 'hang', expr='nervous' if f >= br else 'neutral',
            skin=2, hair='#151515')
    put_placa(c, 'BRASIL', BRA, 640, 1120, f, br, 70, -3)
    num(c, 'NENHUM', 640, 740, f, wt(7, 'nenhum') - 3, 150, -4)
    num(c, 'BRASILEIRO', 640, 900, f, br, 120, 3)
    z = lerp(1.0, 1.12, easeOut(ramp(f, 0, 60))) * (1 + .0005 * f)
    return c, (640, 1400, z, lerp(0, -2, smooth(ramp(f, 0, 60)))), 'dusk'


SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]


def SFX(s):
    s.thunk(s.W(0, 'recorde') - 4, 120, 1.0)
    s.ting(s.W(1, 'FIFPro') - 3, .3)
    s.ting(s.W(2, 'jogadores') - 3, .3)
    s.thunk(s.W(3, 'oitava') - 3, 160, .9)
    s.ting(s.W(4, 'Yamal') - 3, .3)
    s.thunk(s.W(5, 'Vitinha') - 3, 200, .6)
    s.thunk(s.W(6, 'fora') - 3, 140, 1.0)
    s.thunk(s.W(7, 'brasileiro') - 3, 220, .6)
