import random

# Gera uma lista de 20 elementos entre -10 e 10
original_list = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", original_list)

# Função para encontrar o intervalo com o maior número de negativos
def find_interval_with_most_negatives(lst):
    max_negatives = 0
    max_interval = (0, 0)
    
    # Verifica todos os possíveis intervalos
    for start in range(len(lst)):
        for end in range(start + 1, len(lst) + 1):
            sublist = lst[start:end]
            negative_count = sum(1 for x in sublist if x < 0)
            
            if negative_count > max_negatives:
                max_negatives = negative_count
                max_interval = (start, end)
                
    return max_interval

# Encontra o intervalo com a maior quantidade de números negativos
start, end = find_interval_with_most_negatives(original_list)

# Deleta o intervalo da lista
del original_list[start:end]

print("Lista editada:", original_list)
