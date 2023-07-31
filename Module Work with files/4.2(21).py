# программа, выводящая упорядоченную информацию о количестве учащихся в школе в разные годы по классам
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/student_counts.csv', encoding='utf-8') as r_file, open('sorted_student_counts.csv', 'w', encoding='utf-8') as w_file:
    import csv
    r_data = csv.DictReader(r_file)
    w_data = []
    for elem in r_data:
        new_info = {'year': elem.pop('year')}
        sorted_elem = sorted(elem, key=lambda x: (int(x[:x.index('-')]), x[-1]))
        for s in sorted_elem:
            new_info[s] = elem[s]

        w_data.append(new_info)

    columns = w_data[0].keys()
    writer = csv.DictWriter(w_file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(w_data)
