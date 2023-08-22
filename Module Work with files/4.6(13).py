# программа, выводящая значение функции, содержащейся в pickle-файле
import sys
import pickle
filename = input()
args_for_func = [str(elem.rstrip()) for elem in sys.stdin]

with open(filename, 'rb') as file:
    func_from_file = pickle.load(file)
    print(func_from_file(*args_for_func))
