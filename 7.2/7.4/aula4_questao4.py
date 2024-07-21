import random

def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras

def carregar_enforcado(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        enforcados = arquivo.read().splitlines()
    return enforcados

def imprime_enforcado(estagios, erros):
    if erros < len(estagios):
        print(estagios[erros])
    else:
        print("Número de erros excedeu o limite!")

def jogo_da_forca():
    palavras = carregar_palavras("gabarito_forca.txt")
    enforcados = carregar_enforcado("gabarito_enforcado.txt")

    palavra = random.choice(palavras).upper()
    palavra_oculta = ['_'] * len(palavra)
    letras_erradas = set()
    erros = 0
    tentativas_max = 6

    print("Bem-vindo ao jogo da Forca!")
    
    while erros < tentativas_max and '_' in palavra_oculta:
        print(" ".join(palavra_oculta))
        print(f"Tentativas restantes: {tentativas_max - erros}")
        imprime_enforcado(enforcados, erros)
        letra = input("Digite uma letra: ").upper()

        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[i] = letra
        else:
            if letra not in letras_erradas:
                letras_erradas.add(letra)
                erros += 1
            else:
                print("Você já tentou essa letra.")

    if '_' not in palavra_oculta:
        print(f"Parabéns! Você acertou a palavra: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")
        imprime_enforcado(enforcados, erros)

# Executa o jogo
jogo_da_forca()
