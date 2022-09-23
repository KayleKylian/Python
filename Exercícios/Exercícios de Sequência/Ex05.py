int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real: '))

a = (int1 * 2) * (int2 / 2)
b = (int1 * 3) + real
c = real * 3

print(f'Resultado de a = {a:.2f};\n'
      f'Resultado de b = {b:.2f};\n'
      f'Resultado de c = {c:.2f}.')
