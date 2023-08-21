# программа, выводящая список файлов из архива с их характеристиками
from zipfile import ZipFile
import datetime
with ZipFile('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/workbook.zip') as zip_file:
    info = zip_file.infolist()
    name_info = list(filter(lambda z: z != '', map(lambda y: y if '/' not in y else y[y.rindex('/')+1:], map(lambda x: x.filename, info))))
    name_info.sort()

    result = {}
    for elem in info:
        if elem.is_dir() != True:
            elem_date = datetime.datetime(int(elem.date_time[0]), int(elem.date_time[1]), int(elem.date_time[2]), int(elem.date_time[3]), int(elem.date_time[4]), int(elem.date_time[5]))
            if '/' in elem.filename:
                result[elem.filename[elem.filename.rindex('/') + 1:]] = {'  Дата модификации файла:': elem_date,
                                                                         '  Объем исходного файла:': f'{elem.file_size} байт(а)',
                                                                         '  Объем сжатого файла:': f'{elem.compress_size} байт(а)'}
            else:
                result[elem.filename] = {'  Дата модификации файла:': elem_date,
                                         '  Объем исходного файла:': f'{elem.file_size} байт(а)',
                                         '  Объем сжатого файла:': f'{elem.compress_size} байт(а)'}
    
    for name in name_info:
        print(name)
        for key, value in result[name].items():
            print(key, value)
        print()
    

