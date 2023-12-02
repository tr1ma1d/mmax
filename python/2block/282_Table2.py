test_string = '''
3
2
тройка
треф
семерка
червей
дама 
пик
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

(n,m) = (int(input()), int(input()))

for i in range(m):
    a = []
    for j in range(n):
        a.append(input())
    print('\t'.join(a))

