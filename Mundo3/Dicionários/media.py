boletim = {}

boletim ['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))

if boletim['Média'] >= 7:
    boletim['Situação'] = 'APROVADO'
elif boletim['Média'] >= 5 and boletim['Média'] < 7:
    boletim['Situação'] = 'RECUPERAÇÃO'
else:
    boletim['Situação'] = 'REPROVADO'

print('-='*30)
for k, v in boletim.items():
    print(f'    - {k} é igual a {v}')