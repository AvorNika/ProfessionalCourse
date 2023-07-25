# программа, определяющая количество дней в заданном месяце
import calendar
user_info = input().split()
user_year, user_month = int(user_info[0]), list(calendar.month_name).index(user_info[1])

print(calendar.monthrange(user_year, user_month)[1])
