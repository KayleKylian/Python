salario_hora = float(input('Quanto você ganha por hora? '))
hora_trabalho = float(input('Quantas horas você trabalhou no mês? '))
mes = str(input('Digite o mês que você trabalhou: '))

salario = salario_hora * hora_trabalho

print(f'Você trabalhou por {hora_trabalho:.0f} horas no mês {mes}, e ganha R${salario_hora:.2f} por hora, como resultado,'
      f' seu salário por mês é: R${salario:.2f}.')
