test_string = '''
-3
4
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

xcoord, ycoord = int(input()), int(input())

def quarter(xcoord, ycoord):
    quadrant = {
        (1, 1): "Точка находится в первой четверти (I)",
        (-1, 1): "Точка находится во второй четверти (II)",
        (-1, -1): "Точка находится в третьей четверти (III)",
        (1, -1): "Точка находится в четвертой четверти (IV)",
        (0, 1): "Точка лежит на оси OY",
        (1, 0): "Точка лежит на оси OX",
        (0, 0): "Точка совпадает с началом координат"
    }
    position = (1 if xcoord > 0 else -1 if xcoord < 0 else 0, 1 if ycoord > 0 else -1 if ycoord < 0 else 0)
    print(quadrant.get(position, "Некорректные координаты"))

quarter(xcoord, ycoord)