from math import hypot
ca = float(input('Digite o número do Cateto Adjacente: '))
co = float(input('Digite o número do Cateto Oposto: '))
hipo = hypot(ca, co)

print(f'A hipotenusa dos catetos adjaente {ca} e oposto {co} é: {hipo}')
