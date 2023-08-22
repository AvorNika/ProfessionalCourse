# программа, создающая csv файл с информацией о студентах старше 18 лет с прогрессом по курсу более 75 %
with open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/students.json', encoding='utf-8') as r_file, open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/data.csv', 'w', encoding='utf-8') as w_file:
    import json
    import csv
    r_data = json.load(r_file)
    w_data = []
    names = []
    for elem in r_data:
        new_elem = {}
        if elem['age'] >= 18 and elem['progress'] >= 75:
            new_elem['name'] = elem['name']
            new_elem['phone'] = elem['phone']
            names.append(elem['name'])
        else:
            continue
        w_data.append(new_elem)

    columns = ['name', 'phone']
    names.sort()
    result = []

    for name in names:
        for w_elem in w_data:
            if w_elem['name'] == name:
                result.append(w_elem)

    writer = csv.DictWriter(w_file, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for row in result:
        writer.writerow(row)