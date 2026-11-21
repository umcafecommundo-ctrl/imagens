# Formato MISTÉRIO — Curiosidades da IA (desde 21/11/2026, decisão do Luis em 20/11/2026)

**Este é o formato atual da página Curiosidades da IA.** Os posts deixaram de ser curiosidades reais com o Professor Bigode
e passaram a ser HISTÓRIAS DE MISTÉRIO INVENTADAS, em 1ª pessoa, em 2 partes, no estilo do vídeo de referência que o Luis
mandou (cartões na tela, carimbos, placar digital, onomatopeias, legenda de 1 palavra, voz grave e calma, sem música).
O PROFESSOR BIGODE SAIU DE VEZ: não use put_prof nos posts novos. O resto deste guia (motor, wt, câmera, SFX, conferência)
continua valendo; as seções antigas sobre o Professor e as historinhas "explica" ficam só como histórico.

Exemplo oficial completo: `exemplos/misterio/historia.py` (copie e reescreva). Kit do estilo: `sombrio.py`
(`from kit import *` e depois `from sombrio import *`; chame `instala_legenda()` no topo).

## Roteiro
- 1ª pessoa, mundo com UMA regra estranha: "Na minha cidade...", "No meu prédio...", "Na minha escola...", "Na casa da
  minha avó...". Estrutura: a regra estranha -> ninguém sabe a origem -> como a regra funciona (detalhe concreto: hora,
  número, objeto) -> a exceção/o que deu errado -> o acontecimento de hoje -> gancho final.
- Parte 1 (35 a 50 s): termina num gancho forte ("E a única pessoa na praça... era eu."). Parte 2 (35 a 50 s): começa com
  1 frase que situa quem não viu ("Na parte um, o relógio da praça parou..."), resolve com uma virada e um fim que fecha a
  história (pode deixar um arrepio, mas a história termina).
- Clima de mistério/suspense leve: nada de sangue, morte mostrada, violência, suicídio, doença real, crime, política,
  religião, pessoas reais com nome, marcas ou personagens conhecidos. Pode ser estranho e arrepiante, nunca chocante.
