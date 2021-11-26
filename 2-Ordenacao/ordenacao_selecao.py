from busca_menor import busca_menor


def ordenacao_selecao(arr):
    resposta = []
    while(len(arr) > 0):
        menor = busca_menor(arr)
        resposta.append(arr.pop(menor))

    print(resposta)


ordenacao_selecao([1, 4, 2, 6, 5])
