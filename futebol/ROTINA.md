# ROTINA do Anima Futebol (versão 20/11/2026 — mudanças pedidas pelo Luis)

Página "Anima Futebol": @anima.futebol no Instagram e no TikTok, canal "Anima Futebol" no YouTube. Tudo em português do Brasil.
Publicação AUTOMÁTICA pelo Metricool (brandId/blogId "7958170", timezone "America/Sao_Paulo", autoPublish true), sem aprovação
manual. Como sai sem revisão, a checagem dos fatos e do vídeo é responsabilidade de quem roda: **na dúvida sobre um fato, não use**.

Há dois modos:
- **PLANEJAR** (tarefa diária ~17:41): monta a agenda do DIA SEGUINTE e cria as tarefas de cada post.
- **POST** (tarefas de uma vez só, criadas pelo planejador): faz o desenho e agenda 1 post.

---------------------------------------------------------------------------------------------------
## Regras gerais (valem nos dois modos)

### Quantidade e horários (decisão do Luis em 20/11/2026)
- **Instagram (Reel) e YouTube (Short): até 4 posts por dia**, em horários FLEXÍVEIS que seguem os jogos:
  - **PÓS-JOGO**: o post sai logo que o jogo grande TERMINA (alvo: até ~30 min depois do apito final).
  - **PRÉVIA / RAIO-X**: análise do jogo principal do dia, 2 a 5 h antes do início.
  - **NOTÍCIA**: só quando o dia não tem jogo grande suficiente; use os horários 07h, 12h, 19h ou 21h.
  - De manhã (~07h-09h) pode sair o resultado de jogo que acabou tarde na noite anterior (se ainda não saiu) ou a prévia do dia.
  - Pelo menos 1h30 entre dois posts; nada entre 00h30 e 06h30 (jogo que acaba depois de 00h vira post das 07h).
- **TikTok: só 2 vídeos por dia, e só do JOGO PRINCIPAL do dia** (normalmente a prévia/raio-x e o pós-jogo dele).
  Os outros posts saem só no Instagram e no YouTube. Em dia sem jogo grande, os 2 TikToks vão para os 2 assuntos mais fortes.

### Pauta (regras do Luis, 08/11/2026)
- Foco: FUTEBOL BRASILEIRO (Brasileirão, Copa do Brasil, Seleção, clubes brasileiros, transferências de/para o Brasil) e
  LIBERTADORES (também Sul-Americana com time brasileiro). Sem nada forte do Brasil: futebol europeu, de preferência com brasileiro.
- MESSI ou CRISTIANO RONALDO: só com grande notícia (recorde, gol histórico, título, aposentadoria, transferência, polêmica grande).
- Sempre o que está MAIS EM ALTA (jogo grande que acabou, decisão, classificação, eliminação, contratação bombástica, recorde).
- Jogo principal do dia = o que mais gente está acompanhando: decisão de título, final, clássico, jogo de Flamengo/Corinthians/
  Palmeiras/São Paulo/Vasco/Grêmio/Inter/Atlético-MG/Cruzeiro com algo em jogo, Seleção, mata-mata de Libertadores/Copa do Brasil.
- NUNCA repita postagem: um assunto só volta com FATO NOVO (resultado, decisão, número novo), e o vídeo destaca o fato novo.
- Nada de apostas, palpites de bet, odds ou casas de apostas. Tom neutro entre torcidas, sem ofensa. Brigas/violência/tragédias:
  tom sério, sem humor e sem mostrar violência.

### SÉRIES que geram retorno (decisão do Luis em 20/11/2026)
Todo post entra numa série fixa, com número de episódio, para quem segue voltar. Registro em `futebol/series.txt`
(`série | último episódio | data | assunto`). Use o próximo número e atualize a linha ao publicar.
- **CONTA DO TÍTULO** — a briga pelo título do Brasileirão (quem precisa de quê, a conta após cada rodada). Quando o título for
  decidido, o episódio final é o do campeão e a série passa a ser **CONTA DA VAGA** (Libertadores/G-?), se fizer sentido.
