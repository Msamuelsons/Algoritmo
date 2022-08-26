#Faça um Programa que verifique se uma letra 
#digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino, M - Masculino, Sexo Inválido.


letra = input('F or M ? ').lower()

if letra == 'm':
    print('M - Masculino')
elif letra == 'f':
    print('F - Feminino')
else:
    print('Sexo Inválido')
