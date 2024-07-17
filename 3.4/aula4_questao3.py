# Loop para solicitar anos até que o usuário decida parar
while True:
    # Solicita ao usuário para inserir um ano
    ano = int(input("Insira um ano (ou 0 para sair): "))
    
    # Verifica se o usuário deseja sair
    if ano == 0:
        break
    
    # Verifica se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Bissexto")
    else:
        print("Não Bissexto")
