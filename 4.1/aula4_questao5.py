# Lê a quantidade de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Inicializa uma lista para armazenar as idades
idades = []

# Lê as idades dos respondentes
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i + 1}: "))
    idades.append(idade)

# Calcula a média das idades
media_idades = sum(idades) / N

# Imprime a média das idades
print(f"A média das idades dos respondentes é: {media_idades:.2f}")
