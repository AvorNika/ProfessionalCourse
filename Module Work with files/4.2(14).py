# программа, сортирующая значения в заданном столбце, и выводящая на печать содержимое всей таблицы
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/deniro.csv', encoding='utf-8') as file:
    import csv
    n = int(input())
    info = csv.reader(file)

    result = sorted(info, key=lambda x: int(x[n-1]) if x[n-1].isdigit() else x[n-1])
    for r in result:
        print(*r, sep=',')