- **QUEM CAI?** — a briga contra o rebaixamento (Z4, conta de cada time, confrontos diretos).
- **RAIO-X** — prévia/análise do jogo principal do dia (o que está em jogo, desfalques, como cada time joga, na prancheta).
- **FIM DE JOGO** — pós-jogo de jogo grande que não é título nem rebaixamento (final, mata-mata, clássico, Seleção, Europa).
- **BASTIDORES** — notícias fora de campo (técnico, contratação, polêmica de arbitragem, declaração).
No vídeo: a 1ª cena mostra a marca da série grande (ex.: `QUEM CAI? · EP. 4`) por ~1,5 s; o SELO do topo continua
'<COMPETIÇÃO>  ·  <FASE/RODADA>'. Nos títulos/legendas: veja "Legendas".

---------------------------------------------------------------------------------------------------
## MODO PLANEJAR (tarefa diária)

1. Data de amanhã em America/Sao_Paulo (D). Repositório (veja "Repositório" abaixo). Leia `futebol/temas.txt`, `futebol/series.txt`
   e as agendas recentes em `futebol/agenda/`.
2. Pesquise (WebSearch/WebFetch, 2 fontes) os JOGOS de D com horário de Brasília: Brasileirão, Copa do Brasil, Série B/playoffs,
   Libertadores, Sul-Americana, Seleção, e os grandes da Europa com brasileiro. Escolha o **JOGO PRINCIPAL** e até 2 outros jogos grandes.
3. Monte até 4 slots para D (regras em "Quantidade e horários"). Para cada slot defina:
   - `post` = horário do post; `inicio` = quando a tarefa POST deve começar:
     - PRÉVIA/NOTÍCIA: inicio = post - 50 min.
     - PÓS-JOGO de pontos corridos: inicio = início do jogo + 1h50 (o post sai ~25-35 min depois).
     - PÓS-JOGO de mata-mata que pode ter prorrogação/pênaltis: inicio = início + 1h55 (se o jogo não tiver acabado, a tarefa espera).
   - tipo (PREVIA, POS-JOGO, NOTICIA), série, jogo/assunto, `tiktok: sim/não` (só 2 no dia, do jogo principal).
4. Escreva `futebol/agenda/D.txt` (uma linha por slot: `inicio | post | tipo | série | jogo ou assunto | tiktok sim/não`),
   commit "futebol: agenda D" e push (fetch+rebase+push até 3 vezes).
5. Para CADA slot, crie uma tarefa de uma vez só com `create_trigger` (ferramenta do servidor Claude Code Remote; carregue com
   ToolSearch "create_trigger"): name "anima.futebol POST D <post> <tipo>", `run_once_at` = "<D>T<inicio>:00[America/Sao_Paulo]",
   initiation "human_schedule", notifications {"push": true}, prompt =
   "Anima Futebol — MODO POST. Dados do slot: data <D>; post <HH:MM>; tipo <tipo>; série <série>; assunto <jogo/assunto>; tiktok <sim/não>.
   Clone o repositório umcafecommundo-ctrl/imagens (git clone --depth 1 https://github.com/umcafecommundo-ctrl/imagens /home/claude/imagens;
   se a ferramenta add_repo existir, chame antes com owner umcafecommundo-ctrl, repo imagens, access push), leia INTEIRO futebol/ROTINA.md
   e siga o MODO POST com estes dados. Publicação automática pelo Metricool (blogId 7958170) pedida pelo Luis."
   Confira na resposta que cada tarefa foi criada com o horário certo. Não crie tarefa repetida: liste antes com `list_triggers`
   (as de nome "anima.futebol POST D ..." que já existirem ficam).
6. Se não conseguir criar as tarefas, avise o Luis com PushNotification (o que falhou e a agenda de D).
7. Termine com 1 linha por slot (horário do post, tipo, série, assunto, TikTok sim/não).

