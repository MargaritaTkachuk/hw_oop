from math import isclose
from a import generate_sequence_a, get_element_a
from b import compute_product_b
from c import compute_determinant_c
from d import compute_sum_d
from e import taylor_ln_series, compare_with_math_ln

print("Завдання a:")
x = 2
k = 3
print(f"x = {x}, k = {k}")
print(f"x_k = {get_element_a(x, k):.5f}")
print("Перші 5 членів послідовності:")
gen_a = generate_sequence_a(x)
for i in range(5):
    print(f"x_{i} = {next(gen_a):.5f}")
print()


print("Завдання b:")
n = 5
print(f"P_{n} = {compute_product_b(n):.5f}")
print()


print("Завдання c:")
n = 4
a = 2
b = 3
print(f"determinant = {compute_determinant_c(n, a, b)}")
print()


print("Завдання d:")
n = 10
print(f"S_{n} = {compute_sum_d(n):.5f}")
print()


print("Завдання e:")
x = 0.5
eps = 1e-6
taylor_result, math_result = compare_with_math_ln(x, eps)
print(f"x = {x}, ε = {eps}")
print(f"Taylor result: {taylor_result:.6f}")
print(f"math.log result: {math_result:.6f}")
print(f"Різниця: {abs(taylor_result - math_result):.2e}")
print(f"Збігається з math.log: {isclose(taylor_result, math_result, rel_tol=1e-5)}")
