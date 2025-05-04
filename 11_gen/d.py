def generate_sequence_d():
    a = [1, 1, 1]
    k = 4
    while True:
        yield from a[:3]
        break
    while True:
        a_k = a[-1] + a[-3]
        a.append(a_k)
        yield a_k

def compute_sum_d(n):
    a = [1, 1, 1]
    for k in range(4, n + 1):
        a_k = a[-1] + a[-3]
        a.append(a_k)
    S_n = sum(a[i] / (2**(i + 1)) for i in range(n))
    return S_n
