# программа, выводящая количество дней между максимальной и минимальной датами последовательности
import sys
from datetime import datetime

dates = [datetime.strptime(line.strip(), '%Y-%m-%d') for line in sys.stdin.readlines()]

print((max(dates) - min(dates)).days)
