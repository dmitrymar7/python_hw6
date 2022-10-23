# 6 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

#Используется zip

def prod_pars(lst:list):
    middle = len(lst) // 2
    lst1 = lst[: middle]
    lst2 = lst[middle:]
    lst2.reverse()
    if len(lst) % 2 != 0:
        lst1.append(lst2[-1])
    lst3 = [x * y for x, y in zip(lst1, lst2)]
    return lst3

def task6():
    lst = [2, 3, 4, 5, 6]
    res = prod_pars(lst)
    print(f"{lst} => {res}")

    lst = [2, 3, 5, 6]
    res = prod_pars(lst)
    print(f"{lst} => {res}")


task6()