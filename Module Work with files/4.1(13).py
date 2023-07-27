# программа, высчитывающая минимальный, максимальный и средний рост учеников
import sys
length = [int(i) for i in sys.stdin.readlines()]
if length:
    sys.stdout.write(f'Рост самого низкого ученика: {min(length)}\nРост самого высокого ученика: {max(length)}\nСредний рост: {sum(length) / len(length)}')
else:
    print('нет учеников')