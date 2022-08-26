#As Organizações Tabajara resolveram dar um aumento de salário aos seus 
#colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
#seguinte critério, baseado no salário atual:

''' 
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salarioColaborador = float(input())

aumento = salarioColaborador

if  0 < salarioColaborador <= 280:
    print('O percentual de aumento aplicado foi de 20%')
    aumento *= 1.2
elif 280 < salarioColaborador <= 700:
    print('O percentual de aumento aplicado foi de 15%')
    aumento *= 1.15
elif 700 < salarioColaborador <= 1500:
    print('O percentual de aumento aplicado foi de 10%')
    aumento *= 1.1
elif salarioColaborador > 1500:
    print('O percentual de aumento aplicado foi de 5%')
    aumento *= 1.05

print(f'O salário antes do reajuste {salarioColaborador}')
print(f'O valor do aumento {aumento - salarioColaborador}')
print(f'O novo salário {aumento}')

