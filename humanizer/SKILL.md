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
- Frases curtas separadas por ponto que poderiam ser unidas por vírgula
- Listas com bullets quando o conteúdo fluiria melhor como prosa
- Três itens em paralelo sintático forçado ("clareza, consistência e credibilidade")

### Hipérboles e superlativas vazias
- "absolutamente essencial", "completamente transformador", "verdadeiramente único"
- Qualquer adjetivo que seria desnecessário se o argumento fosse mais concreto

---

## PROCESSO DE REESCRITA

### Passo 1 — Diagnóstico
Liste os padrões encontrados com trechos específicos do texto. Não reescreva ainda. Mostre o que vai mudar e por quê.

### Passo 2 — Análise de voz (se houver amostras)
Se a usuária forneceu amostras de sua própria escrita:
- Identifique comprimento médio de frase
- Palavras de transição que ela usa naturalmente
- Tom (direto, coloquial, técnico, narrativo)
- Palavras que ela repete como marcadores de identidade
- Estruturas de argumentação preferidas

Se não houver amostras, reescreva em português direto e conversacional, sem região ou registro marcado.

### Passo 3 — Reescrita
Reescreva o texto completo aplicando:
- Substituição de vocabulário inflado por equivalente direto
- Desfazer estruturas artificiais mantendo o raciocínio
- Ajustar ritmo (frases mais variadas, menos paralelas)
- Aplicar voz da usuária se detectada nas amostras
- Manter a informação e o argumento originais intactos

### Passo 4 — Comparação
Apresente:
1. Trecho original com os problemas sublinhados (use **negrito** para marcar)
2. Versão reescrita
3. Lista curta do que foi alterado e por quê

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
