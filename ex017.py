'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

#https://docs.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year

ano = int(input())


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')