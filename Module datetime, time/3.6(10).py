# функция, возвращающая результат вызова функции, передаваемой в нее, и время выполнения этой функции
import time


def calculate_it(func, *args):
    start_time = time.monotonic()
    x = func(*args)
    finish_time = time.monotonic()
    elasted_time = finish_time - start_time
    return x, elasted_time