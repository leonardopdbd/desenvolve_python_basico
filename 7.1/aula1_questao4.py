def format_phone_number():
    # Solicita o número do celular do usuário
    phone_number = input("Digite o número: ")
    
    # Verifica o comprimento do número
    if len(phone_number) == 8:
        # Adiciona o 9 na frente se o número tiver 8 dígitos
        phone_number = "9" + phone_number
    elif len(phone_number) == 9 and phone_number[0] != "9":
        print("Número inválido. O primeiro dígito deve ser 9.")
        return
    
    # Adiciona o separador "-"
    formatted_number = phone_number[:5] + "-" + phone_number[5:]
    
    # Exibe o número completo formatado
    print(f"Número completo: {formatted_number}")

# Chama a função
format_phone_number()
