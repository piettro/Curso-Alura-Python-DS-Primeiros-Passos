record_1 = float(input('Write the 1° record: '))
record_2 = float(input('Write the 2° record: '))

print(f'Mean: {(record_1+record_2)/2}')

counter = 1

while counter <= 10:
    print(counter)
    counter += 1

students = 3

while students >= 1:
    record_1 = float(input('Write the 1° record: '))
    record_2 = float(input('Write the 2° record: '))

    print(f'Student: {students} Mean: {(record_1+record_2)/2}')

    students -= 1

for counter in range(1,11):
  print(counter)

for counter in range(1,4):
    record_1 = float(input('Write the 1° record: '))
    record_2 = float(input('Write the 2° record: '))

    print(f'Student: {students} Mean: {(record_1+record_2)/2}')