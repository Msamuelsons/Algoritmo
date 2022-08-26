#Faça um Programa que leia três números e mostre o maior deles.

x = float(input())
y = float(input())
z = float(input())

if y < x > z:
    print(f'O maior número {x}')
elif x < y > z:
    print(f'O maior número {y}')
elif x < z > y:
    print(f'O maior número {z}')

