peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é de {:.2f}, estando Abaixo do Peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.2f}, estando no Peso Ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.2f}, estando em Sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.2f}, configurando Obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.2f}, configurando Obesidade Morbida.'.format(imc))
