velocidade = float(input('Digite a Velocidade do Veículo: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Sua velocidade de {:.1f} km/h superou o limite de velocidade. Você foi Multado !'.format(velocidade))
    print('Sua Multa é no valor de R${:.2f}. Custando R$7.00 por km acima do limite'.format(multa))
else:
    print('Você está há {:.1f} km/h, dentro do limite de velocidade.'.format(velocidade))