---------------------------------------------------------------------------------------------------
## MODO POST (1 post)

### 1. Horário e duplicidade
Pegue data/hora em America/Sao_Paulo. Chame getScheduledPosts do Metricool (brandId "7958170", timezone "America/Sao_Paulo", hoje):
se já existe post desse slot numa rede, não duplique. Se o tipo é PÓS-JOGO e o jogo ainda não terminou (confira placar ao vivo em
2 fontes), espere com `sleep 300` e confira de novo (até 45 min); se ainda não acabou, faça a notícia mais forte do momento e avise.

### 2. Repositório e voz
Veja "Repositório" abaixo. `pip install --break-system-packages edge-tts pillow numpy`. Leia INTEIRO `curiosidades/desenho/LEIA.md`,
`curiosidades/desenho/futebol.py`, `curiosidades/desenho/futebol2.py`, `curiosidades/desenho/futebol3.py` (cenários novos) e o
post de exemplo `futebol/2026-11-20-07h/historia.py` (ponto de partida).

### 3. Pesquisa e checagem de fatos (OBRIGATÓRIA — pedido do Luis em 20/11/2026)
a) Leia `futebol/temas.txt` e liste para você os assuntos dos últimos 7 dias; leia `futebol/series.txt`.
b) Pesquise o assunto do slot (ge.globo, UOL Esporte, ESPN, Lance!, CNN Esporte, Gazeta Esportiva, Agência Brasil, sites oficiais;
   Europa: BBC Sport, ESPN, AS, Marca, A Bola, Record). ~10-15 min.
c) Escreva `$P/fatos.txt`: UMA LINHA POR FATO que vai entrar no vídeo ou nas legendas, com as 2 fontes que confirmam.
   Fato sem 2 fontes que batem: arredonde ("no fim do primeiro tempo") ou tire.
d) **Palavras de lance só se a fonte disser exatamente isso**: virada/virou (só se o time esteve PERDENDO e terminou ganhando),
   empatou, descontou (só quem estava perdendo por 2+), de cabeça, de pênalti, de falta, contra, nos acréscimos, expulso, VAR.
   "Abriu o placar" ≠ "virou". Confira quem marcou para qual time.
e) RESERVA: fetch+rebase, releia `futebol/temas.txt` (outro post pode ter reservado o mesmo assunto; se sim, troque), acrescente
   "AAAA-MM-DD | HHhMM | COMPETIÇÃO | [SÉRIE EP. N] tema com palavras-chave (reservado) | fato novo, ou -", commit
   ("futebol: reserva <HHhMM>") e push na hora (até 3 tentativas).

### 4. Desenho (identidade visual + mudanças de 20/11/2026)
Pasta `P=futebol/<AAAA-MM-DD>-<HHhMM>` (ex.: futebol/2026-11-21-18h50). Copie `futebol/2026-11-20-07h/historia.py` e REESCREVA tudo
(`from kit import *; import kit; from futebol import *; from futebol2 import *; from futebol3 import *`). Fontes no comentário do topo.

**Identidade visual (obrigatória, não muda):**
- Desenho animado narrado 100% em código; NUNCA escudos, logos de clubes/ligas/patrocinadores, taças reais nem rosto de jogador real.
  Times por PLAQUINHAS com o nome nas cores do clube (put_placa) e jogadores genéricos com camisa nas cores (put_atleta; cores em
  TIMES de futebol.py — se faltar um time, acrescente só as cores). Jogador citado = boneco genérico + placa do nome.
- Gol LONGE, atrás dos jogadores (put_gol2 + put_goleiro; mire a bola em (gx + 90, gy)); bola proporcional (r = raio_bola(altura);
  diminui até raio_bola(300) indo para o gol). Quem chuta fica na frente (pés y≈1950-2030, altura ~820-880).
