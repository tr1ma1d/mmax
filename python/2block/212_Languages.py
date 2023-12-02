test_string = '''
3
3
Иванов
Петров
Васечкин
Иванов
Петров
Васечкин
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

eng_count = int(input('Английский изучают: '))
germ_count = int(input('Немецкий изучают: '))

eng_class = set()
germ_class = set()


for i in range(eng_count + germ_count):
    lastname = input("Lastname: ")
    if lastname is not eng_class:
        eng_class.add(lastname)
    else:
        germ_class.add(lastname)

result = len(eng_class.difference(germ_class))

if result:
    print(f'Кол-во учеников изучающие только один предмет "{result}"')
else:
    print('NO')

