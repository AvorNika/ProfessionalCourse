# программа, выводящая название файла из архива, имеющего наилучший показатель степени сжатия
from zipfile import ZipFile
with ZipFile('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/workbook.zip') as zip_file:
    info = list(filter(lambda y: y if y.is_dir() == False else None, zip_file.infolist()))
    coef_info = list(map(lambda x: (x.compress_size * 100) / x.file_size, info))
    result = info[coef_info.index(min(coef_info))].filename
    print(result[result.rindex('/') + 1:])