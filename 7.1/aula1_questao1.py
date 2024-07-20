def print_name_stairs():
    # Solicita o nome do usuário
    name = input("Digite seu nome: ")
    
    # Imprime o nome em forma de escada
    for i in range(1, len(name) + 1):
        print(name[:i])

# Chama a função
print_name_stairs()
