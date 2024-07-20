def print_birthdate():
    # Solicita a data de nascimento do usuário
    birthdate = input("Digite uma data de nascimento (dd/mm/aaaa): ")
    
    # Divide a data em dia, mês e ano
    day, month, year = birthdate.split("/")
    
    # Lista dos meses por extenso
    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
              "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    # Converte o mês de string para inteiro e ajusta para índice da lista
    month_index = int(month) - 1
    
    # Recupera o nome do mês correspondente
    month_name = months[month_index]
    
    # Imprime a data com o mês por extenso
    print(f"Você nasceu em {day} de {month_name} de {year}.")

# Chama a função
print_birthdate()
