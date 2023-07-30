# программа, выводящая список выживших на Титанике
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/titanic.csv', encoding='utf-8') as file:
    import csv
    data = csv.DictReader(file, delimiter=';')
    men = []
    women = []
    for line in data:
        if line['survived'] == '1' and float(line['age']) < 18:
            if line['sex'] == 'male':
                men.append(line['name'])
            else:
                women.append(line['name'])

    print(*men, sep='\n')
    print(*women, sep='\n')