- CARTÃO FINAL pronto (CTA_CARD de futebol.py, pergunta CTA_TEXTO + "SIGA PARA MAIS"); ARROBA = ''. Não reescreva nem desative.
- SEM MÚSICA (MUSICA = False) e com som de estádio (veja item 6). Voz pt-BR-AntonioNeural; SELO = '<COMPETIÇÃO>  ·  <FASE/RODADA>'; SELO_CORES = ((22, 92, 52), (255, 255, 255)).

**1) VÍDEO CURTO: história de 20 a 30 s** (o motor imprime a duração em `narrar`; passou de 30 s, corte frases e narre de novo).
   LINES = 4 a 6 frases, 1 por cena, cada frase com NO MÁXIMO ~14 palavras. Números por extenso nas LINES, algarismos na CAPTXT.
   Estrutura: PERGUNTA POLÊMICA -> o fato principal -> 1 ou 2 detalhes que escalam -> o que muda / a conta -> fim curto.

**3) PERGUNTA POLÊMICA NO COMEÇO**: a 1ª frase é a pergunta que divide a torcida e que o vídeo responde
   (ex.: "O Inter vai cair? Olha a conta.", "Foi pênalti no Gabigol?", "O Flamengo já pode comemorar?"). Na 1ª cena ela aparece
   GRANDE na tela junto com a marca da série. CTA_TEXTO e FALA_TIKTOK repetem a mesma pergunta no fim
   (FALA_TIKTOK = "<pergunta de 1 toque>? Comenta aqui, e segue o Anima Futebol pra mais!"; CTA_TEXTO até ~14 letras).

**4) MENOS TEXTO NA TELA, TUDO MAIOR**:
   - Em cada momento, além do SELO e da legenda, no MÁXIMO 1 elemento de texto (um número, OU uma placa, OU a manchete).
     Quando entra o próximo, o anterior sai (desenhe só enquanto `f < próximo - 2`).
   - Tamanhos mínimos: put_placa >= 64; num/txt >= 110 (textos longos 90-100, sem cortar nas laterais); tabela no máximo 3 linhas.
   - `destaque(...)` (manchete do OVERLAY) no máximo em 2 cenas e nunca junto de um num(...) na mesma hora.
   - Textos em y >= 680 do palco (acima disso o SELO cobre); rostos e ação acima da legenda (y≈1600 da saída).

**5) CENÁRIO VARIADO**: no máximo 2 cenas no mesmo cenário; use pelo menos 3 cenários diferentes por vídeo, conforme a frase:
   - lance/gol: `estadio2('dusk'|'day'|'golden')` + gol, bola e atleta;
   - placar, conta, tabela: `telao()` + `telao_txt(...)` ou `conta_bg()` + `numero_gigante(...)`;
   - esquema, desfalques, como o time joga, lance explicado: `prancheta()` + `pino(...)` + `seta(...)`;
   - técnico, declaração, demissão, contratação: `coletiva(cores)` + atleta + `mesa_coletiva(c)`;
   - clima do elenco, tristeza/alegria pós-jogo, pressão: `vestiario(cores, faixa)`;
   - datas: `calendario(dia, mes)`; títulos/finais: `trofeu()`. Câmera sempre em movimento.

**6) VOZ E RITMO**: RATE '+15%'; frases curtas; ponha o número no FIM da frase depois de vírgula ou "...", para dar uma pausa antes
   dele ("E o placar final... dois a um."). Um som de impacto (`s.thunk`) em CADA número, gol e virada de cena, e `s.ting` na resposta
   da pergunta. Corte seco entre cenas (o whoosh é automático).

