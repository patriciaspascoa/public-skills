---
name: humanizer
description: >
  Elimina AI Slop de textos — padrões que entregam que o conteúdo foi gerado por IA.
  Detecta vícios de linguagem (travessões decorativos, vocabulário inflado, estruturas
  repetitivas) e reescreve para soar natural. Ideal para e-mails e redes sociais.
  Usa amostras de escrita da própria usuária quando fornecidas para preservar a voz.
  Ativar quando mencionar: humanizar texto, parece IA, tirar o AI slop, reescrever,
  esse texto parece ChatGPT, tornar mais natural, revisar tom.
tools:
  - Read
  - Write
---

# HUMANIZER — Eliminador de AI Slop

## MODO DE OPERAÇÃO

Se o prompt contiver `modo=auditor`, execute exclusivamente o seguinte e pare — não leia nem aplique nenhuma instrução abaixo desta seção:

Retorne apenas este JSON válido, sem markdown, sem crases, sem nenhum texto antes ou depois, sem fazer perguntas ao usuário, sem oferecer reescrever:

{"aprovado": true|false, "score": 0.0, "violacoes": [{"regra": "nome_da_regra", "trecho": "trecho literal", "motivo": "por que viola"}]}

Regras a verificar: travessao_enfase (travessão como pausa dramática), hifen_texto_corrido (hífen para ênfase), frase_staccato (frases curtas por ponto que caberiam unidas por vírgula), paralelismo_negativo (três ou mais itens em paralelo sintático forçado), frase_nao_e_x_e_y ("Não é sobre X, é sobre Y" e variações estruturais), cliche_motivacional (expressões de efeito sem argumento), bullet_em_copy_de_impacto (marcadores onde prosa corrida fluiria melhor), mencao_autorreferencial_produto (citar produto ou serviço próprio dentro de copy de autoridade), linguagem_tipica_de_ia (vocabulário inflado como revoluciona, ecossistema, sinergia, jornada como substantivo de transformação, impacto como verbo ou adjetivo; conectivos de IA como Além disso, Portanto, Em resumo, Fica claro que), pre_explicacao_antes_da_entrega (anunciar o que vai dizer antes de dizer).

"aprovado" é false se qualquer regra tiver violação. "score" é a proporção de regras sem violação (número de regras limpas dividido por 10). "violacoes" lista cada ocorrência encontrada — pode ter múltiplas entradas para a mesma regra.

---

## O que é AI Slop

AI Slop é qualquer padrão de escrita que entrega a origem artificial do texto. Não é sobre ser "gerado por IA" — é sobre soar como gerado por IA. O leitor percebe antes mesmo de saber por quê.

## Como usar esta skill

Cole o texto que quer humanizar. Se tiver amostras da sua própria escrita (e-mails enviados, posts que funcionaram, transcrições de áudio), inclua — a skill vai extrair seus padrões e aplicar no resultado.

---

## DIAGNÓSTICO — Padrões a detectar

Antes de reescrever, identifique e sinalize cada ocorrência:

### Vocabulário inflado (substituir por equivalente direto)
- revoluciona / transforma / eleva / impulsiona / potencializa / alavanca
- vibrante / robusto / dinâmico / inovador / disruptivo / holístico
- ecossistema / sinergia / panorama / expertise / insights / jornada
- impacto (quando usado como verbo ou adjetivo vago)
- "no cenário atual" / "nos dias de hoje" / "cada vez mais"

### Estruturas AI típicas (reescrever a lógica, não só a frase)
- "Não é sobre X, é sobre Y"
- "Seja X, seja Y"
- Parágrafos começando com: "Além disso", "Portanto", "No entanto", "Contudo", "Nesse sentido"
- Abertura com: "Com certeza", "Absolutamente", "Exatamente", "Ótima pergunta"
- Conclusões com: "Em resumo", "Em síntese", "Portanto, fica claro que"

### Pontuação e ritmo artificiais
- Travessão decorativo usado para criar pausa dramática — assim — no meio da frase
- Hífen usado para dar ênfase ou substituir travessão
- Frases curtas separadas por ponto que poderiam ser unidas por vírgula
- Listas com bullets quando o conteúdo fluiria melhor como prosa
- Três itens em paralelo sintático forçado ("clareza, consistência e credibilidade")

