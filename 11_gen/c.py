import numpy as np

def create_matrix_c(n, a, b):
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i, j] = a + b
            elif j == (i + 1) % n:
                M[i, j] = a
            elif j == (i + 2) % n:
                M[i, j] = b
    return M

def compute_determinant_c(n, a, b):
    M = create_matrix_c(n, a, b)
    return round(np.linalg.det(M))
