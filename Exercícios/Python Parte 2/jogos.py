import adivinhacao
import forca

print('='*30)
print('==Seja bem vindo aos jogos!!==')
print('='*30)
print('')
print('Escolha um: (1)Adivinhação (2)Forca')

jogo = int(input('Escolho: '))

if jogo == 1:
    print('Iniciando o Jogo! \n')
    adivinhacao.jogar()
elif jogo == 2:
    print('Iniciando o Jogo! \n')
    forca.jogar()
    