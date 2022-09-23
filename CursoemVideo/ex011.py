largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
metragem = altura * largura
tinta = metragem / 2

print(f'Sua parede com a dimensão de {largura}x{altura} e sua área é de {metragem}m².')
print(f'Essa parede com área de {metragem}m² pode ser pintada por {tinta} litros de tinta')
