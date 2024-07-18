import random

def adivinhar_numero():
    # Gerando um número aleatório entre 1 e 10
    numero_secreto = random.randint(1, 10)
    
    while True:
        # Pedindo ao usuário para adivinhar o número
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        
        # Verificando se o palpite é muito alto, muito baixo ou correto
        if palpite < numero_secreto:
            print("Muito baixo, tente novamente!")
        elif palpite > numero_secreto:
            print("Muito alto, tente novamente!")
        else:
            print(f"Correto! O número é {numero_secreto}.")
            break

# Chamando a função para começar o jogo
adivinhar_numero()
