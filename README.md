# lnpg-cap9-subprogramas-marcos-tenorio

**Nome:** Marcos Antonio Ferreira Tenorio
**LLM utilizado:** Claude
**Modelo:** Claude Sonnet 4.5
**Turma:** LNPG-BSI-2026.1
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

Nesta tarefa foi criado um programa em Java para demonstrar como funciona a passagem de parâmetros por valor utilizando um tipo primitivo.
No programa observei, que a variável número recebe o valor 10 no método main. Esse valor é passado para o método alterarNumero(int x), onde o parâmetro x recebe apenas uma cópia do valor original e é alterado para 20 dentro do método.
Mesmo após mudar, a variável número no main continua valendo 10. Isso acontece porque Java não passa a variável original para o método, ou seja, ele passa uma cópia do valor armazenado nela. 
Qualquer modificação feita em x existe apenas dentro do método alterarNumero() e some quando ele termina.

O que aprendi: Tipos primitivos como int, double e boolean são sempre passados por valor em Java. Isso significa que o método trabalha com uma cópia, ou seja, o dado original fica protegido de alterações externas.

Dificuldade encontrada: No início achei confuso entender por que o valor não mudava no main, mas depois de ver a saída do programa ficou bem claro, conseguir entender rodando e observando o código, pois o método alterava apenas a sua cópia local.


## Tarefa 4 — Objetos e Referência (Java)

Nesta tarefa foi criado um programa em Java para demonstrar a diferença entre passar um tipo primitivo e passar um objeto para um método.
No programa, um objeto da classe Produto foi criado com o nome "Notebook" e preço de R$ 3000,00. Esse objeto foi passado para o método aplicarDesconto(), que reduziu o preço em 10%.
Diferente da tarefa 3, onde o valor não mudava no main, aqui o preço do produto mudou, de R$ 3000,00 para R$ 2700,00, mesmo quando depois o método terminar.

Quando passamos um objeto para um método em Java, não estamos passando o objeto em si, mas sim o endereço de onde ele está na memória. O método recebe esse endereço e vai até o objeto original para fazer a alteração. Por isso a mudança persiste no main.

Comparando com a tarefa 3:
Na tarefa 3, o número não mudou porque Java copiou o valor. Na tarefa 4, o preço mudou porque Java copiou o endereço do objeto, e ambas as variáveis apontavam para o mesmo lugar na memória.

Dificuldade encontrada: Essa foi a tarefa mais difícil de entender, pois no começo não conseguir como o Java passava o objeto na qual estou trabalhando. 
Java passa por valor, mas o objeto mudou. A explicação do endereço de memória ajudou a clarear essa dúvida.


## Tarefa 5 — Gerenciamento de Tarefas (Python)

Nesta tarefa foi desenvolvido em Python um sistema de gerenciamento de tarefas, com o objetivo de permitir que o usuário adicione, liste, conclua, remova e busque tarefas. O sistema retorna os valores de forma organizada, dando ao usuário controle total sobre suas tarefas.

Legibilidade e fluxo: O fluxo das funções ficou bem organizado e dinâmico. Por já ter familiaridade com Python, consegui distribuir corretamente cada função em sua determinada responsabilidade, mantendo uma boa coesão entre elas.

Estrutura utilizada: Optei por utilizar tanto dicionários quanto listas no programa, e os dicionários para armazenar os dados de cada tarefa e a lista para guardar todas as tarefas cadastradas.

Tamanho dos métodos e coesão: Cada função ficou com um tamanho razoável e bem coesa, onde cada uma tem um propósito claro dentro do sistema.
Dificuldade encontrada: A única dificuldade foi na função de remover tarefa, que exigiu um pouco mais de atenção por utilizar índice para localizar e remover o item correto da lista.

Vantagens da modularização: Dividir o código em funções foi a melhor escolha, se tudo ficasse junto, atrapalharia o raciocínio e o fluxo do programa. Com as funções separadas, consigo identificar falhas com mais facilidade, reutilizar o código quando necessário e detalhar cada parte de forma independente.

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

A divisão em subprogramas foi escolhida porque deixar tudo junto em um único bloco de código atrapalharia o raciocínio e dificultaria a identificação do fluxo do programa. Com cada função tendo sua própria responsabilidade, o código ficou mais organizado, legível e fácil de entender. Além disso, a separação permite identificar falhas com mais facilidade e reutilizar funções em diferentes partes do sistema sem precisar reescrever o código.

## Dificuldades encontradas

A maior dificuldade geral foi na Tarefa 4, onde foi necessário entender como Java passa objetos para métodos. No início parecia contraditório — Java passa por valor, mas o objeto mudava. A explicação do endereço de memória ajudou a clarear essa dúvida. Na Tarefa 5, a função de remover tarefa exigiu mais atenção por utilizar índice para localizar e remover o item correto da lista.

## Vantagens percebidas da modularização:

Código mais legível e organizado;
Fácil identificação de falhas em cada função;
Possibilidade de reutilizar funções sem repetir código;
Manutenção mais simples — qualquer correção é feita apenas na função responsável;
Fluxo de execução mais claro e dinâmico.
---


