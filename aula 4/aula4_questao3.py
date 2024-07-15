# Solicita as informações do produto 1
produto1_nome = input("Digite o nome do produto 1: ")  # Entrada do nome do produto 1
produto1_preco = float(input("Digite o preço unitário do produto 1: "))  # Entrada do preço unitário do produto 1
produto1_quantidade = int(input("Digite a quantidade do produto 1: "))  # Entrada da quantidade do produto 1

# Solicita as informações do produto 2
produto2_nome = input("Digite o nome do produto 2: ")  # Entrada do nome do produto 2
produto2_preco = float(input("Digite o preço unitário do produto 2: "))  # Entrada do preço unitário do produto 2
produto2_quantidade = int(input("Digite a quantidade do produto 2: "))  # Entrada da quantidade do produto 2

# Solicita as informações do produto 3
produto3_nome = input("Digite o nome do produto 3: ")  # Entrada do nome do produto 3
produto3_preco = float(input("Digite o preço unitário do produto 3: "))  # Entrada do preço unitário do produto 3
produto3_quantidade = int(input("Digite a quantidade do produto 3: "))  # Entrada da quantidade do produto 3

# Calcula o preço total para cada produto
total_produto1 = produto1_preco * produto1_quantidade  # Cálculo do total do produto 1
total_produto2 = produto2_preco * produto2_quantidade  # Cálculo do total do produto 2
total_produto3 = produto3_preco * produto3_quantidade  # Cálculo do total do produto 3

# Calcula o preço total da compra
preco_total = total_produto1 + total_produto2 + total_produto3  # Cálculo do preço total da compra

# Imprime o resultado formatado com separador de milhar e duas casas decimais
print(f"Total: R${preco_total:,.2f}")  # Impressão do resultado formatado
