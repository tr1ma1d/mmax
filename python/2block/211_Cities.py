test_string = '''
8
Лондон
Париж
Москва
Вашингтон
Берлин
Вена
Мадрид
Рим
Мадрид
'''[1:-1].split('\n')[::-1]

count_cities = int(input('Кол-во городов: '))
my_set = set()


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

for i in range(count_cities):
    city_name = input('Название города: ')
    my_set.add(city_name)


last_city_name = input('Название города: ')
if last_city_name in my_set:
    print("TRY ANOTHER")
else:
    print("OK")