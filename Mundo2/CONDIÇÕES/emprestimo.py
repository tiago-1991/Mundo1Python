
# Online Python - IDE, Editor, Compiler, Interpreter
casa = float(input('Qual o valor da Casa?'))
salario = float(input('Qual o seu salário?'))
anos = int(input('Irá pagar o empréstimo em quantos anos?'))

prestacao = casa / (anos*12)

if prestacao > salario * 0.3:
    print('Infelizmente não podemos aprovar seu empréstimo pois a parcela de R${:.2f} excede seu limite de crédito'.format(valorParcela))
else:
    print('A parcela mensal ficará em R${:.2f} dividido em {} parcelas'.format(prestacao,(anos*12)))
