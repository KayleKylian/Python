from random import shuffle
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo: '))
a3 = str(input('Digite o nome do terceiro: '))
a4 = str(input('Digite o nome do quarto: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem dos alunos será a seguinte: {lista}.')
