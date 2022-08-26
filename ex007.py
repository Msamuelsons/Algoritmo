#Faça um Programa que leia três números e mostre o maior e o menor deles.

x = float(input())
y = float(input())
z = float(input())

maior = x

if y > x and y > z:
    maior = y
elif z > x and z > y:
    maior = z

menor = x

if y < x and y < z:
    menor = y
elif z < x and z < y:
    menor = z

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')