import re

def processar_arquivo():
    # Lê o conteúdo do arquivo "frase.txt"
    with open("frase.txt", "r") as arquivo:
        frase = arquivo.read()
    
    # Remove todos os caracteres não alfabéticos e espaços em branco
    palavras = re.findall(r'[a-zA-Z]+', frase)
    
    # Salva as palavras em "palavras.txt", uma por linha
    with open("palavras.txt", "w") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")
    
    # Lê e imprime o conteúdo do arquivo "palavras.txt"
    with open("palavras.txt", "r") as arquivo:
        conteudo = arquivo.read()
    
    print(conteudo)

# Chama a função
processar_arquivo()
