# Solicita ao usuário a entrada de um valor inteiro em reais
valor = int(input("Digite um valor em reais: "))

# Define as notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Inicializa um dicionário para armazenar a quantidade de cada nota
quantidade_notas = {}

# Calcula a quantidade de cada nota necessária
for nota in notas:
    quantidade_notas[nota] = valor // nota  # Calcula a quantidade de notas de valor 'nota'
    valor %= nota  # Atualiza o valor restante após a retirada das notas de valor 'nota'

# Imprime o resultado formatado
for nota in notas:
    print(f"{quantidade_notas[nota]} nota(s) de R${nota},00")
