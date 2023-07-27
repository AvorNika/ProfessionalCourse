# программа, определяющая вид прогрессии последовательности
import sys
numbers = [int(i.strip()) for i in sys.stdin.readlines()]
arith_prog = []
geom_prog = []

for i in range(len(numbers) - 1):
    arith_prog.append(numbers[i + 1] - numbers[i])
    geom_prog.append(numbers[i + 1] / numbers[i])

flag_a = True
flag_g = True

for i in range(len(arith_prog) - 1):
    if arith_prog[i] != arith_prog[i + 1]:
        flag_a = False
        break

for j in range(len(geom_prog) - 1):
    if geom_prog[j] != geom_prog[j + 1]:
        flag_g = False
        break

if flag_a:
    print('Арифметическая прогрессия')
elif flag_g:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
