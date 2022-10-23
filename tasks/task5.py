# 5 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

#Предполагаю, что в файле храняться именно индексы элементов масссива, т.е. начиная с 0

#Используется enumerate, map

from random import randint

def task5():
    try:
        n = int(input("Введите количество элементов: "))
    except ValueError:
        print("Введено не целое число")
        return

    if n < 0:
        print("Количество элементов должно быть не отрицательным числом")
        return

    lst = [randint(-n, n) for i in range(n)]
    try:
        with open("file.txt") as input_file:
            lst_index = input_file.read().split()
    except FileNotFoundError:
        print("Файл не найден")
        return


    try:
        lst_index   = list(map(int, lst_index))
    except ValueError:
        print("В файле указаны не корректные значения")
        return    

    prod = None
    for i, value in enumerate(lst_index):
        if i >= len(lst):
            print("Значение некроторых индексов из файла выходят за границы исходного массива")
            return

        if i == 0:
            prod = lst[value]
        else:
            prod *= lst[value]

    print(f"Исходный список: {lst}", f"Позиции элементов: {lst_index}", f"Произведение: {prod}", sep="\n")

task5()