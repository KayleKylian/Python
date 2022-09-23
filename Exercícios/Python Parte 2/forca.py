from random import randrange

def jogar():
    mensagem_boas_vindas()
    palavra = escolhe_palavra_secreta()
    letra_acertada = esboço_resposta(palavra)
    chute_digitado = esboço_chute(letra_acertada)
    
    enforcado = False
    acertou = False
    erros = 0
    
    while not enforcado and not acertou:
        chute = pede_chute()
        frase = ''.join(letra_acertada)
        
        if len(chute) == len(palavra) and chute == palavra:
            print('Você Ganhou!!')
            mensagem_vitoria(frase)
            break
        
        chute = verifica_chute(chute)
        
        print('')
        chute_digitado.append(chute)
        
        for n in chute_digitado:
            count = chute_digitado.count(chute)
            if count > 1:
                chute_digitado.remove(chute)
                print('Essa letra já foi digitada.')
                continue
        
        if chute not in palavra:
            print('Essa letra não existe.')
            erros += 1
            desenha_forca(erros)
        else:
            marca_chute_correto(palavra, letra_acertada, chute)
            
        print('Letras digitadas: {}.'.format('-'.join(chute_digitado)))
        
        print(' '.join(frase))

        acertou = frase == palavra
        enforcado = erros == 7
    
    if acertou:
        mensagem_vitoria(frase)
    elif enforcado:
        mensagem_derrota(frase)


def mensagem_boas_vindas():
    print('='*34)
    print('===Bem vindo ao jogo da forca!!===')
    print('='*34)

def mensagem_vitoria(frase):
    print('Parabéns, você ganhou!!')
    print(f'A palavra era: {frase.capitalize()}')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_derrota(frase):
    print('Você foi enfrocado!!')
    print('Tente Novamente')
    print(f'A palavra secreta era: {frase.capitalize()}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def escolhe_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    
    numero = randrange(0, len(palavras))
    palavra = palavras[numero].strip()
    return palavra
    
def esboço_resposta(var):
    return ['_' for letra in var]
    
def esboço_chute(var):
    chute_digitado = list()
    print('A palavra tem {} letras.\n{}'.format(len(var), ' '.join(var)))
    return chute_digitado

def pede_chute():
    chute = input('Digite uma letra: ')
    if not chute:
        print('Digite corretamente o chute')
        return input('Digite uma letra: ')
    else:
        return chute
    
def verifica_chute(chute):
    chute = chute.lower().strip()
    if len(chute) > 1:
        chute = input('Digite somente um caractere: ').lower().strip()
        if len(chute) > 1:
            return input('Digite somente um caractere: ').lower().strip()
        else:
            return chute
    else:
        return chute
    
def marca_chute_correto(palavra, letra_acertada, chute):
    index = 0
    for letra in palavra:
        if chute == letra:
            letra_acertada[index] = chute
        index += 1

if __name__ == '__main__':
    jogar()
