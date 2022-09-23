from random import choice

char_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's','t','u','v','w','x','y','z']
char_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']
num_char = ['0','1','2','3','4','5','6','7','8','9']

def escolhe_4_char(primeira_lista, segunda_lista, terceira_lista):
    senha = []
    while len(senha) <= 12:
        listas = [primeira_lista, segunda_lista, terceira_lista] 
        lista_random = choice(listas)
        escolha = choice(lista_random)
        senha.append(escolha)
    return senha

senha = escolhe_4_char(char_lower, char_upper, num_char)

print(''.join(senha))
