# Introdução a algoritmos :metal:

 * Um algoritmo é um conjunto de instruções que realizam uma tarefa. 
 * A rapidez de um algoritmo não é medida em segundos, mas pelo crescimento do número de operações. :runner:
 * Se discute o tempo de execução de um algoritmo conforme a quantidade de elementos aumenta.  :clock1:

## Pesquisa Simples
 - Faz busca sequencial, item por item.
 - O numero de etapas é igual ao tamanho do vetor.
 - Ocorre em tempo linear.

 Ex: pesquisa_simples.py

## Pesquisa Binária :eyes:
 - Pesquisa que segue o paradigma de divisão e conquista. 
 - O vetor deve estar ordenado.
 - Realizando sucessivas divisões do espaço comparando a com a busca.
 - O numero de etapas é o logaritmo do tamanho do vetor + 1. 
        ex: [1, 2, 3, 4] log2 4 = 2 
            Resposta: 3 etapas. 
 - Ocorre em tempo logarítmico.

 Ex: pesquisa_binaria.py

## BIG O :heavy_exclamation_mark: :eyes:
 - Diz quão rápido é um algoritmo. 
 - Ajuda a determinar qual o comportamento do algoritmo na pior das hipóteses.
 - O(n) = Pesquisa simples, tempo linear.
 - O(log n) = Pesquisa binária, tempo logaritmico.
 - O(n * log n) = Quicksort, uma ordenação rápida.
 - O(n^2) = Ordenação por seleção, uma ordenação lenta.
 - O(n!) = Caixeiro viajante, um algoritmo bem lento.

## Caixeiro-viajante
 - É um problema que tenta determinar a menor rota para percorrer uma série de cidades.
 - É um problema de otimização difícil. :ghost:
