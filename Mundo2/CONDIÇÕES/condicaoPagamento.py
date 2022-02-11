preco = float(input('Digite o valor do produto em R$:'))
print('=='*20)
print('1 - Para Pagamento à vista em Dinheiro / Cheque')
print('2 - À vista no Cartão de Crédito')
print('3 - Em até 2x no Cartão')
print('4 - 3x ou mais no Cartão')
print('=='*20)
pagamento = int(input('Qual a Forma de Pagamento?'))

if pagamento == 1:
    precoFinal = preco - (preco * 0.1)
    print('O valor Total é de R${:.2f}, com desconto de R${:.2f}.'.format(precoFinal,preco * 0.1))
elif pagamento == 2:
    precoFinal = preco - (preco * 0.05)
    print('O valor Total é de R${:.2f}, com desconto de R${:.2f}.'.format(precoFinal,preco * 0.05))
elif pagamento == 3:
    print('O valor Total é de R${:.2f}, sem desconto.'.format(preco))
elif pagamento == 4:
    precoFinal = preco + (preco * 0.2)
    print('O valor total é de R${:.2f}, com juros de R${:.2f}.'.format(precoFinal,preco * 0.2))
else:
    print('Opção Inválida')
print('=='*20)    
print('Operação Finalizada!')