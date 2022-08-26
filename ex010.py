#Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou
#"Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('M-matutino ou V-Vespertino ou N- Noturno. ').lower()

if turno == 'm-matutino' or turno == 'm':
    print('Bom Dia!')
elif turno == 'v-vespertino' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'n-noturno' or turno == 'n':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
