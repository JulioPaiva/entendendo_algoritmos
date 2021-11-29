# Introdução a algoritmos :metal:

Um algoritmo é um conjunto de instruções que realizam uma tarefa. O tempo de execução é medido por meio de seu crescimento e expresso na notação big O. :runner:

## Pesquisa Simples
Faz uma busca sequencial na lista, item por item. Com isso seu número de etapas é igual ao tamanho do vetor. Ocorre em tempo linear.

    '''Ex: pesquisa_simples.py'''

## Pesquisa Binária :eyes:
Esta pesquisa que segue o paradigma de divisão e conquista. Realiza sucessivas divisões do espaço comparando a com a busca.   Ocorre em tempo logarítmico, lembrando que o vetor deve estar ordenado.

    '''Ex: pesquisa_binaria.py'''


## BIG O :heavy_exclamation_mark: :eyes:
Diz quão rápido é um algoritmo. Ajuda a determinar qual o comportamento do algoritmo na pior das hipóteses.
| Notação | Exemplo |
|:---:|:---:|
|O(n) | Pesquisa simples, tempo linear |
|O(log n) | Pesquisa binária, tempo logaritmico |
|O(n * log n) | Quicksort, uma ordenação rápida |
|O(n^2) | Ordenação por seleção, uma ordenação lenta |
|O(n!) | Caixeiro viajante, um algoritmo bem lento |


## :duck:Caixeiro-viajante
    É um problema de otimização difícil que tenta determinar a menor rota para percorrer uma série de cidades. :ghost:
