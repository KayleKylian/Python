num = int(input('Digite um número de 0 a 9999: '))
if len(num) > 4:
    print('Esse número é maior que 9999.')

elif len(num) == 4:
    print(f'''Milhar: {num[-4]}
Centena: {num[-3]}
Dezena: {num[-2]}
Unidade: {num[-1]}''')

elif len(num) == 3:
    print(f'''Centena: {num[-3]}
Dezena: {num[-2]}
Unidade: {num[-1]}''')

elif len(num) == 2:
    print(f'''Dezena: {num[-2]}
Unidade: {num[-1]}''')

elif len(num) == 1:
    print(f'Unidade : {num[-1]}')

else:
    print('Esse valor não corresponde ao solicitado')