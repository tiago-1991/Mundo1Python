galera = []
pessoa = {}
soma = media = 0 
while True:
    pessoa.clear
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa ['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apeanas M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa ['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N!')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['Idade']>= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')