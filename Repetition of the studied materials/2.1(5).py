# функция, принимающая список целых числе и возвращающая список целых чисел с той же чётностью, что и первый элемент исходного списка
def same_parity(numbers):
    new_numbers = list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))
    return new_numbers


print(same_parity([1, 3, 5, 7, 9]))
