pessoas = {'nome':'Tiago','sexo': 'M','idade':30}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['sexo']

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')