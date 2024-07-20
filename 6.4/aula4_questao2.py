# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Definindo conjuntos de vogais e consoantes
vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# Usando compreensão de listas para gerar as listas de vogais e consoantes
lista_vogais = sorted([char for char in frase if char in vogais])
lista_consoantes = [char for char in frase if char in consoantes]

# Imprimindo as listas geradas
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
