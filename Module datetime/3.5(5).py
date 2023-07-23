# программа, определяющая самого старшего сотрудника в организации
from datetime import datetime
n = int(input())
data = [input().split() for _ in range(n)]

new_data = sorted(data, key=lambda x: datetime.strptime(x[2], '%d.%m.%Y'))

counter = 1
for i in range(n - 1):
    if new_data[i][2] == new_data[i + 1][2]:
        counter += 1
    else:
         break

if counter == 1:
    print(new_data[0][2], new_data[0][0], new_data[0][1])
else:
     print(new_data[0][2], counter)
