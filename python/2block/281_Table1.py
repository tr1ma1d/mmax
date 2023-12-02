test_string = '''
3
2
тройка
треф
семёрка
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


n = int(input('Введите число'))
m = int(input('Введите число')) 

words = [] 
for _ in range(n):
    words.extend(input()) 

for i in range(n):
    for j in range(m):
        print(words[i * m + j], end="\t") 
    print() 