sex = str(input('Digite seu sexo (Masculino ou Feminino): ')).strip()

if 'M' in sex[0] or 'm' in sex[0]:
    print(f'Você é Masculino.')
elif 'F' in sex[0] or 'f' in sex[0]:
    print(f'Você é Feminino.')
else:
    print(f'Sexo Inválido.')
