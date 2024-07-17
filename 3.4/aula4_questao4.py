# Solicita a distância da entrega em quilômetros
distancia = float(input("Digite a distância da entrega (em km): "))

# Solicita o peso do pacote em quilogramas
peso = float(input("Digite o peso do pacote (em kg): "))

# Inicializa a taxa de frete
if distancia <= 100:
    taxa_por_kg = 1.0
elif 101 <= distancia <= 300:
    taxa_por_kg = 1.50
else:
    taxa_por_kg = 2.0

# Calcula o valor do frete
frete = taxa_por_kg * peso

# Adiciona taxa adicional para pacotes acima de 10 kg
if peso > 10:
    frete += 10

# Imprime o valor final do frete
print(f"O valor do frete é: R${frete:.2f}")
