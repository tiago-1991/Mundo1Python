extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n <0 or n > 20:
    n=int(input('Tente Novamente. Digite um número entre 0 e 20: '))
#while True:
 #n=int(input('Tente Novamente. Digite um número entre 0 e 20: '))
 #if 0<=n <=20:
    #break
#print('Tente Novamente. ', end = '')
 
print(f'Você digitou o número {extenso[n]}')