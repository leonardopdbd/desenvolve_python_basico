import random

def encrypt(names):
    # Gera um valor aleatório n entre 1 e 10
    key = random.randint(1, 10)
    
    # Função auxiliar para criptografar uma string
    def encrypt_name(name, key):
        encrypted_name = ""
        for char in name:
            # Verifica se o caracter está no intervalo de caracteres visíveis
            if 33 <= ord(char) <= 126:
                # Substitui o caracter pelo caracter c + n
                new_char = chr(((ord(char) - 33 + key) % 94) + 33)
                encrypted_name += new_char
            else:
                # Se o caracter não estiver no intervalo, mantém o mesmo
                encrypted_name += char
        return encrypted_name
    
    # Criptografa cada nome na lista
    encrypted_names = [encrypt_name(name, key) for name in names]
    
    return encrypted_names, key

# Lista de nomes para criptografar
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Chama a função encrypt
nomes_cript, chave_aleatoria = encrypt(nomes)

# Exibe os nomes criptografados e a chave de criptografia
print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")
