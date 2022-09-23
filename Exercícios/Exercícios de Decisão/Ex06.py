num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite mais um número inteiro: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é: {num1}.')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é: {num2}.')
elif num3 > num1 and num3 > num2:
    print(f'O maior número é: {num3}.')

if num1 < num2 and num1 < num3:
    print(f'O menor número é: {num1}.')
elif num2 < num1 and num2 < num3:
    print(f'O menor número é: {num2}.')
elif num3 < num1 and num3 < num2:
    print(f'O menor número é: {num3}.')
