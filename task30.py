# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def ArithmeticProgression(firstElement):
    step = int(input("Введите размер шага: "))
    size = int(input("Введите количество элементов: "))
    for i in range(1, size + 1):
        array.append(firstElement + (i - 1) * step)


firstElement = int(input("Введите первый элемент: "))
array = []
ArithmeticProgression(firstElement)
print(array)