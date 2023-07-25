# программа, сортирующая записи в файле в хронологическом порядке
with open('diary.txt', 'r', encoding='utf-8') as file:
    from datetime import datetime
    data = {}
    for line in file:
        try:
            my_datetime = datetime.strptime(line.rstrip(), '%d.%m.%Y; %H:%M')
            data[my_datetime] = ''
        except ValueError:
            data[my_datetime] += line

new_data = sorted(data)

for d in new_data:
    print(d.strftime('%d.%m.%Y; %H:%M'))
    print(data[d].rstrip())
    print()
