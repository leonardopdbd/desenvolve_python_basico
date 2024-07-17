# Solicita as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se ambas as idades são maiores de 17
podem_entrar = idade_juliana > 17 and idade_cris > 17

# Imprime o resultado
print(podem_entrar)
