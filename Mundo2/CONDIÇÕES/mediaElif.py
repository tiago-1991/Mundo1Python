nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media >= 7:
    print('A média do aluno é {}, Ele está Aprovado!'.format(media))
elif media > 5 and media <= 6.9:  #ou if 7> média >= 5
    print('A média do aluno é {}, Ele está de Recuperação!'.format(media))
else:
    print('A média do aluno é {}, Ele está Reprovado!'.format(media))