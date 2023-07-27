# программа, сортирующая и выводящая новости в порядке увеличения достоверности
import sys
data = [i for i in sys.stdin.readlines()]
category = data.pop(-1).strip()
news = list(filter(lambda y: y[1] == category, map(lambda x: x.split(' / '), data)))

result = sorted(news, key=lambda x: (x[2], x[0]))

for r in result:
    print(r[0])