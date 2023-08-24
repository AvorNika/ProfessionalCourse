# программа, выводящая наименование района с наибольшим кол-вом заведений общепита, а также выводящая имя сети заведений с наибольшим кол-вом объектов
with open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/food_services.json', encoding='utf-8') as file:
    import json
    data = json.load(file)
    companies = {}
    districts = {}

    for elem in data:
        districts[elem['District']] = districts.get(elem['District'], 0) + 1
        if elem['OperatingCompany'] != '':
            companies[elem['OperatingCompany']] = companies.get(elem['OperatingCompany'], 0) + 1

    max_company = max(companies.items(), key=lambda x: x[1])
    max_district = max(districts.items(), key=lambda x: x[1])

    print(f'{max_district[0]}: {max_district[1]}')
    print(f'{max_company[0]}: {max_company[1]}')