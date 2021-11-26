from pesquisa_binaria import pesquisa_binaria
from pesquisa_simples import pesquisa_simples

vetor = []
item = 500
for i in range(0, 1024, 1):
    vetor.append(i)

binaria = pesquisa_binaria(vetor, item)
simples = pesquisa_simples(vetor, item)
print(f'binária: {binaria}')
print(f'simples: {simples}')
