import random
from math import sqrt

def calcular_raiz_quadrada_soma(n):
    # Gerando n valores inteiros aleatórios entre 0 e 100
    valores = [random.randint(0, 100) for _ in range(n)]
    
    # Calculando a soma dos valores
    soma = sum(valores)
    
    # Calculando a raiz quadrada da soma
    raiz_quadrada_soma = sqrt(soma)
    
    # Exibindo os valores gerados e o resultado
    print(f"Valores gerados: {valores}")
    print(f"Soma dos valores: {soma}")
    print(f"Raiz quadrada da soma: {raiz_quadrada_soma}")

# Pedindo ao usuário o valor de n
n = int(input("Digite o valor de n: "))

# Chamando a função para calcular a raiz quadrada da soma
calcular_raiz_quadrada_soma(n)
