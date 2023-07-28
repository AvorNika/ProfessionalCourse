# программа, выводящая список товаров, цена на которые уменьшилась
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/sales.csv', encoding='utf-8') as file:
    import csv
    data = csv.DictReader(file, delimiter=';')
    for record in data:
        if int(record['old_price']) > int(record['new_price']):
            print(record['name'])
