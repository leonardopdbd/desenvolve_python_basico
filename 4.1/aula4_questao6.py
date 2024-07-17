# Lê a quantidade de experimentos registrados
N = int(input("Digite a quantidade de experimentos registrados: "))

# Inicializa variáveis para armazenar os totais
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Lê os dados de cada experimento
for _ in range(N):
    entrada = input("Digite a quantidade de cobaias e o tipo (S, R ou C): ")
    quantia, tipo = entrada.split()
    quantia = int(quantia)
    
    # Atualiza os totais de acordo com o tipo de cobaia
    total_cobaias += quantia
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

# Calcula os percentuais de cada tipo de cobaia
percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

# Imprime os resultados
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
