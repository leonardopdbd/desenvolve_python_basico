import random
from collections import Counter

# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrar a interseção sem duplicatas
interseccao = list(set(lista1) & set(lista2))

# Ordenar a lista de interseção
interseccao_ordenada = sorted(interseccao)

# Contar a quantidade de vezes que cada elemento aparece em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Imprimir as listas e a interseção
print("Lista1:", lista1)
print("Lista2:", lista2)
print("Interseccao:", interseccao_ordenada)

# Imprimir a contagem dos elementos
print("Contagem")
for elemento in interseccao_ordenada:
    cont_lista1 = contagem_lista1[elemento]
    cont_lista2 = contagem_lista2[elemento]
    print(f"{elemento}: (lista1={cont_lista1}, lista2={cont_lista2})")
