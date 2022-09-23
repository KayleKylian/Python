salHora = float(input('Digite seu salário por hora: '))
horasMes = int(input('Digite o total de horas trabalhadas no mês: '))
salarioBruto = salHora * horasMes
IR = (salarioBruto * 0.11)
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = IR + INSS + sindicato
salarioLiquido = salarioBruto - descontos

print(f'''Você teve um faturamento bruto de: R${salarioBruto:.2f} nesse mês;\n'
      Seu faturamento líquido (após descontos) foi de: R${salarioLiquido:.2f};\n'
      Seu IR (Imposto de Renda) foi de: R${IR:.2f};\n'
      Seu INSS foi de: R${INSS:.2f};\n'
      O custo do sindicato foi de: R${sindicato:.2f}.''')
