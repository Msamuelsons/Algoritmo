print(40 * '*')
print(10 *'*', 'Jogo da adivinhação','*' * 9)
print(40 * '*')

numeroSecreto = 42
chute = int(input('Digite um número: '))
print(f'Você digitou {chute}')

acerto = numeroSecreto == chute
maior = chute > numeroSecreto
menor = chute < numeroSecreto

if acerto:
    print('Você acertou!!!!')
elif maior:
    print(f'O seu chute foi de {chute} passou do número correto {numeroSecreto}')
elif menor:
    print(f'O seu chute foi de {chute} esta antes do número correto {numeroSecreto}')
