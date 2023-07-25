# программа, определяющая, является ли год високосным
import calendar
n = int(input())
years = [int(input()) for _ in range(n)]

for y in years:
    print(calendar.isleap(y))
