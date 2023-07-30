# программа, подсчитывающая кол-во точек доступа в разных районах Москвы по списку адресов
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/wifi.csv', encoding='utf-8') as file:
    import csv
    data = csv.DictReader(file, delimiter=';')
    result = {}
    for line in data:
        result[line['district']] = result.get(line['district'], 0) + int(line['number_of_access_points'])

    sorted_dist = sorted(sorted(result), key=lambda x: result[x], reverse=True)
    for elem in sorted_dist:
        print(f'{elem}: {result[elem]}')