**SEM MÚSICA DE FUNDO, SOM DE ESTÁDIO (pedido do Luis em 20/11/2026)**: todo historia.py tem `MUSICA = False`. O clima vem dos
   sons ambientes do motor, chamados em `SFX(s)`:
   - `s.torcida(quadro_ini, quadro_fim)` — murmúrio de torcida de fundo (fica bem abaixo da voz; nível em `AMBIENTE_NIVEL`, padrão .11).
     Use em TODAS as cenas de estádio/telão (ex.: `s.torcida(0, s.cut(3))`); nas cenas de prancheta, coletiva, vestiário e estúdio,
     deixe sem torcida (o contraste ajuda) ou só uma torcida bem baixa (g=.4) vinda "de longe".
   - gol: `s.chute(s.W(cena, 'palavra') - 3)` no chute, `s.rede(...)` quando a bola entra e `s.rugido(...)` logo depois (a torcida explode);
   - `s.apito(quadro)` no início do lance/jogo e `s.apito(quadro, longo=True)` no fim do jogo/resultado;
   - continue com `s.thunk` nos números e `s.ting` na resposta da pergunta. Nada de música, nem trecho de música real.
   Exemplo de SFX completo: `futebol/2026-11-20-07h/historia.py` (versão com som de estádio).

Depois: `python3 curiosidades/desenho/motor.py narrar $P` (erro de certificado: `SSL_CERT_FILE=~/.ccr/ca-bundle.crt` antes do
comando; NoAudioReceived: espere 5 s e tente até 3 vezes) -> confira a duração (20-30 s) -> `motor.py stills $P` e abra
`$P/conferir_cenas.jpg` com Read. Corrija: mais de 1 texto de efeito ao mesmo tempo, texto pequeno/cortado/sobreposto, placa ou
jogador fora do quadro, gol grande ou jogador "voando" na frente da trave, bola fora de proporção, legenda cobrindo rosto, cena vazia,
cenário repetido em mais de 2 cenas, erro de português (até 4 rodadas; `motor.py quadro $P <cena> <quadro>` para 1 quadro grande).
`motor.py render $P` (timeout 600000 ms) e `motor.py final $P`: os dois vídeos "ok (sem quadro parado ou preto)"; abra
`$P/conferir_video.jpg`. video_tiktok.mp4 vai para Instagram e TikTok; video_youtube.mp4 para o YouTube.

**7) CONFERÊNCIA FINAL DE FATOS** (antes de publicar): releia LINES, CAPTXT, os textos que aparecem na tela (placas, num, telão,
destaque) e as 3 legendas, frase por frase, contra `$P/fatos.txt`. Qualquer palavra de lance, placar, minuto, autor de gol,
posição ou pontos que não esteja lá = erro: corrija (e renderize de novo se estiver no vídeo).

### 5. Publicar arquivos
fetch + rebase; em `futebol/temas.txt` troque "(reservado)" da sua linha por "(desenho)"; atualize `futebol/series.txt`.
`git add futebol curiosidades/desenho/futebol.py` (sem voz/, scenes/, __pycache__); commit (user.name "umcafecommundo",
user.email "umcafecommundo@users.noreply.github.com"); fetch + rebase + `git push origin HEAD:main` (até 3 vezes).
Links fixos: `https://raw.githubusercontent.com/umcafecommundo-ctrl/imagens/<git rev-parse HEAD>/<P>/video_tiktok.mp4` e
`.../video_youtube.mp4` (confira 200 com `curl -s -o /dev/null -w "%{http_code}"`). Push falhou: espelho
`https://cdn.jsdelivr.net/gh/umcafecommundo-ctrl/imagens@main/...`; último recurso: SendUserFile (proactive) + SendUserMessage +
PushNotification.

