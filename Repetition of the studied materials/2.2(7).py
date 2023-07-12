# программа, выводящая схожие слова для заданного слова (совпадает количество и расположение гласных букв)
word = input().lower()
n = int(input())
words_for_check = [input().lower() for _ in range(n)]


def check_word(x):
    check_model = []
    counter = 0
    for elem in x:
        if elem in 'ауоыиэяюёе':
            counter += 1
            check_model.append(counter)
        else:
            check_model.append(0)
    while check_model[-1] == 0:
        del check_model[-1]

    return check_model


result_check_word = check_word(word)
result = []
for w in words_for_check:
    if check_word(w) == result_check_word:
        result.append(w)

print(*result, sep='\n')
