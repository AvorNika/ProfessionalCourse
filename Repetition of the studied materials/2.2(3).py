# программа, переворачивающая элементы последовательности
n, X, Y, A, B = [int(i) for i in input().split()]
seq = [i for i in range(1, n+1)]
med_seq = seq[:X-1] + seq[X-1:Y][::-1] + seq[Y:]
result_seq = med_seq[:A-1] + med_seq[A-1:B][::-1] + med_seq[B:]

print(*result_seq)
