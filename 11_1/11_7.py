from math import factorial

#################### task a ####################
x = int(input())
n = int(input())
x0 = x
print(x0)
for k in range(1, n):
    x0 = x0 * (x**2 / (4 * k**2 + 2 * k))
    print(x0)

#################### task b ####################
x = int(input())
n = int(input())
x1 = - x
print(x1)
for k in range(2, n + 1):
    x1 = x1 * (x * (1 - k) /  k)
    print(x1)

#################### task c ####################
x = int(input())
n = int(input())
x0 = 1
print(x0)
for k in range(1, n):
    x0 *= - x * factorial(k**2 - k) / factorial(k**2 + k)
    print(x0)


#################### task d ####################
x = int(input())
n = int(input())
x0 = 1
print(x0)
for k in range(1, n):
    x0 = x0 * (x * (k + 1) /  k**2)
    print(x0)
