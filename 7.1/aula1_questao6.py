def find_anagrams():
    # Solicita a frase e a palavra objetivo do usuário
    phrase = input("Digite uma frase: ")
    target_word = input("Digite a palavra objetivo: ")
    
    # Converte a palavra objetivo para uma lista de caracteres ordenada
    sorted_target = sorted(target_word.lower())
    
    # Inicializa a lista de anagramas
    anagrams = []
    
    # Divide a frase em palavras
    words = phrase.split()
    
    # Itera sobre as palavras na frase
    for word in words:
        # Compara a palavra atual com a palavra objetivo (ordenada)
        if sorted(word.lower()) == sorted_target:
            anagrams.append(word)
    
    # Exibe a lista de anagramas encontrados
    print(f"Anagramas: {anagrams}")

# Chama a função
find_anagrams()
