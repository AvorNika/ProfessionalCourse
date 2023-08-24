# программа, выводящая бассейн из файла json с наиболее подходящими характеристиками
with open('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/pools.json', encoding='utf-8') as file:
    import json
    from datetime import datetime, time
    data = json.load(file)
    result_length = 0
    result_width = 0
    result_address = ''

    for elem in data:
        start_hour = datetime.strptime(elem['WorkingHoursSummer']['Понедельник'][:5], '%H:%M')
        finish_hour = datetime.strptime(elem['WorkingHoursSummer']['Понедельник'][6:], '%H:%M')
        if start_hour.time() <= time(10, 0, 0) and finish_hour.time() >= time(12, 0, 0):
            if elem['DimensionsSummer']['Length'] >= result_length:
                result_length = elem['DimensionsSummer']['Length']
                result_width = elem['DimensionsSummer']['Width']
                result_address = elem['Address']

    print(f'{result_length}x{result_width}')
    print(result_address)