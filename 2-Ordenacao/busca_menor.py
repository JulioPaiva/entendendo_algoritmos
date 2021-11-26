def busca_menor(arr):
    menor_elemento = arr[0]
    menor_indice = 0
    for item in range(1, len(arr)):
        if arr[item] < menor_elemento:
            menor_elemento = arr[item]
            menor_indice = item

    return menor_indice
