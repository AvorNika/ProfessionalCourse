# программа, подсчитывающая объем файлов, содержащихся в zip-архиве
from zipfile import ZipFile
with ZipFile('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/workbook.zip') as zip_file:
    info = zip_file.infolist()
    all_file_size = 0
    all_compress_size = 0
    for elem in info:
        all_file_size += elem.file_size
        all_compress_size += elem.compress_size
    print(f'Объем исходных файлов: {all_file_size} байт(а)\nОбъем сжатых файлов: {all_compress_size} байт(а)')