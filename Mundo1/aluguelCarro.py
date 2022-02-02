km = float(input('Digite a quantidade de Km rodados pelo carro:'))
dias = int(input('Digite a quantidade de dias em que o carro ficou alugado:'))

calcKm = km*0.15
calcDias = dias*60
aPagar = calcKm+calcDias

print('Valor Kilometragem = R${:.2f}\nValor por dias alugados = R${:.2f}\nValor Total a Pagar = R${:.2f}'
.format(calcKm,calcDias,aPagar))