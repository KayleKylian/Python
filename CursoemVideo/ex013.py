salario = float(input('Qual é o seu salário? R$'))
aumen = int(input('Quanto é a porcentagem do seu aumento? '))
aumento = (aumen / 100) * salario
novoSalario = salario + aumento

print(f'O novo salário é: R${novoSalario:.2f} com um aumento de R${aumento:.2f}'
      f' com uma porcentagem de {aumen}% do valor inicial de: R${salario:.2f}')
