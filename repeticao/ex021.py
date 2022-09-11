#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for i in range(1, 7):
    numeros = int(input(f'Digite o {i}° número: ')) 
    if numeros % 2 == 0:
       soma = soma + numeros
print(f'A soma dos numerais pares é {soma}')