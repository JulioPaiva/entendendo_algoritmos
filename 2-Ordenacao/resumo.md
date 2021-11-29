# Ordenação por Seleção

A memória de seu computador é como um conjunto de gavetas. Quando se quer armazenar múltiplos elementos, usa-se um array ou uma lista.

## Lista encadeada
Os elementos são espalhados e um elemento guarda o endereço de memória do próximo elemento. Permite rápidas inserções e eliminações.

 - Tempo de execução para leitura O(n)
 - Tempo de execução para inserção O(1)
 - Tempo de execução para exclusão O(1)

## Arrays
Todos os elementos são armazenados um ao lado do outro. Permite uma rápida leitura, se inicia com indice 0, seus elementos devem ser do mesmo tipo.

 - Tempo de execução para leitura O(1)
 - Tempo de execução para inserção O(n)
 - Tempo de execução para exclusão O(n)

| - | Array | Lista |
| ----- | ----- | ----- |
| **Leitura** | O(1) | O(n) |
| **Inserção** | O(n) | O(1) |
| **Eliminação** | O(n) | O(1) |
