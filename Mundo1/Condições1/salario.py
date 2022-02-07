salario = float(input('Digite o valor do seu salário atual: '))

if salario > 1250:
    print('Seu aumento é de 10%, ficando um total de R${:.2f} mensais'.format(salario+(salario*0.1)))
else:
     print('Seu aumento é de 15%, ficando um total de R${:.2f} mensais'.format(salario+(salario*0.15)))