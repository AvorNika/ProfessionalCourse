# функция, выводящая все переданные в неё аргументы с указанием их типов
def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    sorted_list = sorted(kwargs)
    for key in sorted_list:
        print(key, kwargs[key], type(kwargs[key]))


print(print_given())
