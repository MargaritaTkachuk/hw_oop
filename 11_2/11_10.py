def limited(n):
    a0 = 2.5
    yield a0
    for k in range(1, n):
        a0 = 2 + (1 / (a0 + 4 - (1 / ((2 * k - 1) * (2 * k + 1)))))
        yield a0

def infinite():
    a0 = 2.5
    k = 1
    yield a0
    while True:
        a0 = 2 + (1 / (a0 + 4 - (1 / ((2 * k - 1) * (2 * k + 1)))))
        yield a0
        k += 1

#################### головна програма ####################
if __name__ == "__main__":
    n = int(input("Введіть n: "))

    print("Обмежений генератор:")
    for val in limited(n):
        print(val)
    print("Нескінченний генератор (перші 10):")
    gen = infinite()
    for _ in range(10):
        print(next(gen))