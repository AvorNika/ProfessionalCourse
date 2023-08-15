# программа, составляющая список стран, исповедующих одну религию
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/countries.json', encoding='utf-8') as r_file, open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/religion.json', 'w', encoding='utf-8') as w_file:
    import json
    r_data = json.load(r_file)
    result = {}
    for line in r_data:
        result[line['religion']] = result.get(line['religion'], []) + [line['country']]

    json.dump(result, w_file) 