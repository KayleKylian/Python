real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 5.02
euro = 5.29
iene = 0.039
conversaoRUS = real / dolar
conversaoREUR = real / euro
conversaoRIENE = real / iene

print(f'Com R${real:.2f}, você pode comprar US${conversaoRUS:.2f} ou EUR€{conversaoREUR:.2f')
print(f'Convertendo de real para iene o total será de: JP¥{conversaoRIENE:.2f}')
