# функция, принимающая произвольное количество слов и
# возвращающая словарь, ключи которого - первые буквы слов, а значения - максимальная длина слова на эту букву
def spell(*args):
    result = {}
    for arg in args:
        if len(arg) > result.setdefault(arg.lower()[0], 0):
            result[arg.lower()[0]] = len(arg)
    return result


words = ['a', 'ab', 'abc', 'abcd', 'ба', 'аб', 'абвгдеЁёёЁЁжбБбБввВ', 'ёёё', 'Ёаaа']
print(spell(*words))
