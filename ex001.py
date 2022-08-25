# Faça um Programa que peça dois números e imprima o maior deles.
x = float(input())
y = float(input())


if x > y:
    print(f'O valor {x} > maior que {y}')
elif x < y:
    print(f'O valor {y} > maior que {x}')
else:
    print(f'O valor {x} = {y} são iguais')