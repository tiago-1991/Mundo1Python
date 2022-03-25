'''aula = []
aula.append('Tiago')
aula.append(30)

galera = []
galera.append(aula[:])
aula[0] = 'Bena'
aula[1] = 31
galera.append(aula)
print(galera)
'''
galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]

#print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')


