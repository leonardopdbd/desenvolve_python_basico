import random

# Gerar 20 valores inteiros aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Criar uma cópia da lista para ordenar sem modificar a original
valores_ordenados = sorted(valores)

# Encontrar o índice do maior e do menor valor
indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

# Imprimir os resultados
print("Lista ordenada:", valores_ordenados)
print("Lista original:", valores)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
