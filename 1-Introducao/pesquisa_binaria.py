def pesquisa_binaria(lista, item):
    baixo = 0
    alto = (len(lista) - 1)
    tentativas = 1

    while (baixo <= alto):
        tentativas += 1
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return tentativas
