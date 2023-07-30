# программа, подсчитывающая количество доменов электронной почты и выводящая список доменов в порядке возрастания
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/data.csv', encoding='utf-8') as r_file, open('domain_usage.csv', 'w', encoding='utf-8', newline='') as w_file:
    import csv
    data = csv.DictReader(r_file)
    result = {}
    for line in data:
        dom = line['email'][line['email'].index('@') + 1:]
        result[dom] = result.get(dom, 0) + 1

    sorted_domain = sorted(result, key=lambda x: (result[x], x))

    columns = ['domain', 'count']
    writer = csv.writer(w_file)
    writer.writerow(columns)
    for elem in sorted_domain:
        writer.writerow((elem, result[elem]))
