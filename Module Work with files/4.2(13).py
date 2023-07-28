# программа, выводящая список компаний по возрастанию средних зарплат их сотрудников
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/salary_data.csv', encoding='utf-8') as file:
    import csv
    data = csv.DictReader(file, delimiter=';')

    result = {}
    for record in data:
        result[record['company_name']] = result.get(record['company_name'], [0]) + [int(record['salary'])]

    result_for_print = sorted(result, key=lambda x: (sum(result[x]) / len(result[x]), x))
    print(*result_for_print, sep='\n')