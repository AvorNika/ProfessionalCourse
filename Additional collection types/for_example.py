A, B, C, D = [int(i) for i in input().split()]
if D <= B:
    print(A)
else:
    print((D - B) * C + A)