# программа, выводящая календарь на заданные год и месяц
import calendar
data = input().split()
user_year = int(data[0])
user_month = list(calendar.month_abbr).index(data[1])

calendar.prmonth(user_year, user_month)
