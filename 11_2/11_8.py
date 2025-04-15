#################### task a ####################
def sum_sequence_a_limited(n):
    s = 1
    yield s
    for k in range(2, n + 1):
        s += (-1)**(k + 1) * k
        yield s

def sum_sequence_a_infinite():
    s = 1
    k = 2
    yield s
    while True:
        s += (-1)**(k + 1) * k
        yield s
        k += 1

#################### task b ####################
def sum_sequence_b_limited(n):
    s = 0.5
    yield s
    for k in range(3, n + 2):
        s += 1 / ((k - 1) * k)
        yield s

def sum_sequence_b_infinite():
    s = 0.5
    k = 3
    yield s
    while True:
        s += 1 / ((k - 1) * k)
        yield s
        k += 1

#################### task c ####################
def sum_sequence_c_limited(n):
    s = 0.5
    yield s
    for k in range(3, n + 2):
        s += (-1)**k * (k - 1) / k
        yield s

def sum_sequence_c_infinite():
    s = 0.5
    k = 3
    yield s
    while True:
        s += (-1)**k * (k - 1) / k
        yield s
        k += 1

#################### головна програма ####################
if __name__ == "__main__":
    n = int(input("Введіть n: "))

    print("\n#################### task a ####################")
    print("Обмежений генератор:")
    for val in sum_sequence_a_limited(n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = sum_sequence_a_infinite()
    for _ in range(10):
        print(next(gen))

    print("\n#################### task b ####################")
    print("Обмежений генератор:")
    for val in sum_sequence_b_limited(n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = sum_sequence_b_infinite()
    for _ in range(10):
        print(next(gen))

    print("\n#################### task c ####################")
    print("Обмежений генератор:")
    for val in sum_sequence_c_limited(n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = sum_sequence_c_infinite()
    for _ in range(10):
        print(next(gen))
