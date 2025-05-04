from math import log

def taylor_ln_series(x, epsilon):
    if abs(x) >= 1:
        raise ValueError("x must be in (-1, 1)")
    term = x
    result = 0
    k = 1
    while abs(term) > epsilon:
        result += term
        k += 2
        term = x**k / k
    return 2 * result

def compare_with_math_ln(x, epsilon):
    taylor_result = taylor_ln_series(x, epsilon)
    math_result = log((1 + x) / (1 - x))
    return taylor_result, math_result
