# программа, добавляющая недостающие ключи в инфу о людях
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/people.json', encoding='utf-8') as r_file, open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/updated_people.json', 'w', encoding='utf-8') as w_file:
    import json
    people_keys = set()
    r_data = json.load(r_file)
    w_data = []
    for line in r_data:
        people_keys.update(line.keys())

    for line in r_data:
        new_line = line
        for elem in people_keys:
            new_line.setdefault(elem, None)
        w_data.append(new_line)

    json.dump(w_data, w_file)
    
    