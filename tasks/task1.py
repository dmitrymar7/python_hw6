# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#Используется list comprehension, lambda, reduce

from functools import reduce
def task1():
    num = input("Введите число: ")
    lst = [int(i) for i in num if i.isdigit()]
    if len(lst) < 1:
        return
    sum_el = reduce(lambda x, y:  x + y, lst)
    print(sum_el)
task1()