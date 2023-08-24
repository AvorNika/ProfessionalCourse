# программа, выводящая информацию о максимальной оценке студентов на экзаменах и пересдачах
with open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/exam_results.csv', encoding='utf-8') as r_file, open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/best_scores.json', 'w', encoding='utf-8') as w_file:
    import csv
    import json
    from datetime import datetime
    r_data = csv.DictReader(r_file)
    w_data = []
    emails = []
    for elem in r_data:
        if elem['email'] not in emails:
            info_student = {}
            emails.append(elem['email'])
            info_student['name'] = elem['name']
            info_student['surname'] = elem['surname']
            info_student['best_score'] = int(elem['score'])
            info_student['date_and_time'] = elem['date_and_time']
            info_student['email'] = elem['email']
            w_data.append(info_student)

        else:
            for w_elem in w_data:
                if w_elem['email'] == elem['email']:
                    if int(w_elem['best_score']) < int(elem['score']):
                        w_elem['best_score'] = int(elem['score'])
                        w_elem['date_and_time'] = elem['date_and_time']
                    elif int(w_elem['best_score']) == int(elem['score']):
                        w_elem_datetime = datetime.strptime(w_elem['date_and_time'], '%Y-%m-%d %H:%M:%S')
                        elem_datetime = datetime.strptime(elem['date_and_time'], '%Y-%m-%d %H:%M:%S')
                        if w_elem_datetime < elem_datetime:
                            w_elem['date_and_time'] = elem['date_and_time']
                        
    emails.sort()
    result = []

    for email in emails:
        for w_el in w_data:
            if w_el['email'] == email:
                result.append(w_el)

    json.dump(result, w_file)