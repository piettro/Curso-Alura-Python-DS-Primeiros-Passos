import datetime

print('Hello World!')

print(10)

print('Piettro', 23)

print('Escola de Dados da Alura!')

name = 'Piettro'
undername = 'Rodrigues'
print(f'Name: {name} \nUndername: {undername}')

for i in name:
    print(i)

birth_date = datetime.datetime(2001, 11, 13)

print(birth_date)
print(f'Current Year: {datetime.datetime.now().year}')