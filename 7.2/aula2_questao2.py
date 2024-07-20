def replace_vowels():
    # Solicita a frase do usuário
    phrase = input("Digite uma frase: ")
    
    # Define as vogais
    vowels = "aeiouAEIOU"
    
    # Substitui todas as vogais por "*"
    modified_phrase = ""
    for char in phrase:
        if char in vowels:
            modified_phrase += "*"
        else:
            modified_phrase += char
    
    # Exibe a frase modificada
    print(f"Frase modificada: {modified_phrase}")

# Chama a função
replace_vowels()
