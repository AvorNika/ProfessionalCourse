# программа, определяющая, в какую из дат родилось больше всего сотрудников
from datetime import datetime
n = int(input())
data = [input().split() for _ in range(n)]

counter = {}
new_data = list(map(lambda x: [x[0], x[1], datetime.strptime(x[2], '%d.%m.%Y')], data))

for elem in new_data:
    counter[elem[2]] = counter.get(elem[2], 0) + 1


min_len = min(counter.values())
max_len = max(counter.values())
result = []
if min_len == max_len:
    result = counter.keys()
else:
    for key, value in counter.items():
        if value > min_len:
            result.append(key)

result.sort()

for res in result:
    print(res.strftime('%d.%m.%Y'))
