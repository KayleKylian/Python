a = str(input('Digite um caractere: ')).strip().lower()

if len(a) != 1:
    print(f'Erro de digitação')
elif len(a) == 1 and a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print(f'A letra escrita é uma vogal.')
elif a != 'a' or a != 'e' or a != 'i' or a != 'o' or a != 'u':
    print(f'A letra escrita é uma consoante.')