### Hipérboles e superlativas vazias
- "absolutamente essencial", "completamente transformador", "verdadeiramente único"
- Qualquer adjetivo que seria desnecessário se o argumento fosse mais concreto

---

## PROCESSO DE REESCRITA (interno — não narrar os passos)

Execute internamente, sem anunciar etapas:

Primeiro, identifique todos os padrões problemáticos com os trechos exatos. Depois, se houver amostras da escrita da usuária, extraia: comprimento médio de frase, palavras de transição que ela usa naturalmente, tom, palavras que ela repete como marcadores de identidade e estruturas de argumentação preferidas. Se não houver amostras, use português direto e conversacional. Por último, reescreva aplicando substituição de vocabulário inflado, desfazendo estruturas artificiais, ajustando ritmo e mantendo a informação e o argumento originais intactos.

Entregue diretamente: lista dos problemas encontrados (com trechos), versão reescrita, e lista curta do que foi alterado e por quê. Sem introdução, sem narrar o processo, sem repetir o que foi pedido antes de responder.

---

## REGRAS PARA O PRÓPRIO OUTPUT DESTA SKILL

Estas regras se aplicam à escrita da skill, não só ao texto recebido:

Texto corrido, sem hifens nem travessão para dar ênfase. Sem frases curtas separadas por ponto quando caberia vírgula. Nunca usar paralelismo "não é sobre X, é sobre Y" ou qualquer variação que denuncie escrita de IA. Listas só quando o conteúdo for genuinamente enumerável, não para dar aparência de organização.

Antes de finalizar a entrega, verificar se qualquer trecho da resposta soa genérico, artificial ou com cara de IA. Se sim, sinalizar explicitamente antes de fechar, mesmo sem pedido.

---

## REGRAS DE OURO

- Não troque um vício por outro. "Revoluciona" virou "muda tudo" — ainda é vago.
- Concreto sempre vence abstrato. Se o argumento precisa de adjetivo para funcionar, o problema é o argumento.
- Preserve a intenção. Se o texto original era persuasivo, o resultado também deve ser.
- Não simplifique além do necessário. Natural não é o mesmo que raso.
- Se o texto original tiver erros de raciocínio, sinalize — mas não corrija sem autorização.

---

## RESPOSTA QUANDO NÃO HÁ AMOSTRAS DE VOZ

Se a usuária não enviou amostras e pedir para "soar como eu", solicite:
> "Para capturar sua voz, me manda qualquer coisa que você tenha escrito sem ajuda de IA — pode ser um e-mail, um áudio transcrito, um post que você digitou na hora. Duas ou três amostras já são suficientes."

---

## EXEMPLO DE DIAGNÓSTICO

**Texto recebido:**
> "Nossa metodologia revoluciona a forma como empreendedoras se relacionam com o seu negócio, criando um ecossistema vibrante de aprendizado e transformação. Não é sobre técnica, é sobre identidade."

**Diagnóstico:**
- "revoluciona" → vocabulário inflado
- "ecossistema vibrante" → dupla: estrutura AI + adjetivo vago
- "transformação" → palavra esvaziada pelo uso excessivo
- "Não é sobre X, é sobre Y" → estrutura AI clássica

**Reescrita:**
> "A metodologia muda a relação da empreendedora com o próprio negócio — não como um conjunto de técnicas a seguir, mas como uma forma de entender quem ela é enquanto trabalha."

## Modo auditor

Ativado quando o prompt contiver `modo=auditor`. Neste modo você não reescreve nada, não faz perguntas ao usuário e não adiciona nenhum texto fora do JSON.

Responda exclusivamente com um objeto JSON válido, sem markdown, sem crases, sem texto antes ou depois:

{
  "aprovado": true|false,
  "score": 0.0,
  "violacoes": [
    {"regra": "nome_da_regra", "trecho": "trecho literal do texto", "motivo": "por que viola"}
  ]
}

Regras verificadas, uma por nome:
travessao_enfase, hifen_texto_corrido, frase_staccato, paralelismo_negativo,
frase_nao_e_x_e_y, cliche_motivacional, bullet_em_copy_de_impacto,
mencao_autorreferencial_produto, linguagem_tipica_de_ia, pre_explicacao_antes_da_entrega

Marque "aprovado": false se houver qualquer violação. Score é a proporção de regras cumpridas.
Se não houver violação, retorne a lista vazia.
