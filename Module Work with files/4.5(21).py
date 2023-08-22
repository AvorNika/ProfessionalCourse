# функция, извлекающая из архива заданные файлы
from zipfile import ZipFile
def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            for arg in args:
                zip_file.extract(arg)
        else:
            zip_file.extractall()