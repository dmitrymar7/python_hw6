# 4 Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#Используется map, filter, lambda

import decimal
def fractional_part(num):
    lst_num = str(num).split(".")
    if len(lst_num) < 2:
        return 0
    res = decimal.Decimal(f"0.{lst_num[1]}")
    return res


def task4():
    '''Исходя из примера учитываются только дробные части, при этом знак не учитывются
    целые числа (т.е. числа с нулевой дробной частью)'''
    lst = [1.1, 1.2, 3.1, 5, 10.01]
    lst_frac_part = list(map(fractional_part, lst))
    lst_frac_part = list(filter(lambda x: abs(x) > 0, lst_frac_part))
    min_el = min(lst_frac_part)
    max_el = max(lst_frac_part)
    diff = max_el - min_el
    print(f"{lst} => {diff}")


task4()