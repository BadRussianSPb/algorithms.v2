# Необходимо сравнить скорость работы 2 алгоритмов вычисления чисел Фибоначчи и определить,
# какой из них работает быстрее. Так различия начнутся уже с 40 члена последовательности.
from math import sqrt
from timeit import timeit


# линейный способ
def fib_var1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        cur_numb = 0
        next_numb = 1
        for i in range(1, n+1):
            next_numb, cur_numb = cur_numb + next_numb, next_numb
        return cur_numb


# формула Бине (не точно уже на 71 числе)
def fib_var2(n):
    spam = (sqrt(5))
    section = ((1 + spam) / 2) ** n
    pairing = ((1 - spam) / 2) ** n
    return round((section - pairing) / spam)


# рекусрсия
def fib_var3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_var3(n - 1) + fib_var3(n - 2)


if __name__ == '__main__':
    attempts = 20
    fib_numb = 25
    print(f'Попыток для числа {fib_numb}:', attempts)
    print('-' * 25)
    for i in range(3):
        print(f'Время на вариант {i+1}: ', round(timeit(f'fib_var{i+1}({fib_numb})',
                                                        number=attempts, globals=globals()), 6) * 100)
