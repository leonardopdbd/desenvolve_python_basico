def get_integer_input():
    while True:
        try:
            return int(input("Digite um número inteiro (ou 'done' para terminar): "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Solicita ao usuário pelo menos 4 números inteiros
numbers = []
print("Por favor, insira pelo menos 4 números inteiros.")
while len(numbers) < 4:
    number = get_integer_input()
    numbers.append(number)

# Continuar solicitando números até o usuário digitar 'done'
while True:
    user_input = input("Digite 'done' para terminar ou um número inteiro para adicionar à lista: ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Realiza as operações solicitadas usando fatiamento de listas
print(f"Lista original: {numbers}")
print(f"Os 3 primeiros elementos: {numbers[:3]}")
print(f"Os 2 últimos elementos: {numbers[-2:]}")
print(f"Lista invertida: {numbers[::-1]}")
print(f"Elementos de índice par: {numbers[::2]}")
print(f"Elementos de índice ímpar: {numbers[1::2]}")
