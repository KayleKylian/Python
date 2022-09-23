nome = str(input('Digite seu nome completo: ')).strip()
nomeDividido = nome.split()
print(f"""Seu nome completo é: {nome}
Seu primeiro nome é: {nomeDividido[0]} 
E tem: {len(nomeDividido[0])} carâcteres
Nome maiúsculo: {nome.upper()}
Nome minúsculo: {nome.lower()}
Seu nome tem: {len(nome.replace(' ', ''))} carâcteres.""")
