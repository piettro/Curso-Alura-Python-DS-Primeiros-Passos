if 2 < 7:
    print(True)
else:
    print(False)

if 2 > 7:
    print(True)
else:
    print(False)

mean = float(input('Write the mean: '))

if mean >= 6.0:
    print('Approved')
else:
    print('Denied') 

mean = float(input('Write the mean: '))

if mean >= 6.0:
    print('Approved')
if 6.0 > mean >= 4.0:
    print('Recovery')
if mean < 4.0:
    print('Denied')

if mean >= 6.0:
    print('Approved')
elif 6.0 > mean >= 4.0:
    print('Recovery')
else:
    print('Denied')

t1 = t2 = True
f1 = f2 = False

if t1 and t2:
  print('Expression True')
else:
  print('Expression False')

if f1 or f2:
  print('Expression True')
else:
  print('Expression False')

if not t1:
  print('Expression True')
else:
  print('Expression False')

if not f1:
  print('Expression True')
else:
  print('Expression False')

list_names = 'José da Silva, Maria Oliveira, Pedro Martins, Ana Souza, Carlos Rodrigues, Juliana Santos, Bruno Gomes, Beatriz Costa, Felipe Almeida, Mariana Fernandes, João Pinto, Luísa Nascimento, Gabriel Souza, Manuela Santos, Thiago Oliveira, Sofia Ferreira, Rafael Albuquerque, Isabella Gomes, Bruno Costa, Maria Martins, Rafaela Souza, Matheus Fernandes, Luísa Almeida, Beatriz Pinto, Mariana Rodrigues, Gabriel Nascimento, João Ferreira, Maria Albuquerque, Felipe Oliveira'

name_1 = 'Mariana Rodrigues'
name_2 = 'Marcelo Nogueira'

if name_1 in list_names:
  print(f'{name_1} is in list')
else:
  print(f'{name_1} is not in list')

if name_2 in list_names:
  print(f'{name_1} is in lis')
else:
  print(f'{name_1} is not in list')