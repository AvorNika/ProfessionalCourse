# программа, удаляющая строки кода, содержащие только комментарии
import sys
code = [line for line in sys.stdin.readlines()]
result = []
for c in code:
    for elem in c:
        if elem == ' ':
            continue
        elif elem == '#':
            break
        else:
            result.append(c)
            break

sys.stdout.writelines(result)