# программа, преобразующая файл формата json, согласно условиям
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/data.json', encoding='utf-8') as r_file, open('updated_data.json', 'w', encoding='utf-8') as w_file:
    import json

    data = json.load(r_file)
    new_d = []
    for line in data:
        if isinstance(line, str):
            new_d.append(line + '!')
        elif isinstance(line, bool):
            new_d.append(not line)
        elif isinstance(line, int):
            new_d.append(int(line) + 1)
        elif isinstance(line, float):
            new_d.append(float(line) + 1)

        elif isinstance(line, list):
            new_d.append(line * 2)
        elif isinstance(line, dict):
            line.setdefault("newkey", None)
            new_d.append(line)
        elif line == 'null':
            continue
    json.dump(new_d, w_file)
