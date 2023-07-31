# программа, преобразующая текстовый файл в формат csv
import csv


def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as r_file, open('condensed.csv', 'w', encoding='utf-8') as w_file:
        r_data = csv.reader(r_file)
        obj = []
        w_data = []
        for line in r_data:
            if line[0] not in obj:
                obj.append(line[0])
                w_data.append({id_name: line[0], line[1]: line[2]})
            else:
                w_data[obj.index(line[0])].update({line[1]: line[2]})
        
        columns = w_data[0].keys()

        writer = csv.DictWriter(w_file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(w_data)

    return w_file


# TEST_4:
text = '''ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none'''

with open('data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('data.csv', id_name='ID')

with open('condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())