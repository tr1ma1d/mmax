test_string = '''
4
4
Хоббит
Алиса в стране чудес
Том Сойер
Остров сокровищ
Буратино
Хоббит
Остров сокровищ
Война и мир
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

books_count = int(input())
take_count_books = int(input())

set_library = set() 

for i in range(books_count):
    name_book = input()
    set_library.add(name_book)


print("--------Take a book------")
for i in range(take_count_books):
    name_book = input()
    if name_book in set_library:
        print("YES")
    else:
        print("No")