# программа, выводящая пары ключ: значение json-объекта
import sys
import json

data_json = sys.stdin.read()
data = json.loads(data_json)

for key, value in data.items():
    if isinstance(value, list):
        print(f'{key}:', end=' ')
        print(*value, sep=', ')
    else:
        print(f'{key}: {value}')
