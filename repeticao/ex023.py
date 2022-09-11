#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input())

count = 0

for c in range(1, num + 1):
    if num % c == 0:
        count = count + 1
if count > 2:
    print('Não é primo', count)
else:
    print('É primo', count)