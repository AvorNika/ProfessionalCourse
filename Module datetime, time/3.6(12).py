# программа, вычислящая наименьшее время вычисления факториала числа
from math import factorial
import time


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


n = int(input())
result_time = []
result = []

start_time_1 = time.monotonic()
result_1 = factorial(n)
end_time_1 = time.monotonic()
elasted_time_1 = end_time_1 - start_time_1
result_time.append(elasted_time_1)
result.append(result_1)


start_time_2 = time.monotonic()
result_2 = factorial_recurrent(n)
end_time_2 = time.monotonic()
elasted_time_2 = end_time_2 - start_time_2
result_time.append(elasted_time_2)
result.append(result_2)

start_time_3 = time.monotonic()
result_3 = factorial_classic(n)
end_time_3 = time.monotonic()
elasted_time_3 = end_time_3 - start_time_3
result_time.append(elasted_time_3)
result.append(result_3)

print(min(result_time), result_time.index(min(result_time)))
