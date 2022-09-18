#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0
anoAtual = date().today().year
for i in range(1, 5):
    anoNascimento = int(input('Digite o ano de seu nascimento: '))

    if (anoAtual - anoNascimento) > 18:
        maior += 1
    else:
        menor += 1
print(f'Existe {maior} maiores de idade')
print(f'Existe {menor} menores de idade')

