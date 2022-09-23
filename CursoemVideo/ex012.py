preço = float(input('Qual o preço do produto? R$'))
desc = int(input('Digite o desconto: '))
desconto = preço - (preço * desc / 100)

print(f'O preço de R${preço:.2f} do produto na promoção com desconto de {desc}% custa R${desconto:.2f}.')
