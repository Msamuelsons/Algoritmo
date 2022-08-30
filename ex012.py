'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

valorHoraTrabalho = float(input())
qtdHoraTrabalho = int(input())

salarioBruto = valorHoraTrabalho * qtdHoraTrabalho


descontoIR = salarioBruto

if salarioBruto <= 900:
    descontoIR*= 0
elif salarioBruto <= 1500:
    descontoIR*= 0.95
elif salarioBruto <= 2500:
    descontoIR*= 0.90
else:
    descontoIR *= 0.80

impostoRenda = salarioBruto - descontoIR
inss = salarioBruto * 0.1
fgts = salarioBruto * 0.11
totDescontos= inss + impostoRenda
salarioLiquido = salarioBruto - totDescontos

print(
    f"\nSalário Bruto: R${salarioBruto:.2f}",
    f"\n(-) IR (5%): R${impostoRenda:.2f}",
    f"\n(-) INSS ( 10%): R${inss:.2f}",
    f"\nFGTS (11%): R${fgts:.2f}",
    f"\nTotal de descontos: R${totDescontos:.2f}",
    f"\nSalário Liquido   : R${salarioLiquido:.2f}",

)