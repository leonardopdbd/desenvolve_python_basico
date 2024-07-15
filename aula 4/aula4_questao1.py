# Solicita ao usuário a entrada do comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno em metros: "))

# Solicita ao usuário a entrada da largura do terreno
largura = int(input("Digite a largura do terreno em metros: "))

# Solicita ao usuário a entrada do preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado em reais: "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime o resultado formatado com duas casas decimais
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
