from random import randrange

palavras = []
with open('palavras_senha.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

senha = []
for n in range(12):
    numero = randrange(0, len(palavras))
    senha.append(palavras[numero])

print('-'.join(senha))
#print(*senha, sep='-')
