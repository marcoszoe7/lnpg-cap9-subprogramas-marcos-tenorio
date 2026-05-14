# lnpg-cap9-subprogramas-marcos-tenorio

**Nome:** Marcos Antonio Ferreira Tenorio
**LLM utilizado:** Claude
**Modelo:** Claude Sonnet 4.5

---

## Tarefa 1 — Sistema Acadêmico (Java)

Nessa tarefa foi desenvolvido um sistema acadêmico que solicita o nome do aluno e suas 3 notas, calcula a média e retorna a situação: Aprovado, Recuperação ou Reprovado, dependendo do resultado.

Comparação — Monolítica vs Modularizada:
Na versão monolítica, todo o código estava concentrado no método main, o que dificultava a leitura e a identificação de cada etapa. Já na versão modularizada, cada bloco de código foi separado em métodos com responsabilidades claras, tornando muito mais fácil identificar o que cada parte faz.

Legibilidade e fluxo: A versão modularizada apresentou um fluxo de execução bem mais organizado e lógico, onde cada chamada de método indica claramente o que está acontecendo naquele momento.

Tamanho dos métodos: Os métodos ficaram com um número razoável de linhas, de fácil entendimento, sem sobrecarregar o leitor com informações desnecessárias.

Coesão: Cada método pertence a um mesmo propósito e contexto, funcionando em conjunto para uma finalidade clara — calcular e exibir a situação acadêmica do aluno.

Reutilização e manutenção: Por estar modularizado, qualquer correção ou melhoria pode ser feita diretamente no método responsável, sem precisar alterar o resto do código.

## Tarefa 2 — Sistema de Vendas (Python)

Nesta tarefa foi desenvolvido um sistema de vendas simples em Python, que solicita o produto, a quantidade e o preço unitário desejado pelo cliente. No final, o sistema calcula o subtotal, aplica o desconto conforme o valor da compra e retorna o total a pagar.

Comparação — Monolítica vs Modularizada:
Na versão monolítica, consegui entender o código, porém as informações estavam misturadas em sequência, sem divisão clara de responsabilidades. Qualquer alteração exigiria modificar várias partes do código manualmente.
Na versão modularizada, a organização ficou nítida — cada função tem seu próprio fluxo e argumentos bem definidos, tornando o sistema mais legível e fácil de modificar.

Legibilidade e fluxo: A versão modularizada apresentou melhor legibilidade e execução mais organizada. Em cada função foi possível identificar claramente o que ela recebe, o que faz e o que retorna.

Tamanho dos métodos: Os métodos ficaram com um número razoável de linhas, sem sobrecarregar quem está lendo, mantendo um fluxo rápido e direto de informações.

Coesão: Cada método pertence ao contexto do sistema de vendas, funcionando em conjunto para calcular e retornar o total correto ao cliente.

Reutilização e manutenção: Por estar em Python, sem necessidade de declarar tipos, o código ficou ainda mais conciso que o Java da tarefa 1, mantendo a mesma clareza de responsabilidades.

## Tarefa 3 — Passagem por Valor (Java)

## Tarefa 4 — Objetos e Referência (Java)

## Tarefa 5 — Gerenciamento de Tarefas (Python)

---

## Diagrama de chamadas

### Tarefa 1
```
main()
├── lerAluno()
├── lerNotas()
├── calcularMedia(notas)
├── determinarSituacao(media)
└── imprimirRelatorio(nome, media, situacao)
```

### Tarefa 5
```
main()
├── exibir_menu()
├── adicionar_tarefa(titulo, prioridade)
├── listar_tarefas()
├── concluir_tarefa(indice)
├── remover_tarefa(indice)
└── buscar_tarefa(palavra)
```
## Justificativa da divisão dos subprogramas

## Dificuldades encontradas

## Vantagens percebidas da modularização
---


