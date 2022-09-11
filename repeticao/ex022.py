#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#https://helpdesk.fapam.edu.br/escoladeeducacao/wp-content/uploads/2020/11/Formula-termo-geral-PA-1024x335.jpg

r = int(input('Digite a razão da PA: '))
a1 = int(input('Digite o 1° termo dessa PA: '))
an = a1 + (11 - 1) * r
for n in range(a1, an, r):
    print(n, end=' → ')
