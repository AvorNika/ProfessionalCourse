# программа, выводящая имя победителя в игре, в которой игроки вытаскивают по очереди произвольное кол-во предметов. Побеждает тот, кто вытащит последним чётное кол-во предметов
import sys
items = [int(i) for i in sys.stdin.readlines()]
if len(items) % 2 == 1:
    if items[-1] % 2 == 0:
        print('Анри')
    else:
        print('Дима')
else:
    if items[-1] % 2 == 0:
        print('Дима')
    else:
        print('Анри')