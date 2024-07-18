def calcular_diferenca_absoluta():
    # Solicita ao usuário para inserir os dois números decimais
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Calcula a diferença absoluta entre os números
    diferenca_absoluta = abs(num1 - num2)
    
    # Arredonda o resultado para duas casas decimais
    diferenca_arredondada = round(diferenca_absoluta, 2)
    
    # Exibe o resultado para o usuário
    print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")

# Chama a função para executar o programa
calcular_diferenca_absoluta()
