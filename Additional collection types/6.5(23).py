def flip_dict(dict_of_lists):
    from collections import defaultdict
    data1 = defaultdict(list)
    for key, value in dict_of_lists.items():
        for elem in value:
            data1[elem].append(key)

    return data1



data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')