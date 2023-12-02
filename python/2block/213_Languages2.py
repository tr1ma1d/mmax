test_string = '''
2
2
2
Иванов
Петров
Сидоров
Иванов
Петров
Иванов
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

people = set()
pause = set()
n = int(input())
m = int(input())
k = int(input())
cout = 0
for i in range(n + m + k):
    name = input()
    if name in people:
        cout += 1
        pause.add(name)
    people.add(name)
if (n == k == m) and len(people) == n:
    print('NO')
else:
    if len(pause) + cout > 0:
        if ((len(pause) + cout) % 2 != 0):
            print((len(pause) + cout) % 2)
        else:
            print((len(pause) + cout) // 2)
    else:
        print('NO')