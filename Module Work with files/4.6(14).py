# функция, принимающая три аргумента и возвращающая pickle файл с сериализованным списком объектов с заданным типом данных
def filter_dump(filename, objects, typename):
    import pickle
    with open(filename, 'wb') as file:
        result_obj = list(filter(lambda x: isinstance(x, typename) is True, objects))
        return pickle.dump(result_obj, file)