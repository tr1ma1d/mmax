test_string = '''
привет
-100
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

word = input()
letter_count = int(input())

if (letter_count < 0) or letter_count > len(word):
    print("Ошибка")
else: 
    print(word[letter_count-1])