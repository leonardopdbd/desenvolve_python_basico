import string

def validador_senha(senha):
    # Verifica o comprimento mínimo da senha
    if len(senha) < 8:
        return False
    
    # Inicializa as flags para verificar a presença de cada tipo de caractere
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Define os caracteres especiais
    special_characters = string.punctuation
    
    # Verifica cada caractere da senha
    for char in senha:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    # Retorna True se todos os critérios forem atendidos
    return has_upper and has_lower and has_digit and has_special

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
