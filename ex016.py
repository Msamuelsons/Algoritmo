'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma 
ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
'''
a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c

x1 = (-1 * b + delta ** 0.5) / 2 * a
x2 = (-1 * b - delta ** 0.5) / 2 * a

if a == 0:
    print('A equação não é do segundo grau ')
elif delta < 0:
    print('A equalção não é real')
elif delta == 0:
    print(f'A raíz da equalção é: {x1}')
else:
    print(f'X1: {x1}\nX2: {x2}')
