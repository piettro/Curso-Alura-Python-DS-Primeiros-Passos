list_python = ['Fabricio Daniel',9.5,9.0,8.0,True]
print(list_python)
print(f'Name: {list_python[0]}')
print(f'Last Record: {list_python[-1]}')

for i in list_python:
    print(i)

mean = (list_python[1] + list_python[2] + list_python[3]) / 3
print(mean)

print(len(list_python))

print(list_python[1:4])

list_python.append(mean)

new_records_to_list = [10.0,8.0,9.0]
list_python.extend(new_records_to_list)
print(new_records_to_list)

list_python.append(new_records_to_list)
print(new_records_to_list)
list_python.remove(new_records_to_list)
print(new_records_to_list)

dict_python = {
    'key':'value'
}

dict_python = {
    'id': 2000168933,
    'created_day': 25,
    'created_month': 10,
    'class': '2E'
}

print(dict_python)
print(dict_python['id'])

dict_python['class'] = '2G'
print(dict_python)

dict_python['Type'] = 'EAD'
print(dict_python)

dict_python.pop('class')
print(dict_python)

print(dict_python.items())
print(dict_python.keys())
print(dict_python.values())

for key in dict_python.keys():
    print(dict_python[key])

for value in dict_python.values():
    print(value)

for key, value in dict_python.items():
    print(key , value)

sets_python = {'Jetta','Passat','Crossfox','Polo'}
print(sets_python)

for i in sets_python:
    print(i)
