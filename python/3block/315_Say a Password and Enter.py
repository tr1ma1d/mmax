test_string = '''
qwerty
1234
йцукен

'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

def ask_password(_password):
    count = 0
    for i in range(3):
        try_pass = input()
        
        if _password == try_pass:
            print("Пароль принят")
            return
        else:
            count += 1

        if count == 3:
            print("В доступе отказано")
password = "password"
ask_password(password)