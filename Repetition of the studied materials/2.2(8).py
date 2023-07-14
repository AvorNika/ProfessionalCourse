# программа, формирующая адрес электронной почты сотрудников
n = int(input())
employees = [input() for _ in range(n)]
m = int(input())
new_employees = [input() for _ in range(m)]

info = {}
for emp in employees:
    name_emp = emp[:emp.index('@')]
    if name_emp[-1].isdigit():
        if name_emp[:-1] not in info:
            info[name_emp[:-1]] = {int(name_emp[-1]): name_emp}
        else:
            info[name_emp[:-1]].update({int(name_emp[-1]): name_emp})
    else:
        if name_emp not in info:
            info[name_emp] = {0: name_emp}
        else:
            info[name_emp].update({0: name_emp})

mail_for_new = []
for new in new_employees:
    if new not in info:
        info[new] = {0: new}
        mail_for_new.append(new + '@beegeek.bzz')
    else:
        if sorted(info[new].keys()) == [i for i in range(len(info[new]))]:
            info[new].update({len(info[new]): new + str(len(info[new]))})
            mail_for_new.append(info[new][len(info[new]) - 1] + '@beegeek.bzz')
        else:
            new_key = [i for i in range(len(info[new])) if i not in info[new].keys()]
            info[new].update({new_key[0]: new + str(new_key[0])})
            if new_key[0] != 0:
                mail_for_new.append(info[new][new_key[0]] + '@beegeek.bzz')
            else:
                mail_for_new.append(new + '@beegeek.bzz')

print(*mail_for_new, sep='\n')
