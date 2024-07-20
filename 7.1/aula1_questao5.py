def count_vowels():
    # Solicita a frase do usuário
    phrase = input("Digite uma frase: ")
    
    # Define as vogais
    vowels = "aeiouAEIOU"
    
    # Inicializa o contador de vogais e a lista de índices
    vowel_count = 0
    vowel_indices = []
    
    # Itera sobre a frase para contar vogais e armazenar os índices
    for index, char in enumerate(phrase):
        if char in vowels:
            vowel_count += 1
            vowel_indices.append(index)
    
    # Exibe o número de vogais e os índices
    print(f"{vowel_count} vogais")
    print(f"Índices {vowel_indices}")

# Chama a função
count_vowels()
