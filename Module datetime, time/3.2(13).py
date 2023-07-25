# программа, выводящая введённые даты в порядке их неубывания
from datetime import date
dates = [date.fromisoformat(input()) for _ in range(int(input()))]
dates.sort()
result = list(map(lambda x: x.strftime('%d/%m/%Y'), dates))

print(*result, sep='\n')
