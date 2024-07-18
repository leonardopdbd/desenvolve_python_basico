from datetime import datetime

def exibir_data_hora():
    # Obtendo a data e hora atuais
    agora = datetime.now()
    
    # Formatando a data no formato desejado (dia/mês/ano)
    data_formatada = agora.strftime("Data: %d/%m/%Y")
    
    # Formatando a hora no formato desejado (hora:minuto)
    hora_formatada = agora.strftime("Hora: %H:%M")
    
    # Exibindo a data e hora formatadas
    print(data_formatada)
    print(hora_formatada)

# Chamando a função para exibir a data e hora atuais formatadas
exibir_data_hora()
