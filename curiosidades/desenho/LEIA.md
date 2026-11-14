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
