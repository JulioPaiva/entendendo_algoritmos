grafo = {}
grafo['rama'] = ['alex', 'amy', 'beethoven']

grafo['livro'] = {}
grafo['livro']['lp'] = 5
grafo['livro']['poster'] = 0

grafo['lp'] = {}
grafo['lp']['baixo'] = 15
grafo['lp']['bateria'] = 20

grafo['poster'] = {}
grafo['poster']['baixo'] = 30
grafo['poster']['bateria'] = 35

grafo['bateria'] = {}
grafo['bateria']['piano'] = 10

grafo['baixo'] = {}
grafo['baixo']['piano'] = 20

grafo['piano'] = {}

infinito = float('inf')

custos = {}
custos['lp'] = 5
custos['poster'] = 0
custos['baixo'] = infinito
custos['bateria'] = infinito
custos['piano'] = infinito

pais = {}
pais['lp'] = 'livro'
pais['poster'] = 'livro'
pais['baixo'] = None
pais['bateria'] = None
pais['piano'] = None

processados = []


def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo

    return nodo_custo_mais_baixo


nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]

    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)


print(grafo)
print(custos)
print(pais)
