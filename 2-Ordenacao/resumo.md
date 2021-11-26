# Ordenação por Seleção

 - Faremos um algoritmo de ordenação.
 - Quando se quer armazenar muitos elementos usamos lista ou array.

## Lista encadeada
 - Armazena um item em um espaço de memória e guarda referência para o próximo item. 
 - Cada item da lista não necessáriamente está um do lado do outro nos slots de memória.
 - Boa para distribuição e espaço de memória. 
 - Ruim quando quer acessar o último elemento da lista.
 - Melhores para adicionar um elemento no meio da lista.
 - Tempo de execução para leitura O(n)
 - Tempo de execução para inserção O(1)
 - Tempo de execução para exclusão O(1)

## Arrays
 - Armazena seus itens sequencialmente na memória. 
 - Ruim para encontrar espaço em memória. 
 - Bom para ler elementos aleatórios.
 - Começa com indice 0.
 - Tempo de execução para leitura O(1)
 - Tempo de execução para inserção O(n)
 - Tempo de execução para exclusão O(n)