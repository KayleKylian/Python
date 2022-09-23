from math import ceil
metros = float(input('Digite em metros quadrados a área a ser pintada: '))
tinta = metros / 6
lataGrande = tinta / 18
custoGrande = lataGrande * 80
galaoMenor = tinta / 3.6
custoMenor = galaoMenor * 25
misturado = (custoGrande / 2) + (custoMenor / 2)

print(f'''Você ira pintar uma área de {metros:.0f}m², e precisará de {tinta:.2f} litros de tinta;
Comprando somente latas grandes o custo sera de: R${custoGrande:.2f} para {lataGrande:.0f} latas grandes;
Comprando somente latas pequenas o custo sera de: R${custoMenor:.2f} para {galaoMenor:.0f} galões pequenos;
Comprando galões pequenos e latas grandes o custo sera de: R${misturado:.2f};
Sendo: R${custoGrande / 2:.2f} latas grandes e R${custoMenor / 2:.2f} galões pequenos;
A quantidade de latas grandes será {ceil(lataGrande / 2)} e galões pequenos {ceil(galaoMenor / 2)}.
''')
