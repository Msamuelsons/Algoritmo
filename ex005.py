#Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

x = float(input())
y = float(input())

media = ( x + y ) / 2

if media == 10:
    print('Aprovado com Distinção') 
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')