# функция, преобразующая регистр строки в зависимости от количества строчных и прописных букв в ней
def convert(string):
    counter_letters = 0
    counter_upper_letters = 0
    for char in string:
        counter_letters += char.isalpha()
        counter_upper_letters += char.isupper()
    if counter_upper_letters > counter_letters // 2:
        return string.upper()
    else:
        return string.lower()


print(convert('dEfAbC'))
