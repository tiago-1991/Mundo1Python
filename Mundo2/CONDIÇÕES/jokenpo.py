from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('=='*20)

jogador = int((input('Qual sua opção?')))
print('=='*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Computador = {}\nVocê = {}\nJOGADOR VENCEU'.format(itens[pc],itens[jogador]))
    elif jogador == 2:
        print('Computador = {}\nVocê = {}\nCOMPUTADOR VENCEU'.format(itens[pc],itens[jogador]))
    else:
        print('Jogada Inválida')
elif pc == 1:
    if jogador == 0:
        print('Computador = {}\nVocê = {}\nCOMPUTADOR VENCEU'.format(itens[pc],itens[jogador]))
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Computador = {}\nVocê = {}\nJOGADOR VENCEU'.format(itens[pc],itens[jogador]))
    else:
        print('Jogada Inválida')
elif pc == 2:
    if jogador == 0:
        print('Computador = {}\nVocê = {}\nJOGADOR VENCEU'.format(itens[pc],itens[jogador]))
    elif jogador == 1:
        print('Computador = {}\nVocê = {}\nCOMPUTADOR VENCEU'.format(itens[pc],itens[jogador]))
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')

    


