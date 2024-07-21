import csv

def processar_arquivo(nome_arquivo):
    """Processa o arquivo CSV e retorna a lista das músicas mais tocadas de 2012 a 2022."""
    musicas_por_ano = {}

    with open(nome_arquivo, mode='r', encoding='latin-1') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        
        for linha in leitor_csv:
            try:
                # Extrai os dados necessários
                nome_musica = linha['track_name'].strip('"')
                artista_nome = linha['artist(s)_name'].strip('"')
                ano_lancamento = int(linha['released_year'])
                streams = int(linha['streams'])
                
                # Verifica se o ano está no intervalo desejado
                if 2012 <= ano_lancamento <= 2022:
                    if ano_lancamento not in musicas_por_ano:
                        musicas_por_ano[ano_lancamento] = [nome_musica, artista_nome, ano_lancamento, streams]
                    else:
                        # Atualiza a música com mais streams
                        musica_atual = musicas_por_ano[ano_lancamento]
                        if streams > musica_atual[3]:
                            musicas_por_ano[ano_lancamento] = [nome_musica, artista_nome, ano_lancamento, streams]
            except ValueError:
                # Ignora linhas com dados inválidos
                continue

    # Ordena a lista por ano
    lista_musicas = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano)]
    
    return lista_musicas

# Nome do arquivo CSV
nome_arquivo = 'spotify-2023.csv'

# Processa o arquivo e imprime a lista de músicas mais tocadas
lista_musicas = processar_arquivo(nome_arquivo)
print(lista_musicas)
