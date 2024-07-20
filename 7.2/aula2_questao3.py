import string

def is_palindrome(phrase):
    # Remove espaços e sinais de pontuação, e converte para minúsculas
    cleaned_phrase = ''.join(char.lower() for char in phrase if char.isalnum())
    
    # Verifica se a frase é um palíndromo
    return cleaned_phrase == cleaned_phrase[::-1]

def main():
    while True:
        # Solicita uma frase do usuário
        user_input = input('Digite uma frase (digite "fim" para encerrar): ')
        
        # Encerra o loop se o usuário digitar "fim"
        if user_input.lower() == "fim":
            break
        
        # Verifica se a frase é um palíndromo
        if is_palindrome(user_input):
            print(f'"{user_input}" é palíndromo')
        else:
            print(f'"{user_input}" não é palíndromo')

# Chama a função principal
main()
