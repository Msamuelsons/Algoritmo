#Faça um programa que pergunte o preço de três produtos e 
#informe qual produto você deve comprar, sabendo que a decisão
#é sempre pelo mais barato.

precoProduto_1 = float(input())
precoProduto_2 = float(input())
precoProduto_3 = float(input())

produtoBarato = precoProduto_1

if precoProduto_2 < precoProduto_1 and precoProduto_2 < precoProduto_3:
    produtoBarato = precoProduto_2
elif precoProduto_3 < precoProduto_1 and precoProduto_3 < precoProduto_2:
    produtoBarato = precoProduto_3
    
print(f'O produto mais barato custa {produtoBarato} R$')