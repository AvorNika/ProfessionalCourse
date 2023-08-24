# программа, выводящая структуру файлов рабочего стола и их объем
from zipfile import ZipFile
with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    last_name = ''
    for elem in info:
        if elem.is_dir():
            if last_name.find(elem.filename[:-1]) == -1:
                
