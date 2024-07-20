def welcome_user():
    # Solicita o primeiro nome do usuário
    first_name = input("Digite seu primeiro nome: ")
    
    # Solicita o sobrenome do usuário
    last_name = input("Digite seu sobrenome: ")
    
    # Concatena o primeiro nome e o sobrenome
    full_name = first_name + " " + last_name
    
    # Exibe a mensagem de boas-vindas
    print(f"Bem-vindo(a), {full_name}!")

# Chama a função
welcome_user()
