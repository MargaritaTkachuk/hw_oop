def generate_sequence_a(x):
    k = 0
    current = 1  # x_0
    while True:
        yield current
        k += 1
        current *= (x**2) / (2 * k * (2 * k - 1))

def get_element_a(x, k):
    current = 1
    for i in range(1, k + 1):
        current *= (x**2) / (2 * i * (2 * i - 1))
    return current

