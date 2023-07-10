# функция, возвращающая строку с указанием информации о количестве лайкнувших запись
def likes(names):
    x, y, z = '', '', ''
    if len(names) < 4:
        if len(names) == 1:
            x = names[0]
        elif len(names) == 2:
            x, y = names[0], names[1]
        elif len(names) == 3:
            x, y, z = names[0], names[1], names[2]
        info = {0: 'Никто не оценил данную запись',
                1: f'{x} оценил(а) данную запись',
                2: f'{x} и {y} оценили данную запись',
                3: f'{x}, {y} и {z} оценили данную запись'}
        return info[len(names)]
    else:
        return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'


print(likes(['Артур', 'Тимур', 'Руслан', 'Анри', 'Дима', 'Алиса']))