### 6. Legendas (com a série)
- Instagram: 1ª linha = a pergunta polêmica com palavras que as pessoas pesquisam + ⚽ e 1 emoji; linha em branco;
  "📺 <SÉRIE> · Ep. <N>"; 2 a 3 linhas curtas com emoji (resultado/detalhe/o que muda); linha em branco; a pergunta de 1 toque +
  "Comenta 👇"; linha em branco; "Segue @anima.futebol pra não perder o próximo episódio ⚽"; linha em branco; 4 a 5 hashtags sem
  acentos (#futebol + competição + times). Nunca #fyp #viral #bet.
- TikTok (só se o slot tem tiktok sim): tiktokData.title (até ~90 caracteres) = a pergunta + emoji; legenda: a pergunta; linha em
  branco; "<SÉRIE> · Ep. <N>" + 1 linha que aumenta a curiosidade + "Assiste até o fim 👀"; linha em branco; pergunta de 1 toque +
  "Comenta 👇"; linha em branco; "Segue @anima.futebol pra não perder o próximo episódio ⚽"; linha em branco; 4 a 5 hashtags.
- YouTube Short: youtubeData.title (até ~70 caracteres, máx. 100, sem "<" ou ">") = "<frase de busca> | <SÉRIE> Ep. <N> <emoji> #shorts";
  text = 1ª linha com a pergunta e palavras-chave; linha em branco; 1 a 2 frases do que o vídeo conta; linha em branco; pergunta +
  "Comenta 👇" e "Se inscreve pra acompanhar a série ⚽"; linha em branco; #shorts #futebol + 1 a 2 do tema (máx. 4 hashtags);
  youtubeData.tags = 5 a 8 palavras-chave com acentos (times, competição, a pergunta como as pessoas buscam).

### 7. Agendar (Metricool createScheduledPost)
Horário = o `post` do slot; se já passou ou faltam menos de 5 min, use 5 minutos a partir de agora (é o normal no PÓS-JOGO).
Todos com blogId "7958170", date "<AAAA-MM-DD>T<HH:MM>:00-03:00", publicationDate {"dateTime":"<AAAA-MM-DD>T<HH:MM>:00",
"timezone":"America/Sao_Paulo"} (mesmo horário), autoPublish true, draft false, descendants [], firstCommentText "",
hasNotReadNotes false, mediaAltText [], shortener false, smartLinkData {"ids":[]}:
a) Instagram: media [video_tiktok.mp4], providers [{"network":"instagram"}], instagramData {"type":"REEL","collaborators":[],
   "showReelOnFeed":true,"isAiGenerated":true}, videoCoverMilliseconds 1500, text = legenda do Instagram. Sem audioConfiguration.
b) TikTok — SÓ se o slot tem tiktok sim: media [video_tiktok.mp4], providers [{"network":"tiktok"}], tiktokData {"title":"<título>",
   "privacyOption":"PUBLIC_TO_EVERYONE","disableComment":false,"disableDuet":false,"disableStitch":false,
   "commercialContentThirdParty":false,"commercialContentOwnBrand":false,"autoAddMusic":false,"isAigc":true}, text = legenda do TikTok.
c) YouTube: media [video_youtube.mp4], providers [{"network":"youtube"}], text = descrição, youtubeData {"title":"...","type":"short",
   "privacy":"public","tags":[...],"category":"SPORTS","madeForKids":false,"isAiGeneratedContent":true}.
Confira em cada resposta que media voltou com 1 .mp4. No máximo 2 tentativas por rede; se uma falhar, mantenha as outras e avise
com PushNotification.

### 8. Falhas
Desenho travou ou não ficou bom em 2 tentativas, ou passou 25 min do horário: simplifique (menos cenas, reaproveite cenas de posts
anteriores) e avise com PushNotification. Voz não funcionou: PushNotification ("voz da Microsoft indisponível: confira se
speech.platform.bing.com segue nos domínios permitidos do Claude") e não publique sem voz.

### 9. Fim
1 linha: horário, redes agendadas, série/episódio, competição, tema e duração do vídeo.

---------------------------------------------------------------------------------------------------
## Repositório
Se a ferramenta add_repo existir (ToolSearch "add_repo"), chame com owner "umcafecommundo-ctrl", repo "imagens", access "push".
`git clone --depth 1 https://github.com/umcafecommundo-ctrl/imagens /home/claude/imagens` (se já existir:
`git -C /home/claude/imagens fetch origin main` e `git -C /home/claude/imagens checkout -B main origin/main`).
Teste: `git -C /home/claude/imagens push --dry-run origin HEAD:main`.
