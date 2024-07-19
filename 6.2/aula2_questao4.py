# Função para ler uma lista de números do usuário
def ler_lista(mensagem):
    quantidade = int(input(mensagem))
    lista = []
    for i in range(quantidade):
        numero = int(input())
        lista.append(numero)
    return lista

# Função para intercala duas listas
def intercalar_listas(lista1, lista2):
    intercalada = []
    # Intercalar elementos
    for i in range(min(len(lista1), len(lista2))):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    # Adicionar os elementos restantes da lista maior
    if len(lista1) > len(lista2):
        intercalada.extend(lista1[len(lista2):])
    else:
        intercalada.extend(lista2[len(lista1):])
    return intercalada

# Leitura das listas do usuário
lista1 = ler_lista("Digite a quantidade de elementos da lista 1: ")
lista2 = ler_lista("Digite a quantidade de elementos da lista 2: ")

# Intercalar as listas
lista_intercalada = intercalar_listas(lista1, lista2)

# Imprimir a lista intercalada
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
