# программа, определяющая минимальное время выполнения функций
import time


def for_and_append():                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result
        

def list_comprehension():                        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]



start_1 = time.monotonic()
result_1 = for_and_append()
end_1 = time.monotonic()
elasted_time_1 = end_1 - start_1


start_2 = time.monotonic()
result_2 = list_comprehension()
end_2 = time.monotonic()
elasted_time_2 = end_2 - start_2

if elasted_time_1 > elasted_time_2:
    print('for and append')
else:
    print('list_comrehension')