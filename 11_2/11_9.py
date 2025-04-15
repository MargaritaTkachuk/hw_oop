from math import factorial

#################### task a ####################
def product_sequence_a_limited(n):
    p = 0.75
    yield p
    for k in range(3, n + 2):
        p *= (1 - 1 / k**2)
        yield p

def product_sequence_a_infinite():
    p = 0.75
    k = 3
    yield p
    while True:
        p *= (1 - 1 / k**2)
        yield p
        k += 1

#################### task b ####################
def product_sequence_b_limited(n):
    p = 3
    yield p
    for k in range(2, n + 1):
        p *= (2 + 1 / factorial(k))
        yield p

def product_sequence_b_infinite():
    p = 3
    k = 2
    yield p
    while True:
        p *= (2 + 1 / factorial(k))
        yield p
        k += 1

#################### task c ####################
def product_sequence_c_limited(n):
    p = 2 / 3
    yield p
    for k in range(2, n + 1):
        p *= (k + 1) / (k + 2)
        yield p

def product_sequence_c_infinite():
    p = 2 / 3
    k = 2
    yield p
    while True:
        p *= (k + 1) / (k + 2)
        yield p
        k += 1

#################### головна програма ####################
if __name__ == "__main__":
    n = int(input("Введіть n: "))

    print("\n#################### task a ####################")
    print("Обмежений генератор:")
    for val in product_sequence_a_limited(n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = product_sequence_a_infinite()
    for _ in range(10):
        print(next(gen))

    print("\n#################### task b ####################")
    print("Обмежений генератор:")
    for val in product_sequence_b_limited(n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = product_sequence_b_infinite()
    for _ in range(10):
        print(next(gen))

    print("\n#################### task c ####################")
    print("Обмежений генератор:")
    for val in product_sequence_c_limited(n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = product_sequence_c_infinite()
    for _ in range(10):
        print(next(gen))
