import re

def analisar_arquivo(nome_arquivo):
    # Abre o arquivo para leitura
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    # 1. Imprime o texto das primeiras 25 linhas
    print("Texto das primeiras 25 linhas:")
    for i in range(min(25, len(linhas))):
        print(linhas[i].strip())
    print()
    
    # 2. Número de linhas do arquivo
    numero_linhas = len(linhas)
    print(f"Número de linhas do arquivo: {numero_linhas}")
    
    # 3. Linha com maior número de caracteres
    linha_maior = max(linhas, key=len)
    print(f"Linha com maior número de caracteres:")
    print(linha_maior.strip())
    print()
    
    # 4. Contagem de menções aos nomes dos personagens "Nonato" e "Íria"
    def contar_mencoes(texto, nome):
        return len(re.findall(rf'\b{nome}\b', texto, re.IGNORECASE))
    
    total_nonato = sum(contar_mencoes(linha, "Nonato") for linha in linhas)
    total_iria = sum(contar_mencoes(linha, "Íria") for linha in linhas)
    
    print(f"Número de menções a 'Nonato': {total_nonato}")
    print(f"Número de menções a 'Íria': {total_iria}")

# Nome do arquivo
nome_arquivo = 'estomago.txt'

# Chama a função de análise
analisar_arquivo(nome_arquivo)
