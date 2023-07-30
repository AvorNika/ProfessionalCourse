# программа, записывающая в файл последние обновления имени пользователя
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/name_log.csv', encoding='utf-8') as r_file, open('new_name_log.csv', 'w', encoding='utf-8') as w_file:
    import csv
    from datetime import datetime
    data = csv.DictReader(r_file)
    writer = csv.writer(w_file)

    writer.writerow(data.fieldnames)
    result = {}

    for line in data:
        e_mail = line['email']
        date = datetime.strptime(line['dtime'], '%d/%m/%Y %H:%M')
        if e_mail not in result:
            result[e_mail] = line
        else:
            if date > datetime.strptime(result[e_mail]['dtime'], '%d/%m/%Y %H:%M'):
                result[e_mail] = line

    sorted_emails = sorted(result)
    for elem in sorted_emails:
        writer.writerow(result[elem].values())