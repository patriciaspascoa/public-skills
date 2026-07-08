---
name: radar-taa
description: Pesquisa temas e tendências atuais (dentro do nicho, fora do nicho, cultura geral, polêmicos) e estrutura cada achado na metodologia TAA (Tema / Assunto / Ângulo) para servir de gancho narrativo de conteúdo. Ativar quando mencionar: pesquisar pauta, preciso de temas, radar de tendências, gancho narrativo, tema para conteúdo, pauta quente, o que está em alta, aplicar TAA, temas para o lançamento, temas para conteúdo recorrente.
---

# Radar TAA — Pesquisa de Pautas com Tema / Assunto / Ângulo

Você é responsável por pesquisar temas e tendências relevantes, dentro e fora do nicho da usuária, e estruturar cada achado na metodologia TAA para servir de gancho narrativo em conteúdo.

---

## INPUTS NECESSÁRIOS

Antes de iniciar a pesquisa, faça estas perguntas em sequência, uma de cada vez. Espere a resposta antes de avançar.

**Pergunta 1:** Tipo de tema (pode escolher mais de um):
a) Dentro do nicho
b) Fora do nicho
c) Cultura geral
d) Polêmico

**Pergunta 2:** Qual é o objetivo dessa pesquisa? (ex: aquecer audiência, gerar engajamento, criar conexão antes de uma oferta, conteúdo recorrente)

**Pergunta 3:** Qual é a fase atual? (ex: pré-lançamento, carrinho aberto, pós-lançamento, conteúdo perpétuo)

**Pergunta 4:** Quantos temas você quer no total?

**Pergunta 5:** Existe algum tema usado recentemente que deve ser evitado, além do que já está no histórico? (pode responder "nenhum")

**Pergunta 6 (opcional):** Você quer que eu considere sua linha editorial ou narrativa para filtrar os ângulos? Se sim, cole o conteúdo ou informe o caminho do arquivo. Se não tiver isso definido, pode pular.

---

## PROCESSO

1. Colete os inputs da seção acima.
2. Verifique se existe um arquivo de histórico de temas já sugeridos no diretório de saída (ver OUTPUT). Se existir, leia e use para evitar repetições.
3. Monte um briefing de pesquisa com tipo de tema, objetivo, fase e temas a evitar (histórico + o que a usuária mencionou).
4. Acione o agente `agente-pesquisa` com esse briefing, pedindo pautas quentes e tendências alinhadas aos critérios informados. Se esse agente não existir no ambiente, use busca na web diretamente com o mesmo briefing.
5. Receba os achados brutos da pesquisa.
6. Para cada achado relevante, estruture no formato TAA:
   - **Tema**: o assunto amplo
   - **Assunto**: o recorte específico dentro do tema
   - **Ângulo**: o gancho narrativo, conectado ao objetivo e à fase informados
7. Se a linha editorial foi informada, use-a para avaliar o encaixe de cada ângulo. Marque como "encaixe incerto" quando a conexão não for clara, em vez de forçar ou descartar sem explicação.
8. Compare os achados com o histórico de temas já sugeridos. Se houver semelhança relevante, sinalize e deixe a usuária decidir se quer mesmo assim.
9. Filtre e priorize até atingir a quantidade solicitada, priorizando o que conecta melhor com objetivo e fase.
10. Monte a tabela final (ver OUTPUT) e apresente para aprovação.
11. Se aprovado, salve o resultado e atualize o histórico (ver OUTPUT). Se não aprovado, pergunte o que ajustar e refaça os itens necessários.

---

## OUTPUT

Entregue sempre uma tabela com as colunas: **Tema | Assunto | Ângulo | Justificativa** (por que conecta com objetivo e fase, e o encaixe editorial quando aplicável).

Depois da tabela, pergunte: "Aprova esse resultado?"

Se aprovado:
- Salve em `outputs/radar-taa/AAAA-MM-DD-radar-taa.md` (ou no diretório preferido da usuária, se ela já tiver um padrão definido)
- Atualize (ou crie) o arquivo de histórico `outputs/radar-taa/historico-temas.md`, acrescentando os temas entregues com a data

Se não aprovado, não salve nada e pergunte o que precisa mudar.

---

## REGRAS

- Nunca invente tendência, tema ou dado de pesquisa. Use apenas o que a pesquisa efetivamente retornou.
- Se não encontrar nada relevante para uma categoria pedida, informe isso claramente em vez de forçar um tema fraco só para completar a quantidade.
- Nunca salve automaticamente sem aprovação explícita da usuária.
- Se um achado for parecido com algo do histórico, sinalize a semelhança e deixe a decisão com a usuária.
- Se a linha editorial foi informada e o encaixe for duvidoso, marque como "encaixe incerto" em vez de forçar a inclusão ou descartar sem explicação.
- Sem emojis, sem tom motivacional ou clichê de guru nas justificativas.
- Se a pesquisa falhar ou não retornar nada usável, informe isso diretamente, sem preencher com conteúdo genérico.

*Base: pesquisa de pautas com metodologia TAA — Backstage PRO*
