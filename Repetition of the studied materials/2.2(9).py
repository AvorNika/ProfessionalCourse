# программа, подсчитывающая общий объем файлов, указанных в файле, и вывоядщая их блоками в зависимости от расширения
with open('files.txt', 'r', encoding='utf-8') as file:
    info = []
    for line in file:
        info.append(line.rstrip().split())

    for i in info:
        if i[2] == 'MB':
            i[1] = int(i[1]) * 1024 ** 2
            i[2] = 'B'
        if i[2] == 'KB':
            i[1] = int(i[1]) * 1024 ** 1
            i[2] = 'B'
        if i[2] == 'GB':
            i[1] = int(i[1]) * 1024 ** 3
            i[2] = 'B'

    my_dict = {}
    for j in info:
        if j[0][j[0].rindex('.'):] not in my_dict:
            my_dict[j[0][j[0].rfind('.'):]] = [(j[0], j[1])]
        else:
            my_dict[j[0][j[0].rfind('.'):]] = my_dict[j[0][j[0].rfind('.'):]] + [(j[0], j[1])]

    result = {}
    for key, value in my_dict.items():
        counter = 0
        my_list = []
        for elem in value:
            my_list.append(elem[0])
            counter += int(elem[1])
        c = 0
        while int(counter) > 1024:
            counter /= 1024
            c += 1
        res = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
        result[key] = (counter, res[c], sorted(my_list))

    new_res = sorted(result.items())
    for r in new_res:
        print(*r[1][2], sep='\n')
        print('-' * 10)
        print(f'Summary: {round(r[1][0])} {r[1][1]}')
        print()
