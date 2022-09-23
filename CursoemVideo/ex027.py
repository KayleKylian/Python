nome = str(input('Digite seu nome: '))
nomeDiv = nome.split()

print(f'''Seu nome é: {nome}
Seu primeiro nome é: {nomeDiv[0]}
Seu último nome é: {nomeDiv[-1]}
''')