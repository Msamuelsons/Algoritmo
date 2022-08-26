#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letter = input().lower()

if letter.isalpha():
    if letter == 'a':
        print('Vogal')
    elif letter == 'e':
        print('Vogal')
    elif letter == 'i':
        print('Vogal')
    elif letter == 'o':
        print('Vogal')
    elif letter == 'u':
        print('Vogal')
    else:
        print('Consoante')
else:
    print('Não é letra!')