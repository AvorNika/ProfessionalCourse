# программа, выводящая повторяющиеся числа из последовательности чисел
numbers = [int(i) for i in input().split()]
result = []
numbers.sort()
for i in range(len(numbers)-1):
    if numbers[i+1] == numbers[i] and numbers[i+1] not in result:
        result.append(numbers[i+1])

print(*result)
