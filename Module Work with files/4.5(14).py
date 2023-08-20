# программа, считающая количество файлов в zip архиве
from zipfile import ZipFile
with ZipFile('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/workbook.zip') as zip_file:
    data = zip_file.infolist()
    counter = 0
    for elem in data:
        if elem.is_dir() is False:
            counter += 1
    print(counter)
