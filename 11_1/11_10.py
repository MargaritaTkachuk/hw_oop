n = int(input())
a0 = 2.5
print(a0)
for k in range(1, n):
    a0 = 2 + (1 / (a0 + 4 - (1 / ((2 * k - 1) * (2 * k + 1)))))
    print(a0)