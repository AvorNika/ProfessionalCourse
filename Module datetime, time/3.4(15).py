# программа, выводящая предыдущую и следующую дату для вводимого числа
from datetime import datetime, timedelta
date_input = datetime.strptime(input(), '%d.%m.%Y')
prev_date = date_input - timedelta(days=1)
next_date = date_input + timedelta(days=1)
print(prev_date.date().strftime('%d.%m.%Y'))
print(next_date.date().strftime('%d.%m.%Y'))
