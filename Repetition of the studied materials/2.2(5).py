# программа, формирующая группы чисел по сумме их цифр и выводящая количество элементов самой большой группы
from functools import reduce
n = int(input())
numbers = [i for i in range(1, n+1)]
sum_nums = {}
for num in numbers:
    sum_n = reduce(lambda x, y: int(x)+int(y), str(num))
    sum_nums[int(sum_n)] = sum_nums.get(int(sum_n), []) + [num]

print(len(max(sum_nums.values(), key=len)))
