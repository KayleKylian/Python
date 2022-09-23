from random import choice
a1 = str(input('Digite o nome do primeiro aluno a ser sorteado: '))
a2 = str(input('Digite o segundo: '))
a3 = str(input('Digite o terceiro: '))
a4 = str(input('Digite o quarto: '))
sorteio = choice([a1, a2, a3, a4])

print(f'Entre os alunos sorteados, o escolhido foi {sorteio}.')
