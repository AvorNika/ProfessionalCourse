# программа, возвращающая список наиболее популярных языков
n = int(input())
languages = [[lan for lan in input().split(', ')] for _ in range(n)]
dict_with_lang = {}

for i in range(n):
    for elem in languages[i]:
        dict_with_lang[elem] = dict_with_lang.get(elem, 0) + 1

result = sorted(map(lambda y: y[0], filter(lambda x: x[1] == n, dict_with_lang.items())))
if result:
    print(', '.join(result))
else:
    print('Сериал снять не удастся')
