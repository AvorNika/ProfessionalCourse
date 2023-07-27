# программа, меняющая порядок символов в строке на обратный
import sys
data = [line.strip() for line in sys.stdin.readlines()]

for d in data:
    d = d[::-1]
    print(d)