# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def IndexSearch(elements, indices, _min, _max):
    for i in range(len(elements)):
        if _max >= elements[i] and _min <= elements[i]:
            indices.append(i)


elements = list(map(int, input("Введите элементы через пробел: ").split()))
_min = int(input("Введите минимальное значение элемента: "))
_max = int(input("Введите максимальное значение элемента: "))
indices = []
IndexSearch(elements, indices, _min, _max)
print(f"Элементы массива:\n {elements}")
print(
    f"Индексы элементов, лежащих в диапозоне от {_min} до {_max}:\n", indices)