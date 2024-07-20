def count_spaces():
    # Solicita a frase do usuário
    phrase = input("Digite a frase: ")
    
    # Conta os espaços em branco
    space_count = phrase.count(" ")
    
    # Exibe o número de espaços em branco
    print(f"Espaços em branco: {space_count}")

# Chama a função
count_spaces()
