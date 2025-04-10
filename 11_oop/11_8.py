#################### task a ####################
n = int(input())
s1 = 1
for k in range(2, n + 1):
    s1 = s1 + (-1)**(k + 1) * k
print(s1)

#################### task b ####################
n = int(input())
s2 = 0.5
for k in range(3, n + 2):
    s2 = s2 + (1 / ((k -1) * k))
print(s2)

#################### task c ####################
n = int(input())
s2 = 0.5
for k in range(3, n + 2):
    s2 = s2 + ((-1)**k * (k - 1) / k)
print(s2)