# функция, возвращающая функцию с наименьшим временем выполнения
import time


def get_the_fastest_func(funcs, arg):
    result_time = []
    for func in funcs:
        start_time = time.monotonic()
        x = func(arg)
        end_time = time.monotonic()
        elasted_time = end_time - start_time
        result_time.append(elasted_time)

    min_time = min(result_time)

    return funcs[result_time.index(min_time)]
