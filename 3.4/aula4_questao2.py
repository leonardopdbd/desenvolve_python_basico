# Solicita a avaliação do filme
avaliacao = int(input("Insira a avaliação do filme (de 1 a 5): "))

# Verifica a avaliação e imprime a mensagem correspondente
if avaliacao == 5:
    mensagem = "Excelente!"
elif avaliacao == 4:
    mensagem = "Muito Bom!"
elif avaliacao == 3:
    mensagem = "Bom!"
elif avaliacao == 2:
    mensagem = "Regular."
elif avaliacao == 1:
    mensagem = "Ruim."
else:
    mensagem = "Avaliação inválida. Por favor, insira um valor entre 1 e 5."

# Imprime a mensagem
print(mensagem)
