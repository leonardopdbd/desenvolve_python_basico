# Leia n1, n2, n3
n1 = float(input("Digite a primeira nota (n1): "))
n2 = float(input("Digite a segunda nota (n2): "))
n3 = float(input("Digite a terceira nota (n3): "))

# Calcule a média
m = (n1 + n2 + n3) / 3

# Verifique as condições
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

# Imprima "Fim"
print("Fim")
