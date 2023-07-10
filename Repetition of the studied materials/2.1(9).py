# функция, возвращающая список анаграмм принимаемого слова
def filter_anagrams(word, words):
    check_word = sorted(word)
    anagrams = [w for w in words if sorted(w) == check_word]
    return anagrams


print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))
