# программа, выводящая наименование самого дешевого продукта и название магазина, в котором он продаётся
with open('/home/viktoriya/Документы/PythonProjects/ProfessionalCourse/Module Work with files/prices.csv', encoding='utf-8') as file:
    import csv
    data = csv.DictReader(file, delimiter=';')
    min_price = 1000000
    min_grocery = 'яяяяя'
    min_store = 'яяяяя'

    for elem in data:
        store = elem.pop('Магазин')
        min_elem = min(elem, key=lambda x: (int(elem[x]), x.lower()))
        if int(elem[min_elem]) < min_price:
            min_price = int(elem[min_elem])
            min_grocery = min_elem
            min_store = store
        elif int(elem[min_elem]) == min_price:
            if min_elem < min_grocery:
                min_grocery = min_elem
            elif min_elem == min_grocery:
                if store < min_store:
                    min_store = store
    
    print(f'{min_grocery}: {min_store}')