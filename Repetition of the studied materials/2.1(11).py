# функция, возвращающая из списка исходных чисел индекс ближайшего по значению числа к заданному числу
def index_of_nearest(numbers, number):
    new_numbers = list(map(lambda x: abs(x-number), numbers))
    if new_numbers:
        return new_numbers.index(min(new_numbers))
    else:
        return -1


print(index_of_nearest([1, 1, 1, 1, 1], 1))
