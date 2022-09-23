dia_alug = int(input('Quantos dias alugado? '))
km_rol = float(input('Quantos Km rodados? '))
preço_dia = 60
preço_km = 0.15
preço = (dia_alug * preço_dia) + (km_rol * preço_km)

print(f'O carro foi alugado por {dia_alug} dias e rodou {km_rol:.0f}Kms, o preço a pagar é: R${preço:.2f}.')
