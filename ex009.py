#Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for i in range(3):
    numeros = float(input())
    lista.append(numeros)

lista.sort(reverse=True)


print(" → ".join(map(str,lista)), ' Ordem decrescente')