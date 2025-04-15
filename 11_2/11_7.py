from math import factorial

#################### task a ####################
def sequence_a_limited(x, n):
    x0 = x
    yield x0
    for k in range(1, n):
        x0 = x0 * (x**2 / (4 * k**2 + 2 * k))
        yield x0

def sequence_a_infinite(x):
    x0 = x
    k = 1
    yield x0
    while True:
        x0 = x0 * (x**2 / (4 * k**2 + 2 * k))
        yield x0
        k += 1

#################### task b ####################
def sequence_b_limited(x, n):
    x1 = -x
    yield x1
    for k in range(2, n + 1):
        x1 = x1 * (x * (1 - k) / k)
        yield x1

def sequence_b_infinite(x):
    x1 = -x
    k = 2
    yield x1
    while True:
        x1 = x1 * (x * (1 - k) / k)
        yield x1
        k += 1

#################### task c ####################
def sequence_c_limited(x, n):
    x0 = 1
    yield x0
    for k in range(1, n):
        x0 *= - x * factorial(k**2 - k) / factorial(k**2 + k)
        yield x0

def sequence_c_infinite(x):
    x0 = 1
    k = 1
    yield x0
    while True:
        x0 *= - x * factorial(k**2 - k) / factorial(k**2 + k)
        yield x0
        k += 1

#################### task d ####################
def sequence_d_limited(x, n):
    x0 = 1
    yield x0
    for k in range(1, n):
        x0 = x0 * (x * (k + 1) / k**2)
        yield x0

def sequence_d_infinite(x):
    x0 = 1
    k = 1
    yield x0
    while True:
        x0 = x0 * (x * (k + 1) / k**2)
        yield x0
        k += 1

#################### головна програма ####################
if __name__ == "__main__":
    x = int(input("Введіть x: "))
    n = int(input("Введіть n: "))

    print("\n#################### task a ####################")
    print("Обмежений генератор:")
    for val in sequence_a_limited(x, n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = sequence_a_infinite(x)
    for _ in range(10):
        print(next(gen))

    print("\n#################### task b ####################")
    print("Обмежений генератор:")
    for val in sequence_b_limited(x, n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = sequence_b_infinite(x)
    for _ in range(10):
        print(next(gen))

    print("\n#################### task c ####################")
    print("Обмежений генератор:")
    for val in sequence_c_limited(x, n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = sequence_c_infinite(x)
    for _ in range(10):
        print(next(gen))

    print("\n#################### task d ####################")
    print("Обмежений генератор:")
    for val in sequence_d_limited(x, n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = sequence_d_infinite(x)
    for _ in range(10):
        print(next(gen))
