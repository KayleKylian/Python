from random import randrange

def jogar():
    #Variáveis Iniciais.
    tent = 0
    numeros = 0

    #Introdução ao jogo.
    print('='*40)
    print('  Bem vindo ao jogo da adivinhação!!')
    print('='*40)
    print('Selecione uma dificuldade: ')
    print('(1)Facil (2)Médio (3)Difícil')

    #Tentando obter a dificuldade a partir da entrada do usuário.
    try:
        dificult = int(input('Dificuldade: '))
    except (TypeError, ValueError) as err:
        print('Houve um Erro: {0}'.format(err))

    #Definindo a dificuldade assim como definindo o alcance dos números.
    if dificult:
        if dificult == 1:
            tent += 20
            numeros += 300
        elif dificult == 2:
            tent += 10
            numeros += 200
        elif dificult == 3:
            tent += 5
            numeros += 100
        else:
            print('Dificuldade Inválida')
    else:
        print('Digite corretamente')

    #O número aleatório a ser acertado.
    numb = randrange(1, numeros)

    #Dica sobre o alcance dos números aleatórios.
    if numeros == 100:
        print('Digite um número entre 1 à 100!')
    elif numeros == 200:
            print('Digite um número entre 1 à 200!')
    elif numeros == 300:
            print('Digite um número entre 1 à 300!')

    #Pontuação do jogo.
    pontos = 1000

    #Loop confirmando e verificando a resposta do usuário.
    for rodada in range(1, tent + 1):
        #Declarando qual a tentativa e a pontuação.
        print(f'Tentativa {rodada} de {tent}')
        
        #Pede o chute do usuário.
        try:
            chute = int(input('Digite seu número: '))
        except (ValueError, TypeError):
            print('Digite corretamente os valores em inteiros!')
            continue
        
        #Variáveis para descobrir o resultado.
        acerto = numb == chute
        maior = chute > numb
        menor = chute < numb
        
        #Mensagem de verificação
        msg_verify = "Digite um número entre 1 à {}"

        #Verifica o chute do usuário se está no alcance do número secreto.
        if 1 < chute > numeros:
            if numeros == 100: 
                print(msg_verify.format(100))
                continue
            elif numeros == 200:
                print(msg_verify.format(200))
                continue
            elif numeros == 300:
                print(msg_verify.format(300))
                continue
        
        #Mensagem de derrota.
        mensagem_perda = f'''Você perdeu!!\n
        Sua pontuação final foi: {pontos} pontos.\n
        E o número secreto era: {numb}'''

        #Verifica se o número foi o correto ou não, e se não, verifica se é maior ou menor.
        if acerto:
            print(f'Parabéns, você acertou e fez {pontos} pontos!!')
            break
        else:
            if maior:
                print('O número é maior do que o secreto.')
                if rodada == tent:
                    print(mensagem_perda)
            elif menor:
                print('O número é menor do que o secreto.')
                if rodada == tent:
                    print(mensagem_perda)
            else:
                print('O número está errado.')
            perda = abs(numb - chute)
            pontos = pontos - perda

    #Declara o fim de jogo.
    print('Fim de Jogo')
