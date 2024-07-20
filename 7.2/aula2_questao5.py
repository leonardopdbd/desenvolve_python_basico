import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 2:
            return palavra
        
        # Mantém a primeira e a última letra
        primeira_letra = palavra[0]
        ultima_letra = palavra[-1]
        letras_interiores = list(palavra[1:-1])
        
        # Embaralha as letras interiores
        random.shuffle(letras_interiores)
        
        # Reconstrói a palavra
        palavra_embaralhada = primeira_letra + ''.join(letras_interiores) + ultima_letra
        return palavra_embaralhada
    
    # Divide a frase em palavras, embaralha cada uma e junta de volta
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(p) for p in palavras]
    frase_embaralhada = ' '.join(palavras_embaralhadas)
    
    return frase_embaralhada

# Exemplo de uso
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
