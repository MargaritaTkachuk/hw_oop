def generate_sequence_b():
    n = 1
    product = 1
    while True:
        product *= (1 + 1 / (n**2))
        yield product
        n += 1

def compute_product_b(n):
    product = 1
    for i in range(1, n + 1):
        product *= (1 + 1 / (i**2))
    return product
