# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

#Используется dictionary comprehension

def task3():
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Введено не целое число")
        return
    d = {i : round((1 + (1 / i)) ** i, 2) for i in range(1, n + 1)}
    sum_values = sum(d.values())
    print(f"Последовательность: {d}", f"Сумма: {sum_values}", sep="\n")
task3()