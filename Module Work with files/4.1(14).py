# программа, подсчитывающая количество строк-комментариев в коде
import sys
code = [line.strip() for line in sys.stdin.readlines()]
counter = 0
for c in code:
    if c[0] == '#':
        counter += 1

print(counter)