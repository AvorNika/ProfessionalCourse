# программа, выводящая заведение каждого типа с наибольшим кол-вом посадочных мест
with open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/food_services.json', encoding='utf-8') as file:
    import json
    data = json.load(file)

    objects = []
    result = {}

    for elem in data:
        if elem['TypeObject'] not in objects:
            objects.append(elem['TypeObject'])
            obj = {}
            obj['name'] = elem['Name']
            obj['count'] = int(elem['SeatsCount'])
            result[elem['TypeObject']] = obj

        else:
            if result[elem['TypeObject']]['count'] < int(elem['SeatsCount']):
                result[elem['TypeObject']]['count'] = int(elem['SeatsCount'])
                result[elem['TypeObject']]['name'] = elem['Name']

    objects.sort()

    for object in objects:
        print(f'{object}: {result[object]["name"]}, {result[object]["count"]}')
