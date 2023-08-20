# программа, преобразующая список спортивных площадок в json-файл с разбивкой по адм. районам
with open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/playgrounds.csv', encoding='utf-8') as r_file, open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/addresses.json', 'w', encoding='utf-8') as w_file:
    import json
    import csv
    r_data = csv.DictReader(r_file, delimiter=';')
    w_data = {}
    for line in r_data:
        w_data.setdefault(line['AdmArea'], {}).setdefault(line['District'], []).append(line['Address'])
        

    json.dump(w_data, w_file, ensure_ascii=False)