distancia = float(input('Qual a distância da Viagem em Km?'))

if distancia <= 200:
    print('A distância é de {} km. Valor total da passagem: R${:.2f}'.format(distancia,distancia*0.5))
else:
    print('A distância é de {} km. Valor total da passagem: R${:.2f}'.format(distancia,distancia*0.45))
