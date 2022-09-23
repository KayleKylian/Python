metros = float(input('Digite o tamanho da área a ser pintada: '))
tinta = metros / 3
lata = tinta / 18
custoLata = 80 * lata

print(f'''Uma área de {metros}m² pode ser pintada com {lata:.0f} latas de tinta', com um custo de R${custoLata:.2f}''')
