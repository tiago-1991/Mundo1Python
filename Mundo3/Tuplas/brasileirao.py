tabela = ('Atlético MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino',
'Fluminense','América MG','Atlético GO','Santos','Ceará','Internacional','São Paulo',
'Athletico PR','Cuiabá','Juventude','Chapecoense','Grêmio','Bahia','Sport')
print(f'Os 5 primeiros colocados foram {tabela[:5]}')
print(f'Os 4 últimos colocados foram {tabela[16:20]}') #[-4:]
print(f'Os Vinte times em ordem alfabética São: {sorted(tabela)}')
print(f'A Chapecoense terminou o campeonato na {tabela.index("Chapecoense")+1}ª Posição')