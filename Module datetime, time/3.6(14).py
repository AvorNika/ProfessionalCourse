# программа, вычисляющая функию с наименьшим временем исполнения
import time
def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable)


iter = range(100_000)
result_time = []
result = []

start_1 = time.perf_counter()
result_1 = for_and_append(iter)
end_1 = time.perf_counter()
result_time.append(end_1 - start_1)
result.append('for_and_append')

start_2 = time.perf_counter()
result_2 = list_comprehension(iter)
end_2 = time.perf_counter()
result_time.append(end_2 - start_2)
result.append('list_comprehension')

start_3 = time.perf_counter()
result_3 = list_function(iter)
end_3 = time.perf_counter()
result_time.append(end_3 - start_3)
result.append('list_function')

print(result[result_time.index(min(result_time))])