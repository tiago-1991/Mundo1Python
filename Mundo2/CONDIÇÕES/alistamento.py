from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'. format(nascimento,idade,atual))

sexo = str(input('Qual seu sexo?\nResponda M para Masculino ou F para Feminino'))
sexo = sexo.upper()
if sexo == 'M':

    if idade > 18:
        saldo = idade - 18 
        ano = atual - saldo
        print('Você deveria ter se alistado em {}\nEstá {} anos atrasado.'.format(ano, saldo))
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Você deverá se alistar em {}\nFaltam {} anos para isso.'.format(ano, saldo))
    else:
        print('Você deve se alistar IMEDIATAMENTE!')
else:
    print('O alistamento é obrigatório apenas para Homens')