- Frases curtas e faladas, números por extenso, 6 a 9 LINES por parte. Não use "Você vê".
- `FALA_TIKTOK` (decisão do Luis em 21/11/2026): só o pedido de comentário de UMA palavra, sem "segue"/"se inscreve":
  Parte 1 "Comenta QUERO pra parte dois." ; Parte 2 uma pergunta de 1 toque + "Comenta sim ou não." (ex.: "Você abriria a
  porta? Comenta sim ou não."). `CTA_CARD = cta_card`; `CTA_TEXTO` = "COMENTA QUERO" (Parte 1) ou "SIM OU NÃO?" (Parte 2);
  `ARROBA = ''` (o cartão não mostra o @). O `video_tiktok.mp4` (com esse cartão curto) vai para as 3 redes.
- PRIMEIRO QUADRO = CAPA NO FEED (21/11/2026): a cena 0 abre JÁ no quadro 0 com `put_close` do narrador reagindo
  (expr 'choque', 'medo' ou 'preocupado'), o carimbo 'PARTE 1'/'PARTE 2' e o gancho da história em até 2 linhas GRANDE em cima
  (sem cobrir os olhos). Nada de fade-in ou tela vazia. Esse quadro vira a `capa.jpg` (`motor.py quadro $P 0 3`).
- Voz: `VOZ = 'pt-BR-AntonioNeural'; RATE = '+4%'; PITCH = '-6Hz'` (mais grave e calma). `MUSICA = False`.

## Visual (sombrio.py)
- Personagens: `put_menino(c, x, pés, altura, f, walk=0|1, flip, expr, look, pele, cabelo, penteado, roupa, calca, oculos,
  barba, velho)`; expr: neutro, preocupado, choque, sorriso; penteado: curto, coque, longo, careca. O narrador ("eu") é
  sempre o mesmo personagem dentro de uma história (mesmas cores nas 2 partes). Outros personagens no mesmo traço (olhos
  enormes com olheiras). Bichos/objetos novos com a Pen, contorno escuro, cores lisas.
- Andar com o cenário passando: `rua(f, scroll=f * 9, luz=..., neb=...)` + `put_menino(..., walk=1)`. Cenários prontos:
  `rua` (rua com casas e postes), `put_torre` (torre de relógio), e todos os `CEN('nome')` do kit (quarto, sala, cozinha,
  escola, praia, floresta, espaco...). Desenhe com a Pen o lugar que a história pedir (metrô, ginásio, farol, prédio).
- CORES CONFORME O CONTEXTO (pedido do Luis): nada de deixar tudo cinza. Escolha a luz de cada cena pelo lugar e pelo
  clima da frase: dia claro/escola/praia/casa -> `rua(luz='dia', neb=0)` e luz `'vivo'`; fim de tarde/lembrança ->
  `luz='tarde'` e `'tarde'`; neblina/estranheza -> `luz='neblina'` e `'sombrio'`; noite -> `luz='noite'` e `'sombrio_noite'`;
  neve/hospital/madrugada fria -> `'frio'`. Uma história pode começar colorida e ir escurecendo conforme o mistério cresce.
- HUD (no `OVERLAY(im, si, lf)`, coordenadas da saída 1080x1920; converta para RGBA e termine com `grao(...)`):
  `stamp` (título de carimbo; big=True para "A REGRA"), `card(titulo, sub, x, y, s, alvo)` (cartão com linha até o
  objeto; use `to_out` do exemplo para achar o objeto na tela), `painel(rotulo, valor, ..., glitch)` (placar digital),
  `burst('?!')` (onomatopeia), `interrog` (pontos de interrogação). 1 a 2 elementos de HUD por frase, nunca cobrindo rosto
  nem a legenda (y≈1505), nunca um sobre o outro.
- Na 1ª cena: carimbo `stamp(im, 'PARTE 1', ...)` ou 'PARTE 2' por ~1,5 s, e o carimbo do lugar ("NA MINHA CIDADE").
- O VÍDEO SÓ ACABA (pedido do Luis em 20/11/2026): sem pedido de comentar/seguir/se inscrever dentro do vídeo; em todas as
  redes (inclusive TikTok) publique o `video_youtube.mp4`, que termina na última frase. O `video_tiktok.mp4` não é usado.
- Legenda: 1 palavra por vez (automática com `instala_legenda()`).
- CLOSE NO ROSTO (pedido do Luis em 20/11/2026, OBRIGATÓRIO): toda parte tem PELO MENOS 2 closes no rosto do narrador
  (ou de quem reage): um no momento de susto/descoberta e um na última cena (o gancho final). Use
  `c = put_close(c, f, expr=..., look=..., escurece=0..1, shake=0..1, suor=0|1, **CORES_DO_PERSONAGEM)` depois de desenhar
  a cena (ele borra o cenário e põe o rosto grande no centro) e câmera `(621, 1104, ~1.05-1.3, 0)`. expr do close: neutro,
  preocupado, choque, medo, sorriso, desconfiado. `look=0` = olhando pra câmera (bom no fim). Entre no close de repente na
  palavra forte (com kick) ou com zoom rápido; o HUD no close fica no alto (y≈230-300), nunca em cima do rosto.

# Formato DESENHO — Curiosidades da IA (desde 05/11/2026)

Desenho animado curto e narrado, feito 100% em código: personagens "feijão" com contorno ameixa
(#241726), sombra em 2 tons, bichos de lado com olho grande, câmera que se mexe sem parar,
legenda grande palavra por palavra, música e efeitos BAIXOS (a voz manda). Voz: pt-BR-AntonioNeural +15%.
Exemplos completos: `exemplos/galo/historia.py` (Curiosidades da IA, voz Antonio) e
`exemplos/cafe_curiosidade/historia.py` (Um Café com o Mundo, notícia de curiosidade, voz Francisca,
etiqueta SELO no topo). Na historia.py dá para trocar `VOZ`, `RATE`, `ARROBA`, `SELO` e `SELO_CORES`.

## Passo a passo de um post

```bash
P=curiosidades/AAAA-MM-DD-HHh          # pasta do post
mkdir -p $P && cp curiosidades/desenho/exemplos/galo/historia.py $P/   # ponto de partida
# edite $P/historia.py: LINES, CAPTXT, FALA_TIKTOK, CTA_TEXTO, cenas, SFX, CHECK
python3 curiosidades/desenho/motor.py narrar $P     # voz + tempo de cada palavra (falas.json)
python3 curiosidades/desenho/motor.py stills $P     # $P/conferir_cenas.jpg  -> ABRA e confira
python3 curiosidades/desenho/motor.py quadro $P <cena> <quadro>   # 1 quadro grande em $P/quadro.jpg
python3 curiosidades/desenho/motor.py render $P     # ~1 min a cada 5 s de vídeo (2 núcleos)
python3 curiosidades/desenho/motor.py final $P      # video_tiktok.mp4, video_youtube.mp4, conferir_video.jpg
```
Se a voz der erro de certificado, rode com `SSL_CERT_FILE=~/.ccr/ca-bundle.crt` (se existir).
Depois de `narrar`, só rode de novo se mudar o texto das LINES (o tempo das cenas vem da voz).

## Roteiro (LINES = 1 frase por cena, 5 a 8 cenas, 25 a 45 s)
1. **Gancho**: afirmação absurda/surpreendente, sem introdução ("O galo não canta por causa do sol.").
2. **Cenário** com um detalhe concreto (lugar, ano, número).
3. **2 a 4 batidas que escalam** (alguém duvida, exagero engraçado, número impressionante).
4. **Virada** "Você vê, ..." / "Mas..." revelando o mecanismo com comparação do dia a dia.
5. **Fim irônico curto** — as últimas palavras são a piada ("quem acorda o galo... é o próprio galo.").
Português falado, frases curtas, números por extenso nas LINES (na CAPTXT pode usar algarismos:
"100 decibéis"). Nunca descreva o que está na tela. Todo fato conferido em fonte confiável.
`FALA_TIKTOK` = pedido de comentário de 1 toque + "segue pra mais curiosidades!" (só no TikTok);
`CTA_TEXTO` = a resposta de 1 toque em letras grandes ("SIM OU NÃO?"). O YouTube termina na virada (loop).

## SEM MÚSICA DE FUNDO (OBRIGATÓRIO no Curiosidades da IA, decisão do Luis em 15/11/2026)
Todo historia.py do Curiosidades da IA tem `MUSICA = False`: o vídeo fica só com a voz e os efeitos/sons ambientes do `SFX`
(whoosh, thunk, ting, patter, splash...). Capriche nos sons ambientes (passos, vento, cidade, relógio) já que não há música.

## Personagem fixo: PROFESSOR BIGODE (OBRIGATÓRIO, decisão do Luis em 14/11/2026)
Vale para a página CURIOSIDADES DA IA (posts em curiosidades/); NÃO vale para o Anima Futebol (futebol/) nem para o Um Café com o Mundo.
Todo post do Curiosidades da IA tem o Professor Bigode (professor.py): senhor careca com tufos brancos, bigodão branco de guidão,
gravata-borboleta vermelha, camisa branca e colete marrom. Ele é o apresentador/narrador da página.
`put_prof(c, x, pés, altura, f, seed=1, flip=False, expr=..., arms=..., look=...)`
expr: neutral, grin, shock, smug, pained, stern, proud, nervous; arms: hang, point, up, wave, chin, shrug.
- Aparece SEMPRE na 1ª cena (o gancho: apresenta, aponta, se espanta) e na última cena (reage ao fim irônico).
- Nas outras cenas, entra sempre que precisar de "uma pessoa" sem papel específico (quem testa, quem explica, quem se
  surpreende) e pode visitar qualquer cenário (cozinha, espaço, Roma antiga, dentro do corpo...). Bichos, objetos e
  personagens com papel próprio (astronauta, cientista da pesquisa, soldado, bispo...) continuam sendo desenhados à parte.
- Nunca mude o visual dele (cores, bigode, gravata). Ele nunca fala com voz própria: a narração continua a mesma.
- Rosto dele acima da legenda (y≈1600 da saída), como qualquer personagem.

## Cenas (`SCENES`): cada uma é `def sN(f): ... return canvas, (cx, cy, zoom, roll), luz`
- `f` = quadro local da cena (30 fps). Palco 1242x2208; saída 1080x1920. zoom 1 = palco todo.
- **Sincronia**: `wt(N, 'palavra')` = quadro em que a voz fala a palavra (sem acento tanto faz).
  Faça cada ação cair 0-3 quadros ANTES da palavra (`back(ramp(f, k-3, k+6))` para pular na tela).
- **Luz**: 'day' história normal; 'golden' tempo passando/decadência; 'dusk' explicação ou fim.
  Fundos: `CEN('nome', luz)` (ver abaixo); `BG('day'|'golden'|'dusk')` é o PASTO e `BG('lab')` o laboratório.

## Cenário = o lugar da história (OBRIGATÓRIO, decisão do Luis em 06/11/2026)
Cada cena acontece no lugar de que a frase fala. O pasto (`BG('day')`/`CEN('pasto')`) só serve para histórias
de campo, fazenda ou bichos do campo; nunca use o pasto como fundo "neutro".
`CEN(nome, luz)` (cenarios.py, 1242x2208, chão em y≈1500-1650; luz muda céu/janela):
quarto, sala, cozinha, banheiro, escola, escritorio, fabrica, museu, lab (interiores);
cidade, praia, fundo_mar, floresta, deserto, neve, montanha, antiga (Roma/Grécia), pasto (exteriores);
espaco, estacao (estação espacial), corpo (dentro do corpo), mapa (mar com continente).
Ex.: comida/cozinhar -> cozinha; dormir/acordar -> quarto; tecnologia/computador -> escritorio ou quarto;
oceano/peixe -> fundo_mar ou praia; país/lugar -> mapa + o tipo de paisagem do lugar; história antiga -> antiga.
Se nenhum servir, desenhe o cenário certo no historia.py com a Pen (como `estrada_bg` em 2026-11-06-20h).
Antes de montar as cenas, escreva para você mesmo o cenário de cada cena.
- **Câmera**: nunca parada — puxe para trás no gancho, desça de grua até o detalhe, aproxime na virada,
  `kick(f, f0)` em impactos, roll 2-4° no drama. Corte seco só quando muda lugar/tempo.
- **Legenda** fica em y≈1600 da saída: rostos e a ação principal ACIMA disso.
- **Nada parado por mais de 4 quadros** (piscar, respirar, zoom lento). Os personagens já respiram e piscam.

## Personagens e objetos prontos (kit.py / personagens.py / art.py)
- `put_prof(...)` — PROFESSOR BIGODE, personagem fixo de todos os posts (veja acima)
- `put_roo(c, x, pés, altura, flip, crow=0..1, sleep=0..1, expr, look, chief, ear)` — galo
- `put_emu(c, x, pés, altura, flip, run, phase, peck, expr, look, helmet)` — emu / ave pernalta
- `put_sci(c, x, pés, altura, f, seed, expr, arms, skin, hair, bun, glasses)` — cientista de jaleco
- `put_soldier(c, x, pés, altura, f, seed, expr, arms, mous, skin, sweat, walk)` — pessoa de capacete
- expressões: neutral, stern, grin, proud, shock, pained, smug, nervous; bichos: calm, side, smug, shock, sleep
- braços: hang, clip, ears, cheek, point, up, salute, thumb, shrug
- objetos/efeitos: `clock_img`, `P.truck`, `thought(...)`, `sun_icon`, `rings` (ondas de som), `zzz`,
  `txt('TEXTO!', tamanho, rot)` (palavra de efeito; sem emoji), `put_dust` (poeira ao surgir), `P.lamp_glow`.

### Bicho ou pessoa NOVA (quase todo tema precisa)
Escreva a função no próprio historia.py com a `Pen` (veja `rooster` em personagens.py e `emu` em art.py):
- bicho de lado: desenho 600x800, pés em y≈780, olhando para a direita; pessoa: 600x1000, pés em y≈975.
- `p.shape(pontos, cor, cor_escura, contorno, sombra)` = forma cheia com sombra e contorno;
  `p.line`, `p.stroke`, `p.dot`, `p.poly`, `p.arc`; `ell_pts(cx, cy, rx, ry)` dá os pontos de uma elipse.
- olho grande branco com pupila que olha (`look`) e pálpebra (`side`/`smug`); boca/bico que abre.
- desenhe com `put_sprite(c, 'nome_da_funcao', x, pés, altura, largura/altura, flip, {'param': passos}, **kw)`.
- teste antes: `python3 -c "import sys; sys.path.insert(0,'curiosidades/desenho'); ..."` salvando um PNG e abrindo com Read.

## Regras
- História, personagens e piadas originais; nunca copiar vídeo de outro criador.
- Nada de pessoas reais com nome, logotipos, mascotes de marca ou personagens conhecidos.
- Sem violência gráfica (no máximo susto/poeira); temas leves e verificáveis.
- `SFX(s)`: efeitos nas palavras (`s.W(cena,'palavra')`): whoosh, thunk, ting, patter, engine, trill, splash.
  Whoosh em cada corte e o sting na virada (`TWIST`) já são automáticos.

## Conferência (obrigatória — o post sai sem revisão)
1. `stills` → abra `conferir_cenas.jpg`: cabeça/chapéu cortado, personagem escondido, câmera dentro de
   objeto, legenda cobrindo rosto, quadro vazio, texto espelhado, ação fora do quadro na palavra certa.
2. `final` imprime "ok (sem quadro parado ou preto)" para os 2 vídeos; abra `conferir_video.jpg`.

## Futebol: VISUAL NOVO (anima.futebol, aprovado pelo Luis em 14/11/2026)
Os posts de futebol usam `futebol2.py` por cima de `futebol.py` (`from futebol import *; from futebol2 import *`).
Exemplo completo: `exemplos/futebol2/historia.py` (copie e reescreva). Resumo:
- Fundo `estadio2('dusk'|'day'|'golden')` (não use mais `estadio`); jogadores `put_atleta(...)` (não use mais `put_jog`),
  com `run=fase` para correr, `kick=pulse(...)` para chutar, `hs` (cabelo), `num_` (número), `skin` 0-5.
- Gol: `put_gol2(c, x, estufa=...)` + `put_goleiro`; bola com `raio_bola` e rastro (`bola_voo` do exemplo); `gol_txt` (estrela + GOL!).
- Ênfase no assunto: `foco(...)` no jogador citado; `OVERLAY(im, si, lf)` com `placar_tv` (muda a cada gol) e
  `destaque(...)` (manchete do assunto em cada cena; nos lances de gol entra DEPOIS do gol para não cobrir a bola).
- `linhas_vel` sempre ANTES de desenhar o jogador; `confete` nas comemorações.
