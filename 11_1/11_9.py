from math import factorial

#################### task a ####################
n = int(input())
p2 = 0.75
for k in range(3, n + 2):
    p2 = p2 * (1 - 1 / k ** 2)
print(p2)

#################### task b ####################
n = int(input())
p1 = 3
for k in range(2, n + 1):
    p1 = p1 * (2 + 1 / factorial(k))
print(p1)

#################### task c ####################
n = int(input())
p1 = 2/3
for k in range(2, n + 1):
    p1 = p1 * ((k + 1) / (k + 2))
print(p1)

