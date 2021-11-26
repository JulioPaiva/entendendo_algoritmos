def pesquisa_simples(vetor, item):
    tentativas = 0
    for v in vetor:
        tentativas += 1
        if v == item:
            return tentativas
