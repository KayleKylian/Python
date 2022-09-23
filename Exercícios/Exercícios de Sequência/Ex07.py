peso = float(input('Digite o peso da carga: '))
excesso = peso - 50
multa = excesso * 4.00

print(f'O peso total da carga é: {peso:.2f}kg, com o excesso sendo: {excesso:.2f}kg, '
      f'e a multa resultante sendo de: R${multa:.2f}.')
