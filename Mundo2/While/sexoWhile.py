sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, Digite seu sexo: [M/F]')).strip().upper()[0]
print('Sexo {} Registrado com Sucesso'.format(sexo))