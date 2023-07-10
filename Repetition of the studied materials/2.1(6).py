# функция, проверяющая корректность pin-кода
def is_valid(string):
    return 4 <= len(string) <= 6 and string.isdigit()


print(is_valid('aaaa'))
