# программа, вычисляющая контрольную сумму из полученного файла и сравнивающая ее с заданным числом
import pickle
filename = input()
res_sum = int(input())

with open(filename, 'rb') as file:
    data = pickle.load(file)
    if isinstance(data, list):
        new_data = list(filter(lambda x: x if isinstance(x, int) else None, data))
        if new_data:
            my_res_sum = min(new_data) * max(new_data)
        else:
            my_res_sum = 0

    else:
        new_data = list(filter(lambda x: x if isinstance(x, int) else None, data.keys()))
        if new_data:
            my_res_sum = sum(new_data)
        else:
            my_res_sum = 0

    if res_sum == my_res_sum:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')
       