from time import sleep
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

opc = 0
while opc != 5:
   print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair''')
   opc = int(input('Digite sua opção: '))
   if opc == 1:
       print('{} + {} = {}'.format(num1, num2,num1+num2))
   elif opc == 2:
        print('{} x {} = {}'.format(num1, num2,num1*num2))
   elif opc == 3:
       if num1 > num2:
          maior = num1
       else:
          maior = num2
       print('Entre {} e {}, o maior valor é {}'.format(num1,num2,maior))
   elif opc == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
   elif opc == 5:   
        print('FINALIZANDO O PROGRAMA....')  
   else:
      print('Opção Inválida')
   print('=-='*10)
   sleep(2)
print('Fim do Programa. Volte Sempre!')
            