def validate_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return "Inválido"
    
    # Calcula o primeiro dígito verificador
    def calculate_digit(cpf, length):
        total_sum = 0
        multiplier = length + 1
        for i in range(length):
            total_sum += int(cpf[i]) * multiplier
            multiplier -= 1
        remainder = total_sum % 11
        if remainder < 2:
            return 0
        else:
            return 11 - remainder
    
    # Calcula os dígitos verificadores
    first_digit = calculate_digit(cpf, 9)
    second_digit = calculate_digit(cpf[:9] + str(first_digit), 10)
    
    # Verifica se os dígitos calculados são iguais aos dígitos informados
    if cpf[-2:] == str(first_digit) + str(second_digit):
        return "Válido"
    else:
        return "Inválido"

# Solicita o CPF do usuário
cpf_input = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")
result = validate_cpf(cpf_input)
print(result)
