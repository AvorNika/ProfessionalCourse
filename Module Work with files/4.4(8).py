# программа, объединяющая содержимое двух json файлов
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/data1.json', encoding='utf-8') as file1, open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/data2.json', encoding='utf-8') as file2, open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/data_merge.json', 'w', encoding='utf-8') as w_file:
    import json
    data1 = json.load(file1)
    data2 = json.load(file2)
    data1.update(data2)
    json.dump(data1, w_file)