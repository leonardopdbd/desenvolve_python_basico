# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista para armazenar os domínios
dominios = []

# Extrai o nome principal de cada URL
for url in urls:
    dominio = url[4:-4]  # Remove "www." (4 primeiros caracteres) e ".com" (4 últimos caracteres)
    dominios.append(dominio)

# Imprime a lista de domínios
print(dominios)
