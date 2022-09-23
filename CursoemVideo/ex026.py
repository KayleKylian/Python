frase = str(input('Digite uma frase: '))
letra = str(input('Digite uma letra: '))

print(f'''
Sua frase tem: {frase.count(letra)} letras {letra}.
Apareceu a primeira vez na posição: {frase.find(letra)}.
Apareceu a ultima vez na posição: {frase.rfind(letra)}.
''')