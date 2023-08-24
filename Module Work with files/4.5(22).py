# программа, выводящая имена футболистов в алфавитном порядке, выступающих за Арсенал, из json файлов
from zipfile import ZipFile
import json
with ZipFile('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/data.zip') as zip_file:
    
    
    def is_correct_json(string):
        try:
            json_string = json.loads(string)
            if json_string:
                return json_string
        except json.decoder.JSONDecodeError:
            return None
    

    info = zip_file.infolist()
    result = []

    for i in info:
        with zip_file.open(i) as file:
            try:
                r_file = file.read().decode('utf-8')
            except UnicodeDecodeError:
                continue
            data = is_correct_json(r_file)
            if data is not None:
                    if data['team'] == 'Arsenal':
                        result.append((data['first_name'], data['last_name']))

    for_print = sorted(result, key=lambda x: (x[0], x[1]))

    for p in for_print:
        print(*p)
