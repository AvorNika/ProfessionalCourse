# программа, выводящая список файлов из архива, созданных позже 30.11.2021 14:22
from zipfile import ZipFile
with ZipFile('/media/viktoriya/5EC8109F59F51685/PythonProjects/ProfessionalCourse/Module Work with files/workbook.zip') as zip_file:
    info = list(filter(lambda x: x if x.date_time > (2021, 11, 30, 14, 22, 0) else None, zip_file.infolist()))
    name_info = list(map(lambda z: z[z.rindex('/') + 1:] if '/' in z else z, map(lambda y: y.filename, info)))
    print(*sorted(filter(lambda a: a != '', name_info)), sep='\n')