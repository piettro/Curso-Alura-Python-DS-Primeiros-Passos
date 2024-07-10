age = 5
print(age)

age = 10
print(age)

age:int = 5
pi:float = 3.14
name:str = 'Piettro'
is_bool:bool = True

print(age, pi, name, is_bool)
print(type(age), type(pi), type(name), type(is_bool))

q_security = 5
s_security = 3000

q_teacher = 16
s_teacher = 6000

q_director = 1
s_director = 12500

total_employees = q_security + q_teacher + q_director
diff_salary = s_director - s_security
mean = (q_security*s_security + q_teacher*s_teacher + q_director*s_director) / (total_employees)

print(f'Total employees {total_employees}')
print(f'Diff salary {diff_salary}')
print(f'Mean {mean}')

full_name = 'piettro enrico de farias rodrigues '
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(full_name.replace('de', ''))
print(full_name.strip())

new_name = input('Write your name: ')