def encontrar_maior_numero():
    """
    Função que encontra o maior número entre vários números digitados pelo usuário.

    Retorna:
        int: O maior número digitado.
    """
    maior = None

    while True:
        try:
            numero_vezes_loop = int(input("Digite o número de vezes que o loop irá rodar: "))
            if numero_vezes_loop < 1:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro positivo.")

    for _ in range(numero_vezes_loop):
        try:
            numero = int(input("Digite um número: "))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue

        if maior is None or numero > maior:
            maior = numero

    return maior


if __name__ == "__main__":
    maior_numero = encontrar_maior_numero()
    print(f"O maior número lido foi: {maior_numero}")
5